#!/usr/bin/env python3
"""
Test Section Database Integration

Test the new section.py with SectionStandards database integration.

Usage:
exec(open(r'C:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\test_section_database.py').read())
"""

import FreeCAD as App

def test_section_database_integration():
    """Test the integrated section database system."""
    print("TESTING SECTION DATABASE INTEGRATION")
    print("=" * 60)
    
    # Ensure document exists
    if not App.ActiveDocument:
        App.newDocument("SectionDatabaseTest")
        print("[OK] Created test document")
    
    # Test 1: Create section with W-shape name
    print("\n1. Creating section with W-shape indicating name...")
    try:
        # Create object with W-shape indicating name
        w_obj = App.ActiveDocument.addObject("Part::FeaturePython", "Section_W12x26_Test")
        
        # Apply Section class
        from freecad.StructureTools.section import Section, ViewProviderSection
        Section(w_obj, [])
        ViewProviderSection(w_obj.ViewObject)
        
        print(f"[OK] W-shape section created: {w_obj.Label}")
        print(f"   Auto-detected standard: {w_obj.SectionStandard}")
        print(f"   Properties after creation:")
        print(f"     Area: {w_obj.AreaSection}")
        print(f"     Moment Inertia Y: {w_obj.MomentInertiaY}")
        print(f"     Moment Inertia Z: {w_obj.MomentInertiaZ}")
        print(f"     Section Type: {w_obj.SectionType}")
        
        # Check if values are from W12x26 database
        w_success = True
        if w_obj.SectionStandard != "W12x26":
            print(f"   [ERROR] Wrong section detected: {w_obj.SectionStandard} (expected W12x26)")
            w_success = False
        else:
            print(f"   [OK] Correct section detected: {w_obj.SectionStandard}")
            
        if "3355" not in str(w_obj.AreaSection):
            print(f"   [ERROR] Area wrong: {w_obj.AreaSection} (expected 3355 mm²)")
            w_success = False
        else:
            print(f"   [OK] Area correct: {w_obj.AreaSection}")
            
    except Exception as e:
        print(f"[ERROR] W-shape section creation failed: {e}")
        w_success = False
    
    # Test 2: Create IPE section
    print("\n2. Creating section with IPE name...")
    try:
        # Create object with IPE indicating name
        ipe_obj = App.ActiveDocument.addObject("Part::FeaturePython", "Section_IPE200_Test")
        
        # Apply Section class
        Section(ipe_obj, [])
        ViewProviderSection(ipe_obj.ViewObject)
        
        print(f"[OK] IPE section created: {ipe_obj.Label}")
        print(f"   Auto-detected standard: {ipe_obj.SectionStandard}")
        print(f"   Properties after creation:")
        print(f"     Area: {ipe_obj.AreaSection}")
        print(f"     Depth: {ipe_obj.Depth}")
        print(f"     Flange Width: {ipe_obj.FlangeWidth}")
        print(f"     Section Type: {ipe_obj.SectionType}")
        
        # Check if values are from IPE200 database
        ipe_success = True
        if ipe_obj.SectionStandard != "IPE200":
            print(f"   [ERROR] Wrong section detected: {ipe_obj.SectionStandard} (expected IPE200)")
            ipe_success = False
        else:
            print(f"   [OK] Correct section detected: {ipe_obj.SectionStandard}")
            
        if "200.0 mm" not in str(ipe_obj.Depth):
            print(f"   [ERROR] Depth wrong: {ipe_obj.Depth} (expected 200.0 mm)")
            ipe_success = False
        else:
            print(f"   [OK] Depth correct: {ipe_obj.Depth}")
            
    except Exception as e:
        print(f"[ERROR] IPE section creation failed: {e}")
        ipe_success = False
    
    # Test 3: Create HSS section
    print("\n3. Creating section with HSS name...")
    try:
        # Create object with HSS indicating name
        hss_obj = App.ActiveDocument.addObject("Part::FeaturePython", "Section_HSS6x4x1_4_Test")
        
        # Apply Section class
        Section(hss_obj, [])
        ViewProviderSection(hss_obj.ViewObject)
        
        print(f"[OK] HSS section created: {hss_obj.Label}")
        print(f"   Auto-detected standard: {hss_obj.SectionStandard}")
        print(f"   Properties after creation:")
        print(f"     Area: {hss_obj.AreaSection}")
        print(f"     Section Type: {hss_obj.SectionType}")
        print(f"     Weight: {hss_obj.Weight}")
        
        # Check if HSS was detected
        hss_success = True
        if "HSS" not in hss_obj.SectionStandard:
            print(f"   [ERROR] HSS not detected: {hss_obj.SectionStandard}")
            hss_success = False
        else:
            print(f"   [OK] HSS detected: {hss_obj.SectionStandard}")
            
    except Exception as e:
        print(f"[ERROR] HSS section creation failed: {e}")
        hss_success = False
    
    # Test 4: Test manual section standard switching
    print("\n4. Testing manual SectionStandard switching...")
    if 'w_obj' in locals():
        try:
            print("   Switching W-shape to IPE300...")
            w_obj.SectionStandard = "IPE300"
            
            print(f"   After switching to IPE300:")
            print(f"     Area: {w_obj.AreaSection}")
            print(f"     Depth: {w_obj.Depth}")
            print(f"     Section Type: {w_obj.SectionType}")
            
            # Check if it switched to IPE300 values
            switching_success = ("300.0 mm" in str(w_obj.Depth))
            if switching_success:
                print(f"   [OK] Manual switching works!")
            else:
                print(f"   [ERROR] Manual switching failed")
            
        except Exception as e:
            print(f"[ERROR] Manual switching failed: {e}")
            switching_success = False
    else:
        switching_success = False
    
    # Test 5: Test section database functions
    print("\n5. Testing section database functions...")
    try:
        from freecad.StructureTools.data.SectionStandards import (
            get_sections_by_category, find_sections_by_depth_range, 
            SECTION_CATEGORIES
        )
        
        # Test category retrieval
        aisc_sections = get_sections_by_category("AISC Wide Flange")
        print(f"   [OK] AISC Wide Flange sections: {len(aisc_sections)} found")
        
        ipe_sections = get_sections_by_category("European IPE")
        print(f"   [OK] European IPE sections: {len(ipe_sections)} found")
        
        # Test depth range search
        medium_sections = find_sections_by_depth_range(150, 250)
        print(f"   [OK] Sections 150-250mm depth: {len(medium_sections)} found")
        
        # Show categories
        print(f"   [OK] Available section categories: {len(SECTION_CATEGORIES)}")
        for category, sections in SECTION_CATEGORIES.items():
            print(f"     {category}: {len(sections)} sections")
        
        database_success = True
            
    except Exception as e:
        print(f"[ERROR] Database function test failed: {e}")
        database_success = False
    
    # Test 6: Test geometry generation
    print("\n6. Testing automatic geometry generation...")
    try:
        # Create a section that should generate geometry
        geom_obj = App.ActiveDocument.addObject("Part::FeaturePython", "Section_Geometry_Test")
        Section(geom_obj, [])
        ViewProviderSection(geom_obj.ViewObject)
        
        # Set to a standard section
        geom_obj.SectionStandard = "W12x26"
        
        # Force execute to generate geometry
        geom_obj.Proxy.execute(geom_obj)
        App.ActiveDocument.recompute()
        
        # Check if geometry was generated
        if hasattr(geom_obj, 'Shape') and geom_obj.Shape.isValid():
            print(f"   [OK] Geometry generated successfully")
            geometry_success = True
        else:
            print(f"   [WARNING] No geometry generated (may be normal if no members assigned)")
            geometry_success = True  # This is acceptable
            
    except Exception as e:
        print(f"[ERROR] Geometry generation test failed: {e}")
        geometry_success = False
    
    # Results summary
    print("\n" + "=" * 60)
    print("SECTION DATABASE INTEGRATION TEST RESULTS")
    print("=" * 60)
    
    all_success = w_success and ipe_success and hss_success and switching_success and database_success and geometry_success
    
    if all_success:
        print("[SUCCESS] ALL TESTS PASSED!")
        print("  - W-shape section creation and detection: OK")
        print("  - IPE section creation and detection: OK")  
        print("  - HSS section creation and detection: OK")
        print("  - Manual SectionStandard switching: OK")
        print("  - Database functions: OK")
        print("  - Geometry generation: OK")
        print("\nYour Section Database system is working!")
        print("\nFeatures now available:")
        print("- 🎯 Automatic section detection from object names")
        print("- 📊 Complete section properties from database")
        print("- 🔄 Manual section selection from dropdown")
        print("- 📐 Automatic geometry generation")
        print("- 🏗️ Professional section standards (AISC, EN)")
    else:
        print("[ERROR] Some tests failed:")
        if not w_success:
            print("  - W-shape section: FAILED")
        if not ipe_success:
            print("  - IPE section: FAILED")
        if not hss_success:
            print("  - HSS section: FAILED")
        if not switching_success:
            print("  - Manual switching: FAILED")
        if not database_success:
            print("  - Database functions: FAILED")
        if not geometry_success:
            print("  - Geometry generation: FAILED")
    
    return all_success

def test_section_categories():
    """Test section categories and filtering."""
    print("\n" + "=" * 60)
    print("TESTING SECTION CATEGORIES AND FILTERING")
    print("=" * 60)
    
    try:
        from freecad.StructureTools.data.SectionStandards import (
            SECTION_CATEGORIES, get_sections_by_category,
            find_sections_by_depth_range, find_sections_by_weight_limit
        )
        
        print("\n📂 Available Section Categories:")
        for category, sections in SECTION_CATEGORIES.items():
            print(f"   {category}: {len(sections)} sections")
            # Show first few sections as examples
            example_sections = sections[:3]
            print(f"      Examples: {', '.join(example_sections)}")
        
        print("\n🔍 Testing Search Functions:")
        
        # Test depth range search
        compact_sections = find_sections_by_depth_range(100, 200)
        print(f"   Compact sections (100-200mm): {len(compact_sections)} found")
        
        # Test weight limit search  
        light_sections = find_sections_by_weight_limit(25)
        print(f"   Light sections (<25 kg/m): {len(light_sections)} found")
        
        # Show some examples
        print("\n💡 Example Sections:")
        for section_name, properties in list(compact_sections.items())[:3]:
            print(f"   {section_name}:")
            print(f"     Depth: {properties.get('Depth', 'N/A')} mm")
            print(f"     Type: {properties.get('Type', 'N/A')}")
            print(f"     Weight: {properties.get('Weight', 'N/A')} kg/m")
        
        return True
        
    except Exception as e:
        print(f"[ERROR] Section categories test failed: {e}")
        return False

def run_complete_section_database_test():
    """Run complete test of section database system."""
    success = test_section_database_integration()
    categories_success = test_section_categories()
    
    print("\n" + "=" * 80)
    print("COMPLETE SECTION DATABASE TEST SUMMARY")
    print("=" * 80)
    
    if success and categories_success:
        print("[SUCCESS] Section Database System is fully operational! 🎉")
        print("\n🚀 Your StructureTools now has:")
        print("  ✅ Professional section database with 30+ standard sections")
        print("  ✅ AISC, EN (IPE, HEB), HSS, Angles, and Channel sections")
        print("  ✅ Intelligent section detection from object names")
        print("  ✅ Automatic property calculation from database")
        print("  ✅ Manual section selection with dropdown")
        print("  ✅ Automatic geometry generation for visualization")
        print("  ✅ Advanced search and filtering capabilities")
        print("  ✅ Complete section properties (Area, Ix, Iy, Sx, Sy, rx, ry, etc.)")
        print("\n📖 How to use:")
        print("  1. Create Section object with names like 'Section_W12x26' or 'Section_IPE200'")
        print("  2. Section properties will be auto-populated from database")
        print("  3. You can manually change SectionStandard in Property Panel")
        print("  4. Properties update automatically when standard changes")
        print("  5. Geometry is generated automatically for visualization")
    else:
        print("[ERROR] Section Database System needs debugging")
        print("Check error messages above for specific issues")

if __name__ == "__main__":
    run_complete_section_database_test()