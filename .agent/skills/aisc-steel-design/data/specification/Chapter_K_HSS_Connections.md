# Chapter K: HSS Connections

**AISC 360-22 Specification for Structural Steel Buildings**
**Original PDF Pages**: 225-241 (17 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Design of HSS and Box Member Connections

**Description**: Hollow structural section connections

---

# CHAPTER K
# ADDITIONAL REQUIREMENTS FOR HSS AND BOX-SECTION CONNECTIONS

This chapter addresses additional requirements for connections to HSS members and box sections of uniform wall thickness, where seam welds between box-section elements or complete-joint-penetration (CJP) groove welds in the connection region. The requirements of Chapter J also apply.

The chapter is organized as follows:

K1. General Provisions and Parameters for HSS Connections
K2. Concentrated Forces on HSS
K3. HSS-to-HSS Truss Connections
K4. HSS-to-HSS Moment Connections
K5. Welds of Plates and Branches to HSS

## K1. GENERAL PROVISIONS AND PARAMETERS FOR HSS CONNECTIONS

For the purposes of this chapter, the centerlines of branch members and chord members shall lie in a common plane. Rectangular HSS connections are further limited to having all members oriented with walls parallel to the plane.

The tables in this chapter are often accompanied by limits of applicability. Connections complying with the limits of applicability listed can be designed considering the limit states provided for each joint configuration. Connections not complying with the limits of applicability listed are not prohibited and must be designed by rational analysis.

**User Note:** The connection strengths calculated in Chapter K, including the applicable sections of Chapter J, are based on strength limit states only. See the Commentary if excessive connection deformations may cause serviceability or stability concerns.

**User Note:** Connection strength is often governed by the size of HSS members, especially the wall thickness of truss chords, and this must be considered in the initial design. To ensure economical and dependable connections can be designed, the connections should be considered in the design of the members. Angles between the chord and the branch(es) of less than 30° can make welding and inspection difficult and should be avoided. The limits of applicability provided reflect limitations on tests conducted to date, measures to eliminate undesirable limit states, and other considerations discussed in the Commentary. See Section J3.11b for through-bolt provisions.

---

This section provides parameters to be used in the design of plate-to-HSS and HSSto-HSS connections.

The design strength, $\phi R_n$, $\phi M_n$, and $\phi P_n$, and the allowable strength, $R_n/\Omega$, $M_n/\Omega$, and $P_n/\Omega$, of connections shall be determined in accordance with the provisions of this chapter and the provisions of Chapter B.

### 1. Definitions of Parameters

$A_g$ = gross cross-sectional area of member, in.$^2$ (mm$^2$)

$B$ = overall width of rectangular HSS chord member measured 90° to the plane of the connection, in. (mm)

$B_b$ = overall width of rectangular HSS branch member or plate measured 90° to the plane of the connection, in. (mm)

$B_e$ = effective width of rectangular HSS branch member or plate for local yielding of the chord face element, in. (mm)

$B_{ep}$ = effective width of rectangular HSS branch member or plate for punching shear, in. (mm)

$D$ = outside diameter of round HSS chord member, in. (mm)

$D_b$ = outside diameter of round HSS branch member, in. (mm)

$F_c$ = available stress in chord member, ksi (MPa)
    = $F_y$ for LRFD; $0.60F_y$ for ASD

$F_u$ = specified minimum tensile strength of HSS chord member material, ksi (MPa)

$F_{ub}$ = specified minimum tensile strength of HSS branch member material, ksi (MPa)

$F_y$ = specified minimum yield stress of HSS chord member material, ksi (MPa)

$F_{yb}$ = specified minimum yield stress of HSS branch member material, ksi (MPa)

$H$ = overall height of rectangular HSS chord member measured in the plane of the connection, in. (mm)

$H_b$ = overall height of rectangular HSS branch member measured in the plane of the connection, in. (mm)

$Q_f$ = chord-stress interaction parameter

$l_{end}$ = distance from the near side of the connecting branch or plate to end of chord, in. (mm)

$t$ = design wall thickness of HSS chord member, in. (mm)

$t_b$ = design wall thickness of HSS branch member or thickness of plate, in. (mm)

$\beta$ = width ratio; the ratio of branch diameter to chord diameter = $D_b/D$ for round HSS; the ratio of overall branch width to chord width = $B_b/B$ for rectangular HSS

$\beta_{eff}$ = effective width ratio; the sum of the perimeters of the two branch members in a K-connection divided by eight times the chord width

$\gamma$ = chord slenderness ratio; the ratio of one-half the diameter to the wall thickness
    = $D/2t$ for round HSS, or the ratio of one-half the width to wall thickness
    = $B/2t$ for rectangular HSS

$\eta$ = load length parameter, applicable only to rectangular HSS; the ratio of the length of contact of the branch with the chord in the plane of the connection to the chord width = $l_b/B$

$\theta$ = acute angle between branch and chord, degrees

---

where $P_{ro}$ and $M_{ro}$ are determined in the HSS chord member on the side of the joint that has lower compression stress for round HSS and higher compression stress for rectangular HSS. $P_{ro}$ and $M_{ro}$ refer to required strengths in the HSS chord: $P_{ro} = P_u$ for LRFD, and $P_u$ for ASD; $M_{ro} = M_u$ for LRFD, and $M_a$ for ASD.

Limits of applicability:
- $D/t \leq 50$ for round HSS T-, Y-, and K-connections
- $D/t \leq 40$ for round HSS cross-connections
- $B/t$ and $H/t \leq 35$ for rectangular HSS gapped K-connections and T-, Y-, and cross-connections
- $F_y \leq 52$ ksi (360 MPa)
- $F_y/F_u \leq 0.8$ (Note: ASTM A500/A500M Grade C is acceptable.)

### 4. End Distance

The available strength of the connection in Chapters J and K assume a chord member with a minimum end distance, $l_{end}$, on both sides of a connection.

(a) For rectangular sections

$$l_{end} \geq B\sqrt{1-\beta}$$ for $\beta \leq 0.85$$ (K1-7)

(b) For round sections

$$l_{end} \geq D\left(1.25 - \frac{\beta}{2}\right)$$ (K1-8)

When the connection occurs at a distance less than $l_{end}$ from an unreinforced end of the chord, the available strength of the connection shall be reduced by 50%.

## K2. CONCENTRATED FORCES ON HSS

### 1. Definitions of Parameters

$l_b$ = bearing length of the load measured parallel to the axis of the HSS member (or measured across the width of the HSS in the case of loaded cap plates), in. (mm)

### 2. Round HSS

The available strength of plate-to-round HSS connections, within the limits in Table K2.1A, shall be determined as shown in Table K2.1.

### 3. Rectangular HSS

The available strength of connections to rectangular HSS with concentrated loads shall be determined based on the applicable limit states from Chapter J.

## K3. HSS-TO-HSS TRUSS CONNECTIONS

HSS-to-HSS truss connections consist of one or more branch members directly welded to a chord that passes as a continuous element through the connection. Such connections shall be classified as follows:

---

<!-- Table: K2.1 - Available Strengths of Plate-to-Round HSS Connections -->

<table>
  <thead>
    <tr>
      <th colspan="4" style="text-align: center;"><strong>TABLE K2.1</strong><br><strong>Available Strengths of Plate-to-Round HSS<br>Connections</strong></th>
    </tr>
    <tr>
      <th>Connection Type</th>
      <th colspan="2">Connection Available Strength</th>
      <th>Plate Bending</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Transverse plate T-, Y-, and<br>cross-connections</td>
      <td colspan="3" style="text-align: center;"><strong>Limit state: HSS local yielding</strong></td>
    </tr>
    <tr>
      <td rowspan="2"><strong>Plate axial load</strong></td>
      <td><strong>In-plane</strong></td>
      <td><strong>Out-of-plane</strong></td>
    </tr>
    <tr>
      <td>$P_n \sin\theta = F_y t^2 \left[\frac{5.5}{1-0.81\left(\frac{B_b}{D}\right)}\right]$<br>(K2-1a)</td>
      <td>–</td>
      <td>$M_n = 0.5B_bP_n$<br>(K2-1b)</td>
    </tr>
    <tr>
      <td colspan="4" style="text-align: center;">$\phi = 0.90$ (LRFD) &nbsp;&nbsp;&nbsp; $\Omega = 1.67$ (ASD)</td>
    </tr>
    <tr>
      <td rowspan="2">Longitudinal plate T-, Y-, and<br>cross-connections</td>
      <td colspan="3" style="text-align: center;"><strong>Limit state: HSS plastification</strong></td>
    </tr>
    <tr>
      <td rowspan="2"><strong>Plate axial load</strong></td>
      <td><strong>In-plane</strong></td>
      <td><strong>Out-of-plane</strong></td>
    </tr>
    <tr>
      <td>$P_n \sin\theta = 5.5F_yt^2\left[1 + 0.25\left(\frac{l_b}{D}\right)\right]$<br>$Q_f$<br>(K2-2a)</td>
      <td>$M_n = 0.8l_bP_n$<br>(K2-2b)</td>
      <td>–</td>
    </tr>
    <tr>
      <td colspan="4" style="text-align: center;">$\phi = 0.90$ (LRFD) &nbsp;&nbsp;&nbsp; $\Omega = 1.67$ (ASD)</td>
    </tr>
  </tbody>
</table>

**Table summary**: Available strengths for plate-to-round HSS connections showing limit states for local yielding and plastification for transverse and longitudinal plate connections.

<!-- Table: K2.1A - Limits of Applicability -->

<table>
  <thead>
    <tr>
      <th colspan="2" style="text-align: center;"><strong>TABLE K2.1A</strong><br><strong>Limits of Applicability of Table K2.1</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>HSS wall slenderness:</td>
      <td>$D/t < 50$ for T-connections under branch plate axial load or bending<br>$D/t \leq 40$ for cross-connections under branch plate axial load or bending</td>
    </tr>
    <tr>
      <td>Width ratio:<br>Material strength:<br>Ductility:</td>
      <td>$0.2 < B_b/D \leq 1.0$ for transverse branch plate connections<br>$F_y \leq 52$ ksi (360 MPa)<br>$F_y/F_u \leq 0.8$ &nbsp;&nbsp; Note: ASTM A500/A500M Grade C is acceptable.</td>
    </tr>
  </tbody>
</table>

**Table summary**: Limits of applicability for Table K2.1 including wall slenderness, width ratio, material strength, and ductility requirements.

(a) When the punching load, $P$, sin$\theta$, in a branch member is equilibrated by beam shear in the chord member, the connection shall be classified as a T-connection when the branch is perpendicular to the chord, and classified as a Y-connection otherwise.

(b) When the punching load, $P$, sin$\theta$, in a branch member is essentially equilibrated (within 20%) by loads in other branch member(s) on the same side of the connection, the connection shall be classified as a K-connection. The relevant gap is between the primary branch members whose loads equilibrate.

**User Note:** A K-connection with one branch perpendicular to the chord is often called an N-connection.

---

(c) When the punching load, $P$, sin$\theta$, is transmitted through the chord member and is equilibrated by branch member(s) on the opposite side, the connection shall be classified as a cross-connection.

(d) When a connection has more than two primary branch members or branch members in more than one plane, the connection shall be classified as a general or multiplanar connection.

**User Note:** Limit states are not defined for general or multiplanar HSS-toHSS truss connections.

When branch members transmit part of their load as K-connections and part of their load as T-, Y-, or cross-connections, the adequacy of the connections shall be determined by interpolation on the proportion of the available strength of each in total.

For trusses that are made with HSS that are connected by welding branch members to chord members, eccentricities within the limits of applicability are permitted without consideration of the resulting moments for the design of the connection.

### 1. Definitions of Parameters

$O_v = l_{ov}/l_p \times 100$, %

$e$ = eccentricity in a truss connection, positive being away from the branches, in. (mm)

$g$ = gap between toes of branch members in a gapped K-connection, neglecting the welds, in. (mm)

$l_b = H_b/\sin\theta$, in. (mm)

$l_{ov}$ = overlap length measured along the connecting face of the chord beneath the two branches, in. (mm)

$l_p$ = projected length of the overlapping branch on the chord, in. (mm)

$\zeta$ = gap ratio; the ratio of the gap between the branches of a gapped K-connection to the width of the chord = $g/B$ for rectangular HSS

### 2. Round HSS

The available strength of round HSS-to-HSS truss connections, within the limits in Table K3.1A, shall be taken as the lowest value obtained according to the limit states shown in Table K3.1.

### 3. Rectangular HSS

The available strength, $\phi P_n$ and $P_n/\Omega$, of rectangular HSS-to-HSS truss connections within the limits in Table K3.2A, shall be taken as the lowest value obtained according to limit states shown in Table K3.2 and Chapter J.

**User Note:** Outside the limits in Table K3.2A, the limit states of Chapter J are still applicable and the applicable limit states of Chapter K are not defined.

**User Note:** Maximum gap size in Table K3.2A will be controlled by the $e/H$ limit. If the gap is large, treat as two Y-connections.

---

<!-- Table: K2.1 - Available Strengths of Plate-to-Round HSS Connections (from page 228) -->

(Diagram shows transverse and longitudinal plate T-, Y-, and cross-connections to round HSS)

**Figure description**: Two connection diagrams showing:
1. Top: Transverse plate T-, Y-, and cross-connections with axial load $P$ and $R$ applied perpendicular to round HSS chord of diameter $D$ and thickness $t$, with branch width $B_b$
2. Bottom: Longitudinal plate T-, Y-, and cross-connections with axial load $P$ and $M$ applied along the axis of round HSS chord, with bearing length $l_b$ and branch width $B_b$

---

<!-- Table: K3.1 - Available Strengths of Round HSS-to-HSS Truss Connections -->

<table>
  <thead>
    <tr>
      <th colspan="2" style="text-align: center;"><strong>TABLE K3.1</strong><br><strong>Available Strengths of Round<br>HSS-to-HSS Truss Connections</strong></th>
    </tr>
    <tr>
      <th>Connection Type</th>
      <th>Connection Available Axial Strength</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>General check for T-, Y-, cross-, and<br>K-connections with gap, when<br><br>$D_b(\text{tens/comp}) < (D - 2t)$</td>
      <td>Limit state: shear yielding (punching)<br><br>$P_n = 0.6F_y\pi D_b\left(\frac{1 + \sin\theta}{2\sin^2\theta}\right)$ &nbsp;&nbsp; (K3-1)<br><br>$\phi = 0.95$ (LRFD) &nbsp;&nbsp;&nbsp; $\Omega = 1.58$ (ASD)</td>
    </tr>
    <tr>
      <td>T- and Y-connections<br><br>(Diagram showing branch member with $t_b$, $D_b$, angle $\theta$, axial load $P$ connected to round chord with diameter $D$ and thickness $t$)</td>
      <td>Limit state: chord plastification<br><br><br>$P_n\sin\theta = F_yt^2(3.1 + 15.6\beta^2)\gamma^{0.2}Q_f$ &nbsp;&nbsp; (K3-2)<br><br><br>$\phi = 0.90$ (LRFD) &nbsp;&nbsp;&nbsp; $\Omega = 1.67$ (ASD)</td>
    </tr>
    <tr>
      <td>Cross-connections<br><br>(Diagram showing two branch members on opposite sides with $t_b$, $D_b$, angle $\theta$, axial loads $P$ connected to round chord with diameter $D$ and thickness $t$)</td>
      <td>Limit state: chord plastification<br><br><br>$P_n\sin\theta = F_yt^2\left(\frac{5.7}{1 - 0.81\beta}\right)Q_f$ &nbsp;&nbsp; (K3-3)<br><br><br>$\phi = 0.90$ (LRFD) &nbsp;&nbsp;&nbsp; $\Omega = 1.67$ (ASD)</td>
    </tr>
    <tr>
      <td>K-connections with gap or overlap<br><br>(Diagram showing gapped K-connection with compression branch $D_{b\,comp}$, $P_{comp}$, $\theta_{comp}$, tension branch $D_{b\,tens}$, $P_{tens}$, $\theta_{tens}$, gap $g$, connected to round chord with diameter $D$ and thickness $t$)</td>
      <td>Limit state: chord plastification<br><br>$(P_n\sin\theta)_{\text{compression branch}}$<br><br>$= F_yt^2\left[2.0 + 11.33\left(\frac{D_{b\,comp}}{D}\right)\right]Q_gQ_f$ (K3-4)<br><br>$(P_n\sin\theta)_{\text{tension branch}}$<br>$= (P_n\sin\theta)_{\text{compression branch}}$ &nbsp;&nbsp; (K3-5)<br><br>$\phi = 0.90$ (LRFD) &nbsp;&nbsp;&nbsp; $\Omega = 1.67$ (ASD)</td>
    </tr>
    <tr>
      <td colspan="2" style="text-align: center;"><strong>Functions</strong></td>
    </tr>
    <tr>
      <td colspan="2">$Q_g = \gamma^{0.2}\left[1 + \frac{0.024\gamma^{1.2}}{\exp\left(\frac{0.5g}{t} - 1.33\right) + 1}\right]$ &nbsp;&nbsp;&nbsp;&nbsp; (K3-6)<br><br>Note that exp$(x)$ is equal to $e^x$, where $e = 2.71828$ is the base of the natural logarithm.</td>
    </tr>
  </tbody>
</table>

**Table summary**: Available strengths for round HSS-to-HSS truss connections showing limit states for shear yielding and chord plastification for T-, Y-, cross-, and K-connections.

---

<!-- Table: K3.1A - Limits of Applicability of Table K3.1 -->

<table>
  <thead>
    <tr>
      <th colspan="2" style="text-align: center;"><strong>TABLE K3.1A</strong><br><strong>Limits of Applicability of Table K3.1</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Connection eccentricity:</td>
      <td>$-0.55 \leq e/D \leq 0.25$ for K-connections</td>
    </tr>
    <tr>
      <td>Chord wall slenderness:</td>
      <td>$D/t \leq 50$ for T-, Y-, and K-connections<br>$D/t \leq 40$ for cross-connections</td>
    </tr>
    <tr>
      <td>Branch wall slenderness:</td>
      <td>$D_b/t_b \leq 50$ for tension and compression branch<br>$D_b/t_b \leq 0.05E/F_{yb}$ for compression branch</td>
    </tr>
    <tr>
      <td>Width ratio:</td>
      <td>$0.2 \leq D_b/D \leq 1.0$ for T-, Y-, cross-, and overlapped K-connections<br>$0.4 \leq D_b/D \leq 1.0$ for gapped K-connections</td>
    </tr>
    <tr>
      <td>Gap:</td>
      <td>$g \geq t_{b\,comp} + t_{b\,tens}$ for gapped K-connections</td>
    </tr>
    <tr>
      <td>Overlap:</td>
      <td>$25\% < O_v \leq 100\%$ for overlapped K-connections</td>
    </tr>
    <tr>
      <td>Branch thickness:</td>
      <td>$t_{b\,overlapping} \leq t_{b\,overlapped}$ for branches in overlapped K-connections</td>
    </tr>
    <tr>
      <td>Material strength:</td>
      <td>$F_y$ and $F_{yb} \leq 52$ ksi (360 MPa)</td>
    </tr>
    <tr>
      <td>Ductility strength:</td>
      <td>$F_y/F_u$ and $F_{yb}/F_{ub} \leq 0.8$ Note: ASTM A500/A500M Grade C is acceptable.</td>
    </tr>
  </tbody>
</table>

**Table summary**: Limits of applicability for round HSS-to-HSS truss connections including eccentricity, wall slenderness, width ratio, gap, overlap, and material requirements.

**User Note:** The available axial strength for rectangular HSS-to-HSS member connections, $\phi P_n$ or $P_n/\Omega$, is obtained from Chapter J and the AISC *Steel Construction Manual* Part 9.

## K4. HSS-TO-HSS MOMENT CONNECTIONS

HSS-to-HSS moment connections are defined as connections that consist of one or two branch members that are directly welded to a continuous chord that passes through the connection, with the branch or branches loaded by bending moments.

A connection shall be classified as

(a) A T-connection when there is one branch and it is perpendicular to the chord and as a Y-connection when there is one branch, but not perpendicular to the chord

(b) A cross-connection when there is a branch on each (opposite) side of the chord

### 1. Definitions of Parameters

$Z_b$ = plastic section modulus of branch about the axis of bending, in.$^3$ (mm$^3$)

### 2. Round HSS

The available strength of round HSS-to-HSS moment connections within the limits of Table K4.1A shall be taken as the lowest value of the applicable limit states shown in Table K4.1.

---

<!-- Table: K3.2 - Available Strengths of Rectangular HSS-to-HSS Truss Connections -->

<table>
  <thead>
    <tr>
      <th colspan="2" style="text-align: center;"><strong>TABLE K3.2</strong><br><strong>Available Strengths of Rectangular<br>HSS-to-HSS Truss Connections</strong></th>
    </tr>
    <tr>
      <th>Connection Type</th>
      <th>Connection Available Axial Strength</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gapped K-Connections<br><br>(Diagram showing gapped K-connection with branches $H_b$, $B_b$, thickness $t_b$, angles $\theta$, gap $g$, eccentricity $e$, connected to rectangular chord with dimensions $H$, $B$, thickness $t$)</td>
      <td>Limit state: chord wall plastification, for all β<br>$P_n\sin\theta = F_yt^2(9.8\eta + 0.5)Q_f$ &nbsp;&nbsp; (K3-7)<br>$\phi = 0.90$ (LRFD) &nbsp;&nbsp;&nbsp; $\Omega = 1.67$ (ASD)<br>Limit state: shear yielding (punching), when $B_b < B - 2t$<br>This limit state need not be checked for square branches.<br>$P_n\sin\theta = 0.6F_yuB[2\eta + \beta + \beta_{oop}]$ &nbsp;&nbsp; (K3-8)<br>$\phi = 0.95$ (LRFD) &nbsp;&nbsp;&nbsp; $\Omega = 1.58$ (ASD)<br>Limit state: shear of chord side walls in the gap region<br>Determine $P_n\sin\theta$ in accordance with Section G4.<br>This limit state need not be checked for square chords.<br>Limit state: local yielding of branch/branches due to<br>uneven load distribution<br>This limit state need not be checked for square<br>branches or where $B/t \leq 15$.<br>$P_n = F_{yb}t_b(2H_b + B_b - 4t_b)$ &nbsp;&nbsp; (K3-9)<br>$\phi = 0.95$ (LRFD) &nbsp;&nbsp;&nbsp; $\Omega = 1.58$ (ASD)</td>
    </tr>
    <tr>
      <td>Overlapped K-Connections<br><br>(Diagram showing overlapped K-connection with branches $H_b$, $B_b$, thickness $t_b$, angles $\theta$, overlap region, connected to rectangular chord with dimensions $H$, $B$, thickness $t$)</td>
      <td>Limit state: local yielding of branch/branches due to<br>uneven load distribution<br>$\phi = 0.95$ (LRFD) &nbsp;&nbsp;&nbsp; $\Omega = 1.58$ (ASD)<br>When 25% ≤ $O_v$ < 50%<br>$P_{ni} = F_{yb}t_{bi}\left(\frac{O_v}{100}\right)\left(\frac{2H_{bi}}{\sin\theta_i} + \frac{O_v}{100}\left(\frac{H_{bj}}{\sin(\theta_i + \theta_j)}\right)\right)$<br>$+ B_{evi} + B_{ov}$ &nbsp;&nbsp; (K3-10)<br>When 50% ≤ $O_v$ < 80%<br>$P_{ni} = F_{yb}t_{bi}(2H_{bi} - 4t_{bi} + B_{evi} + B_{ov})$ &nbsp;&nbsp; (K3-11)<br>When 80% ≤ $O_v$ ≤ 100%<br>$P_{ni} = F_{yb}t_{bi}(2H_{bi} - 4t_{bi} + B_{bi} + B_{ov})$ &nbsp;&nbsp; (K3-12)<br><br>$B_{evi} = \frac{10}{B/t}\left(\frac{F_yt}{F_{yb}t_{bi}}\right)B_{bi} \leq B_{bi}$ &nbsp;&nbsp; (K3-13)<br><br>$B_{ov} = \frac{10}{B_{bj}/t_{bj}}\left(\frac{F_{yb}t_{bj}}{F_{yb}t_{bi}}\right)B_{bi} \leq B_{bi}$ &nbsp;&nbsp; (K3-14)<br><br>Subscript $i$ refers to the overlapping branch.<br>Subscript $j$ refers to the overlapped branch.<br><br>$P_{nj} = P_{ni}\left(\frac{F_{ybi}A_{bi}}{F_{ybi}A_{bj}}\right)$ &nbsp;&nbsp; (K3-15)</td>
    </tr>
    <tr>
      <td colspan="2" style="text-align: center;"><strong>Functions</strong></td>
    </tr>
    <tr>
      <td colspan="2">$\beta_{eff} = \left[(B_b + H_b)_{\text{compression branch}} + (B_b + H_b)_{\text{tension branch}}\right]/4B$ &nbsp;&nbsp;&nbsp;&nbsp; (K3-16)<br><br>$\beta_{oop} = \frac{B_{bp}}{B}$ &nbsp;&nbsp;&nbsp;&nbsp; (K3-17)</td>
    </tr>
  </tbody>
</table>

**Table summary**: Available strengths for rectangular HSS-to-HSS truss connections showing limit states for chord wall plastification, shear yielding, and local yielding for gapped and overlapped K-connections.

---

<!-- Table: K3.2A - Limits of Applicability of Table K3.2 -->

<table>
  <thead>
    <tr>
      <th colspan="2" style="text-align: center;"><strong>TABLE K3.2A</strong><br><strong>Limits of Applicability of Table K3.2</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Connection eccentricity:</td>
      <td>$-0.55 \leq e/H \leq 0.25$ for K-connections</td>
    </tr>
    <tr>
      <td>Chord wall slenderness:</td>
      <td>$B/t$ and $H/t \leq 35$ for gapped K-connections and T-, Y-,<br>and cross-connections<br><br>$B/t \leq 30$ for overlapped K-connections<br><br>$H/t \leq 35$ for overlapped K-connections</td>
    </tr>
    <tr>
      <td>Branch wall slenderness:</td>
      <td>$B_b/t_b$ and $H_b/t_b \leq 35$ for tension branch<br><br>$\leq 1.25\sqrt{\frac{E}{F_{yb}}}$ for compression branch of gapped<br>K-, T-, Y-, and cross-connections<br><br>$\leq 35$ for compression branch of gapped K-,<br>T-, Y-, and cross-connections<br><br>$\leq 1.1\sqrt{\frac{E}{F_{yb}}}$ for compression branch of<br>overlapped K-connections</td>
    </tr>
    <tr>
      <td>Width ratio:</td>
      <td>$B_b/B$ and $H_b/B \geq 0.25$ for T-, Y-, cross-, and overlapped<br>K-connections</td>
    </tr>
    <tr>
      <td>Aspect ratio:</td>
      <td>$0.5 \leq H_b/B_b \leq 2.0$ and $0.5 \leq H/B \leq 2.0$</td>
    </tr>
    <tr>
      <td>Overlap:</td>
      <td>$25\% \leq O_v \leq 100\%$ for overlapped K-connections</td>
    </tr>
    <tr>
      <td>Branch width ratio:</td>
      <td>$B_{bi}/B_{bj} \geq 0.75$ for overlapped K-connections, where<br>subscript $i$ refers to the overlapping branch<br>and subscript $j$ refers to the overlapped<br>branch</td>
    </tr>
    <tr>
      <td>Branch thickness ratio:</td>
      <td>$t_{bi}/t_{bj} \leq 1.0$ for overlapped K-connections, where<br>subscript $i$ refers to the overlapping branch<br>and subscript $j$ refers to the overlapped<br>branch</td>
    </tr>
    <tr>
      <td>Material strength:</td>
      <td>$F_y$ and $F_{yb} \leq 52$ ksi (360 MPa)</td>
    </tr>
    <tr>
      <td>Ductility:</td>
      <td>$F_y/F_u$ and $F_{yb}/F_{ub} \leq 0.8$ Note: ASTM A500/A500M Grade C is<br>acceptable.</td>
    </tr>
    <tr>
      <td colspan="2" style="text-align: center;"><strong>Additional Limits for Gapped K-Connections</strong></td>
    </tr>
    <tr>
      <td>Width ratio:</td>
      <td>$B_b/B$ and $H_b/B \geq 0.1 + \frac{\gamma}{50}$<br><br>$\beta_{eff} \geq 0.35$</td>
    </tr>
    <tr>
      <td>Gap ratio:</td>
      <td>$\zeta = g/B \geq 0.5(1 - \beta_{eff})$</td>
    </tr>
    <tr>
      <td>Gap:</td>
      <td>$g \geq t_{b\,compression\,branch} + t_{b\,tension\,branch}$</td>
    </tr>
    <tr>
      <td>Branch size:</td>
      <td>smaller $B_b \geq 0.63$(larger $B_b$), if both branches are square</td>
    </tr>
  </tbody>
</table>

**Table summary**: Limits of applicability for rectangular HSS-to-HSS truss connections including connection eccentricity, chord/branch slenderness, width ratios, overlap, and additional limits for gapped K-connections.

---

<!-- Table: K4.1 - Available Strengths of Round HSS-to-HSS Moment Connections -->

<table>
  <thead>
    <tr>
      <th colspan="2" style="text-align: center;"><strong>TABLE K4.1</strong><br><strong>Available Strengths of Round HSS-to-HSS<br>Moment Connections</strong></th>
    </tr>
    <tr>
      <th>Connection Type</th>
      <th>Connection Available Flexural Strength</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Branch(es) under in-plane bending<br>T-, Y-, and cross-connections<br><br>(Diagram showing branch member with $t_b$, $D_b$, moment $M$, angle $\theta$ connected to round chord with diameter $D$ and thickness $t$)</td>
      <td>Limit state: chord plastification<br><br>$M_{n-ip} = 5.39F_yt^2\gamma^{0.5}\beta\left(\frac{D_b}{\sin\theta}\right)Q_f$ &nbsp;&nbsp; (K4-1)<br><br>$\phi = 0.90$ (LRFD) &nbsp;&nbsp;&nbsp; $\Omega = 1.67$ (ASD)<br><br>Limit state: shear yielding (punching),<br>when $D_b < (D - 2t)$<br><br>$M_{n-ip} = 0.6F_ytD_b^2\left(\frac{1 + 3\sin\theta}{4\sin^2\theta}\right)$ &nbsp;&nbsp; (K4-2)<br><br>$\phi = 0.95$ (LRFD) &nbsp;&nbsp;&nbsp; $\Omega = 1.58$ (ASD)</td>
    </tr>
    <tr>
      <td>Branch(es) under out-of-plane bending<br>T-, Y-, and cross-connections<br><br>(Diagram showing branch member with moment $M$, $D_b$, $t_b$ connected perpendicular to round chord with diameter $D$ and thickness $t$)</td>
      <td>Limit state: chord plastification<br><br>$M_{n-op} = \frac{F_yt^2D_b}{\sin\theta}\left(\frac{3.0}{1 - 0.81\beta}\right)Q_f$ &nbsp;&nbsp; (K4-3)<br><br>$\phi = 0.90$ (LRFD) &nbsp;&nbsp;&nbsp; $\Omega = 1.67$ (ASD)<br><br>Limit state: shear yielding (punching),<br>when $D_b < (D - 2t)$<br><br>$M_{n-op} = 0.6F_ytD_b^2\left(\frac{3 + \sin\theta}{4\sin^2\theta}\right)$ &nbsp;&nbsp; (K4-4)<br><br>$\phi = 0.95$ (LRFD) &nbsp;&nbsp;&nbsp; $\Omega = 1.58$ (ASD)</td>
    </tr>
    <tr>
      <td colspan="2">For T-, Y-, and cross-connections, with branch(es) under combined axial load, in-plane bending, and out-of-plane bending, or any combination of these load effects<br><br>$\frac{P_r}{P_c} + \left(\frac{M_{r-ip}}{M_{c-ip}}\right)^2 + \frac{M_{r-op}}{M_{c-op}} \leq 1.0$ &nbsp;&nbsp;&nbsp;&nbsp; (K4-5)<br><br>$P_r$ = required axial strength in branch using LRFD or ASD load combinations, kips (N)<br>$M_{r-ip}$ = required in-plane flexural strength in branch using LRFD or ASD load combinations,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;kip-in. (N-mm)<br>$M_{r-op}$ = required out-of-plane flexural strength in branch using LRFD or ASD load<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;combinations, kip-in. (N-mm)<br>$P_c$ = available axial strength obtained from Table K3.1, kips (N)<br>$M_{c-ip}$ = available strength for in-plane bending, kip-in. (N-mm)<br>$M_{c-op}$ = available strength for out-of-plane bending, kip-in. (N-mm)</td>
    </tr>
  </tbody>
</table>

**Table summary**: Available strengths for round HSS-to-HSS moment connections showing limit states for in-plane and out-of-plane bending, including interaction equation for combined loads.

---

<!-- Table: K4.1A - Limits of Applicability of Table K4.1 -->

<table>
  <thead>
    <tr>
      <th colspan="2" style="text-align: center;"><strong>TABLE K4.1A</strong><br><strong>Limits of Applicability of Table K4.1</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Chord wall slenderness:</td>
      <td>$D/t \leq 50$ for T- and Y-connections<br>$D/t \leq 40$ for cross-connections</td>
    </tr>
    <tr>
      <td>Branch wall slenderness:</td>
      <td>$D_b/t_b \leq 50$<br><br>$0.05E/F_{yb} \leq D_b/t_b$</td>
    </tr>
    <tr>
      <td>Width ratio:</td>
      <td>$0.2 < D_b/D \leq 1.0$</td>
    </tr>
    <tr>
      <td>Material strength:</td>
      <td>$F_y$ and $F_{yb} \leq 52$ ksi (360 MPa)</td>
    </tr>
    <tr>
      <td>Ductility:</td>
      <td>$F_y/F_u$ and $F_{yb}/F_{ub} \leq 0.8$ Note: ASTM A500/A500M Grade C is<br>acceptable.</td>
    </tr>
  </tbody>
</table>

**Table summary**: Limits of applicability for round HSS-to-HSS moment connections.

### 3. Rectangular HSS

The available strength, $\phi P_n$ and $P_n/\Omega$, of rectangular HSS-to-HSS moment connections within the limits in Table K4.2A shall be taken as the lowest value obtained according to limit states shown in Table K4.2 and Chapter J.

**User Note:** Outside the limits in Table K4.2A, the limit states of Chapter J are still applicable and the applicable limit states of Chapter K are not defined.

## K5. WELDS OF PLATES AND BRANCHES TO HSS

The available strength of branch connections shall be determined considering the nonuniformity of load transfer along the line of weld, due to differences in relative stiffness of HSS walls in HSS-to-HSS connections and between elements in transverse plate-to-HSS connections, as follows:

$$R_n \text{ or } P_n = F_{nw}t_wl_e$$ (K5-1)

$$M_{n-ip} = F_{nw}S_{ip}$$ (K5-2)

$$M_{n-op} = F_{nw}S_{op}$$ (K5-3)

Interaction shall be considered.

(a) For fillet welds

$$\phi = 0.75 \text{ (LRFD)} \qquad \Omega = 2.00 \text{ (ASD)}$$

(b) For partial-joint-penetration groove welds

$$\phi = 0.80 \text{ (LRFD)} \qquad \Omega = 1.88 \text{ (ASD)}$$

---

<!-- Table: K4.2 - Available Strengths of Rectangular HSS-to-HSS Moment Connections -->

<table>
  <thead>
    <tr>
      <th colspan="2" style="text-align: center;"><strong>TABLE K4.2</strong><br><strong>Available Strengths of Rectangular HSS-to-HSS<br>Moment Connections</strong></th>
    </tr>
    <tr>
      <th>Connection Type</th>
      <th>Connection Available Flexural Strength</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Branch(es) under out-of-plane bending<br>T- and cross-connections<br><br>(Diagram showing branch with $B_b$, $t_b$, $H_b$, moment $M$ connected to rectangular chord with dimensions $H$, $B$, thickness $t$)</td>
      <td>Limit state: chord sidewall local yielding<br><br>$M_{n-op} = F_y^3t(B - t)(H_b + 5t)$ &nbsp;&nbsp; (K4-6)<br><br>$\phi = 1.00$ (LRFD) &nbsp;&nbsp;&nbsp; $\Omega = 1.50$ (ASD)<br><br>Limit state: chord distortional failure, for<br>T-connections and unbalanced cross-connections<br><br>$M_{n-op} = 2F_yt[H_{eff} + \sqrt{BH(B + H)}]$ &nbsp;&nbsp; (K4-7)<br><br>$\phi = 0.95$ (LRFD) &nbsp;&nbsp;&nbsp; $\Omega = 1.58$ (ASD)</td>
    </tr>
    <tr>
      <td>Branch(es) under in-plane bending<br>T- and cross-connections<br><br>(Diagram showing branch with moment $M$, $t_b$, $B_b$, $H_b$, angle $\theta$ connected to rectangular chord with dimensions $H$, $B$, thickness $t$)<br><br>Note: Not present for T-connection (indicated with circular arrow)</td>
      <td>Limit state: sidewall local yielding<br><br>When β > 0.85<br><br>$M_{n-ip} = 0.5F_y^3t(H_b + 5t)^2$ &nbsp;&nbsp; (K4-8)<br><br>$\phi = 1.00$ (LRFD) &nbsp;&nbsp;&nbsp; $\Omega = 1.50$ (ASD)</td>
    </tr>
    <tr>
      <td colspan="2">For T- and cross-connections, with branch(es) under combined axial load, in-plane bending,<br>and out-of-plane bending, or any combination of these load effects<br><br>$\frac{P_r}{P_c} + \frac{M_{r-ip}}{M_{c-ip}} + \frac{M_{r-op}}{M_{c-op}} \leq 1.0$ &nbsp;&nbsp;&nbsp;&nbsp; (K4-9)<br><br>$P_r$ = required axial strength in branch using LRFD or ASD load combinations, kips (N)<br>$M_{r-ip}$ = required in-plane flexural strength in branch using LRFD or ASD load combinations,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;kip-in. (N-mm)<br>$M_{r-op}$ = required out-of-plane flexural strength in branch using LRFD or ASD load combina-<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tions, kip-in. (N-mm)<br>$P_c$ = available axial strength, kips (N)<br>$M_{c-ip}$ = available strength for in-plane bending, kip-in. (N-mm)<br>$M_{c-op}$ = available strength for out-of-plane bending, kip-in. (N-mm)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= $\phi M_{n-op}$ (LRFD); = $M_{n-op}/\Omega$ (ASD)</td>
    </tr>
    <tr>
      <td colspan="2" style="text-align: center;"><strong>Functions</strong></td>
    </tr>
    <tr>
      <td colspan="2">$F_y^3 = F_y$ for T-connections and $0.8F_y$ for cross-connections<br>$P_{ro} = P_u$ for LRFD, and $P_a$ for ASD; $M_{ro} = M_u$ for LRFD, and $M_a$ for ASD</td>
    </tr>
  </tbody>
</table>

**Table summary**: Available strengths for rectangular HSS-to-HSS moment connections showing limit states for out-of-plane and in-plane bending, including interaction equation for combined loads.

---

<!-- Table: K4.2A - Limits of Applicability of Table K4.2 -->

<table>
  <thead>
    <tr>
      <th colspan="2" style="text-align: center;"><strong>TABLE K4.2A</strong><br><strong>Limits of Applicability of Table K4.2</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Branch angle:</td>
      <td>$\theta = 90°$</td>
    </tr>
    <tr>
      <td>Chord wall slenderness:</td>
      <td>$B/t$ and $H/t \leq 35$</td>
    </tr>
    <tr>
      <td>Branch wall slenderness:</td>
      <td>$B_b/t_b$ and $H_b/t_b \leq 35$<br><br>$\leq 1.25\sqrt{\frac{E}{F_{yb}}}$</td>
    </tr>
    <tr>
      <td>Width ratio:</td>
      <td>$B_b/B \geq 0.25$</td>
    </tr>
    <tr>
      <td>Aspect ratio:</td>
      <td>$0.5 \leq H_b/B_b \leq 2.0$ and $0.5 \leq H/B \leq 2.0$</td>
    </tr>
    <tr>
      <td>Material strength:</td>
      <td>$F_y$ and $F_{yb} \leq 52$ ksi (360 MPa)</td>
    </tr>
    <tr>
      <td>Ductility:</td>
      <td>$F_y/F_u$ and $F_{yb}/F_{ub} \leq 0.8$ Note: ASTM A500/A500M Grade<br>C is acceptable.</td>
    </tr>
  </tbody>
</table>

**Table summary**: Limits of applicability for rectangular HSS-to-HSS moment connections.

where

$F_{nw}$ = nominal stress of weld metal in accordance with Chapter J, ksi (MPa)

$S_{ip}$ = effective elastic section modulus of welds for in-plane bending (Table K5.1), in.$^3$ (mm$^3$)

$S_{op}$ = effective elastic section modulus of welds for out-of-plane bending (Table K5.1), in.$^3$ (mm$^3$)

$l_e$ = total effective weld length of groove and fillet welds to HSS for weld strength calculations, in. (mm)

$t_w$ = smallest effective weld throat thickness around the perimeter of branch or plate, in. (mm)

**User Note:** Where flexure results in tension in any load case in the weld the directional strength increase factor cannot exceed 1.0 in fillet welds to the end of rectangular HSS.

When a rectangular overlapped K-connection has been designed in accordance with Table K3.2, and the branch member component forces normal to the chord are 80% balanced (in other words, the branch member forces normal to the chord face differ by no more than 20%), the hidden weld under an overlapping branch may be omitted if the remaining welds to the overlapped branch everywhere develop the full capacity of the overlapped branch member walls.

The weld checks in Tables K5.1 and K5.2 are not required if the welds are capable of developing the full strength of the branch member wall along its entire perimeter (or a plate along its entire length).

**User Note:** The approach used here to allow downsizing of welds assumes a constant weld size around the full perimeter of the HSS branch. Special attention is required for equal width (or near-equal width) connections to rectangular HSS, which combine partial-joint-penetration groove welds along the matched edges of the connection, with fillet welds generally across the chord member face.

---

<!-- Table: K5.1 - Effective Weld Properties for Connections to Rectangular HSS -->

<table>
  <thead>
    <tr>
      <th colspan="2" style="text-align: center;"><strong>TABLE K5.1</strong><br><strong>Effective Weld Properties for Connections to<br>Rectangular HSS</strong></th>
    </tr>
    <tr>
      <th>Connection Type</th>
      <th>Weld Properties</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Transverse plate T- and cross-<br>connections under plate axial load<br><br>(Diagram showing plate with axial load $R$, width $B_b$, bearing length $t_p$ connected to rectangular chord with dimensions $H$, $B$, thickness $t$)</td>
      <td>Effective weld properties<br><br><br>$l_e = 2B_e$ &nbsp;&nbsp;&nbsp;&nbsp; (K5-4)<br><br><br>where $l_e$ = total effective weld length for welds on<br>both sides of the transverse plate, in. (mm)</td>
    </tr>
    <tr>
      <td>T-, Y-, and cross-connections<br>under branch axial load or bending<br><br>(Diagram showing branch with $t_b$, $H_b$, moment or axial load $M$ or $P$, $B_b$, angles A1, θ1A connected to rectangular chord with dimensions $H$, $B$, thickness $t$)<br><br>Note: $M$ or $P$ circular arrow indicates not present for T- or Y- connection<br><br>(Additional diagram showing section A-A with $H_b/\sin\theta$ and $B_e/2$)</td>
      <td>Effective weld properties<br><br><br>$l_e = \frac{2H_b}{\sin\theta} + 2B_e$ &nbsp;&nbsp;&nbsp;&nbsp; (K5-5)<br><br><br>$S_{ip} = \frac{t_w}{3}\left(\frac{H_b}{\sin\theta}\right)^2 + t_wB_e\left(\frac{H_b}{\sin\theta}\right)$ &nbsp;&nbsp;&nbsp;&nbsp; (K5-6)<br><br><br>$S_{op} = t_w\left(\frac{H_b}{\sin\theta}\right)B_b + \frac{t_w}{3}(B_b^2) - \frac{(t_w/3)(B_b - B_e)^3}{B_b}$ &nbsp;&nbsp; (K5-7)<br><br><br>When β > 0.85 or θ > 50°, $B_e/2$ shall not exceed<br>$B_b/4$.</td>
    </tr>
    <tr>
      <td>Gapped K-connections under branch<br>axial load<br><br>(Diagram showing gapped K-connection with branches $H_b$, $B_b$, thickness $t_b$, $H_b$, angles $\theta$, gap $g$, eccentricity $+e$, connected to rectangular chord with dimensions $H$, $B$, thickness $t$)<br><br>(Additional diagram showing section A-A with 4th side effective when θ ≤ 50°, and note about effective weld for θ ≥ 60°)</td>
      <td>Effective weld properties<br><br><br>When $\theta \leq 50°$<br><br>$l_e = \frac{2(H_b - 1.2t_b)}{\sin\theta} + 2(B_b - 1.2t_b)$ &nbsp;&nbsp; (K5-8)<br><br><br>When $\theta \geq 60°$<br><br>$l_e = \frac{2(H_b - 1.2t_b)}{\sin\theta} + B_b - 1.2t_b$ &nbsp;&nbsp; (K5-9)<br><br><br>When 50° < $\theta$ < 60°, linear interpolation shall be<br>used to determine $l_e$.</td>
    </tr>
  </tbody>
</table>

**Table summary**: Effective weld properties (lengths and section moduli) for connections to rectangular HSS for transverse plates, T-/Y-/cross-connections, and gapped K-connections.

---

<!-- Table: K5.1 (continued) - Effective Weld Properties for Connections to Rectangular HSS -->

<table>
  <thead>
    <tr>
      <th colspan="2" style="text-align: center;"><strong>TABLE K5.1 (continued)</strong><br><strong>Effective Weld Properties for Connections to<br>Rectangular HSS</strong></th>
    </tr>
    <tr>
      <th>Connection Type</th>
      <th>Weld Properties</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Overlapped K-connections<br>under branch axial load<br><br>(Diagrams showing overlapped K-connection with branches $H_b$, $B_b$, thickness $t_b$, $H_b$, angles $\theta$ (compression and tension), connected to rectangular chord with dimensions $H$, $B$, thickness $t$)<br><br>Note that the force arrows shown<br>for overlapped K-connections may<br>be reversed; $i$ and $j$ control member<br>identification.<br><br>(Additional diagram showing section A-A with effective weld when $H_b/\sin\theta$ and $B_e/2$ dimensions)<br><br>(Another diagram showing section A-A with $H_b - 1.2t_b/\sin\theta$ dimensions when $B_b/B > 0.85$ or $\theta_j > 50°$)</td>
      <td>Overlapping member effective weld properties<br>(all dimensions are for the overlapping branch, $i$)<br><br>When 25% ≤ $O_v$ < 50%<br><br>$l_{ei} = \frac{2O_v}{50}\left[\left(1 - \frac{O_v}{100}\right)\left(\frac{H_{bi}}{\sin\theta_i}\right) + \frac{O_v}{100}\left(\frac{H_{bj}}{\sin(\theta_i + \theta_j)}\right)\right]$<br>$+ B_{evi} + B_{ov}$ &nbsp;&nbsp; (K5-10)<br><br>When 50% ≤ $O_v$ < 80%<br><br>$l_{ei} = 2\left[\left(1 - \frac{O_v}{100}\right)\left(\frac{H_{bi}}{\sin\theta_i}\right) + \frac{O_v}{100}\left(\frac{H_{bj}}{\sin(\theta_i + \theta_j)}\right)\right]$<br>$+ B_{evi} + B_{ov}$ &nbsp;&nbsp; (K5-11)<br><br>When 80% ≤ $O_v$ < 100%<br><br>$l_{ei} = 2\left[\left(1 - \frac{O_v}{100}\right)\left(\frac{H_{bi}}{\sin\theta_i}\right) + \frac{O_v}{100}\left(\frac{H_{bj}}{\sin(\theta_i + \theta_j)}\right)\right]$<br>$+ B_{bi} + B_{ov}$ &nbsp;&nbsp; (K5-12)<br><br>$B_{evi} = \frac{10}{B/t}\left(\frac{F_yt}{F_{ybi}t_{bi}}\right)B_{bi} \leq B_{bi}$ &nbsp;&nbsp; (K5-13)<br><br>$B_{ov} = \frac{10}{B_{bj}/t_{bj}}\left(\frac{F_{ybj}t_{bj}}{F_{ybi}t_{bi}}\right)B_{bi} \leq B_{bi}$ &nbsp;&nbsp; (K5-14)<br><br>When $B_{bi}/B > 0.85$ or $\theta_j > 50°$<br><br>$l_{ei} = 2(H_{bi} - 1.2t_{bi})/\sin\theta_i$ &nbsp;&nbsp; (K5-15)<br><br>Subscript $i$ refers to the overlapping branch.<br>Subscript $j$ refers to the overlapped branch.<br><br>Overlapped member effective weld properties<br>(all dimensions are for the overlapped branch, $j$)<br><br>$l_{ej} = \frac{2H_{bj}}{\sin\theta_j} + 2B_{ej}$ &nbsp;&nbsp;&nbsp;&nbsp; (K5-13)<br><br>$B_{ej} = \frac{10}{B/t}\left(\frac{F_yt}{F_{ybj}t_{bj}}\right)B_{bj} \leq B_{bj}$ &nbsp;&nbsp; (K5-14)<br><br>When $B_{bi}/B > 0.85$ or $\theta_j > 50°$<br><br>$l_{ej} = 2(H_{bj} - 1.2t_{bj})/\sin\theta_j$ &nbsp;&nbsp; (K5-15)</td>
    </tr>
  </tbody>
</table>

**Table summary**: Effective weld properties for overlapped K-connections to rectangular HSS, showing formulas for overlapping and overlapped branch members.

---

<!-- Table: K5.2 - Effective Weld Properties for Connections to Round HSS -->

<table>
  <thead>
    <tr>
      <th colspan="2" style="text-align: center;"><strong>TABLE K5.2</strong><br><strong>Effective Weld Properties for Connections to<br>Round HSS</strong></th>
    </tr>
    <tr>
      <th>Connection Type</th>
      <th>Weld Properties</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>T-, Y-, and cross-connections under<br>branch axial load<br><br>(Diagram showing branch member with $t_b$, $D_b$, axial load $P$, angle $\theta$ connected to round chord with diameter $D$ and thickness $t$, with points A marked on both sides)<br><br>Note: Circular arrow with $P$ indicates not present for T- or Y-connections<br><br>Additional diagram showing section A-A with $l_e/2$ dimensions and effective weld indication</td>
      <td>Effective weld properties<br><br>When $0.1 \leq \beta \leq 0.5$, $60° \leq \theta \leq 90°$, and<br>$10 \leq D/t \leq 50$<br><br>$l_e = \frac{4}{\sqrt{2\beta(D/t)}}t_w \leq l_w$ &nbsp;&nbsp;&nbsp;&nbsp; (K5-16)<br><br><br>where $l_w$ is the total weld length around<br>the branch. This may be obtained from 3D<br>models of intersection cylinders, or from<br><br>$l_w = \pi D_b\frac{1 + 1/\sin\theta}{2}$ &nbsp;&nbsp;&nbsp;&nbsp; (K5-17)</td>
    </tr>
  </tbody>
</table>

**Table summary**: Effective weld properties for T-, Y-, and cross-connections to round HSS.

---
