# ShowReactionText Functionality - Usage Guide

## Overview

The ShowReactionText feature displays reaction forces and moments as 3D text labels directly on the structural model, positioned near support nodes. This provides immediate visual feedback of the analysis results.

## Prerequisites

1. A structural model with support conditions (fixed or pinned supports)
2. Completed structural analysis (run the Calc command)
3. At least one load combination with results

## Usage

### Basic Usage

```python
# In FreeCAD Python Console
doc = FreeCAD.ActiveDocument
calc_obj = doc.getObject('Calc')  # or your Calc object name

# Enable reaction text display
calc_obj.ShowReactionText = True

# Disable reaction text display
calc_obj.ShowReactionText = False
```

### Configuration Properties

The following properties control the appearance and behavior of reaction text:

```python
# Text precision (decimal places)
calc_obj.ReactionPrecision = 2  # Default: 2

# Text offset from node position (mm)
calc_obj.ReactionTextOffset = 100.0  # Default: 100.0

# Font size
calc_obj.ReactionFontSize = 12.0  # Default: 12.0

# Active load combination
calc_obj.LoadCombination = "100_DL"  # Changes displayed values
```

### Example Usage Session

```python
import FreeCAD as App

# Get the Calc object
doc = App.ActiveDocument
calc = doc.getObject('Calc')

# Configure display properties
calc.ReactionPrecision = 3
calc.ReactionTextOffset = 150.0
calc.ReactionFontSize = 14.0

# Enable reaction text
calc.ShowReactionText = True

# Switch between load combinations
calc.LoadCombination = "1000_1.4DL+1.7LL"  # Text updates automatically
calc.LoadCombination = "100_DL"             # Back to dead load only
```

## Features

### Automatic Updates

The reaction text automatically updates when:
- ShowReactionText property changes
- LoadCombination changes  
- Analysis is re-run
- Display properties (precision, offset, font size) change

### Filtering

- Only displays reactions for nodes with support conditions
- Filters out negligible values (< 1e-6)
- Only shows significant force/moment components

### Text Format

The displayed text format is:
```
Node: N1
FX: -25.40 kN
FZ: -100.25 kN
MZ: -15.75 kN·m
```

Where:
- **FX, FY, FZ**: Force reactions in X, Y, Z directions (kN)
- **MX, MY, MZ**: Moment reactions about X, Y, Z axes (kN·m)

## Visual Properties

- **Color**: Red text for visibility
- **Position**: Offset from node location by configurable distance
- **Units**: Forces in kN, moments in kN·m
- **Precision**: Configurable decimal places

## Troubleshooting

### Problem: No text appears when ShowReactionText = True

**Solutions:**
1. Ensure analysis has been completed:
   ```python
   calc.execute()  # Run analysis
   ```

2. Check for support nodes:
   ```python
   # Run the test script
   exec(open('test_reaction_text.py').read())
   test_show_reaction_text()
   ```

3. Verify reactions exist:
   ```python
   show_reaction_values()  # From test script
   ```

### Problem: Text appears in wrong location

**Solution:**
Adjust the text offset:
```python
calc.ReactionTextOffset = 200.0  # Increase offset
```

### Problem: Too many decimal places

**Solution:**
Reduce precision:
```python
calc.ReactionPrecision = 1  # Show 1 decimal place
```

### Problem: Text is too small/large

**Solution:**
Adjust font size:
```python
calc.ReactionFontSize = 16.0  # Larger text
```

## Advanced Usage

### Manual Refresh

If text doesn't update automatically:
```python
vp = calc.ViewObject.Proxy
if hasattr(vp, 'updateReactionTextDisplay'):
    vp.updateReactionTextDisplay()
```

### Clean Up Text Objects

To remove all reaction text objects:
```python
calc.ShowReactionText = False  # This automatically cleans up
```

Or manually:
```python
vp = calc.ViewObject.Proxy
if hasattr(vp, 'clearReactionTexts'):
    vp.clearReactionTexts()
```

### Check Created Text Objects

```python
doc = FreeCAD.ActiveDocument
text_objects = [obj for obj in doc.Objects if obj.Label.startswith("Reactions_")]
print(f"Found {len(text_objects)} reaction text objects")
```

## Integration with Workflow

1. **Model Creation**: Create structural geometry and assign properties
2. **Load Application**: Apply loads and boundary conditions  
3. **Analysis**: Run structural analysis with Calc command
4. **Results Visualization**: Enable ShowReactionText to see reactions
5. **Load Combination Study**: Switch between combinations to compare results

## Technical Notes

- Text objects are created as Draft Text objects
- Text is positioned using node coordinates plus offset vector
- Text objects are automatically managed (created/destroyed) by the ViewProvider
- Changes to LoadCombination trigger automatic text updates
- All text objects are cleaned up when ShowReactionText is disabled

## API Reference

### Properties
- `ShowReactionText` (Bool): Enable/disable reaction text display
- `ReactionPrecision` (Int): Number of decimal places (default: 2)
- `ReactionTextOffset` (Float): Offset distance in mm (default: 100.0)
- `ReactionFontSize` (Float): Text font size (default: 12.0)
- `LoadCombination` (String): Active load combination

### Methods (ViewProvider)
- `updateReactionTextDisplay()`: Refresh reaction text display
- `createReactionTexts()`: Create text objects for all support nodes
- `clearReactionTexts()`: Remove all reaction text objects
- `getNodeReactions(node, combo)`: Extract reaction values for a node
- `formatReactionText(name, reactions, precision)`: Format reaction values as text