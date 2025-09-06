# Comprehensive Tests for StructureTools

This directory contains comprehensive test suites for the StructureTools FreeCAD workbench, specifically for the `calc.py` and `diagram.py` modules.

## Test Files

1. **test_calc_comprehensive.py** - Comprehensive tests for calc.py functionality
2. **test_diagram_comprehensive.py** - Comprehensive tests for diagram.py functionality
3. **test_structuretools_full.py** - Full integration tests for both modules working together

## How to Run Tests

### Method 1: Running Tests in FreeCAD Python Console

1. Open FreeCAD
2. Open the Python console (View → Panels → Python console)
3. Run the following commands:

```python
import sys
sys.path.append('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools')

# Run calc tests
exec(open('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/test_calc_comprehensive.py').read())
run_tests()

# Run diagram tests
exec(open('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/test_diagram_comprehensive.py').read())
run_tests()

# Run full integration tests
exec(open('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/test_structuretools_full.py').read())
run_full_tests()
```

### Method 2: Running Tests from Command Line

If you have FreeCAD accessible from the command line:

```bash
# Run calc tests
FreeCADCmd c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/test_calc_comprehensive.py

# Run diagram tests
FreeCADCmd c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/test_diagram_comprehensive.py

# Run full integration tests
FreeCADCmd c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/test_structuretools_full.py
```

### Method 3: Running Individual Test Cases

You can also run specific test cases:

```python
import sys
sys.path.append('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools')
import unittest

# Import the test module
import test_calc_comprehensive

# Run specific test class
suite = unittest.TestLoader().loadTestsFromTestCase(test_calc_comprehensive.TestCalc)
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
```

## Test Coverage

### calc.py Tests Cover:

1. **Object Creation** - Verifying Calc object is created with all required properties
2. **NumPoints Properties** - Testing all diagram resolution properties exist with correct defaults
3. **Backward Compatibility** - Testing ensure_required_properties and _addPropIfMissing methods
4. **Execute Method** - Testing execute method runs without NumPointsMoment AttributeError
5. **Load Handling** - Testing load factor calculations and direction compatibility
6. **Reaction Results** - Testing reaction force properties and methods
7. **Structured Results** - Testing MemberResults and export methods
8. **Unit Properties** - Testing LengthUnit and ForceUnit defaults
9. **Integration Tests** - Testing with multiple elements and frame structures

### diagram.py Tests Cover:

1. **Object Creation** - Verifying Diagram object creation with all properties
2. **Basic Properties** - Testing color, transparency, font, precision settings
3. **Unit Properties** - Testing force, moment, and Thai unit properties
4. **Diagram Type Properties** - Testing moment, shear, torque, and axial properties
5. **Method Testing** - Testing all public and private methods
6. **Integration with Calc** - Testing diagram creation with calc objects
7. **View Provider** - Testing ViewProviderDiagram functionality
8. **Execute Method** - Testing diagram generation

### Full Integration Tests Cover:

1. **Calc-Diagram Integration** - Testing both modules work together
2. **Backward Compatibility** - Testing compatibility features
3. **Unit Conversion** - Testing unit synchronization between modules
4. **Reaction Results** - Testing reaction force integration
5. **Structured Results** - Testing result data flow between modules
6. **Load Combinations** - Testing load combination handling
7. **Display Options** - Testing diagram display properties
8. **Error Handling** - Testing error conditions and edge cases

## Test Results

- ✅ **Pass**: Test completed successfully
- ❌ **Fail**: Test failed (will show specific assertion errors)
- ⚠️ **Warning**: Test had non-critical issues

## Troubleshooting

1. **Import Errors**: Make sure the path `c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools` is in your Python path
2. **Module Not Found**: Ensure FreeCAD is running and modules are properly installed
3. **AttributeError**: If you see NumPointsMoment errors, the fixes may not be properly applied
4. **GUI Issues**: Some tests may fail in headless environments (normal behavior)

## Test Development

To add new tests:

1. Follow the existing pattern in the test files
2. Use descriptive test method names (test_what_you_are_testing)
3. Include appropriate assertions
4. Handle FreeCAD document creation/teardown properly
5. Test both success and failure cases

## Continuous Integration

These tests can be used for:
- Verifying bug fixes
- Regression testing
- Pre-release validation
- Development workflow validation