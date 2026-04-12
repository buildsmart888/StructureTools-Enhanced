# Failure Modes Guide

Comprehensive guide to the critical failure modes for castellated and cellular beams per AISC Design Guide 31.

## Overview of Failure Modes

Castellated and cellular beams must be checked for all failure modes applicable to standard wide-flange beams, plus additional modes unique to beams with web openings:

### Standard Beam Failure Modes
1. Lateral-torsional buckling (LTB)
2. Flange local buckling
3. Overall flexural strength
4. Overall shear strength

### Additional Failure Modes for Expanded Beams
5. **Vierendeel bending** (typically governing)
6. **Web post buckling** (critical for closely-spaced openings)
7. **Horizontal shear** in web posts
8. **Vertical shear** at net section
9. Web local yielding/crippling at concentrated loads

---

## 1. Vierendeel Bending

### Description
The most critical and unique failure mode for castellated and cellular beams. Vierendeel bending is a secondary moment that develops in the top and bottom tees due to the transfer of shear force around web openings.

### Mechanism
- Global shear must be transferred between top and bottom tees at each opening
- Creates moment couples in the tees
- Four plastic hinges form around each opening at ultimate load:
  - Two hinges in top tee (one on each side of opening)
  - Two hinges in bottom tee (one on each side of opening)

### When It Governs
- High shear regions (near supports)
- Widely-spaced openings (low s/d_p ratio)
- Noncomposite beams (no concrete to resist top tee compression)

### Formulas

#### Axial Force in Tees
```
P_r = M_r / d_effec
```
Where:
- M_r = required global moment at opening
- d_effec = distance between centroids of top and bottom tees

#### Vierendeel Moment - Castellated Beams
```
M_Vr = V_r × (A_tee / A_net) × (e/2)
```

#### Vierendeel Moment - Cellular Beams
```
M_Vr = V_r × (A_tee-crit / A_crit) × (D_o/4)
```
- Critical section located 0.225D_o from opening center
- Moment arm = D_o/4 (not D_o/2)

#### Vierendeel Moment - Composite Beams
```
V_net = V_r - V_c
M_Vr = V_net × (A_tee / A_net) × (lever arm)
```
Where:
- V_c = concrete deck punching shear strength
- Concrete reduces net shear, reducing Vierendeel moment

### Check Procedure

**Step 1:** Calculate axial force in tee
```
P_r = M_r / d_effec
```

**Step 2:** Calculate Vierendeel moment (use appropriate formula above)

**Step 3:** Calculate available axial strength
- Flexural buckling: AISC Spec. Section E3
- Flexural-torsional buckling: AISC Spec. Section E4
- Use minimum of the two

**Step 4:** Calculate available flexural strength
- Yielding: AISC Spec. Section F9.1
- Lateral-torsional buckling: AISC Spec. Section F9.2
- Flange local buckling: AISC Spec. Section F9.3
- Stem local buckling: AISC Spec. Section F9.4
- Use minimum of all applicable

**Step 5:** Check interaction equation
If P_r/(φ_c P_n) ≥ 0.2:
```
P_r/(φ_c P_n) + (8/9)[M_rx/(φ_b M_nx)] ≤ 1.0  (AISC Spec. Eq. H1-1a)
```

If P_r/(φ_c P_n) < 0.2:
```
P_r/(2φ_c P_n) + M_rx/(φ_b M_nx) ≤ 1.0  (AISC Spec. Eq. H1-1b)
```

### Design Assumptions
- K_x = 0.65 (rotation fixed, translation fixed at tee ends)
- K_y = 1.0 (rotation free, translation fixed)
- L = e for castellated beams
- L = D_o/2 for cellular beams

### Reference
Section 3.2 (noncomposite), Section 3.3 (composite)

---

## 2. Web Post Buckling

### Description
Local buckling failure of the solid web section (web post) between adjacent openings. Can occur by flexural failure or buckling failure of the web post.

### Mechanism
- Horizontal shear force develops due to difference in axial forces at adjacent openings
- Web post acts as a vertical strut resisting this horizontal shear
- Failure controlled by web post aspect ratio s/d_p

### When It Governs
- Closely-spaced openings (high s/d_p ratio)
- Thin webs (high e/t_w ratio)
- First opening near support (highest horizontal shear)
- Cutting angles θ near 52.5° for castellated beams (lowest φ_b)

### Critical Parameters

#### Web Post Aspect Ratio
```
Castellated: 2h/e (typical range 1.5 to 4.0)
Cellular: S/D_o (limits: 1.08 < S/D_o < 1.5)
```

#### Web Post Slenderness
```
e/t_w  or  D_o/t_w
```

#### Recommended Minimum Ratios
```
s/d_p > 1.25 to 1.5  (to prevent buckling)
```

### Formulas

#### Horizontal Shear Force
```
V_rh = |T_r(i) - T_r(i+1)|
```
Where:
- T_r(i) = axial force in tee at opening i
- T_r(i+1) = axial force in tee at adjacent opening

#### Required Flexural Strength in Web Post

**Castellated beams:**
```
M_rh = V_rh × h
```
Where h = half-height of opening

**Cellular beams:**
```
M_rh = 0.90 × (D_o/2) × V_rh
```

#### Available Flexural Strength - Castellated Beams

**Plastic moment:**
```
M_p = 0.25 × t_w × (e + 2b)² × F_y
```

**Critical moment ratio** - depends on cutting angle θ:

For θ = 45°:
```
M_ocr/M_p = f(2h/e, e/t_w)  - use Equations 3-23 to 3-25
Limited to 0.26 maximum
```

For θ = 60°:
```
M_ocr/M_p = f(2h/e, e/t_w)  - use Equations 3-26 to 3-28
Limited to 0.493 maximum
```

Interpolate for intermediate angles.

**Resistance factors** (LRFD):
- θ = 43° to 47°: φ_b = 0.90
- θ = 52.5°: φ_b = 0.60 (minimum - least favorable)
- θ = 58° to 62°: φ_b = 0.90
- Linear interpolation between 47° and 58°

**Available strength:**
```
φ_b M_n = φ_b × (M_ocr/M_p) × M_p  (LRFD)
M_n/Ω_b = (M_ocr/M_p) × (M_p/Ω_b)   (ASD)
```

#### Available Flexural Strength - Cellular Beams

**Elastic moment at 0.9R:**
```
M_e = [t_w(S - D_o + 0.564D_o)²/6] × F_y
```

**Coefficients:**
```
C1 = 5.097 + 0.1464(D_o/t_w) - 0.00174(D_o/t_w)²
C2 = 1.441 + 0.0625(D_o/t_w) - 0.000683(D_o/t_w)²
C3 = 3.645 + 0.0853(D_o/t_w) - 0.00108(D_o/t_w)²
```

**Allowable moment ratio:**
```
M_allow/M_e = C1(S/D_o) - C2(S/D_o)² - C3
```

**Available strength:**
```
φ_b M_n = φ_b × (M_allow/M_e) × M_e  (LRFD)
φ_b = 0.90
```

### Check Procedure

**Step 1:** Calculate horizontal shear at each web post
```
V_rh = |T_r(i) - T_r(i+1)|
```

**Step 2:** Calculate required moment (use formula for beam type)

**Step 3:** Calculate available flexural strength
- Use castellated or cellular formulas as appropriate
- Account for cutting angle θ if castellated

**Step 4:** Verify adequacy
```
M_rh ≤ φ_b M_n  (LRFD)
M_rh ≤ M_n/Ω_b   (ASD)
```

**Step 5:** If inadequate, options to improve:
- Increase web thickness (different parent beam)
- Increase opening spacing S
- Change cutting pattern
- Add web post stiffeners (non-standard)

### Reference
Section 3.4.1 (castellated), Section 3.4.2 (cellular)

---

## 3. Horizontal Shear

### Description
Shear force acting along the horizontal neutral axis at each web post. Related to web post buckling but checked as a pure shear limit state.

### Mechanism
Same horizontal shear force V_rh as web post buckling, but checked against shear yielding strength of web post rather than buckling.

### When It Governs
- Rarely governs compared to web post buckling
- More likely for stocky web posts (low e/t_w)
- May govern for very thin parent beam webs

### Formula

#### Required Strength
```
V_rh = |T_r(i) - T_r(i+1)|
```

#### Available Strength
```
V_n = 0.6 × F_y × A_w
```
Where:
- A_w = e × t_w (area of web post)

#### Check
```
LRFD: V_rh ≤ φ_v V_n  (φ_v = 1.00)
ASD:  V_rh ≤ V_n/Ω_v   (Ω_v = 1.50)
```

### Check Procedure

**Step 1:** Calculate V_rh (same as web post buckling)

**Step 2:** Calculate nominal strength
```
V_n = 0.6 × F_y × e × t_w
```

**Step 3:** Apply resistance factor
```
φ_v V_n = 1.00 × V_n  (LRFD)
```

**Step 4:** Verify adequacy
```
V_rh ≤ φ_v V_n
```

### Reference
Section 3.5.1

---

## 4. Vertical Shear

### Description
Traditional beam shear, but must be checked at both the net section (through opening) and gross section (at web post). Net section typically more critical.

### Mechanism
- Global shear force must be resisted by reduced net section at openings
- Web area is reduced where openings occur
- For asymmetric composite sections, shear is distributed between tees based on relative areas

### When It Governs
- Short spans with high shear
- Large openings (high D_o/d_g ratio)
- Near supports

### Formulas

#### At Net Section (Through Opening)

Divide shear between tees:
```
V_r,top = V_r × (A_tee,top / A_net)
V_r,bot = V_r × (A_tee,bot / A_net)
```

Check each tee separately using AISC Spec. Section G3:
```
h/t_w = d_t/t_w
k_v = 1.2 (for tee stems)

When h/t_w ≤ 1.10√(k_v E/F_y):
  C_v2 = 1.0

When h/t_w > 1.10√(k_v E/F_y):
  C_v2 = 1.10√(k_v E/F_y) / (h/t_w)

V_n = 0.6 × F_y × (d_t × t_w) × C_v2
```

For composite beams, add concrete shear strength:
```
V_nc = 3(h_r + t_c)t_c√(4√f'_c)
V_r,net = V_r - V_c  (net shear in steel)
```

#### At Gross Section (At Web Post)

Use AISC Spec. Section G2:
```
h/t_w = (d_g - k_top - k_bot)/t_w
k_v = 5.34 (for webs with flanges both sides)

When h/t_w ≤ 1.10√(k_v E/F_y):
  C_v1 = 1.0

When h/t_w > 1.10√(k_v E/F_y):
  C_v1 = 1.10√(k_v E/F_y) / (h/t_w)

V_n = 0.6 × F_y × (d_g × t_w) × C_v1
```

#### Resistance Factors

```
When h/t_w ≤ 2.24√(E/F_y):
  φ_v = 1.00  (LRFD)
  Ω_v = 1.50  (ASD)

When h/t_w > 2.24√(E/F_y):
  φ_v = 0.90  (LRFD)
  Ω_v = 1.67  (ASD)
```

### Check Procedure

**Step 1:** Calculate global shear V_r at opening location

**Step 2:** For composite beams, calculate concrete shear contribution V_c

**Step 3:** Check net section:
- Distribute shear between top and bottom tees
- Calculate C_v2 for each tee
- Calculate V_n for each tee
- Verify V_r,tee ≤ φ_v V_n

**Step 4:** Check gross section:
- Use full global shear V_r
- Calculate C_v1 for full depth
- Calculate V_n
- Verify V_r ≤ φ_v V_n

**Step 5:** Select appropriate φ_v or Ω_v based on h/t_w

### Reference
Section 3.5.2

---

## 5. Lateral-Torsional Buckling (LTB)

### Description
Out-of-plane buckling of the compression flange combined with twisting of the cross-section. Checked similar to standard wide-flange beams.

### When It Governs
- Long unbraced lengths
- Beams without lateral bracing
- Noncomposite beams (composite deck usually braces top flange)

### Key Differences from Solid Web Beams
1. Use **gross section properties** for calculations
2. No special modifications needed for web openings
3. Expansion increases I_x, generally improving LTB resistance

### Formula

Check per AISC Specification Chapter F, Sections F2-F5:
```
Use gross section:
  I_x-gross
  S_x-gross
  Z_x-gross

Calculate L_p, L_r, M_cr per standard procedures
```

### Check Procedure

**Step 1:** Determine unbraced length L_b

**Step 2:** Calculate gross section properties

**Step 3:** Check per AISC Spec. Chapter F
- Use standard W-shape procedures
- Apply to gross section

**Step 4:** For composite beams:
- May assume deck provides full lateral bracing to top flange
- Bottom flange checked for tension flange yielding

### Reference
Section 3.6

---

## 6. Deflection

### Description
Vertical deflection under service loads. Additional deflection occurs due to shear deformations around openings.

### When It Governs
- Long spans
- Light loading
- Strict deflection limits (vibration-sensitive applications)

### Key Difference from Solid Web Beams
Use **90% of net section moment of inertia** to account for additional shear deformations:
```
I_effective = 0.90 × I_x-net
```

### Formulas

#### Simple Span, Uniform Load
```
Δ = (5wL⁴) / [384E × I_x-net × 0.90]
```

#### Composite Beams - Staged Analysis

**Pre-composite (before deck hardens):**
```
Δ_pre = (5w_pre L⁴) / [384E × I_x-steel × 0.90]
Use steel section only
```

**Post-composite (after deck hardens):**
```
Δ_post = (5w_post L⁴) / [384E × I_x-composite × 0.90]
Use transformed composite section
```

**Total deflection:**
```
Δ_total = Δ_pre + Δ_post
```

### Check Procedure

**Step 1:** Calculate net section I_x

**Step 2:** Apply 90% factor
```
I_eff = 0.90 × I_x-net
```

**Step 3:** Calculate deflection using standard formulas with I_eff

**Step 4:** For composite beams:
- Calculate pre-composite deflection (construction loads on steel only)
- Calculate post-composite deflection (superimposed loads on composite section)
- Sum for total

**Step 5:** Check against limits
```
Live load: Δ_LL ≤ L/240 or L/360
Total load: Δ_TL ≤ L/180 or L/240
```

**Step 6:** Specify camber if needed
```
Typical camber ≈ Δ_DL (dead load deflection)
```

### Reference
Section 3.7

---

## Summary of Typical Governing Failure Modes

### By Beam Type

**Noncomposite Castellated:**
1. Vierendeel bending (high shear regions)
2. Web post buckling (first opening)
3. Deflection (if span/depth > 25)

**Noncomposite Cellular:**
1. Vierendeel bending at critical section
2. Web post buckling
3. Deflection

**Composite Castellated:**
1. Vierendeel bending (reduced but still critical)
2. Web post buckling
3. Pre-composite deflection

**Composite Cellular:**
1. Vierendeel bending at critical section
2. Web post buckling
3. Pre-composite deflection

### By Location Along Beam

**Near Supports (high shear):**
1. Vierendeel bending
2. Web post buckling
3. Vertical shear

**Midspan (high moment):**
1. Overall flexure
2. Lateral-torsional buckling (if unbraced)
3. Deflection

**At Concentrated Loads:**
1. Web local yielding
2. Web crippling
3. Flange local bending

---

## Design Strategy

### Step-by-Step Approach

1. **Select trial section and opening geometry**
   - Start with d_g ≈ 1.5d (parent depth)
   - Check geometric limits

2. **Check Vierendeel bending at each opening**
   - Calculate at multiple locations
   - Usually governs near supports

3. **Check web post buckling**
   - Focus on first few web posts
   - Adjust spacing if needed

4. **Check shear (horizontal and vertical)**
   - Usually satisfied if web post buckling ok

5. **Check lateral-torsional buckling**
   - Use gross section properties
   - Usually not critical if braced

6. **Check deflection**
   - Use 90% I_x factor
   - May govern for long spans

7. **Iterate if needed**
   - Adjust opening size/spacing
   - Change parent beam if necessary

### Quick Checks for Feasibility

Before detailed analysis:
```
1. s/d_p > 1.5 (avoid web post buckling issues)
2. D_o < 0.8d (avoid excessive net section reduction)
3. L/d_g < 30 (deflection likely ok)
4. First opening > 0.5D_o from support (shear ok)
```

---

## References

- Section 3.1: Introduction to design procedures
- Section 3.2: Vierendeel bending in noncomposite beams
- Section 3.3: Vierendeel bending in composite beams
- Section 3.4: Web post buckling
- Section 3.5: Horizontal and vertical shear
- Section 3.6: Lateral-torsional buckling
- Section 3.7: Deflection
- Section 3.8: Concentrated loading
- Chapter 4: Design examples (all failure modes demonstrated)
