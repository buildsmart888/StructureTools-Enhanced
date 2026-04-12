# Chapter G: Shear

**AISC Specification v16.0 - Design Examples**
**Original PDF Pages**: 237-262 (26 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Design of Members for Shear

**Examples Included**: ['G.1A~G.8B: Shear design examples']

---

## Table of Contents

- [EXAMPLE G.1A W-SHAPE IN MAJOR-AXIS SHEAR](#example-g1a-w-shape-in-major-axis-shear)
- [EXAMPLE G.1B W-SHAPE IN MAJOR-AXIS SHEAR](#example-g1b-w-shape-in-major-axis-shear)
- [EXAMPLE G.2A CHANNEL IN MAJOR-AXIS SHEAR](#example-g2a-channel-in-major-axis-shear)
- [EXAMPLE G.2B CHANNEL IN MAJOR-AXIS SHEAR](#example-g2b-channel-in-major-axis-shear)
- [EXAMPLE G.3 ANGLE IN SHEAR](#example-g3-angle-in-shear)
- [EXAMPLE G.4 RECTANGULAR HSS IN SHEAR](#example-g4-rectangular-hss-in-shear)
- [EXAMPLE G.5 ROUND HSS IN SHEAR](#example-g5-round-hss-in-shear)
- [EXAMPLE G.6 DOUBLY SYMMETRIC SHAPE IN MINOR-AXIS SHEAR](#example-g6-doubly-symmetric-shape-in-minor-axis-shear)
- [EXAMPLE G.7 SINGLY SYMMETRIC SHAPE IN MINOR-AXIS SHEAR](#example-g7-singly-symmetric-shape-in-minor-axis-shear)
- [EXAMPLE G.8A BUILT-UP GIRDER WITH TRANSVERSE STIFFENERS](#example-g8a-built-up-girder-with-transverse-stiffeners)
- [EXAMPLE G.8B BUILT-UP GIRDER WITH TRANSVERSE STIFFENERS](#example-g8b-built-up-girder-with-transverse-stiffeners)

---

# G-1

# Chapter G
# Design of Members for Shear

## INTRODUCTION

This *Specification* chapter addresses webs of singly or doubly symmetric members subjected to shear in the plane of the web, single angles and HSS subjected to shear, and shear in the weak direction of singly or doubly symmetric shapes.

## G1. GENERAL PROVISIONS

The design shear strength, $\phi_v V_n$, and the allowable shear strength, $V_n/\Omega_v$, are determined as follows:

$V_n =$ nominal shear strength based on shear yielding or shear buckling
$\phi_v = 0.90$ (LRFD)
$\Omega_v = 1.67$ (ASD)

Exception: For all current ASTM A6/A6M, W-, S-, and HP-shapes except W44×230, W40×149, W36×135, W33×118, W30×90, W24×55, W16×26, and W12×14 for $F_y = 50$ ksi:

$\phi_v = 1.00$ (LRFD)
$\Omega_v = 1.50$ (ASD)

Major-axis shear values are tabulated for W-shapes in AISC *Manual* Tables 3-2, 3-6, and 6-1, for S-shapes in AISC *Manual* Table 3-7, for C-shapes in AISC *Manual* Table 3-8, and for MC-shapes in AISC *Manual* Table 3-9. Major- and minor-axis shear values for rectangular HSS are tabulated in AISC *Manual* Table 3-12. The shear values for square HSS are tabulated in AISC *Manual* Table 3-13. The shear values for round HSS and pipe are tabulated in the *Companion to the AISC Steel Construction Manual, Volume 2: Design Tables* (AISC, 2023). Minor-axis shear values for W-shapes, S-shapes, C-shapes, and MC-shapes, and shear values for angles and box members are not tabulated.

## G2. I-SHAPED MEMBERS AND CHANNELS

This section includes provisions for shear strength of webs without the use of tension field action, for interior web panels considering tension field action, and for web panels not permitting tension field action. Provisions for the design of transverse stiffeners are also included in Section G2.

As indicated in the User Note of this section, virtually all W-, S-, and HP-shapes are not subject to shear buckling and are also eligible for the more liberal safety and resistance factors, $\phi_v = 1.00$ (LRFD) and $\Omega_v = 1.50$ (ASD). This is presented in Examples G.1A and G.1B for a W-shape. Channel shear strength design is presented in Examples G.2A and G.2B. A built-up girder with a thin web and transverse stiffeners is presented in Examples G.8A and G.8B.

## G3. SINGLE ANGLES AND TEES

A single angle example is illustrated in Example G.3.

---

# G-2

## G4. RECTANGULAR HSS, BOX SECTIONS, AND OTHER SINGLY AND DOUBLY SYMMETRIC MEMBERS

The shear height for HSS, $h$, is taken as the clear distance between the flanges less the inside corner radius on each side. If the corner radii are unknown, $h$ shall be taken as the corresponding outside dimension minus 3 times the design wall thickness. A rectangular HSS example is provided in Example G.4.

## G5. ROUND HSS

For all round HSS of ordinary length listed in the AISC *Manual*, $F_{cr}$ can be taken as $0.6F_y$ in AISC *Specification* Equation G5-1. A round HSS example is illustrated in Example G.5.

## G6. DOUBLY SYMMETRIC AND SINGLY SYMMETRIC MEMBERS SUBJECTED TO MINOR-AXIS SHEAR

For examples of minor-axis shear, see Example G.6 and Example G.7.

## G7. BEAMS AND GIRDERS WITH WEB OPENINGS

For a beam and girder with web openings example, see AISC Design Guide 2, *Design of Steel and Composite Beams with Web Openings* (Darwin, 1990).

---

# G-3

## EXAMPLE G.1A W-SHAPE IN MAJOR-AXIS SHEAR

### Given:

Using AISC *Manual* tables, determine the available shear strength and adequacy of an ASTM A992/A992M W24×62 with end shears of 48 kips from dead load and 145 kips from live load.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From Chapter 2 of ASCE/SEI 7, the required shear strength is:

| LRFD | ASD |
|------|-----|
| $V_u = 1.2(48 \text{ kips}) + 1.6(145 \text{ kips})$ | $V_a = 48 \text{ kips} + 145 \text{ kips}$ |
| $= 290 \text{ kips}$ | $= 193 \text{ kips}$ |

From AISC *Manual* Table 3-2, the available shear strength is:

| LRFD | ASD |
|------|-----|
| $\phi_v V_{nx} = 306 \text{ kips} > 290 \text{ kips}$ **o.k.** | $\dfrac{V_{nx}}{\Omega_v} = 204 \text{ kips} > 193 \text{ kips}$ **o.k.** |

---

# G-4

## EXAMPLE G.1B W-SHAPE IN MAJOR-AXIS SHEAR

### Given:

The available shear strength of the W-shape in Example G.1A was easily determined using tabulated values in the AISC *Manual*. This example demonstrates the calculation of the available strength by directly applying the provisions of the AISC *Specification*.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-1, the geometric properties are as follows:

W24×62
$d = 23.7 \text{ in.}$
$t_w = 0.430 \text{ in.}$

**Nominal Shear Strength**

Except for very few sections, which are listed in the User Note, AISC *Specification* Section G2.1(a) is applicable to the I-shaped beams published in the AISC *Manual* for $F_y = 50$ ksi. The W-shape sections that do not meet the criteria of AISC *Specification* Section G2.1(a) are indicated with footnote "[v]" in Tables 1-1, 3-2, and 6-1.

$$C_{v1} = 1.0$$
$$\text{(Spec. Eq. G2-2)}$$

From AISC *Specification* Section G2.1, area of the web, $A_w$, is determined as follows:

$$A_w = dt_w$$

$$= (23.7 \text{ in.})(0.430 \text{ in.})$$

$$= 10.2 \text{ in.}^2$$

From AISC *Specification* Section G2.1, the nominal shear strength is:

$$V_n = 0.6F_y A_w C_{v1}$$
$$\text{(Spec. Eq. G2-1)}$$

$$= 0.6(50 \text{ ksi})(10.2 \text{ in.}^2)(1.0)$$

$$= 306 \text{ kips}$$

**Available Shear Strength**

From AISC *Specification* Section G2.1, the available shear strength is:

| LRFD | ASD |
|------|-----|
| $\phi_v = 1.00$ | $\Omega_v = 1.50$ |
| $\phi_v V_n = 1.00(306 \text{ kips})$ | $\dfrac{V_n}{\Omega_v} = \dfrac{306 \text{ kips}}{1.50}$ |
| $= 306 \text{ kips}$ | $= 204 \text{ kips}$ |

---

# G-5

## EXAMPLE G.2A CHANNEL IN MAJOR-AXIS SHEAR

### Given:

Using AISC *Manual* tables, verify the available shear strength and adequacy of an ASTM A992/A992M C15×33.9 channel with end shears of 25 kips from dead load and 75 kips from live load.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From Chapter 2 of ASCE/SEI 7, the required shear strength is:

| LRFD | ASD |
|------|-----|
| $V_u = 1.2(25 \text{ kips}) + 1.6(75 \text{ kips})$ | $V_a = 25 \text{ kips} + 75 \text{ kips}$ |
| $= 150 \text{ kips}$ | $= 100 \text{ kips}$ |

From AISC *Manual* Table 3-8, the available shear strength is:

| LRFD | ASD |
|------|-----|
| $\phi_v V_n = 162 \text{ kips} > 150 \text{ kips}$ **o.k.** | $\dfrac{V_n}{\Omega_v} = 108 \text{ kips} > 100 \text{ kips}$ **o.k.** |

---

# G-6

## EXAMPLE G.2B CHANNEL IN MAJOR-AXIS SHEAR

### Given:

The available shear strength of the channel in Example G.2A was easily determined using tabulated values in the AISC *Manual*. This example demonstrates the calculation of the available strength by directly applying the provisions of the AISC *Specification*.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-5, the geometric properties are as follows:

C15×33.9
$d = 15.0 \text{ in.}$
$t_w = 0.400 \text{ in.}$

**Nominal Shear Strength**

All ASTM A992/A992M channels listed in the AISC *Manual* have $h/t_w \leq 1.10\sqrt{k_v E/F_y}$; therefore,

$$C_{v1} = 1.0$$
$$\text{(Spec. Eq. G2-3)}$$

From AISC *Specification* Section G2.1, the area of the web, $A_w$, is determined as follows:

$$A_w = dt_w$$

$$= (15.0 \text{ in.})(0.400 \text{ in.})$$

$$= 6.00 \text{ in.}^2$$

From AISC *Specification* Section G2.1, the nominal shear strength is:

$$V_n = 0.6F_y A_w C_{v1}$$
$$\text{(Spec. Eq. G2-1)}$$

$$= 0.6(50 \text{ ksi})(6.00 \text{ in.}^2)(1.0)$$

$$= 180 \text{ kips}$$

**Available Shear Strength**

Because AISC *Specification* Section G2.1(a) does not apply for channels, the values of $\phi_v = 1.00$ (LRFD) and $\Omega_v = 1.50$ (ASD) may not be used. Instead $\phi_v = 0.90$ (LRFD) and $\Omega_v = 1.67$ (ASD) from AISC *Specification* Section G1(a) must be used.

| LRFD | ASD |
|------|-----|
| $\phi_v = 0.90$ | $\Omega_v = 1.67$ |
| $\phi_v V_n = 0.90(180 \text{ kips})$ | $\dfrac{V_n}{\Omega_v} = \dfrac{180 \text{ kips}}{1.67}$ |
| $= 162 \text{ kips}$ | $= 108 \text{ kips}$ |

---

# G-7

## EXAMPLE G.3 ANGLE IN SHEAR

### Given:

Determine the available shear strength and adequacy of an ASTM A572/A572 Grade 50 L5×3×¼ (long leg vertical) with end shears of 5 kips from dead load and 15 kips from live load.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-7, the geometric properties are as follows:

L5×3×¼
$b = 5.00 \text{ in.}$
$t = \frac{1}{4} \text{ in.}$

From Chapter 2 of ASCE/SEI 7, the required shear strength is:

| LRFD | ASD |
|------|-----|
| $V_u = 1.2(5 \text{ kips}) + 1.6(15 \text{ kips})$ | $V_a = 5 \text{ kips} + 15 \text{ kips}$ |
| $= 30.0 \text{ kips}$ | $= 20.0 \text{ kips}$ |

**Nominal Shear Strength**

Note: There are no tables in the AISC *Manual* for angles in shear, but the nominal shear strength can be calculated according to AISC *Specification* Section G3, as follows:

From AISC *Specification* Section G3:

$$k_v = 1.2$$

Determine $C_{v2}$ from AISC *Specification* Section G2.2.

$$\frac{h}{t_w} = \frac{b}{t}$$

$$= \frac{5.00 \text{ in.}}{\frac{1}{4} \text{ in.}}$$

$$= 20.0$$

$$1.10\sqrt{\frac{k_v E}{F_y}} = 1.10\sqrt{\frac{1.2(29,000 \text{ ksi})}{50 \text{ ksi}}}$$

$$= 29.0 > 20.0$$

Therefore, use AISC *Specification* Equation G2-9:

$$C_{v2} = 1.0$$
$$\text{(Spec. Eq. G2-9)}$$

---

# G-8

From AISC *Specification* Section G3, the nominal shear strength is:

$$V_n = 0.6F_y btC_{v2}$$
$$\text{(Spec. Eq. G3-1)}$$

$$= 0.6(50 \text{ ksi})(5.00 \text{ in.})(\frac{1}{4} \text{ in.})(1.0)$$

$$= 37.5 \text{ kips}$$

**Available Shear Strength**

From AISC *Specification* Section G1, the available shear strength is:

| LRFD | ASD |
|------|-----|
| $\phi_v = 0.90$ | $\Omega_v = 1.67$ |
| $\phi_v V_n = 0.90(37.5 \text{ kips})$ | $\dfrac{V_n}{\Omega_v} = \dfrac{37.5 \text{ kips}}{1.67}$ |
| $= 33.8 \text{ kips} > 30.0 \text{ kips}$ **o.k.** | $= 22.5 \text{ kips} > 20.0 \text{ kips}$ **o.k.** |

---

# G-9

## EXAMPLE G.4 RECTANGULAR HSS IN SHEAR

### Given:

Determine the available shear strength by directly applying the provisions of the AISC *Specification* for an ASTM A500/A500M Grade C HSS6×4×⅜ (wide walls vertical) beam with end shears of 11 kips from dead load and 33 kips from live load.

Note: There are tables in AISC *Manual* Part 3 and the *Companion to the AISC Steel Construction Manual, Volume 2: Design Tables* (AISC, 2023) that provide the shear strength of rectangular and square HSS shapes.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A500/A500M Grade C, rectangular
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-11, the geometric properties are as follows:

HSS6×4×⅜
$H = 6.00 \text{ in.}$
$B = 4.00 \text{ in.}$
$t = 0.349 \text{ in.}$

From Chapter 2 of ASCE/SEI 7, the required shear strength is:

| LRFD | ASD |
|------|-----|
| $V_u = 1.2(11 \text{ kips}) + 1.6(33 \text{ kips})$ | $V_a = 11 \text{ kips} + 33 \text{ kips}$ |
| $= 66.0 \text{ kips}$ | $= 44.0 \text{ kips}$ |

**Nominal Shear Strength**

The nominal shear strength can be determined from AISC *Specification* Section G4 as follows:

The web shear buckling strength coefficient, $C_{v2}$, is found using AISC *Specification* Section G2.2 with $h/t_w = h/t$ and $k_v = 5$.

From AISC *Specification* Section G4, if the exact radius is unknown, $h$ shall be taken as the corresponding outside dimension minus three times the design thickness.

$$h = H - 3t$$
$$= 6.00 \text{ in.} - 3(0.349 \text{ in.})$$
$$= 4.95 \text{ in.}$$

$$\frac{h}{t} = \frac{4.95 \text{ in.}}{0.349 \text{ in.}}$$
$$= 14.2$$

Note, $h/t$ is also tabulated in AISC *Manual* Table 1-11.

---

# G-10

$$1.10\sqrt{\frac{k_v E}{F_y}} = 1.10\sqrt{\frac{5(29,000 \text{ ksi})}{50 \text{ ksi}}}$$

$$= 59.2 > 14.2$$

Therefore, use AISC *Specification* Equation G2-9:

$$C_{v2} = 1.0$$
$$\text{(Spec. Eq. G2-9)}$$

Note: Most standard HSS sections listed in the AISC *Manual* have $C_{v2} = 1.0$ at $F_y \leq 50$ ksi.

Calculate $A_w$.

$$A_w = 2ht$$

$$= 2(4.95 \text{ in.})(0.349 \text{ in.})$$

$$= 3.46 \text{ in.}^2$$

Calculate $V_n$.

$$V_n = 0.6F_y A_w C_{v2}$$
$$\text{(Spec. Eq. G4-1)}$$

$$= 0.6(50 \text{ ksi})(3.46 \text{ in.}^2)(1.0)$$

$$= 104 \text{ kips}$$

**Available Shear Strength**

From AISC *Specification* Section G1, the available shear strength is:

| LRFD | ASD |
|------|-----|
| $\phi_v = 0.90$ | $\Omega_v = 1.67$ |
| $\phi_v V_n = 0.90(104 \text{ kips})$ | $\dfrac{V_n}{\Omega_v} = \dfrac{104 \text{ kips}}{1.67}$ |
| $= 93.6 \text{ kips} > 66.0 \text{ kips}$ **o.k.** | $= 62.3 \text{ kips} > 44.0 \text{ kips}$ **o.k.** |

Note: the values calculated above do not precisely match the values tabulated in AISC *Manual* Table 3-12 due to rounding.

---

# G-11

## EXAMPLE G.5 ROUND HSS IN SHEAR

### Given:

Determine the available shear strength by directly applying the provisions of the AISC *Specification* for an ASTM A500/A500M Grade C round HSS16.000×0.375 beam spanning 32 ft with end shears of 30 kips from uniform dead load and 90 kips from uniform live load.

Note: There are tables in the *Companion to the AISC Steel Construction Manual, Volume 2: Design Tables* (AISC, 2023) that provide the shear strength of ASTM A500/A500M Grade C round HSS shapes.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A500/A500M Grade C, round HSS
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-13, the geometric properties are as follows:

HSS16.000×0.375
$A_g = 17.2 \text{ in.}^2$
$\dfrac{D}{t} = 45.8$

From Chapter 2 of ASCE/SEI 7, the required shear strength is:

| LRFD | ASD |
|------|-----|
| $V_u = 1.2(30 \text{ kips}) + 1.6(90 \text{ kips})$ | $V_a = 30 \text{ kips} + 90 \text{ kips}$ |
| $= 180 \text{ kips}$ | $= 120 \text{ kips}$ |

**Nominal Shear Strength**

The nominal strength can be determined from AISC *Specification* Section G5, as follows:

Using AISC *Specification* Section G5, calculate $F_{cr}$ as the larger of:

$$F_{cr} = \frac{1.60E}{\sqrt{\dfrac{L_v}{D}\left(\dfrac{D}{t}\right)^4}}$$
$$\text{(Spec. Eq. G5-2a)}$$

and

$$F_{cr} = \frac{0.78E}{\left(\dfrac{D}{t}\right)^3}$$ , but not to exceed $0.6F_y$
$$\text{(Spec. Eq. G5-2b)}$$

where $L_v$ is taken as the distance from maximum shear force to zero; in this example, half the span.

$$L_v = 0.5(32 \text{ ft})(12 \text{ in./ft})$$
$$= 192 \text{ in.}$$

---

# G-12

$$F_{cr} = \frac{1.60E}{\sqrt{\dfrac{L_v}{D}\left(\dfrac{D}{t}\right)^4}}$$
$$\text{(Spec. Eq. G5-2a)}$$

$$= \frac{1.60(29,000 \text{ ksi})}{\sqrt{\dfrac{192 \text{ in.}}{16.0 \text{ in.}}(45.8)^{5/4}}}$$

$$= 112 \text{ ksi}$$

$$F_{cr} = \frac{0.78E}{\left(\dfrac{D}{t}\right)^3}$$
$$\text{(Spec. Eq. G5-2b)}$$

$$= \frac{0.78(29,000 \text{ ksi})}{(45.8)^{3/2}}$$

$$= 73.0 \text{ ksi}$$

The maximum value of $F_{cr}$ permitted is,

$$F_{cr} = 0.6F_y$$

$$= 0.6(50 \text{ ksi})$$

$$= 30.0 \text{ ksi}$$ **controls**

Note: AISC *Specification* Equations G5-2a and G5-2b will not normally control for the sections published in the AISC *Manual* except when high strength steel is used or the span is unusually long.

Calculate $V_n$ using AISC *Specification* Section G5.

$$V_n = \frac{F_{cr}A_g}{2}$$
$$\text{(Spec. Eq. G5-1)}$$

$$= \frac{(30.0 \text{ ksi})(17.2 \text{ in.}^2)}{2}$$

$$= 258 \text{ kips}$$

**Available Shear Strength**

From AISC *Specification* Section G1, the available shear strength is:

| LRFD | ASD |
|------|-----|
| $\phi_v = 0.90$ | $\Omega_v = 1.67$ |
| $\phi_v V_n = 0.90(258 \text{ kips})$ | $\dfrac{V_n}{\Omega_v} = \dfrac{258 \text{ kips}}{1.67}$ |
| $= 232 \text{ kips} > 180 \text{ kips}$ **o.k.** | $= 155 \text{ kips} > 120 \text{ kips}$ **o.k.** |

---

# G-13

## EXAMPLE G.6 DOUBLY SYMMETRIC SHAPE IN MINOR-AXIS SHEAR

### Given:

Verify the available shear strength and adequacy of an ASTM A992/A992M W21×48 beam with end shears of 20.0 kips from dead load and 60.0 kips from live load in the weak direction.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-1, the geometric properties are as follows:

W21×48
$b_f = 8.14 \text{ in.}$
$t_f = 0.430 \text{ in.}$

From Chapter 2 of ASCE/SEI 7, the required shear strength is:

| LRFD | ASD |
|------|-----|
| $V_u = 1.2(20.0 \text{ kips}) + 1.6(60.0 \text{ kips})$ | $V_a = 20.0 \text{ kips} + 60.0 \text{ kips}$ |
| $= 120 \text{ kips}$ | $= 80.0 \text{ kips}$ |

**Nominal Shear Strength**

From AISC *Specification* Section G6, for minor axis shear, use AISC *Specification* Equation G6-1.

Calculate $C_{v2}$ using AISC *Specification* Section G2.2 with $h/t_w = b_f/2t_f$ and $k_v = 1.2$.

$$\frac{h}{t_w} = \frac{b_f}{2t_f}$$

$$= \frac{8.14 \text{ in.}}{2(0.430 \text{ in.})}$$

$$= 9.47$$

$$1.10\sqrt{\frac{k_v E}{F_y}} = 1.10\sqrt{\frac{1.2(29,000 \text{ ksi})}{50 \text{ ksi}}}$$

$$= 29.0 > 9.47$$

Therefore, use AISC *Specification* Equation G2-9:

$$C_{v2} = 1.0$$
$$\text{(Spec. Eq. G2-9)}$$

Note: From the User Note in AISC *Specification* Section G6, $C_{v2} = 1.0$ for all ASTM A6/A6M W-, S-, M-, and HP-shapes when $F_y \leq 70$ ksi.

Calculate $V_n$ using AISC *Specification* Section G6, multiplying the flange area by two to account for both shear resisting elements:

---

# G-14

$$V_n = 0.6F_y b_f t_f C_{v2}(2)$$
$$\text{(from Spec. Eq. G6-1)}$$

$$= 0.6(50 \text{ ksi})(8.14 \text{ in.})(0.430 \text{ in.})(1.0)(2)$$

$$= 210 \text{ kips}$$

**Available Shear Strength**

From AISC *Specification* Section G1, the available shear strength is:

| LRFD | ASD |
|------|-----|
| $\phi_v = 0.90$ | $\Omega_v = 1.67$ |
| $\phi_v V_n = 0.90(210 \text{ kips})$ | $\dfrac{V_n}{\Omega_v} = \dfrac{210 \text{ kips}}{1.67}$ |
| $= 189 \text{ kips} > 120 \text{ kips}$ **o.k.** | $= 126 \text{ kips} > 80.0 \text{ kips}$ **o.k.** |

---

# G-15

## EXAMPLE G.7 SINGLY SYMMETRIC SHAPE IN MINOR-AXIS SHEAR

### Given:

Verify the available shear strength and adequacy of an ASTM A992/A992M C9×20 channel with end shears of 7.5 kips from dead load and 22.5 kips from live load in the weak direction.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-5, the geometric properties are as follows:

C9×20
$b_f = 2.65 \text{ in.}$
$t_f = 0.413 \text{ in.}$

From Chapter 2 of ASCE/SEI 7, the required shear strength is:

| LRFD | ASD |
|------|-----|
| $V_u = 1.2(7.5 \text{ kips}) + 1.6(22.5 \text{ kips})$ | $V_a = 7.5 \text{ kips} + 22.5 \text{ kips}$ |
| $= 45.0 \text{ kips}$ | $= 30.0 \text{ kips}$ |

**Nominal Shear Strength**

Note: There are no AISC *Manual* tables for minor-axis shear in channel sections, but the available strength can be determined from AISC *Specification* Section G6.

Calculate $C_{v2}$ using AISC *Specification* Section G2.2 with $h/t_w = b_f/t_f$ and $k_v = 1.2$.

$$\frac{h}{t_w} = \frac{b_f}{t_f}$$

$$= \frac{2.65 \text{ in.}}{0.413 \text{ in.}}$$

$$= 6.42$$

$$1.10\sqrt{\frac{k_v E}{F_y}} = 1.10\sqrt{\frac{1.2(29,000 \text{ ksi})}{50 \text{ ksi}}}$$

$$= 29.0 > 6.42$$

Therefore, use AISC *Specification* Equation G2-9:

$$C_{v2} = 1.0$$
$$\text{(Spec. Eq. G2-9)}$$

Calculate $V_n$ using AISC *Specification* Section G6, multiplying the flange area by two to account for both shear resisting elements:

---

# G-16

$$V_n = 0.6F_y b_f t_f C_{v2}(2)$$
$$\text{(from Spec. Eq. G6-1)}$$

$$= 0.6(50 \text{ ksi})(2.65 \text{ in.})(0.413 \text{ in.})(1.0)(2)$$

$$= 65.7 \text{ kips}$$

**Available Shear Strength**

From AISC *Specification* Section G1, the available shear strength is:

| LRFD | ASD |
|------|-----|
| $\phi_v = 0.90$ | $\Omega_v = 1.67$ |
| $\phi_v V_n = 0.90(65.7 \text{ kips})$ | $\dfrac{V_n}{\Omega_v} = \dfrac{65.7 \text{ kips}}{1.67}$ |
| $= 59.1 \text{ kips} > 45.0 \text{ kips}$ **o.k.** | $= 39.3 \text{ kips} > 30.0 \text{ kips}$ **o.k.** |

---

# G-17

## EXAMPLE G.8A BUILT-UP GIRDER WITH TRANSVERSE STIFFENERS

### Given:

Determine the available shear strength of a built-up I-shaped girder for the span and loading as shown in Figure G.8A. The girder is ASTM A572/A572M Grade 50 material and is 36 in. deep with PL1½ in. × 16 in. flanges and a ⅜-in.-thick web. The compression flange is continuously braced. Determine if the member has sufficient available shear strength to support the end shear, without and with tension field action. Use transverse stiffeners, as required.

Note: This built-up girder was purposely selected with a thin web in order to illustrate the design of transverse stiffeners. A more conventionally proportioned plate girder may have at least a ½-in.-thick web and slightly smaller flanges.

$$w_D = 1.25 \text{ kip/ft}$$
$$w_L = 3.75 \text{ kip/ft}$$

![Beam loading and bracing diagram showing a simply supported beam with continuously braced top flange, span length L = 56'-0"]

*Fig. G.8A. Beam loading and bracing diagram.*

### Solution:

From AISC *Manual* Table 2-5, the material properties are as follows:

ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$

The geometric properties are as follows:

Built-up girder
$t_w = \frac{3}{16} \text{ in.}$
$d = 36.0 \text{ in.}$
$b_f = b_{fc} = 16.0 \text{ in.}$
$t_f = 1\frac{1}{2} \text{ in.}$
$h = 33.0 \text{ in.}$

From Chapter 2 of ASCE/SEI 7, the required shear strength at the support is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(1.25 \text{ kip/ft}) + 1.6(3.75 \text{ kip/ft})$ | $w_a = 1.25 \text{ kip/ft} + 3.75 \text{ kip/ft}$ |
| $= 7.50 \text{ kip/ft}$ | $= 5.00 \text{ kip/ft}$ |
| $V_u = \dfrac{w_u L}{2}$ | $V_a = \dfrac{w_a L}{2}$ |
| $= \dfrac{(7.50 \text{ kip/ft})(56 \text{ ft})}{2}$ | $= \dfrac{(5.00 \text{ kip/ft})(56 \text{ ft})}{2}$ |
| $= 210 \text{ kips}$ | $= 140 \text{ kips}$ |

---

# G-18

**Stiffener Requirement Check**

From AISC *Specification* Section G2.1:

$$A_w = dt_w$$

$$= (36.0 \text{ in.})(\frac{3}{16} \text{ in.})$$

$$= 11.3 \text{ in.}^2$$

For webs without transverse stiffeners, $k_v = 5.34$ from AISC *Specification* Section G2.1(b)(2)(i).

$$\frac{h}{t_w} = \frac{33.0 \text{ in.}}{\frac{3}{16} \text{ in.}}$$

$$= 106$$

$$1.10\sqrt{\frac{k_v E}{F_y}} = 1.10\sqrt{\frac{(5.34)(29,000 \text{ ksi})}{50 \text{ ksi}}}$$

$$= 61.2 < 106$$

Therefore, use AISC *Specification* Equation G2-4:

$$C_{v1} = \frac{1.10\sqrt{k_v E/F_y}}{h/t_w}$$
$$\text{(Spec. Eq. G2-4)}$$

$$= \frac{61.2}{106}$$

$$= 0.577$$

Calculate $V_n$ using AISC *Specification* Section G2.1:

$$V_n = 0.6F_y A_w C_{v1}$$
$$\text{(Spec. Eq. G2-1)}$$

$$= 0.6(50 \text{ ksi})(11.3 \text{ in.}^2)(0.577)$$

$$= 196 \text{ kips}$$

From AISC *Specification* Section G1, the available shear strength without stiffeners is:

| LRFD | ASD |
|------|-----|
| $\phi_v = 0.90$ | $\Omega_v = 1.67$ |
| $\phi_v V_n = 0.90(196 \text{ kips})$ | $\dfrac{V_n}{\Omega_v} = \dfrac{196 \text{ kips}}{1.67}$ |
| $= 176 \text{ kips} < 210 \text{ kips}$ **n.g.** | $= 117 \text{ kips} < 140 \text{ kips}$ **n.g.** |
| **Therefore, stiffeners are required.** | **Therefore, stiffeners are required.** |

AISC *Manual* Tables 3-16a and 3-16b can be used to select the stiffener spacing needed to develop the required stress in the web.

---

# G-19

**Stiffener Spacing for End Panel**

AISC *Specification* Section G2.3 permits the use of tension field action in end panels; however, it is not incorporated in the AISC *Manual* Tables. Conservatively, tension field action is not considered at the end panel in this example, therefore use AISC *Manual* Table 3-16a.

| LRFD | ASD |
|------|-----|
| Use $V_u = \phi_v V_n$ to determine the required stress in the web by dividing by the web area. | Use $V_a = V_n/\Omega_v$ to determine the required stress in the web by dividing by the web area. |
| $\dfrac{\phi_v V_n}{A_w} = \dfrac{V_u}{A_w}$ | $\dfrac{V_n}{\Omega_v A_w} = \dfrac{V_a}{A_w}$ |
| $= \dfrac{210 \text{ kips}}{11.3 \text{ in.}^2}$ | $= \dfrac{140 \text{ kips}}{11.3 \text{ in.}^2}$ |
| $= 18.6 \text{ ksi}$ | $= 12.4 \text{ ksi}$ |

Use Table 3-16a from the AISC *Manual* to select the required stiffener ratio $a/h$ based on the $h/t_w$ ratio of the girder and the required stress. Interpolate and follow an available stress curve, $\phi_v V_n/A_w = 18.6 \text{ ksi}$ for LRFD, $V_n/\Omega_v A_w = 12.4 \text{ ksi}$ for ASD, until it intersects the horizontal line for an $h/t_w$ value of 106. Project down from this intersection and approximate the value for $a/h$ as 1.35 from the axis across the bottom. Because $h = 33.0 \text{ in.}$, stiffeners are required at $(1.35)(33.0 \text{ in.}) = 44.6 \text{ in.}$ maximum. Conservatively, use a 42 in. spacing.

**Stiffener Spacing for the Second Panel**

From AISC *Specification* Section G2.2, tension field action is allowed in the second panel. However, a web panel aspect ratio, $a/h$, must not exceed three. The required shear strength at the start of the second panel, 42 in. from the end, is:

| LRFD | ASD |
|------|-----|
| $V_u = 210 \text{ kips} - (7.50 \text{ kip/ft})(42.0 \text{ in.})(1 \text{ ft}/12 \text{ in.})$ | $V_a = 140 \text{ kips} - (5.00 \text{ kip/ft})(42.0 \text{ in.})(1 \text{ ft}/12 \text{ in.})$ |
| $= 184 \text{ kips}$ | $= 123 \text{ kips}$ |

From AISC *Specification* Section G1, the available shear strength without stiffeners is:

| LRFD | ASD |
|------|-----|
| $\phi_v = 0.90$ | $\Omega_v = 1.67$ |
| From previous calculations, | From previous calculations, |
| $\phi_v V_n = 176 \text{ kips} < 184 \text{ kips}$ **n.g.** | $\dfrac{V_n}{\Omega_v} = 117 \text{ kips} < 123 \text{ kips}$ **n.g.** |
| **Therefore, additional stiffeners are required.** | **Therefore, additional stiffeners are required.** |

---

# G-20

| LRFD | ASD |
|------|-----|
| Use $V_u = \phi_v V_n$ to determine the required stress in the web by dividing by the web area. | Use $V_a = V_n/\Omega_v$ to determine the required stress in the web by dividing by the web area. |
| $\dfrac{\phi_v V_n}{A_w} = \dfrac{V_u}{A_w}$ | $\dfrac{V_n}{\Omega_v A_w} = \dfrac{V_a}{A_w}$ |
| $= \dfrac{184 \text{ kips}}{11.3 \text{ in.}^2}$ | $= \dfrac{123 \text{ kips}}{11.3 \text{ in.}^2}$ |
| $= 16.3 \text{ ksi}$ | $= 10.9 \text{ ksi}$ |

Table 3-16b from the AISC *Manual*, including tension field action, may be used to select the required stiffener ratio $a/h$ based on the $h/t_w$ ratio of the girder and the required stress, provided that the limitations of $2A_w/(A_{fc} + A_{fl}) \leq 2.5$, $h/b_{fc} \leq 6.0$, and $h/b_{fl} \leq 6.0$ are met.

$$\frac{2A_w}{A_{fc} + A_{fl}} = \frac{2(11.3 \text{ in.}^2)}{(16.0 \text{ in.})(1\frac{1}{2} \text{ in.}) + (16.0 \text{ in.})(1\frac{1}{2} \text{ in.})}$$

$$= 0.471 < 2.5$$ **o.k.**

$$\frac{h}{b_{fc}} = \frac{h}{b_fl}$$

$$= \frac{33.0 \text{ in.}}{16.0 \text{ in.}}$$

$$= 2.06 < 6.0$$ **o.k.**

The limitations have been met. AISC *Manual* Table 3-16b may be used.

Interpolate and follow an available stress curve, $\phi_v V_n/A_w = 16.3 \text{ ksi}$ for LRFD, $V_n/\Omega_v A_w = 10.9 \text{ ksi}$ for ASD, until it intersects the horizontal line for an $h/t_w$ value of 106. Because the available stress does not intersect the $h/t_w$ value of 106, the maximum value of 3.00 for $a/h$ may be used. Because $h = 33.0 \text{ in.}$, an additional stiffener is required at $(3.00)(33.0 \text{ in.}) = 99.0 \text{ in.}$ maximum from the previous one. Conservatively, 90.0 in. spacing may be used.

**Stiffener Spacing for the Third Panel**

From AISC *Specification* Section G2.2, tension field action is allowed in the next panel.

The required shear strength at the start of the third panel, 132 in. from the end is:

| LRFD | ASD |
|------|-----|
| $V_u = 210 \text{ kips} - (7.50 \text{ kip/ft})(132 \text{ in.})(1 \text{ ft}/12 \text{ in.})$ | $V_a = 140 \text{ kips} - (5.00 \text{ kip/ft})(132 \text{ in.})(1 \text{ ft}/12 \text{ in.})$ |
| $= 128 \text{ kips}$ | $= 85.0 \text{ kips}$ |

From AISC *Specification* Section G1, the available shear strength without stiffeners is:

---

# G-21

| LRFD | ASD |
|------|-----|
| $\phi_v = 0.90$ | $\Omega_v = 1.67$ |
| From previous calculations, | From previous calculations, |
| $\phi_v V_n = 176 \text{ kips} > 128 \text{ kips}$ **o.k.** | $\dfrac{V_n}{\Omega_v} = 117 \text{ kips} > 85.0 \text{ kips}$ **o.k.** |
| **Therefore, additional stiffeners are not required.** | **Therefore, additional stiffeners are not required.** |

The three tables in the AISC *Manual*, 3-16a, 3-16b, and 3-16c, are useful because they permit a direct solution for the required stiffener spacing. Alternatively, you can select a stiffener spacing and check the resulting strength, although this process is likely to be iterative. In Example G.8B, the stiffener spacings used are taken from this example.

---

# G-22

## EXAMPLE G.8B BUILT-UP GIRDER WITH TRANSVERSE STIFFENERS

### Given:

Verify the available shear strength and adequacy of the stiffener spacings from Example G.8A, which were easily determined from the tabulated values of the AISC *Manual*, by directly applying the provisions of the AISC *Specification*. Stiffeners are spaced at 42 in. in the first panel and 90 in. in the second panel.

### Solution:

From AISC *Manual* Table 2-5, the material properties are as follows:

ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$

From Example G.8A, the required shear strength at the support is:

| LRFD | ASD |
|------|-----|
| $V_u = 210 \text{ kips}$ | $V_a = 140 \text{ kips}$ |

**Shear Strength of End Panel**

The web plate buckling coefficient, $k_v$, is determined from AISC *Specification* Equation G2-5.

$$\frac{h}{t_w} = \frac{33.0 \text{ in.}}{\frac{3}{16} \text{ in.}}$$

$$= 106$$

$$k_v = 5 + \frac{5}{(a/h)^2}$$
$$\text{(Spec. Eq. G2-5)}$$

$$= 5 + \frac{5}{(42.0 \text{ in.}/33.0 \text{ in.})^2}$$

$$= 8.09$$

$$1.10\sqrt{\frac{k_v E}{F_y}} = 1.10\sqrt{\frac{8.09(29,000 \text{ ksi})}{50 \text{ ksi}}}$$

$$= 75.3 < 106$$

Therefore, use AISC *Specification* Equation G2-4.

$$C_{v1} = \frac{1.10\sqrt{k_v E/F_y}}{h/t_w}$$
$$\text{(Spec. Eq. G2-4)}$$

$$= \frac{75.3}{106}$$

$$= 0.710$$

Calculate $V_n$ using AISC *Specification* Section G2.1:

From Example G.8A:

$$A_w = 11.3 \text{ in.}^2$$

---

# G-23

$$V_n = 0.6F_y A_w C_{v1}$$
$$\text{(Spec. Eq. G2-1)}$$

$$= 0.6(50 \text{ ksi})(11.3 \text{ in.}^2)(0.710)$$

$$= 241 \text{ kips}$$

From AISC *Specification* Section G1, the available shear strength for the end panel is:

| LRFD | ASD |
|------|-----|
| $\phi_v = 0.90$ | $\Omega_v = 1.67$ |
| $\phi_v V_n = 0.90(241 \text{ kips})$ | $\dfrac{V_n}{\Omega_v} = \dfrac{241 \text{ kips}}{1.67}$ |
| $= 217 \text{ kips} > 210 \text{ kips}$ **o.k.** | $= 144 \text{ kips} > 140 \text{ kips}$ **o.k.** |

**Shear Strength of the Second Panel**

From Example G.8A, the required shear strength at the start of the second panel is:

| LRFD | ASD |
|------|-----|
| $V_u = 184 \text{ kips}$ | $V_a = 123 \text{ kips}$ |

The web plate buckling coefficient, $k_v$, is determined from AISC *Specification* Equation G2-5.

$$k_v = 5 + \frac{5}{(a/h)^2}$$
$$\text{(Spec. Eq. G2-5)}$$

$$= 5 + \frac{5}{(90.0 \text{ in.}/33.0 \text{ in.})^2}$$

$$= 5.67$$

$$1.37\sqrt{\frac{k_v E}{F_y}} = 1.37\sqrt{\frac{5.67(29,000 \text{ ksi})}{50 \text{ ksi}}}$$

$$= 78.6 < 106$$

Therefore, use AISC *Specification* Equation G2-11 to calculate $C_{v2}$.

$$C_{v2} = \frac{1.51k_v E}{(h/t_w)^2 F_y}$$
$$\text{(Spec. Eq. G2-11)}$$

$$= \frac{1.51(5.67)(29,000 \text{ ksi})}{(106)^2 (50 \text{ ksi})}$$

$$= 0.442$$

The limitations of AISC *Specification* Section G2.2(b)(1) are checked as follows:

$$\frac{2A_w}{A_{fc} + A_{fl}} = \frac{2(11.3 \text{ in.}^2)}{(16.0 \text{ in.})(1\frac{1}{2} \text{ in.}) + (16.0 \text{ in.})(1\frac{1}{2} \text{ in.})}$$

$$= 0.471 < 2.5$$

---

# G-24

$$\frac{h}{b_{fc}} = \frac{h}{b_{fl}}$$

$$= \frac{33.0 \text{ in.}}{16.0 \text{ in.}}$$

$$= 2.06 < 6.0$$

Because $2A_w/(A_{fc} + A_{fl}) \leq 2.5$, $h/b_{fc} \leq 6.0$, and $h/b_{fl} \leq 6.0$, use AISC *Specification* Equation G2-7 with $a = 90.0 \text{ in.}$

$$V_n = 0.6F_y A_w \left[C_{v2} + \frac{1 - C_{v2}}{1.15\sqrt{1 + (a/h)^2}}\right]$$
$$\text{(Spec. Eq. G2-7)}$$

$$= 0.6(50 \text{ ksi})(11.3 \text{ in.}^2)\left[0.442 + \frac{1 - 0.442}{1.15\sqrt{1 + \left(\frac{90.0 \text{ in.}}{33.0 \text{ in.}}\right)^2}}\right]$$

$$= 206 \text{ kips}$$

From AISC *Specification* Section G1, the available shear strength for the second panel is:

| LRFD | ASD |
|------|-----|
| $\phi_v = 0.90$ | $\Omega_v = 1.67$ |
| $\phi_v V_n = 0.90(206 \text{ kips})$ | $\dfrac{V_n}{\Omega_v} = \dfrac{206 \text{ kips}}{1.67}$ |
| $= 185 \text{ kips} > 184 \text{ kips}$ **o.k.** | $= 123 \text{ kips} > 123 \text{ kips}$ **o.k.** |

---

# G-25

## CHAPTER G DESIGN EXAMPLE REFERENCES

AISC (2023), *Companion to the AISC Steel Construction Manual, Volume 2: Design Tables*, V16.0, American Institute of Steel Construction, Chicago, Ill.

Darwin, D. (1990), *Steel and Composite Beams with Web Openings*, Design Guide 2, AISC, Chicago, Ill.

---

# G-26

---
