# Material System Integration Guide

This guide explains the enhanced material system in StructureTools that supports both old and new material objects and integrates seamlessly with the calc object for structural analysis.

## Overview

The material system now supports two types of material objects:
1. **Legacy Material** (`material.py`) - Basic material properties, now enhanced for calc compatibility
2. **StructuralMaterial** (`objects/StructuralMaterial.py`) - Advanced material object with validation, standards, and design code integration

Both material types are fully compatible with the calc object and provide the same interface for structural analysis.

## Key Features

### Enhanced Legacy Material Support
- ✅ **Calc Compatibility**: Added `get_calc_properties()` method for seamless calc integration
- ✅ **Property Validation**: Poisson ratio validation (0.0 to 0.5 range)
- ✅ **Unit Conversion**: Automatic unit conversion for different analysis systems
- ✅ **Name Synchronization**: Automatic sync between Label and Name properties
- ✅ **Default Values**: Proper default values for structural steel (ASTM A992 equivalent)

### Advanced StructuralMaterial Features
- ✅ **Material Standards**: Built-in support for ASTM, EN, and other standards
- ✅ **Design Properties**: Yield strength, ultimate strength, fatigue properties
- ✅ **Temperature Effects**: Thermal expansion and temperature-dependent properties
- ✅ **Quality Control**: Certification levels, testing standards, and audit trails
- ✅ **Validation System**: Comprehensive property validation and warning system
- ✅ **Cost/Sustainability**: Unit cost and carbon footprint tracking

### Calc Integration
- ✅ **Automatic Detection**: Calc automatically detects and uses the appropriate material interface
- ✅ **Fallback Support**: Graceful fallback for materials without enhanced methods
- ✅ **Unit Compatibility**: Full support for different unit systems (m-kN, mm-N, etc.)
- ✅ **Plate Elements**: Enhanced material support for plate/shell elements
- ✅ **Error Handling**: Robust error handling with default material fallbacks

## Usage Examples

### Creating Materials Programmatically

```python
# Create steel material (new enhanced method)
from freecad.StructureTools.commands.CreateMaterial import create_steel_material
steel = create_steel_material("Steel_A992", "ASTM_A992")

# Create concrete material
from freecad.StructureTools.commands.CreateMaterial import create_concrete_material
concrete = create_concrete_material("Concrete_25", fc=25.0)

# Validate material for calc compatibility
from freecad.StructureTools.commands.CreateMaterial import validate_material_for_calc
is_valid = validate_material_for_calc(steel)
```

### Using Materials with Calc

```python
# Materials are automatically integrated with calc
# No special handling required - calc will detect and use appropriate interface

# For beam analysis
beam.MaterialMember = steel  # Both old and new materials work

# For plate analysis  
plate.Material = concrete  # Automatic material property extraction
```

### Manual Material Creation

#### Legacy Material (Basic)
```python
import FreeCAD as App
from freecad.StructureTools.material import Material, ViewProviderMaterial

# Create basic material
obj = App.ActiveDocument.addObject("Part::FeaturePython", "Steel")
Material(obj)
ViewProviderMaterial(obj.ViewObject)

# Set properties
obj.ModulusElasticity = "200000 MPa"
obj.PoissonRatio = 0.30
obj.Density = "7850 kg/m^3"
```

#### StructuralMaterial (Advanced)
```python
import FreeCAD as App
from freecad.StructureTools.objects.StructuralMaterial import StructuralMaterial, ViewProviderStructuralMaterial

# Create advanced material
obj = App.ActiveDocument.addObject("App::DocumentObjectGroupPython", "StructuralMaterial")
StructuralMaterial(obj)
ViewProviderStructuralMaterial(obj.ViewObject)

# Properties are set automatically based on MaterialStandard
obj.MaterialStandard = "ASTM_A992"  # Auto-populates properties
```

## Material Property Interface

Both material types support the `get_calc_properties()` method:

```python
# Get properties for calc integration
props = material.Proxy.get_calc_properties(material, unit_length='m', unit_force='kN')

# Returns dictionary with:
# {
#     'name': str,          # Material name
#     'E': float,           # Elastic modulus in target units
#     'G': float,           # Shear modulus (calculated)
#     'nu': float,          # Poisson ratio
#     'density': float,     # Density in force/volume units
#     'unit_system': str    # Unit system identifier
# }
```

## Calc Integration Details

### Material Processing Flow

1. **Detection**: Calc checks if material has `get_calc_properties()` method
2. **Enhanced Path**: Uses material's calc-compatible interface if available
3. **Fallback Path**: Uses original property extraction for legacy materials
4. **Error Handling**: Creates default material if extraction fails
5. **Unit Conversion**: Automatic conversion to calc's unit system

### Unit System Support

The material system supports multiple unit systems:
- **Metric**: m-kN, mm-N, cm-kN
- **Imperial**: ft-kip, in-kip, in-lb
- **Custom**: Any consistent length-force combination

### Validation and Error Handling

```python
# Property validation occurs automatically
material.PoissonRatio = 0.8  # Invalid - automatically corrected to 0.3

# Comprehensive error messages in FreeCAD console
# Warnings for property inconsistencies
# Fallback values for missing properties
```

## GUI Integration

### Material Creation Commands
- **Original Command**: `material` - Creates basic Material object
- **Enhanced Command**: `CreateMaterial` - Creates StructuralMaterial with options
- **Utility Functions**: `create_steel_material()`, `create_concrete_material()`

### Task Panels (Planned)
- Material creation wizard with standard selection
- Property editing panel with real-time validation  
- Material database browser with import/export

### Visual Indicators
- Dynamic icons showing material type and validation status
- Color-coded validation warnings in property editor
- Tooltip information with material specifications

## Migration Guide

### Updating Existing Models

Existing models with old materials will continue to work without modification:

1. **No Breaking Changes**: Old materials retain full functionality
2. **Enhanced Features**: Old materials gain calc compatibility automatically
3. **Validation**: Existing property values are validated on first load
4. **Upgrading**: Can replace old materials with StructuralMaterial for enhanced features

### Best Practices

1. **New Projects**: Use `CreateMaterial` command for enhanced features
2. **Legacy Projects**: Keep existing materials or selectively upgrade
3. **Standards Compliance**: Use StructuralMaterial for projects requiring design code compliance
4. **Performance**: Both material types have equivalent calc performance

## Technical Implementation

### File Structure
```
freecad/StructureTools/
├── material.py                        # Enhanced legacy Material class
├── objects/StructuralMaterial.py      # Advanced StructuralMaterial class  
├── commands/CreateMaterial.py         # Material creation commands
├── data/MaterialStandards.py         # Material standards database
└── calc.py                           # Enhanced with material integration
```

### Key Methods

#### Material Classes
- `get_calc_properties(obj, unit_length, unit_force)` - Calc interface
- `onChanged(obj, prop)` - Property validation
- `execute(obj)` - Property updates and validation

#### Calc Integration  
- `setMaterialAndSections()` - Enhanced material processing
- Material detection and fallback logic
- Plate element material handling

## Troubleshooting

### Common Issues

1. **Material Not Found in Calc**
   - Check that material has `Name` property
   - Verify material is assigned to structural element
   - Check FreeCAD console for error messages

2. **Property Validation Errors**
   - Poisson ratio must be 0.0-0.5
   - Elastic modulus must be positive
   - Density must be positive

3. **Unit Conversion Issues**
   - Verify property units match expected format
   - Check calc unit settings (LengthUnit, ForceUnit)
   - Use material's `get_calc_properties()` for debugging

### Debug Information

Enable detailed material processing information:
```python
# In FreeCAD Python console
App.Console.PrintMessage("Material debugging enabled\n")
# Material validation messages will appear in console
```

## Future Enhancements

### Planned Features
- Material database with import/export
- Temperature-dependent analysis
- Nonlinear material models
- Composite material support
- Material optimization tools

### API Extensions
- REST API for material database
- Plugin architecture for custom materials
- Integration with external material libraries
- Cloud synchronization for material libraries

---

This enhanced material system provides a solid foundation for professional structural analysis while maintaining backward compatibility with existing models and workflows.