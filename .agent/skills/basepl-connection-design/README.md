# Base Plate Connection Design Skill

**AI-powered expert system for steel column base plate and anchor rod connection design per AISC Design Guide 1 (3rd Edition)**

## Overview

This Claude Code skill provides comprehensive access to AISC Design Guide 1 content, including:
- 220 pages consolidated into 8 searchable chapter files (626 KB total)
- 15 fully worked design examples
- 8 quick-reference guides for common design questions
- 4 Python automation scripts for calculations and searches
- Support for both LRFD and ASD design methods
- Complete coverage of exposed and embedded base connections

## Quick Start

### For Users

**Ask questions naturally:**
- "How do I design a base plate for 200 kips compression?"
- "What is the formula for concrete bearing strength?"
- "Show me an example of large moment base plate design"
- "What are the anchor rod placement tolerances?"

**The skill will:**
1. Identify your design scenario
2. Find relevant formulas, examples, or procedures
3. Provide step-by-step guidance
4. Reference specific sections and examples
5. Show both LRFD and ASD methods

### Common Use Cases

**1. Find a worked example:**
```
"Show me an example for compression with shear"
→ Skill will search examples-index and direct you to Example 4.7.4 or 4.7.5
```

**2. Get design formulas:**
```
"What is the formula for base plate thickness?"
→ Skill will extract formulas from Chapter 4 with variable definitions
```

**3. Follow design procedure:**
```
"What are the steps to design a base plate with moment?"
→ Skill will provide flowchart-based procedure from design-flowchart.md
```

**4. Quick calculations:**
```
"Calculate bearing strength for 18x14 plate on 4000 psi concrete"
→ Skill can run base_plate_calculator.py script
```

## Skill Contents

### Data Files (626 KB, 8 files)

| File | Pages | Size | Content |
|------|-------|------|---------|
| Chapter_1_Introduction.md | 1-6 | 5.3 KB | Overview, scope |
| Chapter_2_Materials.md | 7-10 | 11.9 KB | Materials, F1554 anchors |
| Chapter_3_Base_Plate_Design.md | 11-18 | 34.7 KB | Design theory |
| **Chapter_4_Exposed_Connections.md** | **19-140** | **315.6 KB** | **Main chapter, 15 examples** |
| Chapter_5_Embedded_Connections.md | 141-150 | 18.8 KB | Embedded bases |
| Chapter_6_Seismic_Design.md | 151-162 | 43.7 KB | Seismic provisions |
| Appendix_A_Specialty_Anchors.md | 163-172 | 33.2 KB | Specialty systems |
| Appendix_B_Alternate_Methods.md | 173-220 | 163.1 KB | Alternative approaches |

### Reference Guides (7 files)

1. **examples-index.md** - Complete catalog of 15 worked examples
   - Quick reference table by loading type
   - Search by design feature (friction, shear lug, biaxial, etc.)
   - Complexity ratings (basic, intermediate, advanced)

2. **symbols.md** - Complete notation guide
   - Geometric parameters (N, B, t_pl, m, n)
   - Load parameters (LRFD and ASD)
   - Resistance/safety factors (φ, Ω)

3. **design-flowchart.md** - Step-by-step design procedures
   - 7 design paths based on loading
   - Decision trees for connection selection
   - Moment classification (small vs large)

4. **limit-states-guide.md** - All limit states organized by component
   - 16 limit states with formulas and checks
   - Resistance factors summary table
   - Hierarchy of checks by connection type

5. **anchor-rod-guide.md** - F1554 anchor rod selection
   - Grade comparison (36, 55, 105)
   - Capacity tables by diameter
   - Embedment depth guidelines

6. **load-combinations.md** - LRFD and ASD load combinations
   - ASCE 7 combinations
   - Critical combinations for base plates
   - Seismic and wind provisions

7. **moment-classification.md** - Small vs large moment distinction
   - Eccentricity calculation
   - Classification criteria
   - Design implications

### Python Scripts (4 files)

1. **smart_search.py** - Keyword-based content search
   ```bash
   python3 smart_search.py "bearing strength"
   python3 smart_search.py "shear lug" --max-results 10
   ```

2. **base_plate_calculator.py** - Preliminary sizing calculations
   ```bash
   python3 base_plate_calculator.py --method lrfd --load 200 --fc 4000 --fy 36 --N 18 --B 14
   ```

3. **example_matcher.py** - Find examples by loading conditions
   ```bash
   python3 example_matcher.py --compression --shear
   python3 example_matcher.py --tension --moment --biaxial
   ```

4. **consolidate_chapters.py** - Data preparation (used during skill creation)

## Design Coverage

### Loading Types Covered

- ✓ Axial compression (concentric and eccentric)
- ✓ Axial tension/uplift
- ✓ Uniaxial moment (small and large)
- ✓ Biaxial moments
- ✓ Shear (friction and shear lug)
- ✓ Combined loading (compression + moment + shear)
- ✓ Braced frame connections
- ✓ Seismic loading

### Design Methods

- ✓ LRFD (Load and Resistance Factor Design)
- ✓ ASD (Allowable Strength Design)
- ✓ Both methods shown side-by-side in all examples

### Key Features

**Moment Classification:**
- Small moment case (e ≤ e_crit): Uniform bearing, no anchor tension
- Large moment case (e > e_crit): Triangular bearing, anchors required

**Shear Transfer:**
- Friction method (μ = 0.55 for steel on grout)
- Shear lug design when friction insufficient

**Anchor Rod Design:**
- Steel strength per ACI 318-17.6.1
- Concrete breakout per ACI 318-17.6.2
- Combined tension-shear interaction per ACI 318-17.8

**Concrete Bearing:**
- Confinement factor √(A2/A1) up to 2.0
- ACI 318 Section 22.8 provisions

## Worked Examples Summary

| # | Title | Loading | Complexity |
|---|-------|---------|------------|
| 4.7.1 | Compression (Small Plate, Confinement) | C | Basic |
| 4.7.2 | Compression (Large Plate, Confinement) | C | Basic |
| 4.7.3 | Compression (Small Plate) | C | Basic |
| 4.7.4 | Shear (Friction) | C + V | Intermediate |
| 4.7.5 | Shear (Shear Lug) | C + V | Intermediate |
| 4.7.6 | Tension + Shear | T + V | Intermediate |
| 4.7.7 | Brace (Reversible) | T/C + V | Advanced |
| 4.7.8 | Brace (Tension Only) | T + V | Advanced |
| 4.7.9 | Eccentric Compression (Small Moment) | C + M | Intermediate |
| 4.7.10 | Pure Bending | M | Intermediate |
| 4.7.11 | Compression + Moment + Shear (Low) | C + M + V | Advanced |
| 4.7.12 | Compression + Moment + Shear (Large) | C + M + V | Advanced |
| 4.7.13 | Biaxial Compression + Bending | C + Mx + My | Advanced |
| 4.7.14 | Biaxial Tension + Bending | T + Mx + My | Advanced |
| 4.7.15 | Biaxial (Most Complex) | C + Mx + My + Vx + Vy | Advanced |

*C=Compression, T=Tension, M=Moment, V=Shear*

## Typical Workflows

### Workflow 1: Design a simple compression base
1. Ask: "Design a base plate for [load] kips on [fc] psi concrete"
2. Skill runs base_plate_calculator.py
3. Get preliminary sizing (plate dimensions, thickness)
4. Reference Example 4.7.1 for detailed design

### Workflow 2: Classify moment case
1. Ask: "Is this a small or large moment case? P=100 kips, M=1200 kip-in"
2. Skill calculates e = M/P
3. Guides through e_crit calculation
4. Classifies moment and recommends design path

### Workflow 3: Find relevant example
1. Ask: "Show me example for compression with moment and shear"
2. Skill uses example_matcher.py or examples-index.md
3. Presents Example 4.7.11 (small) or 4.7.12 (large)
4. Summarizes approach and key results

### Workflow 4: Get specific formula
1. Ask: "What is the concrete breakout formula?"
2. Skill searches Chapter 4, Section 4.5
3. Extracts ACI 318-17.6.2 formula with variables
4. Provides context and applicable examples

### Workflow 5: Design procedure
1. Ask: "What are the steps to design a base plate with biaxial loading?"
2. Skill reads design-flowchart.md
3. Presents Path F (biaxial) step-by-step
4. References Example 4.7.13 or 4.7.15

## Design Limitations

**This skill covers:**
- Exposed base plate connections (primary)
- Embedded base connections (basic coverage)
- Cast-in anchor rods (F1554)
- Typical structural steel shapes (W, HSS)
- Normal-weight concrete (f'_c typically 3000-6000 psi)

**Not covered in detail:**
- Post-installed anchors (refer to ACI 355.2)
- Specialty anchor systems (Appendix A provides overview)
- Precast concrete connections
- Timber or masonry supports
- Offshore or corrosive environments (special considerations)

## Integration with Other Codes

**This skill references:**
- **ACI 318** (Building Code Requirements for Structural Concrete)
  - Chapter 17: Anchoring to Concrete
  - Section 22.8: Bearing Strength
- **AISC Specification** (ANSI/AISC 360)
  - Chapter J: Connections
  - Section J2: Welds
- **ASCE 7** (Minimum Design Loads)
  - Chapter 2: Load Combinations
- **ASTM F1554** (Anchor Bolts Specification)
  - Grades 36, 55, 105

## Best Practices

1. **Start simple**: Begin with basic examples (4.7.1-4.7.3) before complex cases

2. **Check both methods**: LRFD and ASD may give different results; understand which applies

3. **Classify moment early**: Small vs large moment determines entire approach

4. **Use references first**: Quick-reference guides answer most common questions faster

5. **Verify with examples**: Always cross-reference your design with similar worked example

6. **Consider construction**: Tolerances, grouting, and installation affect performance

7. **Document assumptions**: Note confinement factors, load combinations, material grades

## For Developers

**Skill Architecture:**
- Progressive disclosure: References → Chapters → Full examples
- Token-efficient: Scripts for calculations, Grep for searches
- Dual-method support: All content shows LRFD and ASD

**Extending the Skill:**
- Add new reference guides in `references/`
- Create additional Python scripts in `scripts/`
- Update SKILL.md workflows for new capabilities

**Maintenance:**
- Update for new Design Guide 1 editions
- Sync with ACI 318 and AISC Specification updates
- Add user-requested example scenarios

## Version History

**Version 1.0** (2025-11-14)
- Initial release
- 220 pages consolidated from AISC Design Guide 1 (3rd Edition)
- 8 chapters, 7 reference guides, 4 Python scripts
- 8 workflow types in SKILL.md
- Full LRFD and ASD coverage

## License and Attribution

**Source Material:**
- AISC Design Guide 1: Base Connection Design for Steel Structures (3rd Edition)
- Published by American Institute of Steel Construction (AISC)

**Skill Implementation:**
- Created for Claude Code Skills framework
- Consolidation, automation, and reference guides are derivative works
- For educational and design assistance purposes

**Usage:**
- This skill is for design assistance only
- Final designs should be reviewed by licensed professional engineer
- Critical connections require special attention and peer review

## Support

**For skill issues:**
- Check CHANGES.md for consolidation methodology
- Verify file paths in skill directory
- Ensure Python 3.x available for scripts

**For design questions:**
- Use skill's natural language interface
- Reference Design Guide 1 directly for authoritative guidance
- Consult licensed structural engineer for critical applications

## Quick Reference

**Most common queries:**
1. "Design a base plate for X kips compression"
2. "Show me example for [loading type]"
3. "What is the formula for [design parameter]"
4. "Is this a small or large moment case?"
5. "What anchor rod grade should I use?"
6. "What load combinations do I need?"
7. "What are the fabrication tolerances?"
8. "How do I design for shear?"

**Most useful files:**
- examples-index.md → Find worked examples
- design-flowchart.md → Design procedure
- limit-states-guide.md → What to check
- moment-classification.md → Small vs large moment

**Most common examples:**
- Example 4.7.1 → Simple compression
- Example 4.7.9 → Small moment
- Example 4.7.12 → Large moment with shear
- Example 4.7.4 → Friction shear
- Example 4.7.5 → Shear lug

---

**Ready to design base plates? Just ask!**
