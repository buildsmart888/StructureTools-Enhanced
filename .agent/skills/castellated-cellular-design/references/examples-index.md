# Design Examples Index

Quick reference guide to the four comprehensive design examples in AISC Design Guide 31, Chapter 4.

## Summary Table

| Example | Beam Type | Composite | Parent Beam | Expanded Beam | Span | Application | Key Checks | Pages |
|---------|-----------|-----------|-------------|---------------|------|-------------|------------|-------|
| **4.1** | Castellated | No | W12×14 | CB18×14 | 40 ft | Roof beam | All failure modes | 25-39 (51-70 in PDF) |
| **4.2** | Cellular | No | W12×14 | LB18×14 | 40 ft | Roof beam | All failure modes | 40-54 (71-88 in PDF) |
| **4.3** | Castellated | Yes (Full) | W21×44 (top)<br>W21×57 (bot) | CB30×44/57 | 50 ft | Floor beam | Composite action<br>Asymmetric section | 55-77 (89-104 in PDF) |
| **4.4** | Cellular | Yes (Full) | W21×44 (top)<br>W21×57 (bot) | LB30×44/57 | 50 ft | Floor beam | Composite action<br>Asymmetric section | 78-100 (105-117 in PDF) |

## Example 4.1: Noncomposite Castellated Beam

### Description
40-ft simple span roof beam with uniform loading, fully braced by roof deck.

### Key Parameters
- **Parent Beam:** W12×14
- **Castellated Beam:** CB18×14
- **Geometry:**
  - e = 3.00 in. (tee length)
  - b = 3.50 in. (horizontal length)
  - h = 5.90 in. (half-height of opening)
  - h₀ = 11.8 in. (opening height)
  - θ = 59.3° (cutting angle)
  - S = 13.0 in. (opening spacing)
  - d_g = 17.8 in. (expanded depth)
- **Material:** ASTM A992 (F_y = 50 ksi)
- **Loading:**
  - Dead load = 25 psf (+ beam weight)
  - Live load = 20 psf
  - Beam spacing = 5 ft
- **Bracing:** Fully braced (L_b = 0)

### Failure Modes Checked
1. Vierendeel bending (Section 3.2)
   - Axial compression in tees
   - Flexural bending in tees
   - Combined axial + flexural interaction
2. Web post buckling (Section 3.4.1)
   - Horizontal shear in web posts
   - Web post flexural strength
3. Horizontal shear (Section 3.5.1)
4. Vertical shear - net section (Section 3.5.2)
5. Vertical shear - gross section (Section 3.5.2)
6. Deflection (Section 3.7)
   - Live load: L/430 < L/240 ✓
   - Total load: L/180 = L/180 ✓
   - Camber: 1.5 in. specified

### Design Methods
Both LRFD and ASD presented in parallel.

### Key Results
- Governing interaction: 0.741 (LRFD), 0.815 (ASD) at Opening 16
- Web post buckling controls at first opening
- All checks pass

### Learning Points
- Symmetric section (same tee top and bottom)
- Shows complete calculation workflow
- Demonstrates importance of checking each opening
- Illustrates use of 90% I_x for deflection

## Example 4.2: Noncomposite Cellular Beam

### Description
Same configuration as Example 4.1 but with cellular (circular) openings instead of castellated (hexagonal).

### Key Parameters
- **Parent Beam:** W12×14
- **Cellular Beam:** LB18×14
- **Geometry:**
  - D₀ = 12.3 in. (opening diameter)
  - S = 16.8 in. (opening spacing)
  - e = 4.50 in. (web post length)
  - d_g = 17.6 in. (expanded depth)
  - d_{t-net} = 2.65 in. (tee depth at net section)
  - d_{t-crit} = 3.31 in. (tee depth at critical section)
  - Critical section at 0.225D₀ from center
- **Limits checked:**
  - S/D₀ = 1.37 (1.08 < S/D₀ < 1.5 ✓)
  - d_g/D₀ = 1.43 (1.25 < d_g/D₀ < 1.75 ✓)
- **Material:** ASTM A992 (F_y = 50 ksi)
- **Loading:** Same as Example 4.1

### Failure Modes Checked
1. Vierendeel bending (Section 3.2)
   - Calculations at both net section and critical section
   - Critical section located 0.225D₀ from opening center
2. Web post buckling (Section 3.4.2)
   - Uses cellular beam equations (C1, C2, C3 coefficients)
3. Horizontal shear (Section 3.5.1)
4. Vertical shear - net and gross sections (Section 3.5.2)
5. Deflection (Section 3.7)

### Key Results
- Similar performance to castellated beam
- Slightly different failure mode interactions
- All checks pass

### Learning Points
- Critical section concept for cellular beams
- Different web post buckling formulation vs. castellated
- Geometric limit verification important
- Smoother stress distribution vs. castellated

## Example 4.3: Composite Castellated Beam

### Description
50-ft simple span floor beam with composite action, asymmetric section using two different parent beams.

### Key Parameters
- **Parent Beams:**
  - Top: W21×44 (smaller - in compression with concrete)
  - Bottom: W21×57 (larger - in tension)
- **Castellated Beam:** CB30×44/57
- **Geometry:**
  - e = 4.50 in. (tee length)
  - b = 5.25 in. (horizontal length)
  - h = 8.87 in. (half-height of opening)
  - θ = 59.4° (cutting angle)
  - S = 19.5 in. (opening spacing)
  - d_g = 30.5 in. (expanded depth)
- **Slab:**
  - 3.25 in. normal weight concrete on 3 in. deck
  - Effective width = 12.5 ft (interior beam)
  - f'_c = 4 ksi
- **Shear Studs:**
  - 3/4 in. diameter × 4.5 in. tall
  - 54 total studs (full composite action achieved)
- **Material:** ASTM A992 steel
- **Loading:**
  - Dead load = 100 psf (incl. slab, fireproofing, MEP)
  - Live load = 125 psf (heavy office/commercial)
  - Beam spacing = 12.5 ft

### Failure Modes Checked
1. Composite section strength
   - Check if fully composite or partially composite
   - Calculate concrete compression block depth
2. Vierendeel bending in composite beams (Section 3.3)
   - Concrete deck reduces top tee force
   - Asymmetric top/bottom tee forces
   - Concrete punching shear strength considered
3. Web post buckling
   - Top and bottom tees checked separately (different sizes)
4. Horizontal and vertical shear
5. Deflection
   - Pre-dead load (before composite action)
   - Post-dead load (after composite action)
   - Live load

### Design Methods
Both LRFD and ASD presented.

### Key Results
- Full composite action achieved with 54 studs
- Asymmetric section reduces top tee size requirement
- Concrete takes compression, reduces Vierendeel moments
- Deflection controlled by pre-composite condition

### Learning Points
- Benefits of asymmetric sections for composite beams
- Importance of checking composite vs. non-composite
- Concrete contribution to shear resistance
- Staged construction deflection analysis
- Shear stud density calculations

## Example 4.4: Composite Cellular Beam

### Description
Same configuration as Example 4.3 but with cellular openings. Demonstrates full composite cellular beam design with asymmetric section.

### Key Parameters
- **Parent Beams:**
  - Top: W21×44
  - Bottom: W21×57
- **Cellular Beam:** LB30×44/57
- **Geometry:**
  - D₀ = 18.5 in. (opening diameter)
  - S = 25.2 in. (opening spacing)
  - d_g = 30.5 in. (expanded depth)
  - Critical sections at 0.225D₀ from center
- **Limits checked:**
  - S/D₀ = 1.36 (1.08 < S/D₀ < 1.5 ✓)
  - d_g/D₀ = 1.65 (1.25 < d_g/D₀ < 1.75 ✓)
- **Composite Details:** Same as Example 4.3
- **Material:** ASTM A992
- **Loading:** Same as Example 4.3

### Failure Modes Checked
1. Full composite action verification
2. Vierendeel bending at critical section
   - Top and bottom tees (asymmetric)
   - Concrete contribution
3. Web post buckling (cellular formulation)
4. Horizontal and vertical shear
5. Deflection (staged analysis)

### Key Results
- Full composite action achieved
- All checks pass with asymmetric cellular sections
- Performance similar to castellated equivalent

### Learning Points
- Cellular beam equations for composite design
- Critical section analysis for cellular + composite
- Asymmetric section benefits maintained
- Staged deflection analysis same approach

## Comparison of Examples

### Noncomposite vs. Composite
| Aspect | Noncomposite (4.1, 4.2) | Composite (4.3, 4.4) |
|--------|-------------------------|----------------------|
| Tee forces | Symmetric, both in flexure | Asymmetric, concrete takes compression |
| Vierendeel moment | Higher (no concrete help) | Lower (concrete resists shear) |
| Deflection | Single calculation | Staged (pre/post composite) |
| Section selection | Symmetric usually optimal | Asymmetric often optimal |
| Complexity | Moderate | Higher |

### Castellated vs. Cellular
| Aspect | Castellated (4.1, 4.3) | Cellular (4.2, 4.4) |
|--------|------------------------|---------------------|
| Opening shape | Hexagonal | Circular |
| Vierendeel moment location | At opening center | At critical section (0.225D₀) |
| Web post buckling | Angle-dependent (θ = 45°, 60°) | D₀/t_w dependent (C1, C2, C3) |
| Geometric limits | θ angle, e/h₀ ratio | S/D₀ and d_g/D₀ ratios |
| Stress concentration | Higher at corners | Lower (smooth transitions) |
| Galvanizing | More difficult (re-entrant corners) | Easier (smooth curves) |

## Using These Examples

### For Design
1. Select example matching your application (composite/noncomposite, castellated/cellular)
2. Follow step-by-step workflow
3. Adapt geometry and loading to your project
4. Verify all geometric limits before proceeding

### For Verification
1. Use as benchmark for software calculations
2. Check each failure mode independently
3. Verify interaction equations

### For Learning
1. Start with Example 4.1 (simplest case)
2. Progress to Example 4.2 (cellular variation)
3. Move to Examples 4.3 and 4.4 (composite complexity)

## Key Formulas by Example

### All Examples
- Axial force: P_r = M_r / d_effec
- Deflection: Use 0.90·I_x

### Castellated (4.1, 4.3)
- Vierendeel moment: M_Vr = V_r(e/2)
- Web post moment: M_rh = V_rh·h

### Cellular (4.2, 4.4)
- Vierendeel moment: M_Vr = V_r(D₀/4)(A_tee-crit/A_crit)
- Web post moment: M_rh = 0.90(D₀/2)V_rh
- Critical section: 0.225D₀ from center

### Composite (4.3, 4.4)
- Concrete force: C_1 = 0.85f'_c·a·b_eff
- Concrete shear: V_nc = 3(h_r + t_c)t_c√(4√f'_c)
- Stud requirement: N ≥ V'/Q_n

## Common Pitfalls Illustrated

1. **Forgetting geometric limits** - Examples 4.2 and 4.4 show verification
2. **Using wrong Vierendeel location** - Critical section vs. center for cellular
3. **Neglecting concrete shear contribution** - Examples 4.3 and 4.4 show proper inclusion
4. **Incorrect deflection calculation** - All examples use 0.90·I_x factor
5. **Missing staged analysis** - Examples 4.3 and 4.4 show pre/post composite
6. **Wrong web post buckling equations** - Different for castellated vs. cellular

## References Within Examples

Each example references specific sections of Chapter 3 for detailed procedures:
- Section 3.2: Vierendeel bending
- Section 3.3: Composite Vierendeel bending
- Section 3.4: Web post buckling
- Section 3.5: Shear
- Section 3.6: Lateral-torsional buckling
- Section 3.7: Deflection
- Section 3.8: Concentrated loading
