# Glossary of Terms

Key technical terms used in castellated and cellular beam design.

## Beam Types

### Castellated Beam (CB)
A structural steel beam manufactured by cutting a wide-flange section along a zigzag (typically hexagonal) pattern through the web, then offsetting and welding the two halves together. This process expands the depth by approximately 1.5 times the original depth while maintaining the same weight. Characterized by hexagonal web openings.

**Example:** CB18×14 indicates a castellated beam with approximately 18-inch depth made from a W12×14 parent beam.

**Reference:** Section 1.2, Chapter 1

### Cellular Beam (LB)
A structural steel beam manufactured by cutting a wide-flange section through a series of circular cuts along the web, then offsetting and welding the two halves together. Similar to castellated beams but with circular web openings, providing smoother stress transitions and better galvanizing characteristics.

**Example:** LB18×14 indicates a cellular beam with approximately 18-inch depth made from a W12×14 parent beam.

**Reference:** Section 1.2, Chapter 1

### Parent Beam / Root Beam
The original wide-flange section that is cut to create a castellated or cellular beam. The parent beam designation determines the weight per foot of the resulting expanded beam.

**Reference:** Section 1.3, Chapter 1

### Asymmetric Section
A castellated or cellular beam created from two different parent beam sizes, with one size used for the top tee and a different size for the bottom tee. Often used in composite construction where a smaller top section is paired with a larger bottom section.

**Example:** CB30×44/57 uses W21×44 for the top and W21×57 for the bottom.

**Reference:** Section 2.2.6, Chapter 2

## Geometric Terms

### Tee Section
The T-shaped portion of the beam between two adjacent web openings. Consists of one flange and a portion of the web. Critical for Vierendeel bending analysis.

**Reference:** Section 3.2, Chapter 3

### Web Post
The solid vertical portion of the web between two adjacent openings. Critical failure location for web post buckling. Length denoted as "s" or "e" depending on beam type.

**Reference:** Section 3.4, Chapter 3

### Expansion Ratio
The ratio of the expanded beam depth to the parent beam depth. Typically 1.5 for standard patterns, but can range from 1.25 to 1.75.

**Formula:** Expansion Ratio = d_g / d

**Reference:** Section 2.3, Chapter 2

### Opening Spacing (S)
The center-to-center distance between adjacent openings measured along the beam length.

**Limits:**
- Castellated: S = 2e + 2b
- Cellular: 1.08 < S/D₀ < 1.5

**Reference:** Section 2.3, Chapter 2

### Web Post Aspect Ratio
The ratio of web post length to web post depth. Critical parameter for web post buckling.

**Formula:** s/d_p (castellated) or (S-D₀)/d_p (cellular)

**Limits:** Typically s/d_p > 1.25 to 1.5

**Reference:** Section 3.4, Chapter 3

## Structural Behavior Terms

### Vierendeel Bending / Vierendeel Moment
A secondary bending moment that develops in the top and bottom tees due to the transfer of shear force around web openings. Named after Arthur Vierendeel. This is the most critical failure mode for castellated and cellular beams.

**Mechanism:** Global shear creates moment couples in the tees at each opening, causing plastic hinges to form at four locations around each opening under ultimate load.

**Reference:** Section 3.2, Chapter 3

### Web Post Buckling
A local buckling failure mode where the web post between openings buckles due to the horizontal shear force transferred between top and bottom tees. Can occur by:
1. Flexural failure of the web post
2. Buckling failure of the web post

**Critical Parameter:** Web post aspect ratio s/d_p and slenderness e/t_w

**Reference:** Section 3.4, Chapter 3

### Horizontal Shear
The shear force acting horizontally along the neutral axis at each web post, created by the difference in axial forces between adjacent openings.

**Formula:** V_rh = |T_r(i) - T_r(i+1)|

**Reference:** Section 3.5, Chapter 3

### Composite Action
Interaction between the steel beam and concrete deck through shear studs, where the concrete deck resists compression forces and reduces Vierendeel moments in the top tee.

**Types:**
- Fully composite: All compression force resisted by concrete
- Partially composite: Compression force shared between concrete and steel

**Reference:** Section 3.3, Chapter 3

## Neutral Axis Definitions

### Elastic Neutral Axis (ENA)
The axis about which the section remains in elastic equilibrium under service loads. Location where normal stress is zero under elastic behavior.

**Reference:** All sections

### Plastic Neutral Axis (PNA)
The axis that divides the cross-section into equal areas in tension and compression under plastic conditions. Used for ultimate strength calculations.

**Reference:** Section 3.2, Chapter 3

## Failure Modes

### Lateral-Torsional Buckling (LTB)
Out-of-plane buckling of the beam's compression flange combined with twisting of the cross-section. Checked similar to solid web beams but using gross section properties.

**Note:** Deflection calculated using 90% of net section moment of inertia accounts for additional deformations.

**Reference:** Section 3.6, Chapter 3

### Flange Local Buckling
Local buckling of the flange plate between welds. Controlled by flange width-to-thickness ratio b_f/2t_f.

**Compact Limit:** λ ≤ 0.38√(E/F_y)

**Reference:** Section 3.2.2.2, Chapter 3

### Stem Local Buckling
Local buckling of the tee stem (web portion) when in compression. Controlled by depth-to-thickness ratio d_t/t_w.

**Compact Limit:** λ ≤ 0.75√(E/F_y)

**Reference:** Section 3.2.2.2, Chapter 3

### Web Local Yielding
Yielding of the web at concentrated loads. Requires checking per AISC Specification Section J10.

**Reference:** Section 3.8, Chapter 3

### Web Crippling
Localized crushing failure of the web at concentrated loads or reactions.

**Reference:** Section 3.8, Chapter 3

## Design-Related Terms

### Critical Section
For cellular beams, the section located 0.225D₀ from the center of the opening where Vierendeel moment is maximum.

**Reference:** Example 4.2, Chapter 4

### Global Forces
The overall shear and moment acting on the beam as a whole, calculated using standard beam analysis.

**Reference:** Section 3.1, Chapter 3

### Local Forces
The axial forces and Vierendeel moments in individual tee sections resulting from global forces.

**Reference:** Section 3.2.1, Chapter 3

### End Spacing
The distance from the beam support to the edge of the first web opening. Typically minimized as "a" with recommended minimum to avoid shear failure.

**Typical:** a = 0.5D₀ to 0.8D₀

**Reference:** Section 2.3.1, Chapter 2

### Cut Pattern
The arrangement of web openings, designated by numbers indicating filled vs. open positions at beam ends.

**Examples:**
- "1" pattern: Full opening at end
- "O" pattern: Half opening at end (crown)
- "OO" pattern: Two half openings at ends

**Reference:** Section 2.3, Chapter 2

## Manufacturing Terms

### Cutting Angle (θ)
The angle of the hexagonal cut pattern in castellated beams. Typical values are 45°, 52.5°, or 60°.

**Impact:** Affects web post buckling resistance factor (φ_b varies from 0.60 to 0.90 based on θ).

**Reference:** Section 3.4.1, Chapter 3

### Waste Material
Material removed during the cellular beam cutting process. Unlike castellated beams where material is conserved by the zigzag pattern, cellular beams produce waste strips between circular cuts.

**Reference:** Section 1.2, Chapter 1

### Hot Cutting
The thermal cutting process (oxyfuel or plasma) used to create the opening patterns in the parent beam web.

**Reference:** Section 1.2, Chapter 1

## Loading and Performance Terms

### Deflection Factor
For castellated and cellular beams, deflections are calculated using 90% of the net section moment of inertia to account for additional shear deformations around openings.

**Formula:** Δ = 5wL⁴ / [384EI_x(0.90)]

**Reference:** Section 3.7, Chapter 3

### Service Integration
The practice of routing HVAC ducts, electrical conduits, and other building services through the web openings to reduce floor-to-floor height.

**Reference:** Section 2.2.3, Chapter 2

### Vibration Resistance
Enhanced resistance to vibration due to increased depth (approximately 1.5× parent beam) which increases natural frequency.

**Reference:** Section 2.2.5, Chapter 2

## Construction Terms

### Erection Bracing
Temporary lateral bracing required during construction before the deck or permanent bracing is in place. Castellated and cellular beams may exhibit less stability than solid web beams during handling.

**Reference:** Section 2.4.3, Chapter 2

### Fireproofing
Fire protection requirements for castellated and cellular beams. The increased heated perimeter compared to solid web beams may require more spray-on fireproofing material.

**Reference:** Section 2.4.4, Chapter 2

### Galvanizing
Hot-dip galvanizing coating for corrosion protection. Cellular beams with smooth transitions are preferred over castellated beams with re-entrant corners to avoid coating issues.

**Reference:** Section 2.4.5, Chapter 2

## Abbreviations Used

- **ASD:** Allowable Strength Design
- **ASTM:** American Society for Testing and Materials
- **HVAC:** Heating, Ventilation, and Air Conditioning
- **LRFD:** Load and Resistance Factor Design
- **LTB:** Lateral-Torsional Buckling
- **WT-shape:** Structural tee cut from W-shape

## Notes

1. All failure modes must be checked per AISC Specification and this Design Guide.
2. Vierendeel bending typically governs for beams with high shear-to-moment ratios.
3. Web post buckling typically governs for closely-spaced openings (low s/d_p ratios).
4. Always verify geometric limits before applying design procedures.
