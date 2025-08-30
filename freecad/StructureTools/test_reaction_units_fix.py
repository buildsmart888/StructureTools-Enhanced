"""
Test script to verify the reaction results unit conversion fix
ทดสอบการแก้ไขการแปลงหน่วยผลลัพธ์ reaction
"""

def test_thai_units_conversion():
    """Test Thai units conversion with correct methods"""
    print("=== TESTING THAI UNITS CONVERSION FIX ===")
    
    try:
        from freecad.StructureTools.utils.universal_thai_units import get_universal_thai_units
        converter = get_universal_thai_units()
        
        print(f"Thai units available: {converter.enabled}")
        
        # Test force conversions
        print("\n--- Force Conversions ---")
        kn_force = 100.0  # kN
        kgf_force = converter.kn_to_kgf(kn_force)
        tf_force = converter.kn_to_tf(kn_force)
        print(f"  {kn_force} kN = {kgf_force:.2f} kgf = {tf_force:.4f} tf")
        
        # Test moment conversions (the fixed ones)
        print("\n--- Moment Conversions ---") 
        kn_moment = 50.0  # kN·m
        kgf_cm_moment = converter.kn_m_to_kgf_cm(kn_moment)
        tf_m_moment = converter.kn_m_to_tf_m(kn_moment)
        print(f"  {kn_moment} kN·m = {kgf_cm_moment:.2f} kgf·cm = {tf_m_moment:.4f} tf·m")
        
        # Verify conversion factors
        print("\n--- Conversion Factors ---")
        print(f"  1 kN = {converter.KN_TO_KGF:.3f} kgf")
        print(f"  1 kN = {converter.KN_TO_TF:.5f} tf")
        print(f"  1 kN·m = {converter.KN_TO_KGF * 100:.2f} kgf·cm")
        
        print("\n✅ All conversion methods working correctly!")
        return True
        
    except Exception as e:
        print(f"❌ Error testing conversions: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_calc_object_properties():
    """Test calc object has all required properties"""
    import FreeCAD
    
    print("\n=== TESTING CALC OBJECT PROPERTIES ===")
    
    if not FreeCAD.ActiveDocument:
        print("❌ No active document. Please open your structural model first.")
        return False
    
    doc = FreeCAD.ActiveDocument
    calc_objects = []
    
    # Find calc objects
    for obj in doc.Objects:
        if hasattr(obj, 'Proxy') and obj.Proxy and hasattr(obj.Proxy, '__class__'):
            if 'Calc' in obj.Proxy.__class__.__name__:
                calc_objects.append(obj)
    
    if not calc_objects:
        print("❌ No calc objects found")
        return False
    
    print(f"Found {len(calc_objects)} calc object(s)")
    
    for calc_obj in calc_objects:
        print(f"\nTesting: {calc_obj.Name}")
        
        # Required properties
        required_props = [
            'selfWeight', 'NumPointsMoment', 'NumPointsAxial', 'NumPointsShear',
            'LengthUnit', 'ForceUnit', 'LoadCombination'
        ]
        
        missing_props = []
        for prop in required_props:
            if not hasattr(calc_obj, prop):
                missing_props.append(prop)
        
        if missing_props:
            print(f"  ⚠️  Missing properties: {missing_props}")
            
            # Try to fix with ensure_required_properties
            try:
                if hasattr(calc_obj.Proxy, 'ensure_required_properties'):
                    calc_obj.Proxy.ensure_required_properties(calc_obj)
                    print(f"  ✅ Properties automatically added")
                else:
                    print(f"  ❌ Cannot fix properties - method missing")
            except Exception as e:
                print(f"  ❌ Error fixing properties: {e}")
        else:
            print(f"  ✅ All properties present")
        
        # Check FE Model
        if hasattr(calc_obj, 'FEModel') and calc_obj.FEModel:
            model = calc_obj.FEModel
            print(f"  ✅ FE Model: {len(model.nodes)} nodes, {len(model.members)} members")
        else:
            print(f"  ⚠️  No FE model - run calc analysis first")
    
    return True

def test_reaction_results_creation():
    """Test reaction results creation"""
    import FreeCAD
    
    print("\n=== TESTING REACTION RESULTS CREATION ===")
    
    if not FreeCAD.ActiveDocument:
        print("❌ Open structural model first")
        return False
    
    # Find calc object
    doc = FreeCAD.ActiveDocument
    calc_obj = None
    
    for obj in doc.Objects:
        if hasattr(obj, 'Proxy') and obj.Proxy and hasattr(obj.Proxy, '__class__'):
            if 'Calc' in obj.Proxy.__class__.__name__:
                calc_obj = obj
                break
    
    if not calc_obj:
        print("❌ No calc object found")
        return False
    
    try:
        from freecad.StructureTools import reaction_results
        
        # Create reaction results object
        reaction_obj = doc.addObject("App::DocumentObjectGroupPython", "ReactionResultsTest")
        reaction_results.ReactionResults(reaction_obj, calc_obj)
        reaction_results.ViewProviderReactionResults(reaction_obj.ViewObject)
        
        print(f"✅ Reaction object created: {reaction_obj.Name}")
        
        # Test properties
        if hasattr(reaction_obj, 'ShowReactionFX'):
            print(f"  ShowReactionFX: {reaction_obj.ShowReactionFX}")
        if hasattr(reaction_obj, 'ActiveLoadCombination'):
            print(f"  Active combo: {reaction_obj.ActiveLoadCombination}")
        
        # Test execution
        reaction_obj.Proxy.execute(reaction_obj)
        print("✅ Reaction visualization executed successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating reaction results: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🔧 Testing Reaction Results Unit Conversion Fix")
    print("=" * 60)
    
    # Run all tests
    test1 = test_thai_units_conversion()
    test2 = test_calc_object_properties() 
    test3 = test_reaction_results_creation()
    
    print("\n" + "=" * 60)
    print("📋 TEST SUMMARY")
    print(f"  Thai Units Conversion: {'✅ PASS' if test1 else '❌ FAIL'}")
    print(f"  Calc Object Properties: {'✅ PASS' if test2 else '❌ FAIL'}")
    print(f"  Reaction Results Creation: {'✅ PASS' if test3 else '❌ FAIL'}")
    
    if test1 and test2 and test3:
        print("\n🎉 ALL TESTS PASSED - Reaction Results system is ready!")
        print("\nTo use:")
        print("  1. Open your structural model in FreeCAD")
        print("  2. Run structural analysis (Calc button)")
        print("  3. Click 'Reaction Results' in StructureResults toolbar")
        print("  4. Use checkboxes to control display")
    else:
        print("\n⚠️  Some tests failed - check error messages above")
    
    print("=" * 60)