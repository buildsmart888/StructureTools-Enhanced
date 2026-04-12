# AISC Steel Design Standards Skill

**Claude Code Skill for AISC 360-22 Specification and Design Examples v16.0**

**Created**: 2025-11-09
**Version**: 1.0
**Status**: Production Ready

---

## Overview

This Claude Code skill provides comprehensive access to:

1. **AISC 360-22 Specification** - Official design code for structural steel buildings
2. **Design Examples v16.0** - Step-by-step applications of the specification

**Purpose**: Enable AI-powered structural steel design workflows including formula lookup, example matching, calculation assistance, and cross-referencing between code requirements and practical applications.

---

## Quick Start

### Typical Queries

```
"What is the formula for lateral-torsional buckling strength?"
→ Returns: Formula from Chapter F with variable definitions

"Show me an example of W-shape beam design"
→ Returns: Example F.1-1A with step-by-step LRFD/ASD calculations

"Calculate flexural strength: W18x50, Fy=50ksi, Lb=15ft"
→ Returns: Python calculation following AISC procedures

"What does Cb mean?"
→ Returns: Symbol definition from symbols.md

"Compare LRFD and ASD"
→ Returns: Design philosophy comparison from Chapter B
```

### Using Automation Scripts

```bash
# Search for relevant chapters
python3 scripts/smart_search.py "beam flexure"

# Find specific formulas
python3 scripts/formula_finder.py "Mn =" "Chapter_F"

# Match examples to query
python3 scripts/example_matcher.py "column compression"

# Cross-reference specification and examples
python3 scripts/cross_reference.py "Chapter_E"
```

---

## Directory Structure

```
aisc-steel-design/
├── SKILL.md              # Main skill definition (how Claude uses this)
├── CHANGES.md            # Consolidation methodology
├── README.md             # This file (user guide)
│
├── data/                 # Core documents (30 chapter files, ~2.1 MB)
│   ├── specification/    # AISC 360-22 Chapters A-N (14 files)
│   │   ├── Chapter_A_General_Provisions.md
│   │   ├── Chapter_E_Compression.md
│   │   ├── Chapter_F_Flexure.md
│   │   ├── Chapter_J_Connections.md
│   │   └── ...
│   │
│   └── design-examples/  # Design Examples v16.0 (16 files)
│       ├── Part_I/       # Specification-based examples (11 chapters)
│       │   ├── Chapter_E_Compression_Members.md
│       │   ├── Chapter_F_Flexural_Members.md
│       │   └── ...
│       ├── Part_II/      # Connection examples (4 chapters)
│       │   ├── Chapter_IIA_Simple_Shear_Connections.md
│       │   ├── Chapter_IIB_Moment_Connections.md
│       │   └── ...
│       └── Part_III/     # Building system example (1 chapter)
│           └── Chapter_Building_System_Analysis.md
│
├── references/           # Quick lookup materials (7 files, ~170 KB)
│   ├── symbols.md                     # 100+ engineering symbols
│   ├── glossary.md                    # 150+ technical terms
│   ├── abbreviations.md               # Standard abbreviations
│   ├── specification-structure.md     # Complete ToC
│   ├── design-examples-index.md       # 93 examples indexed
│   ├── conventions.md                 # Design methodology
│   └── key-modifications-360-22.md    # 2022 edition changes
│
└── scripts/              # Automation tools (5 Python scripts)
    ├── extract_front_matter.py        # Extract reference materials
    ├── smart_search.py                # Keyword → chapter mapping
    ├── formula_finder.py              # Extract formulas with context
    ├── example_matcher.py             # Match queries to examples
    └── cross_reference.py             # Link Spec ↔ Examples
```

---

## Document System

### Two-Tier Architecture

#### 1. AISC 360-22 Specification (Code Requirements)

**Location**: `data/specification/` (14 chapter files)

**What it provides**:
- Official design formulas and equations
- Limit states and design requirements
- Material properties and resistance factors
- Code provisions you **must** follow

**When to use**:
- Need official formula or requirement
- Want to understand code provisions
- Looking up resistance factors (φ) or safety factors (Ω)
- Checking limit states (yielding, buckling, rupture, etc.)

**Chapter Topics**:
| Chapter | Topic | Key Content |
|---------|-------|-------------|
| A | General | Scope, materials, design documents |
| B | Design Requirements | LRFD vs ASD, loads, analysis |
| C | Stability | Direct analysis, second-order effects |
| D | Tension | Net area, tensile strength |
| E | Compression | Flexural/torsional buckling, KL/r |
| F | Flexure | Lateral-torsional buckling, Cb, Lb |
| G | Shear | Web shear, tension field action |
| H | Combined Forces | P-M interaction, torsion |
| I | Composite | Shear studs, effective width |
| J | Connections | Bolts, welds, bearing, block shear |
| K | HSS Connections | Hollow structural sections |
| L | Serviceability | Deflection limits |
| M | Fabrication | Fabrication requirements |
| N | Quality | QC/QA procedures |

#### 2. Design Examples v16.0 (Step-by-Step Applications)

**Location**: `data/design-examples/Part_I/`, `Part_II/`, `Part_III/` (16 chapter files)

**What it provides**:
- Worked examples with calculations
- LRFD and ASD shown side-by-side
- Step-by-step design procedures
- Practical application of formulas

**When to use**:
- Need to see how to apply a formula
- Want step-by-step calculation procedure
- Learning a new design topic
- Validating your own calculations

**Organization**:
- **Part I** (11 chapters): Member design (follows Spec Chapters A-K)
- **Part II** (4 chapters): Connection design (60+ examples)
  - II-A: Simple shear connections (27 examples)
  - II-B: Moment connections (15+ examples)
  - II-C: Bracing connections
  - II-D: Miscellaneous connections
- **Part III** (1 chapter): 4-story building system analysis

---

## Reference Files

### Symbols (symbols.md)

**100+ engineering symbols** from AISC 360-22 with definitions, units, and section references.

**Format**: Symbol | Definition | Units | Section

**Example**:
```
Cb = Lateral-torsional buckling modification factor | dimensionless | F2.2
Fcr = Critical stress | ksi | E3
φ = Resistance factor | dimensionless | B3.1
```

### Glossary (glossary.md)

**150+ technical terms** precisely defined per AISC 360-22.

**Key terms**:
- Allowable strength vs Nominal strength
- Compact vs Non-compact vs Slender sections
- Effective length factor
- Lateral-torsional buckling
- Limit states (yielding, rupture, buckling, etc.)
- Resistance factor (LRFD) vs Safety factor (ASD)

### Design Examples Index (design-examples-index.md)

**93 worked examples** mapped by topic and example number.

**Format**: Example number | Description | Location

**Example**:
```
E.1A: W-shape column, KL/r approach | Part_I/Chapter_E
F.1-1A: W-shape beam, simply supported | Part_I/Chapter_F
II-A.1: Simple shear connection, bolted | Part_II/Chapter_IIA
```

---

## Automation Scripts

### 1. smart_search.py - Keyword Search

**Purpose**: Find relevant chapters based on keywords

**Usage**:
```bash
python3 scripts/smart_search.py "lateral-torsional buckling"
python3 scripts/smart_search.py "bolt connection"
```

**Output**: JSON with matched chapters and files

**Keyword mapping**:
- "flexure" → Chapters F, H
- "compression" → Chapters E, H
- "connection" → Chapters J, K, Part II
- "composite" → Chapter I

### 2. formula_finder.py - Formula Extraction

**Purpose**: Extract formulas with context from Specification

**Usage**:
```bash
python3 scripts/formula_finder.py "Mn =" "Chapter_F"
python3 scripts/formula_finder.py "φ =" --all
python3 scripts/formula_finder.py "Fcr" "Chapter_E"
```

**Output**: JSON with formula, line number, ±5 lines context, section number

### 3. example_matcher.py - Example Matching

**Purpose**: Match user queries to appropriate examples

**Usage**:
```bash
python3 scripts/example_matcher.py "W-shape beam flexure"
python3 scripts/example_matcher.py "column compression"
```

**Output**: JSON with top 5 matching examples and previews

### 4. cross_reference.py - Cross-Referencing

**Purpose**: Link Specification chapters to related examples

**Usage**:
```bash
python3 scripts/cross_reference.py "Chapter_E"
python3 scripts/cross_reference.py "F" --show-examples
```

**Output**: JSON mapping showing Spec file, Example files, citations

### 5. extract_front_matter.py - Reference Extraction

**Purpose**: Extract symbols, glossary, etc. from page files

**Usage**:
```bash
python3 scripts/extract_front_matter.py
```

**Output**: 7 reference markdown files in `references/`

**Note**: Already executed during skill setup. Only re-run if page files change.

---

## Usage Patterns

### Formula Lookup

**Workflow**:
1. Ask: "What is the formula for lateral-torsional buckling?"
2. Claude searches: `data/specification/Chapter_F_Flexure.md`
3. Returns: Formula + variable definitions from `references/symbols.md`
4. Cites: AISC 360-22 Section F2.2

### Example-Based Learning

**Workflow**:
1. Ask: "Show me how to design a W-shape beam"
2. Claude checks: `references/design-examples-index.md`
3. Identifies: Example F.1-1A
4. Reads: `data/design-examples/Part_I/Chapter_F_Flexural_Members.md`
5. Returns: Step-by-step with LRFD/ASD

### Calculation Assistance

**Workflow**:
1. Ask: "Calculate flexural strength: W18x50, Fy=50ksi, Lb=15ft, Cb=1.0"
2. Claude finds: Formula from Specification Chapter F
3. Claude references: Example F.1-1A for methodology
4. Generates: Python code following example structure
5. Executes: Calculation with validation

### Cross-Referencing

**Workflow**:
1. Ask: "Show me examples using Chapter E formulas"
2. Claude uses: `scripts/cross_reference.py "Chapter_E"`
3. Returns: Specification Section + Matching examples
4. Presents: Side-by-side formula and application

---

## Design Methods: LRFD vs ASD

### LRFD (Load and Resistance Factor Design)

**Equation**: Design Strength ≥ Required Strength
**Format**: φ × Nominal Strength ≥ Σ (Load Factor × Load)

**Resistance Factors (φ)**:
- Flexure (yielding): φ = 0.90
- Compression (buckling): φ = 0.90
- Shear: φ = 0.90 or 1.00
- Bolts (shear): φ = 0.75
- Bolts (bearing): φ = 0.75

**Load Combinations**: ASCE/SEI 7-22 (1.2D + 1.6L, etc.)

### ASD (Allowable Strength Design)

**Equation**: Allowable Strength ≥ Required Strength
**Format**: Nominal Strength / Ω ≥ Σ Loads

**Safety Factors (Ω)**:
- Flexure (yielding): Ω = 1.67
- Compression (buckling): Ω = 1.67
- Shear: Ω = 1.50 or 1.67
- Bolts (shear): Ω = 2.00
- Bolts (bearing): Ω = 2.00

**Load Combinations**: ASCE/SEI 7-22 (D + L, etc.)

### Key Point

Both methods yield **equivalent safety** - same nominal strength, different factors.

---

## File Statistics

| Category | Files | Total Size | Avg Size |
|----------|------:|-----------:|---------:|
| **Specification** | 14 | 428 KB | 31 KB |
| **Design Examples** | 16 | 1.73 MB | 108 KB |
| **References** | 7 | 170 KB | 24 KB |
| **Scripts** | 5 | ~20 KB | 4 KB |
| **Documentation** | 3 | ~30 KB | 10 KB |
| **TOTAL** | 45 | 2.38 MB | - |

---

## Version Information

**AISC 360-22 Specification**:
- Standard: ANSI/AISC 360-22
- Published: August 1, 2022
- Revised: September 2023
- Replaces: AISC 360-16

**Design Examples v16.0**:
- Companion to: 16th Edition AISC Steel Construction Manual
- Follows: AISC 360-22 Specification
- Includes: ASCE/SEI 7-22 load combinations

---

## Typical Material Properties

**Steel (unless specified otherwise)**:
- Fy = 50 ksi (Grade 50 for W-shapes, typical)
- Fu = 65 ksi (Grade 50)
- E = 29,000 ksi (modulus of elasticity)

**Concrete (composite design)**:
- f'c = 4 ksi (normal-weight concrete, typical)
- wc = 145 pcf (normal-weight)

**Bolts**:
- ASTM A325: Commonly referenced
- ASTM A490: High-strength

**Welds**:
- E70 electrodes: Common for fillet and groove welds

---

## Example Numbering System

**Format**: `{Chapter}.{Number}{Variant}`

**Examples**:
- `E.1A`: Chapter E, Example 1, Variant A
- `F.1-1A`: Chapter F, Example 1-1, Variant A
- `II-A.1`: Part II, Chapter A, Example 1

**LRFD vs ASD variants**:
- Many examples show **both methods side-by-side**
- Same example number, different columns on page

---

## Related Files (Parent Directory)

**In `/Users/hi/2025OFFICEWORK/AISC_Engineer/`**:

- `a360_chapters/`: Consolidated Specification chapters (source for skill)
- `Design_ex_chapters/`: Consolidated Example chapters (source for skill)
- `a360_markdown/`: Original page-level Specification files (780 pages)
- `Design_ex_markdown/`: Original page-level Example files (1,049 pages)
- `scripts/`: Consolidation scripts (original consolidation tools)
- `MARKDOWN_CONSOLIDATION_GUIDE.md`: General consolidation methodology

---

## Troubleshooting

### Script Errors

**"File not found"**:
- Verify you're running from `scripts/` directory
- Check that `data/` and `references/` directories exist
- Ensure chapter files were copied correctly

**"Module not found"**:
- Scripts use only Python standard library
- Requires Python 3.6+

### Search Not Finding Results

**"No matches found"**:
- Try broader keywords ("beam" vs "lateral-torsional buckling")
- Check spelling
- Use `smart_search.py` to see keyword→chapter mapping

---

## Contribution Guidelines

**If adding new reference files**:
1. Extract from original page files using similar methodology
2. Add metadata header (Source, Extracted date, Format)
3. Clean headers/footers consistently
4. Update this README

**If modifying scripts**:
1. Maintain Python 3.6+ compatibility
2. Use standard library only (no external dependencies)
3. Add docstrings and usage examples
4. Output JSON for easy parsing

---

## Support

**For AISC skill questions**:
- See `SKILL.md` for Claude Code skill definition
- See `CHANGES.md` for consolidation methodology
- See parent `MARKDOWN_CONSOLIDATION_GUIDE.md` for general approach

**For AISC technical questions**:
- Refer to official AISC website: https://www.aisc.org/
- Consult AISC 360-22 Specification (official PDF)
- Consult Design Examples v16.0 (official publication)

---

**Last Updated**: 2025-11-09
**Skill Status**: Production Ready
**Total Documentation**: ~2.5 MB optimized for AI context windows
