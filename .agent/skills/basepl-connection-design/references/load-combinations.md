# Load Combinations for Base Plate Design

*LRFD and ASD load combinations per ASCE 7*

## LRFD Load Combinations (Load and Resistance Factor Design)

Per ASCE 7, Chapter 2:

1. **1.4D**

2. **1.2D + 1.6L + 0.5(L_r or S or R)**

3. **1.2D + 1.6(L_r or S or R) + (L or 0.5W)**

4. **1.2D + 1.0W + L + 0.5(L_r or S or R)**

5. **1.2D + 1.0E + L + 0.2S**

6. **0.9D + 1.0W**

7. **0.9D + 1.0E**

### Load Notations:
- **D** = dead load
- **L** = live load
- **L_r** = roof live load
- **S** = snow load
- **R** = rain load
- **W** = wind load
- **E** = seismic load

### Critical Combinations for Base Plates:

**Maximum compression**:
- Combination 2: 1.2D + 1.6L (gravity loads)
- Combination 4: 1.2D + 1.0W + L (wind downward)

**Maximum uplift (tension)**:
- Combination 6: 0.9D + 1.0W (wind uplift)
- Combination 7: 0.9D + 1.0E (seismic uplift)

**Maximum moment**:
- Combination 4: 1.2D + 1.0W + L
- Combination 5: 1.2D + 1.0E + L

---

## ASD Load Combinations (Allowable Strength Design)

Per ASCE 7, Chapter 2:

1. **D**

2. **D + L**

3. **D + (L_r or S or R)**

4. **D + 0.75L + 0.75(L_r or S or R)**

5. **D + (0.6W or 0.7E)**

6. **D + 0.75L + 0.75(0.6W) + 0.75(L_r or S or R)**

7. **D + 0.75L + 0.75(0.7E) + 0.75S**

8. **0.6D + 0.6W**

9. **0.6D + 0.7E**

### Critical Combinations for Base Plates:

**Maximum compression**:
- Combination 2: D + L
- Combination 5: D + 0.6W (wind downward)

**Maximum uplift (tension)**:
- Combination 8: 0.6D + 0.6W
- Combination 9: 0.6D + 0.7E

**Maximum moment**:
- Combination 5: D + 0.6W
- Combination 5: D + 0.7E

---

## LRFD vs ASD Comparison

| Aspect | LRFD | ASD |
|--------|------|-----|
| **Load factors** | Applied to loads | Included in combination factors |
| **Resistance factors** | φ < 1.0 (reduces strength) | Ω > 1.0 (reduces strength via division) |
| **Design equation** | Σ(γ_i × Q_i) ≤ φR_n | Σ(load factors × Q_i) ≤ R_n/Ω |
| **Typical factors** | 1.2D, 1.6L, 1.0W, 1.0E | D, L, 0.6W, 0.7E |
| **Result relationship** | LRFD loads ≈ 1.5-1.6 × ASD loads | ASD loads ≈ 0.6-0.7 × LRFD loads |

### Resistance/Safety Factors by Limit State:

| Limit State | φ (LRFD) | Ω (ASD) |
|-------------|----------|---------|
| Concrete bearing | 0.65 | 2.31 |
| Plate yielding | 0.90 | 1.67 |
| Anchor tension (steel) | 0.75 | 2.00 |
| Anchor breakout | 0.75 | 2.50 |
| Anchor shear (steel) | 0.65 | 2.00 |
| Shear friction | 0.75 | 2.00 |

---

## Seismic Load Combinations

### Basic Seismic Load Effect:

**E = ρQ_E ± 0.2S_DS D**

Where:
- **ρ** = redundancy factor (typically 1.0)
- **Q_E** = effect of horizontal seismic forces
- **S_DS** = design spectral response acceleration (short period)
- **0.2S_DS D** = vertical seismic effect

### LRFD Seismic Combinations:

**1.2D + 1.0E + L + 0.2S**
Expanded: 1.2D + 1.0(ρQ_E + 0.2S_DS D) + L + 0.2S
        = (1.2 + 0.2S_DS)D + ρQ_E + L + 0.2S

**0.9D + 1.0E**
Expanded: 0.9D + 1.0(ρQ_E - 0.2S_DS D)
        = (0.9 - 0.2S_DS)D + ρQ_E

### ASD Seismic Combinations:

**D + 0.7E + L**
**0.6D + 0.7E**

---

## Wind Load Combinations

### Wind Load Components:

Wind load **W** can create:
- **Axial**: Uplift or downward pressure
- **Shear**: Lateral force at base
- **Moment**: Overturning moment

### Critical Wind Cases:

**LRFD**:
- Uplift: 0.9D + 1.0W (governs tension in anchors)
- Downward: 1.2D + 1.0W + L (governs compression)
- Lateral: 1.2D + 1.0W + L (governs shear and moment)

**ASD**:
- Uplift: 0.6D + 0.6W
- Downward: D + 0.6W
- Lateral: D + 0.6W

---

## Special Load Cases for Base Plates

### Construction Loads

During erection, before permanent connections/bracing:
- Anchor rods must resist construction wind and stability loads
- Typically use reduced wind speed or lower load factors
- Check OSHA requirements for construction safety

### Ponding and Drainage

Roof drainage affects column load:
- Check rain load **R** combinations
- Progressive ponding can increase loads

### Temperature and Shrinkage

Restraint of expansion/contraction:
- May create moments at base
- Consider in base plate rotational stiffness
- Typically not a load combination, but serviceability check

---

## Load Combination Selection Guide

### For Typical Building Column Base:

**Check these combinations minimum**:

**Gravity dominant**:
1. LRFD: 1.2D + 1.6L → compression, plate bearing
2. ASD: D + L → compression, plate bearing

**Wind/lateral dominant**:
3. LRFD: 0.9D + 1.0W → tension in anchors (uplift)
4. LRFD: 1.2D + 1.0W + L → moment, shear, combined loading
5. ASD: 0.6D + 0.6W → tension in anchors (uplift)
6. ASD: D + 0.6W → moment, shear, combined loading

**Seismic (if applicable)**:
7. LRFD: 0.9D + 1.0E → tension, seismic overstrength
8. LRFD: 1.2D + 1.0E + L → combined loading
9. ASD: 0.6D + 0.7E → tension
10. ASD: D + 0.7E → combined loading

### For Braced Frame Base:

Additional considerations:
- Brace force creates axial and shear at base
- Reversible braces: Check both tension and compression in brace
- Seismic braced frames: Use seismic load combinations with overstrength

**See Examples 4.7.7 and 4.7.8 for braced frame combinations**

---

## Determining Governing Combination

### Typical Governing Combinations by Limit State:

| Limit State | Typical Governing Combination |
|-------------|-------------------------------|
| Concrete bearing | LRFD: 1.2D + 1.6L (maximum compression) |
| Base plate thickness (compression zone) | LRFD: 1.2D + 1.6L |
| Anchor rod tension | LRFD: 0.9D + 1.0W or 0.9D + 1.0E (uplift) |
| Anchor rod shear | LRFD: 1.2D + 1.0W + L (lateral wind) |
| Combined axial + moment | LRFD: 1.2D + 1.0W + L (both compression and moment) |

### Multiple Combinations Required:

Base plates typically require checking **multiple load combinations** because different combinations govern different limit states:

- Bearing strength: Maximum compression combination
- Anchor tension: Maximum uplift combination
- Moment/eccentricity: Maximum moment combination
- Shear: Maximum lateral force combination

**Best practice**: Check all applicable combinations, design for the most demanding.

---

## Load Combination Workflow

1. **Identify applicable load types**: D, L, W, E, etc.

2. **Generate all relevant combinations**:
   - Gravity combinations (D, L)
   - Wind combinations (with and without D+L)
   - Seismic combinations (if applicable)

3. **Calculate base reactions** for each combination:
   - Axial force (P)
   - Shear force (V)
   - Moment (M)

4. **Identify critical combinations**:
   - Maximum P_compression → bearing design
   - Maximum P_tension → anchor tension design
   - Maximum M → moment/eccentricity design
   - Maximum V → shear transfer design
   - Critical combinations of P + M + V → combined loading

5. **Design base plate** for envelope of all critical combinations

---

## Quick Reference Tables

### Wind Load Factors:

| Method | Downward | Uplift | Lateral |
|--------|----------|--------|---------|
| **LRFD** | 1.0W | 1.0W | 1.0W |
| **ASD** | 0.6W | 0.6W | 0.6W |

### Seismic Load Factors:

| Method | E Factor | Notes |
|--------|----------|-------|
| **LRFD** | 1.0E | E includes ρ and vertical component |
| **ASD** | 0.7E | E includes ρ and vertical component |

### Dead Load Factors:

| Method | With Gravity | With Uplift |
|--------|--------------|-------------|
| **LRFD** | 1.2D | 0.9D |
| **ASD** | D | 0.6D |

---

## Notes

- **Design Guide 1 Examples**: All examples show both LRFD and ASD calculations side-by-side
- **Most common**: LRFD is more widely used in modern practice
- **Project specifications**: Always check project-specific requirements for load combinations
- **IBC/ASCE 7**: Verify edition of building code applicable to project

**References**: ASCE 7, IBC, Design Guide 1 Section 4.3
