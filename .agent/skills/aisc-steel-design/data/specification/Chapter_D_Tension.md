# Chapter D: Tension

**AISC 360-22 Specification for Structural Steel Buildings**
**Original PDF Pages**: 100-105 (6 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Design of Members for Tension

**Description**: Tensile strength and effective net area

---

# CHAPTER D
# DESIGN OF MEMBERS FOR TENSION

This chapter applies to members subjected to axial tension.

The chapter is organized as follows:

- D1. Slenderness Limitations
- D2. Tensile Strength
- D3. Effective Net Area
- D4. Built-Up Members
- D5. Pin-Connected Members
- D6. Eyebars

**User Note:** For cases not included in this chapter, the following sections apply:
- B3.11 Members subjected to fatigue
- Chapter H Members subjected to combined axial tension and flexure
- J3 Threaded rods
- J4.1 Connecting elements in tension
- J4.3 Block shear rupture strength at end connections of tension members

## D1. SLENDERNESS LIMITATIONS

There is no maximum slenderness limit for members in tension.

**User Note:** For members designed on the basis of tension, the slenderness ratio of the member as fabricated—taken as the fabricated length of the member divided by the least radius of gyration of the section—preferably should not exceed 300. This suggestion does not apply to rods.

## D2. TENSILE STRENGTH

The design tensile strength, $\phi_t P_n$, and the allowable tensile strength, $P_n/\Omega_t$, of tension members shall be the lower value obtained according to the limit states of tensile yielding in the gross section and tensile rupture in the net section.

(a) For tensile yielding

$$P_n = F_y A_g$$ (D2-1)

$$\phi_t = 0.90 \text{ (LRFD)} \qquad \Omega_t = 1.67 \text{ (ASD)}$$

---

## BUILT-UP MEMBERS [Sect. D4.]

(b) For tensile rupture

$$P_n = F_u A_e$$ (D2-2)

$$\phi_t = 0.75 \text{ (LRFD)} \qquad \Omega_t = 2.00 \text{ (ASD)}$$

where

$A_e$ = effective net area, in.$^2$ (mm$^2$)
$A_g$ = gross area of member, in.$^2$ (mm$^2$)
$F_y$ = specified minimum yield stress, ksi (MPa)
$F_u$ = specified minimum tensile strength, ksi (MPa)

Where connections use plug, slot, or fillet welds in holes or slots, the effective net area through the holes shall be used in Equation D2-2.

## D3. EFFECTIVE NET AREA

The gross area, $A_g$, and net area, $A_n$, of tension members shall be determined in accordance with the provisions of Section B4.3.

The effective net area of tension members shall be determined as

$$A_e = A_n U$$ (D3-1)

where $U$, the shear lag factor, is determined as shown in Table D3.1.

For open cross sections such as W, M, S, C, or HP shapes, WTs, STs, and single and double angles, the shear lag factor, $U$, need not be less than the ratio of the gross area of the connected element(s) to the member gross area. This provision does not apply to closed sections, such as HSS, nor to plates.

## D4. BUILT-UP MEMBERS

For limitations on the longitudinal spacing of connectors between elements in continuous contact consisting of a plate and a shape, or two plates, see Section J3.5.

Lacing, perforated cover plates, or tie plates without lacing are permitted to be used on the open sides of built-up tension members. Tie plates shall have a length not less than two-thirds the distance between the lines of welds or fasteners connecting them to the components of the member. The thickness of such tie plates shall not be less than one-fiftieth of the distance between these lines. The longitudinal spacing of intermittent welds or fasteners at tie plates shall not exceed 6 in. (150 mm).

**User Note:** The longitudinal spacing of connectors between components should preferably limit the slenderness ratio in any component between the connectors to 300.

---

## BUILT-UP MEMBERS [Sect. D4.

| **TABLE D3.1**<br/>**Shear Lag Factors for Connections**<br/>**to Tension Members** |
|---|

| **Case** | **Description of Element** | **Shear Lag Factor, $U$** | **Examples** |
|---|---|---|---|
| 1 | All tension members where the tension load is transmitted directly to each of the cross-sectional elements by fasteners or welds (except as in Cases 4, 5, and 6). | $U = 1.0$ | – |
| 2 | All tension members, except HSS, where the tension load is transmitted to some but not all of the cross-sectional elements by fasteners or by longitudinal welds in combination with transverse welds. Alternatively, Case 7 is permitted for W, M, S, and HP shapes and Case 8 is permitted for angles. | $U = 1 - \frac{\bar{x}}{l}$ | [Diagrams showing I-sections, channels, and double angles with dimension $\bar{x}$ and $l$ marked] |
| 3 | All tension members where the tension load is transmitted only by transverse welds to some but not all of the cross-sectional elements. | $U = 1.0$ and<br/>$A_n$ = area of the directly connected elements | – |
| 4[a] | Plates, angles, or channels with welds at heels, toes, and W-shapes with connected element only, where the tension load is transmitted by longitudinal welds only. See Case 7 for definition of $\bar{x}$. | $U = \frac{3l^2}{3l^2 + w^2}\left(1 - \frac{\bar{x}}{l}\right)$ | [Diagram showing W-section and plate/connected element with dimensions $l$, $w$, and $\bar{x}$ marked] |
| 5 | Round and rectangular HSS with single concentric gusset plate through slots in the HSS. | $\bar{x} = \frac{R\sin\theta}{\theta} - \frac{1}{2}t_p$<br/>(θ in rad)<br/>$U = 1 + \left(\frac{\bar{x}}{l}\right)^{2.2}$^10<br/>or<br/>$\bar{x} = b - \frac{2h^2 + t_H - 2t^2}{2H + 4b - 4t}$<br/>$U = 1 - \frac{\bar{x}}{l}$ | [Diagrams showing round HSS with radius R and rectangular HSS with dimensions H, B, and $\bar{x}$ marked] |
| 6 | Rectangular HSS with two side gusset plates. | $U = \frac{BL_B + HL_H}{H + B}$<br/>$U_B = \frac{3l^2}{3l^2 + B^2}$<br/>$U_H = \frac{3l^2}{3l^2 + H^2}$ | [Diagram showing rectangular HSS with side plates and dimensions B, H marked] |

$B$ = overall width of rectangular HSS member, measured 90° to the plane of the connection, in. (mm);
$D$ = outside diameter of round HSS, in. (mm); $H$ = overall height of rectangular HSS member, measured in the plane of the connection, in. (mm); $d$ = depth of section, in. (mm); for tees, $d$ = depth of the section from which the tee was cut, in. (mm); $l$ = length of connection, in. (mm); $w$ = width of plate, in. (mm); $\bar{x}$ = eccentricity of connection, in. (mm).

$\frac{l + l_2}{2}$ , where $l_1$ and $l_2$ shall not be less than 4 times the weld size.

---

## PIN-CONNECTED MEMBERS [Sect. D5.]

| **TABLE D3.1 (continued)**<br/>**Shear Lag Factors for Connections**<br/>**to Tension Members** |
|---|

| **Case** | **Description of Element** | **Shear Lag Factor, $U$** | **Examples** |
|---|---|---|
| 7 | W-, M-, S-, or HP-shapes, channels, or tees cut from these shapes. (If $U$ is calculated per Case 2, the larger value is permitted to be used.) | with flange connected with three or more fasteners per line in the direction of loading | $b_f \geq \frac{2}{3}d, U = 0.90$<br/>$b_f < \frac{2}{3}d, U = 0.85$ |
| | | with web connected with four or more fasteners per line in the direction of loading | $U = 0.70$ |
| 8 | Single and double angles. (If $U$ is calculated per Case 2, the larger value is permitted to be used.) | with four or more fasteners per line in the direction of loading | $U = 0.80$ |
| | | with three fasteners per line in the direction of loading (with fewer than three fasteners per line in the direction of loading, use Case 2) | $U = 0.60$ |

$B$ = overall width of rectangular HSS member, measured 90° to the plane of the connection, in. (mm);
$D$ = outside diameter of round HSS, in. (mm); $H$ = overall height of rectangular HSS member, measured in the plane of the connection, in. (mm); $d$ = depth of section, in. (mm); for tees, $d$ = depth of the section from which the tee was cut, in. (mm); $l$ = length of connection, in. (mm); $w$ = width of plate, in. (mm); $\bar{x}$ = eccentricity of connection, in. (mm).

$b_f = \frac{l + l_2}{2}$, where $l_1$ and $l_2$ shall not be less than 4 times the weld size.

## D5. PIN-CONNECTED MEMBERS

### 1. Tensile Strength

The design tensile strength, $\phi_t P_n$, and the allowable tensile strength, $P_n/\Omega_t$, of pin-connected members, shall be the lower value determined according to the limit states of tensile rupture, shear rupture, bearing, and yielding.

(a) For tensile rupture

$$P_n = F_u(2tb_e)$$ (D5-1)

$$\phi_t = 0.75 \text{ (LRFD)} \qquad \Omega_t = 2.00 \text{ (ASD)}$$

(b) For shear rupture

$$P_n = 0.6C_r F_u A_{sf}$$ (D5-2)

$$\phi_t = 0.75 \text{ (LRFD)} \qquad \Omega_t = 2.00 \text{ (ASD)}$$

where

$$A_{sf} = 2t(a + d/2)$$

= area on the shear failure path, in.$^2$ (mm$^2$)

---

## PIN-CONNECTED MEMBERS [Sect. D5.

$C_r$ = reduction factor for shear rupture on pin-connected members
= 1.0 when $d_h - d \leq \frac{1}{32}$ in. (1 mm)
= 0.95 when $\frac{1}{32}$ in. $< d_h - d \leq \frac{1}{16}$ in. (1 mm $< d_h - d \leq$ 2 mm)

$a$ = shortest distance from edge of the pin hole to the edge of the member measured parallel to the direction of the force, in. (mm)

$b_e$ = $2t + 0.63$, in. (= $2t + 16$, mm), but not more than the actual distance from the edge of the hole to the edge of the part measured in the direction normal to the applied force, in. (mm)

$d$ = diameter of pin, in. (mm)

$d_h$ = diameter of hole, in. (mm)

$t$ = thickness of plate, in. (mm)

(c) For bearing on the projected area of the pin, use Section J7.

(d) For yielding on the gross section, use Section D2(a).

### 2. Dimensional Requirements

Pin-connected members shall meet the following requirements:

(a) The pin hole shall be located midway between the edges of the member in the direction normal to the applied force.

(b) When the pin is expected to provide for relative movement between connected parts while under full load, the diameter of the pin hole shall not be more than $\frac{1}{32}$ in. (1 mm) greater than the diameter of the pin for pins of 3 in. (75 mm) in diameter and not more than $\frac{1}{16}$ in. (2 mm) greater than the diameter of the pin for pins of 3 in. (75 mm) in diameter or greater.

(c) The width of the plate at the pin hole shall not be less than $2b_e + d$, and the minimum extension, $a$, beyond the bearing end of the pin hole, parallel to the axis of the member, shall not be less than $1.33b_e$.

(d) The corners beyond the pin hole are permitted to be cut at 45° to the axis of the member, provided the net area beyond the pin hole, on a plane perpendicular to the cut, is not less than that required beyond the pin hole parallel to the axis of the member.

## D6. EYEBARS

### 1. Tensile Strength

The available tensile strength of eyebars shall be determined in accordance with Section D2, with $A_g$ taken as the gross area of the eyebar body.

For calculation purposes, the width of the body of the eyebar shall not exceed eight times its thickness.

---

## EYEBARS [Sect. D6.]

## 2. Dimensional Requirements

Eyebars shall meet the following requirements:

(a) Eyebars shall be of uniform thickness, without reinforcement at the pin holes, and have circular heads with the periphery concentric with the pin hole.

(b) The radius of transition between the circular head and the eyebar body shall not be less than the head diameter.

(c) The pin diameter shall not be less than seven-eighths times the eyebar body width, and the pin-hole diameter shall not be more than $\frac{1}{32}$ in. (1 mm) greater than the pin diameter.

(d) For steels having $F_y$ greater than 70 ksi (485 MPa), the hole diameter shall not exceed five times the plate thickness, and the width of the eyebar body shall be reduced accordingly.

(e) A thickness of less than $\frac{1}{2}$ in. (13 mm) is permissible only if external nuts are provided to tighten pin plates and filler plates into snug contact.

(f) The width from the hole edge to the plate edge perpendicular to the direction of applied load shall be greater than two-thirds and, for the purpose of calculation, not more than three-fourths times the eyebar body width.

---
