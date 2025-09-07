# -*- coding: utf-8 -*-
"""
Enhanced Steel Database with Complete Shape Information
ฐานข้อมูลเหล็กที่มีข้อมูลครบถ้วนจาก steelpy shape files
"""

import os
import json
import math
from pathlib import Path

# Safe steelpy import
try:
    import steelpy
    from steelpy import aisc
    STEELPY_AVAILABLE = True
    print("[INFO] steelpy library loaded for Enhanced Database")
except ImportError:
    STEELPY_AVAILABLE = False
    print("[WARNING] steelpy library not available for Enhanced Database")

class EnhancedSteelDatabase:
    """Enhanced database with complete shape information including geometry data"""
    
    def __init__(self):
        self.available = STEELPY_AVAILABLE
        self.database_file = Path(__file__).parent / "enhanced_steel_database.json"
        self.sections_database = {}
        self.shape_geometries = {}
        
        if self.available:
            self.initialize_enhanced_database()
    
    def initialize_enhanced_database(self):
        """Initialize enhanced database with complete information"""
        try:
            # Load from cache if available and recent
            if self.database_file.exists():
                self.load_from_cache()
            else:
                self.build_enhanced_database()
        except Exception as e:
            print(f"[ERROR] Failed to initialize enhanced database: {e}")
            self.available = False
    
    def build_enhanced_database(self):
        """Build complete database with all shape information"""
        print("[INFO] Building enhanced steel database...")
        
        # Define comprehensive shape collections
        shape_definitions = {
            'W_shapes': {
                'name': 'Wide Flange Beams',
                'description': 'Wide flange structural steel beams (W-shapes)',
                'category': 'I-Beams',
                'geometry_type': 'I_BEAM',
                'standard': 'AISC'
            },
            'M_shapes': {
                'name': 'M Shapes',
                'description': 'Miscellaneous steel shapes (M-shapes)',
                'category': 'I-Beams',
                'geometry_type': 'I_BEAM',
                'standard': 'AISC'
            },
            'S_shapes': {
                'name': 'Standard I-Beams',
                'description': 'Standard I-beam shapes (S-shapes)',
                'category': 'I-Beams',
                'geometry_type': 'I_BEAM',
                'standard': 'AISC'
            },
            'HP_shapes': {
                'name': 'HP Shapes',
                'description': 'HP bearing pile shapes',
                'category': 'H-Piles',
                'geometry_type': 'H_PILE',
                'standard': 'AISC'
            },
            'WT_shapes': {
                'name': 'WT Shapes',
                'description': 'Structural tees cut from W-shapes',
                'category': 'Tees',
                'geometry_type': 'TEE',
                'standard': 'AISC'
            },
            'MT_shapes': {
                'name': 'MT Shapes',
                'description': 'Structural tees cut from M-shapes',
                'category': 'Tees',
                'geometry_type': 'TEE',
                'standard': 'AISC'
            },
            'ST_shapes': {
                'name': 'ST Shapes',
                'description': 'Structural tees cut from S-shapes',
                'category': 'Tees',
                'geometry_type': 'TEE',
                'standard': 'AISC'
            },
            'L_shapes': {
                'name': 'Angles',
                'description': 'Equal and unequal leg angles',
                'category': 'Angles',
                'geometry_type': 'ANGLE',
                'standard': 'AISC'
            }
        }
        
        # Try to access additional shapes that might be available
        additional_shapes = {
            'Pipe': {
                'name': 'Steel Pipe',
                'description': 'Standard steel pipe sections',
                'category': 'Circular',
                'geometry_type': 'PIPE',
                'standard': 'AISC'
            },
            'HSS_round': {
                'name': 'HSS Round',
                'description': 'Round hollow structural sections',
                'category': 'Circular',
                'geometry_type': 'HSS_ROUND',
                'standard': 'AISC'
            },
            'HSS_rect': {
                'name': 'HSS Rectangular',
                'description': 'Rectangular hollow structural sections',
                'category': 'Rectangular',
                'geometry_type': 'HSS_RECT',
                'standard': 'AISC'
            },
            'Double_L': {
                'name': 'Double Angles',
                'description': 'Double angle sections',
                'category': 'Angles',
                'geometry_type': 'DOUBLE_ANGLE',
                'standard': 'AISC'
            }
        }
        
        # Merge all shape definitions
        all_shapes = {**shape_definitions, **additional_shapes}
        
        self.sections_database = {
            'metadata': {
                'version': '2.0',
                'source': 'steelpy_enhanced',
                'standard': 'AISC',
                'units': 'metric_converted',
                'build_date': str(Path(__file__).stat().st_mtime),
                'total_sections': 0,
                'total_shapes': 0
            },
            'shape_types': {},
            'sections': {},
            'geometries': {}
        }
        
        total_sections = 0
        
        # Process each shape type
        for shape_key, shape_info in all_shapes.items():
            try:
                if not hasattr(aisc, shape_key):
                    print(f"[SKIP] {shape_key}: Not available in this steelpy version")
                    continue
                
                collection = getattr(aisc, shape_key)
                sections_data = {}
                geometry_data = {}
                
                print(f"[INFO] Processing {shape_info['name']}...")
                
                # Get all sections from collection
                section_names = [attr for attr in dir(collection) if not attr.startswith('_')]
                
                for section_name in section_names:
                    try:
                        section = getattr(collection, section_name)
                        
                        # Extract complete properties
                        properties = self.extract_complete_properties(section, shape_key, section_name, shape_info)
                        
                        # Extract geometry data for drawing
                        geometry = self.extract_geometry_data(section, shape_key, section_name, shape_info)
                        
                        if properties and geometry:
                            sections_data[section_name] = properties
                            geometry_data[section_name] = geometry
                            total_sections += 1
                        
                    except Exception as e:
                        print(f"[WARNING] Failed to process {section_name}: {e}")
                        continue
                
                # Store data if we got any sections
                if sections_data:
                    self.sections_database['shape_types'][shape_key] = {
                        'name': shape_info['name'],
                        'description': shape_info['description'],
                        'category': shape_info['category'],
                        'geometry_type': shape_info['geometry_type'],
                        'standard': shape_info['standard'],
                        'sections': sorted(list(sections_data.keys())),
                        'count': len(sections_data)
                    }
                    
                    self.sections_database['sections'][shape_key] = sections_data
                    self.sections_database['geometries'][shape_key] = geometry_data
                    
                    print(f"[OK] {shape_info['name']}: {len(sections_data)} sections")
                
            except Exception as e:
                print(f"[WARNING] Failed to process shape type {shape_key}: {e}")
                continue
        
        # Update metadata
        self.sections_database['metadata']['total_sections'] = total_sections
        self.sections_database['metadata']['total_shapes'] = len(self.sections_database['shape_types'])
        
        # Save to cache
        self.save_to_cache()
        
        print(f"[OK] Enhanced database built: {total_sections} sections in {len(self.sections_database['shape_types'])} shape types")
    
    def extract_complete_properties(self, section, shape_type, section_name, shape_info):
        """Extract complete section properties with units conversion"""
        try:
            properties = {
                'name': section_name,
                'shape_type': shape_type,
                'shape_category': shape_info['category'],
                'geometry_type': shape_info['geometry_type'],
                'standard': 'AISC',
                'source': 'steelpy_enhanced',
                'units': 'metric'
            }
            
            # Imperial to metric conversion factors
            AREA_CONV = 645.16        # in² to mm²
            LENGTH_CONV = 25.4        # in to mm
            MOMENT_CONV = 416231.43   # in⁴ to mm⁴
            MODULUS_CONV = 16387.06   # in³ to mm³
            WEIGHT_CONV = 1.488       # lb/ft to kg/m
            
            # Basic properties
            property_mappings = [
                ('A', 'area', AREA_CONV, 'mm²'),
                ('W', 'weight', WEIGHT_CONV, 'kg/m'),
                
                # Dimensions
                ('d', 'height', LENGTH_CONV, 'mm'),
                ('bf', 'width', LENGTH_CONV, 'mm'),
                ('tw', 'web_thickness', LENGTH_CONV, 'mm'),
                ('tf', 'flange_thickness', LENGTH_CONV, 'mm'),
                ('t', 'thickness', LENGTH_CONV, 'mm'),
                
                # Alternative dimension names
                ('H', 'height', LENGTH_CONV, 'mm'),
                ('B', 'width', LENGTH_CONV, 'mm'),
                
                # For circular sections
                ('OD', 'outer_diameter', LENGTH_CONV, 'mm'),
                ('ID', 'inner_diameter', LENGTH_CONV, 'mm'),
                
                # For angles
                ('d1', 'leg1_length', LENGTH_CONV, 'mm'),
                ('d2', 'leg2_length', LENGTH_CONV, 'mm'),
                
                # Moment of inertia
                ('Ix', 'moment_inertia_x', MOMENT_CONV, 'mm⁴'),
                ('Iy', 'moment_inertia_y', MOMENT_CONV, 'mm⁴'),
                
                # Section moduli
                ('Sx', 'section_modulus_x', MODULUS_CONV, 'mm³'),
                ('Sy', 'section_modulus_y', MODULUS_CONV, 'mm³'),
                
                # Plastic moduli
                ('Zx', 'plastic_modulus_x', MODULUS_CONV, 'mm³'),
                ('Zy', 'plastic_modulus_y', MODULUS_CONV, 'mm³'),
                
                # Radii of gyration
                ('rx', 'radius_gyration_x', LENGTH_CONV, 'mm'),
                ('ry', 'radius_gyration_y', LENGTH_CONV, 'mm'),
                
                # Torsional properties
                ('J', 'torsional_constant', MOMENT_CONV, 'mm⁴'),
                ('Cw', 'warping_constant', MOMENT_CONV * LENGTH_CONV * LENGTH_CONV, 'mm⁶'),
                
                # Additional properties for specific shapes
                ('k', 'detailing_dimension_k', LENGTH_CONV, 'mm'),
                ('k1', 'detailing_dimension_k1', LENGTH_CONV, 'mm'),
                ('kdes', 'design_dimension_k', LENGTH_CONV, 'mm'),
                ('T', 'flange_width_half', LENGTH_CONV, 'mm'),
            ]
            
            # Extract available properties
            for steelpy_name, prop_name, conversion, unit in property_mappings:
                if hasattr(section, steelpy_name):
                    try:
                        value = getattr(section, steelpy_name)
                        if isinstance(value, (int, float)) and value > 0:
                            properties[prop_name] = {
                                'value': round(value * conversion, 2),
                                'unit': unit,
                                'original': value
                            }
                    except:
                        continue
            
            # Add derived properties for compatibility
            if 'moment_inertia_x' in properties:
                properties['ix'] = properties['moment_inertia_x']['value']
                properties['major_axis_inertia'] = properties['moment_inertia_x']['value']
            
            if 'moment_inertia_y' in properties:
                properties['iy'] = properties['moment_inertia_y']['value'] 
                properties['minor_axis_inertia'] = properties['moment_inertia_y']['value']
            
            if 'section_modulus_x' in properties:
                properties['sx'] = properties['section_modulus_x']['value']
                properties['major_axis_modulus'] = properties['section_modulus_x']['value']
            
            if 'section_modulus_y' in properties:
                properties['sy'] = properties['section_modulus_y']['value']
                properties['minor_axis_modulus'] = properties['section_modulus_y']['value']
            
            # Simple properties for backward compatibility
            for key, prop_data in properties.items():
                if isinstance(prop_data, dict) and 'value' in prop_data:
                    # Also store simple value
                    simple_key = key.replace('_', '').lower()
                    properties[simple_key] = prop_data['value']
            
            return properties
            
        except Exception as e:
            print(f"[WARNING] Property extraction failed for {section_name}: {e}")
            return None
    
    def extract_geometry_data(self, section, shape_type, section_name, shape_info):
        """Extract geometry data for drawing sections"""
        try:
            geometry = {
                'name': section_name,
                'type': shape_info['geometry_type'],
                'category': shape_info['category']
            }
            
            # Extract key dimensions based on shape type
            if shape_info['geometry_type'] in ['I_BEAM', 'H_PILE']:
                # I-beam geometry
                geometry.update({
                    'beam_type': 'I_BEAM',
                    'height': self.safe_get_dimension(section, ['d', 'H'], 25.4),
                    'width': self.safe_get_dimension(section, ['bf', 'B'], 25.4),
                    'web_thickness': self.safe_get_dimension(section, ['tw'], 25.4),
                    'flange_thickness': self.safe_get_dimension(section, ['tf'], 25.4),
                    'fillet_radius': self.safe_get_dimension(section, ['k', 'k1'], 25.4, default=10),
                    'drawing_points': self.calculate_i_beam_points(section)
                })
            
            elif shape_info['geometry_type'] == 'TEE':
                # T-section geometry
                geometry.update({
                    'beam_type': 'TEE',
                    'height': self.safe_get_dimension(section, ['d', 'H'], 25.4),
                    'width': self.safe_get_dimension(section, ['bf', 'B'], 25.4),
                    'web_thickness': self.safe_get_dimension(section, ['tw'], 25.4),
                    'flange_thickness': self.safe_get_dimension(section, ['tf'], 25.4),
                    'drawing_points': self.calculate_tee_points(section)
                })
            
            elif shape_info['geometry_type'] == 'ANGLE':
                # Angle geometry
                geometry.update({
                    'beam_type': 'ANGLE',
                    'leg1': self.safe_get_dimension(section, ['d1', 'd'], 25.4),
                    'leg2': self.safe_get_dimension(section, ['d2', 'bf'], 25.4),
                    'thickness': self.safe_get_dimension(section, ['t'], 25.4),
                    'drawing_points': self.calculate_angle_points(section)
                })
            
            elif shape_info['geometry_type'] in ['PIPE', 'HSS_ROUND']:
                # Circular geometry
                geometry.update({
                    'beam_type': 'CIRCULAR',
                    'outer_diameter': self.safe_get_dimension(section, ['OD', 'd'], 25.4),
                    'inner_diameter': self.safe_get_dimension(section, ['ID'], 25.4),
                    'wall_thickness': self.safe_get_dimension(section, ['t'], 25.4),
                    'drawing_points': self.calculate_circular_points(section)
                })
            
            elif shape_info['geometry_type'] == 'HSS_RECT':
                # Rectangular HSS geometry
                geometry.update({
                    'beam_type': 'RECTANGULAR',
                    'height': self.safe_get_dimension(section, ['H', 'd'], 25.4),
                    'width': self.safe_get_dimension(section, ['B', 'bf'], 25.4),
                    'thickness': self.safe_get_dimension(section, ['t'], 25.4),
                    'drawing_points': self.calculate_rect_hss_points(section)
                })
            
            return geometry
            
        except Exception as e:
            print(f"[WARNING] Geometry extraction failed for {section_name}: {e}")
            return None
    
    def safe_get_dimension(self, section, attr_names, conversion=1.0, default=None):
        """Safely get dimension from section with conversion"""
        for attr in attr_names:
            if hasattr(section, attr):
                try:
                    value = getattr(section, attr)
                    if isinstance(value, (int, float)) and value > 0:
                        return round(value * conversion, 2)
                except:
                    continue
        return default
    
    def calculate_i_beam_points(self, section):
        """Calculate drawing points for I-beam"""
        try:
            h = self.safe_get_dimension(section, ['d', 'H'], 25.4, 200)
            w = self.safe_get_dimension(section, ['bf', 'B'], 25.4, 100)
            tw = self.safe_get_dimension(section, ['tw'], 25.4, 8)
            tf = self.safe_get_dimension(section, ['tf'], 25.4, 12)
            
            # I-beam outline points (centered at origin)
            points = [
                # Top flange
                (-w/2, h/2), (w/2, h/2), (w/2, h/2-tf), (tw/2, h/2-tf),
                # Web to bottom
                (tw/2, -h/2+tf), (w/2, -h/2+tf),
                # Bottom flange  
                (w/2, -h/2), (-w/2, -h/2), (-w/2, -h/2+tf), (-tw/2, -h/2+tf),
                # Web back to top
                (-tw/2, h/2-tf), (-w/2, h/2-tf), (-w/2, h/2)
            ]
            
            return points
            
        except:
            return []
    
    def calculate_tee_points(self, section):
        """Calculate drawing points for T-section"""
        try:
            h = self.safe_get_dimension(section, ['d', 'H'], 25.4, 100)
            w = self.safe_get_dimension(section, ['bf', 'B'], 25.4, 100)
            tw = self.safe_get_dimension(section, ['tw'], 25.4, 8)
            tf = self.safe_get_dimension(section, ['tf'], 25.4, 12)
            
            # T-section outline points
            points = [
                # Top flange
                (-w/2, h/2), (w/2, h/2), (w/2, h/2-tf), (tw/2, h/2-tf),
                # Web down
                (tw/2, -h/2), (-tw/2, -h/2),
                # Web back up
                (-tw/2, h/2-tf), (-w/2, h/2-tf), (-w/2, h/2)
            ]
            
            return points
            
        except:
            return []
    
    def calculate_angle_points(self, section):
        """Calculate drawing points for angle section"""
        try:
            leg1 = self.safe_get_dimension(section, ['d1', 'd'], 25.4, 75)
            leg2 = self.safe_get_dimension(section, ['d2', 'bf'], 25.4, 75) 
            t = self.safe_get_dimension(section, ['t'], 25.4, 6)
            
            # L-section outline points (corner at origin)
            points = [
                (0, 0), (leg2, 0), (leg2, t), (t, t), (t, leg1), (0, leg1), (0, 0)
            ]
            
            return points
            
        except:
            return []
    
    def calculate_circular_points(self, section):
        """Calculate drawing points for circular section"""
        try:
            od = self.safe_get_dimension(section, ['OD', 'd'], 25.4, 100)
            id_val = self.safe_get_dimension(section, ['ID'], 25.4, 0)
            
            # Store as circle parameters
            return {
                'type': 'circle',
                'outer_radius': od/2,
                'inner_radius': id_val/2 if id_val else 0,
                'center': (0, 0)
            }
            
        except:
            return {'type': 'circle', 'outer_radius': 50, 'inner_radius': 0, 'center': (0, 0)}
    
    def calculate_rect_hss_points(self, section):
        """Calculate drawing points for rectangular HSS"""
        try:
            h = self.safe_get_dimension(section, ['H', 'd'], 25.4, 100)
            w = self.safe_get_dimension(section, ['B', 'bf'], 25.4, 100)
            t = self.safe_get_dimension(section, ['t'], 25.4, 6)
            
            # Outer rectangle
            outer = [(-w/2, -h/2), (w/2, -h/2), (w/2, h/2), (-w/2, h/2), (-w/2, -h/2)]
            
            # Inner rectangle (if wall thickness allows)
            inner_w = w - 2*t
            inner_h = h - 2*t
            inner = []
            if inner_w > 0 and inner_h > 0:
                inner = [(-inner_w/2, -inner_h/2), (inner_w/2, -inner_h/2), 
                        (inner_w/2, inner_h/2), (-inner_w/2, inner_h/2), (-inner_w/2, -inner_h/2)]
            
            return {'outer': outer, 'inner': inner}
            
        except:
            return {'outer': [], 'inner': []}
    
    def save_to_cache(self):
        """Save database to cache file"""
        try:
            with open(self.database_file, 'w') as f:
                json.dump(self.sections_database, f, indent=2)
            print(f"[OK] Enhanced database cached to {self.database_file}")
        except Exception as e:
            print(f"[ERROR] Failed to save cache: {e}")
    
    def load_from_cache(self):
        """Load database from cache file"""
        try:
            with open(self.database_file, 'r') as f:
                self.sections_database = json.load(f)
            
            total_sections = self.sections_database['metadata']['total_sections']
            total_shapes = self.sections_database['metadata']['total_shapes']
            
            print(f"[OK] Enhanced database loaded from cache: {total_sections} sections, {total_shapes} shapes")
            
        except Exception as e:
            print(f"[ERROR] Failed to load cache: {e}")
            self.build_enhanced_database()
    
    def get_shape_types(self):
        """Get all available shape types"""
        if not self.available or not self.sections_database:
            return {}
        return self.sections_database.get('shape_types', {})
    
    def get_sections_list(self, shape_type):
        """Get sections list for a shape type"""
        if not self.available or not self.sections_database:
            return []
        
        shape_info = self.sections_database.get('shape_types', {}).get(shape_type, {})
        return shape_info.get('sections', [])
    
    def get_section_properties(self, shape_type, section_name):
        """Get complete properties for a section"""
        if not self.available or not self.sections_database:
            return None
        
        sections = self.sections_database.get('sections', {}).get(shape_type, {})
        return sections.get(section_name)
    
    def get_section_geometry(self, shape_type, section_name):
        """Get geometry data for drawing"""
        if not self.available or not self.sections_database:
            return None
        
        geometries = self.sections_database.get('geometries', {}).get(shape_type, {})
        return geometries.get(section_name)
    
    def search_sections(self, query, shape_type=None, category=None):
        """Advanced search with category filtering"""
        if not self.available or not self.sections_database:
            return []
        
        results = []
        query_lower = query.lower() if query else ""
        
        shape_types_to_search = [shape_type] if shape_type else self.sections_database.get('shape_types', {}).keys()
        
        for st in shape_types_to_search:
            shape_info = self.sections_database.get('shape_types', {}).get(st, {})
            
            # Filter by category if specified
            if category and shape_info.get('category') != category:
                continue
            
            sections = self.sections_database.get('sections', {}).get(st, {})
            
            for section_name, properties in sections.items():
                if not query_lower or query_lower in section_name.lower():
                    results.append({
                        'name': section_name,
                        'shape_type': st,
                        'shape_name': shape_info.get('name', st),
                        'category': shape_info.get('category', 'Unknown'),
                        'properties': properties,
                        'geometry': self.get_section_geometry(st, section_name)
                    })
        
        return results
    
    def get_statistics(self):
        """Get enhanced database statistics"""
        if not self.available or not self.sections_database:
            return {'total_sections': 0, 'total_shapes': 0, 'by_category': {}, 'by_type': {}}
        
        metadata = self.sections_database.get('metadata', {})
        shape_types = self.sections_database.get('shape_types', {})
        
        stats = {
            'total_sections': metadata.get('total_sections', 0),
            'total_shapes': metadata.get('total_shapes', 0),
            'by_category': {},
            'by_type': {}
        }
        
        # Group by category
        for shape_type, info in shape_types.items():
            category = info.get('category', 'Unknown')
            if category not in stats['by_category']:
                stats['by_category'][category] = {'count': 0, 'shapes': []}
            
            stats['by_category'][category]['count'] += info.get('count', 0)
            stats['by_category'][category]['shapes'].append(info.get('name', shape_type))
            
            stats['by_type'][shape_type] = {
                'name': info.get('name', shape_type),
                'category': category,
                'count': info.get('count', 0)
            }
        
        return stats

# Create global enhanced database instance
enhanced_steel_database = EnhancedSteelDatabase()

# Export functions
def get_enhanced_database():
    """Get enhanced steel database instance"""
    return enhanced_steel_database

def get_enhanced_shape_types():
    """Get shape types from enhanced database"""
    return enhanced_steel_database.get_shape_types()

def get_enhanced_sections(shape_type):
    """Get sections from enhanced database"""
    return enhanced_steel_database.get_sections_list(shape_type)

def get_enhanced_section_data(shape_type, section_name):
    """Get complete section data"""
    return enhanced_steel_database.get_section_properties(shape_type, section_name)

def get_section_geometry_data(shape_type, section_name):
    """Get geometry data for drawing"""
    return enhanced_steel_database.get_section_geometry(shape_type, section_name)

def search_enhanced_sections(query, shape_type=None, category=None):
    """Search enhanced database"""
    return enhanced_steel_database.search_sections(query, shape_type, category)

# Test function
def test_enhanced_database():
    """Test the enhanced database"""
    print("Testing Enhanced Steel Database:")
    print("=" * 50)
    
    if not enhanced_steel_database.available:
        print("[ERROR] Enhanced database not available")
        return False
    
    # Test statistics
    stats = enhanced_steel_database.get_statistics()
    print(f"Total sections: {stats['total_sections']}")
    print(f"Total shapes: {stats['total_shapes']}")
    
    print("\nBy Category:")
    for category, info in stats['by_category'].items():
        print(f"  {category}: {info['count']} sections")
    
    # Test section lookup
    shape_types = get_enhanced_shape_types()
    if shape_types:
        first_shape = list(shape_types.keys())[0]
        sections = get_enhanced_sections(first_shape)
        if sections:
            sample_section = sections[0]
            properties = get_enhanced_section_data(first_shape, sample_section)
            geometry = get_section_geometry_data(first_shape, sample_section)
            
            print(f"\nSample section: {sample_section}")
            print(f"Properties available: {len(properties) if properties else 0}")
            print(f"Geometry available: {bool(geometry)}")
    
    return True

if __name__ == "__main__":
    test_enhanced_database()