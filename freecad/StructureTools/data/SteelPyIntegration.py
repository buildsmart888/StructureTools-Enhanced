# -*- coding: utf-8 -*-
"""
SteelPy Integration for StructureTools
การเชื่อมต่อกับ steelpy database สำหรับข้อมูลเหล็ก
"""

import sys
import json
import os
from pathlib import Path

# Safe steelpy import
try:
    import steelpy
    from steelpy import aisc
    STEELPY_AVAILABLE = True
    print("[INFO] steelpy library loaded successfully")
except ImportError:
    STEELPY_AVAILABLE = False
    print("[WARNING] steelpy library not available")
    print("Install with: pip install steelpy")

class SteelPyDatabaseManager:
    """Manager for steelpy database operations"""
    
    def __init__(self):
        self.available = STEELPY_AVAILABLE
        self.cache_file = Path(__file__).parent / "steelpy_cache.json"
        self.section_cache = {}
        
        if self.available:
            self.initialize_database()
    
    def initialize_database(self):
        """Initialize steelpy database and create cache"""
        try:
            # Load cached data if available
            if self.cache_file.exists():
                self.load_cache()
            else:
                self.build_cache()
        except Exception as e:
            print(f"[ERROR] Failed to initialize steelpy database: {e}")
            self.available = False
    
    def build_cache(self):
        """Build complete cache of all steelpy sections"""
        if not self.available:
            return
        
        print("[INFO] Building steelpy section cache...")
        
        # Define all shape collections with their details
        shape_collections = {
            'W_shapes': {
                'name': 'Wide Flange Beams',
                'description': 'Wide flange structural steel beams (W-shapes)',
                'collection': aisc.W_shapes,
                'type': 'beam'
            },
            'M_shapes': {
                'name': 'M Shapes',
                'description': 'Miscellaneous steel shapes (M-shapes)',
                'collection': aisc.M_shapes,
                'type': 'beam'
            },
            'S_shapes': {
                'name': 'Standard I-Beams',
                'description': 'Standard I-beam shapes (S-shapes)',
                'collection': aisc.S_shapes,
                'type': 'beam'
            },
            'HP_shapes': {
                'name': 'HP Shapes',
                'description': 'HP bearing pile shapes',
                'collection': aisc.HP_shapes,
                'type': 'pile'
            },
            'WT_shapes': {
                'name': 'WT Shapes',
                'description': 'Structural tees cut from W-shapes',
                'collection': aisc.WT_shapes,
                'type': 'tee'
            },
            'MT_shapes': {
                'name': 'MT Shapes',
                'description': 'Structural tees cut from M-shapes',
                'collection': aisc.MT_shapes,
                'type': 'tee'
            },
            'ST_shapes': {
                'name': 'ST Shapes',
                'description': 'Structural tees cut from S-shapes',
                'collection': aisc.ST_shapes,
                'type': 'tee'
            },
            'Pipe': {
                'name': 'Pipe',
                'description': 'Standard steel pipe',
                'collection': aisc.Pipe,
                'type': 'circular'
            },
            'HSS_round': {
                'name': 'HSS Round',
                'description': 'Round hollow structural sections',
                'collection': aisc.HSS_round,
                'type': 'circular'
            },
            'HSS_rect': {
                'name': 'HSS Rectangular',
                'description': 'Rectangular hollow structural sections',
                'collection': aisc.HSS_rect,
                'type': 'rectangular'
            },
            'L_shapes': {
                'name': 'Angles',
                'description': 'Equal and unequal leg angles',
                'collection': aisc.L_shapes,
                'type': 'angle'
            },
            'Double_L': {
                'name': 'Double Angles',
                'description': 'Double angle sections',
                'collection': aisc.Double_L,
                'type': 'double_angle'
            }
        }
        
        self.section_cache = {
            'metadata': {
                'version': '1.0',
                'source': 'steelpy',
                'standard': 'AISC',
                'units': 'imperial_to_metric',
                'sections_count': 0
            },
            'shape_types': {},
            'sections': {}
        }
        
        total_sections = 0
        
        # Process each shape collection
        for shape_key, shape_info in shape_collections.items():
            try:
                collection = shape_info['collection']
                sections_list = []
                sections_data = {}
                
                # Get all section names from collection
                for attr_name in dir(collection):
                    if not attr_name.startswith('_'):
                        try:
                            section = getattr(collection, attr_name)
                            
                            # Extract properties
                            properties = self.extract_section_properties(section, shape_key, attr_name)
                            
                            if properties:
                                sections_list.append(attr_name)
                                sections_data[attr_name] = properties
                                total_sections += 1
                                
                        except Exception as e:
                            print(f"[WARNING] Failed to process section {attr_name}: {e}")
                
                # Store in cache
                self.section_cache['shape_types'][shape_key] = {
                    'name': shape_info['name'],
                    'description': shape_info['description'],
                    'type': shape_info['type'],
                    'sections': sorted(sections_list),
                    'count': len(sections_list)
                }
                
                self.section_cache['sections'][shape_key] = sections_data
                
                print(f"[INFO] Cached {len(sections_list)} sections for {shape_info['name']}")
                
            except Exception as e:
                print(f"[WARNING] Failed to process shape type {shape_key}: {e}")
        
        self.section_cache['metadata']['sections_count'] = total_sections
        
        # Save cache to file
        self.save_cache()
        
        print(f"[INFO] steelpy cache built successfully: {total_sections} sections total")
    
    def extract_section_properties(self, section, shape_type, section_name):
        """Extract and convert section properties from steelpy object"""
        try:
            properties = {
                'name': section_name,
                'shape_type': shape_type,
                'standard': 'AISC',
                'source': 'steelpy'
            }
            
            # Imperial to metric conversion factors
            AREA_CONV = 645.16        # in² to mm²
            LENGTH_CONV = 25.4        # in to mm
            MOMENT_CONV = 416231.43   # in⁴ to mm⁴
            MODULUS_CONV = 16387.06   # in³ to mm³
            WEIGHT_CONV = 1.488       # lb/ft to kg/m
            
            # Basic properties
            if hasattr(section, 'A'):
                properties['area'] = round(section.A * AREA_CONV, 2)  # mm²
                
            if hasattr(section, 'W'):
                properties['weight'] = round(section.W * WEIGHT_CONV, 2)  # kg/m
            
            # Dimensions
            if hasattr(section, 'd'):
                properties['height'] = round(section.d * LENGTH_CONV, 2)  # mm
                properties['d'] = properties['height']
                
            if hasattr(section, 'bf'):
                properties['width'] = round(section.bf * LENGTH_CONV, 2)  # mm
                properties['bf'] = properties['width']
                
            if hasattr(section, 'tw'):
                properties['web_thickness'] = round(section.tw * LENGTH_CONV, 2)  # mm
                properties['tw'] = properties['web_thickness']
                
            if hasattr(section, 'tf'):
                properties['flange_thickness'] = round(section.tf * LENGTH_CONV, 2)  # mm
                properties['tf'] = properties['flange_thickness']
            
            # For HSS sections
            if hasattr(section, 't'):
                properties['thickness'] = round(section.t * LENGTH_CONV, 2)  # mm
                
            if hasattr(section, 'H'):
                properties['height'] = round(section.H * LENGTH_CONV, 2)  # mm
                
            if hasattr(section, 'B'):
                properties['width'] = round(section.B * LENGTH_CONV, 2)  # mm
            
            # For circular sections
            if hasattr(section, 'OD'):
                properties['outer_diameter'] = round(section.OD * LENGTH_CONV, 2)  # mm
                properties['diameter'] = properties['outer_diameter']
                
            if hasattr(section, 'ID'):
                properties['inner_diameter'] = round(section.ID * LENGTH_CONV, 2)  # mm
            
            # For angles
            if hasattr(section, 'd1'):
                properties['leg1'] = round(section.d1 * LENGTH_CONV, 2)  # mm
                
            if hasattr(section, 'd2'):
                properties['leg2'] = round(section.d2 * LENGTH_CONV, 2)  # mm
                
            if hasattr(section, 't'):
                properties['thickness'] = round(section.t * LENGTH_CONV, 2)  # mm
            
            # Moment of inertia
            if hasattr(section, 'Ix'):
                properties['ix'] = round(section.Ix * MOMENT_CONV, 0)  # mm⁴
                properties['moment_inertia_y'] = properties['ix']  # Major axis
                
            if hasattr(section, 'Iy'):
                properties['iy'] = round(section.Iy * MOMENT_CONV, 0)  # mm⁴
                properties['moment_inertia_z'] = properties['iy']  # Minor axis
            
            # Section moduli
            if hasattr(section, 'Sx'):
                properties['sx'] = round(section.Sx * MODULUS_CONV, 0)  # mm³
                properties['section_modulus_y'] = properties['sx']
                
            if hasattr(section, 'Sy'):
                properties['sy'] = round(section.Sy * MODULUS_CONV, 0)  # mm³
                properties['section_modulus_z'] = properties['sy']
            
            # Plastic section moduli
            if hasattr(section, 'Zx'):
                properties['zx'] = round(section.Zx * MODULUS_CONV, 0)  # mm³
                properties['plastic_modulus_y'] = properties['zx']
                
            if hasattr(section, 'Zy'):
                properties['zy'] = round(section.Zy * MODULUS_CONV, 0)  # mm³
                properties['plastic_modulus_z'] = properties['zy']
            
            # Radii of gyration
            if hasattr(section, 'rx'):
                properties['rx'] = round(section.rx * LENGTH_CONV, 2)  # mm
                properties['radius_gyration_y'] = properties['rx']
                
            if hasattr(section, 'ry'):
                properties['ry'] = round(section.ry * LENGTH_CONV, 2)  # mm
                properties['radius_gyration_z'] = properties['ry']
            
            # Torsional properties
            if hasattr(section, 'J'):
                properties['j'] = round(section.J * MOMENT_CONV, 0)  # mm⁴
                properties['torsional_constant'] = properties['j']
            
            # Warping constant
            if hasattr(section, 'Cw'):
                properties['cw'] = round(section.Cw * MOMENT_CONV * LENGTH_CONV * LENGTH_CONV, 0)  # mm⁶
                properties['warping_constant'] = properties['cw']
            
            return properties
            
        except Exception as e:
            print(f"[WARNING] Failed to extract properties for {section_name}: {e}")
            return None
    
    def save_cache(self):
        """Save cache to JSON file"""
        try:
            with open(self.cache_file, 'w') as f:
                json.dump(self.section_cache, f, indent=2)
            print(f"[INFO] Cache saved to {self.cache_file}")
        except Exception as e:
            print(f"[ERROR] Failed to save cache: {e}")
    
    def load_cache(self):
        """Load cache from JSON file"""
        try:
            with open(self.cache_file, 'r') as f:
                self.section_cache = json.load(f)
            
            sections_count = self.section_cache['metadata']['sections_count']
            print(f"[INFO] steelpy cache loaded: {sections_count} sections available")
            
        except Exception as e:
            print(f"[ERROR] Failed to load cache: {e}")
            self.build_cache()
    
    def get_shape_types(self):
        """Get available shape types"""
        if not self.available or not self.section_cache:
            return {}
        
        return self.section_cache.get('shape_types', {})
    
    def get_sections_list(self, shape_type):
        """Get list of sections for a shape type"""
        if not self.available or not self.section_cache:
            return []
        
        shape_info = self.section_cache.get('shape_types', {}).get(shape_type, {})
        return shape_info.get('sections', [])
    
    def get_section_properties(self, shape_type, section_name):
        """Get properties for a specific section"""
        if not self.available or not self.section_cache:
            return None
        
        sections_data = self.section_cache.get('sections', {}).get(shape_type, {})
        return sections_data.get(section_name)
    
    def search_sections(self, query, shape_type=None):
        """Search sections by name or properties"""
        if not self.available or not self.section_cache:
            return []
        
        results = []
        query_lower = query.lower()
        
        shape_types_to_search = [shape_type] if shape_type else self.section_cache.get('shape_types', {}).keys()
        
        for st in shape_types_to_search:
            sections = self.section_cache.get('sections', {}).get(st, {})
            for section_name, properties in sections.items():
                if query_lower in section_name.lower():
                    results.append({
                        'name': section_name,
                        'shape_type': st,
                        'shape_name': self.section_cache['shape_types'][st]['name'],
                        'properties': properties
                    })
        
        return results
    
    def filter_sections(self, filters, shape_type=None):
        """Filter sections by property criteria"""
        if not self.available or not self.section_cache:
            return []
        
        results = []
        shape_types_to_filter = [shape_type] if shape_type else self.section_cache.get('shape_types', {}).keys()
        
        for st in shape_types_to_filter:
            sections = self.section_cache.get('sections', {}).get(st, {})
            
            for section_name, properties in sections.items():
                matches = True
                
                for prop_name, criteria in filters.items():
                    if prop_name not in properties:
                        matches = False
                        break
                    
                    value = properties[prop_name]
                    
                    if isinstance(criteria, dict):
                        if 'min' in criteria and value < criteria['min']:
                            matches = False
                            break
                        if 'max' in criteria and value > criteria['max']:
                            matches = False
                            break
                    elif value != criteria:
                        matches = False
                        break
                
                if matches:
                    results.append({
                        'name': section_name,
                        'shape_type': st,
                        'shape_name': self.section_cache['shape_types'][st]['name'],
                        'properties': properties
                    })
        
        return results
    
    def get_statistics(self):
        """Get database statistics"""
        if not self.available or not self.section_cache:
            return {}
        
        stats = {
            'total_sections': self.section_cache['metadata']['sections_count'],
            'shape_types': len(self.section_cache.get('shape_types', {})),
            'by_type': {}
        }
        
        for shape_type, info in self.section_cache.get('shape_types', {}).items():
            stats['by_type'][shape_type] = {
                'name': info['name'],
                'count': info['count']
            }
        
        return stats

# Global instance
steelpy_manager = SteelPyDatabaseManager()

def get_steelpy_manager():
    """Get global steelpy manager instance"""
    return steelpy_manager

# Convenience functions
def get_available_shape_types():
    """Get available shape types"""
    return steelpy_manager.get_shape_types()

def get_sections_for_shape(shape_type):
    """Get sections for a shape type"""
    return steelpy_manager.get_sections_list(shape_type)

def get_section_data(shape_type, section_name):
    """Get section properties"""
    return steelpy_manager.get_section_properties(shape_type, section_name)

def search_steel_sections(query, shape_type=None):
    """Search steel sections"""
    return steelpy_manager.search_sections(query, shape_type)

def filter_steel_sections(filters, shape_type=None):
    """Filter steel sections"""
    return steelpy_manager.filter_sections(filters, shape_type)

# Export main classes and functions
__all__ = [
    'SteelPyDatabaseManager',
    'steelpy_manager',
    'get_steelpy_manager',
    'get_available_shape_types',
    'get_sections_for_shape',
    'get_section_data',
    'search_steel_sections',
    'filter_steel_sections',
    'STEELPY_AVAILABLE'
]