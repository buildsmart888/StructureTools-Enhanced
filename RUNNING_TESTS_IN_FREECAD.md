# Running Tests in FreeCAD

This document provides instructions on how to run the comprehensive test suites within FreeCAD's Python environment.

## Prerequisites

1. FreeCAD installed and running
2. StructureTools workbench installed in `C:\Users\<username>\AppData\Roaming\FreeCAD\Mod\StructureTools`

## Method 1: Quick Verification Test (Recommended)

This is the fastest way to verify that the NumPoints properties fix is working:

1. Open FreeCAD
2. Open the Python console (View → Panels → Python console)
3. Run the following commands:

```python
import sys
sys.path.append('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools')
from quick_verification_test import run_quick_test
run_quick_test()
```

This will run a focused test that specifically verifies:
- All NumPoints properties exist with correct defaults
- Backward compatibility functions are present
- The execute method runs without NumPointsMoment AttributeError
- getattr usage with defaults works correctly

## Method 2: Running Individual Test Suites

### Running Calc Comprehensive Tests

```python
import sys
sys.path.append('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools')
exec(open('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/test_calc_comprehensive.py').read())
run_tests()
```

### Running Diagram Comprehensive Tests

```python
import sys
sys.path.append('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools')
exec(open('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/test_diagram_comprehensive.py').read())
run_tests()
```

### Running Full Integration Tests

```python
import sys
sys.path.append('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools')
exec(open('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/test_structuretools_full.py').read())
run_full_tests()
```

## Method 3: Running All Tests at Once

```python
import sys
sys.path.append('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools')
exec(open('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/run_all_tests.py').read())
run_all_tests()
```

## Expected Results

### Success Case
```
🎉 ALL TESTS PASSED!
✅ All NumPoints properties exist with correct defaults
✅ Backward compatibility functions working
✅ Calc execute completed without NumPointsMoment errors
```

### Failure Case
```
❌ SOME TESTS FAILED!
❌ NumPointsMoment property missing
❌ AttributeError still occurs
```

## Troubleshooting

### 1. ImportError: No module named 'FreeCAD'
**Cause**: Tests are being run outside of FreeCAD's Python environment
**Solution**: Run tests in FreeCAD's Python console, not in system Python

### 2. AttributeError: 'FeaturePython' object has no attribute 'NumPointsMoment'
**Cause**: The fix may not be properly applied
**Solution**: 
- Verify that the changes to calc.py are correctly implemented
- Check that all NumPoints properties are initialized in the constructor
- Ensure backward compatibility functions exist

### 3. Path Issues
**Cause**: Incorrect path to StructureTools directory
**Solution**: Verify the path `c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools` exists

### 4. Syntax Errors
**Cause**: Corrupted or incorrectly modified files
**Solution**: 
- Check that all Python files have correct syntax
- Verify indentation is consistent (4 spaces)
- Ensure no mixed tabs and spaces

## Test Coverage

The test suites verify:

1. **NumPoints Properties Fix**:
   - NumPointsMoment (default: 5)
   - NumPointsAxial (default: 3)
   - NumPointsShear (default: 4)
   - NumPointsTorque (default: 3)
   - NumPointsDeflection (default: 4)

2. **Backward Compatibility**:
   - ensure_required_properties method
   - _addPropIfMissing helper function
   - Property restoration for older objects

3. **Integration**:
   - Calc and diagram modules working together
   - Unit conversion between modules
   - Reaction results flow

4. **Error Handling**:
   - AttributeError prevention
   - Graceful handling of missing properties
   - Exception handling in critical methods

## Best Practices

1. **Always run tests after making changes** to verify functionality
2. **Run quick verification test first** to check the main fix
3. **Run full test suite** before releasing changes
4. **Check FreeCAD console** for any warning or error messages
5. **Close documents properly** to avoid memory issues

## Support

If you continue to experience issues:

1. Verify all files are correctly modified according to the fix
2. Check FreeCAD version compatibility
3. Ensure all dependencies are installed
4. Review the COMPREHENSIVE_TESTS_README.md for detailed instructions