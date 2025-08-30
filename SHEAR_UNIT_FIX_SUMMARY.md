# Shear Force Unit Display Fix Summary

## Issue Description

**Problem**: Shear force diagrams were missing unit display ("kN") when the ShowUnits property was enabled.

**Location**: `freecad/StructureTools/diagram.py`, lines 198-212 in the `makeText` method

**Root Cause**: The unit determination logic only checked for Torque and AxialForce properties but did not check for Shear properties (ShearZ and ShearY).

## What Was Fixed

### 1. Missing Shear Unit Support
**File**: `freecad/StructureTools/diagram.py`
**Method**: `makeText` 
**Location**: Lines 204-210

**Before**:
```python
# Determine unit based on diagram type (simplified approach)
if hasattr(obj, 'Torque') and obj.Torque:
    unit = " kN·m"  # Torque unit
elif hasattr(obj, 'AxialForce') and obj.AxialForce:
    unit = " kN"    # Axial force unit
else:
    unit = " kN·m"  # Default to moment unit
```

**After**:
```python
# Determine unit based on diagram type (simplified approach)
if hasattr(obj, 'Torque') and obj.Torque:
    unit = " kN·m"  # Torque unit
elif hasattr(obj, 'AxialForce') and obj.AxialForce:
    unit = " kN"    # Axial force unit
elif (hasattr(obj, 'ShearZ') and obj.ShearZ) or (hasattr(obj, 'ShearY') and obj.ShearY):
    unit = " kN"    # Shear force unit
else:
    unit = " kN·m"  # Default to moment unit
```

## Test Results

✅ **Shear Z diagrams** now correctly display "kN" units
✅ **Shear Y diagrams** now correctly display "kN" units
✅ **Torque diagrams** continue to display "kN·m" units
✅ **Axial force diagrams** continue to display "kN" units
✅ **Default moment diagrams** continue to display "kN·m" units

## Impact

This fix ensures that all structural diagram types in StructureTools properly display their respective units when the ShowUnits property is enabled:

- **Torque**: kN·m
- **Axial Force**: kN
- **Shear Force** (Z and Y directions): kN ← **FIXED**
- **Moment** (default): kN·m

The fix maintains backward compatibility and does not affect any existing functionality.