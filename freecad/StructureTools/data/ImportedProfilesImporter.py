"""ImportedProfilesImporter

Convert a simple profiles JSON (as produced by scripts/import_steelpy_shapes.py)
into the EnhancedSteelDatabase in-memory schema and save to cache.

The expected input JSON format is:
  { "profiles": [ { "id": "name", "name": "...", "type": "steel", "properties": {...}, "points": [[x,y], ...] }, ... ] }

This module provides import_profiles_json(file_path, db_instance) -> bool
which merges the profiles into db_instance and saves the cache.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Any
from freecad.StructureTools.data.ProfileGeometryGenerator import generate_geometry_from_properties


def import_profiles_json(file_path: str, db_instance) -> bool:
    """Load the profiles JSON and merge into the given EnhancedSteelDatabase instance.

    Returns True on success, False otherwise.
    """
    p = Path(file_path)
    if not p.exists():
        print(f"[ERROR] Import file not found: {file_path}")
        return False

    try:
        with p.open('r', encoding='utf-8') as f:
            data = json.load(f)

        profiles = data.get('profiles') or data.get('items') or []
        if not profiles:
            print(f"[ERROR] No profiles found in {file_path}")
            return False

        # Prepare shape_type key for imported profiles
        shape_key = 'IMPORTED'
        shape_name = 'Imported Profiles'

        sections = {}
        geometries = {}

        # Helper: map incoming property names to enhanced keys
        prop_map = {
            'A': 'area', 'area': 'area',
            'Ix': 'moment_inertia_x', 'ix': 'moment_inertia_x',
            'Iy': 'moment_inertia_y', 'iy': 'moment_inertia_y',
            'J': 'torsional_constant', 'j': 'torsional_constant',
            'Sx': 'section_modulus_x', 'sx': 'section_modulus_x',
            'Sy': 'section_modulus_y', 'sy': 'section_modulus_y',
            'Zx': 'plastic_modulus_x', 'zx': 'plastic_modulus_x',
            'Zy': 'plastic_modulus_y', 'zy': 'plastic_modulus_y',
            'd': 'height', 'H': 'height',
            'bf': 'width', 'B': 'width',
            'tf': 'flange_thickness', 'tw': 'web_thickness', 't': 'thickness'
        }

        # Small heuristic to auto-detect units (inches vs mm)
        sample_areas = []
        for prof in profiles[:10]:
            props = prof.get('properties') or {}
            for k in ('A', 'area'):
                if k in props:
                    try:
                        sample_areas.append(float(props[k]))
                    except Exception:
                        pass
        detected_unit = 'in' if (sample_areas and sum(sample_areas)/len(sample_areas) < 1000) else 'mm'

        # Conversion factors (from imperial to metric)
        AREA_CONV = 645.16        # in^2 to mm^2
        LENGTH_CONV = 25.4        # in to mm
        MOMENT_CONV = 416231.43   # in^4 to mm^4
        MODULUS_CONV = 16387.06   # in^3 to mm^3

        for prof in profiles:
            pid = str(prof.get('id') or prof.get('name') or '')
            if not pid:
                continue

            raw_props = prof.get('properties', {}) or {}
            raw_points = prof.get('points') or prof.get('drawing_points') or []

            mapped_props = {}
            for k, v in raw_props.items():
                key = prop_map.get(k) or prop_map.get(k.lower())
                try:
                    val = float(v)
                except Exception:
                    mapped_props[k] = v
                    continue

                if detected_unit == 'in':
                    if key == 'area':
                        conv_val = round(val * AREA_CONV, 2)
                        mapped_props[key] = {'value': conv_val, 'unit': 'mm²', 'original': val}
                    elif key in ('moment_inertia_x', 'moment_inertia_y', 'torsional_constant'):
                        conv_val = round(val * MOMENT_CONV, 2)
                        mapped_props[key] = {'value': conv_val, 'unit': 'mm⁴', 'original': val}
                    elif key in ('section_modulus_x', 'section_modulus_y', 'plastic_modulus_x', 'plastic_modulus_y'):
                        conv_val = round(val * MODULUS_CONV, 2)
                        mapped_props[key] = {'value': conv_val, 'unit': 'mm³', 'original': val}
                    elif key in ('height', 'width', 'flange_thickness', 'web_thickness', 'thickness'):
                        conv_val = round(val * LENGTH_CONV, 2)
                        mapped_props[key] = {'value': conv_val, 'unit': 'mm', 'original': val}
                    else:
                        mapped_props[key or k] = val
                else:
                    if key == 'area':
                        mapped_props[key] = {'value': round(val, 2), 'unit': 'mm²', 'original': val}
                    elif key in ('moment_inertia_x', 'moment_inertia_y', 'torsional_constant'):
                        mapped_props[key] = {'value': round(val, 2), 'unit': 'mm⁴', 'original': val}
                    elif key in ('section_modulus_x', 'section_modulus_y', 'plastic_modulus_x', 'plastic_modulus_y'):
                        mapped_props[key] = {'value': round(val, 2), 'unit': 'mm³', 'original': val}
                    elif key in ('height', 'width', 'flange_thickness', 'web_thickness', 'thickness'):
                        mapped_props[key] = {'value': round(val, 2), 'unit': 'mm', 'original': val}
                    else:
                        mapped_props[key or k] = val

            drawing = None
            if raw_points:
                pts = []
                for pt in raw_points:
                    try:
                        x = float(pt[0])
                        y = float(pt[1])
                        if detected_unit == 'in':
                            x = round(x * LENGTH_CONV, 3)
                            y = round(y * LENGTH_CONV, 3)
                        pts.append([x, y])
                    except Exception:
                        continue
                if pts:
                    drawing = pts
            else:
                # No raw points: try to synthesize geometry from numeric properties
                try:
                    synth = generate_geometry_from_properties(raw_props, pid)
                    if synth:
                        # The generator returns either type/keys and possibly drawing_points
                        drawing = synth.get('drawing_points')
                        # Merge top-level numeric keys into mapped_props so drawing functions can use them
                        for k in ('height', 'width', 'flange_thickness', 'web_thickness', 'thickness', 'leg1', 'leg2', 'outer_diameter', 'inner_diameter'):
                            if k in synth and k not in mapped_props:
                                mapped_props[k] = synth[k]
                        # Also include type so drawer picks geometry correctly
                        if 'type' in synth:
                            mapped_props['beam_type'] = synth['type']
                except Exception:
                    pass

            sections[pid] = mapped_props

            # Normalize geometry payload for SectionDrawing
            if drawing:
                # Determine beam_type: prefer mapped_props['beam_type'] from synth; fallback to POLYLINE
                beam_type = mapped_props.get('beam_type') or 'POLYLINE'
                geometries[pid] = {
                    'beam_type': beam_type,
                    'drawing_points': drawing
                }
            else:
                # No explicit drawing points; attempt to create a typed geometry payload
                # Detect circular sections by presence of outer/inner diameter
                if 'outer_diameter' in mapped_props or 'inner_diameter' in mapped_props:
                    od = mapped_props.get('outer_diameter')
                    id_ = mapped_props.get('inner_diameter')
                    geometries[pid] = {
                        'beam_type': 'CIRCULAR',
                        'outer_diameter': od,
                        'inner_diameter': id_
                    }
                else:
                    # No drawing available; leave out geometry (drawer will handle absence)
                    pass

        if not hasattr(db_instance, 'sections_database') or not isinstance(db_instance.sections_database, dict):
            db_instance.sections_database = {'metadata': {}, 'shape_types': {}, 'sections': {}, 'geometries': {}}

        db = db_instance.sections_database
        db.setdefault('shape_types', {})

        db['shape_types'][shape_key] = {
            'name': shape_name,
            'description': 'Profiles imported from external JSON',
            'category': 'Imported',
            'geometry_type': 'IMPORTED',
            'standard': 'custom',
            'sections': sorted(list(sections.keys())),
            'count': len(sections)
        }

        db.setdefault('sections', {})
        db.setdefault('geometries', {})
        db['sections'][shape_key] = {**db['sections'].get(shape_key, {}), **sections}
        db['geometries'][shape_key] = {**db['geometries'].get(shape_key, {}), **geometries}

        meta = db.setdefault('metadata', {})
        meta['version'] = meta.get('version', '2.0')
        meta['source'] = meta.get('source', 'imported_profiles')
        meta['standard'] = meta.get('standard', 'custom')
        meta['units'] = meta.get('units', 'mm')

        total_sections = sum(info.get('count', 0) for info in db.get('shape_types', {}).values())
        meta['total_sections'] = total_sections
        meta['total_shapes'] = len(db.get('shape_types', {}))

        try:
            db_instance.available = True
            db_instance.sections_database = db
            if hasattr(db_instance, 'save_to_cache'):
                db_instance.save_to_cache()
            print(f"[OK] Imported {len(sections)} profiles into EnhancedSteelDatabase (shape_type={shape_key})")
            return True
        except Exception as e:
            print(f"[ERROR] Failed to merge imported profiles: {e}")
            return False

    except Exception as e:
        print(f"[ERROR] Import failed: {e}")
        return False
