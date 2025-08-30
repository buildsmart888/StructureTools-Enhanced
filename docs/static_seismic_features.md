# Static Seismic Analysis Features

## Overview

The StructureTools workbench now includes enhanced static seismic analysis capabilities with a professional MIDAS nGen-like interface. This implementation provides comprehensive tools for calculating and visualizing seismic forces in buildings according to ASCE 7-22 and other standards.

## New Features

### 1. Static Seismic Tab

A new tab has been added to the Seismic Load Generator interface with the following features:

- **Professional MIDAS nGen-like Interface**: Clean, organized layout matching industry standards
- **Seismic Code Selection**: Support for ASCE 7-22, TIS 1301-61, and Custom codes
- **Site and Building Characteristics**: Input for site class and risk category
- **Response Parameters**: Configuration of R, Ω₀, Cd, and Ie factors
- **Seismic Coefficients**: Direct input and display of SS, S1, SDS, and SD1 values

### 2. Story Forces Distribution

The implementation includes multiple methods for distributing seismic forces to building stories:

- **ASCE 7-22 Method**: Code-compliant distribution using the k-factor approach
- **Linear Distribution**: Simple linear distribution with height
- **Uniform Distribution**: Equal force distribution to all stories
- **Custom Distribution**: Placeholder for user-defined distributions

### 3. Vertical Component Analysis

- **Vertical Seismic Component**: Calculation of vertical seismic forces
- **ASCE 7-22 Compliance**: Default 0.2*SDS factor with customizable options
- **Toggle Option**: Enable/disable vertical component analysis

### 4. Visualization

- **Story Forces Plot**: Professional visualization of force distribution with height
- **Data Point Labels**: Clear annotation of key force values
- **Interactive Table**: Tabular display of story forces with height and weight data

### 5. Results Display

- **Base Shear Results**: Clear display of X and Y direction base shears
- **Total Weight**: Building weight summary
- **Detailed Story Data**: Complete force distribution information

## Technical Implementation

### Core Modules

1. **`seismic/story_forces.py`**: Core calculation functions for seismic force distribution
2. **`seismic/static_seismic.py`**: GUI components and analysis integration
3. **`commands/command_seismic_load_gui.py`**: Main seismic load interface with new tab

### Key Functions

- `calculate_seismic_coefficient()`: ASCE 7-22 compliant seismic coefficient calculation
- `calculate_base_shear()`: Base shear force calculation
- `distribute_forces_asce()`: ASCE 7-22 story force distribution
- `distribute_forces_linear()`: Linear story force distribution
- `distribute_forces_uniform()`: Uniform story force distribution
- `calculate_vertical_component()`: Vertical seismic force calculation

## Usage Instructions

1. **Access the Feature**: Open the Seismic Load Generator from the StructureTools toolbar
2. **Select Analysis Type**: Choose "Static Seismic" from the Analysis Type tab
3. **Configure Parameters**: Set building characteristics, site class, and risk category
4. **Set Response Parameters**: Enter R, Ω₀, Cd, and Ie factors
5. **Select Distribution Method**: Choose from ASCE 7-22, Linear, or Uniform
6. **Enable Vertical Component**: Check the box if vertical seismic forces are needed
7. **Calculate Loads**: Click "Calculate Seismic Loads" to perform the analysis
8. **Review Results**: Check the story forces distribution in the table and plot

## Code Compliance

- **ASCE 7-22**: Full compliance with ASCE 7-22 standards for static seismic analysis
- **TIS 1301-61**: Support for Thai seismic standards (additional implementation in progress)
- **Fundamental Period**: ASCE 7-22 Equation 12.8-7 for approximate period calculation
- **Seismic Coefficient**: ASCE 7-22 Section 12.8.1 equations
- **Vertical Forces**: ASCE 7-22 Section 12.4.2.2 requirements

## Future Enhancements

- Additional Thai standard implementations
- Load pattern visualization
- Multiple spectrum comparison views
- 3D visualization of load application
- More building type presets
- Enhanced error handling and validation

## Testing

Comprehensive unit tests have been implemented to verify:
- Module imports and creation
- Parameter handling
- Calculation accuracy
- Analysis workflow
- GUI component creation

Run tests with: `python -m pytest tests/unit/test_static_seismic.py -v`