# Load Distribution Visualization

## Overview

This module provides comprehensive visualization and calculation tools for slab load distribution patterns in structural analysis. It helps engineers visualize how area loads on slabs are transferred to supporting beams using established structural analysis methods.

## Features

### 1. **Two-Way Slab (Yield Line Method)**
- Visualizes yield line patterns with 45° diagonal lines from corners
- Calculates triangular loads on short span beams
- Calculates trapezoidal loads on long span beams
- Shows tributary areas with color coding
- Applicable for slabs with aspect ratio Lx/Ly < 2.0

### 2. **One-Way Slab**
- Visualizes parallel load strips
- Calculates uniform loads on supporting beams  
- Shows load transfer direction
- Applicable for slabs with aspect ratio Lx/Ly ≥ 2.0

### 3. **Beam Load Visualization**
- Displays distributed loads on beams with load diagrams
- Supports uniform, triangular, and trapezoidal distributions
- Shows load envelopes with proper scaling
- Visual arrows proportional to load magnitude

### 4. **Load Calculations**
- Automatic calculation of beam reactions
- Load balance verification
- Console output with detailed load summaries
- Export-ready data for structural analysis

## Usage

### Basic Usage in FreeCAD

#### 1. Create an Area Load
```python
import FreeCAD as App
from freecad.StructureTools.objects.AreaLoad import AreaLoad

# Select faces or create area load via GUI
# StructureTools → Create Area Load
```

#### 2. Visualize Load Distribution
```python
from freecad.StructureTools.visualization.LoadDistributionVisualizer import LoadDistributionVisualizer

doc = App.ActiveDocument
viz = LoadDistributionVisualizer(doc)

# Define slab corners (counterclockwise)
corners = [
    App.Vector(0, 0, 0),       # A
    App.Vector(6000, 0, 0),    # B (6m)
    App.Vector(6000, 5000, 0), # C (5m)
    App.Vector(0, 5000, 0)     # D
]

# Two-way slab visualization
viz.visualize_two_way_yield_line(corners, load_intensity=10.0, name_prefix="Slab1")

# One-way slab visualization
viz.visualize_one_way_distribution(corners, span_direction="short", 
                                   load_intensity=10.0, name_prefix="Slab2")
```

#### 3. Calculate Beam Loads
```python
from freecad.StructureTools.visualization.LoadDistributionVisualizer import SlabLoadCalculator

calc = SlabLoadCalculator()

# Calculate two-way beam loads
beam_loads = calc.calculate_two_way_beam_loads(corners, load_intensity=10.0)
calc.print_beam_loads(beam_loads)

# Calculate one-way beam loads
beam_loads = calc.calculate_one_way_beam_loads(corners, load_intensity=10.0, 
                                                 span_direction="short")
calc.print_beam_loads(beam_loads)
```

#### 4. Complete Visualization with Beam Loads
```python
# All-in-one method
viz.visualize_slab_with_beam_loads(
    corners,
    load_intensity=10.0,
    distribution_type="two_way",  # or "one_way"
    name_prefix="CompleteViz"
)
```

### Using GUI Commands

#### Visualize Load Distribution Command
1. Select an AreaLoad object in the tree
2. Click **Visualize Load Distribution** button (or menu: StructureTools → Visualize Load Distribution)
3. Choose distribution type (Two-Way or One-Way)
4. Set load intensity
5. Click "Create Visualization"

#### Clear Load Distribution Command
- Click **Clear Load Distribution** to remove all visualization objects
- Menu: StructureTools → Clear Load Distribution

## Load Calculation Theory

### Two-Way Slab (Yield Line Method)

For rectangular slabs supported on all four edges:

**Short Span Beams (Triangular Load):**
```
w_max = q × (Lshort / 2)
Total Force = q × Lshort × Llong / 4
```

**Long Span Beams (Trapezoidal Load):**
```
w_uniform = q × (Lshort / 2)
Uniform Length = Llong - Lshort
Total Force = q × Llong × Lshort / 4 + q × uniform_length × (Lshort/2)
```

Where:
- `q` = Load intensity (kN/m²)
- `Lshort` = Short span (m)
- `Llong` = Long span (m)

### One-Way Slab

For slabs spanning in one direction:

**Supporting Beams (Uniform Load):**
```
w = q × Lspan / 2
Total Force = w × Lbeam
```

Where:
- `Lspan` = Span length perpendicular to beam
- `Lbeam` = Beam length

## Example: 6m × 5m Slab with 10 kN/m²

```python
from freecad.StructureTools.visualization.LoadDistributionVisualizer import (
    LoadDistributionVisualizer, SlabLoadCalculator
)

# Define slab
corners = [
    App.Vector(0, 0, 0),
    App.Vector(6000, 0, 0),
    App.Vector(6000, 5000, 0),
    App.Vector(0, 5000, 0)
]
load = 10.0  # kN/m²

# Visualize
viz = LoadDistributionVisualizer(App.ActiveDocument)
viz.visualize_slab_with_beam_loads(corners, load, "two_way", "Example")

# Calculate
calc = SlabLoadCalculator()
beam_loads = calc.calculate_two_way_beam_loads(corners, load)
calc.print_beam_loads(beam_loads)
```

**Expected Output:**
```
=== Beam Load Distribution ===
Edge AB: Triangular w_max = 25.00 kN/m, L = 5.00 m
         Total Force: 75.00 kN
Edge CD: Triangular w_max = 25.00 kN/m, L = 5.00 m
         Total Force: 75.00 kN
Edge BC: Trapezoidal w = 25.00 kN/m, L = 6.00 m
         Total Force: 75.00 kN
Edge DA: Trapezoidal w = 25.00 kN/m, L = 6.00 m
         Total Force: 75.00 kN
==============================
Total slab load: 10 × 6 × 5 = 300 kN
Sum of beam reactions: 300.00 kN
```

## Testing

Run the test suite to verify functionality:

```python
exec(open('c:/Users/g_np2/AppData/Roaming/FreeCAD/Mod/StructureTools/freecad/StructureTools/test_load_distribution.py').read())
```

Or in FreeCAD Python Console:
```python
from freecad.StructureTools import test_load_distribution
test_load_distribution.run_all_tests()
```

## Design References

- **Two-Way Slab Design**: Based on yield line theory and ACI 318
- **Load Distribution**: Follows structural analysis principles for plate bending
- **Beam Loading**: Uses tributary area method for support reactions

## Visualization Objects

The module creates the following FreeCAD objects:

| Object Type | Name Pattern | Description |
|------------|--------------|-------------|
| Yield Lines | `{prefix}_YieldLine_{i}` | Dashed orange lines showing yield line pattern |
| Boundary | `{prefix}_Boundary` | Solid black outline of slab |
| Tributary Areas | `{prefix}_Area_{i}` | Semi-transparent colored faces |
| Load Arrows | `{prefix}_Arrow_{i}` | Magenta arrows showing load magnitude |
| Load Envelope | `{prefix}_Envelope` | Line showing load distribution shape |
| Beam Line | `{prefix}_Beam` | Gray line representing the beam |
| Load Label | `{prefix}_LoadLabel` | Text annotation with load value |

## Advanced Features

### Custom Beam Positions
```python
# Define custom beam positions
edge_beams = {
    "AB": (App.Vector(0, 0, -200), App.Vector(6000, 0, -200)),
    "BC": (App.Vector(6000, 0, -200), App.Vector(6000, 5000, -200)),
    "CD": (App.Vector(6000, 5000, -200), App.Vector(0, 5000, -200)),
    "DA": (App.Vector(0, 5000, -200), App.Vector(0, 0, -200))
}

beam_loads = calc.calculate_two_way_beam_loads(corners, load, edge_beams)
```

### Clear Previous Visualizations
```python
viz.clear_visualization()  # Removes all objects created by this visualizer
```

### Scale Arrows
```python
viz.arrow_scale = 100.0  # mm per kN/m (default: 50.0)
```

## Integration with AreaLoad

The `AreaLoad` object automatically creates load distribution visualizations when `ShowLoadDistribution` is enabled:

```python
area_load_obj.ShowLoadDistribution = True
area_load_obj.SlabDistributionType = "Two-Way (Yield Line)"  # or "One-Way (Short Span)"
App.ActiveDocument.recompute()
```

## Troubleshooting

### Issue: Visualization not appearing
- Check that corners are in counterclockwise order
- Verify all 4 corners are provided
- Ensure document is recomputed: `App.ActiveDocument.recompute()`

### Issue: Load balance doesn't match
- Check corner coordinates (units are mm in FreeCAD)
- Verify load intensity units (kN/m²)
- Review console output for calculation details

### Issue: Commands not available
- Ensure `command_load_distribution.py` is imported in `init_gui.py`
- Restart FreeCAD after installation
- Check console for import errors

## Future Enhancements

- [ ] Support for irregular slab shapes
- [ ] Point load and line load visualization
- [ ] Export beam loads to FEM analysis
- [ ] Automatic detection of supporting beams
- [ ] Support for slabs with openings
- [ ] Moment distribution diagrams
- [ ] Load combination visualization

## License

Part of the StructureTools FreeCAD add-on.

## Credits

Developed as part of the comprehensive structural analysis enhancement for FreeCAD StructureTools.

Based on established structural engineering principles and modern building codes (ACI 318, AS 3600, EC2).
