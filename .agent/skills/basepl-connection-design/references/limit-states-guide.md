# Limit States Guide for Base Plate Connections

*Quick reference for limit states and failure modes in base plate connection design*

## Overview

Base plate connections must satisfy multiple limit states to ensure safe and serviceable performance. This guide summarizes the key limit states organized by component.

---

## BASE PLATE LIMIT STATES

### 1. Plate Bending/Yielding

**Description**: Base plate bends under bearing stress or anchor rod tension, potentially exceeding yield stress.

**Critical Locations**:
- Cantilever portions beyond column flanges
- Region between anchor rods (in tension)
- Bearing zone under high compression

**Design Check**:
- Required thickness: t_pl(reqd) based on cantilever length and bending moment
- Resistance: φM_n = φ × F_y × Z_pl (plastic section modulus)

**LRFD**: φ = 0.90
**ASD**: Ω = 1.67

**References**: Section 4.4.2, 4.4.3, 4.4.4

---

## CONCRETE/GROUT LIMIT STATES

### 2. Concrete Bearing Strength

**Description**: Concrete crushing under base plate bearing stress.

**Formula**:

LRFD: φP_p = 0.65 × 0.85f'_c × A1 × √(A2/A1) ≤ 0.65 × 1.7f'_c × A1

ASD: P_p/Ω = (0.85f'_c × A1 × √(A2/A1))/2.31 ≤ (1.7f'_c × A1)/2.31

Where:
- A1 = base plate area
- A2 = supporting concrete area (max √(A2/A1) = 2.0)
- φ_c = 0.65 (LRFD)
- Ω_c = 2.31 (ASD)

**Key Factors**:
- Confinement: √(A2/A1) increases capacity when plate is smaller than pier
- Maximum confinement factor = 2.0

**References**: Section 3.2, 4.4.2, ACI 318 Section 22.8

### 3. Concrete Edge Distance

**Description**: Inadequate edge distance from anchor rods to concrete edge.

**Minimum Requirements**:
- Typically ≥ 1.5h_ef (1.5 times embedment depth)
- ACI 318 Section 17 specifies edge distance requirements
- Affects breakout cone geometry

**References**: Section 4.5, ACI 318 Section 17.9

---

## ANCHOR ROD LIMIT STATES

### 4. Anchor Rod Tensile Strength (Steel)

**Description**: Anchor rod steel yields or fractures in tension.

**Formula**:

LRFD: φN_sa = φ × 0.75 × A_se × F_uta

ASD: N_sa/Ω = (0.75 × A_se × F_uta) / 2.00

Where:
- A_se = effective tensile stress area of anchor
- F_uta = specified tensile strength (Grade 36: 58 ksi, Grade 55: 75 ksi, Grade 105: 125 ksi)
- φ = 0.75
- Ω = 2.00

**References**: Section 4.4.1, ACI 318 Section 17.6.1

### 5. Concrete Breakout Strength (Tension)

**Description**: Concrete cone failure around anchor rods in tension.

**Failure Mode**: Conical breakout surface extending from anchor at approximately 35° angle.

**Formula (simplified for cast-in anchors)**:

LRFD: φN_cb = φ × (A_Nc / A_Nco) × Ψ_ec,N × Ψ_ed,N × Ψ_c,N × N_b

ASD: N_cb/Ω = [(A_Nc / A_Nco) × Ψ_ec,N × Ψ_ed,N × Ψ_c,N × N_b] / 2.50

Where:
- N_b = basic concrete breakout strength = k_c × λ_a × √f'_c × h_ef^1.5
- k_c = 24 for cast-in anchors
- h_ef = effective embedment depth
- Ψ factors account for eccentricity, edge distance, cracking

**Key Factors**:
- Embedment depth h_ef (most significant parameter)
- Anchor spacing (overlapping cones for anchor groups)
- Edge distance effects
- Concrete cracking condition

**Typical h_ef for common applications**:
- Light loads: 8"-12"
- Moderate loads: 12"-18"
- Heavy loads: 18"-30"+

**References**: Section 4.5, ACI 318 Section 17.6.2

### 6. Anchor Rod Pullout Strength

**Description**: Anchor head or threads pull out of concrete without cone breakout.

**Governing when**: Shallow embedment with large bearing area (e.g., headed studs, plate washers).

**Formula**:

LRFD: φN_pn = φ × Ψ_c,P × 8 × A_brg × f'_c

ASD: N_pn/Ω = (Ψ_c,P × 8 × A_brg × f'_c) / 3.00

Where:
- A_brg = bearing area of anchor head or nut
- φ = 0.70
- Ω = 3.00

**References**: ACI 318 Section 17.6.3

### 7. Anchor Rod Side-Face Blowout

**Description**: Concrete spalls from side face when anchor is close to edge.

**Governing when**: Anchors near edge with h_ef > 2.5 × edge distance.

**References**: ACI 318 Section 17.6.4

### 8. Anchor Rod Shear Strength (Steel)

**Description**: Anchor rod shears at concrete surface or at threaded section.

**Formula**:

LRFD: φV_sa = φ × 0.6 × A_se × F_uta (for anchor rods without shear lugs)

ASD: V_sa/Ω = (0.6 × A_se × F_uta) / 2.00

Where:
- 0.6 = shear strength factor
- φ = 0.65
- Ω = 2.00

**References**: Section 4.4.6, ACI 318 Section 17.7.1

### 9. Concrete Breakout Strength (Shear)

**Description**: Concrete breaks out in front of anchor under shear load.

**Failure Mode**: Half-cone breakout on loaded side.

**Critical parameters**:
- Edge distance (c_a1)
- Anchor diameter
- Embedment depth
- Concrete strength

**References**: Section 4.4.6, ACI 318 Section 17.7.2

### 10. Concrete Pryout Strength (Shear)

**Description**: Concrete fails in tension on back side when shear creates prying action.

**Governing when**: Deep embedment (h_ef large relative to edge distance).

**Formula related to concrete breakout in tension**:

LRFD: φV_cp = φ × k_cp × N_cb

Where k_cp = 2.0 for h_ef ≥ 2.5"

**References**: ACI 318 Section 17.7.3

### 11. Combined Tension and Shear Interaction

**Description**: Anchor rods subjected to both tension and shear simultaneously.

**Interaction Equation (ACI 318 Section 17.8)**:

(T_ua / φN_n)^(5/3) + (V_ua / φV_n)^(5/3) ≤ 1.0 (LRFD)

Where:
- T_ua = factored tension force
- V_ua = factored shear force
- N_n = controlling tension strength
- V_n = controlling shear strength

**Exemption**: If T_ua ≤ 0.2φN_n, interaction check not required (shear alone governs).
**Exemption**: If V_ua ≤ 0.2φV_n, interaction check not required (tension alone governs).

**References**: Section 4.4.6, Example 4.7.6

---

## SHEAR TRANSFER LIMIT STATES

### 12. Shear Friction Resistance

**Description**: Friction between base plate and grout/concrete resists shear.

**Formula**:

LRFD: φV_f = 0.75 × μ × P_u

ASD: V_f/Ω = (μ × P_a) / 2.00

Where:
- μ = 0.55 (coefficient of friction for steel on grout or concrete)
- P_u, P_a = clamping force (axial compression)
- φ = 0.75
- Ω = 2.00

**Limitations**:
- Only applicable when compression force exists
- Anchor rods must be adequate for factored tension forces
- Cannot be combined with other shear transfer mechanisms

**References**: Section 4.4.6, Example 4.7.4

### 13. Shear Lug Bearing on Concrete

**Description**: Shear lug transfers load by bearing against concrete.

**Design per**: ACI 318 Section 17.5.2.1 (structural steel embedment)

**Limit states for shear lug**:
- Steel yielding/rupture of lug
- Concrete bearing in front of lug
- Welds connecting lug to base plate

**References**: Section 4.4.6, Example 4.7.5

---

## COLUMN-TO-PLATE WELD LIMIT STATES

### 14. Weld Strength

**Description**: Welds connecting column to base plate must resist load transfer.

**Governing Limit States**:
- Weld metal shear rupture
- Base metal rupture
- Base metal yielding

**Design per**: AISC Specification Section J2

**Typical approach**: Size welds for full column strength or actual load, whichever is less.

**References**: Section 3.2, 4.6.5

---

## SERVICEABILITY LIMIT STATES

### 15. Anchor Rod Hole Size and Tolerances

**Description**: Oversized holes or misalignment affects load transfer.

**Standard hole sizes**:
- Minimum: d_h = anchor diameter + 1/4"
- Maximum: d_h = anchor diameter + 1/2"

**Tolerances (AISC Code of Standard Practice)**:
- Anchor rod placement: ± 1/4" typical, ± 1/2" maximum
- Affects design assumptions

**References**: Section 4.6.3, 4.6.4

### 16. Grout Thickness and Quality

**Description**: Inadequate grout thickness or poor quality affects bearing transfer.

**Requirements**:
- Minimum thickness: typically 1/2" (some specs require 1")
- Maximum thickness: typically 3"
- Grout strength: f'_g ≥ f'_c (concrete)

**References**: Section 2.5, 4.6.2

---

## LIMIT STATE HIERARCHY

**For most base plate designs, check in this order:**

### Compression-dominated connections:
1. Concrete bearing strength (Limit State #2)
2. Base plate bending (Limit State #1)
3. Shear transfer (Limit States #12 or #13)
4. Column-to-plate welds (Limit State #14)

### Tension-dominated connections:
1. Anchor rod steel strength (Limit State #4)
2. Concrete breakout strength (Limit State #5)
3. Base plate bending (Limit State #1)
4. Anchor rod shear (if applicable) (Limit State #8)
5. Combined tension-shear interaction (if both present) (Limit State #11)

### Combined loading:
1. Classify moment (small vs. large)
2. If large moment: Anchor rod design (Limit States #4, #5)
3. Concrete bearing (Limit State #2)
4. Base plate bending (Limit State #1)
5. Shear transfer (Limit States #12 or #13)
6. Combined loading interaction if applicable (Limit State #11)

---

## RESISTANCE FACTORS AND SAFETY FACTORS SUMMARY

| Limit State | φ (LRFD) | Ω (ASD) | Reference |
|-------------|----------|---------|-----------|
| Concrete bearing | 0.65 | 2.31 | ACI 318-22.8 |
| Steel yielding (plate) | 0.90 | 1.67 | AISC Spec F1 |
| Anchor tension (steel) | 0.75 | 2.00 | ACI 318-17.6.1 |
| Anchor breakout (tension) | 0.75 | 2.50 | ACI 318-17.6.2 |
| Anchor pullout | 0.70 | 3.00 | ACI 318-17.6.3 |
| Anchor shear (steel) | 0.65 | 2.00 | ACI 318-17.7.1 |
| Anchor breakout (shear) | 0.70 | 2.50 | ACI 318-17.7.2 |
| Shear friction | 0.75 | 2.00 | Per Design Guide |
| Welds | 0.75 | 2.00 | AISC Spec J2 |

---

## PRACTICAL NOTES

**Most common governing limit states by connection type:**

- **Simple compression**: Concrete bearing, plate thickness
- **Compression + shear**: Shear friction, shear lug bearing (if required)
- **Tension + shear**: Anchor rod strength, concrete breakout, tension-shear interaction
- **Large moment**: Anchor rod tension (steel), concrete breakout, plate thickness

**Failure mode preferences:**
- Ductile failures preferred: Steel yielding, plate bending
- Brittle failures to avoid: Concrete breakout, anchor pullout, weld rupture
- Design to ensure ductile limit states govern

**Common design iterations:**
- Concrete bearing insufficient → Increase plate size (N × B)
- Plate too thick → Increase plate size or reduce cantilever
- Anchor breakout insufficient → Increase h_ef or number of anchors
- Shear friction insufficient → Add shear lug
