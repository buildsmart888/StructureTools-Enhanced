# Base Plate Connection Design Flowchart

*Decision tree and step-by-step process for designing steel column base connections*

---

## STEP 1: Define Connection Type and Loading

### 1.1 Determine Connection Configuration

**Is the column embedded in concrete?**

→ **YES** → Use **Chapter 5: Embedded Base Connections**
   - Column extends into concrete footing/pier
   - Load transfer through embedded portion
   - See Section 5.2 for load transfer mechanisms

→ **NO** → Use **Chapter 4: Exposed Base Connections** (most common)
   - Base plate sits on top of concrete
   - Load transfer through plate bearing and anchor rods
   - Continue to Step 1.2

### 1.2 Identify Loading Components

Check which load components are present:

- [ ] Axial compression (P_compression)
- [ ] Axial tension (P_tension)
- [ ] Moment about one axis (M_x or M_y)
- [ ] Moment about both axes (biaxial: M_x AND M_y)
- [ ] Shear in one direction (V_x or V_y)
- [ ] Shear in both directions (biaxial: V_x AND V_y)

**Proceed to Step 2 with identified load components**

---

## STEP 2: Select Design Path Based on Loading

### Loading Category Matrix

| Axial | Moment | Shear | Design Path | Example |
|-------|--------|-------|-------------|---------|
| Compression only | No | No | **Path A: Simple Compression** | 4.7.1, 4.7.2, 4.7.3 |
| Compression | No | Yes | **Path B: Compression + Shear** | 4.7.4, 4.7.5 |
| Tension only | No | Yes | **Path C: Tension + Shear** | 4.7.6, 4.7.8 |
| Compression | Uniaxial | No | **Path D: Compression + Moment** | 4.7.9, 4.7.10 |
| Compression | Uniaxial | Yes | **Path E: Compression + Moment + Shear** | 4.7.11, 4.7.12 |
| Compression | Biaxial | Any | **Path F: Biaxial Loading** | 4.7.13, 4.7.15 |
| Tension | Biaxial | Any | **Path G: Tension + Biaxial** | 4.7.14 |

---

## PATH A: Simple Compression (Axial Only)

**Applicable when**: Compression with negligible moment and shear

### A.1 Material Selection
1. Select base plate material (typically A36, Fy = 36 ksi)
2. Select concrete strength (f'_c, typically 3000-4000 psi)
3. Select grout strength (f'_g ≥ f'_c)

### A.2 Initial Base Plate Sizing
1. Estimate initial plate dimensions N × B
   - Rule of thumb: Start with plate extending 2"-4" beyond column flanges
   - For W-shapes: N ≈ d + 4", B ≈ b_f + 4"

### A.3 Check Concrete Bearing Strength

**Calculate available bearing strength:**

LRFD: φP_p = 0.65 × 0.85f'_c × A1 × √(A2/A1) ≤ 0.65 × 1.7f'_c × A1

ASD: P_p/Ω = (0.85f'_c × A1 × √(A2/A1)) / 2.31 ≤ (1.7f'_c × A1) / 2.31

Where:
- A1 = N × B (base plate area)
- A2 = larger supporting area (maximum √(A2/A1) = 2.0)
- Confinement factor √(A2/A1) increases capacity when A2 > A1

**Check:** P_r ≤ φP_p (LRFD) or P_r ≤ P_p/Ω (ASD)

### A.4 Determine Required Base Plate Thickness

**Calculate cantilever dimensions:**
- m = (N - 0.95d) / 2
- n = (B - 0.80b_f) / 2
- λ = 2√X / (1 + √(1-X))
  where X = (4d_b P_u) / ((d+b_f)² × f_p)

**Calculate required thickness:**
- l = max(m, n, λn')
- t_pl(reqd) = l × √(2P_u / (0.9F_y × B × N))

**Select standard plate thickness** t_pl ≥ t_pl(reqd)

### A.5 Design Column-to-Plate Welds
1. Calculate required weld size based on column load
2. Typically use fillet welds around column perimeter
3. Check AISC Specification Section J2

### A.6 Select Anchor Rods (for erection/wind uplift only)
- Minimum 4 anchor rods for stability
- Typically (4) 3/4" or 1" diameter, Grade 36
- Designed for construction loads and wind uplift

**→ Design complete for Path A**

---

## PATH B: Compression + Shear

**Applicable when**: Axial compression with horizontal shear force

### B.1 Complete Path A (Steps A.1 through A.5)
Design for compression as if shear were not present

### B.2 Check Shear Transfer Mechanism

**Calculate available friction resistance:**

LRFD: φV_f = 0.75 × μ × P_u = 0.75 × 0.55 × P_u

ASD: V_f/Ω = (μ × P_a) / 2.00 = (0.55 × P_a) / 2.00

Where μ = 0.55 (friction coefficient for steel on grout/concrete)

### B.3 Evaluate Shear Transfer

**Is friction sufficient?**

→ **YES** (V_r ≤ φV_f or V_r ≤ V_f/Ω)
   - Shear transferred by friction alone
   - No additional elements required
   - **→ Design complete for Path B**

→ **NO** (V_r > φV_f or V_r > V_f/Ω)
   - Friction insufficient
   - **Proceed to Step B.4 (Shear Lug Design)**

### B.4 Design Shear Lug

**Shear lug required when friction is inadequate**

1. **Size the shear lug:**
   - Required shear: V_lug = V_r - φV_f (or V_r - V_f/Ω)
   - Typical: Use plate welded to bottom of base plate
   - Height: Sufficient for concrete bearing
   - Length: Full width or portion of base plate

2. **Check shear lug bearing on concrete:**
   - Per ACI 318, Section 17 (structural steel embedment)
   - Available bearing: φ × A_bearing × design bearing stress

3. **Design welds:**
   - Shear lug to base plate welds
   - Must transfer full shear force

**See Example 4.7.5 for detailed shear lug design**

**→ Design complete for Path B**

---

## PATH C: Tension + Shear (Anchor Rods)

**Applicable when**: Axial tension (uplift) with shear

### C.1 Material Selection
1. Select base plate material
2. Select anchor rod grade (ASTM F1554 Grade 36, 55, or 105)
3. Determine concrete strength f'_c

### C.2 Preliminary Anchor Rod Layout
1. Determine number of anchor rods (typically 4, 6, or 8)
2. Establish anchor rod pattern
   - Align with column bolt holes if possible
   - Provide adequate edge distance

### C.3 Design Anchor Rods for Tension

**Calculate required anchor rod strength:**
- T_per_rod = T_total / number of rods
- Include prying action if applicable

**Check anchor rod steel strength (ACI 318 Section 17.6.1):**

LRFD: φN_sa = φ × 0.75 × A_se × F_uta

ASD: N_sa/Ω = (0.75 × A_se × F_uta) / 2.00

Where:
- A_se = effective cross-sectional area of anchor rod
- F_uta = specified tensile strength
- φ = 0.75 for tension

**Check concrete breakout strength (ACI 318 Section 17.6.2):**
- Individual anchor: Based on h_ef (embedment depth)
- Anchor group: Overlapping failure cones
- See Section 4.5 for detailed calculations

### C.4 Design for Shear

**Check anchor rod shear strength (ACI 318 Section 17.7):**

LRFD: φV_sa = φ × 0.6 × A_se × F_uta

ASD: V_sa/Ω = (0.6 × A_se × F_uta) / 2.00

**Check concrete breakout in shear:**
- Edge distance effects
- Concrete pryout

### C.5 Check Combined Tension + Shear Interaction

**ACI 318 interaction equation:**

(T_ua / φN_n)^(5/3) + (V_ua / φV_n)^(5/3) ≤ 1.0 (LRFD)

(T_a × Ω / N_n)^(5/3) + (V_a × Ω / V_n)^(5/3) ≤ 1.0 (ASD)

### C.6 Design Base Plate

1. Calculate required plate thickness for prying action
2. Design column-to-plate welds

**See Example 4.7.6 for tension + shear design**

**→ Design complete for Path C**

---

## PATH D: Compression + Moment (Uniaxial)

**Applicable when**: Axial compression with moment about one axis

### D.1 Calculate Eccentricity and Classify Moment

**Calculate eccentricity:**
e = M_r / P_r

**Determine moment classification:**

Calculate critical eccentricity:
e_crit = (N/2) - (P_r / (q_max))

where q_max = f_p(max) × B

**Classify moment:**

→ **e ≤ e_crit** → **SMALL MOMENT CASE** (Path D-Small)
   - Uniform bearing stress distribution
   - No anchor rod tension required
   - Full bearing contact
   - Use Section 4.4.4 methodology

→ **e > e_crit** → **LARGE MOMENT CASE** (Path D-Large)
   - Triangular bearing stress distribution
   - Anchor rods required for tension
   - Partial bearing contact
   - Use Section 4.4.3 and 4.4.4 methodology

### PATH D-Small: Small Moment Case

**Step D-Small.1: Size Base Plate**
1. Select initial N × B dimensions
2. Ensure e ≤ e_crit with selected dimensions

**Step D-Small.2: Calculate Bearing Stress**
- Bearing stress is uniform over bearing length Y
- Bearing resultant located at distance ε from centerline

**Step D-Small.3: Check Bearing Capacity**
- Similar to Path A
- P_r ≤ φP_p (LRFD) or P_r ≤ P_p/Ω (ASD)

**Step D-Small.4: Calculate Required Plate Thickness**
- Account for eccentricity effects
- Calculate bending moments in cantilever portions

**Step D-Small.5: Design Welds and Anchor Rods**
- Column-to-plate welds for full load
- Anchor rods for erection only (no tension from applied loads)

**See Example 4.7.9 for small moment design**

**→ Design complete for Path D-Small**

### PATH D-Large: Large Moment Case

**Step D-Large.1: Size Base Plate**
1. Select trial N × B dimensions
2. Position anchor rods (distance f from column face)

**Step D-Large.2: Solve for Bearing Length Y**

Iterative solution for equivalent bearing length Y:
- Equilibrium of forces: C = T (compression = tension)
- Equilibrium of moments about column centerline
- Compatibility with triangular stress distribution

**Step D-Large.3: Calculate Anchor Rod Tension**

T_r = (M_r + P_r × ε) / (d/2 + f)

**Step D-Large.4: Design Anchor Rods**
- Calculate tension per rod
- Check steel strength (ACI 318 Section 17.6.1)
- Check concrete breakout (ACI 318 Section 17.6.2)
- Select anchor rod diameter and grade

**Step D-Large.5: Calculate Required Plate Thickness**
- Check bearing zone cantilever
- Check tension zone cantilever
- Select larger thickness

**Step D-Large.6: Design Welds**
- Column-to-plate welds
- Account for moment and axial load

**See Example 4.7.10 and 4.7.12 for large moment design**

**→ Design complete for Path D-Large**

---

## PATH E: Compression + Moment + Shear

**Applicable when**: Axial compression, moment, and shear combined

### E.1 Classify Moment (Same as Path D)
- Calculate e = M_r / P_r
- Determine if e ≤ e_crit (small) or e > e_crit (large)

### E.2 Design for Compression + Moment
- **If small moment**: Follow Path D-Small
- **If large moment**: Follow Path D-Large

### E.3 Add Shear Design (Same as Path B)
- Check friction resistance: φV_f or V_f/Ω
- If friction insufficient, add shear lug
- Design shear lug per Step B.4

### E.4 Check Anchor Rods for Combined Loading
- **If large moment**: Anchor rods carry tension from moment
- **Check interaction**: Tension from moment + shear force
- Use combined loading provisions (ACI 318 Section 17.8)

**See Examples:**
- **Small moment + shear**: Example 4.7.11
- **Large moment + shear**: Example 4.7.12

**→ Design complete for Path E**

---

## PATH F: Biaxial Loading (Compression + Biaxial Moments)

**Applicable when**: Moments about both axes (M_x AND M_y)

### F.1 Three-Dimensional Analysis Required
- Cannot use simplified 2D approach
- Must consider 3D stress distribution
- Typically requires iterative solution

### F.2 Establish Anchor Rod Pattern
- Typically rectangular pattern (4, 6, or 8 rods)
- Symmetrical about both axes
- Adequate spacing for concrete breakout cones

### F.3 Calculate Neutral Axis Location
- Iterative process to find neutral axis position and angle
- Compression zone on one side, tension zone on opposite
- Satisfies force and moment equilibrium

### F.4 Calculate Anchor Rod Tensions
- Based on distance from neutral axis
- Compatibility of strains
- Rods farthest from neutral axis carry highest tension

### F.5 Design Anchor Rods
- Check each rod individually
- Steel strength per ACI 318 Section 17.6.1
- Concrete breakout for anchor group

### F.6 Calculate Base Plate Thickness
- Check multiple critical sections
- Account for 3D bending

### F.7 Add Shear if Present
- Check friction resistance in both directions
- Shear lug if required (typically along one edge)

**See Examples:**
- **Biaxial compression + bending**: Example 4.7.13
- **Biaxial + shear**: Example 4.7.15

**→ Design complete for Path F**

---

## PATH G: Tension + Biaxial Moments

**Applicable when**: Axial tension (uplift) with moments about both axes

### G.1 All Anchor Rods in Tension
- No bearing on concrete (or minimal)
- All rods participate in resisting tension and moments

### G.2 Calculate Tension in Each Anchor Rod
- Direct tension: T_axial = P_tension / n (n = number of rods)
- Additional tension from M_x based on rod distance from x-axis
- Additional tension from M_y based on rod distance from y-axis
- Combine: T_rod = T_axial + T_Mx + T_My

### G.3 Design Anchor Rods
- Maximum tension governs (typically corner rods)
- Steel strength per ACI 318
- Concrete breakout strength
- Check anchor group behavior

### G.4 Design Base Plate
- Plate must resist prying action at all rods
- Calculate required thickness
- Check at multiple critical sections

### G.5 Design Welds
- Column-to-plate welds for tension load

**See Example 4.7.14 for biaxial tension + bending**

**→ Design complete for Path G**

---

## SPECIAL CONSIDERATIONS

### Seismic Design (Chapter 6)
If connection is part of seismic force-resisting system:
1. Use Chapter 6 provisions in addition to above
2. Consider capacity design principles
3. Check deformation compatibility
4. Use AISC Seismic Provisions requirements

**See Section 6.5 and 6.6 for seismic-specific design**

### Braced Frame Connections
If column base is at braced frame:
1. Resolve brace force into column base loads
2. Check both tension and compression cases (if reversible)
3. Consider gusset plate effects

**See Examples 4.7.7 and 4.7.8 for braced frame bases**

### Embedded Connections (Chapter 5)
If column is embedded in concrete:
1. Load transfer through embedment bearing
2. Different analysis approach
3. See Section 5.2 for load transfer mechanisms

---

## SUMMARY DECISION TREE

```
START
  │
  ├─ Embedded? ─YES→ Chapter 5
  │      │
  │     NO
  │      │
  ├─ Loads? ──┬─ Compression only ───────────→ PATH A
  │           ├─ Compression + Shear ─────────→ PATH B
  │           ├─ Tension + Shear ─────────────→ PATH C
  │           ├─ Compression + Moment ────────→ PATH D
  │           │    ├─ Small moment (e ≤ e_crit)
  │           │    └─ Large moment (e > e_crit)
  │           ├─ Compression + Moment + Shear ─→ PATH E
  │           ├─ Biaxial (compression) ───────→ PATH F
  │           └─ Biaxial (tension) ───────────→ PATH G
  │
  └─ Seismic? ─YES→ Also use Chapter 6
         │
        NO
         │
    COMPLETE
```

---

## QUICK START GUIDE

**For most common case (gravity column base):**
1. Use **PATH A** for initial design (compression only)
2. Add **PATH B** if lateral loads create shear
3. Add **PATH D** or **PATH E** if lateral loads create moments
4. Check if moment is "small" (e ≤ e_crit) or "large" (e > e_crit)
5. Refer to applicable worked example for detailed calculations

**Recommended example progression:**
- Start: Example 4.7.1 (simple compression)
- Add shear: Example 4.7.4 (friction) or 4.7.5 (shear lug)
- Add moment: Example 4.7.9 (small) or 4.7.12 (large)
