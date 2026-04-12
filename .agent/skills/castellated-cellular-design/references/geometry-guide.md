# Geometry Guide

Quick reference for castellated and cellular beam geometry, nomenclature, and design limits.

## Nomenclature Systems

### Castellated Beam Designation

**Format:** CB[depth]×[weight]

**Example:** CB18×14
- CB = Castellated Beam
- 18 = Approximate depth in inches (≈ 1.5 × parent depth)
- 14 = Weight per linear foot (same as parent beam)

**Parent Beam:** W12×14 (12 in. depth, 14 lb/ft)

### Cellular Beam Designation

**Format:** LB[depth]×[weight]

**Example:** LB18×14
- LB = Cellular/Litzka Beam
- 18 = Approximate depth in inches (≈ 1.5 × parent depth)
- 14 = Weight per linear foot (same as parent beam)

**Parent Beam:** W12×14

### Asymmetric Section Designation

**Format:** CB[depth]×[top weight]/[bottom weight]

**Example:** CB30×44/57
- Depth: 30 in. (expanded)
- Top tee from: W21×44
- Bottom tee from: W21×57
- Average weight: (44 + 57)/2 = 50.5 lb/ft

**Used when:** Different parent beams for top and bottom
**Common in:** Composite floor beams (smaller top tee with concrete)

---

## Geometric Parameters

### Castellated Beams

```
Parent beam depth:    d
Expanded beam depth:  d_g = d + h_o
Expansion ratio:      d_g/d ≈ 1.5 (typical)

Opening dimensions:
  Height:             h_o = 2h
  Half-height:        h
  Horizontal length:  b = 0.5h_o/tan(θ)
  Cutting angle:      θ (typically 45°, 60°, or custom)

Tee dimensions:
  Length:             e
  Depth:              d_t = (d - h_o)/2

Spacing:
  Opening spacing:    S = 2e + 2b
  Web post length:    s = 2e
```

#### Key Ratios
```
h_o/d ≈ 1.0    (opening height ≈ parent depth)
e/h_o ≈ 0.5    (typical)
2h/e = 1.5-4.0 (web post aspect ratio)
```

### Cellular Beams

```
Parent beam depth:     d
Opening diameter:      D_o
Expanded beam depth:   d_g = d + D_o/2 - loss

Loss calculation:
  loss = D_o/2 - √[(D_o/2)² - (S-D_o)²/4]

Tee dimensions:
  Depth at net section:      d_t-net = (d_g - D_o)/2
  Depth at critical section: d_t-crit = D_o/2 - y + d_t-net

Critical section:
  Distance from center:      0.225D_o
  y = √[(0.5D_o)² - (0.225D_o)²]

Spacing:
  Opening spacing:           S (center-to-center)
  Web post length:           s = S - D_o
```

#### Key Ratios
```
D_o/d ≈ 1.0-1.2    (opening ≈ parent depth)
S/D_o = 1.08-1.5   (REQUIRED LIMIT)
d_g/D_o = 1.25-1.75 (REQUIRED LIMIT)
```

---

## Typical Geometry Ranges

### Expansion Ratios

| Type | Minimum | Typical | Maximum | Notes |
|------|---------|---------|---------|-------|
| Castellated | 1.25 | 1.5 | 1.75 | Standard is 1.5 |
| Cellular | 1.25 | 1.43-1.50 | 1.75 | Check limits |

**Formula:**
```
Expansion Ratio = d_g / d
```

**Example:** W12×14 → CB18×14
```
18 in. / 12 in. = 1.5
```

### Opening Sizes

#### Castellated Beams

| Parent Depth | Typical h_o | Typical Opening Height | b (θ=60°) |
|--------------|-------------|------------------------|-----------|
| 8 in. | 8 in. | 2×4 in. | 2.3 in. |
| 12 in. | 12 in. | 2×6 in. | 3.5 in. |
| 16 in. | 16 in. | 2×8 in. | 4.6 in. |
| 21 in. | 21 in. | 2×10.5 in. | 6.1 in. |
| 24 in. | 24 in. | 2×12 in. | 6.9 in. |

**Rule of Thumb:** h_o ≈ d (opening height ≈ parent depth)

#### Cellular Beams

| Parent Depth | Typical D_o | D_o/d Ratio | Typical S |
|--------------|-------------|-------------|-----------|
| 8 in. | 8-9 in. | 1.0-1.1 | 10-12 in. |
| 12 in. | 12-13 in. | 1.0-1.1 | 15-18 in. |
| 16 in. | 16-18 in. | 1.0-1.1 | 20-24 in. |
| 21 in. | 21-23 in. | 1.0-1.1 | 26-32 in. |
| 24 in. | 24-26 in. | 1.0-1.1 | 30-36 in. |

**Rule of Thumb:** D_o ≈ 1.0d to 1.1d

### Opening Spacing

#### Castellated Beams
```
S = 2e + 2b

Typical e/d ratios: 0.25 to 0.4
Results in S/d: 1.0 to 1.5
```

#### Cellular Beams
```
S/D_o must be: 1.08 < S/D_o < 1.5

Typical S/D_o: 1.25 to 1.40
```

| D_o | Min S (S/D_o=1.08) | Typical S (S/D_o=1.35) | Max S (S/D_o=1.5) |
|-----|-------------------|----------------------|------------------|
| 12 in. | 13.0 in. | 16.2 in. | 18.0 in. |
| 18 in. | 19.4 in. | 24.3 in. | 27.0 in. |
| 24 in. | 25.9 in. | 32.4 in. | 36.0 in. |

---

## Design Limits and Constraints

### Geometric Limits for Cellular Beams

**CRITICAL - Must verify before using design procedures:**

```
1.08 < S/D_o < 1.5
1.25 < d_g/D_o < 1.75
```

**If outside these limits:** Design procedures in Section 3.4.2 may not be applicable.

### Web Post Aspect Ratio

**Recommended minimum to prevent buckling:**
```
s/d_p > 1.25 to 1.5
```

Where:
- s = web post length
- d_p = web post depth

**For castellated:**
```
s = 2e
d_p ≈ d_t (varies slightly through depth)
```

**For cellular:**
```
s = S - D_o
d_p ≈ d_t-net
```

### Cutting Angle Limits (Castellated)

| Angle θ | Web Post φ_b | Applications | Notes |
|---------|--------------|--------------|-------|
| 43-47° | 0.90 | Standard | Good buckling resistance |
| 52.5° | 0.60 | Avoid | Lowest resistance |
| 58-62° | 0.90 | Standard | Good buckling resistance |
| Custom | Interpolate | Special | Linear interpolation |

**Most common:** θ = 60° (equilateral triangle pattern)

### Opening Size vs. Beam Depth

| D_o/d or h_o/d | Classification | Performance | Notes |
|----------------|----------------|-------------|-------|
| < 0.8 | Conservative | Excellent | May not need expansion |
| 0.8 - 1.0 | Typical | Good | Standard range |
| 1.0 - 1.2 | Aggressive | Adequate | Check deflection carefully |
| > 1.2 | Excessive | Poor | Not recommended |

---

## End Spacing and Connection Details

### Minimum Distance from Support

**End spacing "a"** = distance from support to edge of first opening

#### Castellated Beams
```
Recommended minimum: a ≥ 0.5h_o to 0.8h_o
Typical: a ≈ e (same as opening spacing)
```

#### Cellular Beams
```
Recommended minimum: a ≥ 0.5D_o to 0.8D_o
Typical: a ≈ 0.75D_o
```

### End Pattern Designations

| Pattern | Description | At Beam End | Applications |
|---------|-------------|-------------|--------------|
| **"1"** | Full opening | Full opening | Maximum depth at end |
| **"O"** | Half opening (crown) | Half circle/hexagon | Reduced end depth |
| **"OO"** | Two half openings | Split opening | Special connections |

**Standard recommendation:** Use "O" or partial opening at ends to:
- Reduce shear demand at first full opening
- Provide better bearing area
- Simplify end connections

### Minimum Diagonal Distance to First Opening

For coped ends:
```
e' ≥ s (minimum diagonal distance from cope corner to opening edge)
```

Where:
- e' = diagonal distance
- s = opening spacing (or web post length)

**Purpose:** Prevent shear failure path through cope

---

## Comparison: Castellated vs. Cellular

### Geometric Comparison

| Feature | Castellated | Cellular | Advantage |
|---------|-------------|----------|-----------|
| **Opening shape** | Hexagonal | Circular | Cellular: smoother stress |
| **Manufacturing** | Zigzag cut | Two circular cuts | Castellated: less waste |
| **Typical depth** | 1.5d | 1.43-1.50d | Castellated: more expansion |
| **Opening size** | h_o ≈ d | D_o ≈ 1.0-1.1d | Similar |
| **Spacing flexibility** | Free (S=2e+2b) | Limited (1.08<S/D_o<1.5) | Castellated: more flexible |
| **Sharp corners** | Yes (4 per opening) | No | Cellular: better for galvanizing |
| **Vierendeel location** | At center | At 0.225D_o | Cellular: more complex |
| **Critical section** | Not needed | Required | Castellated: simpler |

### When to Use Each

**Prefer Castellated when:**
- Maximum depth expansion desired (1.5×)
- Flexibility in spacing needed
- Paint/bare steel finish
- Lower fabrication cost important
- Existing design standards/details

**Prefer Cellular when:**
- Hot-dip galvanizing required
- Smoother stress distribution desired
- Architectural appearance important
- HVAC duct clearance critical (round ducts)
- European/international standards followed

---

## Standard Cutting Patterns

### Castellated Beam Patterns

#### 60° Pattern (Most Common)
```
tan(60°) = √3 ≈ 1.732
b = h/tan(60°) = h/1.732 ≈ 0.577h
For h = 6 in.: b ≈ 3.46 in.
```

#### 45° Pattern
```
tan(45°) = 1.0
b = h/tan(45°) = h
For h = 6 in.: b = 6 in.
```

### Cellular Beam Standard Patterns

| Pattern | S/D_o | d_g/D_o | Description | Use |
|---------|-------|---------|-------------|-----|
| **Tight** | 1.10 | 1.30 | Close spacing | High shear regions |
| **Standard** | 1.35 | 1.50 | Typical | General purpose |
| **Wide** | 1.45 | 1.65 | Wide spacing | Low shear, high moment |

---

## Depth Customization

### Fixed Depth Requirements

If specific depth required:
1. Work backwards from d_g
2. Select appropriate parent beam
3. Calculate required opening size
4. Verify against limits

**Example:** Need 20-in. depth cellular beam
```
Target: d_g = 20 in.
Try: W14 series parent
If D_o/d_g = 0.70 (conservative):
  D_o = 0.70 × 20 = 14 in.
Check: Parent W14 can accommodate D_o = 14 in.
Calculate actual d_g and iterate
```

### Depth Range by Parent Beam

| Parent Series | Typical d | Castellated d_g | Cellular d_g |
|---------------|-----------|----------------|--------------|
| **W8×** | 8-9 in. | 12-13 in. | 11-13 in. |
| **W10×** | 10-11 in. | 15-17 in. | 14-16 in. |
| **W12×** | 12-13 in. | 18-20 in. | 17-19 in. |
| **W14×** | 14-15 in. | 21-23 in. | 20-22 in. |
| **W16×** | 16-17 in. | 24-26 in. | 23-25 in. |
| **W18×** | 18-19 in. | 27-29 in. | 26-28 in. |
| **W21×** | 21-22 in. | 31-33 in. | 30-32 in. |
| **W24×** | 24-25 in. | 36-38 in. | 34-37 in. |

---

## Asymmetric Section Geometry

### When to Use

**Composite beams:** Often optimal
- Smaller top tee (W21×44 in example)
- Larger bottom tee (W21×57 in example)
- Concrete resists top compression

**Noncomposite beams:** Rarely used
- Symmetric usually more efficient

### Design Approach

1. Both parent beams must have:
   - Same nominal depth (W21 + W21)
   - Compatible flange widths
   - Compatible web thicknesses (ideally same)

2. Calculate separate properties for:
   - Top tee
   - Bottom tee
   - Combined section

3. Check Vierendeel bending:
   - Top tee (smaller)
   - Bottom tee (larger)
   - Different available strengths

### Weight Calculation

**Average of two parent beams:**
```
CB weight = (W_top + W_bot) / 2

Example: CB30×44/57
Weight = (44 + 57) / 2 = 50.5 lb/ft
```

---

## Quick Reference Formulas

### Castellated Beams
```
d_g = d + h_o
h_o = 2h
S = 2e + 2b
b = h/tan(θ)
d_t = (d - h_o)/2
d_effec ≈ d_g - 2d_t + 2ȳ_tee
```

### Cellular Beams
```
loss = D_o/2 - √[(D_o/2)² - ((S-D_o)/2)²]
d_g = d + D_o/2 - loss
d_t-net = (d_g - D_o)/2
s = S - D_o
Critical section at: 0.225D_o from center
y = √[(0.5D_o)² - (0.225D_o)²]
```

### Section Properties
```
A_net = 2A_tee
I_x-net = 2I_x-tee + 2A_tee(d_effec/2)²
S_x-net = I_x-net / (d_g/2)
Z_x-net = 2A_tee(d_effec/2)
```

---

## Common Pitfalls

1. **Forgetting geometric limits for cellular beams**
   - Always verify 1.08 < S/D_o < 1.5
   - Always verify 1.25 < d_g/D_o < 1.75

2. **Wrong critical section for cellular beams**
   - Use 0.225D_o from center, NOT center
   - Different tee depth at critical vs. net section

3. **Inconsistent units**
   - Keep all dimensions in inches
   - Convert to feet only for loading

4. **Expansion ratio errors**
   - d_g/d ≠ always 1.5
   - Calculate actual expansion based on geometry

5. **End spacing too small**
   - First opening too close to support
   - Results in high shear at first opening

6. **Incompatible parent beams for asymmetric sections**
   - Must use same nominal depth series
   - Check web thickness compatibility

---

## References

- Section 1.3: Nomenclature
- Section 2.3: Web opening size and spacing
- Section 2.3.1: End spacing
- Figure 1-1: Castellated beam manufacturing
- Figure 1-3: Cellular beam manufacturing
- Figure 2-10: Typical split patterns
- Figure 2-11: Depth recommendations (Knowles, 1991)
