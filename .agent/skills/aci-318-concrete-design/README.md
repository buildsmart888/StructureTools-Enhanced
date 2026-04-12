# ACI 318-25 Concrete Design Skill

**Comprehensive Claude Code skill for reinforced and prestressed concrete structural design per ACI 318-25**

---

## Overview

This skill provides expert-level assistance with concrete structural design using ACI 318-25 (Building Code for Structural Concrete). It includes:

- **Complete ACI 318-25 documentation** (CODE + COMMENTARY)
- **Intelligent search** across all chapters
- **Formula extraction** with variable definitions
- **Exposure class selection guide** (F/W/C/S series)
- **Seismic design category guide** (SDC A-F)
- **Automated calculation workflows**

## Quick Start

### Basic Usage

Simply ask questions about concrete design, and the skill will automatically activate:

```
"What is the shear strength formula for concrete beams?"
"How to select exposure class for a parking garage?"
"Show me SDC D special moment frame requirements"
"Calculate development length for #8 bars, f'c=5000 psi"
```

### Trigger Keywords

**English**: ACI 318, concrete, reinforced concrete, slab, beam, column, wall, foundation, shear, flexure, exposure class, seismic, SDC

**Korean**: ACI 318, 콘크리트, 철근콘크리트, 슬래브, 보, 기둥, 벽체, 기초, 전단, 휨, 노출등급, 내진

## Features

### 1. Document Search

Search across 40,000+ lines of consolidated ACI 318-25 documentation:

```bash
# Smart keyword search
python3 scripts/smart_search.py "beam shear" --max-results 10

# Search without commentary
python3 scripts/smart_search.py "exposure class" --no-commentary
```

### 2. Formula Extraction

Extract formulas with full context and variable definitions:

```bash
# Find all shear formulas in Chapter 22.5
python3 scripts/formula_finder.py --pattern "V_c" --section "22.5"

# Include commentary
python3 scripts/formula_finder.py --pattern "M_n" --commentary
```

### 3. Exposure Class Selection

Interactive guide for determining exposure classes (F/W/C/S):

- **F-Series**: Freezing and thawing (F0, F1, F2, F3)
- **W-Series**: Water penetration (W0, W1, W2)
- **C-Series**: Corrosion protection (C0, C1, C2)
- **S-Series**: Sulfate attack (S0, S1, S2, S3)

See `references/exposure-guide.md` for complete flowchart.

### 4. Seismic Design Guidance

System selection and detailing requirements by SDC:

- **SDC A**: No special seismic requirements
- **SDC B**: Ordinary systems + basic detailing
- **SDC C**: Intermediate systems
- **SDC D/E/F**: Special systems with stringent detailing

See `references/seismic-categories.md` for complete guide.

## Directory Structure

```
.claude/skills/aci-318-concrete-design/
├── SKILL.md                          # Main skill file (30+ KB)
├── README.md                         # This file
├── consolidation_metadata.txt        # Processing metadata
│
├── data/                             # Consolidated ACI 318-25 content
│   ├── code/                         # CODE sections (9 part files)
│   │   ├── Part_1_General.md
│   │   ├── Part_2_Loads_Analysis.md
│   │   ├── Part_3_Members.md         # Chapters 7-13
│   │   ├── Part_4_Joints_Connections.md
│   │   ├── Part_5_Earthquake_Resistance.md
│   │   ├── Part_6_Materials_Durability.md
│   │   ├── Part_7_Strength_Serviceability.md
│   │   ├── Part_8_Construction.md
│   │   └── Part_10_Evaluation.md
│   │
│   ├── commentary/                   # COMMENTARY sections (9 files)
│   │   ├── Commentary_Part_1_General.md
│   │   ├── Commentary_Part_2_Loads_Analysis.md
│   │   └── ... (corresponding to CODE files)
│   │
│   ├── appendices/                   # 4 appendices
│   │   ├── Appendix_A_Nonlinear_Analysis.md
│   │   ├── Appendix_B_Performance_Wind.md
│   │   ├── Appendix_C_Sustainability.md
│   │   └── Appendix_D_Steel_Info.md
│   │
│   └── Notation_Symbols.md           # Chapter 2 notation
│
├── scripts/                          # Python automation tools
│   ├── consolidate_pages.py          # Page consolidation (already run)
│   ├── smart_search.py               # Intelligent keyword search
│   └── formula_finder.py             # Formula extraction
│
└── references/                       # Quick reference guides
    ├── exposure-guide.md             # F/W/C/S exposure class selection
    └── seismic-categories.md         # SDC A-F seismic requirements
```

## Data Files Summary

| Category | Files | Size | Content |
|----------|-------|------|---------|
| CODE | 9 parts | ~1.2 MB | Mandatory requirements |
| COMMENTARY | 9 parts | ~1.0 MB | Background and rationale |
| Appendices | 4 files | ~0.3 MB | Advanced topics |
| Notation | 1 file | ~50 KB | Symbols and definitions |
| **Total** | **23 files** | **~2.5 MB** | **40,000+ lines** |

## Common Workflows

### 1. Formula Lookup

**Query**: "What is the formula for beam shear strength?"

**Response includes**:
- Formula from ACI 318-25 Section 22.5.5.1
- Variable definitions (Vc, λ, √f'c, bw, d)
- Equation number
- Context from CODE
- Explanation from COMMENTARY

### 2. Exposure Class Selection

**Query**: "What exposure class for parking garage deck?"

**Response includes**:
- F3 (de-icing salts + saturation)
- C2 (chloride exposure)
- W1 (water penetration)
- Required: f'c ≥ 5,000 psi, w/cm ≤ 0.40, air-entrainment
- Minimum cover: 2.5"

### 3. Seismic Design Requirements

**Query**: "What are SDC D special moment frame requirements?"

**Response includes**:
- System: Special Moment Frame (SMF) per Section 17.5
- Strong-column/weak-beam requirement
- Confinement reinforcement details
- Hoop spacing requirements
- Joint shear verification
- Boundary element requirements (if walls)

### 4. Design Calculation

**Query**: "Calculate beam flexural capacity: b=12 in, d=20 in, As=4 in², f'c=4000 psi, fy=60 ksi"

**Response includes**:
- Formula from Section 22.3
- Step-by-step calculation
- Strain compatibility check
- φ factor determination (tension vs compression-controlled)
- Final φMn value
- Check against minimum reinforcement

## Chapter Quick Reference

### Members (Part 3)
- **Chapter 7**: One-Way Slabs
- **Chapter 8**: Two-Way Slabs
- **Chapter 9**: Beams
- **Chapter 10**: Columns
- **Chapter 11**: Walls
- **Chapter 12**: Diaphragms
- **Chapter 13**: Foundations

### Strength (Part 7)
- **Chapter 21**: Strength Reduction Factors (φ)
- **Chapter 22**: Sectional Strength (Mn, Vn, Pn)
- **Chapter 23**: Strut-and-Tie Method
- **Chapter 24**: Serviceability
- **Chapter 25**: Reinforcement Details

### Seismic (Part 5)
- **Chapter 17**: Earthquake-Resistant Structures
  - 17.2: General requirements (SDC B+)
  - 17.5: Special Moment Frames (SDC D/E/F)
  - 17.6: Intermediate Moment Frames (SDC C)
  - 17.7: Special Structural Walls (SDC D/E/F)

### Durability (Part 6)
- **Chapter 19**: Exposure Classes (F/W/C/S)
- **Chapter 20**: Steel Reinforcement, Cover

## Exposure Classes Summary

| Class | Condition | Example | Requirements |
|-------|-----------|---------|--------------|
| **F0** | No freezing | Interior | Minimal |
| **F1** | Moderate freeze | Exterior walls | w/cm ≤ 0.55 |
| **F2** | Severe freeze | Exterior slabs | w/cm ≤ 0.50, air |
| **F3** | Very severe + salts | Bridge decks | w/cm ≤ 0.45, air |
| **W0** | No water | Interior | Minimal |
| **W1** | Low permeability | Basement walls | w/cm ≤ 0.50 |
| **W2** | Very low permeability | Water tanks | w/cm ≤ 0.40 |
| **C0** | Dry | Interior dry | Minimal |
| **C1** | Moisture, no chlorides | Interior wet | w/cm ≤ 0.50 |
| **C2** | Chloride exposure | Parking, marine | w/cm ≤ 0.40 |
| **S0** | No sulfates | Most soils | Minimal |
| **S1** | Moderate sulfates | Some soils | Type II cement |
| **S2** | Severe sulfates | High sulfate soil | SR cement |
| **S3** | Very severe sulfates | Rare | Special protection |

## Seismic Design Categories Summary

| SDC | System | Chapter 17 | Key Requirements |
|-----|--------|------------|------------------|
| **A** | Ordinary | Not applicable | No special requirements |
| **B** | Ordinary | 17.2 | Basic detailing |
| **C** | Intermediate | 17.2, 17.6, 17.9 | Enhanced detailing |
| **D/E/F** | Special | Full Chapter | Stringent detailing |

## Technical Specifications

- **ACI Version**: ACI CODE-318-25 (2025 edition)
- **Units**: Inch-Pound (IN-LB)
- **Publisher**: American Concrete Institute
- **Total Pages**: 702 (original), consolidated to 23 files
- **Chapters**: 27 chapters + 4 appendices

## Development Notes

### Consolidation Process

Original 702 individual page markdown files were consolidated into logical chapter-based files:

1. **Split by Part**: Organized into 9 major parts
2. **Separate CODE/COMMENTARY**: Independent files for each
3. **Extract Notation**: Chapter 2 symbols in dedicated file
4. **Appendices**: 4 separate appendix files

### Scripts Developed

1. **consolidate_pages.py**: Merged 702 pages into 23 files (✅ completed)
2. **smart_search.py**: Keyword-based intelligent search (✅ completed)
3. **formula_finder.py**: Formula extraction with context (✅ completed)

### Future Enhancements

- [ ] `cross_reference.py`: Map section dependencies
- [ ] `exposure_selector.py`: Interactive exposure class tool
- [ ] `seismic_checker.py`: SDC requirement validator
- [ ] `validate_design.py`: Design compliance checker
- [ ] Additional reference guides (formulas index, terminology)

## Usage Examples

### Example 1: Search for Requirements

```python
# Find beam minimum dimensions
python3 scripts/smart_search.py "minimum beam width" --max-results 5
```

### Example 2: Extract Formulas

```python
# Find all development length formulas
python3 scripts/formula_finder.py --pattern "ld =" --section "25"
```

### Example 3: Read Specific Section

```bash
# Read Chapter 9 (Beams) CODE requirements
cat data/code/Part_3_Members.md | grep -A 20 "CHAPTER 9"
```

## Support and Documentation

- **SKILL.md**: Complete workflow documentation
- **exposure-guide.md**: Exposure class selection flowchart
- **seismic-categories.md**: SDC requirements and system selection
- **Notation_Symbols.md**: Symbol definitions from Chapter 2

## License and Copyright

- **Source**: ACI CODE-318-25 © American Concrete Institute
- **Skill**: Developed for educational and professional use
- **Note**: Original ACI 318-25 document is copyrighted material

---

**Version**: 1.0
**Created**: 2025-11-14
**Last Updated**: 2025-11-14

For issues or questions, refer to the SKILL.md file for detailed workflows.
