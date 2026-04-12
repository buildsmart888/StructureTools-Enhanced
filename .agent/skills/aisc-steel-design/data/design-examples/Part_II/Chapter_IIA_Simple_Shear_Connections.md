# Chapter IIA: Simple Shear Connections

**AISC Specification v16.0 - Design Examples**
**Original PDF Pages**: 541-848 (308 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Simple Shear Connections

**Examples Included**: ['II.A-1~II.A-30: 30 shear connection examples']

---

## Table of Contents

- [EXAMPLE II.A-19B EXTENDED SINGLE-PLATE CONNECTION SUBJECT TO AXIAL AND SHEAR LOADING](#example-iia-19b-extended-single-plate-connection-subject-to-axial-and-shear-loading)
- [EXAMPLE II.A-20 ALL-BOLTED SINGLE-PLATE SHEAR SPLICE](#example-iia-20-all-bolted-single-plate-shear-splice)
- [EXAMPLE II.A-21 BOLTED/WELDED SINGLE-PLATE SHEAR SPLICE](#example-iia-21-bolted/welded-single-plate-shear-splice)
- [EXAMPLE II.A-22 BOLTED BRACKET PLATE DESIGN](#example-iia-22-bolted-bracket-plate-design)
- [EXAMPLE II.A-23 WELDED BRACKET PLATE DESIGN](#example-iia-23-welded-bracket-plate-design)
- [EXAMPLE II.A-24 ECCENTRICALLY LOADED BOLT GROUP (IC METHOD)](#example-iia-24-eccentrically-loaded-bolt-group-(ic-method))
- [EXAMPLE II.A-25 ECCENTRICALLY LOADED BOLT GROUP (ELASTIC METHOD)](#example-iia-25-eccentrically-loaded-bolt-group-(elastic-method))
- [EXAMPLE II.A-26 ECCENTRICALLY LOADED WELD GROUP (IC METHOD)](#example-iia-26-eccentrically-loaded-weld-group-(ic-method))
- [EXAMPLE II.A-27 ECCENTRICALLY LOADED WELD GROUP (ELASTIC METHOD)](#example-iia-27-eccentrically-loaded-weld-group-(elastic-method))
- [EXAMPLE II.A-28A ALL-BOLTED SINGLE-ANGLE CONNECTION (BEAM-TO-GIRDER WEB)](#example-iia-28a-all-bolted-single-angle-connection-(beam-to-girder-web))
- [EXAMPLE II.A-28B ALL-BOLTED SINGLE ANGLE CONNECTION—STRUCTURAL INTEGRITY CHECK](#example-iia-28b-all-bolted-single-angle-connection—structural-integrity-check)
- [EXAMPLE II.A-29 BOLTED/WELDED SINGLE-ANGLE CONNECTION (BEAM-TO-COLUMN FLANGE)](#example-iia-29-bolted/welded-single-angle-connection-(beam-to-column-flange))
- [EXAMPLE II.A-30 ALL-BOLTED TEE CONNECTION (BEAM-TO-COLUMN FLANGE)](#example-iia-30-all-bolted-tee-connection-(beam-to-column-flange))
- [EXAMPLE II.A-31 BOLTED/WELDED TEE CONNECTION (BEAM-TO-COLUMN FLANGE)](#example-iia-31-bolted/welded-tee-connection-(beam-to-column-flange))

---

# IIA-1

# Chapter IIA Simple Shear Connections

The design of connecting elements is covered in Part 9 of the AISC *Manual*. The design of simple shear connections is covered in Part 10 of the AISC *Manual*. The design of simple connections for combined forces is covered in Part 12 of the AISC *Manual*.

---

# IIA-2

# EXAMPLE II.A-1A ALL-BOLTED DOUBLE-ANGLE CONNECTION

## Given:

Verify the available strength of an all-bolted double-angle shear connection between an ASTM A992/A992M W36×231 beam and an ASTM A992/A992M W14×90 column flange, as shown in Figure II.A-1A-1, supporting the following beam end reactions:

$R_D = 37.5$ kips
$R_L = 113$ kips

Use ASTM A572/A572M Grade 50 angles.

This example is repeated using the following two procedures:

Part A: Determine the available connection strength using the tables in *Manual* Part 10.
Part B: Determine the available connection strength by checking individual limit states.

<div style="text-align: center;">
<img src="connection_geometry" alt="Connection diagram showing:
- Left view: W36×231 beam with 2L5×3½×⅜ × 1'-11½" (SLBB) angles
- Vertical dimensions: 1⅞", 13¾" spacing, 1⅞", total 7 @ 3" = 1'-9"
- Right view (Section A-A): Column flange connection detail showing ¾" dia. Group 120 bolts in standard holes
- Dimensions showing 3⅝", 3⅜", 1⅞", 1⅜" spacing
- Note about web thickness and bolt spacing">
</div>

\* This dimension (see sketch, Section A-A) is determined as one-half of the decimal web thickness rounded to the next higher ⅛ in. Example: 0.760"/2 = 0.380"; use ⅞ in. This will produce spacing of holes in the supporting beam slightly larger than detailed in the angles to permit spreading of angles (angles can be spread but not closed) at time of erection to supporting member. Alternatively, consider using horizontal short slots in the support legs of the angles.
\*\*See AISC *Manual* Tables 7-15 and 7-16 for driving clearance.

*Fig. II.A-1A-1. Connection geometry for Example II.A-1A.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam and column
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

---

# IIA-3

Angles
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W36×231
$t_w = 0.760$ in.

Column
W14×90
$t_f = 0.710$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(37.5 \text{ kips}) + 1.6(113 \text{ kips})$ | $R_a = 37.5 \text{ kips} + 113 \text{ kips}$ |
| $= 226$ kips | $= 151$ kips |

*Part A—Determine the Available Connection Strength Using the Tables in Manual Part 10*

*Available Angle Strength*

AISC *Manual* Table 10-1a includes checks for the limit states of shear yielding, shear rupture, and block shear rupture of the angles.

Use 8 rows of ¾-in.-diameter bolts in standard holes and 2L5×3½×⅜ (SLBB). From AISC *Manual* Table 10-1a:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 302 \text{ kips} > 226 \text{ kips}$ **o.k.** | $\frac{R_n}{\Omega} = 201 \text{ kips} > 151 \text{ kips}$ **o.k.** |

*Available Shear Transfer Strength at Bolt Holes at Beam Web*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength determined in accordance with AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the angles at the bolt hole determined in accordance with AISC *Specification* Section J3.11a, and (3) the available bearing or tearout strength of the beam web or support element at the bolt hole determined in accordance with AISC *Specification* Section J3.11a.

From AISC *Manual* Table 10-1b, the available bolt shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9$ kips | $\frac{r_n}{\Omega} = 11.9$ kips |

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the angle per bolt for ¾-in.-diameter bolts in standard holes is:

---

# IIA-4

| LRFD | ASD |
|------|-----|
| For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): | For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): |
| $\phi r_n = (49.4 \text{ kip/in.})(\frac{5}{16} \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kip/in.})(\frac{5}{16} \text{ in.})$ |
| $= 15.4$ kips | $= 10.3$ kips |
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kip/in.})(\frac{5}{16} \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(\frac{5}{16} \text{ in.})$ |
| $= 27.4$ kips | $= 18.3$ kips |

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the beam web per bolt for ¾-in.- diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kip/in.})(0.760 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(0.760 \text{ in.})$ |
| $= 66.7$ kips | $= 44.5$ kips |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by two because the bolts are in double shear), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by two because there are two angles), and available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min\begin{Bmatrix} [17.9 \text{ kips}(2) = 35.8 \text{ kips},] \\ [27.4 \text{ kips}(2) = 54.8 \text{ kips},] \\ [66.7 \text{ kips}] \end{Bmatrix}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{Bmatrix} [11.9 \text{ kips}(2) = 23.8 \text{ kips},] \\ [18.3 \text{ kips}(2) = 36.6 \text{ kips},] \\ [44.5 \text{ kips}] \end{Bmatrix}$ |
| $= 35.8$ kips | $= 23.8$ kips |

At the middle connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by two because the bolts are in double shear), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by two because there are two angles), and available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,mid} = \min\begin{Bmatrix} [17.9 \text{ kips}(2) = 35.8 \text{ kips},] \\ [27.4 \text{ kips}(2) = 54.8 \text{ kips},] \\ [66.7 \text{ kips}] \end{Bmatrix}$ | $\frac{r_{n,mid}}{\Omega} = \min\begin{Bmatrix} [11.9 \text{ kips}(2) = 23.8 \text{ kips},] \\ [18.3 \text{ kips}(2) = 36.6 \text{ kips},] \\ [44.5 \text{ kips}] \end{Bmatrix}$ |
| $= 35.8$ kips | $= 23.8$ kips |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by two because the bolts are in double shear), the available bearing and tearout strength of the angles for an edge bolt (multiplied by two because there are two angles), and available bearing and tearout strength of the beam web for a non-edge bolt:

---

# IIA-5

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min\begin{Bmatrix} [17.9 \text{ kips}(2) = 35.8 \text{ kips},] \\ [15.4 \text{ kips}(2) = 30.8 \text{ kips},] \\ [66.7 \text{ kips}] \end{Bmatrix}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{Bmatrix} [11.9 \text{ kips}(2) = 23.8 \text{ kips},] \\ [10.3 \text{ kips}(2) = 20.6 \text{ kips},] \\ [44.5 \text{ kips}] \end{Bmatrix}$ |
| $= 30.8$ kips | $= 20.6$ kips |

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi r_{n,top} + \phi r_{n,mid}(n-2) + \phi r_{n,bot}$ | $\frac{R_n}{\Omega} = \frac{r_{n,top}}{\Omega} + \frac{r_{n,mid}}{\Omega}(n-2) + \frac{r_{n,bot}}{\Omega}$ |
| $= 35.8 \text{ kips} + (35.8 \text{ kips})(8-2) + 30.8 \text{ kips}$ | $= 23.8 \text{ kips} + (23.8 \text{ kips})(8-2) + 20.6 \text{ kips}$ |
| $= 281 \text{ kips} > 226 \text{ kips}$ **o.k.** | $= 187 \text{ kips} > 151 \text{ kips}$ **o.k.** |

*Available Beam Web Strength*

Because the beam is not coped, the limit states of block shear rupture and shear rupture of the beam are not applicable. The beam web is adequate for the required loads.

*Available Shear Transfer Strength at Bolt Holes at Column Flange*

The available bolt shear strength and available bearing and tearout strength of the angles is calculated in the previous section.

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the column flange per bolt for ¾-in.- diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kip/in.})(0.710 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(0.710 \text{ in.})$ |
| $= 62.3$ kips | $= 41.5$ kips |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because there are two bolts per row), the available bearing and tearout strength of the angles for an edge bolt (multiplied by 2 because there are two angles), and available bearing and tearout strength of the column flange (multiplied by 2 because there are two bolts per row):

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min\begin{Bmatrix} [17.9 \text{ kips}(2) = 35.8 \text{ kips},] \\ [15.4 \text{ kips}(2) = 30.8 \text{ kips},] \\ [62.3 \text{ kips}(2) = 125 \text{ kips}] \end{Bmatrix}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{Bmatrix} [11.9 \text{ kips}(2) = 23.8 \text{ kips},] \\ [10.3 \text{ kips}(2) = 20.6 \text{ kips},] \\ [41.5 \text{ kips}(2) = 83.0 \text{ kips}] \end{Bmatrix}$ |
| $= 30.8$ kips | $= 20.6$ kips |

At the middle connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because there are two bolts per row), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by 2 because there are two angles), and available bearing and tearout strength of the column flange (multiplied by 2 because there are two bolts per row):

---

# IIA-6

| LRFD | ASD |
|------|-----|
| $\phi r_{n,mid} = \min\begin{Bmatrix} [17.9 \text{ kips}(2) = 35.8 \text{ kips},] \\ [27.4 \text{ kips}(2) = 54.8 \text{ kips},] \\ [62.3 \text{ kips}(2) = 125 \text{ kips}] \end{Bmatrix}$ | $\frac{r_{n,mid}}{\Omega} = \min\begin{Bmatrix} [11.9 \text{ kips}(2) = 23.8 \text{ kips},] \\ [18.3 \text{ kips}(2) = 36.6 \text{ kips},] \\ [41.5 \text{ kips}(2) = 83.0 \text{ kips}] \end{Bmatrix}$ |
| $= 35.8$ kips | $= 23.8$ kips |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because there are two bolts per row), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by 2 because there are two angles), and the available bearing and tearout strength of the column flange (multiplied by 2 because there are two bolts per row):

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min\begin{Bmatrix} [17.9 \text{ kips}(2) = 35.8 \text{ kips},] \\ [27.4 \text{ kips}(2) = 54.8 \text{ kips},] \\ [62.3 \text{ kips}(2) = 125 \text{ kips}] \end{Bmatrix}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{Bmatrix} [11.9 \text{ kips}(2) = 23.8 \text{ kips},] \\ [18.3 \text{ kips}(2) = 36.6 \text{ kips},] \\ [41.5 \text{ kips}(2) = 83.0 \text{ kips}] \end{Bmatrix}$ |
| $= 35.8$ kips | $= 23.8$ kips |

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi r_{n,top} + \phi r_{n,mid}(n-2) + \phi r_{n,bot}$ | $\frac{R_n}{\Omega} = \frac{r_{n,top}}{\Omega} + \frac{r_{n,mid}}{\Omega}(n-2) + \frac{r_{n,bot}}{\Omega}$ |
| $= 30.8 \text{ kips} + (35.8 \text{ kips})(8-2) + 35.8 \text{ kips}$ | $= 20.6 \text{ kips} + (23.8 \text{ kips})(8-2) + 23.8 \text{ kips}$ |
| $= 281 \text{ kips} > 226 \text{ kips}$ **o.k.** | $= 187 \text{ kips} > 151 \text{ kips}$ **o.k.** |

*Summary*

The available shear strength of the connection is controlled by the available shear transfer strength at the bolt holes.

| LRFD | ASD |
|------|-----|
| $\phi R_n = 281 \text{ kips} > 226 \text{ kips}$ **o.k.** | $\frac{R_n}{\Omega} = 187 \text{ kips} > 151 \text{ kips}$ **o.k.** |

The connection is found to be adequate as given for the applied loads.

*Part B—Verify the Available Connection Strength by Checking Individual Limit States*

*Shear Strength of Angles*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the angles is determined as follows:

$$A_{gv} = (2 \text{ angles})lt$$
$$= (2 \text{ angles})(23\frac{1}{2} \text{ in.})(\frac{5}{16} \text{ in.})$$
$$= 14.7 \text{ in.}^2$$

---

# IIA-7

$$R_n = 0.60F_y A_{gv}$$
(*Spec.* Eq. J4-3)

$$= 0.60(50 \text{ ksi})(14.7 \text{ in.}^2)$$

$$= 441 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
| $\phi R_n = 1.00(441 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{441 \text{ kips}}{1.50}$ |
| $= 441 \text{ kips} > 226 \text{ kips}$ **o.k.** | $= 294 \text{ kips} > 151 \text{ kips}$ **o.k.** |

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the angle is determined using the net area determined in accordance with AISC *Specification* Section B4.3b.

$$A_{nv} = (2 \text{ angles})[l - n(d_h + \frac{1}{16} \text{ in.})]t$$

$$= (2 \text{ angles})[23\frac{1}{2} \text{ in.} - 8(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](\frac{5}{16} \text{ in.})$$

$$= 10.3 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$
(*Spec.* Eq. J4-4)

$$= 0.60(65 \text{ ksi})(10.3 \text{ in.}^2)$$

$$= 402 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(402 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{402 \text{ kips}}{2.00}$ |
| $= 302 \text{ kips} > 226 \text{ kips}$ **o.k.** | $= 201 \text{ kips} > 151 \text{ kips}$ **o.k.** |

*Block Shear Rupture of Angles*

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture for the angles is determined as follows. By inspection, block shear rupture of the angles will control at the beam web side of the connection because the horizontal edge distance at the beam web (1⅞ in.) is lesser than the horizontal edge distance at the column flange side of the connection (1⅞ in.).

$$R_{nv} = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$
(*Spec.* Eq. J4-5)

where

$$A_{gv} = (2 \text{ angles})(l - l_{ev})t$$
$$= (2 \text{ angles})(23\frac{1}{2} \text{ in.} - 1\frac{1}{4} \text{ in.})(\frac{5}{16} \text{ in.})$$
$$= 13.9 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (2 \text{ angles})[n - 0.5](d_h + \frac{1}{16} \text{ in.})t$$
$$= 13.9 \text{ in.}^2 - (2 \text{ angles})(8 - 0.5)(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})(\frac{5}{16} \text{ in.})$$
$$= 9.80 \text{ in.}^2$$

---

# IIA-8

$$A_{nt} = (2 \text{ angles})[l_{eh} - 0.5(d_h + \frac{1}{16} \text{ in.})]t$$

$$= (2 \text{ angles})[1⅞ \text{ in.} - 0.5(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](\frac{5}{16} \text{ in.})$$

$$= 0.586 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_{nv} = 0.60(65 \text{ ksi})(9.80 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.586 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(13.9 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.586 \text{ in.}^2)$$

$$= 420 \text{ kips} < 455 \text{ kips}$$

Therefore:

$$R_{nv} = 420 \text{ kips}$$

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture of the angles is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_{nv} = 0.75(420 \text{ kips})$ | $\frac{R_{nv}}{\Omega} = \frac{420 \text{ kips}}{2.00}$ |
| $= 315 \text{ kips} > 226 \text{ kips}$ **o.k.** | $= 210 \text{ kips} > 151 \text{ kips}$ **o.k.** |

*Available Shear Transfer Strength at Bolt Holes at Beam Web*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength determined in accordance with AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the angles at the bolt hole determined in accordance with AISC *Specification* Section J3.11a, and (3) the available bearing or tearout strength of the beam web or support element at the bolt hole determined in accordance with AISC *Specification* Section J3.11a.

From AISC *Manual* Table 7-1, the available shear strength for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9$ kips | $\frac{r_n}{\Omega} = 11.9$ kips |

The available bearing strength of the angles is determined from AISC *Specification* Section J3.11, assuming deformation at service load is a design consideration:

$$r_n = 2.4dtF_u$$
(from *Spec.* Eq. J3-6a)

$$= (2.4)(\frac{3}{4} \text{ in.})(\frac{5}{16} \text{ in.})(65 \text{ ksi})$$

$$= 36.6 \text{ kips}$$

---

# IIA-9

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(36.6 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{36.6 \text{ kips}}{2.00}$ |
| $= 27.5$ kips | $= 18.3$ kips |

The available tearout strength of the angles is determined from AISC *Specification* Section J3.11, assuming deformation at service load is a design consideration.

For edge bolt tearout, the clear distance along the line of action of the force, between the edge of the hole and the edge of the angle is:

$$l_c = l_{ev} - 0.5d_h$$
$$= 1\frac{1}{4} \text{ in.} - 0.5(1\frac{3}{16} \text{ in.})$$
$$= 0.844 \text{ in.}$$

The available tearout strength of the angles at the edge bolt is:

$$r_n = 1.2l_c tF_u$$
(from *Spec.* Eq. J3-6c)

$$= (1.2)(0.844 \text{ in.})(\frac{5}{16} \text{ in.})(65 \text{ ksi})$$

$$= 20.6 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(20.6 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{20.6 \text{ kips}}{2.00}$ |
| $= 15.5$ kips | $= 10.3$ kips |

For non-edge bolt tearout in the angles, the clear distance is between bolt holes:

$$l_c = s - d_h$$
$$= 3 \text{ in.} - 1\frac{3}{16} \text{ in.}$$
$$= 2.19 \text{ in.}$$

The available tearout strength of the angles at non-edge bolts is:

$$r_n = 1.2l_c tF_u$$
(from *Spec.* Eq. J3-6c)

$$= (1.2)(2.19 \text{ in.})(\frac{5}{16} \text{ in.})(65 \text{ ksi})$$

$$= 53.4 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(53.4 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{53.4 \text{ kips}}{2.00}$ |
| $= 40.1$ kips | $= 26.7$ kips |

---

# IIA-10

The available bearing strength of the beam web is determined from AISC *Specification* Section J3.11, assuming deformation at service load is a design consideration:

$$r_n = 2.4dtF_u$$
(from *Spec.* Eq. J3-6a)

$$= (2.4)(\frac{3}{4} \text{ in.})(0.760 \text{ in.})(65 \text{ ksi})$$

$$= 88.9 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(88.9 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{88.9 \text{ kips}}{2.00}$ |
| $= 66.7$ kips | $= 44.5$ kips |

The available tearout strength of the beam web is determined from AISC *Specification* Section J3.11, assuming deformation at service load is a design consideration.

There is no edge bolt tearout for the beam web. For non-edge bolt tearout in the beam web, the clear distance is between bolt holes:

$$l_c = s - d_h$$
$$= 3 \text{ in.} - 1\frac{3}{16} \text{ in.}$$
$$= 2.19 \text{ in.}$$

The available tearout strength of the beam web at non-edge bolts is:

$$r_n = 1.2l_c tF_u$$
(from *Spec.* Eq. J3-6c)

$$= (1.2)(2.19 \text{ in.})(0.760 \text{ in.})(65 \text{ ksi})$$

$$= 130 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(130 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{130 \text{ kips}}{2.00}$ |
| $= 97.5$ kips | $= 65.0$ kips |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because the bolts are in double shear), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by 2 because there are two angles), and the available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min\begin{Bmatrix} [17.9 \text{ kips}(2) = 35.8 \text{ kips},] \\ [27.5 \text{ kips}(2) = 55.0 \text{ kips},] \\ [40.1 \text{ kips}(2) = 80.2 \text{ kips},] \\ [66.7 \text{ kips},] \\ [97.5 \text{ kips}] \end{Bmatrix}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{Bmatrix} [11.9 \text{ kips}(2) = 23.8 \text{ kips},] \\ [18.3 \text{ kips}(2) = 36.6 \text{ kips},] \\ [26.7 \text{ kips}(2) = 53.4 \text{ kips},] \\ [44.5 \text{ kips},] \\ [65.0 \text{ kips}] \end{Bmatrix}$ |
| $= 35.8$ kips | $= 23.8$ kips |

---

# IIA-11

At the middle connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because the bolts are in double shear), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by 2 because there are two angles), and the available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,mid} = \min\begin{Bmatrix} [17.9 \text{ kips}(2) = 35.8 \text{ kips},] \\ [27.5 \text{ kips}(2) = 55.0 \text{ kips},] \\ [40.1 \text{ kips}(2) = 80.2 \text{ kips},] \\ [66.7 \text{ kips},] \\ [97.5 \text{ kips}] \end{Bmatrix}$ | $\frac{r_{n,mid}}{\Omega} = \min\begin{Bmatrix} [11.9 \text{ kips}(2) = 23.8 \text{ kips},] \\ [18.3 \text{ kips}(2) = 36.6 \text{ kips},] \\ [26.7 \text{ kips}(2) = 53.4 \text{ kips},] \\ [44.5 \text{ kips},] \\ [65.0 \text{ kips}] \end{Bmatrix}$ |
| $= 35.8$ kips | $= 23.8$ kips |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because the bolts are in double shear), the available bearing and tearout strength of the angles for an edge bolt (multiplied by 2 because there are two angles), and the available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min\begin{Bmatrix} [17.9 \text{ kips}(2) = 35.8 \text{ kips},] \\ [27.5 \text{ kips}(2) = 55.0 \text{ kips},] \\ [15.5 \text{ kips}(2) = 31.0 \text{ kips},] \\ [66.7 \text{ kips},] \\ [97.5 \text{ kips}] \end{Bmatrix}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{Bmatrix} [11.9 \text{ kips}(2) = 23.8 \text{ kips},] \\ [18.3 \text{ kips}(2) = 36.6 \text{ kips},] \\ [10.3 \text{ kips}(2) = 20.6 \text{ kips},] \\ [44.5 \text{ kips},] \\ [65.0 \text{ kips}] \end{Bmatrix}$ |
| $= 31.0$ kips | $= 20.6$ kips |

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi r_{n,top} + \phi r_{n,mid}(n-2) + \phi r_{n,bot}$ | $\frac{R_n}{\Omega} = \frac{r_{n,top}}{\Omega} + \frac{r_{n,mid}}{\Omega}(n-2) + \frac{r_{n,bot}}{\Omega}$ |
| $= 35.8 \text{ kips} + (35.8 \text{ kips})(8-2) + 31.0 \text{ kips}$ | $= 23.8 \text{ kips} + (23.8 \text{ kips})(8-2) + 20.6 \text{ kips}$ |
| $= 282 \text{ kips} > 226 \text{ kips}$ **o.k.** | $= 187 \text{ kips} > 151 \text{ kips}$ **o.k.** |

*Available Shear Transfer Strength at Bolt Holes at Column Flange*

The available bolt shear strength and available bearing and tearout strength of the angles is calculated in the previous section.

The available bearing strength of the column flange is determined from AISC *Specification* Section J3.11, assuming deformation at service load is a design consideration:

$$r_n = 2.4dtF_u$$
(from *Spec.* Eq. J3-6a)

$$= (2.4)(\frac{3}{4} \text{ in.})(0.710 \text{ in.})(65 \text{ ksi})$$

$$= 83.1 \text{ kips}$$

---

# IIA-12

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(83.1 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{83.1 \text{ kips}}{2.00}$ |
| $= 62.3$ kips | $= 41.6$ kips |

The available tearout strength of the column flange is determined from AISC *Specification* Section J3.11, assuming deformation at service load is a design consideration.

There is no edge bolt tearout for the column flange. For non-edge bolt tearout in the column flange, the clear distance between bolt holes is:

$$l_c = s - d_h$$
$$= 3 \text{ in.} - 1\frac{3}{16} \text{ in.}$$
$$= 2.19 \text{ in.}$$

The available tearout strength of the beam web at non-edge bolts is:

$$r_n = 1.2l_c tF_u$$
(from *Spec.* Eq. J3-6c)

$$= (1.2)(2.19 \text{ in.})(0.710 \text{ in.})(65 \text{ ksi})$$

$$= 121 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(121 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{121 \text{ kips}}{2.00}$ |
| $= 90.8$ kips | $= 60.5$ kips |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because there are two bolts per row), the available bearing and tearout strength of the angles for an edge bolt (multiplied by 2 because there are two angles), and the available bearing and tearout strength of the column flange (multiplied by 2 because there are two bolts per row):

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min\begin{Bmatrix} [17.9 \text{ kips}(2) = 35.8 \text{ kips},] \\ [27.5 \text{ kips}(2) = 55.0 \text{ kips},] \\ [15.5 \text{ kips}(2) = 31.0 \text{ kips},] \\ [62.3 \text{ kips}] \\ [90.8 \text{ kips}] \end{Bmatrix}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{Bmatrix} [11.9 \text{ kips}(2) = 23.8 \text{ kips},] \\ [18.3 \text{ kips}(2) = 36.6 \text{ kips},] \\ [10.3 \text{ kips}(2) = 20.6 \text{ kips},] \\ [41.6 \text{ kips},] \\ [60.5 \text{ kips}] \end{Bmatrix}$ |
| $= 31.0$ kips | $= 20.6$ kips |

At the middle connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because there are two bolts per row), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by 2 because there are two angles), and the available bearing and tearout strength of the column flange (multiplied by 2 because there are two bolts per row):

---

# IIA-13

| LRFD | ASD |
|------|-----|
| $\phi r_{n,mid} = \min\begin{Bmatrix} [17.9 \text{ kips}(2) = 35.8 \text{ kips},] \\ [27.5 \text{ kips}(2) = 55.0 \text{ kips},] \\ [40.1 \text{ kips}(2) = 80.2 \text{ kips},] \\ [62.3 \text{ kips},] \\ [90.8 \text{ kips}] \end{Bmatrix}$ | $\frac{r_{n,mid}}{\Omega} = \min\begin{Bmatrix} [11.9 \text{ kips}(2) = 23.8 \text{ kips},] \\ [18.3 \text{ kips}(2) = 36.6 \text{ kips},] \\ [26.7 \text{ kips}(2) = 53.4 \text{ kips},] \\ [41.6 \text{ kips},] \\ [60.5 \text{ kips}] \end{Bmatrix}$ |
| $= 35.8$ kips | $= 23.8$ kips |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because the bolts are in double shear), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by 2 because there are two angles), and available bearing strength of the column flange (multiplied by 2 because there are two bolts per row):

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min\begin{Bmatrix} [17.9 \text{ kips}(2) = 35.8 \text{ kips},] \\ [27.5 \text{ kips}(2) = 55.0 \text{ kips},] \\ [40.1 \text{ kips}(2) = 80.2 \text{ kips},] \\ [62.3 \text{ kips}] \end{Bmatrix}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{Bmatrix} [11.9 \text{ kips}(2) = 23.8 \text{ kips},] \\ [18.3 \text{ kips}(2) = 36.6 \text{ kips},] \\ [26.7 \text{ kips}(2) = 53.4 \text{ kips},] \\ [41.6 \text{ kips}] \end{Bmatrix}$ |
| $= 35.8$ kips | $= 23.8$ kips |

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi r_{n,top} + \phi r_{n,mid}(n-2) + \phi r_{n,bot}$ | $\frac{R_n}{\Omega} = \frac{r_{n,top}}{\Omega} + \frac{r_{n,mid}}{\Omega}(n-2) + \frac{r_{n,bot}}{\Omega}$ |
| $= 31.0 \text{ kips} + (35.8 \text{ kips})(8-2) + 35.8 \text{ kips}$ | $= 20.6 \text{ kips} + (23.8 \text{ kips})(8-2) + 23.8 \text{ kips}$ |
| $= 282 \text{ kips} > 226 \text{ kips}$ **o.k.** | $= 187 \text{ kips} > 151 \text{ kips}$ **o.k.** |

*Available Beam Web Strength*

Because the beam is not coped, the limit states of block shear rupture and shear rupture of the beam are not applicable. The beam web is adequate for the required loading.

*Conclusion*

The available shear strength of the connection is controlled by the available shear transfer strength at the bolt holes.

| LRFD | ASD |
|------|-----|
| $\phi R_n = 282 \text{ kips} > 226 \text{ kips}$ **o.k.** | $\frac{R_n}{\Omega} = 187 \text{ kips} > 151 \text{ kips}$ **o.k.** |

The connection is found to be adequate as given for the applied loads.

---

# IIA-14

# EXAMPLE II.A-1B ALL-BOLTED DOUBLE-ANGLE CONNECTION SUBJECT TO AXIAL AND SHEAR LOADING

## Given:

Verify the available strength of an all-bolted double-angle connection for an ASTM A992/A992M W18×50 beam, as shown in Figure II.A-1B-1, to support the following beam end reactions:

| LRFD | ASD |
|------|-----|
| Shear, $V_u = 75$ kips | Shear, $V_a = 50$ kips |
| Axial tension, $N_u = 60$ kips | Axial tension, $N_a = 40$ kips |

Use ASTM A572/A572M Grade 50 double angles that will be shop-bolted to the beam.

<div style="text-align: center;">
<img src="connection_geometry" alt="Connection diagram showing:
- Left view: W18×50 beam with 2L5×3½×⅜×1'-2½" (SLBB) angles
- Vertical dimensions: 1⅜", 2¼", 3½", 1⅜" spacing, with 4 @ 3" = 1'-2"
- Labels for Bolt 1, Bolt 2, forces V and N
- Right view (Section A-A): Column connection detail showing ¾" dia. Group 120 bolts in standard holes, 7½" gage dimension">
</div>

*Fig. II.A-1B-1. Connection geometry for Example II.A-1B.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Angles
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W18×50
$A_g = 14.7 \text{ in.}^2$
$d = 18.0$ in.

---

# IIA-15

$t_w = 0.355$ in.
$t_f = 0.570$ in.

From AISC *Specification* Table J3.3, the hole diameter for ¾-in.-diameter bolts with standard holes is:

$$d_h = 1\frac{3}{16} \text{ in.}$$

The resultant load is:

| LRFD | ASD |
|------|-----|
| $R_u = \sqrt{V_u^2 + N_u^2}$ | $R_a = \sqrt{V_a^2 + N_a^2}$ |
| $= \sqrt{(75 \text{ kips})^2 + (60 \text{ kips})^2}$ | $= \sqrt{(50 \text{ kips})^2 + (40 \text{ kips})^2}$ |
| $= 96.0$ kips | $= 64.0$ kips |

Try 5 rows of bolts and 2L5×3½×⅜ (SLBB).

*Strength of the Bolted Connection—Angles*

From the User Note in AISC *Specification* Section J3.7, the strength of the bolt group is taken as the sum of the individual strengths of the individual fasteners, which may be taken as the lesser of the fastener shear strength per AISC *Specification* Section J3.7, the bearing strength at the bolt hole per AISC *Specification* Section J3.11a, or the tearout strength at the bolt hole per AISC *Specification* Section J3.11a.

*Bolt shear*

From AISC *Manual* Table 7-1, the available shear strength for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) in double shear (or pair of bolts) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 48.7$ kips/bolt (or per pair of bolts) | $\frac{r_n}{\Omega} = 32.5$ kips/bolt (or per pair of bolts) |

*Bolt bearing on angles*

The available bearing strength of the angles per bolt in double shear is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration:

$$r_n = (2 \text{ angles})2.4dtF_u$$
(from *Spec.* Eq. J3-6a)

$$= (2 \text{ angles})(2.4)(\frac{3}{8} \text{ in.})(\frac{5}{8} \text{ in.})(65 \text{ ksi})$$

$$= 171 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(171 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{171 \text{ kips/bolt}}{2.00}$ |
| $= 128$ kips/bolt | $= 85.5$ kips/bolt |

---

# IIA-16

*Bolt tearout on angles*

From AISC *Specification* Section J3.11a, the available tearout strength of the angles per bolt in double shear is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration.

As shown in Figures II.A-1B-2(a) and II.A-1B-2(b), the tearout dimensions on the angle differ between the edge bolt and the other bolts.

The angle θ, as shown in Figure II.A-1B-2(a), of the resultant force on the edge bolt is:

| LRFD | ASD |
|------|-----|
| $\theta = \tan^{-1}\left(\frac{N_u}{V_u}\right)$ | $\theta = \tan^{-1}\left(\frac{N_a}{V_a}\right)$ |
| $= \tan^{-1}\left(\frac{60 \text{ kips}}{75 \text{ kips}}\right)$ | $= \tan^{-1}\left(\frac{40 \text{ kips}}{50 \text{ kips}}\right)$ |
| $= 38.7°$ | $= 38.7°$ |

The length from the center of the bolt hole to the edge of the angle along the line of action of the force is:

$$l_e = \frac{1\frac{1}{4} \text{ in.}}{\cos 38.7°}$$
$$= 1.60 \text{ in.}$$

The clear distance along the line of action of the force, between the edge of the hole and the edge of the angle is:

$$l_c = l_e - 0.5d_h$$
$$= 1.60 \text{ in.} - 0.5(1\frac{3}{16} \text{ in.})$$
$$= 1.13 \text{ in.}$$

<div style="text-align: center;">
<img src="tearout_diagrams" alt="Two diagrams showing:
(a) Edge bolt: Single bolt with 1⅛" dimension and angle θ marked
(b) Other bolts: Multiple bolts showing angle β and 1⅛" dimension">
</div>

*(a) Edge bolt                    (b) Other bolts*

*Fig. II.A-1B-2. Bolt tearout on angles.*

---

# IIA-17

The available tearout strength of the pair of angles at the edge bolt is:

$$r_n = (2 \text{ angles})1.2l_c tF_u$$
(from *Spec.* Eq. J3-6c)

$$= (2 \text{ angles})(1.2)(1.13 \text{ in.})(\frac{5}{8} \text{ in.})(65 \text{ ksi})$$

$$= 110 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(110 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{110 \text{ kips/bolt}}{2.00}$ |
| $= 82.5$ kips/bolt | $= 55.0$ kips/bolt |

Therefore, bolt shear controls over bearing or tearout of the angles at the edge bolt.

The angle β, as shown in Figure II.A-1B-2(b), of the resultant force on the other bolts is:

| LRFD | ASD |
|------|-----|
| $\beta = \tan^{-1}\left(\frac{V_u}{N_u}\right)$ | $\beta = \tan^{-1}\left(\frac{V_a}{N_a}\right)$ |
| $= \tan^{-1}\left(\frac{75 \text{ kips}}{60 \text{ kips}}\right)$ | $= \tan^{-1}\left(\frac{50 \text{ kips}}{40 \text{ kips}}\right)$ |
| $= 51.3°$ | $= 51.3°$ |

The length from the center of the bolt hole to the edge of the angle along the line of action of the force is:

$$l_e = \frac{1\frac{1}{4} \text{ in.}}{\cos 51.3°}$$
$$= 2.00 \text{ in.}$$

The clear distance along the line of action of the force, between the edge of the hole and the edge of the angle is:

$$l_c = l_e - 0.5d_h$$
$$= 2.00 \text{ in.} - 0.5(1\frac{3}{16} \text{ in.})$$
$$= 1.53 \text{ in.}$$

The available tearout strength of the pair of angles at the other bolts is:

$$r_n = (2 \text{ angles})1.2l_c tF_u$$
(from *Spec.* Eq. J3-6c)

$$= (2 \text{ angles})(1.2)(1.53 \text{ in.})(\frac{5}{8} \text{ in.})(65 \text{ ksi})$$

$$= 149 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(149 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{149 \text{ kips/bolt}}{2.00}$ |
| $= 112$ kips/bolt | $= 74.5$ kips/bolt |

---

# IIA-18

Therefore, bolt shear controls over bearing or tearout of the angles at the other bolt.

The effective strength for the bolted connection at the angles is determined by summing the effective strength for each bolt using the minimum available strength calculated for bolt shear, bearing on the angles, and tearout on the angles.

| LRFD | ASD |
|------|-----|
| $\phi R_n = n\phi r_n$ | $\frac{R_n}{\Omega} = n\frac{r_n}{\Omega}$ |
| $= (5 \text{ bolts})(48.7 \text{ kips/bolt})$ | $= (5 \text{ bolts})(32.5 \text{ kips/bolt})$ |
| $= 244 \text{ kips} > 96.0 \text{ kips}$ **o.k.** | $= 163 \text{ kips} > 64.0 \text{ kips}$ **o.k.** |

*Strength of the Bolted Connection—Beam Web*

*Bolt bearing on beam web*

The available bearing strength of the beam web per bolt is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration:

$$r_n = 2.4dtF_u$$
(*Spec.* Eq. J3-6a)

$$= 2.4(\frac{3}{8} \text{ in.})(0.355 \text{ in.})(65 \text{ ksi})$$

$$= 48.5 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(48.5 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{48.5 \text{ kips/bolt}}{2.00}$ |
| $= 36.4$ kips/bolt | $= 24.3$ kips/bolt |

*Bolt tearout on beam web*

From AISC *Specification* Section J3.11a, the available tearout strength of the beam web is determined from AISC *Specification* Equation J3-6c, assuming deformation at the bolt hole is a design consideration, where the edge distance, $l_c$, is based on the angle of the resultant load. As shown in Figure II.A-1B-3, a horizontal edge distance of 1⅜ in. is used, which includes a ⅛ in. tolerance to account for possible mill underrun.

<div style="text-align: center;">
<img src="beam_web_tearout" alt="Diagram showing bolt tearout on beam web with angle θ marked, force line, and dimension 1⅜" - ⅛" (underrun) = 1⅛"">
</div>

*Fig. II.A-1B-3. Bolt tearout on beam web.*

---

# IIA-19

The angle, θ, of the resultant force is:

| LRFD | ASD |
|------|-----|
| $\theta = \tan^{-1}\left(\frac{V_u}{N_u}\right)$ | $\theta = \tan^{-1}\left(\frac{V_a}{N_a}\right)$ |
| $= \tan^{-1}\left(\frac{75 \text{ kips}}{60 \text{ kips}}\right)$ | $= \tan^{-1}\left(\frac{50 \text{ kips}}{40 \text{ kips}}\right)$ |
| $= 51.3°$ | $= 51.3°$ |

The length from the center of the bolt hole to the edge of the web along the line of action of the force is:

$$l_e = \frac{1\frac{1}{4} \text{ in.}}{\cos 51.3°}$$
$$= 2.40 \text{ in.}$$

The clear distance along the line of action of the force, between the edge of the hole and the edge of the web is:

$$l_c = l_e - 0.5d_h$$
$$= 2.40 \text{ in.} - 0.5(1\frac{3}{16} \text{ in.})$$
$$= 1.93 \text{ in.}$$

The available tearout strength of the beam web is determined as follows:

$$r_n = 1.2l_c tF_u$$
(*Spec.* Eq. J3-6c)

$$= 1.2(1.93 \text{ in.})(0.355 \text{ in.})(65 \text{ ksi})$$

$$= 53.4 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(53.4 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{53.4 \text{ kips/bolt}}{2.00}$ |
| $= 40.1$ kips/bolt | $= 26.7$ kips/bolt |

Therefore, bolt bearing on the beam web is the controlling limit state for all bolts.

The effective strength for the bolted connection at the beam web is determined by summing the effective strength for each bolt using the minimum available strength calculated for bolt shear, bearing on the beam web, and tearout on the beam web.

| LRFD | ASD |
|------|-----|
| $\phi R_n = n\phi r_n$ | $\frac{R_n}{\Omega} = n\frac{r_n}{\Omega}$ |
| $= (5 \text{ bolts})(36.4 \text{ kips/bolt})$ | $= (5 \text{ bolts})(24.3 \text{ kips/bolt})$ |
| $= 182 \text{ kips} > 96.0 \text{ kips}$ **o.k.** | $= 122 \text{ kips} > 64.0 \text{ kips}$ **o.k.** |

*Bolt Shear and Tension Interaction—Outstanding Angle Legs*

---

# IIA-20

The available tensile strength of the bolts due to the effect of combined tension and shear is determined from AISC *Specification* Section J3.8.

The required shear stress is:

$$f_{rv} = \frac{V_r}{nA_b}$$

where

$$A_b = 0.601 \text{ in.}^2 \text{ (from AISC *Manual* Table 7-1)}$$
$$n = 10$$

| LRFD | ASD |
|------|-----|
| $f_{rv} = \frac{V_u}{nA_b}$ | $f_{rv} = \frac{V_a}{nA_b}$ |
| $= \frac{75 \text{ kips}}{10(0.601 \text{ in.}^2)}$ | $= \frac{50 \text{ kips}}{10(0.601 \text{ in.}^2)}$ |
| $= 12.5$ ksi | $= 8.32$ ksi |

The nominal tensile strength modified to include the effects of shear stress is determined from AISC *Specification* Section J3.8 as follows. From AISC *Specification* Table J3.2:

$$F_{nt} = 90 \text{ ksi}$$
$$F_{nv} = 54 \text{ ksi}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $F'_{nt} = 1.3F_{nt} - \frac{F_{nt}}{\phi F_{nv}}f_{rv} \leq F_{nt}$ (*Spec.* Eq. J3-3a) | $F'_{nt} = 1.3F_{nt} - \frac{\Omega F_{nt}}{F_{nv}}f_{rv} \leq F_{nt}$ (*Spec.* Eq. J3-3b) |
| $= 1.3(90 \text{ ksi}) - \frac{90 \text{ ksi}}{0.75(54 \text{ ksi})}(12.5 \text{ ksi}) < 90 \text{ ksi}$ | $= 1.3(90 \text{ ksi}) - \frac{2.00(90 \text{ ksi})}{54 \text{ ksi}}(8.32 \text{ ksi}) < 90 \text{ ksi}$ |
| $= 89.2 \text{ ksi} < 90 \text{ ksi}$ | $= 89.3 \text{ ksi} < 90 \text{ ksi}$ |
| Therefore: | Therefore: |
| $F'_{nt} = 89.2$ ksi | $F'_{nt} = 89.3$ ksi |

Using the value of $F'_{nt}$ determined for LRFD, the nominal tensile strength of one bolt is:

$$r_n = F'_{nt} A_b$$
(from *Spec.* Eq. J3-2)

$$= (89.2 \text{ ksi})(0.601 \text{ in.}^2)$$

$$= 53.6 \text{ kips}$$

The available tensile strength of the bolts due to combined tension and shear is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |

---

# IIA-21

| LRFD | ASD |
|------|-----|
| $\phi r_n = 0.75(53.6 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{53.6 \text{ kips/bolt}}{2.00}$ |
| $= 40.2$ kips | $= 26.8$ kips |
| | |
| $\phi R_n = n\phi r_n$ | $\frac{R_n}{\Omega} = n\frac{r_n}{\Omega}$ |
| $= (10 \text{ bolts})(40.2 \text{ kips/bolt})$ | $= (10 \text{ bolts})(26.8 \text{ kips/bolt})$ |
| $= 402 \text{ kips} > 60 \text{ kips}$ **o.k.** | $= 268 \text{ kips} > 40 \text{ kips}$ **o.k.** |

*Prying Action*

From AISC *Manual* Part 9, the available tensile strength of the bolts in the outstanding angle legs taking prying action into account is determined as follows:

$$b = \frac{gage - t_w - t}{2}$$

$$= \frac{7\frac{1}{2} \text{ in.} - 0.355 \text{ in.} - \frac{5}{8} \text{ in.}}{2}$$

$$= 3.26 \text{ in.}$$

$$a = \frac{2(angle\ leg) + t_w - gage}{2} \leq 1.25b$$

$$= \frac{2(5 \text{ in.}) + 0.355 \text{ in.} - 7\frac{1}{2} \text{ in.}}{2} \leq 1.25(3.26 \text{ in.})$$

$$= 1.43 \text{ in.} \leq 4.08 \text{ in.}$$

$$= 1.43 \text{ in.}$$

$$a' = a + \frac{d}{2}$$
(*Manual* Eq. 9-23)

$$= 1.43 \text{ in.} + \frac{\frac{3}{8} \text{ in.}}{2}$$

$$= 1.87 \text{ in.}$$

$$b' = b - \frac{d}{2}$$
(*Manual* Eq. 9-24)

$$= 3.26 \text{ in.} - \frac{\frac{3}{8} \text{ in.}}{2}$$

$$= 2.82 \text{ in.}$$

$$\rho = \frac{b'}{a'}$$
(*Manual* Eq. 9-29)

$$= \frac{2.82 \text{ in.}}{1.87 \text{ in.}}$$

$$= 1.51$$

Note that end distances of 1¼ in. are used on the angles, so $p$ is the average pitch of the bolts:

---

# IIA-22

$$p = \frac{l}{n}$$

$$= \frac{14\frac{1}{2} \text{ in.}}{5 \text{ rows}}$$

$$= 2.90 \text{ in.}$$

Check that $p \leq s$:

$$p < s = 3.00 \text{ in.}$$ **o.k.**

$$d' = d_h$$
$$= 1\frac{3}{16} \text{ in.}$$

$$\delta = 1 - \frac{d'}{p}$$
(*Manual* Eq. 9-28)

$$= 1 - \frac{1\frac{3}{16} \text{ in.}}{2.90 \text{ in.}}$$

$$= 0.677$$

The angle thickness required to develop the available strength of the bolt with no prying action is determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
| $T_c = 40.2$ kips/bolt (calculated previously) | $T_c = 26.8$ kips/bolt (calculated previously) |
| $t_c = \sqrt{\frac{4T_c b'}{\phi_b pF_u}}$ (*Manual* Eq. 9-30a) | $t_c = \sqrt{\frac{4\Omega_b T_c b'}{pF_u}}$ (*Manual* Eq. 9-30b) |
| $= \sqrt{\frac{4(40.2 \text{ kips/bolt})(2.82 \text{ in.})}{0.90(2.90 \text{ in.})(65 \text{ ksi})}}$ | $= \sqrt{\frac{4(1.67)(26.8 \text{ kips/bolt})(2.82 \text{ in.})}{(2.90 \text{ in.})(65 \text{ ksi})}}$ |
| $= 1.63$ in. | $= 1.64$ in. |

Conservatively using the ASD value for $t_c$:

$$\alpha' = \frac{1}{\delta(1+\rho)}\left[\left(\frac{t_c}{t}\right)^2 - 1\right]$$
(*Manual* Eq. 9-38)

$$= \frac{1}{0.677(1+1.51)}\left[\left(\frac{1.64 \text{ in.}}{\frac{5}{8} \text{ in.}}\right)^2 - 1\right]$$

$$= 3.46$$

Because $\alpha' > 1$, the angles have insufficient strength to develop the bolt strength, therefore:

$$Q = \left(\frac{t}{t_c}\right)^2(1+\delta)$$
(*Manual* Eq. 9-39c)

$$= \left(\frac{\frac{5}{8} \text{ in.}}{1.64 \text{ in.}}\right)^2(1+0.677)$$

$$= 0.244$$

---

# IIA-23

The available tensile strength of the bolts taking prying action into account is determined using AISC *Manual* Equation 9-40 as follows:

| LRFD | ASD |
|------|-----|
| $T_{c, adj} = QT_c$ | $T_{c, adj} = QT_c$ |
| $= (0.244)(40.2 \text{ kips/bolt})$ | $= (0.244)(26.8 \text{ kips/bolt})$ |
| $= 9.81$ kips/bolt | $= 6.54$ kips/bolt |
| $\phi R_n = nT_{c, adj}$ | $\frac{R_n}{\Omega} = nT_{c, adj}$ |
| $= (10 \text{ bolts})(9.81 \text{ kips/bolt})$ | $= (10 \text{ bolts})(6.54 \text{ kips/bolt})$ |
| $= 98.1 \text{ kips} > 60 \text{ kips}$ **o.k.** | $= 65.4 \text{ kips} > 40 \text{ kips}$ **o.k.** |

*Shear Strength of Angles*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the angles is determined as follows:

$$A_{gv} = (2 \text{ angles})lt$$
$$= (2 \text{ angles})(14\frac{1}{2} \text{ in.})(\frac{5}{8} \text{ in.})$$
$$= 18.1 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$
(*Spec.* Eq. J4-3)

$$= 0.60(50 \text{ ksi})(18.1 \text{ in.}^2)$$

$$= 543 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
| $\phi R_n = 1.00(543 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{543 \text{ kips}}{1.50}$ |
| $= 543 \text{ kips} > 96.0 \text{ kips}$ **o.k.** | $= 362 \text{ kips} > 64.0 \text{ kips}$ **o.k.** |

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the angle is determined using the net area determined in accordance with AISC *Specification* Section B4.3b.

$$A_{nv} = (2 \text{ angles})[l - n(d_h + \frac{1}{16} \text{ in.})]t$$

$$= (2 \text{ angles})[14\frac{1}{2} \text{ in.} - 5(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](\frac{5}{8} \text{ in.})$$

$$= 11.9 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$
(*Spec.* Eq. J4-4)

$$= 0.60(65 \text{ ksi})(11.9 \text{ in.}^2)$$

$$= 464 \text{ kips}$$

---

# IIA-24

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(464 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{464 \text{ kips}}{2.00}$ |
| $= 348 \text{ kips} > 96.0 \text{ kips}$ **o.k.** | $= 232 \text{ kips} > 64.0 \text{ kips}$ **o.k.** |

*Tensile Strength of Angles*

From AISC *Specification* Section J4.1(a), the available tensile yielding strength of the angles is determined as follows:

$$A_g = (2 \text{ angles})lt$$
$$= (2 \text{ angles})(14\frac{1}{2} \text{ in.})(\frac{5}{8} \text{ in.})$$
$$= 18.1 \text{ in.}^2$$

$$R_n = F_y A_g$$
(*Spec.* Eq. J4-1)

$$= (50 \text{ ksi})(18.1 \text{ in.}^2)$$

$$= 905 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
| $\phi R_n = 0.90(905 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{905 \text{ kips}}{1.67}$ |
| $= 815 \text{ kips} > 60 \text{ kips}$ **o.k.** | $= 542 \text{ kips} > 40 \text{ kips}$ **o.k.** |

From AISC *Specification* Section J4.1(b), the available tensile rupture strength of the angles is determined from AISC *Specification* Equation J4-2. AISC *Specification* Table D3.1, Case 1, applies in this case because the tension load is transmitted directly to the cross-sectional element by the fasteners; therefore, $U = 1.00$. With $A_{nt} = A_{nv}$ (calculated previously), the effective net area is:

$$A_e = A_{nt}U$$
(*Spec.* Eq. D3-1)

$$= (11.9 \text{ in.}^2)(1.00)$$

$$= 11.9 \text{ in.}^2$$

$$R_n = F_u A_e$$
(*Spec.* Eq. J4-2)

$$= (65 \text{ ksi})(11.9 \text{ in.}^2)$$

$$= 774 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(774 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{774 \text{ kips}}{2.00}$ |
| $= 581 \text{ kips} > 60 \text{ kips}$ **o.k.** | $= 387 \text{ kips} > 40 \text{ kips}$ **o.k.** |

*Block Shear Rupture of Angles—Beam Web Side*

---

# IIA-25

The nominal strength for the limit state of block shear rupture of the angles, assuming an L-shaped tearout due to shear load only, is determined as follows. The tearout pattern is shown in Figure II.A-1B-4.

$$R_{bsv} = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$
(from *Spec.* Eq. J4-5)

where

$$A_{gv} = (2 \text{ angles})(l - l_{ev})t$$
$$= (2 \text{ angles})(14\frac{1}{2} \text{ in.} - 1\frac{1}{4} \text{ in.})(\frac{5}{8} \text{ in.})$$
$$= 16.6 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (2 \text{ angles})(n - 0.5)(d_h + \frac{1}{16} \text{ in.})t$$
$$= 16.6 \text{ in.}^2 - (2 \text{ angles})(5 - 0.5)(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})(\frac{5}{8} \text{ in.})$$
$$= 11.0 \text{ in.}^2$$

$$A_{nt} = (2 \text{ angles})[l_{eh} - 0.5(d_h + \frac{1}{16} \text{ in.})]t$$
$$= (2 \text{ angles})[1\frac{1}{4} \text{ in.} - 0.5(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](\frac{5}{8} \text{ in.})$$
$$= 0.938 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_{bsv} = 0.60(65 \text{ ksi})(11.0 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.938 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(16.6 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.938 \text{ in.}^2)$$

$$= 490 \text{ kips} < 559 \text{ kips}$$

Therefore:

$$R_{bsv} = 490 \text{ kips}$$

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture of the angles is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_{bsv} = 0.75(490 \text{ kips})$ | $\frac{R_{bsv}}{\Omega} = \frac{490 \text{ kips}}{2.00}$ |
| $= 368 \text{ kips} > 75 \text{ kips}$ **o.k.** | $= 245 \text{ kips} > 50 \text{ kips}$ **o.k.** |

---

# IIA-26

<div style="text-align: center;">
<img src="block_shear_diagram" alt="Diagram showing block shear rupture pattern with:
- Vertical dimension: 1⅜"
- Horizontal dimension: 1⅜"
- Hatched area showing shear path
- Multiple bolt holes arranged vertically
- Total vertical dimension: 4 @ 3" = 1'-2"
- Force V indicated">
</div>

*Fig. II.A-1B-4. Block shear rupture of angles for shear load only.*

The block shear rupture failure path due to axial load only could occur as an L- or U-shape. Assuming an L-shaped tearout relative to the axial load on the angles, the nominal block shear rupture strength of the angles is determined as follows. The tearout pattern is shown in Figure II.A-1B-5.

$$R_{bsn} = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$
(from *Spec.* Eq. J4-5)

where

$$A_{gv} = (2 \text{ angles})l_{eh}t$$
$$= (2 \text{ angles})(1\frac{1}{4} \text{ in.})(\frac{5}{8} \text{ in.})$$
$$= 1.56 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (2 \text{ angles})(0.5)(d_h + \frac{1}{16} \text{ in.})t$$
$$= 1.56 \text{ in.}^2 - (2 \text{ angles})(0.5)(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})(\frac{5}{8} \text{ in.})$$
$$= 0.935 \text{ in.}^2$$

$$A_{nt} = (2 \text{ angles})[(l - l_{ev}) - (n - 0.5)(d_h + \frac{1}{16} \text{ in.})]t$$
$$= (2 \text{ angles})[(14\frac{1}{2} \text{ in.} - 1\frac{1}{4} \text{ in.}) - (5 - 0.5)(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](\frac{5}{8} \text{ in.})$$
$$= 10.9 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_{bsn} = 0.60(65 \text{ ksi})(0.935 \text{ in.}^2) + 1.0(65 \text{ ksi})(10.9 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(1.56 \text{ in.}^2) + 1.0(65 \text{ ksi})(10.9 \text{ in.}^2)$$

$$= 745 \text{ kips} < 755 \text{ kips}$$

Therefore:

$$R_{bsn} = 745 \text{ kips}$$

---

# IIA-27

<div style="text-align: center;">
<img src="block_shear_L_shape" alt="Diagram showing L-shaped block shear rupture pattern with:
- Vertical dimension: 1⅜"
- Horizontal dimension: 1⅜"
- Hatched area showing failure path
- Multiple bolt holes arranged vertically
- Total vertical dimension: 4 @ 3" = 1'-2"
- Force N indicated (horizontal)">
</div>

*Fig. II.A-1B-5. Block shear rupture of angles for axial load only—L-shape.*

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture of the angles is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_{bsn} = 0.75(745 \text{ kips})$ | $\frac{R_{bsn}}{\Omega} = \frac{745 \text{ kips}}{2.00}$ |
| $= 559 \text{ kips} > 60 \text{ kips}$ **o.k.** | $= 373 \text{ kips} > 40 \text{ kips}$ **o.k.** |

The nominal strength for the limit state of block shear rupture assuming a U-shaped tearout relative to the axial load on the angles is determined as follows. The tearout pattern is shown in Figure II.A-1B-6.

$$R_{bsn} = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$
(from *Spec.* Eq. J4-5)

where

$$A_{gv} = (2 \text{ angles})(2 \text{ planes})l_{eh}t$$
$$= (2 \text{ angles})(2 \text{ planes})(1\frac{1}{4} \text{ in.})(\frac{5}{8} \text{ in.})$$
$$= 3.13 \text{ in.}^2$$

$$A_{nv} = (2 \text{ angles})(2 \text{ planes})[l_{eh} - 0.5(d_h + \frac{1}{16} \text{ in.})]t$$
$$= (2 \text{ angles})(2 \text{ planes})[1\frac{1}{4} \text{ in.} - 0.5(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](\frac{5}{8} \text{ in.})$$
$$= 1.88 \text{ in.}^2$$

$$A_{nt} = (2 \text{ angles})[l - (n-1)(d_h + \frac{1}{16} \text{ in.})]t$$
$$= (2 \text{ angles})[12.0 \text{ in.} - (5-1)(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](\frac{5}{8} \text{ in.})$$
$$= 10.0 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_{bsn} = 0.60(65 \text{ ksi})(1.88 \text{ in.}^2) + 1.0(65 \text{ ksi})(10.0 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(3.13 \text{ in.}^2) + 1.0(65 \text{ ksi})(10.0 \text{ in.}^2)$$

$$= 723 \text{ kips} < 744 \text{ kips}$$

---

# IIA-28

<div style="text-align: center;">
<img src="block_shear_U_shape" alt="Diagram showing U-shaped block shear rupture pattern with:
- Vertical dimension: 1⅜"
- Horizontal dimension: 1⅜"
- Hatched area showing failure path on both sides
- Multiple bolt holes arranged vertically
- Total vertical dimension: 4 @ 3" = 1'-2"
- Force N indicated (horizontal)">
</div>

*Fig. II.A-1B-6. Block shear rupture of angles for axial load only—U-shape.*

Therefore:

$$R_{bsn} = 723 \text{ kips}$$

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture of the angles is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_{bsn} = 0.75(723 \text{ kips})$ | $\frac{R_{bsn}}{\Omega} = \frac{723 \text{ kips}}{2.00}$ |
| $= 542 \text{ kips} > 60 \text{ kips}$ **o.k.** | $= 362 \text{ kips} > 40 \text{ kips}$ **o.k.** |

Considering the interaction of shear and axial loads, apply a formulation that is similar to AISC *Manual* Equation 12-1:

| LRFD | ASD |
|------|-----|
| $\left(\frac{V_r}{\phi R_{bsv}}\right)^2 + \left(\frac{N_r}{\phi R_{bsn}}\right)^2 \leq 1$ | $\left(\frac{V_r}{R_{bsv}/\Omega}\right)^2 + \left(\frac{N_r}{R_{bsn}/\Omega}\right)^2 \leq 1$ |
| $\left(\frac{75 \text{ kips}}{368 \text{ kips}}\right)^2 + \left(\frac{60 \text{ kips}}{559 \text{ kips}}\right)^2 = 0.0531 \leq 1$ **o.k.** | $\left(\frac{50 \text{ kips}}{245 \text{ kips}}\right)^2 + \left(\frac{40 \text{ kips}}{373 \text{ kips}}\right)^2 = 0.0531 \leq 1$ **o.k.** |

*Block Shear Rupture of Angles—Outstanding Legs*

The nominal strength for the limit state of block shear rupture relative to the shear load on the angles is determined as follows. The tearout pattern is shown in Figure II.A-1B-7.

$$R_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$
(*Spec.* Eq. J4-5)

---

# IIA-29

<div style="text-align: center;">
<img src="block_shear_outstanding_legs" alt="Diagram showing block shear rupture of outstanding legs with:
- Cross-sectional view showing both angle legs
- Hatched areas on both sides showing failure paths
- Multiple bolt holes arranged vertically
- Total vertical dimension: 4 @ 3" = 1'-2"
- Forces V/2 indicated on both sides
- Dimensions: 1⅞", 7½" gage, 1⅞"
- Top/bottom dimensions: 1⅜"">
</div>

*Fig. II.A-1B-7. Block shear rupture of outstanding legs of angles.*

where

$$A_{gv} = (2 \text{ angles})(l - l_{ev})t$$
$$= (2 \text{ angles})(14\frac{1}{2} \text{ in.} - 1\frac{1}{4} \text{ in.})(\frac{5}{8} \text{ in.})$$
$$= 16.6 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (2 \text{ angles})(n - 0.5)(d_h + \frac{1}{16} \text{ in.})t$$
$$= 16.6 \text{ in.}^2 - (2 \text{ angles})(5 - 0.5)(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})(\frac{5}{8} \text{ in.})$$
$$= 11.0 \text{ in.}^2$$

$$A_{nt} = (2 \text{ angles})[l_{eh} - 0.5(d_h + \frac{1}{16} \text{ in.})]t$$
$$= (2 \text{ angles})[1⅞ \text{ in.} - 0.5(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](\frac{5}{8} \text{ in.})$$
$$= 1.17 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_n = 0.60(65 \text{ ksi})(11.0 \text{ in.}^2) + 1.0(65 \text{ ksi})(1.17 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(16.6 \text{ in.}^2) + 1.0(65 \text{ ksi})(1.17 \text{ in.}^2)$$

$$= 505 \text{ kips} < 574 \text{ kips}$$

Therefore:

$$R_n = 505 \text{ kips}$$

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture of the angles is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |

---

# IIA-30

| LRFD | ASD |
|------|-----|
| $\phi R_n = 0.75(505 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{505 \text{ kips}}{2.00}$ |
| $= 379 \text{ kips} > 75 \text{ kips}$ **o.k.** | $= 253 \text{ kips} > 50 \text{ kips}$ **o.k.** |

*Shear Strength of Beam Web*

From AISC *Specification* Section J4.2(a), the available shear yield strength of the beam web is determined as follows:

$$A_{gv} = dt_w$$
$$= (18.0 \text{ in.})(0.355 \text{ in.})$$
$$= 6.39 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$
(*Spec.* Eq. J4-3)

$$= 0.60(50 \text{ ksi})(6.39 \text{ in.}^2)$$

$$= 192 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
| $\phi R_n = 1.00(192 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{192 \text{ kips}}{1.50}$ |
| $= 192 \text{ kips} > 75 \text{ kips}$ **o.k.** | $= 128 \text{ kips} > 50 \text{ kips}$ **o.k.** |

The limit state of shear rupture of the beam web does not apply in this example because the beam is uncoped.

*Tensile Strength of Beam*

From AISC *Specification* Section J4.1(a), the available tensile yielding strength of the beam is determined as follows:

$$R_n = F_y A_g$$
(*Spec.* Eq. J4-1)

$$= (50 \text{ ksi})(14.7 \text{ in.}^2)$$

$$= 735 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
| $\phi R_n = 0.90(735 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{735 \text{ kips}}{1.67}$ |
| $= 662 \text{ kips} > 60 \text{ kips}$ **o.k.** | $= 440 \text{ kips} > 40 \text{ kips}$ **o.k.** |

From AISC *Specification* Section J4.1(b), determine the available tensile rupture strength of the beam. The effective net area is $A_e = A_n U$. No cases in AISC *Specification* Table D3.1 apply to this configuration; therefore, $U$ is determined from AISC *Specification* Section D3.

---

# IIA-31

$$A_n = A_g - n(d_h + \frac{1}{16} \text{ in.})(t_w)$$
$$= 14.7 \text{ in.}^2 - 5(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.})(0.355 \text{ in.})$$
$$= 12.9 \text{ in.}^2$$

As stated in AISC *Specification* Section D3, the value of $U$ can be determined as the ratio of the gross area of the connected element (beam web) to the member gross area.

$$U = \frac{(d - 2t_f)(t_w)}{A_g}$$
$$= \frac{[18.0 \text{ in.} - 2(0.570 \text{ in.})](0.355 \text{ in.})}{14.7 \text{ in.}^2}$$
$$= 0.407$$

$$A_e = A_n U$$
(*Spec.* Eq. D3-1)
$$= (12.9 \text{ in.}^2)(0.407)$$
$$= 5.25 \text{ in.}^2$$

$$R_n = F_u A_e$$
(*Spec.* Eq. J4-2)
$$= (65 \text{ ksi})(5.25 \text{ in.}^2)$$
$$= 341 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(341 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{341 \text{ kips}}{2.00}$ |
| $= 256 \text{ kips} > 60 \text{ kips}$ **o.k.** | $= 171 \text{ kips} > 40 \text{ kips}$ **o.k.** |

*Block Shear Rupture Strength of Beam Web*

Block shear rupture is only applicable in the direction of the axial load because the beam is uncoped and the limit state is not applicable for an uncoped beam subject to vertical shear. Assuming a U-shaped tearout relative to the axial load, and assuming a horizontal edge distance of $l_{eh} = 1\frac{3}{4}$ in. $- \frac{1}{4}$ in. $= 1\frac{1}{2}$ in. to account for a possible beam underrun of $\frac{1}{4}$ in., the block shear rupture strength is:

$$R_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$
(*Spec.* Eq. J4-5)

where

$$A_{gv} = (2)l_{eh}t_w$$
$$= (2)(1\frac{1}{2} \text{ in.})(0.355 \text{ in.})$$
$$= 1.07 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (2)(0.5)(d_h + \frac{1}{16} \text{ in.})t_w$$
$$= 1.07 \text{ in.}^2 - (2)(0.5)(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.})(0.355 \text{ in.})$$
$$= 0.715 \text{ in.}^2$$

---

# IIA-32

$$A_{nt} = [l - (n-1)(d_h + \frac{1}{16} \text{ in.})]t_w$$
$$= [12.0 \text{ in.} - (5-1)(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.})](0.355 \text{ in.})$$
$$= 2.84 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_n = 0.60(65 \text{ ksi})(0.715 \text{ in.}^2) + 1.0(65 \text{ ksi})(2.84 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(1.07 \text{ in.}^2) + 1.0(65 \text{ ksi})(2.84 \text{ in.}^2)$$
$$= 212 \text{ kips} < 217 \text{ kips}$$

Therefore:
$$R_n = 212 \text{ kips}$$

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture of the beam web is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(212 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{212 \text{ kips}}{2.00}$ |
| $= 159 \text{ kips} > 60 \text{ kips}$ **o.k.** | $= 106 \text{ kips} > 40 \text{ kips}$ **o.k.** |

*Conclusion*

The connection is found to be adequate as given for the applied loads.

---

# IIA-33

# EXAMPLE II.A-1C ALL-BOLTED DOUBLE-ANGLE CONNECTION—STRUCTURAL INTEGRITY CHECK

## Given:

Verify the all-bolted double-angle connection from Example II.A-1B, as shown in Figure II.A-1C-1, for the structural integrity provisions of AISC *Specification* Section B3.9. The connection is verified as a beam and girder end connection and as an end connection of a member bracing a column. Note that these checks are necessary when design for structural integrity is required by the applicable building code.

The beam is an ASTM A992/A992M W18×50 and the angles are ASTM A572/A572M Grade 50 material.

<div style="text-align: center;">
<img src="connection_diagram" alt="Diagram showing:
- W18×50 beam
- 2L4×3½×⅝×1'-2½" (SLBB) double angles
- 5 bolts in vertical arrangement, 4 @ 3" = 12", Gage = 7½"
- Top and bottom edge distances: 1¾"
- Horizontal dimensions: 2¼", 3½", and 3" spacing
- ⅞" dia. Group 120 bolts, thread condition N, std. holes
- Beam web thickness: ½"
- End dimensions: 1¾", 1⅜"">
</div>

*Fig. II.A-1C-1. Connection geometry for Example II.A-1C.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

Angle
ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W18×50
$t_w = 0.355$ in.

---

# IIA-34

From AISC *Specification* Table J3.3, the hole diameter for ⅞-in.-diameter bolts with standard holes is:

$$d_h = \frac{15}{16} \text{ in.}$$

*Beam and Girder End Connection*

From Example II.A-1B, the required shear strength is:

| LRFD | ASD |
|------|-----|
| $V_u = 75 \text{ kips}$ | $V_a = 50 \text{ kips}$ |

From AISC *Specification* Section B3.9(b), the minimum nominal axial tensile strength is:

| LRFD | ASD |
|------|-----|
| $T = \frac{2}{3}V_u \geq 10 \text{ kips}$ | $T = V_a \geq 10 \text{ kips}$ |
| $= \frac{2}{3}(75 \text{ kips}) > 10 \text{ kips}$ | $= 50 \text{ kips} > 10 \text{ kips}$ |
| $= 50 \text{ kips} > 10 \text{ kips}$ | $= 50 \text{ kips}$ |
| $= 50 \text{ kips}$ |  |

From AISC *Specification* Section B3.9, these strength requirements are evaluated independently from other strength requirements.

*Bolt Shear*

From AISC *Specification* Section J3.7, the nominal bolt shear strength for Group 120 bolts with threads not excluded from the thread plane (thread condition N) is:

$$F_{nv} = 54 \text{ ksi, from AISC } Specification \text{ Table J3.2}$$

$$T_n = nF_{nv}A_b(2 \text{ shear planes})$$
(from *Spec.* Eq. J3-1)
$$= (5 \text{ bolts})(54 \text{ ksi})(0.601 \text{ in.}^2)(2 \text{ shear planes})$$
$$= 325 \text{ kips}$$

*Bolt Tension*

From AISC *Specification* Section J3.7, the nominal bolt tensile strength for Group 120 bolts is:

$$F_{nt} = 90 \text{ ksi, from AISC } Specification \text{ Table J3.2}$$

$$T_n = nF_{nt}A_b$$
(from *Spec.* Eq. J3-1)
$$= (10 \text{ bolts})(90 \text{ ksi})(0.601 \text{ in.}^2)$$
$$= 541 \text{ kips}$$

*Bolt Bearing and Tearout*

From AISC *Specification* Section B3.9, for the purpose of satisfying structural integrity requirements, inelastic deformations of the connection are permitted; therefore, AISC *Specification* Equations J3-6b and J3-6d are used to determine the nominal bearing and tearout strength. By inspection the beam web will control. For bolt bearing on the beam web:

---

# IIA-35

$$T_n = (5 \text{ bolts})3.0dt_wF_u$$
(from *Spec.* Eq. J3-6b)
$$= (5 \text{ bolts})(3.0)(\frac{7}{8} \text{ in.})(0.355 \text{ in.})(65 \text{ ksi})$$
$$= 303 \text{ kips}$$

For bolt tearout on the beam web (including a ¼ in. tolerance to account for possible beam underrun):

$$l_c = l_{eh} - 0.5d_h$$
$$= (1\frac{3}{4} \text{ in.} - \frac{1}{4} \text{ in.}) - 0.5(\frac{15}{16} \text{ in.})$$
$$= 1.03 \text{ in.}$$

$$T_n = (5 \text{ bolts})1.5l_ct_wF_u$$
(from *Spec.* Eq. J3-6d)
$$= (5 \text{ bolts})(1.5)(1.03 \text{ in.})(0.355 \text{ in.})(65 \text{ ksi})$$
$$= 178 \text{ kips}$$

*Angle Bending and Prying Action*

From AISC *Manual* Part 9, the nominal strength of the angles accounting for prying action is determined as follows:

$$b = \frac{gage - t_w - t}{2}$$
$$= \frac{7\frac{1}{2} \text{ in.} - 0.355 \text{ in.} - \frac{5}{8} \text{ in.}}{2}$$
$$= 3.26 \text{ in.}$$

$$a = \frac{2(angle\ leg) + t_w - gage}{2} \leq 1.25b$$
$$= \frac{2(5 \text{ in.}) + 0.355 \text{ in.} - 7\frac{1}{2} \text{ in.}}{2} \leq 1.25(3.26 \text{ in.})$$
$$= 1.43 \text{ in.} \leq 4.08 \text{ in.}$$
$$= 1.43 \text{ in.}$$

$$a' = a + \frac{d_h}{2}$$
(*Manual* Eq. 9-23)
$$= 1.43 \text{ in.} + \frac{\frac{7}{8} \text{ in.}}{2}$$
$$= 1.87 \text{ in.}$$

$$b' = b - \frac{d_h}{2}$$
(*Manual* Eq. 9-24)
$$= 3.26 \text{ in.} - \frac{\frac{7}{8} \text{ in.}}{2}$$
$$= 2.82 \text{ in.}$$

$$\rho = \frac{b'}{a'}$$
(*Manual* Eq. 9-29)
$$= \frac{2.82 \text{ in.}}{1.87 \text{ in.}}$$
$$= 1.51$$

---

# IIA-36

Note that end distances of 1¼ in. are used on the angles, so $p$ is the average pitch of the bolts:

$$p = \frac{l}{n}$$
$$= \frac{14\frac{1}{2} \text{ in.}}{5 \text{ bolts}}$$
$$= 2.90 \text{ in.}$$

Check that $p \leq s$ :

$$p < s = 3.00 \text{ in.} \quad \text{o.k.}$$

$$d' = d_h$$
$$= \frac{15}{16} \text{ in.}$$

$$\delta = 1 - \frac{d'}{p}$$
(*Manual* Eq. 9-28)
$$= 1 - \frac{\frac{15}{16} \text{ in.}}{2.90 \text{ in.}}$$
$$= 0.677$$

$$T_c = F_{nt}A_b$$
$$= (90 \text{ ksi})(0.601 \text{ in.}^2)$$
$$= 54.1 \text{ kips/bolt}$$

$$t_c = \sqrt{\frac{4T_c b'}{pF_u}}$$
(from *Manual* Eq. 9-30)
$$= \sqrt{\frac{4(54.1 \text{ kips/bolt})(2.82 \text{ in.})}{(2.90 \text{ in.})(65 \text{ ksi})}}$$
$$= 1.80 \text{ in.}$$

$$\alpha' = \frac{1}{\delta(1+\rho)}\left[\left(\frac{t_c}{t}\right)^2 - 1\right]$$
(*Manual* Eq. 9-38)
$$= \frac{1}{0.677(1+1.51)}\left[\left(\frac{1.80 \text{ in.}}{\frac{5}{8} \text{ in.}}\right)^2 - 1\right]$$
$$= 4.29$$

Because $\alpha' > 1$, the angles have insufficient strength to develop the bolt strength, therefore:

$$Q = \left(\frac{t}{t_c}\right)^2(1+\delta)$$
(*Manual* Eq. 9-39c)
$$= \left(\frac{\frac{5}{8} \text{ in.}}{1.80 \text{ in.}}\right)^2(1+0.677)$$
$$= 0.202$$

---

# IIA-37

$$T_{c,adj} = QT_c$$
(*Manual* Eq. 9-40)
$$= 0.202(54.1 \text{ kips/bolt})$$
$$= 10.9 \text{ kips/bolt}$$

$$T_n = nT_{c,adj}$$
$$= (10 \text{ bolts})(10.9 \text{ kips/bolt})$$
$$= 109 \text{ kips}$$

Note: The 109 kips includes any prying forces, so there is no need to calculate the prying force per bolt, $q_i$.

*Tensile Yielding of Angles*

From AISC *Specification* Section J4.1, the nominal tensile yielding strength of the angles is determined as follows:

$$A_g = (2 \text{ angles})lt$$
$$= (2 \text{ angles})(14\frac{1}{2} \text{ in.})(\frac{5}{8} \text{ in.})$$
$$= 18.1 \text{ in.}^2$$

$$T_n = F_y A_g$$
(from *Spec.* Eq. J4-1)
$$= (50 \text{ ksi})(18.1 \text{ in.}^2)$$
$$= 905 \text{ kips}$$

*Tensile Rupture of Angles*

From AISC *Specification* Section J4.1, the nominal tensile rupture strength of the angles is determined as follows:

$$A_n = (2 \text{ angles})[l - n(d_h + \frac{1}{16} \text{ in.})]t$$
$$= (2 \text{ angles})[14\frac{1}{2} \text{ in.} - 5(\frac{15}{16} \text{ in.} + \frac{1}{16} \text{ in.})](\frac{5}{8} \text{ in.})$$
$$= 11.9 \text{ in.}^2$$

AISC *Specification* Table D3.1, Case 1, applies in this case because tension load is transmitted directly to the cross-section element by fasteners; therefore, $U = 1.0$.

$$A_e = A_n U$$
(*Spec.* Eq. D3-1)
$$= (11.9 \text{ in.}^2)(1.0)$$
$$= 11.9 \text{ in.}^2$$

$$T_n = F_u A_e$$
(from *Spec.* Eq. J4-2)
$$= (65 \text{ ksi})(11.9 \text{ in.}^2)$$
$$= 774 \text{ kips}$$

*Block Shear Rupture*

By inspection, block shear rupture of the beam web will control. From AISC *Specification* Section J4.3, the available block shear rupture strength of the beam web is determined as follows (account for possible ¼ in. beam underrun):

---

# IIA-38

$$T_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$
(from *Spec.* Eq. J4-5)

where

$$A_{gv} = 2l_{eh}t_w$$
$$= 2(1\frac{3}{4} \text{ in.} - \frac{1}{4} \text{ in.})(0.355 \text{ in.})$$
$$= 1.07 \text{ in.}^2$$

$$A_{nv} = 2[l_{eh} - 0.5(d_h + \frac{1}{16} \text{ in.})]t_w$$
$$= 2[(1\frac{3}{4} \text{ in.} - \frac{1}{4} \text{ in.}) - 0.5(\frac{15}{16} \text{ in.} + \frac{1}{16} \text{ in.})](0.355 \text{ in.})$$
$$= 0.710 \text{ in.}^2$$

$$A_{nt} = [l - 4(d_h + \frac{1}{16} \text{ in.})]t_w$$
$$= [12.0 \text{ in.} - 4(\frac{15}{16} \text{ in.} + \frac{1}{16} \text{ in.})](0.355 \text{ in.})$$
$$= 2.84 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$T_n = 0.60(65 \text{ ksi})(0.710 \text{ in.}^2) + 1.0(65 \text{ ksi})(2.84 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(1.07 \text{ in.}^2) + 1.0(65 \text{ ksi})(2.84 \text{ in.}^2)$$
$$= 212 \text{ kips} < 217 \text{ kips}$$

Therefore:
$$T_n = 212 \text{ kips}$$

*Nominal Tensile Strength*

The controlling nominal tensile strength, $T_n$, is the least of those previously calculated:

$$T_n = \min\{325 \text{ kips}, 541 \text{ kips}, 303 \text{ kips}, 178 \text{ kips}, 109 \text{ kips}, 905 \text{ kips}, 774 \text{ kips}, 212 \text{ kips}\}$$
$$= 109 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $T_n = 109 \text{ kips} > 50 \text{ kips} \quad \text{o.k.}$ | $T_n = 109 \text{ kips} > 50 \text{ kips} \quad \text{o.k.}$ |

*Column Bracing*

From AISC *Specification* Section B3.9(c), the minimum nominal tensile strength for the connection of a member bracing a column is equal to 1% of two-thirds of the required column axial strength for LRFD and equal to 1% of the required column axial for ASD. These requirements are evaluated independently from other strength requirements.

The maximum column axial force this connection is able to brace is determined as follows:

| LRFD | ASD |
|------|-----|
| $T_n \geq 0.01\left(\frac{2}{3}\right)P_u$ | $T_n \geq 0.01P_a$ |

---

# IIA-39

| LRFD | ASD |
|------|-----|
| Solving for the column axial force: | Solving for the column axial force: |
| $P_u \leq 100\left(\frac{3}{2}\right)T_n$ | $P_a \leq 100T_n$ |
| $= 100\left(\frac{3}{2}\right)(109 \text{ kips})$ | $= 100(109 \text{ kips})$ |
| $= 16,400 \text{ kips}$ | $= 10,900 \text{ kips}$ |

As long as the required column axial strength is less than $P_u = 16,400$ kips or $P_a = 10,900$ kips, this connection is an adequate column brace.

---

# IIA-40

# EXAMPLE II.A-2A BOLTED/WELDED DOUBLE-ANGLE CONNECTION

## Given:

Verify the available strength of a double-angle shear connection with welds on the support legs (welds B) and bolts in the supported-beam-web legs, as shown in Figure II.A-2A-1. The ASTM A992/A992M W36×231 beam is attached to an ASTM A992/A992M W14×90 column flange supporting the following beam end reactions:

$$R_D = 37.5 \text{ kips}$$
$$R_L = 113 \text{ kips}$$

Use ASTM A572/A572M Grade 50 angles and 70-ksi weld electrodes.

This example is repeated using the following two procedures:
Part A: Determine the available connection strength using the tables in *Manual* Part 10.
Part B: Determine the available connection strength by checking individual limit states.

<div style="text-align: center;">
<img src="connection_detail" alt="Diagram showing:
- Front view with 7 bolts @ 3" = 1'-9", total height 1⅜"
- Dimensions: 2¼", 1⅝", 1⅝" at top
- Section A-A showing:
  - ⅝/₁₆ return at top (typ.)
  - ¾" dia. Group 120 bolts, thread condition N, std. holes
  - 2L4×3½×⅜ × 1'-11½" (SLBB) angles
  - W36×231 beam
  - W14×90 column
  - Bottom flange coped for erection
- Note: See AISC Manual Figure 10-5(a) for recommended erection clearance between double angles shop attached to a column flange.">
</div>

*Fig. II.A-2A-1. Connection geometry for Example II.A-2A.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam and column
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

Angles
ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

---

# IIA-41

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W36×231
$t_w = 0.760$ in.

Column
W14×90
$t_f = 0.710$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(37.5 \text{ kips}) + 1.6(113 \text{ kips})$ | $R_a = 37.5 \text{ kips} + 113 \text{ kips}$ |
| $= 226 \text{ kips}$ | $= 151 \text{ kips}$ |

*Part A—Determine the Available Connection Strength Using the Tables in Manual Part 10*

*Weld Design*

Use AISC *Manual* Table 10-2 (welds B) with $n = 8$. Try $\frac{5}{16}$ in. weld size, $l = 23\frac{1}{2}$ in. From AISC *Manual* Table 10-2, the minimum support thickness is:

$$t_{min} = 0.238 \text{ in.} < 0.710 \text{ in.} \quad \text{o.k.}$$

| LRFD | ASD |
|------|-----|
| $\phi R_n = 318 \text{ kips} > 226 \text{ kips} \quad \text{o.k.}$ | $\frac{R_n}{\Omega} = 212 \text{ kips} > 151 \text{ kips} \quad \text{o.k.}$ |

*Angle Thickness*

From AISC *Specification* Section J2.2b, the minimum angle thickness for a $\frac{5}{16}$ in. fillet weld is:

$$t = w + \frac{1}{16} \text{ in.}$$
$$= \frac{5}{16} \text{ in.} + \frac{1}{16} \text{ in.}$$
$$= \frac{3}{8} \text{ in.}$$

Try 2L4×3½×⅜ (SLBB).

*Angle Design*

AISC *Manual* Table 10-1a includes checks for shear rupture and block shear rupture of the angles.

Check 8 rows of ¾-in.-diameter bolts in standard holes and ⅜ in. angle thickness. From AISC *Manual* Table 10-1a:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 362 \text{ kips} > 226 \text{ kips} \quad \text{o.k.}$ | $\frac{R_n}{\Omega} = 241 \text{ kips} > 151 \text{ kips} \quad \text{o.k.}$ |

*Available Shear Transfer Strength at Bolt Holes*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength determined in

---

# IIA-42

accordance with AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the angles at the bolt hole determined in accordance with AISC *Specification* Section J3.11a, and (3) the available bearing or tearout strength of the beam web or support element at the bolt hole determined in accordance with AISC *Specification* Section J3.11a.

From AISC *Manual* Table 10-1b, the available bolt shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) in double shear is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9 \text{ kips}(2)$ | $\frac{r_n}{\Omega} = 11.9 \text{ kips}(2)$ |
| $= 35.8 \text{ kips}$ | $= 23.8 \text{ kips}$ |

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the angle per bolt for ¾-in.-diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): | For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): |
| $\phi r_n = (49.4 \text{ kip/in.})(\frac{3}{8} \text{ in.})(2 \text{ angles})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kip/in.})(\frac{3}{8} \text{ in.})(2 \text{ angles})$ |
| $= 37.1 \text{ kips}$ | $= 24.7 \text{ kips}$ |
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kip/in.})(\frac{3}{8} \text{ in.})(2 \text{ angles})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(\frac{3}{8} \text{ in.})(2 \text{ angles})$ |
| $= 65.9 \text{ kips}$ | $= 43.9 \text{ kips}$ |

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the beam web per bolt for ¾-in.-diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kip/in.})(0.760 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(0.760 \text{ in.})$ |
| $= 66.7 \text{ kips}$ | $= 44.5 \text{ kips}$ |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the angle for a non-edge bolt, and available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min\begin{Bmatrix} 35.8 \text{ kips,} \\ 65.9 \text{ kips,} \\ 66.7 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{Bmatrix} 23.8 \text{ kips,} \\ 43.9 \text{ kips,} \\ 44.5 \text{ kips} \end{Bmatrix}$ |
| $= 35.8 \text{ kips}$ | $= 23.8 \text{ kips}$ |

At the middle connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the angle for a non-edge bolt, and available bearing and tearout strength of the beam web for a non-edge bolt:

---

# IIA-43

| LRFD | ASD |
|------|-----|
| $\phi r_{n,mid} = \min\begin{Bmatrix} 35.8 \text{ kips,} \\ 65.9 \text{ kips,} \\ 66.7 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,mid}}{\Omega} = \min\begin{Bmatrix} 23.8 \text{ kips,} \\ 43.9 \text{ kips,} \\ 44.5 \text{ kips} \end{Bmatrix}$ |
| $= 35.8 \text{ kips}$ | $= 23.8 \text{ kips}$ |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the angles for an edge bolt, and available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min\begin{Bmatrix} 35.8 \text{ kips,} \\ 37.1 \text{ kips,} \\ 66.7 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{Bmatrix} 23.8 \text{ kips,} \\ 24.7 \text{ kips,} \\ 44.5 \text{ kips} \end{Bmatrix}$ |
| $= 35.8 \text{ kips}$ | $= 23.8 \text{ kips}$ |

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi r_{n,top} + \phi r_{n,mid}(n-2) + \phi r_{n,bot}$ | $\frac{R_n}{\Omega} = \frac{r_{n,top}}{\Omega} + \frac{r_{n,mid}}{\Omega}(n-2) + \frac{r_{n,bot}}{\Omega}$ |
| $= 35.8 \text{ kips} + (35.8 \text{ kips})(8-2) + 35.8 \text{ kips}$ | $= 23.8 \text{ kips} + (23.8 \text{ kips})(8-2) + 23.8 \text{ kips}$ |
| $= 286 \text{ kips} > 226 \text{ kips} \quad \text{o.k.}$ | $= 190 \text{ kips} > 151 \text{ kips} \quad \text{o.k.}$ |

*Available Beam Web Strength*

The available beam web strength is the lesser of the limit states of block shear rupture, shear yielding, and shear rupture. In this example, because of the small size of the cope relative to the overall beam size, the coped section can be found to not control using AISC *Manual* Part 9.

*Available Column Flange Strength*

Because the thickness of the column flange, $t_f = 0.710$ in., is greater than the thickness of the angles, $t = \frac{3}{8}$ in., the available shear rupture strength of the angles is less than that of the column flange. The column flange is adequate for the required loading.

*Summary*

The available shear strength of the connection is controlled by the available shear transfer strength at the bolt holes.

| LRFD | ASD |
|------|-----|
| $\phi R_n = 286 \text{ kips} > 226 \text{ kips} \quad \text{o.k.}$ | $\frac{R_n}{\Omega} = 190 \text{ kips} > 151 \text{ kips} \quad \text{o.k.}$ |

The connection is found to be adequate as given for the applied loads.

*Part B—Determine the Available Connection Strength by Checking Individual Limit States*

*Available Shear Strength of Angles*

---

# IIA-44

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the angles is determined as follows:

$$A_{gv} = (2 \text{ angles})lt$$
$$= (2 \text{ angles})(23\frac{1}{2} \text{ in.})(\frac{3}{8} \text{ in.})$$
$$= 17.6 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$
(*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(17.6 \text{ in.}^2)$$
$$= 528 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
| $\phi R_n = 1.00(528 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{528 \text{ kips}}{1.50}$ |
| $= 528 \text{ kips} > 226 \text{ kips} \quad \text{o.k.}$ | $= 352 \text{ kips} > 151 \text{ kips} \quad \text{o.k.}$ |

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the angle is determined using the net area determined in accordance with AISC *Specification* Section B4.3b.

$$A_{nv} = (2 \text{ angles})[l - n(d_h + \frac{1}{16} \text{ in.})]t$$
$$= (2 \text{ angles})[23\frac{1}{2} \text{ in.} - 8(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.})](\frac{3}{8} \text{ in.})$$
$$= 12.4 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$
(*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(12.4 \text{ in.}^2)$$
$$= 484 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(484 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{484 \text{ kips}}{2.00}$ |
| $= 363 \text{ kips} > 226 \text{ kips} \quad \text{o.k.}$ | $= 242 \text{ kips} > 151 \text{ kips} \quad \text{o.k.}$ |

*Available Block Shear Rupture of Angles*

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture of the angles is determined as follows:

$$R_{bsv} = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$
(from *Spec.* Eq. J4-5)

where

$$A_{gv} = (2 \text{ angles})(l - l_{ev})t$$
$$= (2 \text{ angles})(23\frac{1}{2} \text{ in.} - 1\frac{1}{4} \text{ in.})(\frac{3}{8} \text{ in.})$$
$$= 16.7 \text{ in.}^2$$

---

# IIA-45

$$A_{nv} = A_{gv} - (2 \text{ angles})(n - 0.5)(d_h + \frac{1}{16} \text{ in.})t$$
$$= 16.7 \text{ in.}^2 - (2 \text{ angles})(8 - 0.5)(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.})(\frac{3}{8} \text{ in.})$$
$$= 11.8 \text{ in.}^2$$

$$A_{nt} = (2 \text{ angles})[l_{eh} - 0.5(d_h + \frac{1}{16} \text{ in.})]t$$
$$= (2 \text{ angles})[1\frac{5}{8} \text{ in.} - 0.5(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.})](\frac{3}{8} \text{ in.})$$
$$= 0.703 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_{bsv} = 0.60(65 \text{ ksi})(11.8 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.703 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(16.7 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.703 \text{ in.}^2)$$
$$= 506 \text{ kips} < 547 \text{ kips}$$

Therefore:
$$R_{bsv} = 506 \text{ kips}$$

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture of the angles is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_{bsv} = 0.75(506 \text{ kips})$ | $\frac{R_{bsv}}{\Omega} = \frac{506 \text{ kips}}{2.00}$ |
| $= 380 \text{ kips} > 226 \text{ kips} \quad \text{o.k.}$ | $= 253 \text{ kips} > 151 \text{ kips} \quad \text{o.k.}$ |

*Available Shear Transfer Strength at Bolt Holes*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength determined in accordance with AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the angles at the bolt hole determined in accordance with AISC *Specification* Section J3.11a, and (3) the available bearing or tearout strength of the beam web at the bolt hole determined in accordance with AISC *Specification* Section J3.11a.

*Bolt shear*

From AISC *Manual* Table 7-1, the available shear strength for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9 \text{ kips}$ | $\frac{r_n}{\Omega} = 11.9 \text{ kips}$ |

The available bearing strength of the angles is determined from AISC *Specification* Section J3.11, assuming deformation at service load is a design consideration:

$$r_n = 2.4dtF_u$$
(from *Spec.* Eq. J3-6a)
$$= (2.4)(\frac{3}{4} \text{ in.})(\frac{3}{8} \text{ in.})(65 \text{ ksi})$$
$$= 43.9 \text{ kips}$$

---

# IIA-46

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(43.9 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{43.9 \text{ kips}}{2.00}$ |
| $= 32.9 \text{ kips}$ | $= 22.0 \text{ kips}$ |

The available tearout strength of the angles is determined from AISC *Specification* Section J3.11, assuming deformation at service load is a design consideration.

For edge bolt tearout, the clear distance along the line of action of the force, between the edge of the hole and the edge of the angle is:

$$l_c = l_{ev} - 0.5d_h$$
$$= 1\frac{1}{4} \text{ in.} - 0.5(\frac{13}{16} \text{ in.})$$
$$= 0.844 \text{ in.}$$

The available tearout strength of the angles at the edge bolt is:

$$r_n = 1.2l_ctF_u$$
(from *Spec.* Eq. J3-6c)
$$= (1.2)(0.844 \text{ in.})(\frac{3}{8} \text{ in.})(65 \text{ ksi})$$
$$= 24.7 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(24.7 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{24.7 \text{ kips}}{2.00}$ |
| $= 18.5 \text{ kips}$ | $= 12.4 \text{ kips}$ |

For non-edge bolt tearout in the angles, the clear distance is between bolt holes:

$$l_c = s - d_h$$
$$= 3 \text{ in.} - \frac{13}{16} \text{ in.}$$
$$= 2.19 \text{ in.}$$

The available tearout strength of the angles at non-edge bolts is:

$$r_n = 1.2l_ctF_u$$
(from *Spec.* Eq. J3-6c)
$$= (1.2)(2.19 \text{ in.})(\frac{3}{8} \text{ in.})(65 \text{ ksi})$$
$$= 64.1 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(64.1 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{64.1 \text{ kips}}{2.00}$ |
| $= 48.1 \text{ kips}$ | $= 32.1 \text{ kips}$ |

---

# IIA-47

The available bearing strength of the beam web is determined from AISC *Specification* Section J3.11, assuming deformation at service load is a design consideration:

$$r_n = 2.4dtF_u$$
(from *Spec.* Eq. J3-6a)
$$= (2.4)(\frac{3}{4} \text{ in.})(0.760 \text{ in.})(65 \text{ ksi})$$
$$= 88.9 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(88.9 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{88.9 \text{ kips/bolt}}{2.00}$ |
| $= 66.7 \text{ kips}$ | $= 44.5 \text{ kips/bolt}$ |

The available tearout strength of the beam web is determined from AISC *Specification* Section J3.11, assuming deformation at service load is a design consideration.

There is no edge bolt tearout for the beam web. For non-edge bolt tearout in the beam web, the clear distance is between bolt holes:

$$l_c = s - d_h$$
$$= 3 \text{ in.} - \frac{13}{16} \text{ in.}$$
$$= 2.19 \text{ in.}$$

The available tearout strength of the beam web at non-edge bolts is:

$$r_n = 1.2l_ctF_u$$
(from *Spec.* Eq. J3-6c)
$$= (1.2)(2.19 \text{ in.})(0.760 \text{ in.})(65 \text{ ksi})$$
$$= 130 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(130 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{130 \text{ kips}}{2.00}$ |
| $= 97.5 \text{ kips}$ | $= 65.0 \text{ kips}$ |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because the bolts are in double shear), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by 2 because there are two angles), and the available bearing and tearout strength of the beam web for a non-edge bolt:

---

# IIA-48

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min\begin{Bmatrix} 17.9 \text{ kips}(2) = 35.8 \text{ kips,} \\ 32.9 \text{ kips}(2) = 65.8 \text{ kips,} \\ 48.1 \text{ kips}(2) = 96.2 \text{ kips,} \\ 66.7 \text{ kips,} \\ 97.5 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips}(2) = 23.8 \text{ kips,} \\ 22.0 \text{ kips}(2) = 44.0 \text{ kips,} \\ 32.1 \text{ kips}(2) = 64.2 \text{ kips,} \\ 44.5 \text{ kips,} \\ 65.0 \text{ kips} \end{Bmatrix}$ |
| $= 35.8 \text{ kips}$ | $= 23.8 \text{ kips}$ |

At the middle connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because the bolts are in double shear), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by 2 because there are two angles), and the available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,mid} = \min\begin{Bmatrix} 17.9 \text{ kips}(2) = 35.8 \text{ kips,} \\ 32.9 \text{ kips}(2) = 65.8 \text{ kips,} \\ 48.1 \text{ kips}(2) = 96.2 \text{ kips,} \\ 66.7 \text{ kips,} \\ 97.5 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,mid}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips}(2) = 23.8 \text{ kips,} \\ 22.0 \text{ kips}(2) = 44.0 \text{ kips,} \\ 32.1 \text{ kips}(2) = 64.2 \text{ kips,} \\ 44.5 \text{ kips,} \\ 65.0 \text{ kips} \end{Bmatrix}$ |
| $= 35.8 \text{ kips}$ | $= 23.8 \text{ kips}$ |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because the bolts are in double shear), the available bearing and tearout strength of the angles for an edge bolt (multiplied by 2 because there are two angles), and the available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min\begin{Bmatrix} 17.9 \text{ kips}(2) = 35.8 \text{ kips,} \\ 32.9 \text{ kips}(2) = 65.8 \text{ kips,} \\ 18.5 \text{ kips}(2) = 37.0 \text{ kips,} \\ 66.7 \text{ kips,} \\ 97.5 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips}(2) = 23.8 \text{ kips,} \\ 22.0 \text{ kips}(2) = 44.0 \text{ kips,} \\ 12.4 \text{ kips}(2) = 24.8 \text{ kips,} \\ 44.5 \text{ kips,} \\ 65.0 \text{ kips} \end{Bmatrix}$ |
| $= 35.8 \text{ kips}$ | $= 23.8 \text{ kips}$ |

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi r_{n,top} + \phi r_{n,mid}(n-2) + \phi r_{n,bot}$ | $\frac{R_n}{\Omega} = \frac{r_{n,top}}{\Omega} + \frac{r_{n,mid}}{\Omega}(n-2) + \frac{r_{n,bot}}{\Omega}$ |
| $= 35.8 \text{ kips} + (35.8 \text{ kips})(8-2) + 35.8 \text{ kips}$ | $= 23.8 \text{ kips} + (23.8 \text{ kips})(8-2) + 23.8 \text{ kips}$ |
| $= 286 \text{ kips} > 226 \text{ kips} \quad \text{o.k.}$ | $= 190 \text{ kips} > 151 \text{ kips} \quad \text{o.k.}$ |

---

# IIA-49

*Available Beam Web Strength*

Because the beam is not coped at the top flange, limit states of block shear rupture and shear rupture of the beam are not applicable. The beam web is adequate for the required loading.

*Available Weld Strength*

The available weld strength is determined using AISC *Manual* Table 8-4, with Angle = 0°.

$$k = 0$$
$$e_x = al$$
$$= 4 \text{ in.}$$
$$a = \frac{4 \text{ in.}}{23.5 \text{ in.}}$$
$$= 0.170$$

Interpolating from AISC *Manual* Table 8-4:

$$C = 3.61$$

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi CC_1Dl$ | $\frac{R_n}{\Omega} = \frac{CC_1Dl(2 \text{ welds})}{\Omega}$ |
| $= 0.75(3.61)(1.0)(5)(23.5 \text{ in.})$ | $= \frac{(3.61)(1.0)(5)(23.5 \text{ in.})}{2.00}$ |
| $= 318 \text{ kips} > 226 \text{ kips} \quad \text{o.k.}$ | $= 212 \text{ kips} > 151 \text{ kips} \quad \text{o.k.}$ |

*Minimum Support Thickness*

The minimum support thickness at the welds is determined as follows:

$$t_{min} = \frac{3.09D}{F_u}$$
(*Manual* Eq. 9-6)
$$= \frac{3.09(5)}{65 \text{ ksi}}$$
$$= 0.237 \text{ in.} < 0.710 \text{ in.} \quad \text{o.k.}$$

*Summary*

The available shear strength of the connection is controlled by the available shear transfer strength at the bolt holes.

| LRFD | ASD |
|------|-----|
| $\phi R_n = 286 \text{ kips} > 226 \text{ kips} \quad \text{o.k.}$ | $\frac{R_n}{\Omega} = 190 \text{ kips} > 151 \text{ kips} \quad \text{o.k.}$ |

The connection is found to be adequate as given for the applied loads.

---

# IIA-50

# EXAMPLE II.A-2B BOLTED/WELDED DOUBLE-ANGLE CONNECTION SUBJECT TO AXIAL AND SHEAR LOADING

## Given:

Verify the available strength of a double-angle connection with welds in the supported-beam-web legs and bolts in the outstanding legs for an ASTM A992/A992M W18×50 beam, as shown in Figure II.A-2B-1, to support the following beam end reactions:

| LRFD | ASD |
|------|-----|
| Shear, $V_u = 75$ kips | Shear, $V_a = 50$ kips |
| Axial tension, $N_u = 60$ kips | Axial tension, $N_a = 40$ kips |

Use ASTM A572/A572M Grade 50 angles and 70-ksi electrodes.

<div style="text-align: center;">
<img src="connection_detail" alt="Diagram showing:
- ⅞" dia. Group 120 bolts, thread condition N, std. holes
- 4 @ 3" = 12", gage = 5½"
- 2L4×3½×⅝×1'-2½" (SLBB) angles
- W18×50 beam
- Vertical dimensions: 1¼" top and bottom
- Horizontal dimensions: 3½", 3", ½"
- Weld sizes: ⅜₁₆, ⅜₁₆">
</div>

*Fig. II.A-2B-1. Connection geometry for Example II.A-2B.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

Angles
ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

---

# IIA-51

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W18×50
$A_g = 14.7 \text{ in.}^2$
$d = 18.0$ in.
$t_w = 0.355$ in.
$b_f = 7.50$ in.
$t_f = 0.570$ in.

From AISC *Specification* Table J3.3, the hole diameter for ⅞-in.-diameter bolts with standard holes is:

$$d_h = \frac{15}{16} \text{ in.}$$

The resultant load is:

| LRFD | ASD |
|------|-----|
| $R_u = \sqrt{V_u^2 + N_u^2}$ | $R_a = \sqrt{V_a^2 + N_a^2}$ |
| $= \sqrt{(75 \text{ kips})^2 + (60 \text{ kips})^2}$ | $= \sqrt{(50 \text{ kips})^2 + (40 \text{ kips})^2}$ |
| $= 96.0 \text{ kips}$ | $= 64.0 \text{ kips}$ |

The following bolt shear, bearing, and tearout calculations are for a pair of bolts.

*Bolt Shear*

From AISC *Manual* Table 7-1, the available shear strength for ⅞-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) in double shear (or pair of bolts):

| LRFD | ASD |
|------|-----|
| $\phi r_n = 48.7 \text{ kips (for pair of bolts)}$ | $\frac{r_n}{\Omega} = 32.5 \text{ kips (for pair of bolts)}$ |

*Bolt Bearing on Angles*

The available bearing strength of the double angle is determined from AISC *Specification* Section J3.11a, assuming deformation at the bolt hole is a design consideration:

$$r_n = (2 \text{ bolts})2.4dtF_u$$
(from *Spec.* Eq. J3-6a)
$$= (2 \text{ bolts})(2.4)(\frac{7}{8} \text{ in.})(\frac{1}{2} \text{ in.})(65 \text{ ksi})$$
$$= 137 \text{ kips (for pair of bolts)}$$

The available bearing strength for a pair of bolts is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(137 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{137 \text{ kips}}{2.00}$ |
| $= 103 \text{ kips (for pair of bolts)}$ | $= 68.5 \text{ kips (for pair of bolts)}$ |

The bolt shear strength controls over bearing in the angles.

---

# IIA-52

*Bolt Tearout on Angles*

The available tearout strength of the angle is determined from AISC *Specification* Section J3.11a, assuming deformation at the bolt hole is a design consideration:

For the edge bolt:

$$l_c = l_e - 0.5d_h$$
$$= 1\frac{1}{4} \text{ in.} - 0.5(\frac{15}{16} \text{ in.})$$
$$= 0.781 \text{ in.}$$

$$r_n = (2 \text{ bolts})1.2l_ctF_u$$
(from *Spec.* Eq. J3-6c)
$$= (2 \text{ bolts})(1.2)(0.781 \text{ in.})(\frac{1}{2} \text{ in.})(65 \text{ ksi})$$
$$= 60.9 \text{ kips (for pair of bolts)}$$

The available tearout strength of the angles for a pair of edge bolts is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(60.9 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{60.9 \text{ kips}}{2.00}$ |
| $= 45.7 \text{ kips (for pair of bolts)}$ | $= 30.5 \text{ kips (for pair of bolts)}$ |

The tearout strength controls over bolt shear and bearing for the edge bolts in the angles.

For the other bolts:

$$l_c = s - d_h$$
$$= 3 \text{ in.} - \frac{15}{16} \text{ in.}$$
$$= 2.06 \text{ in.}$$

$$r_n = (2 \text{ bolts})1.2l_ctF_u$$
(from *Spec.* Eq. J3-6c)
$$= (2 \text{ bolts})(1.2)(2.06 \text{ in.})(\frac{1}{2} \text{ in.})(65 \text{ ksi})$$
$$= 161 \text{ kips (for pair of bolts)}$$

The available tearout strength for a pair of other bolts is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(161 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{161 \text{ kips}}{2.00}$ |
| $= 121 \text{ kips (for pair of bolts)}$ | $= 80.5 \text{ kips (for pair of bolts)}$ |

Bolt shear strength controls over tearout and bearing strength for the other bolts in the angles.

---

# IIA-53

*Strength of Bolted Connection*

The effective strength for the bolted connection at the angles is determined by summing the effective strength for each bolt using the minimum available strength calculated for bolt shear, bearing on the angles, and tearout on the angles.

| LRFD | ASD |
|------|-----|
| $\phi R_n = (1 \text{ bolt})(45.7 \text{ kips})$ | $\frac{R_n}{\Omega} = (1 \text{ bolt})(30.5 \text{ kips})$ |
| $+ (4 \text{ bolts})(48.7 \text{ kips})$ | $+ (4 \text{ bolts})(32.5 \text{ kips})$ |
| $= 241 \text{ kips} > 75 \text{ kips} \quad \text{o.k.}$ | $= 161 \text{ kips} > 50 \text{ kips} \quad \text{o.k.}$ |

*Shear and Tension Interaction in Bolts*

The required shear stress for each bolt is determined as follows:

$$f_{rv} = \frac{V_r}{nA_b}$$

where
$$A_b = 0.601 \text{ in.}^2 \text{ (from AISC } Manual \text{ Table 7-1)}$$
$$n = 10 \text{ bolts}$$

| LRFD | ASD |
|------|-----|
| $f_{rv} = \frac{75 \text{ kips}}{(10 \text{ bolts})(0.601 \text{ in.}^2)}$ | $f_{rv} = \frac{50 \text{ kips}}{(10 \text{ bolts})(0.601 \text{ in.}^2)}$ |
| $= 12.5 \text{ ksi}$ | $= 8.32 \text{ ksi}$ |

The nominal tensile stress modified to include the effects of shear stress is determined from AISC *Specification* Section J3.8 as follows. From AISC *Specification* Table J3.2:

$$F_{nt} = 90 \text{ ksi}$$
$$F_{nv} = 54 \text{ ksi}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $F'_{nt} = 1.3F_{nt} - \frac{F_{nt}}{\phi F_{nv}}f_{rv} \leq F_{nt}$ &nbsp;&nbsp;&nbsp;&nbsp; (*Spec.* Eq. J3-3a) | $F'_{nt} = 1.3F_{nt} - \frac{\Omega F_{nt}}{F_{nv}}f_{rv} \leq F_{nt}$ &nbsp;&nbsp;&nbsp;&nbsp; (*Spec.* Eq. J3-3b) |
| $= 1.3(90 \text{ ksi}) - \frac{90 \text{ ksi}}{0.75(54 \text{ ksi})}(12.5 \text{ ksi}) \leq 90 \text{ ksi}$ | $= 1.3(90 \text{ ksi}) - \frac{2.00(90 \text{ ksi})}{54 \text{ ksi}}(8.32 \text{ ksi}) \leq 90 \text{ ksi}$ |
| $= 89.2 \text{ ksi} < 90 \text{ ksi} \quad \text{o.k.}$ | $= 89.3 \text{ ksi} < 90 \text{ ksi} \quad \text{o.k.}$ |

Using the value of $F'_{nt} = 89.2$ ksi determined for LRFD, the nominal tensile strength of one bolt is:

$$r_n = F'_{nt}A_b$$
(from *Spec.* Eq. J3-2)
$$= (89.2 \text{ ksi})(0.601 \text{ in.}^2)$$
$$= 53.6 \text{ kips}$$

The available tensile strength due to combined tension and shear is:

---

# IIA-54

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = n\phi r_n$ | $\frac{R_n}{\Omega} = n\frac{r_n}{\Omega}$ |
| $= (10 \text{ bolts})(0.75)(53.6 \text{ kips})$ | $= (10 \text{ bolts})\left(\frac{53.6 \text{ kips}}{2.00}\right)$ |
| $= 402 \text{ kips} > 60 \text{ kips} \quad \text{o.k.}$ | $= 268 \text{ kips} > 40 \text{ kips}$ **o.k.** |

*Prying Action on Bolts*

From AISC *Manual* Part 9, the available tensile strength of the bolts in the outstanding angle legs taking prying action into account is determined as follows:

$$b = \frac{gage - t_w - t}{2}$$
$$= \frac{5\frac{1}{2} \text{ in.} - 0.355 \text{ in.} - \frac{1}{2} \text{ in.}}{2}$$
$$= 2.32 \text{ in.}$$

$$a = \frac{angle\ leg(2) + t_w - gage}{2} \leq 1.25b$$
$$= \frac{(4.00 \text{ in.})(2) + 0.355 \text{ in.} - 5\frac{1}{2} \text{ in.}}{2} \leq 1.25(2.32 \text{ in.})$$
$$= 1.43 \text{ in.} \leq 2.90 \text{ in.}$$
$$= 1.43 \text{ in.}$$

Note: Although it is not shown in this example, if the distance from the bolt centerline to the edge of the supporting element is smaller than $a = 1.43$ in., use the smaller $a$ in the following calculation.

$$a' = a + \frac{d_h}{2}$$
(*Manual* Eq. 9-23)
$$= 1.43 \text{ in.} + \frac{\frac{7}{8} \text{ in.}}{2}$$
$$= 1.87 \text{ in.}$$

$$b' = b - \frac{d_h}{2}$$
(*Manual* Eq. 9-24)
$$= 2.32 \text{ in.} - \frac{\frac{7}{8} \text{ in.}}{2}$$
$$= 1.88 \text{ in.}$$

$$\rho = \frac{b'}{a'}$$
(*Manual* Eq. 9-29)
$$= \frac{1.88 \text{ in.}}{1.87 \text{ in.}}$$
$$= 1.01$$

Note that end distances of 1¼ in. are used on the angles, so $p$ is the average pitch of the bolts:

---

# IIA-55

$$p = \frac{l}{n}$$
$$= \frac{14\frac{1}{2} \text{ in.}}{5}$$
$$= 2.90 \text{ in.}$$

Check that $p \leq s$ :

$$p \leq s$$
$$2.90 \text{ in.} < 3 \text{ in.} \quad \text{o.k.}$$

$$d' = d_h$$
$$= \frac{15}{16} \text{ in.}$$

$$\delta = 1 - \frac{d'}{p}$$
(*Manual* Eq. 9-28)
$$= 1 - \frac{\frac{15}{16} \text{ in.}}{2.90 \text{ in.}}$$
$$= 0.677$$

The angle thickness required to develop the available strength of the bolt with no prying action is determined as follows:

| LRFD | ASD |
|------|-----|
| $T_c = 40.2 \text{ kips/bolt (from previous calculations)}$ | $T_c = 26.8 \text{ kips/bolt (from previous calculations)}$ |
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $t_c = \sqrt{\frac{4T_c b'}{\phi_b pF_u}}$ &nbsp;&nbsp;&nbsp;&nbsp; (*Manual* Eq. 9-30a) | $t_c = \sqrt{\frac{\Omega_b 4T_c b'}{pF_u}}$ &nbsp;&nbsp;&nbsp;&nbsp; (*Manual* Eq. 9-30b) |
| $= \sqrt{\frac{4(40.2 \text{ kips/bolt})(1.88 \text{ in.})}{0.90(2.90 \text{ in.})(65 \text{ ksi})}}$ | $= \sqrt{\frac{1.67(4)(26.8 \text{ kips/bolt})(1.88 \text{ in.})}{(2.90 \text{ in.})(65 \text{ ksi})}}$ |
| $= 1.33 \text{ in.}$ | $= 1.34 \text{ in.}$ |

$$\alpha' = \frac{1}{\delta(1+\rho)}\left[\left(\frac{t_c}{t}\right)^2 - 1\right]$$
(*Manual* Eq. 9-38)
$$= \frac{1}{0.677(1+1.01)}\left[\left(\frac{1.34 \text{ in.}}{\frac{1}{2} \text{ in.}}\right)^2 - 1\right]$$
$$= 4.54$$

Because $\alpha' > 1$, the angles have insufficient strength to develop the bolt strength, therefore:

$$Q = \left(\frac{t}{t_c}\right)^2(1+\delta)$$
(*Manual* Eq. 9-39c)
$$= \left(\frac{\frac{1}{2} \text{ in.}}{1.34 \text{ in.}}\right)^2(1+0.677)$$
$$= 0.233$$

---

# IIA-56

The available tensile strength of the bolts taking prying action into account is determined from AISC *Manual* Equation 9-40 as follows:

| LRFD | ASD |
|------|-----|
| $\phi R_n = nT_{c,adj}$ | $\frac{R_n}{\Omega} = nT_{c,adj}$ |
| $= nQT_c$ | $= nQT_c$ |
| $= (10 \text{ bolts})(0.233)(40.2 \text{ kips/bolt})$ | $= (10 \text{ bolts})(0.233)(26.8 \text{ kips/bolt})$ |
| $= 93.7 \text{ kips} > 60 \text{ kips} \quad \text{o.k.}$ | $= 62.4 \text{ kips} > 40 \text{ kips} \quad \text{o.k.}$ |

*Weld Design*

The resultant load angle on the weld is:

| LRFD | ASD |
|------|-----|
| $\theta = \tan^{-1}\left(\frac{N_u}{V_u}\right)$ | $\theta = \tan^{-1}\left(\frac{N_a}{V_a}\right)$ |
| $= \tan^{-1}\left(\frac{60 \text{ kips}}{75 \text{ kips}}\right)$ | $= \tan^{-1}\left(\frac{40 \text{ kips}}{50 \text{ kips}}\right)$ |
| $= 38.7°$ | $= 38.7°$ |

From AISC *Manual* Table 8-8 for Angle = 30° (which will lead to a conservative result), using a total beam setback of $\frac{1}{2}$ in. $+ \frac{1}{4}$ in. $= \frac{3}{4}$ in. (the $\frac{1}{4}$ in. is included to account for mill underrun):

$$l = 14\frac{1}{2} \text{ in.}$$

$$kl = 3\frac{1}{2} \text{ in.} - \frac{3}{4} \text{ in.}$$
$$= 2.75 \text{ in.}$$

$$k = \frac{kl}{l}$$
$$= \frac{2.75 \text{ in.}}{14\frac{1}{2} \text{ in.}}$$
$$= 0.190$$

$$x = 0.0269 \text{ by interpolation}$$

$$al = 3\frac{1}{2} \text{ in.} - xl$$
$$= 3\frac{1}{2} \text{ in.} - 0.0269(14\frac{1}{2} \text{ in.})$$
$$= 3.11 \text{ in.}$$

$$a = \frac{al}{l}$$
$$= \frac{3.11 \text{ in.}}{14\frac{1}{2} \text{ in.}}$$
$$= 0.214$$

$$C = 2.69 \text{ by interpolation}$$

---

# IIA-57

The required weld size is determined using AISC *Manual* Equation 8-30, as follows:

| LRFD | ASD |
|------|-----|
| $D_{min} = \frac{R_u}{\phi CC_1l}$ | $D_{min} = \frac{\Omega R_a}{CC_1l}$ |
| $= \frac{96.0 \text{ kips}}{0.75(2.69)(1)(14\frac{1}{2} \text{ in.})(2 \text{ sides})}$ | $= \frac{2.00(64.0 \text{ kips})}{2.69(1)(14\frac{1}{2} \text{ in.})(2 \text{ sides})}$ |
| $= 1.64 \text{ sixteenths}$ | $= 1.64 \text{ sixteenths}$ |

Use a $\frac{3}{16}$ in. fillet weld (minimum size from AISC *Specification* Table J2.4).

*Beam Web Strength at Fillet Weld*

The minimum beam web thickness required to match the shear rupture strength of a weld on both sides to that of the base metal is:

$$t_{min} = \frac{6.19D_{min}}{F_u}$$
(from *Manual* Eq. 9-7)
$$= \frac{6.19(1.64)}{65 \text{ ksi}}$$
$$= 0.156 \text{ in.} < 0.355 \text{ in.} \quad \text{o.k.}$$

*Shear Strength of Angles*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the angles is determined as follows:

$$A_{gv} = (2 \text{ angles})lt$$
$$= (2 \text{ angles})(14\frac{1}{2} \text{ in.})(\frac{1}{2} \text{ in.})$$
$$= 14.5 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$
(*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(14.5 \text{ in.}^2)$$
$$= 435 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
| $\phi R_n = 1.00(435 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{435 \text{ kips}}{1.50}$ |
| $= 435 \text{ kips} > 96.0 \text{ kips} \quad \text{o.k.}$ | $= 290 \text{ kips} > 64.0 \text{ kips} \quad \text{o.k.}$ |

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the angle is determined as follows. The effective net area is determined in accordance with AISC *Specification* Section B4.3b.

$$A_{nv} = (2 \text{ angles})[l - n(d_h + \frac{1}{16} \text{ in.})]t$$
$$= (2 \text{ angles})[14\frac{1}{2} \text{ in.} - 5(\frac{15}{16} \text{ in.} + \frac{1}{16} \text{ in.})](\frac{1}{2} \text{ in.})$$
$$= 9.50 \text{ in.}^2$$

---

# IIA-58

$$R_n = 0.60F_u A_{nv}$$
(*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(9.50 \text{ in.}^2)$$
$$= 371 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(371 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{371 \text{ kips}}{2.00}$ |
| $= 278 \text{ kips} > 96.0 \text{ kips} \quad \text{o.k.}$ | $= 186 \text{ kips} > 64.0 \text{ kips} \quad \text{o.k.}$ |

*Tensile Strength of Angles—Beam Web Side*

From AISC *Specification* Section J4.1(a), the available tensile yielding strength of the angles is determined as follows:

$$A_g = (2 \text{ angles})lt$$
$$= (2 \text{ angles})(14\frac{1}{2} \text{ in.})(\frac{1}{2} \text{ in.})$$
$$= 14.5 \text{ in.}^2$$

$$R_n = F_y A_g$$
(*Spec.* Eq. J4-1)
$$= (50 \text{ ksi})(14.5 \text{ in.}^2)$$
$$= 725 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
| $\phi R_n = 0.90(725 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{725 \text{ kips}}{1.67}$ |
| $= 653 \text{ kips} > 60 \text{ kips} \quad \text{o.k.}$ | $= 434 \text{ kips} > 40 \text{ kips} \quad \text{o.k.}$ |

From AISC *Specification* Sections J4.1(b), the available tensile rupture strength of the angles is determined as follows:

$$R_n = F_u A_e$$
(*Spec.* Eq. J4-2)

Because the angle legs are welded to the beam web there is no bolt hole reduction and $A_e = A_g$; therefore, tensile rupture will not control.

*Block Shear Rupture Strength of Angles–Outstanding Legs*

The nominal strength for the limit state of block shear rupture of the angles assuming an L-shaped tearout relative to shear load, is determined as follows. The tearout pattern is shown in Figure II.A-2B-2.

$$R_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$
(*Spec.* Eq. J4-5)

where

---

# IIA-59

$$l_{eh} = \frac{2(angle\ leg) + t_w - gage}{2}$$
$$= \frac{2(4 \text{ in.}) + 0.355 \text{ in.} - 5\frac{1}{2} \text{ in.}}{2}$$
$$= 1.43 \text{ in.}$$

$$A_{nt} = (2 \text{ angles})[l_{eh} - 0.5(d_h + \frac{1}{16} \text{ in.})](t)$$
$$= (2 \text{ angles})[1.43 \text{ in.} - 0.5(\frac{15}{16}\text{in.} + \frac{1}{16} \text{ in.})](\frac{1}{2} \text{ in.})$$
$$= 0.930 \text{ in.}^2$$

$$A_{gv} = (2 \text{ angles})[l_{ev} + (n-1)s](t)$$
$$= (2 \text{ angles})[1\frac{1}{4} \text{ in.} + (5-1)(3 \text{ in.})](\frac{1}{2} \text{ in.})$$
$$= 13.3 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (2 \text{ angles})(n - 0.5)(d_h + \frac{1}{16} \text{ in.})(t)$$
$$= 13.3 \text{ in.}^2 - (2 \text{ angles})(5 - 0.5)(\frac{15}{16} \text{ in.} + \frac{1}{16} \text{ in.})(\frac{1}{2} \text{ in.})$$
$$= 8.80 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_n = 0.60(65 \text{ ksi})(8.80 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.930 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(13.3 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.930 \text{ in.}^2)$$
$$= 404 \text{ kips} < 459 \text{ kips}$$

Therefore:

$$R_n = 404 \text{ kips}$$

<div style="text-align: center;">
<img src="block_shear_diagram" alt="Diagram showing block shear rupture of outstanding legs of angles with:
- Cross-sectional view showing both angle legs with V/2 forces
- Hatched areas indicating failure paths
- 4 @ 3" = 12" vertical spacing
- 5½" gage dimension
- 1¼" top and bottom edge distances">
</div>

*Fig. II.A-2B-2. Block shear rupture of outstanding legs of angles.*

---

# IIA-60

The available block shear rupture strength of the angles is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(404 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{404 \text{ kips}}{2.00}$ |
| $= 303 \text{ kips} > 75 \text{ kips} \quad \text{o.k.}$ | $= 202 \text{ kips} > 50 \text{ kips} \quad \text{o.k.}$ |

*Shear Strength of Beam*

From AISC *Specification* Section J4.2(a), the available shear yield strength of the beam web is determined as follows:

$$A_{gv} = dt_w$$
$$= (18.0 \text{ in.})(0.355 \text{ in.})$$
$$= 6.39 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$
(*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(6.39 \text{ in.}^2)$$
$$= 192 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
| $\phi R_n = 1.00(192 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{192 \text{ kips}}{1.50}$ |
| $= 192 \text{ kips} > 75 \text{ kips} \quad \text{o.k.}$ | $= 128 \text{ kips} > 50 \text{ kips} \quad \text{o.k.}$ |

The limit state of shear rupture of the beam web does not apply in this example because the beam is uncoped.

*Block Shear Rupture Strength of Beam Web*

Assuming a U-shaped tearout along the weld relative to the axial load, and a total beam setback of ¾ in. (includes ¼ in. tolerance to account for possible mill underrun), the nominal block shear rupture strength is determined as follows.

$$R_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$
(*Spec.* Eq. J4-5)

where

$$A_{nt} = lt_w$$
$$= (14\frac{1}{2} \text{ in.})(0.355 \text{ in.})$$
$$= 5.15 \text{ in.}^2$$

$$A_{gv} = (2)(leg - setback)t_w$$
$$= (2)(3\frac{1}{2} \text{ in.} - \frac{3}{4} \text{ in.})(0.355 \text{ in.})$$
$$= 1.95 \text{ in.}^2$$

Because the angles are welded and there is no reduction for bolt holes:

---

# IIA-61

$$A_{nv} = A_{gv}$$
$$= 1.95 \text{ in.}^2$$

$$U_{bs} = 1$$

and

$$R_n = 0.60(65 \text{ ksi})(1.95 \text{ in.}^2) + 1.0(65 \text{ ksi})(5.15 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(1.95 \text{ in.}^2) + 1.0(65 \text{ ksi})(5.15 \text{ in.}^2)$$
$$= 411 \text{ kips} > 393 \text{ kips}$$

Therefore:

$$R_n = 393 \text{ kips}$$

The available block shear rupture strength of the web is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(393 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{393 \text{ kips}}{2.00}$ |
| $= 295 \text{ kips} > 60 \text{ kips} \quad \text{o.k.}$ | $= 197 \text{ kips} > 40 \text{ kips} \quad \text{o.k.}$ |

*Tensile Strength of Beam*

From AISC *Specification* Section J4.1(a), the available tensile yielding strength of the beam is determined from AISC *Specification* Equation J4-1:

$$R_n = F_y A_g$$
(*Spec.* Eq. J4-1)
$$= (50 \text{ ksi})(14.7 \text{ in.}^2)$$
$$= 735 \text{ kips}$$

The available tensile yielding strength of the beam is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
| $\phi R_n = 0.90(735 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{735 \text{ kips}}{1.67}$ |
| $= 662 \text{ kips} > 60 \text{ kips} \quad \text{o.k.}$ | $= 440 \text{ kips} > 40 \text{ kips} \quad \text{o.k.}$ |

From AISC *Specification* Section J4.1(b), determine the available tensile rupture strength of the beam. The effective net area is $A_e = A_nU$, where $U$ is determined from AISC *Specification* Table D3.1, Case 2. The value of $\bar{x}$ is determined by treating the W-shape as two channels back-to-back and finding the horizontal distance to the center of gravity of one of the channels from the centerline of the beam. (Note that the fillets are ignored.)

---

# IIA-62

$$\bar{x} = \frac{\Sigma(A\bar{x})}{\Sigma A}$$
$$= \frac{\left(\frac{t_w}{2}\right)(d - 2t_f)\left(\frac{t_w/2}{2}\right) + 2t_f\left(\frac{b_f}{2}\right)\left(\frac{b_f/2}{2}\right)}{\left(\frac{A_g}{2}\right)}$$
$$= \frac{\left(\frac{0.355 \text{ in.}}{2}\right)[18.0 \text{ in.} - 2(0.570 \text{ in.})]\left(\frac{0.355 \text{ in.}/2}{2}\right) + 2(0.570 \text{ in.})\left(\frac{7.50 \text{ in.}}{2}\right)\left(\frac{7.50 \text{ in.}/2}{2}\right)}{\left(\frac{14.7 \text{ in.}^2}{2}\right)}$$
$$= 1.13 \text{ in.}$$

The connection length, $l$, used in the determination of $U$ will be reduced by ¼ in. to account for possible mill underrun. The shear lag factor, $U$, is:

$$U = 1 - \frac{\bar{x}}{l}$$
$$= 1 - \frac{1.13 \text{ in.}}{(3 \text{ in.} - \frac{1}{4} \text{ in.})}$$
$$= 0.589$$

The minimum value of $U$ can be determined from AISC *Specification* Section D3, where $U$ is the ratio of the gross area of the connected element to the member gross area.

$$U = \frac{A_{wt}}{A_g}$$
$$= \frac{(d - 2t_f)t_w}{A_g}$$
$$= \frac{[18.0 \text{ in.} - 2(0.570 \text{ in.})](0.355 \text{ in.})}{14.7 \text{ in.}^2}$$
$$= 0.407$$

AISC *Specification* Table D3.1, Case 2, controls; use $U = 0.589$. Because the angles are welded and there is no reduction for bolt holes:

$$A_n = A_g$$
$$= 14.7 \text{ in.}^2$$

$$A_e = A_nU$$
(*Spec.* Eq. D3-1)
$$= (14.7 \text{ in.}^2)(0.589)$$
$$= 8.66 \text{ in.}^2$$

$$R_n = F_u A_e$$
(*Spec.* Eq. J4-2)
$$= (65 \text{ ksi})(8.66 \text{ in.}^2)$$
$$= 563 \text{ kips}$$

---

# IIA-63

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(563 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{563 \text{ kips}}{2.00}$ |
| $= 422 \text{ kips} > 60 \text{ kips} \quad \text{o.k.}$ | $= 282 \text{ kips} > 40 \text{ kips} \quad \text{o.k.}$ |

*Conclusion*

The connection is found to be adequate as given for the applied loads.

---

# IIA-64

# EXAMPLE II.A-3 ALL-WELDED DOUBLE-ANGLE CONNECTION

## Given:

Repeat Example II.A-1A using AISC *Manual* Table 10-3 and applicable provisions from the AISC *Specification* to verify the strength of an all-welded double-angle connection between an ASTM A992/A992M W36×231 beam and an ASTM A992/A992M W14×90 column flange, as shown in Figure II.A-3-1. Use 70-ksi electrodes and ASTM A572/A572M Grade 50 angles.

<div style="text-align: center;">
<img src="connection_detail" alt="Connection diagram showing:
- Front view: 2'-0" height, ½" dimension at top
- Section A-A showing ½" return at top (typ.), ⅜₁₆ weld size
- W36×231 beam
- W14×90 column
- 2L4×3½×⅝/₁₆ × 2'-0" (SLBB) angles">
</div>

*Fig. II.A-3-1. Connection geometry for Example II.A-3.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam and column
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

Angles
ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W36×231
$t_w = 0.760$ in.

Column
W14×90
$t_f = 0.710$ in.

---

# IIA-65

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(37.5 \text{ kips}) + 1.6(113 \text{ kips})$ | $R_a = 37.5 \text{ kips} + 113 \text{ kips}$ |
| $= 226 \text{ kips}$ | $= 151 \text{ kips}$ |

*Design of Weld between Beam Web and Angles*

Use AISC *Manual* Table 10-3 (Welds A). Try $\frac{3}{16}$ in. weld size, $l = 24$ in.

| LRFD | ASD |
|------|-----|
| $\phi R_n = 257 \text{ kips} > 226 \text{ kips} \quad \text{o.k.}$ | $\frac{R_n}{\Omega} = 171 \text{ kips} > 151 \text{ kips} \quad \text{o.k.}$ |

From AISC *Manual* Table 10-3, the minimum beam web thickness is:

$$t_{w\ min} = 0.286 \text{ in.} < 0.760 \text{ in.} \quad \text{o.k.}$$

*Design of Weld between Column Flange and Angles*

Use AISC *Manual* Table 10-3 (Welds B). Try ¼ in. weld size, $l = 24$ in.

| LRFD | ASD |
|------|-----|
| $\phi R_n = 260 \text{ kips} > 226 \text{ kips} \quad \text{o.k.}$ | $\frac{R_n}{\Omega} = 173 \text{ kips} > 151 \text{ kips} \quad \text{o.k.}$ |

From AISC *Manual* Table 10-3, the minimum column flange thickness is:

$$t_{f\ min} = 0.190 \text{ in.} < 0.710 \text{ in.} \quad \text{o.k.}$$

*Angle Thickness*

Minimum angle thickness for weld from AISC *Specification* Section J2.2b:

$$t_{min} = w + \frac{1}{16} \text{ in.}$$
$$= \frac{1}{4} \text{ in.} + \frac{1}{16} \text{ in.}$$
$$= \frac{5}{16} \text{ in.}$$

Try 2L4×3½×⅝/₁₆ (SLBB).

*Shear Strength of Angles*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the angles is determined as follows:

$$A_{gv} = (2 \text{ angles})lt$$
$$= (2 \text{ angles})(24 \text{ in.})(\frac{5}{16} \text{ in.})$$
$$= 15.0 \text{ in.}^2$$

---

# IIA-66

$$R_n = 0.60F_y A_{gv}$$
(*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(15.0 \text{ in.}^2)$$
$$= 450 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
| $\phi R_n = 1.00(450 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{450 \text{ kips}}{1.50}$ |
| $= 450 \text{ kips} > 226 \text{ kips} \quad \text{o.k.}$ | $= 300 \text{ kips} > 151 \text{ kips} \quad \text{o.k.}$ |

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the angles is determined as follows:

$$A_{nv} = (2 \text{ angles})lt$$
$$= (2 \text{ angles})(24 \text{ in.})(\frac{5}{16} \text{ in.})$$
$$= 15.0 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$
(*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(15.0 \text{ in.}^2)$$
$$= 585 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(585 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{585 \text{ kips}}{2.00}$ |
| $= 439 \text{ kips} > 226 \text{ kips} \quad \text{o.k.}$ | $= 293 \text{ kips} > 151 \text{ kips} \quad \text{o.k.}$ |

*Conclusion*

The connection is found to be adequate as given for the applied loads.

---

# IIA-67

# EXAMPLE II.A-4 ALL-BOLTED DOUBLE-ANGLE CONNECTION IN A COPED BEAM

## Given:

Use AISC *Manual* Table 10-1 to verify the available strength of an all-bolted double-angle connection between an ASTM A992/A992M W18×50 beam and an ASTM A992/A992M W21×62 girder web, as shown in Figure II.A-4-1, to support the following beam end reactions:

$$R_D = 10 \text{ kips}$$
$$R_L = 30 \text{ kips}$$

The beam top flange cope is 2 in. deep by 4 in. long, $l_{ev} = 1\frac{1}{4}$ in., $l_{eh} = 1\frac{5}{8}$ in. Use ASTM A572/A572M Grade 50 angles.

<div style="text-align: center;">
<img src="connection_detail" alt="Detailed connection diagram showing:
- Front view with dimensions: ½", 6 = 4", 2¼", 1⅝", cope details
- Vertical spacing: 2 @ 3" = 6", 1⅜"
- Section A-A showing ¾" dia. Group 120 bolts, thread condition N, std. holes
- 2L5×3½×¾ × 0'-8½" (SLBB) angles
- W18×50 beam
- Girder web thickness and related dimensions
- Note about entering and tightening clearances from AISC Manual Table 7-15">
</div>

*Fig. II.A-4-1. Connection geometry for Example II.A-4.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam and girder
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

Angles
ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

From AISC *Manual* Table 1-1 the geometric properties are as follows:

Beam
W18×50
$d = 18.0$ in.
$t_w = 0.355$ in.

---

# IIA-68

Girder
W21×62
$t_w = 0.400$ in.

From AISC *Specification* Table J3.3, the hole diameter of a ¾-in.-diameter bolt in a standard hole is:

$$d_h = \frac{13}{16} \text{ in.}$$

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(10 \text{ kips}) + 1.6(30 \text{ kips})$ | $R_a = 10 \text{ kips} + 30 \text{ kips}$ |
| $= 60.0 \text{ kips}$ | $= 40.0 \text{ kips}$ |

*Connection Design*

Tabulated values in AISC *Manual* Table 10-1a consider the limit states of shear yielding of the angles, shear rupture of the angles, and block shear rupture of the angles.

Try 3 rows of bolts and 2L5×3½×¼ (SLBB).

| LRFD | ASD |
|------|-----|
| $\phi R_n = 85.9 \text{ kips} > 60.0 \text{ kips} \quad \text{o.k.}$ | $\frac{R_n}{\Omega} = 57.3 \text{ kips} > 40.0 \text{ kips} \quad \text{o.k.}$ |

*Shear Transfer Strength at Bolt Holes at Beam Web*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength determined in accordance with AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the angles at the bolt hole determined in accordance with AISC *Specification* Section J3.11a, and (3) the available bearing or tearout strength of the beam web or support element at the bolt hole determined in accordance with AISC *Specification* Section J3.11a.

From AISC *Manual* Table 10-1b, the available bolt shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9 \text{ kips}$ | $\frac{r_n}{\Omega} = 11.9 \text{ kips}$ |

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the angle per bolt for ¾-in.-diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): | For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): |
| $\phi r_n = (49.4 \text{ kip/in.})(\frac{1}{4} \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kip/in.})(\frac{1}{4} \text{ in.})$ |
| $= 12.4 \text{ kips}$ | $= 8.23 \text{ kips}$ |

---

# IIA-69

| LRFD | ASD |
|------|-----|
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kip/in.})(\frac{1}{4} \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(\frac{1}{4} \text{ in.})$ |
| $= 22.0 \text{ kips}$ | $= 14.6 \text{ kips}$ |

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the beam web per bolt for ¾-in.-diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): | For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): |
| $\phi r_n = (49.4 \text{ kip/in.})(0.355 \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kip/in.})(0.355 \text{ in.})$ |
| $= 17.5 \text{ kips}$ | $= 11.7 \text{ kips}$ |
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kip/in.})(0.355 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(0.355 \text{ in.})$ |
| $= 31.2 \text{ kips}$ | $= 20.8 \text{ kips}$ |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by two because the bolts are in double shear), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by two there are are two angles), and the available bearing and tearout strength of the beam web for an edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min\begin{Bmatrix} 17.9 \text{ kips}(2) = 35.8 \text{ kips,} \\ 22.0 \text{ kips}(2) = 44.0 \text{ kips,} \\ 17.5 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips}(2) = 23.8 \text{ kips,} \\ 14.6 \text{ kips}(2) = 29.2 \text{ kips,} \\ 11.7 \text{ kips} \end{Bmatrix}$ |
| $= 17.5 \text{ kips}$ | $= 11.7 \text{ kips}$ |

At the middle connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by two because the bolts are in double shear), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by two because there are two angles), and the available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,mid} = \min\begin{Bmatrix} 17.9 \text{ kips}(2) = 35.8 \text{ kips,} \\ 22.0 \text{ kips}(2) = 44.0 \text{ kips,} \\ 31.2 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,mid}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips}(2) = 23.8 \text{ kips,} \\ 14.6 \text{ kips}(2) = 29.2 \text{ kips,} \\ 20.8 \text{ kips} \end{Bmatrix}$ |
| $= 31.2 \text{ kips}$ | $= 20.8 \text{ kips}$ |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by two because the bolts are in double shear), the available bearing and tearout strength of the angles for an edge bolt (multiplied by two because there are two angles), and the available bearing and tearout strength of the beam web for a non-edge bolt:

---

# IIA-70

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min\begin{Bmatrix} 17.9 \text{ kips}(2) = 35.8 \text{ kips,} \\ 12.4 \text{ kips}(2) = 24.8 \text{ kips,} \\ 31.2 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips}(2) = 23.8 \text{ kips,} \\ 8.23 \text{ kips}(2) = 16.5 \text{ kips,} \\ 20.8 \text{ kips} \end{Bmatrix}$ |
| $= 24.8 \text{ kips}$ | $= 16.5 \text{ kips}$ |

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi r_{n,top} + \phi r_{n,mid}(n-2) + \phi r_{n,bot}$ | $\frac{R_n}{\Omega} = \frac{r_{n,top}}{\Omega} + \frac{r_{n,mid}}{\Omega}(n-2) + \frac{r_{n,bot}}{\Omega}$ |
| $= 17.5 \text{ kips} + (31.2 \text{ kips})(3-2) + 24.8 \text{ kips}$ | $= 11.7 \text{ kips} + (20.8 \text{ kips})(3-2) + 16.5 \text{ kips}$ |
| $= 73.5 \text{ kips} > 60.0 \text{ kips} \quad \text{o.k.}$ | $= 49.0 \text{ kips} > 40.0 \text{ kips} \quad \text{o.k.}$ |

*Shear Transfer Strength at Bolt Holes at Girder Web*

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the girder web per bolt for ¾-in.-diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kip/in.})(0.400 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(0.400 \text{ in.})$ |
| $= 35.1 \text{ kips}$ | $= 23.4 \text{ kips}$ |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because there are two bolts per row), the available bearing and tearout strength of the angles for an edge bolt (multiplied by 2 because there are two angles), and the available bearing and tearout strength of the girder web (multiplied by 2 because there are two bolts per row):

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min\begin{Bmatrix} 17.9 \text{ kips}(2) = 35.8 \text{ kips,} \\ 12.4 \text{ kips}(2) = 24.8 \text{ kips,} \\ 35.1 \text{ kips}(2) = 70.2 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips}(2) = 23.8 \text{ kips,} \\ 8.23 \text{ kips}(2) = 16.5 \text{ kips,} \\ 23.4 \text{ kips}(2) = 46.8 \text{ kips} \end{Bmatrix}$ |
| $= 24.8 \text{ kips}$ | $= 16.5 \text{ kips}$ |

At the middle connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because there are two bolts per row), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by 2 because there are two angles), and the available bearing and tearout strength of the girder web (multiplied by 2 because there are two bolts per row):

| LRFD | ASD |
|------|-----|
| $\phi r_{n,mid} = \min\begin{Bmatrix} 17.9 \text{ kips}(2) = 35.8 \text{ kips,} \\ 22.0 \text{ kips}(2) = 44.0 \text{ kips,} \\ 35.1 \text{ kips}(2) = 70.2 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,mid}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips}(2) = 23.8 \text{ kips,} \\ 14.6 \text{ kips}(2) = 29.2 \text{ kips,} \\ 23.4 \text{ kips}(2) = 46.8 \text{ kips} \end{Bmatrix}$ |
| $= 35.8 \text{ kips}$ | $= 23.8 \text{ kips}$ |

---

# IIA-71

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because there are two bolts per row), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by 2 because there are two angles), and the available bearing and tearout strength of the girder web (multiplied by 2 because there are two bolts per row):

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min\begin{Bmatrix} 17.9 \text{ kips}(2) = 35.8 \text{ kips,} \\ 22.0 \text{ kips}(2) = 44.0 \text{ kips,} \\ 35.1 \text{ kips}(2) = 70.2 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips}(2) = 23.8 \text{ kips,} \\ 14.6 \text{ kips}(2) = 29.2 \text{ kips,} \\ 23.4 \text{ kips}(2) = 46.8 \text{ kips} \end{Bmatrix}$ |
| $= 35.8 \text{ kips}$ | $= 23.8 \text{ kips}$ |

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi r_{n,top} + \phi r_{n,mid}(n-2) + \phi r_{n,bot}$ | $\frac{R_n}{\Omega} = \frac{r_{n,top}}{\Omega} + \frac{r_{n,mid}}{\Omega}(n-2) + \frac{r_{n,bot}}{\Omega}$ |
| $= 24.8 \text{ kips} + (35.8 \text{ kips})(3-2) + 35.8 \text{ kips}$ | $= 16.5 \text{ kips} + (23.8 \text{ kips})(3-2) + 23.8 \text{ kips}$ |
| $= 96.4 \text{ kips} > 60.0 \text{ kips} \quad \text{o.k.}$ | $= 64.1 \text{ kips} > 40.0 \text{ kips} \quad \text{o.k.}$ |

*Coped Beam Strength*

From AISC *Manual* Part 9, the available coped beam web strength is the lesser of the limit states of flexural local web buckling, shear yielding, shear rupture, block shear rupture, and the sum of the effective strengths of the individual fasteners. From the User Note in AISC *Specification* Section J3.7, the effective strength of an individual fastener is the lesser of the fastener shear strength, the bearing strength at the bolt holes, and the tearout strength at the bolt holes.

*Flexural local web buckling of beam web*

As shown in AISC *Manual* Figure 9-2, the cope dimensions are:

$$c = 4 \text{ in.}$$

$$d_c = 2.00 \text{ in.}$$

$$e = c + setback$$
$$= 4 \text{ in.} + \frac{1}{2} \text{ in.}$$
$$= 4.50 \text{ in.}$$

$$h_o = d - d_c$$
$$= 18.0 \text{ in.} - 2.00 \text{ in.}$$
$$= 16.0 \text{ in.}$$

$$\frac{c}{d} = \frac{4 \text{ in.}}{18.0 \text{ in.}}$$
$$= 0.222$$

$$\frac{c}{h_o} = \frac{4 \text{ in.}}{16.0 \text{ in.}}$$
$$= 0.250$$

---

# IIA-72

Because $\frac{c}{d} \leq 1.0$ :

$$f = 2\left(\frac{c}{d}\right)$$
(*Manual* Eq. 9-20a)
$$= 2(0.222)$$
$$= 0.444$$

Because $\frac{c}{h_o} \leq 1.0$ :

$$k = 2.2\left(\frac{h_o}{c}\right)^{1.65}$$
(*Manual* Eq. 9-19a)
$$= 2.2\left(\frac{16.0 \text{ in.}}{4 \text{ in.}}\right)^{1.65}$$
$$= 21.7$$

$$\lambda = \frac{h_o}{t_w}$$
(*Manual* Eq. 9-17)
$$= \frac{16.0 \text{ in.}}{0.355 \text{ in.}}$$
$$= 45.1$$

$$k_1 = fk \geq 1.61$$
(*Manual* Eq. 9-14)
$$= (0.444)(21.7) \geq 1.61$$
$$= 9.63$$

$$\lambda_p = 0.475\sqrt{\frac{k_1E}{F_y}}$$
(*Manual* Eq. 9-18)
$$= 0.475\sqrt{\frac{(9.63)(29,000 \text{ ksi})}{50 \text{ ksi}}}$$
$$= 35.5$$

$$2\lambda_p = 2(35.5)$$
$$= 71.0$$

Because $\lambda_p < \lambda \leq 2\lambda_p$, calculate the nominal flexural strength using AISC *Manual* Equation 9-11.

The plastic section modulus of the coped section, $Z_c$, is determined from AISC *Manual* Table 9-2b.

$$Z_c = 42.5 \text{ in.}^3$$

$$M_p = F_yZ_c$$
(*Manual* Eq. 9-15)
$$= (50 \text{ ksi})(42.5 \text{ in.}^3)$$
$$= 2,130 \text{ kip-in.}$$

---

# IIA-73

From AISC *Manual* Table 9-2a:

$$S_c = 23.4 \text{ in.}^3$$

$$M_y = F_yS_c$$
(*Manual* Eq. 9-16)
$$= (50 \text{ ksi})(23.4 \text{ in.}^3)$$
$$= 1,170 \text{ kip-in.}$$

$$M_n = M_p - (M_p - M_y)\left(\frac{\lambda}{\lambda_p} - 1\right)$$
(*Manual* Eq. 9-11)
$$= (2,130 \text{ kip-in.}) - (2,130 \text{ kip-in.} - 1,170 \text{ kip-in.})\left(\frac{45.1}{35.5} - 1\right)$$
$$= 1,870 \text{ kip-in.}$$

$$R_n = \frac{M_n}{e}$$
(from *Manual* Eq. 9-9)
$$= \frac{1,870 \text{ kip-in.}}{4.50 \text{ in.}}$$
$$= 416 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
| $\phi R_n = 0.90(416 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{416 \text{ kips}}{1.67}$ |
| $= 374 \text{ kips} > 60.0 \text{ kips} \quad \text{o.k.}$ | $= 249 \text{ kips} > 40.0 \text{ kips} \quad \text{o.k.}$ |

*Shear Strength of Beam Web*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the beam web is determined as follows:

$$A_{gv} = h_ot_w$$
$$= (16.0 \text{ in.})(0.355 \text{ in.})$$
$$= 5.68 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$
(*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(5.68 \text{ in.}^2)$$
$$= 170 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
| $\phi R_n = 1.00(170 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{170 \text{ kips}}{1.50}$ |
| $= 170 \text{ kips} > 60.0 \text{ kips} \quad \text{o.k.}$ | $= 113 \text{ kips} > 40.0 \text{ kips} \quad \text{o.k.}$ |

---

# IIA-74

Because the beam is coped at the top flange only, the limit state of shear rupture does not apply.

*Block Shear Rupture of Beam Web*

From AISC *Specification* Section J4.3, the block shear rupture strength of the beam web, assuming a total beam setback of ¾ in. (includes ¼ in. tolerance to account for possible mill underrun), is determined as follows.

$$R_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$
(*Spec.* Eq. J4-5)

where

$$A_{gv} = (l_{ev} + 2s)t_w$$
$$= [1\frac{1}{4} \text{ in.} + 2(3.00 \text{ in.})](0.355 \text{ in.})$$
$$= 2.57 \text{ in.}^2$$

$$A_{nv} = A_{gv} - 2.5(d_h + \frac{1}{16} \text{ in.})t_w$$
$$= 2.57 \text{ in.}^2 - 2.5(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.})(0.355 \text{ in.})$$
$$= 1.79 \text{ in.}^2$$

$$A_{nt} = [l_{eh} - \frac{1}{4} \text{ in.(underrun)} - 0.5(d_h + \frac{1}{16} \text{ in.})]t_w$$
$$= [1\frac{5}{8} \text{ in.} - \frac{1}{4} \text{ in.(underrun)} - 0.5(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.})](0.355 \text{ in.})$$
$$= 0.333 \text{ in.}^2$$

The block shear reduction coefficient, $U_{bs}$, is 1.0 for a single row beam end connection as illustrated in AISC *Specification* Commentary Figure C-J4.2.

$$R_n = 0.60(65 \text{ ksi})(1.79 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.333 \text{ in.}^2) < 0.60(50 \text{ ksi})(2.57 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.333 \text{ in.}^2)$$
$$= 91.5 \text{ kips} \leq 98.7 \text{ kips}$$

Therefore:
$$R_n = 91.5 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(91.5 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{91.5 \text{ kips}}{2.00}$ |
| $= 68.6 \text{ kips} > 60.0 \text{ kips} \quad \text{o.k.}$ | $= 45.8 \text{ kips} > 40.0 \text{ kips} \quad \text{o.k.}$ |

*Conclusion*

The available shear strength of the connection is controlled by the available block shear rupture of the beam web.

| LRFD | ASD |
|------|-----|
| $\phi R_n = 68.6 \text{ kips} > 60.0 \text{ kips} \quad \text{o.k.}$ | $\frac{R_n}{\Omega} = 45.8 \text{ kips} > 40.0 \text{ kips} \quad \text{o.k.}$ |

The connection is found to be adequate as given for the applied loads.

---

# IIA-75

# EXAMPLE II.A-5 WELDED/BOLTED DOUBLE-ANGLE CONNECTION IN A COPED BEAM

## Given:

Use AISC *Manual* Table 10-2 to verify the available strength of a double angle shear connection welded to an ASTM A992/A992M W18×50 beam and bolted to an ASTM A992/A992M W21×62 girder web, as shown in Figure II.A-5-1. Use 70-ksi electrodes and ASTM A572/A572M Grade 50 angles. The connection supports the following beam end reactions:

$$R_D = 10 \text{ kips}$$
$$R_L = 30 \text{ kips}$$

<div style="text-align: center;">
<img src="connection_detail" alt="Detailed connection diagram showing:
- Front view with dimensions: ½", G = 4", cope details
- Vertical spacing: 2 @ 6" = 6", dimensions 1⅜", 1⅝"
- Section A-A showing ¾" dia. Group 120 bolts, thread condition N, std. holes
- Weld sizes: ⅜₁₆, ⅜₁₆
- 2L4×3½×¼ × 0'-8½" (SLBB) angles
- W18×50 beam
- d_c = 2.00", l_ev = 1⅝"
- Note about decimal web thickness rounding">
</div>

*Fig. II.A-5-1. Connection geometry for Example II.A-5.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam and girder
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

Angles
ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

From AISC *Manual* Tables 1-1, the geometric properties are as follows:

Beam
W18×50
$d = 18.0$ in.
$t_w = 0.355$ in.

---

# IIA-76

Girder
W21×62
$t_w = 0.400$ in.

From AISC *Specification* Table J3.3, the hole diameter of a ¾-in.-diameter bolt in a standard hole is:

$$d_h = \frac{13}{16} \text{ in.}$$

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(10 \text{ kips}) + 1.6(30 \text{ kips})$ | $R_a = 10 \text{ kips} + 30 \text{ kips}$ |
| $= 60.0 \text{ kips}$ | $= 40.0 \text{ kips}$ |

*Weld Design*

Use AISC *Manual* Table 10-2 (Welds A). Try $\frac{3}{16}$ in. weld size, $l = 8\frac{1}{2}$ in.

| LRFD | ASD |
|------|-----|
| $\phi R_n = 110 \text{ kips} > 60.0 \text{ kips} \quad \text{o.k.}$ | $\frac{R_n}{\Omega} = 73.5 \text{ kips} > 40.0 \text{ kips} \quad \text{o.k.}$ |

From AISC *Manual* Table 10-2, the minimum beam web thickness is:

$$t_{w\ min} = 0.286 \text{ in.} < 0.355 \text{ in.} \quad \text{o.k.}$$

*Minimum Angle Thickness for Weld*

From AISC *Specification* Section J2.2b, the minimum angle thickness is:

$$t_{min} = w + \frac{1}{16} \text{ in.}$$
$$= \frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.}$$
$$= \frac{1}{4} \text{ in.}$$

*Connection Design*

Tabulated values in AISC *Manual* Table 10-1a consider the limit states of shear yielding of the angles, shear rupture of the angles, and block shear rupture of the angles.

Try 3 rows of bolts and 2L4×3½×¼ (SLBB).

| LRFD | ASD |
|------|-----|
| $\phi R_n = 85.9 \text{ kips} > 60.0 \text{ kips} \quad \text{o.k.}$ | $\frac{R_n}{\Omega} = 57.3 \text{ kips} > 40.0 \text{ kips} \quad \text{o.k.}$ |

*Shear Transfer Strength at Bolt Holes at Girder Web*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength determined in accordance with AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the angles at the bolt hole determined in accordance with AISC *Specification* Section J3.11a, and (3) the available bearing or tearout strength of the girder web at the bolt hole determined in accordance with AISC *Specification* Section J3.11a.

---

# IIA-77

From AISC *Manual* Table 10-1b, the available bolt shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9 \text{ kips}$ | $\frac{r_n}{\Omega} = 11.9 \text{ kips}$ |

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the angle per bolt for ¾-in.-diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): | For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): |
| $\phi r_n = (49.4 \text{ kip/in.})(\frac{1}{4} \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kip/in.})(\frac{1}{4} \text{ in.})$ |
| $= 12.4 \text{ kips}$ | $= 8.23 \text{ kips}$ |
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kip/in.})(\frac{1}{4} \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(\frac{1}{4} \text{ in.})$ |
| $= 22.0 \text{ kips}$ | $= 14.6 \text{ kips}$ |

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the girder web per bolt for ¾-in.-diameter bolts in standard holes is determined as follows. The non-edge bolt strength is used for all bolts in the girder web.

| LRFD | ASD |
|------|-----|
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kip/in.})(0.400 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(0.400 \text{ in.})$ |
| $= 35.1 \text{ kips}$ | $= 23.4 \text{ kips}$ |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by two because there are two columns of bolts), the available bearing and tearout strength of the angles for an edge bolt (multiplied by two because there are two columns of bolts), and the available bearing and tearout strength of the girder web for a non-edge bolt (multiplied by two because there are two columns of bolts):

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min\begin{Bmatrix} 17.9 \text{ kips}(2) = 35.8 \text{ kips,} \\ 12.4 \text{ kips}(2) = 24.8 \text{ kips,} \\ 35.1 \text{ kips}(2) = 70.2 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips}(2) = 23.8 \text{ kips,} \\ 8.23 \text{ kips}(2) = 16.5 \text{ kips,} \\ 23.4 \text{ kips}(2) = 46.8 \text{ kips} \end{Bmatrix}$ |
| $= 24.8 \text{ kips}$ | $= 16.5 \text{ kips}$ |

At the middle connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by two because there are two columns of bolts), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by two because there are two columns of bolts), and the available bearing and tearout strength of the girder web for a non-edge bolt (multiplied by two because there are two columns of bolts):

---

# IIA-78

| LRFD | ASD |
|------|-----|
| $\phi r_{n,mid} = \min\begin{Bmatrix} 17.9 \text{ kips}(2) = 35.8 \text{ kips,} \\ 22.0 \text{ kips}(2) = 44.0 \text{ kips,} \\ 35.1 \text{ kips}(2) = 70.2 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,mid}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips}(2) = 23.8 \text{ kips,} \\ 14.6 \text{ kips}(2) = 29.2 \text{ kips,} \\ 23.4 \text{ kips}(2) = 46.8 \text{ kips} \end{Bmatrix}$ |
| $= 35.8 \text{ kips}$ | $= 23.8 \text{ kips}$ |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by two because there are two columns of bolts), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by two because there are two columns of bolts), and the available bearing and tearout strength of the girder web for a non-edge bolt (multiplied by two because there are two columns of bolts):

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min\begin{Bmatrix} 17.9 \text{ kips}(2) = 35.8 \text{ kips,} \\ 22.0 \text{ kips}(2) = 44.0 \text{ kips,} \\ 35.1 \text{ kips}(2) = 70.2 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips}(2) = 23.8 \text{ kips,} \\ 14.6 \text{ kips}(2) = 29.2 \text{ kips,} \\ 23.4 \text{ kips}(2) = 46.8 \text{ kips} \end{Bmatrix}$ |
| $= 35.8 \text{ kips}$ | $= 23.8 \text{ kips}$ |

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi r_{n,top} + \phi r_{n,mid}(n-2) + \phi r_{n,bot}$ | $\frac{R_n}{\Omega} = \frac{r_{n,top}}{\Omega} + \frac{r_{n,mid}}{\Omega}(n-2) + \frac{r_{n,bot}}{\Omega}$ |
| $= 24.8 \text{ kips} + (35.8 \text{ kips})(3-2) + 35.8 \text{ kips}$ | $= 16.5 \text{ kips} + (23.8 \text{ kips})(3-2) + 23.8 \text{ kips}$ |
| $= 96.4 \text{ kips} > 60.0 \text{ kips} \quad \text{o.k.}$ | $= 64.1 \text{ kips} > 40.0 \text{ kips} \quad \text{o.k.}$ |

*Coped Beam Strength*

The available flexural local web buckling strength of the coped beam is verified in Example II.A-4.

*Block Shear Rupture of Beam Web*

From AISC *Specification* Section J4.3, the block shear rupture strength of the beam web, assuming a total beam setback of ¾ in. (includes ¼ in. tolerance to account for possible mill underrun), is determined as follows.

$$R_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$
(*Spec.* Eq. J4-5)

where

$$A_{gv} = (l + \frac{3}{8} \text{ in.})t_w$$
$$= (8\frac{1}{2} \text{ in.} + \frac{3}{8} \text{ in.})(0.355 \text{ in.})$$
$$= 3.15 \text{ in.}^2$$

$$A_{nv} = A_{gv}$$
$$= 3.15 \text{ in.}^2$$

---

# IIA-79

$$A_{nt} = (leg - \frac{3}{4} \text{ in.})t_w$$
$$= (3\frac{1}{2} \text{ in.} - \frac{3}{4} \text{ in.})(0.355 \text{ in.})$$
$$= 0.976 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_n = 0.60(65 \text{ ksi})(3.15 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.976 \text{ in.}^2) < 0.60(50 \text{ ksi})(3.15 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.976 \text{ in.}^2)$$
$$= 186 \text{ kips} > 158 \text{ kips}$$

Therefore:

$$R_n = 158 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(158 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{158 \text{ kips}}{2.00}$ |
| $= 119 \text{ kips} > 60.0 \text{ kips} \quad \text{o.k.}$ | $= 79.0 \text{ kips} > 40.0 \text{ kips} \quad \text{o.k.}$ |

*Shear Strength of Beam Web*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the beam web is determined as follows:

$$A_{gv} = (d - d_c)t_w$$
$$= (18.0 \text{ in.} - 2.00 \text{ in.})(0.355 \text{ in.})$$
$$= 5.68 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$
(*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(5.68 \text{ in.}^2)$$
$$= 170 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
| $\phi R_n = 1.00(170 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{170 \text{ kips}}{1.50}$ |
| $= 170 \text{ kips} > 60.0 \text{ kips} \quad \text{o.k.}$ | $= 113 \text{ kips} > 40.0 \text{ kips} \quad \text{o.k.}$ |

*Summary*

The connection is found to be adequate as given for the applied loads.

---

# IIA-80

# EXAMPLE II.A-6 BEAM END COPED AT THE TOP FLANGE ONLY

## Given:

For an ASTM A992/A992M W21×62 beam with an 8-in.-deep by 9-in.-long cope at the top flange only, assuming a ½ in. setback ($e = 9\frac{1}{2}$ in.) and using an ASTM A572/A572M Grade 50 plate for the stiffeners and doubler:

A. Calculate the available strength of the beam end, as shown in Figure II.A-6-1(a), considering the limit states of flexural yielding, flexural local buckling, shear yielding, and shear rupture.

B. Choose an alternate ASTM A992/A992M W21 shape to eliminate the need for stiffening for the following end reactions:

$$R_D = 23 \text{ kips}$$
$$R_L = 67 \text{ kips}$$

C. Determine the size of doubler plate needed to reinforce the W21×62, as shown in Figure II.A-6-1(b), for the given end reactions in Solution B.

D. Determine the size of longitudinal stiffeners needed to stiffen the W21, as shown in Figure II.A-6-1(c), for the given end reactions in Solution B.

Assume the shear connection is welded to the beam web.

<div style="text-align: center;">
<img src="connection_diagrams" alt="Three connection configurations showing:
(a) Simple shear connection - W21×62 beam with c = 9", d_c = 8"
(b) Doubler plate - W21×62 beam with c and ≥ d_c dimensions, doubler plate
(c) Longitudinal stiffener - W21×62 beam with c and ≥ d_c dimensions, longitudinal stiffener">
</div>

*Fig. II.A-6-1. Connection geometry for Example II.A-6.*

## Solution A:

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

---

# IIA-81

Beam
W21×62
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

Plate
ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W21×62
$d = 21.0$ in.
$t_w = 0.400$ in.
$b_f = 8.24$ in.
$t_f = 0.615$ in.

*Coped Beam Strength*

The beam is assumed to be braced at the end of the uncoped section. Such bracing can be provided by a bracing member or by a slab or other suitable means.

*Flexural Local Buckling of Beam Web*

The limit states of flexural yielding and local web buckling of the coped beam web are checked using AISC *Manual* Part 9 as follows.

From the geometry shown in AISC *Manual* Figure 9-2:

$$h_o = d - d_c$$
$$= 21.0 \text{ in.} - 8.00 \text{ in.}$$
$$= 13.0 \text{ in.}$$

$$\frac{c}{d} = \frac{9.00 \text{ in.}}{21.0 \text{ in.}}$$
$$= 0.429$$

$$\frac{c}{h_o} = \frac{9.00 \text{ in.}}{13.0 \text{ in.}}$$
$$= 0.692$$

Because $\frac{c}{d} \leq 1.0$, the buckling adjustment factor, $f$, is calculated as:

$$f = 2\left(\frac{c}{d}\right)$$
(*Manual* Eq. 9-20a)
$$= 2(0.429)$$
$$= 0.858$$

---

# IIA-82

Because $\frac{c}{h_o} \leq 1.0$, the plate buckling coefficient, $k$, is calculated as:

$$k = 2.2\left(\frac{h_o}{c}\right)^{1.65}$$
(*Manual* Eq. 9-19a)
$$= 2.2\left(\frac{13.0 \text{ in.}}{9.00 \text{ in.}}\right)^{1.65}$$
$$= 4.04$$

The modified plate buckling coefficient, $k_1$, is calculated as:

$$k_1 = fk \geq 1.61$$
(*Manual* Eq. 9-14)
$$= (0.858)(4.04) > 1.61$$
$$= 3.47$$

The plastic section modulus, $Z_c$, is determined from AISC *Manual* Table 9-2b:

$$Z_c = 32.2 \text{ in.}^3$$

The plastic bending moment, $M_p$, is:

$$M_p = F_yZ_c$$
(*Manual* Eq. 9-15)
$$= (50 \text{ ksi})(32.2 \text{ in.}^3)$$
$$= 1,610 \text{ kip-in.}$$

The elastic section modulus, $S_c$, is determined from AISC *Manual* Table 9-2a:

$$S_c = 17.8 \text{ in.}^3$$

The flexural yield moment, $M_y$, is:

$$M_y = F_yS_c$$
(*Manual* Eq. 9-16)
$$= (50 \text{ ksi})(17.8 \text{ in.}^3)$$
$$= 890 \text{ kip-in.}$$

$$\lambda = \frac{h_o}{t_w}$$
(*Manual* Eq. 9-17)
$$= \frac{13.0 \text{ in.}}{0.400 \text{ in.}}$$
$$= 32.5$$

$$\lambda_p = 0.475\sqrt{\frac{k_1E}{F_y}}$$
(*Manual* Eq. 9-18)
$$= 0.475\sqrt{\frac{(3.47)(29,000 \text{ ksi})}{50 \text{ ksi}}}$$
$$= 21.3$$

---

# IIA-83

$$2\lambda_p = 2(21.3)$$
$$= 42.6$$

Because $\lambda_p < \lambda \leq 2\lambda_p$, the nominal flexural strength is:

$$M_n = M_p - (M_p - M_y)\left(\frac{\lambda}{\lambda_p} - 1\right)$$
(*Manual* Eq. 9-11)
$$= 1,610 \text{ kip-in.} - (1,610 \text{ kip-in.} - 890 \text{ kip-in.})\left(\frac{32.5}{21.3} - 1\right)$$
$$= 1,230 \text{ kip-in.}$$

The nominal strength of the coped section is:

$$R_n = \frac{M_n}{e}$$
(from *Manual* Eq. 9-9)
$$= \frac{1,230 \text{ kip-in.}}{9.50 \text{ in.}}$$
$$= 129 \text{ kips}$$

The available strength of the coped section is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b R_n = 0.90(129 \text{ kips})$ | $\frac{R_n}{\Omega_b} = \frac{129 \text{ kips}}{1.67}$ |
| $= 116 \text{ kips}$ | $= 77.2 \text{ kips}$ |

*Shear Strength of Beam Web*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the beam web is determined as follows:

$$A_{gv} = (d - d_c)t_w$$
$$= (21.0 \text{ in.} - 8.00 \text{ in.})(0.400 \text{ in.})$$
$$= 5.20 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$
(*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(5.20 \text{ in.}^2)$$
$$= 156 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
| $\phi R_n = 1.00(156 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{156 \text{ kips}}{1.50}$ |
| $= 156 \text{ kips}$ | $= 104 \text{ kips}$ |

---

# IIA-84

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the beam web is determined as follows. Because the connection is welded to the beam web there is no reduction for bolt holes, therefore:

$$A_{nv} = A_{gv}$$
$$= 5.20 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$
(*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(5.20 \text{ in.}^2)$$
$$= 203 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(203 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{203 \text{ kips}}{2.00}$ |
| $= 152 \text{ kips}$ | $= 102 \text{ kips}$ |

Thus, the available strength of the beam is controlled by the coped section.

| LRFD | ASD |
|------|-----|
| $\phi R_n = 116 \text{ kips}$ | $\frac{R_n}{\Omega} = 77.2 \text{ kips}$ |

## Solution B:

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(23 \text{ kips}) + 1.6(67 \text{ kips})$ | $R_a = 23 \text{ kips} + 67 \text{ kips}$ |
| $= 135 \text{ kips}$ | $= 90.0 \text{ kips}$ |

Try a W21×73.

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam
W21×73
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W21×73
$d = 21.2$ in.
$t_w = 0.455$ in.
$b_f = 8.30$ in.
$t_f = 0.740$ in.

*Flexural Local Buckling of Beam Web*

---

# IIA-85

The limit states of flexural yielding and local web buckling of the coped beam web are checked using AISC *Manual* Part 9 as follows.

From the geometry shown in AISC *Manual* Figure 9-2:

$$h_o = d - d_c$$
$$= 21.2 \text{ in.} - 8.00 \text{ in.}$$
$$= 13.2 \text{ in.}$$

$$\frac{c}{d} = \frac{9.00 \text{ in.}}{21.2 \text{ in.}}$$
$$= 0.425$$

$$\frac{c}{h_o} = \frac{9.00 \text{ in.}}{13.2 \text{ in.}}$$
$$= 0.682$$

Because $\frac{c}{d} \leq 1.0$, the buckling adjustment factor, $f$, is calculated as:

$$f = 2\left(\frac{c}{d}\right)$$
(*Manual* Eq. 9-20a)
$$= 2(0.425)$$
$$= 0.850$$

Because $\frac{c}{h_o} \leq 1.0$, the plate buckling coefficient, $k$, is calculated as:

$$k = 2.2\left(\frac{h_o}{c}\right)^{1.65}$$
(*Manual* Eq. 9-19a)
$$= 2.2\left(\frac{13.2 \text{ in.}}{9.00 \text{ in.}}\right)^{1.65}$$
$$= 4.14$$

The modified plate buckling coefficient, $k_1$, is calculated as:

$$k_1 = fk \geq 1.61$$
(*Manual* Eq. 9-14)
$$= (0.850)(4.14) > 1.61$$
$$= 3.52$$

The plastic section modulus, $Z_c$, is determined from AISC *Manual* Table 9-2b:

$$Z_c = 37.6 \text{ in.}^3$$

The plastic bending moment, $M_p$, is:

---

# IIA-86

$$M_p = F_yZ_c$$
(*Manual* Eq. 9-15)
$$= (50 \text{ ksi})(37.6 \text{ in.}^3)$$
$$= 1,880 \text{ kip-in.}$$

The elastic section modulus, $S_c$, is determined from AISC *Manual* Table 9-2a:

$$S_c = 21.0 \text{ in.}^3$$

The flexural yield moment, $M_y$, is:

$$M_y = F_yS_c$$
(*Manual* Eq. 9-16)
$$= (50 \text{ ksi})(21.0 \text{ in.}^3)$$
$$= 1,050 \text{ kip-in.}$$

$$\lambda = \frac{h_o}{t_w}$$
(*Manual* Eq. 9-17)
$$= \frac{13.2 \text{ in.}}{0.455 \text{ in.}}$$
$$= 29.0$$

$$\lambda_p = 0.475\sqrt{\frac{k_1E}{F_y}}$$
(*Manual* Eq. 9-18)
$$= 0.475\sqrt{\frac{(3.52)(29,000 \text{ ksi})}{50 \text{ ksi}}}$$
$$= 21.5$$

$$2\lambda_p = 2(21.5)$$
$$= 43.0$$

Because $\lambda_p < \lambda \leq 2\lambda_p$, the nominal flexural strength is:

$$M_n = M_p - (M_p - M_y)\left(\frac{\lambda}{\lambda_p} - 1\right)$$
(*Manual* Eq. 9-11)
$$= 1,880 \text{ kip-in.} - (1,880 \text{ kip-in.} - 1,050 \text{ kip-in.})\left(\frac{29.0}{21.5} - 1\right)$$
$$= 1,590 \text{ kip-in.}$$

The nominal strength of the coped section is:

$$R_n = \frac{M_n}{e}$$
(from *Manual* Eq. 9-9)
$$= \frac{1,590 \text{ kip-in.}}{9.50 \text{ in.}}$$
$$= 167 \text{ kips}$$

The available strength of the coped section is:

---

# IIA-87

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b R_n = 0.90(167 \text{ kips})$ | $\frac{R_n}{\Omega_b} = \frac{167 \text{ kips}}{1.67}$ |
| $= 150 \text{ kips}$ | $= 100 \text{ kips}$ |

*Shear Strength of Beam Web*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the beam web is determined as follows:

$$A_{gv} = (d - d_c)t_w$$
$$= (21.2 \text{ in.} - 8.00 \text{ in.})(0.455 \text{ in.})$$
$$= 6.01 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$
(*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(6.01 \text{ in.}^2)$$
$$= 180 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
| $\phi R_n = 1.00(180 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{180 \text{ kips}}{1.50}$ |
| $= 180 \text{ kips}$ | $= 120 \text{ kips}$ |

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the beam web is determined as follows. Because the connection is welded to the beam web, there is no reduction for bolt holes, therefore:

$$A_{nv} = A_{gv}$$
$$= 6.01 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$
(*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(6.01 \text{ in.}^2)$$
$$= 234 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(234 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{234 \text{ kips}}{2.00}$ |
| $= 176 \text{ kips}$ | $= 117 \text{ kips}$ |

Thus, the available strength is controlled by the coped section, and the available strength of the beam is:

---

# IIA-88

| LRFD | ASD |
|------|-----|
| $\phi R_n = 150 \text{ kips} > 135 \text{ kips} \quad \text{o.k.}$ | $\frac{R_n}{\Omega} = 100 \text{ kips} > 90.0 \text{ kips} \quad \text{o.k.}$ |

## Solution C:

*Doubler Plate Design*

The doubler plate is designed using AISC *Manual* Part 9. An ASTM A572/A572M Grade 50 plate is recommended in order to match the beam yield strength. A ¼ in. minimum plate thickness will be used in order to allow the use of a $\frac{3}{16}$ in. fillet weld. The depth of the plate will be set so that a compact $h/t$ ratio from AISC *Specification* Table B4.1b will be satisfied. This is a conservative criterion that will allow local buckling of the doubler to be neglected.

$$\frac{d_p}{t_p} \leq 1.12\sqrt{\frac{E}{F_y}}$$

Solving for $d_p$:

$$d_p \leq 1.12t_p\sqrt{\frac{E}{F_y}}$$
$$\leq 1.12(\frac{1}{4} \text{ in.})\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$
$$\leq 6.74 \text{ in.}$$

A 6.50 in. doubler plate will be used.

Using principles of mechanics, the elastic section modulus, $S_c$, and plastic section modulus, $Z_c$, are calculated neglecting the fillets and assuming the doubler plate is placed ½ in. down from the top of the cope.

$$S_c = 25.5 \text{ in.}^3$$
$$Z_c = 44.8 \text{ in.}^3$$

The plastic bending moment, $M_p$, of the reinforced section is:

$$M_p = F_yZ_c$$
(*Manual* Eq. 9-15)
$$= (50 \text{ ksi})(44.8 \text{ in.}^3)$$
$$= 2,240 \text{ kip-in.}$$

The flexural yield moment, $M_y$, of the reinforced section is:

$$M_y = F_yS_c$$
(*Manual* Eq. 9-16)
$$= (50 \text{ ksi})(25.5 \text{ in.}^3)$$
$$= 1,280 \text{ kip-in.}$$

Because $\lambda_p < \lambda \leq 2\lambda_p$ for the unreinforced section, the nominal flexural strength is:

---

# IIA-89

$$M_n = M_p - (M_p - M_y)\left(\frac{\lambda}{\lambda_p} - 1\right)$$
(*Manual* Eq. 9-11)
$$= 2,240 \text{ kip-in.} - (2,240 \text{ kip-in.} - 1,280 \text{ kip-in.})\left(\frac{32.5}{21.3} - 1\right)$$
$$= 1,740 \text{ kip-in.}$$

The available strength of the coped section is determined as follows:

$$R_n = \frac{M_n}{e}$$
(from *Manual* Eq. 9-9)
$$= \frac{1,740 \text{ kip-in.}}{9.50 \text{ in.}}$$
$$= 183 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b R_n = 0.90(183 \text{ kips})$ | $\frac{R_n}{\Omega_b} = \frac{183 \text{ kips}}{1.67}$ |
| $= 165 \text{ kips}$ | $= 110 \text{ kips}$ |

*Shear Strength of Beam Web*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the beam web reinforced with the doubler plate is determined as follows:

$$A_{gv-web} = (d - d_c)t_w$$
$$= (21.0 \text{ in.} - 8.00 \text{ in.})(0.400 \text{ in.})$$
$$= 5.20 \text{ in.}^2$$

$$A_{gv-plate} = d_pt_p$$
$$= (6.50 \text{ in.})(\frac{1}{4} \text{ in.})$$
$$= 1.63 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv-web} + 0.60F_y A_{gv-plate}$$
(from *Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(5.20 \text{ in.}^2) + 0.60(50 \text{ ksi})(1.63 \text{ in.}^2)$$
$$= 205 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
| $\phi R_n = 1.00(205 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{205 \text{ kips}}{1.50}$ |
| $= 205 \text{ kips}$ | $= 137 \text{ kips}$ |

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the beam web reinforced with the doubler plate is determined as follows. Because the connection is welded, there is no reduction for bolt holes, therefore:

---

# IIA-90

$$A_{nv-web} = A_{gv-web}$$
$$= 5.20 \text{ in.}^2$$

$$A_{nv-plate} = A_{gv-plate}$$
$$= 1.63 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv-web} + 0.60F_u A_{nv-plate}$$
(from *Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(5.20 \text{ in.}^2) + 0.60(65 \text{ ksi})(1.63 \text{ in.}^2)$$
$$= 266 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(266 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{266 \text{ kips}}{2.00}$ |
| $= 200 \text{ kips}$ | $= 133 \text{ kips}$ |

Thus, the available strength of the beam is controlled by the coped section.

| LRFD | ASD |
|------|-----|
| $\phi R_n = 165 \text{ kips} > 135 \text{kips} \quad \text{o.k.}$ | $\frac{R_n}{\Omega} = 110 \text{ kips} > 90.0 \text{ kips} \quad \text{o.k.}$ |

*Weld Design*

Determine the length of weld required to transfer the force into and out of the doubler plate. From Solution A, the available strength of the beam web is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 116 \text{ kips}$ | $\frac{R_n}{\Omega} = 77.2 \text{ kips}$ |

The available strength of the beam web reinforced with the doubler plate is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 165 \text{ kips}$ | $\frac{R_n}{\Omega} = 110 \text{ kips}$ |

The force in the doubler plate is determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
| $F_d = 0.90(50 \text{ ksi})(\frac{1}{4} \text{ in.})(6.50 \text{ in.})\left(\frac{116 \text{ kips}}{165 \text{ kips}}\right)$ | $F_d = \frac{(50 \text{ ksi})(\frac{1}{4} \text{ in.})(6.50 \text{ in.})}{1.67}\left(\frac{77.2 \text{ kips}}{110 \text{ kips}}\right)$ |
| $= 51.4 \text{ kips}$ | $= 34.1 \text{ kips}$ |

From AISC *Specification* Section J2.4, the doubler plate weld is designed as follows:

---

# IIA-91

$$R_n = 0.85R_{nwl} + 1.5R_{nwt}$$
(from *Spec.* Eq. J2-6)

| LRFD | ASD |
|------|-----|
| From AISC *Manual* Equation 8-2a: | From AISC *Manual* Equation 8-2b: |
| $R_{nw} = 1.392Dl$ | $R_{nw} = 0.928Dl$ |
| From AISC *Specification* Equation J2-6: | From AISC *Specification* Equation J2-6: |
| $51.4 \text{ kips} = \left[\frac{(2 \text{ welds})(0.85)(1.392 \text{ kips/in.})}{\times(3 \text{ sixteenths})l_w}\right] + \left[\frac{(1.5)(1.392 \text{ kips/in.})(3 \text{ sixteenths})}{\times(6.50 \text{ in.})}\right]$ | $34.1 \text{ kips} = \left[\frac{(2 \text{ welds})(0.85)(0.928 \text{ kips/in.})}{\times(3 \text{ sixteenths})l_w}\right] + \left[\frac{1.5(0.928 \text{ kips/in.})(3 \text{ sixteenths})}{\times(6.50 \text{ in.})}\right]$ |
| Solving for $l_w$: | Solving for $l_w$: |
| $l_w = 1.50 \text{ in.}$ | $l_w = 1.47 \text{ in.}$ |

Use 1.50 in. of $\frac{3}{16}$ in. longitudinal fillet weld, minimum.

The doubler plate must extend at least $d_c$ beyond the cope. Use a PL¼ in. × 6½ in. × 1 ft-5 in. with $\frac{3}{16}$ in. welds all around.

## Solution D:

*Longitudinal Stiffener Design*

Try PL¼ in.×4 in. slotted to fit over the beam web.

Determine $Z_c$ for the stiffened section:

$$A_w = (d - d_c - t_f)t_w$$
$$= (21.0 \text{ in.} - 8.00 \text{ in.} - 0.615 \text{ in.})(0.400 \text{ in.})$$
$$= 4.95 \text{ in.}^2$$

$$A_f = b_ft_f$$
$$= (8.24 \text{ in.})(0.615 \text{ in.})$$
$$= 5.07 \text{ in.}^2$$

$$A_{rp} = b_pt_p$$
$$= (4.00 \text{ in.})(\frac{1}{4} \text{ in.})$$
$$= 1.00 \text{ in.}^2$$

$$A_t = A_w + A_f + A_{rp}$$
$$= 4.95 \text{ in.}^2 + 5.07 \text{ in.}^2 + 1.00 \text{ in.}^2$$
$$= 11.0 \text{ in.}^2$$

The location of the elastic neutral axis (neglecting fillets) from the outside of the flange is:

---

# IIA-92

$$y_o = \frac{A_f\left(\frac{t_f}{2}\right) + A_w\left(\frac{d - d_c + t_f}{2}\right) + A_{rp}\left(d - d_c - \frac{t_p}{2}\right)}{A_t}$$

$$= \frac{(5.07 \text{ in.}^2)\left(\frac{0.615 \text{ in.}}{2}\right) + (4.95 \text{ in.}^2)\left(\frac{21.0 \text{ in.} - 8.00 \text{ in.} + 0.615 \text{ in.}}{2}\right) + (1.00 \text{ in.}^2)\left(21.0 \text{ in.} - 8.00 \text{ in.} - \frac{\frac{1}{4} \text{ in.}}{2}\right)}{11.0 \text{ in.}^2}$$

$$= 4.38 \text{ in.}$$

The location of the plastic neutral axis (neglecting fillets) from the inside of the flange is:

$$t_fb_f + y_pt_w = t_pb_p + (d - d_c - t_f - y_p)t_w$$
$$(0.615 \text{ in.})(8.24 \text{ in.}) + y_p(0.400 \text{ in.}) = (\frac{1}{4} \text{ in.})(4.00 \text{ in.}) + (21.0 \text{ in.} - 8.00 \text{ in.} - 0.615 \text{ in.} - y_p)(0.400 \text{ in.})$$

$$y_p = 1.12 \text{ in.}$$

From elementary mechanics, the section properties are as follows:

$$Z_c = 44.3 \text{ in.}^3$$
$$I_c = 253 \text{ in.}^4$$
$$S_{xc} = 28.6 \text{ in.}^3$$
$$S_{xt} = 57.7 \text{ in.}^3$$

$$h_c = 2(d - d_c - y_o)$$
$$= 2(21.0 \text{ in.} - 8.00 \text{ in.} - 4.38 \text{ in.})$$
$$= 17.2 \text{ in.}$$

$$h_p = 2(d - d_c - y_p - t_f)$$
$$= 2(21.0 \text{ in.} - 8.00 \text{ in.} - 1.12 \text{ in.} - 0.615 \text{ in.})$$
$$= 22.5 \text{ in.}$$

Compact section properties for the longitudinal stiffener and the web are determined from AISC *Specification* Table B4.1b, Cases 11 and 16.

$$\lambda_p = 0.38\sqrt{\frac{E}{F_y}}$$
(*Spec.* Table B4.1b, Case 11)
$$= 0.38\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$
$$= 9.15$$

$$\lambda = \frac{b}{t}$$
$$= \frac{(4.00 \text{ in.}/2)}{\frac{1}{4} \text{ in.}}$$
$$= 8.00$$

Because $\lambda < \lambda_p$, the stiffener is compact in flexure.

---

# IIA-93

$$\lambda_r = 5.70\sqrt{\frac{E}{F_y}}$$
(*Spec.* Table B4.1b, Case 16)
$$= 5.70\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$
$$= 137$$

$$\lambda = \frac{h_c}{t_w}$$
$$= \frac{17.2 \text{ in.}}{0.400 \text{ in.}}$$
$$= 43.0$$

Because $\lambda < \lambda_r$, the web is not slender, therefore AISC *Specification* Section F4 applies.

Determine if lateral-torsional buckling is a design consideration.

$$a_w = \frac{h_ct_w}{b_fct_fc}$$
(*Spec.* Eq. F4-12)
$$= \frac{(17.2 \text{ in.})(0.400 \text{ in.})}{(4.00 \text{ in.})(\frac{1}{4} \text{ in.})}$$
$$= 6.88$$

$$r_t = \frac{b_{fc}}{\sqrt{12\left[1 + \frac{1}{6}a_w\right]}}$$
(*Spec.* Eq. F4-11)
$$= \frac{4.00 \text{ in.}}{\sqrt{12\left[1 + \frac{1}{6}(6.88)\right]}}$$
$$= 0.788 \text{ in.}$$

$$L_p = 1.1r_t\sqrt{\frac{E}{F_y}}$$
(*Spec.* Eq. F4-7)
$$= 1.1(0.788 \text{ in.})\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$
$$= 20.9 \text{ in.}$$

The stiffener will not reach a length of 20.9 in. Lateral-torsional buckling is not a design consideration.

Determine if the web of the singly symmetric shape is compact. AISC *Specification* Table B4.1b, Case 16, applies.

$$M_p = F_yZ_c$$
$$= (50 \text{ ksi})(44.3 \text{ in.}^3)$$
$$= 2,220 \text{ kip-in.}$$

---

# IIA-94

$$M_y = F_yS_{xc}$$
$$= (50 \text{ ksi})(28.6 \text{ in.}^3)$$
$$= 1,430 \text{ kip-in.}$$

$$\lambda_p = \frac{\frac{h_c}{h_p}\sqrt{\frac{E}{F_y}}}{\left[0.54\frac{M_p}{M_y} - 0.09\right]^2} \leq 5.70\sqrt{\frac{E}{F_y}}$$

$$= \frac{\frac{17.2 \text{ in.}}{22.5 \text{ in.}}\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}}{\left[0.54\left(\frac{2,220 \text{ kip-in.}}{1,430 \text{ kip-in.}}\right) - 0.09\right]^2} \leq 5.70\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 32.9 < 137$$
$$= 32.9$$

$$\lambda = \frac{h_c}{t_w}$$
$$= \frac{17.2 \text{ in.}}{0.400 \text{ in.}}$$
$$= 43.0$$

Because $\lambda > \lambda_p$, the web is noncompact, and AISC *Specification* Section F4 applies.

Because $S_{xt} > S_{xc}$, tension flange yielding does not govern. Determine the flexural strength based on compression flange yielding.

$$M_{yc} = F_yS_{xc}$$
(*Spec.* Eq. F4-4)
$$= (50 \text{ ksi})(28.6 \text{ in.}^3)$$
$$= 1,430 \text{ kip-in.}$$

$$I_{yc} = \frac{t_pb_p^3}{12}$$
$$= \frac{(\frac{1}{4} \text{ in.})(4.00 \text{ in.})^3}{12}$$
$$= 1.33 \text{ in.}^4$$

$$I_y = I_{yc} + \frac{t_fb_f^3}{12} + \frac{(d - d_c - t_f)t_w^3}{12}$$
$$= 1.33 \text{ in.}^4 + \frac{(0.615 \text{ in.})(8.24 \text{ in.})^3}{12} + \frac{(21.0 \text{ in.} - 8.00 \text{ in.} - 0.615 \text{ in.})(0.400 \text{ in.})^3}{12}$$
$$= 30.1 \text{ in.}^4$$

---

# IIA-95

$$\frac{I_{yc}}{I_y} = \frac{1.33 \text{ in.}^4}{30.1 \text{ in.}^4}$$
$$= 0.0442$$

Because $\frac{I_{yc}}{I_y} \leq 0.23$, $R_{pc} = 1.0$ and:

$$M_n = R_{pc}M_{yc}$$
(*Spec* Eq. F4-1)
$$= 1.0(1,430 \text{ kip-in.})$$
$$= 1,430 \text{ kip-in.}$$

The nominal strength of the reinforced section is:

$$R_n = \frac{M_n}{e}$$
$$= \frac{1,430 \text{ kip-in.}}{9.50 \text{ in.}}$$
$$= 151 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b R_n = 0.90(151 \text{ kips})$ | $\frac{R_n}{\Omega_b} = \frac{151 \text{ kips}}{1.67}$ |
| $= 136 \text{ kips} > 135 \text{ kips} \quad \text{o.k.}$ | $= 90.4 \text{ kips} > 90.0 \text{ kips} \quad \text{o.k.}$ |

*Plate Dimensions*

Because the longitudinal stiffening must extend at least $d_c$ beyond the cope, use PL¼ in.×4 in.×1 ft 5 in. with ¼ in. welds.

*Weld Strength*

By calculations not shown, the moment of inertia of the reinforced section and distance from the centroid to the bottom of the reinforcement plate are:

$$I_{net} = 253 \text{ in.}^4$$

$$\bar{y} = 8.61 \text{ in.}$$

The first moment of the reinforcement plate is:

$$Q = A_py$$
$$= (\frac{1}{4} \text{ in.})(4.00 \text{ in.})[8.61 \text{ in.} + 0.5(\frac{1}{4} \text{ in.})]$$
$$= 8.74 \text{ in.}^3$$

where $A_p$ is the area of the reinforcement plate and $y$ is the distance from the centroid of the reinforced section to the centroid of the reinforcement plate.

---

# IIA-96

From mechanics of materials and shear flow, the force per length that the weld must resist in the area of the cope is:

| LRFD | ASD |
|------|-----|
| $r_u = \frac{V_uQ}{I_{net}(2 \text{ welds})}$ | $r_a = \frac{V_aQ}{I_{net}(2 \text{ welds})}$ |
| $= \frac{(135 \text{ kips})(8.74 \text{ in.}^3)}{(253 \text{ in.}^4)(2 \text{ welds})}$ | $= \frac{(90.0 \text{ kips})(8.74 \text{ in.}^3)}{(253 \text{ in.}^4)(2 \text{ welds})}$ |
| $= 2.33 \text{ kips/in.}$ | $= 1.55 \text{ kips/in.}$ |

From mechanics of materials, the force per length that the weld must resist to transfer the force in the reinforcement plate to the beam web is:

| LRFD | ASD |
|------|-----|
| $r_u = \frac{V_{u}eQ}{I_{net}(2 \text{ welds})(l - c)}$ | $r_a = \frac{V_{a}eQ}{I_{net}(2 \text{ welds})(l - c)}$ |
| $= \frac{(135 \text{ kips})(9.50 \text{ in.})(8.74 \text{ in.}^3)}{(253 \text{ in.}^4)(2 \text{ welds})(17.0 \text{ in.} - 9.00 \text{ in.})}$ | $= \frac{(90.0 \text{ kips})(9.50 \text{ in.})(8.74 \text{ in.}^3)}{(253 \text{ in.}^4)(2 \text{ welds})(17.0 \text{ in.} - 9.00 \text{ in.})}$ |
| $= 2.77 \text{ kips/in.} \quad \textbf{controls}$ | $= 1.85 \text{ kips/in.} \quad \textbf{controls}$ |

From AISC *Manual* Part 8, the available strength of the weld is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = (1.392 \text{ kip/in.})D$ &nbsp;&nbsp;&nbsp;&nbsp; (from *Manual* Eq. 8-2a) | $\frac{r_n}{\Omega} = (0.928 \text{ kip/in.})D$ &nbsp;&nbsp;&nbsp;&nbsp; (from *Manual* Eq. 8-2b) |
| $= (1.392 \text{ kips/in.})(4 \text{ sixteenths})$ | $= (0.928 \text{ kips/in.})(4 \text{ sixteenths})$ |
| $= 5.57 \text{ kips/in.} > 2.77 \text{ kips/in.} \quad \text{o.k.}$ | $= 3.71 \text{ kips/in.} > 1.85 \text{ kips/in.} \quad \text{o.k.}$ |

Determine if the web has adequate shear rupture strength:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = \phi0.60F_uA_{nv}$ &nbsp;&nbsp;&nbsp;&nbsp; (from *Spec.* Eq. J4-4) | $\frac{r_n}{\Omega} = \frac{0.60F_uA_{nv}}{\Omega}$ &nbsp;&nbsp;&nbsp;&nbsp; (from *Spec.* Eq. J4-4) |
| $= \frac{0.75(0.60)(65 \text{ ksi})(0.400 \text{ in.})}{2 \text{ welds}}$ | $= \frac{0.60(65 \text{ ksi})(0.400 \text{ in.})}{2.00(2 \text{ welds})}$ |
| $= 5.85 \text{ kips/in.} > 2.77 \text{ kips/in.} \quad \text{o.k.}$ | $= 3.90 \text{ kips/in.} > 1.85 \text{ kips/in.} \quad \text{o.k.}$ |

---

# IIA-97

# EXAMPLE II.A-7 BEAM END COPED AT THE TOP AND BOTTOM FLANGES

## Given:

Determine the available strength for an ASTM A992/A992M W16×40 with a 3½-in.-deep by 9½-in.-wide cope at the top flange and 2-in.-deep by 9½-in.-wide cope at the bottom flange, as shown in Figure II.A-7-1, considering the limit states of flexural yielding and local buckling. Assume a ½ in. setback from the face of the support to the end of the beam.

<div style="text-align: center;">
<img src="connection_diagram" alt="Diagram showing W16×40 beam with:
- Top cope: ½" setback, c_t = 9½", d_ct = 3½"
- Bottom cope: c_b = 9½", d_cb = 2"
- Simple shear connection between copes
- Beam depth notation showing cope dimensions">
</div>

*Fig. II.A-7-1. Connection geometry for Example II.A-7.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam
W16×40
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

From AISC *Manual* Table 1-1 and AISC *Manual* Figure 9-3, the geometric properties are as follows:

Beam
W16×40
$d = 16.0$ in.
$t_w = 0.305$ in.
$t_f = 0.505$ in.
$b_f = 7.00$ in.
$c_t = 9\frac{1}{2}$ in.
$d_{ct} = 3\frac{1}{2}$ in.
$c_b = 9\frac{1}{2}$ in.
$d_{cb} = 2$ in.
$e = 9\frac{1}{2}$ in. $+ \frac{1}{2}$ in.
$\quad = 10.0$ in.
$h_c = d - d_{ct} - d_{cb}$
$\quad = 16.0 \text{ in.} - 3\frac{1}{2} \text{ in.} - 2 \text{ in.}$
$\quad = 10.5$ in.

---

# IIA-98

For a beam that is coped at both flanges, the local flexural strength is determined in accordance with AISC *Specification* Section F11.

*Available Strength at Coped Section*

The cope at the tension side of the beam is equal to the cope length at the compression side. From AISC *Manual* Part 9, $L_b = c_t$.

$$C_b = \left[3 + \ln\left(\frac{L_b}{d}\right)\right]\left(1 - \frac{d_{ct}}{d}\right) \geq 1.84$$
(*Manual* Eq. 9-21)

$$= \left[3 + \ln\left(\frac{9\frac{1}{2} \text{ in.}}{16.0 \text{ in.}}\right)\right]\left(1 - \frac{3\frac{1}{2} \text{ in.}}{16.0 \text{ in.}}\right) \geq 1.84$$

$$= 1.94 > 1.84$$

Use $C_b = 1.94$.

The available strength of the coped section is determined using AISC *Specification* Section F11, with $d = h_c = 10.5$ in. and the unbraced length $L_b = c_t = 9\frac{1}{2}$ in.

$$\frac{L_bd}{t^2} = \frac{(9\frac{1}{2} \text{ in.})(10.5 \text{ in.})}{(0.305 \text{ in.})^2}$$
$$= 1,070$$

$$\frac{0.08E}{F_y} = \frac{0.08(29,000 \text{ ksi})}{50 \text{ ksi}}$$
$$= 46.4$$

$$\frac{1.9E}{F_y} = \frac{1.9(29,000 \text{ ksi})}{50 \text{ ksi}}$$
$$= 1,100$$

Because $\frac{0.08E}{F_y} < \frac{L_bd}{t^2} \leq \frac{1.9E}{F_y}$, the limit state of lateral-torsional buckling applies. The nominal flexural strength of the coped portion of the web is determined using AISC *Specification* Section F11.2(b).

Determine the net elastic and plastic section moduli:

$$S_c = \frac{t_wh_c^2}{6}$$
$$= \frac{(0.305 \text{ in.})(10.5 \text{ in.})^2}{6}$$
$$= 5.60 \text{ in.}^3$$

---

# IIA-99

$$Z_c = \frac{t_wh_c^2}{4}$$
$$= \frac{(0.305 \text{ in.})(10.5 \text{ in.})^2}{4}$$
$$= 8.41 \text{ in.}^3$$

$$M_y = F_yS_c$$
$$= (50 \text{ ksi})(5.60 \text{ in.}^3)$$
$$= 280 \text{ kip-in.}$$

$$M_p = F_yZ_c$$
$$= (50 \text{ ksi})(8.41 \text{ in.}^3)$$
$$= 421 \text{ kip-in.}$$

$$M_n = C_b\left[1.52 - 0.274\left(\frac{L_bd}{t^2}\right)\left(\frac{F_y}{E}\right)\right]M_y \leq M_p$$
(*Spec.* Eq. F11-3)

$$= 1.94\left[1.52 - 0.274(1,070)\left(\frac{50 \text{ ksi}}{29,000 \text{ ksi}}\right)\right](280 \text{ kip-in.}) \leq 421 \text{ kip-in.}$$

$$= 551 \text{ kip-in.} > 421 \text{ kip-in.}$$

The nominal flexural strength of the reduced section is 421 kip-in. The nominal strength of the coped section is:

$$R_n = \frac{M_n}{e}$$
(from *Manual* Eq. 9-9)
$$= \frac{421 \text{ kip-in.}}{10.0 \text{ in.}}$$
$$= 42.1 \text{ kips}$$

The available strength at the coped end is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b R_n = 0.90(42.1 \text{ kips})$ | $\frac{R_n}{\Omega_b} = \frac{42.1 \text{ kips}}{1.67}$ |
| $= 37.9 \text{ kips}$ | $= 25.2 \text{ kips}$ |

---

# IIA-100

# EXAMPLE II.A-8 ALL-BOLTED DOUBLE-ANGLE CONNECTIONS (BEAMS-TO-GIRDER WEB)

## Given:

Verify the all-bolted double-angle connections for back-to-back ASTM A992/A992M W12×40 and W21×50 beams to an ASTM A992/A992M W30×99 girder web to support the end reactions shown in Figure II.A-8-1. Use ASTM A572/A572M Grade 50 angles.

<div style="text-align: center;">
<img src="connection_diagram" alt="Detailed connection diagram showing:
- Part Plan view with Beam A (W12×40) and Beam B (W21×50) on W30×99 girder
- Beam A: R_D = 4.17 kips, R_L = 12.5 kips
- Beam B: R_D = 18.3 kips, R_L = 55 kips
- Section A-A details showing 2L5×3½×¼ × 0'-5½" (SLBB) for Beam A
- Section B-B details showing 2L5×3½×¼ × 1'-2½" (SLBB) for Beam B
- ¾" dia. Group 120 bolts, thread condition N, std. holes
- l_eh = 1⅝" (typ.), ½" setback (typ.)
- Dimensional notes about entering and tightening clearances from AISC Manual Table 7-15">
</div>

*Fig. II.A-8-1. Connection geometry for Example II.A-8.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

Beams and girder
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

Angles
ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

---

# IIA-101

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W12×40
$d = 11.9$ in.
$t_w = 0.295$ in.

Beam
W21×50
$d = 20.8$ in.
$t_w = 0.380$ in.

Girder
W30×99
$d = 29.7$ in.
$t_w = 0.520$ in.

From AISC *Specification* Table J3.3, for ¾-in.-diameter bolts with standard holes:

$d_h = 13⁄16$ in.

**Beam A Connection:**

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(4.17 \text{ kips}) + 1.6(12.5 \text{ kips})$ | $R_a = 4.17 \text{ kips} + 12.5 \text{ kips}$ |
| $= 25.0 \text{ kips}$ | $= 16.7 \text{ kips}$ |

*Available Angle Strength*

AISC *Manual* Table 10-1a includes checks for the limit states of shear yielding, shear rupture, and block shear rupture of the angles.

Use 2 rows of ¾-in.-diameter bolts in standard holes and 2L5×3½×¼ (SLBB). From AISC *Manual* Table 10-1a:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 54.8 \text{ kips} > 25.0 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 36.6 \text{ kips} > 16.7 \text{ kips} \quad \textbf{o.k.}$ |

*Available Shear Transfer Strength at Bolt Holes at Beam Web*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength determined in accordance with AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the angles at the bolt hole determined in accordance with AISC *Specification* Section J3.11a, and (3) the available bearing or tearout strength of the beam web at the bolt hole determined in accordance with AISC *Specification* Section J3.11a.

From AISC *Manual* Table 10-1b, the available bolt shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

---

# IIA-102

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9 \text{ kips}$ | $\frac{r_n}{\Omega} = 11.9 \text{ kips}$ |

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the angle per bolt for ¾-in.-diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): | For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): |
| $\phi r_n = (49.4 \text{ kips/in.})(1/4 \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kips/in.})(1/4 \text{ in.})$ |
| $= 12.4 \text{ kips}$ | $= 8.23 \text{ kips}$ |
| | |
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kips/in.})(1/4 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(1/4 \text{ in.})$ |
| $= 22.0 \text{ kips}$ | $= 14.6 \text{ kips}$ |

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the beam web per bolt for ¾-in.- diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the edge bolt ($l_{ev} = 2$ in.): | For the edge bolt ($l_{ev} = 2$ in.): |
| $\phi r_n = (87.8 \text{ kips/in.})(0.295 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(0.295 \text{ in.})$ |
| $= 25.9 \text{ kips}$ | $= 17.3 \text{ kips}$ |
| | |
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kips/in.})(0.295 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(0.295 \text{ in.})$ |
| $= 25.9 \text{ kips}$ | $= 17.3 \text{ kips}$ |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by two because bolts are in double shear), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by two because there are two angles), and the available bearing and tearout strength of the beam web for an edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min\begin{cases}(17.9 \text{ kips})(2) = 35.8 \text{ kips,}\\(22.0 \text{ kips})(2) = 44.0 \text{ kips,}\\25.9 \text{ kips}\end{cases}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{cases}(11.9 \text{ kips})(2) = 23.8 \text{ kips,}\\(14.6 \text{ kips})(2) = 29.2 \text{ kips,}\\17.3 \text{ kips}\end{cases}$ |
| $= 25.9 \text{ kips}$ | $= 17.3 \text{ kips}$ |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by two because bolts are in double shear), the available bearing and tearout strength of the angles for an edge bolt (multiplied by two because there are two angles), and the available bearing and tearout strength of the beam web for a non-edge bolt:

---

# IIA-103

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min\begin{cases}(17.9 \text{ kips})(2) = 35.8 \text{ kips,}\\(12.4 \text{ kips})(2) = 24.8 \text{ kips,}\\25.9 \text{ kips}\end{cases}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{cases}(11.9 \text{ kips})(2) = 23.8 \text{ kips,}\\(8.23 \text{ kips})(2) = 16.5 \text{ kips,}\\17.3 \text{ kips}\end{cases}$ |
| $= 24.8 \text{ kips}$ | $= 16.5 \text{ kips}$ |

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi r_{n,top} + \phi r_{n,bot}$ | $\frac{R_n}{\Omega} = \frac{r_{n,top}}{\Omega} + \frac{r_{n,bot}}{\Omega}$ |
| $= 25.9 \text{ kips} + 24.8 \text{ kips}$ | $= 17.3 \text{ kips} + 16.5 \text{ kips}$ |
| $= 50.7 \text{ kips} > 25.0 \text{ kips} \quad \textbf{o.k.}$ | $= 33.8 \text{ kips} > 16.7 \text{ kips} \quad \textbf{o.k.}$ |

*Coped Beam Strength*

From AISC *Manual* Part 9, the available coped beam web strength for top cope only is the lesser of the limit states of flexural local web buckling and block shear rupture.

*Beam Web Available Shear Strength*

AISC *Manual* Table 10-1c includes checks for the limit states of block shear rupture of the beam web.

From AISC *Manual* Table 10-1c, with ¾-in.-diameter bolts in standard holes:

| LRFD | ASD |
|------|-----|
| For the web above the top edge hole (conservatively assuming $l_{ev,t} = 1\frac{1}{4}$ in.): | For the web above the top edge hole (conservatively assuming $l_{ev,t} = 1\frac{1}{4}$ in.): |
| $\phi r_n = 31.1 \text{ kips/in.}$ | $\frac{r_n}{\Omega} = 20.7 \text{ kips/in.}$ |
| | |
| For the web between the center holes ($s = 3$ in.): | For web between the the center holes ($s = 3$ in.): |
| $\phi r_n = 62.2 \text{ kips/in.}$ | $\frac{r_n}{\Omega} = 41.4 \text{ kips/in.}$ |
| | |
| For the web at the bottom edge hole (conservatively assuming $l_{eb} = 1\frac{1}{4}$ in.): | For the web at the bottom edge hole (conservatively assuming $l_{eb} = 1\frac{1}{4}$ in.): |
| $\phi r_n = 39.6 \text{ kips/in.}$ | $\frac{r_n}{\Omega} = 26.4 \text{ kips/in.}$ |
| | |
| $\phi R_n = (31.1 \text{ kips/in.} + 62.2 \text{ kips/in.} + 39.6 \text{ kips/in.})$ | $\frac{R_n}{\Omega} = (20.7 \text{ kips/in.} + 41.4 \text{ kips/in.} + 26.4 \text{ kips/in.})$ |
| $\times(0.295 \text{ in.})$ | $\times(0.295 \text{ in.})$ |
| $= 39.2 \text{ kips} > 25.0 \text{ kips} \quad \textbf{o.k.}$ | $= 26.1 \text{ kips} > 16.7 \text{ kips} \quad \textbf{o.k.}$ |

*Flexural local web buckling of beam web*

---

# IIA-104

The limit states of flexural yielding and local web buckling of the coped beam web are checked using AISC *Manual* Part 9 as follows:

$$e = c + setback$$
$$= 5 \text{ in.} + \frac{1}{2} \text{ in.}$$
$$= 5.50 \text{ in.}$$

From the geometry shown in AISC *Manual* Figure 9-2:

$$h_c = d - d_c$$
$$= 11.9 \text{ in.} - 2 \text{ in.}$$
$$= 9.90 \text{ in.}$$

$$\frac{c}{d} = \frac{5 \text{ in.}}{11.9 \text{ in.}}$$
$$= 0.420$$

$$\frac{c}{h_c} = \frac{5 \text{ in.}}{9.90 \text{ in.}}$$
$$= 0.505$$

Because $\frac{c}{d} \leq 1.0$, the buckling adjustment factor, $f$, is calculated as follows:

$$f = 2\left(\frac{c}{d}\right)$$ (*Manual* Eq. 9-20a)
$$= 2(0.420)$$
$$= 0.840$$

Because $\frac{c}{h_c} \leq 1.0$, the plate buckling coefficient, $k$, is calculated as follows:

$$k = 2.2\left(\frac{h_c}{c}\right)^{1.65}$$ (*Manual* Eq. 9-19a)
$$= 2.2\left(\frac{9.90 \text{ in.}}{5 \text{ in.}}\right)^{1.65}$$
$$= 6.79$$

$$\lambda = \frac{h_c}{t_w}$$ (*Manual* Eq. 9-17)
$$= \frac{9.90 \text{ in.}}{0.295 \text{ in.}}$$
$$= 33.6$$

$$k_1 = fk \geq 1.61$$ (*Manual* Eq. 9-14)
$$= (0.840)(6.79) \geq 1.61$$
$$= 5.70 > 1.61$$

---

# IIA-105

$$\lambda_p = 0.475\sqrt{\frac{k_1E}{F_y}}$$ (*Manual* Eq. 9-18)
$$= 0.475\sqrt{\frac{(5.70)(29,000 \text{ ksi})}{50 \text{ ksi}}}$$
$$= 27.3$$

$$2\lambda_p = 2(27.3)$$
$$= 54.6$$

Because $\lambda_w < \lambda \leq 2\lambda_p$, calculate the nominal moment strength using AISC *Manual* Equation 9-11.

The plastic section modulus of the coped section, $Z_c$, is determined from AISC *Manual* Table 9-2b.

$$Z_c = 14.0 \text{ in.}^3$$

$$M_p = F_yZ_c$$ (*Manual* Eq. 9-15)
$$= (50 \text{ ksi})(14.0 \text{ in.}^3)$$
$$= 700 \text{ kip-in.}$$

From AISC *Manual* Table 9-2a:

$$S_c = 8.03 \text{ in.}^3$$

$$M_y = F_yS_c$$ (*Manual* Eq. 9-16)
$$= (50 \text{ ksi})(8.03 \text{ in.}^3)$$
$$= 402 \text{ kip-in.}$$

$$M_n = M_p - (M_p - M_y)\left(\frac{\lambda}{\lambda_p} - 1\right)$$ (*Manual* Eq. 9-11)
$$= 700 \text{ kip-in.} - (700 \text{ kip-in.} - 402 \text{ kip-in.})\left[\left(\frac{33.6}{27.3}\right) - 1\right]$$
$$= 631 \text{ kip-in.}$$

$$R_n = \frac{M_n}{e}$$ (from *Manual* Eq. 9-9)
$$= \frac{631 \text{ kip-in.}}{5.50 \text{ in.}}$$
$$= 115 \text{ kips}$$

The available strength of the coped section is:

---

# IIA-106

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b R_n = 0.90(115 \text{ kips})$ | $\frac{R_n}{\Omega_b} = \frac{115 \text{ kips}}{1.67}$ |
| $= 104 \text{ kips} > 25.0 \text{ kips} \quad \textbf{o.k.}$ | $= 68.9 \text{ kips} > 16.7 \text{ kips} \quad \textbf{o.k.}$ |

**Beam B Connection:**

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(18.3 \text{ kips}) + 1.6(55 \text{ kips})$ | $R_a = 18.3 \text{ kips} + 55 \text{ kips}$ |
| $= 110 \text{ kips}$ | $= 73.3 \text{ kips}$ |

*Available Angle Strength*

AISC *Manual* Table 10-1a includes checks for the limit states of shear yielding, shear rupture, and block shear rupture of the angles.

Use 5 rows of ¾-in.-diameter bolts in standard holes and 2L5×3½×¼ (SLBB). From AISC *Manual* Table 10-1a:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 148 \text{ kips} > 110 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 98.7 \text{ kips} > 73.3 \text{ kips} \quad \textbf{o.k.}$ |

*Available Shear Transfer Strength at Bolt Holes at Beam Web*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength determined in accordance with AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the angles at the bolt hole, and (3) the available bearing or tearout strength of the beam web at the bolt hole.

From AISC *Manual* Table 10-1b, the available bolt shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9 \text{ kips}$ | $\frac{r_n}{\Omega} = 11.9 \text{ kips}$ |

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the angle per bolt for ¾-in.-diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): | For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): |
| $\phi r_n = (49.4 \text{ kips/in.})(1/4 \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kips/in.})(1/4 \text{ in.})$ |
| $= 12.4 \text{ kips}$ | $= 8.23 \text{ kips}$ |

---

# IIA-107

| LRFD | ASD |
|------|-----|
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kips/in.})(1/4 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(1/4 \text{ in.})$ |
| $= 22.0 \text{ kips}$ | $= 14.6 \text{ kips}$ |

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the beam web per bolt for ¾-in.- diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the edge bolt ($l_{ev} = 2$ in.): | For the edge bolt ($l_{ev} = 2$ in.): |
| $\phi r_n = (87.8 \text{ kips/in.})(0.380 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(0.380 \text{ in.})$ |
| $= 33.4 \text{ kips}$ | $= 22.2 \text{ kips}$ |
| | |
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kips/in.})(0.380 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(0.380 \text{ in.})$ |
| $= 33.4 \text{ kips}$ | $= 22.2 \text{ kips}$ |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by two because the bolts are in double shear), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by two because there are two angles), and the available bearing and tearout strength of the beam web for an edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min\begin{cases}(17.9 \text{ kips})(2) = 35.8 \text{ kips,}\\(22.0 \text{ kips})(2) = 44.0 \text{ kips,}\\33.4 \text{ kips}\end{cases}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{cases}(11.9 \text{ kips})(2) = 23.8 \text{ kips,}\\(14.6 \text{ kips})(2) = 29.2 \text{ kips,}\\22.2 \text{ kips}\end{cases}$ |
| $= 33.4 \text{ kips}$ | $= 22.2 \text{ kips}$ |

At the middle connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by two because the bolts are in double shear), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by 2 because there are two angles), and available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,mid} = \min\begin{cases}(17.9 \text{ kips})(2) = 35.8 \text{ kips,}\\(22.0 \text{ kips})(2) = 44.0 \text{ kips,}\\33.4 \text{ kips}\end{cases}$ | $\frac{r_{n,mid}}{\Omega} = \min\begin{cases}(11.9 \text{ kips})(2) = 23.8 \text{ kips,}\\(14.6 \text{ kips})(2) = 29.2 \text{ kips,}\\22.2 \text{ kips}\end{cases}$ |
| $= 33.4 \text{ kips}$ | $= 22.2 \text{ kips}$ |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by two because the bolts are in double shear), the available bearing and tearout strength of the angles for an edge bolt (multiplied by two because there are two angles), and the available bearing and tearout strength of the beam web for a non-edge bolt:

---

# IIA-108

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min\begin{cases}(17.9 \text{ kips})(2) = 35.8 \text{ kips,}\\(12.4 \text{ kips})(2) = 24.8 \text{ kips,}\\33.4 \text{ kips}\end{cases}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{cases}(11.9 \text{ kips})(2) = 23.8 \text{ kips,}\\(8.23 \text{ kips})(2) = 16.5 \text{ kips,}\\22.2 \text{ kips}\end{cases}$ |
| $= 24.8 \text{ kips}$ | $= 16.5 \text{ kips}$ |

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi r_{n,top} + \phi r_{n,mid}(n - 2) + \phi r_{n,bot}$ | $\frac{R_n}{\Omega} = \frac{r_{n,top}}{\Omega} + \frac{r_{n,mid}}{\Omega}(n - 2) + \frac{r_{n,bot}}{\Omega}$ |
| $= 33.4 \text{ kips} + (33.4 \text{ kips})(5 - 2) + 24.8 \text{ kips}$ | $= 22.2 \text{ kips} + (22.2 \text{ kips})(5 - 2) + 16.5 \text{ kips}$ |
| $= 158 \text{ kips} > 110 \text{ kips} \quad \textbf{o.k.}$ | $= 105 \text{ kips} > 73.3 \text{ kips} \quad \textbf{o.k.}$ |

*Coped Beam Strength*

From AISC *Manual* Part 9, the available coped beam web strength for top cope only is the lesser of the limit states of flexural local web buckling and block shear rupture.

*Beam Web Available Shear Strength*

AISC *Manual* Table 10-1c includes checks for the limit states of block shear rupture of the beam web.

From AISC *Manual* Table 10-1c, with ¾-in.-diameter bolts in standard holes:

| LRFD | ASD |
|------|-----|
| For the top edge hole (conservatively assuming $l_{ev,t} = 1\frac{1}{2}$ in.): | For the top edge hole (conservatively assuming $l_{ev,t} = 1\frac{1}{2}$ in.): |
| $\phi r_n = 31.1 \text{ kips/in.}$ | $\frac{r_n}{\Omega} = 20.7 \text{ kips/in.}$ |
| | |
| For the center holes ($s = 3$ in.): | For the center holes ($s = 3$ in.): |
| $\phi r_n = 62.2 \text{ kips/in.}$ | $\frac{r_n}{\Omega} = 41.4 \text{ kips/in.}$ |
| | |
| For the bottom edge hole (conservatively assuming $l_{eb} = 1\frac{1}{2}$ in.): | For the bottom edge hole (conservatively assuming $l_{eb} = 1\frac{1}{2}$ in.): |
| $\phi r_n = 39.6 \text{ kips/in.}$ | $\frac{r_n}{\Omega} = 26.4 \text{ kips/in.}$ |
| | |
| $\phi R_n = [31.1 \text{ kips/in.} + 4(62.2 \text{ kips/in.}) + 39.6 \text{ kips/in.}]$ | $\frac{R_n}{\Omega} = [20.7 \text{ kips/in.} + 4(41.4 \text{ kips/in.}) + 26.4 \text{ kips/in.}]$ |
| $\times(0.380 \text{ in.})$ | $\times(0.380 \text{ in.})$ |
| $= 121 \text{ kips} > 110 \text{ kips} \quad \textbf{o.k.}$ | $= 80.8 \text{ kips} > 73.3 \text{ kips} \quad \textbf{o.k.}$ |

---

# IIA-109

*Flexural local web buckling of beam web*

The limit states of flexural yielding and local web buckling of the coped beam web are checked using AISC *Manual* Part 9 as follows:

$$e = c + setback$$
$$= 5 \text{ in.} + \frac{1}{2} \text{ in.}$$
$$= 5.50 \text{ in.}$$

From the geometry shown in AISC *Manual* Figure 9-2:

$$h_c = d - d_c$$
$$= 20.8 \text{ in.} - 2 \text{ in.}$$
$$= 18.8 \text{ in.}$$

$$\frac{c}{d} = \frac{5 \text{ in.}}{20.8 \text{ in.}}$$
$$= 0.240$$

$$\frac{c}{h_c} = \frac{5 \text{ in.}}{18.8 \text{ in.}}$$
$$= 0.266$$

Because $\frac{c}{d} \leq 1.0$, the buckling adjustment factor, $f$, is calculated as follows:

$$f = 2\left(\frac{c}{d}\right)$$ (*Manual* Eq. 9-20a)
$$= 2(0.240)$$
$$= 0.480$$

Because $\frac{c}{h_c} \leq 1.0$, the plate buckling coefficient, $k$, is calculated as follows:

$$k = 2.2\left(\frac{h_c}{c}\right)^{1.65}$$ (*Manual* Eq. 9-19a)
$$= 2.2\left(\frac{18.8 \text{ in.}}{5 \text{ in.}}\right)^{1.65}$$
$$= 19.6$$

$$\lambda = \frac{h_c}{t_w}$$ (*Manual* Eq. 9-17)
$$= \frac{18.8 \text{ in.}}{0.380 \text{ in.}}$$
$$= 49.5$$

---

# IIA-110

$$k_1 = fk \geq 1.61$$ (*Manual* Eq. 9-14)
$$= (0.480)(19.6) \geq 1.61$$
$$= 9.41 > 1.61$$

$$\lambda_p = 0.475\sqrt{\frac{k_1E}{F_y}}$$ (*Manual* Eq. 9-18)
$$= 0.475\sqrt{\frac{(9.41)(29,000 \text{ ksi})}{50 \text{ ksi}}}$$
$$= 35.1$$

$$2\lambda_p = 2(35.1)$$
$$= 70.2$$

Because $\lambda_w < \lambda \leq 2\lambda_p$, calculate the nominal flexural strength using AISC *Manual* Equation 9-11.

The plastic section modulus of the coped section, $Z_c$, is determined from AISC *Manual* Table 9-2b:

$$Z_c = 56.5 \text{ in.}^3$$

$$M_p = F_yZ_c$$ (*Manual* Eq. 9-15)
$$= (50 \text{ ksi})(56.5 \text{ in.}^3)$$
$$= 2,830 \text{ kip-in.}$$

From AISC *Manual* Table 9-2a:

$$S_c = 32.5 \text{ in.}^3$$

$$M_y = F_yS_c$$ (*Manual* Eq. 9-16)
$$= (50 \text{ ksi})(32.5 \text{ in.}^3)$$
$$= 1,630 \text{ kip-in.}$$

$$M_n = M_p - (M_p - M_y)\left(\frac{\lambda}{\lambda_p} - 1\right)$$ (*Manual* Eq. 9-11)
$$= 2,830 \text{ kip-in.} - (2,830 \text{ kip-in.} - 1,630 \text{ kip-in.})\left[\left(\frac{49.5}{35.1}\right) - 1\right]$$
$$= 2,340 \text{ kip-in.}$$

$$R_n = \frac{M_n}{e}$$ (from *Manual* Eq. 9-9)
$$= \frac{2,340 \text{ kip-in.}}{5.50 \text{ in.}}$$
$$= 425 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |

---

# IIA-111

| LRFD | ASD |
|------|-----|
| $\phi_b R_n = 0.90(425 \text{ kips})$ | $\frac{R_n}{\Omega_b} = \frac{425 \text{ kips}}{1.67}$ |
| $= 383 \text{ kips} > 110 \text{ kips} \quad \textbf{o.k.}$ | $= 254 \text{ kips} > 73.3 \text{ kips} \quad \textbf{o.k.}$ |

**Supporting Girder Connection**

*Supporting Girder Web*

The required effective strength per bolt is the minimum from the limit states of bolt shear and bolt bearing and tearout. The bolts that are loaded by both connections will have the largest demand. Thus, for the design of these four critical bolts, the required strength is determined as follows:

| LRFD | ASD |
|------|-----|
| From the W12×40 beam, each bolt must support one-fourth of 25.0 kips or 6.25 kips/bolt. | From the W12×40 beam, each bolt must support one-fourth of 16.7 kips or 4.18 kips/bolt. |
| From the W21×50 beam, each bolt must support one-tenth of 110 kips or 11.0 kips/bolt. | From the W21×50 beam, each bolt must support one-tenth of 73.3 kips or 7.33 kips/bolt. |

The required strength for each of the shared bolts is:

| LRFD | ASD |
|------|-----|
| $R_u = 6.25 \text{ kips/bolt} + 11.0 \text{ kips/bolt}$ | $R_a = 4.18 \text{ kips/bolt} + 7.33 \text{ kips/bolt}$ |
| $= 17.3 \text{ kips/bolt}$ | $= 11.5 \text{ kips/bolt}$ |

The available bolt shear strength and available tearout strength of the angles was previously found to be acceptable. From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the girder web per bolt for ¾-in.- diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kip/in.})(0.520 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(0.520 \text{ in.})$ |
| $= 45.7 \text{ kips/bolt} > 17.3 \text{ kips/bolt} \quad \textbf{o.k.}$ | $= 30.4 \text{ kips/bolt} > 11.5 \text{ kips/bolt} \quad \textbf{o.k.}$ |

*Conclusion*

The connection is found to be adequate as given for the applied loads.

---

# IIA-112

# EXAMPLE II.A-9 OFFSET ALL-BOLTED DOUBLE-ANGLE CONNECTIONS (BEAMS-TO-GIRDER WEB)

## Given:

Verify the all-bolted double-angle connections for back-to-back ASTM A992/A992M W16×45 beams to an ASTM A992/A992M W18×50 girder web to support the end reactions shown in Figure II.A-9-1. The beam centerlines are offset 6 in., and the beam connections share a vertical row of bolts. Use ASTM A572/A572M Grade 50 angles. The strength of the W16×45 beams and angles are verified in Example II.A-4 and are not repeated here.

<div style="text-align: center;">
<img src="connection_diagram" alt="Part plan showing:
- Beam A (W16×45): R_D = 10 kips, R_L = 30 kips
- Beam B (W16×45): R_D = 10 kips, R_L = 30 kips
- Girder: W18×50
- Offset D = 6"

Section E-E (bolts on same gage) showing:
- c = 4½" on both sides
- d_c = 1¼"
- Connection details with angles
- ½" setback (typ.)

Section F-F (bolts on same gage) showing:
- ¾" dia. Group 120, thread condition N
- SSL holes in angles
- STD holes in beam web
- Connection arrangement details">
</div>

*Fig. II.A-9-1. Connection geometry for Example II.A-9.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

Beams and girder
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

Angles
ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

---

# IIA-113

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Girder
W18×50
$d = 18.0$ in.
$t_w = 0.355$ in.

Beam
W16×45
$d = 16.1$ in.
$t_w = 0.345$ in.

Modify the 2L5×3½×¼ SLBB connection designed in Example II.A-4 to work in the configuration shown in Figure II.A-9-1. The offset dimension (6 in.) is approximately equal to the gage on the support from the previous example (6¼ in.) and, therefore, is not recalculated.

Thus, the available strength of the middle vertical row of bolts (through both connections) that carry a portion of the reaction for both connections must be verified for this configuration.

From ASCE/SEI 7, Chapter 2, the required strength of the Beam A and Beam B connections to the girder web is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(10 \text{ kips}) + 1.6(30 \text{ kips})$ | $R_a = 10 \text{ kips} + 30 \text{ kips}$ |
| $= 60.0 \text{ kips}$ | $= 40.0 \text{ kips}$ |

In the girder web connection, each bolt will have the same effective strength; therefore, check the individual bolt effective strength. At the middle vertical row of bolts, the required strength for one bolt is the sum of the required shear strength per bolt for each connection.

| LRFD | ASD |
|------|-----|
| $r_u = (2 \text{ sides})\left(\frac{60.0 \text{ kips}}{6 \text{ bolts}}\right)$ | $r_a = (2 \text{ sides})\left(\frac{40.0 \text{ kips}}{6 \text{ bolts}}\right)$ |
| $= 20.0 \text{ kips/bolt (for middle vertical row)}$ | $= 13.3 \text{ kips/bolt (for middle vertical row)}$ |

*Bolt Shear*

From AISC *Manual* Table 7-1, the available shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) in double shear is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 35.8 \text{ kips/bolt} > 20.0 \text{ kips/bolt} \quad \textbf{o.k.}$ | $\frac{r_n}{\Omega} = 23.9 \text{ kips/bolt} > 13.3 \text{ kips/bolt} \quad \textbf{o.k.}$ |

*Bearing on the Girder Web*

The available bearing strength per bolt is determined from AISC *Manual* Table 7-4 with $s = 3$ in.

| LRFD | ASD |
|------|-----|
| $\phi r_n = (87.8 \text{ kip/in.})(0.355 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(0.355 \text{ in.})$ |
| $= 31.2 \text{ kips/bolt} > 20.0 \text{ kips/bolt} \quad \textbf{o.k.}$ | $= 20.8 \text{ kips/bolt} > 13.3 \text{ kips/bolt} \quad \textbf{o.k.}$ |

---

# IIA-114

Note: If the bolts are not spaced equally from the supported beam web, the force in each column of bolts should be determined by using a simple beam analogy between the bolts and applying the laws of statics.

*Conclusion*

The connections are found to be adequate as given for the applied loads.

---

# IIA-115

# EXAMPLE II.A-10 SKEWED DOUBLE BENT-PLATE CONNECTION (BEAM-TO-GIRDER WEB)

## Given:

Design the skewed double bent-plate connection between an ASTM A992/A992M W16×77 beam and ASTM A992/A992M W27×94 girder web to support the following beam end reactions:

$R_D = 13.3 \text{ kips}$
$R_L = 40 \text{ kips}$

Use 70-ksi electrodes and ASTM A572/A572M Grade 50 plates. The final design is shown in Figure II.A-10-1.

<div style="text-align: center;">
<img src="connection_diagram" alt="Multi-view diagram showing:

(a) Plan view:
- W27×94(-4) girder
- W16×77 beam
- 16°-9¾" dimension
- 7'-6" length
- 12° angle
- 6" offset

(b) Section A showing:
- W16×77 beam
- 1¼" dimension
- ¾" typical
- 1⅛" dimension
- PL⅝×8½×6⅛ NS(B)
- PL⅝×8½×7¼ FS(A)
- Bent plate configuration

(c) Detail showing:
- 2¼" and 3¾" dimensions
- ⅝" and ¾" measurements
- ⅞" dia. Group 120, thread condition N
- std. holes in girder
- SSL holes in plates
- R = ⅝"
- 12° and 6° angles

(d) Force diagram showing:
- C.G. location
- R_u force
- al dimension
- kl = 2½"
- (al + xl) = 3⅝"
- 8½" total width">
</div>

*Fig. II.A-10-1. Skewed double bent-plate connection (beam-to-girder web).*

---

# IIA-116

## Solution:

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Beam and girder
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

Plate
ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W16×77
$d = 16.5$ in.
$t_w = 0.455$ in.

Girder
W27×94
$t_w = 0.490$ in.

From AISC *Specification* Table J3.3, for ⅞-in.-diameter bolts with standard holes:

$d_h = 15⁄16$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(13.3 \text{ kips}) + 1.6(40 \text{ kips})$ | $R_a = 13.3 \text{ kips} + 40 \text{ kips}$ |
| $= 80.0 \text{ kips}$ | $= 53.3 \text{ kips}$ |

From Figure II.A-10-1(c), assign load to each vertical row of bolts by assuming a simple beam analogy between bolts and applying the principles of statics.

| LRFD | ASD |
|------|-----|
| Required strength for bent plate A: | Required strength for bent plate A: |
| $R_u = \frac{(80.0 \text{ kips})(2\frac{1}{4} \text{ in.})}{6.00 \text{ in.}}$ | $R_a = \frac{(53.3 \text{ kips})(2\frac{1}{4} \text{ in.})}{6.00 \text{ in.}}$ |
| $= 30.0 \text{ kips}$ | $= 20.0 \text{ kips}$ |
| Required strength for bent plate B: | Required strength for bent plate B: |
| $R_u = 80.0 \text{ kips} - 30.0 \text{ kips}$ | $R_a = 53.3 \text{ kips} - 20.0 \text{ kips}$ |
| $= 50.0 \text{ kips}$ | $= 33.3 \text{ kips}$ |

Assume that the welds across the top and bottom of the plates will be 2½ in. long, and that the load acts at the intersection of the beam centerline and the support face.

---

# IIA-117

While the welds do not coincide on opposite faces of the beam web and the weld groups are offset, the locations of the weld groups will be averaged and considered identical. See Figure II.A-10-1(d).

*Weld Design*

Assume a plate length of $l = 8\frac{1}{2}$ in.

$$k = \frac{kl}{l}$$
$$= \frac{2\frac{1}{2} \text{ in.}}{8\frac{1}{2} \text{ in.}}$$
$$= 0.294$$

Interpolating from AISC *Manual* Table 8-8, with angle = 0° and $k = 0.294$,

$$x = 0.0544$$

$$xl = (0.0544)(8\frac{1}{2} \text{ in.})$$
$$= 0.462 \text{ in.}$$

$$a = \frac{(al + xl) - xl}{l}$$
$$= \frac{3\frac{5}{8} \text{ in} - 0.462 \text{ in.}}{8\frac{1}{2} \text{ in.}}$$
$$= 0.372$$

Interpolating from AISC *Manual* Table 8-8, with $\theta = 0°$, $a = 0.372$, and $k = 0.294$,

$$C = 2.52$$

The required weld size is determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $D_{req} = \frac{R_u}{\phi CC_1l}$ | $D_{req} = \frac{\Omega R_u}{CC_1l}$ |
| $= \frac{50.0 \text{ kips}}{0.75(2.52)(1.0)(8\frac{1}{2} \text{ in})}$ | $= \frac{2.00(33.3 \text{ kips})}{2.52(1.0)(8\frac{1}{2} \text{ in})}$ |
| $= 3.11 \text{ sixteenths}$ | $= 3.11 \text{ sixteenths}$ |

Use ¼ in. fillet welds and at least 5⁄16-in.-thick bent plates to allow for the welds.

*Beam Web Strength at Fillet Weld*

The minimum beam web thickness required to match the shear rupture strength of the weld to that of the base metal is:

---

# IIA-118

$$t_{min} = \frac{6.19D_{min}}{F_u}$$ (from *Manual* Eq. 9-7)
$$= \frac{6.19(3.11)}{65 \text{ ksi}}$$
$$= 0.296 \text{ in.} < 0.455 \text{ in.} \quad \textbf{o.k.}$$

*Available Shear Transfer Strength at Bolt Holes at Girder Web*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength determined in accordance with AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the plate at the bolt hole determined in accordance with AISC *Specification* Section J3.11a, and (3) the available bearing or tearout strength of the girder web at the bolt hole determined in accordance with AISC *Specification* Section J3.11a.

From AISC *Manual* Table 10-1b, the available bolt shear strength per bolt for ⅞-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 24.3 \text{ kips}$ | $\frac{r_n}{\Omega} = 16.2 \text{ kips}$ |

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the plate per bolt for ⅞-in.-diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): | For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): |
| $\phi r_n = (45.7 \text{ kip/in.})(5⁄16 \text{ in.})$ | $\frac{r_n}{\Omega} = (30.5 \text{ kip/in.})(5⁄16 \text{ in.})$ |
| $= 14.3 \text{ kips}$ | $= 9.53 \text{ kips}$ |
| | |
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (102 \text{ kip/in.})(5⁄16 \text{ in.})$ | $\frac{r_n}{\Omega} = (68.3 \text{ kip/in.})(5⁄16 \text{ in.})$ |
| $= 31.9 \text{ kips}$ | $= 21.3 \text{ kips}$ |

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the girder web per bolt for ⅞-in.- diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (102 \text{ kip/in.})(0.490 \text{ in.})$ | $\frac{r_n}{\Omega} = (68.3 \text{ kip/in.})(0.490 \text{ in.})$ |
| $= 50.0 \text{ kips}$ | $= 33.5 \text{ kips}$ |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the plate for an edge bolt, and the available bearing and tearout strength of the girder web for a non-edge bolt:

---

# IIA-119

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min\begin{cases}24.3 \text{ kips,}\\14.3 \text{ kips,}\\50.0 \text{ kips}\end{cases}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{cases}16.2 \text{ kips,}\\9.53 \text{ kips,}\\33.5 \text{ kips}\end{cases}$ |
| $= 14.3 \text{ kips}$ | $= 9.53 \text{ kips}$ |

At the middle connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the plate for a non-edge bolt, and the available bearing and tearout strength of the girder web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,mid} = \min\begin{cases}24.3 \text{ kips,}\\31.9 \text{ kips,}\\50.0 \text{ kips}\end{cases}$ | $\frac{r_{n,mid}}{\Omega} = \min\begin{cases}16.2 \text{ kips,}\\21.3 \text{ kips,}\\33.5 \text{ kips}\end{cases}$ |
| $= 24.3 \text{ kips}$ | $= 16.2 \text{ kips}$ |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the plate for a non-edge bolt, and the available bearing and tearout strength of the girder web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min\begin{cases}24.3 \text{ kips,}\\31.9 \text{ kips,}\\50.0 \text{ kips}\end{cases}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{cases}16.2 \text{ kips,}\\21.3 \text{ kips,}\\33.5 \text{ kips}\end{cases}$ |
| $= 24.3 \text{ kips}$ | $= 16.2 \text{ kips}$ |

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi r_{n,top} + \phi r_{n,mid}(n - 2) + \phi r_{n,bot}$ | $\frac{R_n}{\Omega} = \frac{r_{n,top}}{\Omega} + \frac{r_{n,mid}}{\Omega}(n - 2) + \frac{r_{n,bot}}{\Omega}$ |
| $= 14.3 \text{ kips} + (24.3 \text{ kips})(3 - 2) + 24.3 \text{ kips}$ | $= 9.53 \text{ kips} + (16.2 \text{ kips})(3 - 2) + 16.2 \text{ kips}$ |
| $= 62.9 \text{ kips} > 50.0 \text{ kips} \quad \textbf{o.k.}$ | $= 41.9 \text{ kips} > 33.3 \text{ kips} \quad \textbf{o.k.}$ |

*Shear Strength of Plate*

From AISC *Specification* Section J4.2, the available shear yielding strength of bent plate B (see Figure II.A-10-1) is determined as follows:

$$A_{gv} = lt$$
$$= (8\frac{1}{2} \text{ in.})(5⁄16 \text{ in.})$$
$$= 2.66 \text{ in.}^2$$

$$R_n = 0.60F_yA_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(2.66 \text{ in.}^2)$$
$$= 79.8 \text{ kips}$$

---

# IIA-120

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
| $\phi R_n = 1.00(79.8 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{79.8 \text{ kips}}{1.50}$ |
| $= 79.8 \text{ kips} > 50.0 \text{ kips} \quad \textbf{o.k.}$ | $= 53.2 \text{ kips} > 33.3 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.2, the available shear rupture strength of bent plate B is determined as follows:

$$A_{nv} = [l - n(d_h + 1⁄16 \text{ in.})]t$$
$$= [8\frac{1}{2} \text{ in.} - 3(15⁄16 \text{ in.} + 1⁄16 \text{ in.})](5⁄16 \text{ in.})$$
$$= 1.72 \text{ in.}^2$$

$$R_n = 0.60F_uA_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(1.72 \text{ in.}^2)$$
$$= 67.1 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(67.1 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{67.1 \text{ kips}}{2.00}$ |
| $= 50.3 \text{ kips} > 50.0 \text{ kips} \quad \textbf{o.k.}$ | $= 33.6 \text{ kips} > 33.3 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture of Plate*

The nominal strength for the limit state of block shear rupture is given by AISC *Specification* Section J4.3.

$$R_n = 0.60F_uA_{nv} + U_{bs}F_uA_{nt} \leq 0.60F_yA_{gv} + U_{bs}F_uA_{nt}$$ (*Spec.* Eq. J4-5)

where

$$A_{gv} = (l - l_{ev})t$$
$$= (8\frac{1}{2} \text{ in.} - 1\frac{1}{4} \text{ in.})(5⁄16 \text{ in.})$$
$$= 2.27 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (n - 0.5)(d_h + 1⁄16 \text{ in.})t$$
$$= 2.27 \text{ in.}^2 - (3 - 0.5)(15⁄16 \text{ in.} + 1⁄16 \text{ in.})(5⁄16 \text{ in.})$$
$$= 1.49 \text{ in.}^2$$

$$A_{nt} = [l_{eh} - 0.5(d_h + 1⁄16 \text{ in.})]t$$
$$= [1\frac{1}{4} \text{ in.} - 0.5(15⁄16 \text{ in.} + 1⁄16 \text{ in.})](5⁄16 \text{ in.})$$
$$= 0.234 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

---

# IIA-121

$$R_{bsv} = 0.60(65 \text{ ksi})(1.49 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.234 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(2.27 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.234 \text{ in.}^2)$$
$$= 73.3 \text{ kips} < 83.3 \text{ kips}$$

Therefore:

$$R_{bsv} = 73.3 \text{ kips}$$

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture on bent-plate B is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_{bsv} = 0.75(73.3 \text{ kips})$ | $\frac{R_{bsv}}{\Omega} = \frac{73.3 \text{ kips}}{2.00}$ |
| $= 55.0 \text{ kips} > 50.0 \text{ kips} \quad \textbf{o.k.}$ | $= 36.7 \text{ kips} > 33.3 \text{ kips} \quad \textbf{o.k.}$ |

Thus, the configuration shown in Figure II.A-10-1 can be supported using 5⁄16 in. bent plates, and ¼ in. fillet welds.

---

# IIA-122

# EXAMPLE II.A-11A SHEAR END-PLATE CONNECTION (BEAM-TO-GIRDER WEB)

## Given:

Verify the available strength of a shear end-plate connection to connect an ASTM A992/A992M W18×50 beam to an ASTM A992/A992M W21×62 girder web, as shown in Figure II.A-11A-1, to support the following beam end reactions:

$R_D = 10 \text{ kips}$
$R_L = 30 \text{ kips}$

Use 70-ksi electrodes and ASTM A572/A572M Grade 50 plate.

This example is repeated using the following two procedures:

Part A: Determine the available connection strength using the tables in *Manual* Part 10.
Part B: Determine the available connection strength by checking individual limit states.

<div style="text-align: center;">
<img src="connection_diagram" alt="Connection diagram showing:
- W18×50 beam with end plate
- c = 4" cope dimension
- d_c = 1¼"
- 1¼" edge distances
- 3" bolt spacing
- 1¼" dimensions
- A-A section detail
- PL¼×6×0'-8½"
- ⅜" welds on both sides
- ¾" dia. Group 120, thread condition N, std. holes
- l_eh = 1¼"
- 6" gage
- Connection between W18×50 beam and support">
</div>

*Fig. II.A-11A-1. Connection geometry for Example II.A-11A.*

## Solution:

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Beam and girder
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

Plate
ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

From AISC *Manual* Table 1-1, the geometric properties are as follows:

---

# IIA-123

Beam
W18×50
$t_w = 0.355$ in.

Girder
W21×62
$t_w = 0.400$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(10 \text{ kips}) + 1.6(30 \text{ kips})$ | $R_a = 10 \text{ kips} + 30 \text{ kips}$ |
| $= 60.0 \text{ kips}$ | $= 40.0 \text{ kips}$ |

*Part A— Determine the Available Connection Strength Using the Tables in Manual Part 10*

*End-Plate Available Strength*

Tabulated values in AISC *Manual* Table 10-4a consider the limit states of shear rupture of the end plate and block shear rupture of the end plate.

From AISC *Manual* Table 10-4a, for three rows of ¾-in.-diameter bolts in standard holes and ¼ in. plate thickness:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 85.9 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 57.3 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

*Available Shear Transfer Strength at Bolt Holes*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength determined in accordance with AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the plate at the bolt hole determined in accordance with AISC *Specification* Section J3.11a, and (3) the available bearing or tearout strength of the support at the bolt hole determined in accordance with AISC *Specification* Section J3.11a.

From AISC *Manual* Table 10-4b, the available bolt shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) in single shear is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9 \text{ kips}$ | $\frac{r_n}{\Omega} = 11.9 \text{ kips}$ |

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the ¼ in. end plate per bolt for ¾-in.- diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): | For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): |
| $\phi r_n = (49.4 \text{ kips/in.})(1/4 \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kips/in.})(1/4 \text{ in.})$ |
| $= 12.4 \text{ kips}$ | $= 8.23 \text{ kips}$ |

---

# IIA-124

| LRFD | ASD |
|------|-----|
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kips/in.})(1/4 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(1/4 \text{ in.})$ |
| $= 22.0 \text{ kips}$ | $= 14.6 \text{ kips}$ |

Because the thickness of the girder web, $t_w = 0.400$ in., is greater than the thickness of the plate, $t = ¼$ in., bolt bearing and tearout will control for the plate.

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because there are two bolts per row) and the available bearing and tearout strength of the end plate for an edge bolt (multiplied by 2 because there are two bolts per row).

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min\begin{cases}(17.9 \text{ kips})(2) = 35.8 \text{ kips,}\\(12.4 \text{ kips})(2) = 24.8 \text{ kips}\end{cases}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{cases}(11.9 \text{ kips})(2) = 23.8 \text{ kips,}\\(8.23 \text{ kips})(2) = 16.5 \text{ kips}\end{cases}$ |
| $= 24.8 \text{ kips}$ | $= 16.5 \text{ kips}$ |

At the middle connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because there are two bolts per row) and the available bearing and tearout strength of the plate for a non-edge bolt (multiplied by 2 because there are two bolts per row):

| LRFD | ASD |
|------|-----|
| $\phi r_{n,mid} = \min\begin{cases}(17.9 \text{ kips})(2) = 35.8 \text{ kips,}\\(22.0 \text{ kips})(2) = 44.0 \text{ kips}\end{cases}$ | $\frac{r_{n,mid}}{\Omega} = \min\begin{cases}(11.9 \text{ kips})(2) = 23.8 \text{ kips,}\\(14.6 \text{ kips})(2) = 29.2 \text{ kips}\end{cases}$ |
| $= 35.8 \text{ kips}$ | $= 23.8 \text{ kips}$ |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because there are two bolts per row) and the available bearing and tearout strength of the plate for a non-edge bolt (multiplied by 2 because there are two bolts per row).

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min\begin{cases}(17.9 \text{ kips})(2) = 35.8 \text{ kips,}\\(21.9 \text{ kips})(2) = 43.8 \text{ kips}\end{cases}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{cases}(11.9 \text{ kips})(2) = 23.8 \text{ kips,}\\(14.6 \text{ kips})(2) = 29.2 \text{ kips}\end{cases}$ |
| $= 35.8 \text{ kips}$ | $= 23.8 \text{ kips}$ |

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi r_{n,top} + \phi r_{n,mid}(n - 2) + \phi r_{n,bot}$ | $\frac{R_n}{\Omega} = \frac{r_{n,top}}{\Omega} + \frac{r_{n,mid}}{\Omega}(n - 2) + \frac{r_{n,bot}}{\Omega}$ |
| $= 24.8 \text{ kips} + (35.8 \text{ kips})(3 - 2) + 35.8 \text{ kips}$ | $= 16.5 \text{ kips} + (23.8 \text{ kips})(3 - 2) + 23.8 \text{ kips}$ |
| $= 96.4 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $= 64.1 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

*Weld and Beam Web Available Strength*

Try 3⁄16 in. weld. From AISC *Manual* Table 10-4c, the minimum beam web thickness is:

---

# IIA-125

$$t_{w\,min} = 0.286 \text{ in.} < 0.355 \text{ in.} \quad \textbf{o.k.}$$

From AISC *Manual* Table 10-4c, the weld and beam web available strength is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 67.9 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 45.2 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

*Coped Beam Strength*

As was shown in Example II.A-4, the coped section does not control the design. **o.k.**

*Beam Web Shear Yielding*

As was shown in Example II.A-4, beam web shear does not control the design. **o.k.**

*Summary*

The available shear strength of the connection is controlled by weld and beam web available strength.

| LRFD | ASD |
|------|-----|
| $\phi R_n = 67.9 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 45.2 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

The connection is found to be adequate as given for the applied loads.

*Part B—Verify the Available Connection Strength by Checking Individual Limit States*

*Shear Strength of End Plate*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the end plate is determined as follows:

$$A_{gv} = 2lt$$
$$= 2(8\frac{1}{2} \text{ in.})(1/4 \text{ in.})$$
$$= 4.25 \text{ in.}^2$$

$$R_n = 0.60F_yA_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(4.25 \text{ in.}^2)$$
$$= 128 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
| $\phi R_n = 1.00(128 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{128 \text{ kips}}{1.50}$ |
| $= 128 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $= 85.3 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the end plate is determined using the net area determined in accordance with AISC *Specification* Section B4.3b.

---

# IIA-126

$$A_{nv} = 2[l - n(d_h + 1⁄16 \text{ in.})]t$$
$$= 2[8\frac{1}{2} \text{ in.} - 3(13⁄16 \text{ in.} + 1⁄16 \text{ in.})](1/4 \text{ in.})$$
$$= 2.94 \text{ in.}^2$$

$$R_n = 0.60F_uA_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(2.94 \text{ in.}^2)$$
$$= 115 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(115 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{115 \text{ kips}}{2.00}$ |
| $= 86.3 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $= 57.5 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture of End Plate*

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture of the end plate is determined as follows.

$$R_{bsv} = 0.60F_uA_{nv} + U_{bs}F_uA_{nt} \leq 0.60F_yA_{gv} + U_{bs}F_uA_{nt}$$ (from *Spec.* Eq. J4-5)

where

$$A_{gv} = 2(l - l_{ev})t$$
$$= 2(8\frac{1}{2} \text{ in.} - 1\frac{1}{4} \text{ in.})(1/4 \text{ in.})$$
$$= 3.63 \text{ in.}^2$$

$$A_{nv} = A_{gv} - 2(n - 0.5)(d_h + 1⁄16 \text{ in.})t$$
$$= 3.63 \text{ in.}^2 - 2(3 - 0.5)(13⁄16 \text{ in.} + 1⁄16 \text{ in.})(1/4 \text{ in.})$$
$$= 2.54 \text{ in.}^2$$

$$A_{nt} = 2[l_{eh} - 0.5(d_h + 1⁄16 \text{ in.})]t$$
$$= 2[1\frac{1}{4} \text{ in.} - 0.5(13⁄16 \text{ in.} + 1⁄16 \text{ in.})](1/4 \text{ in.})$$
$$= 0.406 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_{bsv} = 0.60(65 \text{ ksi})(2.54 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.406 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(3.63 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.406 \text{ in.}^2)$$
$$= 125 \text{ kips} < 135 \text{ kips}$$

Therefore:

$$R_{bsv} = 125 \text{ kips}$$

---

# IIA-127

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture of the end plate is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_{bsv} = 0.75(125 \text{ kips})$ | $\frac{R_{bsv}}{\Omega} = \frac{125 \text{ kips}}{2.00}$ |
| $= 93.8 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $= 62.5 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

*Available Shear Transfer Strength at Bolt Holes*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength determined in accordance with AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the end plate at the bolt hole determined in accordance with AISC *Specification* Section J3.11a, and (3) the available bearing or tearout strength of the support element at the bolt hole determined in accordance with AISC *Specification* Section J3.11a.

*Bolt shear*

From AISC *Manual* Table 7-1, the available shear strength for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) per pair of bolts is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9 \text{ kips}$ | $\frac{r_n}{\Omega} = 11.9 \text{ kips}$ |

The available bearing strength of the end plate is determined from AISC *Specification* Section J3.11, assuming deformation at service load is a design consideration:

$$r_n = 2.4dtF_u$$ (from *Spec.* Eq. J3-6a)
$$= (2.4)(3/4 \text{ in.})(1/4 \text{ in.})(65 \text{ ksi})$$
$$= 29.3 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(29.3 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{29.3 \text{ kips}}{2.00}$ |
| $= 22.0 \text{ kips}$ | $= 14.7 \text{ kips}$ |

The available tearout strength of the end plate is determined from AISC *Specification* Section J3.11, assuming deformation at service load is a design consideration.

For edge bolt tearout, the clear distance along the line of action of the force between the edge of the hole and the edge of the end plate is:

$$l_c = l_{ev} - 0.5d_h$$
$$= 1\frac{1}{4} \text{ in.} - 0.5(13⁄16 \text{ in.})$$
$$= 0.844 \text{ in.}$$

---

# IIA-128

The available tearout strength of the end plate at the edge bolt is:

$$r_n = 1.2l_ctF_u$$ (from *Spec.* Eq. J3-6c)
$$= (1.2)(0.844 \text{ in.})(1/4 \text{ in.})(65 \text{ ksi})$$
$$= 16.5 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(16.5 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{16.5 \text{ kips}}{2.00}$ |
| $= 12.4 \text{ kips}$ | $= 8.25 \text{ kips}$ |

For non-edge bolt tearout in the end plate, the clear distance is between bolt holes:

$$l_c = s - d_h$$
$$= 3 \text{ in.} - 13⁄16 \text{ in.}$$
$$= 2.19 \text{ in.}$$

The available tearout strength of the end plate at non-edge bolts is:

$$r_n = 1.2l_ctF_u$$ (from *Spec.* Eq. J3-6c)
$$= (1.2)(2.19 \text{ in.})(1/4 \text{ in.})(65 \text{ ksi})$$
$$= 42.7 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(42.7 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{42.7 \text{ kips}}{2.00}$ |
| $= 32.0 \text{ kips}$ | $= 21.4 \text{ kips}$ |

Because the thickness of the girder web, $t_w = 0.400$ in., is greater than the thickness of the plate, $t = ¼$ in., bolt bearing and tearout will control for the plate.

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because there are two bolts per row) and the available bearing and tearout strength of the end plate for an edge bolt (multiplied by 2 because there are two bolts per row).

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min\begin{cases}(17.9 \text{ kips})(2) = 35.8 \text{ kips,}\\(22.0 \text{ kips})(2) = 44.0 \text{ kips,}\\(12.4 \text{ kips})(2) = 24.8 \text{ kips}\end{cases}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{cases}(11.9 \text{ kips})(2) = 23.8 \text{ kips,}\\(14.7 \text{ kips})(2) = 29.4 \text{ kips,}\\(8.25 \text{ kips})(2) = 16.5 \text{ kips}\end{cases}$ |
| $= 24.8 \text{ kips}$ | $= 16.5 \text{ kips}$ |

At the middle connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because there are two bolts per row) and the available bearing and tearout strength of the end plate for a non-edge bolt (multiplied by 2 because there are two bolts per row):

---

# IIA-129

| LRFD | ASD |
|------|-----|
| $\phi r_{n,mid} = \min\begin{cases}(17.9 \text{ kips})(2) = 35.8 \text{ kips,}\\(22.0 \text{ kips})(2) = 44.0 \text{ kips,}\\(32.0 \text{ kips})(2) = 64.0 \text{ kips}\end{cases}$ | $\frac{r_{n,mid}}{\Omega} = \min\begin{cases}(11.9 \text{ kips})(2) = 23.8 \text{ kips,}\\(14.7 \text{ kips})(2) = 29.4 \text{ kips,}\\(21.4 \text{ kips})(2) = 42.8 \text{ kips}\end{cases}$ |
| $= 35.8 \text{ kips}$ | $= 23.8 \text{ kips}$ |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by 2 because there are two bolts per row) and the available bearing and tearout strength of the end plate for a non-edge bolt (multiplied by 2 because there are two bolts per row).

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min\begin{cases}(17.9 \text{ kips})(2) = 35.8 \text{ kips,}\\(22.0 \text{ kips})(2) = 44.0 \text{ kips,}\\(32.0 \text{ kips})(2) = 64.0 \text{ kips}\end{cases}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{cases}(11.9 \text{ kips})(2) = 23.8 \text{ kips,}\\(14.7 \text{ kips})(2) = 29.4 \text{ kips,}\\(21.4 \text{ kips})(2) = 42.8 \text{ kips}\end{cases}$ |
| $= 35.8 \text{ kips}$ | $= 23.8 \text{ kips}$ |

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi r_{n,top} + \phi r_{n,mid}(n - 2) + \phi r_{n,bot}$ | $\frac{R_n}{\Omega} = \frac{r_{n,top}}{\Omega} + \frac{r_{n,mid}}{\Omega}(n - 2) + \frac{r_{n,bot}}{\Omega}$ |
| $= 24.8 \text{ kips} + 35.8 \text{ kips}(3 - 2) + 35.8 \text{ kips}$ | $= 16.5 \text{ kips} + 23.8 \text{ kips}(3 - 2) + 23.8 \text{ kips}$ |
| $= 96.4 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $= 64.1 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

*Weld Strength*

The available weld strength is determined as follows. The effective weld length equals the end-plate length minus twice the weld size.

$$l_w = 8\frac{1}{2} \text{ in.} - 2(5⁄16 \text{ in.})$$
$$= 8.13 \text{ in.}$$

| LRFD | ASD |
|------|-----|
| $\phi R_n = 2(1.392 \text{ kips/in.})Dl_w$ | $\frac{R_n}{\Omega} = 2(0.928 \text{ kips/in.})Dl_w$ |
| $= 2(1.392 \text{ kips/in.})(3)(8.13 \text{ in.})$ | $= 2(0.928 \text{ kips/in.})(3)(8.13 \text{ in.})$ |
| $= 67.9 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $= 45.3 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

*Summary*

The available shear strength of the connection is controlled by the available weld strength.

| LRFD | ASD |
|------|-----|
| $\phi R_n = 67.9 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 45.3 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

The connection is found to be adequate as given for the applied loads.

---

# IIA-130

# EXAMPLE II.A-11B END-PLATE CONNECTION SUBJECT TO AXIAL AND SHEAR LOADING

## Given:

Verify the available strength of an end-plate connection for an ASTM A992/A992M W18×50 beam, as shown in Figure II.A-11B-1, to support the following beam end reactions:

| LRFD | ASD |
|------|-----|
| Shear, $V_u = 75 \text{ kips}$ | Shear, $V_a = 50 \text{ kips}$ |
| Axial tension, $N_u = 60 \text{ kips}$ | Axial tension, $N_a = 40 \text{ kips}$ |

Use 70-ksi electrodes and ASTM A572/A572M Grade 50 plate.

<div style="text-align: center;">
<img src="connection_diagram" alt="Connection diagram showing:
- W18×50 beam
- End plate connection with dimensions
- 1⅛" top dimension
- 4@3" = 1'-0" vertical spacing
- Gage = 5⅝"
- 1¼" bottom dimension
- ⅝" dia. Group 120, thread condition N, std. holes
- PL½×8½×1'-2½"
- Vertical load V and axial load N indicated
- ⅜" welds on both sides">
</div>

*Fig. II.A-11B-1. Connection geometry for Example II.A-11B.*

## Solution:

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Beam
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

Plate
ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

From AISC *Manual* Table 1-1, the geometric properties are as follows:

---

# IIA-131

Beam
W18×50
$A_g = 14.7 \text{ in.}^2$
$d = 18.0$ in.
$t_w = 0.355$ in.

From AISC *Specification* Table J3.3, for ⅞-in.-diameter bolts with standard holes:

$d_h = 15⁄16$ in.

The resultant load is:

| LRFD | ASD |
|------|-----|
| $R_u = \sqrt{V_u^2 + N_u^2}$ | $R_a = \sqrt{V_a^2 + N_a^2}$ |
| $= \sqrt{(75 \text{ kips})^2 + (60 \text{ kips})^2}$ | $= \sqrt{(50 \text{ kips})^2 + (40 \text{ kips})^2}$ |
| $= 96.0 \text{ kips}$ | $= 64.0 \text{ kips}$ |

The connection will first be checked for the shear load. The following bolt shear and bearing and tearout calculations are for a pair of bolts.

*Bolt Shear*

From AISC *Manual* Table 7-1, the available shear strength for ⅞-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) in double shear, or pair of bolts in this example, is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 48.7 \text{ kips/pair of bolts}$ | $\frac{r_n}{\Omega} = 32.5 \text{ kips/pair of bolts}$ |

*Bolt Bearing on the Plate*

The nominal bearing strength of the plate is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration:

$$r_n = 2.4dtF_u$$ (from *Spec.* Eq. J3-6a)
$$= (2.4)(7/8 \text{ in.})(1/2 \text{ in.})(65 \text{ ksi})$$
$$= 68.3 \text{ kips}$$

From AISC *Specification* Section J3.11a, the available bearing strength of the plate for a pair of bolts is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(2)(68.3 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{(2)(68.3 \text{ kips})}{2.00}$ |
| $= 102 \text{ kips/pair of bolts}$ | $= 68.3 \text{ kips/pair of bolts}$ |

*Bolt Tearout on the Plate*

The available tearout strength of the plate is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration. For the top edge bolts:

---

# IIA-132

$$l_c = l_e - 0.5d_h$$
$$= 1\frac{1}{4} \text{ in.} - 0.5(15⁄16 \text{ in.})$$
$$= 0.781 \text{ in.}$$

$$r_n = 1.2l_ctF_u$$ (from *Spec.* Eq. J3-6c)
$$= (1.2)(0.781 \text{ in.})(1/2 \text{ in.})(65 \text{ ksi})$$
$$= 30.5 \text{ kips}$$

The available bolt tearout strength for the pair of top edge bolts is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(2)(30.5 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{(2)(30.5 \text{ kips})}{2.00}$ |
| $= 45.8 \text{ kips/pair of bolts}$ | $= 30.5 \text{ kips/pair of bolts}$ |

Tearout controls over bolt shear and bearing strength for the top edge bolts in the plate.

For interior bolts:

$$l_c = s - d_h$$
$$= 3.00 \text{ in.} - 15⁄16 \text{ in.}$$
$$= 2.06 \text{ in.}$$

$$r_n = 1.2l_ctF_u$$ (from *Spec.* Eq. J3-6c)
$$= (1.2)(2.06 \text{ in.})(1/2 \text{ in.})(65 \text{ ksi})$$
$$= 80.3 \text{ kips}$$

The available bolt tearout strength for a pair of interior bolts is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(2)(80.3 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{(2)(80.3 \text{ kips})}{2.00}$ |
| $= 120 \text{ kips/pair of bolts}$ | $= 80.3 \text{ kips/pair of bolts}$ |

Bolt shear controls over tearout and bearing strength for the interior bolts in the plate.

*Shear Strength of Bolted Connection*

| LRFD | ASD |
|------|-----|
| $\phi R_n = (1 \text{ row})(45.8 \text{ kips/pair of bolts})$ | $\frac{R_n}{\Omega} = (1 \text{ row})(30.5 \text{ kips/pair of bolts})$ |
| $+ (4 \text{ rows})(48.7 \text{ kips/pair of bolts})$ | $+ (4 \text{ rows})(32.5 \text{ kips/pair of bolts})$ |
| $= 241 \text{ kips} > 75 \text{ kips} \quad \textbf{o.k.}$ | $= 161 \text{ kips} > 50 \text{ kips} \quad \textbf{o.k.}$ |

---

# IIA-133

*Bolt Shear and Tension Interaction*

The available strength of the bolts due to the effect of combined tension and shear is determined from AISC *Specification* Section J3.8. The required shear stress is:

$$f_{rv} = \frac{V_r}{nA_b}$$

where
$A_b = 0.601 \text{ in.}^2$ (from *Manual* Table 7-1)
$n = 10 \text{ bolts}$

| LRFD | ASD |
|------|-----|
| $f_{rv} = \frac{75 \text{ kips}}{10(0.601 \text{ in.}^2)}$ | $f_{rv} = \frac{50 \text{ kips}}{10(0.601 \text{ in.}^2)}$ |
| $= 12.5 \text{ ksi}$ | $= 8.32 \text{ ksi}$ |

The nominal tensile stress modified to include the effects of shear stress is determined from AISC *Specification* Section J3.8 as follows. From AISC *Specification* Table J3.2:

$F_{nt} = 90 \text{ ksi}$
$F_{nv} = 54 \text{ ksi}$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $F'_{nt} = 1.3F_{nt} - \frac{F_{nt}}{\phi F_{nv}}f_{rv} \leq F_{nt}$ (*Spec.* Eq. J3-3a) | $F'_{nt} = 1.3F_{nt} - \frac{\Omega F_{nt}}{F_{nv}}f_{rv} \leq F_{nt}$ (*Spec.* Eq. J3-3b) |
| $= 1.3(90 \text{ ksi}) - \frac{90 \text{ ksi}}{0.75(54 \text{ ksi})}(12.5 \text{ ksi}) \leq 90 \text{ ksi}$ | $= 1.3(90 \text{ ksi}) - \frac{2.00(90 \text{ ksi})}{54 \text{ ksi}}(8.32 \text{ ksi}) \leq 90 \text{ ksi}$ |
| $= 89.2 \text{ ksi} < 90 \text{ ksi} \quad \textbf{o.k.}$ | $= 89.3 \text{ ksi} < 90 \text{ ksi} \quad \textbf{o.k.}$ |

Using the value of $F'_{nt} = 89.2 \text{ ksi}$ determined for LRFD, the nominal tensile strength of one bolt is:

$$r_n = F'_{nt}A_b$$ (from *Spec.* Eq. J3-2)
$$= (89.2 \text{ ksi})(0.601 \text{ in.}^2)$$
$$= 53.6 \text{ kips}$$

The available tensile strength due to combined tension and shear is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_n = 0.75(53.6 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{53.6 \text{ kips}}{2.00}$ |
| $= 40.2 \text{ kips/bolt}$ | $= 26.8 \text{ kips/bolt}$ |

---

# IIA-134

| LRFD | ASD |
|------|-----|
| $\phi R_n = n\phi r_n$ | $\frac{R_n}{\Omega} = n\frac{r_n}{\Omega}$ |
| $= (10 \text{ bolts})(40.2 \text{ kips/bolt})$ | $= (10 \text{ bolts})(26.8 \text{ kips/bolt})$ |
| $= 402 \text{ kips} > 60 \text{ kips} \quad \textbf{o.k.}$ | $= 268 \text{ kips} > 40 \text{ kips} \quad \textbf{o.k.}$ |

*Prying Action*

From AISC *Manual* Part 9, the available tensile strength of the bolts in the end plate taking prying action into account is determined as follows:

$$b = \frac{\text{gage} - t_w}{2}$$
$$= \frac{5\frac{1}{2} \text{ in.} - 0.355 \text{ in.}}{2}$$
$$= 2.57 \text{ in.}$$

$$a = \frac{width\;of\;plate - gage}{2} \leq 1.25b$$
$$= \frac{8\frac{1}{2} \text{ in.} - 5\frac{1}{2} \text{ in.}}{2} < 1.25(1.50 \text{ in.})$$
$$= 1.50 \text{ in.} < 1.88 \text{ in.}$$
$$= 1.50 \text{ in.}$$

Note: If $a$ at the supporting element is smaller than $a = 1.50$ in., use the smaller $a$ in the preceding calculations.

$$a' = a + \frac{d}{2}$$ (*Manual* Eq. 9-23)
$$= 1.50 \text{ in.} + \frac{7/8 \text{ in.}}{2}$$
$$= 1.94 \text{ in.}$$

$$b' = b - \frac{d}{2}$$ (*Manual* Eq. 9-24)
$$= 2.57 \text{ in.} - \frac{7/8 \text{ in.}}{2}$$
$$= 2.13 \text{ in.}$$

$$\rho = \frac{b'}{a'}$$ (*Manual* Eq. 9-29)
$$= \frac{2.13 \text{ in.}}{1.94 \text{ in.}}$$
$$= 1.10$$

Note that end distances of 1¼ in. are used on the end plate, so $p$ is the average pitch of the bolts:

---

# IIA-135

$$p = \frac{l}{n}$$
$$= \frac{14\frac{1}{2} \text{ in.}}{5}$$
$$= 2.90 \text{ in.}$$

Check that $p \leq s$:

$$p = 2.90 \text{ in.} < s = 3 \text{ in.} \quad \textbf{o.k.}$$

$$d' = d$$
$$= 15⁄16 \text{ in.}$$

$$\delta = 1 - \frac{d'}{p}$$ (*Manual* Eq. 9-28)
$$= 1 - \frac{15⁄16 \text{ in.}}{2.90 \text{ in.}}$$
$$= 0.677$$

From AISC *Manual* Equations 9-30a or 9-30b, the required end-plate thickness to develop the available strength of the bolt without prying action is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $T_c = 40.2 \text{ kips/bolt}$ (from previous calculations) | $T_c = 26.8 \text{ kips/bolt}$ (from previous calculations) |
| $t_c = \sqrt{\frac{4T_cb'}{\phi_b pF_u}}$ | $t_c = \sqrt{\frac{4\Omega_bT_cb'}{pF_u}}$ |
| $= \sqrt{\frac{4(40.2 \text{ kips/bolt})(2.13 \text{ in.})}{0.90(2.90 \text{ in.})(65 \text{ ksi})}}$ | $= \sqrt{\frac{4(1.67)(26.8 \text{ kips/bolt})(2.13 \text{ in.})}{(2.90 \text{ in.})(65 \text{ ksi})}}$ |
| $= 1.42 \text{ in.}$ | $= 1.42 \text{ in.}$ |

Because the end-plate thickness of ½ in. is less than $t_c$, calculate the effect of prying action on the bolts.

$$\alpha' = \frac{1}{\delta(1+\rho)}\left[\left(\frac{t_c}{t}\right)^2 - 1\right]$$ (*Manual* Eq. 9-38)
$$= \frac{1}{0.677(1+1.10)}\left[\left(\frac{1.42 \text{ in.}}{1/2 \text{ in.}}\right)^2 - 1\right]$$
$$= 4.97$$

Because $\alpha' > 1$, the end plate has insufficient strength to develop the bolt strength, therefore:

---

# IIA-136

$$Q = \left(\frac{t}{t_c}\right)^2(1+\delta)$$ (*Manual* Eq. 9-39c)
$$= \left(\frac{1/2 \text{ in.}}{1.42 \text{ in.}}\right)^2(1+0.677)$$
$$= 0.208$$

The available tensile strength of the bolts taking prying action into account is determined from AISC *Manual* Equation 9-40 as follows:

| LRFD | ASD |
|------|-----|
| $T_{c,\,adj} = QT_c$ | $T_{c,\,adj} = QT_c$ |
| $= (0.208)(40.2 \text{ kips/bolt})$ | $= (0.208)(26.8 \text{ kips/bolt})$ |
| $= 8.36 \text{ kips/bolt}$ | $= 5.57 \text{ kips/bolt}$ |
| $\phi R_n = nT_{c,\,adj}$ | $\frac{R_n}{\Omega} = nT_{c,\,adj}$ |
| $= (10 \text{ bolts})(8.36 \text{ kips/bolt})$ | $= (10 \text{ bolts})(5.57 \text{ kips/bolt})$ |
| $= 83.6 \text{ kips} > 60 \text{ kips} \quad \textbf{o.k.}$ | $= 55.7 \text{ kips} > 40 \text{ kips} \quad \textbf{o.k.}$ |

*Weld Design*

Assume a 3⁄16 in. fillet weld on each side of the beam web, with the weld stopping short of the end of the plate at a distance equal to the weld size.

$$l_w = 14\frac{1}{2} \text{ in.} - 2(5⁄16 \text{ in.})$$
$$= 14.1 \text{ in.}$$

| LRFD | ASD |
|------|-----|
| $\theta = \tan^{-1}\left(\frac{N_u}{V_u}\right)$ | $\theta = \tan^{-1}\left(\frac{N_a}{V_a}\right)$ |
| $= \tan^{-1}\left(\frac{60 \text{ kips}}{75 \text{ kips}}\right)$ | $= \tan^{-1}\left(\frac{40 \text{ kips}}{50 \text{ kips}}\right)$ |
| $= 38.7°$ | $= 38.7°$ |

From AISC *Manual* Table 8-4 for Angle = 30° (which will lead to a conservative result):

Special Case: $k = a = 0$

$C = 4.37$

The required weld size is determined from AISC *Manual* Equation 8-30 as follows:

---

# IIA-137

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $D_{min} = \frac{R_u}{\phi CC_1l_w}$ | $D_{min} = \frac{\Omega R_u}{CC_1l_w}$ |
| $= \frac{96.0 \text{ kips}}{0.75(4.37)(1.0)(14.1 \text{ in.})}$ | $= \frac{2.00(64.0 \text{ kips})}{(4.37)(1.0)(14.1 \text{ in.})}$ |
| $= 2.08 \text{ sixteenths}$ | $= 2.08 \text{ sixteenths}$ |

Use a 3⁄16 in. fillet weld based on the minimum weld size from AISC *Specification* Table J2.4.

*Beam Web Strength at Fillet Weld*

The minimum beam web thickness required to match the shear rupture strength of the connecting element to that of the base metal is:

$$t_{min} = \frac{6.19D_{min}}{F_u}$$ (from *Manual* Eq. 9-7)
$$= \frac{6.19(2.08)}{65 \text{ ksi}}$$
$$= 0.198 \text{ in.} < 0.355 \text{ in.} \quad \textbf{o.k.}$$

*Shear Strength of the Plate*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the plate is determined as follows:

$$A_{gv} = 2lt$$
$$= (2)(14\frac{1}{2} \text{ in.})(1/2 \text{ in.})$$
$$= 14.5 \text{ in.}^2$$

$$R_n = 0.60F_yA_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(14.5 \text{ in.}^2)$$
$$= 435 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
| $\phi R_n = 1.00(435 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{435 \text{ kips}}{1.50}$ |
| $= 435 \text{ kips} > 96.0 \text{ kips} \quad \textbf{o.k.}$ | $= 290 \text{ kips} > 64.0 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the plate is determined as follows:

$$A_{nv} = 2[l - n(d_h + 1⁄16 \text{ in.})]t$$
$$= 2[14\frac{1}{2} \text{ in.} - 5(15⁄16 \text{ in.} + 1⁄16 \text{ in.})](1/2 \text{ in.})$$
$$= 9.50 \text{ in.}^2$$

---

# IIA-138

$$R_n = 0.60F_uA_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(9.50 \text{ in.}^2)$$
$$= 371 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(371 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{371 \text{ kips}}{2.00}$ |
| $= 278 \text{ kips} > 96.0 \text{ kips} \quad \textbf{o.k.}$ | $= 186 \text{ kips} > 64.0 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture Strength of the Plate*

The nominal strength for the limit state of block shear rupture of the plate assuming an L-shaped tearout relative to shear load, is determined as follows. The tearout pattern is shown in Figure II.A-11B-2.

$$R_n = 0.60F_uA_{nv} + U_{bs}F_uA_{nt} \leq 0.60F_yA_{gv} + U_{bs}F_uA_{nt}$$ (*Spec.* Eq. J4-5)

where

$$l_{eh} = \frac{b - gage}{2}$$
$$= \frac{8\frac{1}{2} \text{ in.} - 5\frac{1}{2} \text{ in.}}{2}$$
$$= 1.50 \text{ in.}$$

$$A_{gv} = (2)[l_{ev} + (n-1)s](t)$$
$$= (2)[1\frac{1}{4} \text{ in.} + (5-1)(3.00 \text{ in.})](1/2 \text{ in.})$$
$$= 13.3 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (2)(n-0.5)(d_h + 1⁄16 \text{ in.})(t)$$
$$= 13.3 \text{ in.}^2 - (2)(5-0.5)(15⁄16 \text{ in.} + 1⁄16 \text{ in.})(1/2 \text{ in.})$$
$$= 8.80 \text{ in.}^2$$

<div style="text-align: center;">
<img src="block_shear_diagram" alt="Block shear rupture diagram showing:
- 8½" width
- 5⅝" gage
- 1⅛" dimension
- 4@3" = 1'-0" vertical spacing
- 1¼" bottom dimension
- Hatched areas showing tearout pattern on both sides">
</div>

*Fig. II.A-11B-2. Block shear rupture of end plate.*

---

# IIA-139

$$A_{nt} = (2)[l_{eh} - 0.5(d_h + 1⁄16 \text{ in.})](t)$$
$$= (2)[1.50 \text{ in.} - 0.5(15⁄16 \text{ in.} + 1⁄16 \text{ in.})](1/2 \text{ in.})$$
$$= 1.00 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_n = 0.60(65 \text{ ksi})(8.80 \text{ in.}^2) + 1.0(65 \text{ ksi})(1.00 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(13.3 \text{ in.}^2) + 1.0(65 \text{ ksi})(1.00 \text{ in.}^2)$$
$$= 408 \text{ kips} < 464 \text{ kips}$$

Therefore:

$$R_n = 408 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(408 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{408 \text{ kips}}{2.00}$ |
| $= 306 \text{ kips} > 75 \text{ kips} \quad \textbf{o.k.}$ | $= 204 \text{ kips} > 50 \text{ kips} \quad \textbf{o.k.}$ |

*Shear Strength of Beam*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the beam is determined as follows:

$$A_{gv} = dt_w$$
$$= (18.0 \text{ in.})(0.355 \text{ in.})$$
$$= 6.39 \text{ in.}^2$$

$$R_n = 0.60F_yA_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(6.39 \text{ in.}^2)$$
$$= 192 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
| $\phi R_n = 1.00(192 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{192 \text{ kips}}{1.50}$ |
| $= 192 \text{ kips} > 75 \text{ kips} \quad \textbf{o.k.}$ | $= 128 \text{ kips} > 50 \text{ kips} \quad \textbf{o.k.}$ |

The limit state of shear rupture of the beam web does not apply in this example because the beam is uncoped.

*Tensile Strength of Beam*

From AISC *Specification* Section J4.1(a), the available tensile yield strength of the beam is determined as follows:

---

# IIA-140

$$R_n = F_yA_g$$ (*Spec.* Eq. J4-1)
$$= (50 \text{ ksi})(14.7 \text{ in.}^2)$$
$$= 735 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
| $\phi R_n = 0.90(735 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{735 \text{ kips}}{1.67}$ |
| $= 662 \text{ kips} > 60 \text{ kips} \quad \textbf{o.k.}$ | $= 440 \text{ kips} > 40 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.1(b), determine the available tensile rupture strength of the beam. The effective net area is $A_e = A_nU$ from AISC *Specification* Section D3, where $U$ is determined from AISC *Specification* Table D3.1, Case 3.

$U = 1.0$

$A_n = $ area of the directly connected elements
$= l_wt_w$
$= (14.1 \text{ in.})(0.355 \text{ in.})$
$= 5.01 \text{ in.}^2$

The available tensile rupture strength is:

$$R_n = F_uA_e$$ (*Spec.* Eq. J4-2)
$$= F_uA_nU$$
$$= (65 \text{ ksi})(5.01 \text{ in.}^2)(1.0)$$
$$= 326 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(326 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{326 \text{ kips}}{2.00}$ |
| $= 245 \text{ kips} > 60 \text{ kips} \quad \textbf{o.k.}$ | $= 163 \text{ kips} > 40 \text{ kips} \quad \textbf{o.k.}$ |

*Conclusion*

The connection is found to be adequate as given for the applied loads.

---

# IIA-141

# EXAMPLE II.A-11C SHEAR END-PLATE CONNECTION—STRUCTURAL INTEGRITY CHECK

## Given:

Verify the available strength of the shear end-plate connection from Example II.A-11B for the structural integrity provisions of AISC *Specification* Section B3.9. The ASTM A992/A992M W18×50 beam is bracing a column, and the connection geometry is shown in Figure II.A-11C-1. Note that these checks are necessary when design for structural integrity is required by the applicable building code.

Use 70-ksi electrodes and ASTM A572/A572M Grade 50 plate.

<div style="text-align: center;">
<img src="connection_diagram" alt="Connection diagram showing:
- W18×50 beam with end plate
- 1⅛" top dimension
- 3" spacing
- 4@3" = 1'-0" vertical dimension
- Gage = 5⅝"
- 1¼" bottom dimension
- ⅞" dia. Group 120, thread condition N, std. holes
- PL½×8½×1'-2½"
- Vertical load V and axial load N indicated
- ½" setback
- ⅜" welds on both sides">
</div>

*Fig. II.A-11C-1. Connection geometry for Example II.A-11C.*

## Solution:

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Beam
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

Plate
ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W18×50
$t_w = 0.355$ in.

---

# IIA-142

From Example II.A-11B, the required shear strength is:

| LRFD | ASD |
|------|-----|
| $V_u = 75 \text{ kips}$ | $V_a = 50 \text{ kips}$ |

From AISC *Specification* Section B3.9, the minimum nominal axial tensile strength is:

| LRFD | ASD |
|------|-----|
| $T = \frac{2}{3}V_u \geq 10 \text{ kips}$ | $T = V_a \geq 10 \text{ kips}$ |
| $= \frac{2}{3}(75 \text{ kips}) > 10 \text{ kips}$ | $= 50 \text{ kips} > 10 \text{ kips}$ |
| $= 50 \text{ kips} > 10 \text{ kips}$ | $= 50 \text{ kips}$ |
| $= 50 \text{ kips}$ | |

From AISC *Specification* Section B3.9, these requirements are evaluated independently from other strength requirements.

*Bolt Tension*

From AISC *Specification* Section J3.7, the nominal bolt tensile strength is:

$F_{nt} = 90 \text{ ksi}$, from AISC *Specification* Table J3.2

$$T_n = nF_{nt}A_b$$ (from *Spec.* Eq. J3-1)
$$= (10 \text{ bolts})(90 \text{ ksi})(0.601 \text{ in.}^2)$$
$$= 541 \text{ kips}$$

*Plate Bending and Prying Action*

From AISC *Manual* Part 9, the nominal strength of the end plate accounting for prying action is determined as follows. Note that the use of the prying action method is a conservative approach when evaluating a connection for structural integrity requirements.

$$b = \frac{gage - t_w}{2}$$
$$= \frac{5\frac{1}{2} \text{ in.} - 0.355 \text{ in.}}{2}$$
$$= 2.57 \text{ in.}$$

$$a = \frac{width\;of\;plate - gage}{2} \leq 1.25b$$
$$= \frac{8\frac{1}{2} \text{ in.} - 5\frac{1}{2} \text{ in.}}{2} < 1.25(1.50 \text{ in.})$$
$$= 1.50 \text{ in.} < 1.88 \text{ in.}$$
$$= 1.50 \text{ in.}$$

---

# IIA-143

$$a' = a + \frac{d}{2}$$ (*Manual* Eq. 9-23)
$$= 1.50 \text{ in.} + \frac{7/8 \text{ in.}}{2}$$
$$= 1.94 \text{ in.}$$

$$b' = b - \frac{d}{2}$$ (*Manual* Eq. 9-24)
$$= 2.57 \text{ in.} - \frac{7/8 \text{ in.}}{2}$$
$$= 2.13 \text{ in.}$$

$$\rho = \frac{b'}{a'}$$ (*Manual* Eq. 9-29)
$$= \frac{2.13 \text{ in.}}{1.94 \text{ in.}}$$
$$= 1.10$$

Note that end distances of 1¼ in. are used on the end plate, so $p$ is the average pitch of the bolts:

$$p = \frac{l}{n}$$
$$= \frac{14\frac{1}{2} \text{ in.}}{5}$$
$$= 2.90 \text{ in.}$$

Check that $p \leq s$:

$$p = 2.90 \text{ in.} \leq s = 3.00 \text{ in.} \quad \textbf{o.k.}$$

$$d' = d$$
$$= 15⁄16 \text{ in.}$$

$$\delta = 1 - \frac{d'}{p}$$ (*Manual* Eq. 9-28)
$$= 1 - \frac{15⁄16 \text{ in.}}{2.90 \text{ in.}}$$
$$= 0.677$$

$$T_c = F_{nt}A_b$$
$$= (90 \text{ ksi})(0.601 \text{ in.}^2)$$
$$= 54.1 \text{ kips/bolt}$$

---

# IIA-144

$$t_c = \sqrt{\frac{4T_cb'}{pF_u}}$$ (from *Manual* Eq. 9-30)
$$= \sqrt{\frac{4(54.1 \text{ kips/bolt})(2.13 \text{ in.})}{(2.90 \text{ in.})(65 \text{ ksi})}}$$
$$= 1.56 \text{ in.}$$

$$\alpha' = \frac{1}{\delta(1+\rho)}\left[\left(\frac{t_c}{t}\right)^2 - 1\right]$$ (*Manual* Eq. 9-38)
$$= \frac{1}{0.677(1+1.10)}\left[\left(\frac{1.56 \text{ in.}}{1/2 \text{ in.}}\right)^2 - 1\right]$$
$$= 6.14$$

Because $\alpha' > 1$, the end plate has insufficient strength to develop the bolt strength, therefore:

$$Q = \left(\frac{t}{t_c}\right)^2(1+\delta)$$ (*Manual* Eq. 9-39c)
$$= \left(\frac{1/2 \text{ in.}}{1.56 \text{ in.}}\right)^2(1+0.677)$$
$$= 0.172$$

$$T_n = nQT_c$$ (from *Manual* Eq. 9-40)
$$= (10 \text{ bolts})(0.172)(54.1 \text{ kips/bolt})$$
$$= 93.1 \text{ kips}$$

*Weld Strength*

From AISC *Specification* Section J2.4, the nominal tensile strength of the weld is determined as follows:

$$F_{nw} = 0.60F_{EXX}\left(1.0 + 0.50\sin^{1.5}\theta\right)$$
$$= 0.60(70 \text{ ksi})\left(1.0 + 0.50\sin^{1.5}90°\right)$$
$$= 63.0 \text{ ksi}$$

The weld length accounts for termination equal to the weld size.

$$l_w = l - 2w$$
$$= 14\frac{1}{2} \text{ in.} - 2(5⁄16 \text{ in.})$$
$$= 14.1 \text{ in.}$$

The throat dimension is used to calculate the effective area of the fillet weld.

$$A_{we} = \frac{w}{\sqrt{2}}l_w(2 \text{ welds})$$
$$= \frac{5⁄16 \text{ in.}}{\sqrt{2}}(14.1 \text{ in.})(2 \text{ welds})$$
$$= 3.74 \text{ in.}^2$$

---

# IIA-145

$$T_n = F_{nw}A_{we}$$ (from *Spec.* Eq. J2-4)
$$= (63.0 \text{ ksi})(3.74 \text{ in.}^2)$$
$$= 236 \text{ kips}$$

*Tensile Strength of Beam Web at the Weld*

From AISC *Specification* Section J4.1, the nominal tensile strength of the beam web at the weld is:

$$A_e = l_wt_w$$
$$= (14.1 \text{ in.})(0.355 \text{ in.})$$
$$= 5.01 \text{ in.}^2$$

$$T_n = F_uA_e$$ (from *Spec.* Eq. J4-2)
$$= (65 \text{ ksi})(5.01 \text{ in.}^2)$$
$$= 326 \text{ kips}$$

*Nominal Tensile Strength*

The controlling nominal tensile strength, $T_n$, is the least of those previously calculated:

$$T_n = \min\{541 \text{ kips}, 93.1 \text{ kips}, 236 \text{ kips}, 326 \text{ kips}\}$$
$$= 93.1 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $T_n = 93.1 \text{ kips} > 50 \text{ kips} \quad \textbf{o.k.}$ | $T_n = 93.1 \text{ kips} > 50 \text{ kips} \quad \textbf{o.k.}$ |

*Column Bracing*

From AISC *Specification* Section B3.9(c), the minimum axial tension strength for the connection of a member bracing a column is equal to 1% or two-thirds of the required column axial strength for LRFD and equal to 1% of the required column axial strength for ASD. These requirements are evaluated independently from other strength requirements.

The maximum column axial force this connection is able to brace is determined as follows:

| LRFD | ASD |
|------|-----|
| $T_n \geq 0.01\left(\frac{2}{3}P_u\right)$ | $T_n \geq 0.01P_a$ |

---

# IIA-146

| LRFD | ASD |
|------|-----|
| Solving for the column axial force: | Solving for the column axial force: |
| $P_u \leq 100\left(\frac{3}{2}T_n\right)$ | $P_a \leq 100T_n$ |
| $= 100\left(\frac{3}{2}\right)(93.1 \text{ kips})$ | $= 100(93.1 \text{ kips})$ |
| $= 14,000 \text{ kips}$ | $= 9,310 \text{ kips}$ |

As long as the required column axial strength is less than or equal to $P_u = 14,000 \text{ kips}$ or $P_a = 9,310 \text{ kips}$, this connection is an adequate column brace.

---

# IIA-147

# EXAMPLE II.A-12A ALL-BOLTED UNSTIFFENED SEATED CONNECTION (BEAM-TO-COLUMN WEB)

## Given:

Verify the all-bolted unstiffened seated connection between an ASTM A992/A992M W16×50 beam and an ASTM A992/A992M W14×90 column web, as shown in Figure II.A-12A-1, to support the following end reactions:

$R_D = 9 \text{ kips}$
$R_L = 27.5 \text{ kips}$

Use ASTM A572/A572M Grade 50 angles.

<div style="text-align: center;">
<img src="connection_diagram" alt="Connection diagram showing:
- W14×90 column web
- W16×50 beam
- L4×4×⅜, loose angle top angle with (2) ¾" dia. Group 120 bolts, thread condition N, std. holes in each leg
- ⅛" to ¼" clearance
- ½" nominal setback
- 2½" dimension
- 2" dimension
- L6×4×⅝×0'-8" (4 in. OSL) seat angle
- ¾" dia. Group 120, thread condition N, std. holes
- Type B (2 rows of bolts) diagram showing 8" width and 5½" gage">
</div>

*Fig. II.A-12A-1. Connection geometry for Example II.A-12A.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam and column
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

Angles
ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

---

# IIA-148

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W16×50
$d = 16.3$ in.
$t_w = 0.380$ in.
$b_f = 7.07$ in.
$t_f = 0.630$ in.
$k_{des} = 1.03$ in.

Column
W14×90
$t_w = 0.440$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(9 \text{ kips}) + 1.6(27.5 \text{ kips})$ | $R_a = 9 \text{ kips} + 27.5 \text{ kips}$ |
| $= 54.8 \text{ kips}$ | $= 36.5 \text{ kips}$ |

*Minimum Bearing Length*

From AISC *Manual* Part 10, the minimum required bearing length, $l_{b\,min}$, is the length of bearing required for the limit states of web local yielding and web local crippling on the beam, but not less than $k_{des}$.

Using AISC *Manual* Equations 10-1a or 10-1b, the minimum required bearing length for web local yielding is:

| LRFD | ASD |
|------|-----|
| $l_{b,yielding} = \frac{R_u}{\phi F_yt_w} - 2.5k_{des}$ | $l_{b,yielding} = \frac{\Omega R_a}{F_yt_w} - 2.5k_{des}$ |
| $= \frac{54.8 \text{ kips}}{(1.00)(50 \text{ ksi})(0.380 \text{ in.})} - 2.5(1.03 \text{ in.})$ | $= \frac{1.50(36.5 \text{ kips})}{(50 \text{ ksi})(0.380 \text{ in.})} - 2.5(1.03 \text{ in.})$ |
| $= 0.309 \text{ in.}$ | $= 0.307 \text{ in.}$ |

For web local crippling, the maximum bearing length-to-depth ratio is determined as follows (including ¼ in. tolerance to account for possible beam underrun):

$$\left(\frac{l_b}{d}\right)_{max} = \frac{3.25 \text{ in.}}{16.3 \text{ in.}}$$
$$= 0.199 < 0.2$$

Using AISC *Manual* Equations 10-2a or 10-2b, when $\frac{l_b}{d} < 0.2$:

---

# IIA-149

| LRFD | ASD |
|------|-----|
| $l_{b,crippling} = \frac{d}{3}\left[\frac{R_u}{\phi(0.40)t_w^2\sqrt{\frac{t_w}{EF_yt_f}} - 1}\right]\left(\frac{t_f}{t_w}\right)^{1.5}$ | $l_{b,crippling} = \frac{d}{3}\left[\frac{\Omega R_a}{0.40t_w^2\sqrt{\frac{t_w}{EF_yt_f}} - 1}\right]\left(\frac{t_f}{t_w}\right)^{1.5}$ |
| $= \frac{16.3 \text{ in.}}{3}$ | $= \frac{16.3 \text{ in.}}{3}$ |
| $\times\left[\frac{54.8 \text{ kips}}{0.75(0.40)(0.380 \text{ in.})^2\sqrt{\frac{0.380 \text{ in.}}{(29,000 \text{ ksi})(50 \text{ ksi})(0.630 \text{ in.})}} - 1}\right]$ | $\times\left[\frac{2.00(36.5 \text{ kips})}{0.40(0.380 \text{ in.})^2\sqrt{\frac{0.380 \text{ in.}}{(29,000 \text{ ksi})(50 \text{ ksi})(0.630 \text{ in.})}} - 1}\right]$ |
| $\times\left(\frac{0.630 \text{ in.}}{0.380 \text{ in.}}\right)^{1.5}$ | $\times\left(\frac{0.630 \text{ in.}}{0.380 \text{ in.}}\right)^{1.5}$ |
| This results in a negative quantity; therefore, | This results in a negative quantity; therefore, |
| $l_{b\,min} = k_{des} = 1.03 \text{ in.}$ | $l_{b\,min} = k_{des} = 1.03 \text{ in.}$ |

*Connection Selection*

AISC *Manual* Table 10-5 includes checks for the limit states of shear yielding and flexural yielding of the outstanding angle leg.

For an 8 in. angle length with a ⅝ in. thickness, a 3½ in. minimum outstanding leg, and conservatively using $l_{b\,req} = 1⅛$ in., from AISC *Manual* Table 10-5:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 113 \text{ kips} > 54.8 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 74.9 \text{ kips} > 36.5 \text{ kips} \quad \textbf{o.k.}$ |

The 8-in.-long L6×4×⅝ (4 in. OSL) with 5½ in. bolt gage, Connection Type B (four bolts), is acceptable.

*Available Bolt Shear Strength*

From the bottom portion of AISC *Manual* Table 10-5 for L6, with ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N), the available shear strength is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 107 \text{ kips} > 54.8 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 71.6 \text{ kips} > 36.5 \text{ kips} \quad \textbf{o.k.}$ |

*Bolt Bearing and Tearout*

As noted in *Manual* Table 10-5, footnote [b], if the angle thickness and supporting element thickness is greater than or equal to $t_{min}$, the available shear transfer strength is equal to the available bolt shear strength.

From *Manual* Table 10-5, for Connection Type B with ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N):

$t_{min} = 0.204 \text{ in.}$

---

# IIA-150

For the seat angle

$$t = 5/8 \text{ in.} > 0.204 \text{ in.}$$

For the column web

$$t_w = 0.440 \text{ in.} > 0.204 \text{ in.}$$

Therefore, the available shear transfer strength is controlled by the available bolt shear strength.

*Top Angle and Bolts*

As discussed in AISC *Manual* Part 10, use an L4×4×⅜ with two ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) through each leg.

*Conclusion*

The connection design shown in Figure II.A-12A-1 is acceptable.

---

# IIA-151

# EXAMPLE II.A-12B ALL-BOLTED UNSTIFFENED SEATED CONNECTION—STRUCTURAL INTEGRITY CHECK

## Given:

Verify the all-bolted unstiffened seated connection from Example II.A-12A, as shown in Figure II.A-12B-1, for the structural integrity provisions of AISC *Specification* Section B3.9. The connection is verified as a beam and girder end connection and as an end connection of a member bracing a column. Note that these checks are necessary when design for structural integrity is required by the applicable building code.

The beam is an ASTM A992/A992M W16×50 and the angles are ASTM A572/A572M Grade 50 material.

<div style="text-align: center;">
<img src="connection_diagram" alt="Connection diagram showing:
- W14×90 column web
- W16×50 beam
- L4×4×⅜, loose angle top angle with (2) ¾" dia. Group 120 bolts, thread condition N, std. holes in each leg
- ⅛" to ¼" clearance
- ½" nominal setback
- 2½" dimension
- 2" dimension
- 3" dimension
- L6×4×⅝×0'-8" (4 in. OSL) seat angle
- ¾" dia. Group 120, thread condition N, std. holes
- Type B (2 rows of bolts) diagram showing 8" width and 5½" gage">
</div>

*Fig. II.A-12B-1. Connection geometry for Example II.A-12B.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

Angle
ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

---

# IIA-152

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W16×50
$b_f = 7.07$ in.
$t_f = 0.630$ in.

From AISC *Specification* Table J3.3, the hole diameter for ¾-in.-diameter bolts with standard holes is:

$d_h = 13⁄16$ in.

From Example II.A-12A, the required shear strength is:

| LRFD | ASD |
|------|-----|
| $V_u = 54.8 \text{ kips}$ | $V_a = 36.5 \text{ kips}$ |

From AISC *Specification* Section B3.9(b), the minimum nominal axial tensile strength is:

| LRFD | ASD |
|------|-----|
| $T = \frac{2}{3}V_u \geq 10 \text{ kips}$ | $T = V_a \geq 10 \text{ kips}$ |
| $= \frac{2}{3}(54.8 \text{ kips}) > 10 \text{ kips}$ | $= 36.5 \text{ kips} > 10 \text{ kips}$ |
| $= 36.5 \text{ kips}$ | $= 36.5 \text{ kips}$ |

From AISC *Specification* Section B3.9, these strength requirements are evaluated independently from other strength requirements.

*Bolt Shear*

Bolt shear is checked for the outstanding leg of the seat angle. From AISC *Specification* Section J3.7, the nominal bolt shear strength is:

$F_{nv} = 54 \text{ ksi}$, from AISC *Specification* Table J3.2

$$T_n = nF_{nv}A_b$$ (from *Spec.* Eq. J3-1)
$$= (2 \text{ bolts})(54 \text{ ksi})(0.442 \text{ in.}^2)$$
$$= 47.7 \text{ kips}$$

*Bolt Tension*

Bolt tension is checked for the top row of bolts on the support leg of the seat angle. From AISC *Specification* Section J3.7, the nominal bolt tensile strength is:

$F_{nt} = 90 \text{ ksi}$, from AISC *Specification* Table J3.2

$$T_n = nF_{nt}A_b$$ (from *Spec.* Eq. J3-1)
$$= (2 \text{ bolts})(90 \text{ ksi})(0.442 \text{ in.}^2)$$
$$= 79.6 \text{ kips}$$

---

# IIA-153

*Bolt Bearing and Tearout*

Bolt bearing and tearout is checked for the outstanding leg of the seat angle. From AISC *Specification* Section B3.9, for the purpose of satisfying structural integrity requirements, inelastic deformations of the connection are permitted; therefore, AISC *Specification* Equations J3-6b and J3-6d are used to determine the nominal bearing and tearout strength. By inspection, bolt bearing and tearout will control for the angle.

For bolt bearing on the angle:

$$T_n = n3.0dtF_u$$ (from *Spec.* Eq. J3-6b)
$$= (2 \text{ bolts})(3.0)(3/4 \text{ in.})(5/8 \text{ in.})(65 \text{ ksi})$$
$$= 183 \text{ kips}$$

For bolt tearout on the angle:

$$l_c = leg - 2\frac{1}{2} \text{ in.} - 0.5d_h$$
$$= 4.00 \text{ in.} - 2\frac{1}{2} \text{ in.} - 0.5(13⁄16 \text{ in.})$$
$$= 1.09 \text{ in.}$$

$$T_n = n1.5l_ctF_u$$ (from *Spec.* Eq. J3-6d)
$$= (2 \text{ bolts})(1.5)(1.09 \text{ in.})(5/8 \text{ in.})(65 \text{ ksi})$$
$$= 133 \text{ kips}$$

*Angle Bending and Prying Action*

From AISC *Manual* Part 9, the nominal strength of the angle accounting for prying action is determined as follows:

$$b = 2 \text{ in.} - \frac{3/8 \text{ in.}}{2}$$
$$= 1.69 \text{ in.}$$

$$a = \min\{3 \text{ in.}, 1.25b\}$$
$$= \min\{3 \text{ in.}, 1.25(1.69 \text{ in.})\}$$
$$= 2.11 \text{ in.}$$

$$b' = b - \frac{d}{2}$$ (*Manual* Eq. 9-24)
$$= 1.69 \text{ in.} - \frac{3/4 \text{ in.}}{2}$$
$$= 1.32 \text{ in.}$$

$$a' = a + \frac{d}{2}$$ (from *Manual* Eq. 9-23)
$$= 2.11 \text{ in.} + \frac{3/4 \text{ in.}}{2}$$
$$= 2.49 \text{ in.}$$

---

# IIA-154

$$\rho = \frac{b'}{a'}$$ (*Manual* Eq. 9-29)
$$= \frac{1.32 \text{ in.}}{2.49 \text{ in.}}$$
$$= 0.530$$

Note that end distances of 1¼ in. are used on the angles, so $p$ is the average pitch of the bolts:

$$p = \frac{l}{n}$$
$$= \frac{8.00 \text{ in.}}{2}$$
$$= 4.00 \text{ in.}$$

Check that $p \leq s$:

$$p = 4.00 \text{ in.} \leq s = 5\frac{1}{2} \text{ in.} \quad \textbf{o.k.}$$

$$d' = d$$
$$= 13⁄16 \text{ in.}$$

$$\delta = 1 - \frac{d'}{p}$$ (*Manual* Eq. 9-28)
$$= 1 - \frac{13⁄16 \text{ in.}}{4.00 \text{ in.}}$$
$$= 0.797$$

$$T_c = F_{nt}A_b$$
$$= (90 \text{ ksi})(0.442 \text{ in.}^2)$$
$$= 39.8 \text{ kips/bolt}$$

$$t_c = \sqrt{\frac{4T_cb'}{pF_u}}$$ (from *Manual* Eq. 9-30)
$$= \sqrt{\frac{4(39.8 \text{ kips/bolt})(1.32 \text{ in.})}{(4.00 \text{ in.})(65 \text{ ksi})}}$$
$$= 0.899 \text{ in.}$$

$$\alpha' = \frac{1}{\delta(1+\rho)}\left[\left(\frac{t_c}{t}\right)^2 - 1\right]$$ (*Manual* Eq. 9-38)
$$= \frac{1}{0.797(1+0.530)}\left[\left(\frac{0.899 \text{ in.}}{5/8 \text{ in.}}\right)^2 - 1\right]$$
$$= 0.877$$

Because $0 < \alpha' \leq 1$, the angle has insufficient strength to develop the bolt strength, therefore:

---

# IIA-155

$$Q = \left(\frac{t}{t_c}\right)^2(1+\delta\alpha')$$
$$= \left(\frac{5/8 \text{ in.}}{0.899 \text{ in.}}\right)^2[1+0.797(0.877)]$$
$$= 0.821$$

$$T_n = nQT_c$$ (from *Manual* Eq. 9-40)
$$= (2 \text{ bolts})(0.821)(39.8 \text{ kips/bolt})$$
$$= 65.4 \text{ kips}$$

*Block Shear Rupture*

By comparison of the seat angle length and flange width, block shear rupture of the beam flange will control. The block shear rupture failure path is shown in Figure II.A-12B-2. From AISC *Specification* Section J4.3, the available block shear rupture strength of the beam flange is determined as follows (accounting for a possible ¼ in. beam underrun):

$$T_n = 0.60F_uA_{nv} + U_{bs}F_uA_{nt} \leq 0.60F_yA_{gv} + U_{bs}F_uA_{nt}$$ (from *Spec.* Eq. J4-5)

where

$$A_{gv} = (2)l_et_f$$
$$= (2)(1\frac{3}{4} \text{ in.})(0.630 \text{ in.})$$
$$= 2.21 \text{ in.}^2$$

$$A_{nv} = (2)\left[l_e - 0.5(d_h + 1⁄16 \text{ in.})\right]t_f$$
$$= (2)\left[1\frac{3}{4} \text{ in.} - 0.5(13⁄16 \text{ in.} + 1⁄16 \text{ in.})\right](0.630 \text{ in.})$$
$$= 1.65 \text{ in.}^2$$

$$A_{nt} = (2)\left[\frac{b_f - gage}{2} - 0.5(d_h + 1⁄16 \text{ in.})\right]t_f$$
$$= (2)\left[\frac{7.07 \text{ in.} - 5\frac{1}{2} \text{ in.}}{2} - 0.5(13⁄16 \text{ in.} + 1⁄16 \text{ in.})\right](0.630 \text{ in.})$$
$$= 0.438 \text{ in.}^2$$

$$U_{bs} = 1.0$$

<div style="text-align: center;">
<img src="block_shear_diagram" alt="Block shear rupture diagram showing:
- l_e = 2½" - ½" (setback) - ¼" (underrun) = 1¾"
- 5½" gage dimension
- b_f = 7.07" flange width
- Bottom flange of W16×50 beam with hatched areas showing tearout pattern">
</div>

*Fig. II.A-12B-2. Beam flange block shear rupture.*

---

# IIA-156

and

$$T_n = 0.60(65 \text{ ksi})(1.65 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.438 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(2.21 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.438 \text{ in.}^2)$$
$$= 92.8 \text{ kips} < 94.8 \text{ kips}$$
$$= 92.8 \text{ kips}$$

*Nominal Tensile Strength*

The controlling tensile strength, $T_n$, is the least of those previously calculated:

$$T_n = \min\{47.7 \text{ kips}, 79.6 \text{ kips}, 183 \text{ kips}, 133 \text{ kips}, 65.4 \text{ kips}, 92.8 \text{ kips}\}$$
$$= 47.7 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $T_n = 47.7 \text{ kips} > 36.5 \text{ kips} \quad \textbf{o.k.}$ | $T_n = 47.7 \text{ kips} > 36.5 \text{ kips} \quad \textbf{o.k.}$ |

*Column Bracing*

From AISC *Specification* Section B3.9(c), the minimum axial tension strength for the connection of a member bracing a column is equal to 1% of two-thirds of the required column axial strength for LRFD and equal to 1% of the required column axial strength for ASD. These requirements are evaluated independently from other strength requirements.

The maximum column axial force this connection is able to brace is determined as follows,

| LRFD | ASD |
|------|-----|
| $T_n \geq 0.01\left(\frac{2}{3}P_u\right)$ | $T_n \geq 0.01P_a$ |
| Solving for the column axial force: | Solving for the column axial force: |
| $P_u \leq 100\left(\frac{3}{2}T_n\right)$ | $P_a \leq 100T_n$ |
| $= 100\left(\frac{3}{2}\right)(47.7 \text{ kips})$ | $= 100(47.7 \text{ kips})$ |
| $= 7,160 \text{ kips}$ | $= 4,770 \text{ kips}$ |

As long as the required column axial strength is less than $P_u = 7,160 \text{ kips}$ or $P_a = 4,770 \text{ kips}$, this connection is an adequate column brace.

---

# IIA-157

# EXAMPLE II.A-13 BOLTED/WELDED UNSTIFFENED SEATED CONNECTION (BEAM-TO-COLUMN FLANGE)

## Given:

Verify the unstiffened seated connection between an ASTM A992/A992M W21×62 beam and an ASTM A992/A992M W14×61 column flange, as shown in Figure II.A-13-1, to support the following beam end reactions:

$R_D = 9 \text{ kips}$
$R_L = 27.5 \text{ kips}$

Use ASTM A572/A572M Grade 50 angles and 70-ksi weld electrodes.

<div style="text-align: center;">
<img src="connection_diagram" alt="Connection diagram showing:
- W14×61 column with W21×62 beam
- L4×4×¼, top angle with optional top angle location
- ½" nominal setback
- ¾" dia. Group 120, thread condition N, std. holes
- L8×4×⅝×0'-8" (4" OSL) seat angle
- 8" width
- 5" height
- ⅝" return at top
- 5⁄16" fillet weld">
</div>

*Fig. II.A-13-1. Connection geometry for Example II.A-13.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam and column
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

Angles
ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

---

# IIA-158

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W21×62
$d = 21.0$ in.
$t_w = 0.400$ in.
$b_f = 8.24$ in.
$t_f = 0.615$ in.
$k_{des} = 1.12$ in.

Column
W14×61
$t_f = 0.645$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(9 \text{ kips}) + 1.6(27.5 \text{ kips})$ | $R_a = 9 \text{ kips} + 27.5 \text{ kips}$ |
| $= 54.8 \text{ kips}$ | $= 36.5 \text{ kips}$ |

*Minimum Bearing Length*

From AISC *Manual* Part 10, the minimum required bearing length, $l_{b\,min}$, is the length of bearing required for the limit states of web local yielding and web local crippling on the beam, but not less than $k_{des}$.

Using AISC *Manual* Equations 10-1a or 10-1b, the minimum required bearing length for web local yielding is:

| LRFD | ASD |
|------|-----|
| $l_{b,yielding} = \frac{R_u}{\phi F_yt_w} - 2.5k_{des}$ | $l_{b,yielding} = \frac{\Omega R_a}{F_yt_w} - 2.5k_{des}$ |
| $= \frac{54.8 \text{ kips}}{(1.00)(50 \text{ ksi})(0.400 \text{ in.})} - 2.5(1.12 \text{ in.})$ | $= \frac{1.50(36.5 \text{ kips})}{(50 \text{ ksi})(0.400 \text{ in.})} - 2.5(1.12 \text{ in.})$ |
| This results in a negative quantity; therefore, | This results in a negative quantity; therefore, |
| $l_{b\,min} = k_{des} = 1.12 \text{ in.}$ | $l_{b\,min} = k_{des} = 1.12 \text{ in.}$ |

For web local crippling, the maximum bearing length-to-depth ratio is determined as follows (including a ¼ in. tolerance to account for possible beam underrun):

$$\left(\frac{l_b}{d}\right)_{max} = \frac{3.25 \text{ in.}}{21.0 \text{ in.}}$$
$$= 0.155 < 0.2$$

From AISC *Manual* Equations 10-2a or 10-2b, when $\frac{l_b}{d} < 0.2$:

---

# IIA-159

| LRFD | ASD |
|------|-----|
| $l_{b,crippling} = \frac{d}{3}\left[\frac{R_u}{\phi(0.40)t_w^2\sqrt{\frac{t_w}{EF_yt_f}} - 1}\right]\left(\frac{t_f}{t_w}\right)^{1.5}$ | $l_{b,crippling} = \frac{d}{3}\left[\frac{\Omega R_a}{0.40t_w^2\sqrt{\frac{t_w}{EF_yt_f}} - 1}\right]\left(\frac{t_f}{t_w}\right)^{1.5}$ |
| $= \frac{21.0 \text{ in.}}{3}$ | $= \frac{21.0 \text{ in.}}{3}$ |
| $\times\left[\frac{54.8 \text{ kips}}{0.75(0.40)(0.400 \text{ in.})^2\sqrt{\frac{0.400 \text{ in.}}{(29,000 \text{ ksi})(50 \text{ ksi})(0.615 \text{ in.})}} - 1}\right]$ | $\times\left[\frac{2.00(36.5 \text{ kips})}{0.40(0.400 \text{ in.})^2\sqrt{\frac{0.400 \text{ in.}}{(29,000 \text{ ksi})(50 \text{ ksi})(0.615 \text{ in.})}} - 1}\right]$ |
| $\times\left(\frac{0.615 \text{ in.}}{0.400 \text{ in.}}\right)^{1.5}$ | $\times\left(\frac{0.615 \text{ in.}}{0.400 \text{ in.}}\right)^{1.5}$ |
| This results in a negative quantity; therefore, | This results in a negative quantity; therefore, |
| $l_{b\,min} = k_{des} = 1.12 \text{ in.}$ | $l_{b\,min} = k_{des} = 1.12 \text{ in.}$ |

*Connection Selection*

AISC *Manual* Table 10-6 includes checks for the limit states of shear yielding and flexural yielding of the outstanding angle leg.

For an 8 in. angle length with a ⅝ in. thickness, a 3½ in. minimum outstanding leg, and conservatively using $l_{b\,req} = 1⅛$ in., from AISC *Manual* Table 10-6:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 113 \text{ kips} > 54.8 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 74.9 \text{ kips} > 36.5 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Manual* Table 10-6, for an L8×4×⅝ (4 in. OSL), 8 in. long, with 5⁄16 in. fillet welds, the weld available strength is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 66.7 \text{ kips} > 54.8 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 44.5 \text{ kips} > 36.5 \text{ kips} \quad \textbf{o.k.}$ |

Use two ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) to connect the beam to the seat angle.

The strength of the bolts, welds, and angles must be verified if horizontal forces are added to the connection.

*Top Angle, Bolts, and Welds*

Use an L4×4×¼ with two ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) through the supported beam leg of the angle. Use a 3⁄16 in. fillet weld along the toe of the angle to the column flange. See the discussion in AISC *Manual* Part 10.

*Conclusion*

The connection design shown in Figure II.A-13-1 is acceptable.

---

# IIA-160

# EXAMPLE II.A-14 STIFFENED SEATED CONNECTION—WELDED STIFFENING ELEMENT (BEAM-TO-COLUMN FLANGE)

## Given:

Verify the bolted/welded stiffened seated connection between an ASTM A992/A992M W21×68 beam and an ASTM A992/A992M W14×90 column flange, as shown in Figure II.A-14-1, to support the following end reactions:

$R_D = 21 \text{ kips}$
$R_L = 62.5 \text{ kips}$

Use 70-ksi weld electrodes and ASTM A572/A572M Grade 50 angles and plate.

<div style="text-align: center;">
<img src="connection_diagram" alt="Detailed connection diagram showing:
- W14×90 column
- W21×68 beam
- Stiffener fit to bear
- L4×4×¼, top angle, shop attached to beam
- Weld toe only
- ½" nominal setback
- 3" dimension
- ⅞" dimension
- 9" height
- 4" (optional) dimension
- PL⅜×7×9" stiffener plate
- 5⁄16 welds (6 places)
- PL⅜×7×1'-3" optional trim lines
- W = 7" width
- 5⁄16 welds
- 5⁄8" dimension
- 5½" spacing
- Dimensions l = 1'-3", ¾" dia. Group 120, thread condition N, std. holes
- Optional location top angle">
</div>

*Fig. II.A-14-1. Connection geometry for Example II.A-14.*

## Solution:

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Beam and column
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

Angle and plates
ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

---

# IIA-161

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W21×68
$d = 21.1$ in.
$t_w = 0.430$ in.
$b_f = 8.27$ in.
$t_f = 0.685$ in.
$k_{des} = 1.19$ in.

Column
W14×90
$t_f = 0.710$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(21 \text{ kips}) + 1.6(62.5 \text{ kips})$ | $R_a = 21 \text{ kips} + 62.5 \text{ kips}$ |
| $= 125 \text{ kips}$ | $= 83.5 \text{ kips}$ |

*Required Stiffener Width*

The minimum stiffener width, $W_{min}$, is determined based on the limit states of web local yielding and web local crippling for the beam.

The minimum stiffener width for web local crippling of the beam web, for the force applied less than one-half of the depth of the beam from the end of the beam and assuming $l_b/d > 0.2$, is determined from AISC *Manual* Equations 9-63a or 9-63b and AISC *Manual* Table 9-4, as follows (including a ¼ in. tolerance to account for possible beam underrun):

| LRFD | ASD |
|------|-----|
| $W_{min} = \frac{R_u - \phi R_5}{\phi R_6} + \text{setback} + \text{underrun}$ | $W_{min} = \frac{R_a - R_5/\Omega}{R_6/\Omega} + \text{setback} + \text{underrun}$ |
| $= \frac{125 \text{ kips} - 75.9 \text{ kips}}{7.95 \text{ kip/in.}} + \frac{1}{2} \text{ in.} + \frac{1}{4} \text{ in.}$ | $= \frac{83.5 \text{ kips} - 50.6 \text{ kips}}{5.30 \text{ kip/in.}} + \frac{1}{2} \text{ in.} + \frac{1}{4} \text{ in.}$ |
| $= 6.93 \text{ in.}$ | $= 6.96 \text{ in.}$ |

The minimum stiffener width for web local yielding of the beam, for the force applied less than the depth of the beam from the end of the beam, is determined from AISC *Manual* Equations 9-60a or 9-60b and AISC *Manual* Table 9-4, as follows (including a ¼ in. tolerance to account for possible beam underrun):

| LRFD | ASD |
|------|-----|
| $W_{min} = \frac{R_u - \phi R_1}{\phi R_2} + \text{setback} + \text{underrun}$ | $W_{min} = \frac{R_a - R_1/\Omega}{R_2/\Omega} + \text{setback} + \text{underrun}$ |
| $= \frac{125 \text{ kips} - 64.0 \text{ kips}}{21.5 \text{ kip/in.}} + \frac{1}{2} \text{ in.} + \frac{1}{4} \text{ in.}$ | $= \frac{83.5 \text{ kips} - 42.6 \text{ kips}}{14.3 \text{ kip/in.}} + \frac{1}{2} \text{ in.} + \frac{1}{4} \text{ in.}$ |
| $= 3.59 \text{ in.}$ | $= 3.61 \text{ in.}$ |

Use $W = 7$ in.

Check assumption:

---

# IIA-162

$$\frac{l_b}{d} = \frac{W - \text{setback} - \text{underrun}}{d}$$
$$= \frac{7 \text{ in.} - \frac{1}{2} \text{ in.} - \frac{1}{4} \text{ in.}}{21.1 \text{ in.}}$$
$$= 0.296 > 0.2 \quad \textbf{o.k.}$$

*Stiffener Length and Stiffener-to-Column Flange Weld Size*

Use a stiffener with $l = 15$ in. and 5⁄16 in. fillet welds.

From AISC *Manual* Table 10-8, with $W = 7$ in.:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 139 \text{ kips} > 125 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 93.0 \text{ kips} > 83.5 \text{ kips} \quad \textbf{o.k.}$ |

*Seat Plate Welds*

Use 5⁄16 in. fillet welds on each side of the stiffener. From AISC *Manual* Figure 10-11(b), minimum length of seat plate-to-column flange weld is $0.2l = 3$ in. As discussed in AISC *Manual* Part 10, the weld between the seat plate and stiffener plate is required to have a strength equal to or greater than the weld between the seat plate and the column flange, use 5⁄16 in. fillet welds on each side of the stiffener to the seat plate; length of weld = 6 in. per side.

*Seat Plate Dimensions*

A dimension of 9 in. is adequate to accommodate the ¾-in.-diameter bolts on a 5½ in. gage connecting the beam flange to the seat plate.

Use a PL⅜ in.×7 in.×9 in. for the seat.

*Stiffener Plate Thickness*

As discussed in AISC *Manual* Part 10, the minimum stiffener plate thickness to develop the seat plate weld for $F_y =$ 50 ksi plate material is:

$$t_{min} = 1.5w$$
$$= 1.5(5⁄16 \text{ in.})$$
$$= 0.469 \text{ in.}$$

As discussed in AISC *Manual* Part 10, the minimum plate thickness for a stiffener and beam with $F_y = 50$ ksi is:

$$t_{min} = \left(\frac{50 \text{ ksi}}{50 \text{ ksi}}\right)t_w$$
$$= \left(\frac{50 \text{ ksi}}{50 \text{ ksi}}\right)(0.430 \text{ in.})$$
$$= 0.430 \text{ in.} < 0.469 \text{ in.}$$

Use a PL⅝ in.×7 in.×1 ft 3 in.

---

# IIA-163

*Top Angle, Bolts, and Welds*

Use an L4×4×¼ with two ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) through the supported beam leg of the angle. Use a 3⁄16 in. fillet weld along the toe of the angle to the column flange. See discussion in AISC *Manual* Part 10.

*Conclusion*

The connection design shown in Figure II.A-14-1 is acceptable.

---

# IIA-164

# EXAMPLE II.A-15 STIFFENED SEATED CONNECTION—WELDED STIFFENING ELEMENT (BEAM-TO-COLUMN WEB)

## Given:

Verify the stiffened seated connection between an ASTM A992/A992M W21×68 beam and an ASTM A992/A992M W14×90 column web, as shown in Figure II.A-15-1, to support the following beam end reactions:

$R_D = 21 \text{ kips}$
$R_L = 62.5 \text{ kips}$

Use 70-ksi weld electrodes and ASTM A572/A572M Grade 50 angles and plate.

<div style="text-align: center;">
<img src="connection_diagram" alt="Detailed connection diagram showing:
- W14×90 column web
- W21×68 beam
- Stiffener fit to bear
- L4×4×¼, top angle, shop attached to beam
- Weld toe only
- ½" nominal setback
- 3" dimension
- ⅞" dimension
- 9" height
- 4" (optional) dimension
- PL⅜×7×9" stiffener plate
- 5⁄16 welds (6 places)
- PL⅜×7×1'-3" optional trim lines
- W = 7" width
- 5⁄16 welds
- 5⁄8" dimension
- 5½" spacing
- Dimensions l = 1'-3", ¾" dia. Group 120, thread condition N, std. holes
- Optional location top angle">
</div>

*Fig. II.A-15-1. Connection geometry for Example II.A-15.*

## Solution:

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Beam and column
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

Angle and Plates
ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

---

# IIA-165

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W21×68
$d = 21.1$ in.
$t_w = 0.430$ in.
$b_f = 8.27$ in.
$t_f = 0.685$ in.
$k_{des} = 1.19$ in.

Column
W14×90
$t_w = 0.440$ in.
$T = 10$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(21 \text{ kips}) + 1.6(62.5 \text{ kips})$ | $R_a = 21 \text{ kips} + 62.5 \text{ kips}$ |
| $= 125 \text{ kips}$ | $= 83.5 \text{ kips}$ |

*Required Stiffener Width*

The minimum stiffener width, $W_{min}$, is determined based on the limit states of web local yielding and web local crippling for the beam.

The minimum stiffener width for web local crippling of the beam web, for the force applied less than one-half of the depth of the beam from the end of the beam and assuming $l_b/d > 0.2$, is determined from AISC *Manual* Equations 9-63a or 9-63b and AISC *Manual* Table 9-4, as follows (including a ¼ in. tolerance to account for possible beam underrun):

| LRFD | ASD |
|------|-----|
| $W_{min} = \frac{R_u - \phi R_5}{\phi R_6} + \text{setback} + \text{underrun}$ | $W_{min} = \frac{R_a - R_5/\Omega}{R_6/\Omega} + \text{setback} + \text{underrun}$ |
| $= \frac{125 \text{ kips} - 75.9 \text{ kips}}{7.95 \text{ kip/in.}} + \frac{1}{2} \text{ in.} + \frac{1}{4} \text{ in.}$ | $= \frac{83.5 \text{ kips} - 50.6 \text{ kips}}{5.30 \text{ kip/in.}} + \frac{1}{2} \text{ in.} + \frac{1}{4} \text{ in.}$ |
| $= 6.93 \text{ in.}$ | $= 6.96 \text{ in.}$ |

The minimum stiffener width for web local yielding of the beam, for the force applied less than the depth of the beam from the end of the beam, is determined from AISC *Manual* Equations 9-60a or 9-60b and AISC *Manual* Table 9-4, as follows (including a ¼ in. tolerance to account for possible beam underrun):

| LRFD | ASD |
|------|-----|
| $W_{min} = \frac{R_u - \phi R_1}{\phi R_2} + \text{setback} + \text{underrun}$ | $W_{min} = \frac{R_a - R_1/\Omega}{R_2/\Omega} + \text{setback} + \text{underrun}$ |
| $= \frac{125 \text{ kips} - 64.0 \text{ kips}}{21.5 \text{ kip/in.}} + \frac{1}{2} \text{ in.} + \frac{1}{4} \text{ in.}$ | $= \frac{83.5 \text{ kips} - 42.6 \text{ kips}}{14.3 \text{ kip/in.}} + \frac{1}{2} \text{ in.} + \frac{1}{4} \text{ in.}$ |
| $= 3.59 \text{ in.}$ | $= 3.61 \text{ in.}$ |

Use $W = 7$ in.

Check assumption:

---

# IIA-166

$$\frac{l_b}{d} = \frac{W - \text{setback} - \text{underrun}}{d}$$
$$= \frac{7 \text{ in.} - \frac{1}{2} \text{ in.} - \frac{1}{4} \text{ in.}}{21.1 \text{ in.}}$$
$$= 0.296 > 0.2 \quad \textbf{o.k.}$$

*Stiffener Length and Stiffener-to-Column Web Weld Size*

Use a stiffener with $l = 15$ in. and 5⁄16 in. fillet welds.

From AISC *Manual* Table 10-8, with $W = 7$ in., the weld available strength is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 139 \text{ kips} > 125 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 93.0 \text{ kips} > 83.5 \text{ kips} \quad \textbf{o.k.}$ |

*Seat Plate Welds*

Use 5⁄16 in. fillet welds on each side of the stiffener. From AISC *Manual* Figure 10-11(b), the minimum length of the seat plate-to-column web weld is $0.2l = 3$ in. As discussed in AISC *Manual* Part 10, the weld between the seat plate and stiffener plate is required to have a strength equal to or greater than the weld between the seat plate and the column web, use 5⁄16 in. fillet welds on each side of the stiffener to the seat plate; length of weld = 6 in. per side.

*Seat Plate Dimensions*

A dimension of 9 in. is adequate to accommodate the ¾-in.-diameter bolts on a 5½ in. gage connecting the beam flange to the seat plate.

Use a PL⅜ in.×7 in.×9 in. for the seat.

*Stiffener Plate Thickness*

As discussed in AISC *Manual* Part 10, the minimum stiffener plate thickness to develop the seat plate weld for $F_y =$ 50 ksi plate material is:

$$t_{min} = 1.5w$$
$$= 1.5(5⁄16 \text{ in.})$$
$$= 0.469 \text{ in.}$$

As discussed in AISC *Manual* Part 10, the minimum plate thickness for a beam and stiffener with $F_y = 50$ ksi is:

$$t_{min} = \left(\frac{50 \text{ ksi}}{50 \text{ ksi}}\right)t_w$$
$$= \left(\frac{50 \text{ ksi}}{50 \text{ ksi}}\right)(0.430 \text{ in.})$$
$$= 0.430 \text{ in.} < 0.469 \text{ in.}$$

Use a PL⅝ in.×7 in.×1 ft 3 in.

*Top Angle, Bolts, and Welds*

---

# IIA-167

Use an L4×4×¼ with two ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) through the supported beam leg of the angle. Use a 3⁄16 in. fillet weld along the toe of the angle to the column web. See discussion in AISC *Manual* Part 10.

*Column Web*

If the seat is welded to a column web, the base metal strength of the column must be checked.

If only one side of the column web has a stiffened seated connection, then:

$$t_{min} = \frac{3.09D}{F_u}$$ (*Manual* Eq. 9-6)
$$= \frac{3.09(5 \text{ sixteenths})}{65 \text{ ksi}}$$
$$= 0.238 \text{ in.} < 0.440 \text{ in.} \quad \textbf{o.k.}$$

If both sides of the column web have a stiffened seated connection, then:

$$t_{min} = \frac{6.19D}{F_u}$$ (*Manual* Eq. 9-7)
$$= \frac{6.19(5 \text{ sixteenths})}{65 \text{ ksi}}$$
$$= 0.476 \text{ in.} > 0.440 \text{ in.} \quad \textbf{n.g.}$$

The column is sufficient for a one-sided stiffened seated connection. For a two-sided connection, the weld available strength must be reduced as discussed in AISC *Manual* Part 10.

Note: Additional detailing considerations for stiffened seated connections are given in Part 10 of the AISC *Manual*.

*Conclusion*

The connection design shown in Figure II.A-15-1 is acceptable.

---

# IIA-168

# EXAMPLE II.A-16 OFFSET WELDED UNSTIFFENED SEATED CONNECTION (BEAM-TO-COLUMN FLANGE)

## Given:

Verify the seat angle and weld size required for the unstiffened seated connection between an ASTM A992/A992M W14×38 beam and an ASTM A992/A992M W12×65 column flange connection with an offset of 5½ in., as shown in Figure II.A-16-1, to support the following beam end reactions:

$R_D = 5 \text{ kips}$
$R_L = 15 \text{ kips}$

Use an ASTM A572/A572M Grade 50 angle and 70-ksi weld electrodes.

<div style="text-align: center;">
<img src="connection_diagram" alt="Connection diagram showing:
Section A-A view with:
- W14×38 C beam with 5½" offset
- W12×65 C column
- L7×4×⅝×6" (4" OSL) seat angle
- 3½" dimension
- Note A: End return is omitted because the AWS Code does not permit weld returns to be carried around the corner formed by the column flange toe and seat angle heel.
- Note B: Beam and top angle not shown for clarity.
- Note C: The nominal setback of the beam from the face of the column flange is ½ in.
- ¾" dia. Group 120, thread condition N, std. holes
- 5⁄16 and 5⁄16 welds shown
- 3½" and 3½" spacing dimensions">
</div>

*Fig. II.A-16-1. Connection geometry for Example II.A-16.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam and column
ASTM A992/A992M
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

Angle
ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W14×38
$d = 14.1$ in.
$k_{des} = 0.915$ in.

---

# IIA-169

Column
W12×65
$t_f = 0.605$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(5 \text{ kips}) + 1.6(15 \text{ kips})$ | $R_a = 5 \text{ kips} + 15 \text{ kips}$ |
| $= 30.0 \text{ kips}$ | $= 20.0 \text{ kips}$ |

*Minimum Bearing Length*

From AISC *Manual* Part 10, the minimum required bearing length, $l_{b\,min}$, is the length of bearing required for the limit states of web local yielding and web local crippling of the beam, but not less than $k_{des}$.

From AISC *Manual* Equations 9-60a or 9-60b and AISC *Manual* Table 9-4, the minimum required bearing length for web local yielding is:

| LRFD | ASD |
|------|-----|
| $l_{b\,min} = \frac{R_u - \phi R_1}{\phi R_2} \geq k_{des}$ | $l_{b\,min} = \frac{R_a - R_1/\Omega}{R_2/\Omega} \geq k_{des}$ |
| $= \frac{30.0 \text{ kips} - 35.5 \text{ kips}}{15.5 \text{ kips/in.}} \geq 0.915 \text{ in.}$ | $= \frac{20.0 \text{ kips} - 23.6 \text{ kips}}{10.3 \text{ kips/in.}} \geq 0.915 \text{ in.}$ |
| This results in a negative quantity; therefore, | This results in a negative quantity; therefore, |
| $l_{b\,min} = k_{des} = 0.915 \text{ in.}$ | $l_{b\,min} = k_{des} = 0.915 \text{ in.}$ |

From AISC *Manual* Equations 9-62a or 9-62b and AISC *Manual* Table 9-4, the minimum required bearing length for web local crippling, assuming $l_b/d \leq 0.2$, is:

| LRFD | ASD |
|------|-----|
| $l_{b\,min} = \frac{R_u - \phi R_3}{\phi R_4} \geq k_{des}$ | $l_{b\,min} = \frac{R_a - R_3/\Omega}{R_4/\Omega} \geq k_{des}$ |
| $= \frac{30.0 \text{ kips} - 44.7 \text{ kips}}{4.45 \text{ kips/in.}} \geq 0.915 \text{ in.}$ | $= \frac{20.0 \text{ kips} - 29.8 \text{ kips}}{2.96 \text{ kips/in.}} \geq 0.915 \text{ in.}$ |
| This results in a negative quantity; therefore, | This results in a negative quantity; therefore, |
| $l_{b\,min} = k_{des} = 0.915 \text{ in.}$ | $l_{b\,min} = k_{des} = 0.915 \text{ in.}$ |

Check assumption:

$$\frac{l_b}{d} = \frac{0.915 \text{ in.}}{14.1 \text{ in.}}$$
$$= 0.0649 < 0.2 \quad \textbf{o.k.}$$

*Seat Angle and Welds*

The required strength for the righthand weld can be determined by summing moments about the lefthand weld.

---

# IIA-170

| LRFD | ASD |
|------|-----|
| $R_{uR} = \frac{(30.0 \text{ kips})(3.00 \text{ in.})}{3.50 \text{ in.}}$ | $R_{aR} = \frac{(20.0 \text{ kips})(3.00 \text{ in.})}{3.50 \text{ in.}}$ |
| $= 25.7 \text{ kips}$ | $= 17.1 \text{ kips}$ |

Conservatively design the seat for twice the force in the more highly loaded weld. Therefore, design the seat for the following:

| LRFD | ASD |
|------|-----|
| $R_u = 2(25.7 \text{ kips})$ | $R_a = 2(17.1 \text{ kips})$ |
| $= 51.4 \text{ kips}$ | $= 34.2 \text{ kips}$ |

Use a 6 in. angle length with a ⅝ in. thickness and a 3½ in. minimum outstanding leg and conservatively using $l_{b\,req} = 15⁄16$ in., from AISC *Manual* Table 10-6:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 113 \text{ kips} > 51.4 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 75.0 \text{ kips} > 34.2 \text{ kips} \quad \textbf{o.k.}$ |

Use an L7×4×⅝ (4 in. OSL), 6 in. long with 5⁄16 in. fillet welds. From AISC *Manual* Table 10-6, the weld available strength is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 53.4 \text{ kips} > 51.4 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 35.6 \text{ kips} > 34.2 \text{ kips} \quad \textbf{o.k.}$ |

Use an L7×4×⅝×0 ft 6 in. for the seat angle. Use two ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) to connect the beam to the seat angle. Weld the angle to the column with 5⁄16 in. fillet welds.

*Top Angle, Bolts, and Welds*

Use an L4×4×¼ with two ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) through the outstanding leg of the angle.

Use a 3⁄16 in. fillet weld along the toe of the angle to the column flange [maximum size permitted by AISC *Specification* Section J2.2b(b)(2)].

*Conclusion*

The connection is found to be adequate as given for the applied loads.

---

# IIA-171

# EXAMPLE II.A-17A SINGLE-PLATE CONNECTION (CONVENTIONAL BEAM-TO-COLUMN FLANGE)

## Given:

Verify the available strength of the single-plate connection between an ASTM A992/A992M W16×50 beam and an ASTM A992/A992M W14×90 column flange, as shown in Figure II.A-17A-1, to support the following beam end reactions:

$R_D = 8$ kips
$R_L = 25$ kips

Use 70-ksi electrodes and an ASTM A572/A572M Grade 50 plate.

This example is repeated using the following two procedures:

Part A: Determine the available connection strength using the tables in *Manual* Part 10.
Part B: Determine the available connection strength by checking individual limit states.

<div style="text-align: center;">
<img src="connection_diagram" alt="Connection diagram showing:
- W14×90 column
- W16×50 beam
- PL¼×4½×0'-11½" single plate
- 4 @ 3" = 1'-0" vertical spacing
- ¾" dia. Group 120 bolts, thread condition N, std. holes
- 3" edge distance at top
- 1½" edge distance
- 1⅛" and 1⅛" horizontal dimensions
- ⅜ and ⅜ fillet welds
- a = 3" dimension">
</div>

*Fig. II.A-17A-1. Connection geometry for Example II.A-17A.*

## Solution:

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Beam and column
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

---

# IIA-172

Plate
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W16×50
$d = 16.3$ in.
$t_w = 0.380$ in.

Column
W14×90
$t_f = 0.710$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(8 \text{ kips}) + 1.6(25 \text{ kips})$ | $R_a = 8 \text{ kips} + 25 \text{ kips}$ |
| $= 49.6 \text{ kips}$ | $= 33.0 \text{ kips}$ |

*Part A— Determine the Available Connection Strength Using the Tables in Manual Part 10*

*Single Plate Available Strength*

AISC *Manual* Table 10-10a includes checks for the limit states of shear rupture of the plate, block shear rupture of the plate, and weld shear.

Check four rows of ¾-in.-diameter bolts in standard holes, ¼ in. plate thickness, and ⅜ in. fillet weld size. From AISC *Manual* Table 10-10a, the weld and single-plate available strength is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 58.5 \text{ kips} > 49.6 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 39.0 \text{ kips} > 33.0 \text{ kips} \quad \textbf{o.k.}$ |

*Available Shear Transfer Strength at Bolt Holes*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength determined in accordance with AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the plate at the bolt hole determined in accordance with AISC *Specification* Section J3.11a, and (3) the available bearing or tearout strength of the beam web at the bolt hole determined in accordance with AISC *Specification* Section J3.11a.

From AISC *Manual* Table 10-10b, the available bolt shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) in single shear is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9 \text{ kips}$ | $\frac{r_n}{\Omega} = 11.9 \text{ kips}$ |

From AISC *Manual* Table 10-10b, the available bearing and tearout strength of the plate per bolt for ¾-in.-diameter bolts in standard holes is:

---

# IIA-173

| LRFD | ASD |
|------|-----|
| For the edge bolt ($l_{ev} = 1¼$ in.): | For the edge bolt ($l_{ev} = 1¼$ in.): |
| $\phi r_n = (49.4 \text{ kips/in.})(¼ \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kips/in.})(¼ \text{ in.})$ |
| $= 12.4 \text{ kips}$ | $= 8.23 \text{ kips}$ |
|  |  |
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kips/in.})(¼ \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(¼ \text{ in.})$ |
| $= 22.0 \text{ kips}$ | $= 14.6 \text{ kips}$ |

From AISC *Manual* Table 10-10b, the available bearing and tearout strength of the beam web per bolt for ¾-in.- diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kips/in.})(0.380 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(0.380 \text{ in.})$ |
| $= 33.4 \text{ kips}$ | $= 22.2 \text{ kips}$ |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the plate for a non-edge bolt, and the available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min \begin{cases} 17.9 \text{ kips,} \\ 22.0 \text{ kips,} \\ 33.4 \text{ kips} \end{cases}$ | $\frac{r_{n,top}}{\Omega} = \min \begin{cases} 11.9 \text{ kips,} \\ 14.6 \text{ kips,} \\ 22.2 \text{ kips} \end{cases}$ |
| $= 17.9 \text{ kips}$ | $= 11.9 \text{ kips}$ |

At the middle connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the plate for a non-edge bolt, and the available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,mid} = \min \begin{cases} 17.9 \text{ kips,} \\ 22.0 \text{ kips,} \\ 33.4 \text{ kips} \end{cases}$ | $\frac{r_{n,mid}}{\Omega} = \min \begin{cases} 11.9 \text{ kips,} \\ 14.6 \text{ kips,} \\ 22.2 \text{ kips} \end{cases}$ |
| $= 17.9 \text{ kips}$ | $= 11.9 \text{ kips}$ |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the plate for an edge bolt, and the available bearing and tearout strength of the beam web for a non-edge bolt:

---

# IIA-174

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min \begin{cases} 17.9 \text{ kips,} \\ 12.4 \text{ kips,} \\ 33.4 \text{ kips} \end{cases}$ | $\frac{r_{n,bot}}{\Omega} = \min \begin{cases} 11.9 \text{ kips,} \\ 8.23 \text{ kips,} \\ 22.2 \text{ kips} \end{cases}$ |
| $= 12.4 \text{ kips}$ | $= 8.23 \text{ kips}$ |

To account for eccentricity, the available shear transfer strength is multiplied by the factor $C/n$. From AISC *Manual* Table 10-10b, for 4 bolts in standard holes:

$C/n = 0.885$

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = (C/n)\left[\phi r_{n,top} + \phi r_{n,mid} (n-2) + \phi r_{n,bot}\right]$ | $\frac{R_n}{\Omega} = (C/n)\left[\frac{r_{n,top}}{\Omega} + \frac{r_{n,mid}}{\Omega} (n-2) + \frac{r_{n,bot}}{\Omega}\right]$ |
| $= (0.885)\left[17.9 \text{ kips} + (17.9 \text{ kips})(4-2) + 12.4 \text{ kips}\right]$ | $= (0.885)\left[11.9 \text{ kips} + (11.9 \text{ kips})(4-2) + 8.23 \text{ kips}\right]$ |
| $= 58.5 \text{ kips} > 49.6 \text{ kips} \quad \textbf{o.k.}$ | $= 38.9 \text{ kips} > 33.0 \text{ kips} \quad \textbf{o.k.}$ |

Note: To provide for stability during erection, it is recommended that the minimum plate length be one-half the T-dimension of the beam to be supported. AISC *Manual* Table 10-1a may be used as a reference to determine the recommended maximum and minimum connection lengths for a supported beam. Block shear rupture, shear yielding, and shear rupture will not control for an uncoped section.

*Conclusion*

The available shear strength of the connection is controlled by the available shear transfer strength at bolt holes.

| LRFD | ASD |
|------|-----|
| $\phi R_n = 58.5 \text{ kips} > 49.6 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 38.9 \text{ kips} > 33.0 \text{ kips} \quad \textbf{o.k.}$ |

The connection is found to be adequate as given for the applied loads.

*Part B—Verify the Available Connection Strength by Checking Individual Limit States*

*Connection Eccentricity*

Connection eccentricity is determined using AISC *Manual* Table 10-9. For a connection with $n = 4$ using standard holes:

$$e = \frac{a}{2}$$
$$= \frac{3 \text{ in.}}{2}$$
$$= 1.50 \text{ in.}$$

*Dimensional Limitations*

---

# IIA-175

Either the plate thickness or the beam web thickness must satisfy the maximum thickness provided in AISC *Manual* Table 10-9. For a connection with $n = 4$ using standard holes:

$$t_p \text{ or } t_w \leq \frac{d}{2} + \frac{1}{16} \text{ in.}$$
$$= \frac{¾ \text{ in.}}{2} + \frac{1}{16} \text{ in.}$$
$$= 0.438 \text{ in.}$$

Both the plate ($t = ¼$ in.) and beam web ($t_w = 0.380$ in.) satisfy this limit. **o.k.**

The vertical bolt edge distance on the plate must satisfy AISC *Specification* Table J3.4 requirements. For a ¾-in.- diameter bolt, the minimum edge distance is 1 in.

$$l_{ev} \geq 1 \text{ in.}$$
$$1¼ \text{ in.} > 1 \text{ in.} \quad \textbf{o.k.}$$

The horizontal bolt edge distance on the plate and beam web must be greater than or equal to $2d$.

$$2d = 2\left(¾ \text{ in.}\right)$$
$$= 1.50 \text{ in.} \quad \textbf{o.k.}$$

*Available Weld Strength*

From AISC *Manual* Part 10, the weld between the single plate and the support should be sized as $(5/8)t_p$.

$$(5/8)t_p = (5/8)(¼ \text{ in.})$$
$$= 0.156 \text{ in.}$$

Use ⅜ in. fillet welds.

*Support Thickness*

The minimum support thickness that matches the column flange strength to the ⅜ in. fillet weld strength is:

$$t_{min} = \frac{3.09D}{F_u}$$ (*Manual* Eq. 9-6)
$$= \frac{3.09(3)}{65 \text{ ksi}}$$
$$= 0.143 \text{ in.} < 0.710 \text{ in.} \quad \textbf{o.k.}$$

*Shear Strength of Single Plate*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the single plate is determined as follows:

$$A_{gv} = lt$$
$$= (11½ \text{ in.})(¼ \text{ in.})$$
$$= 2.88 \text{ in.}^2$$

---

# IIA-176

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(2.88 \text{ in.}^2)$$
$$= 86.4 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(86.4 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{86.4 \text{ kips}}{1.50}$ |
| $= 86.4 \text{ kips} > 49.6 \text{ kips} \quad \textbf{o.k.}$ | $= 57.6 \text{ kips} > 33.0 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the single plate is determined using the net area determined in accordance with AISC *Specification* Section B4.3b.

$$A_{nv} = \left[l - n\left(d_h + \frac{1}{16} \text{ in.}\right)\right]t$$
$$= \left[11½ \text{ in.} - 4\left(^{13}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right](¼ \text{ in.})$$
$$= 2.00 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(2.00 \text{ in.}^2)$$
$$= 78.0 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(78.0 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{78.0 \text{ kips}}{2.00}$ |
| $= 58.5 \text{ kips} > 49.6 \text{ kips} \quad \textbf{o.k.}$ | $= 39.0 \text{ kips} > 33.0 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture of Single Plate*

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture on the single plate is determined as follows.

$$R_{bsv} = 0.60F_u A_{nv} + U_{bs} F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs} F_u A_{nt}$$ (from *Spec.* Eq. J4-5)

where

$$A_{gv} = (l - l_{ev})t$$
$$= (11½ \text{ in.} - 1¼ \text{ in.})(¼ \text{ in.})$$
$$= 2.56 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (n - 0.5)(d_h + \frac{1}{16} \text{ in.})t$$
$$= 2.56 \text{ in.}^2 - (4 - 0.5)\left(^{13}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)(¼ \text{ in.})$$
$$= 1.79 \text{ in.}^2$$

---

# IIA-177

$$A_{nt} = \left[l_{eh} - 0.5\left(d_h + \frac{1}{16} \text{ in.}\right)\right]t$$
$$= \left[1⅛ \text{ in.} - 0.5\left(^{13}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right](¼ \text{ in.})$$
$$= 0.266 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_{bsv} = 0.60(65 \text{ ksi})(1.79 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.266 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(2.56 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.266 \text{ in.}^2)$$
$$= 87.1 \text{ kips} < 94.1 \text{ kips}$$

Therefore:

$$R_{bsv} = 87.1 \text{ kips}$$

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture of the single plate is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_{bsv} = 0.75(87.1 \text{ kips})$ | $\frac{R_{bsv}}{\Omega} = \frac{87.1 \text{ kips}}{2.00}$ |
| $= 65.3 \text{ kips} > 49.6 \text{ kips} \quad \textbf{o.k.}$ | $= 43.6 \text{ kips} > 33.0 \text{ kips} \quad \textbf{o.k.}$ |

*Available Shear Transfer Strength at Bolt Holes*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength determined in accordance with AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the single plate at the bolt hole determined in accordance with AISC *Specification* Section J3.11a, and (3) the available bearing or tearout strength of the beam web at the bolt hole determined in accordance with AISC *Specification* Section J3.11a.

From AISC *Manual* Table 7-1, the available shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9 \text{ kips}$ | $\frac{r_n}{\Omega} = 11.9 \text{ kips}$ |

The available bearing and tearout strength of the single plate at a bolt adjacent to an edge is determined using AISC *Manual* Table 7-5, with $l_e = 1¼$ in.:

| LRFD | ASD |
|------|-----|
| $\phi r_n = (49.4 \text{ kips/in.})(¼ \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kips/in.})(¼ \text{ in.})$ |
| $= 12.4 \text{ kips}$ | $= 8.23 \text{ kips}$ |

The available bearing and tearout strength of the single plate at a bolt not adjacent to an edge is determined using AISC *Manual* Table 7-4 with $s = 3$ in.

---

# IIA-178

| LRFD | ASD |
|------|-----|
| $\phi r_n = (87.8 \text{ kips/in.})(¼ \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(¼ \text{ in.})$ |
| $= 22.0 \text{ kips}$ | $= 14.6 \text{ kips}$ |

The available bearing and tearout strength for all bolts in the beam web is determined using AISC *Manual* Table 7-4 with $s = 3$ in.

| LRFD | ASD |
|------|-----|
| $\phi r_n = (87.8 \text{ kips/in.})(0.380 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(0.380 \text{ in.})$ |
| $= 33.4 \text{ kips}$ | $= 22.2 \text{ kips}$ |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the single plate for a non-edge bolt, and the available bearing and tearout strength of the beam web:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min \begin{cases} 17.9 \text{ kips,} \\ 22.0 \text{ kips,} \\ 33.4 \text{ kips} \end{cases}$ | $\frac{r_{n,top}}{\Omega} = \min \begin{cases} 11.9 \text{ kips,} \\ 14.6 \text{ kips,} \\ 22.2 \text{ kips} \end{cases}$ |
| $= 17.9 \text{ kips}$ | $= 11.9 \text{ kips}$ |

At the middle connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the single plate for a non-edge bolt, and the available bearing and tearout strength of the beam web:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,mid} = \min \begin{cases} 17.9 \text{ kips,} \\ 22.0 \text{ kips,} \\ 33.4 \text{ kips} \end{cases}$ | $\frac{r_{n,mid}}{\Omega} = \min \begin{cases} 11.9 \text{ kips,} \\ 14.6 \text{ kips,} \\ 22.2 \text{ kips} \end{cases}$ |
| $= 17.9 \text{ kips}$ | $= 11.9 \text{ kips}$ |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the single plate for an edge bolt, and the available bearing and tearout strength of the beam web:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min \begin{cases} 17.9 \text{ kips,} \\ 12.4 \text{ kips,} \\ 33.4 \text{ kips} \end{cases}$ | $\frac{r_{n,bot}}{\Omega} = \min \begin{cases} 11.9 \text{ kips,} \\ 8.23 \text{ kips,} \\ 22.2 \text{ kips} \end{cases}$ |
| $= 12.4 \text{ kips}$ | $= 8.23 \text{ kips}$ |

To account for eccentricity, the available shear transfer strength is multiplied by the factor $C/n$. From AISC *Manual* Table 7-6 with Angle $= 0°$, $n = 4$, and interpolating for $e = 1.50$ in.:

$$C = 3.54$$

The available shear transfer strength at the bolt holes is:

---

# IIA-179

| LRFD | ASD |
|------|-----|
| $\phi R_n = \left(\frac{C}{n}\right)\left[\phi r_{n,top} + \phi r_{n,mid} (n-2) + \phi r_{n,bot}\right]$ | $\frac{R_n}{\Omega} = \left(\frac{C}{n}\right)\left[\frac{r_{n,top}}{\Omega} + \frac{r_{n,mid}}{\Omega} (n-2) + \frac{r_{n,bot}}{\Omega}\right]$ |
| $= \left(\frac{3.54}{4}\right)\left[17.9 \text{ kips} + 17.9 \text{ kips}(4-2) + 12.4 \text{ kips}\right]$ | $= \left(\frac{3.54}{4}\right)\left[11.9 \text{ kips} + 11.9 \text{ kips}(4-2) + 8.23 \text{ kips}\right]$ |
| $= 58.5 \text{ kips} > 49.6 \text{ kips} \quad \textbf{o.k.}$ | $= 38.9 \text{ kips} > 33.0 \text{ kips} \quad \textbf{o.k.}$ |

*Available Beam Web Strength*

Because the beam is not coped, the limit states of block shear rupture and shear rupture of the beam are not applicable. The beam web is adequate for the required loading.

*Conclusion*

The available shear strength of the connection is controlled by the available shear transfer strength at bolt holes.

| LRFD | ASD |
|------|-----|
| $\phi R_n = 58.5 \text{ kips} > 49.6 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 38.9 \text{ kips} > 33.0 \text{ kips} \quad \textbf{o.k.}$ |

The connection is found to be adequate as given for the applied loads.

---

# IIA-180

# EXAMPLE II.A-17B SINGLE-PLATE CONNECTION SUBJECT TO AXIAL AND SHEAR LOADING (BEAM-TO-COLUMN FLANGE)

## Given:

Verify the available strength of a single-plate connection for an ASTM A992/A992M W18×50 beam connected to an ASTM A992/A992M W14×90 column flange, as shown in Figure II.A-17B-1, to support the following beam end reactions:

| LRFD | ASD |
|------|-----|
| Shear, $V_u = 75$ kips | Shear, $V_a = 50$ kips |
| Axial tension, $N_u = 60$ kips | Axial tension, $N_a = 40$ kips |

Use 70-ksi electrodes and an ASTM A572/A572M Grade 50 plate. The beam is assumed to be braced against rotation about the longitudinal axis.

<div style="text-align: center;">
<img src="connection_diagram" alt="Connection diagram showing:
- W14×90 column
- W18×50 beam
- PL½×5×1'-2½" single plate
- 2½", 2½" edge distances at top
- 4 @ 3" = 1'-0" vertical spacing
- 1⅛" and 1⅛" horizontal dimensions
- ¾" and 1¾" dimensions at bottom
- V (vertical) and N (axial) force arrows
- ⅞" dia. Group 120 bolts, thread condition N, std. holes
- ⅝ and ⅝ fillet welds">
</div>

*Fig. II.A-17B-1. Connection geometry for Example II.A-17B.*

## Solution:

From AISC *Manual* Table 2-4 and Table 2-5, the material properties are as follows:

Beam and column
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Plate
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

---

# IIA-181

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W18×50
$A_g = 14.7$ in.<sup>2</sup>
$d = 18.0$ in.
$t_w = 0.355$ in.
$t_f = 0.570$ in.

Column
W14×90
$t_f = 0.710$ in.

From AISC *Specification* Table J3.3, for ⅞-in.-diameter bolts with standard holes:

$d_h = ^{15}/{16}$ in.

The resultant load is:

| LRFD | ASD |
|------|-----|
| $R_u = \sqrt{V_u^2 + N_u^2}$ | $R_a = \sqrt{V_a^2 + N_a^2}$ |
| $= \sqrt{(75 \text{ kips})^2 + (60 \text{ kips})^2}$ | $= \sqrt{(50 \text{ kips})^2 + (40 \text{ kips})^2}$ |
| $= 96.0$ kips | $= 64.0$ kips |

The resultant load angle measured from the vertical is:

| LRFD | ASD |
|------|-----|
| $\theta = \tan^{-1}\left(\frac{60 \text{ kips}}{75 \text{ kips}}\right)$ | $\theta = \tan^{-1}\left(\frac{40 \text{ kips}}{50 \text{ kips}}\right)$ |
| $= 38.7°$ | $= 38.7°$ |

*Bolt Shear Strength*

From AISC *Manual* Part 12, the eccentricity, $e$, is the distance from the support to the centroid of the bolt group.

$$e = a$$
$$= 2½ \text{ in.}$$

The coefficient for eccentrically loaded bolts is determined by interpolating from AISC *Manual* Table 7-6 for Angle = 30°, $n = 5$ and $e_x = 2½$ in. Note that 30° is used conservatively in order to employ AISC *Manual* Table 7-6. A direct analysis method can be performed to obtain a more precise value using the instantaneous center of rotation method.

$$C = 4.07$$

From AISC *Manual* Table 7-1, the available shear strength for a ⅞-in.-diameter, Group 120 bolt with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 24.3$ kips/bolt | $\frac{r_n}{\Omega} = 16.2$ kips/bolt |

---

# IIA-182

*Bolt Bearing*

Note that bolt bearing of the beam web will control over bearing of the plate because the beam web is thinner than the plate; therefore, this limit state will only be checked on the beam web.

The nominal bearing strength is determined using AISC *Specification* Equation J3-6b in lieu of Equation J3-6a, because plowing of the bolts in the beam web is desirable to provide some flexibility in the connection.

$$r_n = 3.0dtF_u$$ (from *Spec.* Eq. J3-6b)
$$= 3.0(⅞ \text{ in.})(0.355 \text{ in.})(65 \text{ ksi})$$
$$= 60.6 \text{ kips/bolt}$$

From AISC *Specification* Section J3.11, the available bearing strength of the beam per bolt is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(60.6 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{60.6 \text{ kips/bolt}}{2.00}$ |
| $= 45.5$ kips/bolt | $= 30.3$ kips/bolt |

*Bolt Tearout*

The nominal tearout strength is determined using AISC *Specification* Equation J3-6d in lieu of Equation J3-6c, because plowing of the bolts in the beam web is desirable to provide some flexibility in the connection. Because the direction of the load on the bolt is unknown, the minimum bolt edge distance of the beam web and plate is used to determine a worst case available tearout strength. If a computer program is available, the true $l_c$ can be calculated based on the instantaneous center of rotation.

For the beam web, the bolt edge distance in the horizontal direction controls for this design. Therefore, for worst case edge distance in the beam web, and considering possible length underrun of ¼ in. on the beam length:

$$l_c = l_{eh} - 0.5d_h - \text{underrun}$$
$$= 1⅜ \text{ in.} - 0.5(^{15}/{16} \text{ in.}) - ¼ \text{ in.}$$
$$= 1.03 \text{ in.}$$

$$r_n = 1.5l_ct F_u$$ (from *Spec.* Eq. J3-6d)
$$= 1.5(1.03 \text{ in.})(0.355 \text{ in.})(65 \text{ ksi})$$
$$= 35.7 \text{ kips/bolt}$$

For the plate, the bolt edge distance in the vertical direction controls for this design.

$$l_c = l_{ev} - 0.5d_h$$
$$= 1¼ \text{ in.} - 0.5(^{15}/{16} \text{ in.})$$
$$= 0.781 \text{ in.}$$

$$r_n = 1.5l_ct F_u$$ (from *Spec.* Eq. J3-6d)
$$= 1.5(0.781 \text{ in.})(½ \text{ in.})(65 \text{ ksi})$$
$$= 38.1 \text{ kips/bolt}$$

---

# IIA-183

Therefore, tearout of the beam web controls. Use $r_n = 35.7$ kips.

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(35.7 \text{ kips})$ | $\frac{r_n}{\Omega} = \frac{35.7 \text{ kips}}{2.00}$ |
| $= 26.8$ kips/bolt | $= 17.9$ kips/bolt |

*Strength of Bolted Connection*

Bolt shear is the controlling limit state for all bolts at the connection to the beam web. The available strength of the connection is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = C\phi r_n$ | $\frac{R_n}{\Omega} = \frac{Cr_n}{\Omega}$ |
| $= 4.07(24.3 \text{ kips/bolt})$ | $= 4.07(16.2 \text{ kips/bolt})$ |
| $= 98.9 \text{ kips} > 96.0 \text{ kips} \quad \textbf{o.k.}$ | $= 65.9 \text{ kips} > 64.0 \text{ kips} \quad \textbf{o.k.}$ |

*Strength of Weld*

A weld size of $(⅝)t_p$ is used to develop the strength of the shear plate, because, in general, the moment generated by this connection is indeterminate.

$$w = ⅝t_p$$
$$= ⅝(½ \text{ in.})$$
$$= ⅝ \text{ in.}$$

Use a two-sided ⅝ in. fillet weld.

*Shear Strength of Supporting Column Flange*

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the column flange is determined as follows:

$$A_{nv} = (2 \text{ shear planes})lt_f$$
$$= (2 \text{ shear planes})(14.5 \text{ in.})(0.710 \text{ in.})$$
$$= 20.6 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(20.6 \text{ in.}^2)$$
$$= 803 \text{ kips}$$

---

# IIA-184

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(803 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{803 \text{ kips}}{2.00}$ |
| $= 602 \text{ kips} > 75 \text{ kips} \quad \textbf{o.k.}$ | $= 402 \text{ kips} > 50 \text{ kips} \quad \textbf{o.k.}$ |

The available shear yielding strength of the column flange need not be checked because $A_{nv} = A_{gv}$ and shear rupture will control.

*Shear Yielding Strength of the Plate*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the plate is determined as follows:

$$A_{gv} = lt$$
$$= (14.5 \text{ in.})(½ \text{ in.})$$
$$= 7.25 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(7.25 \text{ in.}^2)$$
$$= 218 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(218 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{218 \text{ kips}}{1.50}$ |
| $= 218 \text{ kips} > 75 \text{ kips} \quad \textbf{o.k.}$ | $= 145 \text{ kips} > 50 \text{ kips} \quad \textbf{o.k.}$ |

*Tensile Yielding Strength of the Plate*

From AISC *Specification* Section J4.1(a), the available tensile yielding strength of the plate is determined as follows:

$$A_g = lt$$
$$= (14.5 \text{ in.})(½ \text{ in.})$$
$$= 7.25 \text{ in.}^2$$

$$R_n = F_y A_g$$ (*Spec.* Eq. J4-1)
$$= (50 \text{ ksi})(7.25 \text{ in.}^2)$$
$$= 363 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi R_n = 0.90(363 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{363 \text{ kips}}{1.67}$ |
| $= 327 \text{ kips} > 60 \text{ kips} \quad \textbf{o.k.}$ | $= 217 \text{ kips} > 40 \text{ kips} \quad \textbf{o.k.}$ |

---

# IIA-185

*Flexural Yielding of the Plate*

From AISC *Manual* Part 12, the required flexural strength is calculated using AISC *Specification* Section F11, with $C_b = 1.84$. The required flexural strength is based on the shear strength and the eccentricity previously calculated:

| LRFD | ASD |
|------|-----|
| $M_u = V_u e$ | $M_a = V_a e$ |
| $= (75 \text{ kips})(2½ \text{ in.})$ | $= (50 \text{ kips})(2½ \text{ in.})$ |
| $= 188$ kip-in. | $= 125$ kip-in. |

From AISC *Specification* Section F11.1, the flexural strength of the plate for the limit state of yielding strength is determined as follows:

$$Z_x = \frac{t_p l^2}{4}$$
$$= \frac{(½ \text{ in.})(14.5 \text{ in.})^2}{4}$$
$$= 26.3 \text{ in.}^3$$

$$S_x = \frac{t_p l^2}{6}$$
$$= \frac{(½ \text{ in.})(14.5 \text{ in.})^2}{6}$$
$$= 17.5 \text{ in.}^3$$

$$M_n = F_y Z_x \leq 1.5F_y S_x$$ (from *Spec.* Eq. F11-1)
$$= (50 \text{ ksi})(26.3 \text{ in.}^3) < 1.5(50 \text{ ksi})(17.5 \text{ in.}^3)$$
$$= 1,320 \text{ kip-in.} > 1,310 \text{ kip-in.}$$
$$= 1,310 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi M_n = 0.90(1,310 \text{ kip-in.})$ | $\frac{M_n}{\Omega} = \frac{1,310 \text{ kip-in.}}{1.67}$ |
| $= 1,180 \text{ kip-in.} > 188 \text{ kip-in.} \quad \textbf{o.k.}$ | $= 784 \text{ kip-in.} > 125 \text{ kip-in.} \quad \textbf{o.k.}$ |

From AISC *Specification* Section F11.2, the flexural strength of the plate for the limit state of lateral-torsional buckling is determined as follows:

$$\frac{L_b d}{t^2} = \frac{(2½ \text{ in.})(14.5 \text{ in.})}{(½ \text{ in.})^2}$$
$$= 145$$

$$\frac{0.08E}{F_y} = \frac{0.08(29,000 \text{ ksi})}{50 \text{ ksi}}$$
$$= 46.4$$

---

# IIA-186

$$\frac{1.9E}{F_y} = \frac{1.9(29,000 \text{ ksi})}{50 \text{ ksi}}$$
$$= 1,100$$

Because $\frac{0.08E}{F_y} < \frac{L_b d}{t^2} \leq \frac{1.9E}{F_y}$, AISC *Specification* Section F11.2(b) applies:

$$M_n = F_y Z_x$$
$$= (50 \text{ ksi})(26.3 \text{ in.}^3)$$
$$= 1,320 \text{ kip-in.}$$

$$M_y = F_y S_x$$
$$= (50 \text{ ksi})(17.5 \text{ in.}^3)$$
$$= 875 \text{ kip-in.}$$

$$M_n = C_b\left[1.52 - 0.274\left(\frac{L_b d}{t^2}\right)\frac{F_y}{E}\right]M_y \leq M_p$$ (*Spec.* Eq. F11-3)
$$= (1.84)\left[1.52 - 0.274(145)\left(\frac{50 \text{ ksi}}{29,000 \text{ ksi}}\right)\right](875 \text{ kip-in.}) > 1,320 \text{ kip-in.}$$
$$= 2,340 \text{ kip-in.} > 1,320 \text{ kip-in.}$$
$$= 1,320 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi M_n = 0.90(1,320 \text{ kip-in.})$ | $\frac{M_n}{\Omega} = \frac{1,320 \text{ kip-in.}}{1.67}$ |
| $= 1,190 \text{ kip-in.} > 188 \text{ kip-in.} \quad \textbf{o.k.}$ | $= 790 \text{ kip-in.} > 125 \text{ kip-in.} \quad \textbf{o.k.}$ |

*Interaction of Axial, Flexural, and Shear Yielding in Plate*

The interaction of axial, shear, and flexure in the plate are checked using the method described in AISC *Manual* Part 12. Because the beam is assumed to be braced against rotation about its longitudinal axis, the minor-axis term $M_{ry} / M_{cy} = 0$ in the following equations.

| LRFD | ASD |
|------|-----|
| $\frac{N_u}{\phi R_{np}} = \frac{60 \text{ kips}}{327 \text{ kips}}$ | $\frac{N_a}{R_{np}/\Omega} = \frac{40 \text{ kips}}{217 \text{ kips}}$ |
| $= 0.183$ | $= 0.184$ |

---

# IIA-187

| LRFD | ASD |
|------|-----|
| Because $\frac{N_u}{\phi R_{np}} < 0.2$, use AISC *Manual* Eq. 12-2: | Because $\frac{N_a}{R_{np}/\Omega} < 0.2$, use AISC *Manual* Eq. 12-2: |
| $\left[\frac{N_u}{2\phi R_{np}} + \left(\frac{M_{ux}}{\phi M_{nx}} + \frac{M_{uy}}{\phi M_{ny}}\right)\right]^2 + \left(\frac{V_u}{\phi R_{nv}}\right)^2 \leq 1$ | $\left[\frac{\Omega N_a}{2R_{np}} + \left(\frac{\Omega M_{ax}}{M_{nx}} + \frac{\Omega M_{ay}}{M_{ny}}\right)\right]^2 + \left(\frac{\Omega V_a}{R_{nv}}\right)^2 \leq 1$ |
| $\left[\frac{60 \text{ kips}}{2(327 \text{ kips})} + \left(\frac{188 \text{ kip-in.}}{1,180 \text{ kip-in.}} + 0\right)\right]^2 + \left(\frac{75 \text{ kips}}{218 \text{ kips}}\right)^2 \leq 1$ | $\left[\frac{40 \text{ kips}}{2(217 \text{ kips})} + \left(\frac{125 \text{ kip-in.}}{784 \text{ kip-in.}} + 0\right)\right]^2 + \left(\frac{50 \text{ kips}}{145 \text{ kips}}\right)^2 \leq 1$ |
| $0.181 < 1 \quad \textbf{o.k.}$ | $0.182 < 1 \quad \textbf{o.k.}$ |

*Shear Rupture Strength of the Plate*

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the plate is determined as follows:

$$A_{nv} = \left[l - n\left(d_h + \frac{1}{16} \text{ in.}\right)\right]t$$
$$= \left[14.5 \text{ in.} - 5\left(^{15}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right](½ \text{ in.})$$
$$= 4.75 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(4.75 \text{ in.}^2)$$
$$= 185 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(185 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{185 \text{ kips}}{2.00}$ |
| $= 139 \text{ kips} > 75 \text{ kips} \quad \textbf{o.k.}$ | $= 92.5 \text{ kips} > 50 \text{ kips} \quad \textbf{o.k.}$ |

*Tensile Rupture of the Plate*

From AISC *Specification* Section J4.1(b), the available tensile rupture strength of the plate is determined as follows:

$$A_n = \left[l - n\left(d_h + \frac{1}{16} \text{ in.}\right)\right]t$$
$$= \left[14.5 \text{ in.} - 5\left(^{15}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right](½ \text{ in.})$$
$$= 4.75 \text{ in.}^2$$

Table D3.1, Case 1, applies in this case because the tension load is transmitted directly to the cross-sectional element by fasteners; therefore, $U = 1.0$.

$$A_e = A_nU$$ (*Spec.* Eq. D3-1)
$$= \left(4.75 \text{ in.}^2\right)(1.0)$$
$$= 4.75 \text{ in.}^2$$

$$R_n = F_u A_e$$ (*Spec.* Eq. J4-2)
$$= (65 \text{ ksi})(4.75 \text{ in.}^2)$$
$$= 309 \text{ kips}$$

---

# IIA-188

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(309 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{309 \text{ kips}}{2.00}$ |
| $= 232 \text{ kips} > 60 \text{ kips} \quad \textbf{o.k.}$ | $= 155 \text{ kips} > 40 \text{ kips} \quad \textbf{o.k.}$ |

*Flexural Rupture of the Plate*

The available flexural rupture strength of the plate is determined as follows:

$$Z_{net} = Z_g - \frac{t_p}{4}\left[\left(d_h + \frac{1}{16} \text{ in.}\right)(s)\left(n^2 - 1\right) + \left(d_h + \frac{1}{16} \text{ in.}\right)^2\right]$$
$$= 26.3 \text{ in.}^3 - \frac{½ \text{ in.}}{4}\left[\left(^{15}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)(3.00 \text{ in.})\left(5^2 - 1\right) + \left(^{15}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)^2\right]$$
$$= 17.2 \text{ in.}^3$$

$$M_n = F_u Z_{net}$$ (*Manual* Eq. 9-8)
$$= (65 \text{ ksi})(17.2 \text{ in.}^3)$$
$$= 1,120 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi M_n = 0.75(1,120 \text{ kip-in.})$ | $\frac{M_n}{\Omega} = \frac{1,120 \text{ kip-in.}}{2.00}$ |
| $= 840 \text{ kip-in.} > 188 \text{ kip-in.} \textbf{ o.k.}$ | $= 560 \text{ kip-in.} > 125 \text{ kip-in.} \textbf{ o.k.}$ |

*Interaction of Axial, Flexure, and Shear Rupture in Plate*

The interaction of axial, shear, and flexure in the plate are checked using the method described in AISC *Manual* Part 12. Because the beam is assumed to be braced against rotation about its longitudinal axis, the minor-axis term $M_{ry} / M_{cy} = 0$ in the following equations.

| LRFD | ASD |
|------|-----|
| $\frac{N_u}{\phi R_{np}} = \frac{60 \text{ kips}}{232 \text{ kips}}$ | $\frac{N_a}{R_{np}/\Omega} = \frac{40 \text{ kips}}{155 \text{ kips}}$ |
| $= 0.259$ | $= 0.258$ |
|  |  |
| Because $\frac{N_u}{\phi R_{np}} > 0.2$, use AISC *Manual* Eq. 12-3: | Because $\frac{N_a}{R_{np}/\Omega} > 0.2$, use AISC *Manual* Eq. 12-3: |
| $\left[\frac{N_u}{\phi R_{np}} + \frac{8}{9}\left(\frac{M_{ux}}{\phi M_{nx}} + \frac{M_{uy}}{\phi M_{ny}}\right)\right]^2 + \left(\frac{V_u}{\phi R_{nv}}\right)^2 \leq 1$ | $\left[\frac{\Omega N_a}{R_{np}} + \frac{8}{9}\left(\frac{\Omega M_{ax}}{M_{nx}} + \frac{\Omega M_{ay}}{M_{ny}}\right)\right]^2 + \left(\frac{\Omega V_a}{R_{nv}}\right)^2 \leq 1$ |
| $\left[\frac{60 \text{ kips}}{232 \text{ kips}} + \frac{8}{9}\left(\frac{188 \text{ kip-in.}}{840 \text{ kip-in.}} + 0\right)\right]^2 + \left(\frac{75 \text{ kips}}{139 \text{ kips}}\right)^2 \leq 1$ | $\left[\frac{40 \text{ kips}}{155 \text{ kips}} + \frac{8}{9}\left(\frac{125 \text{ kip-in.}}{560 \text{ kip-in.}} + 0\right)\right]^2 + \left(\frac{50 \text{ kips}}{92.5 \text{ kips}}\right)^2 \leq 1$ |
| $0.500 < 1 \quad \textbf{o.k.}$ | $0.501 < 1 \quad \textbf{o.k.}$ |

---

# IIA-189

*Block Shear Rupture Strength of the Plate—Beam Shear Direction*

The nominal strength for the limit state of block shear rupture of the plate, assuming an L-shaped tearout due the shear load only, is determined as follows:

$$R_n = 0.60F_u A_{nv} + U_{bs} F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs} F_u A_{nt}$$ (*Spec.* Eq. J4-5)

where

$$A_{gv} = (l - l_{ev})t$$
$$= \left[14.5 \text{ in.} - 1¼ \text{ in.}\right](½ \text{ in.})$$
$$= 6.63 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (n - 0.5)(d_h + \frac{1}{16} \text{ in.})t$$
$$= 6.63 \text{ in.}^2 - (5 - 0.5)\left(^{15}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)(½ \text{ in.})$$
$$= 4.38 \text{ in.}^2$$

$$A_{nt} = \left[l_{eh} - 0.5\left(d_h + \frac{1}{16} \text{ in.}\right)\right]t$$
$$= \left[2½ \text{ in.} - 0.5\left(^{15}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right](½ \text{ in.})$$
$$= 1.00 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_n = 0.60(65 \text{ ksi})(4.38 \text{ in.}^2) + 1.0(65 \text{ ksi})(1.00 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(6.63 \text{ in.}^2) + 1.0(65 \text{ ksi})(1.00 \text{ in.}^2)$$
$$= 236 \text{ kips} < 264 \text{ kips}$$

Therefore:
$$R_n = 236 \text{ kips}$$

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture of the plate is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(236 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{236 \text{ kips}}{2.00}$ |
| $= 177 \text{ kips} > 75 \text{ kips} \quad \textbf{o.k.}$ | $= 118 \text{ kips} > 50 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture Strength of the Plate—Beam Axial Direction*

The plate block shear rupture failure path due to axial load only could occur as an L- or U-shape. Assuming an L-shaped failure path due to axial load only, the available block shear rupture strength of the plate is:

$$R_n = 0.60F_u A_{nv} + U_{bs} F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs} F_u A_{nt}$$ (*Spec.* Eq. J4-5)

where

$$A_{gv} = l_{eh}t$$
$$= (2½ \text{ in.})(½ \text{ in.})$$
$$= 1.25 \text{ in.}^2$$

---

# IIA-190

$$A_{nv} = A_{gv} - 0.5\left(d_h + \frac{1}{16} \text{ in.}\right)t$$
$$= 1.25 \text{ in.}^2 - 0.5\left(^{15}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)(½ \text{ in.})$$
$$= 1.00 \text{ in.}^2$$

$$A_{nt} = \left[l - l_{ev} - (n - 0.5)\left(d_h + \frac{1}{16} \text{ in.}\right)\right]t$$
$$= \left[14.5 \text{ in.} - 1¼ \text{ in.} - (5 - 0.5)\left(^{15}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right](½ \text{ in.})$$
$$= 4.38 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_n = 0.60(65 \text{ ksi})(1.00 \text{ in.}^2) + 1.0(65 \text{ ksi})(4.38 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(1.25 \text{ in.}^2) + 1.0(65 \text{ ksi})(4.38 \text{ in.}^2)$$
$$= 324 \text{ kips} > 322 \text{ kips}$$

Therefore:
$$R_n = 322 \text{ kips}$$

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture of the plate is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(322 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{322 \text{ kips}}{2.00}$ |
| $= 242 \text{ kips} > 60 \text{ kips} \quad \textbf{o.k.}$ | $= 161 \text{ kips} > 40 \text{ kips} \quad \textbf{o.k.}$ |

Assuming a U-shaped failure path in the plate due to axial load, the available block shear rupture strength of the plate is:

$$R_n = 0.60F_u A_{nv} + U_{bs} F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs} F_u A_{nt}$$ (*Spec.* Eq. J4-5)

where

$$A_{gv} = (2 \text{ shear planes})l_{eh}t$$
$$= (2 \text{ shear planes})(2½ \text{ in.})(½ \text{ in.})$$
$$= 2.50 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (2 \text{ shear planes})(0.5)\left(d_h + \frac{1}{16} \text{ in.}\right)t$$
$$= 2.50 \text{ in.}^2 - (2 \text{ shear planes})(0.5)\left(^{15}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)(½ \text{ in.})$$
$$= 2.00 \text{ in.}^2$$

$$A_{nt} = \left[l - 2l_{ev} - (n - 1)\left(d_h + \frac{1}{16} \text{ in.}\right)\right]t$$
$$= \left[14.5 \text{ in.} - 2(1¼ \text{ in.}) - (5 - 1)\left(^{15}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right](½ \text{ in.})$$
$$= 4.00 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

---

# IIA-191

$$R_n = 0.60(65 \text{ ksi})(2.00 \text{ in.}^2) + 1.0(65 \text{ ksi})(4.00 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(2.50 \text{ in.}^2) + 1.0(65 \text{ ksi})(4.00 \text{ in.}^2)$$
$$= 338 \text{ kips} > 335 \text{ kips}$$

Therefore:
$$R_n = 335 \text{ kips}$$

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture of the plate is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(335 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{335 \text{ kips}}{2.00}$ |
| $= 251 \text{ kips} > 60 \text{ kips} \quad \textbf{o.k.}$ | $= 168 \text{ kips} > 40 \text{ kips} \quad \textbf{o.k.}$ |

The L-shaped failure path controls in the shear plate.

Check shear and tension interaction for plate block shear on the L-shaped failure plane using AISC *Manual* Eq. 12-1:

| LRFD | ASD |
|------|-----|
| $\left(\frac{V_u}{\phi R_{bv}}\right)^2 + \left(\frac{N_u}{\phi R_{nt}}\right)^2 \leq 1$ | $\left(\frac{V_a}{R_{bv}/\Omega}\right)^2 + \left(\frac{N_a}{R_{nt}/\Omega}\right)^2 \leq 1$ |
| $\left(\frac{75 \text{ kips}}{177 \text{ kips}}\right)^2 + \left(\frac{60 \text{ kips}}{242 \text{ kips}}\right)^2 = 0.241 < 1 \quad \textbf{o.k.}$ | $\left(\frac{50 \text{ kips}}{118 \text{ kips}}\right)^2 + \left(\frac{40 \text{ kips}}{161 \text{ kips}}\right)^2 = 0.241 < 1 \quad \textbf{o.k.}$ |

*Shear Strength of the Beam Web*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the beam web is determined as follows:

$$A_{gv} = dt_w$$
$$= (18.0 \text{ in.})(0.355 \text{ in.})$$
$$= 6.39 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(6.39 \text{ in.}^2)$$
$$= 192 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(192 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{192 \text{ kips}}{1.50}$ |
| $= 192 \text{ kips} > 75 \text{ kips} \quad \textbf{o.k.}$ | $= 128 \text{ kips} > 50 \text{ kips} \quad \textbf{o.k.}$ |

The limit state of shear rupture of the beam web will not control in this example because the beam is uncoped.

*Tensile Strength of the Beam*

---

# IIA-192

From AISC *Specification* Section J4.1(a), the available tensile yielding strength of the beam is determined as follows:

$$R_n = F_y A_g$$ (*Spec.* Eq. J4-1)
$$= (50 \text{ ksi})(14.7 \text{ in.}^2)$$
$$= 735 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi R_n = 0.90(735 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{735 \text{ kips}}{1.67}$ |
| $= 662 \text{ kips} > 60 \text{ kips} \quad \textbf{o.k.}$ | $= 440 \text{ kips} > 40 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.1, the available tensile rupture strength of the beam is determined from AISC *Specification* Equation J4-2. No cases in AISC *Specification* Table D3.1 apply to this configuration; therefore, $U$ is determined in accordance with AISC *Specification* Section D3, where the minimum value of $U$ is the ratio of the gross area of the connected element to the member gross area.

$$U = \frac{(d - 2t_f)t_w}{A_g}$$
$$= \frac{\left[18.0 \text{ in.} - 2(0.570 \text{ in.})\right](0.355 \text{ in.})}{14.7 \text{ in.}^2}$$
$$= 0.407$$

$$A_n = A_g - n(d_h + \frac{1}{16} \text{ in.})t_w$$
$$= 14.7 \text{ in.}^2 - 5\left(^{15}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)(0.355 \text{ in.})$$
$$= 12.9 \text{ in.}^2$$

$$A_e = A_nU$$ (*Spec.* Eq. D3-1)
$$= (12.9 \text{ in.}^2)(0.407)$$
$$= 5.25 \text{ in.}^2$$

$$R_n = F_u A_e$$ (*Spec.* Eq. J4-2)
$$= (65 \text{ ksi})(5.25 \text{ in.}^2)$$
$$= 341 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(341 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{341 \text{ kips}}{2.00}$ |
| $= 256 \text{ kips} > 60 \text{ kips} \quad \textbf{o.k.}$ | $= 171 \text{ kips} > 40 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture of the Beam Web*

Block shear rupture is only applicable in the direction of the axial load because the beam is uncoped and the limit state is not applicable for an uncoped beam subject to vertical shear. Assuming a U-shaped tearout relative to the axial load,

---

# IIA-193

and assuming a horizontal edge distance of $l_{eh} = 1¾$ in. $- ¼$ in. $= 1½$ in. to account for a possible beam underrun of ¼ in., the block shear rupture strength is:

$$R_n = 0.60F_u A_{nv} + U_{bs} F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs} F_u A_{nt}$$ (*Spec.* Eq. J4-5)

where

$$A_{gv} = (2 \text{ shear planes})l_{eh}t_w$$
$$= (2 \text{ shear planes})(1½ \text{ in.})(0.355 \text{ in.})$$
$$= 1.07 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (2 \text{ shear planes})(0.5)(d_h + \frac{1}{16} \text{ in.})t_w$$
$$= 1.07 \text{ in.}^2 - (2 \text{ shear planes})(0.5)\left(^{15}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)(0.355 \text{ in.})$$
$$= 0.715 \text{ in.}^2$$

$$A_{nt} = \left[12.0 \text{ in.} - (n - 1)(d_h + \frac{1}{16} \text{ in.})\right]t_w$$
$$= \left[12.0 \text{ in.} - (5 - 1)\left(^{15}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right](0.355 \text{ in.})$$
$$= 2.84 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_n = 0.60(65 \text{ ksi})(0.715 \text{ in.}^2) + 1.0(65 \text{ ksi})(2.84 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(1.07 \text{ in.}^2) + 1.0(65 \text{ ksi})(2.84 \text{ in.}^2)$$
$$= 212 \text{ kips} < 217 \text{ kips}$$

Therefore:
$$R_n = 212 \text{ kips}$$

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture of the beam web is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 0.75(212 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{212 \text{ kips}}{2.00}$ |
| $= 159 \text{ kips} > 60 \text{ kips} \quad \textbf{o.k.}$ | $= 106 \text{ kips} > 40 \text{ kips} \quad \textbf{o.k.}$ |

*Conclusion*

The connection is found to be adequate as given for the applied loads. Note that because the supported member was assumed to be continuously laterally braced, it is not necessary to check weak-axis moment.

---

# IIA-194

# EXAMPLE II.A-17C SINGLE-PLATE CONNECTION—STRUCTURAL INTEGRITY CHECK

## Given:

Verify the single plate connection from Example II.A-17A, as shown in Figure II.A-17C-1, for the structural integrity provisions of AISC *Specification* Section B3.9. The connection is verified as a beam and girder end connection and as an end connection of a member bracing a column. Note that these checks are necessary when design for structural integrity is required by the applicable building code.

Use 70-ksi electrodes and an ASTM A572/A572M Grade 50 plate.

<div style="text-align: center;">
<img src="connection_diagram" alt="Connection diagram showing:
- W14×90 column
- W16×50 beam
- PL¼×4½×0'-11½" single plate
- a = 3" dimension
- 1½" edge distance
- 3 @ 3" = 9" vertical spacing
- 1⅛" and 1⅛" horizontal dimensions
- ¾" dia. Group 120 bolts, thread condition N, std. holes
- ⅜ and ⅜ fillet welds">
</div>

*Fig. II.A-17C-1. Connection geometry for Example II.A-17C.*

## Solution:

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Beam
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Plate
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W16×50
$t_w = 0.380$ in.

---

# IIA-195

From AISC *Specification* Table J3.3, the hole diameter for ¾-in.-diameter bolts with standard holes is:

$$d_h = ^{13}/{16} \text{ in.}$$

*Beam and Girder End Connection*

From Example II.A-17A, the required shear strength is:

| LRFD | ASD |
|------|-----|
| $V_u = 49.6$ kips | $V_a = 33.0$ kips |

From AISC *Specification* Section B3.9(b), the minimum nominal axial tensile strength is:

| LRFD | ASD |
|------|-----|
| $T = \frac{2}{3}V_u \geq 10$ kips | $T = V_a \geq 10$ kips |
| $= \frac{2}{3}(49.6 \text{ kips}) > 10$ kips | $= 33.0 \text{ kips} > 10$ kips |
| $= 33.1 \text{ kips} > 10$ kips | $= 33.0$ kips |
| $= 33.1$ kips |  |

*Bolt Shear*

From AISC *Specification* Section J3.7, the nominal bolt shear strength is:

$F_{nv} = 54$ ksi, from AISC *Specification* Table J3.2

$$T_n = nF_{nv}A_b$$ (from *Spec.* Eq. J3-1)
$$= (4 \text{ bolts})(54 \text{ ksi})(0.442 \text{ in.}^2)$$
$$= 95.5 \text{ kips}$$

*Bolt Bearing and Tearout*

From AISC *Specification* Section B3.9, for the purpose of satisfying structural integrity requirements, inelastic deformations of the connection are permitted; therefore, AISC *Specification* Equations J3-6b and J3-6d are used to determine the nominal bearing and tearout strength. By inspection, bolt bearing and tearout will control for the plate.

For bolt bearing on the plate:

$$T_n = n(3.0dtF_u)$$ (from *Spec.* Eq. J3-6b)
$$= (4 \text{ bolts})(3.0)(¾ \text{ in.})(¼ \text{ in.})(65 \text{ ksi})$$
$$= 146 \text{ kips}$$

For bolt tearout on the plate:

$$l_c = l_{eh} - 0.5d_h$$
$$= 1½ \text{ in.} - 0.5\left(^{13}/{16} \text{ in.}\right)$$
$$= 1.09 \text{ in.}$$

---

# IIA-196

$$T_n = n(1.5l_ctF_u)$$ (from *Spec.* Eq. J3-6d)
$$= (4 \text{ bolts})(1.5)(1.09 \text{ in.})(¼ \text{ in.})(65 \text{ ksi})$$
$$= 106 \text{ kips}$$

*Tensile Yielding of Plate*

From AISC *Specification* Section J4.1, the nominal tensile yielding strength of the shear plate is determined as follows:

$$A_g = lt$$
$$= (11.5 \text{ in.})(¼ \text{ in.})$$
$$= 2.88 \text{ in.}^2$$

$$T_n = F_y A_g$$ (from *Spec.* Eq. J4-1)
$$= (50 \text{ ksi})(2.88 \text{ in.}^2)$$
$$= 144 \text{ kips}$$

*Tensile Rupture of Plate*

From AISC *Specification* Section J4.1, the nominal tensile rupture strength of the shear plate is determined as follows:

$$A_n = \left[l - n(d_h + \frac{1}{16} \text{ in.})\right]t$$
$$= \left[11.5 \text{ in.} - (4 \text{ bolts})\left(^{13}/{16} \text{ in.} + \frac{1}{16}\text{in.}\right)\right](¼ \text{ in.})$$
$$= 2.00 \text{ in.}^2$$

AISC *Specification* Table D3.1, Case 1, applies in this case because tensile load is transmitted directly to the cross-section element by fasteners; therefore, $U = 1.0$.

$$A_e = A_nU$$ (*Spec.* Eq. D3-1)
$$= (2.00 \text{ in.}^2)(1.0)$$
$$= 2.00 \text{ in.}^2$$

$$T_n = F_u A_e$$ (from *Spec.* Eq. J4-2)
$$= (65 \text{ ksi})(2.00 \text{ in.}^2)$$
$$= 130 \text{ kips}$$

*Block Shear Rupture—Plate*

The nominal block shear rupture strength, due to axial load, of the plate is determined using AISC *Specification* Section J4.3.

$$T_n = 0.60F_u A_{nv} + U_{bs} F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs} F_u A_{nt}$$ (from *Spec.* Eq. J4-5)

The nominal block shear rupture strength of the plate for a U-shaped failure plane is:

---

# IIA-197

$$A_{gv} = (2 \text{ shear planes})l_{eh}t$$
$$= (2 \text{ shear planes})(1½ \text{ in.})(¼ \text{ in.})$$
$$= 0.750 \text{ in.}^2$$

$$A_{nv} = (2 \text{ shear planes})\left[l_{eh} - 0.5(d_h + \frac{1}{16} \text{ in.})\right]t$$
$$= (2 \text{ shear planes})\left[1½ \text{ in.} - 0.5\left(^{13}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right](¼ \text{ in.})$$
$$= 0.531 \text{ in.}^2$$

$$A_{nt} = \left[l - 2l_{ev} - (n - 1)(d_h + \frac{1}{16} \text{ in.})\right]t$$
$$= \left[11.5 \text{ in.} - 2(1¼ \text{ in.}) - (4 - 1)\left(^{13}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right](¼ \text{ in.})$$
$$= 1.59 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$T_n = 0.60(65 \text{ ksi})(0.531 \text{ in.}^2) + 1.0(65 \text{ ksi})(1.59 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(0.750 \text{ in.}^2) + 1.0(65 \text{ ksi})(1.59 \text{ in.}^2)$$
$$= 124 \text{ kips} < 126 \text{ kips}$$
$$= 124 \text{ kips}$$

The nominal block shear rupture strength of the plate for an L-shaped failure plane is:

$$A_{gv} = l_{eh}t$$
$$= (1½ \text{ in.})(¼ \text{ in.})$$
$$= 0.375 \text{ in.}^2$$

$$A_{nv} = \left[l_{eh} - 0.5(d_h + \frac{1}{16} \text{ in.})\right]t$$
$$= \left[1½ \text{ in.} - 0.5\left(^{13}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right](¼ \text{ in.})$$
$$= 0.266 \text{ in.}^2$$

$$A_{nt} = \left[l - l_{ev} - (n - 0.5)(d_h + \frac{1}{16} \text{ in.})\right]t$$
$$= \left[11.5 \text{ in.} - 1¼ \text{ in.} - (4 - 0.5)\left(^{13}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right](¼ \text{ in.})$$
$$= 1.80 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$T_n = 0.60(65 \text{ ksi})(0.266 \text{ in.}^2) + 1.0(65 \text{ ksi})(1.80 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(0.375 \text{ in.}^2) + 1.0(65 \text{ ksi})(1.80 \text{ in.}^2)$$
$$= 127 \text{ kips} < 128 \text{ kips}$$
$$= 127 \text{ kips}$$

*Block Shear Rupture—Beam Web*

---

# IIA-198

From AISC *Specification* Section J4.3, the nominal block shear rupture strength, due to axial load, of the beam web is determined as follows (accounting for a possible ¼ in. beam underrun):

$$T_n = 0.60F_u A_{nv} + U_{bs} F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs} F_u A_{nt}$$ (from *Spec.* Eq. J4-5)

where

$$A_{gv} = (2 \text{ shear planes})(l_{eh} - underrun)t_w$$
$$= (2 \text{ shear planes})(2½ \text{ in.} - ¼ \text{ in.})(0.380 \text{ in.})$$
$$= 1.71 \text{ in.}^2$$

$$A_{nv} = (2 \text{ shear planes})\left[l_{eh} - underrun - 0.5(d_h + \frac{1}{16} \text{ in.})\right]t_w$$
$$= (2 \text{ shear planes})\left[2½ \text{ in.} - ¼ \text{ in.} - 0.5\left(^{13}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right](0.380 \text{ in.})$$
$$= 1.38 \text{ in.}^2$$

$$A_{nt} = \left[9.00 \text{ in.} - 3\left(^{13}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right](0.380 \text{ in.})$$
$$= 2.42 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$T_n = 0.60(65 \text{ ksi})(1.38 \text{ in.}^2) + 1.0(65 \text{ ksi})(2.42 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(1.71 \text{ in.}^2) + 1.0(65 \text{ ksi})(2.42 \text{ in.}^2)$$
$$= 211 \text{ kips} > 209 \text{ kips}$$
$$= 209 \text{ kips}$$

*Weld Strength*

From AISC *Specification* Section J2.4, the nominal tensile strength of the weld is determined as follows:

$$F_{nw} = 0.60F_{EXX}\left(1.0 + 0.50\sin^{1.5}\theta\right)$$
$$= 0.60(70 \text{ ksi})\left(1.0 + 0.50\sin^{1.5}90°\right)$$
$$= 63.0 \text{ ksi}$$

The throat dimension is used to calculate the effective area of the fillet weld.

$$A_{we} = \frac{w}{\sqrt{2}}l(2 \text{ welds})$$
$$= \frac{⅜ \text{ in.}}{\sqrt{2}}(11.5 \text{ in.})(2 \text{ welds})$$
$$= 3.05 \text{ in.}^2$$

$$T_n = F_{nw}A_{we}$$ (from *Spec.* Eq. J2-4)
$$= (63.0 \text{ ksi})(3.05 \text{ in.}^2)$$
$$= 192 \text{ kips}$$

*Nominal Tensile Strength*

---

# IIA-199

The controlling tensile strength, $T_n$, is the least of those previously calculated:

$$T_n = \min\{95.5 \text{ kips}, \, 146 \text{ kips}, \, 106 \text{ kips}, \, 144 \text{ kips}, \, 130 \text{ kips}, \, 124 \text{ kips}, \, 127 \text{ kips}, \, 209 \text{ kips}, \, 192 \text{ kips}\}$$
$$= 95.5 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $T_n = 95.5 \text{ kips} > 33.1 \text{ kips} \quad \textbf{o.k.}$ | $T_n = 95.5 \text{ kips} > 33.0 \text{ kips} \quad \textbf{o.k.}$ |

*Column Bracing*

From AISC *Specification* Section B3.9(c), the minimum nominal axial tension strength for the connection of a member bracing a column is equal to 1% of two-thirds of the required column axial strength for LRFD and equal to 1% of the required column axial strength for ASD. These requirements are evaluated independently from other strength requirements.

The maximum column axial force this connection is able to brace is determined as follows:

| LRFD | ASD |
|------|-----|
| $T_n \geq 0.01\left(\frac{2}{3}P_u\right)$ | $T_n \geq 0.01P_a$ |
|  |  |
| Solving for the column axial force: | Solving for the column axial force: |
|  |  |
| $P_u \leq 100\left(\frac{3}{2}T_n\right)$ | $P_a \leq 100T_n$ |
| $= 100\left(\frac{3}{2}\right)(95.5 \text{ kips})$ | $= 100(95.5 \text{ kips})$ |
| $= 14,300$ kips | $= 9,550$ kips |

As long as the required column axial strength is less than $P_u = 14,300$ kips or $P_a = 9,550$ kips, this connection is an adequate column brace.

---

# IIA-200

# EXAMPLE II.A-18 SINGLE-PLATE CONNECTION (BEAM-TO-GIRDER WEB)

## Given:

Verify a single-plate connection between an ASTM A992/A992M W18×35 beam and an ASTM A992/A992M W21×62 girder web, as shown in Figure II.A-18-1, to support the following beam end reactions:

$R_D = 6.5$ kips
$R_L = 20$ kips

The top flange is coped 2 in. deep by 4 in. long, $l_{ev} = 1½$ in. Use 70-ksi electrodes and an ASTM A572/A572M Grade 50 plate.

<div style="text-align: center;">
<img src="connection_diagram" alt="Connection diagram showing:
- W21×62 girder web
- W18×35 beam with coped top flange
- PL¼×4½×0'-11½" single plate
- c = 4" cope length
- 2" cope depth
- $l_{ev} = 1½$ in. vertical edge distance
- 3 @ 3" = 9" vertical bolt spacing
- a = 3" dimension
- 1½" and 1¼" horizontal dimensions
- ¾" dia. Group 120 bolts, thread condition N, std. holes
- ⅜ and ⅜ fillet welds">
</div>

*Fig. II.A-18-1. Connection geometry for Example II.A-18.*

## Solution:

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Beam and girder
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Plate
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

---

# IIA-201

Beam
W18×35
$d = 17.7$ in.
$t_w = 0.300$ in.
$t_f = 0.425$ in.

Girder
W21×62
$t_w = 0.400$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(6.5 \text{ kips}) + 1.6(20 \text{ kips})$ | $R_a = 6.5 \text{ kips} + 20 \text{ kips}$ |
| $= 39.8$ kips | $= 26.5$ kips |

*Single Plate Available Strength*

AISC *Manual* Table 10-10a includes checks for the limit states of shear rupture of the plate, block shear rupture of the plate, and weld shear.

Check four rows of ¾-in-diameter bolts in standard holes, ¼ in. plate thickness, and ⅜ in. fillet weld size. From AISC *Manual* Table 10-10a, the weld and single-plate available strength is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 58.5 \text{ kips} > 39.8 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 39.0 \text{ kips} > 26.5 \text{ kips} \quad \textbf{o.k.}$ |

*Available Shear Transfer Strength at Bolt Holes*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength determined in accordance with AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the plate at the bolt hole determined in accordance with AISC *Specification* Section J3.11a, and (3) the available bearing or tearout strength of the beam web at the bolt hole determined in accordance with AISC *Specification* Section J3.11a.

From AISC *Manual* Table 10-10b, the available bolt shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) in single shear is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9$ kips | $\frac{r_n}{\Omega} = 11.9$ kips |

From AISC *Manual* Table 10-10b, the available bearing and tearout strength of the plate per bolt for ¾-in.-diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the edge bolt ($l_{ev} = 1¼$ in.): | For the edge bolt ($l_{ev} = 1¼$ in.): |
| $\phi r_n = (49.4 \text{ kips/in.})(¼ \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kips/in.})(¼ \text{ in.})$ |
| $= 12.4$ kips | $= 8.23$ kips |

---

# IIA-202

| LRFD | ASD |
|------|-----|
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kips/in.})(¼ \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(¼ \text{ in.})$ |
| $= 22.0$ kips | $= 14.6$ kips |

From AISC *Manual* Table 10-10b, the available bearing and tearout strength of the beam web per bolt for ¾-in.- diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the edge bolt ($l_{ev} = 1½$ in.): | For the edge bolt ($l_{ev} = 1½$ in.): |
| $\phi r_n = (64.0 \text{ kips/in.})(0.300 \text{ in.})$ | $\frac{r_n}{\Omega} = (42.7 \text{ kips/in.})(0.300 \text{ in.})$ |
| $= 19.2$ kips | $= 12.8$ kips |
|  |  |
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kips/in.})(0.300 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(0.300 \text{ in.})$ |
| $= 26.3$ kips | $= 17.6$ kips |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the plate for a non-edge bolt, and the available bearing and tearout strength of the beam web for an edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min \begin{cases} 17.9 \text{ kips,} \\ 22.0 \text{ kips,} \\ 19.2 \text{ kips} \end{cases}$ | $\frac{r_{n,top}}{\Omega} = \min \begin{cases} 11.9 \text{ kips,} \\ 14.6 \text{ kips,} \\ 12.8 \text{ kips} \end{cases}$ |
| $= 17.9$ kips | $= 11.9$ kips |

At the middle connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the plate for a non-edge bolt, and the available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,mid} = \min \begin{cases} 17.9 \text{ kips,} \\ 22.0 \text{ kips,} \\ 26.3 \text{ kips} \end{cases}$ | $\frac{r_{n,mid}}{\Omega} = \min \begin{cases} 11.9 \text{ kips,} \\ 14.6 \text{ kips,} \\ 17.6 \text{ kips} \end{cases}$ |
| $= 17.9$ kips | $= 11.9$ kips |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the plate for an edge bolt, and the available bearing and tearout strength of the beam web for a non-edge bolt:

---

# IIA-203

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min \begin{cases} 17.9 \text{ kips,} \\ 12.4 \text{ kips,} \\ 26.3 \text{ kips} \end{cases}$ | $\frac{r_{n,bot}}{\Omega} = \min \begin{cases} 11.9 \text{ kips,} \\ 8.23 \text{ kips,} \\ 17.6 \text{ kips} \end{cases}$ |
| $= 12.4$ kips | $= 8.23$ kips |

To account for eccentricity, the available shear transfer strength is multiplied by the factor $C/n$. From AISC *Manual* Table 10-10b, for 4 bolts in standard holes:

$$C/n = 0.885$$

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = (C/n)\left[\phi r_{n,top} + \phi r_{n,mid} (n-2) + \phi r_{n,bot}\right]$ | $\frac{R_n}{\Omega} = (C/n)\left[\frac{r_{n,top}}{\Omega} + \frac{r_{n,mid}}{\Omega} (n-2) + \frac{r_{n,bot}}{\Omega}\right]$ |
| $= (0.885)\left[17.9 \text{ kips} + 17.9 \text{ kips}(4-2) + 12.4 \text{ kips}\right]$ | $= (0.885)\left[11.9 \text{ kips} + 11.9 \text{ kips}(4-2) + 8.23 \text{ kips}\right]$ |
| $= 58.5 \text{ kips} > 39.8 \text{ kips} \quad \textbf{o.k.}$ | $= 38.9 \text{ kips} > 26.5 \text{ kips} \quad \textbf{o.k.}$ |

*Coped Beam Strength*

From AISC *Manual* Part 9, the available coped beam web strength for top cope only is the lesser of the limit states of flexural local web buckling and block shear rupture.

*Beam Web Available Shear Strength*

AISC *Manual* Table 10-10c includes checks for the limit state of block shear rupture of the beam web.

From AISC *Manual* Table 10-10c, with ¾-in.-diameter bolts in standard holes:

| LRFD | ASD |
|------|-----|
| For the top edge hole ($l_{ev,t} = 1½$ in.): | For the top edge hole ($l_{ev,t} = 1½$ in.): |
| $\phi r_n = 31.1$ kips/in. | $\frac{r_n}{\Omega} = 20.7$ kips/in. |
|  |  |
| For the center holes ($s = 3$ in.): | For the center holes ($s = 3$ in.): |
| $\phi r_n = 62.2$ kips/in. | $\frac{r_n}{\Omega} = 41.4$ kips/in. |
|  |  |
| For the bottom edge hole (conservatively assuming $l_{eh} =$ 2¼ in.): | For the bottom edge hole (conservatively assuming $l_{eh} =$ 2¼ in.): |
| $\phi r_n = 76.2$ kips/in. | $\frac{r_n}{\Omega} = 50.8$ kips/in. |

---

# IIA-204

| LRFD | ASD |
|------|-----|
| $\phi R_n = \left[31.1 \text{ kips/in.} + (4-1)(62.2 \text{ kips/in.})\right]$ | $\frac{R_n}{\Omega} = \left[20.7 \text{ kips/in.} + (4-1)(41.4 \text{ kips/in.})\right]$ |
| $+76.2 \text{ kips/in.}$ | $+50.8 \text{ kips/in.}$ |
| $\times(0.300 \text{ in.})$ | $\times(0.300 \text{ in.})$ |
| $= 88.2 \text{ kips} > 39.8 \text{ kips} \quad \textbf{o.k.}$ | $= 58.7 \text{ kips} > 26.5 \text{ kips} \quad \textbf{o.k.}$ |

*Flexural local web buckling of beam web*

For coped beam sections, the limit states of flexural yielding and local buckling should be checked independently per AISC *Manual* Part 9. However, for the shallow cope in this example, these limit states do not govern. For an illustration of these checks, see Example II.A-4.

*Shear Rupture of the Girder Web at the Weld*

The minimum support thickness to match the shear rupture strength of the weld is determined as follows:

$$t_{min} = \frac{3.09D}{F_u}$$ (*Manual* Eq. 9-6)
$$= \frac{3.09(3 \text{ sixteenths})}{65 \text{ ksi}}$$
$$= 0.143 \text{ in.} < 0.400 \text{ in.} \quad \textbf{o.k.}$$

*Conclusion*

The connection is found to be adequate as given for the applied loads.

---

# IIA-205

# EXAMPLE II.A-19A EXTENDED SINGLE-PLATE CONNECTION (BEAM-TO-COLUMN WEB)

## Given:

Verify the connection between an ASTM A992/A992M W16×36 beam and the web of an ASTM A992/A992M W14×90 column, as shown in Figure II.A-19A-1, to support the following beam end reactions:

$R_D = 6$ kips
$R_L = 18$ kips

Use 70-ksi electrodes and ASTM A572/A572M Grade 50 plate. Assume the beam is braced against rotation about its longitudinal axis.

<div style="text-align: center;">
<img src="connection_diagram" alt="Connection diagram showing:
- W14×90 column web
- W16×36 beam
- PL½×12×1'-1¼" extended single plate
- a = 9" dimension
- 3" and $l_{eh} = 1¼$ edge distances
- 1½" and ½" horizontal dimensions
- 3 @ 3" = 9" vertical bolt spacing
- ¾" dia. Group 120 bolts, thread condition N, std. holes
- ⅝ and ⅝ fillet welds
- 1⅛" dimension">
</div>

*Fig. II.A-19A-1. Connection geometry for Example II.A-19A.*

Note: All dimensional limitations are satisfied.

## Solution:

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Beam and column
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Plate
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

---

# IIA-206

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W16×36
$d = 15.9$ in.
$t_w = 0.295$ in.

Column
W14×90
$t_w = 0.440$ in.
$b_f = 14.5$ in.

From AISC *Specification* Table J3.3, the hole diameter for a ¾-in.-diameter bolt with standard holes is:

$$d_h = ^{13}/{16} \text{ in.}$$

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(6 \text{ kips}) + 1.6(18 \text{ kips})$ | $R_a = 6 \text{ kips} + 18 \text{ kips}$ |
| $= 36.0$ kips | $= 24.0$ kips |

*Strength of the Bolted Connection—Beam Web*

From AISC *Manual* Part 10, determine the distance from the support to the first line of bolts and the distance to the center of gravity of the bolt group.

$$e = 9 \text{ in.} + \frac{3 \text{ in.}}{2}$$
$$= 10.5 \text{ in.}$$

From AISC *Manual* Table 7-1, the available shear strength per bolt for ¾-in-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9$ kips | $\frac{r_n}{\Omega} = 11.9$ kips |

Tearout for the bolts in the beam web does not control due to the presence of the beam top flange.

The available bearing strength of the beam web per bolt is determined using AISC *Manual* Table 7-4 with $s = 3$ in.

| LRFD | ASD |
|------|-----|
| $\phi r_n = (87.8 \text{ kip/in.})(0.295 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(0.295 \text{ in.})$ |
| $= 25.9$ kips | $= 17.3$ kips |

Therefore, bolt shear controls over bearing.

The strength of the bolt group is determined by interpolating AISC *Manual* Table 7-7, with $e = 10.5$ in. and Angle = 0°:

---

# IIA-207

$$C = 2.33$$

| LRFD | ASD |
|------|-----|
| $\phi R_n = C\phi r_n$ | $\frac{R_n}{\Omega} = \frac{Cr_n}{\Omega}$ |
| $= 2.33(17.9 \text{ kips})$ | $= 2.33(11.9 \text{ kips})$ |
| $= 41.7 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ | $= 27.7 \text{ kips} > 24.0 \text{ kips} \quad \textbf{o.k.}$ |

*Maximum Plate Thickness*

From AISC *Manual* Part 10, determine the maximum plate thickness, $t_{max}$, that will result in the plate yielding before the bolts shear.

$F_{nv} = 54$ ksi from AISC *Specification* Table J3.2

$C' = 26.0$ in. from AISC *Manual* Table 7-7 for the moment-only case (Angle = 0°)

$$M_{max} = \frac{F_{nv}}{0.90}(A_b C')$$ (*Manual* Eq. 10-7)
$$= \left(\frac{54 \text{ ksi}}{0.90}\right)(0.442 \text{ in.}^2)(26.0 \text{ in.})$$
$$= 690 \text{ kip-in.}$$

$$t_{max} = \frac{6M_{max}}{F_y l^2}$$ (*Manual* Eq. 10-6)
$$= \frac{6(690 \text{ kip-in.})}{(50 \text{ ksi})(12.0 \text{ in.})^2}$$
$$= 0.575 \text{ in.}$$

Try a plate thickness of ½ in.

*Strength of the Bolted Connection—Plate*

The available bearing strength of the plate per bolt is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration, as follows:

$$r_n = 2.4dtF_u$$ (from *Spec.* Eq. J3-6a)
$$= 2.4(¾ \text{ in.})(½ \text{ in.})(65 \text{ ksi})$$
$$= 58.5 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(58.5 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{58.5 \text{ kips/bolt}}{2.00}$ |
| $= 43.9$ kips/bolt | $= 29.3$ kips/bolt |

The available tearout strength of the bottom edge bolt in the plate is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration, as follows:

---

# IIA-208

$$l_c = l_{ev} - 0.5d_h$$
$$= 1½ \text{ in.} - 0.5\left(^{13}/{16} \text{ in.}\right)$$
$$= 1.09 \text{ in.}$$

$$r_n = 1.2l_ct F_u$$ (from *Spec.* Eq. J3-6c)
$$= 1.2(1.09 \text{ in.})(½ \text{ in.})(65 \text{ ksi})$$
$$= 42.5 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(42.5 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{42.5 \text{ kips/bolt}}{2.00}$ |
| $= 31.9$ kips/bolt | $= 21.3$ kips/bolt |

Therefore, the bolt shear determined previously controls for the bolt group in the plate.

*Shear Strength of Plate*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the plate is determined as follows:

$$A_{gv} = lt$$
$$= (12.0 \text{ in.})(½ \text{ in.})$$
$$= 6.00 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(6.00 \text{ in.}^2)$$
$$= 180 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(180 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{180 \text{ kips}}{1.50}$ |
| $= 180 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ | $= 120 \text{ kips} > 24.0 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the plate is determined using the net area determined in accordance with AISC *Specification* Section B4.3b.

$$A_{nv} = \left[l - n(d_h + \frac{1}{16} \text{ in.})\right]t$$
$$= \left[12.0 \text{ in.} - 4\left(^{13}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right](½ \text{ in.})$$
$$= 4.25 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(4.25 \text{ in.}^2)$$
$$= 166 \text{ kips}$$

---

# IIA-209

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(166 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{166 \text{ kips}}{2.00}$ |
| $= 125 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ | $= 83.0 \text{ kips} > 24.0 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture of Plate*

From AISC *Specification* Section J4.3, the block shear rupture strength of the plate is determined as follows.

$$R_n = 0.60F_u A_{nv} + U_{bs} F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs} F_u A_{nt}$$ (*Spec.* Eq. J4-5)

where

$$A_{gv} = (l - l_{ev})t$$
$$= (12.0 \text{ in.} - 1½ \text{ in.})(½ \text{ in.})$$
$$= 5.25 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (n - 0.5)(d_h + \frac{1}{16} \text{ in.})t$$
$$= 5.25 \text{ in.}^2 - (4 - 0.5)\left(^{13}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)(½ \text{ in.})$$
$$= 3.72 \text{ in.}^2$$

$$A_{nt} = \left[3 \text{ in.} + 1¼ \text{ in.} - 1.5(d_h + \frac{1}{16} \text{ in.})\right]t$$
$$= \left[3 \text{ in.} + 1¼ \text{ in.} - 1.5\left(^{13}/{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right](½ \text{ in.})$$
$$= 1.47 \text{ in.}^2$$

Because stress is not uniform along the net tensile area:

$$U_{bs} = 0.5$$

and

$$R_n = 0.60(65 \text{ ksi})(3.72 \text{ in.}^2) + 0.5(65 \text{ ksi})(1.47 \text{ in.}^2) < 0.60(50 \text{ ksi})(5.25 \text{ in.}^2) + 0.5(65 \text{ ksi})(1.47 \text{ in.}^2)$$
$$= 193 \text{ kips} < 205 \text{ kips}$$

Therefore:
$$R_n = 193 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(193 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{193 \text{ kips}}{2.00}$ |
| $= 145 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ | $= 96.5 \text{ kips} > 24.0 \text{ kips} \quad \textbf{o.k.}$ |

*Flexural Strength of Plate*

---

# IIA-210

From AISC *Manual* Part 10, the available flexural strength of the plate is determined in accordance with AISC *Specification* Section F11. Because the beam is braced, $C_b = 1.84$. The required flexural strength is determined as follows:

| LRFD | ASD |
|------|-----|
| $M_r = M_u$ | $M_r = M_a$ |
| $= V_u a$ | $= V_a a$ |
| $= (36.0 \text{ kips})(9 \text{ in.})$ | $= (24.0 \text{ kips})(9 \text{ in.})$ |
| $= 324$ kip-in. | $= 216$ kip-in. |

From AISC *Specification* Section F11.1, the flexural strength of the plate for the limit state of yielding is determined as follows:

$$Z_x = \frac{t_p d^2}{4}$$
$$= \frac{(½ \text{ in.})(12.0 \text{ in.})^2}{4}$$
$$= 18.0 \text{ in.}^3$$

$$S_x = \frac{t_p d^2}{6}$$
$$= \frac{(½ \text{ in.})(12.0 \text{ in.})^2}{6}$$
$$= 12.0 \text{ in.}^3$$

$$M_n = F_y Z \leq 1.5F_y S_x$$
$$= (50 \text{ ksi})(18.0 \text{ in.}^3) = 1.5(50 \text{ ksi})(12.0 \text{ in.}^3)$$
$$= 900 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
|  |  |
| $\phi_b M_n = 0.90(900 \text{ kip-in.})$ | $\frac{M_n}{\Omega_b} = \frac{900 \text{ kip-in}}{1.67}$ |
| $= 810 \text{ kip-in.} > 324 \text{ kip-in.} \quad \textbf{o.k.}$ | $= 539 \text{ kip-in.} > 216 \text{ kip-in.} \quad \textbf{o.k.}$ |

From AISC *Specification* Section F11.2, the flexural strength of the plate for the limit state of lateral-torsional buckling is determined as follows:

$$\frac{L_b d}{t^2} = \frac{(9 \text{ in.})(12 \text{ in.})}{(½ \text{ in.})^2}$$
$$= 432$$

$$\frac{0.08E}{F_y} = \frac{0.08(29,000 \text{ ksi})}{50 \text{ ksi}}$$
$$= 46.4$$

---

# IIA-211

$$\frac{1.9E}{F_y} = \frac{1.9(29,000 \text{ ksi})}{50 \text{ ksi}}$$
$$= 1,100$$

Because $\frac{0.08E}{F_y} < \frac{L_b d}{t^2} \leq \frac{1.9E}{F_y}$, AISC *Specification* Section F11.2(b) applies:

$$M_p = F_y Z_x$$
$$= (50 \text{ ksi})(18.0 \text{ in.}^3)$$
$$= 900 \text{ kip-in.}$$

$$M_y = F_y S_x$$
$$= (50 \text{ ksi})(12.0 \text{ in.}^3)$$
$$= 600 \text{ kip-in.}$$

$$M_n = C_b \left[1.52 - 0.274\left(\frac{L_b d}{t^2}\right)\frac{F_y}{E}\right] M_y \leq M_p$$ (*Spec.* Eq. F11-3)
$$= (1.84)\left[1.52 - 0.274(432)\left(\frac{50 \text{ ksi}}{29,000 \text{ ksi}}\right)\right](600 \text{ kip-in.}) > 900 \text{ kip-in.}$$
$$= 1,450 \text{ kip-in.} > 900 \text{ kip-in.}$$

Therefore:
$$M_n = 900 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
|  |  |
| $\phi_b M_n = 0.90(900 \text{ kip-in.})$ | $\frac{M_n}{\Omega_b} = \frac{900 \text{ kip-in}}{1.67}$ |
| $= 810 \text{ kip-in.} > 324 \text{ kip-in.} \quad \textbf{o.k.}$ | $= 539 \text{ kip-in.} > 216 \text{ kip-in.} \quad \textbf{o.k.}$ |

*Interaction of Shear Yielding and Flexural Yielding of Plate*

From AISC *Manual* Part 10, the plate is checked for the interaction of shear yielding and yielding due to flexure as follows:

| LRFD | ASD |
|------|-----|
| $\left(\frac{V_r}{V_c}\right)^2 + \left(\frac{M_r}{M_c}\right)^2 \leq 1.0$ (*Manual* Eq. 10-8) | $\left(\frac{V_r}{V_c}\right)^2 + \left(\frac{M_r}{M_c}\right)^2 \leq 1.0$ (*Manual* Eq. 10-8) |
|  |  |
| $\left(\frac{36.0 \text{ kips}}{180 \text{ kips}}\right)^2 + \left(\frac{324 \text{ kip-in.}}{810 \text{ kip-in.}}\right)^2 = 0.200 < 1.0 \quad \textbf{o.k.}$ | $\left(\frac{24.0 \text{ kips}}{120 \text{ kips}}\right)^2 + \left(\frac{216 \text{ kip-in.}}{539 \text{ kip-in.}}\right)^2 = 0.201 < 1.0 \quad \textbf{o.k.}$ |

*Flexural Rupture of Plate*

The net plastic section modulus of the plate, $Z_{net}$, is determined from AISC *Manual* Table 15-2:

---

# IIA-212

$$Z_{net} = 12.8 \text{ in.}^3$$

From AISC *Manual* Equation 9-8:

$$M_n = F_u Z_{net}$$ (*Manual* Eq. 9-8)
$$= (65 \text{ ksi})(12.8 \text{ in.}^3)$$
$$= 832 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.75$ | $\Omega_b = 2.00$ |
|  |  |
| $\phi_b M_n = 0.75(832 \text{ kip-in.})$ | $\frac{M_n}{\Omega} = \frac{832 \text{ kip-in.}}{2.00}$ |
| $= 624 \text{ kip-in.} > 324 \text{ kip-in.} \quad \textbf{o.k.}$ | $= 416 \text{ kip-in.} > 216 \text{ kip-in.} \quad \textbf{o.k.}$ |

*Weld Between Plate and Column Web*

From AISC *Manual* Part 10, a weld size of $(\frac{5}{8})t_p$ is used to develop the strength of the shear plate.

$$w = \frac{5}{8}t_p$$
$$= \frac{5}{8}(½ \text{ in.})$$
$$= \frac{5}{16} \text{ in.}$$

Use a two-sided $\frac{5}{16}$ in. fillet weld.

*Strength of Column Web at Weld*

The minimum column web thickness to match the shear rupture strength of the weld is determined as follows:

$$t_{min} = \frac{3.09D}{F_u}$$ (*Manual* Eq. 9-6)
$$= \frac{3.09(5 \text{ sixteenths})}{65 \text{ ksi}}$$
$$= 0.238 \text{ in.} < 0.440 \text{ in.} \quad \textbf{o.k.}$$

*Conclusion*

The connection is found to be adequate as given for the applied loads.

---

# IIA-213

## EXAMPLE II.A-19B EXTENDED SINGLE-PLATE CONNECTION SUBJECT TO AXIAL AND SHEAR LOADING

**Given:**

Verify the available strength of an extended single-plate connection for an ASTM A992/A992M W18×60 beam to the web of an ASTM A992/A992M W14×90 column, as shown in Figure II.A-19B-1, to support the following beam end reactions:

| LRFD | ASD |
|------|-----|
| Shear, $V_u = 75$ kips | Shear, $V_a = 50$ kips |
| Axial, $N_u = 60$ kips | Axial, $N_a = 40$ kips |

Use 70-ksi electrodes and ASTM A572/A572M Grade 50 plate. Assume a slab is present on top of the supported beam that provides sufficient restraint against minor-axis rotation of the single-plate connection.

![Connection diagram showing W14×90 column and W18×60 beam with extended single-plate connection. Left view shows elevation with dimensions: a = 9¾", 3" spacing, 2" edge distances, 3" spacing between bolt rows (12" total), ¾" edge distance at bottom, and PL ⅜×15×1'-2¾" plate. Right view shows Section A-A with 1" dia. Group 120 bolts in standard holes, thread condition N, with ¾" spacing and 3" centers indicated. Both beam and column members are labeled.]

*Fig. II.A-19B-1. Connection geometry for Example II.A-19B.*

**Solution:**

From AISC *Manual* Table 2-4 and Table 2-5, the material properties are as follows:

Beam, column
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

---

# IIA-214

Plate
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W18×60
$A_g = 17.6 \text{ in.}^2$
$d = 18.2$ in.
$t_w = 0.415$ in.
$b_f = 7.56$ in.
$t_f = 0.695$ in.
$Z_x = 20.6 \text{ in.}^3$

Column
W14×90
$d = 14.0$ in.
$t_w = 0.440$ in.
$k_{des} = 1.31$ in.

From AISC *Specification* Table J3.3, for 1-in.-diameter bolts with standard holes:

$$d_h = 1⅛ \text{ in.}$$

Per AISC *Specification* Section J3.3, standard holes are required for both the plate and beam web because the beam axial force acts longitudinally to the direction of a slotted hole, and bolts are designed for bearing.

The resultant load is determined as follows:

| LRFD | ASD |
|------|-----|
| $R_u = \sqrt{V_u^2 + N_u^2}$ | $R_a = \sqrt{V_a^2 + N_a^2}$ |
| $= \sqrt{(75 \text{ kips})^2 + (60 \text{ kips})^2}$ | $= \sqrt{(50 \text{ kips})^2 + (40 \text{ kips})^2}$ |
| $= 96.0$ kips | $= 64.0$ kips |

The resultant load angle is determined as follows:

| LRFD | ASD |
|------|-----|
| $\theta = \tan^{-1}\left(\frac{60 \text{ kips}}{75 \text{ kips}}\right)$ | $\theta = \tan^{-1}\left(\frac{40 \text{ kips}}{50 \text{ kips}}\right)$ |
| $= 38.7°$ | $= 38.7°$ |

The following checks are illustrated for an axial force in tension. See "Comments" at the end of the example discussing the case for axial force in compression.

*Maximum Plate Thickness*

Determine the maximum plate thickness, $t_{max}$, that will result in the plate yielding before the bolts shear. From AISC *Specification* Table J3.2:

$$F_{nv} = 54 \text{ ksi}$$

---

# IIA-215

From AISC *Manual* Table 7-7 for two columns of bolts, Angle = 0°, $s = 3$ in., and $n = 5$:

$$C' = 38.7 \text{ in.}$$

$$M_{max} = \frac{F_{nv}}{0.90}(A_b C')$$ (*Manual* Eq. 10-7)
$$= \frac{54 \text{ ksi}}{0.90}(0.785 \text{ in.}^2)(38.7 \text{ in.})$$
$$= 1,820 \text{ kip-in.}$$

$$t_{max} = \frac{6M_{max}}{F_y l^2}$$ (*Manual* Eq. 10-6)
$$= \frac{6(1,820 \text{ kip-in.})}{(50 \text{ ksi})(15 \text{ in.})^2}$$
$$= 0.971 \text{ in.} > ⅜ \text{ in.} \quad \textbf{o.k.}$$

*Strength of Bolted Connection*

The strength of the bolt group is determined by interpolating AISC *Manual* Table 7-7 for Angle = 30° and $n = 5$. Note that 30° is used conservatively in order to employ AISC *Manual* Table 7-7. A direct analysis can be performed to obtain an accurate value using the instantaneous center of rotation method.

$$e_x = a + 0.5s$$
$$= 9¾ \text{ in.} + 0.5(3 \text{ in.})$$
$$= 11.3 \text{ in.}$$

$$C = 3.53 \text{ by interpolation}$$

From AISC *Manual* Table 7-1, the available shear strength per bolt for 1-in-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 31.8$ kips/bolt | $\frac{r_n}{\Omega} = 21.2$ kips/bolt |

The available bearing strength of the beam web is determined from AISC *Specification* Equation J3-6b. This equation is applicable in lieu of Equation J3-6a because plowing of the bolts in the beam web is desirable to provide some flexibility in the connection:

$$r_n = 3.0dt_w F_u$$ (from *Spec.* Eq. J3-6b)
$$= 3.0(1 \text{ in.})(0.415 \text{ in.})(65 \text{ ksi})$$
$$= 80.9 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(80.9 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{80.9 \text{ kips/bolt}}{2.00}$ |
| $= 60.7$ kips/bolt | $= 40.5$ kips/bolt |

---

# IIA-216

The available tearout strength of the beam web is determined from *Specification* Equation J3-6d. Similar to the bearing strength determination, this equation is used to allow plowing of the bolts in the beam web, and thus provide some flexibility in the connection.

Because the direction of load on the bolt is unknown, the minimum bolt edge distance is used to determine a worst case available tearout strength (including a ⅛ in. tolerance to account for possible beam underrun). If a computer program is available, the true $l_c$ can be calculated based on the instantaneous center of rotation.

$$l_c = l_{eh} - 0.5d_h$$
$$= (2 \text{ in.} - ⅛ \text{ in.}) - 0.5(1⅛ \text{ in.})$$
$$= 1.19 \text{ in.}$$

$$r_n = 1.5l_ct_w F_u$$ (from *Spec.* Eq. J3-6d)
$$= 1.5(1.19 \text{ in.})(0.415 \text{ in.})(65 \text{ ksi})$$
$$= 48.2 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(48.2 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{48.2 \text{ kips/bolt}}{2.00}$ |
| $= 36.2$ kips/bolt | $= 24.1$ kips/bolt |

The available bearing strength of the plate is determined from AISC *Specification* Equation J3-6b. This equation is applicable in lieu of Equation J3-6a because plowing of the bolts in the plate is desirable to provide some flexibility in the connection:

$$r_n = 3.0dt F_u$$ (from *Spec.* Eq. J3-6b)
$$= 3.0(1 \text{ in.})(¾ \text{ in.})(65 \text{ ksi})$$
$$= 146 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(146 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{146 \text{ kips/bolt}}{2.00}$ |
| $= 110$ kips/bolt | $= 73.0$ kips/bolt |

As was discussed for the beam web, the available tearout strength of the plate is determined from AISC *Specification* Equation J3-6d. The bolt edge distance in the vertical direction controls for this design.

$$l_c = l_{ev} - 0.5d_h$$
$$= 1½ \text{ in.} - 0.5(1⅛ \text{ in.})$$
$$= 0.938 \text{ in.}$$

$$r_n = 1.5l_ct F_u$$ (from *Spec.* Eq. J3-6d)
$$= 1.5(0.938 \text{ in.})(¾ \text{ in.})(65 \text{ ksi})$$
$$= 68.6 \text{ kips/bolt}$$

---

# IIA-217

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(68.6 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{68.6 \text{ kips/bolt}}{2.00}$ |
| $= 51.5$ kips/bolt | $= 34.3$ kips/bolt |

The available strength of the bolted connection is determined using the minimum available strength calculated for bolt shear, bearing and tearout on the beam web, and bearing or tearout on the plate. From AISC *Manual* Equation 7-15, the bolt group eccentricity is accounted for by multiplying the minimum available bolt strength by the bolt coefficient $C$.

| LRFD | ASD |
|------|-----|
| $\phi R_n = C\phi r_n$ | $\frac{R_n}{\Omega} = C\frac{r_n}{\Omega}$ |
| $= 3.53(31.8 \text{ kips/bolt})$ | $= 3.53(21.2 \text{ kips/bolt})$ |
| $= 112 \text{ kips} > 96.0 \text{ kips} \quad \textbf{o.k.}$ | $= 74.8 \text{ kips} > 64.0 \text{ kips} \quad \textbf{o.k.}$ |

*Tensile Yielding Strength of Beam*

From AISC *Specification* Section D2(a), the available tensile yielding strength of the beam web is determined as follows:

$$R_n = F_y A_g$$ (*Spec.* Eq. D2-1)
$$= (50 \text{ ksi})(17.6 \text{ in.}^2)$$
$$= 880 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi R_n = 0.90(880 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{880 \text{ kips}}{1.67}$ |
| $= 792 \text{ kips} > 60 \text{ kips} \quad \textbf{o.k.}$ | $= 527 \text{ kips} > 40 \text{ kips} \quad \textbf{o.k.}$ |

*Tensile Rupture Strength of Beam*

From AISC *Specification* Section D2(b), determine the available tensile rupture strength of the beam. The effective net area is $A_e = A_n U$, where $U$ is determined from AISC *Specification* Table D3.1, Case 2.

From AISC *Specification* Commentary Section D3, the equation for $\overline{x}$ is:

$$\overline{x} = \frac{Z_x}{A}$$
$$= \frac{20.6 \text{ in.}^3}{17.6 \text{ in.}^2}$$
$$= 1.17 \text{ in.}$$

---

# IIA-218

$$U = 1 - \frac{\overline{x}}{l}$$
$$= 1 - \frac{1.17 \text{ in.}}{3.00 \text{ in.}}$$
$$= 0.610$$

$$A_n = A_g - n(d_h + \frac{1}{16} \text{ in.})t_w$$
$$= 17.6 \text{ in.}^2 - 5(1⅛ \text{ in.} + \frac{1}{16} \text{ in.})(0.415 \text{ in.})$$
$$= 15.1 \text{ in.}^2$$

$$R_n = F_u A_e$$ (*Spec.* Eq. D2-2)
$$= F_u A_n U$$
$$= (65 \text{ ksi})(15.1 \text{ in.}^2)(0.610)$$
$$= 599 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(599 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{599 \text{ kips}}{2.00}$ |
| $= 449 \text{ kips} > 60 \text{ kips} \quad \textbf{o.k.}$ | $= 300 \text{ kips} > 40 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture of Beam Web*

Block shear rupture is only applicable in the direction of the axial load because the beam is uncoped and the limit state is not applicable for an uncoped beam subject to vertical shear. Assuming a U-shaped tearout relative to the axial load, and assuming a horizontal edge distance of $l_{eh} = 2$ in. $- ⅛$ in. $= 1¾$ in. to account for a possible beam underrun of ⅛ in., the block shear rupture strength is:

$$R_n = 0.60F_u A_{nv} + U_{bs} F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs} F_u A_{nt}$$ (*Spec.* Eq. J4-5)

where

$$A_{gv} = (2 \text{ shear planes})(s + l_{eh})t_w$$
$$= (2 \text{ shear planes})(3 \text{ in.} + 1¾ \text{ in.})(0.415 \text{ in.})$$
$$= 3.94 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (2 \text{ shear planes})(1.5)(d_h + \frac{1}{16} \text{ in.})t_w$$
$$= 3.94 \text{ in.}^2 - (2 \text{ shear planes})(1.5)(1⅛ \text{ in.} + \frac{1}{16} \text{ in.})(0.415 \text{ in.})$$
$$= 2.46 \text{ in.}^2$$

$$A_{nt} = \left[12.0 \text{ in.} - (n - 1)(d_h + \frac{1}{16} \text{ in.})\right]t_w$$
$$= \left[12.0 \text{ in.} - (5 - 1)(1⅛ \text{ in.} + \frac{1}{16} \text{ in.})\right](0.415 \text{ in.})$$
$$= 3.01 \text{ in.}^2$$

$$U_{bs} = 1.0$$

---

# IIA-219

and

$$R_n = 0.60(65 \text{ ksi})(2.46 \text{ in.}^2) + 1.0(65 \text{ ksi})(3.01 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(3.94 \text{ in.}^2) + 1.0(65 \text{ ksi})(3.01 \text{ in.}^2)$$
$$= 292 \text{ kips} < 314 \text{ kips}$$

Therefore:
$$R_n = 292 \text{ kips}$$

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture of the beam web is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(292 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{292 \text{ kips}}{2.00}$ |
| $= 219 \text{ kips} > 60 \text{ kips} \quad \textbf{o.k.}$ | $= 146 \text{ kips} > 40 \text{ kips} \quad \textbf{o.k.}$ |

*Flexural Strength of Plate*

The required flexural strength of the plate is determined as follows:

| LRFD | ASD |
|------|-----|
| $M_{rx} = V_r a$ (*Manual* Eq. 12-4) | $M_{rx} = V_r a$ (*Manual* Eq. 12-4) |
| $= (75 \text{ kips})(9¾ \text{ in.})$ | $= (50 \text{ kips})(9¾ \text{ in.})$ |
| $= 731$ kip-in. | $= 488$ kip-in. |
|  |  |
| Because the beam is restrained against rotation about the minor axis: | Because the beam is restrained against rotation about the minor axis: |
|  |  |
| $M_{ry} = 0$ | $M_{ry} = 0$ |

The plate is checked for the limit state of flexural yielding, rupture, and lateral-torsional buckling using the provisions of AISC *Specification* Section F11, with $C_b = 1.84$.

The available flexural strength of the plate is determined using AISC *Specification* Section F11 as follows:

For yielding of the plate:

$$M_n = M_p = F_y Z \leq 1.5F_y S_x$$ (*Spec.* Eq. F11-1)
$$= (50 \text{ ksi})\left[\frac{(¾ \text{ in.})(15 \text{ in.})^2}{4}\right] \leq 1.5(50 \text{ ksi})\left[\frac{(¾ \text{ in.})(15 \text{ in.})^2}{6}\right]$$
$$= 2,110 \text{ kip-in.} < 2,110 \text{ kip-in.}$$
$$= 2,110 \text{ kip-in.}$$

For lateral-torsional buckling of the plate:

$$\frac{L_b d}{t^2} = \frac{(9¾ \text{ in.})(15 \text{ in.})}{(¾ \text{ in.})^2}$$
$$= 260$$

---

# IIA-220

$$\frac{0.08E}{F_y} = \frac{0.08(29,000 \text{ ksi})}{50 \text{ ksi}}$$
$$= 46.4$$

$$\frac{1.9E}{F_y} = \frac{1.9(29,000 \text{ ksi})}{50 \text{ ksi}}$$
$$= 1,100$$

Because $\frac{0.08E}{F_y} < \frac{L_b d}{t^2} \leq \frac{1.9E}{F_y}$, AISC *Specification* Section F11.2(b) applies:

$$M_y = F_y S_x$$
$$= (50 \text{ ksi})\left[\frac{(¾ \text{ in.})(15 \text{ in.})^2}{6}\right]$$
$$= 1,410 \text{ kip-in.}$$

$$M_n = C_b \left[1.52 - 0.274\left(\frac{L_b d}{t^2}\right)\frac{F_y}{E}\right] M_y \leq M_p$$ (*Spec.* Eq. F11-3)
$$= 1.84\left[1.52 - 0.274(260)\left(\frac{50 \text{ ksi}}{29,000 \text{ ksi}}\right)\right](1,410 \text{ kip-in.}) \leq 2,110 \text{ kip-in.}$$
$$= 3,620 \text{ kip-in.} > 2,110 \text{ kip-in.}$$

Therefore:

$$M_n = 2,110 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
|  |  |
| $\phi_b M_n = 0.90(2,110 \text{ kip-in.})$ | $\frac{M_n}{\Omega_b} = \frac{2,110 \text{ kip-in.}}{1.67}$ |
| $= 1,900 \text{ kip-in.} > 731 \text{ kip-in.} \quad \textbf{o.k.}$ | $= 1,260 \text{ kip-in.} > 488 \text{ kip-in.} \quad \textbf{o.k.}$ |

*Shear Yielding Strength of Plate*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the plate is determined as follows:

$$A_{gv} = lt$$
$$= (15 \text{ in.})(¾ \text{ in.})$$
$$= 11.3 \text{ in.}^2$$

$$R_{nv} = 0.60F_y A_{gv}$$ (from *Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(11.3 \text{ in.}^2)$$
$$= 339 \text{ kips}$$

---

# IIA-221

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_{nv} = 1.00(339 \text{ kips})$ | $\frac{R_{nv}}{\Omega} = \frac{339 \text{ kips}}{1.50}$ |
| $= 339 \text{ kips} > 75 \text{ kips} \quad \textbf{o.k.}$ | $= 226 \text{ kips} > 50 \text{ kips} \quad \textbf{o.k.}$ |

*Tension Yielding Strength of Plate*

From AISC *Specification* Section J4.1(a), the available tensile yielding strength of the plate is determined as follows:

$$A_g = lt$$
$$= (15 \text{ in.})(¾ \text{ in.})$$
$$= 11.3 \text{ in.}^2$$

$$R_{np} = F_y A_g$$ (from *Spec.* Eq. J4-1)
$$= (50 \text{ ksi})(11.3 \text{ in.}^2)$$
$$= 565 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi R_{np} = 0.90(565 \text{ kips})$ | $\frac{R_{np}}{\Omega} = \frac{565 \text{ kips}}{1.67}$ |
| $= 509 \text{ kips} > 60 \text{ kips} \quad \textbf{o.k.}$ | $= 338 \text{ kips} > 40 \text{ kips} \quad \textbf{o.k.}$ |

*Interaction of Axial, Flexure, and Shear Yielding in Plate*

Interaction is checked using the method outlined in AISC *Manual* Part 12.

| LRFD | ASD |
|------|-----|
| $\frac{P_r}{P_c} = \frac{N_u}{\phi R_{np}}$ | $\frac{P_r}{P_c} = \frac{\Omega N_a}{R_{np}}$ |
| $= \frac{60 \text{ kips}}{509 \text{ kips}}$ | $= \frac{40 \text{ kips}}{338 \text{ kips}}$ |
| $= 0.118$ | $= 0.118$ |
|  |  |
| Because $\frac{P_r}{P_c} < 0.2$, use AISC *Manual* Equation 12-2: | Because $\frac{P_r}{P_c} < 0.2$, use AISC *Manual* Equation 12-2: |
|  |  |
| $\left[\frac{P_r}{2P_c} + \left(\frac{M_{rx}}{M_{cx}} + \frac{M_{ry}}{M_{cy}}\right)\right]^2 + \left(\frac{V_r}{V_c}\right)^2 \leq 1$ | $\left[\frac{P_r}{2P_c} + \left(\frac{M_{rx}}{M_{cx}} + \frac{M_{ry}}{M_{cy}}\right)\right]^2 + \left(\frac{V_r}{V_c}\right)^2 \leq 1$ |
|  |  |
| $= \left[\frac{60 \text{ kips}}{2(509 \text{ kips})} + \left(\frac{731 \text{ kip-in.}}{1,900 \text{ kip-in.}} + 0\right)\right]^2$ | $= \left[\frac{40 \text{ kips}}{2(338 \text{ kips})} + \left(\frac{488 \text{ kip-in.}}{1,260 \text{ kip-in.}} + 0\right)\right]^2$ |
| $+ \left(\frac{75 \text{ kips}}{339 \text{ kips}}\right)^2 \leq 1$ | $+ \left(\frac{50 \text{ kips}}{226 \text{ kips}}\right)^2 \leq 1$ |
| $= 0.246 < 1 \quad \textbf{o.k.}$ | $= 0.248 < 1 \quad \textbf{o.k.}$ |

---

# IIA-222

*Tensile Rupture Strength of Plate*

From AISC *Specification* Section J4.1(b), the available tensile rupture strength of the plate is determined as follows:

$$A_n = \left[l - n(d_h + \frac{1}{16} \text{ in.})\right]t$$
$$= \left[15 \text{ in.} - (5 \text{ bolts})(1⅛ \text{ in.} + \frac{1}{16} \text{ in.})\right](¾ \text{ in.})$$
$$= 6.80 \text{ in.}^2$$

AISC *Specification* Table D3.1, Case 1, applies in this case because the tension load is transmitted directly to the cross-sectional element by fasteners; therefore, $U = 1.0$.

$$A_e = A_n U$$ (*Spec.* Eq. D3-1)
$$= (6.80 \text{ in.}^2)(1.0)$$
$$= 6.80 \text{ in.}^2$$

$$R_{np} = F_u A_e$$ (from *Spec.* Eq. J4-2)
$$= (65 \text{ ksi})(6.80 \text{ in.}^2)$$
$$= 442 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_{np} = 0.75(442 \text{ kips})$ | $\frac{R_{np}}{\Omega} = \frac{442 \text{ kips}}{2.00}$ |
| $= 332 \text{ kips} > 60 \text{ kips} \quad \textbf{o.k.}$ | $= 221 \text{ kips} > 40 \text{ kips} \quad \textbf{o.k.}$ |

*Flexural Rupture of the Plate*

The available flexural rupture strength of the plate is determined as follows:

$$Z_{net} = \frac{1}{4}t\left(s - d_h'\right)\left(n^2 s + d_h'^2\right)$$ (*Manual* Eq. 15-4)
$$= \frac{1}{4}(¾ \text{ in.})\left[3 \text{ in.} - (1⅛ \text{ in.} + \frac{1}{16} \text{ in.})\right]\left[(5)^2(3 \text{ in.}) + (1⅛ \text{ in.} + \frac{1}{16} \text{ in.})\right]$$
$$= 25.9 \text{ in.}^3$$

$$M_n = F_u Z_{net}$$ (*Manual* Eq. 9-8)
$$= (65 \text{ ksi})(25.9 \text{ in.}^3)$$
$$= 1,680 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi M_n = 0.75(1,680 \text{ kip-in.})$ | $\frac{M_n}{\Omega} = \frac{1,680 \text{ kip-in.}}{2.00}$ |
| $= 1,260 \text{ kip-in.} > 731 \text{ kip-in.} \quad \textbf{o.k.}$ | $= 840 \text{ kip-in.} > 488 \text{ kip-in.} \quad \textbf{o.k.}$ |

---

# IIA-223

*Shear Rupture Strength of Plate*

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the plate is determined as follows:

$$A_{nv} = \left[l - n(d_h + \frac{1}{16} \text{ in.})\right]t_p$$
$$= \left[15 \text{ in.} - 5(1⅛ \text{ in.} + \frac{1}{16} \text{ in.})\right](¾ \text{ in.})$$
$$= 6.80 \text{ in.}^2$$

$$R_{nv} = 0.60F_u A_{nv}$$ (from *Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(6.80 \text{ in.}^2)$$
$$= 265 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_{nv} = 0.75(265 \text{ kips})$ | $\frac{R_{nv}}{\Omega} = \frac{265 \text{ kips}}{2.00}$ |
| $= 199 \text{ kips} > 75 \text{ kips} \quad \textbf{o.k.}$ | $= 133 \text{ kips} > 50 \text{ kips} \quad \textbf{o.k.}$ |

*Interaction of Axial, Flexure, and Shear Rupture in Plate*

Interaction is checked using the method outlined in AISC *Manual* Part 12.

| LRFD | ASD |
|------|-----|
| $\frac{P_r}{P_c} = \frac{N_u}{\phi R_{np}}$ | $\frac{P_r}{P_c} = \frac{\Omega N_a}{R_{np}}$ |
| $= \frac{60 \text{ kips}}{332 \text{ kips}}$ | $= \frac{40 \text{ kips}}{221 \text{ kips}}$ |
| $= 0.181$ | $= 0.181$ |
|  |  |
| Because $\frac{P_r}{P_c} < 0.2$, use AISC *Manual* Equation 12-2: | Because $\frac{P_r}{P_c} < 0.2$, use AISC *Manual* Equation 12-2: |
|  |  |
| $\left[\frac{P_r}{2P_c} + \left(\frac{M_{rx}}{M_{cx}} + \frac{M_{ry}}{M_{cy}}\right)\right]^2 + \left(\frac{V_r}{V_c}\right)^2 \leq 1$ | $\left[\frac{P_r}{2P_c} + \left(\frac{M_{rx}}{M_{cx}} + \frac{M_{ry}}{M_{cy}}\right)\right]^2 + \left(\frac{V_r}{V_c}\right)^2 \leq 1$ |
|  |  |
| $\left[\frac{60 \text{ kips}}{2(332 \text{ kips})} + \left(\frac{731 \text{ kip-in.}}{1,260 \text{ kip-in.}} + 0\right)\right]^2 + \left(\frac{75 \text{ kips}}{199 \text{ kips}}\right)^2 \leq 1$ | $\left[\frac{40 \text{ kips}}{2(221 \text{ kips})} + \left(\frac{488 \text{ kip-in.}}{840 \text{ kip-in.}} + 0\right)\right]^2 + \left(\frac{50 \text{ kips}}{133 \text{ kips}}\right)^2 \leq 1$ |
| $0.592 < 1 \quad \textbf{o.k.}$ | $0.592 < 1 \quad \textbf{o.k.}$ |

*Block Shear Rupture Strength of Plate—Beam Shear Direction*

The nominal strength for the limit state of block shear rupture of the plate, assuming an L-shaped tearout due to the shear load only as shown in Figure II.A-19B-2(a), is determined as follows:

$$R_{bsv} = 0.60F_u A_{nv} + U_{bs} F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs} F_u A_{nt}$$ (from *Spec.* Eq. J4-5)

where

---

# IIA-224

$$A_{gv} = (l - l_{ev})t$$
$$= (15 \text{ in.} - 1½ \text{ in.})(¾ \text{ in.})$$
$$= 10.1 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (n_v - 0.5)(d_h + \frac{1}{16} \text{ in.})t$$
$$= 10.1 \text{ in.}^2 - (5 - 0.5)(1⅛ \text{ in.} + \frac{1}{16} \text{ in.})(¾ \text{ in.})$$
$$= 6.09 \text{ in.}^2$$

$$A_{nt} = \left[l_{eh} + (n_t - 1)s - (n_t - 0.5)(d_h + \frac{1}{16} \text{ in.})\right]t$$
$$= \left[2 \text{ in.} + (2 - 1)(3 \text{ in.}) - (2 - 0.5)(1⅛ \text{ in.} + \frac{1}{16} \text{ in.})\right](¾ \text{ in.})$$
$$= 2.41 \text{ in.}^2$$

Because stress is not uniform along the net tensile area, $U_{bs} = 0.5$.

$$R_{bsv} = 0.60(65 \text{ ksi})(6.09 \text{ in.}^2) + 0.5(65 \text{ ksi})(2.41 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(10.1 \text{ in.}^2) + 0.5(65 \text{ ksi})(2.41 \text{ in.}^2)$$
$$= 316 \text{ kips} < 381 \text{ kips}$$

Therefore:
$$R_{bsv} = 316 \text{ kips}$$

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture on the plate is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_{bsv} = 0.75(316 \text{ kips})$ | $\frac{R_{bsv}}{\Omega} = \frac{316 \text{ kips}}{2.00}$ |
| $= 237 \text{ kips} > 75 \text{ kips} \quad \textbf{o.k.}$ | $= 158 \text{ kips} > 50 \text{ kips} \quad \textbf{o.k.}$ |

![Three diagrams showing block shear rupture failure modes for a bolted plate connection. Each shows a vertical plate with bolt holes. (a) shows beam shear direction with vertical shear load V, with dimensions indicating 4@3"=12" bolt spacing, 1½" edge distance, 3" and 2" edge margins, and total length l = 15". (b) shows beam axial direction L-shaped failure pattern with horizontal load N and similar dimensions. (c) shows beam axial direction U-shaped failure pattern, also with horizontal load N and same dimensional layout. All three diagrams show hatched areas indicating the block shear failure zones.]

*(a) Beam shear direction*
*(b) Beam axial direction—L-shaped*
*(c) Beam axial direction—U-shaped*

*Fig. II.A-19B-2. Block shear rupture of plate.*

---

# IIA-225

*Block Shear Rupture Strength of the Plate—Beam Axial Direction*

The plate block shear rupture failure path due to axial load only could occur as an L- or U-shape. Assuming an L-shaped failure path due to axial load only, as shown in Figure II.A-19B-2(b), the available block shear rupture strength of the plate is:

$$R_{bsh} = 0.60F_u A_{nv} + U_{bs} F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs} F_u A_{nt}$$ (from *Spec.* Eq. J4-5)

where

$$A_{gv} = \left[(n_h - 1)s + l_{eh}\right]t$$
$$= \left[(2 - 1)(3 \text{ in.}) + 2 \text{ in.}\right](¾ \text{ in.})$$
$$= 3.75 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (n_h - 0.5)(d_h + \frac{1}{16} \text{ in.})t$$
$$= 3.75 \text{ in.}^2 - (2 - 0.5)(1⅛ \text{ in.} + \frac{1}{16} \text{ in.})(¾ \text{ in.})$$
$$= 2.41 \text{ in.}^2$$

$$A_{nt} = \left[l_{ev} + (n_c - 1)s - (n_c - 0.5)(d_h + \frac{1}{16} \text{ in.})\right]t$$
$$= \left[1½ \text{ in.} + (5 - 1)(3 \text{ in.}) - (5 - 0.5)(1⅛ \text{ in.} + \frac{1}{16} \text{ in.})\right](¾ \text{ in.})$$
$$= 6.12 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_{bsh} = 0.60(65 \text{ ksi})(2.41 \text{ in.}^2) + 1.0(65 \text{ ksi})(6.12 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(3.75 \text{ in.}^2) + 1.0(65 \text{ ksi})(6.12 \text{ in.}^2)$$
$$= 492 \text{ kips} < 510 \text{ kips}$$

Therefore:
$$R_{bsh} = 492 \text{ kips}$$

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture on the plate is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_{bsh} = 0.75(492 \text{ kips})$ | $\frac{R_{bsh}}{\Omega} = \frac{492 \text{ kips}}{2.00}$ |
| $= 369 \text{ kips} > 60 \text{ kips} \quad \textbf{o.k.}$ | $= 246 \text{ kips} > 40 \text{ kips} \quad \textbf{o.k.}$ |

Assuming a U-shaped failure path in the plate due to axial load, as shown in Figure II.A-19B-2(c), the available block shear rupture strength of the plate is:

$$R_{bsh} = 0.60F_u A_{nv} + U_{bs} F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs} F_u A_{nt}$$ (from *Spec.* Eq. J4-5)

where

---

# IIA-226

$$A_{gv} = (2 \text{ shear planes})\left[l_{eh} + (n_h - 1)s\right]t$$
$$= (2 \text{ shear planes})\left[2 \text{ in.} + (2 - 1)(3 \text{ in.})\right](¾ \text{ in.})$$
$$= 7.50 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (2 \text{ shear planes})(n_h - 0.5)(d_h + \frac{1}{16} \text{ in.})t$$
$$= 7.50 \text{ in.}^2 - (2 \text{ shear planes})(2 - 0.5)(1⅛ \text{ in.} + \frac{1}{16} \text{ in.})(¾ \text{ in.})$$
$$= 4.83 \text{ in.}^2$$

$$A_{nt} = \left[(n_v - 1)s - (n_v - 1)(d_h + \frac{1}{16} \text{ in.})\right]t$$
$$= \left[(5 - 1)(3 \text{ in.}) - (5 - 1)(1⅛ \text{ in.} + \frac{1}{16} \text{ in.})\right](¾ \text{ in.})$$
$$= 5.44 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_{bsh} = 0.60(65 \text{ ksi})(4.83 \text{ in.}^2) + 1.0(65 \text{ ksi})(5.44 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(7.50 \text{ in.}^2) + 1.0(65 \text{ ksi})(5.44 \text{ in.}^2)$$
$$= 542 \text{ kips} < 579 \text{ kips}$$

Therefore:
$$R_{bsh} = 542 \text{ kips}$$

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture on the plate is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_{bsh} = 0.75(542 \text{ kips})$ | $\frac{R_{bsh}}{\Omega} = \frac{542 \text{ kips}}{2.00}$ |
| $= 407 \text{ kips} > 60 \text{ kips} \quad \textbf{o.k.}$ | $= 271 \text{ kips} > 40 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture Strength of Plate—Combined Shear and Axial Interaction*

The same L-shaped block shear rupture failure path is loaded by forces in both the shear and axial directions. The interaction of loading in both directions is determined using AISC *Manual* Equation 12-1 as follows:

| LRFD | ASD |
|------|-----|
| $\left(\frac{V_u}{\phi R_{bsv}}\right)^2 + \left(\frac{N_u}{\phi R_{bsh}}\right)^2 \leq 1$ | $\left(\frac{\Omega V_a}{R_{bsv}}\right)^2 + \left(\frac{\Omega N_a}{R_{bsh}}\right)^2 \leq 1$ |
|  |  |
| $\left(\frac{75 \text{ kips}}{237 \text{ kips}}\right)^2 + \left(\frac{60 \text{ kips}}{369 \text{ kips}}\right)^2 = 0.127 < 1 \quad \textbf{o.k.}$ | $\left(\frac{50 \text{ kips}}{158 \text{ kips}}\right)^2 + \left(\frac{40 \text{ kips}}{246 \text{ kips}}\right)^2 = 0.127 < 1 \quad \textbf{o.k.}$ |

*Shear Rupture Strength of Column Web at Weld*

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the column web is determined as follows:

---

# IIA-227

$$A_{nv} = 2lt_w$$
$$= 2(15 \text{ in.})(0.440 \text{ in.})$$
$$= 13.2 \text{ in.}^2$$

$$R_n = 0.60F_u A_v$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(13.2 \text{ in.}^2)$$
$$= 515 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(515 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{515 \text{ kips}}{2.00}$ |
| $= 386 \text{ kips} > 96.0 \text{ kips} \quad \textbf{o.k.}$ | $= 258 \text{ kips} > 64.0 \text{ kips} \quad \textbf{o.k.}$ |

*Yield Line Analysis on Supporting Column Web*

A yield line analysis is used to determine the strength of the column web in the direction of the axial tension load. The yield line and associated dimensions are shown in Figure II.A-19B-3, and the available strength is determined as follows:

$$w = d - 2k_{des}$$
$$= 14.0 \text{ in.} - 2(1.31 \text{ in.})$$
$$= 11.4 \text{ in.}$$

![Diagram showing a yield line analysis for a column web. The diagram depicts a front view of a column web with vertical dimensions labeled. Two horizontal lines marked as "kdes" appear at the top and bottom. The width "w" is shown in the middle section. The yield line forms a pattern with dimensions "a", "b", and "c" marked horizontally, and total height "l" marked vertically. The yield line pattern shows a spread from the connection plate into the column web. The column is indicated on both sides of the diagram.]

*Fig II.A-19B-3. Yield line for column web.*

---

# IIA-228

$$a = \frac{d}{2} - k_{des} + \frac{t_w}{2}$$
$$= \frac{14.0 \text{ in.}}{2} - 1.31 \text{ in.} + \frac{0.415 \text{ in.}}{2}$$
$$= 5.90 \text{ in.}$$

$$b = \frac{d}{2} - k_{des} - \frac{t_w}{2} - t_p$$
$$= \frac{14.0 \text{ in.}}{2} - 1.31 \text{ in.} - \frac{0.415 \text{ in.}}{2} - ¾ \text{ in.}$$
$$= 4.73 \text{ in.}$$

$$c = t_p$$
$$= ¾ \text{ in.}$$

$$R_n = \frac{t_w^2 F_y}{4}\left[\frac{4\sqrt{2wab(a + b)} + l(a + b)}{ab}\right]$$ (*Manual* Eq. 9-45)
$$= \frac{(0.440 \text{ in.})^2(50 \text{ ksi})}{4}\left[\frac{4\sqrt{2(11.4 \text{ in.})(5.90 \text{ in.})(4.73 \text{ in.})(5.90 \text{ in.} + 4.73 \text{ in.})} + (15 \text{ in.})(5.90 \text{ in.} + 4.73 \text{ in.})}{(5.90 \text{ in.})(4.73 \text{ in.})}\right]$$
$$= 42.4 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(42.4 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{42.4 \text{ kips}}{1.50}$ |
| $= 42.4 \text{ kips} < 60 \text{ kips} \quad \textbf{n.g.}$ | $= 28.3 \text{ kips} < 40 \text{ kips} \quad \textbf{n.g.}$ |

The available column web strength is not adequate to resist the axial force in the beam. The column may be increased in size for an adequate web thickness or reinforced with stiffeners or web doubler plates. For example, a W14×120 column, with $t_w = 0.590$ in., has adequate strength to resist the given forces.

*Strength of Weld*

A two-sided fillet weld with size of $(\frac{5}{8})t_p = 0.469$ in. (use ½ in. fillet welds) is used. As discussed in AISC *Manual* Part 10, this weld size will develop the strength of the shear plate.

*Conclusion*

The configuration given does not work due to the inadequate column web. The column would need to be increased in size or reinforced as discussed previously.

*Comments:* If the applied axial load were in compression, the connection plate would need to be checked for compressive flexural buckling strength as follows. This is required in the case of the extended or conventional configuration where $L_c/r > 25$.

From AISC *Specification* Table C-A-7.1, Case (d):

$$K = 1.2$$

---

# IIA-229

$$\frac{L_c}{r} = \frac{KL}{r}$$
$$= \frac{1.2(9¾ \text{ in.})}{¾ \text{ in.}/\sqrt{12}}$$
$$= 54.0$$

As stated in AISC *Specification* Section J4.4, if $L_c/r$ is greater than 25, Chapter E applies. The available critical stress of the plate, $\phi F_{cr}$ or $F_{cr}/\Omega$, is determined using AISC *Manual* Table 4-14 as follows:

| LRFD | ASD |
|------|-----|
| $\phi F_{cr} = 36.4$ ksi | $\frac{F_{cr}}{\Omega} = 24.2$ ksi |
|  |  |
| $\phi R_n = \phi F_{cr}lt_p$ | $\frac{R_n}{\Omega} = \frac{F_{cr}}{\Omega}lt_p$ |
| $= (36.4 \text{ ksi})(15 \text{ in.})(¾ \text{ in.})$ | $= (24.2 \text{ ksi})(15 \text{ in.})(¾ \text{ in.})$ |
| $= 410 \text{ kips} > 60 \text{ kips} \quad \textbf{o.k.}$ | $= 272 \text{ kips} > 40 \text{ kips} \quad \textbf{o.k.}$ |

*Column Reinforcement*

As mentioned previously, there are three options to correct the column web failure. These options are as follows:

1) Use a heavier column. This may not be practical because the steel may have been purchased and perhaps detailed and fabricated before the problem is found.

2) Use a web doubler plate. This plate would be fitted about the shear plate on the same side of the column web as the shear plate. This necessitates a large amount of cutting, fitting, and welding, and is therefore expensive.

3) Use stiffeners or stabilizer plates—also called continuity plates. A common practice for using stiffeners in this manner is to maintain the shear force eccentricity at the face of the column web, which avoids introducing a weak-axis moment to the column. Alternatively, reducing eccentricity of the connection is possible if the column has available flexural strength for the induced weak-axis moment.

---

# IIA-230

## EXAMPLE II.A-20 ALL-BOLTED SINGLE-PLATE SHEAR SPLICE

**Given:**

Verify that the all-bolted single-plate shear splice between two ASTM A992/A992M beams, as shown in Figure II.A-20-1, is adequate to support the following beam end reactions:

$$R_D = 10 \text{ kips}$$
$$R_L = 30 \text{ kips}$$

Use ASTM A572/A572M Grade 50 plate.

![Connection diagram showing a single-plate shear splice between two W24 beams (W24×68 on left, W24×55 on right). The connection shows a vertical plate (PL⅜×8×1'-0") centered between the beams with 8 bolts (⅞" dia. Group 120, thread condition N, std. holes) arranged in two vertical columns. The splice plate is centered with moment M = Re/2 indicated by arrows. Dimensions show 2½" spacing at ends, 1⅜" edge distance, 5" vertical spacing between bolt rows (3 @ 3" = 9" total), ½" horizontal spacing, and ½" edge distance at bottom.]

*Fig. II.A-20-1. Connection geometry for Example II.A-20.*

**Solution:**

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Beam and column
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Plate
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W24×55
$t_w = 0.395$ in.

---

# IIA-231

Beam
W24×68
$t_w = 0.415$ in.

From AISC *Specification* Table J3.3, for ⅞-in.-diameter bolts with standard holes:

$$d_h = \frac{15}{16} \text{ in.}$$

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(10 \text{ kips}) + 1.6(30 \text{ kips})$ | $R_a = 10 \text{ kips} + 30 \text{ kips}$ |
| $= 60.0$ kips | $= 40.0$ kips |

*Strength of the Bolted Connection—Plate*

Note: When the splice is symmetrical, the eccentricity of the shear to the center of gravity of either bolt group is equal to half the distance between the centroids of the bolt groups. Therefore, each bolt group can be designed for the shear, $R_u$ or $R_a$, and one-half the eccentric moment. Thus, the eccentricity on each bolt group is determined as follows:

$$\frac{e}{2} = \frac{5 \text{ in.}}{2}$$
$$= 2.50 \text{ in.}$$

From the User Note in AISC *Specification* Section J3.7, the strength of the bolt group is taken as the sum of the individual strengths of the individual fasteners, which may be taken as the lesser of the fastener shear strength per AISC *Specification* Section J3.7, the bearing strength at the bolt hole per AISC *Specification* Section J3.11, or the tearout strength at the bolt hole per AISC *Specification* Section J3.11.

From AISC *Manual* Table 7-1, the available shear strength per bolt for ⅞-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 24.3$ kips/bolt | $\frac{r_n}{\Omega} = 16.2$ kips/bolt |

The available bearing strength of the plate per bolt is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration:

$$r_n = 2.4dtF_u$$ (from *Spec.* Eq. J3-6a)
$$= (2.4)(⅞ \text{ in.})(⅜ \text{ in.})(65 \text{ ksi})$$
$$= 51.2 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(51.2 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{51.2 \text{ kips/bolt}}{2.00}$ |
| $= 38.4$ kips/bolt | $= 25.6$ kips/bolt |

---

# IIA-232

The available tearout strength of the plate per bolt is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration. Note: The available tearout strength based on edge distance will conservatively be used for all of the bolts.

$$l_c = l_{ev} - 0.5(d_h)$$
$$= 1½ \text{in.} - 0.5(\frac{15}{16} \text{ in.})$$
$$= 1.03 \text{ in.}$$

$$r_n = 1.2l_ctF_u$$ (from *Spec.* Eq. J3-6c)
$$= 1.2(1.03 \text{ in.})(⅜ \text{ in.})(65 \text{ ksi})$$
$$= 30.1 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(30.1 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{30.1 \text{ kips/bolt}}{2.00}$ |
| $= 22.6$ kips/bolt | $= 15.1$ kips/bolt |

The tearout strength controls over bearing and shear for bolts in the plate.

The available strength of the bolt group is determined by interpolating AISC *Manual* Table 7-6, with $n = 4$, Angle = 0°, and $e_x = 2½$ in.

$$C = 3.07$$

| LRFD | ASD |
|------|-----|
| $C_{min} = \frac{R_u}{\phi r_n}$ | $C_{min} = \frac{R_a}{r_n/\Omega}$ |
| $= \frac{60.0 \text{ kips}}{22.6 \text{ kips/bolt}}$ | $= \frac{40.0 \text{ kips}}{15.1 \text{ kips/bolt}}$ |
| $= 2.65 < 3.07 \quad \textbf{o.k.}$ | $= 2.65 < 3.07 \quad \textbf{o.k.}$ |

*Strength of the Bolted Connection—Beam Web*

By inspection, bearing and tearout on the webs of the beams will not govern because the web thicknesses are greater than the plate thickness.

*Flexural Yielding of Plate*

The required flexural strength is determined as follows:

| LRFD | ASD |
|------|-----|
| $M_u = R_u \left(\frac{e}{2}\right)$ | $M_a = R_a \left(\frac{e}{2}\right)$ |
|  |  |
| $= 60.0 \text{ kips}\left(\frac{5 \text{ in.}}{2}\right)$ | $= 40.0 \text{ kips}\left(\frac{5 \text{ in.}}{2}\right)$ |
| $= 150$ kip-in. | $= 100$ kip-in. |

The available flexural strength is determined as follows:

---

# IIA-233

$$M_n = F_y Z_x$$
$$= (50\text{ksi})\left[\frac{(⅜ \text{ in.})(12 \text{ in.})^2}{4}\right]$$
$$= 675 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
|  |  |
| $\phi M_n = 0.90(675 \text{ kip-in.})$ | $\frac{M_n}{\Omega_b} = \frac{675 \text{ kip-in.}}{1.67}$ |
| $= 608 \text{ kip-in.} > 150 \text{ kip-in.} \quad \textbf{o.k.}$ | $= 404 \text{ kip-in.} > 100 \text{ kip-in.} \quad \textbf{o.k.}$ |

*Flexural Rupture of Plate*

The net plastic section modulus of the plate, $Z_{net}$, is determined from AISC *Manual* Table 15-2:

$$Z_{net} = 9.00 \text{ in.}^3$$

$$M_n = F_u Z_{net}$$ (*Manual* Eq. 9-8)
$$= (65 \text{ ksi})(9.00 \text{ in.}^3)$$
$$= 585 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.75$ | $\Omega_b = 2.00$ |
|  |  |
| $\phi_b M_n = 0.75(585 \text{ kip-in.})$ | $\phi_b M_n = \frac{585 \text{ kip-in.}}{2.00}$ |
| $= 439 \text{ kip-in.} > 150 \text{ kip-in.} \quad \textbf{o.k.}$ | $= 293 \text{ kip-in.} > 100 \text{ kip-in.} \quad \textbf{o.k.}$ |

*Shear Strength of Plate*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the plate is determined as follows:

$$A_{gv} = lt$$
$$= (12 \text{ in.})(⅜ \text{ in.})$$
$$= 4.50 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(4.50 \text{ in.}^2)$$
$$= 135 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(135 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{135 \text{ kips}}{1.50}$ |
| $= 135 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $= 90.0 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

---

# IIA-234

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the plate is determined using the net area determined in accordance with AISC *Specification* Section B4.3b.

$$A_{nv} = \left[d - n(d_h + \frac{1}{16} \text{ in.})\right]t$$
$$= \left[12 \text{ in.} - 4(\frac{15}{16} \text{ in.} + \frac{1}{16} \text{ in.})\right](⅜ \text{ in.})$$
$$= 3.00 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(3.00 \text{ in.}^2)$$
$$= 117 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(117 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{117 \text{ kips}}{2.00}$ |
| $= 87.8 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $= 58.5 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture of Plate*

The nominal strength for the limit state of block shear rupture is given by AISC *Specification* Section J4.3.

$$R_n = 0.60F_u A_{nv} + U_{bs} F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs} F_u A_{nt}$$ (*Spec.* Eq. J4-5)

The available block shear rupture strength of the plate is determined as follows, using AISC *Manual* Tables 9-3a, 9-3b, and 9-3c, and AISC *Specification* Equation J4-5, with $n = 4$, $l_{eh} = l_{ev} = 1½$ in., and $U_{bs} = 1.0$.

| LRFD | ASD |
|------|-----|
| Tension rupture component from AISC *Manual* Table 9-3a: | Tension rupture component from AISC *Manual* Table 9-3a: |
|  |  |
| $\frac{\phi F_u A_{nt}}{t} = 48.8$ kips/in. | $\frac{F_u A_{nt}}{\Omega t} = 32.5$ kips/in. |
|  |  |
| Shear yielding component from AISC *Manual* Table 9-3b: | Shear yielding component from AISC *Manual* Table 9-3b: |
|  |  |
| $\frac{\phi 0.60F_y A_{gv}}{t} = 236$ kips/in. | $\frac{0.60F_y A_{gv}}{\Omega t} = 158$ kips/in. |
|  |  |
| Shear rupture component from AISC *Manual* Table 9-3c: | Shear rupture component from AISC *Manual* Table 9-3c: |
|  |  |
| $\frac{\phi 0.60F_u A_{nv}}{t} = 205$ kips/in. | $\frac{0.60F_u A_{nv}}{\Omega t} = 137$ kips/in. |

---

# IIA-235

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi 0.60F_u A_{nv} + \phi U_{bs} F_u A_{nt}$ | $\frac{R_n}{\Omega} = \frac{0.60F_u A_{nv}}{\Omega} + \frac{U_{bs} F_u A_{nt}}{\Omega}$ |
| $\leq \phi 0.60F_y A_{gv} + \phi U_{bs} F_u A_{nt}$ | $\leq \frac{0.60F_y A_{gv}}{\Omega} + \frac{U_{bs} F_u A_{nt}}{\Omega}$ |
|  |  |
| $= (⅜ \text{ in.})\left[205 \text{ kip/in.} + (1.0)(48.8 \text{ kip/in.})\right]$ | $= (⅜ \text{ in.})\left[137 \text{ kip/in.} + (1.0)(32.5 \text{ kip/in.})\right]$ |
| $\leq (⅜ \text{ in.})\left[236 \text{ kip/in.} + (1.0)(48.8 \text{ kip/in.})\right]$ | $\leq (⅜ \text{ in.})\left[158 \text{ kip/in.} + (1.0)(32.5 \text{ kip/in.})\right]$ |
| $= 95.2 \text{ kips} < 107 \text{ kips}$ | $= 63.6 \text{ kips} < 71.4 \text{ kips}$ |
|  |  |
| Therefore: | Therefore: |
|  |  |
| $\phi R_n = 95.2 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 63.6 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

*Conclusion*

The connection is found to be adequate as given for the applied force.

---

# IIA-236

## EXAMPLE II.A-21 BOLTED/WELDED SINGLE-PLATE SHEAR SPLICE

**Given:**

Verify that the single-plate shear splice between two ASTM A992/A992M beams, as shown in Figure II.A-21-1, is adequate to support the following beam end reactions:

$$R_D = 8 \text{ kips}$$
$$R_L = 24 \text{ kips}$$

Use an ASTM A572/A572M Grade 50 plate and 70-ksi electrodes.

![Connection diagram showing a single-plate shear splice between two W16 beams (W16×50 on left, W16×31 on right). The connection shows a vertical plate (PL⅜×8×1'-0") with 4 bolts (⅞" dia. Group 120, thread condition N, std. holes) arranged vertically on the left side at 3" spacing (3 @ 3" = 9"), with 1⅜" edge distances top and bottom. The right side shows a weld centroid. Dimensions show 3" horizontal spacing, 3½" from weld to right edge, ½" plate offset, and ⅜" thickness. The plate is shown in plan view with hatching.]

*Fig. II.A-21-1. Connection geometry for Example II.A-21.*

**Solution:**

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Beam
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Plate
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W16×31
$t_w = 0.275$ in.

---

# IIA-237

Beam
W16×50
$t_w = 0.380$ in.

From AISC *Specification* Table J3.3, for ¾-in.-diameter bolts with standard holes:

$$d_h = \frac{13}{16} \text{ in.}$$

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(8 \text{ kips}) + 1.6(24 \text{ kips})$ | $R_a = 8 \text{ kips} + 24 \text{ kips}$ |
| $= 48.0$ kips | $= 32.0$ kips |

*Strength of the Welded Connection—Plate*

Because the splice is unsymmetrical and the weld group is more rigid, it will be designed for the full moment from the eccentric shear.

Use a PL⅜ in.×8 in.×1 ft 0 in.

Use AISC *Manual* Table 8-8 to determine the weld size.

$$k = \frac{kl}{l}$$
$$= \frac{3½ \text{ in.}}{12 \text{ in.}}$$
$$= 0.292$$

Interpolating from AISC *Manual* Table 8-8, with Angle = 0°, and $k = 0.292$:

$$x = 0.0538$$

$$xl = (0.0538)(12 \text{ in.})$$
$$= 0.646 \text{ in.}$$

$$e_x = al$$
$$= 6.50 \text{ in.} - 0.646 \text{ in.}$$
$$= 5.85 \text{ in.}$$

$$a = \frac{al}{l}$$
$$= \frac{5.85 \text{ in.}}{12 \text{ in.}}$$
$$= 0.488$$

By interpolating AISC *Manual* Table 8-8, with Angle = 0°:

$$C = 2.15$$

---

# IIA-238

From AISC *Manual* Equation 8-30, with $C_1 = 1.00$ from AISC *Manual* Table 8-3, the required weld size is determined as follows:

| LRFD | ASD |
|------|-----|
| $D_{min} = \frac{R_u}{\phi CC_1l}$ | $D_{min} = \frac{\Omega R_a}{CC_1l}$ |
|  |  |
| $= \frac{48.0 \text{ kips}}{0.75(2.15)(1.00)(12 \text{ in.})}$ | $= \frac{(2.00)(32.0 \text{ kips})}{2.15(1.00)(12 \text{ in.})}$ |
| $= 2.48 \rightarrow 3 \text{ sixteenths}$ | $= 2.48 \rightarrow 3 \text{ sixteenths}$ |

The minimum required weld size from AISC *Specification* Table J2.4 is $\frac{3}{16}$ in.

Use a $\frac{3}{16}$ in. fillet weld.

*Shear Rupture of W16×31 Beam Web at Weld*

For fillet welds with $F_{EXX} = 70$ ksi on one side of the connection, the minimum thickness required to match the available shear rupture strength of the connection element to the available shear rupture strength of the base metal is:

$$t_{min} = \frac{3.09D}{F_u}$$ (*Manual* Eq. 9-6)
$$= \frac{3.09(2.48)}{65 \text{ ksi}}$$
$$= 0.118 \text{ in.} < 0.275 \text{ in.} \quad \textbf{o.k.}$$

*Strength of the Bolted Connection—Plate*

From the User Note in AISC *Specification* Section J3.7, the strength of the bolt group is taken as the sum of the individual strengths of the individual fasteners, which may be taken as the lesser of the fastener shear strength per AISC *Specification* Section J3.7, the bearing strength at the bolt hole per AISC *Specification* Section J3.11a, or the tearout strength at the bolt hole per AISC *Specification* Section J3.11a.

From AISC *Manual* Table 7-1, the available shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9$ kips/bolt | $\frac{r_n}{\Omega} = 11.9$ kips/bolt |

The available bearing strength of the plate per bolt is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration:

$$r_n = 2.4dtF_u$$ (from *Spec.* Eq. J3-6a)
$$= (2.4)(¾ \text{ in.})(⅜ \text{ in.})(65 \text{ ksi})$$
$$= 43.9 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(43.9 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{43.9 \text{ kips/bolt}}{2.00}$ |
| $= 32.9$ kips/bolt | $= 22.0$ kips/bolt |

---

# IIA-239

The available tearout strength of the plate per bolt is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration. Note: The available tearout strength based on edge distance will conservatively be used for all of the bolts.

$$l_c = l_{ev} - 0.5(d_h)$$
$$= 1½ \text{ in.} - 0.5(\frac{13}{16} \text{ in.})$$
$$= 1.09 \text{ in.}$$

$$r_n = 1.2l_ctF_u$$ (from *Spec.* Eq. J3-6c)
$$= 1.2(1.09 \text{ in.})(⅜ \text{ in.})(65 \text{ ksi})$$
$$= 31.9 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(31.9 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{31.9 \text{ kips/bolt}}{2.00}$ |
| $= 23.9$ kips/bolt | $= 16.0$ kips/bolt |

The bolt shear strength controls for bolts in the plate.

Because the weld group is designed for the full eccentric moment, the bolt group is designed for shear only.

| LRFD | ASD |
|------|-----|
| $n_{min} = \frac{R_u}{\phi r_n}$ | $n_{min} = \frac{R_a}{r_n/\Omega}$ |
|  |  |
| $= \frac{48.0 \text{ kips}}{17.9 \text{ kips/bolt}}$ | $= \frac{32.0 \text{ kips}}{11.9 \text{ kips/bolt}}$ |
| $= 2.68 \text{ bolts} < 4 \text{ bolts} \quad \textbf{o.k.}$ | $= 2.69 \text{ bolts} < 4 \text{ bolts} \quad \textbf{o.k.}$ |

*Strength of the Bolted Connection—Beam Web*

By inspection, bearing and tearout on the W16×50 beam web will not govern because the web is thicker than the plate.

*Flexural Yielding of Plate*

The required flexural strength of the plate is determined as follows:

| LRFD | ASD |
|------|-----|
| $M_u = R_u e_x$ | $M_a = R_a e_x$ |
| $= (48.0 \text{ kips})(5.85 \text{ in.})$ | $= (32.0 \text{ kips})(5.85 \text{ in.})$ |
| $= 281$ kip-in. | $= 187$ kip-in. |

The available flexural strength of the plate is determined as follows:

---

# IIA-240

$$M_n = F_y Z_x$$
$$= (50\text{ksi})\left[\frac{(⅜ \text{ in.})(12 \text{ in.})^2}{4}\right]$$
$$= 675 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
|  |  |
| $\phi_b M_n = 0.90(675 \text{ kip-in.})$ | $\frac{M_n}{\Omega_b} = \frac{675 \text{ kip-in.}}{1.67}$ |
| $= 608 \text{ kip-in.} > 281 \text{ kip-in.} \quad \textbf{o.k.}$ | $= 404 \text{ kip-in.} > 187 \text{ kip-in.} \quad \textbf{o.k.}$ |

*Flexural Rupture of Plate*

The net plastic section modulus of the plate, $Z_{net}$, is determined from AISC *Manual* Table 15-2:

$$Z_{net} = 9.56 \text{ in.}^3$$

$$M_n = F_u Z_{net}$$ (*Manual* Eq. 9-8)
$$= (65 \text{ ksi})(9.56 \text{ in.}^3)$$
$$= 621 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.75$ | $\Omega_b = 2.00$ |
|  |  |
| $\phi_b M_n = 0.75(621 \text{ kip-in.})$ | $\phi M_n = \frac{621 \text{ kip-in.}}{2.00}$ |
| $= 466 \text{ kip-in.} > 281 \text{ kip-in.} \quad \textbf{o.k.}$ | $= 311 \text{ kip-in.} > 187 \text{ kip-in.} \quad \textbf{o.k.}$ |

*Shear Strength of Plate*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the plate is determined as follows:

$$A_{gv} = lt$$
$$= (12 \text{ in.})(⅜ \text{ in.})$$
$$= 4.50 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(4.50 \text{ in.}^2)$$
$$= 135 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(135 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{135 \text{ kips}}{1.50}$ |
| $= 135 \text{ kips} > 48.0 \text{ kips} \quad \textbf{o.k.}$ | $= 90.0 \text{ kips} > 32.0 \text{ kips} \quad \textbf{o.k.}$ |

---

# IIA-241

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the plate is determined using the net area determined in accordance with AISC *Specification* Section B4.3b.

$$A_{nv} = \left[d - n(d_h + \frac{1}{16} \text{ in.})\right]t$$
$$= \left[12 \text{ in.} - 4(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.})\right](⅜ \text{ in.})$$
$$= 3.19 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(3.19 \text{ in.}^2)$$
$$= 124 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(124 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{124 \text{ kips}}{2.00}$ |
| $= 93.0 \text{ kips} > 48.0 \text{ kips} \quad \textbf{o.k.}$ | $= 62.0 \text{ kips} > 32.0 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture of Plate*

The nominal strength for the limit state of block shear rupture is given by AISC *Specification* Section J4.3.

$$R_n = 0.60F_u A_{nv} + U_{bs} F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs} F_u A_{nt}$$ (*Spec.* Eq. J4-5)

The available block shear rupture strength of the plate is determined as follows, using AISC *Manual* Tables 9-3a, 9-3b, and 9-3c, and AISC *Specification* Equation J4-5, with $n = 4$, $l_{eh} = l_{ev} = 1½$ in., and $U_{bs} = 1.0$.

| LRFD | ASD |
|------|-----|
| Tension rupture component from AISC *Manual* Table 9-3a: | Tension rupture component from AISC *Manual* Table 9-3a: |
|  |  |
| $\frac{\phi F_u A_{nt}}{t} = 51.8$ kips/in. | $\frac{F_u A_{nt}}{\Omega t} = 34.5$ kips/in. |
|  |  |
| Shear yielding component from AISC *Manual* Table 9-3b: | Shear yielding component from AISC *Manual* Table 9-3b: |
|  |  |
| $\frac{\phi 0.60F_y A_{gv}}{t} = 236$ kips/in. | $\frac{0.60F_y A_{gv}}{\Omega t} = 158$ kips/in. |
|  |  |
| Shear rupture component from AISC *Manual* Table 9-3c: | Shear rupture component from AISC *Manual* Table 9-3c: |
|  |  |
| $\frac{\phi 0.60F_u A_{nv}}{t} = 218$ kips/in. | $\frac{0.60F_u A_{nv}}{\Omega t} = 145$ kips/in. |

---

# IIA-242

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi 0.60F_u A_{nv} + \phi U_{bs} F_u A_{nt}$ | $\frac{R_n}{\Omega} = \frac{0.60F_u A_{nv}}{\Omega} + \frac{U_{bs} F_u A_{nt}}{\Omega}$ |
| $\leq \phi 0.60F_y A_{gv} + \phi U_{bs} F_u A_{nt}$ | $\leq \frac{0.60F_y A_{gv}}{\Omega} + \frac{U_{bs} F_u A_{nt}}{\Omega}$ |
|  |  |
| $= (⅜ \text{ in.})\left[218 \text{ kips/in.} + (1.0)(51.8 \text{ kips/in.})\right]$ | $= (⅜ \text{ in.})\left[145 \text{ kips/in.} + (1.0)(34.5 \text{ kips/in.})\right]$ |
| $\leq (⅜ \text{ in.})\left[236 \text{ kips/in.} + (1.0)(51.8 \text{ kips/in.})\right]$ | $\leq (⅜ \text{ in.})\left[158 \text{ kips/in.} + (1.0)(34.5 \text{ kips/in.})\right]$ |
| $= 101 \text{ kips} < 108 \text{ kips}$ | $= 67.3 \text{ kips} < 72.2 \text{ kips}$ |
|  |  |
| Therefore: | Therefore: |
|  |  |
| $\phi R_n = 101 \text{ kips} > 48.0 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 67.3 \text{ kips} > 32.0 \text{ kips} \quad \textbf{o.k.}$ |

*Conclusion*

The connection is found to be adequate as given for the applied force.

---

# IIA-243

## EXAMPLE II.A-22 BOLTED BRACKET PLATE DESIGN

**Given:**

Verify that the bracket plate is adequate to support the loads as shown in Figure II.A-22-1 (loads are per bracket plate). Use ASTM A572/A572M Grade 50 plate. Assume the column has sufficient available strength for the connection.

![Bracket plate connection diagram showing a shaped plate bolted to a column with ¾" dia. Group 120 bolts in standard holes. The plate is (2)PL⅜×23×1'-8" shaped with dimensions: e = 9¼" horizontal distance, 1'-0" total width, 2¾" edge margin, 2⅛" spacing. Vertical dimensions show 5@3"=15" for 6 bolts arranged in two columns, with 2½" edge distances. Applied loads are PD = 6 kips and PL = 18 kips. The diagram includes force vectors showing θ angle, and components Vr, Mr, Nr at point A. Section A-A is indicated, and dimensions b = 15¼" and 5½" spacing are shown. The 2¼" dimension is also marked.]

*Fig. II.A-22-1. Connection geometry for Example II.A-22.*

**Solution:**

For discussion of the design of a bracket plate, see AISC *Manual* Part 15.

From AISC *Manual* Table 2-5, the material properties are as follows:

Plate
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(6 \text{ kips}) + 1.6(18 \text{ kips})$ | $P_a = 6 \text{ kips} + 18 \text{ kips}$ |
| $= 36.0$ kips | $= 24.0$ kips |

---

# IIA-244

From the geometry shown in Figure II.A-22-1 and AISC *Manual* Figure 15-2(a):

$$a = 20 \text{ in.}$$
$$b = 15¼ \text{ in.}$$
$$e = 9¼ \text{ in.}$$

$$\theta = \tan^{-1}\left(\frac{b}{a}\right)$$
$$= \tan^{-1}\left(\frac{15¼ \text{ in.}}{20 \text{ in.}}\right)$$
$$= 37.3°$$

$$a' = \frac{a}{\cos \theta}$$ (*Manual* Eq. 15-17)
$$= \frac{20 \text{ in.}}{\cos 37.3°}$$
$$= 25.1 \text{ in.}$$

$$b' = a \sin \theta$$
$$= (20 \text{ in.})(\sin 37.3°)$$
$$= 12.1 \text{ in.}$$

*Strength of the Bolted Connection—Plate*

From the User Note in AISC *Specification* Section J3.7, the strength of the bolt group is taken as the sum of the individual strengths of the individual fasteners, which may be taken as the lesser of the fastener shear strength per AISC *Specification* Section J3.7, the bearing strength at the bolt hole per AISC *Specification* Section J3.11a, or the tearout strength at the bolt hole per AISC *Specification* Section J3.11a.

From AISC *Manual* Table 7-1, the available shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9$ kips/bolt | $\frac{r_n}{\Omega} = 11.9$ kips/bolt |

The available bearing and tearout strength of the plate is determined using AISC *Manual* Table 7-5 conservatively using $l_c = 2$ in. Note: The available bearing and tearout strength based on edge distance will conservatively be used for all of the bolts.

| LRFD | ASD |
|------|-----|
| $\phi r_n = (87.8 \text{ kips/in.})(⅜ \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(⅜ \text{ in.})$ |
| $= 32.9$ kips/bolt | $= 21.9$ kips/bolt |

Bolt shear strength controls for bolts in the plate.

The strength of the bolt group is determined by interpolating AISC *Manual* Table 7-8 with Angle = 0°, a $5½$ in. gage with $s = 3$ in., $e_x = 12$ in., and $n = 6$:

$$C = 4.53$$

---

# IIA-245

| LRFD | ASD |
|------|-----|
| $C_{min} = \frac{P_u}{\phi r_n}$ | $C_{min} = \frac{\Omega P_a}{r_n}$ |
|  |  |
| $= \frac{36.0 \text{ kips}}{17.9 \text{ kips/bolt}}$ | $= \frac{24.0 \text{ kips}}{11.9 \text{ kips/bolt}}$ |
| $= 2.01 < 4.53 \quad \textbf{o.k.}$ | $= 2.02 < 4.53 \quad \textbf{o.k.}$ |

*Flexural Yielding of Bracket Plate on Section A-A (see Figure II.A-22-1)*

The required flexural yielding strength of the plate at Section A-A is determined from AISC *Manual* Equation 15-1 as follows:

| LRFD | ASD |
|------|-----|
| $M_u = P_u e$ | $M_a = P_a e$ |
| $= (36.0 \text{ kips})(9¼ \text{ in.})$ | $= (24.0 \text{ kips})(9¼ \text{ in.})$ |
| $= 333$ kip-in. | $= 222$ kip-in. |

The available flexural yielding strength of the bracket plate is determined as follows:

$$M_n = F_y Z$$ (*Manual* Eq. 15-2)
$$= (50 \text{ ksi})\left[\frac{(⅜ \text{ in.})(20 \text{ in.})^2}{4}\right]$$
$$= 1,880 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi M_n = 0.90(1,880 \text{ kip-in.})$ | $\frac{M_n}{\Omega} = \frac{1,880 \text{ kip-in.}}{1.67}$ |
| $= 1,690 \text{ kip-in.} > 333 \text{ kip-in.} \quad \textbf{o.k.}$ | $= 1,130 \text{ kip-in.} > 222 \text{ kip-in.} \quad \textbf{o.k.}$ |

*Flexural Rupture of Bracket Plate on Section A-A (see Figure II.A-22-1)*

From AISC *Manual* Table 15-2, for a ⅜-in.-thick bracket plate, with ¾ in. bolts and six bolts in a row, $Z_{net} = 21.5 \text{ in.}^3$ Note that AISC *Manual* Table 15-2 conservatively considers $l_{ev} = 1½$ in. for holes spaced at 3 in.

The available flexural yielding rupture of the bracket plate at Section A-A is determined as follows:

$$M_n = F_u Z_{net}$$ (*Manual* Eq. 15-3)
$$= (65 \text{ ksi})(21.5 \text{ in.}^3)$$
$$= 1,400 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi M_n = 0.75(1,400 \text{ kip-in.})$ | $\frac{M_n}{\Omega} = \frac{1,400 \text{ kip-in.}}{2.00}$ |
| $= 1,050 \text{ kip-in.} > 333 \text{ kip-in.} \quad \textbf{o.k.}$ | $= 700 \text{ kip-in.} > 222 \text{ kip-in.} \quad \textbf{o.k.}$ |

---

# IIA-246

*Shear Yielding of Bracket Plate on Section B-B (see Figure II.A-22-1)*

The required shear strength of the bracket plate on Section B-B is determined from AISC *Manual* Equation 15-6a or 15-6b as follows:

| LRFD | ASD |
|------|-----|
| $V_u = P_u \sin \theta$ | $V_a = P_a \sin \theta$ |
| $= (36.0 \text{ kips})(\sin 37.3°)$ | $= (24.0 \text{ kips})(\sin 37.3°)$ |
| $= 21.8$ kips | $= 14.5$ kips |

The available shear yielding strength of the plate is determined as follows:

$$V_n = 0.60F_y tb'$$ (*Manual* Eq. 15-7)
$$= 0.60(50 \text{ ksi})(⅜ \text{ in.})(12.1 \text{ in.})$$
$$= 136 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi V_n = 1.00(136 \text{ kips})$ | $\frac{V_n}{\Omega} = \frac{136 \text{ kips}}{1.50}$ |
| $= 136 \text{ kips} > 21.8 \text{ kips} \quad \textbf{o.k.}$ | $= 90.7 \text{ kips} > 14.5 \text{ kips} \quad \textbf{o.k.}$ |

*Local Yielding and Local Buckling of Bracket Plate on Section B-B (see Figure II.A-22-1)*

For local yielding:

$$F_{cr} = F_y$$ (*Manual* Eq. 15-13)
$$= 50 \text{ ksi}$$

For local buckling:

$$F_{cr} = QF_y$$ (*Manual* Eq. 15-14)

where

$$\lambda = \frac{\left(\frac{b'}{t}\right)\sqrt{F_y}}{5\sqrt{475 + 1,120\left(\frac{b'}{a'}\right)^2}}$$ (*Manual* Eq. 15-18)
$$= \frac{\left(\frac{12.1 \text{ in.}}{⅜ \text{ in.}}\right)\sqrt{50 \text{ ksi}}}{5\sqrt{475 + 1,120\left(\frac{12.1 \text{ in.}}{25.1 \text{ in.}}\right)^2}}$$
$$= 1.68$$

Because $1.41 < \lambda$:

---

# IIA-247

$$Q = \frac{1.30}{\lambda^2}$$ (*Manual* Eq. 15-16)
$$= \frac{1.30}{(1.68)^2}$$
$$= 0.461$$

$$F_{cr} = QF_y$$ (*Manual* Eq. 15-14)
$$= 0.461(50 \text{ ksi})$$
$$= 23.1 \text{ ksi}$$

Local buckling controls over local yielding.

*Interaction of Normal and Flexural Strengths on Section B-B (see Figure II.A-22-1)*

Check that AISC *Manual* Equation 15-10 is satisfied:

| LRFD | ASD |
|------|-----|
| $N_u = P_u \cos \theta$ (*Manual* Eq. 15-9) | $N_a = P_a \cos \theta$ (*Manual* Eq. 15-9) |
| $= (36.0 \text{ kips})(\cos 37.3°)$ | $= (24.0 \text{ kips})(\cos 37.3°)$ |
| $= 28.6$ kips | $= 19.1$ kips |
|  |  |
| $N_n = F_{cr}tb'$ (*Manual* Eq. 15-11) | $N_n = F_{cr}tb'$ (*Manual* Eq. 15-11) |
| $= (23.1 \text{ ksi})(⅜ \text{ in.})(12.1 \text{ in.})$ | $= (23.1 \text{ ksi})(⅜ \text{ in.})(12.1 \text{ in.})$ |
| $= 105$ kips | $= 105$ kips |
|  |  |
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $N_c = \phi N_n$ | $N_c = \frac{N_n}{\Omega}$ |
| $= 0.90(105 \text{ kips})$ | $= \frac{105 \text{ kips}}{1.67}$ |
| $= 94.5$ kips | $= 62.9$ kips |
|  |  |
| $M_u = P_u e - N_u \left(\frac{b'}{2}\right)$ (*Manual* Eq. 15-8) | $M_a = P_a e - N_a \left(\frac{b'}{2}\right)$ (*Manual* Eq. 15-8) |
|  |  |
| $= (36.0 \text{ kips})(9¼ \text{ in.}) - (28.6 \text{ kips})\left(\frac{12.1 \text{ in.}}{2}\right)$ | $= (24.0 \text{ kips})(9¼ \text{ in.}) - (19.1 \text{ kips})\left(\frac{12.1 \text{ in.}}{2}\right)$ |
| $= 160$ kip-in. | $= 106$ kip-in. |
|  |  |
| $M_n = \frac{F_{cr}tb'^2}{4}$ (*Manual* Eq. 15-12) | $M_n = \frac{F_{cr}tb'^2}{4}$ (*Manual* Eq. 15-12) |
|  |  |
| $= \frac{(23.1 \text{ ksi})(⅜ \text{ in.})(12.1 \text{ in.})^2}{4}$ | $= \frac{(23.1 \text{ ksi})(⅜ \text{ in.})(12.1 \text{ in.})^2}{4}$ |
| $= 317$ kip-in. | $= 317$ kip-in. |

---

# IIA-248

| LRFD | ASD |
|------|-----|
| $M_c = \phi M_n$ | $M_c = \frac{M_n}{\Omega}$ |
| $= 0.90(317 \text{ kip-in.})$ | $= \frac{317 \text{ kip-in.}}{1.67}$ |
| $= 285$ kip-in. | $= 190$ kip-in. |
|  |  |
| $\frac{N_r}{N_c} + \frac{M_r}{M_c} \leq 1.0$ (*Manual* Eq. 15-10) | $\frac{N_r}{N_c} + \frac{M_r}{M_c} \leq 1.0$ (*Manual* Eq. 15-10) |
|  |  |
| $\frac{28.6 \text{ kips}}{94.5 \text{ kips}} + \frac{160 \text{ kip-in.}}{285 \text{ kip-in.}} = 0.864 < 1.0 \quad \textbf{o.k.}$ | $\frac{19.1 \text{ kips}}{62.9 \text{ kips}} + \frac{106 \text{ kip-in.}}{190 \text{ kip-in.}} = 0.862 < 1.0 \quad \textbf{o.k.}$ |

*Shear Strength of Bracket Plate on Section A-A (see Figure II.A-22-1)*

From AISC *Specification* Section J4.2, the available shear yielding strength of the plate on Section A-A is determined as follows:

$$A_{gv} = at$$
$$= (20 \text{ in.})(⅜ \text{ in.})$$
$$= 7.50 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(7.50 \text{ in.}^2)$$
$$= 225 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(225 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{225 \text{ kips}}{1.50}$ |
| $= 225 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ | $= 150 \text{ kips} > 24.0 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.2, the available shear rupture strength of the plate on Section A-A is determined as follows:

$$A_{nv} = \left[a - n(d_h + \frac{1}{16} \text{ in.})\right]t$$
$$= \left[20 \text{ in.} - 6(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.})\right](⅜ \text{ in.})$$
$$= 5.53 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(5.53 \text{ in.}^2)$$
$$= 216 \text{ kips}$$

---

# IIA-249

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(216 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{216 \text{ kips}}{2.00}$ |
| $= 162 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ | $= 108 \text{ kips} > 24.0 \text{ kips} \quad \textbf{o.k.}$ |

*Conclusion*

The connection is found to be adequate as given for the applied force.

---

# IIA-250

## EXAMPLE II.A-23 WELDED BRACKET PLATE DESIGN

**Given:**

Verify that the welded bracket plate is adequate to support the loads as shown in Figure II.A-23-1 (loads are resisted equally by the two bracket plates). Use ASTM A572/A572M Grade 50 plate and 70-ksi electrodes. Assume the column has sufficient available strength for the connection.

![Welded bracket connection diagram showing a shaped plate welded to column W14×90. The plate is (2)PL⅜×14½×1'-6" shaped with dimensions: e = 8½" horizontal distance, 7⅞" spacing, applied loads PD = 9 kips and PL = 27 kips. Vertical dimension shows a = 18" total height. The diagram includes force vectors showing θ angle, and components Vr, Mr, Nr at point A. Dimensions b = 11½" and 14½" total width are shown, with 3" and 3⅞" spacing from edges. A "3" return, top and bottom" note indicates ⅜" fillet weld returns. Section A-A is marked. The min. clearance is shown on the left side of the column.]

*Fig. II.A-23-1. Connection geometry for Example II.A-23.*

**Solution:**

From AISC *Manual* Table 2-5, the material properties are as follows:

Plate
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From ASCE/SEI 7, Chapter 2, the required strength to be resisted by the bracket plates is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(9 \text{ kips}) + 1.6(27 \text{ kips})$ | $P_a = 9 \text{ kips} + 27 \text{ kips}$ |
| $= 54.0$ kips | $= 36.0$ kips |

---

# IIA-251

From the geometry shown in Figure II.A-23-1 and AISC *Manual* Figure 15-2(b):

$a = 18$ in.
$b = 11½$ in.
$e = 8¼$ in.

$$\theta = \tan^{-1}\left(\frac{b}{a}\right)$$
$$= \tan^{-1}\left(\frac{11½ \text{ in.}}{18 \text{ in.}}\right)$$
$$= 32.6°$$

$$a' = \frac{a}{\cos \theta}$$ (*Manual* Eq. 15-17)
$$= \frac{18 \text{ in.}}{\cos 32.6°}$$
$$= 21.4 \text{ in.}$$

$$b' = a \sin \theta$$
$$= (18 \text{ in.})(\sin 32.6°)$$
$$= 9.70 \text{ in.}$$

*Shear Yielding of Bracket Plate at Section A-A (see Figure II.A-23-1)*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the bracket plate at Section A-A is determined as follows:

$$A_{gv} = (2 \text{ plates})at$$
$$= (2 \text{ plates})(18 \text{ in.})(⅜ \text{ in.})$$
$$= 13.5 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(13.5 \text{ in.}^2)$$
$$= 405 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(405 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{405 \text{ kips}}{1.50}$ |
| $= 405 \text{ kips} > 54.0 \text{ kips} \quad \textbf{o.k.}$ | $= 270 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ |

Shear rupture strength is adequate by inspection.

*Flexural Yielding of Bracket Plate at Section A-A (see Figure II.A-23-1)*

The required flexural strength of the bracket plate is determined using AISC *Manual* Equation 15-1 as follows:

---

# IIA-252

| LRFD | ASD |
|------|-----|
| $M_u = P_u e$ | $M_a = P_a e$ |
| $= (54.0 \text{ kips})(8¼ \text{ in.})$ | $= (36.0 \text{ kips})(8¼ \text{ in.})$ |
| $= 446$ kip-in. | $= 297$ kip-in. |

The available flexural strength of the bracket plate is determined using AISC *Manual* Equation 15-2, as follows:

$$M_n = (2 \text{ plates})F_y Z$$ (from *Manual* Eq. 15-2)
$$= (2 \text{ plates})(50 \text{ ksi})\left[\frac{(⅜ \text{ in.})(18 \text{ in.})^2}{4}\right]$$
$$= 3,040 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi M_n = 0.90(3,040 \text{ kip-in.})$ | $\frac{M_n}{\Omega} = \frac{3,040 \text{ kip-in.}}{1.67}$ |
| $= 2,740 \text{ kip-in.} > 446 \text{ kip-in.} \quad \textbf{o.k.}$ | $= 1,820 \text{ kip-in.} > 297 \text{ kip-in.} \quad \textbf{o.k.}$ |

*Weld Strength*

Try a C-shaped weld with $kl = 3$ in. and $l = 18$ in.

$$k = \frac{kl}{l}$$
$$= \frac{3 \text{ in.}}{18 \text{ in.}}$$
$$= 0.167$$

$$xl = \frac{(kl)^2}{2(kl) + l}$$
$$= \frac{(3 \text{ in.})^2}{2(3 \text{ in.}) + 18 \text{ in.}}$$
$$= 0.375 \text{ in.}$$

$$al = 11¼ \text{ in.} - 0.375 \text{ in.}$$
$$= 10.9 \text{ in.}$$

$$a = \frac{al}{l}$$
$$= \frac{10.9 \text{ in.}}{18 \text{ in.}}$$
$$= 0.606$$

Interpolate AISC *Manual* Table 8-8 using Angle = 0°, $k = 0.167$, and $a = 0.606$.

$C = 1.46$

---

# IIA-253

From AISC *Manual* Table 8-3:

$C_1 = 1.00$ (for E70 electrodes)

The required weld size is determined using AISC *Manual* Equation 8-30 as follows:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $D_{min} = \frac{P_u}{\phi CC_1l}$ | $D_{min} = \frac{\Omega P_a}{CC_1l}$ |
|  |  |
| $= \frac{54.0 \text{ kips}}{0.75(1.46)(1.00)(18 \text{ in.})(2 \text{ plates})}$ | $= \frac{2.00(36.0 \text{ kips})}{(1.46)(1.00)(18 \text{ in.})(2 \text{ plates})}$ |
| $= 1.37 \rightarrow 3$ sixteenths | $= 1.37 \rightarrow 3$ sixteenths |

From AISC *Specification* Section J2.2b(b)(2), the maximum weld size is:

$$w_{max} = ⅜ \text{ in.} - \frac{1}{16} \text{ in.}$$
$$= \frac{5}{16} \text{ in.} > \frac{3}{16} \text{ in.} \quad \textbf{o.k.}$$

From AISC *Specification* Table J2.4, the minimum weld size is:

$w_{min} = \frac{3}{16}$ in.

*Shear Yielding Strength of Bracket at Section B-B (see Figure II.A-23-1)*

The required shear strength of the bracket plate at Section B-B is determined from AISC *Manual* Equation 15-6 as follows:

| LRFD | ASD |
|------|-----|
| $V_u = P_u \sin \theta$ | $V_a = P_a \sin \theta$ |
| $= (54.0 \text{ kips})(\sin 32.6°)$ | $= (36.0 \text{ kips})(\sin 32.6°)$ |
| $= 29.1$ kips | $= 19.4$ kips |

From AISC *Manual* Part 15, the available shear yielding strength of the bracket plate at Section B-B is determined as follows:

$$V_n = (2 \text{ plates})0.60F_y tb'$$ (from *Manual* Eq. 15-7)
$$= (2 \text{ plates})(0.60)(50 \text{ ksi})(⅜ \text{ in.})(9.70 \text{ in.})$$
$$= 218 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi V_n = 1.00(218 \text{ kips})$ | $\frac{V_n}{\Omega} = \frac{218 \text{ kips}}{1.50}$ |
| $= 218 \text{ kips} > 29.1 \text{ kips} \quad \textbf{o.k.}$ | $= 145 \text{ kips} > 19.4 \text{ kips} \quad \textbf{o.k.}$ |

---

# IIA-254

*Bracket Plate Normal and Flexural Strength at Section B-B (see Figure II.A-23-1)*

From AISC *Manual* Part 15, the required strength of the bracket plate at Section B-B is determined as follows:

| LRFD | ASD |
|------|-----|
| $N_u = P_u \cos \theta$ (*Manual* Eq. 15-9) | $N_a = P_a \cos \theta$ (*Manual* Eq. 15-9) |
| $= (54.0 \text{ kips})(\cos 32.6°)$ | $= (36.0 \text{ kips})(\cos 32.6°)$ |
| $= 45.5$ kips | $= 30.3$ kips |
|  |  |
| $M_u = P_u e - N_u \left(\frac{b'}{2}\right)$ (*Manual* Eq. 15-8) | $M_a = P_a e - N_a \left(\frac{b'}{2}\right)$ (*Manual* Eq. 15-8) |
|  |  |
| $= (54.0 \text{ kips})(8¼ \text{ in.}) - (45.5 \text{ kips})\left(\frac{9.70 \text{ in.}}{2}\right)$ | $= (36.0 \text{ kips})(8¼ \text{ in.}) - (30.3 \text{ kips})\left(\frac{9.70 \text{ in.}}{2}\right)$ |
| $= 225$ kip-in. | $= 150$ kip-in. |

For local yielding at the bracket plate:

$$F_{cr} = F_y$$ (*Manual* Eq. 15-13)
$$= 50 \text{ ksi}$$

For local buckling of the bracket plate:

$$F_{cr} = QF_y$$ (*Manual* Eq. 15-14)

where

$$\lambda = \frac{\left(\frac{b'}{t}\right)\sqrt{F_y}}{5\sqrt{475 + 1,120\left(\frac{b'}{a'}\right)^2}}$$ (*Manual* Eq. 15-18)

$$= \frac{\left(\frac{9.70 \text{ in.}}{⅜ \text{ in.}}\right)\sqrt{50 \text{ ksi}}}{5\sqrt{475 + 1,120\left(\frac{9.70 \text{ in.}}{21.4 \text{ in.}}\right)^2}}$$

$$= 1.38$$

Because $0.70 < \lambda \leq 1.41$:

$$Q = 1.34 - 0.486\lambda$$ (*Manual* Eq. 15-15)
$$= 1.34 - 0.486(1.38)$$
$$= 0.669$$

$$F_{cr} = QF_y$$ (*Manual* Eq. 15-14)
$$= 0.669(50 \text{ ksi})$$
$$= 33.5 \text{ ksi}$$

Therefore; local buckling governs over yielding.

---

# IIA-255

The nominal strength of the bracket plate for the limit states of local yielding and local buckling is:

$$N_n = (2 \text{ plates})F_{cr}tb'$$ (from *Manual* Eq. 15-11)
$$= (2 \text{ plates})(33.5 \text{ ksi})(⅜ \text{ in.})(9.70 \text{ in.})$$
$$= 244 \text{ kips}$$

The nominal flexural strength of the bracket plate for the limit states of local yielding and local buckling is:

$$M_n = (2 \text{ plates})\frac{F_{cr}tb'^2}{4}$$ (from *Manual* Eq. 15-12)
$$= (2 \text{ plates})\frac{(33.5 \text{ ksi})(⅜ \text{ in.})(9.70 \text{ in.})^2}{4}$$
$$= 591 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $M_r = M_u$ | $M_r = M_a$ |
| $= 225$ kip-in. | $= 150$ kip-in. |
|  |  |
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $M_c = \phi M_n$ | $M_c = \frac{M_n}{\Omega}$ |
| $= 0.90(591 \text{ kip-in.})$ | $= \frac{591 \text{ kip-in.}}{1.67}$ |
| $= 532 \text{ kip-in.} > 225 \text{ kip-in.} \quad \textbf{o.k.}$ | $= 354 \text{ kip-in.} > 150 \text{ kip-in.} \quad \textbf{o.k.}$ |
|  |  |
| $N_r = N_u$ | $N_r = N_a$ |
| $= 45.5$ kips | $= 30.3$ kips |
|  |  |
| $N_c = \phi N_n$ | $N_c = \frac{N_n}{\Omega}$ |
| $= 0.90(244 \text{ kips})$ | $= \frac{244 \text{ kips}}{1.67}$ |
| $= 220 \text{ kips} > 45.5 \text{ kips} \quad \textbf{o.k.}$ | $= 146 \text{ kips} > 30.3 \text{ kips} \quad \textbf{o.k.}$ |
|  |  |
| $\frac{N_r}{N_c} + \frac{M_r}{M_c} \leq 1.0$ (*Manual* Eq. 15-10) | $\frac{N_r}{N_c} + \frac{M_r}{M_c} \leq 1.0$ (*Manual* Eq. 15-10) |
|  |  |
| $\frac{45.5 \text{ kips}}{220 \text{ kips}} + \frac{225 \text{ kip-in.}}{532 \text{ kip-in.}} = 0.630 < 1.0 \quad \textbf{o.k.}$ | $\frac{30.3 \text{ kips}}{146 \text{ kips}} + \frac{150 \text{ kip-in.}}{354 \text{ kip-in.}} = 0.631 < 1.0 \quad \textbf{o.k.}$ |

*Conclusion*

The connection is found to be adequate as given for the applied force.

---

# IIA-256

## EXAMPLE II.A-24 ECCENTRICALLY LOADED BOLT GROUP (IC METHOD)

**Given:**

Use AISC *Manual* Table 7-8 to determine the largest eccentric force, acting vertically (0° angle) and at a 15° angle, that can be supported by the available shear strength of the bolts using the instantaneous center of rotation method. Assume that bolt shear controls over bearing and tearout.

**Solution A (θ = 0°):**

The load acting on the connection plate is vertical (θ = 0°), as shown in Figure II.A-24-1:

From AISC *Manual* Table 7-1, the available shear strength per bolt for ⅞-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) in single shear is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 24.3$ kips/bolt | $\frac{r_n}{\Omega} = 16.2$ kips/bolt |

The available strength of the bolt group is determined using AISC *Manual* Table 7-8, with Angle = 0° and a 5½ in. gage with $s = 3$ in., $e_x = 16$ in., and $n = 6$:

$C = 3.55$

| LRFD | ASD |
|------|-----|
| $\phi R_n = C\phi r_n$ (from *Manual* Eq. 7-15) | $\frac{R_n}{\Omega} = C\frac{r_n}{\Omega}$ (from *Manual* Eq. 7-15) |
| $= 3.55(24.3 \text{ kips/bolt})$ | $= 3.55(16.2 \text{ kips/bolt})$ |
| $= 86.3$ kips | $= 57.5$ kips |
|  |  |
| Thus, $P_u$ must be less than or equal to 86.3 kips. | Thus, $P_a$ must be less than or equal to 57.5 kips. |

![Connection diagram showing a PL⅞" plate with 6 bolts (⅞" dia. Group 120, thread condition N, std. holes) arranged vertically with 3" spacing (5 @ 3" = 15"). The bolts are positioned 1½" from vertical centerline in X-direction. Load Pr is applied at eccentricity e = 1'-4" from the bolt group centerline (CG). Horizontal dimensions show 2¾" spacing on each side totaling 5½". The diagram shows X-X and Y-Y centerlines.]

*Fig. II.A-24-1. Connection geometry for Example II.A-24—Solution A (θ = 0°).*

---

# IIA-257

Note: The eccentricity of the load significantly reduces the shear strength of the bolt group.

**Solution B (θ = 15°):**

The load acting on the connection plate is at an angle of 15° with respect to vertical (θ = 15°), as shown in Figure II.A-24-2:

$$e_x = 16 \text{ in.} - (7.5 \text{ in.})(\tan 15°)$$
$$= 14.0 \text{ in.}$$

The available strength of the bolt group is determined from AISC *Manual* Table 7-8, with Angle = 15° and a 5½ in. gage with $s = 3$ in., $e_x = 14.0$ in., and $n = 6$:

$C = 4.05$

| LRFD | ASD |
|------|-----|
| $\phi R_n = C\phi r_n$ (from *Manual* Eq. 7-15) | $\frac{R_n}{\Omega} = C\frac{r_n}{\Omega}$ (from *Manual* Eq. 7-15) |
| $= 4.05(24.3 \text{ kips/bolt})$ | $= 4.05(16.2 \text{ kips/bolt})$ |
| $= 98.4$ kips | $= 65.6$ kips |
|  |  |
| Thus, $P_u$ must be less than or equal to 98.4 kips. | Thus, $P_a$ must be less than or equal to 65.6 kips. |

![Connection diagram showing a PL⅞" plate with 6 bolts (⅞" dia. Group 120, thread condition N, std. holes) arranged vertically with 3" spacing (5 @ 3" = 15"). The bolts are positioned 1½" from vertical centerline. Load Pr is applied at 15° angle from vertical with horizontal eccentricity ex and total dimension 7⅛" from centerline. Horizontal dimensions show 1'-4" and 2¾" spacing on each side totaling 5½". The diagram shows X-X and Y-Y centerlines with CG marked.]

*Fig. II.A-24-2. Connection geometry for Example II.A-24—Solution B (θ = 15°).*

---

# IIA-258

## EXAMPLE II.A-25 ECCENTRICALLY LOADED BOLT GROUP (ELASTIC METHOD)

**Given:**

Determine the largest eccentric force that can be supported by the available shear strength of the bolts using the elastic method for θ = 0°, as shown in Figure II.A-25-1. Compare the result with that of Example II.A-24. Assume that bolt shear controls over bearing and tearout.

![Connection diagram showing a PL⅞" plate with 6 bolts (⅞" dia. Group 120, thread condition N, std. holes) arranged vertically with 3" spacing (5 @ 3" = 15"). The bolts are positioned 1½" from vertical centerline in X-direction. Load Pu or Pa is applied at eccentricity e = 1'-4" from the bolt group centerline (CG). Horizontal dimensions show 2¾" spacing on each side totaling 5½". The diagram shows X-X and Y-Y centerlines.]

*Fig. II.A-25-1. Connection geometry for Example II.A-25.*

**Solution:**

From AISC *Manual* Table 7-1, the available shear strength per bolt for ⅞-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) in single shear is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 24.3$ kips/bolt | $\frac{r_n}{\Omega} = 16.2$ kips/bolt |

The direct shear force per bolt is determined as follows:

| LRFD | ASD |
|------|-----|
| $r_{upx} = 0$ | $r_{apx} = 0$ |
|  |  |
| $r_{upy} = \frac{P_u}{n}$ (from *Manual* Eq. 7-2) | $r_{apy} = \frac{P_a}{n}$ (from *Manual* Eq. 7-2) |
|  |  |
| $= \frac{P_u}{12}$ | $= \frac{P_a}{12}$ |

Additional shear force due to eccentricity is determined as follows:

The polar moment of inertia of the bolt group is:

---

# IIA-259

$$I_x = \Sigma y^2$$
$$= 4(7.50 \text{ in.})^2 + 4(4.50 \text{ in.})^2 + 4(1.50 \text{ in.})^2$$
$$= 315 \text{ in.}^4/\text{in.}^2$$

$$I_y = \Sigma x^2$$
$$= 12(2.75 \text{ in.})^2$$
$$= 90.8 \text{ in.}^4/\text{in.}^2$$

$$I_p = I_x + I_y$$
$$= 315 \text{ in.}^4/\text{in.}^2 + 90.8 \text{ in.}^4/\text{in.}^2$$
$$= 406 \text{ in.}^4/\text{in.}^2$$

| LRFD | ASD |
|------|-----|
| $r_{unnx} = \frac{P_u e_x c_y}{I_p}$ (from *Manual* Eq. 7-6) | $r_{annx} = \frac{P_a e_x c_y}{I_p}$ (from *Manual* Eq. 7-6) |
|  |  |
| $= \frac{P_u (16.0 \text{ in.})(7.50 \text{ in.})}{406 \text{ in.}^4/\text{in.}^2}$ | $= \frac{P_a (16.0 \text{ in.})(7.50 \text{ in.})}{406 \text{ in.}^4/\text{in.}^2}$ |
| $= 0.296P_u$ | $= 0.296P_a$ |
|  |  |
| $r_{unny} = \frac{P_u e_x c_x}{I_p}$ (from *Manual* Eq. 7-7) | $r_{anny} = \frac{P_a e_x c_x}{I_p}$ (from *Manual* Eq. 7-7) |
|  |  |
| $= \frac{P_u (16.0 \text{ in.})(2.75 \text{ in.})}{406 \text{ in.}^4/\text{in.}^2}$ | $= \frac{P_a (16.0 \text{ in.})(2.75 \text{ in.})}{406 \text{ in.}^4/\text{in.}^2}$ |
| $= 0.108P_u$ | $= 0.108P_a$ |
|  |  |
| The resultant shear force is determined from AISC *Manual* Equation 7-8: | The resultant shear force is determined from AISC *Manual* Equation 7-8: |
|  |  |
| $r_u = \sqrt{(r_{upx} + r_{unnx})^2 + (r_{upy} + r_{unny})^2}$ | $r_a = \sqrt{(r_{apx} + r_{annx})^2 + (r_{apy} + r_{anny})^2}$ |
|  |  |
| $= \sqrt{(0 + 0.296P_u)^2 + \left(\frac{P_u}{12} + 0.108P_u\right)^2}$ | $= \sqrt{(0 + 0.296P_a)^2 + \left(\frac{P_a}{12} + 0.108P_a\right)^2}$ |
|  |  |
| $= 0.352P_u$ | $= 0.352P_a$ |
|  |  |
| Because $r_u$ must be less than or equal to the available strength: | Because $r_a$ must be less than or equal to the available strength: |
|  |  |
| $P_u \leq \frac{\phi r_n}{0.352}$ | $P_a \leq \frac{r_n/\Omega}{0.352}$ |
|  |  |
| $= \frac{24.3 \text{ kips/bolt}}{0.352}$ | $= \frac{16.2 \text{ kips/bolt}}{0.352}$ |
|  |  |
| $= 69.0$ kips | $= 46.0$ kips |

Note: The elastic method, shown here, is more conservative than the instantaneous center of rotation method, shown in Example II.A-24.

---

# IIA-260

## EXAMPLE II.A-26 ECCENTRICALLY LOADED WELD GROUP (IC METHOD)

**Given:**

Use AISC *Manual* Table 8-8 to determine the largest eccentric force, acting vertically and at a 75° angle, that can be supported by the available shear strength of the weld group, using the instantaneous center of rotation method. Use a ⅜ in. fillet weld and 70-ksi electrodes.

**Solution A (θ = 0°):**

Assume that the load is vertical (θ = 0°), as shown in Figure II.A-26-1.

$$k = \frac{kl}{l}$$
$$= \frac{5 \text{ in.}}{10 \text{ in.}}$$
$$= 0.500$$

$$xl = \frac{(kl)^2}{2(kl) + l}$$
$$= \frac{(5 \text{ in.})^2}{2(5 \text{ in.}) + 10 \text{ in.}}$$
$$= 1.25 \text{ in.}$$

$$xl + al = 10.0 \text{ in.}$$
$$1.25 \text{ in.} + a(10 \text{ in.}) = 10 \text{ in.}$$
$$a = 0.875$$

$$e_x = al$$
$$= 0.875(10 \text{ in.})$$
$$= 8.75 \text{ in.}$$

![C-shaped weld diagram showing a vertical weld of length l = 10" with a horizontal return kl = 5" at the top. The weld is positioned with xl = 1⅛" from the top edge and ex = al extending to the point of load application Pr on the right side. Total width is 10".]

*Fig. II.A-26-1. Weld geometry—Solution A (θ = 0°).*

---

# IIA-261

The available weld strength is determined using AISC *Manual* Equation 8-30 and interpolating AISC *Manual* Table 8-8, with Angle = 0°, $a = 0.875$, and $k = 0.5$:

$C = 1.88$

$C_1 = 1.00$ (from AISC *Manual* Table 8-3)

$$R_n = CC_1Dl$$ (*Manual* Eq. 8-30)
$$= 1.88(1.00)(6)(10 \text{ in.})$$
$$= 113 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\phi = 2.00$ |
|  |  |
| $\phi R_n = 0.75(113 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{113 \text{ kips}}{2.00}$ |
| $= 84.8$ kips | $= 56.5$ kips |
|  |  |
| Thus, $P_u$ must be less than or equal to 84.8 kips. | Thus, $P_a$ must be less than or equal to 56.5 kips. |

Note: The eccentricity of the load significantly reduces the shear strength of this weld group as compared to the concentrically loaded case.

**Solution B (θ = 75°):**

Assume that the load acts at the same point as in Solution A, but at an angle of 75° with respect to vertical (θ = 75°) as shown in Figure II.A-26-2.

As determined in Solution A:

$k = 0.500$
$a = 0.875$

![C-shaped weld diagram showing a vertical weld of length l = 10" with a horizontal return kl = 5" at the top. The weld is positioned with xl = 1⅛" from the top edge. Load Pr is applied at 75° angle from vertical at the point of load application on the right side, with ex = al extending from the weld.]

*Fig. II.A-26-2. Weld geometry—Solution B (θ = 75°).*

---

# IIA-262

The available weld strength is determined using AISC *Manual* Equation 8-30 and interpolating AISC *Manual* Table 8-8, with Angle = 75°, $a = 0.875$, and $k = 0.5$:

$C = 3.45$

$C_1 = 1.00$ (from AISC *Manual* Table 8-3)

$$R_n = CC_1Dl$$ (*Manual* Eq. 8-30)
$$= 3.45(1.00)(6)(10 \text{ in.})$$
$$= 207 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\phi = 2.00$ |
|  |  |
| $\phi R_n = 0.75(207 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{207 \text{ kips}}{2.00}$ |
| $= 155$ kips | $= 104$ kips |
|  |  |
| Thus, $P_u$ must be less than or equal to 155 kips. | Thus, $P_a$ must be less than or equal to 104 kips. |

---

# IIA-263

## EXAMPLE II.A-27 ECCENTRICALLY LOADED WELD GROUP (ELASTIC METHOD)

**Given:**

Using the elastic method, determine the largest eccentric force that can be supported by the available shear strength of the welds in the connection shown in Figure II.A-27-1. Compare the result with that of Example II.A-26. Use ⅜ in. fillet welds and 70-ksi electrodes.

![C-shaped weld diagram showing a vertical weld of length l = 10" with a horizontal return kl = 5" at the top (labeled as t₂). The weld is positioned with xl = 1⅛" from the top edge and ex = al extending to the point of load application Pr on the right side. Total width is 10".]

*Fig. II.A-27-1. Weld geometry for Example II.A-27.*

**Solution:**

From the weld geometry shown in Figure II.A-27-1 and AISC *Manual* Table 8-8:

$$k = \frac{kl}{l}$$
$$= \frac{5 \text{ in.}}{10 \text{ in.}}$$
$$= 0.500$$

$$xl = \frac{(kl)^2}{2(kl) + l}$$
$$= \frac{(5 \text{ in.})^2}{2(5 \text{ in.}) + 10 \text{ in.}}$$
$$= 1.25 \text{ in.}$$

$$xl + al = 10.0 \text{ in.}$$
$$1.25 \text{ in.} + a(10 \text{ in.}) = 10 \text{ in.}$$
$$a = 0.875$$

$$e_x = al$$
$$= 0.875(10 \text{ in.})$$
$$= 8.75 \text{ in.}$$

*Direct Shear Force Per Inch of Weld*

---

# IIA-264

| LRFD | ASD |
|------|-----|
| $r_{upx} = 0$ | $r_{apx} = 0$ |
|  |  |
| $r_{upy} = \frac{P_u}{l_{total}}$ (from *Manual* Eq. 8-11) | $r_{apy} = \frac{P_a}{l_{total}}$ (from *Manual* Eq. 8-11) |
|  |  |
| $= \frac{P_u}{20.0 \text{ in.}}$ | $= \frac{P_a}{20.0 \text{ in.}}$ |
|  |  |
| $= \frac{0.0500P_u}{\text{in.}}$ | $= \frac{0.0500P_a}{\text{in.}}$ |

*Additional Shear Force due to Eccentricity*

Determine the polar moment of inertia referring to AISC *Manual* Figure 8-7:

$$I_x = \frac{l^3}{12} + 2(kl)(y)^2$$
$$= \frac{(10 \text{ in.})^3}{12} + 2(5 \text{ in.})(5 \text{ in.})^2$$
$$= 333 \text{ in.}^4/\text{in.}$$

$$I_y = 2\left[\frac{(kl)^3}{12} + (kl)\left(\frac{kl}{2} - xl\right)^2\right] + l(xl)^2$$
$$= 2\left[\frac{(5 \text{ in.})^3}{12} + (5 \text{ in.})(2.50 \text{ in.} - 1¼ \text{ in.})^2\right] + (10 \text{ in.})(1¼ \text{ in.})^2$$
$$= 52.1 \text{ in.}^4/\text{in.}$$

$$I_p = I_x + I_y$$
$$= 333 \text{ in.}^4/\text{in.} + 52.1 \text{ in.}^4/\text{in.}$$
$$= 385 \text{ in.}^4/\text{in.}$$

| LRFD | ASD |
|------|-----|
| $r_{unnx} = \frac{P_u e_x c_y}{I_p}$ (from *Manual* Eq. 8-15) | $r_{annx} = \frac{P_a e_x c_y}{I_p}$ (from *Manual* Eq. 8-15) |
|  |  |
| $= \frac{P_u (8.75 \text{ in.})(5 \text{ in.})}{385 \text{ in.}^4/\text{in.}}$ | $= \frac{P_a (8.75 \text{ in.})(5 \text{ in.})}{385 \text{ in.}^4/\text{in.}}$ |
|  |  |
| $= \frac{0.114P_u}{\text{in.}}$ | $= \frac{0.114P_a}{\text{in.}}$ |

---

# IIA-265

| LRFD | ASD |
|------|-----|
| $r_{unny} = \frac{P_u e_x c_x}{I_p}$ (from *Manual* Eq. 8-16) | $r_{anny} = \frac{P_a e_x c_x}{I_p}$ (from *Manual* Eq. 8-16) |
|  |  |
| $= \frac{P_u (8.75 \text{ in.})(3.75 \text{ in.})}{385 \text{ in.}^4/\text{in.}}$ | $= \frac{P_a (8.75 \text{ in.})(3.75 \text{ in.})}{385 \text{ in.}^4/\text{in.}}$ |
|  |  |
| $= \frac{0.0852P_u}{\text{in.}}$ | $= \frac{0.0852P_a}{\text{in.}}$ |
|  |  |
| The resultant shear force is determined using AISC *Manual* Equation 8-17: | The resultant shear force is determined using AISC *Manual* Equation 8-17: |
|  |  |
| $r_u = \sqrt{(r_{upx} + r_{unnx})^2 + (r_{upy} + r_{unny})^2}$ | $r_a = \sqrt{(r_{apx} + r_{annx})^2 + (r_{apy} + r_{anny})^2}$ |
|  |  |
| $= \sqrt{\left(0 + \frac{0.114P_u}{\text{in.}}\right)^2 + \left(\frac{0.0500P_u}{\text{in.}} + \frac{0.0852P_u}{\text{in.}}\right)^2}$ | $= \sqrt{\left(0 + \frac{0.114P_a}{\text{in.}}\right)^2 + \left(\frac{0.0500P_a}{\text{in.}} + \frac{0.0852P_a}{\text{in.}}\right)^2}$ |
|  |  |
| $= \frac{0.177P_u}{\text{in.}}$ | $= \frac{0.177P_a}{\text{in.}}$ |
|  |  |
| Because $r_u$ must be less than or equal to the available strength: | Because $r_a$ must be less than or equal to the available strength: |
|  |  |
| $r_u = \frac{0.177P_u}{\text{in.}} \leq \phi r_n$ | $r_a = \frac{0.177P_a}{\text{in.}} \leq \frac{r_n}{\Omega}$ |
|  |  |
| Solving for $P_u$ and using AISC *Manual* Equation 8-2a: | Solving for $P_a$ and using AISC *Manual* Equation 8-2b: |
|  |  |
| $P_u \leq \phi r_n \left(\frac{\text{in.}}{0.177}\right)$ | $P_a \leq \frac{r_n}{\Omega}\left(\frac{\text{in.}}{0.177}\right)$ |
|  |  |
| $\leq (1.392 \text{kip/in.})(6)\left(\frac{\text{in.}}{0.177}\right)$ | $\leq (0.928 \text{kip/in.})(6)\left(\frac{\text{in.}}{0.177}\right)$ |
|  |  |
| $\leq 47.2$ kips | $\leq 31.5$ kips |

Note: The strength of the weld group calculated using the elastic method, as shown here, is significantly less than that calculated using the instantaneous center of rotation method in Example II.A-26.

---

# IIA-266

## EXAMPLE II.A-28A ALL-BOLTED SINGLE-ANGLE CONNECTION (BEAM-TO-GIRDER WEB)

**Given:**

Verify that the all-bolted single-angle connection (Case I in AISC *Manual* Table 10-11) between an ASTM A992/A992M W18×35 beam and an ASTM A992/A992M W21×62 girder web, as shown in Figure II.A-28A-1, is adequate to support the following beam end reactions:

$R_D = 6.5$ kips
$R_L = 20$ kips

The top flange is coped 2 in. deep by 4 in. long, $l_{ev} = 1½$ in., and $l_{eh} = 1¼$ in. Use an ASTM A572/A572M Grade 50 angle. Use standard angle gages.

![Connection diagram showing W18×35 beam connected to W21×62 girder web using an L4×3×⅜×0'-11½" angle (3" leg with 1¾" gage shop-attached to girder web). Four ¾" dia. Group 120 bolts with thread condition N in standard holes are shown. The angle has leh = 1¼" at 3" leg and leh = 1½" at 4" leg. The top flange is coped (c = 4", dc = 2") and the web is 1⅛" thick. Horizontal offset is 2½" and vertical spacing is 1⅛" at top, 9" at 3 @ 3" = 9" spacing, and 1⅛" at bottom.]

*Fig. II.A-28A-1. Connection geometry for Example II.A-28A.*

**Solution:**

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam and girder
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Angle
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

---

# IIA-267

Beam
W18×35
$d = 17.7$ in.
$t_w = 0.300$ in.
$t_f = 0.425$ in.

Girder
W21×62
$t_w = 0.400$ in.

From AISC *Specification* Table J3.3, for ¾-in-diameter bolts with standard holes:

$d_h = 1\frac{3}{16}$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(6.5 \text{ kips}) + 1.6(20 \text{ kips})$ | $R_a = 6.5 \text{ kips} + 20 \text{ kips}$ |
| $= 39.8$ kips | $= 26.5$ kips |

*Strength of the Bolted Connection—Angle*

Check eccentricity of connection.

For the 4 in. angle leg attached to the supported beam (W18×35):

$e = 2½$ in. < 3.00 in., therefore, eccentricity does not need to be considered for this leg. (See AISC *Manual* Figure 10-15)

For the 3 in. angle leg attached to the supporting girder (W21×62):

$$e = 1¾ \text{ in.} + \frac{0.300 \text{ in.}}{2}$$
$$= 1.90 \text{ in.}$$

Because $e = 1.90$ in. < 2½ in., AISC *Manual* Table 10-11 may be conservatively used for bolt shear. From AISC *Manual* Table 10-11, Case I, with $n = 4$:

$C = 3.07$

From the User Note in AISC *Specification* Section J3.7, the strength of the bolt group is taken as the sum of the individual strengths of the individual bolts times the eccentrically loaded bolt group coefficient, C. Per AISC *Specification* Section J3.7, the bearing strength at the bolt hole per AISC *Specification* Section J3.11a, or the tearout strength at the bolt hole per AISC *Specification* Section J3.11a. In this case, the 3 in. leg of the angle is attached to the supporting girder will control because eccentricity must be taken into consideration and the available strength will be determined based on the bolt group using the eccentrically loaded bolt coefficient, C.

From AISC *Manual* Table 7-1, the available shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9$ kips/bolt | $\frac{r_n}{\Omega} = 11.9$ kips/bolt |

---

# IIA-268

The available bearing and tearout strength of the angle at the bottom edge bolt is determined using AISC *Manual* Table 7-5, with $l_e = 1¼$ in., as follows:

| LRFD | ASD |
|------|-----|
| $\phi r_n = (49.4 \text{ kips/in.})(⅜ \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kips/in.})(⅜ \text{ in.})$ |
| $= 18.5$ kips/bolt | $= 12.3$ kips/bolt |

The available bearing and tearout strength of the angle at the interior bolts (not adjacent to the edge) is determined using AISC *Manual* Table 7-4 with $s = 3$ in.

| LRFD | ASD |
|------|-----|
| $\phi r_n = (87.8 \text{ kips/in.})(⅜ \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(⅜ \text{ in.})$ |
| $= 32.9$ kips/bolt | $= 21.9$ kips/bolt |

The available strength of the bolted connection at the angle is conservatively determined using the minimum available strength calculated for bolt shear, bearing at the edge bolt, and tearout at the edge bolt for the angle. The bolt group eccentricity is accounted for by multiplying the minimum available strength by the bolt coefficient, C.

| LRFD | ASD |
|------|-----|
| $\phi R_n = C\phi r_n$ | $\frac{R_n}{\Omega} = C\frac{r_n}{\Omega}$ |
| $= 3.07(17.9 \text{ kips/bolt})$ | $= 3.07(11.9 \text{ kips/bolt})$ |
| $= 55.0 \text{ kips} > 39.8 \text{ kips} \quad \textbf{o.k.}$ | $= 36.5 \text{ kips} > 26.5 \text{ kips} \quad \textbf{o.k.}$ |

*Strength of the Bolted Connection—W18×35 Beam Web*

The available bearing and tearout strength of the beam web at the top edge bolt is determined using AISC *Manual* Table 7-5, conservatively using $l_e = 1¼$ in., as follows:

| LRFD | ASD |
|------|-----|
| $\phi r_n = (49.4 \text{ kips/in.})(0.300 \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kips/in.})(0.300 \text{ in.})$ |
| $= 14.8$ kips/bolt | $= 9.87$ kips/bolt |

The available bearing and tearout strength of the beam web at the interior bolts (not adjacent to the edge) is determined using AISC *Manual* Table 7-4 with $s = 3$ in.

| LRFD | ASD |
|------|-----|
| $\phi r_n = (87.8 \text{ kips/in.})(0.300 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(0.300 \text{ in.})$ |
| $= 26.3$ kips/bolt | $= 17.6$ kips/bolt |

The available strength of the bolted connection at the beam web is determined by summing the effective strength for each bolt using the minimum available strength calculated for bolt shear, bearing on the web, and tearout on the web.

---

# IIA-269

| LRFD | ASD |
|------|-----|
| $\phi R_n = n\phi r_n$ | $\frac{R_n}{\Omega} = n\frac{r_n}{\Omega}$ |
| $= (1 \text{ bolt})(14.8 \text{ kips/bolt})$ | $= (1 \text{ bolt})(9.87 \text{ kips/bolt})$ |
| $+ (3 \text{ bolts})(17.9 \text{ kips/bolt})$ | $+ (3 \text{ bolts})(11.9 \text{ kips/bolt})$ |
| $= 68.5 \text{ kips} > 39.8 \text{ kips} \quad \textbf{o.k.}$ | $= 45.6 \text{ kips} > 26.5 \text{ kips} \quad \textbf{o.k.}$ |

*Strength of the Bolted Connection—W21×62 Girder Web*

The available bearing and tearout strength of the girder web is determined using AISC *Manual* Table 7-4 with $s = 3$ in.

| LRFD | ASD |
|------|-----|
| $\phi r_n = (87.8 \text{ kips/in.})(0.400 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(0.400 \text{ in.})$ |
| $= 35.1$ kips/bolt | $= 23.4$ kips/bolt |

Therefore, bolt shear controls over bearing or tearout on the girder web and is adequate based on previous calculations.

*Shear Strength of Angle*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the angle is determined as follows:

$$A_{gv} = lt$$
$$= (11½ \text{ in.})(⅜ \text{ in.})$$
$$= 4.31 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(4.31 \text{ in.}^2)$$
$$= 129 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(129 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{129 \text{ kips}}{1.50}$ |
| $= 129 \text{ kips} > 39.8 \text{ kips} \quad \textbf{o.k.}$ | $= 86.0 \text{ kips} > 26.5 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the angle is determined using the net area determined in accordance with AISC *Specification* Section B4.3b.

$$A_{nv} = [l - n(d_h + \frac{1}{16} \text{ in.})]t$$
$$= [11½ \text{ in.} - 4(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](⅜ \text{ in.})$$
$$= 3.00 \text{ in.}^2$$

---

# IIA-270

$$R_n = 0.60F_u A_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(3.00 \text{ in.}^2)$$
$$= 117 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(117 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{117 \text{ kips}}{2.00}$ |
| $= 87.8 \text{ kips} > 39.8 \text{ kips} \quad \textbf{o.k.}$ | $= 58.5 \text{ kips} > 26.5 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture of Angle*

The nominal strength for the limit state of block shear rupture is given by AISC *Specification* Section J4.3.

$$R_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$ (*Spec.* Eq. J4-5)

The available block shear rupture strength of the 3 in. leg is determined as follows, using AISC *Manual* Tables 9-3a, 9-3b, and 9-3c, and AISC *Specification* Equation J4-5, with $n = 4$, $l_{ev} = l_{eh} = 1¼$ in., and $U_{bs} = 1.0$.

| LRFD | ASD |
|------|-----|
| Tension rupture component from AISC *Manual* Table 9-3a: | Tension rupture component from AISC *Manual* Table 9-3a: |
|  |  |
| $\frac{\phi F_u A_{nt}}{t} = 39.6$ kips/in. | $\frac{F_u A_{nt}}{\Omega t} = 26.4$ kips/in. |
|  |  |
| Shear yielding component from AISC *Manual* Table 9-3b: | Shear yielding component from AISC *Manual* Table 9-3b: |
|  |  |
| $\frac{\phi 0.6F_y A_{gv}}{t} = 231$ kips/in. | $\frac{0.6F_y A_{gv}}{\Omega t} = 154$ kips/in. |
|  |  |
| Shear rupture component from AISC *Manual* Table 9-3c: | Shear rupture component from AISC *Manual* Table 9-3c: |
|  |  |
| $\frac{\phi 0.6F_u A_{nv}}{t} = 210$ kips/in. | $\frac{0.6F_u A_{nv}}{\Omega t} = 140$ kips/in. |
|  |  |
| $\phi R_n = \phi 0.60F_u A_{nv} + \phi U_{bs}F_u A_{nt}$ | $\frac{R_n}{\Omega} = \frac{0.60F_u A_{nv}}{\Omega} + \frac{U_{bs}F_u A_{nt}}{\Omega}$ |
|  |  |
| $\leq \phi 0.60F_y A_{gv} + \phi U_{bs}F_u A_{nt}$ | $\leq \frac{0.60F_y A_{gv}}{\Omega} + \frac{U_{bs}F_u A_{nt}}{\Omega}$ |
|  |  |
| $= (⅜ \text{ in.})[210 \text{ kips/in.} + (1.0)(39.6 \text{ kips/in.})]$ | $= (⅜ \text{ in.})[140 \text{ kips/in.} + (1.0)(26.4 \text{ kips/in.})]$ |
|  |  |
| $\leq (⅜ \text{ in.})[231 \text{ kips/in.} + (1.0)(39.6 \text{ kips/in.})]$ | $\leq (⅜ \text{ in.})[154 \text{ kips/in.} + (1.0)(26.4 \text{ kips/in.})]$ |
|  |  |
| $= 93.6 \text{ kips} < 101 \text{ kips}$ | $= 62.4 \text{ kips} < 67.7 \text{ kips}$ |

---

# IIA-271

| LRFD | ASD |
|------|-----|
| Therefore: | Therefore: |
|  |  |
| $\phi R_n = 93.6 \text{ kips} > 39.8 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 62.4 \text{ kips} > 26.5 \text{ kips} \quad \textbf{o.k.}$ |

Because the edge distance is smaller, block shear rupture is governed by the 3 in. leg.

*Flexural Yielding Strength of Angle*

The required flexural strength of the support leg of the angle is determined as follows:

| LRFD | ASD |
|------|-----|
| $M_u = R_u e$ | $M_a = R_a e$ |
|  |  |
| $= (39.8 \text{kips})\left(1¾ \text{ in.} + \frac{0.300 \text{ in.}}{2}\right)$ | $= (26.5 \text{kips})\left(1¾ \text{ in.} + \frac{0.300 \text{ in.}}{2}\right)$ |
|  |  |
| $= 75.6$ kip-in. | $= 50.4$ kip-in. |

The available flexural yielding strength of the support leg of the angle is determined as follows:

$$M_n = F_y Z_x$$
$$= (50 \text{ ksi})\left[\frac{(⅜ \text{ in.})(11½ \text{ in.})^2}{4}\right]$$
$$= 620 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi M_n = 0.90(620 \text{ kip-in.})$ | $\frac{M_n}{\Omega} = \frac{620 \text{ kip-in.}}{1.67}$ |
| $= 558 \text{ kip-in.} > 75.6 \text{ kip-in.} \quad \textbf{o.k.}$ | $= 371 \text{ kip-in.} > 50.4 \text{ kip-in.} \quad \textbf{o.k.}$ |

*Flexural Rupture Strength of Angle*

The available flexural rupture strength of the support leg of the angle is determined as follows:

$$Z_{net} = (⅜ \text{ in.})\left[\frac{(11½ \text{ in.})^2}{4} - 2(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})(4.50 \text{ in.}) - 2(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})(1.50 \text{ in.})\right]$$
$$= 8.46 \text{ in.}^3$$

$$M_n = F_u Z_{net}$$ (*Manual* Eq. 9-8)
$$= (65 \text{ ksi})(8.46 \text{ in.}^3)$$
$$= 550 \text{ kip-in.}$$

---

# IIA-272

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.75$ | $\Omega_b = 2.00$ |
|  |  |
| $\phi_b M_n = 0.75(550 \text{ kip-in.})$ | $\frac{M_n}{\Omega_b} = \frac{550 \text{ kip-in.}}{2.00}$ |
| $= 413 \text{ kip-in.} > 75.6 \text{ kip-in.} \quad \textbf{o.k.}$ | $= 275 \text{ kip-in.} > 50.4 \text{ kip-in.} \quad \textbf{o.k.}$ |

*Flexural Yielding and Buckling of Coped Beam Web*

The required flexural strength of the coped section of the beam web is determined using AISC *Manual* Equation 9-9 as follows:

$$e = c + setback$$
$$= 4 \text{ in.} + ¾ \text{ in.}$$
$$= 4.75 \text{ in.}$$

| LRFD | ASD |
|------|-----|
| $M_u = R_u e$ | $M_a = R_a e$ |
| $= (39.8 \text{ kips})(4.75 \text{ in.})$ | $= (26.5 \text{ kips})(4.75 \text{ in.})$ |
| $= 189$ kip-in. | $= 126$ kip-in. |

The minimum length of the connection elements is one-half of the reduced beam depth, $h_o$. From the geometry shown in AISC *Manual* Figure 9-2:

$$h_c = d - d_c$$
$$= 17.7 \text{ in.} - 2 \text{ in.}$$
$$= 15.7 \text{ in.}$$

$$l \quad > 0.5h_c$$
$$11½ \text{ in.} > 0.5(15.7 \text{ in.})$$
$$11½ \text{ in.} > 7.85 \text{ in.} \quad \textbf{o.k.}$$

The available flexural local buckling strength of a beam coped at the top flange is determined as follows:

$$\lambda = \frac{h_c}{t_w}$$ (*Manual* Eq. 9-17)
$$= \frac{15.7 \text{ in.}}{0.300 \text{ in.}}$$
$$= 52.3$$

$$\frac{c}{h_c} = \frac{4 \text{ in.}}{15.7 \text{ in.}}$$
$$= 0.255$$

Because $\frac{c}{h_c} \leq 1.0$, the plate buckling coefficient, $k$, is calculated as follows:

---

# IIA-273

$$k = 2.2\left(\frac{h_c}{c}\right)^{1.65}$$ (*Manual* Eq. 9-19a)
$$= 2.2\left(\frac{15.7 \text{ in.}}{4 \text{ in.}}\right)^{1.65}$$
$$= 21.0$$

$$\frac{c}{d} = \frac{4 \text{ in.}}{17.7 \text{ in.}}$$
$$= 0.226$$

Because $\frac{c}{d} \leq 1.0$, the buckling adjustment factor, $f$, is calculated as follows:

$$f = 2\left(\frac{c}{d}\right)$$ (*Manual* Eq. 9-20a)
$$= 2(0.226)$$
$$= 0.452$$

$$k_1 = fk \geq 1.61$$ (*Manual* Eq. 9-14)
$$= (0.452)(21.0) \geq 1.61$$
$$= 9.49 > 1.61$$
$$= 9.49$$

$$\lambda_p = 0.475\sqrt{\frac{k_1 E}{F_y}}$$ (*Manual* Eq. 9-18)
$$= 0.475\sqrt{\frac{(9.49)(29,000 \text{ ksi})}{50 \text{ ksi}}}$$
$$= 35.2$$

$$2\lambda_p = 2(35.2)$$
$$= 70.4$$

Because $\lambda_p < \lambda \leq 2\lambda_p$, calculate the nominal flexural strength using AISC *Manual* Equation 9-11.

The plastic section modulus of the coped section, $Z_c$, is determined from AISC *Manual* Table 9-2b.

$Z_c = 32.1$ in.<sup>3</sup>

$$M_p = F_y Z_c$$
$$= (50 \text{ ksi})(32.1 \text{ in.}^3)$$
$$= 1,610 \text{ kip-in.}$$

From AISC *Manual* Table 9-2a:

$S_c = 18.2$ in.<sup>3</sup>

---

# IIA-274

$$M_y = F_y S_c$$
$$= (50 \text{ ksi})(18.2 \text{ in.}^3)$$
$$= 910 \text{ kip-in.}$$

$$M_n = M_p - (M_p - M_y)\left(\frac{\lambda}{\lambda_p} - 1\right)$$ (*Manual* Eq. 9-11)
$$= (1,610 \text{ kip-in.}) - (1,610 \text{ kip-in.} - 910 \text{ kip-in.})\left(\frac{52.3}{35.2} - 1\right)$$
$$= 1,270 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
|  |  |
| $\phi_b M_n = 0.90(1,270 \text{ kip-in.})$ | $\frac{M_n}{\Omega_b} = \frac{1,270 \text{ kip-in.}}{1.67}$ |
| $= 1,140 \text{ kip-in.} > 189 \text{ kip-in.} \quad \textbf{o.k.}$ | $= 760 \text{ kip-in.} > 126 \text{ kip-in.} \quad \textbf{o.k.}$ |

*Shear Strength of Beam Web*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the beam web is determined as follows:

$$A_{gv} = h_c t_w$$
$$= (15.7 \text{ in.})(0.300 \text{ in.})$$
$$= 4.71 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(4.71 \text{ in.}^2)$$
$$= 141 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(141 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{141 \text{ kips}}{1.50}$ |
| $= 141 \text{ kips} > 39.8 \text{ kips} \quad \textbf{o.k.}$ | $= 94.0 \text{ kips} > 26.5 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture of Beam Web*

The nominal strength for the limit state of block shear rupture is given by AISC *Specification* Section J4.3.

$$R_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$ (*Spec.* Eq. J4-5)

The available block shear rupture strength of the web is determined as follows, using AISC *Manual* Tables 9-3a, 9-3b, and 9-3c, and AISC *Specification* Equation J4-5, with $n = 4$, $l_{ev} = 1½$ in., $l_{eh} = 1½$ in. (including a ¼ in. tolerance to account for possible beam underrun), and $U_{bs} = 1.0$.

---

# IIA-275

| LRFD | ASD |
|------|-----|
| Tension rupture component from AISC *Manual* Table 9-3a: | Tension rupture component from AISC *Manual* Table 9-3a: |
|  |  |
| $\frac{\phi F_u A_{nt}}{t} = 51.8$ kips/in. | $\frac{F_u A_{nt}}{\Omega t} = 34.5$ kips/in. |
|  |  |
| Shear yielding component from AISC *Manual* Table 9-3b: | Shear yielding component from AISC *Manual* Table 9-3b: |
|  |  |
| $\frac{\phi 0.60F_y A_{gv}}{t} = 236$ kips/in. | $\frac{0.60F_y A_{gv}}{\Omega t} = 158$ kips/in. |
|  |  |
| Shear rupture component from AISC *Manual* Table 9-3c: | Shear rupture component from AISC *Manual* Table 9-3c: |
|  |  |
| $\frac{\phi 0.60F_u A_{nv}}{t} = 218$ kips/in. | $\frac{0.60F_u A_{nv}}{\Omega t} = 145$ kips/in. |
|  |  |
| $\phi R_n = \phi 0.60F_u A_{nv} + \phi U_{bs}F_u A_{nt}$ | $\frac{R_n}{\Omega} = \frac{0.60F_u A_{nv}}{\Omega} + \frac{U_{bs}F_u A_{nt}}{\Omega}$ |
|  |  |
| $\leq \phi 0.60F_y A_{gv} + \phi U_{bs}F_u A_{nt}$ | $\leq \frac{0.60F_y A_{gv}}{\Omega} + \frac{U_{bs}F_u A_{nt}}{\Omega}$ |
|  |  |
| $= (0.300 \text{ in.})[218 \text{ kips/in.} + (1.0)(51.8 \text{ kips/in.})]$ | $= (0.300 \text{ in.})[145 \text{ kips/in.} + (1.0)(34.5 \text{ kips/in.})]$ |
|  |  |
| $\leq (0.300 \text{ in.})[236 \text{ kips/in.} + (1.0)(51.8 \text{ kips/in.})]$ | $\leq (0.300 \text{ in.})[158 \text{ kips/in.} + (1.0)(34.5 \text{ kips/in.})]$ |
|  |  |
| $= 80.9 \text{ kips} < 86.3 \text{ kips}$ | $= 53.9 \text{ kips} < 57.8 \text{ kips}$ |
|  |  |
| Therefore: | Therefore: |
|  |  |
| $\phi R_n = 80.9 \text{ kips} > 39.8 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 53.9 \text{ kips} > 26.5 \text{ kips} \quad \textbf{o.k.}$ |

*Conclusion*

The connection is found to be adequate as given for the applied load.

---

# IIA-276

## EXAMPLE II.A-28B ALL-BOLTED SINGLE ANGLE CONNECTION—STRUCTURAL INTEGRITY CHECK

**Given:**

Verify the all-bolted single-angle connection from Example II.A-28A, as shown in Figure II.A-28B-1, for the structural integrity provisions of AISC *Specification* Section B3.9. The connection is verified as a beam end connection. Note that these checks are necessary when design for structural integrity is required by the applicable building code. The angle is ASTM A572/A572M Grade 50 material.

![Connection diagram showing W18×35 beam connected to W21×62 girder web using an L4×3×⅜×0'-11½" angle (3" leg with 1¾" gage shop-attached to girder web). Four ¾" dia. Group 120 bolts with thread condition N in standard holes are shown. The angle has leh = 1¼" at 3" leg and leh = 1½" at 4" leg. The top flange is coped (c = 4", dc = 2") and the web is 1⅛" thick. Horizontal offset is 2½" and vertical spacing is 1⅛" at top, 9" at 3 @ 3" = 9" spacing, and 1⅛" at bottom.]

*Fig. II.A-28B-1. Connection geometry for Example II.A-28B.*

**Solution:**

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam and Girder
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Angle
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W18×35
$t_w = 0.300$ in.

---

# IIA-277

Girder
W21×62
$d = 21.0$ in.
$t_w = 0.400$ in.
$k_{des} = 1.12$ in.

From AISC *Specification* Table J3.3, the hole diameter for ¾-in-diameter bolts with standard holes is:

$d_h = 1\frac{3}{16}$ in.

From Example II.A-28A, the required shear strength is:

| LRFD | ASD |
|------|-----|
| $V_u = 39.8$ kips | $V_a = 26.5$ kips |

From AISC *Specification* Section B3.9(b), the minimum nominal axial tensile strength is:

| LRFD | ASD |
|------|-----|
| $T = \frac{2}{3}V_u \geq 10$ kips | $T = V_a \geq 10$ kips |
|  | $= 26.5 \text{ kips} > 10 \text{ kips}$ |
| $= \frac{2}{3}(39.8 \text{ kips}) > 10 \text{ kips}$ | $= 26.5$ kips |
| $= 26.5 \text{ kips} > 10 \text{ kips}$ |  |
| $= 26.5$ kips |  |

*Bolt Shear*

From AISC *Specification* Section J3.7, the nominal bolt shear strength is determined as follows:

$F_{nv} = 54$ ksi, from AISC *Specification* Table J3.2

$$T_n = nF_{nv}A_b$$ (from *Spec.* Eq. J3-1)
$$= (4 \text{ bolts})(54 \text{ ksi})(0.442 \text{ in.}^2)$$
$$= 95.5 \text{ kips}$$

*Bolt Tension*

From AISC *Specification* Section J3.7, the nominal bolt tensile strength is determined as follows:

$F_{nt} = 90$ ksi, from AISC *Specification* Table J3.2

$$T_n = nF_{nt}A_b$$ (from *Spec.* Eq. J3-1)
$$= (4 \text{ bolts})(90 \text{ ksi})(0.442 \text{ in.}^2)$$
$$= 159 \text{ kips}$$

*Bolt Bearing and Tearout*

From AISC *Specification* Section B3.9, for the purpose of satisfying structural integrity requirements, inelastic deformations of the connection are permitted; therefore, AISC *Specification* Equations J3-6b and J3-6d are used to determine the nominal bearing and tearout strength.

---

# IIA-278

For bolt bearing on the angle:

$$T_n = (4 \text{ bolts})3.0dtF_u$$ (from *Spec.* Eq. J3-6b)
$$= (4 \text{ bolts})(3.0)(¾ \text{ in.})(⅜ \text{ in.})(65 \text{ ksi})$$
$$= 219 \text{ kips}$$

For bolt bearing on the beam web:

$$T_n = (4 \text{ bolts})3.0dt_w F_u$$ (from *Spec.* Eq. J3-6b)
$$= (4 \text{ bolts})(3.0)(¾ \text{ in.})(0.300 \text{ in.})(65 \text{ ksi})$$
$$= 176 \text{ kips}$$

For bolt tearout on the angle:

$$l_c = l_{eh} - 0.5d_h$$
$$= 1½ \text{ in.} - 0.5(1\frac{3}{16} \text{ in.})$$
$$= 1.09 \text{ in.}$$

$$T_n = (4 \text{ bolts})1.5l_c tF_u$$ (from *Spec.* Eq. J3-6d)
$$= (4 \text{ bolts})(1.5)(1.09 \text{ in.})(⅜ \text{ in.})(65 \text{ ksi})$$
$$= 159 \text{ kips}$$

For bolt tearout on the beam web (including a ¼ in. tolerance to account for possible beam underrun):

$$l_c = l_{eh} - 0.5d_h$$
$$= (1¼ \text{ in.} - ¼ \text{ in.}) - 0.5(1\frac{3}{16} \text{ in.})$$
$$= 1.09 \text{ in.}$$

$$T_n = (4 \text{ bolts})1.5l_{c}t_w F_u$$ (from *Spec.* Eq. J3-6d)
$$= (4 \text{ bolts})(1.5)(1.09 \text{ in.})(0.300 \text{ in.})(65 \text{ ksi})$$
$$= 128 \text{ kips}$$

*Angle Bending and Prying Action*

From AISC *Manual* Part 9, the nominal strength of the angle accounting for prying action is determined as follows:

$$b = gage - \frac{t}{2}$$
$$= 1¾ \text{ in.} - \frac{⅜ \text{ in.}}{2}$$
$$= 1.56 \text{ in.}$$

$$a = \min\{1¼ \text{ in.}, 1.25b\}$$
$$= \min\{1¼ \text{ in.}, 1.25(1.56 \text{ in.})\}$$
$$= 1.25 \text{ in.}$$

---

# IIA-279

$$b' = b - \frac{d}{2}$$ (*Manual* Eq. 9-24)
$$= 1.56 \text{ in.} - \frac{¾ \text{ in.}}{2}$$
$$= 1.19 \text{ in.}$$

$$a' = a + \frac{d}{2}$$ (*Manual* Eq. 9-23)
$$= 1.25 + \frac{¾ \text{ in.}}{2}$$
$$= 1.63 \text{ in.}$$

$$\rho = \frac{b'}{a'}$$ (*Manual* Eq. 9-29)
$$= \frac{1.19 \text{ in.}}{1.63 \text{ in.}}$$
$$= 0.730$$

Note that end distances of 1¼ in. are used on the angles, so $p$ is the average pitch of the bolts:

$$p = \frac{l}{n}$$
$$= \frac{11½ \text{ in.}}{4}$$
$$= 2.88 \text{ in.}$$

Check that $p < s$:

$p = 2.88$ in. < $s = 3.00$ in.     **o.k.**

$$d' = d$$
$$= 1\frac{3}{16} \text{ in.}$$

$$\delta = 1 - \frac{d'}{p}$$ (*Manual* Eq. 9-28)
$$= 1 - \frac{1\frac{3}{16}\text{in.}}{2.88 \text{ in.}}$$
$$= 0.718$$

$$T_c = F_{nt}A_b$$
$$= (90 \text{ ksi})(0.442 \text{ in.}^2)$$
$$= 39.8 \text{ kips/bolt}$$

$$t_c = \sqrt{\frac{4T_c b'}{pF_u}}$$ (from *Manual* Eq. 9-30)
$$= \sqrt{\frac{4(39.8 \text{ kips/bolt})(1.19 \text{ in.})}{(2.88 \text{ in.})(65 \text{ ksi})}}$$
$$= 1.01 \text{ in.}$$

---

# IIA-280

$$\alpha' = \frac{1}{\delta(1+\rho)}\left[\left(\frac{t_c}{t}\right)^2 - 1\right]$$ (*Manual* Eq. 9-38)
$$= \frac{1}{0.718(1 + 0.730)}\left[\left(\frac{1.01 \text{ in.}}{⅜ \text{ in.}}\right)^2 - 1\right]$$
$$= 5.03$$

Because $\alpha' > 1$:

$$Q = \left(\frac{t}{t_c}\right)^2(1 + \delta)$$ (*Manual* Eq. 9-39c)
$$= \left(\frac{⅜ \text{ in.}}{1.01 \text{ in.}}\right)^2(1 + 0.718)$$
$$= 0.237$$

$$T_n = nT_{c, adj}$$ (from *Manual* Eq. 9-40)
$$= nQT_c$$
$$= (4 \text{ bolts})(0.237)(39.8 \text{ kips/bolt})$$
$$= 37.7 \text{ kips}$$

*Block Shear Rupture—Angle*

The nominal block shear rupture strength, due to axial load, of the angle is determined using AISC *Specification* Section J4.3.

$$T_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$ (from *Spec.* Eq. J4-5)

The nominal block shear rupture strength of the angle for a U-shaped failure plane is:

$$A_{gv} = 2l_{eh}t$$
$$= (2)(1½ \text{ in.})(⅜ \text{ in.})$$
$$= 1.13 \text{ in.}^2$$

$$A_{nv} = (2)[l_{eh} - 0.5(d_h + \frac{1}{16} \text{ in.})]t$$
$$= (2)[1½ \text{ in.} - 0.5(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](⅜ \text{ in.})$$
$$= 0.797 \text{ in.}^2$$

$$A_{nt} = [9.00 \text{ in.} - (n-1)(d_h + \frac{1}{16} \text{ in.})]t$$
$$= [9.00 \text{ in.} - (4-1)(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](⅜ \text{ in.})$$
$$= 2.39 \text{ in.}^2$$

$U_{bs} = 1.0$

---

# IIA-281

$$T_n = 0.60(65 \text{ ksi})(0.797 \text{ in.}^2) + 1.0(65 \text{ ksi})(2.39 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(1.13 \text{ in.}^2) + 1.0(65 \text{ ksi})(2.39 \text{ in.}^2)$$
$$= 186 \text{ kips} < 189 \text{ kips}$$
$$= 186 \text{ kips}$$

The nominal block shear rupture strength of the angle for an L-shaped failure plane is:

$$A_{gv} = l_{eh}t$$
$$= (1½ \text{ in.})(⅜ \text{ in.})$$
$$= 0.563 \text{ in.}^2$$

$$A_{nv} = [l_{eh} - 0.5(d_h + \frac{1}{16} \text{ in.})]t$$
$$= [1½ \text{ in.} - 0.5(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](⅜ \text{ in.})$$
$$= 0.398 \text{ in.}^2$$

$$A_{nt} = [l - l_{ev} - (n - 0.5)(d_h + \frac{1}{16} \text{ in.})]t$$
$$= [11.5 \text{ in.} - 1¼ \text{ in.} - (4 - 0.5)(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](⅜ \text{ in.})$$
$$= 2.70 \text{ in.}^2$$

$U_{bs} = 1.0$

$$T_n = 0.60(65 \text{ ksi})(0.398 \text{ in.}^2) + 1.0(65 \text{ ksi})(2.70 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(0.563 \text{ in.}^2) + 1.0(65 \text{ ksi})(2.70 \text{ in.}^2)$$
$$= 191 \text{ kips} < 192 \text{ kips}$$
$$= 191 \text{ kips}$$

*Tensile Yielding of Angle*

From AISC *Specification* Section J4.1, the nominal tensile yielding strength of the angle is determined as follows:

$$A_g = lt$$
$$= (11½ \text{ in.})(⅜ \text{ in.})$$
$$= 4.31 \text{ in.}^2$$

$$T_n = F_y A_g$$ (from *Spec.* Eq. J4-1)
$$= (50 \text{ ksi})(4.31 \text{ in.}^2)$$
$$= 216 \text{ kips}$$

*Tensile Rupture of Angle*

From AISC *Specification* Section J4.1, the nominal tensile rupture strength of the angle is determined as follows:

$$A_e = A_n U$$ (*Spec.* Eq. D3-1)
$$= [l - n(d_h + \frac{1}{16} \text{ in.})]tU$$
$$= [11½ \text{ in.} - 4(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](⅜ \text{ in.})(1.0)$$
$$= 3.00 \text{ in.}^2$$

---

# IIA-282

$$T_n = F_u A_e$$ (from *Spec.* Eq. J4-2)
$$= (65 \text{ ksi})(3.00 \text{ in.}^2)$$
$$= 195 \text{ kips}$$

*Block Shear Rupture—Beam Web*

The nominal block shear rupture strength, due to axial load, of the beam web is determined using AISC *Specification* Section J4.3.

$$T_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$ (from *Spec.* Eq. J4-5)

The nominal block shear rupture strength of the beam web for a U-shaped failure plane is determined as follows (including a ¼ in. tolerance to account for possible beam underrun):

$$A_{gv} = 2l_{eh}t_w$$
$$= (2)(1¼ \text{ in.} - ¼ \text{ in.})(0.300 \text{ in.})$$
$$= 0.900 \text{ in.}^2$$

$$A_{nv} = (2)[l_{eh} - 0.5(d_h + \frac{1}{16} \text{ in.})]t_w$$
$$= (2)[(1¼ \text{ in.} - ¼ \text{ in.}) - 0.5(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](0.300 \text{ in.})$$
$$= 0.638 \text{ in.}^2$$

$$A_{nt} = [9.00 \text{ in.} - 3(d_h + \frac{1}{16} \text{ in.})]t_w$$
$$= [9.00 \text{ in.} - 3(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](0.300 \text{ in.})$$
$$= 1.91 \text{ in.}^2$$

$U_{bs} = 1.0$

$$T_n = 0.60(65 \text{ ksi})(0.638 \text{ in.}^2) + 1.0(65 \text{ ksi})(1.91 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(0.900 \text{ in.}^2) + 1.0(65 \text{ ksi})(1.91 \text{ in.}^2)$$
$$= 149 \text{ kips} < 151 \text{ kips}$$

Therefore:
$T_n = 149$ kips

The nominal block shear rupture strength of the beam web for an L-shaped failure plane is determined as follows (including a ¼ in. tolerance to account for possible beam underrun):

$$A_{gv} = l_{eh}t_w$$
$$= (1¼ \text{ in.} - ¼ \text{ in.})(0.300 \text{ in.})$$
$$= 0.450 \text{ in.}^2$$

$$A_{nv} = [l_{eh} - 0.5(d_h + \frac{1}{16} \text{ in.})]t_w$$
$$= [(1¼ \text{ in.} - ¼ \text{ in.}) - 0.5(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](0.300 \text{ in.})$$
$$= 0.319 \text{ in.}^2$$

---

# IIA-283

$$A_{nt} = [10.5 - (n - 0.5)(d_h + \frac{1}{16} \text{ in.})]t_w$$
$$= [10.5 \text{ in.} - (4 - 0.5)(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](0.300 \text{ in.})$$
$$= 2.23 \text{ in.}^2$$

$U_{bs} = 1.0$

$$T_n = 0.60(65 \text{ ksi})(0.319 \text{ in.}^2) + 1.0(65 \text{ ksi})(2.23 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(0.450 \text{ in.}^2) + 1.0(65 \text{ ksi})(2.23 \text{ in.}^2)$$
$$= 157 \text{ kips} < 158 \text{ kips}$$

Therefore:
$T_n = 157$ kips

*Nominal Tensile Strength*

The controlling tensile strength, $T_n$, is the least of those previously calculated:

$$T_n = \min\begin{Bmatrix}95.5 \text{ kips}, 159 \text{ kips}, 219 \text{ kips}, 176 \text{ kips}, 159 \text{ kips}, 128 \text{ kips}, 37.7 \text{ kips}, \\ 186 \text{ kips}, 191 \text{ kips}, 216 \text{ kips}, 195 \text{ kips}, 149 \text{ kips}, 157 \text{ kips}\end{Bmatrix}$$
$$= 37.7 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $T_n = 37.7 \text{ kips} > 26.5 \text{ kips} \quad \textbf{o.k.}$ | $T_n = 37.7 \text{ kips} > 26.5 \text{ kips} \quad \textbf{o.k.}$ |

---

# IIA-284

## EXAMPLE II.A-29 BOLTED/WELDED SINGLE-ANGLE CONNECTION (BEAM-TO-COLUMN FLANGE)

**Given:**

Verify the available strength of the single-angle connection between an ASTM A992/A992M W16×50 beam and an ASTM A992/A992M W14×90 column flange, as shown in Figure II.A-29-1, to support the following beam end reactions:

$R_D = 9$ kips
$R_L = 27$ kips

Use an ASTM A572/A572M Grade 50 single angle. Use 70-ksi electrode welds to connect the single angle to the column flange.

This example is repeated using the following two procedures:

Part A: Determine the available connection strength using the tables in *Manual* Part 10.
Part B: Determine the available connection strength by checking individual limit states.

![Connection diagram showing W16×50 beam connected to W14×90 column flange using an L4×3×⅜×0'-11½" angle. The connection shows four ¾" dia. Group 120 bolts with thread condition N in standard holes, with 3" spacing (3 @ 3" = 9"). The angle has ⅜" fillet welds (top and bottom) connecting to the column flange. Dimensions show e = 2¾", 4" spacing, leh = 1¼", 1⅛" at top and bottom, and 3" leg spacing. The angle is welded to the column flange and bolted to the beam web.]

*Fig. II.A-29-1. Connection geometry for Example II.A-29.*

**Solution:**

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam and column
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Angle
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

---

# IIA-285

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W16×50
$d = 16.3$ in.
$t_w = 0.380$ in.
$t_f = 0.630$ in.

Column
W14×90
$t_f = 0.710$

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(9 \text{ kips}) + 1.6(27 \text{ kips})$ | $R_a = 9 \text{ kips} + 27 \text{ kips}$ |
| $= 54.0$ kips | $= 36.0$ kips |

*Part A—Determine the Available Connection Strength Using the Tables in Manual Part 10*

*Single Angle and Welds*

Check eccentricity of the connection. The use of AISC *Manual* Table 10-12 limits the eccentricity of the bolt group to $e \leq 3$ in.

For the 4 in. angle leg attached to the supported beam:

$e = 2¾$ in. < 3.00 in.     **o.k.**

For the 3 in. angle leg attached to the supporting column flange:

Because the half-web dimension of the W16×50 supported beam is less than ¼ in., AISC *Manual* Table 10-12a may conservatively be used.

Check a four-bolt single angle (L4×3×⅜).

From AISC *Manual* Table 10-12a, with four rows of ¾-in.-diameter bolts in standard holes, the angle available strength is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 87.8 \text{ kips} > 54.0 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 58.5 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Manual* Table 10-12a, the available weld strength for a $\frac{3}{16}$ in. fillet weld is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 56.6 \text{ kips} > 54.0 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 37.8 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ |

*Available Shear Transfer Strength at Bolt Holes*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength determined in

---

# IIA-286

accordance with AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the angle at the bolt hole, and (3) the available bearing or tearout strength of the beam web at the bolt hole.

From AISC *Manual* Table 10-12b, the available bolt shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9$ kips | $\frac{r_n}{\Omega} = 11.9$ kips |

From AISC *Manual* Table 10-12b, the available bearing and tearout strength of the angle per bolt for ¾-in.-diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the edge bolt ($l_{ev} = 1¼$ in.): | For the edge bolt ($l_{ev} = 1¼$ in.): |
|  |  |
| $\phi r_n = (49.4 \text{ kips/in.})(⅜ \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kips/in.})(⅜ \text{ in.})$ |
| $= 18.5$ kips | $= 12.3$ kips |
|  |  |
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
|  |  |
| $\phi r_n = (87.8 \text{ kips/in.})(⅜ \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(⅜ \text{ in.})$ |
| $= 32.9$ kips | $= 21.9$ kips |

From AISC *Manual* Table 10-12b, the available bearing and tearout strength of the beam web per bolt for ¾-in.-diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
|  |  |
| $\phi r_n = (87.8 \text{ kips/in.})(0.380 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(0.380 \text{ in.})$ |
| $= 33.4$ kips | $= 22.2$ kips |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the angle for a non-edge bolt, and the available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n, top} = \min\begin{Bmatrix}17.9 \text{ kips,} \\ 32.9 \text{ kips,} \\ 33.4 \text{ kips}\end{Bmatrix}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{Bmatrix}11.9 \text{ kips,} \\ 21.9 \text{ kips,} \\ 22.2 \text{ kips}\end{Bmatrix}$ |
|  |  |
| $= 17.9$ kips | $= 11.9$ kips |

At the middle connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the angle for a non-edge bolt, and the available bearing and tearout strength of the beam web for a non-edge bolt:

---

# IIA-287

| LRFD | ASD |
|------|-----|
| $\phi r_{n,mid} = \min\begin{Bmatrix}17.9 \text{ kips,} \\ 32.9 \text{ kips,} \\ 33.4 \text{ kips}\end{Bmatrix}$ | $\frac{r_{n,mid}}{\Omega} = \min\begin{Bmatrix}11.9 \text{ kips,} \\ 21.9 \text{ kips,} \\ 22.2 \text{ kips}\end{Bmatrix}$ |
|  |  |
| $= 17.9$ kips | $= 11.9$ kips |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the angle for an edge bolt, and the available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n, bot} = \min\begin{Bmatrix}17.9 \text{ kips,} \\ 18.5 \text{ kips,} \\ 33.4 \text{ kips}\end{Bmatrix}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{Bmatrix}11.9 \text{ kips,} \\ 12.3 \text{ kips,} \\ 22.2 \text{ kips}\end{Bmatrix}$ |
|  |  |
| $= 17.9$ kips | $= 11.9$ kips |

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi r_{n,top} + \phi r_{n,mid}(n - 2) + \phi r_{n,bot}$ | $\frac{R_n}{\Omega} = \frac{r_{n,top}}{\Omega} + \frac{r_{n,mid}}{\Omega}(n - 2) + \frac{r_{n,bot}}{\Omega}$ |
|  |  |
| $= 17.9 \text{ kips} + (17.9 \text{ kips})(4 - 2) + 17.9 \text{ kips}$ | $= 11.9 \text{ kips} + (11.9 \text{ kips})(4 - 2) + 11.9 \text{ kips}$ |
|  |  |
| $= 71.6 \text{ kips} > 54.0 \text{ kips} \quad \textbf{o.k.}$ | $= 47.6 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ |

*Available Beam Web Strength*

Because the beam is not coped, limit states of block shear rupture and shear rupture of the beam are not applicable. The beam web is adequate for the required loading.

*Support Thickness*

The minimum support thickness that matches the column flange strength to the $\frac{3}{16}$ in. fillet weld strength is:

$$t_{min} = \frac{3.09D}{F_u}$$ (*Manual* Eq. 9-6)
$$= \frac{3.09(3)}{65 \text{ ksi}}$$
$$= 0.143 \text{ in.} < 0.710 \text{ in.} \quad \textbf{o.k.}$$

Note: The minimum thickness values listed in AISC *Manual* Table 10-12 are for conditions with angles on both sides of the web.

Use a four-bolt L4×3×⅜ single-angle connection. The 3 in. leg will be shop welded to the column flange and the 4 in. leg will be field bolted to the beam web.

*Conclusion*

The available connection strength is:

---

# IIA-288

| LRFD | ASD |
|------|-----|
| $\phi R_n = 56.6 \text{ kips} > 54.0 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 37.8 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ |

The connection is found to be adequate as given for the applied load.

*Part B— Verify the Available Connection Strength by Checking Individual Limit States*

*Connection Eccentricity*

Check the eccentricity of the connection. From AISC *Manual* Figure 10-15, eccentricity does not need to be considered at the bolt group on the supported beam web leg of the angle if $e \leq 3$ in.

For the 4 in. angle leg attached to the supported beam:

$e = 2¾$ in. < 3.00 in., therefore, eccentricity does not need to be considered for this leg.

As discussed in AISC *Manual* Part 10, eccentricity must be considered in the design of welds for single-angle connections.

*Available Weld Strength*

The available weld strength is determined using AISC *Manual* Table 8-10 for Angle = 0°:

$l = 11½$ in.
$kl = 4$ in.
$$k = \frac{4 \text{ in.}}{11½ \text{ in.}}$$
$$= 0.348$$

Interpolating from AISC *Manual* Table 8-10:

$x = 0.0456$

$$al + xl = kl + \frac{t_w}{2}$$

Solving for $a$:

$$a = k + \frac{t_w}{2l} - x$$
$$= 0.348 + \frac{0.380 \text{ in.}}{2(11½ \text{ in.})} - 0.0456$$
$$= 0.319$$

Interpolating from AISC *Manual* Table 8-10:

$C = 2.19$

From AISC *Manual* Equation 8-30, with $C_1 = 1.00$ and $D = 3$ sixteenths:

---

# IIA-289

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi CC_1Dl$ | $\frac{R_n}{\Omega} = \frac{CC_1Dl}{\Omega}$ |
|  |  |
| $= 0.75(2.19)(1.00)(3)(11½ \text{ in.})$ | $= \frac{(2.19)(1.00)(3)(11½ \text{ in.})}{2.00}$ |
|  |  |
| $= 56.7 \text{ kips} > 54.0 \text{ kips} \quad \textbf{o.k.}$ | $= 37.8 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ |

*Shear Strength of Angle*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the angle is determined as follows:

$$A_{gv} = lt$$
$$= (11½ \text{ in.})(⅜ \text{ in.})$$
$$= 4.31 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(4.31 \text{ in.}^2)$$
$$= 129 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(129 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{129 \text{ kips}}{1.50}$ |
|  |  |
| $= 129 \text{ kips} > 54.0 \text{ kips} \quad \textbf{o.k.}$ | $= 86.0 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the angle is determined using the net area determined in accordance with AISC *Specification* Section B4.3b.

$$A_{nv} = [l - n(d_h + \frac{1}{16} \text{ in.})]t$$
$$= [11½ \text{ in.} - 4(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](⅜ \text{ in.})$$
$$= 3.00 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(3.00 \text{ in.}^2)$$
$$= 117 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(117 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{117 \text{ kips}}{2.00}$ |
|  |  |
| $= 87.8 \text{ kips} > 54.0 \text{ kips} \quad \textbf{o.k.}$ | $= 58.5 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ |

---

# IIA-290

*Block Shear Rupture of Angle*

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture of the angle is determined as follows.

$$R_{bsv} = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$ (from *Spec.* Eq. J4-5)

where

$$A_{gv} = (l - l_{ev})t$$
$$= (11½ \text{ in.} - 1¼ \text{ in.})(⅜ \text{ in.})$$
$$= 3.84 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (n - 0.5)(d_h + \frac{1}{16} \text{ in.})t$$
$$= 3.84 \text{ in.}^2 - (4 - 0.5)(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})(⅜ \text{ in.})$$
$$= 2.69 \text{ in.}^2$$

$$A_{nt} = [l_{eh} - 0.5(d_h + \frac{1}{16} \text{ in.})]t$$
$$= [1¼ \text{ in.} - 0.5(1\frac{3}{16} \text{ in.} + \frac{1}{16} \text{ in.})](⅜ \text{ in.})$$
$$= 0.305 \text{ in.}^2$$

$U_{bs} = 1.0$

and

$$R_{bsv} = 0.60(65 \text{ ksi})(2.69 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.305 \text{ in.}^2) \leq 0.60(50 \text{ ksi})(3.84 \text{ in.}^2) + 1.0(65 \text{ ksi})(0.305 \text{ in.}^2)$$
$$= 125 \text{ kips} < 135 \text{ kips}$$

Therefore:

$R_{bsv} = 125$ kips

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture of the angle is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_{bsv} = 0.75(125 \text{ kips})$ | $\frac{R_{bsv}}{\Omega} = \frac{125 \text{ kips}}{2.00}$ |
|  |  |
| $= 93.8 \text{ kips} > 54.0 \text{ kips} \quad \textbf{o.k.}$ | $= 62.5 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ |

*Available Shear Transfer Strength at Bolt Holes*

From AISC *Manual* Table 7-1, the available shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9$ kips | $\frac{r_n}{\Omega} = 11.9$ kips |

---

# IIA-291

The available bearing and tearout strength of the angle at the top edge bolt is determined using AISC *Manual* Table 7-5, with $l_e = 1¼$ in., as follows:

| LRFD | ASD |
|------|-----|
| $\phi r_n = (49.4 \text{ kips/in.})(⅜ \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kips/in.})(⅜ \text{ in.})$ |
| $= 18.5$ kips | $= 12.3$ kips |

The available bearing and tearout strength of the angle at the interior bolts (not adjacent to the edge) is determined using AISC *Manual* Table 7-4 with $s = 3$ in.

| LRFD | ASD |
|------|-----|
| $\phi r_n = (87.8 \text{ kips/in.})(⅜ \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(⅜ \text{ in.})$ |
| $= 32.9$ kips | $= 21.9$ kips |

The available bearing and tearout strength for all bolts in the beam web is determined using AISC *Manual* Table 7-4 with $s = 3$ in.

| LRFD | ASD |
|------|-----|
| $\phi r_n = (87.8 \text{ kips/in.})(0.380 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(0.380 \text{ in.})$ |
| $= 33.4$ kips | $= 22.2$ kips |

The available shear transfer strength is controlled by the available bolt shear strength:

| LRFD | ASD |
|------|-----|
| $\phi R_n = n\phi r_n$ | $\frac{R_n}{\Omega} = n\frac{r_n}{\Omega}$ |
| $= 4(17.9 \text{ kips})$ | $= 4(11.9 \text{ kips})$ |
| $= 71.6 \text{ kips} > 54.0 \text{ kips} \quad \textbf{o.k.}$ | $= 47.6 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ |

*Available Beam Web Strength*

Because the beam is not coped, the limit states of block shear rupture and shear rupture of the beam are not applicable. The beam web is adequate for the required loading.

*Support Thickness*

The minimum support thickness that matches the column flange strength to the $\frac{3}{16}$ in. fillet weld strength is:

$$t_{min} = \frac{3.09D}{F_u}$$ (*Manual* Eq. 9-6)
$$= \frac{3.09(3)}{65 \text{ ksi}}$$
$$= 0.143 \text{ in.} < 0.710 \text{ in.} \quad \textbf{o.k.}$$

*Conclusion*

The available connection strength is:

---

# IIA-292

| LRFD | ASD |
|------|-----|
| $\phi R_n = 56.7 \text{ kips} > 54.0 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 37.8 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ |

The connection is found to be adequate as given for the applied load.

---

# IIA-293

## EXAMPLE II.A-30 ALL-BOLTED TEE CONNECTION (BEAM-TO-COLUMN FLANGE)

**Given:**

Verify the available strength of an all-bolted tee connection between an ASTM A992/A992M W16×50 beam and an ASTM A992/A992M W14×90 column flange, as shown in Figure II.A-30-1, to support the following beam end reactions:

$$R_D = 6 \text{ kips}$$
$$R_L = 18 \text{ kips}$$

Use an ASTM A992/A992M WT5×22.5 with a four-bolt connection.

![Connection diagram showing W14×90 column with WT5×22.5 tee connecting to W16×50 beam. Left view shows elevation with dimensions: a = 3.80", l_eh = 1¼", 1¼" spacing, 3@3" = 9" vertical bolt spacing, 1¼" edge distance. Right view shows plan view with 2¾" dimensions on each side of centerline and ¾" dia. Group 120, thread condition N, std. holes bolts. Beam depth l = 11½".]

*Fig. II.A-30-1. Connection geometry for Example II.A-30.*

**Solution:**

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam, column, and tee
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Tables 1-1 and 1-8, the geometric properties are as follows:

Beam
W16×50
$d = 16.3$ in.
$t_w = 0.380$ in.
$t_f = 0.630$ in.

---

# IIA-294

Column
W14×90
$t_f = 0.710$ in.

Tee
WT5×22.5
$d$ = 5.05 in.
$t_{sw}$ = 0.350 in.
$b_f$ = 8.02 in.
$t_f$ = 0.620 in.
$k_1$ = $1\frac{3}{16}$ in. (see W10×45 in AISC *Manual* Table 1-1)
$k_{des}$ = 1.12 in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(6 \text{ kips}) + 1.6(18 \text{ kips})$ | $R_a = 6 \text{ kips} + 18 \text{ kips}$ |
| $= 36.0$ kips | $= 24.0$ kips |

From AISC *Manual* Part 10, eccentricity must be considered when determining the available strength of tee connections. The bolts attaching the tee flange to the support must be designed for the shear, $R_u$. Also, the bolts through the tee stem must be designed for the shear and the eccentric moment, $R_u a$, where $a$ is the distance from the face of the support to the centroid of the bolt group through the tee stem.

*Rotational Ductility*

See rotational ductility discussion at the beginning of AISC *Manual* Part 9. Because the tee is bolted to the support, AISC *Manual* Equation 9-52 will give the minimum diameter for bolts through the tee flange to ensure rotational ductility.

The flexible width, $b$, is determined using AISC *Manual* Figure 9-6(b). Note that the bolt gage is centered on the column and supported beam centerline and is not located symmetrically with respect to the centerline of the tee. The smaller $b$ is used in the following calculations

$$b = 2¾ \text{ in.} - \frac{t_{sw}}{2} - \frac{t_w}{2} - k_1$$
$$= 2¾ \text{ in.} - \frac{0.350 \text{ in.}}{2} - \frac{0.380 \text{ in.}}{2} - 1\frac{3}{16} \text{ in.}$$
$$= 1.57 \text{ in.}$$

The tributary length per bolt, $p$, is determined using AISC *Manual* Figure 9-4. Note that the larger $p$ dimension for a non-edge bolt is used in the following calculations.

$$s/2 = 3.00 \text{ in.}/2$$
$$= 1.50 \text{ in.}$$
$$1.75b = 1.75(1.57 \text{ in.})$$
$$= 2.75 \text{ in.}$$

Because $s/2 \leq 1.75b$:

$$p = s$$
$$= 3.00 \text{ in.}$$

---

# IIA-295

$$d_{min} = 0.0941t_f\sqrt{\frac{F_yp}{b}\left(\frac{b^2}{t^2} + 2\right)} \leq 0.115\sqrt{F_yt_{sw}}$$ (*Manual* Eq. 9-52)

$$= 0.0941(0.620 \text{ in.})\sqrt{\frac{(50 \text{ ksi})(3.00 \text{ in.})}{1.57 \text{ in.}}\left[\frac{(1.57 \text{ in.})^2}{(11½ \text{ in.})^2} + 2\right]} \leq 0.115\sqrt{(50 \text{ ksi})(0.350 \text{ in.})}$$

$$= 0.810 \text{ in.} > 0.481 \text{ in.}$$
$$= 0.481 \text{ in.}$$

Therefore:

$$d_{min} = 0.481 \text{ in.} < ¾ \text{ in.} \quad \textbf{o.k.}$$

Because the tee stem is bolted to the supported beam, AISC *Manual* Part 9 provides the following as an alternate method to ensure rotational ductility of the connection. Either the tee stem or beam web thickness needs to satisfy the following limit:

$$t_w \text{ or } t_{sw} \leq \frac{d}{2} + \frac{3}{16} \text{ in.}$$ (*Manual* Eq. 9-53)
$$= \frac{¾ \text{ in.}}{2} + \frac{3}{16} \text{ in.}$$
$$= 0.438 \text{ in.}$$

Both the tee stem ($t_w = 0.350$ in.) and beam web ($t_w = 0.380$ in.) satisfy this limit.

*Available Shear Transfer Strength at Bolt Holes at Beam Web*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength determined in accordance with AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the tee stem at the bolt hole, and (3) the available bearing or tearout strength of the beam web or support element at the bolt hole.

$$a = d - l_{eh}$$
$$= 5.05 \text{ in.} - 1¼ \text{ in.}$$
$$= 3.80 \text{ in.}$$

From AISC *Manual* Table 7-6 for Angle = 0°, with $s = 3$ in., $n = 4$, and interpolating for $e_v = a = 3.80$ in.:

$$C = 2.45$$

From AISC *Manual* Table 7-1, the available shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9$ kips/bolt | $\frac{r_n}{\Omega} = 11.9$ kips/bolt |

The available bearing and tearout strength of the tee stem at the bottom edge bolt is determined using AISC *Manual* Table 7-5, with $l_e = 1¼$ in., as follows:

---

# IIA-296

| LRFD | ASD |
|------|-----|
| $\phi r_n = (49.4 \text{ kips/in.})(0.350 \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kips/in.})(0.350 \text{ in.})$ |
| $= 17.3$ kips/bolt | $= 11.5$ kips/bolt |

The available bearing and tearout strength of the tee stem at the interior bolts (not adjacent to the edge) is determined using AISC *Manual* Table 7-4 with $s = 3$ in.

| LRFD | ASD |
|------|-----|
| $\phi r_n = (87.8 \text{ kips/in.})(0.350 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(0.350 \text{ in.})$ |
| $= 30.7$ kips/bolt | $= 20.5$ kips/bolt |

The available bearing and tearout strength for all bolts in the beam web is determined using AISC *Manual* Table 7-4 with $s = 3$ in.

| LRFD | ASD |
|------|-----|
| $\phi r_n = (87.8 \text{ kips/in.})(0.380 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(0.380 \text{ in.})$ |
| $= 33.4$ kips/bolt | $= 22.2$ kips/bolt |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the tee stem for a non-edge bolt, and the available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min\begin{Bmatrix}17.9 \text{ kips,} \\ 30.7 \text{ kips,} \\ 33.4 \text{ kips}\end{Bmatrix}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{Bmatrix}11.9 \text{ kips,} \\ 20.5 \text{ kips,} \\ 44.5 \text{ kips}\end{Bmatrix}$ |
| $= 17.9$ kips | $= 11.9$ kips |

At the middle connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the tee stem for a non-edge bolt, and the available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,mid} = \min\begin{Bmatrix}17.9 \text{ kips,} \\ 30.7 \text{ kips,} \\ 33.4 \text{ kips}\end{Bmatrix}$ | $\frac{r_{n,mid}}{\Omega} = \min\begin{Bmatrix}11.9 \text{ kips,} \\ 20.5 \text{ kips,} \\ 22.2 \text{ kips}\end{Bmatrix}$ |
| $= 17.9$ kips | $= 11.9$ kips |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the tee web for an edge bolt, and the available bearing and tearout strength of the beam web for a non-edge bolt:

---

# IIA-297

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min\begin{Bmatrix}17.9 \text{ kips,} \\ 17.3 \text{ kips,} \\ 33.4 \text{ kips}\end{Bmatrix}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{Bmatrix}11.9 \text{ kips,} \\ 11.5 \text{ kips,} \\ 22.2 \text{ kips}\end{Bmatrix}$ |
| $= 17.3$ kips | $= 11.5$ kips |

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = \left(\frac{C}{n}\right)\left[\phi r_{n,top} + \phi r_{n,mid}\left(n - 2\right) + \phi r_{n,bot}\right]$ | $\frac{R_n}{\Omega} = \left(\frac{C}{n}\right)\left[\frac{r_{n,top}}{\Omega} + \frac{r_{n,mid}}{\Omega}\left(n - 2\right) + \frac{r_{n,bot}}{\Omega}\right]$ |
| $= \left(\frac{2.45}{4}\right)\left[17.9 \text{ kips} + 17.9 \text{ kips}\left(4 - 2\right) + 17.3 \text{ kips}\right]$ | $= \left(\frac{2.45}{4}\right)\left[11.9 \text{ kips} + 11.9 \text{ kips}\left(4 - 2\right) + 11.5 \text{ kips}\right]$ |
| $= 43.5 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ | $= 28.9 \text{ kips} > 24.0 \text{ kips} \quad \textbf{o.k.}$ |

*Available Flexural Strength of Stem*

The available flexural yielding and rupture strength of the stem is checked from the bolt line to the face of the support.

| LRFD | ASD |
|------|-----|
| $M_u = P_u a$ | $M_a = P_a a$ |
| $= (36.0 \text{ kips})(3.80 \text{ in.})$ | $= (24.0 \text{ kips})(3.80 \text{ in.})$ |
| $= 137$ kip-in. | $= 91.2$ kip-in. |

The available flexural yielding strength of the tee stem is determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi M_n = \phi F_y Z_x$ | $\frac{M_n}{\Omega} = \frac{F_y Z_x}{\Omega}$ |
| $= 0.90(50 \text{ ksi})\left[\frac{(0.350 \text{ in.})(11½ \text{ in.})^2}{4}\right]$ | $= \left(\frac{50 \text{ ksi}}{1.67}\right)\left[\frac{(0.350 \text{ in.})(11½ \text{ in.})^2}{4}\right]$ |
| $= 521$ kip-in. $> 137$ kip-in. $\quad \textbf{o.k.}$ | $= 346$ kip-in. $> 91.2$ kip-in. $\quad \textbf{o.k.}$ |

The available flexural rupture strength of the tee stem is determined as follows:

$$Z_{net} = (0.350 \text{ in.})\left[\frac{(11½ \text{ in.})^2}{4} - 2\left(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)(4.50 \text{ in.}) - 2\left(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)(1.50 \text{ in.})\right]$$

$$= 7.90 \text{ in.}^3$$

$$M_n = F_u Z_{net}$$ (*Manual* Eq. 9-8)
$$= (65 \text{ ksi})\left(7.90 \text{ in.}^3\right)$$
$$= 514 \text{ kip-in.}$$

---

# IIA-298

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi M_n = 0.75(514 \text{ kip-in.})$ | $\frac{M_n}{\Omega} = \frac{514 \text{ kip-in.}}{2.00}$ |
| $= 386$ kip-in. $> 137$ kip-in. $\quad \textbf{o.k.}$ | $= 257$ kip-in. $> 91.2$ kip-in. $\quad \textbf{o.k.}$ |

*Shear Strength of Stem*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the tee stem is determined as follows:

$$A_{gv} = lt_{sw}$$
$$= (11½ \text{ in.})(0.350 \text{ in.})$$
$$= 4.03 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})\left(4.03 \text{ in.}^2\right)$$
$$= 121 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(121 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{121 \text{ kips}}{1.50}$ |
| $= 121 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ | $= 80.7 \text{ kips} > 24.0 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the tee stem is determined using the net area determined in accordance with AISC *Specification* Section B4.3b.

$$A_{nv} = \left[l - n\left(d_h + \frac{1}{16} \text{ in.}\right)\right]t_{sw}$$
$$= \left[11½ \text{ in.} - 4\left(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right](0.350 \text{ in.})$$
$$= 2.80 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})\left(2.80 \text{ in.}^2\right)$$
$$= 109 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(109 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{109 \text{ kips}}{2.00}$ |
| $= 81.8 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ | $= 54.5 \text{ kips} > 24.0 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture of Stem*

The nominal strength for the limit state of block shear rupture is given by AISC *Specification* Section J4.3.

---

# IIA-299

$$R_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$ (*Spec.* Eq. J4-5)

The available block shear rupture strength of the tee stem is determined as follows, using AISC *Manual* Tables 9-3a, 9-3b, and 9-3c, and AISC *Specification* Equation J4-5, with $n = 4$, $l_{eh} = l_{ev} = 1¼$ in., and $U_{bs} = 1.0$.

| LRFD | ASD |
|------|-----|
| Tension rupture component from AISC *Manual* Table 9-3a: | Tension rupture component from AISC *Manual* Table 9-3a: |
|  |  |
| $\frac{\phi F_u A_{nt}}{t} = 39.6$ kips/in. | $\frac{F_u A_{nt}}{\Omega t} = 26.4$ kips/in. |
|  |  |
| Shear yielding component from AISC *Manual* Table 9-3b: | Shear yielding component from AISC *Manual* Table 9-3b: |
|  |  |
| $\frac{\phi 0.60F_y A_{gv}}{t} = 231$ kips/in. | $\frac{0.60F_y A_{gv}}{\Omega t} = 154$ kips/in. |
|  |  |
| Shear rupture component from AISC *Manual* Table 9-3c: | Shear rupture component from AISC *Manual* Table 9-3c: |
|  |  |
| $\frac{\phi 0.60F_u A_{nv}}{t} = 210$ kips/in. | $\frac{0.60F_u A_{nv}}{\Omega t} = 140$ kips/in. |
|  |  |
| The design block shear rupture strength is: | The allowable block shear rupture strength is: |
|  |  |
| $\phi R_n = \phi 0.60F_u A_{nv} + \phi U_{bs}F_u A_{nt}$ | $\frac{R_n}{\Omega} = \frac{0.60F_u A_{nv}}{\Omega} + \frac{U_{bs}F_u A_{nt}}{\Omega}$ |
| $\leq \phi 0.60F_y A_{gv} + \phi U_{bs}F_u A_{nt}$ | $\leq \frac{0.60F_y A_{gv}}{\Omega} + \frac{U_{bs}F_u A_{nt}}{\Omega}$ |
| $= (0.350 \text{ in.})\left[210 \text{ kips/in.} + (1.0)(39.6 \text{ kips/in.})\right]$ | $= (0.350 \text{ in.})\left[140 \text{ kips/in.} + (1.0)(26.4 \text{ kips/in.})\right]$ |
| $\leq (0.350 \text{ in.})\left[231 \text{ kips/in.} + (1.0)(39.6 \text{ kips/in.})\right]$ | $\leq (0.350 \text{ in.})\left[154 \text{ kips/in.} + (1.0)(26.4 \text{ kips/in.})\right]$ |
| $= 87.4 \text{ kips} < 94.7 \text{ kips}$ | $= 58.2 \text{ kips} < 63.1 \text{ kips}$ |
|  |  |
| Therefore: | Therefore: |
|  |  |
| $\phi R_n = 87.4 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 58.2 \text{ kips} > 24.0 \text{ kips} \quad \textbf{o.k.}$ |

*Available Shear Transfer Strength at Bolt Holes at Column Flange*

From AISC *Manual* Table 7-1, the available shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9$ kips/bolt | $\frac{r_n}{\Omega} = 11.9$ kips/bolt |

The available bearing and tearout strength of the tee flange at the top edge bolt is determined using AISC *Manual* Table 7-5, with $l_e = 1¼$ in., as follows:

---

# IIA-300

| LRFD | ASD |
|------|-----|
| $\phi r_n = (49.4 \text{ kips/in.})(0.620 \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kips/in.})(0.620 \text{ in.})$ |
| $= 30.6$ kips/bolt | $= 20.4$ kips/bolt |

The available bearing and tearout strength of the tee flange at the interior bolts (not adjacent to the edge) is determined using AISC *Manual* Table 7-4 with $s = 3$ in.

| LRFD | ASD |
|------|-----|
| $\phi r_n = (87.8 \text{ kips/in.})(0.620 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(0.620 \text{ in.})$ |
| $= 54.4$ kips/bolt | $= 36.3$ kips/bolt |

The available bearing and tearout strength for all bolts in the column flange is determined using AISC *Manual* Table 7-4 with $s = 3$ in.

| LRFD | ASD |
|------|-----|
| $\phi r_n = (87.8 \text{ kips/in.})(0.710 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(0.710 \text{ in.})$ |
| $= 62.3$ kips/bolt | $= 41.5$ kips/bolt |

The available shear transfer strength is controlled by the available bolt shear strength:

| LRFD | ASD |
|------|-----|
| $\phi R_n = n\phi r_n$ | $\frac{R_n}{\Omega} = n\frac{r_n}{\Omega}$ |
| $= 8(17.9 \text{ kips})$ | $= 8(11.9 \text{ kips})$ |
| $= 143 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ | $= 95.2 \text{ kips} > 24.0 \text{ kips} \quad \textbf{o.k.}$ |

The shear yielding, shear rupture, and block shear rupture of the tee flange are okay by inspection because the above calculations have shown the tee stem to have sufficient strength.

Note: Although the edge distance ($a = 0.895$ in.) for one row of bolts in the tee flange does not meet the minimum value indicated in AISC *Specification* Table J3.4, based on footnote [a], the edge distance provided is acceptable because the provisions of AISC *Specification* Section J3.11 and J4 have been met in this case.

*Conclusion*

The connection is found to be adequate as given for the applied load.

---

# IIA-301

## EXAMPLE II.A-31 BOLTED/WELDED TEE CONNECTION (BEAM-TO-COLUMN FLANGE)

**Given:**

Verify the available strength of a tee connection bolted to an ASTM A992/A992M W16×50 supported beam and welded to an ASTM A992/A992M W14×90 supporting column flange, as shown in Figure II.A-31-1, to support the following beam end reactions:

$$R_D = 6 \text{ kips}$$
$$R_L = 18 \text{ kips}$$

Use 70-ksi electrodes. Use an ASTM A992/A992M WT5×22.5 with a four-bolt connection to the beam web.

![Connection diagram showing W14×90 column with WT5×22.5 tee welded to column flange and bolted to W16×50 beam. Left view shows elevation with dimensions: a = 3.80", l_eh = 1¼", 1¼" spacing, 3@3" = 9" vertical spacing, 1¼" edge distance. Right view shows plan view with ¼ in. and ½ in. fillet weld sizes, ¾" dia. Group 120 bolts with thread condition N in standard holes.]

*Fig. II.A-31-1. Connection geometry for Example II.A-31.*

**Solution:**

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam, column, and tee
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Tables 1-1 and 1-8, the geometric properties are as follows:

Beam
W16×50
$d = 16.3$ in.
$t_w = 0.380$ in.
$t_f = 0.630$ in.

Column
W14×90
$t_f = 0.710$ in.

---

# IIA-302

Tee
WT5×22.5
$d$ = 5.05 in.
$b_f$ = 8.02 in.
$t_f$ = 0.620 in.
$t_{sw}$ = 0.350 in.
$k_1$ = $1\frac{3}{16}$ in. (see W10×45 in AISC *Manual* Table 1-1)
$k_{des}$ = 1.12 in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(6 \text{ kips}) + 1.6(18 \text{ kips})$ | $R_a = 6 \text{ kips} + 18 \text{ kips}$ |
| $= 36.0$ kips | $= 24.0$ kips |

From AISC *Manual* Part 10, eccentricity must be considered when determining the available strength of tee connections. The welds attaching the tee flange to the support must be designed for the shear, $R_u$. Also, the bolts through the tee stem must be designed for the shear and the eccentric moment, $R_u a$, where $a$ is the distance from the face of the support to the centroid of the bolt group through the tee stem.

*Rotational Ductility*

See rotational ductility discussion at the beginning of AISC *Manual* Part 9. Because the tee is welded to the support, AISC *Manual* Equation 9-51 will give the minimum size of the tee flange to ensure rotational ductility.

The flexible width, $b$, is determined using AISC *Manual* Figure 9-6(a), which is the cantilever length taken from the edge of the tee fillet:

$$b = \frac{b_f - 2k_1}{2}$$
$$= \frac{8.02 \text{ in.} - 2\left(\frac{13}{16} \text{ in.}\right)}{2}$$
$$= 3.20 \text{ in.}$$

$$w_{min} = 0.0155\frac{F_y t_f^2}{b}\left(\frac{b^2}{l^2} + 2\right) \leq \left(\frac{5}{8}\right)t_{sw}$$ (*Manual* Eq. 9-51)

$$= 0.0155\left[\frac{(50 \text{ ksi})(0.620 \text{ in.})^2}{3.20 \text{ in.}}\right]\left[\frac{(3.20 \text{ in.})^2}{(11½ \text{ in.})^2} + 2\right] \leq \left(\frac{5}{8}\right)(0.350 \text{ in.})$$

$$= 0.193 \text{ in.} < 0.219 \text{ in.}$$
$$= 0.193 \text{ in.}$$

For a ¼ in. fillet weld:

$$0.250 \text{ in.} > 0.193 \text{ in.} \quad \textbf{o.k.}$$

Because the tee stem is bolted to the supported beam, AISC *Manual* Part 9 provides the following as an alternate method to ensure rotational ductility of the connection. Either the tee stem or beam web thickness needs to satisfy the following limit:

---

# IIA-303

$$t_w \text{ or } t_{sw} \leq \frac{d}{2} + \frac{3}{16} \text{ in.}$$ (*Manual* Eq. 9-53)
$$= \frac{¾ \text{ in.}}{2} + \frac{3}{16} \text{ in.}$$
$$= 0.438 \text{ in.}$$

Both the tee stem ($t_w = 0.350$ in.) and beam web ($t_w = 0.380$ in.) satisfy this limit.

*Weld Design*

From AISC *Manual* Table 10-2, with $n = 4$, $l = 11½$ in., and Welds B = ¼ in.:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 99.7 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 66.5 \text{ kips} > 24.0 \text{ kips} \quad \textbf{o.k.}$ |

Use ¼ in. fillet welds.

*Supporting Column Flange*

From AISC *Manual* Table 10-2, with $n = 4$, $l = 11½$ in., and Welds B = ¼ in., the minimum support thickness is 0.190 in.

$$t_f = 0.710 \text{ in.} > 0.190 \text{ in.} \quad \textbf{o.k.}$$

*Available Shear Transfer Strength at Bolt Holes at Beam Web*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength determined in accordance with AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the tee stem at the bolt hole, and (3) the available bearing or tearout strength of the beam web or support element at the bolt hole.

$$a = d - l_{eh}$$
$$= 5.05 \text{ in.} - 1¼ \text{ in.}$$
$$= 3.80 \text{ in.}$$

From AISC *Manual* Table 7-6 for Angle = 0°, with $s = 3$ in., $n = 4$, and interpolating for $e_v = a = 3.80$ in.:

$$C = 2.45$$

From AISC *Manual* Table 7-1, the available shear strength per bolt for ¾-in-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9$ kips/bolt | $\frac{r_n}{\Omega} = 11.9$ kips/bolt |

The available bearing and tearout strength of the tee stem at the bottom edge bolt is determined using AISC *Manual* Table 7-5, with $l_e = 1¼$ in., as follows:

---

# IIA-304

| LRFD | ASD |
|------|-----|
| $\phi r_n = (49.4 \text{ kips/in.})(0.350 \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kips/in.})(0.350 \text{ in.})$ |
| $= 17.3$ kips/bolt | $= 11.5$ kips/bolt |

The available bearing and tearout strength of the tee stem at the interior bolts (not adjacent to the edge) is determined using AISC *Manual* Table 7-4 with $s = 3$ in.

| LRFD | ASD |
|------|-----|
| $\phi r_n = (87.8 \text{ kips/in.})(0.350 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(0.350 \text{ in.})$ |
| $= 30.7$ kips/bolt | $= 20.5$ kips/bolt |

The available bearing and tearout strength for all bolts in the beam web is determined using AISC *Manual* Table 7-4 with $s = 3$ in.

| LRFD | ASD |
|------|-----|
| $\phi r_n = (87.8 \text{ kips/in.})(0.380 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kips/in.})(0.380 \text{ in.})$ |
| $= 33.4$ kips/bolt | $= 22.2$ kips/bolt |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the tee stem for a non-edge bolt, and the available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min\begin{Bmatrix}17.9 \text{ kips,} \\ 30.7 \text{ kips,} \\ 33.4 \text{ kips}\end{Bmatrix}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{Bmatrix}11.9 \text{ kips,} \\ 20.5 \text{ kips,} \\ 22.2 \text{ kips}\end{Bmatrix}$ |
| $= 17.9$ kips | $= 11.9$ kips |

At the middle connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the tee stem for a non-edge bolt, and the available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,mid} = \min\begin{Bmatrix}17.9 \text{ kips,} \\ 30.7 \text{ kips,} \\ 33.4 \text{ kips}\end{Bmatrix}$ | $\frac{r_{n,mid}}{\Omega} = \min\begin{Bmatrix}11.9 \text{ kips,} \\ 20.5 \text{ kips,} \\ 22.2 \text{ kips}\end{Bmatrix}$ |
| $= 17.9$ kips | $= 11.9$ kips |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the tee web for an edge bolt, and the available bearing and tearout strength of the beam web for a non-edge bolt:

---

# IIA-305

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min\begin{Bmatrix}17.9 \text{ kips,} \\ 17.3 \text{ kips,} \\ 33.4 \text{ kips}\end{Bmatrix}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{Bmatrix}11.9 \text{ kips,} \\ 11.5 \text{ kips,} \\ 22.2 \text{ kips}\end{Bmatrix}$ |
| $= 17.3$ kips | $= 11.5$ kips |

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = \frac{C}{n}\left[\phi r_{n,top} + \phi r_{n,mid}\left(n - 2\right) + \phi r_{n,bot}\right]$ | $\frac{R_n}{\Omega} = \frac{C}{n}\left[\frac{r_{n,top}}{\Omega} + \frac{r_{n,mid}}{\Omega}\left(n - 2\right) + \frac{r_{n,bot}}{\Omega}\right]$ |
| $= \left(\frac{2.45}{4}\right)\left[17.9 \text{ kips} + \left(17.9 \text{ kips}\right)\left(4 - 2\right) + 17.3 \text{ kips}\right]$ | $= \left(\frac{2.45}{4}\right)\left[11.9 \text{ kips} + \left(11.9 \text{ kips}\right)\left(4 - 2\right) + 11.5 \text{ kips}\right]$ |
| $= 43.5 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ | $= 28.9 \text{ kips} > 24.0 \text{ kips} \quad \textbf{o.k.}$ |

*Available Flexural Strength of Tee Stem*

The required flexural strength of the tee stem is determined as follows:

| LRFD | ASD |
|------|-----|
| $M_u = P_u e_b$ | $M_a = P_a e_b$ |
| $= (36.0 \text{ kips})(3.80 \text{ in.})$ | $= (24.0 \text{ kips})(3.80 \text{ in.})$ |
| $= 137$ kip-in. | $= 91.2$ kip-in. |

The available flexural yielding strength of the tee stem is determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi M_n = \phi F_y Z_x$ | $\frac{M_n}{\Omega} = \frac{F_y Z_x}{\Omega}$ |
| $= 0.90(50 \text{ ksi})\left[\frac{(0.350 \text{ in.})(11½ \text{ in.})^2}{4}\right]$ | $= \frac{50 \text{ ksi}}{1.67}\left[\frac{(0.350 \text{ in.})(11½ \text{ in.})^2}{4}\right]$ |
| $= 521$ kip-in. $> 137$ kip-in. $\quad \textbf{o.k.}$ | $= 346$ kip-in. $> 91.2$ kip-in. $\quad \textbf{o.k.}$ |

The available flexural rupture strength of the tee stem is determined as follows:

$$Z_{net} = (0.350 \text{ in.})\left[\frac{(11½ \text{ in.})^2}{4} - 2\left(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)(4.50 \text{ in.}) - 2\left(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)(1.50 \text{ in.})\right]$$

$$= 7.90 \text{ in.}^3$$

$$M_n = F_u Z_{net}$$ (*Manual* Eq. 9-8)
$$= (65 \text{ ksi})\left(7.90 \text{ in.}^3\right)$$
$$= 514 \text{ kip-in.}$$

---

# IIA-306

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi M_n = 0.75(514 \text{ kip-in.})$ | $\frac{M_n}{\Omega} = \frac{514 \text{ kip-in.}}{2.00}$ |
| $= 386$ kip-in. $> 137$ kip-in. $\quad \textbf{o.k.}$ | $= 257$ kip-in. $> 91.2$ kip-in. $\quad \textbf{o.k.}$ |

*Shear Strength of Stem*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the tee stem is determined as follows:

$$A_{gv} = lt_{sw}$$
$$= (11½ \text{ in.})(0.350 \text{ in.})$$
$$= 4.03 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})\left(4.03 \text{ in.}^2\right)$$
$$= 121 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(121 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{121 \text{ kips}}{1.50}$ |
| $= 121 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ | $= 80.7 \text{ kips} > 24.0 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the tee stem is determined using the net area calculated using AISC *Specification* Section B4.3b.

$$A_{nv} = \left[l - n\left(d_h + \frac{1}{16} \text{ in.}\right)\right]t_{sw}$$
$$= \left[11½ \text{ in.} - 4\left(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right](0.350 \text{ in.})$$
$$= 2.80 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})\left(2.80 \text{ in.}^2\right)$$
$$= 109 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(109 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{109 \text{ kips}}{2.00}$ |
| $= 81.8 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ | $= 54.5 \text{ kips} > 24.0 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture of Stem*

The nominal strength for the limit state of block shear rupture is given by AISC *Specification* Section J4.3.

---

# IIA-307

$$R_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$ (*Spec.* Eq. J4-5)

The available block shear rupture strength of the tee stem is determined as follows, using AISC *Manual* Tables 9-3a, 9-3b, and 9-3c, and AISC *Specification* Equation J4-5, with $n = 4$, $l_{eh} = l_{ev} = 1¼$ in., and $U_{bs} = 1.0$.

| LRFD | ASD |
|------|-----|
| Tension rupture component from AISC *Manual* Table 9-3a: | Tension rupture component from AISC *Manual* Table 9-3a: |
|  |  |
| $\frac{\phi F_u A_{nt}}{t} = 39.6$ kips/in. | $\frac{F_u A_{nt}}{\Omega t} = 26.4$ kips/in. |
|  |  |
| Shear yielding component from AISC *Manual* Table 9-3b: | Shear yielding component from AISC *Manual* Table 9-3b: |
|  |  |
| $\frac{\phi 0.60F_y A_{gv}}{t} = 231$ kips/in. | $\frac{0.60F_y A_{gv}}{\Omega t} = 154$ kips/in. |
|  |  |
| Shear rupture component from AISC *Manual* Table 9-3c: | Shear rupture component from AISC *Manual* Table 9-3c: |
|  |  |
| $\frac{\phi 0.60F_u A_{nv}}{t} = 210$ kips/in. | $\frac{0.60F_u A_{nv}}{\Omega t} = 140$ kips/in. |
|  |  |
| The design block shear rupture strength is: | The allowable block shear rupture strength is: |
|  |  |
| $\phi R_n = \phi 0.60F_u A_{nv} + \phi U_{bs}F_u A_{nt}$ | $\frac{R_n}{\Omega} = \frac{0.60F_u A_{nv}}{\Omega} + \frac{U_{bs}F_u A_{nt}}{\Omega}$ |
| $\leq \phi 0.60F_y A_{gv} + \phi U_{bs}F_u A_{nt}$ | $\leq \frac{0.60F_y A_{gv}}{\Omega} + \frac{U_{bs}F_u A_{nt}}{\Omega}$ |
| $= (0.350 \text{ in.})\left[210 \text{ kips/in.} + (1.0)(39.6 \text{ kips/in.})\right]$ | $= (0.350 \text{ in.})\left[140 \text{ kips/in.} + (1.0)(26.4 \text{ kips/in.})\right]$ |
| $\leq (0.350 \text{ in.})\left[231 \text{ kips/in.} + (1.0)(39.6 \text{ kips/in.})\right]$ | $\leq (0.350 \text{ in.})\left[154 \text{ kips/in.} + (1.0)(26.4 \text{ kips/in.})\right]$ |
| $= 87.4 \text{ kips} < 94.7 \text{ kips}$ | $= 58.2 \text{ kips} < 63.1 \text{ kips}$ |
|  |  |
| Therefore: | Therefore: |
|  |  |
| $\phi R_n = 87.4 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 58.2 \text{ kips} > 24.0 \text{ kips} \quad \textbf{o.k.}$ |

*Conclusion*

The connection is found to be adequate as given for the applied load.

---

# IIA-308

---
