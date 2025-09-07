# -*- coding: utf-8 -*-
"""
Fixed SteelPy Integration for StructureTools
การเชื่อมต่อกับ steelpy database แบบแก้ไขปัญหา API
"""

import sys
import json
import os
from pathlib import Path

# Safe steelpy import with API detection
try:
    import steelpy
    from steelpy import aisc
    STEELPY_AVAILABLE = True
    print("[INFO] steelpy library loaded successfully")
except ImportError:
    STEELPY_AVAILABLE = False
    print("[WARNING] steelpy library not available")
    print("Install with: pip install steelpy")

class SafeSteelPyManager:
    """Safe manager for steelpy database operations"""
    
    def __init__(self):
        self.available = STEELPY_AVAILABLE
        self.cache_file = Path(__file__).parent / "steelpy_cache.json"
        self.section_cache = {}
        self.shape_collections = {}
        
        if self.available:
            self.detect_steelpy_api()
    
    def detect_steelpy_api(self):
        """Detect available steelpy API structures"""
        try:
            print("[INFO] Detecting steelpy API structure...")
            
            # Test different possible API structures
            potential_collections = [
                'W_shapes', 'M_shapes', 'S_shapes', 'HP_shapes',
                'WT_shapes', 'MT_shapes', 'ST_shapes',
                'Pipe', 'PIPE', 'pipe',  # Different possible names
                'HSS_round', 'HSS_rect', 'HSS_rectangular',
                'L_shapes', 'Double_L', 'DL_shapes'
            ]
            
            detected_collections = {}
            
            for collection_name in potential_collections:
                try:
                    if hasattr(aisc, collection_name):
                        collection = getattr(aisc, collection_name)
                        
                        # Test if we can access the collection
                        collection_dir = dir(collection)
                        
                        # Count sections (attributes that don't start with _)
                        sections = [attr for attr in collection_dir if not attr.startswith('_')]
                        
                        if len(sections) > 0:
                            detected_collections[collection_name] = {
                                'collection': collection,
                                'section_count': len(sections),
                                'sample_sections': sections[:3]  # First 3 as samples
                            }
                            print(f"[OK] {collection_name}: {len(sections)} sections")
                        else:
                            print(f"[SKIP] {collection_name}: No sections found")
                    else:
                        print(f"[SKIP] {collection_name}: Not available in this steelpy version")
                        
                except Exception as e:
                    print(f"[SKIP] {collection_name}: Error accessing - {e}")
                    continue
            
            # Map detected collections to standard names
            self.shape_collections = {}
            
            # Define mapping from detected names to our standard names
            name_mapping = {
                'W_shapes': ('Wide Flange Beams', 'beam'),
                'M_shapes': ('M Shapes', 'beam'),
                'S_shapes': ('Standard I-Beams', 'beam'),
                'HP_shapes': ('HP Shapes', 'pile'),
                'WT_shapes': ('WT Shapes', 'tee'),
                'MT_shapes': ('MT Shapes', 'tee'),
                'ST_shapes': ('ST Shapes', 'tee'),
                'Pipe': ('Steel Pipe', 'circular'),
                'PIPE': ('Steel Pipe', 'circular'),
                'pipe': ('Steel Pipe', 'circular'),
                'HSS_round': ('HSS Round', 'circular'),
                'HSS_rect': ('HSS Rectangular', 'rectangular'),
                'HSS_rectangular': ('HSS Rectangular', 'rectangular'),
                'L_shapes': ('Angles', 'angle'),
                'Double_L': ('Double Angles', 'double_angle'),
                'DL_shapes': ('Double Angles', 'double_angle')
            }
            
            for detected_name, collection_info in detected_collections.items():
                if detected_name in name_mapping:
                    display_name, shape_type = name_mapping[detected_name]
                    
                    # Use a standardized key (remove duplicates like Pipe/PIPE)
                    if detected_name.upper() == 'PIPE':
                        standard_key = 'Pipe'
                    elif detected_name.upper() == 'HSS_RECTANGULAR':
                        standard_key = 'HSS_rect'
                    elif detected_name.upper() == 'DL_SHAPES':
                        standard_key = 'Double_L'
                    else:
                        standard_key = detected_name
                    
                    # Avoid duplicates
                    if standard_key not in self.shape_collections:
                        self.shape_collections[standard_key] = {
                            'name': display_name,
                            'type': shape_type,
                            'collection': collection_info['collection'],
                            'section_count': collection_info['section_count'],
                            'sample_sections': collection_info['sample_sections']
                        }
            
            total_sections = sum(info['section_count'] for info in self.shape_collections.values())
            print(f"[OK] Detected {len(self.shape_collections)} shape types with {total_sections} total sections")
            
            if not self.shape_collections:
                print("[ERROR] No usable steelpy collections found")
                self.available = False
            
        except Exception as e:
            print(f"[ERROR] Failed to detect steelpy API: {e}")
            self.available = False
    
    def get_shape_types(self):
        """Get available shape types"""
        if not self.available:
            return {}
        
        result = {}
        for key, info in self.shape_collections.items():
            result[key] = {
                'name': info['name'],
                'count': info['section_count'],
                'type': info['type']
            }
        
        return result
    
    def get_sections_list(self, shape_type):
        """Get list of sections for a shape type"""
        if not self.available or shape_type not in self.shape_collections:
            return []
        
        try:
            collection = self.shape_collections[shape_type]['collection']
            sections = [attr for attr in dir(collection) if not attr.startswith('_')]
            return sorted(sections)
        except Exception as e:
            print(f"[ERROR] Failed to get sections for {shape_type}: {e}")
            return []
    
    def get_section_properties(self, shape_type, section_name):
        """Get properties for a specific section"""
        if not self.available or shape_type not in self.shape_collections:
            return None
        
        try:
            collection = self.shape_collections[shape_type]['collection']
            
            if not hasattr(collection, section_name):
                return None
            
            section = getattr(collection, section_name)
            
            # Extract properties safely
            properties = self.extract_properties_safely(section, shape_type, section_name)
            return properties
            
        except Exception as e:
            print(f"[ERROR] Failed to get properties for {section_name}: {e}")
            return None
    
    def extract_properties_safely(self, section, shape_type, section_name):
        """Safely extract properties from section object"""
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
            
            # Define property mappings with safe extraction
            property_mappings = [
                ('A', 'area', AREA_CONV),
                ('W', 'weight', WEIGHT_CONV),
                ('d', 'height', LENGTH_CONV),
                ('bf', 'width', LENGTH_CONV),
                ('tw', 'web_thickness', LENGTH_CONV),
                ('tf', 'flange_thickness', LENGTH_CONV),
                ('t', 'thickness', LENGTH_CONV),
                ('H', 'height', LENGTH_CONV),  # Alternative height
                ('B', 'width', LENGTH_CONV),   # Alternative width
                ('OD', 'outer_diameter', LENGTH_CONV),
                ('ID', 'inner_diameter', LENGTH_CONV),
                ('Ix', 'ix', MOMENT_CONV),
                ('Iy', 'iy', MOMENT_CONV),
                ('Sx', 'sx', MODULUS_CONV),
                ('Sy', 'sy', MODULUS_CONV),
                ('Zx', 'zx', MODULUS_CONV),
                ('Zy', 'zy', MODULUS_CONV),
                ('rx', 'rx', LENGTH_CONV),
                ('ry', 'ry', LENGTH_CONV),
                ('J', 'j', MOMENT_CONV),
                ('Cw', 'cw', MOMENT_CONV * LENGTH_CONV * LENGTH_CONV)
            ]
            
            # Extract properties that exist
            for src_prop, dst_prop, conversion in property_mappings:
                try:
                    if hasattr(section, src_prop):
                        value = getattr(section, src_prop)
                        if isinstance(value, (int, float)) and value > 0:
                            properties[dst_prop] = round(value * conversion, 2 if conversion == WEIGHT_CONV else 0)
                except Exception as e:
                    # Skip properties that can't be extracted
                    continue
            
            # Add derived properties
            if 'ix' in properties:
                properties['moment_inertia_y'] = properties['ix']
            if 'iy' in properties:
                properties['moment_inertia_z'] = properties['iy']
            if 'sx' in properties:
                properties['section_modulus_y'] = properties['sx']
            if 'sy' in properties:
                properties['section_modulus_z'] = properties['sy']
            
            return properties
            
        except Exception as e:
            print(f"[ERROR] Property extraction failed for {section_name}: {e}")
            return None
    
    def search_sections(self, query, shape_type=None):
        """Search sections by name"""
        if not self.available:
            return []
        
        results = []
        query_lower = query.lower()
        
        shape_types_to_search = [shape_type] if shape_type else self.shape_collections.keys()
        
        for st in shape_types_to_search:
            if st not in self.shape_collections:
                continue
                
            sections = self.get_sections_list(st)
            for section_name in sections:
                if query_lower in section_name.lower():
                    properties = self.get_section_properties(st, section_name)
                    if properties:
                        results.append({
                            'name': section_name,
                            'shape_type': st,
                            'shape_name': self.shape_collections[st]['name'],
                            'properties': properties
                        })
        
        return results
    
    def get_statistics(self):
        """Get database statistics"""
        if not self.available:
            return {'total_sections': 0, 'shape_types': 0, 'by_type': {}}
        
        total_sections = sum(info['section_count'] for info in self.shape_collections.values())
        
        stats = {
            'total_sections': total_sections,
            'shape_types': len(self.shape_collections),
            'by_type': {}
        }
        
        for key, info in self.shape_collections.items():
            stats['by_type'][key] = {
                'name': info['name'],
                'count': info['section_count']
            }
        
        return stats

# Create global instance
safe_steelpy_manager = SafeSteelPyManager()

# Export functions that replace the problematic ones
def get_steelpy_manager():
    """Get safe steelpy manager instance"""
    return safe_steelpy_manager

def get_available_shape_types():
    """Get available shape types (safe version)"""
    return safe_steelpy_manager.get_shape_types()

def get_sections_for_shape(shape_type):
    """Get sections for a shape type (safe version)"""
    return safe_steelpy_manager.get_sections_list(shape_type)

def get_section_data(shape_type, section_name):
    """Get section properties (safe version)"""
    return safe_steelpy_manager.get_section_properties(shape_type, section_name)

def search_steel_sections(query, shape_type=None):
    """Search steel sections (safe version)"""
    return safe_steelpy_manager.search_sections(query, shape_type)

# Test function
def test_steelpy_integration():
    """Test the safe integration"""
    print("Testing Safe SteelPy Integration:")
    print("=" * 40)
    
    manager = get_steelpy_manager()
    print(f"Available: {manager.available}")
    
    if manager.available:
        shape_types = get_available_shape_types()
        print(f"Shape types: {len(shape_types)}")
        
        for key, info in list(shape_types.items())[:3]:
            print(f"  {key}: {info['name']} ({info['count']} sections)")
        
        # Test search
        results = search_steel_sections("W12")
        print(f"Search 'W12': {len(results)} results")
        
        if results:
            sample = results[0]
            print(f"Sample: {sample['name']} - Area: {sample['properties'].get('area', 0):.0f} mm²")
    
    return manager.available

if __name__ == "__main__":
    test_steelpy_integration()