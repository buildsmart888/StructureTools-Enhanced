# -*- coding: utf-8 -*-
"""
Steelpy Database Integration Module

Integrates with steelpy CSV database files for comprehensive steel section profiles.
Supports AISC standard sections including W, HSS, PIPE, L, C, and other shapes.

Based on steelpy project: https://github.com/steelpy/steelpy
Supports steelpy /shape files format (W_shapes.csv, HSS_shapes.csv, etc.)
"""

import os
import csv
import math
from typing import Dict, List, Optional, Tuple, Any, Union

# FreeCAD imports
try:
    import FreeCAD as App
    import Part
    FREECAD_AVAILABLE = True
except ImportError:
    FREECAD_AVAILABLE = False


class SteelpyDatabaseManager:
    """Manager for steelpy CSV database files"""
    
    def __init__(self, shape_directory: str = None):
        """
        Initialize with steelpy shape files directory
        
        Args:
            shape_directory: Path to steelpy 'shape files' directory
        """
        self.shape_directory = shape_directory
        self.units = "inch"  # AISC files are in inches
        self.mm_per_inch = 25.4
        
        # Standard steelpy file mapping
        self.files = {
            "W": "W_shapes.csv", "M": "M_shapes.csv", "S": "S_shapes.csv", "HP": "HP_shapes.csv",
            "WT": "WT_shapes.csv", "MT": "MT_shapes.csv", "ST": "ST_shapes.csv",
            "C": "C_shapes.csv", "MC": "MC_shapes.csv",
            "L": "L_shapes.csv",
            "HSS": "HSS_shapes.csv", "HSS_R": "HSS_R_shapes.csv",
            "PIPE": "PIPE_shapes.csv",
        }
        
        # Profile type mapping for StructureTools compatibility
        self.profile_type_mapping = {
            "W": "I-Beam", "M": "I-Beam", "S": "I-Beam", "HP": "I-Beam",
            "WT": "T-Section", "MT": "T-Section", "ST": "T-Section",
            "C": "Channel", "MC": "Channel",
            "L": "Angle",
            "HSS": "HSS Rectangular", "HSS_R": "HSS Circular",
            "PIPE": "HSS Circular"
        }
    
    def set_shape_directory(self, directory: str):
        """Set the steelpy shape files directory"""
        self.shape_directory = directory
        
    def u(self, val: str) -> float:
        """Convert string to float and apply unit conversion"""
        if val is None or val == "":
            return 0.0
        x = float(val)
        # Convert inches to mm if needed
        return x * self.mm_per_inch if self.units.lower() == "inch" else x
    
    def read_shape_row(self, kind: str, designation: str) -> Optional[Dict[str, str]]:
        """
        Read specific profile data from steelpy CSV file
        
        Args:
            kind: Profile kind ('W', 'HSS', 'PIPE', etc.)
            designation: Profile designation (e.g., 'W12X26')
            
        Returns:
            Dictionary of profile properties or None if not found
        """
        if not self.shape_directory or kind not in self.files:
            return None
            
        csv_path = os.path.join(self.shape_directory, self.files[kind])
        if not os.path.exists(csv_path):
            return None
            
        try:
            with open(csv_path, newline="", encoding="utf-8-sig") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row.get("Designation", "").strip() == designation.strip():
                        return row
        except Exception:
            return None
            
        return None
    
    def g(self, row: Dict[str, str], *keys, default: str = "0") -> str:
        """Get value from multiple possible keys (version compatibility)"""
        for k in keys:
            v = row.get(k)
            if v not in (None, ""):
                return v
        return default
    
    def get_available_profiles(self, kind: str) -> List[str]:
        """Get list of available profiles for a given kind"""
        if not self.shape_directory or kind not in self.files:
            return []
            
        csv_path = os.path.join(self.shape_directory, self.files[kind])
        if not os.path.exists(csv_path):
            return []
            
        profiles = []
        try:
            with open(csv_path, newline="", encoding="utf-8-sig") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    designation = row.get("Designation", "").strip()
                    if designation:
                        profiles.append(designation)
        except Exception:
            return []
            
        return profiles
    
    def get_all_available_profiles(self) -> Dict[str, List[str]]:
        """Get all available profiles organized by type"""
        all_profiles = {}
        for kind in self.files.keys():
            profiles = self.get_available_profiles(kind)
            if profiles:
                all_profiles[kind] = profiles
        return all_profiles
    
    def extract_dimensions_from_row(self, kind: str, row: Dict[str, str]) -> Dict[str, float]:
        """Extract dimensions from CSV row and convert to StructureTools format"""
        K = kind.upper()
        dimensions = {}
        
        if K in ("W", "M", "S", "HP"):
            # I-Beam/Wide Flange sections
            dimensions = {
                'height': self.u(self.g(row, "d")),
                'width': self.u(self.g(row, "bf")),
                'web_thickness': self.u(self.g(row, "tw")),
                'flange_thickness': self.u(self.g(row, "tf"))
            }
            
        elif K in ("WT", "MT", "ST"):
            # T-Sections
            dimensions = {
                'height': self.u(self.g(row, "d")),
                'width': self.u(self.g(row, "bf")),
                'web_thickness': self.u(self.g(row, "tw")),
                'flange_thickness': self.u(self.g(row, "tf"))
            }
            
        elif K in ("C", "MC"):
            # Channel sections
            dimensions = {
                'height': self.u(self.g(row, "d")),
                'width': self.u(self.g(row, "bf")),
                'web_thickness': self.u(self.g(row, "tw")),
                'flange_thickness': self.u(self.g(row, "tf"))
            }
            
        elif K == "L":
            # Angle sections
            dimensions = {
                'leg1': self.u(self.g(row, "b", "bf")),
                'leg2': self.u(self.g(row, "d")),
                'thickness': self.u(self.g(row, "t", "tf", "tw"))
            }
            
        elif K == "HSS":
            # Rectangular HSS
            dimensions = {
                'height': self.u(self.g(row, "H", "h", "d")),
                'width': self.u(self.g(row, "B", "b", "bf")),
                'thickness': self.u(self.g(row, "tdes", "tnom", "t"))
            }
            
        elif K in ("HSS_R", "PIPE"):
            # Circular HSS/Pipe
            dimensions = {
                'diameter': self.u(self.g(row, "OD", "Do", "d")),
                'thickness': self.u(self.g(row, "tdes", "tnom", "t"))
            }
            
        return dimensions
    
    def get_profile_properties(self, kind: str, designation: str) -> Optional[Dict[str, Any]]:
        """
        Get complete profile properties from steelpy database
        
        Args:
            kind: Profile kind ('W', 'HSS', etc.)
            designation: Profile designation
            
        Returns:
            Dictionary with dimensions, properties, and StructureTools compatibility info
        """
        row = self.read_shape_row(kind, designation)
        if not row:
            return None
            
        dimensions = self.extract_dimensions_from_row(kind, row)
        profile_type = self.profile_type_mapping.get(kind, "Custom")
        
        # Extract additional properties if available
        properties = {
            'kind': kind,
            'designation': designation,
            'profile_type': profile_type,
            'dimensions': dimensions,
            'raw_data': row
        }
        
        # Add structural properties if available in CSV
        if 'A' in row and row['A']:
            properties['area'] = self.u(row['A']) * self.mm_per_inch  # Convert area units
        if 'Ix' in row and row['Ix']:
            properties['moment_inertia_x'] = self.u(row['Ix']) * (self.mm_per_inch ** 4)
        if 'Iy' in row and row['Iy']:
            properties['moment_inertia_y'] = self.u(row['Iy']) * (self.mm_per_inch ** 4)
        if 'W' in row and row['W']:  # Weight per foot
            properties['weight_per_length'] = float(row['W']) * 14.5939  # lb/ft to N/m
            
        return properties


class SteelpyGeometryGenerator:
    """Generate precise 2D geometry from steelpy database"""
    
    def __init__(self, database_manager: SteelpyDatabaseManager):
        self.db = database_manager
    
    def poly_face(self, points: List[Tuple[float, float]]) -> 'Part.Face':
        """Create Part.Face from list of (x,y) points with automatic closure"""
        if not FREECAD_AVAILABLE:
            raise ImportError("FreeCAD not available for geometry generation")
            
        vs = [App.Vector(x, y, 0) for (x, y) in points]
        if (vs[0] - vs[-1]).Length > 1e-9:
            vs.append(vs[0])  # Close polygon
        wire = Part.makePolygon(vs)
        return Part.Face(wire)
    
    def face_w_like(self, d: float, bf: float, tw: float, tf: float) -> 'Part.Face':
        """Create W/I-beam like sections (W, M, S, HP)"""
        # Center at (0,0)
        outer = self.poly_face([(-bf/2, -d/2), (bf/2, -d/2), (bf/2, d/2), (-bf/2, d/2)])
        
        # Cutouts above/below flanges
        inner_top = self.poly_face([(-bf/2, d/2 - tf), (bf/2, d/2 - tf), (bf/2, d/2), (-bf/2, d/2)])
        inner_bot = self.poly_face([(-bf/2, -d/2), (bf/2, -d/2), (bf/2, -d/2 + tf), (-bf/2, -d/2 + tf)])
        
        # Cutouts left/right of web
        hw = tw / 2
        inner_mid_L = self.poly_face([(-bf/2, -tf/2), (-hw, -tf/2), (-hw, tf/2), (-bf/2, tf/2)])
        inner_mid_R = self.poly_face([(hw, -tf/2), (bf/2, -tf/2), (bf/2, tf/2), (hw, tf/2)])
        
        return outer.cut(inner_top).cut(inner_bot).cut(inner_mid_L).cut(inner_mid_R)
    
    def face_channel(self, d: float, bf: float, tw: float, tf: float) -> 'Part.Face':
        """Create C-channel sections"""
        # Reference web centerline at x=tw/2, opening towards +x
        outer = self.poly_face([(0, -d/2), (bf, -d/2), (bf, d/2), (0, d/2)])
        inner = self.poly_face([(tw, -d/2 + tf), (bf, -d/2 + tf), (bf, d/2 - tf), (tw, d/2 - tf)])
        return outer.cut(inner)
    
    def face_angle(self, b: float, d: float, t: float) -> 'Part.Face':
        """Create L-angle sections"""
        # Inside corner at (0,0) extending to +x, +y
        return self.poly_face([(0, 0), (b, 0), (b, t), (t, t), (t, d), (0, d)])
    
    def face_hss_rect(self, H: float, B: float, t: float) -> 'Part.Face':
        """Create rectangular HSS"""
        outer = self.poly_face([(-B/2, -H/2), (B/2, -H/2), (B/2, H/2), (-B/2, H/2)])
        inner = self.poly_face([
            (-(B/2 - t), -(H/2 - t)), ((B/2 - t), -(H/2 - t)),
            ((B/2 - t), (H/2 - t)), (-(B/2 - t), (H/2 - t))
        ])
        return outer.cut(inner)
    
    def face_pipe(self, Do: float, t: float) -> 'Part.Face':
        """Create circular pipe/HSS"""
        if not FREECAD_AVAILABLE:
            raise ImportError("FreeCAD not available for circular geometry")
            
        Ro, Ri = Do/2.0, Do/2.0 - t
        outer = Part.Face(Part.Wire(Part.makeCircle(Ro, App.Vector(0, 0, 0))))
        inner = Part.Face(Part.Wire(Part.makeCircle(Ri, App.Vector(0, 0, 0))))
        return outer.cut(inner)
    
    def create_2d_face(self, kind: str, designation: str) -> Optional['Part.Face']:
        """
        Create 2D face geometry from steelpy database
        
        Args:
            kind: Profile kind ('W', 'HSS', etc.)
            designation: Profile designation (e.g., 'W12X26')
            
        Returns:
            Part.Face geometry or None if failed
        """
        if not FREECAD_AVAILABLE:
            return None
            
        row = self.db.read_shape_row(kind, designation)
        if not row:
            return None
        
        K = kind.upper()
        
        try:
            if K in ("W", "M", "S", "HP"):
                d = self.db.u(self.db.g(row, "d"))
                bf = self.db.u(self.db.g(row, "bf"))
                tw = self.db.u(self.db.g(row, "tw"))
                tf = self.db.u(self.db.g(row, "tf"))
                return self.face_w_like(d, bf, tw, tf)
                
            elif K in ("WT", "MT", "ST"):
                d = self.db.u(self.db.g(row, "d"))
                bf = self.db.u(self.db.g(row, "bf"))
                tw = self.db.u(self.db.g(row, "tw"))
                tf = self.db.u(self.db.g(row, "tf"))
                # Create I-beam and cut bottom half
                full = self.face_w_like(d * 2, bf, tw, tf)
                cutter = self.poly_face([(-1e4, -1e4), (1e4, -1e4), (1e4, 0), (-1e4, 0)])
                return full.cut(cutter)
                
            elif K in ("C", "MC"):
                d = self.db.u(self.db.g(row, "d"))
                bf = self.db.u(self.db.g(row, "bf"))
                tw = self.db.u(self.db.g(row, "tw"))
                tf = self.db.u(self.db.g(row, "tf"))
                return self.face_channel(d, bf, tw, tf)
                
            elif K == "L":
                b = self.db.u(self.db.g(row, "b", "bf"))
                d = self.db.u(self.db.g(row, "d"))
                t = self.db.u(self.db.g(row, "t", "tf", "tw"))
                return self.face_angle(b, d, t)
                
            elif K == "HSS":
                H = self.db.u(self.db.g(row, "H", "h", "d"))
                B = self.db.u(self.db.g(row, "B", "b", "bf"))
                t = self.db.u(self.db.g(row, "tdes", "tnom", "t"))
                return self.face_hss_rect(H, B, t)
                
            elif K in ("HSS_R", "PIPE"):
                Do = self.db.u(self.db.g(row, "OD", "Do", "d"))
                t = self.db.u(self.db.g(row, "tdes", "tnom", "t"))
                return self.face_pipe(Do, t)
                
            else:
                return None
                
        except Exception as e:
            if FREECAD_AVAILABLE and hasattr(App, 'Console'):
                App.Console.PrintError(f"Steelpy geometry creation failed: {e}\n")
            return None


# ================================================================================================
# INTEGRATION WITH STRUCTURETOOLS PROFILE SYSTEM
# ================================================================================================

def integrate_steelpy_with_profile_system(steelpy_directory: str = None):
    """
    Create integrated steelpy database manager for StructureTools
    
    Args:
        steelpy_directory: Path to steelpy shape files directory
        
    Returns:
        Configured SteelpyDatabaseManager instance
    """
    manager = SteelpyDatabaseManager(steelpy_directory)
    return manager


def search_steelpy_profiles(manager: SteelpyDatabaseManager, 
                           search_term: str = "", 
                           profile_kinds: List[str] = None) -> List[Dict[str, Any]]:
    """
    Search steelpy database for profiles matching criteria
    
    Args:
        manager: SteelpyDatabaseManager instance
        search_term: Search term for designation
        profile_kinds: List of profile kinds to search in
        
    Returns:
        List of matching profiles with their properties
    """
    if profile_kinds is None:
        profile_kinds = list(manager.files.keys())
    
    results = []
    
    for kind in profile_kinds:
        profiles = manager.get_available_profiles(kind)
        for designation in profiles:
            if search_term.upper() in designation.upper():
                properties = manager.get_profile_properties(kind, designation)
                if properties:
                    results.append(properties)
    
    return results


def create_structural_profile_from_steelpy(manager: SteelpyDatabaseManager,
                                         kind: str, designation: str,
                                         profile_name: str = None) -> Optional['StructuralProfile']:
    """
    Create StructuralProfile object from steelpy database entry
    
    Args:
        manager: SteelpyDatabaseManager instance
        kind: Profile kind
        designation: Profile designation
        profile_name: Name for created profile object
        
    Returns:
        StructuralProfile object or None if failed
    """
    if not FREECAD_AVAILABLE:
        return None
        
    try:
        from ..objects.StructuralProfile import create_structural_profile
        
        properties = manager.get_profile_properties(kind, designation)
        if not properties:
            return None
        
        # Create profile object
        if not profile_name:
            profile_name = f"{kind}_{designation.replace('/', '_')}"
            
        profile = create_structural_profile(
            name=profile_name,
            profile_type=properties['profile_type'],
            profile_standard="AISC"
        )
        
        # Set dimensions from steelpy data
        dimensions = properties['dimensions']
        for dim_name, value in dimensions.items():
            if dim_name == 'height' and hasattr(profile, 'Height'):
                profile.Height = f"{value} mm"
            elif dim_name == 'width' and hasattr(profile, 'Width'):
                profile.Width = f"{value} mm"
            elif dim_name == 'web_thickness' and hasattr(profile, 'WebThickness'):
                profile.WebThickness = f"{value} mm"
            elif dim_name == 'flange_thickness' and hasattr(profile, 'FlangeThickness'):
                profile.FlangeThickness = f"{value} mm"
            elif dim_name == 'thickness' and hasattr(profile, 'Thickness'):
                profile.Thickness = f"{value} mm"
            elif dim_name == 'diameter' and hasattr(profile, 'Diameter'):
                profile.Diameter = f"{value} mm"
            elif dim_name == 'leg1' and hasattr(profile, 'Leg1'):
                profile.Leg1 = f"{value} mm"
            elif dim_name == 'leg2' and hasattr(profile, 'Leg2'):
                profile.Leg2 = f"{value} mm"
        
        # Set additional properties
        if hasattr(profile, 'ProfileName'):
            profile.ProfileName = designation
        if hasattr(profile, 'Database'):
            profile.Database = f"Steelpy_{kind}"
            
        # Force geometry update
        if hasattr(profile, 'touch'):
            profile.touch()
            
        App.ActiveDocument.recompute()
        
        return profile
        
    except Exception as e:
        if FREECAD_AVAILABLE and hasattr(App, 'Console'):
            App.Console.PrintError(f"Failed to create StructuralProfile from steelpy: {e}\n")
        return None


# Global steelpy integration instance (will be configured when directory is set)
steelpy_manager = None
steelpy_geometry_generator = None

def configure_steelpy_integration(steelpy_directory: str):
    """Configure steelpy integration with specified directory"""
    global steelpy_manager, steelpy_geometry_generator
    
    steelpy_manager = SteelpyDatabaseManager(steelpy_directory)
    steelpy_geometry_generator = SteelpyGeometryGenerator(steelpy_manager)
    
    if FREECAD_AVAILABLE and hasattr(App, 'Console'):
        App.Console.PrintMessage(f"Steelpy integration configured with directory: {steelpy_directory}\n")
    
    return steelpy_manager


def is_steelpy_available() -> bool:
    """Check if steelpy integration is available and configured"""
    return steelpy_manager is not None and steelpy_manager.shape_directory is not None


def read_csv_profile(csv_file_path: str, designation: str) -> Optional[Dict[str, Any]]:
    """
    Read a specific profile from CSV file
    
    Args:
        csv_file_path: Path to CSV file
        designation: Profile designation to find
        
    Returns:
        Profile properties dictionary or None if not found
    """
    if not os.path.exists(csv_file_path):
        return None
    
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Check various possible designation column names
                profile_name = None
                for col in ['designation', 'AISC_Manual_Label', 'name', 'section']:
                    if col in row:
                        profile_name = row[col].strip()
                        break
                
                if profile_name and profile_name.upper() == designation.upper():
                    # Convert all numeric values
                    properties = {}
                    for key, value in row.items():
                        try:
                            properties[key] = float(value) if value else 0.0
                        except ValueError:
                            properties[key] = value
                    
                    return properties
                    
    except Exception as e:
        if FREECAD_AVAILABLE and hasattr(App, 'Console'):
            App.Console.PrintError(f"Error reading CSV file {csv_file_path}: {e}\n")
    
    return None