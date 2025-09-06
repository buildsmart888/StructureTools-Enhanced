# Moment Units Fix Summary

## Problem
The previous implementation had inconsistent units for moments when using meters for length:
- Thai units were using kgf·cm for moments with m for length, requiring conversion factors
- This led to potential errors and confusion in interpretation

## Solution Implemented

### 1. Updated Unit System Consistency
- Modified Thai units preset to use **kgf·m** instead of **kgf·cm** for moments
- Ensured all units are consistent with meters for length:
  - Length: m
  - Forces: kgf (optionally tf)
  - Moments: kgf·m (optionally tf·m)

### 2. Added Moment Formatting Function
- Added `format_moment()` function to `units_manager.py`
- Supports conversion between all moment units:
  - N·m, kN·m (SI)
  - kgf·m, tf·m (Thai)
  - kip·ft (US)

### 3. Enhanced Export Functionality
- Added CSV export capability in reaction results panel
- Proper unit formatting in exported data
- Clear column headers with units
- Summary information including:
  - Load combination
  - Unit system used
  - Sign convention
  - Total reactions and moments for sanity checking

### 4. Improved Display Formatting
- Updated reaction visualization labels to show properly formatted moment values
- Consistent precision control for all units

## Key Features

### Unit Definitions
- **1 tf = 1000 kgf** (exact, as per Thai standards)
- **1 kgf = 9.80665 N** (exact, as per definition)
- **Moment units**: kgf·m or tf·m when length is in meters

### Sign Convention
- Forces: Positive = reaction direction
- Moments: Right-hand rule (positive = counter-clockwise when looking along positive axis)

### Output Format
CSV export includes:
```
Node ID, DOF, Rx (Force X), Ry (Force Y), Rz (Force Z), Mx (Moment X), My (Moment Y), Mz (Moment Z), X (Position), Y (Position), Z (Position)
```

### Precision Control
- Forces: 2 decimal places
- Moments: 2 decimal places
- Lengths: 3 decimal places

## Benefits
1. **Eliminates conversion errors** by using consistent units
2. **Clearer interpretation** of results with proper unit labeling
3. **Export capability** for further analysis
4. **Compliance with Thai standards** using 1 tf = 1000 kgf
5. **Reduced cognitive load** by avoiding mixed unit systems

## Verification
- All existing functionality preserved
- New export feature tested and working
- Unit conversions verified against standard values
- Backward compatibility maintained