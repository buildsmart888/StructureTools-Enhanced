# Reaction Forces and Moments Visualization Guide

## Overview

This guide explains how to display and visualize reaction forces (FX, FY, FZ) and moments (MX, MY, MZ) in the StructureTools workbench. The visualization includes:

- **Red arrows** for reaction forces (FX, FY, FZ)
- **Green arrows** for reaction moments (MX, MY, MZ)
- **Numerical values** displayed as labels
- **Support for all load combinations**

![Reaction Visualization Example](image/REACTION_VISUALIZATION_GUIDE/reaction_example.png)

## Method 1: Using the GUI

### Step 1: Run Structural Analysis

1. Create your structural model with appropriate supports
2. Apply loads to your structure
3. Click the "Calc" button in the StructureTools toolbar
4. Wait for analysis to complete

### Step 2: Access Reaction Results

1. Click the "Reaction Results" button in the StructureTools toolbar
   - This is located in the "StructureResults" toolbar
   - If not visible, right-click on any toolbar and check "StructureResults"

2. Alternative access methods:
   - Right-click on the Calc object in the model tree and select "View Reaction Results"
   - Use the keyboard shortcut (if configured)

### Step 3: Configure Visualization

In the Reaction Results dialog:

1. **Force Settings (Red Arrows)**
   - Check FX, FY, FZ checkboxes to display desired force components
   - Click "Force Color" button and select red
   - Adjust "Force Scale" slider to control arrow size

2. **Moment Settings (Green Arrows)**
   - Check MX, MY, MZ checkboxes to display desired moment components
   - Click "Moment Color" button and select green
   - Adjust "Moment Scale" slider to control arrow size

3. **Resultant Reactions**
   - Check "Show Resultant Forces" to display combined force vectors
   - Check "Show Resultant Moments" to display combined moment vectors
   - Adjust "Resultant Force Scale" and "Resultant Moment Scale" as needed

4. **Display Options**
   - Check "Show Values" to display numerical labels
   - Set "Precision" to control decimal places (e.g., 2)
   - Adjust "Font Size" to control label size
   - Set "Arrow Thickness" for better visibility
   - Select "Language" for label language (English or Thai)
   - Check "Auto-Scale Reactions" to automatically scale arrows based on model size

5. **Color Gradient Options**
   - Check "Use Color Gradient" to enable color coding based on reaction magnitude
   - Set "Min Gradient Color" for minimum reaction values (default green)
   - Set "Max Gradient Color" for maximum reaction values (default red)

6. **Specialized Visualization**
   - Check "Show Only Maximum Reactions" to display only the largest reaction at each support
   - Check "Show Only Significant Reactions" to filter out small reactions
   - Adjust "Significance Threshold" to control what's considered significant (ratio of max reaction)

7. **Load Combinations**
   - Use the dropdown to select different load cases
   - Each combination will display its specific reaction values

### Step 4: Fine-Tune with Properties Panel

For additional customization:

1. Select the ReactionResults object in the model tree
2. Open the Properties panel (View → Panels → Property panel)
3. Adjust these properties as needed:
   - `ForceArrowColor`: Set to (1.0, 0.0, 0.0) for red
   - `MomentArrowColor`: Set to (0.0, 1.0, 0.0) for green
   - `ScaleReactionForces`: Control force arrow scale
   - `ScaleReactionMoments`: Control moment arrow scale
   - `ShowResultantForces`: Toggle resultant force display
   - `ShowResultantMoments`: Toggle resultant moment display
   - `ScaleResultantForces`: Control resultant force arrow scale
   - `ScaleResultantMoments`: Control resultant moment arrow scale
   - `ShowLabels`: Toggle value labels on/off
   - `Precision`: Set decimal places for values
   - `LabelFontSize`: Control text size
   - `ArrowThickness`: Set arrow line thickness
   - `MinReactionThreshold`: Minimum reaction magnitude to display
   - `AutoScaleReactions`: Automatically scale reactions based on model size
   - `UseColorGradient`: Use color gradient based on reaction magnitude
   - `MinGradientColor`: Color for minimum reaction values
   - `MaxGradientColor`: Color for maximum reaction values
   - `ShowOnlyMaximumReactions`: Show only maximum reactions at each node
   - `ShowOnlySignificantReactions`: Show only reactions above significance threshold
   - `SignificanceThreshold`: Threshold for significant reactions (ratio of max reaction)

## Method 2: Using Python

### Create Reaction Visualization from Scratch

```python
import FreeCAD
doc = FreeCAD.ActiveDocument

# Find Calc object
calc_obj = None
for obj in doc.Objects:
    if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, 'Type'):
        if getattr(obj.Proxy, 'Type', None) == 'Calc':
            calc_obj = obj
            break

# Import required modules
from freecad.StructureTools.reaction_results import ReactionResults, ViewProviderReactionResults

# Create reaction results object
reaction_obj = doc.addObject("Part::FeaturePython", "ReactionResults")
ReactionResults(reaction_obj, calc_obj)
ViewProviderReactionResults(reaction_obj.ViewObject)

# Configure appearance
reaction_obj.ForceArrowColor = (1.0, 0.0, 0.0, 0.0)  # Red
reaction_obj.MomentArrowColor = (0.0, 1.0, 0.0, 0.0)  # Green

# Control which components to display
reaction_obj.ShowReactionFX = True
reaction_obj.ShowReactionFY = True
reaction_obj.ShowReactionFZ = True
reaction_obj.ShowReactionMX = True
reaction_obj.ShowReactionMY = True
reaction_obj.ShowReactionMZ = True

# Set scale factors
reaction_obj.ScaleReactionForces = 1.0
reaction_obj.ScaleReactionMoments = 1.0

# Configure labels
reaction_obj.ShowLabels = True
reaction_obj.Precision = 2
reaction_obj.LabelFontSize = 8

# Advanced features
reaction_obj.ShowResultantForces = True
reaction_obj.ShowResultantMoments = True
reaction_obj.AutoScaleReactions = True
reaction_obj.UseColorGradient = True
reaction_obj.ShowOnlyMaximumReactions = False
reaction_obj.ShowOnlySignificantReactions = False

# Update display
FreeCAD.ActiveDocument.recompute()
```

### Modify Existing Reaction Visualization

```python
# Get existing reaction results object
reaction_obj = doc.getObject("ReactionResults")

# Change display settings
reaction_obj.ForceArrowColor = (1.0, 0.0, 0.0, 0.0)  # Red
reaction_obj.MomentArrowColor = (0.0, 1.0, 0.0, 0.0)  # Green
reaction_obj.ShowReactionFX = True
reaction_obj.ShowReactionMX = True
reaction_obj.ScaleReactionForces = 1.5  # Increase force scale
reaction_obj.Precision = 3  # More decimal places

# Advanced features
reaction_obj.AutoScaleReactions = True  # Auto-scale based on model size
reaction_obj.UseColorGradient = True    # Enable color gradient
reaction_obj.MinReactionThreshold = 1e-5  # Filter small reactions

# Update display
FreeCAD.ActiveDocument.recompute()
```

## Customizing Reaction Table

The reaction table can also be customized to show forces and moments with appropriate formatting:

1. Click "Table View" in the Reaction Results panel
2. Use the table's context menu to:
   - Export data to Excel, CSV or Word
   - Copy specific values
   - Sort by different columns
   - Filter results

## Development Notes

### Implementation Components

Key files for reaction visualization:

- `reaction_results.py`: Main implementation of reaction arrows and labels
- `reaction_results_panel.py`: GUI panel for controlling visualization
- `reaction_table_panel.py`: Table view of reaction values

### Coordinate System

The coordinate system mapping in StructureTools:
- FreeCAD X → Solver X (index 0)
- FreeCAD Y → Solver Z (index 2)
- FreeCAD Z → Solver Y (index 1)

This means for visualization:
- Force arrows for FX: Along FreeCAD X-axis
- Force arrows for FY: Along FreeCAD Z-axis
- Force arrows for FZ: Along FreeCAD Y-axis

### Arrow Creation

Force arrows are created using:
- `create_force_arrow()` method for forces
- `create_moment_arrow()` method for moments
- `create_arrow_shape()` for generating arrow geometry
- `create_curved_arrow_shape()` for moment arrows

### Error Handling

Common issues and solutions:

1. **No reactions visible**:
   - Ensure analysis was completed successfully
   - Check that model has proper support conditions
   - Verify applied loads
   - Try recalculating or reopening document

2. **Arrows too large/small**:
   - Adjust ScaleReactionForces and ScaleReactionMoments
   - Check magnitude of reaction values
   - Consider model unit scale
   - Use AutoScaleReactions for automatic scaling

3. **Missing components**:
   - Ensure all desired checkboxes are checked
   - Verify if specific reactions exist in the model
   - Check if reaction magnitudes are significant (> MinReactionThreshold)

## Enhancement Ideas

Potential improvements to consider:

1. ~~Add support for displaying resultant reactions~~ (IMPLEMENTED)
2. ~~Implement filtering for minimum reaction threshold~~ (IMPLEMENTED)
3. ~~Add auto-scaling option based on model size~~ (IMPLEMENTED)
4. ~~Include color gradient based on reaction magnitude~~ (IMPLEMENTED)
5. ~~Add support for localized labeling (Thai/English)~~ (IMPLEMENTED)
6. ~~Create specialized visualization for specific reaction types~~ (IMPLEMENTED)

## Thai Language Support

ให้เพิ่มป้ายชื่อภาษาไทยสำหรับแรงปฏิกิริยา:
- เพิ่มตัวเลือกภาษาไทยในส่วนการแสดงผล
- ใช้รูปแบบ "แรงในแนวแกน X: 25.4 kN" แทน "FX: 25.4 kN"
- ปรับขนาดฟอนต์ให้เหมาะสมกับภาษาไทย