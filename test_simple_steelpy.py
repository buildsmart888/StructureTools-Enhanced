# -*- coding: utf-8 -*-
"""
Simple SteelPy Integration Test
การทดสอบ steelpy integration แบบง่าย
"""

def test_steelpy_import():
    """Test steelpy import"""
    print("Testing steelpy import...")
    
    try:
        import steelpy
        from steelpy import aisc
        print("[OK] steelpy imported successfully")
        
        # Test basic access
        try:
            w_shapes = aisc.W_shapes
            print("[OK] AISC W_shapes accessible")
            
            # Get first W section
            first_section = getattr(w_shapes, 'W10X12', None)
            if first_section:
                print(f"[OK] Sample section W10X12:")
                print(f"    Area: {first_section.A:.2f} in²")
                print(f"    Weight: {first_section.W:.2f} lb/ft")
                print(f"    Height: {first_section.d:.2f} in")
                print(f"    Width: {first_section.bf:.2f} in")
            else:
                print("[INFO] W10X12 not found, trying other sections...")
                
                # Try to get any section
                for attr in dir(w_shapes):
                    if not attr.startswith('_'):
                        section = getattr(w_shapes, attr)
                        print(f"[OK] Sample section {attr}:")
                        if hasattr(section, 'A'):
                            print(f"    Area: {section.A:.2f} in²")
                        if hasattr(section, 'W'):
                            print(f"    Weight: {section.W:.2f} lb/ft")
                        break
            
            return True
            
        except Exception as e:
            print(f"[ERROR] Failed to access AISC data: {e}")
            return False
            
    except ImportError:
        print("[WARNING] steelpy not installed")
        print("To install: pip install steelpy")
        return False
    except Exception as e:
        print(f"[ERROR] steelpy import failed: {e}")
        return False

def test_integration_module():
    """Test our integration module"""
    print("\nTesting integration module...")
    
    try:
        from freecad.StructureTools.data.SteelPyIntegration import STEELPY_AVAILABLE
        print(f"[INFO] STEELPY_AVAILABLE: {STEELPY_AVAILABLE}")
        
        if STEELPY_AVAILABLE:
            from freecad.StructureTools.data.SteelPyIntegration import (
                get_available_shape_types,
                get_sections_for_shape,
                get_section_data
            )
            
            print("[OK] Integration functions imported")
            
            # Test getting shape types
            try:
                shape_types = get_available_shape_types()
                print(f"[OK] Shape types loaded: {len(shape_types)} types")
                
                for shape_key, info in list(shape_types.items())[:3]:
                    print(f"    {shape_key}: {info['name']} ({info['count']} sections)")
                
                # Test getting sections for W_shapes
                if 'W_shapes' in shape_types:
                    sections = get_sections_for_shape('W_shapes')
                    print(f"[OK] W_shapes sections: {len(sections)} found")
                    
                    # Test getting specific section data
                    if sections:
                        test_section = sections[0]
                        section_data = get_section_data('W_shapes', test_section)
                        
                        if section_data:
                            print(f"[OK] Sample section data for {test_section}:")
                            print(f"    Area: {section_data.get('area', 0):.0f} mm²")
                            print(f"    Weight: {section_data.get('weight', 0):.2f} kg/m")
                
                return True
                
            except Exception as e:
                print(f"[ERROR] Integration functions failed: {e}")
                return False
        else:
            print("[WARNING] steelpy not available for integration")
            return False
        
    except ImportError as e:
        print(f"[ERROR] Integration module import failed: {e}")
        return False
    except Exception as e:
        print(f"[ERROR] Integration test failed: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality without GUI"""
    print("\nTesting basic functionality...")
    
    try:
        # Test mock environment
        print("[OK] Basic Python environment working")
        
        # Test file structure
        import os
        current_dir = os.path.dirname(__file__)
        gui_dir = os.path.join(current_dir, 'freecad', 'StructureTools', 'gui')
        data_dir = os.path.join(current_dir, 'freecad', 'StructureTools', 'data')
        
        print(f"[INFO] GUI directory exists: {os.path.exists(gui_dir)}")
        print(f"[INFO] Data directory exists: {os.path.exists(data_dir)}")
        
        # List key files
        key_files = [
            'freecad/StructureTools/gui/SectionManagerGUI.py',
            'freecad/StructureTools/gui/SteelProfileSelector.py',
            'freecad/StructureTools/data/SteelPyIntegration.py',
            'freecad/StructureTools/commands/advanced_section_manager.py'
        ]
        
        for file_path in key_files:
            full_path = os.path.join(current_dir, file_path)
            exists = os.path.exists(full_path)
            print(f"[INFO] {file_path}: {'EXISTS' if exists else 'MISSING'}")
        
        return True
        
    except Exception as e:
        print(f"[ERROR] Basic functionality test failed: {e}")
        return False

def main():
    """Main test function"""
    print("Advanced Section Manager Integration Test")
    print("=" * 50)
    
    # Run tests
    steelpy_ok = test_steelpy_import()
    integration_ok = test_integration_module()
    basic_ok = test_basic_functionality()
    
    print("\n" + "=" * 50)
    print("TEST RESULTS:")
    
    results = [
        ("SteelPy Import", steelpy_ok),
        ("Integration Module", integration_ok),
        ("Basic Functionality", basic_ok)
    ]
    
    passed = 0
    total = len(results)
    
    for name, result in results:
        status = "PASS" if result else "FAIL"
        symbol = "[OK]" if result else "[FAIL]"
        print(f"  {symbol} {name}: {status}")
        if result:
            passed += 1
    
    print(f"\nSummary: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n[SUCCESS] Ready for FreeCAD integration!")
        print("\nNext steps:")
        print("1. Install steelpy: pip install steelpy")
        print("2. Open FreeCAD and load StructureTools workbench")
        print("3. Look for 'Advanced Section Manager' button in toolbar")
    else:
        print(f"\n[WARNING] {total-passed} test(s) failed")
        if not steelpy_ok:
            print("- Install steelpy: pip install steelpy")
        if not integration_ok:
            print("- Check integration module implementation")
        if not basic_ok:
            print("- Check file structure and paths")
    
    print("\n" + "=" * 50)
    print("FEATURE OVERVIEW:")
    print("1. Advanced Section Manager GUI with database browser")
    print("2. Steel section database from steelpy (1000+ AISC sections)")
    print("3. Property filtering and search capabilities")
    print("4. Section comparison tools")
    print("5. ArchProfile integration for 3D modeling")
    print("6. Direct creation of StructureTools Section objects")

if __name__ == "__main__":
    main()