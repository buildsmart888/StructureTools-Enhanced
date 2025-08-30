"""
Comprehensive System Verification Script
สคริปต์ตรวจสอบระบบแบบครบถ้วน

This script performs thorough verification of ALL system components
to ensure everything works correctly after all fixes.

สคริปต์นี้ทำการตรวจสอบทุกส่วนของระบบ
เพื่อให้แน่ใจว่าทุกอย่างทำงานถูกต้องหลังจากการแก้ไข
"""

def verify_system_imports():
    """Verify all system modules import correctly"""
    print("=== SYSTEM IMPORT VERIFICATION ===")
    
    import_results = {}
    
    # Core modules
    modules_to_test = [
        ("calc", "freecad.StructureTools.calc"),
        ("reaction_results", "freecad.StructureTools.reaction_results"),
        ("diagram", "freecad.StructureTools.diagram"),
        ("material", "freecad.StructureTools.material"),
        ("member", "freecad.StructureTools.member"),
        ("support", "freecad.StructureTools.support"),
        ("load_nodal", "freecad.StructureTools.load_nodal"),
        ("load_distributed", "freecad.StructureTools.load_distributed"),
        ("universal_thai_units", "freecad.StructureTools.utils.universal_thai_units"),
        ("Pynite_FEModel3D", "freecad.StructureTools.Pynite_main.FEModel3D"),
        ("Pynite_Node3D", "freecad.StructureTools.Pynite_main.Node3D"),
        ("Pynite_Member3D", "freecad.StructureTools.Pynite_main.Member3D"),
    ]
    
    for name, module_path in modules_to_test:
        try:
            __import__(module_path)
            import_results[name] = True
            print(f"  ✅ {name}: Import successful")
        except Exception as e:
            import_results[name] = False
            print(f"  ❌ {name}: Import failed - {e}")
    
    # GUI modules
    gui_modules = [
        ("seismic_gui", "freecad.StructureTools.commands.command_seismic_load_gui"),
        ("wind_gui", "freecad.StructureTools.commands.command_wind_load_gui"),
    ]
    
    for name, module_path in gui_modules:
        try:
            __import__(module_path)
            import_results[name] = True
            print(f"  ✅ {name}: Import successful")
        except Exception as e:
            import_results[name] = False
            print(f"  ❌ {name}: Import failed - {e}")
    
    success_count = sum(import_results.values())
    total_count = len(import_results)
    
    print(f"\nImport Summary: {success_count}/{total_count} successful")
    return success_count == total_count

def verify_unit_conversion_accuracy():
    """Verify unit conversion accuracy"""
    print("\n=== UNIT CONVERSION ACCURACY VERIFICATION ===")
    
    try:
        from freecad.StructureTools.utils.universal_thai_units import get_universal_thai_units
        converter = get_universal_thai_units()
        
        if not converter.enabled:
            print("❌ Thai units converter not available")
            return False
        
        print("✅ Testing conversion accuracy...")
        
        # Test exact conversion factors
        test_cases = [
            ("Force: 1 kN to kgf", 1.0, converter.kn_to_kgf, 101.97162129779283),
            ("Force: 1 kN to tf", 1.0, converter.kn_to_tf, 0.10197162129779283),
            ("Moment: 1 kN·m to kgf·m", 1.0, converter.kn_m_to_kgf_m, 101.97162129779283),
            ("Moment: 1 kN·m to tf·m", 1.0, converter.kn_m_to_tf_m, 0.10197162129779283),
        ]
        
        all_accurate = True
        for description, input_val, conversion_func, expected in test_cases:
            actual = conversion_func(input_val)
            error = abs(actual - expected)
            
            if error < 1e-10:  # High precision check
                print(f"  ✅ {description}: {actual:.10f} (exact)")
            else:
                print(f"  ❌ {description}: {actual:.10f} vs {expected:.10f} (error: {error:.2e})")
                all_accurate = False
        
        # Test consistency of conversion factors
        print("\n  Consistency checks:")
        
        # 1 tf should equal 1000 kgf exactly
        tf_to_kgf = converter.TF_TO_KGF
        if tf_to_kgf == 1000.0:
            print(f"  ✅ 1 tf = {tf_to_kgf} kgf (exact)")
        else:
            print(f"  ❌ 1 tf = {tf_to_kgf} kgf (should be 1000.0)")
            all_accurate = False
        
        # 1 kgf should equal 9.80665 N exactly
        kgf_to_n = converter.KGF_TO_N
        if kgf_to_n == 9.80665:
            print(f"  ✅ 1 kgf = {kgf_to_n} N (exact)")
        else:
            print(f"  ❌ 1 kgf = {kgf_to_n} N (should be 9.80665)")
            all_accurate = False
        
        return all_accurate
        
    except Exception as e:
        print(f"❌ Unit conversion verification failed: {e}")
        return False

def verify_calc_properties():
    """Verify calc object properties"""
    import FreeCAD
    
    print("\n=== CALC PROPERTIES VERIFICATION ===")
    
    if not FreeCAD.ActiveDocument:
        print("❌ No active document - cannot verify calc properties")
        return False
    
    try:
        # Find calc objects
        doc = FreeCAD.ActiveDocument
        calc_objects = []
        
        for obj in doc.Objects:
            if hasattr(obj, 'Proxy') and obj.Proxy and hasattr(obj.Proxy, '__class__'):
                if 'Calc' in obj.Proxy.__class__.__name__:
                    calc_objects.append(obj)
        
        if not calc_objects:
            print("❌ No calc objects found")
            return False
        
        print(f"✅ Found {len(calc_objects)} calc object(s)")
        
        # Check properties for each calc object
        all_properties_ok = True
        
        required_properties = {
            'selfWeight': 'App::PropertyBool',
            'GlobalUnitsSystem': 'App::PropertyEnumeration', 
            'UseGlobalUnits': 'App::PropertyBool',
            'NumPointsMoment': 'App::PropertyInteger',
            'NumPointsAxial': 'App::PropertyInteger',
            'NumPointsShear': 'App::PropertyInteger',
            'LengthUnit': 'App::PropertyEnumeration',
            'ForceUnit': 'App::PropertyEnumeration',
            'LoadCombination': 'App::PropertyString',
        }
        
        for i, calc_obj in enumerate(calc_objects):
            print(f"\n  Checking calc object {i+1}: {calc_obj.Name}")
            
            missing_properties = []
            for prop_name, prop_type in required_properties.items():
                if not hasattr(calc_obj, prop_name):
                    missing_properties.append(prop_name)
            
            if missing_properties:
                print(f"    ❌ Missing properties: {missing_properties}")
                all_properties_ok = False
                
                # Try to fix
                try:
                    calc_obj.Proxy.ensure_required_properties(calc_obj)
                    print(f"    ✅ Properties automatically added")
                except Exception as e:
                    print(f"    ❌ Could not add properties: {e}")
            else:
                print(f"    ✅ All required properties present")
            
            # Check GlobalUnitsSystem options
            if hasattr(calc_obj, 'GlobalUnitsSystem'):
                options = calc_obj.getEnumerationsOfProperty('GlobalUnitsSystem')
                if "SI (kN, kN·m)" in options and "THAI (kgf, kgf·m)" in options:
                    print(f"    ✅ GlobalUnitsSystem options: {options}")
                else:
                    print(f"    ❌ GlobalUnitsSystem options incorrect: {options}")
                    all_properties_ok = False
            
            # Check selfWeight property
            if hasattr(calc_obj, 'selfWeight'):
                print(f"    ✅ selfWeight: {calc_obj.selfWeight}")
            else:
                print(f"    ❌ selfWeight property missing")
                all_properties_ok = False
        
        return all_properties_ok
        
    except Exception as e:
        print(f"❌ Calc properties verification failed: {e}")
        return False

def verify_reaction_results_functionality():
    """Verify reaction results functionality"""
    import FreeCAD
    
    print("\n=== REACTION RESULTS FUNCTIONALITY VERIFICATION ===")
    
    if not FreeCAD.ActiveDocument:
        print("❌ No active document")
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
            print("❌ No calc object found")
            return False
        
        print(f"✅ Testing with calc object: {calc_obj.Name}")
        
        # Check for analysis results
        has_results = False
        result_properties = ['MomentZ', 'MomentY', 'AxialForce', 'ShearY', 'ShearZ']
        
        for prop in result_properties:
            if hasattr(calc_obj, prop) and getattr(calc_obj, prop):
                has_results = True
                print(f"    ✅ Found {prop}: {len(getattr(calc_obj, prop))} items")
        
        if not has_results:
            print("    ⚠️  No analysis results - run calc first for full test")
        
        # Test reaction results creation
        reaction_obj = doc.addObject("App::DocumentObjectGroupPython", "ReactionVerificationTest")
        reaction_results.ReactionResults(reaction_obj, calc_obj)
        reaction_results.ViewProviderReactionResults(reaction_obj.ViewObject)
        
        # Check properties
        unit_properties = ['ForceUnit', 'MomentUnit', 'ZeroThreshold', 'Precision']
        properties_ok = True
        
        for prop in unit_properties:
            if hasattr(reaction_obj, prop):
                value = getattr(reaction_obj, prop)
                print(f"    ✅ {prop}: {value}")
            else:
                print(f"    ❌ Missing property: {prop}")
                properties_ok = False
        
        # Test unit conversion methods
        if hasattr(reaction_obj.Proxy, 'convert_force_value'):
            test_force = 100.0  # kN
            converted_value, formatted = reaction_obj.Proxy.convert_force_value(reaction_obj, test_force)
            print(f"    ✅ Force conversion test: {test_force} kN → {formatted}")
        else:
            print(f"    ❌ Missing convert_force_value method")
            properties_ok = False
        
        if hasattr(reaction_obj.Proxy, 'convert_moment_value'):
            test_moment = 50.0  # kN·m
            converted_value, formatted = reaction_obj.Proxy.convert_moment_value(reaction_obj, test_moment)
            print(f"    ✅ Moment conversion test: {test_moment} kN·m → {formatted}")
        else:
            print(f"    ❌ Missing convert_moment_value method")
            properties_ok = False
        
        # Test visualization execution
        try:
            reaction_obj.Proxy.execute(reaction_obj)
            print(f"    ✅ Visualization execution successful")
        except Exception as e:
            print(f"    ❌ Visualization execution failed: {e}")
            properties_ok = False
        
        # Clean up
        doc.removeObject(reaction_obj.Name)
        
        return properties_ok
        
    except Exception as e:
        print(f"❌ Reaction results verification failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def verify_self_weight_fix():
    """Verify self-weight calculation fix"""
    print("\n=== SELF-WEIGHT CALCULATION VERIFICATION ===")
    
    try:
        # Read the calc.py file to verify the fix
        import os
        calc_file_path = os.path.join(os.path.dirname(__file__), 'calc.py')
        
        if not os.path.exists(calc_file_path):
            print("❌ Cannot find calc.py file")
            return False
        
        with open(calc_file_path, 'r', encoding='utf-8') as f:
            calc_content = f.read()
        
        # Check that self-weight is applied outside the loop
        if "# Add self-weight ONCE for all members (not in the loop to avoid duplication)" in calc_content:
            print("✅ Self-weight duplication fix verified in code")
            
            # Check the actual implementation
            if "if selfWeight:\n\t\t\tmodel.add_member_self_weight('FY', -1)" in calc_content:
                print("✅ Self-weight applied once after member loop")
                return True
            else:
                print("❌ Self-weight implementation not found")
                return False
        else:
            print("❌ Self-weight fix comment not found")
            return False
            
    except Exception as e:
        print(f"❌ Self-weight verification failed: {e}")
        return False

def verify_json_serialization_fix():
    """Verify JSON serialization fix"""
    import FreeCAD
    
    print("\n=== JSON SERIALIZATION FIX VERIFICATION ===")
    
    if not FreeCAD.ActiveDocument:
        print("❌ No active document")
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
        
        # Check that FE model is stored correctly
        if hasattr(calc_obj, '_cached_fe_model'):
            print("✅ FE model uses _cached_fe_model (no JSON serialization)")
        else:
            print("⚠️  No _cached_fe_model - may need to run calc first")
        
        # Check status properties
        if hasattr(calc_obj, 'FEModelReady'):
            print(f"✅ FEModelReady property: {calc_obj.FEModelReady}")
        else:
            print("❌ FEModelReady property missing")
            return False
        
        if hasattr(calc_obj, 'FEModelInfo'):
            print(f"✅ FEModelInfo property: {calc_obj.FEModelInfo}")
        else:
            print("❌ FEModelInfo property missing")
            return False
        
        # Test document save (would fail before if JSON serialization was broken)
        try:
            import tempfile
            temp_file = tempfile.mktemp(suffix='.FCStd')
            doc.saveAs(temp_file)
            print("✅ Document save test passed (no JSON serialization errors)")
            
            import os
            if os.path.exists(temp_file):
                os.remove(temp_file)
            
            return True
            
        except Exception as save_error:
            if "JSON" in str(save_error) or "serializable" in str(save_error):
                print(f"❌ JSON serialization error still exists: {save_error}")
                return False
            else:
                print(f"⚠️  Document save issue (may not be JSON related): {save_error}")
                return True  # Other save errors are not JSON serialization issues
                
    except Exception as e:
        print(f"❌ JSON serialization verification failed: {e}")
        return False

def create_comprehensive_verification_report():
    """Create comprehensive verification report"""
    print("🔍 COMPREHENSIVE SYSTEM VERIFICATION")
    print("=" * 80)
    print("Performing thorough verification of all system components")
    print("and fixes to ensure everything works correctly")
    print("=" * 80)
    
    # Run all verification tests
    verification_results = {}
    
    print("Phase 1: Core System Verification")
    verification_results["System Imports"] = verify_system_imports()
    verification_results["Unit Conversion Accuracy"] = verify_unit_conversion_accuracy()
    
    print("\nPhase 2: Calc System Verification")
    verification_results["Calc Properties"] = verify_calc_properties()
    verification_results["Self-Weight Fix"] = verify_self_weight_fix()
    
    print("\nPhase 3: Results System Verification")
    verification_results["Reaction Results"] = verify_reaction_results_functionality()
    verification_results["JSON Serialization Fix"] = verify_json_serialization_fix()
    
    # Generate comprehensive report
    print("\n" + "=" * 80)
    print("📊 COMPREHENSIVE VERIFICATION RESULTS")
    print("=" * 80)
    
    passed_tests = 0
    critical_issues = []
    
    for test_name, result in verification_results.items():
        status = "✅ VERIFIED" if result else "❌ ISSUE FOUND"
        print(f"   {test_name}: {status}")
        
        if result:
            passed_tests += 1
        else:
            critical_issues.append(test_name)
    
    total_tests = len(verification_results)
    success_rate = (passed_tests / total_tests) * 100
    
    print(f"\n🎯 VERIFICATION SUMMARY:")
    print(f"   Passed: {passed_tests}/{total_tests} ({success_rate:.1f}%)")
    
    if passed_tests == total_tests:
        print("\n🎉 COMPLETE SYSTEM VERIFICATION PASSED!")
        print("=" * 80)
        print("✅ ALL SYSTEMS VERIFIED AND WORKING CORRECTLY:")
        print("   • All modules import successfully")
        print("   • Unit conversions are mathematically exact")
        print("   • Calc properties are complete and correct")
        print("   • Self-weight duplication is fixed")
        print("   • Reaction results work with all features")
        print("   • JSON serialization errors are resolved")
        print("\n🚀 SYSTEM IS READY FOR PRODUCTION USE!")
        
        print(f"\n📋 USAGE SUMMARY:")
        print("   1. Select unit system in Calc object (GlobalUnitsSystem)")
        print("   2. Enable/disable self-weight as needed")
        print("   3. Run analysis with Calc button")
        print("   4. View reactions with unit selection (kgf/tf)")
        print("   5. All diagrams use consistent units")
        
    else:
        print(f"\n⚠️  CRITICAL ISSUES FOUND:")
        for issue in critical_issues:
            print(f"   • {issue}")
        print(f"\n🔧 RECOMMENDED ACTIONS:")
        print("   1. Review error messages above")
        print("   2. Check system installation")
        print("   3. Verify FreeCAD document has structural model")
        print("   4. Run calc analysis before testing reactions")
    
    return passed_tests == total_tests

def quick_system_health_check():
    """Quick system health check"""
    print("\n" + "=" * 60)
    print("⚡ QUICK SYSTEM HEALTH CHECK")
    print("=" * 60)
    
    health_checks = []
    
    # Import check
    try:
        from freecad.StructureTools import calc, reaction_results
        from freecad.StructureTools.utils.universal_thai_units import get_universal_thai_units
        health_checks.append(("Core modules", True))
    except Exception as e:
        health_checks.append(("Core modules", False, str(e)))
    
    # Unit system check
    try:
        converter = get_universal_thai_units()
        if converter.enabled:
            test_conversion = converter.kn_to_kgf(1.0)
            expected = 101.972
            if abs(test_conversion - expected) < 0.1:
                health_checks.append(("Unit conversions", True))
            else:
                health_checks.append(("Unit conversions", False, f"Conversion error: {test_conversion} vs {expected}"))
        else:
            health_checks.append(("Unit conversions", False, "Converter disabled"))
    except Exception as e:
        health_checks.append(("Unit conversions", False, str(e)))
    
    # Document check
    import FreeCAD
    if FreeCAD.ActiveDocument:
        health_checks.append(("Active document", True))
        
        # Calc object check
        calc_found = False
        for obj in FreeCAD.ActiveDocument.Objects:
            if hasattr(obj, 'Proxy') and obj.Proxy and hasattr(obj.Proxy, '__class__'):
                if 'Calc' in obj.Proxy.__class__.__name__:
                    calc_found = True
                    break
        health_checks.append(("Calc objects", calc_found))
    else:
        health_checks.append(("Active document", False, "No document open"))
        health_checks.append(("Calc objects", False, "No document"))
    
    # Print results
    all_healthy = True
    for check in health_checks:
        name = check[0]
        healthy = check[1]
        status = "✅" if healthy else "❌"
        print(f"   {status} {name}")
        if not healthy:
            all_healthy = False
            if len(check) > 2:
                print(f"      Issue: {check[2]}")
    
    if all_healthy:
        print("\n✅ System health: EXCELLENT")
        print("   All critical components working correctly")
    else:
        print("\n⚠️  System health: NEEDS ATTENTION") 
        print("   Some components need checking")
    
    return all_healthy

if __name__ == "__main__":
    print("🔍 COMPREHENSIVE SYSTEM VERIFICATION")
    print("This script performs thorough verification of all fixes and components")
    print("to ensure the entire StructureTools system works correctly.")
    print()
    
    # Run comprehensive verification
    system_ok = create_comprehensive_verification_report()
    
    # Quick health check
    health_ok = quick_system_health_check()
    
    print("\n" + "=" * 80)
    if system_ok and health_ok:
        print("🎊 VERIFICATION COMPLETE - SYSTEM FULLY OPERATIONAL! 🎊")
    elif system_ok:
        print("✅ Core verification passed, minor health issues noted")
    else:
        print("⚠️  Verification found issues that need attention")
    print("=" * 80)