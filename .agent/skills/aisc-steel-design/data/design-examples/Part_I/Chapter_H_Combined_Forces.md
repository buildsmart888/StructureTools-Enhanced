# Chapter H: Combined Forces

**AISC Specification v16.0 - Design Examples**
**Original PDF Pages**: 263-296 (34 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Design of Members for Combined Forces and Torsion

**Examples Included**: ['H.1A~H.6B: Combined loading examples']

---

## Table of Contents

- [EXAMPLE H.1A W-SHAPE SUBJECT TO COMBINED COMPRESSION AND BENDING ABOUT BOTH AXES (BRACED FRAME)](#example-h1a-w-shape-subject-to-combined-compression-and-bending-about-both-axes-(braced-frame))
- [EXAMPLE H.1B W-SHAPE SUBJECT TO COMBINED COMPRESSION AND BENDING MOMENT ABOUT BOTH AXES (BRACED FRAME)](#example-h1b-w-shape-subject-to-combined-compression-and-bending-moment-about-both-axes-(braced-frame))
- [EXAMPLE H.2 W-SHAPE SUBJECT TO COMBINED COMPRESSION AND BENDING MOMENT ABOUT BOTH AXES (BY AISC *SPECIFICATION* SECTION H2)](#example-h2-w-shape-subject-to-combined-compression-and-bending-moment-about-both-axes-(by-aisc-*specification*-section-h2))
- [EXAMPLE H.3 W-SHAPE SUBJECT TO COMBINED AXIAL TENSION AND FLEXURE](#example-h3-w-shape-subject-to-combined-axial-tension-and-flexure)
- [EXAMPLE H.4 W-SHAPE SUBJECT TO COMBINED AXIAL COMPRESSION AND FLEXURE](#example-h4-w-shape-subject-to-combined-axial-compression-and-flexure)
- [EXAMPLE H.5A RECTANGULAR HSS TORSIONAL STRENGTH](#example-h5a-rectangular-hss-torsional-strength)
- [EXAMPLE H.5B ROUND HSS TORSIONAL STRENGTH](#example-h5b-round-hss-torsional-strength)
- [EXAMPLE H.5C RECTANGULAR HSS COMBINED TORSIONAL AND FLEXURAL STRENGTH](#example-h5c-rectangular-hss-combined-torsional-and-flexural-strength)
- [EXAMPLE H.6 W-SHAPE TORSIONAL STRENGTH](#example-h6-w-shape-torsional-strength)

---

# H-1

# Chapter H
# Design of Members for Combined Forces and Torsion

For all interaction equations in AISC *Specification* Chapter H, the required forces and moments must include second-order effects, as required by Chapter C of the AISC *Specification*. ASD users of the 1989 AISC *Specification* are accustomed to using an interaction equation that includes a partial second-order amplification. Second-order effects are now addressed in the analysis and are not included in these interaction equations.

---

# H-2

## EXAMPLE H.1A W-SHAPE SUBJECT TO COMBINED COMPRESSION AND BENDING ABOUT BOTH AXES (BRACED FRAME)

### Given:

Using Table 6-J (located in Volume 2 of this document), determine if an ASTM A992/A992M W14×99 has sufficient available strength to support the axial forces and moments listed as follows, obtained from a second-order analysis that includes *P*-δ effects. The unbraced length is 14 ft and the member has pinned ends.

| LRFD | ASD |
|------|-----|
| $P_u = 400 \text{ kips}$ | $P_a = 267 \text{ kips}$ |
| $M_{ux} = 250 \text{ kip-ft}$ | $M_{ax} = 167 \text{ kip-ft}$ |
| $M_{uy} = 80.0 \text{ kip-ft}$ | $M_{ay} = 53.3 \text{ kip-ft}$ |

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

The effective length of the member is:

$$L_{cx} = L_{cy}$$

$$= KL$$

$$= 1.0(14 \text{ ft})$$

$$= 14.0 \text{ ft}$$

For $L_c = 14 \text{ ft}$, the combined strength parameters from Table 6-J are:

| LRFD | ASD |
|------|-----|
| $p = \dfrac{0.887}{10^3 \text{ kips}}$ | $p = \dfrac{1.33}{10^3 \text{ kips}}$ |
| $b_x = \dfrac{1.38}{10^3 \text{ kip-ft}}$ | $b_x = \dfrac{2.08}{10^3 \text{ kip-ft}}$ |
| $b_y = \dfrac{2.85}{10^3 \text{ kip-ft}}$ | $b_y = \dfrac{4.29}{10^3 \text{ kip-ft}}$ |
| Check $P_r/P_c$ limit for AISC *Specification* Equation H1-1a. | Check $P_r/P_c$ limit for AISC *Specification* Equation H1-1a. |
| $\dfrac{P_u}{\phi_c P_n} = pP_u$ | $\dfrac{P_a}{P_n/\Omega_c} = pP_a$ |
| $= \left(\dfrac{0.887}{10^3 \text{ kips}}\right)(400 \text{ kips})$ | $= \left(\dfrac{1.33}{10^3 \text{ kips}}\right)(267 \text{ kips})$ |
| $= 0.355$ | $= 0.355$ |

---

# H-3

| LRFD | ASD |
|------|-----|
| Because $pP_u \geq 0.2$, | Because $pP_a \geq 0.2$, |
| $pP_u + b_x M_{ux} + b_y M_{uy} \leq 1.0$ (from Vol. 2, Eq. 9) | $pP_a + b_x M_{ax} + b_y M_{ay} \leq 1.0$ (from Vol. 2, Eq. 9) |
| $= 0.355 + \left(\dfrac{1.38}{10^3 \text{ kip-ft}}\right)(250 \text{ kip-ft})$ | $= 0.355 + \left(\dfrac{2.08}{10^3 \text{ kip-ft}}\right)(167 \text{ kip-ft})$ |
| $+ \left(\dfrac{2.85}{10^3 \text{ kip-ft}}\right)(80.0 \text{ kip-ft}) \leq 1.0$ | $+ \left(\dfrac{4.29}{10^3 \text{ kip-ft}}\right)(53.3 \text{ kip-ft}) \leq 1.0$ |
| $= 0.928 < 1.0$ **o.k.** | $= 0.931 < 1.0$ **o.k.** |

Table 6-J simplifies the calculation of AISC *Specification* Equations H1-1a and H1-1b. A direct application of these equations is shown in Example H.1B.

---

# H-4

## EXAMPLE H.1B W-SHAPE SUBJECT TO COMBINED COMPRESSION AND BENDING MOMENT ABOUT BOTH AXES (BRACED FRAME)

### Given:

Using AISC *Manual* tables to determine the available compressive and flexural strengths, determine if an ASTM A992/A992M W14×99 has sufficient available strength to support the axial forces and moments listed as follows, obtained from a second-order analysis that includes *P*-δ effects. The unbraced length is 14 ft and the member has pinned ends.

| LRFD | ASD |
|------|-----|
| $P_u = 400 \text{ kips}$ | $P_a = 267 \text{ kips}$ |
| $M_{ux} = 250 \text{ kip-ft}$ | $M_{ax} = 167 \text{ kip-ft}$ |
| $M_{uy} = 80.0 \text{ kip-ft}$ | $M_{ay} = 53.3 \text{ kip-ft}$ |

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

The effective length of the member is:

$$L_{cx} = L_{cy}$$

$$= KL$$

$$= 1.0(14 \text{ ft})$$

$$= 14.0 \text{ ft}$$

For $L_c = 14.0 \text{ ft}$, the available axial and flexural strengths from AISC *Manual* Table 6-1 are:

| LRFD | ASD |
|------|-----|
| $P_c = \phi_c P_n$ | $P_c = \dfrac{P_n}{\Omega_c}$ |
| $= 1{,}130 \text{ kips}$ | $= 750 \text{ kips}$ |
| $M_{cx} = \phi_b M_{nx}$ | $M_{cx} = \dfrac{M_{nx}}{\Omega_b}$ |
| $= 642 \text{ kip-ft}$ | $= 427 \text{ kip-ft}$ |
| $M_{cy} = \phi_b M_{ny}$ | $M_{cy} = \dfrac{M_{ny}}{\Omega_b}$ |
| $= 311 \text{ kip-ft}$ | $= 207 \text{ kip-ft}$ |
| $\dfrac{P_u}{\phi_c P_n} = \dfrac{400 \text{ kips}}{1{,}130 \text{ kips}}$ | $\dfrac{P_a}{P_n/\Omega_c} = \dfrac{267 \text{ kips}}{750 \text{ kips}}$ |
| $= 0.354$ | $= 0.356$ |

---

# H-5

| LRFD | ASD |
|------|-----|
| Because $\dfrac{P_u}{\phi_c P_n} \geq 0.2$, | Because $\dfrac{P_a}{P_n/\Omega_c} \geq 0.2$, |
| $\dfrac{P_r}{P_c} + \dfrac{8}{9}\left(\dfrac{M_{rx}}{M_{cx}} + \dfrac{M_{ry}}{M_{cy}}\right) \leq 1.0$ (*Spec.* Eq. H1-1a) | $\dfrac{P_r}{P_c} + \dfrac{8}{9}\left(\dfrac{M_{rx}}{M_{cx}} + \dfrac{M_{ry}}{M_{cy}}\right) \leq 1.0$ (*Spec.* Eq. H1-1a) |
| $= \dfrac{400 \text{ kips}}{1{,}130 \text{ kips}} + \dfrac{8}{9}\left(\dfrac{250 \text{ kip-ft}}{642 \text{ kip-ft}} + \dfrac{80.0 \text{ kip-ft}}{311 \text{ kip-ft}}\right) \leq 1.0$ | $= \dfrac{267 \text{ kips}}{750 \text{ kips}} + \dfrac{8}{9}\left(\dfrac{167 \text{ kip-ft}}{427 \text{ kip-ft}} + \dfrac{53.3 \text{ kip-ft}}{207 \text{ kip-ft}}\right)$ |
| $= 0.929 < 1.0$ **o.k.** | $= 0.933 < 1.0$ **o.k.** |

---

# H-6

## EXAMPLE H.2 W-SHAPE SUBJECT TO COMBINED COMPRESSION AND BENDING MOMENT ABOUT BOTH AXES (BY AISC *SPECIFICATION* SECTION H2)

### Given:

Using AISC *Specification* Section H2, determine if an ASTM A992/A992M W14×99 has sufficient available strength to support the axial forces and moments listed as follows, obtained from a second-order analysis that includes *P*-δ effects. The unbraced length is 14 ft and the member has pinned ends. This example is included primarily to illustrate the use of AISC *Specification* Section H2.

| LRFD | ASD |
|------|-----|
| $P_u = 360 \text{ kips}$ | $P_a = 240 \text{ kips}$ |
| $M_{ux} = 250 \text{ kip-ft}$ | $M_{ax} = 167 \text{ kip-ft}$ |
| $M_{uy} = 80.0 \text{ kip-ft}$ | $M_{ay} = 53.3 \text{ kip-ft}$ |

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-1, the geometric properties are as follows:

W14×99
$A = 29.1 \text{ in.}^2$
$S_x = 157 \text{ in.}^3$
$S_y = 55.2 \text{ in.}^3$

The required flexural and axial stresses are:

| LRFD | ASD |
|------|-----|
| $f_{ra} = \dfrac{P_u}{A}$ | $f_{ra} = \dfrac{P_a}{A}$ |
| $= \dfrac{360 \text{ kips}}{29.1 \text{ in.}^2}$ | $= \dfrac{240 \text{ kips}}{29.1 \text{ in.}^2}$ |
| $= 12.4 \text{ ksi}$ | $= 8.25 \text{ ksi}$ |
| $f_{rbx} = \dfrac{M_{ux}}{S_x}$ | $f_{rbx} = \dfrac{M_{ax}}{S_x}$ |
| $= \dfrac{(250 \text{ kip-ft})(12 \text{ in./ft})}{157 \text{ in.}^3}$ | $= \dfrac{(167 \text{ kip-ft})(12 \text{ in./ft})}{157 \text{ in.}^3}$ |
| $= 19.1 \text{ ksi}$ | $= 12.8 \text{ ksi}$ |
| $f_{rby} = \dfrac{M_{uy}}{S_y}$ | $f_{rby} = \dfrac{M_{ay}}{S_y}$ |
| $= \dfrac{(80.0 \text{ kip-ft})(12 \text{ in./ft})}{55.2 \text{ in.}^3}$ | $= \dfrac{(53.3 \text{ kip-ft})(12 \text{ in./ft})}{55.2 \text{ in.}^3}$ |
| $= 17.4 \text{ ksi}$ | $= 11.6 \text{ ksi}$ |

---

# H-7

The effective length of the member is:

$$L_{cx} = L_{cy}$$

$$= KL$$

$$= 1.0(14 \text{ ft})$$

$$= 14.0 \text{ ft}$$

For $L_c = 14.0 \text{ ft}$, calculate the available axial and flexural stresses using the available strengths from AISC *Manual* Table 6-1.

| LRFD | ASD |
|------|-----|
| $F_{ca} = \dfrac{\phi_c P_n}{A}$ | $F_{ca} = \dfrac{P_n}{\Omega_c A}$ |
| $= \dfrac{1{,}130 \text{ kips}}{29.1 \text{ in.}^2}$ | $= \dfrac{750 \text{ kips}}{29.1 \text{ in.}^2}$ |
| $= 38.8 \text{ ksi}$ | $= 25.8 \text{ ksi}$ |
| $F_{cbx} = \dfrac{\phi_b M_{nx}}{S_x}$ | $F_{cbx} = \dfrac{M_{nx}}{\Omega_b S_x}$ |
| $= \dfrac{(642 \text{ kip-ft})(12 \text{ in./ft})}{157 \text{ in.}^3}$ | $= \dfrac{(427 \text{ kip-ft})(12 \text{ in./ft})}{157 \text{ in.}^3}$ |
| $= 49.1 \text{ ksi}$ | $= 32.6 \text{ ksi}$ |
| $F_{cby} = \dfrac{\phi_b M_{ny}}{S_y}$ | $F_{cby} = \dfrac{M_{ny}}{\Omega_b S_y}$ |
| $= \dfrac{(311 \text{ kip-ft})(12 \text{ in./ft})}{55.2 \text{ in.}^3}$ | $= \dfrac{(207 \text{ kip-ft})(12 \text{ in./ft})}{55.2 \text{ in.}^3}$ |
| $= 67.6 \text{ ksi}$ | $= 45.0 \text{ ksi}$ |

As shown in the LRFD calculation of $F_{cby}$ in the preceding text, the available flexural stresses can exceed the yield stress in cases where the available strength is governed by yielding and the yielding strength is calculated using the plastic section modulus.

**Combined Stress Ratio**

From AISC *Specification* Section H2, check the combined stress ratios as follows:

| LRFD | ASD |
|------|-----|
| $\dfrac{f_{ra}}{F_{ca}} + \dfrac{f_{rbx}}{F_{cbx}} + \dfrac{f_{rby}}{F_{cby}} \leq 1.0$ (from *Spec.* Eq. H2-1) | $\dfrac{f_{ra}}{F_{ca}} + \dfrac{f_{rbx}}{F_{cbx}} + \dfrac{f_{rby}}{F_{cby}} \leq 1.0$ (from *Spec.* Eq. H2-1) |
| $\dfrac{12.4 \text{ ksi}}{38.8 \text{ ksi}} + \dfrac{19.1 \text{ ksi}}{49.1 \text{ ksi}} + \dfrac{17.4 \text{ ksi}}{67.6 \text{ ksi}} = 0.966 < 1.0$ **o.k.** | $\dfrac{8.25 \text{ ksi}}{25.8 \text{ ksi}} + \dfrac{12.8 \text{ ksi}}{32.6 \text{ ksi}} + \dfrac{11.6 \text{ ksi}}{45.0 \text{ ksi}} = 0.970 < 1.0$ **o.k.** |

A comparison of these results with those from Example H.1B shows that AISC *Specification* Equation H1-1a will produce less conservative results than AISC *Specification* Equation H2-1 when its use is permitted.

Note: This check is made at a point on the cross section (extreme fiber, in this example). The designer must therefore determine which point on the cross section is critical or check multiple points if the critical point cannot be readily determined.

---

# H-8

## EXAMPLE H.3 W-SHAPE SUBJECT TO COMBINED AXIAL TENSION AND FLEXURE

### Given:

Select an ASTM A992/A992M W-shape with a 14 in. nominal depth to carry forces of 29 kips from dead load and 87 kips from live load in axial tension, as well as the following moments due to uniformly distributed loads:

$$M_{xD} = 32 \text{ kip-ft}$$
$$M_{xL} = 96 \text{ kip-ft}$$

$$M_{yD} = 11.3 \text{ kip-ft}$$
$$M_{yL} = 33.8 \text{ kip-ft}$$

The unbraced length is 30 ft and the ends are pinned. Assume the connections are made with no holes.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From ASCE/SEI 7, Chapter 2, the required strengths are:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(29 \text{ kips}) + 1.6(87 \text{ kips})$ | $P_a = 29 \text{ kips} + 87 \text{ kips}$ |
| $= 174 \text{ kips}$ | $= 116 \text{ kips}$ |
| $M_{ux} = 1.2(32 \text{ kip-ft}) + 1.6(96 \text{ kip-ft})$ | $M_{ax} = 32 \text{ kip-ft} + 96 \text{ kip-ft}$ |
| $= 192 \text{ kip-ft}$ | $= 128 \text{ kip-ft}$ |
| $M_{uy} = 1.2(11.3 \text{ kip-ft}) + 1.6(33.8 \text{ kip-ft})$ | $M_{ay} = 11.3 \text{ kip-ft} + 33.8 \text{ kip-ft}$ |
| $= 67.6 \text{ kip-ft}$ | $= 45.1 \text{ kip-ft}$ |

Try a W14×82.

From AISC *Manual* Tables 1-1 and 3-2, the properties are as follows:

W14×82
$A_g = 24.0 \text{ in.}^2$
$S_x = 123 \text{ in.}^3$
$Z_x = 139 \text{ in.}^3$
$S_y = 29.3 \text{ in.}^3$
$Z_y = 44.8 \text{ in.}^3$
$I_y = 148 \text{ in.}^4$
$L_p = 8.76 \text{ ft}$
$L_r = 33.2 \text{ ft}$

**Nominal Tensile Strength**

From AISC *Specification* Section D2(a), the nominal tensile strength due to tensile yielding in the gross section is:

---

# H-9

$$P_n = F_y A_g$$
$$\text{(Spec. Eq. D2-1)}$$

$$= (50 \text{ ksi})(24.0 \text{ in.}^2)$$

$$= 1{,}200 \text{ kips}$$

Note that for a member with holes, the rupture strength of the member would also have to be computed using AISC *Specification* Equation D2-2.

**Nominal Flexural Strength for Bending About the Major Axis**

*Yielding*

From AISC *Specification* Section F2.1, the nominal flexural strength due to yielding (plastic moment) is:

$$M_{nx} = M_p = F_y Z_x$$
$$\text{(Spec. Eq. F2-1)}$$

$$= (50 \text{ ksi})(139 \text{ in.}^3)$$

$$= 6{,}950 \text{ kip-in. or } 579 \text{ kip-ft}$$

*Lateral-Torsional Buckling*

From AISC *Specification* Section F2.2, the nominal flexural strength due to lateral-torsional buckling is determined as follows:

Because $L_p < L_b \leq L_r$, i.e., 8.76 ft < 30 ft < 33.2 ft, AISC *Specification* Equation F2-2 applies.

*Lateral-Torsional Buckling Modification Factor, $C_b$*

From AISC *Manual* Table 3-1, $C_b = 1.14$, without considering the beneficial effects of the tension force. However, per AISC *Specification* Section H1.2, $C_b$ may be modified because the column is in axial tension concurrently with flexure.

$$P_{ey} = \frac{\pi^2 EI_y}{L_b^2}$$
$$\text{(Spec. Eq. H1-2)}$$

$$= \frac{\pi^2 (29{,}000 \text{ ksi})(148 \text{ in.}^4)}{\left[(30 \text{ ft})(12.0 \text{ in./ft})\right]^2}$$

$$= 327 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\sqrt{1 + \dfrac{\alpha P_u}{P_{ey}}} = \sqrt{1 + \dfrac{1.0(174 \text{ kips})}{327 \text{ kips}}}$ | $\sqrt{1 + \dfrac{\alpha P_a}{P_{ey}}} = \sqrt{1 + \dfrac{1.6(116 \text{ kips})}{327 \text{ kips}}}$ |
| $= 1.24$ | $= 1.25$ |

$$C_b = 1.24(1.14)$$

$$= 1.41$$

---

# H-10

$$M_n = C_b\left[M_p - (M_p - 0.7F_y S_x)\left(\frac{L_b - L_p}{L_r - L_p}\right)\right] \leq M_p$$
$$\text{(Spec. Eq. F2-2)}$$

$$= 1.41\left\{6{,}950 \text{ kip-in.} - \left[6{,}950 \text{ kip-in.} - 0.7(50 \text{ ksi})(123 \text{ in.}^3)\right]\left(\frac{30 \text{ ft} - 8.76 \text{ ft}}{33.2 \text{ ft} - 8.76 \text{ ft}}\right)\right\} \leq 6{,}950 \text{ kip-in.}$$

$$= 6{,}560 \text{ kip-in. or } 547 \text{ kip-ft}$$ **controls**

*Local Buckling*

Per AISC *Manual* Table 1-1, a W14×82 does not have an "[f]" footnote, indicating the cross section is compact at $F_y = 50 \text{ ksi}$; therefore, the local buckling limit state does not apply.

**Nominal Flexural Strength for Bending About the Minor Axis and the Interaction of Flexure and Tension**

Because a W14×82 has compact flanges, only the limit state of yielding applies for bending about the minor axis.

$$M_{ny} = M_p = F_y Z_y \leq 1.6F_y S_y$$
$$\text{(Spec. Eq. F6-1)}$$

$$= (50 \text{ ksi})(44.8 \text{ in.}^3) \leq 1.6(50 \text{ ksi})(29.3 \text{ in.}^3)$$

$$= 2{,}240 \text{ kip-in.} < 2{,}340 \text{ kip-in.}$$

$$= 2{,}240 \text{ kip-in. or } 187 \text{ kip-ft}$$

**Available Strength**

From AISC *Specification* Sections D2 and F1, the available strengths are:

| LRFD | ASD |
|------|-----|
| $\phi_b = \phi_t = 0.90$ | $\Omega_b = \Omega_t = 1.67$ |
| $P_c = \phi_t P_n$ | $P_c = \dfrac{P_n}{\Omega_t}$ |
| $= 0.90(1{,}200 \text{ kips})$ | $= \dfrac{1{,}200 \text{ kips}}{1.67}$ |
| $= 1{,}080 \text{ kips}$ | $= 719 \text{ kips}$ |
| $M_{cx} = \phi_b M_{nx}$ | $M_{cx} = \dfrac{M_{nx}}{\Omega_b}$ |
| $= 0.90(547 \text{ kip-ft})$ | $= \dfrac{547 \text{ kip-ft}}{1.67}$ |
| $= 492 \text{ kip-ft}$ | $= 328 \text{ kip-ft}$ |
| $M_{cy} = \phi_b M_{ny}$ | $M_{cy} = \dfrac{M_{ny}}{\Omega_b}$ |
| $= 0.90(187 \text{ kip-ft})$ | $= \dfrac{187 \text{ kip-ft}}{1.67}$ |
| $= 168 \text{ kip-ft}$ | $= 112 \text{ kip-ft}$ |

**Interaction of Tension and Flexure**

Check the limit for AISC *Specification* Equation H1-1a.

---

# H-11

| LRFD | ASD |
|------|-----|
| $\dfrac{P_r}{P_c} = \dfrac{P_u}{\phi_t P_n}$ | $\dfrac{P_r}{P_c} = \dfrac{P_a}{P_n/\Omega_t}$ |
| $= \dfrac{174 \text{ kips}}{1{,}080 \text{ kips}}$ | $= \dfrac{116 \text{ kips}}{719 \text{ kips}}$ |
| $= 0.161 < 0.2$ | $= 0.161 < 0.2$ |
| Because $\dfrac{P_r}{P_c} < 0.2$, | Because $\dfrac{P_r}{P_c} < 0.2$, |
| $\dfrac{P_r}{2P_c} + \left(\dfrac{M_{rx}}{M_{cx}} + \dfrac{M_{ry}}{M_{cy}}\right) \leq 1.0$ (*Spec.* Eq. H1-1b) | $\dfrac{P_r}{2P_c} + \left(\dfrac{M_{rx}}{M_{cx}} + \dfrac{M_{ry}}{M_{cy}}\right) \leq 1.0$ (*Spec.* Eq. H1-1b) |
| $= \dfrac{174 \text{ kips}}{2(1{,}080 \text{ kips})} + \left(\dfrac{192 \text{ kip-ft}}{492 \text{ kip-ft}} + \dfrac{67.6 \text{ kip-ft}}{168 \text{ kip-ft}}\right) \leq 1.0$ | $= \dfrac{116 \text{ kips}}{2(719 \text{ kips})} + \left(\dfrac{128 \text{ kip-ft}}{328 \text{ kip-ft}} + \dfrac{45.1 \text{ kip-ft}}{112 \text{ kip-ft}}\right) \leq 1.0$ |
| $= 0.873 < 1.0$ **o.k.** | $= 0.874 < 1.0$ **o.k.** |

---

# H-12

## EXAMPLE H.4 W-SHAPE SUBJECT TO COMBINED AXIAL COMPRESSION AND FLEXURE

### Given:

Select an ASTM A992/A992M W-shape with a 10 in. nominal depth to carry axial compression forces of 5 kips from dead load and 15 kips from live load. The unbraced length is 14 ft and the ends are pinned. The member also has the following required moment strengths due to uniformly distributed loads, not including second-order effects:

$$M_{xD} = 15 \text{ kip-ft}$$
$$M_{xL} = 45 \text{ kip-ft}$$

$$M_{yD} = 2 \text{ kip-ft}$$
$$M_{yL} = 6 \text{ kip-ft}$$

The member is not subject to sidesway (no lateral translation).

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From Chapter 2 of ASCE/SEI 7, the required strength (not considering second-order effects) is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(5 \text{ kips}) + 1.6(15 \text{ kips})$ | $P_a = 5 \text{ kips} + 15 \text{ kips}$ |
| $= 30.0 \text{ kips}$ | $= 20.0 \text{ kips}$ |
| $M_{ux} = 1.2(15 \text{ kip-ft}) + 1.6(45 \text{ kip-ft})$ | $M_{ax} = 15 \text{ kip-ft} + 45 \text{ kip-ft}$ |
| $= 90.0 \text{ kip-ft}$ | $= 60.0 \text{ kip-ft}$ |
| $M_{uy} = 1.2(2 \text{ kip-ft}) + 1.6(6 \text{ kip-ft})$ | $M_{ay} = 2 \text{ kip-ft} + 6 \text{ kip-ft}$ |
| $= 12.0 \text{ kip-ft}$ | $= 8.00 \text{ kip-ft}$ |

Try a W10×33.

From AISC *Manual* Tables 1-1 and 3-2, the properties are as follows:

W10×33
$S_x = 35.0 \text{ in.}^3$
$Z_x = 38.8 \text{ in.}^3$
$I_x = 171 \text{ in.}^4$
$r_x = 4.19 \text{ in.}$
$S_y = 9.20 \text{ in.}^3$
$Z_y = 14.0 \text{ in.}^3$
$I_y = 36.6 \text{ in.}^4$
$r_y = 1.94 \text{ in.}$
$L_p = 6.85 \text{ ft}$
$L_r = 21.8 \text{ ft}$

---

# H-13

**Available Axial Strength**

From AISC *Specification* Commentary Table C-A-7.1, for a pinned-pinned condition, $K = 1.0$. Because $L_c = KL_x = KL_y = 14.0 \text{ ft}$ and $r_x > r_y$, the *y*-*y* axis will govern.

From AISC *Manual* Table 6-1, the available axial strength is:

| LRFD | ASD |
|------|-----|
| $P_c = \phi_c P_n$ | $P_c = \dfrac{P_n}{\Omega_c}$ |
| $= 253 \text{ kips}$ | $= 168 \text{ kips}$ |

**Required Flexural Strength (including second-order amplification)**

Use the approximate method of second-order analysis procedure from AISC *Specification* Appendix 8. Because the member is not subject to sidesway, only *P*-δ amplifiers need to be added.

$$B_1 = \frac{C_m}{1 - \alpha P_r/P_{e1}} \geq 1$$
$$\text{(Spec. Eq. A-8-3)}$$

where $C_m$ is conservatively taken per AISC *Specification* Appendix 8, Section 8.1.2(b):

$$C_m = 1.0$$

The *x*-*x* axis flexural magnifier is:

$$P_{e1x} = \frac{\pi^2 EI_x}{(L_{e1x})^2}$$
$$\text{(from Spec. Eq. A-8-5)}$$

$$= \frac{\pi^2 (29{,}000 \text{ ksi})(171 \text{ in.}^4)}{\left[(14 \text{ ft})(12 \text{ in./ft})\right]^2}$$

$$= 1{,}730 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\alpha = 1.0$ | $\alpha = 1.6$ |
| $B_{1x} = \dfrac{C_m}{1 - \alpha P_r/P_{e1x}} \geq 1.0$ | $B_{1x} = \dfrac{C_m}{1 - \alpha P_r/P_{e1x}} \geq 1.0$ |
| $= \dfrac{1.0}{1 - 1.0(30.0 \text{ kips}/1{,}730 \text{ kips})} \geq 1.0$ | $= \dfrac{1.0}{1 - 1.6(20.0 \text{ kips}/1{,}730 \text{ kips})} \geq 1.0$ |
| $= 1.02$ | $= 1.02$ |
| $M_{ux} = 1.02(90 \text{ kip-ft})$ | $M_{ax} = 1.02(60 \text{ kip-ft})$ |
| $= 91.8 \text{ kip-ft}$ | $= 61.2 \text{ kip-ft}$ |

The *y*-*y* axis flexural magnifier is:

---

# H-14

$$P_{e1y} = \frac{\pi^2 EI_y}{(L_{e1y})^2}$$
$$\text{(from Spec. Eq. A-8-5)}$$

$$= \frac{\pi^2 (29{,}000 \text{ ksi})(36.6 \text{ in.}^4)}{\left[(14 \text{ ft})(12 \text{ in./ft})\right]^2}$$

$$= 371 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\alpha = 1.0$ | $\alpha = 1.6$ |
| $B_{1y} = \dfrac{C_m}{1 - \alpha P_r/P_{e1y}} \geq 1.0$ | $B_{1y} = \dfrac{C_m}{1 - \alpha P_r/P_{e1y}} \geq 1.0$ |
| $= \dfrac{1.0}{1 - 1.0(30.0 \text{ kips}/371 \text{ kips})} \geq 1.0$ | $= \dfrac{1.0}{1 - 1.6(20.0 \text{ kips}/371 \text{ kips})} \geq 1.0$ |
| $= 1.09$ | $= 1.09$ |
| $M_{uy} = 1.09(12.0 \text{ kip-ft})$ | $M_{ay} = 1.09(8.00 \text{ kip-ft})$ |
| $= 13.1 \text{ kip-ft}$ | $= 8.72 \text{ kip-ft}$ |

**Nominal Flexural Strength about the Major Axis**

*Yielding*

$$M_{nx} = M_p = F_y Z_x$$
$$\text{(Spec. Eq. F2-1)}$$

$$= (50 \text{ ksi})(38.8 \text{ in.}^3)$$

$$= 1{,}940 \text{ kip-in.}$$

*Lateral-Torsional Buckling*

Because $L_p < L_b \leq L_r$, i.e., 6.85 ft < 14.0 ft < 21.8 ft, AISC *Specification* Equation F2-2 applies.

From AISC *Manual* Table 3-1, $C_b = 1.14$.

$$M_{nx} = C_b\left[M_p - (M_p - 0.7F_y S_x)\left(\frac{L_b - L_p}{L_r - L_p}\right)\right] \leq M_p$$
$$\text{(Spec. Eq. F2-2)}$$

$$= 1.14\left\{1{,}940 \text{ kip-in.} - \left[1{,}940 \text{ kip-in.} - 0.7(50 \text{ ksi})(35.0 \text{ in.}^3)\right]\left(\frac{14 \text{ ft} - 6.85 \text{ ft}}{21.8 \text{ ft} - 6.85 \text{ ft}}\right)\right\} < 1{,}940 \text{ kip-in.}$$

$$= 1{,}820 \text{ kip-in.} < 1{,}940 \text{ kip-in.}$$

$$= 1{,}820 \text{ kip-in. or } 152 \text{ kip-ft}$$ **controls**

*Local Buckling*

Per AISC *Manual* Table 1-1, a W10×33 does not have an "[f]" footnote, indicating the member is compact for $F_y = 50 \text{ ksi}$, so the local buckling limit state does not apply.

**Nominal Flexural Strength about the Minor Axis**

---

# H-15

Determine the nominal flexural strength for bending about the minor axis from AISC *Specification* Section F6. Because a W10×33 has compact flanges, only the yielding limit state applies.

From AISC *Specification* Section F6.1:

$$M_{ny} = M_p = F_y Z_y \leq 1.6F_y S_y$$
$$\text{(Spec. Eq. F6-1)}$$

$$= (50 \text{ ksi})(14.0 \text{ in.}^3) \leq 1.6(50 \text{ ksi})(9.20 \text{ in.}^3)$$

$$= 700 \text{ kip-in.} < 736 \text{ kip-in.}$$

$$= 700 \text{ kip-in. or } 58.3 \text{ kip-ft}$$

From AISC *Specification* Section F1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $M_{cx} = \phi_b M_{nx}$ | $M_{cx} = \dfrac{M_{nx}}{\Omega_b}$ |
| $= 0.90(152 \text{ kip-ft})$ | $= \dfrac{152 \text{ kip-ft}}{1.67}$ |
| $= 137 \text{ kip-ft}$ | $= 91.0 \text{ kip-ft}$ |
| $M_{cy} = \phi_b M_{ny}$ | $M_{cy} = \dfrac{M_{ny}}{\Omega_b}$ |
| $= 0.90(58.3 \text{ kip-ft})$ | $= \dfrac{58.3 \text{ kip-ft}}{1.67}$ |
| $= 52.5 \text{ kip-ft}$ | $= 34.9 \text{ kip-ft}$ |

Check the limit for AISC *Specification* Equations H1-1a and H1-1b.

| LRFD | ASD |
|------|-----|
| $\dfrac{P_r}{P_c} = \dfrac{P_u}{\phi_c P_n}$ | $\dfrac{P_r}{P_c} = \dfrac{P_a}{P_n/\Omega_c}$ |
| $= \dfrac{30.0 \text{ kips}}{253 \text{ kips}}$ | $= \dfrac{20.0 \text{ kips}}{168 \text{ kips}}$ |
| $= 0.119 < 0.2$ | $= 0.119 < 0.2$ |
| Because $\dfrac{P_r}{P_c} < 0.2$, | Because $\dfrac{P_r}{P_c} < 0.2$, |
| $\dfrac{P_r}{2P_c} + \left(\dfrac{M_{rx}}{M_{cx}} + \dfrac{M_{ry}}{M_{cy}}\right) \leq 1.0$ (*Spec.* Eq. H1-1b) | $\dfrac{P_r}{2P_c} + \left(\dfrac{M_{rx}}{M_{cx}} + \dfrac{M_{ry}}{M_{cy}}\right) \leq 1.0$ (*Spec.* Eq. H1-1b) |
| $= \dfrac{30.0 \text{ kips}}{2(253 \text{ kips})} + \left(\dfrac{91.8 \text{ kip-ft}}{137 \text{ kip-ft}} + \dfrac{13.1 \text{ kip-ft}}{52.5 \text{ kip-ft}}\right) \leq 1.0$ | $= \dfrac{20.0 \text{ kips}}{2(168 \text{ kips})} + \left(\dfrac{61.2 \text{ kip-ft}}{91.0 \text{ kip-ft}} + \dfrac{8.72 \text{ kip-ft}}{34.9 \text{ kip-ft}}\right)$ |
| $= 0.979 < 1.0$ **o.k.** | $= 0.982 < 1.0$ **o.k.** |

---

# H-16

## EXAMPLE H.5A RECTANGULAR HSS TORSIONAL STRENGTH

### Given:

Determine the available torsional strength of an ASTM A500/A500M, Grade C, HSS6×4×¼.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A500/A500M Grade C
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-11, the geometric properties are as follows:

HSS6×4×¼
$t = 0.233 \text{ in.}$
$b/t = 14.2$
$h/t = 22.8$
$C = 10.1 \text{ in.}^3$

The available torsional strength for rectangular HSS is stipulated in AISC *Specification* Section H3.1. The critical stress, $F_{cr}$, is determined from AISC *Specification* Section H3.1(b).

Because $h/t > b/t$, $h/t = 22.8$ governs.

$$2.45\sqrt{\frac{E}{F_y}} = 2.45\sqrt{\frac{29{,}000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 59.0 > 22.8$$; therefore, use AISC *Specification* Equation H3-3 to determine $F_{cr}$

$$F_{cr} = 0.6F_y$$
$$\text{(Spec. Eq. H3-3)}$$

$$= 0.6(50 \text{ ksi})$$

$$= 30.0 \text{ ksi}$$

The nominal torsional strength is:

$$T_n = F_{cr}C$$
$$\text{(Spec. Eq. H3-1)}$$

$$= (30.0 \text{ ksi})(10.1 \text{ in.}^3)$$

$$= 303 \text{ kip-in.}$$

From AISC *Specification* Section H3.1, the available torsional strength is:

| LRFD | ASD |
|------|-----|
| $\phi_T = 0.90$ | $\Omega_T = 1.67$ |
| $\phi_T T_n = 0.90(303 \text{ kip-in.})$ | $\dfrac{T_n}{\Omega_T} = \dfrac{303 \text{ kip-in.}}{1.67}$ |
| $= 273 \text{ kip-in.}$ | $= 181 \text{ kip-in.}$ |

---

# H-17

Note: For more complete guidance on designing for torsion, see AISC Design Guide 9, *Torsional Analysis of Structural Steel Members* (Seaburg and Carter, 1997).

---

# H-18

## EXAMPLE H.5B ROUND HSS TORSIONAL STRENGTH

### Given:

Determine the available torsional strength of an ASTM A500/A500M, Grade C, HSS5.000×0.250 that is 14 ft long.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A500/A500M Grade C
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-13, the geometric properties are as follows:

HSS5.000×0.250
$t = 0.233 \text{ in.}$
$D/t = 21.5$
$C = 7.95 \text{ in.}^3$

The available torsional strength for round HSS is stipulated in AISC *Specification* Section H3.1. The critical stress, $F_{cr}$, is determined from AISC *Specification* Section H3.1(a).

Calculate the critical stress as the larger of:

$$F_{cr} = \frac{1.23E}{\sqrt{\dfrac{L}{D}\left(\dfrac{D}{t}\right)^{5/4}}}$$
$$\text{(Spec. Eq. H3-2a)}$$

$$= \frac{1.23(29{,}000 \text{ ksi})}{\sqrt{\dfrac{(14 \text{ ft})(12 \text{ in./ft})}{5.00 \text{ in.}}(21.5)^{5/4}}}$$

$$= 133 \text{ ksi}$$

and

$$F_{cr} = \frac{0.60E}{\left(\dfrac{D}{t}\right)^{3/2}}$$
$$\text{(Spec. Eq. H3-2b)}$$

$$= \frac{0.60(29{,}000 \text{ ksi})}{(21.5)^{3/2}}$$

$$= 175 \text{ ksi}$$

However, $F_{cr}$ shall not exceed the following:

$$0.6F_y = 0.6(50 \text{ ksi})$$

$$= 30.0 \text{ ksi}$$

Therefore, $F_{cr} = 30.0 \text{ ksi}$.

---

# H-19

The nominal torsional strength is:

$$T_n = F_{cr}C$$
$$\text{(Spec. Eq. H3-1)}$$

$$= (30.0 \text{ ksi})(7.95 \text{ in.}^3)$$

$$= 239 \text{ kip-in.}$$

From AISC *Specification* Section H3.1, the available torsional strength is:

| LRFD | ASD |
|------|-----|
| $\phi_T = 0.90$ | $\Omega_T = 1.67$ |
| $\phi_T T_n = 0.90(239 \text{ kip-in.})$ | $\dfrac{T_n}{\Omega_T} = \dfrac{239 \text{ kip-in.}}{1.67}$ |
| $= 215 \text{ kip-in.}$ | $= 143 \text{ kip-in.}$ |

Note: For more complete guidance on designing for torsion, see AISC Design Guide 9, *Torsional Analysis of Structural Steel Members* (Seaburg and Carter, 1997).

---

# H-20

## EXAMPLE H.5C RECTANGULAR HSS COMBINED TORSIONAL AND FLEXURAL STRENGTH

### Given:

Verify the strength of an ASTM A500/A500M, Grade C, HSS6×4×¼ loaded as shown. The beam is simply supported and is torsionally fixed at the ends. Bending is about the strong axis.

$$w_D = 0.46 \text{ kip/ft (applied 6 in. off centerline)}$$
$$w_L = 1.38 \text{ kip/ft (applied 6 in. off centerline)}$$

![Beam loading and bracing diagram showing a simply supported beam with distributed loads applied 6 in. off centerline, span length L = 8'-0"]

*Fig. H.5C. Beam loading and bracing diagram.*

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A500/A500M Grade C
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-11, the geometric properties are as follows:

HSS6×4×¼
$t = 0.233 \text{ in.}$
$A_g = 4.30 \text{ in.}^2$
$b/t = 14.2$
$h/t = 22.8$
$r_y = 1.61 \text{ in.}$
$Z_x = 8.53 \text{ in.}^3$
$J = 23.6 \text{ in.}^4$

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.46 \text{ kip/ft}) + 1.6(1.38 \text{ kip/ft})$ | $w_a = 0.46 \text{ kip/ft} + 1.38 \text{ kip/ft}$ |
| $= 2.76 \text{ kip/ft}$ | $= 1.84 \text{ kip/ft}$ |

Calculate the maximum shear (at the supports) using AISC *Manual* Table 3-22, Case 1.

| LRFD | ASD |
|------|-----|
| $V_r = V_u$ | $V_r = V_a$ |
| $= \dfrac{w_u L}{2}$ | $= \dfrac{w_a L}{2}$ |
| $= \dfrac{(2.76 \text{ kip/ft})(8 \text{ ft})}{2}$ | $= \dfrac{(1.84 \text{ kip/ft})(8 \text{ ft})}{2}$ |
| $= 11.0 \text{ kips}$ | $= 7.36 \text{ kips}$ |

---

# H-21

Calculate the maximum torsion (at the supports).

| LRFD | ASD |
|------|-----|
| $T_r = T_u$ | $T_r = T_a$ |
| $= \dfrac{w_u Le}{2}$ | $= \dfrac{w_a Le}{2}$ |
| $= \dfrac{(2.76 \text{ kip/ft})(8 \text{ ft})(6 \text{ in.})}{2}$ | $= \dfrac{(1.84 \text{ kip/ft})(8 \text{ ft})(6 \text{ in.})}{2}$ |
| $= 66.2 \text{ kip-in.}$ | $= 44.2 \text{ kip-in.}$ |

**Available Shear Strength**

Determine the available shear strength from AISC *Specification* Section G4. Using the provisions given in AISC *Specification* Section B4.1b(d), determine the web depth, $h$, as follows:

$$h = 6.00 \text{ in.} - 3(0.233 \text{ in.})$$

$$= 5.30 \text{ in.}$$

From AISC *Specification* Section G4:

$$A_w = 2ht$$

$$= 2(5.30 \text{ in.})(0.233 \text{ in.})$$

$$= 2.47 \text{ in.}^2$$

$$k_v = 5$$

The web shear buckling coefficient is determined from AISC *Specification* Section G2.2.

$$1.10\sqrt{\frac{k_v E}{F_y}} = 1.10\sqrt{\frac{5(29{,}000 \text{ ksi})}{50 \text{ ksi}}}$$

$$= 59.2$$

Because $h/t = 22.8 < 59.2$, use AISC *Specification* Section G2.2(b)(i).

$$C_{v2} = 1.0$$
$$\text{(Spec. Eq. G2-9)}$$

The nominal shear strength from AISC *Specification* Section G4 is:

$$V_n = 0.6F_y A_w C_{v2}$$
$$\text{(Spec. Eq. G4-1)}$$

$$= 0.6(50 \text{ ksi})(2.47 \text{ in.}^2)(1.0)$$

$$= 74.1 \text{ kips}$$

From AISC *Specification* Section G1, the available shear strength is:

---

# H-22

| LRFD | ASD |
|------|-----|
| $\phi_v = 0.90$ | $\Omega_v = 1.67$ |
| $V_c = \phi_v V_n$ | $V_c = \dfrac{V_n}{\Omega_v}$ |
| $= 0.90(74.1 \text{ kips})$ | $= \dfrac{74.1 \text{ kips}}{1.67}$ |
| $= 66.7 \text{ kips}$ | $= 44.4 \text{ kips}$ |

**Available Flexural Strength**

The available flexural strength is determined from AISC *Specification* Section F7 for rectangular HSS. For the limit state of flexural yielding, the nominal flexural strength is:

$$M_n = M_p = F_y Z_x$$
$$\text{(Spec. Eq. F7-1)}$$

$$= (50 \text{ ksi})(8.53 \text{ in.}^3)$$

$$= 427 \text{ kip-in.}$$

Determine if the limit state of flange local buckling applies as follows:

$$\lambda = b/t$$

$$= 14.2$$

Determine the flange compact slenderness limit from AISC *Specification* Table B4.1b, Case 17.

$$\lambda_p = 1.12\sqrt{\frac{E}{F_y}}$$

$$= 1.12\sqrt{\frac{29{,}000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 27.0$$

$\lambda < \lambda_p$; therefore, the flange is compact, and the flange local buckling limit state does not apply.

Determine if the limit state of web local buckling applies as follows:

$$\lambda = h/t$$

$$= 22.8$$

Determine the web compact slenderness limit from AISC *Specification* Table B4.1b, Case 19.

$$\lambda_p = 2.42\sqrt{\frac{E}{F_y}}$$

$$= 2.42\sqrt{\frac{29{,}000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 58.3$$

$\lambda < \lambda_p$; therefore, the web is compact, and the web local buckling limit state does not apply.

---

# H-23

Determine if lateral-torsional buckling applies as follows:

$$L_p = 0.13Er_y \sqrt{\frac{JA_g}{M_p}}$$
$$\text{(Spec. Eq. F7-12)}$$

$$= 0.13(29{,}000 \text{ ksi})(1.61 \text{ in.})\sqrt{\frac{(23.6 \text{ in.}^4)(4.30 \text{ in.}^2)}{427 \text{ kip-in.}}}$$

$$= 143 \text{ in. or } 11.9 \text{ ft}$$

Because $L_b = 8 \text{ ft} < L_p = 11.9 \text{ ft}$, lateral-torsional buckling is not applicable and $M_n = 427 \text{ kip-in.}$, controlled by the flexural yielding limit state. From AISC *Specification* Section F1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $M_c = \phi_b M_n$ | $M_c = \dfrac{M_n}{\Omega_b}$ |
| $= 0.90(427 \text{ kip-in.})$ | $= \dfrac{427 \text{ kip-in.}}{1.67}$ |
| $= 384 \text{ kip-in.}$ | $= 256 \text{ kip-in.}$ |

From Example H.5A, the available torsional strength is:

| LRFD | ASD |
|------|-----|
| $T_c = \phi_T T_n$ | $T_c = \dfrac{T_n}{\Omega_T}$ |
| $= 273 \text{ kip-in.}$ | $= 181 \text{ kip-in.}$ |

Using AISC *Specification* Section H3.2, check combined strength at several locations where $T_r > 0.2T_c$. First check at the supports, which is the point of maximum shear and torsion:

| LRFD | ASD |
|------|-----|
| $\dfrac{T_r}{T_c} = \dfrac{66.2 \text{ kip-in.}}{273 \text{ kip-in.}}$ | $\dfrac{T_r}{T_c} = \dfrac{44.2 \text{ kip-in.}}{181 \text{ kip-in.}}$ |
| $= 0.242 > 0.2$ | $= 0.244 > 0.2$ |
| Therefore, use AISC *Specification* Equation H3-6: | Therefore, use AISC *Specification* Equation H3-6: |
| $\left(\dfrac{P_r}{P_c} + \dfrac{M_{rx}}{M_{cx}} + \dfrac{M_{ry}}{M_{cy}}\right) + \left(\dfrac{V_r}{V_c} + \dfrac{T_r}{T_c}\right)^2 \leq 1.0$ | $\left(\dfrac{P_r}{P_c} + \dfrac{M_{rx}}{M_{cx}} + \dfrac{M_{ry}}{M_{cy}}\right) + \left(\dfrac{V_r}{V_c} + \dfrac{T_r}{T_c}\right)^2 \leq 1.0$ |
| (*Spec* Eq. H3-6) | (*Spec* Eq. H3-6) |
| $= (0 + 0 + 0) + \left(\dfrac{11.0 \text{ kips}}{66.7 \text{ kips}} + \dfrac{66.2 \text{ kip-in.}}{273 \text{ kip-in.}}\right)$ | $= (0 + 0 + 0) + \left(\dfrac{7.36 \text{ kips}}{44.4 \text{ kips}} + \dfrac{44.2 \text{ kip-in.}}{181 \text{ kip-in.}}\right)^2$ |
| $= 0.166 < 1.0$ **o.k.** | $= 0.168 < 1.0$ **o.k.** |

Check the combined strength near the location where $T_r = 0.2T_c$. This is the location with the largest bending moment required to be considered in the interaction. Calculate the shear and moment at this location, $x$.

---

# H-24

| LRFD | ASD |
|------|-----|
| $\dfrac{T_r}{T_c} = 0.20$ | $\dfrac{T_r}{T_c} = 0.20$ |
| Therefore at $x$: | Therefore at $x$: |
| $T_r = 0.20(273 \text{ kip-in.})$ | $T_r = 0.20(181 \text{ kip-in.})$ |
| $= 54.6 \text{ kip-in.}$ | $= 36.2 \text{ kip-in.}$ |
| $x = \dfrac{(T_r \text{ at support}) - (T_r \text{ at } x)}{w_u e}$ | $x = \dfrac{(T_r \text{ at support}) - (T_r \text{ at } x)}{w_a e}$ |
| $= \dfrac{66.2 \text{ kip-in.} - 54.6 \text{ kip-in.}}{(2.76 \text{ kip/ft})(6 \text{ in.})}$ | $= \dfrac{44.2 \text{ kip-in.} - 36.2 \text{ kip-in.}}{(1.84 \text{ kip/ft})(6 \text{ in.})}$ |
| $= 0.700 \text{ ft}$ | $= 0.725 \text{ ft}$ |
| $V_r = 11.0 \text{ kips} - (0.700 \text{ ft})(2.76 \text{ kip/ft})$ | $V_r = 7.36 \text{ kips} - (0.725 \text{ ft})(1.84 \text{ kips/ft})$ |
| $= 9.07 \text{ kips}$ | $= 6.03 \text{ kips}$ |
| From AISC *Manual* Table 3-22, Case 1: | From AISC *Manual* Table 3-22, Case 1: |
| $M_r = \dfrac{w_u x}{2}(l - x)$ | $M_r = \dfrac{w_a x}{2}(l - x)$ |
| $= \dfrac{(2.76 \text{ kip/ft})(0.700 \text{ ft})}{2}(8 \text{ ft} - 0.700 \text{ ft})$ | $= \dfrac{(1.84 \text{ kip/ft})(0.725 \text{ ft})}{2}(8 \text{ ft} - 0.725 \text{ ft})$ |
| $= 7.05 \text{ kip-ft or } 84.6 \text{ kip-in.}$ | $= 4.85 \text{ kip-ft or } 58.2 \text{ kip-in.}$ |
| $\left(\dfrac{P_r}{P_c} + \dfrac{M_{rx}}{M_{cx}} + \dfrac{M_{ry}}{M_{cy}}\right) + \left(\dfrac{V_r}{V_c} + \dfrac{T_r}{T_c}\right)^2 \leq 1.0$ | $\left(\dfrac{P_r}{P_c} + \dfrac{M_{rx}}{M_{cx}} + \dfrac{M_{ry}}{M_{cy}}\right) + \left(\dfrac{V_r}{V_c} + \dfrac{T_r}{T_c}\right)^2 \leq 1.0$ |
| (*Spec* Eq. H3-6) | (*Spec* Eq. H3-6) |
| $= \left(0 + \dfrac{84.6 \text{ kip-in.}}{384 \text{ kip-in.}} + 0\right) + \left(\dfrac{9.07 \text{ kips}}{66.7 \text{ kips}} + 0.20\right)^2$ | $= \left(0 + \dfrac{58.2 \text{ kip-in.}}{256 \text{ kip-in.}} + 0\right) + \left(\dfrac{6.03 \text{ kips}}{44.4 \text{ kips}} + 0.20\right)^2$ |
| $= 0.333 < 1.0$ **o.k.** | $= 0.340 < 1.0$ **o.k.** |

Note: The remainder of the beam, where $T_r \leq 0.2T_c$, must also be checked to determine if the strength without torsion controls over the interaction with torsion.

---

# H-25

## EXAMPLE H.6 W-SHAPE TORSIONAL STRENGTH

### Given:

As shown in Figure H.6-1, an ASTM A992/A992M W10×49 spans 15 ft and supports concentrated loads at midspan that act at a 6-in. eccentricity with respect to the shear center. Determine the stresses on the cross section, the adequacy of the section to support the loads, and the maximum rotation.

$$P_D = 2.5 \text{ kips (applied 6 in. off centerline)}$$
$$P_L = 7.5 \text{ kips (applied 6 in. off centerline)}$$

![Beam loading diagram showing a simply supported beam with concentrated load at midspan applied 6 in. off centerline, supports at 7'-6" from each end, total span L = 15'-0"]

*Fig. H.6-1. Beam loading diagram.*

The end conditions are assumed to be flexurally pinned and unrestrained for warping torsion. The eccentric load can be resolved into a torsional moment and a load applied through the shear center.

A similar design example appears in AISC Design Guide 9, *Torsional Analysis of Structural Steel Members* (Seaburg and Carter, 1997).

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-1, the geometric properties are as follows:

W10×49
$t_w = 0.340 \text{ in.}$
$t_f = 0.560 \text{ in.}$
$I_x = 272 \text{ in.}^4$
$S_x = 54.6 \text{ in.}^3$
$Z_x = 60.4 \text{ in.}^3$
$J = 1.39 \text{ in.}^4$
$C_w = 2{,}070 \text{ in.}^6$

From the V16.0 AISC Shapes Database, the additional torsional properties are as follows:

W10×49
$S_{w1} = 33.0 \text{ in.}^4$
$W_{no} = 23.6 \text{ in.}^2$
$Q_f = 12.8 \text{ in.}^3$
$Q_w = 29.8 \text{ in.}^3$

---

# H-26

From AISC Design Guide 9, the torsional property, $a$, is calculated as follows:

$$a = \sqrt{\frac{EC_w}{GJ}}$$
$$({\text{Design Guide 9, Eq. 3.6}})$$

$$= \sqrt{\frac{(29{,}000 \text{ ksi})(2{,}070 \text{ in.}^6)}{(11{,}200 \text{ ksi})(1.39 \text{ in.}^4)}}$$

$$= 62.1 \text{ in.}$$

From ASCE/SEI 7, Chapter 2, and AISC *Manual* Table 3-22, Case 7, the required strengths are:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(2.5 \text{ kips}) + 1.6(7.5 \text{ kips})$ | $P_a = 2.5 \text{ kips} + 7.5 \text{ kips}$ |
| $= 15.0 \text{ kips}$ | $= 10.0 \text{ kips}$ |
| $V_u = \dfrac{P_u}{2}$ | $V_a = \dfrac{P_a}{2}$ |
| $= \dfrac{15.0 \text{ kips}}{2}$ | $= \dfrac{10.0 \text{ kips}}{2}$ |
| $= 7.50 \text{ kips}$ | $= 5.00 \text{ kips}$ |
| $M_u = \dfrac{P_u L}{4}$ | $M_a = \dfrac{P_a L}{4}$ |
| $= \dfrac{(15.0 \text{ kips})(15 \text{ ft})(12 \text{ in./ft})}{4}$ | $= \dfrac{(10.0 \text{ kips})(15 \text{ ft})(12 \text{ in./ft})}{4}$ |
| $= 675 \text{ kip-in.}$ | $= 450 \text{ kip-in.}$ |
| $T_u = P_u e$ | $T_a = P_a e$ |
| $= (15.0 \text{ kips})(6 \text{ in.})$ | $= (10.0 \text{ kips})(6 \text{ in.})$ |
| $= 90.0 \text{ kip-in.}$ | $= 60.0 \text{ kip-in.}$ |

**Normal and Shear Stresses from Flexure**

The normal and shear stresses from flexure are determined from AISC Design Guide 9, as follows:

| LRFD | ASD |
|------|-----|
| $\sigma_{nb} = \dfrac{M_u}{S_x}$ (from Design Guide 9, Eq. 4.5) | $\sigma_{nb} = \dfrac{M_a}{S_x}$ (from Design Guide 9, Eq. 4.5) |
| $= \dfrac{675 \text{ kip-in.}}{54.6 \text{ in.}^3}$ | $= \dfrac{450 \text{ kip-in.}}{54.6 \text{ in.}^3}$ |
| $= 12.4 \text{ ksi (compression at top, tension at bottom)}$ | $= 8.24 \text{ ksi (compression at top, tension at bottom)}$ |
| $\tau_{wb\text{ web}} = \dfrac{V_u Q_w}{I_x t_w}$ (from Design Guide 9, Eq. 4.6) | $\tau_{wb\text{ web}} = \dfrac{V_a Q_w}{I_x t_w}$ (from Design Guide 9, Eq. 4.6) |
| $= \dfrac{(7.50 \text{ kips})(29.8 \text{ in.}^3)}{(272 \text{ in.}^4)(0.340 \text{ in.})}$ | $= \dfrac{(5.00 \text{ kips})(29.8 \text{ in.}^3)}{(272 \text{ in.}^4)(0.340 \text{ in.})}$ |
| $= 2.42 \text{ ksi}$ | $= 1.61 \text{ ksi}$ |

---

# H-27

| LRFD | ASD |
|------|-----|
| $\tau_{wb\text{ flange}} = \dfrac{V_u Q_f}{I_x t_f}$ (from Design Guide 9, Eq. 4.6) | $\tau_{wb\text{ flange}} = \dfrac{V_a Q_f}{I_x t_f}$ (from Design Guide 9, Eq. 4.6) |
| $= \dfrac{(7.50 \text{ kips})(12.8 \text{ in.}^3)}{(272 \text{ in.}^4)(0.560 \text{ in.})}$ | $= \dfrac{(5.00 \text{ kips})(12.8 \text{ in.}^3)}{(272 \text{ in.}^4)(0.560 \text{ in.})}$ |
| $= 0.630 \text{ ksi}$ | $= 0.420 \text{ ksi}$ |

**Torsional Stresses**

The following functions are taken from AISC Design Guide 9, Appendix B, Case 3, with $\alpha = 0.5$ for the torsional load applied at midspan.

$$\frac{L}{a} = \frac{(15 \text{ ft})(12 \text{ in./ft})}{62.1 \text{ in.}}$$

$$= 2.90$$

Using the graphs in AISC Design Guide 9, Appendix B, select values for $\theta$, $\theta'$, $\theta''$ and $\theta'''$.

At midspan ($z/l = 0.5$):

For $\theta$: $\theta \times \left(\dfrac{GJ}{T_r}\right)\left(\dfrac{1}{l}\right) = +0.09$ Solve for: $\theta = +0.09\dfrac{T_r l}{GJ}$

For $\theta'$: $\theta' \times \left(\dfrac{GJ}{T_r}\right) = 0$ Therefore: $\theta' = 0$

For $\theta''$: $\theta'' \times \left(\dfrac{GJ}{T_r}\right)a = -0.44$ Solve for: $\theta'' = -0.44\dfrac{T_r}{GJa}$

For $\theta'''$: $\theta''' \times \left(\dfrac{GJ}{T_r}\right)a^2 = -0.50$ Solve for: $\theta''' = -0.50\dfrac{T_r}{GJa^2}$

At the support ($z/l = 0$):

For $\theta$: $\theta \times \left(\dfrac{GJ}{T_r}\right)\left(\dfrac{1}{l}\right) = 0$ Therefore: $\theta = 0$

For $\theta'$: $\theta' \times \left(\dfrac{GJ}{T_r}\right) = +0.28$ Solve for: $\theta' = +0.28\dfrac{T_r}{GJ}$

For $\theta''$: $\theta'' \times \left(\dfrac{GJ}{T_r}\right)a = 0$ Therefore: $\theta'' = 0$

For $\theta'''$: $\theta''' \times \left(\dfrac{GJ}{T_r}\right)a^2 = -0.22$ Solve for: $\theta''' = -0.22\dfrac{T_r}{GJa^2}$

In the preceding calculations, note that the applied torque is negative based on the sign convention used in the AISC Design Guide 9 graphs.

Calculate $T_r/GJ$ as follows:

---

# H-28

| LRFD | ASD |
|------|-----|
| $\dfrac{T_u}{GJ} = \dfrac{-90.0 \text{ kip-in.}}{(11{,}200 \text{ ksi})(1.39 \text{ in.}^4)}$ | $\dfrac{T_a}{GJ} = \dfrac{-60.0 \text{ kip-in.}}{(11{,}200 \text{ ksi})(1.39 \text{ in.}^4)}$ |
| $= -5.78 \times 10^{-3} \text{ rad/in.}$ | $= -3.85 \times 10^{-3} \text{ rad/in.}$ |

**Shear Stresses Due to Pure Torsion**

The shear stresses due to pure torsion are determined from AISC Design Guide 9 as follows:

$$\tau_t = Gt\theta'$$
$$({\text{Design Guide 9, Eq. 4.1}})$$

| LRFD | ASD |
|------|-----|
| At midspan: | At midspan: |
| $\theta' = 0$; therefore $\tau_{st} = 0$ | $\theta' = 0$; therefore $\tau_{st} = 0$ |
| At the support, for the web: | At the support, for the web: |
| $\tau_{st} = (11{,}200 \text{ ksi})(0.340 \text{ in.})(0.28)\left(\dfrac{-5.78 \text{ rad}}{10^3 \text{ in.}}\right)$ | $\tau_{st} = (11{,}200 \text{ ksi})(0.340 \text{ in.})(0.28)\left(\dfrac{-3.85 \text{ rad}}{10^3 \text{ in.}}\right)$ |
| $= -6.16 \text{ ksi}$ | $= -4.11 \text{ ksi}$ |
| At the support, for the flange: | At the support, for the flange: |
| $\tau_{st} = (11{,}200 \text{ ksi})(0.560 \text{ in.})(0.28)\left(\dfrac{-5.78 \text{ rad}}{10^3 \text{ in.}}\right)$ | $\tau_{st} = (11{,}200 \text{ ksi})(0.560 \text{ in.})(0.28)\left(\dfrac{-3.85 \text{ rad}}{10^3 \text{ in.}}\right)$ |
| $= -10.2 \text{ ksi}$ | $= -6.76 \text{ ksi}$ |

**Shear Stresses Due to Warping**

The shear stresses due to warping are determined from AISC Design Guide 9 as follows:

$$\tau_w = \frac{-ES_{w1}\theta'''}{t_f}$$
$$({\text{Design Guide 9, Eq. 4.2a}})$$

| LRFD | ASD |
|------|-----|
| At midspan: | At midspan: |
| $\tau_{ww} = \dfrac{(-29{,}000 \text{ ksi})(33.0 \text{ in.}^4)}{0.560 \text{ in.}}\left[\dfrac{-0.50(-5.78 \text{ rad})}{(62.1 \text{ in.})^2 (10^3 \text{ in.})}\right]$ | $\tau_{ww} = \dfrac{(-29{,}000 \text{ ksi})(33.0 \text{ in.}^4)}{0.560 \text{ in.}}\left[\dfrac{-0.50(-3.85 \text{ rad})}{(62.1 \text{ in.})^2 (10^3 \text{ in.})}\right]$ |
| $= -1.28 \text{ ksi}$ | $= -0.853 \text{ ksi}$ |
| At the support: | At the support: |
| $\tau_{ww} = \dfrac{(-29{,}000 \text{ ksi})(33.0 \text{ in.}^4)}{0.560 \text{ in.}}\left[\dfrac{-0.22(-5.78 \text{ rad})}{(62.1 \text{ in.})^2 (10^3 \text{ in.})}\right]$ | $\tau_{ww} = \dfrac{(-29{,}000 \text{ ksi})(33.0 \text{ in.}^4)}{0.560 \text{ in.}}\left[\dfrac{-0.22(-3.85 \text{ rad})}{(62.1 \text{ in.})^2 (10^3 \text{ in.})}\right]$ |
| $= -0.563 \text{ ksi}$ | $= -0.375 \text{ ksi}$ |

**Normal Stresses Due to Warping**

---

# H-29

The normal stresses due to warping are determined from AISC Design Guide 9 as follows:

$$\sigma_w = EW_{no}\theta''$$
$$({\text{Design Guide 9, Eq. 4.3a}})$$

| LRFD | ASD |
|------|-----|
| At midspan: | At midspan: |
| $\sigma_{nw} = (29{,}000 \text{ ksi})(23.6 \text{ in.}^2)\left[\dfrac{-0.44(-5.78 \text{ rad})}{(62.1 \text{ in.})(10^3 \text{ in.})}\right]$ | $\sigma_{nw} = (29{,}000 \text{ ksi})(23.6 \text{ in.}^2)\left[\dfrac{-0.44(-3.85 \text{ rad})}{(62.1 \text{ in.})(10^3 \text{ in.})}\right]$ |
| $= 28.0 \text{ ksi}$ | $= 18.7 \text{ ksi}$ |
| At the support: | At the support: |
| Because $\theta'' = 0$, $\sigma_{nw} = 0$. | Because $\theta'' = 0$, $\sigma_{nw} = 0$. |

**Combined Stresses**

The stresses are summarized in Tables H.6-1A and H.6-1B and shown in Figure H.6-2.

<table>
<caption>Table H.6-1A. Summary of Stresses Due to Flexure and Torsion (LRFD), ksi</caption>
<thead>
<tr>
<th rowspan="2">Location</th>
<th colspan="3">Normal Stress</th>
<th colspan="4">Shear Stress</th>
</tr>
<tr>
<th>σ<sub>nw</sub></th>
<th>σ<sub>nb</sub></th>
<th>f<sub>nn</sub></th>
<th>τ<sub>st</sub></th>
<th>τ<sub>ww</sub></th>
<th>τ<sub>wb</sub></th>
<th>f<sub>nv</sub></th>
</tr>
</thead>
<tbody>
<tr>
<th colspan="8">Midspan</th>
</tr>
<tr>
<td>Flange</td>
<td>±28.0</td>
<td>±12.4</td>
<td>±40.4</td>
<td>0</td>
<td>−1.28</td>
<td>±0.630</td>
<td>−1.91</td>
</tr>
<tr>
<td>Web</td>
<td>−</td>
<td>−</td>
<td></td>
<td>0</td>
<td>−</td>
<td>±2.42</td>
<td>±2.42</td>
</tr>
<tr>
<th colspan="8">Support</th>
</tr>
<tr>
<td>Flange</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>−10.2</td>
<td>−0.563</td>
<td>±0.630</td>
<td>−11.4</td>
</tr>
<tr>
<td>Web</td>
<td>−</td>
<td>−</td>
<td>−</td>
<td>−6.16</td>
<td>−</td>
<td>±2.42</td>
<td>−8.58</td>
</tr>
<tr>
<td>Maximum</td>
<td></td>
<td></td>
<td>±40.4</td>
<td></td>
<td></td>
<td></td>
<td>−11.4</td>
</tr>
</tbody>
</table>

<table>
<caption>Table H.6-1B. Summary of Stresses Due to Flexure and Torsion (ASD), ksi</caption>
<thead>
<tr>
<th rowspan="2">Location</th>
<th colspan="3">Normal Stress</th>
<th colspan="4">Shear Stress</th>
</tr>
<tr>
<th>σ<sub>nw</sub></th>
<th>σ<sub>nb</sub></th>
<th>f<sub>nn</sub></th>
<th>τ<sub>st</sub></th>
<th>τ<sub>ww</sub></th>
<th>τ<sub>wb</sub></th>
<th>f<sub>nv</sub></th>
</tr>
</thead>
<tbody>
<tr>
<th colspan="8">Midspan</th>
</tr>
<tr>
<td>Flange</td>
<td>±18.7</td>
<td>±8.24</td>
<td>±26.9</td>
<td>0</td>
<td>−0.853</td>
<td>±0.420</td>
<td>−1.27</td>
</tr>
<tr>
<td>Web</td>
<td>−</td>
<td>−</td>
<td></td>
<td>0</td>
<td>−</td>
<td>±1.61</td>
<td>±1.61</td>
</tr>
<tr>
<th colspan="8">Support</th>
</tr>
<tr>
<td>Flange</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>−6.76</td>
<td>−0.375</td>
<td>±0.420</td>
<td>−7.56</td>
</tr>
<tr>
<td>Web</td>
<td>−</td>
<td>−</td>
<td>−</td>
<td>−4.11</td>
<td>−</td>
<td>±1.61</td>
<td>−5.72</td>
</tr>
<tr>
<td>Maximum</td>
<td></td>
<td></td>
<td>±26.9</td>
<td></td>
<td></td>
<td></td>
<td>−7.56</td>
</tr>
</tbody>
</table>

---

# H-30

![Diagrams showing normal and shear stresses due to flexure and torsion at midspan and support for both LRFD and ASD. Shows cross-sections with stress values labeled at various points on the I-beam, with arrows indicating torsional moments of Tu = 90.0 kip-in. for LRFD and Ta = 60.0 kip-in. for ASD]

*(a) Normal stresses due to flexure and torsion at midspan—LRFD*

*(b) Normal stresses due to flexure and torsion at midspan—ASD*

*(c) Shear stresses due to flexure and torsion at support—LRFD*

*(d) Shear stresses due to flexure and torsion at support—ASD*

*Fig. H.6-2. Stresses due to flexure and torsion.*

| LRFD | ASD |
|------|-----|
| The maximum normal stress due to flexure and torsion occurs at the edge of the flange at midspan and is equal to 40.4 ksi. | The maximum normal stress due to flexure and torsion occurs at the edge of the flange at midspan and is equal to 26.9 ksi. |
| The maximum shear stress due to flexure and torsion occurs in the middle of the flange at the support and is equal to 11.4 ksi. | The maximum shear stress due to flexure and torsion occurs in the middle of the flange at the support and is equal to 7.56 ksi. |

**Available Torsional Strength**

The available torsional strength is the lowest value determined for the limit states of yielding under normal stress, shear yielding under shear stress, or buckling in accordance with AISC *Specification* Section H3.3. The nominal torsional strength due to the limit states of yielding under normal stress and shear yielding under shear stress are compared to the applicable buckling limit states.

**Buckling**

For the buckling limit state, lateral-torsional buckling and local buckling must be evaluated. The nominal torsional strength due to the limit state of lateral-torsional buckling is determined as follows.

---

# H-31

$C_b = 1.32$ from AISC *Manual* Table 3-1.

Compute $F_n$ for a W10×49 using values from AISC *Manual* Table 6-1 with $L_b = 15 \text{ ft}$ and $C_b = 1.0$.

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 204 \text{ kip-ft}$ | $\dfrac{M_n}{\Omega_b} = 136 \text{ kip-ft}$ |
| $F_n = F_{cr}$ (*Spec.* Eq. H3-9) | $F_n = F_{cr}$ (*Spec.* Eq. H3-9) |
| $= C_b \left(\dfrac{M_n}{S_x}\right)$ | $= C_b \left(\dfrac{M_n}{S_x}\right)$ |
| $= 1.32\left[\dfrac{(204 \text{ kip-ft})(12 \text{ in./ft})}{0.90(54.6 \text{ in.}^3)}\right]$ | $= 1.32\left[\dfrac{167(136 \text{ kip-ft})(12 \text{ in./ft})}{(54.6 \text{ in.}^3)}\right]$ |
| $= 65.8 \text{ ksi}$ | $= 65.9 \text{ ksi}$ |

The limit state of local buckling does not apply because a W10×49 is compact in flexure per the user note in AISC *Specification* Section F2.

**Yielding Under Normal Stress**

The nominal torsional strength due to the limit state of yielding under normal stress is determined as follows:

$$F_n = F_y$$
$$\text{(Spec. Eq. H3-7)}$$

$$= 50 \text{ ksi}$$

Therefore, the limit state of yielding under normal stress controls over buckling. The available torsional strength for yielding under normal stress is determined as follows, from AISC *Specification* Section H3:

| LRFD | ASD |
|------|-----|
| $\phi_T = 0.90$ | $\Omega_T = 1.67$ |
| $\phi_T F_n = 0.90(50 \text{ ksi})$ | $\dfrac{F_n}{\Omega_T} = \dfrac{50 \text{ ksi}}{1.67}$ |
| $= 45.0 \text{ ksi} > 40.4 \text{ ksi}$ **o.k.** | $= 29.9 \text{ ksi} > 26.9 \text{ ksi}$ **o.k.** |

**Shear Yielding Under Shear Stress**

The nominal torsional strength due to the limit state of shear yielding under shear stress is:

$$F_n = 0.6F_y$$
$$\text{(Spec. Eq. H3-8)}$$

$$= 0.6(50 \text{ ksi})$$

$$= 30.0 \text{ ksi}$$

The limit state of shear yielding under shear stress controls over buckling. The available torsional strength for shear yielding under shear stress is determined as follows, from AISC *Specification* Section H3:

---

# H-32

| LRFD | ASD |
|------|-----|
| $\phi_T = 0.90$ | $\Omega_T = 1.67$ |
| $\phi_T F_n = 0.90(30 \text{ ksi})$ | $\dfrac{F_n}{\Omega_T} = \dfrac{30 \text{ ksi}}{1.67}$ |
| $= 27.0 \text{ ksi} > 11.4 \text{ ksi}$ **o.k.** | $= 18.0 \text{ ksi} > 7.56 \text{ ksi}$ **o.k.** |

**Maximum Rotation at Service Load**

The maximum rotation occurs at midspan. The service load torque is:

$$T = Pe$$

$$= -(2.50 \text{ kips} + 7.50 \text{ kips})(6 \text{ in.})$$

$$= -60.0 \text{ kip-in.}$$

As determined previously from AISC Design Guide 9, Appendix B, Case 3 with $\alpha = 0.5$, the maximum rotation is:

$$\theta = +0.09\frac{Tl}{GJ}$$

$$= \frac{0.09(-60.0 \text{ kip-in.})(15 \text{ ft})(12 \text{ in./ft})}{(11{,}200 \text{ ksi})(1.39 \text{ in.}^4)}$$

$$= -0.0624 \text{ rad or } -3.58°$$

See AISC Design Guide 9, *Torsional Analysis of Structural Steel Members*, for additional guidance.

---

# H-33

## CHAPTER H DESIGN EXAMPLE REFERENCES

Seaburg, P.A. and Carter, C.J. (1997), *Torsional Analysis of Structural Steel Members*, Design Guide 9, AISC, Chicago, Ill.

---

# H-34

---
