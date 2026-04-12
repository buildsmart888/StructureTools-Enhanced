# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.0] - Unreleased

### Added
- **AISC Steel Section Database**: Added 67 W-shapes (W44 through W4) with full geometric properties.
- **ACI 318 Concrete Design**: Implemented P-M Interaction Diagram generator for rectangular concrete columns (`PMInteractionDiagram`).
- **Eurocode 3 Design**: Added complete EN 1993-1-1 steel design module covering cross-section classification, flexure, shear, compression, and combined loading (`design/EC3.py`).
- **Connection Design**: Added AISC 360-22 Chapter J foundation for bolted (shear, tension, bearing) and welded connections (`design/connections.py`).
- **Foundation Design**: Added ACI 318-19 isolated spread footing design covering bearing, 1-way/2-way shear, and flexure (`design/foundations.py`).
- **Advanced Analysis**: Added wrapper for Pynite's built-in P-Delta / geometric nonlinear analysis (`analysis/pdelta.py`).
- **Interoperability**: Added SAP2000 / ETABS `$2k` text file parser and Pynite model converter (`analysis/sap2000_import.py`).
- **Real-Time Preview**: Added FreeCAD document observer for responsive, lightweight background structural analysis (`analysis/realtime_preview.py`).

### Changed
- **AISC 360 Checks**: Improved flexural checks for non-compact and slender sections per AISC 360-22 Table B4.1b, F3.2, and F5.
- **Code Organization**: Relocated scattered test files into standard directories (`tests/unit/legacy/`, `tests/unit/loads/`).

### Fixed
- Addressed `StructuralPlate` stiffness matrix concerns by confirming Pynite's native handling.
- Removed duplicate duplicate function definitions (e.g., dead `process_plates` in `model_builder.py`).
- Removed duplicate property registrations in `calc.py`.
- Deleted unused 75KB `calc_backup.py` legacy file.

## [0.0.1] - Initial Release
- Initial basic structural modeling and analysis capabilities.
