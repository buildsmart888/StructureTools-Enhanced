# Moment Classification: Small vs Large Moment

*Critical distinction for base plate design methodology*

## Overview

The classification of moment as "small" or "large" determines the design approach for base plates subjected to combined axial load and flexure. This is one of the most important decisions in base plate design.

---

## Key Concept: Eccentricity

**Eccentricity** (e) = M_r / P_r

Where:
- M_r = required moment (LRFD or ASD)
- P_r = required axial force (compression, LRFD or ASD)

Eccentricity represents the offset of the axial load resultant from the column centerline.

---

## Classification Criterion

**Critical Eccentricity** (e_crit):

e_crit = (N/2) - (P_r / q_max)

Where:
- N = base plate length (parallel to bending), in.
- P_r = required axial compression, kips
- q_max = maximum resultant bearing force per unit width, kips/in.
- q_max = f_p(max) × B
- B = base plate width, in.

### Small Moment Case:
**e ≤ e_crit**

### Large Moment Case:
**e > e_crit**

---

## Small Moment Case (e ≤ e_crit)

### Characteristics:

1. **Full bearing contact**: Entire base plate remains in contact with concrete/grout
2. **Uniform bearing stress distribution**: Bearing stress varies but remains in compression across full plate
3. **No anchor rod tension**: Anchor rods not required to resist applied moment
4. **Bearing resultant shifts**: Compression resultant moves toward high-moment side

### Stress Distribution:

```
 Plate elevation:
 ┌────────────┐
 │            │ ← Column
 │            │
 └────────────┘
 ═════▒▒▒▒▒════  ← Bearing stress (uniform over length Y)
    ↑
  Resultant C
```

Bearing extends over length **Y**, where Y < N. Stress is uniform = f_p over this length.

### Design Approach:

- Use uniform bearing stress methodology (Section 4.4.4)
- Bearing resultant: C = f_p × B × Y
- Resultant location creates eccentricity: ε = N/2 - Y/2
- Moment equilibrium: M_r = P_r × ε
- No anchor rod tension from applied loads

### Anchor Rods:

- Designed for **erection/construction loads only**
- Minimum: (4) rods for stability
- Typical: 3/4" or 1" diameter, Grade 36

### Examples:

- **Example 4.7.9**: Eccentric compression (small moment)
- **Example 4.7.11**: Bending + axial compression + shear (low moment)

---

## Large Moment Case (e > e_crit)

### Characteristics:

1. **Partial bearing contact**: Only portion of plate in compression
2. **Triangular bearing stress distribution**: Stress varies from maximum at edge to zero at neutral axis
3. **Anchor rods in tension**: Required to resist moment
4. **Tension-compression couple**: Internal forces create moment resistance

### Stress Distribution:

```
 Plate elevation:
 ┌────────────┐
 │   ●    ●   │ ← Anchor rods in tension (T)
 │            │ ← Column
 └────────────┘
      ▲▲▲▲      ← Triangular bearing (compression C)
```

Left side: Anchor rods carry tension **T**
Right side: Concrete bearing carries compression **C** (triangular distribution)

### Design Approach:

- Use triangular bearing stress methodology (Section 4.4.3)
- Determine neutral axis location (iterative)
- Calculate anchor rod tension: T
- Calculate compression force: C
- Equilibrium: C = T (for pure moment) or C = T + P_r (for combined loading)
- Moment equilibrium about column centerline

### Anchor Rods:

- **Critical design element**: Must resist calculated tension
- Number, size, grade selected based on required strength
- Check:
  - Steel tensile strength (ACI 318-17.6.1)
  - Concrete breakout strength (ACI 318-17.6.2)
  - Embedment depth h_ef
  - Group effects (overlapping cones)

### Examples:

- **Example 4.7.10**: Pure bending (large moment)
- **Example 4.7.12**: Bending + axial compression + shear (large moment)
- **Example 4.7.13**: Biaxial bending (large moment)

---

## Comparison Table

| Aspect | Small Moment (e ≤ e_crit) | Large Moment (e > e_crit) |
|--------|---------------------------|---------------------------|
| **Bearing contact** | Full plate | Partial plate |
| **Bearing distribution** | Uniform (over length Y) | Triangular |
| **Anchor rod function** | Erection only | Resist moment (tension) |
| **Anchor rod design** | Minimal (construction loads) | Critical (applied loads) |
| **Typical anchor size** | 3/4"-1" Ø, Grade 36 | Varies (often 1"-2"+ Ø) |
| **Design complexity** | Simpler | More complex (iterative) |
| **Common applications** | Gravity columns with small wind | Moment frames, high wind/seismic |
| **Failure mode** | Bearing, plate thickness | Anchor tension, breakout |

---

## Determining Classification

### Step-by-Step Process:

**1. Calculate eccentricity:**
   e = M_r / P_r

**2. Estimate critical eccentricity:**
   - Requires trial base plate size (N × B)
   - Estimate maximum bearing stress f_p(max)
   - Calculate q_max = f_p(max) × B
   - Calculate e_crit = N/2 - P_r/q_max

**3. Compare:**
   - If e ≤ e_crit → **Small moment case**
   - If e > e_crit → **Large moment case**

**4. Iterate if needed:**
   - If large moment case but want small moment behavior:
     - Increase base plate size (N and/or B)
     - Reduces e_crit, may shift to small moment range
   - Trade-off: Larger plate vs. anchor rod tension design

---

## Design Implications

### When to Prefer Small Moment Case:

**Advantages**:
- Simpler design (no anchor rod tension calculations)
- Smaller/fewer anchor rods
- Lower embedment depth requirements
- Easier construction (rod placement less critical)
- More forgiving of construction tolerances

**Design strategy**:
- Increase base plate dimensions to shift e_crit higher
- Often economical for moderate moments

### When Large Moment Case is Unavoidable:

**Situations**:
- High wind or seismic moments
- Moment frame connections (rigid base)
- Space constraints (limited plate size)
- Uplift loading (pure tension + moment)

**Design focus**:
- Anchor rod design is critical
- Concrete breakout often governs
- Adequate embedment depth essential
- Careful construction quality control

---

## Special Cases

### Pure Bending (M only, no P):

- Always **large moment case**
- No axial compression to provide bearing couple
- Anchor rods on one side in tension, bearing on opposite side
- See Example 4.7.10

### High Compression with Small Moment:

- Large P_r, small M_r → small e
- Often **small moment case**
- Typical of interior gravity columns with lateral load
- See Example 4.7.9

### Biaxial Moments:

- More complex analysis required
- Concept extends to 3D: Neutral axis at angle
- Classification less clear-cut
- Typically requires anchor rods (large moment approach)
- See Examples 4.7.13, 4.7.14

---

## Common Misconceptions

**Misconception #1**: "Small moment" means small magnitude
- **Reality**: Classification based on **e_crit**, not absolute moment size
- Large plate can make large moment "small" in classification

**Misconception #2**: Anchor rods not needed for small moment
- **Reality**: Still need anchor rods for erection and construction loads
- Just not required for **applied** loads

**Misconception #3**: Can ignore moment if "small"
- **Reality**: Must still include in bearing stress calculations
- Affects bearing length Y and stress distribution

**Misconception #4**: Always better to use small moment approach
- **Reality**: Sometimes large moment case is more economical
- Very large plates can be expensive vs. anchor rods

---

## Design Workflow

```
START: Have M_r and P_r
  ↓
Calculate e = M_r / P_r
  ↓
Select trial base plate N × B
  ↓
Estimate f_p(max) (from concrete strength)
  ↓
Calculate q_max = f_p(max) × B
  ↓
Calculate e_crit = N/2 - P_r/q_max
  ↓
Compare e to e_crit
  ↓
  ├─ e ≤ e_crit → SMALL MOMENT
  │    ↓
  │    Design per Section 4.4.4
  │    - Uniform bearing approach
  │    - Minimal anchor rods
  │    ↓
  │   COMPLETE
  │
  └─ e > e_crit → LARGE MOMENT
       ↓
       Design per Section 4.4.3
       - Triangular bearing approach
       - Anchor rods for tension
       ↓
      COMPLETE
```

---

## Optimization Strategy

**To minimize anchor rod requirements:**

1. **Maximize base plate size** (N and B) within practical limits
2. **Check if increasing N** shifts to small moment case
3. **Balance**: Cost of larger plate vs. cost of anchor rod design
4. **Consider**:
   - Plate material cost
   - Anchor rod installation complexity
   - Embedment depth requirements
   - Construction tolerances

**General guideline**:
- If close to e_crit, try increasing plate size
- If e >> e_crit, accept large moment case (plate size impractical)

---

## References

- **Section 3.2**: Base connections with axial load
- **Section 4.4.3**: Combined axial tension and flexure
- **Section 4.4.4**: Combined axial compression and flexure
- **Example 4.7.9**: Small moment case illustration
- **Example 4.7.10**: Large moment case (pure bending)
- **Example 4.7.11**: Small moment with shear
- **Example 4.7.12**: Large moment with shear
- **Drake and Elkin (1999)**: Original methodology development
