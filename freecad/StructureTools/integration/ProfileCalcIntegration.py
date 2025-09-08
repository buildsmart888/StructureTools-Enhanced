# -*- coding: utf-8 -*-
"""
Profile-Calc Integration Module

Provides seamless integration between StructuralProfile objects and the calc system
for structural analysis workflows.
"""

import FreeCAD as App
import math

# Import profile system
try:
    from ..objects.StructuralProfile import StructuralProfile
    from ..data.ProfileGeometryGenerator import (
        calculate_section_properties_from_dimensions,
        generate_calc_properties,
        create_profile_geometry_data
    )
    PROFILE_SYSTEM_AVAILABLE = True
except ImportError:
    PROFILE_SYSTEM_AVAILABLE = False

# Import calc system
try:
    from ..calc import Calc
    CALC_SYSTEM_AVAILABLE = True
except ImportError:
    CALC_SYSTEM_AVAILABLE = False


class ProfileCalcIntegrator:
    """Integrator class for Profile-Calc workflows"""
    
    def __init__(self):
        self.supported_profile_types = [
            'I-Beam', 'Wide Flange', 'Channel', 'Angle',
            'HSS Rectangular', 'HSS Circular', 'Rectangle', 'Circle', 'T-Section'
        ]
        
    def extract_profile_properties(self, profile_obj):
        """Extract calc-compatible properties from StructuralProfile object
        
        Args:
            profile_obj: StructuralProfile object
            
        Returns:
            Dictionary of properties for calc integration
        """
        if not self.is_structural_profile(profile_obj):
            raise ValueError("Object is not a StructuralProfile")
        
        try:
            # Try to get pre-calculated properties
            if hasattr(profile_obj, 'CalcProperties') and profile_obj.CalcProperties:
                return profile_obj.CalcProperties
            
            # Fallback: calculate properties from object dimensions
            return self.calculate_properties_from_object(profile_obj)
            
        except Exception as e:
            App.Console.PrintError(f"Failed to extract profile properties: {e}\n")
            return {}
    
    def calculate_properties_from_object(self, profile_obj):
        """Calculate properties from profile object dimensions"""
        profile_type = profile_obj.ProfileType
        
        # Extract dimensions
        dimensions = {}
        
        if profile_type in ['I-Beam', 'Wide Flange', 'Channel', 'T-Section']:
            dimensions = {
                'height': profile_obj.Height.getValueAs('mm') if hasattr(profile_obj, 'Height') else 200,
                'width': profile_obj.Width.getValueAs('mm') if hasattr(profile_obj, 'Width') else 100,
                'web_thickness': profile_obj.WebThickness.getValueAs('mm') if hasattr(profile_obj, 'WebThickness') else 8,
                'flange_thickness': profile_obj.FlangeThickness.getValueAs('mm') if hasattr(profile_obj, 'FlangeThickness') else 12
            }
        elif profile_type == 'HSS Rectangular':
            dimensions = {
                'height': profile_obj.Height.getValueAs('mm') if hasattr(profile_obj, 'Height') else 150,
                'width': profile_obj.Width.getValueAs('mm') if hasattr(profile_obj, 'Width') else 100,
                'thickness': profile_obj.Thickness.getValueAs('mm') if hasattr(profile_obj, 'Thickness') else 6
            }
        elif profile_type == 'HSS Circular':
            dimensions = {
                'diameter': profile_obj.Diameter.getValueAs('mm') if hasattr(profile_obj, 'Diameter') else 100,
                'thickness': profile_obj.Thickness.getValueAs('mm') if hasattr(profile_obj, 'Thickness') else 6
            }
        elif profile_type == 'Rectangle':
            dimensions = {
                'height': profile_obj.Height.getValueAs('mm') if hasattr(profile_obj, 'Height') else 150,
                'width': profile_obj.Width.getValueAs('mm') if hasattr(profile_obj, 'Width') else 100
            }
        elif profile_type == 'Circle':
            dimensions = {
                'diameter': profile_obj.Diameter.getValueAs('mm') if hasattr(profile_obj, 'Diameter') else 100
            }
        elif profile_type == 'Angle':
            dimensions = {
                'leg1': profile_obj.Leg1.getValueAs('mm') if hasattr(profile_obj, 'Leg1') else 75,
                'leg2': profile_obj.Leg2.getValueAs('mm') if hasattr(profile_obj, 'Leg2') else 50,
                'thickness': profile_obj.Thickness.getValueAs('mm') if hasattr(profile_obj, 'Thickness') else 6
            }
        
        # Calculate properties using the advanced calculator
        section_properties = calculate_section_properties_from_dimensions(profile_type, dimensions)
        return generate_calc_properties(section_properties)
    
    def is_structural_profile(self, obj):
        """Check if object is a StructuralProfile"""
        return (hasattr(obj, 'Proxy') and 
                hasattr(obj.Proxy, 'Type') and 
                obj.Proxy.Type == "StructuralProfile")
    
    def apply_profile_to_member(self, member_obj, profile_obj):
        """Apply StructuralProfile properties to a structural member
        
        Args:
            member_obj: Structural member object (line, beam, etc.)
            profile_obj: StructuralProfile object
        """
        if not self.is_structural_profile(profile_obj):
            raise ValueError("Profile object is not a StructuralProfile")
        
        try:
            # Get calc properties
            calc_props = self.extract_profile_properties(profile_obj)
            
            if not calc_props:
                raise ValueError("No calc properties available from profile")
            
            # Apply properties to member
            if not hasattr(member_obj, 'addProperty'):
                raise ValueError("Member object cannot accept properties")
            
            # Add section properties
            self.add_section_properties_to_member(member_obj, calc_props, profile_obj)
            
            App.Console.PrintMessage(f"Applied profile {profile_obj.Label} to member {member_obj.Label}\n")
            
        except Exception as e:
            App.Console.PrintError(f"Failed to apply profile to member: {e}\n")
            raise
    
    def add_section_properties_to_member(self, member_obj, calc_props, profile_obj):
        """Add section properties to member object"""
        # Add reference to profile
        if not hasattr(member_obj, 'StructuralProfile'):
            member_obj.addProperty("App::PropertyLink", "StructuralProfile", "Section", 
                                 "Associated structural profile")
        member_obj.StructuralProfile = profile_obj
        
        # Add calc-compatible properties
        prop_mappings = [
            ('SectionArea', 'Area', 'Cross-sectional area'),
            ('MomentInertiaY', 'Iy', 'Moment of inertia about major axis'),
            ('MomentInertiaZ', 'Iz', 'Moment of inertia about minor axis'),
            ('TorsionalConstant', 'J', 'Torsional constant'),
            ('SectionModulusY', 'Sy', 'Section modulus about major axis'),
            ('SectionModulusZ', 'Sz', 'Section modulus about minor axis'),
            ('RadiusGyrationY', 'ry', 'Radius of gyration about major axis'),
            ('RadiusGyrationZ', 'rz', 'Radius of gyration about minor axis'),
            ('LinearWeight', 'Weight', 'Weight per unit length')
        ]
        
        for prop_name, calc_key, description in prop_mappings:
            if calc_key in calc_props:
                if not hasattr(member_obj, prop_name):
                    member_obj.addProperty("App::PropertyFloat", prop_name, "Section", description)
                setattr(member_obj, prop_name, calc_props[calc_key])
    
    def create_calc_compatible_section(self, profile_obj, section_name=None):
        """Create a calc-compatible section object from StructuralProfile
        
        Args:
            profile_obj: StructuralProfile object
            section_name: Optional name for the section
            
        Returns:
            Section object compatible with calc
        """
        if not CALC_SYSTEM_AVAILABLE:
            raise ImportError("Calc system not available")
        
        if not section_name:
            section_name = f"Section_{profile_obj.Label}"
        
        # Get calc properties
        calc_props = self.extract_profile_properties(profile_obj)
        
        if not calc_props:
            raise ValueError("No calc properties available")
        
        # Create section object using existing section system
        section_obj = App.ActiveDocument.addObject("Part::FeaturePython", section_name)
        
        # Import and initialize section
        from ..section import Section, ViewProviderSection
        Section(section_obj, [])
        ViewProviderSection(section_obj.ViewObject)
        
        # Apply properties
        if 'Area' in calc_props:
            section_obj.Area = calc_props['Area'] * 1e6  # Convert back to mm² for section object
        if 'Iy' in calc_props:
            section_obj.MomentInertiaY = calc_props['Iy'] * 1e12  # Convert back to mm⁴
        if 'Iz' in calc_props:
            section_obj.MomentInertiaZ = calc_props['Iz'] * 1e12
        if 'J' in calc_props:
            section_obj.MomentInertiaPolar = calc_props['J'] * 1e12
        if 'Sy' in calc_props:
            section_obj.SectionModulusY = calc_props['Sy'] * 1e9  # Convert back to mm³
        if 'Sz' in calc_props:
            section_obj.SectionModulusZ = calc_props['Sz'] * 1e9
        if 'Weight' in calc_props:
            section_obj.Weight = calc_props['Weight']
        
        # Set type and name
        section_obj.SectionType = profile_obj.ProfileType
        if hasattr(profile_obj, 'ProfileName'):
            section_obj.Label = f"Section_{profile_obj.ProfileName}"
        
        App.ActiveDocument.recompute()
        
        return section_obj
    
    def find_profiles_in_document(self, doc=None):
        """Find all StructuralProfile objects in document
        
        Args:
            doc: FreeCAD document (uses active document if None)
            
        Returns:
            List of StructuralProfile objects
        """
        if doc is None:
            doc = App.ActiveDocument
        
        if not doc:
            return []
        
        profiles = []
        for obj in doc.Objects:
            if self.is_structural_profile(obj):
                profiles.append(obj)
        
        return profiles
    
    def generate_calc_summary_report(self, profiles):
        """Generate summary report of all profiles for calc integration
        
        Args:
            profiles: List of StructuralProfile objects
            
        Returns:
            Dictionary with summary data
        """
        report = {
            'total_profiles': len(profiles),
            'profile_types': {},
            'calc_properties': [],
            'integration_status': []
        }
        
        for profile in profiles:
            # Count by type
            ptype = profile.ProfileType
            if ptype not in report['profile_types']:
                report['profile_types'][ptype] = 0
            report['profile_types'][ptype] += 1
            
            # Extract properties
            try:
                calc_props = self.extract_profile_properties(profile)
                if calc_props:
                    profile_data = {
                        'name': profile.Label,
                        'type': ptype,
                        'area': calc_props.get('Area', 0),
                        'iy': calc_props.get('Iy', 0),
                        'iz': calc_props.get('Iz', 0),
                        'weight': calc_props.get('Weight', 0)
                    }
                    report['calc_properties'].append(profile_data)
                    report['integration_status'].append({'name': profile.Label, 'status': 'OK'})
                else:
                    report['integration_status'].append({'name': profile.Label, 'status': 'ERROR'})
                    
            except Exception as e:
                report['integration_status'].append({
                    'name': profile.Label, 
                    'status': 'ERROR', 
                    'error': str(e)
                })
        
        return report


# Global integrator instance
_profile_calc_integrator = ProfileCalcIntegrator()


def apply_profile_to_member(member_obj, profile_obj):
    """Convenience function to apply profile to member"""
    return _profile_calc_integrator.apply_profile_to_member(member_obj, profile_obj)


def create_calc_section_from_profile(profile_obj, section_name=None):
    """Convenience function to create calc section from profile"""
    return _profile_calc_integrator.create_calc_compatible_section(profile_obj, section_name)


def get_profile_calc_properties(profile_obj):
    """Convenience function to get calc properties from profile"""
    return _profile_calc_integrator.extract_profile_properties(profile_obj)


def batch_convert_profiles_to_sections():
    """Convert all StructuralProfiles in document to calc-compatible sections"""
    if not App.ActiveDocument:
        App.Console.PrintError("No active document\n")
        return []
    
    profiles = _profile_calc_integrator.find_profiles_in_document()
    if not profiles:
        App.Console.PrintMessage("No StructuralProfile objects found\n")
        return []
    
    converted_sections = []
    
    for profile in profiles:
        try:
            section = create_calc_section_from_profile(profile)
            converted_sections.append(section)
            App.Console.PrintMessage(f"Converted {profile.Label} to {section.Label}\n")
        except Exception as e:
            App.Console.PrintError(f"Failed to convert {profile.Label}: {e}\n")
    
    App.Console.PrintMessage(f"Converted {len(converted_sections)} profiles to sections\n")
    
    return converted_sections


def generate_integration_report():
    """Generate integration status report"""
    if not App.ActiveDocument:
        App.Console.PrintError("No active document\n")
        return None
    
    profiles = _profile_calc_integrator.find_profiles_in_document()
    report = _profile_calc_integrator.generate_calc_summary_report(profiles)
    
    # Print report
    App.Console.PrintMessage("=== Profile-Calc Integration Report ===\n")
    App.Console.PrintMessage(f"Total Profiles: {report['total_profiles']}\n")
    
    App.Console.PrintMessage("Profile Types:\n")
    for ptype, count in report['profile_types'].items():
        App.Console.PrintMessage(f"  {ptype}: {count}\n")
    
    App.Console.PrintMessage("Integration Status:\n")
    for status_info in report['integration_status']:
        if status_info['status'] == 'OK':
            App.Console.PrintMessage(f"  ✓ {status_info['name']}: OK\n")
        else:
            App.Console.PrintError(f"  ✗ {status_info['name']}: {status_info['status']}\n")
            if 'error' in status_info:
                App.Console.PrintError(f"    Error: {status_info['error']}\n")
    
    return report


# Example workflow functions
def demonstrate_profile_calc_workflow():
    """Demonstrate complete Profile-Calc integration workflow"""
    App.Console.PrintMessage("=== Profile-Calc Integration Demonstration ===\n")
    
    if not App.ActiveDocument:
        App.newDocument("ProfileCalcDemo")
    
    try:
        # 1. Create example structural profile
        from ..objects.StructuralProfile import create_structural_profile
        
        profile = create_structural_profile("DemoProfile_W12x26", "I-Beam", "Custom")
        profile.Height = "311.15 mm"
        profile.Width = "165.1 mm" 
        profile.WebThickness = "6.86 mm"
        profile.FlangeThickness = "9.91 mm"
        
        App.ActiveDocument.recompute()
        App.Console.PrintMessage("1. Created StructuralProfile\n")
        
        # 2. Extract calc properties
        calc_props = get_profile_calc_properties(profile)
        App.Console.PrintMessage("2. Extracted calc properties:\n")
        for key, value in calc_props.items():
            if isinstance(value, float):
                App.Console.PrintMessage(f"   {key}: {value:.6e}\n")
            else:
                App.Console.PrintMessage(f"   {key}: {value}\n")
        
        # 3. Create calc-compatible section
        section = create_calc_section_from_profile(profile, "CalcSection_W12x26")
        App.Console.PrintMessage("3. Created calc-compatible section\n")
        
        # 4. Generate integration report
        App.Console.PrintMessage("4. Integration report:\n")
        report = generate_integration_report()
        
        App.Console.PrintMessage("=== Demonstration Complete ===\n")
        
        return {'profile': profile, 'section': section, 'report': report}
        
    except Exception as e:
        App.Console.PrintError(f"Demonstration failed: {e}\n")
        return None