# Point Load Feature Usage Guide

## Overview
The Point Load feature allows you to apply concentrated forces and moments at specific positions along structural members (lines/edges) in StructureTools. This feature fills the gap between nodal loads (applied at nodes only) and distributed loads (applied over a length).

## Features
- Position point loads anywhere along a member using relative positioning (0.0 to 1.0)
- Apply forces in local or global directions
- Apply moments about local axes
- Visualize loads with green arrows positioned along members
- Send loads to structural analysis engine (Pynite)

## Available Load Directions
- **Global Forces**: +X, -X, +Y, -Y, +Z, -Z
- **Local Forces**: +x, -x, +y, -y, +z, -z
- **Moments**: +My, -My, +Mz, -Mz, +Mx, -Mx

## Usage Instructions

### 1. Creating a Point Load
1. Select one or more edges of structural members in the 3D view
2. Click on the "Point Load" button in the StructureLoad toolbar, or
3. Use the keyboard shortcut: **Shift+P**

### 2. Configuring Point Load Properties
After creating a point load, you can configure its properties in the Properties panel:

- **PointLoading**: The magnitude of the point load (force or moment)
- **RelativePosition**: Position along the member (0.0 = start, 0.5 = middle, 1.0 = end)
- **LoadType**: Type of load (DL, LL, H, F, W, E)
- **GlobalDirection**: Direction of the load (+X, -Y, +Mz, etc.)
- **ScaleDraw**: Scale factor for visualization

### 3. Visualization
- Point loads are displayed as green arrows along structural members
- The position is determined by the RelativePosition property
- The label shows the load type, direction, and position percentage

### 4. Running Analysis
Point loads are automatically included when you run structural analysis using the "Calc" command.

## Examples

### Example 1: Mid-span Point Load
To apply a 10 kN downward load at the center of a beam:
1. Create point load on the beam edge
2. Set PointLoading = 10000 N
3. Set RelativePosition = 0.5
4. Set GlobalDirection = -Z (global downward)

### Example 2: End Moment
To apply a 5 kN·m moment at the end of a member:
1. Create point load on the member edge
2. Set PointLoading = 5000 N·m
3. Set RelativePosition = 1.0 (end of member)
4. Set GlobalDirection = +Mz

## Technical Details

### Positioning
The RelativePosition property determines where along the member the load is applied:
- 0.0 = Start of member (first node)
- 0.5 = Midpoint of member
- 1.0 = End of member (second node)
Values are clamped between 0.0 and 1.0.

### Coordinate Systems
- **Global directions** (+X, -Y, etc.) use the global coordinate system
- **Local directions** (+x, -y, etc.) use the member local coordinate system
- **Moments** use member local axes

### Analysis Integration
Point loads are processed by the Pynite engine using the `add_member_pt_load` method with the following parameters:
- Member name
- Load direction
- Load magnitude
- Position along member
- Load case

## Troubleshooting

### Load Not Appearing in Results
- Ensure the load is on a valid structural member
- Check that the member is included in the analysis
- Verify the load magnitude is non-zero

### Incorrect Positioning
- Check that RelativePosition is between 0.0 and 1.0
- Verify the correct edge is selected

### Visualization Issues
- Adjust ScaleDraw property to change arrow size
- Ensure 3D view is refreshed (press F5)

## Limitations
- Point loads can only be applied to straight members (edges)
- Moment visualization is the same as force visualization (improvement for future versions)