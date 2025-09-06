# Concrete Material Creation Fix

## Issue Description
When selecting a concrete material standard like "ACI_Normal_30MPa" in the material selection dialog, the preview shows correct concrete properties (2400 kg/m³ density, 27000 MPa modulus, 0.2 Poisson ratio), but after clicking "Create Material", the created material shows incorrect steel properties instead (7850 kg/m³ density, 200 GPa modulus, 0.30 Poisson ratio).

## Root Cause
The issue was in the material creation workflow in the MaterialSelectionPanel. When creating new materials, the panel was not properly detecting concrete materials and was creating basic Material objects instead of StructuralMaterial objects that properly handle material standards.

## Changes Made

### 1. Updated MaterialSelectionPanel.py

#### Added `find_matching_standard` method:
- Added a method to properly identify database standards that match the selected material
- Implements pattern matching for concrete materials (looking for keywords like "concrete", "คอนกรีต", "fc", "ACI_Normal", "EN_C")
- Implements pattern matching for steel materials (looking for keywords like "steel", "astm", "en_s", "jis")

#### Enhanced `create_new_material` method:
- Now tries to create StructuralMaterial objects first (which properly support material standards)
- Properly sets MaterialType based on the material data
- Uses the new `find_matching_standard` method to set the correct material standard
- Falls back to basic Material objects if StructuralMaterial is not available

#### Enhanced `update_existing_material` method:
- Added proper handling for StructuralMaterial objects
- When updating StructuralMaterial objects, sets the material standard which automatically updates all properties
- Properly handles both StructuralMaterial and basic Material objects

### 2. Updated MaterialHelper.py

#### Enhanced `create_material_from_database` function:
- Improved material type detection for concrete materials
- Ensures StructuralMaterial objects are created when possible
- Sets the MaterialStandard property which automatically updates all material properties
- Falls back to basic Material objects with manual property setting if needed

### 3. Updated StructuralMaterial.py

#### Enhanced `_update_standard_properties` method:
- Added special handling for concrete materials
- For concrete materials, sets YieldStrength and UltimateStrength to CompressiveStrength values for compatibility
- Added more detailed debug output to help with troubleshooting
- Ensured critical properties are forcefully updated

## How the Fix Works

1. When a user selects a concrete material in the MaterialSelectionPanel, the system now properly identifies it as a concrete material
2. Instead of creating a basic Material object, it creates a StructuralMaterial object which has full support for material standards
3. The MaterialStandard property is set, which automatically triggers the `_update_standard_properties` method
4. This method properly applies all the concrete material properties from the database (2400 kg/m³ density, 27000 MPa modulus, 0.2 Poisson ratio for ACI_Normal_30MPa)
5. The material type is correctly set to "Concrete"

## Verification

The fix ensures that when creating a concrete material with the standard "ACI_Normal_30MPa", the material will have:
- Density: 2400 kg/m³ (not 7850 kg/m³)
- Modulus Elasticity: 27000 MPa (not 200000 MPa)
- Poisson Ratio: 0.2 (not 0.3)
- Material Type: Concrete (not Steel)
- Yield Strength: 30 MPa (not 345 MPa)
- Ultimate Strength: 30 MPa (not 450 MPa)

This matches the values defined in the MaterialStandards.py database and resolves the issue where concrete materials were showing steel properties after creation.