# Design Workflow Summary

Step-by-step design checklist for castellated and cellular beams per AISC Design Guide 31.

## Overview

This workflow provides a systematic approach to designing castellated and cellular beams. Follow the steps in order, checking off each as completed.

---

## Phase 1: Preliminary Design

### Step 1: Determine Design Requirements

- [ ] **Span length** (ft)
- [ ] **Beam spacing** (ft)
- [ ] **Loading**
  - Dead load (psf or plf)
  - Live load (psf or plf)
  - Other loads (snow, etc.)
- [ ] **Deflection limits**
  - Live load (typically L/240 or L/360)
  - Total load (typically L/180 or L/240)
- [ ] **Lateral bracing**
  - Unbraced length L_b
  - Bracing type (deck, purlins, etc.)
- [ ] **Composite action?**
  - Yes: Specify slab details (thickness, f'_c, deck type)
  - No: Proceed as noncomposite
- [ ] **Material specification**
  - Steel: ASTM A992 (F_y = 50 ksi) typical
  - Concrete: f'_c (ksi) if composite
- [ ] **Special requirements**
  - Fire protection needs
  - Corrosion protection (galvanizing?)
  - HVAC clearances
  - Architectural appearance

**Reference:** Section 2.1

---

### Step 2: Select Beam Type

Choose between castellated and cellular:

**Select Castellated if:**
- [ ] Maximum depth expansion desired (1.5× typical)
- [ ] Flexible spacing requirements
- [ ] Paint or bare steel finish acceptable
- [ ] Lower fabrication cost priority
- [ ] Sharp corners acceptable

**Select Cellular if:**
- [ ] Hot-dip galvanizing required
- [ ] Architectural appearance important
- [ ] HVAC with round ducts
- [ ] Smoother stress distribution desired
- [ ] European/international practice

**Reference:** Section 1.2, Section 2.2.7

---

### Step 3: Select Parent Beam and Expansion Ratio

#### Trial Parent Beam Selection

Use span/depth guidelines:
```
L/d ≈ 20-30 for solid web beams
L/d_g ≈ 25-35 for expanded beams
```

- [ ] **Estimate required depth:**
  ```
  d_g ≈ L/25 to L/30 (initial estimate)
  ```

- [ ] **Back-calculate parent beam depth:**
  ```
  d ≈ d_g/1.5 (castellated)
  d ≈ d_g/1.43 (cellular, typical)
  ```

- [ ] **Select parent beam from AISC Manual Table 1-1**
  - Choose depth series (W8, W10, W12, W14, W16, W18, W21, W24)
  - Start with lighter weight in series
  - Record: d, b_f, t_f, t_w, I_x, S_x, Z_x

- [ ] **For composite beams, consider asymmetric section:**
  - Top tee: Select lighter parent beam
  - Bottom tee: Select heavier parent beam
  - Must be same depth series (both W21, etc.)
  - Check web thickness compatibility

**Reference:** Section 1.3, Section 2.2.6

---

### Step 4: Determine Opening Size and Spacing

#### Castellated Beams

- [ ] **Select cutting angle θ**
  - θ = 60° (most common)
  - θ = 45° (alternative)
  - θ = 52.5° (avoid - lowest φ_b)

- [ ] **Determine opening dimensions:**
  ```
  h_o ≈ d (opening height ≈ parent depth)
  h = h_o/2 (half-height)
  b = h/tan(θ) (horizontal length)
  ```

- [ ] **Select tee length e:**
  ```
  Typical: e ≈ 0.25d to 0.40d
  Trial: e = d/3
  ```

- [ ] **Calculate spacing:**
  ```
  S = 2e + 2b
  ```

- [ ] **Calculate expanded depth:**
  ```
  d_g = d + h_o
  d_t = (d - h_o)/2 (tee depth)
  ```

- [ ] **Check web post aspect ratio:**
  ```
  s = 2e (web post length)
  d_p ≈ d_t (web post depth)
  s/d_p > 1.5 (recommended minimum)
  If not satisfied: Increase e
  ```

#### Cellular Beams

- [ ] **Select opening diameter:**
  ```
  D_o ≈ 1.0d to 1.1d (typical)
  Trial: D_o = d
  ```

- [ ] **Select opening spacing:**
  ```
  Trial: S = 1.35D_o (typical)
  Must satisfy: 1.08 < S/D_o < 1.5
  ```

- [ ] **Calculate expanded depth:**
  ```
  loss = D_o/2 - √[(D_o/2)² - ((S-D_o)/2)²]
  d_g = d + D_o/2 - loss
  ```

- [ ] **Calculate tee dimensions:**
  ```
  d_t-net = (d_g - D_o)/2
  y = √[(0.5D_o)² - (0.225D_o)²]
  d_t-crit = D_o/2 - y + d_t-net
  ```

- [ ] **Verify geometric limits (REQUIRED):**
  ```
  1.08 < S/D_o < 1.5  ✓
  1.25 < d_g/D_o < 1.75  ✓
  If not satisfied: Adjust D_o or S
  ```

- [ ] **Check web post aspect ratio:**
  ```
  s = S - D_o (web post length)
  d_p ≈ d_t-net
  s/d_p > 1.5 (recommended)
  If not satisfied: Increase S
  ```

**Reference:** Section 2.3, Section 3.4

---

### Step 5: Calculate Section Properties

#### Tee Section Properties

- [ ] **Calculate tee properties using Parallel Axis Theorem**
  - For symmetric sections: Same tee top and bottom
  - For asymmetric sections: Calculate separately for each tee

- [ ] **Required properties for each tee:**
  - A_tee (area)
  - ȳ_tee (centroid location from base)
  - I_x-tee (moment of inertia about own centroid)
  - I_y-tee
  - S_x-tee (section modulus)
  - Z_x-tee (plastic section modulus)
  - r_x, r_y (radii of gyration)
  - J (torsional constant)
  - y_o (shear center location)

- [ ] **For cellular beams, also calculate critical section properties**
  - A_tee-crit
  - All properties at section 0.225D_o from center

**Tip:** Use spreadsheet or structural software for tee calculations

#### Net Section Properties

- [ ] **Calculate net section properties:**
  ```
  A_net = A_tee-top + A_tee-bot
  d_effec = d_g - (ȳ_tee-top + ȳ_tee-bot)
  I_x-net = I_x-tee-top + I_x-tee-bot +
            A_tee-top(d_effec/2)² + A_tee-bot(d_effec/2)²
  S_x-net = I_x-net / (d_g/2)
  Z_x-net = A_tee-top(d_effec/2) + A_tee-bot(d_effec/2)
  ```

#### Gross Section Properties

- [ ] **Calculate gross section properties:**
  ```
  Castellated:
    A_gross = A_net + h_o × t_w
    I_x-gross = I_x-net + (t_w × h_o³)/12

  Cellular:
    A_gross = A_net + D_o × t_w
    I_x-gross = I_x-net + (t_w × D_o³)/12
  ```

#### Composite Section Properties (if applicable)

- [ ] **Calculate transformed composite section:**
  - Effective width b_eff (per AISC Spec. Section I3.1)
  - Modular ratio n = E_s/E_c
  - Transformed concrete area
  - Composite section I_x and S_x

**Reference:** Examples 4.1-4.4 for detailed calculations

---

## Phase 2: Strength Checks

### Step 6: Check Vierendeel Bending at Each Opening

This is typically the governing failure mode.

#### Calculate Global Forces

- [ ] **Determine load combinations (LRFD or ASD)**
  - LRFD: 1.2D + 1.6L (typical)
  - ASD: D + L

- [ ] **Calculate global moment M_r and shear V_r at each opening location**
  - Use standard beam analysis
  - Create table with opening number, distance x, M_r, V_r

#### Calculate Local Forces

**For Noncomposite Beams:**

- [ ] **Calculate axial force in tees:**
  ```
  P_r = M_r / d_effec
  ```
  Both tees carry same axial force (opposite sign)

- [ ] **Calculate Vierendeel moment:**

  **Castellated:**
  ```
  M_Vr = V_r × (e/2)
  ```

  **Cellular:**
  ```
  M_Vr = V_r × (A_tee-crit/A_crit) × (D_o/4)
  ```

**For Composite Beams:**

- [ ] **Determine if fully or partially composite**
  - Calculate required shear stud strength
  - Compare to provided studs
  - If sufficient: Fully composite
  - If not: Calculate partial composite forces

- [ ] **For fully composite sections:**
  - Concrete takes all compression: T_o = 0
  - Bottom tee takes all tension: T_1 = M_r/d_effec-comp

- [ ] **For partially composite sections:**
  ```
  q = 2V_provided / Beam_span (stud density)
  T_o = M_r[1 - q(X_i)/T_1] / d_effec
  T_1-new = q(X_i) + T_o
  ```

- [ ] **Calculate concrete shear contribution:**
  ```
  V_nc = 3(h_r + t_c)t_c√(4√f'_c)
  V_c = φ_v V_nc (LRFD)  or  V_nc/Ω_v (ASD)
  V_net = V_r - V_c
  ```

- [ ] **Calculate Vierendeel moment with net shear:**
  ```
  M_Vr = V_net × (A_tee/A_net) × (lever arm)
  ```
  Distribute between top and bottom based on relative areas

#### Calculate Available Strengths

**Axial Strength - Compression:**

- [ ] **Check flange compactness:**
  ```
  λ = b_f/(2t_f)
  λ_p = 0.38√(E/F_y)
  If λ < λ_p: Compact (no FLB check needed)
  ```

- [ ] **Check stem slenderness:**
  ```
  λ = d_t/t_w
  λ_s = 0.75√(E/F_y)
  If λ < λ_s: Nonslender (no E7 needed)
  ```

- [ ] **Calculate flexural buckling strength (AISC Spec. E3):**
  ```
  L_c = e (castellated) or D_o/2 (cellular)
  K_x = 0.65, K_y = 1.0
  r = min(r_x, r_y)
  Calculate F_e, then F_cr, then P_n
  ```

- [ ] **Calculate flexural-torsional buckling strength (AISC Spec. E4):**
  ```
  Calculate F_ey, F_ez, H
  Calculate F_e per Eq. E4-3
  Calculate F_cr, then P_n
  ```

- [ ] **Available axial strength:**
  ```
  φ_c P_n = 0.90 × min(P_n from E3, P_n from E4)  (LRFD)
  P_n/Ω_c = min(...) / 1.67  (ASD)
  ```

**Axial Strength - Tension (for bottom tee in composite):**

- [ ] **Tensile yielding (AISC Spec. D2):**
  ```
  P_n = F_y × A_tee
  φ_t = 0.90 (LRFD), Ω_t = 1.67 (ASD)
  ```

**Flexural Strength:**

- [ ] **Yielding (AISC Spec. F9.1):**
  ```
  M_n = M_p = F_y × S_x-bot (stem in compression)
  Limited to yield moment M_y
  ```

- [ ] **Lateral-torsional buckling (AISC Spec. F9.2):**
  ```
  L_b = e (castellated) or D_o/2 (cellular)
  If L_b = 0 (braced): LTB does not apply
  If L_b > 0: Calculate L_p, L_r, M_cr per Spec.
  ```

- [ ] **Flange local buckling (AISC Spec. F9.3):**
  ```
  If compact: Does not apply
  If noncompact or slender: Calculate per Spec.
  ```

- [ ] **Stem local buckling (AISC Spec. F9.4):**
  ```
  Calculate F_cr based on d_t/t_w ratio
  M_n = F_cr × S_x
  ```

- [ ] **Available flexural strength:**
  ```
  φ_b M_n = 0.90 × min(all M_n values)  (LRFD)
  M_n/Ω_b = min(...) / 1.67  (ASD)
  ```

#### Check Interaction

- [ ] **For each opening, check interaction (AISC Spec. H1.1):**

  **If P_r/(φ_c P_n) ≥ 0.2:**
  ```
  P_r/(φ_c P_n) + (8/9)[M_Vr/(φ_b M_n)] ≤ 1.0
  ```

  **If P_r/(φ_c P_n) < 0.2:**
  ```
  P_r/(2φ_c P_n) + M_Vr/(φ_b M_n) ≤ 1.0
  ```

- [ ] **Create interaction table for all openings**
  - Typically worst at openings 1-2 (high shear)
  - Or at midspan if partial composite

- [ ] **If any interaction > 1.0:**
  - Option 1: Increase parent beam size
  - Option 2: Decrease opening size
  - Option 3: Increase opening spacing
  - Option 4: For composite: Add more shear studs

**Reference:** Section 3.2 (noncomposite), Section 3.3 (composite)

---

### Step 7: Check Web Post Buckling

Critical at first few openings where horizontal shear is highest.

#### Calculate Horizontal Shear

- [ ] **For each web post, calculate horizontal shear:**
  ```
  V_rh = |T_r(i) - T_r(i+1)|
  ```
  Where T_r values are axial forces from Step 6

- [ ] **Create table with web post number and V_rh values**
  - Maximum typically at first web post

#### Calculate Required Strength

**Castellated Beams:**

- [ ] **Required moment:**
  ```
  M_rh = V_rh × h
  ```

**Cellular Beams:**

- [ ] **Required moment:**
  ```
  M_rh = 0.90 × (D_o/2) × V_rh
  ```

#### Calculate Available Strength

**Castellated Beams:**

- [ ] **Plastic moment:**
  ```
  M_p = 0.25 × t_w × (e + 2b)² × F_y
  ```

- [ ] **Calculate 2h/e ratio and e/t_w ratio**

- [ ] **Determine M_ocr/M_p based on angle θ:**

  **For θ = 45°:**
  - Use Equations 3-23 to 3-25 based on e/t_w
  - Interpolate if needed
  - Limited to 0.26 maximum

  **For θ = 60°:**
  - Use Equations 3-26 to 3-28 based on e/t_w
  - Interpolate if needed
  - Limited to 0.493 maximum

  **For other θ:**
  - Interpolate between 45° and 60° equations

- [ ] **Determine resistance factor φ_b:**
  ```
  θ = 43-47°: φ_b = 0.90
  θ = 52.5°: φ_b = 0.60
  θ = 58-62°: φ_b = 0.90
  Linear interpolation for intermediate angles
  ```

- [ ] **Available strength:**
  ```
  φ_b M_n = φ_b × (M_ocr/M_p) × M_p  (LRFD)
  M_n/Ω_b = (M_ocr/M_p) × M_p / 1.67  (ASD with Ω_b per θ)
  ```

**Cellular Beams:**

- [ ] **Elastic moment:**
  ```
  M_e = [t_w(S - D_o + 0.564D_o)²/6] × F_y
  ```

- [ ] **Calculate coefficients:**
  ```
  C1 = 5.097 + 0.1464(D_o/t_w) - 0.00174(D_o/t_w)²
  C2 = 1.441 + 0.0625(D_o/t_w) - 0.000683(D_o/t_w)²
  C3 = 3.645 + 0.0853(D_o/t_w) - 0.00108(D_o/t_w)²
  ```

- [ ] **Calculate M_allow/M_e:**
  ```
  M_allow/M_e = C1(S/D_o) - C2(S/D_o)² - C3
  ```

- [ ] **Available strength:**
  ```
  φ_b M_n = 0.90 × (M_allow/M_e) × M_e  (LRFD)
  M_n/Ω_b = (M_allow/M_e) × M_e / 1.67  (ASD)
  ```

#### Verify Adequacy

- [ ] **Check each web post:**
  ```
  M_rh ≤ φ_b M_n  (LRFD)
  M_rh ≤ M_n/Ω_b   (ASD)
  ```

- [ ] **If any web post fails:**
  - Option 1: Increase spacing S (reduces V_rh)
  - Option 2: Increase web thickness (larger parent beam)
  - Option 3: Change cutting angle θ (castellated only)

**Reference:** Section 3.4

---

### Step 8: Check Horizontal Shear

Usually not critical if web post buckling is satisfied.

- [ ] **Calculate nominal horizontal shear strength:**
  ```
  V_n = 0.6 × F_y × (e × t_w)
  φ_v = 1.00 (LRFD), Ω_v = 1.50 (ASD)
  ```

- [ ] **Check adequacy:**
  ```
  V_rh ≤ φ_v V_n  (LRFD)
  V_rh ≤ V_n/Ω_v   (ASD)
  ```

- [ ] **If fails (rare):**
  - Increase web thickness
  - Increase spacing

**Reference:** Section 3.5.1

---

### Step 9: Check Vertical Shear

Must check both net section (through opening) and gross section (at web post).

#### Vertical Shear at Net Section

**For Symmetric Sections:**

- [ ] **Check tee stem:**
  ```
  h/t_w = d_t/t_w
  k_v = 1.2 (for tee stems)

  If h/t_w ≤ 1.10√(k_v E/F_y):
    C_v2 = 1.0
  Else:
    C_v2 = 1.10√(k_v E/F_y) / (h/t_w)

  V_n = 0.6 × F_y × (2d_t × t_w) × C_v2
  ```

**For Asymmetric Sections:**

- [ ] **Distribute shear between tees:**
  ```
  V_r-top = V_r × (A_tee-top / A_net)
  V_r-bot = V_r × (A_tee-bot / A_net)
  ```

- [ ] **Check each tee separately:**
  ```
  Top tee: V_n-top = 0.6 × F_y × (d_t-top × t_w-top) × C_v2-top
  Bot tee: V_n-bot = 0.6 × F_y × (d_t-bot × t_w-bot) × C_v2-bot
  ```

**For Composite Beams:**

- [ ] **Add concrete contribution:**
  ```
  V_nc = 3(h_r + t_c)t_c√(4√f'_c)
  V_c = φ_v V_nc (LRFD) or V_nc/Ω_v (ASD)
  V_r-net = V_r - V_c (net shear in steel)
  ```

- [ ] **Determine resistance factors:**
  ```
  If h/t_w ≤ 2.24√(E/F_y):
    φ_v = 1.00, Ω_v = 1.50
  Else:
    φ_v = 0.90, Ω_v = 1.67
  ```

- [ ] **Check adequacy:**
  ```
  V_r-tee ≤ φ_v V_n-tee  (LRFD)
  ```

#### Vertical Shear at Gross Section

- [ ] **Calculate h/t_w for gross section:**
  ```
  h/t_w = (d_g - k_top - k_bot) / t_w
  k_v = 5.34 (for webs with flanges)
  ```

- [ ] **Calculate C_v1:**
  ```
  If h/t_w ≤ 1.10√(k_v E/F_y):
    C_v1 = 1.0
  Else:
    C_v1 = 1.10√(k_v E/F_y) / (h/t_w)
  ```

- [ ] **Calculate nominal strength:**
  ```
  V_n = 0.6 × F_y × (d_g × t_w) × C_v1
  ```

- [ ] **Determine φ_v or Ω_v based on h/t_w**

- [ ] **Check adequacy:**
  ```
  V_r ≤ φ_v V_n  (LRFD)
  ```

- [ ] **If any shear check fails:**
  - Increase parent beam size
  - Reduce opening size
  - Add stiffeners (non-standard)

**Reference:** Section 3.5.2

---

### Step 10: Check Lateral-Torsional Buckling

For unbraced beams only.

- [ ] **If fully braced (L_b = 0):**
  - LTB does not apply
  - Skip to Step 11

- [ ] **If unbraced:**
  - Use gross section properties (I_x-gross, S_x-gross)
  - Check per AISC Specification Chapter F, Sections F2-F5
  - Use standard procedures for W-shapes
  - No special modifications for openings

- [ ] **For composite beams:**
  - Deck usually provides lateral bracing to top flange
  - Check bottom flange for tension flange yielding

- [ ] **If LTB governs:**
  - Add lateral bracing
  - Increase beam size
  - Change bracing configuration

**Reference:** Section 3.6

---

## Phase 3: Serviceability Checks

### Step 11: Check Deflection

Use 90% of net section moment of inertia.

#### Calculate Service Load Deflections

**For Noncomposite Beams:**

- [ ] **Effective moment of inertia:**
  ```
  I_eff = 0.90 × I_x-net
  ```

- [ ] **Live load deflection:**
  ```
  Δ_LL = (5w_LL L⁴) / (384 E I_eff)
  ```

- [ ] **Dead load deflection:**
  ```
  Δ_DL = (5w_DL L⁴) / (384 E I_eff)
  ```

- [ ] **Total load deflection:**
  ```
  Δ_TL = Δ_LL + Δ_DL
  ```

**For Composite Beams (Staged Analysis):**

- [ ] **Pre-composite deflection (steel beam only):**
  ```
  I_eff-steel = 0.90 × I_x-net-steel
  w_pre = slab weight + deck + construction loads
  Δ_pre = (5w_pre L⁴) / (384 E I_eff-steel)
  ```

- [ ] **Post-composite deflection (composite section):**
  ```
  I_eff-comp = 0.90 × I_x-composite
  w_post = superimposed DL + LL
  Δ_post = (5w_post L⁴) / (384 E I_eff-comp)
  ```

- [ ] **Total deflection:**
  ```
  Δ_total-DL = Δ_pre + Δ_post-DL
  Δ_total-LL = Δ_post-LL
  Δ_total = Δ_total-DL + Δ_total-LL
  ```

#### Check Against Limits

- [ ] **Live load deflection:**
  ```
  Δ_LL ≤ L/240 (typical floors)
  or Δ_LL ≤ L/360 (sensitive equipment)
  ```

- [ ] **Total load deflection:**
  ```
  Δ_TL ≤ L/180 (typical)
  or Δ_TL ≤ L/240 (sensitive applications)
  ```

#### Specify Camber if Needed

- [ ] **Calculate recommended camber:**
  ```
  Camber ≈ Δ_DL (or Δ_pre for composite)
  Round to nearest 1/4 inch
  ```

- [ ] **Note on drawings:**
  "Beam to be cambered [X] inches"

- [ ] **If deflection excessive:**
  - Increase parent beam size
  - Reduce span
  - Add intermediate supports
  - For composite: Add more shear studs

**Reference:** Section 3.7

---

### Step 12: Check Concentrated Loads (if applicable)

If concentrated loads are present:

- [ ] **Check at each concentrated load location:**
  - Flange local bending (AISC Spec. J10.1)
  - Web local yielding (AISC Spec. J10.2)
  - Web local crippling (AISC Spec. J10.3)
  - Sidesway web buckling (AISC Spec. J10.4)

- [ ] **If any check fails:**
  - Add bearing stiffeners
  - Add web doubler plates
  - Increase beam size

- [ ] **Special consideration for loads near openings:**
  - Avoid placing concentrated loads directly at openings
  - Minimum distance: 0.5D_o from opening edge

**Reference:** Section 3.8

---

## Phase 4: Detailing and Documentation

### Step 13: End Connection Design

- [ ] **Determine end pattern:**
  - "1" pattern (full opening at end)
  - "O" pattern (half opening - recommended)
  - Custom pattern

- [ ] **Calculate end spacing "a":**
  ```
  Recommended: a ≥ 0.5D_o to 0.8D_o
  Verify against shear demand
  ```

- [ ] **For coped ends:**
  ```
  Verify: e' ≥ s (diagonal distance)
  ```

- [ ] **Design end connection:**
  - Simple shear connection typical
  - Check bearing, bolt shear, tearout
  - Verify weld strength if welded

**Reference:** Section 2.3.1

---

### Step 14: Shear Stud Layout (Composite Beams Only)

- [ ] **Determine total studs required:**
  ```
  N = V' / Q_n (per half-span)
  V' = total horizontal shear
  Q_n = nominal stud strength
  ```

- [ ] **Layout studs:**
  - Uniform spacing typical
  - Avoid placing directly over openings
  - Maximum spacing per AISC Spec.

- [ ] **Detail on drawings:**
  - Stud size and height
  - Number and spacing
  - Welding requirements

**Reference:** Section 3.3 and Examples 4.3, 4.4

---

### Step 15: Fabrication Notes

- [ ] **Specify on drawings:**
  - Parent beam size(s)
  - Beam designation (CB or LB with dimensions)
  - Opening type and size
  - Opening spacing
  - End pattern
  - Cutting angle (castellated)
  - Material specification
  - Camber (if required)
  - Lateral bracing requirements
  - Fire protection (if required)
  - Coating system (if required)

- [ ] **For asymmetric sections:**
  - Clearly identify which parent beam for top
  - Clearly identify which parent beam for bottom
  - Show orientation

- [ ] **Include details for:**
  - Erection bracing requirements
  - Temporary shoring (if needed during construction)
  - Welding requirements (AWS standards)
  - Inspection requirements

**Reference:** Chapter 2 (Applications), Section 2.4 (Special Considerations)

---

## Summary Checklist

### Critical Checks (Must Pass)

- [ ] **Vierendeel bending** - All openings
- [ ] **Web post buckling** - All web posts
- [ ] **Deflection** - Live load and total load
- [ ] **Geometric limits** - For cellular beams

### Important Checks

- [ ] **Vertical shear** - Net and gross sections
- [ ] **Horizontal shear** - All web posts
- [ ] **Lateral-torsional buckling** - If unbraced
- [ ] **Concentrated loads** - If present

### Detailing Requirements

- [ ] **End spacing adequate**
- [ ] **Connection design complete**
- [ ] **Shear studs detailed** (if composite)
- [ ] **Camber specified** (if needed)
- [ ] **Fabrication notes complete**

---

## Common Iteration Scenarios

If design doesn't work:

**Vierendeel bending fails:**
1. Increase parent beam size (stronger tees)
2. Reduce opening size (less moment arm)
3. Increase spacing (less shear transfer)
4. For composite: Add more shear studs

**Web post buckling fails:**
1. Increase spacing S (longer web posts)
2. Increase parent beam size (thicker web)
3. Change cutting angle θ (castellated)

**Deflection excessive:**
1. Increase parent beam size (higher I_x)
2. Specify camber
3. For composite: Increase composite action

**Multiple failures:**
- Consider significantly larger parent beam
- Re-evaluate beam type (castellated vs. cellular)
- Consider reducing span or adding intermediate support

---

## Design Tools and Resources

### AISC Resources
- **Specification:** AISC 360-16
- **Manual:** Steel Construction Manual, 15th Ed.
- **Design Guide 31:** This guide

### Software
- Spreadsheet templates (develop from examples)
- Structural analysis software (SAP2000, RISA, etc.)
- Section property calculators

### Hand Calculations
- Examples 4.1-4.4 provide complete workflows
- Use as templates for similar designs

---

## Final Verification

Before finalizing design:

- [ ] **All strength checks satisfied**
- [ ] **All serviceability limits met**
- [ ] **Geometric constraints verified**
- [ ] **Detailing complete and constructible**
- [ ] **Fabricator can produce (consult if unusual)**
- [ ] **Economical (compare to alternatives)**
- [ ] **Calculations documented**
- [ ] **Drawings clear and complete**

---

## References

Complete reference to applicable sections:

- **Chapter 1:** Introduction, nomenclature
- **Chapter 2:** Applications, use cases, special considerations
- **Chapter 3:** Complete design procedures
  - Section 3.1: Introduction
  - Section 3.2: Vierendeel bending (noncomposite)
  - Section 3.3: Vierendeel bending (composite)
  - Section 3.4: Web post buckling
  - Section 3.5: Horizontal and vertical shear
  - Section 3.6: Lateral-torsional buckling
  - Section 3.7: Deflection
  - Section 3.8: Concentrated loading
- **Chapter 4:** Design examples (follow these workflows)
- **AISC Specification:** Chapters D, E, F, G, H, I, J

---

## Notes

1. This workflow follows AISC Design Guide 31 procedures exactly
2. Both LRFD and ASD methods are applicable (choose one)
3. Always verify geometric limits before proceeding with design
4. Check each opening individually - don't assume uniformity
5. Document all calculations for review and future reference
6. Consult fabricator early for unusual configurations
7. Consider constructibility and economy throughout process
