# Area Load Implementation Documentation

## Overview

This document describes the implementation of area load functionality in the StructureTools FreeCAD module, based on RISA documentation reference. The implementation provides comprehensive area loading capabilities for structural surfaces including pressure loads, distributed loads, wind loads, and thermal effects.

## Key Features

### 1. Load Distribution Methods

The implementation supports three main load distribution methods based on RISA documentation:

1. **One-Way Distribution**: Load is distributed to two parallel edges
2. **Two-Way Distribution**: Load is distributed based on relative span lengths
3. **Open Structure Distribution**: Load is distributed based on projected area

### 2. Load Direction Handling

- Support for load direction vectors in global coordinates
- Effective pressure calculation using dot product between load direction and face normal
- Coordinate system mapping between FreeCAD and solver (X→X, Y→Z, Z→Y)

### 3. Load Case Management

- Integration with load combinations
- Support for different load categories (DL, LL, W, E, H, F, T, CUSTOM)
- Proper load factor handling

## Implementation Details

### AreaLoad Class

The [AreaLoad](file:///c:/Users/thani/AppData/Roaming/FreeCAD/Mod/StructureTools/freecad/StructureTools/objects/AreaLoad.py#L35-L2128) class in `freecad/StructureTools/objects/AreaLoad.py` provides the core functionality:

#### Properties

- `TargetFaces`: Faces or surfaces to apply load
- `LoadDirection`: Load direction vector (global coordinates)
- `LoadIntensity`: Load intensity (pressure)
- `LoadDistribution`: Method for distributing load ("OneWay", "TwoWay", "OpenStructure")
- `OneWayDirection`: Direction for one-way load distribution ("X", "Y", "Custom")
- `CustomDistributionDirection`: Custom direction vector for one-way distribution
- `LoadCategory`: Load category for combinations ("DL", "LL", "W", etc.)

#### Methods

- `calculateEffectivePressure()`: Calculate effective pressure using dot product
- `getEdgeDistributionFactors()`: Calculate edge distribution factors based on method
- `updateLoadVisualization()`: Update visual representation of the load

### Calculation Module

The `calc.py` module in `freecad/StructureTools/calc.py` handles the processing of area loads:

#### Key Functions

- Area load mapping to plates/quads
- Effective pressure calculation
- Edge factor distribution
- Load case mapping
- Coordinate system transformation

## Usage Examples

### Creating an Area Load

```python
import FreeCAD as App
from freecad.StructureTools.objects.AreaLoad import AreaLoad

# Create an area load object
area_load = doc.addObject("App::FeaturePython", "AreaLoad1")
AreaLoad(area_load)

# Set properties
area_load.TargetFaces = [target_plate]
area_load.LoadIntensity = "5.0 kN/m^2"
area_load.LoadDirection = App.Vector(0, 0, -1)  # Downward load
area_load.LoadDistribution = "TwoWay"
```

### Setting Load Distribution

```python
# One-way distribution
area_load.LoadDistribution = "OneWay"
area_load.OneWayDirection = "X"  # or "Y" or "Custom"
# For custom direction:
# area_load.CustomDistributionDirection = App.Vector(1, 0, 0)

# Two-way distribution (default)
area_load.LoadDistribution = "TwoWay"

# Open structure distribution
area_load.LoadDistribution = "OpenStructure"
```

## Technical Details

### Effective Pressure Calculation

The effective pressure is calculated using the dot product between the load direction vector and the face normal:

```
effective_pressure = pressure_magnitude * |dot(load_direction, face_normal)|
```

This ensures that the pressure is correctly projected onto the surface, taking into account the angle between the load direction and the surface normal.

### Coordinate System Mapping

The implementation handles coordinate system mapping between FreeCAD and the solver:

- FreeCAD X → Solver X
- FreeCAD Y → Solver Z
- FreeCAD Z → Solver Y

This mapping ensures compatibility with the solver's coordinate system conventions.

### Edge Distribution Factors

The implementation calculates edge distribution factors based on the selected distribution method:

1. **One-Way**: Load goes to two parallel edges (0.5 each)
2. **Two-Way**: Load is distributed based on relative edge lengths
3. **Open Structure**: Load is distributed based on projection factors

## Testing

The implementation includes comprehensive tests:

1. `test_area_load_implementation.py`: Tests core functionality
2. `test_area_load_fea_validation.py`: Tests FEA model integration
3. `test_plate_integration.py`: Tests plate integration

## Future Enhancements

Potential areas for future development:

1. Advanced visualization of load distribution patterns
2. Support for more complex load shapes and distributions
3. Integration with building code-specific load calculations
4. Enhanced load combination management
5. Improved performance for large models

## Troubleshooting

Common issues and solutions:

1. **No plates found in FEA model**: Ensure plates have proper corner nodes defined
2. **Incorrect load distribution**: Verify load direction and distribution method
3. **Zero effective pressure**: Check that load direction and face normal are not perpendicular

## Conclusion

The area load implementation provides a robust and flexible solution for applying distributed loads to structural surfaces in FreeCAD. The implementation follows RISA documentation reference and provides accurate load distribution to supporting elements.