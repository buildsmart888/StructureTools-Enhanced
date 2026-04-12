# Anchor Rod Selection Guide

*Quick reference for ASTM F1554 anchor rod grades, properties, and selection*

## ASTM F1554 Anchor Rod Grades

| Grade | Yield Strength (F_ya) | Tensile Strength (F_uta) | Typical Applications |
|-------|----------------------|-------------------------|----------------------|
| **36** | 36 ksi | 58 ksi | Light to moderate loads, most common |
| **55** | 55 ksi | 75 ksi | Moderate loads, intermediate choice |
| **105** | 105 ksi | 125 ksi | High loads, limited weldability |

## Selection Guidelines

**Default choice**: Grade 36
- Most economical
- Best weldability
- Adequate for majority of applications
- Available in all sizes

**Use Grade 55 when**: Moderate increase in strength needed, space constraints

**Use Grade 105 when**: Very high loads, cannot accommodate larger diameter Grade 36/55

**Rule of thumb**: Use larger diameter Grade 36 rather than smaller diameter Grade 105 when possible (better ductility, weldability, and cost).

## Common Diameters and Areas

| Diameter | Area (in.²) | Tensile Capacity (kips) |
|----------|-------------|------------------------|
|  | | Grade 36 / 55 / 105 |
| 3/4" | 0.442 | 19.2 / 24.8 / 41.4 |
| 7/8" | 0.601 | 26.1 / 33.8 / 56.4 |
| 1" | 0.785 | 34.1 / 44.1 / 73.6 |
| 1-1/8" | 0.994 | 43.2 / 55.8 / 93.2 |
| 1-1/4" | 1.227 | 53.3 / 68.9 / 115.0 |
| 1-1/2" | 1.767 | 76.8 / 99.3 / 165.8 |
| 1-3/4" | 2.405 | 104.5 / 135.3 / 225.9 |
| 2" | 3.142 | 136.6 / 176.6 / 294.9 |

*Capacities shown: φN_sa = 0.75 × 0.75 × A_se × F_uta (LRFD)*

## Supplementary Requirements

**S1**: Restricted chemistry for improved weldability and toughness
- Required if welding anticipated
- Ensures notch toughness for Charpy V-notch testing

**S4**: Permits mechanical galvanizing per ASTM B695
- Cannot be used with Grade 105

**S5**: Charpy V-notch impact testing requirements

## Embedment Depth (h_ef) Guidelines

Minimum embedment for concrete breakout strength:

| Anchor Load (kips) | Typical h_ef | Concrete f'_c |
|-------------------|--------------|---------------|
| Light (< 20 kips) | 8"-12" | 3000-4000 psi |
| Moderate (20-50 kips) | 12"-18" | 3000-4000 psi |
| Heavy (> 50 kips) | 18"-30"+ | 4000+ psi |

**Note**: Actual h_ef must be calculated based on ACI 318 Section 17.6.2 for concrete breakout strength.

## Galvanizing Considerations

- **Hot-dip galvanizing**: Only Grade 36 (Grade 55/105 risk of embrittlement)
- **Mechanical galvanizing** (ASTM B695): Grades 36 and 55 with S4 supplement
- **Earthquake applications**: Galvanized anchors require special consideration for hydrogen embrittlement

## Minimum Edge Distances

Per ACI 318 Section 17.9:
- Typically ≥ 1.5 × h_ef
- Check ACI 318 for specific requirements based on loading

## Typical Anchor Rod Quantities

| Column Type | Number of Rods | Pattern |
|-------------|----------------|---------|
| Light W-shapes | 4 | Rectangular |
| Moderate W-shapes | 4-6 | Rectangular |
| Heavy W-shapes | 6-8 | Rectangular |
| HSS columns | 4 | Square |
| Biaxial loading | 6-8 | Rectangular/circular |

## Installation Tolerances

**Per AISC Code of Standard Practice:**
- **Preferred**: ± 1/4"
- **Maximum**: ± 1/2"

**Hole size allowances:**
- **Standard**: Anchor diameter + 1/4" to + 1/2"
- **Oversized**: May require plate washers

## Welding Restrictions

**Grade 36**: Weldable with restrictions
- Preheat if thickness > 1"
- Use S1 supplement if welding anticipated

**Grade 55**: Limited weldability
- Special procedures required

**Grade 105**: Not recommended for welding
- Quenched and tempered, welding affects heat treatment

**General**: Welding of anchor rods discouraged unless specifically addressed in project specifications.

## Material Alternatives

**ASTM A307**: Low-carbon steel bolts
- F_u = 60 ksi
- Less common for base plates

**ASTM A36**: Threaded rod (non-standard)
- F_y = 36 ksi, F_u = 58-80 ksi
- Not specifically designed for anchoring

**ASTM A193 Grade B7**: High-strength bolts
- For special applications (high temperature, etc.)

## Quick Selection Process

1. Calculate required tension/shear capacity
2. Select minimum anchor diameter from table above
3. Check concrete breakout (typically governs for larger loads)
4. Determine required h_ef for breakout strength
5. Select Grade 36 unless Grade 55/105 required by space constraints
6. Specify supplementary requirements if needed (S1 for welding, S4 for galvanizing)
7. Design base plate holes for ± 1/4" tolerance

## Common Design Checks

- ✓ Anchor rod steel strength (ACI 318-17.6.1)
- ✓ Concrete breakout strength (ACI 318-17.6.2)
- ✓ Anchor rod shear strength if applicable (ACI 318-17.7.1)
- ✓ Concrete breakout in shear if applicable (ACI 318-17.7.2)
- ✓ Combined tension-shear interaction (ACI 318-17.8)
- ✓ Edge distance requirements (ACI 318-17.9)
- ✓ Anchor spacing (overlapping breakout cones)

## References

- ASTM F1554: Standard Specification for Anchor Bolts, Steel, 36, 55, and 105-ksi Yield Strength
- ACI 318: Building Code Requirements for Structural Concrete, Chapter 17
- Design Guide 1, Sections 2.3, 4.4.1, 4.5
