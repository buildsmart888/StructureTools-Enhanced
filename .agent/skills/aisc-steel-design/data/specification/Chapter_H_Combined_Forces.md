# Chapter H: Combined Forces

**AISC 360-22 Specification for Structural Steel Buildings**
**Original PDF Pages**: 150-156 (7 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Design of Members for Combined Forces and Torsion

**Description**: Interaction equations and torsional strength

---

# CHAPTER H
# DESIGN OF MEMBERS FOR COMBINED FORCES AND TORSION

This chapter addresses members subjected to axial force and flexure about one or both axes, with or without torsion, and members subjected to torsion only.

The chapter is organized as follows:

- H1. Doubly and Singly Symmetric Members Subjected to Flexure and Axial Force
- H2. Unsymmetric and Other Members Subjected to Flexure and Axial Force
- H3. Members Subjected to Torsion and Combined Torsion, Flexure, Shear, and/or Axial Force
- H4. Rupture of Flanges with Bolt Holes and Subjected to Tension

**User Note:** For composite members, see Chapter I.

## H1. DOUBLY AND SINGLY SYMMETRIC MEMBERS SUBJECTED TO FLEXURE AND AXIAL FORCE

### 1. Doubly and Singly Symmetric Members Subjected to Flexure and Compression

The interaction of flexure and compression in doubly symmetric members and singly symmetric members constrained to bend about a geometric axis (x and/or y) shall be limited by Equations H1-1a and H1-1b.

**User Note:** Section H2 may be used in lieu of the provisions of this section.

(a) When $\frac{P_r}{P_c} \geq 0.2$

$$\frac{P_r}{P_c} + \frac{8}{9}\left(\frac{M_{rx}}{M_{cx}} + \frac{M_{ry}}{M_{cy}}\right) \leq 1.0$$ (H1-1a)

(b) When $\frac{P_r}{P_c} < 0.2$

$$\frac{P_r}{2P_c} + \left(\frac{M_{rx}}{M_{cx}} + \frac{M_{ry}}{M_{cy}}\right) \leq 1.0$$ (H1-1b)

where

$P_r$ = required compressive strength, determined in accordance with Chapter C, using LRFD or ASD load combinations, kips (N)

$P_c$ = available compressive strength, $\phi_c P_n$ or $P_n/\Omega_c$, determined in accordance with Chapter E, kips (N)

---

$M_r$ = required flexural strength, determined in accordance with Chapter C, using LRFD or ASD load combinations, kip-in. (N-mm)

$M_n$ = available flexural strength, $\phi_b M_n$ or $M_n/\Omega_b$, determined in accordance with Chapter F, kip-in. (N-mm)

$x$ = subscript relating symbol to major-axis bending

$y$ = subscript relating symbol to minor-axis bending

**User Note:** All terms in Equations H1-1a and H1-1b are to be taken as positive.

## 2. Doubly and Singly Symmetric Members Subjected to Flexure and Tension

The interaction of flexure and tension in doubly symmetric members and singly symmetric members constrained to bend about a geometric axis ($x$ and/or $y$) shall be limited by Equations H1-1a and H1-1b,

where

$P_r$ = required tensile strength, determined in accordance with Chapter C, using LRFD or ASD load combinations, kips (N)

$P_c$ = available tensile strength, $\phi_t P_n$ or $P_n/\Omega_t$, determined in accordance with Chapter D, kips (N)

For doubly symmetric members, $C_b$ in Chapter F is permitted to be multiplied by

$$\sqrt{1 + \frac{\alpha P_r}{P_{ey}}}$$

when axial tension acts concurrently with flexure,

where

$$P_{ey} = \frac{\pi^2 EI_y}{L_b^2}$$ (H1-2)

$\alpha$ = 1.0 (LRFD); $\alpha$ = 1.6 (ASD)

$E$ = modulus of elasticity of steel
    = 29,000 ksi (200 000 MPa)

$I_y$ = moment of inertia about the $y$-axis, in.$^4$ (mm$^4$)

$L_b$ = length between points that are either braced against lateral displacement of the compression flange or braced against twist of the cross section, in. (mm$^4$)

## 3. Doubly Symmetric Rolled Compact Members Subjected to Single-Axis Flexure and Compression

For doubly symmetric rolled compact members, with the effective length for torsional buckling less than or equal to the effective length for $y$-axis flexural buckling, $L_{ez} \leq L_{ey}$, subjected to flexure and compression with moments primarily about their major axis, it is permissible to address the two interaction limit states, in-plane instability and out-of-plane buckling or lateral-torsional buckling, separately in lieu of the combined approach provided in Section H1.1,

where

$L_{ey}$ = effective length for buckling about the $y$-axis, in. (mm)

$L_{ez}$ = effective length for buckling about the longitudinal axis, in. (mm)

---

For members with $M_{rx}/M_{ry} \geq 0.05$, the provisions of Section H1.1 shall be followed.

(a) For the limit state of in-plane instability, Equations H1-1a and H1-1b shall be used with $P_c$ taken as the available compressive strength in the plane of bending and $M_{cx}$ taken as the available flexural strength based on the limit state of yielding.

(b) For the limit state of out-of-plane buckling and lateral-torsional buckling

$$\frac{P_r}{P_{cy}}\left(1.5 - 0.5\frac{P_r}{P_{ey}}\right) + \left(\frac{M_{rx}}{C_b M_{cx}}\right)^2 \leq 1.0$$ (H1-3)

where

$C_b$ = lateral-torsional buckling modification factor determined from Section F1

$M_{cx}$ = available lateral-torsional strength for major-axis flexure determined in accordance with Chapter F using $C_b = 1.0$, kip-in. (N-mm)

$P_{cy}$ = available compressive strength out of the plane of bending, kips (N)

**User Note:** In Equation H1-3, $C_b M_{cx}$ may be larger than $\phi_b M_{px}$ (LRFD) or $M_{px}/\Omega_b$ (ASD). All variables in Equation H1-3 are to be taken as positive. The yielding resistance of the beam-column is captured by Equations H1-1a and H1-1b.

## H2. UNSYMMETRIC AND OTHER MEMBERS SUBJECTED TO FLEXURE AND AXIAL FORCE

This section addresses the interaction of flexure and axial stress for shapes not covered in Section H1. It is permitted to use the provisions of this section for any shape in lieu of the provisions of Section H1.

$$\left|\frac{f_{ra}}{F_{ca}} + \frac{f_{rbw}}{F_{cbw}} + \frac{f_{rbz}}{F_{cbz}}\right| \leq 1.0$$ (H2-1)

where

$f_{ra}$ = required axial stress at the point of consideration, determined in accordance with Chapter C, using LRFD or ASD load combinations, ksi (MPa)

$F_{ca}$ = available axial stress at the point of consideration, determined in accordance with Chapter E for compression or Section D2 for tension, ksi (MPa)

$f_{rbw}, f_{rbz}$ = required flexural stress at the point of consideration, determined in accordance with Chapter C, using LRFD or ASD load combinations, ksi (MPa)

$F_{cbw}, F_{cbz}$ = available flexural stress at the point of consideration, determined in accordance with Chapter F, ksi (MPa). Use the section modulus, $S$, for the specific location in the cross section and consider the sign of the stress.

$w$ = subscript relating symbol to major principal axis bending

$z$ = subscript relating symbol to minor principal axis bending

---

**User Note:** The subscripts $w$ and $z$ refer to the principal axes of the unsymmetric cross section. For doubly symmetric cross sections, these can be replaced by the $x$ and $y$ subscripts.

Equation H2-1 shall be evaluated using the principal bending axes by considering the sense of the flexural stresses at the critical points of the cross section. The flexural terms are either added to or subtracted from the axial term as applicable. When the axial force is compression, second-order effects shall be included according to the provisions of Chapter C.

A more detailed analysis of the interaction of flexure and tension is permitted in lieu of Equation H2-1.

## H3. MEMBERS SUBJECTED TO TORSION AND COMBINED TORSION, FLEXURE, SHEAR, AND/OR AXIAL FORCE

### 1. Round and Rectangular HSS Subjected to Torsion

The design torsional strength, $\phi_T T_n$, and the allowable torsional strength, $T_n/\Omega_T$, for round and rectangular HSS according to the limit states of torsional yielding and torsional buckling shall be determined as follows:

$$T_n = F_{cr}C$$ (H3-1)

$$\phi_T = 0.90 \text{ (LRFD)} \qquad \Omega_T = 1.67 \text{ (ASD)}$$

where

$C$ = HSS torsional constant, in.$^3$ (mm$^3$)

The critical stress, $F_{cr}$, shall be determined as follows:

(a) For round HSS, $F_{cr}$ shall be the larger of

(1) $$\frac{1.23E}{\sqrt{\frac{L}{D}\left(\frac{D}{t}\right)^{5/4}}}$$ (H3-2a)

and

(2) $$F_{cr} = \frac{0.60E}{\left(\frac{D}{t}\right)^{3/2}}$$ (H3-2b)

but shall not exceed $0.6F_y$,

where

$D$ = outside diameter, in. (mm)

$L$ = length of member, in. (mm)

$t$ = design wall thickness defined in Section B4.2, in. (mm)

(b) For rectangular HSS

(1) When $h/t \leq 2.45\sqrt{E/F_y}$

---

$$F_{cr} = 0.6F_y$$ (H3-3)

(2) When $2.45\sqrt{E/F_y} < h/t \leq 3.07\sqrt{E/F_y}$

$$F_{cr} = \frac{0.6F_y\left(2.45\sqrt{E/F_y}\right)}{\left(\frac{h}{t}\right)}$$ (H3-4)

(3) When $3.07\sqrt{E/F_y} < h/t \leq 260$

$$F_{cr} = \frac{0.458\pi^2 E}{\left(\frac{h}{t}\right)^2}$$ (H3-5)

where

$h$ = flat width of longer side, as defined in Section B4.1b(d), in. (mm)

**User Note:** The torsional constant, $C$, may be conservatively taken as:

For round HSS: $C = \frac{\pi(D-t)^2t}{2}$

For rectangular HSS: $C = 2(B-t)(H-t)t - 4.5(4-\pi)t^3$

## 2. HSS Subjected to Combined Torsion, Shear, Flexure, and Axial Force

When the required torsional strength, $T_r$, is less than or equal to 20% of the available torsional strength, $T_c$, the interaction of torsion, shear, flexure, and axial force for HSS may be determined by Section H1 and the torsional effects may be neglected. When $T_r$ exceeds 20% of $T_c$, the interaction of torsion, shear, flexure, and/or axial force shall be limited, at the point of consideration, by

$$\left(\frac{P_r}{P_c} + \frac{M_{rx}}{M_{cx}} + \frac{M_{ry}}{M_{cy}}\right) + \left(\frac{V_r}{V_c} + \frac{T_r}{T_c}\right)^2 \leq 1.0$$ (H3-6)

where

$V_r/V_c$ shall be taken as the larger value for the $x$- or $y$-axis

and

$P_r$ = required axial strength, determined in accordance with Chapter C, using LRFD or ASD load combinations, kips (N)

$P_c$ = available tensile or compressive strength, $\phi P_n$ or $P_n/\Omega$, determined in accordance with Chapter D or E, kips (N)

$M_{rx}, M_{ry}$ = required flexural strength, determined in accordance with Chapter C, using LRFD or ASD load combinations, kip-in. (N-mm)

$M_{cx}, M_{cy}$ = available flexural strength, $\phi_b M_n$ or $M_n/\Omega_b$, determined in accordance with Chapter F, kip-in. (N-mm)

$V_r$ = required shear strength, determined in accordance with Chapter C, using LRFD or ASD load combinations, kips (N)

---

$V_c$ = available shear strength, $\phi_v V_n$ or $V_n/\Omega_v$, determined in accordance with Chapter G, kips (N)

$T_r$ = required torsional strength, determined in accordance with Chapter C, using LRFD or ASD load combinations, kip-in. (N-mm)

$T_c$ = available torsional strength, $\phi_T T_n$ or $T_n/\Omega_T$, determined in accordance with Section H3.1, kip-in. (N-mm)

$x$ = subscript relating symbol to major-axis bending

$y$ = subscript relating symbol to minor-axis bending

**User Note:** All terms in Equations H3-6 are to be taken as positive.

## 3. Non-HSS Members Subjected to Torsion and Combined Stress

The available torsional strength for non-HSS members shall be the lowest value obtained according to the limit states of yielding under normal stress, shear yielding under shear stress, or buckling, determined as follows:

$$\phi_T = 0.90 \text{ (LRFD)} \qquad \Omega_T = 1.67 \text{ (ASD)}$$

(a) For the limit state of yielding under normal stress

$$F_n = F_y$$ (H3-7)

(b) For the limit state of shear yielding under shear stress

$$F_n = 0.6F_y$$ (H3-8)

(c) For the limit state of buckling

$$F_n = F_{cr}$$ (H3-9)

where

$F_{cr}$ = buckling stress for the section as determined by analysis, ksi (MPa)

## H4. RUPTURE OF FLANGES WITH BOLT HOLES AND SUBJECTED TO TENSION

At locations of bolt holes in flanges subjected to tension under combined axial force and major-axis flexure, flange tensile rupture strength shall be limited by Equation H4-1. Each flange subjected to tension due to axial force and flexure shall be checked separately.

$$\frac{P_r}{P_c} + \frac{M_{rx}}{M_{cx}} \leq 1.0$$ (H4-1)

where

$P_r$ = required axial strength of the member at the location of the bolt holes, determined in accordance with Chapter C, using LRFD or ASD load combinations, positive in tension and negative in compression, kips (N)

$P_c$ = available axial strength for the limit state of tensile rupture of the net section at the location of bolt holes, $\phi_t P_n$ or $P_n/\Omega_t$, determined in accordance with Section D2(b), kips (N)

---

$M_{rx}$ = required flexural strength at the location of the bolt holes, determined in accordance with Chapter C, using LRFD or ASD load combinations, positive for tension and negative for compression in the flange under consideration , kip-in. (N-mm)

$M_{cx}$ = available flexural strength about the $x$-axis for the limit state of tensile rupture of the flange, $\phi_b M_n$ or $M_n/\Omega_b$, determined according to Section F13.1. When the limit state of tensile rupture in flexure does not apply, use the plastic moment, $M_p$, determined with bolt holes not taken into consideration, kip-in. (N-mm)

---
