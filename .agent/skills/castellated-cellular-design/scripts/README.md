# Castellated and Cellular Beam Design Scripts

Python automation scripts for AISC Design Guide 31: Castellated and Cellular Beam Design.

## Overview

This directory contains 6 Python scripts that automate calculations, searches, and example matching for castellated and cellular beam design per AISC Design Guide 31.

## Scripts

### 1. geometry_calculator.py (CORE)

**Purpose**: Calculate expanded beam geometry and tee section properties from parent W-section.

**Features**:
- Calculate expanded depth (dg) for castellated or cellular beams
- Compute tee section properties (Atop, Abot, Itop, Ibot, Stop, Sbot)
- Generate expanded beam nomenclature (e.g., "CB27x35", "LB32x44")
- Support for both castellated (hexagonal) and cellular (circular) openings

**Usage**:
```bash
# Castellated beam with 60° hexagonal openings
python3 geometry_calculator.py W18x35 --type CB --opening-height 5.5 --spacing 16.5

# Cellular beam with circular openings
python3 geometry_calculator.py W21x44 --type LB --diameter 14.0 --spacing 21.0

# Interactive mode
python3 geometry_calculator.py --interactive
```

**Key Formulas**:
- Castellated: dg = d + ho, ho = (√3/2) × e
- Cellular: dg = d + Do
- Tee properties: Atee, Itee, Stee calculated from parent section division

**Database**: Includes 16 standard W-sections (W18, W21, W24, W27, W30 series)

---

### 2. vierendeel_calculator.py (CORE)

**Purpose**: Calculate Vierendeel bending moments, axial forces, and interaction ratios at web openings.

**Features**:
- Calculate Vierendeel moments for noncomposite beams (Equations 3-3 to 3-8)
- Calculate Vierendeel moments for composite beams (Equations 3-10 to 3-18)
- Account for concrete deck shear contribution in composite sections
- Check AISC combined forces interaction (H1-1a, H1-1b)

**Usage**:
```bash
# Noncomposite castellated beam
python3 vierendeel_calculator.py --shear 25.0 --type CB --opening-width 11.0 \
  --Atee 5.5 --deffec 16.0

# Composite cellular beam
python3 vierendeel_calculator.py --shear 30.0 --type LB --diameter 14.0 \
  --composite --Vc 5.0 --Ag 10.5 --deffec 18.0

# Interaction check only
python3 vierendeel_calculator.py --interaction --Pr 50 --Pn 120 --Mr 80 --Mn 150
```

**Key Formulas**:
- Noncomposite castellated: Mvr = Vr × (e/2)
- Noncomposite cellular: Mvr = Vr × (Do/4)
- Composite: Vr,net = Vr - Vc, then apply area ratios
- Interaction: Pr/Pn + (8/9)Mr/Mn ≤ 1.0 (H1-1a)

---

### 3. webpost_checker.py (CORE)

**Purpose**: Validate web post buckling capacity and check utilization ratios.

**Features**:
- Calculate web post plastic moment Mp (Equation 3-22)
- Calculate critical elastic buckling moment Mocr (Equations 3-23 to 3-28)
- Apply angle-dependent resistance factors (θ = 45° to 60°)
- Check minimum spacing ratios (s/dp or S/dp)
- Support both LRFD and ASD design methods

**Usage**:
```bash
# Castellated beam (60° hexagonal)
python3 webpost_checker.py --type CB --ho 5.5 --e 11.0 --S 16.5 \
  --tw 0.3 --b 6.0 --Vrh 8.5

# Cellular beam
python3 webpost_checker.py --type LB --Do 14.0 --s 21.0 --tw 0.2 --Vrh 10.0 --ASD
```

**Key Formulas**:
- Castellated: Mp = 0.25 × tw × (e + 2b)² × Fy
- Mocr/Mp from Equations 3-23 to 3-28 (function of θ, e/ho, 2h/e)
- Resistance factors: φb = 0.90 (θ = 60°), φb = 0.60 (θ = 52.5°), interpolate
- Available strength: φMn = φb × Mocr (LRFD)

**Warnings**:
- Warns if S/dp < 1.08 for castellated beams
- Warns if s/Do < 1.5 for cellular beams

---

### 4. smart_search.py (UTILITY)

**Purpose**: Category-aware keyword search across Design Guide 31 chapters and examples.

**Features**:
- Search by category (manufacturing, vierendeel, webpost, etc.)
- Search specific chapters (1, 2, 3) or examples only
- Relevance ranking with formula detection
- Context extraction around matches

**Usage**:
```bash
# Search by category
python3 smart_search.py "Vierendeel bending" --category vierendeel

# Search specific chapter
python3 smart_search.py "web post buckling" --chapter 3

# Search examples only
python3 smart_search.py "W18x35" --examples-only

# Verbose output with context
python3 smart_search.py "Equation 3-3" --verbose
```

**Categories**:
- `manufacturing`: Manufacturing, cutting patterns, nomenclature
- `applications`: Use cases, long span, advantages
- `vierendeel`: Vierendeel bending, local forces, Equations 3-3 to 3-18
- `webpost`: Web post buckling, Equations 3-22 to 3-36
- `shear`: Vertical shear, gross/net section
- `deflection`: Deflection, stiffness, camber
- `ltb`: Lateral-torsional buckling, unbraced length
- `composite`: Composite action, concrete deck, PNA
- `examples`: All worked examples

---

### 5. formula_finder.py (UTILITY)

**Purpose**: Extract formulas and equations from design guide with context and variable definitions.

**Features**:
- Search by equation number (e.g., "3-3", "3-10a")
- Search by keyword near formulas
- Extract LaTeX math expressions
- Parse "where" sections for variable definitions
- Configurable context lines

**Usage**:
```bash
# Find specific equation
python3 formula_finder.py "3-3" --chapter 3

# Find formulas with keyword
python3 formula_finder.py "Vierendeel" --file Chapter_3_Design_Procedures.md

# Find all formulas in a file
python3 formula_finder.py --file Chapter_3_Design_Procedures.md --all-formulas

# Search in example
python3 formula_finder.py "Mvr" --example 4.1
```

**Detection Patterns**:
- Equation references: "Equation 3-3", "(3-10a)"
- LaTeX math: `$$...$$`, `$...$`
- Assignment: `M_vr =`, `V_r =`
- Greek symbols: φ, Ω, λ, θ
- Engineering notation: f_y, M_n, V_r, P_n, T_0

---

### 6. example_matcher.py (UTILITY)

**Purpose**: Match user design requirements to appropriate worked examples from Design Guide 31.

**Features**:
- Decision tree for example selection
- Match by composite action (yes/no)
- Match by beam type (CB/LB)
- Comparison table of all examples
- Display example details and key checks

**Usage**:
```bash
# Select by criteria
python3 example_matcher.py --composite --type CB

# Noncomposite cellular beam
python3 example_matcher.py --no-composite --type LB

# Interactive decision tree
python3 example_matcher.py --interactive

# Show specific example
python3 example_matcher.py --example 4.3

# Show comparison table
python3 example_matcher.py --compare
```

**Example Matrix**:
```
                 Castellated (CB)      Cellular (LB)
Noncomposite     Example 4.1           Example 4.2
Composite        Example 4.3           Example 4.4
```

**Example Details**:
- Example 4.1: Noncomposite CB, W18x35→CB27x35, 60 ft span
- Example 4.2: Noncomposite LB, W21x44→LB32x44, 50 ft span
- Example 4.3: Composite CB, W18x35→CB27x35, 60 ft span, 3" deck
- Example 4.4: Composite LB, W21x44→LB32x44, 50 ft span, 3" deck

---

## Common Workflows

### 1. Design New Castellated Beam

```bash
# Step 1: Calculate geometry
python3 geometry_calculator.py W18x35 --type CB --opening-height 5.5

# Step 2: Check Vierendeel bending
python3 vierendeel_calculator.py --shear 25.0 --type CB --opening-width 11.0 \
  --Atee 5.9 --deffec 16.19

# Step 3: Check web post buckling
python3 webpost_checker.py --type CB --ho 5.5 --e 11.0 --S 16.5 \
  --tw 0.3 --b 6.0 --Vrh 8.5

# Step 4: Find relevant example
python3 example_matcher.py --no-composite --type CB
```

### 2. Find Design Information

```bash
# Search for specific topic
python3 smart_search.py "composite beam design" --category composite

# Find specific equation
python3 formula_finder.py "3-17" --chapter 3

# Locate worked example
python3 example_matcher.py --compare
```

### 3. Verify Calculation

```bash
# Find example calculation
python3 example_matcher.py --example 4.1

# Extract relevant formulas
python3 formula_finder.py "Equation 3-7" --chapter 3

# Search for guidance
python3 smart_search.py "web post spacing" --verbose
```

---

## Design Methods

All calculation scripts support both LRFD and ASD:

**LRFD (default)**:
```bash
python3 vierendeel_calculator.py ... --design-method LRFD
python3 webpost_checker.py ... --LRFD
```

**ASD**:
```bash
python3 vierendeel_calculator.py ... --design-method ASD
python3 webpost_checker.py ... --ASD
```

---

## Dependencies

All scripts use Python 3 standard library only:
- `argparse` - Command-line interface
- `pathlib` - File path handling
- `re` - Regular expressions
- `math` - Mathematical functions
- `sys` - System interaction

**Installation**: None required (uses standard library)

**Python Version**: Python 3.6+

---

## File Structure

```
scripts/
├── README.md                    # This file
├── geometry_calculator.py       # Beam geometry and tee properties
├── vierendeel_calculator.py     # Vierendeel bending analysis
├── webpost_checker.py           # Web post buckling check
├── smart_search.py              # Intelligent document search
├── formula_finder.py            # Formula extraction tool
└── example_matcher.py           # Example selection tool
```

---

## References

All scripts implement calculations per:
- **AISC Design Guide 31**: Castellated and Cellular Beam Design
- **AISC Specification**: Combined forces interaction (Chapter H)

**Key Sections**:
- Section 3.2: Vierendeel Bending in Noncomposite Beams
- Section 3.3: Vierendeel Bending in Composite Beams
- Section 3.4.1: Web Post Buckling in Castellated Beams
- Section 3.4.2: Web Post Buckling in Cellular Beams
- Chapter 4: Worked Examples (4.1, 4.2, 4.3, 4.4)

---

## Authors

Created for the HONEYCOMB_Beam_Engineer skill.

## License

For use with AISC Design Guide 31 reference material.

---

## Quick Reference

**Calculate geometry**: `geometry_calculator.py`
**Check Vierendeel**: `vierendeel_calculator.py`
**Check web post**: `webpost_checker.py`
**Search documents**: `smart_search.py`
**Find formulas**: `formula_finder.py`
**Match examples**: `example_matcher.py`

For help on any script: `python3 <script_name>.py --help`
