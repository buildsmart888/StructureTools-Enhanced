# Chapter G: Shear

**AISC 360-22 Specification for Structural Steel Buildings**
**Original PDF Pages**: 143-149 (7 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Design of Members for Shear

**Description**: Shear strength of webs and flanges

---

# CHAPTER G
# DESIGN OF MEMBERS FOR SHEAR

This chapter addresses webs of singly or doubly symmetric members subjected to shear in the plane of the web, single angles and HSS subjected to shear, and shear in the weak direction of singly or doubly symmetric shapes.

The chapter is organized as follows:

- G1. General Provisions
- G2. I-Shaped Members and Channels
- G3. Single Angles and Tees
- G4. Rectangular HSS, Box Sections, and Other Singly and Doubly Symmetric Members
- G5. Round HSS
- G6. Doubly Symmetric and Singly Symmetric Members Subjected to Minor-Axis Shear
- G7. Beams and Girders with Web Openings

**User Note:** For cases not included in this chapter, the following sections apply:
- H3.3 Unsymmetric sections
- J4.2 Shear strength of connecting elements
- J10.6 Web panel-zone shear

## G1. GENERAL PROVISIONS

The design shear strength, $\phi_v V_n$, and the allowable shear strength, $V_n/\Omega_v$, shall be determined as follows:

(a) For all provisions in this chapter except Section G2.1(a)

$$\phi_v = 0.90 \text{ (LRFD)} \qquad \Omega_v = 1.67 \text{ (ASD)}$$

(b) The nominal shear strength, $V_n$, shall be determined according to Sections G2 through G7.

## G2. I-SHAPED MEMBERS AND CHANNELS

This section addresses the determination of shear strength for I-shaped members and channels. Section G2.1 is applicable for webs with and without transverse stiffeners. Alternatively, Sections G2.2 and G2.3 are permitted to be used for webs with transverse stiffeners.

### 1. Shear Strength of Webs

The nominal shear strength, $V_n$, is

$$V_n = 0.6F_y A_w C_{v1}$$ (G2-1)

---

## I-SHAPED MEMBERS AND CHANNELS [Sect. G2.

where

$F_y$ = specified minimum yield stress of the type of steel being used, ksi (MPa)
$A_w$ = area of web, the overall depth times the web thickness, $dt_w$, in.$^2$ (mm$^2$)

(a) For webs of rolled I-shaped members with $h/t_w \leq 2.24\sqrt{E/F_y}$

$$\phi_v = 1.00 \text{ (LRFD)} \qquad \Omega_v = 1.50 \text{ (ASD)}$$

and

$$C_{v1} = 1.0$$ (G2-2)

where

$E$ = modulus of elasticity of steel
= 29,000 ksi (200 000 MPa)

$h$ = clear distance between flanges less the fillet at each flange, in. (mm)
$t_w$ = thickness of web, in. (mm)

**User Note:** All current ASTM A6/A6M W, S, and HP shapes except W44×230, W40×149, W36×135, W33×118, W30×90, W24×55, W16×26, and W12×14 meet the criteria stated in Section G2.1(a) for $F_y = 50$ ksi (345 MPa).

(b) For all other I-shaped members and channels

(1) The web shear strength coefficient, $C_{v1}$, is determined as follows:

(i) When $h/t_w \leq 1.10\sqrt{k_v E/F_y}$

$$C_{v1} = 1.0$$ (G2-3)

where

$h$ = for built-up welded sections, the clear distance between flanges, in. (mm)
= for built-up bolted sections, the distance between fastener lines, in. (mm)

(ii) When $h/t_w > 1.10\sqrt{k_v E/F_y}$

$$C_{v1} = \frac{1.10\sqrt{k_v E/F_y}}{h/t_w}$$ (G2-4)

(2) The web plate shear buckling coefficient, $k_v$, is determined as follows:

(i) For webs without transverse stiffeners

$$k_v = 5.34$$

(ii) For webs with transverse stiffeners

$$k_v = 5 + \frac{5}{(a/h)^2}$$ (G2-5)

= 5.34 when $a/h > 3.0$

where

$a$ = clear distance between transverse stiffeners, in. (mm)

---

## I-SHAPED MEMBERS AND CHANNELS [Sect. G2.]

**User Note:** $C_{v1} = 1.0$ for all ASTM A6/A6M W, S, M, and HP shapes except M12.5×12.4, M12.5×11.6, M12×11.8, M12×10.8, M12×10, M10×8, and M10×7.5, when $F_y = 50$ ksi (345 MPa).

### 2. Shear Strength of Interior Web Panels with $a/h \leq 3$ Considering Tension Field Action

The nominal shear strength, $V_n$, is determined as follows:

(a) When $h/t_w \leq 1.10\sqrt{k_v E/F_y}$

$$V_n = 0.6F_y A_w$$ (G2-6)

(b) When $h/t_w > 1.10\sqrt{k_v E/F_y}$

(1) When $2A_w/(A_{fc} + A_{ft}) \leq 2.5$, $h/b_{fc} \leq 6.0$, and $h/b_{ft} \leq 6.0$

$$V_n = 0.6F_y A_w\left[C_{v2} + \frac{1 - C_{v2}}{1.15\sqrt{1 + (a/h)^2}}\right]$$ (G2-7)

(2) Otherwise

$$V_n = 0.6F_y A_w\left[C_{v2} + \frac{1 - C_{v2}}{1.15\left[a/h + \sqrt{1 + (a/h)^2}\right]}\right]$$ (G2-8)

where

the web shear buckling coefficient, $C_{v2}$, is determined as follows:

(i) When $h/t_w \leq 1.10\sqrt{k_v E/F_y}$

$$C_{v2} = 1.0$$ (G2-9)

(ii) When $1.10\sqrt{k_v E/F_y} < h/t_w \leq 1.37\sqrt{k_v E/F_y}$

$$C_{v2} = \frac{1.10\sqrt{k_v E/F_y}}{h/t_w}$$ (G2-10)

(iii) When $h/t_w > 1.37\sqrt{k_v E/F_y}$

$$C_{v2} = \frac{1.51k_v E}{(h/t_w)^2 F_y}$$ (G2-11)

$A_{fc}$ = area of compression flange, in.$^2$ (mm$^2$)
$A_{ft}$ = area of tension flange, in.$^2$ (mm$^2$)
$b_{fc}$ = width of compression flange, in. (mm)
$b_{ft}$ = width of tension flange, in. (mm)
$k_v$ is as defined in Section G2.1(b)(2)

---

## I-SHAPED MEMBERS AND CHANNELS [Sect. G2.

The nominal shear strength is permitted to be taken as the larger of the values from Sections G2.1 and G2.2.

**User Note:** Section G2.1 may predict a higher strength for members that do not meet the requirements of Section G2.2(b)(1).

### 3. Shear Strength of End Web Panels with $a/h \leq 3$ Considering Tension Field Action

(a) The nominal shear strength for I-shaped members with equal flange areas in the end panel, $V_n$, is

$$V_n = 0.6F_{yw}A_w\left[C_{v2} + \beta_v\left(\frac{1 - C_{v2}}{1.15\sqrt{1 + (a/h)^2}}\right)\right]$$ (G2-12)

where

$$\beta_v = \frac{2.8\left(\sqrt{M_{pf} + M_{pm}} + \sqrt{M_{pst} + M_{pm}}\right)}{h\sqrt{F_{yw}t_w\left(1 - C_{v2}\right)}} \leq 1.0$$ (G2-13)

$F_{yw}$ = specified minimum yield stress of the web material, ksi (MPa)

$M_{pf}$ = plastic moment of a section composed of the flange and a segment of the web with the depth, $d_c$, kip-in. (N-mm)

$M_{pm}$ = smaller of $M_{pf}$ and $M_{pst}$, kip-in. (N-mm)

$M_{pst}$ = plastic moment of a section composed of the end stiffener plus a length of web equal to $d_c$ plus the distance from the inside face of the stiffener to the end of the beam, except that the distance from the inside face of the stiffener to the end of the beam shall not exceed $0.84t_w\sqrt{E/F_y}$ for calculation purposes, kip-in. (N-mm)

(i) When $C_{v2} \leq 0.8$

$$d_c = 35t_w\left(0.8 - C_{v2}\right)^2$$ (G2-14)

(ii) When $C_{v2} > 0.8$

$$d_c = 0$$ (G2-15)

The flexural stress in the tension flange, $\alpha M_r / S_{xt}$, in the end panel shall not be larger than $0.35F_y$,

where

$\alpha = 1.0$ (LRFD); $\alpha = 1.6$ (ASD)

(b) The nominal shear strength for I-shaped members with unequal flange areas shall be determined by analysis.

**User Note:** An approach for I-shaped members with unequal flange areas is discussed in the Commentary.

### 4. Transverse Stiffeners

For transverse stiffeners, the following shall apply.

---

## I-SHAPED MEMBERS AND CHANNELS [Sect. G2.]

(a) Transverse stiffeners are not required where $h/t_w \leq 2.54\sqrt{E/F_y}$, or where the available shear strength provided in accordance with Section G2.1 for $k_v = 5.34$ is greater than the required shear strength.

(b) Transverse stiffeners are permitted to be stopped short of the tension flange, provided bearing is not needed to transmit a concentrated load or reaction. The weld by which transverse stiffeners are attached to the web shall be terminated not less than four times nor more than six times the web thickness from the near toe of the web-to-flange weld or web-to-flange fillet. When stiffeners are used, they shall be detailed to resist twist of the compression flange.

(c) Bolts connecting stiffeners to the girder web shall be spaced not more than 12 in. (300 mm) on center. If intermittent fillet welds are used, the clear distance between welds shall not be more than 16 times the web thickness nor more than 10 in. (250 mm).

(d) $(b/t)_{st} \leq 0.56\sqrt{\frac{E}{F_{yst}}}$ (G2-16)

(e) $I_{st} \geq I_{st2} = I_{st1}(V_r - V_{c1})\rho_w$ (G2-17)

where

$F_{yst}$ = specified minimum yield stress of the stiffener material, ksi (MPa)
$I_{st}$ = moment of inertia of the transverse stiffeners about an axis in the web center for stiffener pairs, or about the face in contact with the web plate for single stiffeners, in.$^4$ (mm$^4$)

$I_{st1}$ = minimum moment of inertia of the transverse stiffeners required for development of the full shear post-buckling resistance of the stiffened web panels, $V_r = V_{c1}$, in.$^4$ (mm$^4$)

$$= \frac{h^4 t_w^3}{40}\left(\frac{F_{yw}}{E}\right)^{1.5}$$ (G2-18)

$I_{st2}$ = minimum moment of inertia of the transverse stiffeners required for development of the web shear buckling resistance, $V_r = V_{c2}$, in.$^4$ (mm$^4$)

$$= \left[\frac{2.5}{(a/h)^2} - 2\right]b_f t_f^3 \geq 0.5b_f t_f^3$$ (G2-19)

$V_{c1}$ = available shear strength calculated with $V_n$ as defined in Section G2.1 or G2.2, as applicable, kips (N)

$V_{c2}$ = available shear strength, kips (N), calculated with $V_n = 0.6F_y A_w C_{v2}$

$V_r$ = required shear strength in the panel being considered, kips (N)

$b_f$ = smaller of the dimensions $a$ and $h$, in. (mm)

$(b/t)_{st}$ = width-to-thickness ratio of the stiffener

$\rho_w$ = larger of $F_{yw}/F_{yst}$ and 1.0

$\rho_w$ = maximum shear ratio, $\left(\frac{V_r - V_{c2}}{V_{c1} - V_{c2}}\right) \geq 0$ within the web panels on each side of the transverse stiffener

---

## I-SHAPED MEMBERS AND CHANNELS [Sect. G2.

**User Note:** $I_{st1}$ may conservatively be taken as $I_{st2}$. Equation G2-18 provides the minimum stiffener moment of inertia required to attain the web shear post-buckling resistance according to Sections G2.1 and G2.2, as applicable. If less post-buckling shear strength is required, Equation G2-17 provides a linear interpolation between the minimum moment of inertia required to develop web shear buckling and that required to develop the web shear post-buckling strength.

## G3. SINGLE ANGLES AND TEES

The nominal shear strength, $V_n$, of a single-angle leg or a tee stem is

$$V_n = 0.6F_y btC_{v2}$$ (G3-1)

where

$C_{v2}$ = web shear buckling strength coefficient, as defined in Section G2.2 with $h/t_w = h/t$ and $k_v = 1.2$

$b$ = width of the leg resisting the shear force or depth of the tee stem, in. (mm)
$t$ = thickness of angle leg or tee stem, in. (mm)

## G4. RECTANGULAR HSS, BOX SECTIONS, AND OTHER SINGLY AND DOUBLY SYMMETRIC MEMBERS

The nominal shear strength, $V_n$, is

$$V_n = 0.6F_y A_w C_{v2}$$ (G4-1)

For rectangular HSS and box sections

$A_w = 2ht$, in.$^2$ (mm$^2$)

$C_{v2}$ = web shear buckling strength coefficient, as defined in Section G2.2, with $h/t_w = h/t$ and $k_v = 5$

$h$ = width resisting the shear force, taken as the clear distance between the flanges less the inside corner radius on each side for HSS or the clear distance between flanges for box sections, in. (mm). If the corner radius is not known, $h$ shall be taken as the corresponding outside dimension minus 3 times the thickness.

$t$ = design wall thickness, as defined in Section B4.2, in. (mm)

For other singly or doubly symmetric shapes

$A_w$ = area of web or webs, taken as the sum of the overall depth times the web thickness, $dt_w$, in.$^2$ (mm$^2$)

$C_{v2}$ = web shear buckling strength coefficient, as defined in Section G2.2, with $h/t_w = h/t$ and $k_v = 5$

$h$ = width resisting the shear force, in. (mm)
= for built-up welded sections, the clear distance between flanges, in. (mm)
= for built-up bolted sections, the distance between fastener lines, in. (mm)

$t$ = thickness of web, as defined in Section B4, in. (mm)

## G5. ROUND HSS

The nominal shear strength, $V_n$, of round HSS, according to the limit states of shear yielding and shear buckling, shall be determined as

---

## BEAMS AND GIRDERS WITH WEB OPENINGS [Sect. G7.]

$$V_n = F_{cr}A_g/2$$ (G5-1)

where

$F_{cr}$ shall be the larger of

$$F_{cr} = \frac{1.60E}{\sqrt{\frac{L_v}{D}\left(\frac{D}{t}\right)^{\frac{5}{4}}}}$$ (G5-2a)

and

$$F_{cr} = \frac{0.78E}{\left(\frac{D}{t}\right)^{\frac{3}{2}}}$$ (G5-2b)

but shall not exceed $0.6F_y$

$A_g$ = gross area of member, in.$^2$ (mm$^2$)
$D$ = outside diameter, in. (mm)
$L_v$ = distance from maximum to zero shear force, in. (mm)
$t$ = design wall thickness, in. (mm)

**User Note:** The shear buckling equations, Equations G5-2a and G5-2b, will control for $D/t$ over 100, high-strength steels, and long lengths. For standard sections, shear yielding will usually control and $F_{cr} = 0.6F_y$.

## G6. DOUBLY SYMMETRIC AND SINGLY SYMMETRIC MEMBERS SUBJECTED TO MINOR-AXIS SHEAR

For doubly and singly symmetric members loaded in the minor axis without torsion, the nominal shear strength, $V_n$, for each shear resisting element is

$$V_n = 0.6F_y b_f t_f C_{v2}$$ (G6-1)

where

$C_{v2}$ = web shear buckling strength coefficient, as defined in Section G2.2 with $h/t_w = b_f/2t_f$ for I-shaped members and tees, or $h/t_w = b_f/t_f$ for channels, and $k_v = 1.2$

$b_f$ = width of flange, in. (mm)
$t_f$ = thickness of flange, in. (mm)

**User Note:** $C_{v2} = 1.0$ for all ASTM A6/A6M W, S, M, and HP shapes, when $F_y \leq 70$ ksi (485 MPa).

## G7. BEAMS AND GIRDERS WITH WEB OPENINGS

The effect of all web openings on the shear strength of steel and composite beams shall be determined. Reinforcement shall be provided when the required strength exceeds the available strength of the member at the opening.

---
