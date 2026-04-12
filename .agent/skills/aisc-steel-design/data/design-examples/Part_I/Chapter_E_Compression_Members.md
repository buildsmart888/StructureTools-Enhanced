# Chapter E: Compression Members

**AISC Specification v16.0 - Design Examples**
**Original PDF Pages**: 65-162 (98 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Design of Members for Compression

**Examples Included**: ['E.1A~E.14B: 14 compression member examples']

---

## Table of Contents

- [EXAMPLE E.1A W-SHAPE COLUMN DESIGN WITH PINNED ENDS](#example-e1a-w-shape-column-design-with-pinned-ends)
- [EXAMPLE E.1B W-SHAPE COLUMN DESIGN WITH INTERMEDIATE BRACING](#example-e1b-w-shape-column-design-with-intermediate-bracing)
- [EXAMPLE E.1C W-SHAPE AVAILABLE COMPRESSIVE STRENGTH CALCULATION](#example-e1c-w-shape-available-compressive-strength-calculation)
- [EXAMPLE E.1D W-SHAPE AVAILABLE COMPRESSIVE STRENGTH CALCULATION](#example-e1d-w-shape-available-compressive-strength-calculation)
- [EXAMPLE E.1E W-SHAPE COMPRESSION MEMBER WITH SLENDER ELEMENTS](#example-e1e-w-shape-compression-member-with-slender-elements)
- [EXAMPLE E.2 BUILT-UP COLUMN WITH A SLENDER WEB](#example-e2-built-up-column-with-a-slender-web)
- [EXAMPLE E.3 BUILT-UP COLUMN WITH SLENDER FLANGES](#example-e3-built-up-column-with-slender-flanges)

---

# Chapter E
# Design of Members for Compression

This chapter covers the design of compression members, the most common of which are columns. The AISC *Manual* includes design tables for the following compression member types in their most commonly available grades:

• W-shapes and HP-shapes
• Rectangular, square, and round HSS
• Pipes
• WT-shapes
• Double angles
• Single angles

LRFD and ASD information is presented side-by-side for quick selection, design, or verification. All tables account for the reduced strength of sections with slender elements.

The design and selection method for both LRFD and ASD is similar to that of previous editions of the AISC *Specification* and will provide similar results. In the AISC *Specification*, LRFD and ASD will provide identical designs when the live load is approximately three times the dead load.

The design of built-up shapes with slender elements can be tedious and time consuming, and it is recommended that standard rolled shapes be used whenever possible.

---

## E1. GENERAL PROVISIONS

The design compressive strength, ϕ*c* *P*<sub>n</sub>, and the allowable compressive strength, *P*<sub>n</sub>/Ω*c*, are determined as follows:

*P*<sub>n</sub> = nominal compressive strength is the lowest value obtained based on the applicable limit states of flexural buckling, torsional buckling, and flexural-torsional buckling, kips
ϕ*c* = 0.90 (LRFD)
Ω*c* = 1.67 (ASD)

Because the available nominal stress, *F*<sub>cr</sub>, is used extensively in calculations for compression members, it has been tabulated in AISC *Manual* Table 4-14 for all of the common steel yield strengths.

---

## E2. EFFECTIVE LENGTH

In the AISC *Specification*, there is no limit on slenderness, *L*<sub>c</sub>/*r*. Per the User Note in AISC *Specification* Section E2, for members designed on the basis of compression it is recommended that *L*<sub>c</sub>/*r* not exceed 200, as a practical limit based on professional judgment and construction economics.

Although there is no restriction on the unbraced length of columns, AISC *Manual* tables are limited to common or practical lengths for ordinary usage. For example, a double L3×3×¼, with a ⅜ in. separation has an *r*<sub>y</sub> of 1.38 in. At an *L*<sub>c</sub>/*r* of 200, this strut would be 23 ft long. This is thought to be a reasonable limit based on fabrication and handling requirements.

Throughout the AISC *Manual*, shapes that contain slender elements for compression when supplied in their most common material grade are footnoted with the letter "[c]." For example, see a W14×22[c].

---


---

---

## E3. FLEXURAL BUCKLING OF MEMBERS WITHOUT SLENDER ELEMENTS

Nonslender-element compression members, including nonslender built-up I-shaped columns and nonslender HSS columns, are governed by these provisions. The general design curve for critical stress versus *L*<sub>c</sub>/*r* is shown in Figure E-1. The limit between elastic and inelastic buckling is defined to be *L*<sub>c</sub>/*r* = 4.71√*E*/*F*<sub>y</sub> or *F*<sub>y</sub>/*F*<sub>e</sub> = 2.25. For convenience, these limits are defined in Table E-1 for the common values of *F*<sub>y</sub>.

The term *L*<sub>c</sub> is used throughout this chapter to describe the length between points that are braced against lateral and/or rotational displacement.

---

## E4. TORSIONAL AND FLEXURAL-TORSIONAL BUCKLING OF SINGLE ANGLES AND MEMBERS WITHOUT SLENDER ELEMENTS

This section is most commonly applicable to double angles and WT sections, which are singly symmetric shapes subject to torsional and flexural-torsional buckling. The available strengths in axial compression of these shapes are tabulated in AISC *Manual* Part 4 and examples on the use of these tables have been included in this chapter for the shapes.

---

## E5. SINGLE-ANGLE COMPRESSION MEMBERS

The available strength of single-angle compression members is tabulated in AISC *Manual* Part 4.

---

**Table E-1.**
**Limiting Values of** *L*<sub>c</sub>/*r* **and** *F*<sub>e</sub>

| *F*<sub>y</sub>, ksi | Limiting *L*<sub>c</sub>/*r* | *F*<sub>e</sub>, ksi |
|------|------|------|
| 36 | 134 | 16.0 |
| 50 | 113 | 22.2 |
| 65 | 99.5 | 28.9 |
| 70 | 95.9 | 31.1 |

![Standard Column Curve Diagram](diagram)

**Diagram elements:**
- Y-axis: Nominal Stress, *F*<sub>cr</sub> (ksi)
- X-axis: Slenderness, *L*<sub>c</sub>/*r*
- Curve starts at *F*<sub>y</sub> at origin
- *Specification* Equation E3-2 for inelastic buckling region
- Transition between equations (location varies by *F*<sub>y</sub>)
- *Specification* Equation E3-3 for elastic buckling region
- Regions labeled: "Inelastic Buckling" and "Elastic Buckling"

*Fig. E-1. Standard column curve.*

---


---

---

## E6. BUILT-UP MEMBERS

The available strengths in axial compression for built-up double angles with intermediate connectors are tabulated in AISC *Manual* Part 4. There are no tables for other built-up shapes in the AISC *Manual*, due to the number of possible geometries.

---

## E7. MEMBERS WITH SLENDER ELEMENTS

The design of these members is similar to members without slender elements except that a reduced effective area is used in lieu of the gross cross-sectional area.

The tables of AISC *Manual* Part 4 incorporate the appropriate reductions in available strength to account for slender elements.

Design examples have been included in this Chapter for built-up I-shaped members with slender webs and slender flanges. Examples have also been included for a double angle, WT, and a rectangular HSS with slender elements.

---


---

---

## EXAMPLE E.1A W-SHAPE COLUMN DESIGN WITH PINNED ENDS

---

### Given:

Select an ASTM A992/A992M W-shape column to carry the loading shown in Figure E.1A. The column is pinned top and bottom in both axes. Limit the column size to a nominal 14 in. shape.

![Column Loading Diagram](diagram)

**Loading Details:**
- *P*<sub>D</sub> = 140 kips
- *P*<sub>L</sub> = 420 kips
- *L* = 30'-0"
- Column pinned at top and bottom

*Fig. E.1A. Column loading and bracing.*

---

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

**ASTM A992/A992M**
*F*<sub>y</sub> = 50 ksi

From ASCE/SEI 7, Chapter 2, the required compressive strength is:

| LRFD | ASD |
|------|-----|
| *P*<sub>u</sub> = 1.2(140 kips) + 1.6(420 kips) | *P*<sub>a</sub> = 140 kips + 420 kips |
| = 840 kips | = 560 kips |

---

## *Column Selection*

From AISC *Specification* Commentary Table C-A-7.1, for a pinned-pinned condition, *K*<sub>x</sub> = *K*<sub>y</sub> = 1.0. The effective length is:

$$L_c = K_x L_x$$

$$= K_y L_y$$

= 1.0(30 ft)

= 30.0 ft

Because the unbraced length is the same for buckling about the *x*-*x* and *y*-*y* axes and *r*<sub>x</sub> exceeds *r*<sub>y</sub> for all W-shapes, *y*-*y* axis bucking will govern.

Enter AISC *Manual* Table 4-1a with an effective length, *L*<sub>c</sub> = 30 ft, and proceed across the table until reaching the least weight shape with an available strength that equals or exceeds the required strength. Select a W14×132.

---


---

---

From AISC *Manual* Table 4-1a, the available strength for a *y*-*y* axis effective length of 30 ft is:

| LRFD | ASD |
|------|-----|
| ϕ*c* *P*<sub>n</sub> = 893 kips > 840 kips   **o.k.** | *P*<sub>n</sub> / Ω*c* = 594 kips > 560 kips   **o.k.** |

---


---

---

## EXAMPLE E.1B W-SHAPE COLUMN DESIGN WITH INTERMEDIATE BRACING

---

### Given:

Verify an ASTM A992/A992M W14×90 is adequate to carry the loading as shown in Figure E.1B. The column is pinned top and bottom in both axes and braced at the midpoint about the *y*-*y* axis and torsionally.

![Column Loading Diagram](diagram)

**Loading and Bracing Details:**
- *P*<sub>D</sub> = 140 kips
- *P*<sub>L</sub> = 420 kips
- Total height: *L* = 30'-0"
- Upper segment: 15'-0"
- Lower segment: 15'-0"
- Braced *y*-direction and torsionally only at midpoint
- Pinned at top and bottom

*Fig. E.1B. Column loading and bracing.*

---

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

**ASTM A992/A992M**
*F*<sub>y</sub> = 50 ksi

From ASCE/SEI 7, Chapter 2, the required compressive strength is:

| LRFD | ASD |
|------|-----|
| *P*<sub>u</sub> = 1.2(140 kips) + 1.6(420 kips) | *P*<sub>a</sub> = 140 kips + 420 kips |
| = 840 kips | = 560 kips |

---

## *Column Effective Length*

From AISC *Specification* Commentary Table C-A-7.1, for a pinned-pinned condition, *K*<sub>x</sub> = *K*<sub>y</sub> = 1.0. The effective length about the *y*-*y* axis is:

$$L_{cy} = K_y L_y$$

= 1.0(15 ft)

= 15.0 ft

The values tabulated in AISC *Manual* Table 4-1a are provided for buckling in the *y*-*y* direction. To determine the buckling strength about the *x*-*x* axis, an equivalent effective length for the *y*-*y* axis is determined using the *r*<sub>x</sub>/*r*<sub>y</sub> ratio provided at the bottom of this table. For a W14×90, *r*<sub>x</sub>/*r*<sub>y</sub> = 1.66, and the equivalent *y*-*y* axis effective length for *x*-*x* axis buckling is computed as:

---


---

---

$$L_{cx} = K_x L_x$$

= 1.0(30 ft)

= 30.0 ft

$$L_{cy\ eq} = \frac{L_{cx}}{r_x/r_y}$$     (*Manual* Eq. 4-1)

$$= \frac{30.0 \text{ ft}}{1.66}$$

= 18.1 ft

Because 18.1 ft > 15.0 ft, the available compressive strength is governed by the *x*-*x* axis flexural buckling limit state.

---

## *Available Compressive Strength*

The available strength of a W14×90 is determined using AISC *Manual* Table 4-1a, conservatively using an unbraced length of *L*<sub>c</sub> = 19.0 ft.

| LRFD | ASD |
|------|-----|
| ϕ*c* *P*<sub>n</sub> = 903 kips > 840 kips   **o.k.** | *P*<sub>n</sub> / Ω*c* = 601 kips > 560 kips   **o.k.** |

---


---

---

## EXAMPLE E.1C W-SHAPE AVAILABLE COMPRESSIVE STRENGTH CALCULATION

---

### Given:

Calculate the available compressive strength of the column size selected in Example E.1A with an unbraced length of 30 ft for both axes. The loads are as given in Example E.1A.

---

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

**ASTM A992/A992M**
*F*<sub>y</sub> = 50 ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

**W14×132**
*A*<sub>g</sub> = 38.8 in.²
*r*<sub>x</sub> = 6.28 in.
*r*<sub>y</sub> = 3.76 in.
$$\frac{b_f}{2t_f} = 7.15$$
$$\frac{h}{t_w} = 17.7$$

---

## *Slenderness Check*

The width-to-thickness ratio of the flanges of the W14×132 is:

$$\frac{b_f}{2t_f} = 7.15$$

From AISC *Specification* Table B4.1a, Case 1, the limiting width-to-thickness ratio of the flanges is:

$$\lambda_r = 0.56\sqrt{\frac{E}{F_y}}$$

$$= 0.56\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

= 13.5 > 7.15; therefore, the flanges are nonslender

The width-to-thickness ratio of the web of the W14×132 is:

$$\frac{h}{t_w} = 17.7$$

From AISC *Specification* Table B4.1a, Case 5, the limiting width-to-thickness ratio of the web is:

---


---

---

$$\lambda_r = 1.49\sqrt{\frac{E}{F_y}}$$

$$= 1.49\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

= 35.9 > 17.7; therefore, the web is nonslender

Because the web and flanges are nonslender, the limit state of local buckling does not apply.

---

## *Column Effective Length*

From AISC *Specification* Commentary Table C-A-7.1, for a pinned-pinned condition, *K*<sub>x</sub> = *K*<sub>y</sub> = 1.0. The effective length about the *y*-*y* axis is:

$$L_{cy} = K_y L_y$$

= 1.0(30 ft)

= 30.0 ft

Because the unbraced length for the W14×132 column is the same for both axes, the *y*-*y* axis will govern.

$$\frac{L_{cy}}{r_y} = \frac{(30.0 \text{ ft})(12 \text{ in./ft})}{3.76 \text{ in.}}$$

= 95.7

---

## *Nominal Stress*

For *F*<sub>y</sub> = 50 ksi, the available nominal stresses, ϕ*c* *F*<sub>n</sub> or *F*<sub>n</sub>/Ω*c*, for *L*<sub>c</sub>/*r* = 95.7 are interpolated from AISC *Manual* Table 4-14 as follows. The available nominal stress can also be determined as shown in Example E.1D.

| LRFD | ASD |
|------|-----|
| ϕ*c* *F*<sub>n</sub> = 23.0 ksi | *F*<sub>n</sub> / Ω*c* = 15.4 ksi |

---

## *Available Compressive Strength*

From AISC *Specification* Equation E3-1, the available compressive strength of the W14×132 column is:

| LRFD | ASD |
|------|-----|
| ϕ*c* *P*<sub>n</sub> = (ϕ*c* *F*<sub>n</sub>) *A*<sub>g</sub> | *P*<sub>n</sub> / Ω*c* = (*F*<sub>n</sub> / Ω*c*) *A*<sub>g</sub> |
| = (23.0 ksi)(38.8 in.²) | = (15.4 ksi)(38.8 in.²) |
| = 892 kips > 840 kips   **o.k.** | = 598 kips > 560 kips   **o.k.** |

---


---

---

## EXAMPLE E.1D W-SHAPE AVAILABLE COMPRESSIVE STRENGTH CALCULATION

---

### Given:

Calculate the available compressive strength of a W14×90 with an *x*-*x* axis unbraced length of 30 ft and *y*-*y* axis and torsional unbraced lengths of 15 ft. The loads are as given in Example E.1A.

---

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

**ASTM A992/A992M**
*F*<sub>y</sub> = 50 ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

**W14×90**
*A*<sub>g</sub> = 26.5 in.²
*r*<sub>x</sub> = 6.14 in.
*r*<sub>y</sub> = 3.70 in.
$$\frac{b_f}{2t_f} = 10.2$$
$$\frac{h}{t_w} = 25.9$$

---

## *Slenderness Check*

The width-to-thickness ratio of the flanges of the W14×90 is:

$$\frac{b_f}{2t_f} = 10.2$$

From AISC *Specification* Table B4.1a, Case 1, the limiting width-to-thickness ratio of the flanges is:

$$\lambda_r = 0.56\sqrt{\frac{E}{F_y}}$$

$$= 0.56\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

= 13.5 > 10.2; therefore, the flanges are nonslender

The width-to-thickness ratio of the web of the W14×90 is:

$$\frac{h}{t_w} = 25.9$$

From AISC *Specification* Table B4.1a, Case 5, the limiting width-to-thickness ratio of the web is:

---


---

---

$$\lambda_r = 1.49\sqrt{\frac{E}{F_y}}$$

$$= 1.49\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

= 35.9 > 25.9; therefore, the web is nonslender

Because the web and flanges are nonslender, the limit state of local buckling does not apply.

---

## *Column Effective Length*

From AISC *Specification* Commentary Table C-A-7.1, for a pinned-pinned condition, *K*<sub>x</sub> = *K*<sub>y</sub> = 1.0.

$$L_{cx} = K_x L_x$$

= 1.0(30 ft)

= 30.0 ft

$$\frac{L_{cx}}{r_x} = \frac{(30.0 \text{ ft})(12 \text{ in./ft})}{6.14 \text{ in.}}$$

= 58.6   **governs**

$$L_{cy} = K_y L_y$$

= 1.0(15 ft)

= 15.0 ft

$$\frac{L_{cy}}{r_y} = \frac{(15.0 \text{ ft})(12 \text{ in./ft})}{3.70 \text{ in.}}$$

= 48.6

Because $\frac{L_{cx}}{r_x} > \frac{L_{cy}}{r_y}$, *x*-*x* buckling controls.

---

## *Nominal Stress*

The available nominal stress may be interpolated from AISC *Manual* Table 4-14 or calculated directly as follows.

Calculate the elastic buckling stress, *F*<sub>e</sub>, according to AISC *Specification* Section E3. As noted in AISC *Specification* Commentary Section E4, torsional buckling of symmetric shapes is a failure mode usually not considered in the design of hot-rolled columns. This failure mode generally does not govern unless the section is manufactured from relatively thin plates or a torsional unbraced length significantly larger than the *y*-*y* axis flexural unbraced length is present.

$$F_e = \frac{\pi^2 E}{\left(\frac{L_c}{r}\right)^2}$$     (*Spec.* Eq. E3-4)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(58.6)^2}$$

= 83.3 ksi

---


---

---

Calculate the nominal stress, *F*<sub>n</sub>.

$$4.71\sqrt{\frac{E}{F_y}} = 4.71\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

= 113

Because $\frac{L_c}{r} = 58.6 < 113$,

$$F_n = \left(0.658^{\frac{F_y}{F_e}}\right)F_y$$     (*Spec.* Eq. E3-2)

$$= \left(0.658^{\frac{50 \text{ ksi}}{83.3 \text{ ksi}}}\right)(50 \text{ ksi})$$

= 38.9 ksi

---

## *Column Compressive Strength*

From AISC *Specification* Section E3, the nominal compressive strength is:

$$P_n = F_n A_g$$     (*Spec.* Eq. E3-1)

$$= (38.9 \text{ ksi})(26.5 \text{ in.}^2)$$

= 1,030 kips

From AISC *Specification* Section E1, the available compressive strength is:

| LRFD | ASD |
|------|-----|
| ϕ*c* = 0.90 | Ω*c* = 1.67 |
| ϕ*c* *P*<sub>n</sub> = 0.90(1,030 kips) | *P*<sub>n</sub> / Ω*c* = 1,030 kips / 1.67 |
| = 927 kips > 840 kips   **o.k.** | = 617 kips > 560 kips   **o.k.** |

---


---

---

## EXAMPLE E.1E W-SHAPE COMPRESSION MEMBER WITH SLENDER ELEMENTS

---

### Given:

Determine the available strength of an ASTM A992/A992M W16×31 compression member based on the flexural buckling limit state for each of the following unbraced lengths:

a) *L*<sub>c</sub> = 5 ft
b) *L*<sub>c</sub> = 10 ft
c) *L*<sub>c</sub> = 15 ft

---

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

**ASTM A992/A992M**
*F*<sub>y</sub> = 50 ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

**W16×31**
*A*<sub>g</sub> = 9.13 in.²
*b*<sub>f</sub> = 5.53 in.
*d* = 15.9 in.
*t*<sub>f</sub> = 0.440 in.
*t*<sub>w</sub> = 0.275 in.
*r*<sub>x</sub> = 6.41 in.
*r*<sub>y</sub> = 1.17 in.
*k*<sub>des</sub> = 0.842 in.
$$\frac{b_f}{2t_f} = 6.28$$
$$\frac{h}{t_w} = 51.6$$

---

## *Slenderness Check*

The width-to-thickness ratio of the flanges of the W16×31 is:

$$\frac{b_f}{2t_f} = 6.28$$

From AISC *Specification* Table B4.1a, Case 1, the limiting width-to-thickness ratio of the flanges is:

$$\lambda_r = 0.56\sqrt{\frac{E}{F_y}}$$

$$= 0.56\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

= 13.5 > 6.28; therefore, the flanges are nonslender

---


---

---

The width-to-thickness ratio of the web of the W16×31 is:

$$\frac{h}{t_w} = 51.6$$

From AISC *Specification* Table B4.1a, Case 5, the limiting width-to-thickness ratio of the web is:

$$\lambda_r = 1.49\sqrt{\frac{E}{F_y}}$$

$$= 1.49\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

= 35.9 < 51.6; therefore, the web is slender

The W16×31 is slender for *F*<sub>y</sub> = 50 ksi and AISC *Specification* Section E7 applies.

---

## *Solution a* (*L*<sub>c</sub> = 5 ft)

### *Nominal Stress*

$$\left(\frac{L_c}{r}\right)_{max} = \frac{L_c}{r_y}$$

$$= \frac{(5 \text{ ft})(12 \text{ in./ft})}{1.17 \text{ in.}}$$

= 51.3

$$F_e = \frac{\pi^2 E}{\left(\frac{L_c}{r}\right)^2}$$     (*Spec.* Eq. E3-4)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(51.3)^2}$$

= 109 ksi

$$4.71\sqrt{\frac{E}{F_y}} = 4.71\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

= 113

Because $\frac{L_c}{r} = 51.3 < 113$,

$$F_n = \left(0.658^{\frac{F_y}{F_e}}\right)F_y$$     (*Spec.* Eq. E3-2)

$$= \left(0.658^{\frac{50 \text{ ksi}}{109 \text{ ksi}}}\right)(50\text{ksi})$$

= 41.3 ksi

---


---

---

## *Effective Area*

The effective area is determined using AISC *Specification* Section E7. Because the flanges are nonslender, the flange areas are fully effective. The effective area, *A*<sub>e</sub>, is based on the slender web element.

$$\lambda_r\sqrt{\frac{F_{cr}}{F_n}} = 35.9\sqrt{\frac{50 \text{ ksi}}{41.3 \text{ ksi}}}$$

= 39.5

Because λ = 51.6 > 39.5, the web element is not fully effective. Use AISC *Specification* Equation E7-3 to calculate *h*<sub>e</sub>.

Determine the effective width imperfection adjustment factors from AISC *Specification* Table E7.1, Case (a):

*c*₁ = 0.18
*c*₂ = 1.31

From AISC *Specification* Equation E7-5:

$$F_{cl} = \left[c_2 \frac{\lambda_r}{\lambda}\right]^2 F_y$$     (*Spec.* Eq. 7-5)

$$= \left[(1.31)\left(\frac{35.9}{51.6}\right)\right]^2 (50 \text{ ksi})$$

= 41.5 ksi

The web height is determined as follows:

$$h = \left(\frac{h}{t_w}\right)t_w$$

= (51.6)(0.275 in.)

= 14.2 in.

Alternatively,

$$h = d - 2k_{des}$$

= 15.9 in. − 2(0.842 in.)

= 14.2 in.

The effective web height is determined as follows:

$$h_e = h\left(1 - c_1\sqrt{\frac{F_{cl}}{F_n}}\right)\sqrt{\frac{F_{cl}}{F_n}}$$     (from *Spec.* Eq. 7-3)

$$= (14.2 \text{ in.})\left[1 - 0.18\sqrt{\frac{41.5 \text{ ksi}}{41.3 \text{ ksi}}}\right]\left(\sqrt{\frac{41.5 \text{ ksi}}{41.3 \text{ ksi}}}\right)$$

= 11.7 in.

---


---

---

The effective area of the W16×31 is:

$$A_e = A_g - (h - h_e)t_w$$

$$= 9.13 \text{ in.}^2 - (14.2 \text{ in.} - 11.7 \text{ in.})(0.275 \text{ in.})$$

= 8.44 in.²

---

## *Column Compressive Strength*

From AISC *Specification* Section E7, the nominal compressive strength is:

$$P_n = F_n A_e$$     (*Spec.* Eq. E7-1)

$$= (41.3 \text{ ksi})(8.44 \text{ in.}^2)$$

= 349 kips

From AISC *Specification* Section E1, the available compressive strength is:

| LRFD | ASD |
|------|-----|
| ϕ*c* = 0.90 | Ω*c* = 1.67 |
| ϕ*c* *P*<sub>n</sub> = 0.90(349 kips) | *P*<sub>n</sub> / Ω*c* = 349 kips / 1.67 |
| = 314 kips | = 209 kips |

---

## *Solution b* (*L*<sub>c</sub> = 10 ft)

### *Nominal Stress*

$$\left(\frac{L_c}{r}\right)_{max} = \frac{L_c}{r_y}$$

$$= \frac{(10 \text{ ft})(12 \text{ in./ft})}{1.17 \text{ in.}}$$

= 103

$$F_e = \frac{\pi^2 E}{\left(\frac{L_c}{r}\right)^2}$$     (*Spec.* Eq. E3-4)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(103)^2}$$

= 27.0 ksi

$$4.71\sqrt{\frac{E}{F_y}} = 4.71\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

= 113

---


---

Because $\frac{L_c}{r} = 103 < 113$,

$$F_n = \left(0.658^{\frac{F_y}{F_e}}\right) F_y$$
(Spec. Eq. E3-2)

$$= \left(0.658^{\frac{50 \text{ ksi}}{27.0 \text{ ksi}}}\right) (50 \text{ ksi})$$

$$= 23.0 \text{ ksi}$$

**Effective Area**

The effective area is determined using AISC *Specification* Section E7. Because the flanges are nonslender, the flange areas are fully effective. The effective area, $A_e$, is based on the slender web element.

$$\lambda_r \sqrt{\frac{F_y}{F_n}} = 35.9 \sqrt{\frac{50 \text{ ksi}}{23.0 \text{ ksi}}}$$

$$= 52.9$$

Because $\lambda = 51.6 < 52.9$, the web element is fully effective and $A_e = A_g$.

**Column Compressive Strength**

From AISC *Specification* Section E7, the nominal compressive strength is:

$$P_n = F_n A_e$$
(Spec. Eq. E7-1)

$$= (23.0 \text{ ksi})(9.13 \text{ in.}^2)$$

$$= 210 \text{ kips}$$

From AISC *Specification* Section E1, the available compressive strength is:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.90$ | $\Omega_c = 1.67$ |
| $\phi_c P_n = 0.90(210 \text{ kips})$ | $\frac{P_n}{\Omega_c} = \frac{210 \text{ kips}}{1.67}$ |
| $= 189 \text{ kips}$ | $= 126 \text{ kips}$ |

**Solution** $c$ $(L_c = 15 \text{ ft})$

*Nominal Stress*

$$\left(\frac{L_c}{r}\right)_{max} = \frac{L_c}{r_y}$$

$$= \frac{(15 \text{ ft})(12 \text{ in./ft})}{1.17 \text{ in.}}$$

$$= 154$$

---

$$F_e = \frac{\pi^2 E}{\left(\frac{L_c}{r}\right)^2}$$
(Spec. Eq. E3-4)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(154)^2}$$

$$= 12.1 \text{ ksi}$$

$$4.71 \sqrt{\frac{E}{F_y}} = 4.71 \sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 113$$

Because $\frac{L_c}{r} = 154 > 113$,

$$F_n = 0.877F_e$$
(Spec. Eq. E3-3)

$$= 0.877(12.1 \text{ ksi})$$

$$= 10.6 \text{ ksi}$$

**Effective Area**

The effective area is determined using AISC *Specification* Section E7. Because the flanges are nonslender, the flange areas are fully effective. The effective area, $A_e$, is based on the slender web element.

$$\lambda_r \sqrt{\frac{F_y}{F_n}} = 35.9 \sqrt{\frac{50 \text{ ksi}}{10.6 \text{ ksi}}}$$

$$= 78.0$$

Because $\lambda = 51.6 < 78.0$, the web element is fully effective and $A_e = A_g$.

**Column Compressive Strength**

From AISC *Specification* Section E7, the nominal compressive strength is:

$$P_n = F_n A_e$$
(Spec. Eq. E7-1)

$$= (10.6 \text{ ksi})(9.13 \text{ in.}^2)$$

$$= 96.8 \text{ kips}$$

From AISC *Specification* Section E1, the available compressive strength is:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.90$ | $\Omega_c = 1.67$ |
| $\phi_c P_n = 0.90(96.8 \text{ kips})$ | $\frac{P_n}{\Omega_c} = \frac{96.8 \text{ kips}}{1.67}$ |
| $= 87.1 \text{ kips}$ | $= 58.0 \text{ kips}$ |

---

**Summary**

**Table E.1E-1.**
**Example E.1E Design Summary**

| Effective Length, $L_c$, ft | 5 | 10 | 15 |
|------------------------------|---|----|----|
| $F_n$, ksi | 41.3 | 23.0 | 10.6 |
| $F_{nl}$, ksi | 41.5 | Not applicable | Not applicable |
| $\lambda_r \sqrt{\frac{F_y}{F_n}}$ | $39.5 < \lambda = 51.6$ | $52.9 > \lambda = 51.6$ | $78.0 > \lambda = 51.6$ |
| $h_e$, in. | $11.7 < h = 14.2$ | $h_e = h = 14.2$ | $h_e = h = 14.2$ |
| $P_n$, kips | 349 | 210 | 96.8 |
| Available Strength, kips (manually calculated) | $\phi_c P_n = 314$ <br> $P_n/\Omega_c = 209$ | $\phi_c P_n = 189$ <br> $P_n/\Omega_c = 126$ | $\phi_c P_n = 87.1$ <br> $P_n/\Omega_c = 58.0$ |
| Available Strength, kips (AISC *Manual* Table 6-1) | Not listed | $\phi_c P_n = 190$ <br> $P_n/\Omega_c = 127$ | $\phi_c P_n = 87.1$ <br> $P_n/\Omega_c = 58.0$ |

Note: The differences between manually calculated and AISC *Manual* Table 6-1 values are due to rounding.

---

## EXAMPLE E.2 BUILT-UP COLUMN WITH A SLENDER WEB

**Given:**

Verify that a built-up, ASTM A572/A572M Grade 50 column with PL1 in. × 8 in. flanges and a PL¼ in. × 15 in. web, as shown in Figure E2-1, is sufficient to carry a dead load of 70 kips and live load of 210 kips in axial compression. The column's unbraced length is 15 ft and the ends are pinned in both axes.

![Column geometry diagram showing:
- $P_D = 70$ kips
- $P_L = 210$ kips
- $L = 15'0"$
- Cross-section with dimensions: $b_f = 8"$, $t_f = 1"$, $t_w = ¼"$, $h = 15"$, total depth $d = 17"$]

*Fig. E.2-1. Column geometry for Example E.2.*

**Solution:**

From AISC *Manual* Table 2-5, the material properties are as follows:

Built-Up Column
ASTM A572/A572M Grade 50
$F_y = 50$ ksi

The geometric properties are as follows:

Built-Up Column
$d = 17.0$ in.
$b_f = 8.00$ in.
$t_f = 1.00$ in.
$h = 15.0$ in.
$t_w = ¼$ in.

From ASCE/SEI 7, Chapter 2, the required compressive strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(70 \text{ kips}) + 1.6(210 \text{ kips})$ | $P_a = 70 \text{ kips} + 210 \text{ kips}$ |
| $= 420$ kips | $= 280$ kips |

**Built-Up Section Properties (ignoring fillet welds)**

$$A_g = 2b_f t_f + ht_w$$

$$= 2(8.00 \text{ in.})(1.00 \text{ in.}) + (15.0 \text{ in.})(¼ \text{ in.})$$

$$= 19.8 \text{ in.}^2$$

---

$$I_y = \sum \frac{bh^3}{12}$$

$$= 2 \left[\frac{(1.00 \text{ in.})(8.00 \text{ in.})^3}{12}\right] + \frac{(15.0 \text{ in.})(¼ \text{ in.})^3}{12}$$

$$= 85.4 \text{ in.}^4$$

$$r_y = \sqrt{\frac{I_y}{A}}$$

$$= \sqrt{\frac{85.4 \text{ in.}^4}{19.8 \text{ in.}^2}}$$

$$= 2.08 \text{ in.}$$

$$I_x = \sum Ad^2 + \sum \frac{bh^3}{12}$$

$$= 2\left[(8.00 \text{ in.}^2)(8.00 \text{ in.})^2\right] + \frac{(¼ \text{ in.})(15.0 \text{ in.})^3}{12} + 2\left[\frac{(8.00 \text{ in.})(1.00 \text{ in.})^3}{12}\right]$$

$$= 1,100 \text{ in.}^4$$

**Elastic Flexural Buckling Stress**

From AISC *Specification* Commentary Table C-A-7.1, for a pinned-pinned condition, $K_y = 1.0$.

Because the unbraced length is the same for both axes, the $y$-$y$ axis will govern by inspection. With $L_{cy} = K_y L_y = 1.0(15 \text{ ft}) = 15.0$ ft:

$$\frac{L_{cy}}{r_y} = \frac{(15.0 \text{ ft})(12 \text{ in./ft})}{2.08 \text{ in.}}$$

$$= 86.5$$

$$F_e = \frac{\pi^2 E}{\left(\frac{L_{cy}}{r_y}\right)^2}$$
(from Spec. Eq. E3-4)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(86.5)^2}$$

$$= 38.3 \text{ ksi}$$

**Torsional Elastic Buckling Stress**

Note: Torsional buckling generally will not govern for doubly symmetric members if $L_{cy} \geq L_{cz}$; however, the check is included here to illustrate the calculation.

From the User Note in AISC *Specification* Section E4:

---

$$C_w = \frac{I_y h_o^2}{4}$$

$$= \frac{(85.4 \text{ in.}^4)(16.0 \text{ in.})^2}{4}$$

$$= 5,470 \text{ in.}^6$$

From AISC Design Guide 9, Equation 3.4:

$$J = \sum \frac{bt^3}{3}$$

$$= 2\left[\frac{(8.00 \text{ in.})(1.00 \text{ in.})^3}{3}\right] + \frac{(15.0 \text{ in.})(¼ \text{ in.})^3}{3}$$

$$= 5.41 \text{ in.}^4$$

$$F_e = \left(\frac{\pi^2 EC_w}{L_{cz}^2} + GJ\right) \frac{1}{I_x + I_y}$$
(Spec. Eq. E4-2)

$$= \left\{\frac{\pi^2 (29,000 \text{ ksi})(5,470 \text{ in.}^6)}{[1.0(15 \text{ ft})(12 \text{ in./ft})]^2} + (11,200 \text{ ksi})(5.41 \text{ in.}^4)\right\} \left(\frac{1}{1,100 \text{ in.}^4 + 85.4 \text{ in.}^4}\right)$$

$$= 91.9 \text{ ksi} > 38.3 \text{ ksi}$$

Therefore, the flexural buckling limit state controls.

Use $F_e = 38.3$ ksi.

**Flexural Buckling Stress**

$$\frac{F_y}{F_e} = \frac{50 \text{ ksi}}{38.3 \text{ ksi}}$$

$$= 1.31$$

Because $\frac{F_y}{F_e} < 2.25$,

$$F_n = \left(0.658^{\frac{F_y}{F_e}}\right) F_y$$
(Spec. Eq. E3-2)

$$= \left(0.658^{1.31}\right)(50 \text{ ksi})$$

$$= 28.9 \text{ ksi}$$

**Slenderness**

Check for slender flanges using AISC *Specification* Table B4.1a.

Calculate $k_c$ using AISC *Specification* Table B4.1a, note [a].

---

$$k_c = \frac{4}{\sqrt{h/t_w}}$$

$$= \frac{4}{\sqrt{\frac{15.0 \text{ in.}}{¼ \text{ in.}}}}$$

$$= 0.516, \text{ which is between } 0.35 \text{ and } 0.76.$$

For the flanges:

$$\lambda = \frac{b}{t}$$

$$= \frac{4.00 \text{ in.}}{1.00 \text{ in.}}$$

$$= 4.00$$

Determine the flange limiting slenderness ratio, $\lambda_r$, from AISC *Specification* Table B4.1a, Case 2:

$$\lambda_r = 0.64 \sqrt{\frac{k_c E}{F_y}}$$

$$= 0.64 \sqrt{\frac{0.516(29,000 \text{ ksi})}{50 \text{ ksi}}}$$

$$= 11.1$$

Because $\lambda < \lambda_r$, the flanges are not slender and there is no reduction in effective area due to local buckling of the flanges.

Check for a slender web using AISC *Specification* Table B4.1a.

$$\lambda = \frac{h}{t_w}$$

$$= \frac{15.0 \text{ in.}}{¼ \text{ in.}}$$

$$= 60.0$$

Determine the slender web limit from AISC *Specification* Table B4.1a, Case 5:

$$\lambda_r = 1.49 \sqrt{\frac{E}{F_y}}$$

$$= 1.49 \sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 35.9$$

Because $\lambda > \lambda_r$, the web is slender. Determine the effective area for compression, $A_e$, using AISC *Specification* Section E7.1.

Determine the slenderness limit from AISC *Specification* Section E7.1 for a fully effective element:

---

$$\lambda_r \sqrt{\frac{F_y}{F_n}} = 35.9 \sqrt{\frac{50 \text{ ksi}}{28.9 \text{ ksi}}}$$

$$= 47.2$$

Because $\lambda = 60.0 > 47.2$, the effective width is determined from AISC *Specification* Equation E7-3. Determine the effective width imperfection adjustment factors from AISC *Specification* Table E7.1, Case (a):

$$c_1 = 0.18$$

$$c_2 = 1.31$$

The elastic local buckling stress is:

$$F_{cl} = \left(c_2 \frac{\lambda_r}{\lambda}\right)^2 F_y$$
(Spec. Eq. E7-5)

$$= \left[1.31 \left(\frac{35.9}{60.0}\right)\right]^2 (50 \text{ ksi})$$

$$= 30.7 \text{ ksi}$$

Determine the effective width of the web and the resulting effective area:

$$h_e = h \left[1 - c_1 \sqrt{\frac{F_{cl}}{F_n}}\right] \sqrt{\frac{F_{cl}}{F_n}}$$
(from Spec. Eq. E7-3)

$$= (15.0 \text{ in.}) \left[1 - 0.18 \sqrt{\frac{30.7 \text{ ksi}}{28.9 \text{ ksi}}}\right] \sqrt{\frac{30.7 \text{ ksi}}{28.9 \text{ ksi}}}$$

$$= 12.6 \text{ in.}$$

$$A_e = A_g - (h - h_e)t_w$$

$$= 19.8 \text{ in.}^2 - (15.0 \text{ in.} - 12.6 \text{ in.})(¼ \text{ in.})$$

$$= 19.2 \text{ in.}^2$$

**Column Compressive Strength**

From AISC *Specification* Section E7, the nominal compressive strength is:

$$P_n = F_n A_e$$
(Spec. Eq. E7-1)

$$= (28.9 \text{ ksi})(19.2 \text{ in.}^2)$$

$$= 555 \text{ kips}$$

From AISC *Specification* Section E1, the available compressive strength is:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.90$ | $\Omega_c = 1.67$ |
| $\phi_c P_n = 0.90(555 \text{ kips})$ | $\frac{P_n}{\Omega_c} = \frac{555 \text{ kips}}{1.67}$ |
| $= 500 \text{ kips} > 420 \text{ kips}$ **o.k.** | $= 332 \text{ kips} > 280 \text{ kips}$ **o.k.** |

---

## EXAMPLE E.3 BUILT-UP COLUMN WITH SLENDER FLANGES

**Given:**

Determine if a built-up, ASTM A572/A572M Grade 50 column with PL⅜ in. × 10½ in. flanges and a PL¼ in. × 7¼ in. web, as shown in Figure E.3-1, has sufficient available strength to carry a dead load of 40 kips and a live load of 120 kips in axial compression. The column's unbraced length is 15 ft and the ends are pinned in both axes.

![Column geometry diagram showing:
- $P_D = 40$ kips
- $P_L = 120$ kips
- $L = 15'0"$
- Cross-section with dimensions: $b_f = 10½"$, $t_f = ⅜"$, $t_w = ¼"$, $h = 7¼"$, total depth $d = 8"$]

*Fig. E.3-1. Column geometry for Example E.3.*

**Solution:**

From AISC *Manual* Table 2-5, the material properties are as follows:

Built-Up Column
ASTM A572/A572M Grade 50
$F_y = 50$ ksi

The geometric properties are as follows:

Built-Up Column
$d = 8.00$ in.
$b_f = 10½$ in.
$t_f = ⅜$ in.
$h = 7¼$ in.
$t_w = ¼$ in.

From ASCE/SEI 7, Chapter 2, the required compressive strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(40 \text{ kips}) + 1.6(120 \text{ kips})$ | $P_a = 40 \text{ kips} + 120 \text{ kips}$ |
| $= 240$ kips | $= 160$ kips |

**Built-Up Section Properties (ignoring fillet welds)**

$$A_g = 2(10½ \text{ in.})(⅜ \text{ in.}) + (7¼ \text{ in.})(¼ \text{ in.})$$

$$= 9.69 \text{ in.}^2$$

Because the unbraced length is the same for both axes, the $y$-$y$ axis will govern.

---

$$I_y = \sum \frac{bh^3}{12}$$

$$= 2\left[\frac{(⅜ \text{ in.})(10½ \text{ in.})^3}{12}\right] + \frac{(7¼ \text{ in.})(¼ \text{ in.})^3}{12}$$

$$= 72.4 \text{ in.}^4$$

$$r_y = \sqrt{\frac{I_y}{A_g}}$$

$$= \sqrt{\frac{72.4 \text{ in.}^4}{9.69 \text{ in.}^2}}$$

$$= 2.73 \text{ in.}$$

$$I_x = \sum Ad^2 + \sum \frac{bh^3}{12}$$

$$= 2\left[(10½ \text{ in.})(⅜ \text{ in.})(3.81 \text{ in.})^2\right] + \frac{(¼ \text{ in.})(7¼ \text{ in.})^3}{12} + 2\left[\frac{(10½ \text{ in.})(⅜ \text{ in.})^3}{12}\right]$$

$$= 122 \text{ in.}^4$$

**Web Slenderness**

Determine the limiting slenderness ratio, $\lambda_r$, from AISC *Specification* Table B4.1a, Case 5:

$$\lambda_r = 1.49 \sqrt{\frac{E}{F_y}}$$

$$= 1.49 \sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 35.9$$

$$\lambda = \frac{h}{t_w}$$

$$= \frac{7¼ \text{ in.}}{¼ \text{ in.}}$$

$$= 29.0$$

Because $\lambda < \lambda_r$, the web is not slender.

Note that the fillet welds are ignored in the calculation of $h$ for built up sections.

**Flange Slenderness**

Calculate $k_c$ using AISC *Specification* Table B4.1a, note [a]:

---

$$k_c = \frac{4}{\sqrt{h/t_w}}$$

$$= \frac{4}{\sqrt{\frac{7\frac{1}{4} \text{ in.}}{\frac{1}{4} \text{ in.}}}}$$

$$= 0.743, \text{ which is between } 0.35 \text{ and } 0.76$$

Determine the limiting slenderness ratio, $\lambda_r$, from AISC *Specification* Table B4.1a, Case 2:

$$\lambda_r = 0.64\sqrt{\frac{k_c E}{F_y}}$$

$$= 0.64\sqrt{\frac{0.743(29,000 \text{ ksi})}{50 \text{ ksi}}}$$

$$= 13.3$$

$$\lambda = \frac{b}{t}$$

$$= \frac{5.25 \text{ in.}}{\frac{3}{8} \text{ in.}}$$

$$= 14.0$$

Because $\lambda > \lambda_r$, the flanges are slender.

For compression members with slender elements, AISC *Specification* Section E7 applies. The nominal compressive strength, $P_n$, is determined based on the limit states of flexural, torsional, and flexural-torsional buckling. Depending on the slenderness of the column, AISC *Specification* Equation E3-2 or E3-3 applies. $F_e$ is used in both equations and is calculated as the lesser of AISC *Specification* Equations E3-4 and E4-2.

From AISC *Specification* Commentary Table C-A-7.1, for a pinned-pinned condition, $K = 1.0$.

Because the unbraced length is the same for both axes, the $y$-$y$ axis will govern. With $L_{cy} = K_y L_y = 1.0(15 \text{ ft}) = 15.0$ ft:

$$\frac{L_{cy}}{r_y} = \frac{(15.0 \text{ ft})(12 \text{ in./ft})}{2.73 \text{ in.}}$$

$$= 65.9$$

*Elastic Buckling Stress, $F_e$, for Flexural Buckling*

$$F_e = \frac{\pi^2 E}{\left(\frac{L_{cy}}{r_y}\right)^2}$$
(from *Spec.* Eq. E3-4)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(65.9)^2}$$

$$= 65.9 \text{ ksi}$$

---

*Elastic Buckling Stress, $F_e$, for Torsional Buckling*

Note: This limit state is not likely to govern, but the check is included here for completeness.

From the User Note in AISC *Specification* Section E4:

$$C_w = \frac{I_y h_o^2}{4}$$

$$= \frac{(72.4 \text{ in.}^4)(7.63 \text{ in.})^2}{4}$$

$$= 1,050 \text{ in.}^6$$

From AISC Design Guide 9, Equation 3.4:

$$J = \sum \frac{bt^3}{3}$$

$$= \frac{2(10\frac{1}{2} \text{ in.})(\frac{3}{8} \text{ in.})^3 + (7\frac{1}{4} \text{ in.})(\frac{1}{4} \text{ in.})^3}{3}$$

$$= 0.407 \text{ in.}^4$$

With $L_{cz} = K_z L_z = 1.0(15 \text{ ft}) = 15$ ft:

$$F_e = \left(\frac{\pi^2 EC_w}{L_{cz}^2} + GJ\right)\frac{1}{I_x + I_y}$$
(*Spec.* Eq. E4-2)

$$= \left\{\frac{\pi^2 (29,000 \text{ ksi})(1,050 \text{ in.}^6)}{\left[(15 \text{ ft})(12 \text{ in./ft})\right]^2} + (11,200 \text{ ksi})(0.407 \text{ in.}^4)\right\}\left(\frac{1}{122 \text{ in.}^4 + 72.4 \text{ in.}^4}\right)$$

$$= 71.2 \text{ ksi} > 65.9 \text{ ksi}$$

Therefore, use $F_e = 65.9$ ksi.

*Nominal Stress*

$$\frac{F_y}{F_e} = \frac{50 \text{ ksi}}{65.9 \text{ ksi}}$$

$$= 0.759$$

Because $\frac{F_y}{F_e} < 2.25$:

$$F_n = \left(0.658^{\frac{F_y}{F_e}}\right)F_y$$
(*Spec.* Eq. E3-2)

$$= \left(0.658^{0.759}\right)(50 \text{ ksi})$$

$$= 36.4 \text{ ksi}$$

---

*Effective Area*

The effective area, $A_e$, is the summation of the effective areas of the cross section based on the reduced effective widths, $b_e$ or $h_e$. Because the web is nonslender, there is no reduction in the effective area due to web local buckling and $h_e = h$.

Determine the slender flange limit from AISC *Specification* Section E7.1.

$$\lambda_r \sqrt{\frac{F_y}{F_n}} = 13.3\sqrt{\frac{50 \text{ ksi}}{36.4 \text{ ksi}}}$$

$$= 15.6$$

Because $\lambda = 14.0 < 15.6$ for all elements,

$$b_e = b$$
(*Spec.* Eq. E7-2)

Therefore, $A_e = A_g$.

*Column Compressive Strength*

From AISC *Specification* Section E7, the nominal compressive strength is:

$$P_n = F_n A_e$$
(*Spec.* Eq. E7-1)

$$= (36.4 \text{ ksi})(9.69 \text{ in.}^2)$$

$$= 353 \text{ kips}$$

From AISC *Specification* Section E1, the available compressive strength is:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.90$ | $\Omega_c = 1.67$ |
| $\phi_c P_n = 0.90(353 \text{ kips})$ | $\frac{P_n}{\Omega_c} = \frac{353 \text{ kips}}{1.67}$ |
| $= 318 \text{ kips} > 240 \text{ kips}$ **o.k.** | $= 211 \text{ kips} > 160 \text{ kips}$ **o.k.** |

Note: Built-up sections are generally more expensive than standard rolled shapes; therefore, a standard compact shape, such as a W8×35 might be a better choice, even if the weight is somewhat higher. This selection could be taken directly from AISC *Manual* Table 4-1a.

---

# EXAMPLE E.4A W-SHAPE COMPRESSION MEMBER (MOMENT FRAME)

This example is primarily intended to illustrate the use of the alignment chart for sidesway uninhibited columns in conjunction with the effective length method.

## Given:

The member sizes shown for the moment frame illustrated here (sidesway uninhibited in the plane of the frame) have been determined to be adequate for lateral loads. The material for both the beams and the girders is ASTM A992/A992M. The loads shown at each level are the unfactored dead loads and live loads at that story. The column is fixed at the base about the $x$-$x$ axis of the column.

Determine if the column is adequate to support the gravity loads shown. Assume the column is continuously supported in the transverse direction (the $y$-$y$ axis of the column).

![Diagram: Three-story moment frame with:
- Top level (C): W18×50, $P_D = 41.5$ kips, $P_L = 125$ kips, $I_x = 800$ in.⁴, W14×82, $L = 141$ ft, $I_x = 881$ in.⁴
- Mid level (B): W24×55, $P_D = 100$ kips, $P_L = 300$ kips, $I_x = 1,350$ in.⁴, W14×82, $L = 141$ ft, $I_x = 881$ in.⁴
- Base level (A): Fixed support
- Spans: $L = 35$ ft for two bays
- Column heights: 14 ft between levels
- Note: "Webs of columns and girders are in the plane of the frame."]

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

W18×50
$I_x = 800$ in.⁴

W24×55
$I_x = 1,350$ in.⁴

W14×82
$A_g = 24.0$ in.²
$I_x = 881$ in.⁴

*Column B-C*

From ASCE/SEI 7, Chapter 2, the required compressive strength for the column between the roof and floor is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(41.5 \text{ kips}) + 1.6(125 \text{ kips})$ | $P_a = 41.5 \text{ kips} + 125 \text{ kips}$ |
| $= 250$ kips | $= 167$ kips |

---

*Effective Length Factor*

Using the effective length method, the effective length factor is determined using AISC *Specification* Commentary Appendix 7, Section 7.2. As discussed there, column inelasticity should be addressed by incorporating the stiffness reduction parameter, $\tau_b$. Determine $G_{top}$ and $G_{bottom}$ accounting for column inelasticity by replacing $E_{col}I_{col}$ with $\tau_b(E_{col}I_{col})$. Calculate the stiffness reduction parameter, $\tau_b$, for column B-C using AISC *Manual* Table 4-13.

| LRFD | ASD |
|------|-----|
| $\frac{P_u}{A_g} = \frac{250 \text{ kips}}{24.0 \text{ in.}^2}$ | $\frac{P_a}{A_g} = \frac{167 \text{ kips}}{24.0 \text{ in.}^2}$ |
| $= 10.4$ ksi | $= 6.96$ ksi |
| $\tau_b = 1.00$ | $\tau_b = 1.00$ |

Therefore, no reduction in stiffness for inelastic buckling will be required.

Determine $G_{top}$ and $G_{bottom}$.

$$G_{top} = \tau_b \left[\frac{\sum(EI/L)_{col}}{\sum(EI/L)_g}\right]$$
(from *Spec.* Comm. Eq. C-A-7-3)

$$= 1.00\left\{\frac{\left[\frac{(29,000 \text{ ksi})(881 \text{ in.}^4)}{14.0 \text{ ft}}\right]}{2\left[\frac{(29,000 \text{ ksi})(800 \text{ in.}^4)}{35.0 \text{ ft}}\right]}\right\}$$

$$= 1.38$$

$$G_{bottom} = \tau_b \left[\frac{\sum(EI/L)_{col}}{\sum(EI/L)_g}\right]$$
(from *Spec.* Comm. Eq. C-A-7-3)

$$= 1.00\left\{\frac{2\left[\frac{(29,000 \text{ ksi})(881 \text{ in.}^4)}{14.0 \text{ ft}}\right]}{2\left[\frac{(29,000 \text{ ksi})(1,350 \text{ in.}^4)}{35.0 \text{ ft}}\right]}\right\}$$

$$= 1.63$$

From the alignment chart, AISC *Specification* Commentary Figure C-A-7.2, $K$ is slightly less than 1.5; therefore, use $K = 1.5$. Because the column available strength tables are based on the $L_c$ about the $y$-$y$ axis, the equivalent effective column length of the upper segment for use in the table is:

$$L_{cx} = (KL)_x$$

$$= 1.5(14 \text{ ft})$$

$$= 21.0 \text{ ft}$$

---

From AISC *Manual* Table 4-1a, for a W14×82:

$$\frac{r_x}{r_y} = 2.44$$

$$L_c = \frac{L_{cx}}{\left(\frac{r_x}{r_y}\right)}$$

$$= \frac{21.0 \text{ ft}}{2.44}$$

$$= 8.61 \text{ ft}$$

Using $L_c = 9$ ft in AISC *Manual* Table 4-1a, the available strength in axial compression of the W14×82 is:

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 940 \text{ kips} > 250 \text{ kips}$ **o.k.** | $\frac{P_n}{\Omega_c} = 626 \text{ kips} > 167 \text{ kips}$ **o.k.** |

*Column A-B*

From Chapter 2 of ASCE/SEI 7, the required compressive strength for the column between the floor and the foundation is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(100 \text{ kips}) + 1.6(300 \text{ kips})$ | $P_a = 100 \text{ kips} + 300 \text{ kips}$ |
| $= 600$ kips | $= 400$ kips |

*Effective Length Factor*

Determine the stiffness reduction parameter, $\tau_b$, for column A-B using AISC *Manual* Table 4-13.

| LRFD | ASD |
|------|-----|
| $\frac{P_u}{A_g} = \frac{600 \text{ kips}}{24.0 \text{ in.}^2}$ | $\frac{P_a}{A_g} = \frac{400 \text{ kips}}{24.0 \text{ in.}^2}$ |
| $= 25.0$ ksi | $= 16.7$ ksi |
| $\tau_b = 1.00$ | $\tau_b = 0.994$ |

Use $\tau_b = 0.994$.

---

$$G_{top} = \tau_b \left[\frac{\sum(EI/L)_{col}}{\sum(EI/L)_g}\right]$$
(from *Spec.* Comm. Eq. C-A-7-3)

$$= 0.994\left\{\frac{2\left[\frac{(29,000 \text{ ksi})(881 \text{ in.}^4)}{14.0 \text{ ft}}\right]}{2\left[\frac{(29,000 \text{ ksi})(1,350 \text{ in.}^4)}{35.0 \text{ ft}}\right]}\right\}$$

$$= 1.62$$

$G_{bottom} = 1.0$ (fixed), from AISC *Specification* Commentary Appendix 7, Section 7.2

From the alignment chart, AISC *Specification* Commentary Figure C-A-7.2, $K$ is approximately 1.4. Because the column available strength tables are based on $L_c$ about the $y$-$y$ axis, the effective column length of the lower segment for use in the table is:

$$L_{cx} = (KL)_x$$

$$= 1.4(14 \text{ ft})$$

$$= 19.6 \text{ ft}$$

$$L_c = \frac{L_{cx}}{\left(\frac{r_x}{r_y}\right)}$$

$$= \frac{19.6 \text{ ft}}{2.44}$$

$$= 8.03 \text{ ft}$$

Conservatively using $L_c = 9$ ft in AISC *Manual* Table 4-1a, the available strength in axial compression of the W14×82 is:

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 940 \text{ kips} > 600 \text{ kips}$ **o.k.** | $\frac{P_n}{\Omega_c} = 626 \text{ kips} > 400 \text{ kips}$ **o.k.** |

A more accurate strength could be determined by interpolation from AISC *Manual* Table 4-1a.

---

# EXAMPLE E.4B W-SHAPE COMPRESSION MEMBER (MOMENT FRAME)

## Given:

Using the effective length method, determine the available strength of the column shown subject to the same gravity loads shown in Example E.4A with the column pinned at the base about the $x$-$x$ axis. All other assumptions remain the same.

![Diagram: Three-story moment frame with:
- Top level (C): W18×50, $P_D = 41.5$ kips, $P_L = 125$ kips, $I_x = 800$ in.⁴, W14×82, $L = 141$ ft, $I_x = 881$ in.⁴
- Mid level (B): W24×55, $P_D = 100$ kips, $P_L = 300$ kips, $I_x = 1,350$ in.⁴, W14×82, $L = 141$ ft, $I_x = 881$ in.⁴
- Base level (A): Pinned support
- Spans: $L = 35$ ft for two bays
- Column heights: 14 ft between levels
- Note: "Webs of columns and girders are in the plane of the frame."]

## Solution:

As determined in Example E.4A, for the column segment B-C between the roof and the floor, the column strength is adequate.

As determined in Example E.4A, for the column segment A-B between the floor and the foundation,

$$G_{top} = 1.62$$

At the base,

$G_{bottom} = 10$ (pinned) from AISC *Specification* Commentary Appendix 7, Section 7.2

Note: this is the only change in the analysis.

From the alignment chart, AISC *Specification* Commentary Figure C-A-7.2, $K$ is approximately equal to 2.0. Because the column available strength tables are based on the effective length, $L_c$, about the $y$-$y$ axis, the effective column length of the segment A-B for use in the table is:

$$L_{cx} = (KL)_x$$

$$= 2.0(14 \text{ ft})$$

$$= 28.0 \text{ ft}$$

From AISC *Manual* Table 4-1a, for a W14×82:

$$\frac{r_x}{r_y} = 2.44$$

---

$$L_c = \frac{L_{cx}}{\left(\frac{r_x}{r_y}\right)}$$

$$= \frac{28.0 \text{ ft}}{2.44}$$

$$= 11.5 \text{ ft}$$

Interpolate the available strength of the W14×82 from AISC *Manual* Table 4-1a.

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 861 \text{ kips} > 600 \text{ kips}$ **o.k.** | $\frac{P_n}{\Omega_c} = 573 \text{ kips} > 400 \text{ kips}$ **o.k.** |

---

# EXAMPLE E.5 DOUBLE-ANGLE COMPRESSION MEMBER WITHOUT SLENDER ELEMENTS

## Given:

Verify the strength of a 2L4×3½×⅜ LLBB (¾ in. separation) strut, ASTM A572/A572M Grade 50, with a length of 8'-0" and pinned ends carrying an axial dead load of 20 kips and live load of 60 kips. Also, calculate the required number of pretensioned bolted or welded intermediate connectors required. The solution will be provided using:

(1) AISC *Manual* Tables
(2) Calculations using AISC *Specification* provisions

![Diagram: Vertical strut with length L = 8'-0", axial loads $P_D = 20$ kips and $P_L = 60$ kips applied at top, pinned support at bottom]

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A572/A572M Grade 50
$F_y = 50$ ksi

From AISC *Manual* Tables 1-7 and 1-15, the geometric properties are as follows:

L4×3½×⅜
$r_z = 0.719$ in.

2L4×3½×⅜ LLBB
$r_x = 1.25$ in.
$r_y = 1.55$ in. for ¾ in. separation
$r_y = 1.69$ in. for ⅜ in. separation

From ASCE/SEI 7, Chapter 2, the required compressive strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(20 \text{ kips}) + 1.6(60 \text{ kips})$ | $P_a = 20 \text{ kips} + 60 \text{ kips}$ |
| $= 120$ kips | $= 80.0$ kips |

(1) AISC *Manual* Table Solution

From AISC *Specification* Commentary Table C-A-7.1, for a pinned-pinned condition, $K = 1.0$. Therefore, $L_{cx} = L_{cy} = KL = 1.0(8 \text{ ft}) = 8.00$ ft. The available strength in axial compression is taken from the upper (X-X Axis) portion of AISC *Manual* Table 4-9:

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 157 \text{ kips} > 120 \text{ kips}$ **o.k.** | $\frac{P_n}{\Omega_c} = 104 \text{ kips} > 80.0 \text{ kips}$ **o.k.** |

For buckling about the $y$-$y$ axis, the values are tabulated for a separation of ¾ in.

To adjust to a separation of ¾ in., $L_{cy}$ is multiplied by the ratio of the $r_y$ for a ¾ in. separation to the $r_y$ for a ¾ in. separation, where $L_{cy} = K_y L_y = 1.0(8 \text{ ft}) = 8.00$ ft. Thus:

---

$$L_{cy} = (8.00 \text{ ft})\left(\frac{1.55 \text{ in.}}{1.69 \text{ in.}}\right)$$

$$= 7.34 \text{ ft}$$

The calculation of the equivalent $L_{cy}$ in the preceding text is a simplified approximation of AISC *Specification* Section E6.1. To ensure a conservative adjustment for a ¾ in. separation, take $L_{cy} = 8$ ft. The available strength in axial compression is taken from the lower (Y-Y Axis) portion of AISC *Manual* Table 4-9 as:

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 165 \text{ kips} > 120 \text{ kips}$ **o.k.** | $\frac{P_n}{\Omega_c} = 110 \text{ kips} > 80.0 \text{ kips}$ **o.k.** |

Therefore, $x$-$x$ axis flexural buckling governs.

*Intermediate Connectors*

From AISC *Manual* Table 4-9, at least two welded or pretensioned bolted intermediate connectors are required. This can be verified as follows:

$a =$ distance between connectors

$$= \frac{(8.00 \text{ ft})(12 \text{ in./ft})}{3 \text{ spaces}}$$

$$= 32.0 \text{ in.}$$

From AISC *Specification* Section E6.2, the effective slenderness ratio of the individual components of the built-up member based upon the distance between intermediate connectors, $a$, must not exceed three-fourths of the governing slenderness ratio of the built-up member.

Therefore,

$$\frac{a}{r_i} \leq \frac{3}{4}\left(\frac{L_c}{r}\right)_{max}$$

Solving for $a$ gives:

$$a \leq \frac{3r_i\left(\frac{L_c}{r}\right)_{max}}{4}$$

$$\frac{L_{cx}}{r_x} = \frac{(8.00 \text{ ft})(12 \text{ in./ft})}{1.25 \text{ in.}}$$

$$= 76.8 \quad \textbf{controls}$$

$$\frac{L_{cy}}{r_y} = \frac{(8.00 \text{ ft})(12 \text{ in./ft})}{1.69 \text{ in.}}$$

$$= 56.8$$

---

$$a = \frac{3r_z\left(\frac{L_c}{r}\right)_{max}}{4}$$

$$= \frac{3(0.719 \text{ in.})(76.8)}{4}$$

$$= 41.4 \text{ in.}$$

Therefore, because $32.0 \text{ in.} < 41.4 \text{ in.}$, two welded or pretensioned bolted connectors are adequate.

Note that one connector would not be adequate because $48.0 \text{ in.} > 41.4 \text{ in.}$

Available strength can also be determined by hand calculations, as demonstrated in the following.

(2) Calculations Using AISC *Specification* Provisions

From AISC *Manual* Tables 1-7 and 1-15, the geometric properties are as follows:

L4×3½×⅜
$r_z = 0.719$ in.
$J = 0.132$ in.⁴
$C_w = 0.134$ in.⁶

2L4×3½×⅜ LLBB (¾ in. separation)
$A_g = 5.36$ in.²
$r_y = 1.69$ in.
$\bar{r}_o = 2.33$ in.
$H = 0.813$

*Slenderness Check*

$$\lambda = \frac{b}{t}$$

$$= \frac{4.00 \text{ in.}}{\frac{3}{8} \text{ in.}}$$

$$= 10.7$$

Determine the limiting slenderness ratio, $\lambda_r$, from AISC *Specification* Table B4.1a, Case 3:

$$\lambda_r = 0.45\sqrt{\frac{E}{F_y}}$$

$$= 0.45\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 10.8$$

$\lambda < \lambda_r$; therefore, there are no slender elements.

For double-angle compression members without slender elements, AISC *Specification* Sections E3, E4, and E6 apply.

The nominal compressive strength, $P_n$, is determined based on the limit states of flexural, torsional, and flexural-torsional buckling.

---

*Flexural Buckling about the $x$-$x$ Axis*

$$\frac{L_{cx}}{r_x} = \frac{(8.00 \text{ ft})(12 \text{ in./ft})}{1.25 \text{ in.}}$$

$$= 76.8$$

$$F_{ex} = \frac{\pi^2 E}{\left(\frac{L_{cx}}{r_x}\right)^2}$$
(*Spec.* Eq. E4-5)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(76.8)^2}$$

$$= 48.5 \text{ ksi}$$

*Flexural Buckling about the $y$-$y$ Axis*

$$\frac{L_{cy}}{r_y} = \frac{(8.00 \text{ ft})(12 \text{ in./ft})}{1.69 \text{ in.}}$$

$$= 56.8$$

Using AISC *Specification* Section E6, compute the modified $L_c/r$ for built up members with pretensioned bolted or welded connectors. Assume two connectors are required.

$$a = \frac{(8.00 \text{ ft})(12 \text{ in./ft})}{3}$$

$$= 32.0 \text{ in.}$$

$r_i = r_z$ (single angle)

$$= 0.719 \text{ in.}$$

$$\frac{a}{r_i} = \frac{32.0 \text{ in.}}{0.719 \text{ in.}}$$

$$= 44.5 > 40$$

Therefore:

$$\left(\frac{L_c}{r}\right)_m = \sqrt{\left(\frac{L_c}{r}\right)_o^2 + \left(\frac{K_i a}{r_i}\right)^2}$$
(*Spec.* Eq. E6-2b)

where $K_i = 0.50$ for angles back-to-back

$$\left(\frac{L_c}{r}\right)_m = \sqrt{(56.8)^2 + \left[\frac{0.50(32.0 \text{ in.})}{0.719 \text{ in.}}\right]^2}$$

$$= 61.0$$

---

$$F_{ey} = \frac{\pi^2 E}{\left(\frac{L_{cy}}{r_y}\right)^2}$$
(*Spec.* Eq. E4-6)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(61.0)^2}$$

$$= 76.9 \text{ ksi}$$

*Torsional and Flexural-Torsional Buckling*

For nonslender double-angle compression members, AISC *Specification* Equation E4-3 applies. The flexural buckling term about the $y$-$y$ axis, $F_{ey}$, was computed in the preceding section.

$$F_{ez} = \left(\frac{\pi^2 EC_w}{L_{cz}^2} + GJ\right)\frac{1}{A_g \bar{r}_o^2}$$
(*Spec.* Eq. E4-7)

$$= \left\{\frac{\pi^2 (29,000 \text{ ksi})(0.134 \text{ in.}^6)}{\left[(8.00 \text{ in.})(12 \text{ in./ft})\right]^2} + (11,200 \text{ ksi})(0.132 \text{ in.}^4)\right\}\frac{1(2 \text{ angles})}{(5.36 \text{ in.}^2)(2.33 \text{ in.})^2}$$

$$= 102 \text{ ksi}$$

$$F_e = \left(\frac{F_{ey} + F_{ez}}{2H}\right)\left[1 - \sqrt{1 - \frac{4F_{ey}F_{ez}H}{(F_{ey} + F_{ez})^2}}\right]$$
(*Spec.* Eq. E4-3)

$$= \left[\frac{76.9 \text{ ksi} + 102 \text{ ksi}}{2(0.813)}\right]\left[1 - \sqrt{1 - \frac{4(76.9 \text{ ksi})(102 \text{ ksi})(0.813)}{(76.9 \text{ ksi} + 102 \text{ ksi})^2}}\right]$$

$$= 60.5 \text{ ksi}$$

*Nominal Stress*

The nominal stress for the member could be controlled by flexural buckling about either the $x$-$x$ axis or $y$-$y$ axis, $F_{ex}$ or $F_{ey}$, respectively. Note that AISC *Specification* Equations E4-5 and E4-6 reflect the same buckling modes as calculated in AISC *Specification* Equation E3-4. Or, the nominal buckling stress for the member could be controlled by torsional or flexural-torsional buckling calculated per AISC *Specification* Equation E4-3. In this example, $F_e$ calculated in accordance with AISC *Specification* Equation E4-5 (or Equation E3-4) is less than that calculated in accordance with AISC *Specification* Equation E4-3 or E4-6, and controls. Therefore:

$$F_e = 48.5 \text{ ksi}$$

$$\frac{F_y}{F_e} = \frac{50 \text{ ksi}}{48.5 \text{ ksi}}$$

$$= 1.03$$

Per the AISC *Specification* Section E3 User Note, the two inequalities for calculating limits of applicability of Sections E3(a) and E3(b) provide the same result for flexural buckling only. When the elastic buckling stress, $F_e$, is controlled by torsional or flexural-torsional buckling, the $L_c/r$ limits would not be applicable unless an equivalent $L_c/r$ ratio is first calculated by substituting the governing $F_e$ into AISC *Specification* Equation E3-4 and solving for $L_c/r$. The $F_y/F_e$ limits may be used regardless of which buckling mode governs.

---

Because $\frac{F_y}{F_e} < 2.25$:

$$F_n = \left(0.658^{\frac{F_y}{F_e}}\right)F_y$$
(*Spec.* Eq. E3-2)

$$= \left(0.658^{1.03}\right)(50 \text{ ksi})$$

$$= 32.5 \text{ ksi}$$

*Compressive Strength*

From AISC *Specification* Section E4, the nominal compressive strength is:

$$P_n = F_n A_g$$
(*Spec.* Eq. E3-1, Eq. E4-1)

$$= (32.5 \text{ ksi})(5.36 \text{ in.}^2)$$

$$= 174 \text{ kips}$$

From AISC *Specification* Section E1, the available compressive strength is:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.90$ | $\Omega_c = 1.67$ |
| $\phi_c P_n = 0.90(174 \text{ kips})$ | $\frac{P_n}{\Omega_c} = \frac{174 \text{ kips}}{1.67}$ |
| $= 157 \text{ kips} > 120 \text{kips}$ **o.k.** | $= 104 \text{ kips} > 80.0 \text{ kips}$ **o.k.** |

*Intermediate Connectors*

Calculations for the required number of intermediate connectors were shown in the preceding section.

---

# EXAMPLE E.6 DOUBLE-ANGLE COMPRESSION MEMBER WITH SLENDER ELEMENTS

## Given:

Determine if a 2L5×3×¼ LLBB (¾ in. separation) strut, ASTM A572/A572M Grade 50, with a length of 8 ft and pinned ends has sufficient available strength to support a dead load of 10 kips and live load of 30 kips in axial compression. Also, calculate the required number of pretensioned bolted or welded intermediate connectors. The solution will be provided using:

(1) AISC *Manual* Tables
(2) Calculations using AISC *Specification* provisions

![Diagram: Vertical strut with length L = 8'-0", axial loads $P_D = 10$ kips and $P_L = 30$ kips applied at top, pinned support at bottom]

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A572/A572M Grade 50
$F_y = 50$ ksi

From AISC *Manual* Tables 1-7 and 1-15, the geometric properties are as follows:

L5×3×¼
$r_z = 0.652$ in.

2L5×3×¼ LLBB
$r_x = 1.62$ in.
$r_y = 1.19$ in. for ¾ in. separation
$r_y = 1.33$ in. for ¾ in. separation

From ASCE/SEI 7, Chapter 2, the required compressive strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(10 \text{ kips}) + 1.6(30 \text{ kips})$ | $P_a = 10 \text{ kips} + 30 \text{ kips}$ |
| $= 60.0$ kips | $= 40.0$ kips |

(1) AISC *Manual* Table Solution

From AISC *Specification* Commentary Table C-A-7.1, for a pinned-pinned condition, $K = 1.0$. Therefore, $L_{cx} = L_{cy} = KL = 1.0(8 \text{ ft}) = 8.00$ ft. The available strength in axial compression is taken from the upper (X-X Axis) portion of AISC *Manual* Table 4-9:

| LRFD | ASD |
|------|-----|
| $\phi_c P_{nx} = 112 \text{ kips} > 60.0 \text{ kips}$ **o.k.** | $\frac{P_{nx}}{\Omega_c} = 74.3 \text{ kips} > 40.0 \text{ kips}$ **o.k.** |

For buckling about the $y$-$y$ axis, the tabulated values are based on a separation of ⅜ in. To adjust for a separation of ¾ in., $L_{cy}$ is multiplied by the ratio of $r_y$ for a ⅜ in. separation to $r_y$ for a ¾ in. separation.

$$L_{cy} = (8.00 \text{ ft})\left(\frac{1.19 \text{ in.}}{1.33 \text{ in.}}\right)$$

$$= 7.16 \text{ ft}$$

---

This calculation of the equivalent $L_{cy}$ does not completely take into account the effect of AISC *Specification* Section E6.1 and is slightly unconservative.

From the lower portion of AISC *Manual* Table 4-9, interpolate for a value at $L_{cy} = 7.16$ ft.

The available strength in compression is:

| LRFD | ASD |
|------|-----|
| $\phi_c P_{ny} = 75.2 \text{ kips} > 60.0 \text{ kips}$ **o.k.** | $\frac{P_{ny}}{\Omega_c} = 50.0 \text{ kips} > 40.0 \text{ kips}$ **o.k.** |

These strengths are approximate due to the linear interpolation from the table and the approximate value of the equivalent $L_{cy}$ noted in the preceding text. These can be compared to the more accurate values calculated in the second part of this example.

*Intermediate Connectors*

From AISC *Manual* Table 4-9, it is determined that at least two welded or pretensioned bolted intermediate connectors are required. This can be confirmed by calculation, as follows:

$a =$ distance between connectors

$$= \frac{(8.00 \text{ ft})(12 \text{ in./ft})}{3 \text{ spaces}}$$

$$= 32.0 \text{ in.}$$

From AISC *Specification* Section E6.2, the effective slenderness ratio of the individual components of the built-up member based upon the distance between intermediate connectors, $a$, must not exceed three-fourths of the governing slenderness ratio of the built-up member.

Therefore,

$$\frac{a}{r_i} \leq \frac{3}{4}\left(\frac{L_c}{r}\right)_{max}$$

Solving for $a$ gives:

$$a \leq \frac{3r_i\left(\frac{L_c}{r}\right)_{max}}{4}$$

$r_i = r_z$

$$= 0.652 \text{ in.}$$

$$\frac{L_{cx}}{r_x} = \frac{(8.00 \text{ ft})(12 \text{ in./ft})}{1.62 \text{ in.}}$$

$$= 59.3$$

$$\frac{L_{cy}}{r_y} = \frac{(8.00 \text{ ft})(12 \text{ in./ft})}{1.33 \text{ in.}}$$

$$= 72.2 \quad \textbf{controls}$$

---

$$a = \frac{3r_z\left(\frac{L_c}{r}\right)_{max}}{4}$$

$$= \frac{3(0.652 \text{ in.})(72.2)}{4}$$

$$= 35.3 \text{ in.}$$

Therefore, because $32.0 \text{ in.} < 35.3 \text{ in.}$, two welded or pretensioned bolted connectors are adequate.

Available strength can also be determined by hand calculations, as determined in the following.

(2) Calculations Using AISC *Specification* Provisions

From AISC *Manual* Tables 1-7 and 1-15, the geometric properties are as follows.

L5×3×¼
$J = 0.0438$ in.⁴
$r_z = 0.652$ in.
$C_w = 0.0606$ in.⁶

2L5×3×¼ LLBB
$A_g = 3.88$ in.²
$r_x = 1.62$ in.
$r_y = 1.33$ in. for ¾ in. separation
$\bar{r}_o = 2.59$ in. for ¾ in. separation
$H = 0.657$ for ¾ in. separation

*Slenderness Check*

For the 5 in. leg:

$$\lambda = \frac{b}{t}$$

$$= \frac{5.00 \text{ in.}}{\frac{1}{4} \text{ in.}}$$

$$= 20.0$$

For the 3 in. leg:

$$\lambda = \frac{b}{t}$$

$$= \frac{3.00 \text{ in.}}{\frac{1}{4} \text{ in.}}$$

$$= 12.0$$

Calculate the limiting slenderness ratio, $\lambda_r$, from AISC *Specification* Table B4.1a, Case 3:

---

$$\lambda_r = 0.45\sqrt{\frac{E}{F_y}}$$

$$= 0.45\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 10.8$$

For both the longer and shorter leg, $\lambda > \lambda_r$, therefore, both legs are classified as a slender element.

For a double-angle compression member with slender elements, AISC *Specification* Section E7 applies. The nominal compressive strength, $P_n$, is determined based on the limit states of flexural, torsional, and flexural-torsional buckling. $A_e$ will be determined by AISC *Specification* Section E7.1.

*Elastic Buckling Stress about the $x$-$x$ Axis*

With $L_{cx} = K_x L_x = 1.0(8 \text{ ft}) = 8.00$ ft:

$$\frac{L_{cx}}{r_x} = \frac{(8.00 \text{ ft})(12 \text{ in./ft})}{1.62 \text{ in.}}$$

$$= 59.3$$

$$F_{ex} = \frac{\pi^2 E}{\left(\frac{L_{cx}}{r_x}\right)^2}$$
(*Spec.* Eq. 3-4 or E4-5)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(59.3)^2}$$

$$= 81.4 \text{ ksi}$$

*Elastic Buckling Stress about the $y$-$y$ Axis*

With $L_{cy} = K_y L_y = 1.0(8 \text{ ft}) = 8.00$ ft:

$$\frac{L_{cy}}{r_y} = \frac{(8.00 \text{ ft})(12 \text{ in./ft})}{1.33 \text{ in.}}$$

$$= 72.2$$

Using AISC *Specification* Section E6, compute the modified $L_{cy}/r_y$ for built-up members with pretensioned bolted or welded connectors. Assuming two connectors are required:

$$a = \frac{(8.00 \text{ ft})(12 \text{ in./ft})}{3}$$

$$= 32.0 \text{ in.}$$

$r_i = r_z$ (single angle)

$$= 0.652 \text{ in.}$$

$$\frac{a}{r_i} = \frac{32.0 \text{ in.}}{0.652 \text{ in.}}$$

$$= 49.1 > 40$$

---

Therefore:

$$\left(\frac{L_c}{r}\right)_m = \sqrt{\left(\frac{L_c}{r}\right)_o^2 + \left(\frac{K_i a}{r_i}\right)^2}$$
(*Spec.* Eq. E6-2b)

where $K_i = 0.50$ for angles back-to-back

$$\left(\frac{L_c}{r}\right)_m = \sqrt{(72.2)^2 + \left[\frac{0.50(32.0 \text{ in.})}{0.652 \text{ in.}}\right]^2}$$

$$= 76.3$$

$$F_{ey} = \frac{\pi^2 E}{\left(\frac{L_{cy}}{r_y}\right)^2}$$
(*Spec.* Eq. E3-4 or E4-6)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(76.3)^2}$$

$$= 49.2 \text{ ksi}$$

*Torsional and Flexural-Torsional Elastic Buckling Stress*

The flexural buckling term about the $y$-$y$ axis, $F_{ey}$, was computed in the preceding section.

$$F_{ez} = \left(\frac{\pi^2 EC_w}{L_{cz}^2} + GJ\right)\frac{1}{A_g \bar{r}_o^2}$$
(*Spec.* Eq. E4-7)

$$= \left\{\frac{\pi^2 (29,000 \text{ ksi})(0.0606 \text{ in.}^6)}{\left[(8.00 \text{ ft})(12 \text{ in./ft})\right]^2} + (11,200 \text{ ksi})(0.0438 \text{ in.}^4)\right\}\frac{1(2 \text{ angles})}{(3.88 \text{ in.}^2)(2.59 \text{ in.})^2}$$

$$= 37.8 \text{ ksi}$$

$$F_e = \left(\frac{F_{ey} + F_{ez}}{2H}\right)\left[1 - \sqrt{1 - \frac{4F_{ey}F_{ez}H}{(F_{ey} + F_{ez})^2}}\right]$$
(*Spec.* Eq. E4-3)

$$= \left[\frac{49.2 \text{ ksi} + 37.8 \text{ ksi}}{2(0.657)}\right]\left[1 - \sqrt{1 - \frac{4(49.2 \text{ ksi})(37.8 \text{ ksi})(0.657)}{(49.2 \text{ ksi} + 37.8 \text{ ksi})^2}}\right]$$

$$= 26.8 \text{ ksi} \quad \textbf{controls}$$

*Nominal Stress*

The nominal stress for the member could be controlled by flexural buckling about either the $x$-$x$ axis or $y$-$y$ axis, $F_{ex}$ or $F_{ey}$, respectively. Note that AISC *Specification* Equations E4-5 and E4-6 reflect the same buckling modes as calculated in AISC *Specification* Equation E3-4. Or, the nominal buckling stress for the member could be controlled by torsional or flexural-torsional buckling calculated per AISC *Specification* Equation E4-3. In this example, $F_e$ calculated in accordance with AISC *Specification* Equation E4-3 is less than that calculated in accordance with AISC *Specification* Equation E4-5 or E4-6, and controls. Therefore:

$$F_e = 26.8 \text{ ksi}$$

---

$$\frac{F_y}{F_e} = \frac{50 \text{ ksi}}{26.8 \text{ ksi}}$$

$$= 1.87$$

Per the AISC *Specification* Section E3 User Note, the two inequalities for calculating limits of applicability of Sections E3(a) and E3(b) provide the same result for flexural buckling only. When the elastic buckling stress, $F_e$, is controlled by torsional or flexural-torsional buckling, the $L_c/r$ limits would not be applicable unless an equivalent $L_c/r$ ratio is first calculated by substituting the governing $F_e$ into AISC *Specification* Equation E3-4 and solving for $L_c/r$. The $F_y/F_e$ limits may be used regardless of which buckling mode governs.

Because $\frac{F_y}{F_e} < 2.25$:

$$F_n = \left(0.658^{\frac{F_y}{F_e}}\right)F_y$$
(*Spec.* Eq. E3-2)

$$= \left(0.658^{1.87}\right)(50 \text{ ksi})$$

$$= 22.9 \text{ ksi}$$

*Effective Area*

Determine the limits of applicability for local buckling in accordance with AISC *Specification* Section E7.1. Both the longer and shorter leg were shown previously to be slender; therefore, the limits of AISC *Specification* Section E7.1 need to be evaluated.

$$\lambda_r \sqrt{\frac{F_y}{F_n}} = 10.8\sqrt{\frac{50 \text{ ksi}}{22.9 \text{ ksi}}}$$

$$= 16.0$$

For the 3 in. leg:

$$\lambda = 12.0$$

Because $\lambda = 12.0 < 16.0$, the full area of the shorter leg is effective.

For the 5 in. leg:

$$\lambda = 20.0$$

Because $\lambda = 20.0 > 16.0$, determine the effective width imperfection adjustment factors per AISC *Specification* Table E7.1, Case (c).

$$c_1 = 0.22$$
$$c_2 = 1.49$$

Determine the elastic local buckling stress from AISC *Specification* Section E7.1.

---

$$F_{el} = \left[c_2 \frac{\lambda_r}{\lambda}\right]^2 F_y$$
(*Spec.* Eq. E7-5)

$$= \left[1.49\left(\frac{10.8}{20.0}\right)\right]^2 (50 \text{ ksi})$$

$$= 32.4 \text{ ksi}$$

Determine the effective width of the angle leg and the resulting effective area.

$$b_e = b\left[1 - c_1\sqrt{\frac{F_{el}}{F_n}}\right]\sqrt{\frac{F_{el}}{F_n}}$$
(*Spec.* Eq. E7-3)

$$= (5.00 \text{ in.})\left[1 - 0.22\sqrt{\frac{32.4 \text{ ksi}}{22.9 \text{ ksi}}}\right]\sqrt{\frac{32.4 \text{ ksi}}{22.9 \text{ ksi}}}$$

$$= 4.39 \text{ in.}$$

$$A_e = A_g - t\sum(b - b_e)$$

$$= 3.88 \text{ in.}^2 - (\frac{1}{4} \text{ in.})(5.00 \text{ in.} - 4.39 \text{ in.})(2 \text{ angles})$$

$$= 3.58 \text{ in.}^2$$

*Compressive Strength*

From AISC *Specification* Section E7, the nominal compressive strength is:

$$P_n = F_n A_e$$
(*Spec.* Eq. E7-1)

$$= (22.9 \text{ ksi})(3.58 \text{ in.}^2)$$

$$= 82.0 \text{ kips}$$

From AISC *Specification* Section E1, the available compressive strength is:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.90$ | $\Omega_c = 1.67$ |
| $\phi_c P_n = 0.90(82.0 \text{ kips})$ | $\frac{P_n}{\Omega_c} = \frac{82.0 \text{ kips}}{1.67}$ |
| $= 73.8 \text{ kips} > 60.0 \text{ kips}$ **o.k.** | $= 49.1 \text{ kips} > 40.0 \text{ kips}$ **o.k.** |

*Intermediate Connectors*

Calculations for the required number of intermediate connectors were shown in the preceding section.

---

# EXAMPLE E.7 WT COMPRESSION MEMBER WITHOUT SLENDER ELEMENTS

## Given:

Select an ASTM A992/A992M nonslender WT-shape compression member with a length of 20 ft to support a dead load of 20 kips and live load of 60 kips in axial compression. The ends are pinned. The solution will be provided using:

(1) AISC *Manual* Tables
(2) Calculations using AISC *Specification* provisions

![Diagram: Vertical member with length L = 20'-0", axial loads $P_D = 20$ kips and $P_L = 60$ kips applied at top, pinned support at bottom]

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50$ ksi

From ASCE/SEI 7, Chapter 2, the required compressive strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(20 \text{ kips}) + 1.6(60 \text{ kips})$ | $P_a = 20 \text{ kips} + 60 \text{ kips}$ |
| $= 120$ kips | $= 80.0$ kips |

(1) AISC *Manual* Table Solution

From AISC *Specification* Commentary Table C-A-7.1, for a pinned-pinned condition, $K = 1.0$. Therefore, $L_{cx} = L_{cy} = KL = 1.0(20 \text{ ft}) = 20.0$ ft.

Select the lightest nonslender member from AISC *Manual* Table 4-7 with sufficient available strength about both the $x$-$x$ axis (upper portion of the table) and the $y$-$y$ axis (lower portion of the table) to support the required strength.

Try a WT7×34.

The available strength in compression is:

| LRFD | ASD |
|------|-----|
| $\phi_c P_{nx} = 128 \text{ kips} > 120 \text{ kips}$ **o.k. controls** | $\frac{P_{nx}}{\Omega_c} = 85.5 \text{ kips} > 80.0 \text{ kips}$ **o.k. controls** |
| $\phi_c P_{ny} = 222 \text{ kips} > 120 \text{ kips}$ **o.k.** | $\frac{P_{ny}}{\Omega_c} = 147 \text{ kips} > 80.0 \text{ kips}$ **o.k.** |

Available strength can also be determined by hand calculations, as demonstrated in the following.

(2) Calculation Using AISC *Specification* Provisions

From AISC *Manual* Table 1-8, the geometric properties are as follows.

WT7×34
$A_g = 10.0$ in.²
$I_x = 32.6$ in.⁴
$I_y = 60.7$ in.⁴

---

$J = 1.50$ in.⁴
$r_x = 1.81$ in.
$r_y = 2.46$ in.
$t_w = 0.415$ in.
$t_f = 0.720$ in.
$\overline{y} = 1.29$ in.
$C_w = 3.21$ in.⁶
$\frac{b_f}{2t_f} = 6.97$
$\frac{d}{t_w} = 16.9$

*Stem Slenderness Check*

$$\lambda = \frac{d}{t_w}$$

$$= 16.9$$

Determine the stem limiting slenderness ratio, $\lambda_r$, from AISC *Specification* Table B4.1a, Case 4:

$$\lambda_r = 0.75\sqrt{\frac{E}{F_y}}$$

$$= 0.75\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 18.1$$

$\lambda < \lambda_r$; therefore, the stem is not slender.

*Flange Slenderness Check*

$$\lambda = \frac{b_f}{2t_f}$$

$$= 6.97$$

Determine the flange limiting slenderness ratio, $\lambda_r$, from AISC *Specification* Table B4.1a, Case 1:

$$\lambda_r = 0.56\sqrt{\frac{E}{F_y}}$$

$$= 0.56\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 13.5$$

$\lambda < \lambda_r$; therefore, the flange is not slender.

There are no slender elements.

For compression members without slender elements, AISC *Specification* Sections E3 and E4 apply. The nominal compressive strength, $P_n$, is determined based on the limit states of flexural, torsional, and flexural-torsional buckling.

---

*Elastic Flexural Buckling Stress about the $x$-$x$ Axis*

$$\frac{L_{cx}}{r_x} = \frac{(20.0 \text{ ft})(12 \text{ in./ft})}{1.81 \text{ in.}}$$

$$= 133$$

$$F_{ex} = \frac{\pi^2 E}{\left(\frac{L_{cx}}{r_x}\right)^2}$$
(*Spec.* Eq. E3-4 or E4-5)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(133)^2}$$

$$= 16.2 \text{ ksi} \quad \textbf{controls}$$

*Elastic Flexural Buckling Stress about the $y$-$y$ Axis*

$$\frac{L_{cy}}{r_y} = \frac{(20.0 \text{ ft})(12 \text{ in./ft})}{2.46 \text{ in.}}$$

$$= 97.6$$

$$F_{ey} = \frac{\pi^2 E}{\left(\frac{L_{cy}}{r_y}\right)^2}$$
(*Spec.* Eq. E3-4 or E4-6)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(97.6)^2}$$

$$= 30.0 \text{ ksi}$$

*Torsional and Flexural-Torsional Elastic Buckling Stress*

Because the WT7×34 section does not have any slender elements, AISC *Specification* Section E4 will be applicable for torsional and flexural-torsional buckling. $F_e$ will be calculated using AISC *Specification* Equation E4-3. The flexural buckling term about the $y$-$y$ axis, $F_{ey}$, was computed in the preceding section.

$$x_o = 0$$

$$y_o = \overline{y} - \frac{t_f}{2}$$

$$= 1.29 \text{ in.} - \frac{0.720 \text{ in.}}{2}$$

$$= 0.930 \text{ in.}$$

$$\bar{r}_o^2 = x_o^2 + y_o^2 + \frac{I_x + I_y}{A_g}$$
(*Spec.* Eq. E4-9)

$$= 0 + (0.930 \text{ in.})^2 + \frac{32.6 \text{ in.}^4 + 60.7 \text{ in.}^4}{10.0 \text{ in.}^2}$$

$$= 10.2 \text{ in.}^2$$

---

$$F_{ez} = \left(\frac{\pi^2 EC_w}{L_{cz}^2} + GJ\right)\frac{1}{A_g \bar{r}_o^2}$$
(*Spec.* Eq. E4-7)

$$= \left\{\frac{\pi^2 (29,000 \text{ ksi})(3.21 \text{ in.}^6)}{\left[(20.0 \text{ ft})(12 \text{ in./ft})\right]^2} + (11,200 \text{ ksi})(1.50 \text{ in.}^4)\right\}\frac{1}{(10.0 \text{ in.}^2)(10.2 \text{ in.}^2)}$$

$$= 165 \text{ ksi}$$

$$H = 1 - \frac{x_o^2 + y_o^2}{\bar{r}_o^2}$$
(*Spec.* Eq. E4-8)

$$= 1 - \frac{0 + (0.930 \text{ in.})^2}{10.2 \text{ in.}^2}$$

$$= 0.915$$

$$F_e = \left(\frac{F_{ey} + F_{ez}}{2H}\right)\left[1 - \sqrt{1 - \frac{4F_{ey}F_{ez}H}{(F_{ey} + F_{ez})^2}}\right]$$
(*Spec.* Eq. E4-3)

$$= \left[\frac{30.0 \text{ ksi} + 165 \text{ ksi}}{2(0.915)}\right]\left[1 - \sqrt{1 - \frac{4(30.0 \text{ ksi})(165 \text{ ksi})(0.915)}{(30.0 \text{ ksi} + 165 \text{ ksi})^2}}\right]$$

$$= 29.5 \text{ ksi}$$

*Nominal Stress*

The nominal stress for the member could be controlled by flexural buckling about either the $x$-$x$ axis or $y$-$y$ axis, $F_{ex}$ or $F_{ey}$, respectively. Note that AISC *Specification* Equations E4-5 and E4-6 reflect the same buckling modes as calculated in AISC *Specification* Equation E3-4. Or, the nominal buckling stress for the member could be controlled by torsional or flexural-torsional buckling calculated per AISC *Specification* Equation E4-3. In this example, $F_e$ calculated in accordance with AISC *Specification* Equation E4-5 is less than that calculated in accordance with AISC *Specification* Equation E4-3 or E4-6 and controls. Therefore:

$$F_e = 16.2 \text{ ksi}$$

$$\frac{F_y}{F_e} = \frac{50 \text{ ksi}}{16.2 \text{ ksi}}$$

$$= 3.09$$

Per the AISC *Specification* Section E3 User Note for, the two inequalities for calculating limits of applicability of Sections E3(a) and E3(b) provide the same result for flexural buckling only. When the elastic buckling stress, $F_e$, is controlled by torsional or flexural-torsional buckling, the $L_c/r$ limits would not be applicable unless an equivalent $L_c/r$ ratio is first calculated by substituting the governing $F_e$ into AISC *Specification* Equation E3-4 and solving for $L_c/r$. The $F_y/F_e$ limits may be used regardless of which buckling mode governs.

Because $\frac{F_y}{F_e} > 2.25$:

---

$$F_n = 0.877F_e$$
(*Spec.* Eq. E3-3)

$$= 0.877(16.2 \text{ ksi})$$

$$= 14.2 \text{ ksi}$$

*Compressive Strength*

From AISC *Specification* Section E3, the nominal compressive strength is:

$$P_n = F_n A_g$$
(*Spec.* Eq. E3-1)

$$= (14.2 \text{ ksi})(10.0 \text{ in.}^2)$$

$$= 142 \text{ kips}$$

From AISC *Specification* Section E1, the available compressive strength is:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.90$ | $\Omega_c = 1.67$ |
| $\phi_c P_n = 0.90(142 \text{ kips})$ | $\frac{P_n}{\Omega_c} = \frac{142 \text{ kips}}{1.67}$ |
| $= 128 \text{ kips} > 120 \text{ kips}$ **o.k.** | $= 85.0 \text{ kips} > 80.0 \text{ kips}$ **o.k.** |

---

# EXAMPLE E.8 WT COMPRESSION MEMBER WITH SLENDER ELEMENTS

## Given:

Select an ASTM A992/A992M WT-shape compression member with a length of 20 ft to support a dead load of 6 kips and live load of 18 kips in axial compression. The ends are pinned. The solution will be provided using:

(1) AISC *Manual* Tables
(2) Calculations using AISC *Specification* provisions

![Diagram: Vertical member with length L = 20'-0", axial loads $P_D = 6$ kips and $P_L = 18$ kips applied at top, pinned support at bottom]

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50$ ksi

From ASCE/SEI 7, Chapter 2, the required compressive strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(6 \text{ kips}) + 1.6(18 \text{ kips})$ | $P_a = 6 \text{ kips} + 18 \text{ kips}$ |
| $= 36.0$ kips | $= 24.0$ kips |

(1) AISC *Manual* Table Solution

From AISC *Specification* Commentary Table C-A-7.1, for a pinned-pinned condition, $K = 1.0$. Therefore, $L_{cx} = L_{cy} = KL = 1.0(20 \text{ ft}) = 20.0$ ft.

Select the lightest member from AISC *Manual* Table 4-7 with sufficient available strength about the both the $x$-$x$ axis (upper portion of the table) and the $y$-$y$ axis (lower portion of the table) to support the required strength.

Try a WT7×15.

The available strength in axial compression from AISC *Manual* Table 4-7 is:

| LRFD | ASD |
|------|-----|
| $\phi_c P_{nx} = 74.3 \text{ kips} > 36.0 \text{ kips}$ **o.k.** | $\frac{P_{nx}}{\Omega_c} = 49.4 \text{ kips} > 24.0 \text{ kips}$ **o.k.** |
| $\phi_c P_{ny} = 36.6 \text{ kips} > 36.0 \text{ kips}$ **o.k. controls** | $\frac{P_{ny}}{\Omega_c} = 24.4 \text{ kips} > 24.0 \text{ kips}$ **o.k. controls** |

Available strength can also be determined by hand calculations, as demonstrated in the following.

(2) Calculation Using AISC *Specification* Provisions

From AISC *Manual* Table 1-8, the geometric properties are as follows:

WT7×15
$A_g = 4.42$ in.²
$I_x = 19.0$ in.⁴
$I_y = 9.79$ in.⁴

---

$J = 0.190$ in.⁴
$r_x = 2.07$ in.
$r_y = 1.49$ in.
$t_w = 0.270$ in.
$t_f = 0.385$ in.
$\overline{y} = 1.58$ in.
$C_w = 0.287$ in.⁶
$\frac{b_f}{2t_f} = 8.74$
$\frac{d}{t_w} = 25.6$

*Stem Slenderness Check*

$$\lambda = \frac{d}{t_w}$$

$$= 25.6$$

Determine stem limiting slenderness ratio, $\lambda_r$, from AISC *Specification* Table B4.1a, Case 4:

$$\lambda_r = 0.75\sqrt{\frac{E}{F_y}}$$

$$= 0.75\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 18.1$$

$\lambda > \lambda_r$; therefore, the stem is slender.

*Flange Slenderness Check*

$$\lambda = \frac{b_f}{2t_f}$$

$$= 8.74$$

Determine flange limiting slenderness ratio, $\lambda_r$, from AISC *Specification* Table B4.1a, Case 1:

$$\lambda_r = 0.56\sqrt{\frac{E}{F_y}}$$

$$= 0.56\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 13.5$$

$\lambda < \lambda_r$; therefore, the flange is not slender.

Because this WT7×15 has a slender web, AISC *Specification* Section E7 is applicable. The nominal compressive strength, $P_n$, is determined based on the limit states of flexural, torsional, and flexural-torsional buckling.

---

*Elastic Flexural Buckling Stress about the $x$-$x$ Axis*

$$\frac{L_{cx}}{r_x} = \frac{(20.0 \text{ ft})(12 \text{ in./ft})}{2.07 \text{ in.}}$$

$$= 116$$

$$F_{ex} = \frac{\pi^2 E}{\left(\frac{L_{cx}}{r_x}\right)^2}$$
(*Spec.* Eq. E3-4 or E4-5)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(116)^2}$$

$$= 21.3 \text{ ksi}$$

*Elastic Flexural Buckling Stress about the $y$-$y$ Axis*

$$\frac{L_{cy}}{r_y} = \frac{(20.0 \text{ ft})(12 \text{ in./ft})}{1.49 \text{ in.}}$$

$$= 161$$

$$F_{ey} = \frac{\pi^2 E}{\left(\frac{L_{cy}}{r_y}\right)^2}$$
(*Spec.* Eq. E3-4 or E4-6)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(161)^2}$$

$$= 11.0 \text{ ksi}$$

*Torsional and Flexural-Torsional Elastic Buckling Stress*

$F_e$ will be calculated using AISC *Specification* Equation E4-3. The flexural buckling term about the $y$-$y$ axis, $F_{ey}$, was computed in the preceding section.

$$x_o = 0$$

$$y_o = \overline{y} - \frac{t_f}{2}$$

$$= 1.58 \text{ in.} - \frac{0.385 \text{ in.}}{2}$$

$$= 1.39 \text{ in.}$$

$$\bar{r}_o^2 = x_o^2 + y_o^2 + \frac{I_x + I_y}{A_g}$$
(*Spec.* Eq. E4-9)

$$= 0 + (1.39 \text{ in.})^2 + \frac{19.0 \text{ in.}^4 + 9.79 \text{ in.}^4}{4.42 \text{ in.}^2}$$

$$= 8.45 \text{ in.}^2$$

---

$$F_{ez} = \left(\frac{\pi^2 EC_w}{L_{cz}^2} + GJ\right)\frac{1}{A_g \bar{r}_o^2}$$
(*Spec.* Eq. E4-7)

$$= \left\{\frac{\pi^2 (29,000 \text{ ksi})(0.287 \text{ in.}^6)}{\left[(20.0 \text{ ft})(12 \text{ in./ft})\right]^2} + (11,200 \text{ ksi})(0.190 \text{ in.}^4)\right\}\frac{1}{(4.42 \text{ in.}^2)(8.45 \text{ in.}^2)}$$

$$= 57.0 \text{ ksi}$$

$$H = 1 - \frac{x_o^2 + y_o^2}{\bar{r}_o^2}$$
(*Spec.* Eq. E4-8)

$$= 1 - \frac{0 + (1.39 \text{ in.})^2}{8.45 \text{ in.}^2}$$

$$= 0.771$$

$$F_e = \left(\frac{F_{ey} + F_{ez}}{2H}\right)\left[1 - \sqrt{1 - \frac{4F_{ey}F_{ez}H}{(F_{ey} + F_{ez})^2}}\right]$$
(*Spec.* Eq. E4-3)

$$= \left[\frac{11.0 \text{ ksi} + 57.0 \text{ ksi}}{2(0.771)}\right]\left[1 - \sqrt{1 - \frac{4(11.0 \text{ ksi})(57.0 \text{ ksi})(0.771)}{(11.0 \text{ ksi} + 57.0 \text{ ksi})^2}}\right]$$

$$= 10.5 \text{ ksi} \quad \textbf{controls}$$

*Nominal Stress*

The nominal stress for the member could be controlled by flexural buckling about either the $x$-$x$ axis or $y$-$y$ axis, $F_{ex}$ or $F_{ey}$, respectively. Note that AISC *Specification* Equations E4-5 and E4-6 reflect the same buckling modes as calculated in AISC *Specification* Equation E3-4. Or, the nominal buckling stress for the member could be controlled by torsional or flexural-torsional buckling calculated per AISC *Specification* Equation E4-3. In this example, $F_e$ calculated in accordance with AISC *Specification* Equation E4-3 is less than that calculated in accordance with AISC *Specification* Equation E4-5 or E4-6 and controls. Therefore:

$$F_e = 10.5 \text{ ksi}$$

$$\frac{F_y}{F_e} = \frac{50 \text{ ksi}}{10.5 \text{ ksi}}$$

$$= 4.76$$

Per the AISC *Specification* Section E3 User Note, the two inequalities for calculating limits of applicability of Sections E3(a) and E3(b) provide the same result for flexural buckling only. When the elastic buckling stress, $F_e$, is controlled by torsional or flexural-torsional buckling, the $L_c/r$ limits would not be applicable unless an equivalent $L_c/r$ ratio is first calculated by substituting the governing $F_e$ into AISC *Specification* Equation E3-4 and solving for $L_c/r$. The $F_y/F_e$ limits may be used regardless of which buckling mode governs.

Because $\frac{F_y}{F_e} > 2.25$:

---

$$F_n = 0.877F_e$$
(*Spec.* Eq. E3-3)

$$= 0.877(10.5 \text{ ksi})$$

$$= 9.21 \text{ ksi}$$

*Effective Area*

Because this section was found to have a slender element, the limits of AISC *Specification* Section E7.1 must be evaluated to determine if there is a reduction in effective area due to local buckling. Because the flange was found to not be slender, no reduction in effective area due to local buckling in the flange is required. Only a reduction in effective area due to local buckling in the stem may be required.

$$\lambda = 25.6$$

$$\lambda_r \sqrt{\frac{F_y}{F_n}} = 18.1\sqrt{\frac{50 \text{ ksi}}{9.21 \text{ ksi}}}$$

$$= 42.2$$

Because $\lambda < \lambda_r \sqrt{\frac{F_y}{F_n}}$,

$$b_e = b$$
(*Spec.* Eq. E7-2)

There is no reduction in effective area due to local buckling of the stem at the critical stress level and $A_e = A_g$.

*Compressive Strength*

From AISC *Specification* Section E7, the nominal compressive strength is:

$$P_n = F_n A_e$$
(*Spec.* Eq. E7-1)

$$= (9.21 \text{ ksi})(4.42 \text{ in.}^2)$$

$$= 40.7 \text{ kips}$$

From AISC *Specification* Section E1, the available compressive strength is:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.90$ | $\Omega_c = 1.67$ |
| $\phi_c P_n = 0.90(40.7 \text{ kips})$ | $\frac{P_n}{\Omega_c} = \frac{40.7 \text{ kips}}{1.67}$ |
| $= 36.6 \text{ kips} > 36.0 \text{ kips}$ **o.k.** | $= 24.4 \text{ kips} > 24.0 \text{ kips}$ **o.k.** |

---

# EXAMPLE E.9 RECTANGULAR HSS COMPRESSION MEMBER WITHOUT SLENDER ELEMENTS

## Given:

Select an ASTM A500/A500M Grade C rectangular HSS compression member with a length of 20 ft to support a dead load of 85 kips and live load of 255 kips in axial compression. The base is fixed, and the top is pinned. The solution will be provided using:

(1) AISC *Manual* Tables
(2) Calculations using AISC *Specification* provisions

![Diagram: Vertical member with length L = 20'-0", axial loads $P_D = 85$ kips and $P_L = 255$ kips applied at top, fixed support at bottom]

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A500/A500M Grade C, rectangular HSS
$F_y = 50$ ksi

From ASCE/SEI 7, Chapter 2, the required compressive strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(85 \text{ kips}) + 1.6(255 \text{ kips})$ | $P_a = 85 \text{ kips} + 255 \text{ kips}$ |
| $= 510$ kips | $= 340$ kips |

(1) AISC *Manual* Table Solution

From AISC *Specification* Commentary Table C-A-7.1, for a fixed-pinned condition, $K_x = K_y = 0.80$.

$$L_c = K_x L_x$$

$$= K_y L_y$$

$$= 0.80(20 \text{ ft})$$

$$= 16.0 \text{ ft}$$

Enter AISC *Manual* Table 4-3 for rectangular sections.

Try an HSS12×10×⅜.

From AISC *Manual* Table 4-3, the available strength in axial compression is:

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 556 \text{ kips} > 510 \text{ kips}$ **o.k.** | $\frac{P_n}{\Omega_c} = 370 \text{ kips} > 340 \text{ kips}$ **o.k.** |

Available strength can also be determined by hand calculations, as demonstrated in the following.

(2) Calculation Using AISC *Specification* Provisions

From AISC *Manual* Table 1-11, the geometric properties are as follows:

HSS12×10×⅜
$A_g = 14.6$ in.²
$r_x = 4.61$ in.

---

$r_y = 4.01$ in.
$b/t = 25.7$
$h/t = 31.4$

*Slenderness Check*

Determine the wall limiting slenderness ratio, $\lambda_r$, from AISC *Specification* Table B4.1a, Case 6:

$$\lambda_r = 1.40\sqrt{\frac{E}{F_y}}$$

$$= 1.40\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 33.7$$

For the narrow side:

$$\lambda = b/t$$

$$= 25.7$$

For the wide side:

$$\lambda = h/t$$

$$= 31.4$$

$\lambda < \lambda_r$; therefore, the section does not contain slender elements.

*Elastic Buckling Stress*

Because $r_y < r_x$ and $L_{cx} = L_{cy}$, $r_y$ will govern the available strength.

$$\frac{L_{cy}}{r_y} = \frac{(16.0 \text{ ft})(12 \text{ in./ft})}{4.01 \text{ in.}}$$

$$= 47.9$$

$$F_e = \frac{\pi^2 E}{\left(\frac{L_c}{r}\right)^2}$$
(*Spec.* Eq. E3-4)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(47.9)^2}$$

$$= 125 \text{ ksi}$$

*Nominal Stress*

Determine the applicable equation from AISC *Specification* Section E3:

$$4.71\sqrt{\frac{E}{F_y}} = 4.71\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 113 > 47.9$$

---

Therefore, use AISC *Specification* Equation E3-2.

$$F_n = \left(0.658^{\frac{F_y}{F_e}}\right)F_y$$
(*Spec.* Eq. E3-2)

$$= \left(0.658^{\frac{50 \text{ ksi}}{125 \text{ ksi}}}\right)(50 \text{ ksi})$$

$$= 42.3 \text{ ksi}$$

*Compressive Strength*

From AISC *Specification* Section E3, the nominal compressive strength is:

$$P_n = F_n A_g$$
(*Spec.* Eq. E3-1)

$$= (42.3 \text{ ksi})(14.6 \text{ in.}^2)$$

$$= 618 \text{ kips}$$

From AISC *Specification* Section E1, the available compressive strength is:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.90$ | $\Omega_c = 1.67$ |
| $\phi_c P_n = 0.90(618 \text{ kips})$ | $\frac{P_n}{\Omega_c} = \frac{618 \text{ kips}}{1.67}$ |
| $= 556 \text{ kips} > 510 \text{ kips}$ **o.k.** | $= 370 \text{ kips} > 340 \text{ kips}$ **o.k.** |

---

# EXAMPLE E.10 RECTANGULAR HSS COMPRESSION MEMBER WITH SLENDER ELEMENTS

## Given:

Using the AISC *Specification* provisions, calculate the available strength of an HSS12×8×⅛ compression member with an effective length of $L_c = 24$ ft with respect to both axes. The base and top are both pinned. Use ASTM A500/A500M Grade C.

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A500/A500M Grade C, rectangular HSS
$F_y = 50$ ksi

From AISC *Manual* Table 1-11 the geometric properties of an HSS12×8×⅛ are as follows:

$A_g = 6.76$ in.²
$t = 0.174$ in.
$r_x = 4.56$ in.
$r_y = 3.35$ in.
$b/t = 43.0$
$h/t = 66.0$

*Slenderness Check*

Calculate the limiting slenderness ratio, $\lambda_r$, from AISC *Specification* Table B4.1a, Case 6 for walls of rectangular HSS.

$$\lambda_r = 1.40\sqrt{\frac{E}{F_y}}$$

$$= 1.40\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 33.7$$

Determine the width-to-thickness ratios of the HSS walls.

For the narrow side:

$$\lambda = b/t$$

$$= 43.0$$

$\lambda > \lambda_r$; therefore, the walls are slender.

For the wide side:

$$\lambda = h/t$$

$$= 66.0$$

$\lambda > \lambda_r$; therefore, the walls are slender.

All walls of the HSS12×8×⅛ are slender elements, and the provisions of AISC *Specification* Section E7 apply.

---

*Nominal Stress*

From AISC *Specification* Section E7, the nominal stress, $F_n$, is calculated using the gross section properties and following the provisions of AISC *Specification* Section E3. The effective slenderness ratio about the $y$-axis will control. From AISC *Specification* Commentary Table C-A-7.1, for a pinned-pinned condition, $K = 1.0$. Therefore, $L_{cy} = K_y L_y = 1.0(24 \text{ ft}) = 24.0$ ft.

$$\left(\frac{L_c}{r}\right)_{max} = \frac{L_{cy}}{r_y}$$

$$= \frac{(24.0 \text{ ft})(12 \text{ in./ft})}{3.35 \text{ in.}}$$

$$= 86.0$$

$$4.71\sqrt{\frac{E}{F_y}} = 4.71\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 113 > 86.0$$

Therefore, use AISC *Specification* Equation E3-2.

$$F_e = \frac{\pi^2 E}{\left(\frac{L_c}{r}\right)^2}$$
(*Spec.* Eq. E3-4)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(86.0)^2}$$

$$= 38.7 \text{ ksi}$$

$$F_n = \left(0.658^{\frac{F_y}{F_e}}\right)F_y$$
(*Spec.* Eq. E3-2)

$$= \left[0.658^{\left(\frac{50 \text{ ksi}}{38.7 \text{ ksi}}\right)}\right](50 \text{ ksi})$$

$$= 29.1 \text{ ksi}$$

*Effective Area*

Compute the effective wall widths, $h_e$ and $b_e$, in accordance with AISC *Specification* Section E7.1. Compare $\lambda$ for each wall with the following limit to determine if a local buckling reduction applies.

$$\lambda_r \sqrt{\frac{F_y}{F_n}} = 33.7\sqrt{\frac{50 \text{ ksi}}{29.1 \text{ ksi}}}$$

$$= 44.2$$

For the narrow walls:

$$\lambda = b/t$$

$$= 43.0 < 44.2$$

---

Therefore, the narrow wall width does not need to be reduced $(b_e = b)$ per AISC *Specification* Equation E7-2. For the wide walls:

$$\lambda = h/t$$

$$= 66.0 > 44.2$$

Therefore, use AISC *Specification* Equation E7-3, with

$$h = (h/t)t$$

$$= (66.0)(0.174 \text{ in.})$$

$$= 11.5 \text{ in.}$$

The effective width imperfection adjustment factors, $c_1$ and $c_2$, are selected from AISC *Specification* Table E7.1, Case (b):

$$c_1 = 0.20$$
$$c_2 = 1.38$$

$$F_{el} = \left[c_2 \frac{\lambda_r}{\lambda}\right]^2 F_y$$
(*Spec.* Eq. E7-5)

$$= \left[1.38\left(\frac{33.7}{66.0}\right)\right]^2 (50 \text{ ksi})$$

$$= 24.8 \text{ ksi}$$

$$h_e = h\left[1 - c_1\sqrt{\frac{F_{el}}{F_n}}\right]\sqrt{\frac{F_{el}}{F_n}}$$
(*Spec.* Eq. E7-3)

$$= (11.5 \text{ in.})\left[1 - 0.20\sqrt{\frac{24.8 \text{ ksi}}{29.1 \text{ ksi}}}\right]\sqrt{\frac{24.8 \text{ ksi}}{29.1 \text{ ksi}}}$$

$$= 8.66 \text{ in.}$$

The effective area, $A_e$, is determined using the effective width $h_e = 8.66$ in. and the design wall thickness $t = 0.174$ in. As shown in Figure E.10-1, $h - h_e$ is the width of the wall segments that must be reduced from the gross area, $A$, to compute the effective area, $A_e$. Note that a similar reduction would be required for the narrow walls if $b_e < b$.

![Diagram: Cross-section of HSS showing effective width reduction. Height H with effective height $h_e$ indicated, and regions marked for reduction $(h - h_e)$]

*Fig. E.10-1. HSS Effective Area.*

---

$$A_e = A_g - 2(h - h_e)t$$

$$= 6.76 \text{ in.}^2 - 2(11.5 \text{ in.} - 8.66 \text{ in.})(0.174 \text{ in.})$$

$$= 5.77 \text{ in.}^2$$

*Available Compressive Strength*

The effective area is used to compute nominal compressive strength:

$$P_n = F_n A_e$$
(*Spec.* Eq. E7-1)

$$= (29.1 \text{ ksi})(5.77 \text{ in.}^2)$$

$$= 168 \text{ kips}$$

From AISC *Specification* Section E1, the available compressive strength is:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.90$ | $\Omega_c = 1.67$ |
| $\phi_c P_n = 0.90(168 \text{ kips})$ | $\frac{P_n}{\Omega_c} = \frac{168 \text{ kips}}{1.67}$ |
| $= 151$ kips | $= 101$ kips |

*Discussion*

The width-to-thickness criterion, $\lambda_r = 1.40\sqrt{\frac{E}{F_y}}$ for HSS in Table B4.1a is based on the assumption that the element will be stressed to $F_y$. If the nominal stress is less than $F_y$, which it always is for compression members of reasonable length, wall local buckling may or may not occur before member flexural buckling occurs. For the case where the flexural buckling stress is low enough, wall local buckling will not occur. This is the case addressed in AISC *Specification* Section E7.1(a). For members where the flexural buckling stress is high enough, wall local buckling will occur. This is the case addressed in AISC *Specification* Section E7.1(a).

The HSS12×8×⅛ in this example is slender according to Table B4.1a. For effective length $L_c = 24.0$ ft, the flexural buckling nominal stress was $F_n = 29.1$ ksi. By Section E7.1, at $F_n = 29.1$ ksi, the wide wall effective width must be determined but the narrow wall is fully effective. Thus, the axial strength is reduced because of local buckling of the wide wall. Table E.10-1 repeats the example analysis for two other column effective lengths and compares those results to the results for $L_c = 24$ ft calculated previously. For $L_c = 18.0$ ft, the nominal stress, $F_n = 36.9$ ksi, is high enough that both the wide and narrow walls must have their effective width determined according to Equation E7-3. For $L_c = 40.0$ ft, the nominal stress, $F_n = 12.3$ ksi, is low enough that there will be no local buckling of either wall, and the actual widths will be used according to Equation E7-2.

---

**Table E.10-1.**
**Analysis of HSS12×8×⅛ Column at Different Effective Lengths**

| Effective length, $L_c$, ft | 18 | 24 | 40 |
|------------------------------|----|----|-----|
| Check Table B4.1a criterion (same as for $L_c = 24.0$ ft) | | | |
| $\lambda_r$ | 33.7 | 33.7 | 33.7 |
| Narrow wall: $\lambda = b/t = 43.0 > \lambda_r$ | Yes | Yes | Yes |
| Wide wall: $\lambda = h/t = 66.0 > \lambda_r$ | Yes | Yes | Yes |
| Check AISC *Specification* Section E7.1 criteria | | | |
| Nominal stress, $F_n$, ksi | 36.9 | 29.1 | 12.3 |
| Narrow wall: | | | |
| $\lambda_r \sqrt{\frac{F_y}{F_n}}$ | $39.2 < \lambda = 43.0$ | $44.2 > \lambda = 43.0$ | $67.9 > \lambda = 43.0$ |
| Local buckling reduction per AISC *Specification* Section E7.1? | Yes | No | No |
| $F_{el}$, ksi | 58.5 | $-$ | $-$ |
| $b_e$, in. | 7.05 | $-$ | $-$ |
| Wide wall: | | | |
| $\lambda_r \sqrt{\frac{F_y}{F_n}}$ | $39.2 < \lambda = 66.0$ | $44.2 < \lambda = 66.0$ | $67.9 > \lambda = 66.0$ |
| Local buckling reduction per AISC *Specification* Section E7.1? | Yes | Yes | No |
| $F_{el}$ (ksi) | 24.8 | 24.8 | $-$ |
| $h_e$ (in.) | 7.88 | 8.66 | $-$ |
| Effective area, $A_e$, in.² | 5.35 | 5.77 | 6.76 |
| Compressive Strength | | | |
| $P_n$, kips | 197 | 168 | 83.1 |
| $\phi_c P_n$, kips (LRFD) | 177 | 151 | 74.8 |
| $P_n/\Omega_c$, kips (ASD) | 118 | 101 | 49.8 |

---

# EXAMPLE E.11 PIPE COMPRESSION MEMBER

## Given:

Select an ASTM A53/A53M Grade B Pipe compression member with a length of 30 ft to support a dead load of 35 kips and live load of 105 kips in axial compression. The column is pin-connected at the ends in both axes and braced at the midpoint in the $y$-$y$ direction. The solution will be provided using:

(1) AISC *Manual* Tables
(2) Calculations using AISC *Specification* provisions

![Diagram: Vertical column with total length L = 30'-0", with bracing at midpoint in Y-direction only, showing segments of 15'-0" each. Axial loads $P_D = 35$ kips and $P_L = 105$ kips applied at top, pinned support at bottom]

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A53/A53M Grade B
$F_y = 35$ ksi

From ASCE/SEI 7, Chapter 2, the required compressive strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(35 \text{ kips}) + 1.6(105 \text{ kips})$ | $P_a = 35 \text{ kips} + 105 \text{ kips}$ |
| $= 210$ kips | $= 140$ kips |

(1) AISC *Manual* Table Solution

From AISC *Specification* Commentary Table C-A-7.1, for a pinned-pinned condition, $K = 1.0$. Therefore, $L_{cx} = K_x L_x = 1.0(30 \text{ ft}) = 30.0$ ft and $L_{cy} = K_y L_y = 1.0(15 \text{ ft}) = 15.0$ ft. Buckling about the $x$-$x$ axis controls.

Enter AISC *Manual* Table 4-6 with $L_c = 30.0$ ft and select the lightest section with sufficient available strength to support the required strength.

Try a Pipe 10 Std.

From AISC *Manual* Table 4-6, the available strength in axial compression is:

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 222 \text{ kips} > 210 \text{ kips}$ **o.k.** | $\frac{P_n}{\Omega_c} = 148 \text{ kips} > 140 \text{ kips}$ **o.k.** |

Available strength can also be determined by hand calculations, as demonstrated in the following.

(2) Calculation Using AISC *Specification* Provisions

From AISC *Manual* Table 1-14, the geometric properties are as follows:

Pipe 10 Std.
$A_g = 11.5$ in.²
$r = 3.68$ in.
$D/t = 31.6$

---

No Pipes shown in AISC *Manual* Table 4-6 are slender at 35 ksi, so no local buckling check is required; however, some round HSS are slender at higher steel strengths. The following calculations illustrate the required check.

*Limiting Width-to-Thickness Ratio*

Determine the wall limiting slenderness ratio, $\lambda_r$, from AISC *Specification* Table B4.1a, Case 9:

$$\lambda = D/t$$

$$= 31.6$$

$$\lambda_r = 0.11\frac{E}{F_y}$$

$$= 0.11\left(\frac{29,000 \text{ ksi}}{35 \text{ ksi}}\right)$$

$$= 91.1$$

$\lambda < \lambda_r$; therefore, the pipe is not slender.

*Nominal Stress*

$$\frac{L_c}{r} = \frac{(30.0 \text{ ft})(12 \text{ in./ft})}{3.68 \text{ in.}}$$

$$= 97.8$$

$$4.71\sqrt{\frac{E}{F_y}} = 4.71\sqrt{\frac{29,000 \text{ ksi}}{35 \text{ ksi}}}$$

$$= 136 > 97.8, \text{ therefore, use AISC } \textit{Specification} \text{ Equation E3-2.}$$

$$F_e = \frac{\pi^2 E}{\left(\frac{L_c}{r}\right)^2}$$
(*Spec.* Eq. E3-4)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(97.8)^2}$$

$$= 29.9 \text{ ksi}$$

$$F_n = \left(0.658^{\frac{F_y}{F_e}}\right)F_y$$
(*Spec.* Eq. E3-2)

$$= \left[0.658^{\left(\frac{35 \text{ ksi}}{29.9 \text{ ksi}}\right)}\right](35 \text{ ksi})$$

$$= 21.4 \text{ ksi}$$

*Compressive Strength*

From AISC *Specification* Section E3, the nominal compressive strength is:

---

$$P_n = F_n A_g$$
(*Spec.* Eq. E3-1)

$$= (21.4 \text{ ksi})(11.5 \text{ in.}^2)$$

$$= 246 \text{ kips}$$

From AISC *Specification* Section E1, the available compressive strength is:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.90$ | $\Omega_c = 1.67$ |
| $\phi_c P_n = 0.90(246 \text{ kips})$ | $\frac{P_n}{\Omega_c} = \frac{246 \text{ kips}}{1.67}$ |
| $= 221 \text{ kips} > 210 \text{ kips}$ **o.k.** | $= 147 \text{ kips} > 140 \text{ kips}$ **o.k.** |

Note that the design procedure would be similar for a round HSS column.

---

# EXAMPLE E.12 BUILT-UP I-SHAPED MEMBER WITH DIFFERENT FLANGE SIZES

## Given:

Compute the available strength of a built-up compression member with a length of 14 ft, as shown in Figure E.12-1. The ends are pinned. The outside flange is PL¾ in. × 5 in., the inside flange is PL¾ in. × 8 in., and the web is PL⅜ in. × 10½ in. The material is ASTM A572/A572M Grade 50.

![Diagram: I-shaped built-up member showing:
- Length L = 14'-0"
- Applied load $P_r$ at top
- Outside flange: $b_{fo} = 5"$, thickness $t_{fo} = \frac{3}{4}"$
- Inside flange: $b_{fi} = 8"$, thickness $t_{fi} = \frac{3}{4}"$
- Web: $t_w = \frac{3}{8}"$, height $h = 10\frac{1}{2}"$, total height $h = 12"$
- Pinned connections at both ends]

*Fig. E.12-1. Column geometry for Example E.12.*

## Solution:

From AISC *Manual* Table 2-5, the material properties are as follows:

ASTM A572/A572M Grade 50
$F_y = 50$ ksi

There are no tables in the AISC *Manual* for special built-up shapes; therefore, the available strength is calculated as follows.

*Flange Slenderness Check*

From AISC *Specification* Table B4.1a note [a], calculate $k_c$.

$$k_c = \frac{4}{\sqrt{h/t_w}}$$

$$= \frac{4}{\sqrt{\frac{10\frac{1}{2} \text{ in.}}{\frac{3}{8} \text{ in.}}}}$$

$$= 0.756, \text{ which is between } 0.35 \text{ and } 0.76$$

Determine the limiting slenderness ratio, $\lambda_r$, from AISC *Specification* Table B4.1a, Case 2:

---

$$\lambda_r = 0.64\sqrt{\frac{k_c E}{F_y}}$$

$$= 0.64\sqrt{\frac{0.756(29,000 \text{ ksi})}{50 \text{ ksi}}}$$

$$= 13.4$$

For the outside flange, the slenderness ratio is:

$$\lambda = b/t$$

$$= \frac{2.50 \text{ in.}}{\frac{3}{4} \text{ in.}}$$

$$= 3.33$$

$\lambda \leq \lambda_r$; therefore, the outside flange is not slender.

For the inside flange, the slenderness ratio is:

$$\lambda = b/t$$

$$= \frac{4.00 \text{ in.}}{\frac{3}{4} \text{ in.}}$$

$$= 5.33$$

$\lambda \leq \lambda_r$; therefore, the inside flange is not slender.

*Web Slenderness Check*

Determine the limiting slenderness ratio, $\lambda_r$, for the web from AISC *Specification* Table B4.1a, Case 5:

$$\lambda_r = 1.49\sqrt{\frac{E}{F_y}}$$

$$= 1.49\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 35.9$$

The slenderness ratio for the web is:

$$\lambda = h/t$$

$$= \frac{10\frac{1}{2} \text{ in.}}{\frac{3}{8} \text{ in.}}$$

$$= 28.0$$

$\lambda \leq \lambda_r$; therefore, the web is not slender.

*Section Properties (ignoring welds)*

---

$$A_g = b_{fi} t_{fi} + ht_w + b_{fo} t_{fo}$$

$$= (8.00 \text{ in.})(\frac{3}{4} \text{ in.}) + (10\frac{1}{2} \text{ in.})(\frac{3}{8} \text{ in.}) + (5.00 \text{ in.})(\frac{3}{4} \text{ in.})$$

$$= 6.00 \text{ in.}^2 + 3.94 \text{ in.}^2 + 3.75 \text{ in.}^2$$

$$= 13.7 \text{ in.}^2$$

$$\overline{y} = \frac{\sum A_i y_i}{\sum A_i}$$

$$= \frac{(6.00 \text{ in.}^2)(11.6 \text{ in.}) + (3.94 \text{ in.}^2)(6.00 \text{ in.}) + (3.75 \text{ in.}^2)(0.375 \text{ in.})}{13.7 \text{ in.}^2}$$

$$= 6.91 \text{ in.}$$

Note that the center of gravity about the $x$-$x$ axis is measured from the bottom of the outside flange.

$$I_x = \sum\left[\frac{bh^3}{12} + Ad^2\right]$$

$$= \left[\frac{(8.00 \text{ in.})(\frac{3}{4} \text{ in.})^3}{12} + (6.00 \text{ in.}^2)(4.72 \text{ in.})^2\right] + \left[\frac{(\frac{3}{8} \text{ in.})(10\frac{1}{2} \text{ in.})^3}{12} + (3.94 \text{ in.}^2)(0.910 \text{ in.})^2\right]$$

$$+ \left[\frac{(5.00 \text{ in.})(\frac{3}{4} \text{ in.})^3}{12} + (3.75 \text{ in.}^2)(6.54 \text{ in.})^2\right]$$

$$= 334 \text{ in.}^4$$

$$r_x = \sqrt{\frac{I_x}{A}}$$

$$= \sqrt{\frac{334 \text{ in.}^4}{13.7 \text{ in.}^2}}$$

$$= 4.94 \text{ in.}$$

$$I_y = \sum\frac{bh^3}{12}$$

$$= \frac{(\frac{3}{4} \text{ in.})(8.00 \text{ in.})^3}{12} + \frac{(10\frac{1}{2} \text{ in.})(\frac{3}{8} \text{ in.})^3}{12} + \frac{(\frac{3}{4} \text{ in.})(5.00 \text{ in.})^3}{12}$$

$$= 39.9 \text{ in.}^4$$

$$r_y = \sqrt{\frac{I_y}{A}}$$

$$= \sqrt{\frac{39.9 \text{ in.}^4}{13.7 \text{ in.}^2}}$$

$$= 1.71 \text{ in.}$$

*Elastic Buckling Stress about the $x$-$x$ Axis*

From AISC *Specification* Commentary Table C-A-7.1, for a pinned-pinned condition, $K = 1.0$. Therefore, $L_{cx} = L_{cy} = L_{cz} = KL = 1.0(14 \text{ ft}) = 14.0$ ft.

---

The effective slenderness ratio about the $x$-$x$ axis is:

$$\frac{L_{cx}}{r_x} = \frac{(14.0 \text{ ft})(12 \text{ in./ft})}{4.94 \text{ in.}}$$

$$= 34.0$$

$$F_e = \frac{\pi^2 E}{\left(\frac{L_c}{r}\right)^2}$$
(*Spec.* Eq. E3-4)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(34.0)^2}$$

$$= 248 \text{ ksi}$$

*Flexural-Torsional Elastic Buckling Stress*

Calculate the torsional constant, $J$, using AISC Design Guide 9, Equation 3.4:

$$J = \sum\frac{bt^3}{3}$$

$$= \frac{(8.00 \text{ in.})(\frac{3}{4} \text{ in.})^3}{3} + \frac{(10\frac{1}{2} \text{ in.})(\frac{3}{8} \text{ in.})^3}{3} + \frac{(5.00 \text{ in.})(\frac{3}{4} \text{ in.})^3}{3}$$

$$= 2.01 \text{ in.}^4$$

Distance between flange centroids:

$$h_o = d - \frac{t_{fi}}{2} - \frac{t_{fo}}{2}$$

$$= 12.0 \text{ in.} - \frac{\frac{3}{4} \text{ in.}}{2} - \frac{\frac{3}{4} \text{ in.}}{2}$$

$$= 11.3 \text{ in.}$$

Warping constant:

$$C_w = \frac{t_f h_o^2}{12}\left(\frac{b_{fi}^3 b_{fo}^3}{b_{fi}^3 + b_{fo}^3}\right)$$

$$= \frac{(\frac{3}{4} \text{ in.})(11.3 \text{ in.})^2}{12}\left[\frac{(8.00 \text{ in.})^3 (5.00 \text{ in.})^3}{(8.00 \text{ in.})^3 + (5.00 \text{ in.})^3}\right]$$

$$= 802 \text{ in.}^6$$

Due to symmetry, both the centroid and the shear center lie on the $y$-$y$ axis. Therefore, $x_o = 0$. The distance from the center of the outside flange to the shear center is:

---

$$e = h_o\left(\frac{b_{fi}^3}{b_{fi}^3 + b_{fo}^3}\right)$$

$$= (11.3 \text{ in.})\left[\frac{(8.00 \text{ in.})^3}{(8.00 \text{ in.})^3 + (5.00 \text{ in.})^3}\right]$$

$$= 9.08 \text{ in.}$$

Add one-half the flange thickness to determine the shear center location measured from the bottom of the outside flange.

$$\left(e + \frac{t_f}{2}\right) = 9.08 \text{ in.} + \frac{\frac{3}{4} \text{ in.}}{2}$$

$$= 9.46 \text{ in.}$$

$$y_o = \left(e + \frac{t_f}{2}\right) - \overline{y}$$

$$= 9.46 \text{ in.} - 6.91 \text{ in.}$$

$$= 2.55 \text{ in.}$$

$$\bar{r}_o^2 = x_o^2 + y_o^2 + \frac{I_x + I_y}{A_g}$$
(*Spec.* Eq. E4-9)

$$= 0 + (2.55 \text{ in.})^2 + \frac{334 \text{ in.}^4 + 39.9 \text{ in.}^4}{13.7 \text{ in.}^2}$$

$$= 33.8 \text{ in.}^2$$

$$H = 1 - \frac{x_o^2 + y_o^2}{\bar{r}_o^2}$$
(*Spec.* Eq. E4-8)

$$= 1 - \frac{0 + (2.55 \text{ in.})^2}{33.8 \text{ in.}^2}$$

$$= 0.808$$

The effective slenderness ratio about the $y$-$y$ axis is:

$$\frac{L_{cy}}{r_y} = \frac{(14.0 \text{ ft})(12 \text{ in./ft})}{1.71 \text{ in.}}$$

$$= 98.2$$

$$F_{ey} = \frac{\pi^2 E}{\left(\frac{L_{cy}}{r_y}\right)^2}$$
(*Spec.* Eq. E4-6)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(98.2)^2}$$

$$= 29.7 \text{ ksi}$$

---

$$F_{ez} = \left(\frac{\pi^2 EC_w}{L_{cz}^2} + GJ\right)\frac{1}{A_g \bar{r}_o^2}$$
(*Spec.* Eq. E4-7)

$$= \left\{\frac{\pi^2 (29,000 \text{ ksi})(802 \text{ in.}^6)}{\left[(14.0 \text{ ft})(12 \text{ in./ft})\right]^2} + (11,200 \text{ ksi})(2.01 \text{ in.}^4)\right\}\frac{1}{(13.7 \text{ in.}^2)(33.8 \text{ in.}^2)}$$

$$= 66.2 \text{ ksi}$$

$$F_e = \left(\frac{F_{ey} + F_{ez}}{2H}\right)\left[1 - \sqrt{1 - \frac{4F_{ey}F_{ez}H}{(F_{ey} + F_{ez})^2}}\right]$$
(*Spec.* Eq. E4-3)

$$= \left[\frac{29.7 \text{ ksi} + 66.2 \text{ ksi}}{2(0.808)}\right]\left[1 - \sqrt{1 - \frac{4(29.7 \text{ ksi})(66.2 \text{ ksi})(0.808)}{(29.7 \text{ ksi} + 66.2 \text{ ksi})^2}}\right]$$

$$= 26.4 \text{ ksi} \quad \textbf{controls}$$

Torsional and flexural-torsional buckling governs.

$$\frac{F_y}{F_e} = \frac{50 \text{ ksi}}{26.4 \text{ ksi}}$$

$$= 1.89$$

Because $\frac{F_y}{F_e} < 2.25$:

$$F_n = \left(0.658^{\frac{F_y}{F_e}}\right)F_y$$
(*Spec.* Eq. E3-2)

$$= \left(0.658^{1.89}\right)(50 \text{ ksi})$$

$$= 22.7 \text{ ksi}$$

*Compressive Strength*

From AISC *Specification* Section E3, the nominal compressive strength is:

$$P_n = F_n A_g$$
(*Spec.* Eq. E3-1)

$$= (22.7 \text{ ksi})(13.7 \text{ in.}^2)$$

$$= 311 \text{ kips}$$

From AISC *Specification* Section E1, the available compressive strength is:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.90$ | $\Omega_c = 1.67$ |
| $\phi_c P_n = 0.90(311 \text{ kips})$ | $\frac{P_n}{\Omega_c} = \frac{311 \text{ kips}}{1.67}$ |
| $= 280$ kips | $= 186$ kips |

---

# EXAMPLE E.13 DOUBLE-WT COMPRESSION MEMBER

## Given:

Determine the available compressive strength for an ASTM A992/A992M double WT9×20 compression member, as shown in Figure E.13-1. Assume that ½-in.-thick connectors are welded in position at the ends and at equal intervals, "$a$", along the length. Use the minimum number of intermediate connectors needed to force the two WT-shapes to act as a single built-up compression member.

![Diagram: 3D isometric view of double WT compression member showing two WT9×20 shapes connected at intervals with connectors, length L = 9'-0", with applied load $P_r$ at top]

*Fig. E.13-1. Double WT compression member in Example E.13.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50$ ksi

From AISC *Manual* Table 1-8 the geometric properties for a single WT9×20 are as follows:

$A_g = 5.88$ in.²
$d = 8.95$ in.
$t_w = 0.315$ in.
$I_x = 44.8$ in.⁴
$I_y = 9.55$ in.⁴
$r_x = 2.76$ in.
$r_y = 1.27$ in.
$\overline{y} = 2.29$ in.
$J = 0.404$ in.⁴
$C_w = 0.788$ in.⁶
$\frac{d}{t_w} = 28.4$

From mechanics of materials, the combined section properties for two WT9×20s, flange-to-flange, spaced ½ in. apart, are as follows:

$$A = \sum A_{single\ tee}$$

$$= 2(5.88 \text{ in.}^2)$$

$$= 11.8 \text{ in.}^2$$

---

$$I_x = 2\left(I_x + A\bar{y}^2\right)$$

$$= 2\left[44.8 \text{ in.}^4 + (5.88 \text{ in.}^2)(2.29 \text{ in.} + 0.250 \text{ in.})^2\right]$$

$$= 165 \text{ in.}^4$$

$$r_x = \sqrt{\frac{I_x}{A}}$$

$$= \sqrt{\frac{165 \text{ in.}^4}{11.8 \text{ in.}^2}}$$

$$= 3.74 \text{ in.}$$

$$I_y = \Sigma I_y\text{ }_{single\ tee}$$

$$= 2(9.55 \text{ in.}^4)$$

$$= 19.1 \text{ in.}^4$$

$$r_y = \sqrt{\frac{I_y}{A}}$$

$$= \sqrt{\frac{19.1 \text{ in.}^4}{11.8 \text{ in.}^2}}$$

$$= 1.27 \text{ in.}$$

$$J = \Sigma J_{single\ tee}$$

$$= 2(0.404 \text{ in.}^4)$$

$$= 0.808 \text{ in.}^4$$

For the double WT (cruciform) shape shown in Figure E.13-2 it is reasonable to take $C_w = 0$ and ignore any warping contribution to column strength.

![Diagram: Two cross-sectional views showing double WT cruciform shape with X-X and Y-Y axes marked. Left view shows side profile, right view shows plan view with dimension $\overline{y} + \frac{1}{4}"$ and $\frac{1}{2}"$ spacing indicated]

*Fig. E.13-2. Double WT shape cross section.*

---

The $y$-axis of the combined section is the same as the $y$-$y$ axis of the single section. When buckling occurs about the $y$-$y$ axis, there is no relative slip between the two WTs. For buckling about the $x$-$x$ axis of the combined section, the WTs will slip relative to each other unless restrained by welded or slip-critical end connections.

*Intermediate Connectors Dimensional Requirements*

Determine the minimum number of intermediate connectors required.

From AISC *Specification* Section E6.2, the maximum slenderness ratio of each tee should not exceed three-fourths times the maximum slenderness ratio of the double WT built-up section. For a WT9×20, the minimum radius of gyration is:

$$r_i = r_y$$

$$= 1.27 \text{ in.}$$

Use $K = 1.0$ for both the single tee and the double tee; therefore, $L_{cy} = K_y L_y = 1.0(9 \text{ ft}) = 9.00$ ft:

$$\left(\frac{a}{r_i}\right)_{single\ tee} \leq \frac{3}{4}\left(\frac{L_{cy}}{r_{min}}\right)_{double\ tee}$$

Solving for $a$:

$$a \leq \frac{3}{4}\left[\frac{(r_y)_{single\ tee}}{(r_y)_{double\ tee}}\right](L_{cy})_{double\ tee}$$

$$= \frac{3}{4}\left[\frac{1.27 \text{ in.}}{1.27 \text{ in.}}\right][(9.00 \text{ ft})(12 \text{ in./ft})]$$

$$= 81.0 \text{ in.}$$

Thus, one intermediate connector at mid-length $[a = (4.5 \text{ ft})(12 \text{ in./ft}) = 54.0 \text{ in.}]$ satisfies AISC *Specification* Section E6.2 as shown in Figure E.13-3.

![Diagram: 3D isometric view showing double WT member with one intermediate connector at mid-length, spacing $a = 4.5$ ft on each side, total length $L = 9.0$ ft, with WT9×20 sections and applied load $P_r$]

*Figure E.13-3. Minimum connectors required for double WT compression member.*

---

*Flexural Buckling and Torsional Buckling Strength*

Determine the limiting slenderness ratio, $\lambda_r$, for the stem from AISC *Specification* Table B4.1a, Case 4:

$$\lambda_r = 0.75\sqrt{\frac{E}{F_y}}$$

$$= 0.75\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 18.1$$

The slenderness ratio for the stem is:

$$\lambda = \frac{d}{t_w}$$

$$= 28.4$$

$\lambda > \lambda_r$; therefore, the stem is slender.

Because the WT9×20 has a slender stem, the provisions of AISC *Specification* Section E7 apply. Determine the elastic buckling stress for flexural buckling about the $y$-$y$ and $x$-$x$ axes, and torsional buckling. Then, determine the effective area considering local buckling, the critical buckling stress, and the nominal strength.

*Elastic Buckling Stress about the $y$-$y$ Axis*

$$\frac{L_{cy}}{r_y} = \frac{(9.00 \text{ ft})(12 \text{ in./ft})}{1.27 \text{ in.}}$$

$$= 85.0$$

$$F_{ey} = \frac{\pi^2 E}{\left(\frac{L_{cy}}{r_y}\right)^2}$$
(*Spec.* Eq. E4-6)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(85.0)^2}$$

$$= 39.6 \text{ ksi} \quad \textbf{controls}$$

*Elastic Buckling Stress about the $x$-$x$ Axis*

Flexural buckling about the $x$-$x$ axis is determined using the modified slenderness ratio to account for shear deformation of the intermediate connectors.

Note that the provisions of AISC *Specification* Section E6.1, which require that $L_c/r$ be replaced with $(L_c/r)_m$, apply if "the buckling mode involves relative deformations that produce shear forces in the connectors between individual shapes...". Relative slip between the two sections occurs for buckling about the $x$-$x$ axis, and therefore, the provisions of the section apply only to buckling about the $x$-$x$ axis.

The connectors are welded at the ends and the intermediate point. The modified slenderness is calculated using the spacing between intermediate connectors:

---

$$a = (4.5 \text{ ft})(12.0 \text{ in./ft})$$

$$= 54.0 \text{ in.}$$

$$r_i = r_y$$

$$= 1.27 \text{ in.}$$

$$\frac{a}{r_i} = \frac{54.0 \text{ in.}}{1.27 \text{ in.}}$$

$$= 42.5$$

Because $a/r_i > 40$, use AISC *Specification* Equation E6-2b.

$$\left(\frac{L_c}{r}\right)_m = \sqrt{\left(\frac{L_c}{r}\right)_o^2 + \left(\frac{K_i a}{r_i}\right)^2}$$
(*Spec.* Eq. E6-2b)

where

$$\left(\frac{L_c}{r}\right)_o = \frac{L_{cx}}{r_x}$$

$$= \frac{(9.00 \text{ ft})(12 \text{ in./ft})}{3.74 \text{ in.}}$$

$$= 28.9$$

$$K_i = 0.86$$

$$\frac{K_i a}{r_i} = \frac{0.86(4.50 \text{ ft})(12 \text{ in./ft})}{1.27 \text{ in.}}$$

$$= 36.6$$

Thus,

$$\left(\frac{L_c}{r}\right)_m = \sqrt{(28.9)^2 + (36.6)^2}$$

$$= 46.6$$

$$F_{ex} = \frac{\pi^2 E}{\left(\frac{L_{cx}}{r_x}\right)^2}$$
(*Spec.* Eq. E4-5)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(46.6)^2}$$

$$= 132 \text{ ksi}$$

*Torsional Buckling Elastic Stress*

$$F_e = \left(\frac{\pi^2 EC_w}{L_{cz}^2} + GJ\right)\frac{1}{I_x + I_y}$$
(*Spec.* Eq. E4-2)

---

The cruciform section made up of two back-to-back WTs has virtually no warping resistance, thus the warping contribution is ignored and AISC *Specification* Equation E4-2 becomes:

$$F_e = \frac{GJ}{I_x + I_y}$$

$$= \frac{(11,200 \text{ ksi})(0.808 \text{ in.}^4)}{165 \text{ in.}^4 + 19.1 \text{ in.}^4}$$

$$= 49.2 \text{ ksi}$$

*Nominal Stress*

Use the smallest elastic buckling stress, $F_e$, from the limit states considered above to determine $F_n$ using AISC *Specification* Equation E3-2 or Equation E3-3, as follows:

$$F_e = 39.6 \text{ ksi}$$

$$\frac{F_y}{F_e} = \frac{50 \text{ ksi}}{39.6 \text{ ksi}}$$

$$= 1.26$$

Because $\frac{F_y}{F_e} < 2.25$,

$$F_n = \left(0.658^{\frac{F_y}{F_e}}\right)F_y$$
(*Spec.* Eq. E3-2)

$$= \left(0.658^{1.26}\right)(50 \text{ ksi})$$

$$= 29.5 \text{ ksi}$$

*Effective Area*

Because the stem was previously shown to be slender, calculate the limits of AISC *Specification* Section E7.1 to determine if the stem is fully effective or if there is a reduction in effective area due to local buckling of the stem.

$$\lambda = \frac{d}{t_w}$$

$$= 28.4$$

$$\lambda_r = 0.75\sqrt{\frac{E}{F_y}}$$

$$= 0.75\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 18.1$$

$$\lambda_r \sqrt{\frac{F_y}{F_n}} = 18.1\sqrt{\frac{50 \text{ ksi}}{29.5 \text{ ksi}}}$$

$$= 23.6$$

---

Because $\lambda > \lambda_r \sqrt{F_y/F_n}$, the stem will not be fully effective and there will be a reduction in effective area due to local buckling of the stem. The effective width imperfection adjustment factors can be determined from AISC *Specification* Table E7.1, Case (c), as follows.

$$c_1 = 0.22$$
$$c_2 = 1.49$$

Determine the elastic local buckling stress from AISC *Specification* Section E7.1.

$$F_{el} = \left[c_2 \frac{\lambda_r}{\lambda}\right]^2 F_y$$
(*Spec.* Eq. E7-5)

$$= \left[1.49\left(\frac{18.1}{28.4}\right)\right]^2 (50 \text{ ksi})$$

$$= 45.1 \text{ ksi}$$

Determine the effective width of the tee stem and the resulting effective area, where $d = 8.95$ in.

$$d_e = d\left[1 - c_1\sqrt{\frac{F_{el}}{F_n}}\right]\sqrt{\frac{F_{el}}{F_n}}$$
(from *Spec.* Eq. E7-3)

$$= (8.95 \text{ in.})\left[1 - 0.22\sqrt{\frac{45.1 \text{ ksi}}{29.5 \text{ ksi}}}\right]\sqrt{\frac{45.1 \text{ ksi}}{29.5 \text{ ksi}}}$$

$$= 8.06 \text{ in.}$$

$$A_e = \sum A_g - \sum[t_w(d - d_e)]$$

$$= (2)(5.88 \text{ in.}^2) - (2)(0.315 \text{ in.})(8.95 \text{ in.} - 8.06 \text{ in.})$$

$$= 11.2 \text{ in.}^2$$

*Compressive Strength*

From AISC *Specification* Section E7, the nominal compressive strength is:

$$P_n = F_n A_e$$
(*Spec.* Eq. E7-1)

$$= (29.5 \text{ ksi})(11.2 \text{ in.}^2)$$

$$= 330 \text{ kips}$$

From AISC *Specification* Section E1, the available compressive strength is:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.90$ | $\Omega_c = 1.67$ |
| $\phi_c P_n = 0.90(330 \text{ kips})$ | $\frac{P_n}{\Omega_c} = \frac{330 \text{ kips}}{1.67}$ |
| $= 297$ kips | $= 198$ kips |

---

# EXAMPLE E.14A AXIALLY LOADED SINGLE-ANGLE COMPRESSION MEMBER

## Given:

Determine the available compressive strength of an ASTM A572/A572M Grade 50 L5×3×½ single angle compression member with a length of 5 ft. The angle is attached at each end through the same leg with a minimum of two bolts. As shown in Figure E.14A-1, the $y$-$y$ axis of the angle is parallel to the attached leg. The solution will be provided using:

(1) Calculations using AISC *Specification* provisions
(2) AISC *Manual* Tables

![Diagram: Cross-sectional view of single angle showing x-x, y-y, and z-z axes. Note indicates "Attached leg (long leg for this example)" with bolted connection shown]

*Fig. E.14A-1. Single-angle cross section.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A572/A572M Grade 50
$F_y = 50$ ksi

From AISC *Manual* Table 1-7:

L5×3×½
$A_g = 3.75$ in.²
$r_x = 1.58$ in.
$r_y = 0.824$ in.
$r_z = 0.642$ in.

(1) Calculation Using AISC *Specification* Provisions

The nominal compressive strength, $P_n$, of single-angle members is taken as the lowest value based on the limit states of flexural buckling in accordance with Section E3 or Section E7, as applicable, or flexural-torsional buckling in accordance with Section E4.

The effects of eccentricity on single-angle members are permitted to be neglected and the member evaluated as axially loaded using one of the effective slenderness ratios specified in Section E5(a) or E5(b), provided that the following requirements are met:

Members are loaded at the ends in compression through the same one leg. – This requirement is satisfied.

Members are attached by welding or by connections with a minimum of two bolts. – This requirement is satisfied.

---

There are no intermediate transverse loads. – This requirement is satisfied.

$L_c/r$ as determined in this section does not exceed 200. $L_c/r = 127$ as determined below. – This requirement is satisfied.

For unequal leg angles, the ratio of long leg width to short leg width is less than 1.7. $5/3 = 1.67 < 1.7$. – This requirement is satisfied.

In this case, the single-angle can be evaluated as axially loaded using modified slenderness ratios and eccentricity can be neglected.

*Slenderness Check*

$$\lambda = \frac{b}{t}$$

$$= \frac{5.00 \text{ in.}}{\frac{1}{2} \text{ in.}}$$

$$= 10.0$$

Determine the limiting slenderness ratio, $\lambda_r$, from AISC *Specification* Table B4.1a, Case 3

$$\lambda_r = 0.45\sqrt{\frac{E}{F_y}}$$

$$= 0.45\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 10.8$$

$\lambda < \lambda_r$; therefore, there are no slender elements, and Sections E3 and E4 apply.

*Effective Slenderness Ratio*

Determine the slenderness ratio about the axis parallel to the attached leg, $L/r_b$:

$$\frac{L}{r_a} = \frac{(5.00 \text{ ft})(12 \text{ in./ft})}{0.824 \text{ in.}}$$

$$= 72.8$$

For unequal-leg angles that are individual members or webs of a planar truss connected through the longer leg:

When $\frac{L}{r_a} \leq 80$,

$$\frac{L_c}{r} = 72 + 0.75\frac{L}{r_a}$$
(*Spec.* Eq. E5-1)

$$= 72 + 0.75(72.8)$$

$$= 127$$

---

*Nominal Stress*

Calculate the elastic buckling stress about the $y$-$y$ axis:

$$F_e = \frac{\pi^2 E}{\left(\frac{L_c}{r}\right)^2}$$
(*Spec.* Eq. E3-4)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(127)^2}$$

$$= 17.7 \text{ ksi}$$

$$4.71\sqrt{\frac{E}{F_y}} = 4.71\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 113$$

$L_c/r = 127 > 113$; therefore, use AISC *Specification* Equation E3-3.

$$F_n = 0.877F_e$$
(*Spec.* Eq. E3-3)

$$= (0.877)(17.7 \text{ ksi})$$

$$= 15.5 \text{ ksi}$$

Determine if flexural-torsional buckling is applicable according to AISC *Specification* Section E4:

$$0.71\sqrt{\frac{E}{F_y}} = 0.71\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 17.1$$

Because $\lambda < 0.71\sqrt{E/F_y}$, flexural-torsional buckling need not be considered.

*Compressive Strength*

From AISC *Specification* Section E3, the nominal compressive strength is:

$$P_n = F_n A_g$$
(*Spec.* Eq. E3-1)

$$= (15.5 \text{ ksi})(3.75 \text{ in.}^2)$$

$$= 58.1 \text{ kips}$$

From AISC *Specification* Section E1, the available compressive strength is:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.90$ | $\Omega_c = 1.67$ |
| $\phi_c P_n = 0.90(58.1 \text{ kips})$ | $\frac{P_n}{\Omega_c} = \frac{58.1 \text{ kips}}{1.67}$ |
| $= 52.3$ kips | $= 34.8$ kips |

---

(2) AISC *Manual* Tables

To use the concentrically loaded angle tables, determine the effective $KL$ with respect to the $z$-$z$ axis based on the modified slenderness ratio already determined:

$$KL_{eff} = \left(\frac{L_c}{r}\right)r_z$$

$$= (127)(0.642 \text{ in.})$$

$$= 81.5 \text{ in.}$$

$$= 6.79 \text{ ft}$$

From AISC *Manual* Table 4-11, conservatively using $L_c = 7$ ft because interpolating between values in the table can produce unconservative results:

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 49.5$ kips | $\frac{P_n}{\Omega_c} = 32.9$ kips |

Thus, the calculations demonstrate how the values for this member in AISC *Manual* Table 4-11 can be confirmed. Note that AISC *Manual* Table 4-11 values may provide conservative results compared to calculating the available strength directly.

---

# EXAMPLE E.14B ECCENTRICALLY LOADED SINGLE-ANGLE COMPRESSION MEMBER (LONG LEG ATTACHED)

## Given:

Determine the available strength of an eccentrically loaded ASTM A572/A572M Grade 50 L8×4×½ single-angle compression member, as shown in Figure E.14B-1, with an effective length of 5 ft. The long leg of the angle is the attached leg, and the eccentric load is applied at 0.75*r* as shown. Use the provisions of the AISC *Specification* and compare the results to the available strength found in AISC *Manual* Table 4-12.

![Diagram: Plan view of L8×4×½ angle showing:
- Long leg: $b = 8.00"$, half-width $b/2 = 4.00"$
- Short leg: $d = 4.00"$
- Thickness: $\frac{3}{4}t = 0.375"$, $t = \frac{1}{2}"$
- Applied load $P_r$ at distance from edge
- Points A, B, C marked on cross-section
- Z-axis indicated
- Dimension $w$ shown]

*Fig. E.14B-1. Eccentrically loaded single-angle compression member in Example E.14B.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A572/A572M Grade 50
$F_y = 50$ ksi

From AISC *Manual* Table 1-7:

L8×4×½
$\bar{x} = 0.854$ in.
$\bar{y} = 2.84$ in.
$A_g = 5.80$ in.²
$I_x = 38.6$ in.⁴
$I_y = 6.75$ in.⁴
$I_z = 4.32$ in.⁴
$r_z = 0.863$ in.
tan $\alpha = 0.266$

From AISC Shapes Database V16.0:

$I_w = 41.0$ in.⁴
$S_{wA} = 12.4$ in.³
$S_{wB} = 16.3$ in.³
$S_{wC} = 7.98$ in.³
$S_{zA} = 1.82$ in.³
$S_{zB} = 2.77$ in.³
$S_{wC} = 5.81$ in.³

---

The load is applied at the location shown in Figure E.14B-2. Determine the eccentricities about the major ($w$-$w$ axis) and minor ($z$-$z$ axis) principal axes for the load, $P$. From AISC *Manual* Table 1-7, the angle of the principal axes is found to be $\alpha = \tan^{-1}(0.266) = 14.9°$.

Using the geometry shown in Figures E.14B-2 and E.14B-3:

$$e_w = [(\bar{x} + 0.75r)\tan \alpha + 0.5b - \bar{y}]\cos \alpha$$

$$= \{[0.854 \text{ in.} + 0.75(\frac{1}{2} \text{ in.})](0.266) + 0.5(8.00 \text{ in.}) - 2.84 \text{ in.}\}(\cos 14.9°)$$

$$= 1.44 \text{ in.}$$

$$e_z = (\bar{x} + 0.75r)\cos \alpha - (0.5b - \bar{y})\sin \alpha$$

$$= [0.854 \text{ in.} + 0.75(\frac{1}{2} \text{ in.})](\cos 14.9°) - [0.5(8.00 \text{ in.}) - 2.84 \text{ in.}](\sin 14.9°)$$

$$= 0.889 \text{ in.}$$

Because of these eccentricities, the moment resultant has components about both principal axes; therefore, the combined stress provisions of AISC *Specification* Section H2 must be followed.

$$\left|\frac{f_{cn}}{F_{cn}} + \frac{f_{cbw}}{F_{cbw}} + \frac{f_{cbz}}{F_{cbz}}\right| \leq 1.0$$
(*Spec.* Eq. H2-1)

Due to the load and the given eccentricities, moments about the $w$-$w$ and $z$-$z$ axes will have different effects on points A, B, and C. The axial force will produce a compressive stress and the moments, where positive moments are in the direction shown in Figure E.14B-3, will produce stresses with a sign indicated by the sense given in the following. In this example, compressive stresses will be taken as positive and tensile stresses will be taken as negative.

| Point | Caused by $M_w$ | Caused by $M_z$ |
|-------|-----------------|-----------------|
| A | tension | tension |
| B | tension | compression |
| C | compression | tension |

![Diagram: Detailed geometric diagram showing principal axes $w$-$w$ and $z$-$z$, with dimensions including $b$, $b/2$, $\bar{y}$, $d$, points A, B, C, angle $\alpha$, eccentricities $e_w$ and $e_z$, distances $z_B$, $z_A$, $z_C$, and load $P$ position. Axes x-x, y-y, z-z, and w-w marked. Note indicates "Attached leg (long leg for unequal leg angles)"]

*Fig. E.14B-2. Geometry about principal axes.*

---

*Available Compressive Strength*

Check the slenderness of the longest leg for uniform compression.

$$\lambda = \frac{b}{t}$$

$$= \frac{8.00 \text{ in.}}{\frac{1}{2} \text{ in.}}$$

$$= 16.0$$

Check the slenderness of the shorter leg for uniform compression.

$$\lambda = \frac{d}{t}$$

$$= \frac{4.00 \text{ in.}}{\frac{1}{2} \text{ in.}}$$

$$= 8.00$$

From *AISC Specification* Table B4.1a, Case 3, the limiting width-to-thickness ratio is:

$$\lambda_r = 0.45\sqrt{\frac{E}{F_y}}$$

$$= 0.45\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 10.8$$

Because $b/t = 16.0 > 10.8$, the longer leg is classified as a slender element for compression. Because $d/t = 8.00 < 10.8$, the shorter leg is classified as a nonslender element for compression.

Determine if torsional and flexural-torsional buckling is applicable, using the provisions of AISC *Specification* Section E4.

$$\lambda = 16.0$$

$$0.71\sqrt{\frac{E}{F_y}} = 0.71\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 17.1$$

![Diagram: 3D view of angle member showing points A, B, C with applied load P and eccentricities $e_w$ and $e_z$, moments $M_w$ and $M_z$ indicated at point C along w-w and z-z axes]

*Fig. E.14B-3. Applied moments and eccentric axial load.*

---

Because $\lambda < 0.71\sqrt{E/F_y}$, torsional and flexural-torsional buckling are not applicable.

Determine the nominal stress, $F_n$, with $L_c = (5.00 \text{ ft})(12 \text{ in./ft}) = 60.0$ in. for buckling about the $z$-$z$ axis.

$$\frac{L_{cz}}{r_z} = \frac{60.0 \text{ in.}}{0.863 \text{ in.}}$$

$$= 69.5$$

$$F_e = \frac{\pi^2 E}{\left(\frac{L_{cz}}{r_z}\right)^2}$$
(*Spec.* Eq. E3-4)

$$= \frac{\pi^2 (29,000 \text{ ksi})}{(69.5)^2}$$

$$= 59.3 \text{ ksi}$$

$$\frac{F_y}{F_e} = \frac{50 \text{ ksi}}{59.3 \text{ ksi}}$$

$$= 0.843$$

Because $\frac{F_y}{F_e} < 2.25$:

$$F_n = \left(0.658^{\frac{F_y}{F_e}}\right)F_y$$
(*Spec.* Eq. E3-2)

$$= \left(0.658^{0.843}\right)(50 \text{ ksi})$$

$$= 35.1 \text{ ksi}$$

Because the longer leg was found to be slender, the limits of AISC *Specification* Section E7.1 must be evaluated to determine if the leg is fully effective for compression or if a reduction in effective area must be taken to account for local buckling in the longer leg.

$$\lambda = 16.0$$

$$\lambda_r \sqrt{\frac{F_y}{F_n}} = 10.8\sqrt{\frac{50 \text{ ksi}}{35.1 \text{ ksi}}}$$

$$= 12.9$$

Because $\lambda = 16.0 > 12.9$, there will be a reduction in effective area due to local buckling in the longer leg. Determine the effective width imperfection adjustment factors per AISC *Specification* Table E7.1 as follows.

$$c_1 = 0.22$$
$$c_2 = 1.49$$

Determine the elastic local buckling stress from AISC *Specification* Section E7.1.

---

$$F_{el} = \left[c_2 \frac{\lambda_r}{\lambda}\right]^2 F_y$$
(*Spec.* Eq. E7-5)

$$= \left[1.49\left(\frac{10.8}{16.0}\right)\right]^2 (50 \text{ ksi})$$

$$= 50.6 \text{ ksi}$$

Determine the effective width of the angle leg and the resulting effective area.

$$b_e = b\left[1 - c_1\sqrt{\frac{F_{el}}{F_n}}\right]\sqrt{\frac{F_{el}}{F_n}}$$
(*Spec.* Eq. E7-3)

$$= (8.00 \text{ in.})\left[1 - 0.22\sqrt{\frac{50.6 \text{ ksi}}{35.1 \text{ ksi}}}\right]\sqrt{\frac{50.6 \text{ ksi}}{35.1 \text{ ksi}}}$$

$$= 7.07 \text{ in.}$$

$$A_e = A_g - t\sum(b - b_e)$$

$$= 5.80 \text{ in.}^2 - (\frac{1}{2} \text{ in.})(8.00 \text{ in.} - 7.07 \text{ in.})$$

$$= 5.34 \text{ in.}^2$$

*Compressive Strength*

From AISC *Specification* Section E7, the nominal compressive strength is:

$$P_n = F_n A_e$$
(*Spec.* Eq. E7-1)

$$= (35.1 \text{ ksi})(5.34 \text{ in.}^2)$$

$$= 187 \text{ kips}$$

From AISC *Specification* Section E1, the available compressive strength is:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.90$ | $\Omega_c = 1.67$ |
| $\phi_c P_n = 0.90(187 \text{ kips})$ | $\frac{P_n}{\Omega_c} = \frac{187 \text{ kips}}{1.67}$ |
| $= 168$ kips | $= 112$ kips |

Determine the available flexural strengths, $M_{cbw}$ and $M_{cbz}$, and the available flexural stresses at each point on the cross section.

*Yielding*

Consider the limit state of yielding for bending about the $w$-$w$ and $z$-$z$ axes at points A, B, and C according to AISC *Specification* Section F10.1.

---

$w$-$w$ axis:

$$M_{ywA} = F_y S_{wA}$$

$$= (50 \text{ ksi})(12.4 \text{ in.}^3)$$

$$= 620 \text{ kip-in.}$$

$$M_{nwA} = 1.5M_{ywA}$$
(from *Spec.* Eq. F10-1)

$$= 1.5(620 \text{ kip-in.})$$

$$= 930 \text{ kip-in.}$$

$$M_{ywB} = F_y S_{wB}$$

$$= (50 \text{ ksi})(16.3 \text{ in.}^3)$$

$$= 815 \text{ kip-in.}$$

$$M_{nwB} = 1.5M_{ywB}$$
(from *Spec.* Eq. F10-1)

$$= 1.5(815 \text{ kip-in.})$$

$$= 1,220 \text{ kip-in.}$$

$$M_{ywC} = F_y S_{wC}$$

$$= (50 \text{ ksi})(7.98 \text{ in.}^3)$$

$$= 399 \text{ kip-in.}$$

$$M_{nwC} = 1.5M_{ywC}$$
(from *Spec.* Eq. F10-1)

$$= 1.5(399 \text{ kip-in.})$$

$$= 599 \text{ kip-in.}$$

$z$-$z$ axis:

$$M_{yzA} = F_y S_{zA}$$

$$= (50 \text{ ksi})(1.82 \text{ in.}^3)$$

$$= 91.0 \text{ kip-in.}$$

$$M_{nzA} = 1.5M_{yzA}$$
(from *Spec.* Eq. F10-1)

$$= 1.5(91.0 \text{ kip-in.})$$

$$= 137 \text{ kip-in.}$$

$$M_{yzB} = F_y S_{zB}$$

$$= (50 \text{ ksi})(2.77 \text{ in.}^3)$$

$$= 139 \text{ kip-in.}$$

$$M_{nzB} = 1.5M_{yzB}$$
(from *Spec.* Eq. F10-1)

$$= 1.5(139 \text{ kip-in.})$$

$$= 209 \text{ kip-in.}$$

---

$$M_{yzC} = F_y S_{zC}$$

$$= (50 \text{ ksi})(5.81 \text{ in.}^3)$$

$$= 291 \text{ kip-in.}$$

$$M_{nzC} = 1.5M_{yzC}$$
(from *Spec.* Eq. F10-1)

$$= 1.5(291 \text{ kip-in.})$$

$$= 437 \text{ kip-in.}$$

Select the least $M_n$ for each axis.

For the limit state of yielding about the $w$-$w$ axis:

$$M_{nw} = 599 \text{ kip-in. at point C}$$

For the limit state of yielding about the $z$-$z$ axis:

$$M_{nz} = 137 \text{ kip-in. at point A}$$

*Lateral-Torsional Buckling*

From AISC *Specification* Section F10.2, the limit state of lateral-torsional buckling of a single angle without continuous restraint along its length is a function of the elastic lateral-torsional buckling moment about the major principal axis. For bending about the major principal axis for a single angle:

$$M_{cr} = \frac{9EA_g r_z IC_b}{8L_b}\left[\sqrt{1 + \left(4.4\frac{\beta_w r_z}{L_b t}\right)^2} + 4.4\frac{\beta_w r_z}{L_b t}\right]$$
(*Spec.* Eq. F10-4)

From AISC *Specification* Section F1, for uniform moment along the member length, $C_b = 1.0$. From AISC *Specification* Commentary Table C-F10.1, an L8×4×½ has $\beta_w = 5.48$ in. From AISC *Specification* Commentary Figure C-F10.4b, with the tip of the long leg (point C) in compression for bending about the $w$-axis, $\beta_w$ is taken as negative. Thus:

$$M_{cr} = \frac{9(29,000 \text{ ksi})(5.80 \text{ in.}^2)(0.863 \text{ in.})(\frac{1}{2} \text{ in.})(1.0)}{8(60.0 \text{ in.})}$$

$$\times \left\{\sqrt{1 + \left[4.4\frac{(-5.48 \text{ in.})(0.863 \text{ in.})}{(60.0 \text{ in.})(\frac{1}{2} \text{ in.})}\right]^2} + 4.4\frac{(-5.48 \text{ in.})(0.863 \text{ in.})}{(60.0 \text{ in.})(\frac{1}{2} \text{ in.})}\right\}$$

$$= 712 \text{ kip-in.}$$

$$\frac{M_{ywC}}{M_{cr}} = \frac{399 \text{ kip-in.}}{712 \text{ kip-in.}}$$

$$= 0.560$$

Because $M_{ywC}/M_{cr} < 1.0$, determine $M_n$ as follows:

---

$$M_{nwC} = \left[1.92 - 1.17\sqrt{\frac{M_{ywC}}{M_{cr}}}\right]M_{ywC} \leq 1.5M_{ywC}$$
(from *Spec.* Eq. F10-2)

$$= \left(1.92 - 1.17\sqrt{0.560}\right)(399 \text{ kip-in.}) < 1.5(399 \text{ kip-in.})$$

$$= 417 \text{ kip-in.} < 599 \text{ kip-in.}$$

$$= 417 \text{ kip-in.}$$

*Leg Local Buckling*

From AISC *Specification* Section F10.3, the limit state of leg local buckling applies when the toe of the leg is in compression. As discussed previously and indicated in Table E.14-1, the only case in which a toe is in compression is point C for bending about the $w$-$w$ axis. Thus, determine the slenderness of the long leg as a compression element subject to flexure. From AISC *Specification* Table B4.1b, Case 12:

$$\lambda_p = 0.54\sqrt{\frac{E}{F_y}}$$

$$= 0.54\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 13.0$$

$$\lambda_r = 0.91\sqrt{\frac{E}{F_y}}$$

$$= 0.91\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 21.9$$

$$\lambda = \frac{b}{t}$$

$$= \frac{8.0 \text{ in.}}{\frac{1}{2} \text{ in.}}$$

$$= 16.0$$

Because $\lambda_p < \lambda < \lambda_r$, the angle is noncompact for flexure for this loading. From AISC *Specification* Equation F10-6:

$$M_{nwC} = F_y S_{wC}\left[2.43 - 1.72\left(\frac{b}{t}\right)\sqrt{\frac{F_y}{E}}\right]$$
(from *Spec.* Eq. F10-6)

$$= (50 \text{ ksi})(7.98 \text{ in.}^3)\left[2.43 - 1.72(16.0)\sqrt{\frac{50 \text{ ksi}}{29,000 \text{ ksi}}}\right]$$

$$= 514 \text{ kip-in.}$$

Table E.14B-1 provides a summary of nominal flexural strength at each point. T indicates the point is in tension and C indicates it is in compression.

---

**Table E.14B-1**

| | | Yielding | | Lateral-Torsional Buckling | | Leg Local Buckling | |
|-------|-------------|-------------|-------------|-------------|-------------|-------------|
| Point | $M_{nw}$, kip-in. | $M_{nz}$, kip-in. | $M_{nw}$, kip-in. | $M_{nz}$, kip-in. | $M_{nw}$, kip-in. | $M_{nz}$, kip-in. |
| A | 930 T | 137 T | $-$ | $-$ | $-$ | $-$ |
| B | 1,220 T | 209 C | $-$ | $-$ | $-$ | $-$ |
| C | 599 C | 437 T | 417 C | $-$ | 514 C | $-$ |
| Note: (–) indicates that the limit state is not applicable to this point. | | | | | | |

*Available Flexural Strength*

Select the controlling nominal flexural strength for the $w$-$w$ and $z$-$z$ axes.

For the $w$-$w$ axis:

$$M_{nw} = 417 \text{ kip-in.}$$

For the $z$-$z$ axis:

$$M_{nz} = 137 \text{ kip-in.}$$

From AISC *Specification* Section F1, determine the available flexural strength for each axis, $w$-$w$ and $z$-$z$, as follows:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| | |
| $M_{cbw} = \phi_b M_{nw}$ | $M_{cbw} = \frac{M_{nw}}{\Omega_b}$ |
| $= 0.90(417 \text{ kip-in.})$ | $= \frac{417 \text{ kip-in.}}{1.67}$ |
| $= 375$ kip-in. | $= 250$ kip-in. |
| | |
| $M_{cbz} = \phi_b M_{nz}$ | $M_{cbz} = \frac{M_{nz}}{\Omega_b}$ |
| $= 0.90(137 \text{ kip-in.})$ | $= \frac{137 \text{ kip-in.}}{1.67}$ |
| $= 123$ kip-in. | $= 82.0$ kip-in. |

*Required Flexural Strength*

The load on the column is applied at eccentricities about the $w$-$w$ and $z$-$z$ axes resulting in the following moments:

$$M_w = P_r e_w$$

$$= P_r (1.44 \text{ in.})$$

and

$$M_z = P_r e_z$$

$$= P_r (0.889 \text{ in.})$$

---

The combination of axial load and moment will produce second-order effects in the column that must be accounted for.

Using AISC *Specification* Appendix 8.1, an approximate second-order analysis can be performed. The required second-order flexural strengths will be $B_{1w} M_w$ and $B_{1z} M_z$ respectively, where

$$B_1 = \frac{C_m}{1 - \frac{\alpha P_r}{P_{e1}}} \geq 1.0$$
(*Spec.* Eq. A-8-3)

and

$\alpha = 1.0$ (LRFD)
$\alpha = 1.6$ (ASD)
$C_m = 1.0$ for a column with uniform moment along its length

For each axis, parameters $P_{e1w}$ and $P_{e1z}$, as used in the moment magnification terms, $B_{1w}$ and $B_{1z}$, are:

$$P_{e1w} = \frac{\pi^2 EI_w}{(L_{c1})^2}$$
(from *Spec.* Eq. A-8-5)

$$= \frac{\pi^2 (29,000 \text{ ksi})(41.0 \text{ in.}^4)}{(60.0 \text{ in.})^2}$$

$$= 3,260 \text{ kips}$$

$$P_{e1z} = \frac{\pi^2 EI_z}{(L_{c1})^2}$$
(from *Spec.* Eq. A-8-5)

$$= \frac{\pi^2 (29,000 \text{ ksi})(4.32 \text{ in.}^4)}{(60.0 \text{ in.})^2}$$

$$= 343 \text{ kips}$$

and

$$B_{1w} = \frac{C_m}{1 - \frac{\alpha P_r}{P_{e1w}}}$$
(*Spec.* Eq. A-8-3)

$$= \frac{1.0}{1 - \frac{\alpha P_r}{3,260 \text{ kips}}}$$

$$B_{1z} = \frac{C_m}{1 - \frac{\alpha P_r}{P_{e1z}}}$$
(*Spec.* Eq. A-8-3)

$$= \frac{1.0}{1 - \frac{\alpha P_r}{343 \text{ kips}}}$$

Thus, the required second-order flexural strengths are:

---

$$M_{rw} = P_r (1.44 \text{ in.})\left(\frac{1.0}{1 - \frac{\alpha P_r}{3,260 \text{ kips}}}\right)$$

$$M_{rz} = P_r (0.889 \text{ in.})\left(\frac{1.0}{1 - \frac{\alpha P_r}{343 \text{ kips}}}\right)$$

*Interaction of Axial and Flexural Strength*

Evaluate the interaction of axial and flexural stresses according to the provisions of AISC *Specification* Section H2.

The interaction equation is given as:

$$\left|\frac{f_{cw}}{F_{ca}} + \frac{f_{cbw}}{F_{cbw}} + \frac{f_{cbz}}{F_{cbz}}\right| \leq 1.0$$
(*Spec.* Eq. H2-1)

where the stresses are to be considered at each point on the cross section with the appropriate sign representing the sense of the stress. Because the required stress and available stress at any point are both functions of the same section property, $A$ or $S$, it is possible to convert Equation H2-1 from a stress based equation to a force based equation where the section properties will cancel.

Substituting the available strengths and the expressions for the required second-order flexural strengths into AISC *Specification* Equation H2-1 yields:

| LRFD | ASD |
|------|-----|
| $\frac{P_u}{168 \text{ kips}} + \frac{P_u (1.44 \text{ in.})}{375 \text{ kip-in.}}\left(\frac{1.0}{1 - \frac{1.0P_u}{3,260 \text{ kips}}}\right)$ | $\frac{P_a}{112 \text{ kips}} + \frac{P_a (1.44 \text{ in.})}{250 \text{ kip-in.}}\left(\frac{1.0}{1 - \frac{1.6P_a}{3,260 \text{ kips}}}\right)$ |
| $+ \left[\frac{P_u (0.889 \text{ in.})}{123 \text{ kip-in.}}\right]\left(\frac{1}{1 - \frac{1.0P_u}{343 \text{ kips}}}\right)$ $\leq 1.0$ | $+ \left[\frac{P_a (0.889 \text{ in.})}{82.0 \text{ kip-in.}}\right]\left(\frac{1}{1 - \frac{1.6P_a}{343 \text{ kips}}}\right)$ $\leq 1.0$ |

These interaction equations must now be applied at each critical point on the section, points A, B, and C, using the appropriate sign for the sense of the resulting stress, with compression taken as positive.

For point A, the $w$ term is negative, and the $z$ term is negative. Thus:

| LRFD | ASD |
|------|-----|
| $\frac{P_u}{168 \text{ kips}} - \frac{P_u (1.44 \text{ in.})}{375 \text{ kip-in.}}\left(\frac{1.0}{1 - \frac{1.0P_u}{3,260 \text{ kips}}}\right)$ | $\frac{P_a}{112 \text{ kips}} - \frac{P_a (1.44 \text{ in.})}{250 \text{ kip-in.}}\left(\frac{1.0}{1 - \frac{1.6P_a}{3,260 \text{ kips}}}\right)$ |
| $- \left[\frac{P_u (0.889 \text{ in.})}{123 \text{ kip-in.}}\right]\left(\frac{1}{1 - \frac{1.0P_u}{343 \text{ kips}}}\right)$ $\leq 1.0$ | $- \left[\frac{P_a (0.889 \text{ in.})}{82.0 \text{ kip-in.}}\right]\left(\frac{1}{1 - \frac{1.6P_a}{343 \text{ kips}}}\right)$ $\leq 1.0$ |
| By iteration, $P_u = 114$ kips. | By iteration, $P_a = 73.7$ kips. |

For point B, the $w$ term is negative, and the $z$ term is positive. Thus:

---

| LRFD | ASD |
|------|-----|
| $\frac{P_u}{168 \text{ kips}} - \frac{P_u (1.44 \text{ in.})}{375 \text{ kip-in.}}\left(\frac{1.0}{1 - \frac{1.0P_u}{3,260 \text{ kips}}}\right)$ | $\frac{P_a}{112 \text{ kips}} - \frac{P_a (1.44 \text{ in.})}{250 \text{ kip-in.}}\left(\frac{1.0}{1 - \frac{1.6P_a}{3,260 \text{ kips}}}\right)$ |
| $+ \left[\frac{P_u (0.889 \text{ in.})}{123 \text{ kip-in.}}\right]\left(\frac{1}{1 - \frac{1.0P_u}{343 \text{ kips}}}\right)$ $\leq 1.0$ | $+ \left[\frac{P_a (0.889 \text{ in.})}{82.0 \text{ kip-in.}}\right]\left(\frac{1}{1 - \frac{1.6P_a}{343 \text{ kips}}}\right)$ $\leq 1.0$ |
| By iteration, $P_u = 85.9$ kips. | By iteration, $P_a = 56.4$ kips. |

For point C, the $w$ term is positive, and the $z$ term is negative. Thus:

| LRFD | ASD |
|------|-----|
| $\frac{P_u}{168 \text{ kips}} + \frac{P_u (1.44 \text{ in.})}{375 \text{ kip-in.}}\left(\frac{1.0}{1 - \frac{1.0P_u}{3,260 \text{ kips}}}\right)$ | $\frac{P_a}{112 \text{ kips}} + \frac{P_a (1.44 \text{ in.})}{250 \text{ kip-in.}}\left(\frac{1.0}{1 - \frac{1.6P_a}{3,260 \text{ kips}}}\right)$ |
| $- \left[\frac{P_u (0.889 \text{ in.})}{123 \text{ kip-in.}}\right]\left(\frac{1}{1 - \frac{1.0P_u}{343 \text{ kips}}}\right)$ $\leq 1.0$ | $- \left[\frac{P_a (0.889 \text{ in.})}{82.0 \text{ kip-in.}}\right]\left(\frac{1}{1 - \frac{1.6P_a}{343 \text{ kips}}}\right)$ $\leq 1.0$ |
| By iteration, $P_u = 183$ kips. | By iteration, $P_a = 116$ kips. |

*Governing Available Strength*

| LRFD | ASD |
|------|-----|
| From the above iterations, | From the above iterations, |
| $P_u = 85.9$ kips | $P_a = 56.4$ kips |
| From AISC *Manual* Table 4-12, | From AISC *Manual* Table 4-12, |
| $\phi P_n = 86.1$ kips | $\frac{P_n}{\Omega} = 56.5$ kips |

Note, the difference between the calculated vaues and the values from AISC *Manual* Table 4-12 are due to rounding. Thus, the calculations demonstrate how the values for this member in AISC *Manual* Table 4-12 can be confirmed.

---
