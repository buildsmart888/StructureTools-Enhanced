# Reaction Table Panel Feature Summary

## Overview
This feature adds a new tabular view for reaction results with export functionality to the StructureTools workbench. Users can now view reaction forces and moments in an easy-to-read table format and export the data to various formats.

## Key Features Implemented

### 1. Reaction Table Panel
- **Tabular Display**: Shows reaction forces and moments in a clean, organized table
- **Load Combination Selection**: Users can select which load combination to display
- **Node Information**: Displays node ID and coordinates (X, Y, Z)
- **Reaction Components**: Shows all six reaction components (FX, FY, FZ, MX, MY, MZ)
- **Sorting Capability**: Table columns can be sorted by clicking headers
- **Visual Styling**: Alternating row colors for better readability

### 2. Export Functionality
- **Multiple Formats**: Export to Excel (.xlsx), Word (.docx), and CSV (.csv)
- **Formatted Data**: Export includes proper headers and formatting
- **User-Friendly Interface**: Standard file save dialogs for selecting export location

### 3. Integration Points
- **Toolbar Button**: New "Reaction Results Table" command in the StructureResults toolbar
- **Panel Button**: "Table View" button added to the existing Reaction Results panel
- **Context Menu**: Right-click context menu option on ReactionResults objects

## Files Created/Modified

### New Files
1. `freecad/StructureTools/reaction_table_panel.py` - Main implementation of the reaction table panel
2. `freecad/StructureTools/test_reaction_table.py` - Test script for the new functionality
3. `examples/reaction_table_example.py` - Example usage script

### Modified Files
1. `freecad/StructureTools/reaction_results.py` - Added context menu option
2. `freecad/StructureTools/reaction_results_panel.py` - Added "Table View" button
3. `freecad/StructureTools/init_gui.py` - Registered new command
4. `README.md` - Updated documentation

## Usage Instructions

### Method 1: Toolbar Command
1. Select a ReactionResults object in the tree view
2. Click the "Reaction Results Table" button in the StructureResults toolbar
3. The table panel will open showing reaction data

### Method 2: Existing Panel Button
1. Double-click a ReactionResults object to open the control panel
2. Click the "Table View" button at the bottom
3. The table panel will open replacing the control panel

### Method 3: Context Menu
1. Right-click a ReactionResults object in the tree view
2. Select "Open Reaction Table" from the context menu
3. The table panel will open

## Export Options
- **Excel**: Requires `openpyxl` Python package
- **Word**: Requires `python-docx` Python package
- **CSV**: Built-in Python CSV module (no additional dependencies)

## Technical Implementation Details

### Dependencies
The feature uses standard FreeCAD PySide/PySide2 imports and optionally:
- `openpyxl` for Excel export
- `python-docx` for Word export

### Data Mapping
The table correctly maps reaction data from the Pynite model:
- **Node ID**: From `node.name`
- **Coordinates**: From `node.X`, `node.Y`, `node.Z`
- **Reactions**: From `node.RxnFX`, `node.RxnFY`, `node.RxnFZ`, `node.RxnMX`, `node.RxnMY`, `node.RxnMZ`
- **Load Combinations**: Selected from `model.LoadCombos`

### Error Handling
- Graceful handling of missing dependencies with user-friendly error messages
- Proper exception handling for file operations
- Validation of object references and data availability

## Testing
A comprehensive test script is included that verifies:
- Module imports
- Panel class availability
- Command registration
- Basic functionality

## Example Usage
An example script demonstrates creating a simple structure and using the reaction table panel with sample data.

## Future Enhancements
Potential improvements that could be added:
- Customizable column selection
- Filtering options for specific nodes or reaction components
- Unit conversion options in the table view
- Copy/paste functionality for table data
- Print/export to PDF functionality