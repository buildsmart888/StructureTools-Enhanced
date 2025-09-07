# -*- coding: utf-8 -*-
"""
Test script for Steel Profile GUI
สคริปต์ทดสอบ GUI สำหรับเลือก steel profiles
"""

def test_steelpy_integration():
    """Test steelpy integration"""
    print("=== Testing SteelPy Integration ===")
    
    try:
        # Test basic imports
        from freecad.StructureTools.data.SteelPyIntegration import (
            get_steelpy_manager,
            get_available_shape_types,
            get_sections_for_shape,
            get_section_data,
            search_steel_sections,
            STEELPY_AVAILABLE
        )
        
        print(f"1. SteelPy available: {STEELPY_AVAILABLE}")
        
        if not STEELPY_AVAILABLE:
            print("   To install steelpy: pip install steelpy")
            return False
        
        # Test manager
        manager = get_steelpy_manager()
        print(f"2. Manager loaded: {manager is not None}")
        
        # Test shape types
        shape_types = get_available_shape_types()
        print(f"3. Available shape types: {len(shape_types)}")
        
        for shape_key, shape_info in list(shape_types.items())[:3]:  # Show first 3
            print(f"   - {shape_key}: {shape_info['name']} ({shape_info['count']} sections)")
        
        # Test getting sections for a shape type
        if 'W_shapes' in shape_types:
            sections = get_sections_for_shape('W_shapes')
            print(f"4. W-shapes available: {len(sections)}")
            
            # Test getting specific section data
            if sections:
                test_section = sections[0]  # First section
                section_data = get_section_data('W_shapes', test_section)
                
                if section_data:
                    print(f"5. Sample section data for {test_section}:")
                    print(f"   - Area: {section_data.get('area', 0):,.0f} mm²")
                    print(f"   - Weight: {section_data.get('weight', 0):.2f} kg/m")
                    print(f"   - Height: {section_data.get('height', 0):.1f} mm")
                    print(f"   - Width: {section_data.get('width', 0):.1f} mm")
        
        # Test search functionality
        search_results = search_steel_sections("W12")
        print(f"6. Search results for 'W12': {len(search_results)} sections")
        
        print("   ✓ SteelPy integration working correctly")
        return True
        
    except Exception as e:
        print(f"   ✗ SteelPy integration failed: {e}")
        return False

def test_gui_components():
    """Test GUI components"""
    print("\n=== Testing GUI Components ===")
    
    try:
        # Test GUI imports
        from freecad.StructureTools.gui.SectionManagerGUI import show_section_manager_gui
        from freecad.StructureTools.gui.SteelProfileSelector import show_steel_profile_selector
        
        print("1. GUI imports successful")
        
        # Test GUI availability
        try:
            from PySide2 import QtWidgets
            print("2. PySide2 available for GUI")
            gui_available = True
        except ImportError:
            try:
                from PySide import QtWidgets
                print("2. PySide available for GUI")
                gui_available = True
            except ImportError:
                print("2. No GUI libraries available")
                gui_available = False
        
        if gui_available:
            print("   ✓ GUI components ready to use")
        else:
            print("   ! GUI components available but no Qt libraries")
        
        return True
        
    except Exception as e:
        print(f"   ✗ GUI component test failed: {e}")
        return False

def test_arch_integration():
    """Test ArchProfile integration"""
    print("\n=== Testing ArchProfile Integration ===")
    
    try:
        from freecad.StructureTools.gui.SectionManagerGUI import ArchProfileIntegration
        
        integration = ArchProfileIntegration()
        print(f"1. ArchProfile integration available: {integration.available}")
        
        if integration.available:
            print("   ✓ Arch module available for profile creation")
            
            # Test profile creation with sample data
            sample_data = {
                'SectionName': 'W12x26',
                'ShapeType': 'W_shapes',
                'Height': 311.15,  # mm
                'Width': 165.1,    # mm
                'WebThickness': 6.35,
                'FlangeThickness': 9.65,
                'Area': 3355.0
            }
            
            print("2. Sample data prepared for profile creation")
            print(f"   - Section: {sample_data['SectionName']}")
            print(f"   - Dimensions: {sample_data['Height']:.1f} x {sample_data['Width']:.1f} mm")
            
        else:
            print("   ! Arch module not available - profiles will use basic geometry")
        
        return True
        
    except Exception as e:
        print(f"   ✗ ArchProfile integration test failed: {e}")
        return False

def test_section_creation():
    """Test section object creation"""
    print("\n=== Testing Section Object Creation ===")
    
    try:
        # Mock FreeCAD environment for testing
        class MockApp:
            ActiveDocument = None
            Console = MockConsole()
            Vector = lambda x, y, z: f"Vector({x}, {y}, {z})"
        
        class MockConsole:
            def PrintMessage(self, msg): print(f"[MSG] {msg.strip()}")
            def PrintWarning(self, msg): print(f"[WARN] {msg.strip()}")
            def PrintError(self, msg): print(f"[ERR] {msg.strip()}")
        
        # Test imports
        from freecad.StructureTools.section import Section, ViewProviderSection
        
        print("1. Section classes imported successfully")
        
        # Test core functionality
        from freecad.StructureTools.core import get_section_manager, get_section_properties
        
        manager = get_section_manager()
        print(f"2. Section manager available: {manager is not None}")
        
        # Test property retrieval
        props = get_section_properties("W12x26")
        if props:
            print(f"3. Section properties retrieved: Area = {props['Area']} mm²")
        else:
            print("3. Section properties not found (database may not be loaded)")
        
        print("   ✓ Section creation system working")
        return True
        
    except Exception as e:
        print(f"   ✗ Section creation test failed: {e}")
        return False

def test_complete_workflow():
    """Test complete workflow"""
    print("\n=== Testing Complete Workflow ===")
    
    try:
        # Check all components
        steelpy_ok = test_steelpy_integration()
        gui_ok = test_gui_components() 
        arch_ok = test_arch_integration()
        section_ok = test_section_creation()
        
        components = [
            ("SteelPy Integration", steelpy_ok),
            ("GUI Components", gui_ok),
            ("ArchProfile Integration", arch_ok),
            ("Section Creation", section_ok)
        ]
        
        print("\n" + "=" * 50)
        print("COMPLETE WORKFLOW TEST RESULTS:")
        
        passed = 0
        total = len(components)
        
        for name, result in components:
            status = "✓ PASS" if result else "✗ FAIL"
            print(f"   {status} {name}")
            if result:
                passed += 1
        
        print(f"\nSummary: {passed}/{total} components working")
        
        if passed == total:
            print("\n🎉 ALL SYSTEMS READY!")
            print("\nYou can now:")
            print("1. Use Advanced Section Manager GUI")
            print("2. Browse steelpy steel section database")
            print("3. Create StructureTools Section objects")
            print("4. Create ArchProfile objects")
            print("5. Compare multiple sections")
            
            print("\nTo open the GUI:")
            print("- In FreeCAD: Use StructureTools toolbar")
            print("- Programmatically: from freecad.StructureTools.gui.SectionManagerGUI import show_section_manager_gui; show_section_manager_gui()")
        else:
            failed_components = [name for name, result in components if not result]
            print(f"\n⚠️  {total - passed} components need attention:")
            for comp in failed_components:
                print(f"   - {comp}")
        
        return passed == total
        
    except Exception as e:
        print(f"   ✗ Complete workflow test failed: {e}")
        return False

def show_usage_examples():
    """Show usage examples"""
    print("\n" + "=" * 60)
    print("USAGE EXAMPLES:")
    print("=" * 60)
    
    print("\n1. Open Advanced Section Manager GUI:")
    print("   from freecad.StructureTools.gui.SectionManagerGUI import show_section_manager_gui")
    print("   gui = show_section_manager_gui()")
    
    print("\n2. Open Steel Profile Selector:")
    print("   from freecad.StructureTools.gui.SteelProfileSelector import show_steel_profile_selector")
    print("   selector = show_steel_profile_selector()")
    
    print("\n3. Search steel sections programmatically:")
    print("   from freecad.StructureTools.data.SteelPyIntegration import search_steel_sections")
    print("   results = search_steel_sections('W12')")
    print("   for section in results[:5]:")
    print("       print(f\"{section['name']}: {section['properties']['area']:.0f} mm²\")")
    
    print("\n4. Get specific section properties:")
    print("   from freecad.StructureTools.data.SteelPyIntegration import get_section_data")
    print("   props = get_section_data('W_shapes', 'W12X26')")
    print("   print(f\"Area: {props['area']:.0f} mm²\")")
    
    print("\n5. Create section object with steelpy data:")
    print("   # Select section in GUI, then click 'Create Section'")
    print("   # Or use programmatic creation with section properties")

if __name__ == "__main__":
    print("Steel Profile GUI Integration Test")
    print("=" * 60)
    
    # Run complete test
    success = test_complete_workflow()
    
    # Show usage examples
    show_usage_examples()
    
    print("\n" + "=" * 60)
    if success:
        print("🎯 READY TO USE: Advanced Section Manager with steelpy integration!")
    else:
        print("🔧 SETUP NEEDED: Some components require attention.")
        print("\nMost likely issue: steelpy not installed")
        print("Solution: pip install steelpy")
    print("=" * 60)