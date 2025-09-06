# Testing Instructions for NumPoints Properties Fix

## Overview
This document provides instructions for testing the fixes implemented for the AttributeError: 'FeaturePython' object has no attribute 'NumPointsMoment' issue.

## Fixes Implemented

1. **NumPoints Properties Initialization**:
   - Added all missing diagram resolution properties to the Calc class:
     - NumPointsMoment (default: 5)
     - NumPointsAxial (default: 3)
     - NumPointsShear (default: 4)
     - NumPointsTorque (default: 3)
     - NumPointsDeflection (default: 4)

2. **Backward Compatibility**:
   - Added _addPropIfMissing helper function
   - Added ensure_required_properties method
   - Call ensure_required_properties at the beginning of execute method

3. **Unbound Variable Fixes**:
   - Initialized direction and axis variables before match statement
   - Added default case for unexpected GlobalDirection values

4. **Exception Handler Fix**:
   - Ensured selected_combo is defined before using in error messages

5. **Consistent Default Values**:
   - Updated all getattr calls to use consistent default values

## How to Test

### Method 1: Using the Quick Test Script
1. Open FreeCAD
2. Open the Python console (View → Panels → Python console)
3. Run the following commands:
```python
import sys
sys.path.append('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools')
exec(open('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/quick_test.py').read())
```

### Method 2: Using the Full Test Script
1. Open FreeCAD
2. Open the Python console
3. Run the following commands:
```python
import sys
sys.path.append('c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools')
exec(open('c:/Users/thani/AppData/Roaming/FreecAD/Mod/StructureTools/test_num_points_fix.py').read())
test_num_points_properties()
```

### Method 3: Manual Testing in FreeCAD
1. Open FreeCAD
2. Create a new document
3. Create a simple beam (e.g., using Draft or Part workbench)
4. Select the beam
5. Run the Calc command (press "calc" button or use the command)
6. The analysis should complete without the NumPointsMoment AttributeError

## Expected Results
- No AttributeError related to NumPoints properties
- All NumPoints properties should be present with correct default values
- Backward compatibility functions should be available
- Calc execution should complete successfully
- Unbound variable errors should be resolved

## Troubleshooting
If you still encounter issues:
1. Check that all fixes have been applied correctly
2. Restart FreeCAD to ensure changes are loaded
3. Check the FreeCAD console for any error messages
4. Verify that the calc.py file has been updated with all the fixes