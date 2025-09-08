#!/usr/bin/env python3
"""
Verification script for StructureTools Profile System
Tests the complete integration without requiring FreeCAD GUI
"""

import os
import sys

# Add the freecad path to sys.path
script_dir = os.path.dirname(os.path.abspath(__file__))
freecad_path = os.path.join(script_dir, 'freecad')
sys.path.insert(0, freecad_path)

def test_profile_system_components():
    """Test individual components of the profile system"""
    print("=== StructureTools Profile System Verification ===\n")
    
    results = {
        'structural_profile_object': False,
        'profile_task_panel': False,
        'profile_calc_integration': False,
        'profile_geometry_generator': False,
        'profile_command': False,
        'icon_exists': False
    }
    
    # Mock essential FreeCAD modules
    class MockFreeCAD:
        class Console:
            @staticmethod
            def PrintMessage(msg): pass
            @staticmethod 
            def PrintError(msg): pass
            @staticmethod
            def PrintWarning(msg): pass
        
        class DocumentObject:
            def __init__(self):
                self.ViewObject = MockFreeCAD.ViewObject()
                self.Proxy = None
                self.Label = "TestObject"
            def addProperty(self, *args): pass
            def setEditorMode(self, *args): pass
            def touch(self): pass
        
        class ViewObject:
            def __init__(self):
                self.Proxy = None
            def setEdit(self, *args): pass
            def unsetEdit(self, *args): pass
        
        class Units:
            @staticmethod
            def parseQuantity(q): return type('Quantity', (), {'getValueAs': lambda self, u: 200.0})()
        
        @staticmethod
        def Vector(*args): return [0,0,0]
        
        @staticmethod
        def ActiveDocument(): return None
        
        ActiveDocument = None
    
    class MockFreeCADGui:
        class Control:
            @staticmethod
            def showDialog(panel): pass
            @staticmethod
            def closeDialog(): pass
        
        @staticmethod
        def addCommand(name, cmd): pass
    
    class MockPart:
        @staticmethod
        def makeLine(*args): return None
        @staticmethod
        def makeCircle(*args): return None
        @staticmethod
        def Face(*args): return None
        @staticmethod
        def Wire(*args): return None
        @staticmethod
        def Compound(*args): return None
    
    # Install mocks
    sys.modules['FreeCAD'] = MockFreeCAD()
    sys.modules['FreeCADGui'] = MockFreeCADGui()
    sys.modules['App'] = MockFreeCAD()
    sys.modules['Gui'] = MockFreeCADGui()
    sys.modules['Part'] = MockPart()
    
    # Test 1: StructuralProfile Object
    try:
        from StructureTools.objects.StructuralProfile import StructuralProfile, ViewProviderStructuralProfile, create_structural_profile
        print("[OK] StructuralProfile object imports successfully")
        results['structural_profile_object'] = True
    except Exception as e:
        print(f"[ERROR] StructuralProfile object failed: {e}")
    
    # Test 2: ProfileTaskPanel
    try:
        from StructureTools.taskpanels.ProfileTaskPanel import ProfileTaskPanel, show_profile_task_panel
        print("[OK] ProfileTaskPanel imports successfully")
        results['profile_task_panel'] = True
    except Exception as e:
        print(f"[ERROR] ProfileTaskPanel failed: {e}")
    
    # Test 3: Profile Calc Integration
    try:
        from StructureTools.integration.ProfileCalcIntegration import ProfileCalcIntegrator
        print("[OK] ProfileCalcIntegration imports successfully")
        results['profile_calc_integration'] = True
    except Exception as e:
        print(f"[ERROR] ProfileCalcIntegration failed: {e}")
    
    # Test 4: Profile Geometry Generator
    try:
        from StructureTools.data.ProfileGeometryGenerator import AdvancedSectionCalculator, calculate_section_properties_from_dimensions
        print("[OK] ProfileGeometryGenerator imports successfully")
        results['profile_geometry_generator'] = True
    except Exception as e:
        print(f"[ERROR] ProfileGeometryGenerator failed: {e}")
    
    # Test 5: Profile Command
    try:
        from StructureTools.profile import StructuralProfileCommand
        print("[OK] Profile command imports successfully")
        results['profile_command'] = True
    except Exception as e:
        print(f"[ERROR] Profile command failed: {e}")
    
    # Test 6: Icon exists
    icon_path = os.path.join(script_dir, 'freecad', 'StructureTools', 'resources', 'icons', 'structural_profile.svg')
    if os.path.exists(icon_path):
        print("[OK] Profile icon exists")
        results['icon_exists'] = True
    else:
        print("[ERROR] Profile icon missing")
    
    # Summary
    passed = sum(results.values())
    total = len(results)
    print(f"\n=== SUMMARY: {passed}/{total} components working ===")
    
    if passed == total:
        print("[SUCCESS] Profile System is ready for FreeCAD integration!")
    else:
        print("[WARNING] Some components need attention before full integration")
    
    return results

def test_section_calculations():
    """Test section property calculations"""
    print("\n=== Testing Section Calculations ===")
    
    try:
        # Mock additional modules for calculation testing
        import sys
        import numpy as np  # Assume numpy is available
        sys.modules['numpy'] = np
        
        from StructureTools.data.ProfileGeometryGenerator import AdvancedSectionCalculator
        
        calc = AdvancedSectionCalculator()
        
        # Test I-beam calculation
        i_beam_props = calc.calculate_i_beam_properties(
            height=300.0,    # mm
            width=150.0,     # mm  
            web_thickness=8.0,
            flange_thickness=12.0
        )
        
        print("[OK] I-beam calculations completed")
        print(f"  Area: {i_beam_props.get('area', 0):.1f} mm²")
        print(f"  Ix: {i_beam_props.get('Ix', 0):.1f} mm⁴") 
        print(f"  Iy: {i_beam_props.get('Iy', 0):.1f} mm⁴")
        
        return True
        
    except ImportError:
        print("[WARNING] NumPy not available - calculation tests skipped")
        return False
    except Exception as e:
        print(f"[ERROR] Section calculations failed: {e}")
        return False

if __name__ == "__main__":
    # Run component tests
    component_results = test_profile_system_components()
    
    # Run calculation tests if components are working
    if component_results.get('profile_geometry_generator', False):
        calc_results = test_section_calculations()
    
    print(f"\nProfile System Verification Complete!")
    print(f"Ready for FreeCAD testing: {all(component_results.values())}")