# Chapter E: Compression

**AISC 360-22 Specification for Structural Steel Buildings**
**Original PDF Pages**: 106-117 (12 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Design of Members for Compression

**Description**: Flexural buckling and compressive strength

---

# CHAPTER E
# DESIGN OF MEMBERS FOR COMPRESSION

This chapter addresses members subjected to axial compression.

The chapter is organized as follows:

- E1. General Provisions
- E2. Effective Length
- E3. Flexural Buckling of Members Without Slender Elements
- E4. Torsional and Flexural-Torsional Buckling of Single Angles and Members Without Slender Elements
- E5. Single-Angle Compression Members
- E6. Built-Up Members
- E7. Members with Slender Elements

**User Note:** For cases not included in this chapter, the following sections apply:
- H1–H2 Members subjected to combined axial compression and flexure
- H3 Members subjected to axial compression and torsion
- I2 Composite axially loaded members
- J4.4 Compressive strength of connecting elements

## E1. GENERAL PROVISIONS

The design compressive strength, $\phi_c P_n$, and the allowable compressive strength, $P_n/\Omega_c$, are determined as follows.

The nominal compressive strength, $P_n$, shall be the lowest value obtained based on the applicable limit states of flexural buckling, torsional buckling, and flexural-torsional buckling.

$$\phi_c = 0.90 \text{ (LRFD)} \qquad \Omega_c = 1.67 \text{ (ASD)}$$

---

## GENERAL PROVISIONS [Sect. E1.]

| **TABLE USER NOTE E1.1**<br/>**Selection Table for the Application of**<br/>**Chapter E Sections** |
|---|

| | **Without Slender<br/>Elements** | | **With Slender<br/>Elements** | |
|---|---|---|---|---|
| **Cross Section** | **Sections in<br/>Chapter E** | **Limit States** | **Sections in<br/>Chapter E** | **Limit<br/>States** |
| [I-section diagram] | E3<br/>E4 | FB<br/>TB | E7 | LB<br/>FB<br/>TB |
| [Channel and I-section diagrams] | E3<br/>E4 | FB<br/>FTB | E7 | LB<br/>FB<br/>FTB |
| [Rectangular HSS diagram] | E3 | FB | E7 | LB<br/>FB |
| [Round HSS diagram] | E3 | FB | E7 | LB<br/>FB |
| [Tee section diagram] | E3<br/>E4 | FB<br/>FTB | E7 | LB<br/>FB<br/>FTB |
| [Double tee diagram] | E6<br/>E3<br/>E4 | FB<br/>FTB | E6<br/>E7 | LB<br/>FB<br/>FTB |
| [Angle diagrams] | E3<br/>E4<br/>E5 | FB<br/>FTB | E5<br/>E7 | LB<br/>FB |
| [Round and rectangular filled diagrams] | E3 | FB | NA | NA |
| Unsymmetrical shapes other than single angles | E4 | FTB | E7 | LB<br/>FTB |

FB = flexural buckling; FTB = flexural-torsional buckling; LB = local buckling; TB = torsional buckling; NA = not applicable

---

## EFFECTIVE LENGTH [Sect. E2.

## E2. EFFECTIVE LENGTH

The effective length, $L_c$, for calculation of member slenderness, $L_c/r$, shall be determined in accordance with Chapter C or Appendix 7,

where

$L_c$ = effective length of member, in. (mm)
= $KL$
$K$ = effective length factor
$L$ = laterally unbraced length of the member, in. (mm)
$r$ = radius of gyration, in. (mm)

**User Note:** For members designed on the basis of compression, the effective slenderness ratio, $L_c/r$, preferably should not exceed 200. Furthermore, the slenderness ratio of the member as fabricated—taken as the fabricated length of the member divided by the least radius of gyration of the section—preferably should not exceed 300.

**User Note:** The effective length, $L_c$, may be determined using an effective length factor, $K$, or a buckling analysis.

## E3. FLEXURAL BUCKLING OF MEMBERS WITHOUT SLENDER ELEMENTS

This section applies to nonslender-element compression members, as defined in Section B4.1, for elements in axial compression.

**User Note:** When the torsional effective length is larger than the lateral effective length, Section E4 may control.

The nominal compressive strength, $P_n$, shall be determined based on the limit state of flexural buckling:

$$P_n = F_{cr} A_g$$ (E3-1)

The nominal stress, $F_{cr}$, is determined as follows:

(a) When $\frac{L_c}{r} \leq 4.71\sqrt{\frac{E}{F_y}}$ (or $\frac{F_y}{F_e} \leq 2.25$)

$$F_{cr} = \left(0.658^{\frac{F_y}{F_e}}\right)F_y$$ (E3-2)

(b) When $\frac{L_c}{r} > 4.71\sqrt{\frac{E}{F_y}}$ (or $\frac{F_y}{F_e} > 2.25$)

$$F_{cr} = 0.877F_e$$ (E3-3)

---

## TORSIONAL AND FLEXURAL-TORSIONAL BUCKLING [Sect. E4.]

where

$A_g$ = gross area of member, in.$^2$ (mm$^2$)
$E$ = modulus of elasticity of steel, ksi (MPa)
= 29,000 ksi (200 000 MPa)
$F_e$ = elastic buckling stress determined according to Equation E3-4; or as specified in Appendix 7, Section 7.2.3(b); or through an elastic buckling analysis, as applicable, ksi (MPa)

$$= \frac{\pi^2 E}{\left(\frac{L_c}{r}\right)^2}$$ (E3-4)

$F_y$ = specified minimum yield stress of the type of steel being used, ksi (MPa)
$r$ = radius of gyration, in. (mm)

**User Note:** The two inequalities for calculating the limits of applicability of Sections E3(a) and E3(b), one based on $L_c/r$ and one based on $F_y / F_e$, provide the same result for flexural buckling.

## E4. TORSIONAL AND FLEXURAL-TORSIONAL BUCKLING OF SINGLE ANGLES AND MEMBERS WITHOUT SLENDER ELEMENTS

This section applies to singly symmetric and unsymmetric members, certain doubly symmetric members, such as cruciform or built-up members, and doubly symmetric members when the torsional unbraced length exceeds the lateral unbraced length, all without slender elements. These provisions also apply to single angles with $b/t > 0.71\sqrt{E/F_y}$, where $b$ is the width of the longest leg and $t$ is the thickness.

The nominal compressive strength, $P_n$, shall be determined based on the limit states of torsional and flexural-torsional buckling:

$$P_n = F_{cr} A_g$$ (E4-1)

The nominal stress, $F_{cr}$, shall be determined according to Equation E3-2 or E3-3, using the torsional or flexural-torsional elastic buckling stress, $F_e$, determined as follows:

(a) For doubly symmetric members twisting about the shear center

$$F_e = \left(\frac{\pi^2 EC_w}{L_{cz}^2} + GJ\right)\frac{1}{I_x + I_y}$$ (E4-2)

(b) For singly symmetric members twisting about the shear center where y is the axis of symmetry

$$F_e = \left(\frac{F_{ey} + F_{ez}}{2H}\right)\left[1 - \sqrt{1 - \frac{4F_{ey}F_{ez}H}{(F_{ey} + F_{ez})^2}}\right]$$ (E4-3)

---

## TORSIONAL AND FLEXURAL-TORSIONAL BUCKLING [Sect. E4.

**User Note:** For singly symmetric members with the x-axis as the axis of symmetry, such as channels, Equation E4-3 is applicable with $F_{ey}$ replaced by $F_{ex}$.

(c) For unsymmetric members twisting about the shear center, $F_e$ is the lowest root of the cubic equation

$$\left(F_e - F_{ex}\right)\left(F_e - F_{ey}\right)\left(F_e - F_{ez}\right) - F_e^2\left(F_e - F_{ey}\right)\left(\frac{x_o}{\bar{r}_o}\right)^2 - F_e^2\left(F_e - F_{ex}\right)\left(\frac{y_o}{\bar{r}_o}\right)^2 = 0$$

(E4-4)

where

$C_w$ = warping constant, in.$^6$ (mm$^6$)

$$F_{ex} = \frac{\pi^2 E}{\left(\frac{L_{cx}}{r_x}\right)^2}$$ (E4-5)

$$F_{ey} = \frac{\pi^2 E}{\left(\frac{L_{cy}}{r_y}\right)^2}$$ (E4-6)

$$F_{ez} = \left(\frac{\pi^2 EC_w}{L_{cz}^2} + GJ\right)\frac{1}{A_g\bar{r}_o^2}$$ (E4-7)

$G$ = shear modulus of elasticity of steel
= 11,200 ksi (77 200 MPa)

$H$ = flexural constant

$$= 1 - \frac{x_o^2 + y_o^2}{\bar{r}_o^2}$$ (E4-8)

$I_x$, $I_y$ = moment of inertia about the principal axes, in.$^4$ (mm$^4$)

$J$ = torsional constant, in.$^4$ (mm$^4$)

$K_x$ = effective length factor for flexural buckling about x-axis

$K_y$ = effective length factor for flexural buckling about y-axis

$K_z$ = effective length factor for torsional buckling about the longitudinal axis

$L_{cx}$ = effective length of member for buckling about x-axis, in. (mm)
= $K_x L_x$

$L_{cy}$ = effective length of member for buckling about y-axis, in. (mm)
= $K_y L_y$

$L_{cz}$ = effective length of member for buckling about longitudinal axis, in. (mm)
= $K_z L_z$

$L_x$, $L_y$, $L_z$ = laterally unbraced length of the member for each axis, in. (mm)

$\bar{r}_o$ = polar radius of gyration about the shear center, in. (mm)

$$\bar{r}_o^2 = x_o^2 + y_o^2 + \frac{I_x + I_y}{A_g}$$ (E4-9)

$r_x$ = radius of gyration about x-axis, in. (mm)

$r_y$ = radius of gyration about y-axis, in. (mm)

$x_o$, $y_o$ = coordinates of the shear center with respect to the centroid, in. (mm)

---

## SINGLE-ANGLE COMPRESSION MEMBERS [Sect. E5.]

**User Note:** For doubly symmetric I-shaped sections, $C_w$ may be taken as $I_y h_o^2/4$, where $h_o$ is the distance between flange centroids, in lieu of a more precise analysis. For tees and double angles, the term with $C_w$ may be omitted when computing $F_{ez}$.

(d) For doubly symmetric I-shaped members with minor-axis lateral bracing offset from the shear center

$$F_e = \left[\frac{\pi^2 EI_y}{L_c^2}\left(\frac{h_o^2}{4} + y_d^2\right) + GJ\right]\frac{1}{A_g r_o^2}$$ (E4-10)

where

$h_o$ = distance between flange centroids, in. (mm)

$$r_o^2 = r_x^2 + r_y^2 + y_d^2 + x_d^2$$ (E4-11)

$x_d$ = bracing offset distance along x-axis = 0
$y_d$ = bracing offset distance along y-axis, in. (mm)

(e) For doubly symmetric I-shaped members with major-axis lateral bracing offset from the shear center

$$F_e = \left[\frac{\pi^2 EI_x}{L_c^2}\left(\frac{h_o^2}{4} + \frac{I_x}{I_y}x_d^2\right) + GJ\right]\frac{1}{A_g r_o^2}$$ (E4-12)

where

$$r_o^2 = r_x^2 + r_y^2 + y_d^2 + x_d^2$$ (E4-11)

$x_d$ = bracing offset distance along x-axis, in. (mm)
$y_d$ = bracing offset distance along y-axis = 0

(f) For all other members with lateral bracing offset from the shear center, the elastic buckling stress, $F_e$, shall be determined by analysis.

**User Note:** Bracing offset from the shear center is often referred to as constrained-axis torsional buckling and is discussed further in the Commentary. Members that buckle in this mode will exhibit twisting because the braces restrain only lateral movement.

## E5. SINGLE-ANGLE COMPRESSION MEMBERS

The nominal compressive strength, $P_n$, of single-angle members shall be the lowest value based on the limit states of flexural buckling in accordance with Section E3 or if applicable, or flexural-torsional buckling in accordance with Section E4. Flexural-torsional buckling need not be considered when $b/t \leq 0.71\sqrt{E/F_y}$.

The effects of eccentricity on single-angle members are permitted to be neglected and the member evaluated as axially loaded using one of the effective slenderness ratios specified in Section E5(a) or E5(b), provided that the following requirements are met:

---

## SINGLE-ANGLE COMPRESSION MEMBERS [Sect. E5.

(1) Members are loaded at the ends in compression through the same one leg.

(2) Members are attached by welding or by connections with a minimum of two bolts.

(3) There are no intermediate transverse loads.

(4) $L_c/r$ as determined in this section does not exceed 200.

(5) For unequal leg angles, the ratio of long leg width to short leg width is less than 1.7.

Single-angle members that do not meet these requirements or the requirements described in Section E5(a) or (b) shall be evaluated for combined axial load and flexure using the provisions of Chapter H.

(a) For angles that are individual members or are web members of planar trusses with adjacent web members attached to the same side of the gusset plate or chord

(1) For equal-leg angles or unequal-leg angles connected through the longer leg

(i) When $\frac{L}{r_a} \leq 80$

$$\frac{L_c}{r} = 72 + 0.75\frac{L}{r_a}$$ (E5-1)

(ii) When $\frac{L}{r_a} > 80$

$$\frac{L_c}{r} = 32 + 1.25\frac{L}{r_a}$$ (E5-2)

(2) For unequal-leg angles connected through the shorter leg, $L_c/r$ from Equations E5-1 and E5-2 shall be increased by adding $4\left[\left(b_l/b_s\right)^2 - 1\right]$, but $L_c/r$ of the members shall not be taken as less than $0.95L/r_z$.

(b) For angles that are web members of box or space trusses with adjacent web members attached to the same side of the gusset plate or chord

(1) For equal-leg angles or unequal-leg angles connected through the longer leg

(i) When $\frac{L}{r_a} \leq 75$

$$\frac{L_c}{r} = 60 + 0.8\frac{L}{r_a}$$ (E5-3)

(ii) When $\frac{L}{r_a} > 75$

$$\frac{L_c}{r} = 45 + \frac{L}{r_a}$$ (E5-4)

(2) For unequal-leg angles with leg length ratios less than 1.7 and connected through the shorter leg, $L_c/r$ from Equations E5-3 and E5-4 shall be increased by adding $6\left[\left(b_l/b_s\right)^2 - 1\right]$, but $L_c/r$ of the member shall not be taken as less than $0.82L/r_z$.

---

## BUILT-UP MEMBERS [Sect. E6.]

where

$L$ = length of member between work points at truss chord centerlines, in. (mm)
$L_c$ = effective length of the member for buckling about the minor axis, in. (mm)
$b_l$ = length of longer leg of angle, in. (mm)
$b_s$ = length of shorter leg of angle, in. (mm)
$r_a$ = radius of gyration about the geometric axis parallel to the connected leg, in. (mm)
$r_z$ = radius of gyration about the minor principal axis, in. (mm)

## E6. BUILT-UP MEMBERS

### 1. Compressive Strength

This section applies to built-up members composed of two shapes either (a) interconnected by bolts or welds or (b) with at least one open side interconnected by perforated cover plates or lacing with tie plates. The end connection shall be welded or connected by means of pretensioned bolts with Class A or B faying surfaces.

**User Note:** It is acceptable to design a bolted end connection of a built-up compression member for the full compressive load with bolts in bearing and bolt design based on the shear strength; however, the bolts perform better in pretensioned built-up compression members, such as double-angle struts in trusses, a small relative slip between the elements can significantly reduce the compressive strength of the strut. Therefore, the connection between the elements of the ends of built-up members should be designed to resist slip.

The nominal compressive strength of built-up members composed of two shapes that are interconnected by bolts or welds shall be determined in accordance with Sections E3, E4, or E7, subject to the following modification. In lieu of a more accurate analysis, if the buckling mode involves relative deformations that produce shear forces in the connectors between individual shapes, $L_c/r$ is replaced by $(L_c/r)_m$, determined as follows:

(a) For intermediate connectors that are bolted snug-tight

$$\left(\frac{L_c}{r}\right)_m = \sqrt{\left(\frac{L_c}{r}\right)_o^2 + \left(\frac{a}{r_i}\right)^2}$$ (E6-1)

(b) For intermediate connectors that are welded or are connected by means of pretensioned bolts with Class A or B faying surfaces

(1) When $\frac{a}{r_i} \leq 40$

$$\left(\frac{L_c}{r}\right)_m = \left(\frac{L_c}{r}\right)_o$$ (E6-2a)

---

## BUILT-UP MEMBERS [Sect. E6.

(2) When $\frac{a}{r_i} > 40$

$$\left(\frac{L_c}{r}\right)_m = \sqrt{\left(\frac{L_c}{r}\right)_o^2 + \left(\frac{K_i a}{r_i}\right)^2}$$ (E6-2b)

where

$\left(\frac{L_c}{r}\right)_m$ = modified slenderness ratio of built-up member

$\left(\frac{L_c}{r}\right)_o$ = slenderness ratio of built-up member acting as a unit in the buckling direction being addressed

$L_c$ = effective length of built-up member, in. (mm)
$K_i$ = 0.50 for angles back-to-back
= 0.75 for channels back-to-back
= 0.86 for all other cases

$a$ = distance between connectors, in. (mm)
$r_i$ = minimum radius of gyration of individual component, in. (mm)

### 2. General Requirements

Built-up members shall meet the following requirements:

(a) Individual components of compression members composed of two or more shapes that are connected to one another at intervals, $a$, such that the slenderness ratio, $a/r_i$, of each of the component shapes between the fasteners does not exceed three-fourths times the governing slenderness ratio for the built-up member. The minimum radius of gyration, $r_i$, shall be used in computing the slenderness ratio of each component part.

(b) At the ends of built-up compression members bearing on base plates or finished surfaces, all components in contact with one another shall be connected by a weld having a length not less than the maximum width of the member or by bolts spaced longitudinally not more than four diameters apart for a distance apart for a distance equal to 1½ times the maximum width of the member.

Along the length of built-up compression members between the end connections required in the foregoing, longitudinal spacing of intermittent welds or bolts shall be adequate to provide the required strength. For limitations on the longitudinal spacing of fasteners between elements in continuous contact consisting of a plate and a shape, or two plates, see Section J3.6. Where a component of a built-up compression member consists of an outside plate, the maximum spacing shall not exceed the thickness of the thinner outside plate times $0.75\sqrt{E/F_y}$, nor 12 in. (300 mm), when intermittent welds are provided along the edges of the components or when fasteners are provided on all gage lines at each section. When fasteners are staggered, the maximum spacing of fasteners on each gage line shall not exceed the thickness of the thinner outside plate times $1.12\sqrt{E/F_y}$, nor 18 in. (450 mm).

---

## BUILT-UP MEMBERS [Sect. E6.]

(c) Open sides of compression members built up from plates or shapes shall be provided with continuous cover plates perforated with a succession of access openings. The unsupported width of such plates at access openings, as defined in Section B4.1, is assumed to contribute to the available strength provided the following requirements are met:

(1) The width-to-thickness ratio shall conform to the limitations of Section B4.1.

**User Note:** It is conservative to use the limiting width-to-thickness ratio for Case 7 in Table B4.1a with the width, $b$, taken as the transverse distance between the nearest lines of fasteners. The net area of the plate is taken at the widest hole. In lieu of this approach, the limiting width-to-thickness ratio may be determined through analysis.

(2) The ratio of length (in direction of stress) to width of hole shall not exceed 2.

(3) The clear distance between holes in the direction of stress shall be not less than the transverse distance between nearest lines of connecting fasteners or welds.

(4) The periphery of the holes at all points shall have a minimum radius of 1½ in. (38 mm).

(d) As an alternative to perforated cover plates, lacing with tie plates is permitted at each end and at intermediate points if the lacing is interrupted. Tie plates shall be as near the ends as practicable. In members providing available strength, the end tie plates shall have a length of not less than the distance between the lines of fasteners or welds connecting them to the components of the member. Intermediate tie plates shall have a length not less than one-half of this distance. The thickness of tie plates shall be not less than one-fiftieth of the distance between lines of welds or fasteners connecting them to the segments of the members. In welded construction, the welding on each line connecting a tie plate shall not be less than one-third the length of the plate. In bolted construction, the spacing in the direction of stress in tie plates shall be not more than six diameters and the tie plates shall be connected to each segment by at least three fasteners.

(e) Lacing, including flat bars, angles, channels, or other shapes employed as lacing, shall be so spaced that $L/r$ of the flange element included between their connections shall not exceed three-fourths times the governing slenderness ratio for the member as a whole. Lacing shall be proportioned to provide a shearing strength normal to the axis of the member equal to 2% of the available compressive strength of the member. For lacing bars arranged in single systems, $L/r$ shall not exceed 140. For double lacing, this ratio shall not exceed 200. Double lacing bars shall be joined at the intersections. For lacing bars in compression, $L$ is permitted to be taken as the unsupported length of the lacing bar between welds or fasteners connecting it to the components of the built-up member for single lacing, and 70% of that distance for double lacing.

---

## BUILT-UP MEMBERS [Sect. E6.

**User Note:** The inclination of lacing bars to the axis of the member shall preferably be not less than 60° for single lacing and 45° for double lacing. When the distance between the lines of welds or fasteners in the flanges is more than 15 in. (380 mm), the lacing should preferably be double or made of angles.

For additional spacing requirements, see Section J3.6.

## E7. MEMBERS WITH SLENDER ELEMENTS

This section applies to slender-element compression members, as defined in Section B4.1 for elements in axial compression.

The nominal compressive strength, $P_n$, shall be the lowest value based on the applicable limit states of flexural buckling, torsional buckling, and flexural-torsional buckling in interaction with local buckling.

$$P_n = F_{cr} A_e$$ (E7-1)

where

$A_e$ = summation of the effective areas of the cross section based on reduced effective widths, $b_e$, $d_e$, or $h_e$, or the area as given by Equation E7-6 or E7-7, in.$^2$ (mm$^2$)

$F_n$ = nominal stress determined in accordance with Section E3 or E4, ksi (MPa). For single angles, determine $F_n$ in accordance with Section E3 only.

**User Note:** The effective area, $A_e$, may be determined by deducting from the gross area, $A_g$, the reduction in area of each slender element determined as $(b - b_e)t$.

### 1. Slender Element Members Excluding Round HSS

The effective width, $b_e$ (for tees, this is $d_e$; for webs, this is $h_e$), for slender elements is determined as follows:

(a) When $\lambda \leq \lambda_r \sqrt{\frac{F_y}{F_n}}$

$$b_e = b$$ (E7-2)

(b) When $\lambda > \lambda_r \sqrt{\frac{F_y}{F_n}}$

$$b_e = b\left(1 - c_1\sqrt{\frac{F_{el}}{F_n}}\right)\sqrt{\frac{F_{el}}{F_n}}$$ (E7-3)

where

$b$ = width of the element (for tees this is $d$; for webs this is $h$), in. (mm)
$c_1$ = effective width imperfection adjustment factor determined from Table E7.1

$$c_2 = \frac{1 - \sqrt{1 - 4c_1}}{2c_1}$$ (E7-4)

---

## MEMBERS WITH SLENDER ELEMENTS [Sect. E7.]

| **TABLE E7.1**<br/>**Effective Width Imperfection Adjustment Factors,**<br/>$c_1$ **and** $c_2$ |
|---|

| **Case** | **Slender Element** | $c_1$ | $c_2$ |
|---|---|---|---|
| (a) | Stiffened elements except walls of square and rectangular HSS | 0.18 | 1.31 |
| (b) | Walls of square and rectangular HSS | 0.20 | 1.38 |
| (c) | All other elements | 0.22 | 1.49 |

$\lambda$ = width-to-thickness ratio for the element as defined in Section B4.1
$\lambda_r$ = limiting width-to-thickness ratio as defined in Table B4.1a

$$F_{el} = \left(c_2\frac{\lambda_r}{\lambda}\right)^2 F_y$$ (E7-5)

= elastic local buckling stress determined according to Equation E7-5 or an elastic local buckling analysis, ksi (MPa)

### 2. Round HSS

The effective area, $A_e$, is determined as follows:

(a) When $\frac{D}{t} \leq 0.11\frac{E}{F_y}$

$$A_e = A_g$$ (E7-6)

(b) When $0.11\frac{E}{F_y} < \frac{D}{t} < 0.45\frac{E}{F_y}$

$$A_e = \left[\frac{0.038E}{F_y(D/t)} + \frac{2}{3}\right]A_g$$ (E7-7)

where

$D$ = outside diameter of round HSS, in. (mm)
$t$ = thickness of wall, in. (mm)

---
