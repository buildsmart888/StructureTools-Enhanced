# ACI 318-25 Exposure Class Selection Guide

*Quick Reference for Concrete Durability Design*

---

## Overview

Exposure classes are critical for ensuring long-term durability of concrete structures. ACI 318-25 Chapter 19 defines four categories of exposure classes based on environmental conditions.

## The Four Exposure Class Categories

### F - Freezing and Thawing
**Concern**: Damage from freeze-thaw cycles in the presence of moisture

### W - Water Penetration
**Concern**: Water permeability and related issues (not including corrosion)

### C - Corrosion Protection of Reinforcement
**Concern**: Corrosion of reinforcing steel from chlorides

### S - Sulfate Attack
**Concern**: Chemical attack from sulfates in soil or water

---

## Exposure Class Selection Flowchart

### STEP 1: Freezing and Thawing Exposure (F-Series)

**Question 1**: Will the concrete be exposed to freezing temperatures?

- **NO** → **F0** (Not exposed to freezing)
- **YES** → Continue to Question 2

**Question 2**: Will the concrete be in contact with moisture during freezing?

- **Minimal moisture** → **F1** (Moderate exposure)
  - Example: Interior slabs in cold climates

- **Frequent moisture, not saturated** → **F2** (Moderate exposure)
  - Example: Exterior walls above grade

- **Saturated with water** → **F3** (Severe exposure)
  - Example: Bridge decks, parking garage slabs
  - Requires air-entrainment

**Question 3**: Will the concrete also be exposed to de-icing chemicals?

- **YES, with saturation** → **F3** (Severe exposure)
  - Most critical case
  - Requires air-entrainment + low w/cm ratio

---

### STEP 2: Water Penetration Exposure (W-Series)

**Question**: What level of water penetration control is required?

- **No special requirements** → **W0**
  - Interior members not exposed to weather

- **Low permeability required** → **W1**
  - Example: Basement walls below grade

- **Very low permeability required** → **W2**
  - Example: Water-retaining structures, swimming pools
  - Requires maximum w/cm = 0.40

---

### STEP 3: Corrosion Protection (C-Series)

**Question 1**: Will reinforcing steel be exposed to moisture?

- **Dry or protected from moisture** → **C0**
  - Example: Interior members in dry environment

- **YES** → Continue to Question 2

**Question 2**: What is the chloride exposure level?

- **Moisture but no chlorides** → **C1**
  - Example: Interior members occasionally wet

- **Moisture + moderate chlorides** → **C2**
  - Example: Parking garages, exterior walls in coastal areas
  - Requires minimum cover, maximum w/cm

- **Severe chloride exposure** → **C2** (Most restrictive)
  - Example: Marine structures, bridge decks with de-icing salts
  - Requires enhanced protection measures

---

### STEP 4: Sulfate Attack (S-Series)

**Question**: What is the sulfate concentration in soil or water?

Measure: Water-soluble sulfate (SO₄) in soil or sulfate in water

| Exposure | Soil SO₄ (%) | Water SO₄ (ppm) | Class |
|----------|--------------|-----------------|-------|
| Negligible | < 0.10 | < 150 | **S0** |
| Moderate | 0.10 - 0.20 | 150 - 1,500 | **S1** |
| Severe | 0.20 - 2.00 | 1,500 - 10,000 | **S2** |
| Very Severe | > 2.00 | > 10,000 | **S3** |

**S1**: Requires Type II or equivalent cement, maximum w/cm = 0.50
**S2**: Requires sulfate-resistant cement, maximum w/cm = 0.45
**S3**: Requires special sulfate-resistant measures, maximum w/cm = 0.40

---

## Required Concrete Properties by Exposure Class

### Freezing and Thawing (F-Series)

| Class | Air Content | Maximum w/cm | Minimum f'c (psi) |
|-------|-------------|--------------|-------------------|
| F0 | Not required | - | As needed |
| F1 | Not required | 0.55 | 2,500 |
| F2 | Required* | 0.50 | 3,000 |
| F3 | Required* | 0.45 | 4,000 |

*Air content requirements per Table 19.3.2.1

### Water Penetration (W-Series)

| Class | Maximum w/cm | Minimum f'c (psi) | Special Requirements |
|-------|--------------|-------------------|----------------------|
| W0 | - | As needed | None |
| W1 | 0.50 | 3,500 | Low permeability |
| W2 | 0.40 | 5,000 | Very low permeability |

### Corrosion Protection (C-Series)

| Class | Maximum w/cm | Minimum Cover (in) | Minimum f'c (psi) |
|-------|--------------|-------------------|-------------------|
| C0 | - | As needed | As needed |
| C1 | 0.50 | 1.5 - 2.0 | 3,000 |
| C2 | 0.40 | 2.0 - 3.0 | 5,000 |

### Sulfate Attack (S-Series)

| Class | Maximum w/cm | Minimum f'c (psi) | Cement Type |
|-------|--------------|-------------------|-------------|
| S0 | - | As needed | Any |
| S1 | 0.50 | 4,000 | Type II or equivalent |
| S2 | 0.45 | 4,500 | Sulfate-resistant |
| S3 | 0.40 | 5,000 | High sulfate-resistant |

---

## Common Structure Type Examples

### Parking Structures
- **F3** (de-icing salts + saturation)
- **C2** (chloride exposure)
- **W1** (water penetration control)
- **S0** (typically no sulfate concern)

**Required**: f'c ≥ 5,000 psi, w/cm ≤ 0.40, air-entrainment, minimum cover 2.5"

### Bridge Decks
- **F3** (de-icing salts + freezing)
- **C2** (severe chloride)
- **W1** (water penetration)
- **S0** or **S1** (depends on soil)

**Required**: f'c ≥ 5,000 psi, w/cm ≤ 0.40, air-entrainment, cover 2.5-3.0"

### Basement Walls
- **F0** or **F1** (below grade, limited freezing)
- **W1** or **W2** (water-retaining)
- **C1** (moisture, no chlorides)
- **S0**, **S1**, or **S2** (depends on soil sulfates)

**Required**: Test soil for sulfates, typically f'c ≥ 4,000 psi, w/cm ≤ 0.50

### Marine Structures (Splash Zone)
- **F2** or **F3** (if in freezing climate)
- **C2** (severe chloride from seawater)
- **W0** (not water-retaining)
- **S2** (seawater sulfates)

**Required**: f'c ≥ 5,000 psi, w/cm ≤ 0.40, cover 3.0", sulfate-resistant cement

### Interior Slabs (Climate-Controlled Building)
- **F0** (no freezing)
- **W0** (no water exposure)
- **C0** (dry environment)
- **S0** (no soil contact)

**Required**: Minimal restrictions, f'c as needed for structural design

---

## Air Entrainment Requirements

**When Required**: F2 and F3 exposure classes

### Target Air Content (% by volume)

| Nominal Max Aggregate Size | F2 | F3 |
|----------------------------|----|----|
| 3/8 in | 6.0% | 7.5% |
| 1/2 in | 5.5% | 7.0% |
| 3/4 in | 5.0% | 6.0% |
| 1 in | 4.5% | 6.0% |
| 1-1/2 in | 4.5% | 5.5% |

**Tolerance**: ±1.5% from target

---

## Cover Requirements by Exposure Class

### Cast-in-Place Concrete

| Member Type | C0, C1 | C2 |
|-------------|--------|-----|
| Beams, columns | 1.5" | 2.0" |
| Slabs, walls | 3/4" | 1.5" |
| Footings (on soil) | 3.0" | 3.0" |

### Prestressed Concrete

**Higher cover required**: Add 1/2" to values above for C2 exposure

---

## Decision Tree Summary

```
START
  ↓
Freezing? → YES → Moisture level → F1, F2, or F3
  ↓ NO
  F0
  ↓
Water penetration concern? → YES → W1 or W2
  ↓ NO
  W0
  ↓
Chloride exposure? → YES → Chloride level → C1 or C2
  ↓ NO
  C0
  ↓
Soil sulfates? → YES → Test soil → S1, S2, or S3
  ↓ NO
  S0
  ↓
DETERMINE MOST RESTRICTIVE REQUIREMENTS
  ↓
SELECT: f'c, w/cm, cover, cement type, air content
```

---

## Critical Notes

1. **Multiple Exposure Classes**: A member can be in multiple classes simultaneously
   - Use the **most restrictive requirement** for each parameter

2. **Water-Cement Ratio (w/cm)**:
   - Includes all cementitious materials (cement + pozzolans + slag)
   - Critical for durability

3. **Testing**:
   - Sulfate content must be determined by laboratory testing
   - Air content must be verified in fresh concrete

4. **Special Cases**:
   - Lightweight aggregate: May require adjustment
   - Supplementary cementitious materials: Can help meet requirements
   - Admixtures: Must be compatible with air-entrainment

5. **Reference**: ACI 318-25 Chapter 19 for complete requirements

---

*For detailed requirements, consult ACI 318-25 Chapter 19: Concrete - Design and Durability Requirements*
