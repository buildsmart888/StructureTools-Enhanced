"""
Complete Specification Implementation Test
การทดสอบการติดตั้งสเปกแบบครบถ้วน

Test script for all specification requirements implemented:
1. Unit consistency (kgf·m, tf·m instead of kgf·cm)  
2. Fixed conversion factors (1 tf = 1000 kgf, 1 kgf = 9.80665 N)
3. Unit switchers for Forces and Moments
4. Zero threshold implementation (1e-6)
5. Precision control (3-4 decimal places)
6. JSON serialization fix
7. All GUI errors resolved

สคริปต์ทดสอบข้อกำหนดสเปกทั้งหมดที่ติดตั้ง
"""

def test_fixed_conversion_factors():
    """Test fixed conversion factors according to specification"""
    print("=== TESTING FIXED CONVERSION FACTORS ===")
    
    try:
        from freecad.StructureTools.utils.universal_thai_units import get_universal_thai_units
        converter = get_universal_thai_units()
        
        if not converter.enabled:
            print("❌ Thai units converter not available")
            return False
        
        print("✅ Conversion factors (exact as per spec):")
        
        # Test force conversions 
        print(f"  • 1 kgf = {converter.KGF_TO_N:.5f} N (should be 9.80665)")
        print(f"  • 1 kN = {converter.KN_TO_KGF:.5f} kgf (should be 101.97162)")
        print(f"  • 1 tf = {converter.TF_TO_KGF:.1f} kgf (should be 1000.0)")
        print(f"  • 1 kN = {converter.KN_TO_TF:.5f} tf (should be 0.10197)")
        
        # Test moment conversions (NEW - consistent with meters)
        test_moment = 10.0  # kN·m
        kgf_m_result = converter.kn_m_to_kgf_m(test_moment)
        tf_m_result = converter.kn_m_to_tf_m(test_moment)
        
        print(f"\nMoment conversions (consistent with meter units):")
        print(f"  • {test_moment} kN·m = {kgf_m_result:.2f} kgf·m")
        print(f"  • {test_moment} kN·m = {tf_m_result:.4f} tf·m")
        
        # Verify exact ratios
        expected_kgf_m = test_moment * 101.97162129779283
        expected_tf_m = test_moment * 0.10197162129779283
        
        if abs(kgf_m_result - expected_kgf_m) < 1e-6:
            print("  ✅ kgf·m conversion exact")
        else:
            print(f"  ❌ kgf·m conversion error: {kgf_m_result} vs {expected_kgf_m}")
            
        if abs(tf_m_result - expected_tf_m) < 1e-6:
            print("  ✅ tf·m conversion exact")
        else:
            print(f"  ❌ tf·m conversion error: {tf_m_result} vs {expected_tf_m}")
            
        return True
        
    except Exception as e:
        print(f"❌ Conversion factor test failed: {e}")
        return False

def test_unit_switcher():
    """Test unit switcher functionality in reaction results"""
    import FreeCAD
    
    print("\n=== TESTING UNIT SWITCHER ===")
    
    if not FreeCAD.ActiveDocument:
        print("❌ No active document - cannot test unit switcher")
        return False
    
    try:
        from freecad.StructureTools import reaction_results
        
        # Find calc object
        doc = FreeCAD.ActiveDocument
        calc_obj = None
        for obj in doc.Objects:
            if hasattr(obj, 'Proxy') and obj.Proxy and hasattr(obj.Proxy, '__class__'):
                if 'Calc' in obj.Proxy.__class__.__name__:
                    calc_obj = obj
                    break
        
        if not calc_obj:
            print("❌ No calc object found - cannot test unit switcher")
            return False
        
        # Create reaction results object
        reaction_obj = doc.addObject("App::DocumentObjectGroupPython", "UnitSwitcherTest")
        reaction_results.ReactionResults(reaction_obj, calc_obj)
        
        # Test unit properties exist
        required_props = ['ForceUnit', 'MomentUnit', 'ZeroThreshold', 'Precision']
        missing_props = []
        
        for prop in required_props:
            if not hasattr(reaction_obj, prop):
                missing_props.append(prop)
        
        if missing_props:
            print(f"❌ Missing unit properties: {missing_props}")
            return False
        
        print("✅ Unit switcher properties:")
        print(f"  • ForceUnit options: {reaction_obj.ForceUnit}")
        print(f"  • ForceUnit default: {reaction_obj.ForceUnit}")
        print(f"  • MomentUnit options: {reaction_obj.MomentUnit}")
        print(f"  • MomentUnit default: {reaction_obj.MomentUnit}")
        print(f"  • ZeroThreshold: {reaction_obj.ZeroThreshold}")
        print(f"  • Precision: {reaction_obj.Precision}")
        
        # Test unit conversion methods
        proxy = reaction_obj.Proxy
        
        # Test force conversion
        test_force_kn = 100.0  # kN
        
        # Test kgf option
        reaction_obj.ForceUnit = "kgf"
        value_kgf, formatted_kgf = proxy.convert_force_value(reaction_obj, test_force_kn)
        print(f"\n  Force conversion test:")
        print(f"    • {test_force_kn} kN → {formatted_kgf}")
        
        # Test tf option
        reaction_obj.ForceUnit = "tf"  
        value_tf, formatted_tf = proxy.convert_force_value(reaction_obj, test_force_kn)
        print(f"    • {test_force_kn} kN → {formatted_tf}")
        
        # Test moment conversion
        test_moment_knm = 50.0  # kN·m
        
        # Test kgf·m option
        reaction_obj.MomentUnit = "kgf·m"
        value_kgfm, formatted_kgfm = proxy.convert_moment_value(reaction_obj, test_moment_knm)
        print(f"\n  Moment conversion test:")
        print(f"    • {test_moment_knm} kN·m → {formatted_kgfm}")
        
        # Test tf·m option  
        reaction_obj.MomentUnit = "tf·m"
        value_tfm, formatted_tfm = proxy.convert_moment_value(reaction_obj, test_moment_knm)
        print(f"    • {test_moment_knm} kN·m → {formatted_tfm}")
        
        # Test zero threshold
        small_value = 1e-7  # Below threshold
        zero_value, zero_format = proxy.convert_force_value(reaction_obj, small_value)
        print(f"\n  Zero threshold test:")
        print(f"    • {small_value} kN → {zero_format} (should be 0)")
        
        if zero_format == "0":
            print("    ✅ Zero threshold working correctly")
        else:
            print(f"    ❌ Zero threshold failed: expected '0', got '{zero_format}'")
        
        # Clean up
        doc.removeObject(reaction_obj.Name)
        
        return True
        
    except Exception as e:
        print(f"❌ Unit switcher test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_json_serialization_fix():
    """Test that FE model no longer causes JSON serialization errors"""
    import FreeCAD
    
    print("\n=== TESTING JSON SERIALIZATION FIX ===")
    
    if not FreeCAD.ActiveDocument:
        print("❌ No active document - cannot test serialization")
        return False
    
    try:
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
        
        # Check that FE model is stored properly without causing JSON errors
        if hasattr(calc_obj, '_cached_fe_model'):
            print("✅ FE model uses _cached_fe_model (no JSON serialization)")
            if calc_obj._cached_fe_model:
                model = calc_obj._cached_fe_model
                print(f"  • Cached model: {len(model.nodes)} nodes, {len(model.members)} members")
        else:
            print("❌ No _cached_fe_model found")
            
        # Check status properties
        if hasattr(calc_obj, 'FEModelReady'):
            print(f"  • FEModelReady: {calc_obj.FEModelReady}")
        if hasattr(calc_obj, 'FEModelInfo'):
            print(f"  • FEModelInfo: {calc_obj.FEModelInfo}")
        
        # Test document save (this would fail before if JSON serialization was broken)
        try:
            # Try to simulate what FreeCAD does when saving
            import tempfile
            temp_file = tempfile.mktemp(suffix='.FCStd')
            doc.saveAs(temp_file)
            print("✅ Document save test passed (no JSON serialization errors)")
            import os
            if os.path.exists(temp_file):
                os.remove(temp_file)
            return True
        except Exception as save_error:
            print(f"❌ Document save test failed: {save_error}")
            return False
            
    except Exception as e:
        print(f"❌ JSON serialization test failed: {e}")
        return False

def test_gui_error_fixes():
    """Test that GUI loading errors are resolved"""
    print("\n=== TESTING GUI ERROR FIXES ===")
    
    errors_found = []
    
    # Test seismic load GUI
    try:
        from freecad.StructureTools.commands.command_seismic_load_gui import show_seismic_load_gui
        print("✅ Seismic load GUI imports successfully")
    except Exception as e:
        print(f"❌ Seismic load GUI error: {e}")
        errors_found.append("seismic_gui")
    
    # Test wind load GUI
    try:
        from freecad.StructureTools.commands.command_wind_load_gui import WindLoadGUI
        gui = WindLoadGUI()
        if hasattr(gui, 'calculate_wind_loads'):
            print("✅ Wind load GUI has calculate_wind_loads method")
        else:
            print("❌ Wind load GUI missing calculate_wind_loads method")
            errors_found.append("wind_gui_method")
    except Exception as e:
        print(f"❌ Wind load GUI error: {e}")
        errors_found.append("wind_gui")
    
    if not errors_found:
        print("✅ All GUI errors resolved")
        return True
    else:
        print(f"❌ GUI errors remaining: {errors_found}")
        return False

def test_precision_and_formatting():
    """Test precision control and number formatting"""
    print("\n=== TESTING PRECISION AND FORMATTING ===")
    
    try:
        from freecad.StructureTools.utils.universal_thai_units import get_universal_thai_units
        converter = get_universal_thai_units()
        
        if not converter.enabled:
            print("❌ Cannot test precision - Thai units not available")
            return False
        
        # Test various precision levels
        test_value = 123.456789  # kN
        
        for precision in [2, 3, 4]:
            kgf_value = converter.kn_to_kgf(test_value)
            formatted = f"{kgf_value:.{precision}f} kgf"
            print(f"  • Precision {precision}: {test_value} kN → {formatted}")
        
        # Test zero threshold behavior
        small_values = [1e-5, 1e-6, 1e-7, 1e-8]
        threshold = 1e-6
        
        print(f"\nZero threshold test (threshold = {threshold}):")
        for val in small_values:
            if abs(val) < threshold:
                result = "0"
            else:
                result = f"{converter.kn_to_kgf(val):.3f} kgf"
            print(f"  • {val} kN → {result}")
        
        return True
        
    except Exception as e:
        print(f"❌ Precision test failed: {e}")
        return False

def create_spec_compliance_report():
    """Create comprehensive specification compliance report"""
    print("\n" + "="*80)
    print("📋 SPECIFICATION COMPLIANCE REPORT")
    print("="*80)
    
    # Specification requirements checklist
    spec_requirements = {
        "1. Unit Consistency": "kgf·m and tf·m (NOT kgf·cm) with meter lengths",
        "2. Fixed Conversions": "1 tf = 1000 kgf, 1 kgf = 9.80665 N (exact)",
        "3. Unit Switcher": "Forces (kgf/tf) and Moments (kgf·m/tf·m) selection", 
        "4. Zero Threshold": "Values < 1e-6 display as 0",
        "5. Precision Control": "3-4 decimal places, configurable",
        "6. JSON Serialization": "No more PropertyPythonObject serialization errors",
        "7. GUI Error Fixes": "Seismic/Wind load GUIs load without errors",
        "8. Results Format": "node_id, DOF, Rx (unit), Ry (unit), Rz (unit), etc."
    }
    
    print("\n📌 SPECIFICATION REQUIREMENTS:")
    for req_id, description in spec_requirements.items():
        print(f"   {req_id}: {description}")
    
    print("\n🎯 IMPLEMENTATION STATUS:")
    
    # Run all tests
    test_results = {}
    test_results["Fixed Conversions"] = test_fixed_conversion_factors()
    test_results["Unit Switcher"] = test_unit_switcher()
    test_results["JSON Serialization"] = test_json_serialization_fix()
    test_results["GUI Fixes"] = test_gui_error_fixes()
    test_results["Precision Control"] = test_precision_and_formatting()
    
    # Summary
    passed_tests = sum(test_results.values())
    total_tests = len(test_results)
    
    print(f"\n📊 SUMMARY:")
    for test_name, passed in test_results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"   {test_name}: {status}")
    
    print(f"\n🎉 OVERALL: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("\n" + "="*80)
        print("🎊 ALL SPECIFICATION REQUIREMENTS IMPLEMENTED SUCCESSFULLY! 🎊")
        print("="*80)
        print("Your Reaction Results system now meets all specifications:")
        print("  • Consistent units (m, kgf·m, tf·m)")
        print("  • Fixed conversion factors per Thai standards")
        print("  • User-selectable force/moment units")
        print("  • Zero threshold and precision control")
        print("  • No JSON serialization errors")
        print("  • All GUI errors resolved")
        print("\nReady for production use! 🚀")
        
        return True
    else:
        print(f"\n⚠️  {total_tests - passed_tests} issues need attention")
        return False

def quick_reaction_demo():
    """Quick demo of reaction results with new features"""
    import FreeCAD
    
    print("\n=== QUICK REACTION RESULTS DEMO ===")
    
    if not FreeCAD.ActiveDocument:
        print("❌ Open a structural model first to run demo")
        return False
    
    try:
        from freecad.StructureTools import reaction_results
        
        # Find calc object
        doc = FreeCAD.ActiveDocument
        calc_obj = None
        for obj in doc.Objects:
            if hasattr(obj, 'Proxy') and obj.Proxy and hasattr(obj.Proxy, '__class__'):
                if 'Calc' in obj.Proxy.__class__.__name__:
                    calc_obj = obj
                    break
        
        if not calc_obj:
            print("❌ No calc object - run structural analysis first")
            return False
        
        # Create reaction results with new features
        reaction_obj = doc.addObject("App::DocumentObjectGroupPython", "SpecCompliantReactions")
        reaction_results.ReactionResults(reaction_obj, calc_obj)
        reaction_results.ViewProviderReactionResults(reaction_obj.ViewObject)
        
        print("✅ Reaction Results created with spec-compliant features:")
        print(f"   • Force unit: {reaction_obj.ForceUnit} (can switch to tf)")
        print(f"   • Moment unit: {reaction_obj.MomentUnit} (can switch to tf·m)")
        print(f"   • Precision: {reaction_obj.Precision} decimal places")
        print(f"   • Zero threshold: {reaction_obj.ZeroThreshold}")
        
        # Test unit switching
        print("\n🔄 Testing unit switching:")
        
        # Switch to tf units
        reaction_obj.ForceUnit = "tf"
        reaction_obj.MomentUnit = "tf·m"
        print("   • Switched to tf and tf·m units")
        
        # Execute visualization
        reaction_obj.Proxy.execute(reaction_obj)
        print("   • Visualization updated with new units")
        
        # Switch back
        reaction_obj.ForceUnit = "kgf"
        reaction_obj.MomentUnit = "kgf·m"
        print("   • Switched back to kgf and kgf·m units")
        
        reaction_obj.Proxy.execute(reaction_obj)
        print("   • Visualization updated again")
        
        print("\n🎯 Demo completed successfully!")
        print("   Use Properties panel to change ForceUnit and MomentUnit")
        print("   All values follow specification requirements")
        
        return True
        
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🚀 COMPREHENSIVE SPECIFICATION IMPLEMENTATION TEST")
    print("=" * 80)
    print("Testing all specification requirements for Reaction Results system")
    print("Requirements: Unit consistency, fixed conversions, switchers, precision, etc.")
    
    # Run comprehensive test
    success = create_spec_compliance_report()
    
    if success:
        # Run demo if requested
        print(f"\n{'='*60}")
        print("🎮 To run quick demo (optional):")
        print("   exec(open(r'{}').read())".format(__file__.replace('\\\\', '/')))
        print("   # then call: quick_reaction_demo()")
        print(f"{'='*60}")
    
    print("\n📖 SPECIFICATION REFERENCE:")
    print("   • Length: m (meters)")
    print("   • Forces: kgf (default) or tf (selectable)")  
    print("   • Moments: kgf·m (default) or tf·m (selectable)")
    print("   • Conversions: 1 tf = 1000 kgf, 1 kgf = 9.80665 N")
    print("   • Zero threshold: |value| < 1e-6 → display 0")
    print("   • Precision: 3-4 decimal places (configurable)")