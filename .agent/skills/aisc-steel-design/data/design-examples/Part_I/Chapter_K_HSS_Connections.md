# Chapter K: HSS Connections

**AISC Specification v16.0 - Design Examples**
**Original PDF Pages**: 461-537 (77 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Design of HSS and Box Member Connections

**Examples Included**: ['K.1~K.7: HSS connection examples']

---

## Table of Contents

- [EXAMPLE K.1 WELDED/BOLTED WIDE TEE CONNECTION TO AN HSS COLUMN](#example-k1-welded/bolted-wide-tee-connection-to-an-hss-column)

---

# K-1

# Chapter K
# Additional Requirements for HSS and Box-Section Connections

Examples K.1 through K.6 illustrate common beam-to-column shear connections that have been adapted for use with HSS columns. Example K.7 illustrates a through-plate shear connection, which is unique to HSS columns. Calculations for transverse forces applied to round HSS are illustrated in Example K.8. Examples of HSS base plate and end-plate connections are given in Examples K.9 and K.10.

---

# K-2

## EXAMPLE K.1 WELDED/BOLTED WIDE TEE CONNECTION TO AN HSS COLUMN

**Given:**

Verify a connection between an ASTM A992/A992M W16×50 beam and an ASTM A500/A500M, Grade C, HSS8×8×¼ column using an ASTM A992/A992M WT-shape, as shown in Figure K.1-1. Assuming a flexible support condition, design for the following vertical shear loads:

- $P_D = 6.2$ kips
- $P_L = 18.5$ kips

Note: A tee with a flange width wider than 8 in. was selected to provide sufficient surface for flare bevel groove welds on both sides of the column, because the tee will be slightly offset from the column centerline.

![Diagram showing welded/bolted wide tee connection. Elevation view shows HSS8×8×¼ column with WT5×24.5 tee welded to it, connected to W16×50 beam with bolts. Dimensions shown: 3" edge distance, $l_{eh} = 1.99"$, $l_{ev} = 1\frac{5}{8}"$, 3⅝" and 9" heights, $n = 1\frac{1}{2}"$. Section A-A shows ¾" dia. Group 120 bolts, thread condition N, std. holes, with $\frac{5}{16}$ welds. Note indicates beam flanges not shown for clarity, 1¼" dimension shown.]

*Fig K.1-1. Connection geometry for Example K.1.*

**Solution:**

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam
ASTM A992/A992M
- $F_y = 50$ ksi
- $F_u = 65$ ksi

Tee
ASTM A992/A992M
- $F_y = 50$ ksi
- $F_u = 65$ ksi

Column
ASTM A500/A500M Grade C
- $F_y = 50$ ksi
- $F_u = 62$ ksi

---

# K-3

From AISC *Manual* Tables 1-1, 1-8, and 1-12, the geometric properties are as follows:

W16×50
- $t_w = 0.380$ in.
- $d = 16.3$ in.
- $t_f = 0.630$ in.
- $T = 13\frac{5}{8}$ in.

WT5×24.5
- $t_{tw} = t_w = 0.340$ in.
- $d = 4.99$ in.
- $t_f = 0.560$ in.
- $b_f = 10.0$ in.
- $k_1 = 1\frac{3}{16}$ in. (see W10×49)

HSS8×8×¼
- $t = 0.233$ in.
- $B = 8.00$ in.

From AISC *Specification* Table J3.3, the hole diameter for ¾-in.-diameter bolts with standard holes is:

- $d_h = \frac{13}{16}$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(6.2 \text{ kips}) + 1.6(18.5 \text{ kips})$ | $P_a = 6.2 \text{ kips} + 18.5 \text{ kips}$ |
| $= 37.0 \text{ kips}$ | $= 24.7 \text{ kips}$ |

Calculate the available strength assuming a flexible support condition.

*Required Number of Bolts*

The required number of bolts will ultimately be determined using the coefficient, $C$, from AISC *Manual* Table 7-6. First, the available strength per bolt must be determined.

Determine the available shear strength of a single bolt. From AISC *Manual* Table 7-1, for ¾-in.-diameter, Group 120 bolts:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9$ kips | $\frac{r_n}{\Omega} = 11.9$ kips |

The edge distance is checked against the minimum edge distance requirement provided in AISC *Specification* Table J3.4.

$$l_{ev} = 1¼ \text{ in.} > 1 \text{ in.}$$ **o.k.**

The available bearing and tearout strength per bolt on the tee stem based on edge distance is determined from AISC *Manual* Table 7-5, for $l_{ev} = 1¼$ in., as follows:

---

# K-4

| LRFD | ASD |
|------|-----|
| $\phi r_n = (49.4 \text{ kip/in.})(0.340 \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kip/in.})(0.340 \text{ in.})$ |
| $= 16.8$ kips | $= 11.2$ kips |

The bolt spacing is checked against the minimum spacing requirement between centers of standard holes provided in AISC *Specification* Section J3.4.

$$2\frac{2}{3}d = 2\frac{2}{3}(\frac{3}{4} \text{ in.})$$

$$= 2.00 \text{ in.} > s = 3 \text{ in.}$$ **o.k.**

The available bearing and tearout strength per bolt on the tee stem based on spacing is determined from AISC *Manual* Table 7-4, for $s = 3$ in., as follows:

| LRFD | ASD |
|------|-----|
| $\phi r_n = (87.8 \text{ kip/in.})(0.340 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(0.340 \text{ in.})$ |
| $= 29.9$ kips | $= 19.9$ kips |

The tee stem thickness is less than the beam web thickness, therefore, bearing and tearout of the tee stem will control. The available bolt bearing and tearout strength based on edge distance controls over the available shear strength of the bolt. Conservatively, the available bolt group strength is determined using the bearing and tearout strength for an edge bolt. A more precise strength can be determined using the sum of the effective strengths of the individual fasteners as described in the User Note in AISC *Specification* Section J3.7

Determine the coefficient for the eccentrically loaded bolt group.

| LRFD | ASD |
|------|-----|
| $C_{min} = \frac{P_u}{\phi r_n}$ | $C_{min} = \frac{P_a}{r_n/\Omega}$ |
| $= \frac{37.0 \text{ kips}}{16.8 \text{ kips}}$ | $= \frac{24.7 \text{ kips}}{11.2 \text{ kips}}$ |
| $= 2.20$ | $= 2.21$ |
| Using $e = 3$ in. and $s = 3$ in., determine $C$ from AISC *Manual* Table 7-6, Angle = 0°. | Using $e = 3$ in. and $s = 3$ in., determine $C$ from AISC *Manual* Table 7-6, Angle = 0°. |
| Try four rows of bolts: | Try four rows of bolts: |
| $C = 2.81 > 2.20$ **o.k.** | $C = 2.81 > 2.21$ **o.k.** |

*Tee Stem Thickness and Length*

AISC *Manual* Part 9 stipulates a maximum tee stem thickness that should be provided for rotational ductility as follows:

$$t_{sw \text{ max}} = \frac{d}{2} + \frac{1}{16} \text{ in.}$$
(from *Manual* Eq. 9-53)

$$= \frac{\frac{3}{4} \text{ in.}}{2} + \frac{1}{16} \text{ in.}$$

$$= 0.438 \text{ in.} > 0.340 \text{ in.}$$ **o.k.**

---

# K-5

Note: The beam web thickness is greater than the tee stem thickness. If the beam web were thinner than the tee stem, this check could be satisfied by checking the thickness of the beam web.

As discussed in AISC *Manual* Part 10, it is recommended that the minimum length of a simple shear connection is one-half the $T$-dimension of the beam to be supported. The minimum length of the tee is determined as follow:

$$l_{min} = \frac{T}{2}$$

$$= \frac{13\frac{5}{8} \text{ in.}}{2}$$

$$= 6.81 \text{ in.}$$

As discussed in AISC *Manual* Part 10, the detailed length of connection elements must be compatible with the $T$-dimension of the beam. The tee length is checked using the number of bolts, bolt spacing, and edge distances determined previously.

$$l = 3(3 \text{ in.}) + 2(1¼ \text{ in.})$$

$$= 11.5 \text{ in.} < T = 13\frac{5}{8} \text{ in.}$$ **o.k.**

Try $l = 11.5$ in.

*Tee Stem Shear Yielding Strength*

Determine the available shear strength of the tee stem based on the limit state of shear yielding from AISC *Specification* Section J4.2(a).

$$A_{gv} = lt_{tw}$$

$$= (11.5 \text{ in.})(0.340 \text{ in.})$$

$$= 3.91 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$
$(Spec. \text{ Eq. J4-3})$

$$= 0.60(50 \text{ ksi})(3.91 \text{ in.}^2)$$

$$= 117 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
| $\phi R_n = 1.00(117 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{117 \text{ kips}}{1.50}$ |
| $= 117 \text{ kips} > 37.0 \text{ kips}$ **o.k.** | $= 78.0 \text{ kips} > 24.7 \text{ kips}$ **o.k.** |

Because of the geometry of the tee and because the tee flange is thicker than the stem and carries only half of the beam reaction, flexural yielding and shear yielding of the flange are not controlling limit states.

*Tee Stem Shear Rupture Strength*

Determine the available shear strength of the tee stem based on the limit state of shear rupture from AISC *Specification* Section J4.2(b).

---

# K-6

$$A_{nv} = \left[l - n(d_h + \frac{1}{16} \text{ in.})\right]t_{tw}$$

$$= \left[11.5 \text{ in.} - (4)(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.})\right](0.340 \text{ in.})$$

$$= 2.72 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$
$(Spec. \text{ Eq. J4-4})$

$$= 0.60(65 \text{ ksi})(2.72 \text{ in.}^2)$$

$$= 106 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(106 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{106 \text{ kips}}{2.00}$ |
| $= 79.5 \text{ kips} > 37.0 \text{ kips}$ **o.k.** | $= 53.0 \text{ kips} > 24.7 \text{ kips}$ **o.k.** |

*Tee Stem Block Shear Rupture Strength*

The nominal strength for the limit state of block shear rupture is given by AISC *Specification* Section J4.3.

$$R_n = 0.60F_u A_{nv} + U_{bs} F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs} F_u A_{nt}$$
$(Spec. \text{ Eq. J4-5})$

The available block shear rupture strength of the tee stem is determined as follows, using AISC *Manual* Tables 9-3a, 9-3b, and 9-3c and AISC *Specification* Equation J4-5, with $n = 4$, $l_{eh} = 1.99$ in. (assume $l_{eh} = 2.00$ in. to use Table 9-3a), $l_{ev} = 1¼$ in., and $U_{bs} = 1.0$.

| LRFD | ASD |
|------|-----|
| Tension rupture component from AISC *Manual* Table 9-3a: | Tension rupture component from AISC *Manual* Table 9-3a: |
| $\frac{\phi F_u A_{nt}}{t} = 76.2$ kip/in. | $\frac{F_u A_{nt}}{\Omega t} = 50.8$ kip/in. |
| Shear yielding component from AISC *Manual* Table 9-3b: | Shear yielding component from AISC *Manual* Table 9-3b: |
| $\frac{\phi 0.60 F_y A_{gv}}{t} = 231$ kip/in. | $\frac{0.60 F_y A_{gv}}{\Omega t} = 154$ kip/in. |
| Shear rupture component from AISC *Manual* Table 9-3c: | Shear rupture component from AISC *Manual* Table 9-3c: |
| $\frac{\phi 0.60 F_u A_{nv}}{t} = 210$ kip/in. | $\frac{0.60 F_u A_{nv}}{\Omega t} = 140$ kip/in. |

---

# K-7

| LRFD | ASD |
|------|-----|
| The design block shear rupture strength is: | The allowable block shear rupture strength is: |
| $\phi R_n = \phi 0.60 F_u A_{nv} + \phi U_{bs} F_u A_{nt}$ | $\frac{R_n}{\Omega} = \frac{0.60 F_u A_{nv}}{\Omega} + \frac{U_{bs} F_u A_{nt}}{\Omega}$ |
| $\leq \phi 0.60 F_y A_{gv} + \phi U_{bs} F_u A_{nt}$ | $\leq \frac{0.60 F_y A_{gv}}{\Omega} + \frac{U_{bs} F_u A_{nt}}{\Omega}$ |
| $= (210 \text{ kip/in.} + 76.2 \text{ kip/in.})(0.340 \text{ in.})$ | $= (140 \text{ kip/in.} + 50.8 \text{ kip/in.})(0.340 \text{ in.})$ |
| $\leq (231 \text{ kip/in.} + 76.2 \text{ kip/in.})(0.340 \text{ in.})$ | $\leq (154 \text{ kip/in.} + 50.8 \text{ kip/in.})(0.340 \text{ in.})$ |
| $= 97.3 \text{ kips} < 104 \text{ kips}$ | $= 64.9 \text{ kips} < 69.6 \text{ kips}$ |
| Therefore: | Therefore: |
| $\phi R_n = 97.3 \text{ kips} > 37.0 \text{ kips}$ **o.k.** | $\frac{R_n}{\Omega} = 64.9 \text{ kips} > 24.7 \text{ kips}$ **o.k.** |

*Tee Stem Flexural Strength*

The required flexural strength for the tee stem is:

| LRFD | ASD |
|------|-----|
| $M_u = P_u e$ | $M_a = P_a e$ |
| $= (37.0 \text{ kips})(3 \text{ in.})$ | $= (24.7 \text{ kips})(3 \text{ in.})$ |
| $= 111$ kip-in. | $= 74.1$ kip-in. |

From AISC *Specification* Section J4.5, the available flexural strength of the tee stem shall be the lower value obtained according to the limit states of flexural yielding, local buckling, flexural lateral-torsional buckling, and flexural rupture.

The available flexural yielding strength of the tee stem is determined from AISC *Specification* Section F11.1. The stem, in this case, is treated as a rectangular bar.

$$Z = \frac{t_{sw} d^2}{4}$$

$$= \frac{(0.340 \text{ in.})(11.5 \text{ in.})^2}{4}$$

$$= 11.2 \text{ in.}^3$$

$$S_x = \frac{t_{sw} d^2}{6}$$

$$= \frac{(0.340 \text{ in.})(11.5 \text{ in.})^2}{6}$$

$$= 7.49 \text{ in.}^3$$

$$M_n = M_p = F_y Z \leq 1.5F_y S_x$$
$(Spec. \text{ Eq. F11-1})$

$$= (50 \text{ ksi})(11.2 \text{ in.}^3) \leq 1.5(50 \text{ ksi})(7.49 \text{ in.}^3)$$

$$= 560 \text{ kip-in.} < 562 \text{ kip-in.}$$

---

# K-8

Therefore:
$$M_n = 560 \text{ kip-in.}$$

The tee stem available flexural yielding strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(560 \text{ kip-in.})$ | $\frac{M_n}{\Omega_b} = \frac{560 \text{ kip-in.}}{1.67}$ |
| $= 504 \text{ kip-in.} > 111 \text{ kip-in.}$ **o.k.** | $= 335 \text{ kip-in.} > 74.1 \text{ kip-in.}$ **o.k.** |

The tee stem available flexural strength due to lateral-torsional buckling is determined from Section F11.2.

$$\frac{L_b d}{t_{sw}^2} = \frac{(3 \text{ in.})(11.5 \text{ in.})}{(0.340 \text{ in.})^2}$$

$$= 298$$

$$\frac{0.08E}{F_y} = \frac{0.08(29{,}000 \text{ ksi})}{50 \text{ ksi}}$$

$$= 46.4$$

$$\frac{1.9E}{F_y} = \frac{1.9(29{,}000 \text{ ksi})}{50 \text{ ksi}}$$

$$= 1{,}100$$

Because $46.4 < 298 < 1{,}100$, Equation F11-3 is applicable with $C_b = 1.00$.

$$M_n = C_b\left[1.52 - 0.274\left(\frac{L_b d}{t^2}\right)\frac{F_y}{E}\right]M_y \leq M_p$$
$(Spec. \text{ Eq. F11-3})$

$$= 1.00\left[1.52 - 0.274(298)\left(\frac{50 \text{ ksi}}{29{,}000 \text{ ksi}}\right)\right](50 \text{ ksi})(7.49 \text{ in.}^2) \leq (50 \text{ ksi})(11.2 \text{ in.}^3)$$

$$= 517 \text{ kip-in.} < 560 \text{ kip-in.}$$

Therefore:
$$M_n = 517 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(517 \text{ kip-in.})$ | $\frac{M_n}{\Omega_b} = \frac{517 \text{ kip-in.}}{1.67}$ |
| $= 465 \text{ kip-in.} > 111 \text{ kip-in.}$ **o.k.** | $= 310 \text{ kip-in.} > 74.1 \text{ kip-in.}$ **o.k.** |

The tee stem available flexural rupture strength is determined from AISC *Manual* Part 9 as follows:

---

# K-9

$$Z_{net} = \frac{t_{sw} d^2}{4} - 2t_{sw}(d_h + \frac{1}{16}\text{in.})(1.5 \text{ in.} + 4.5 \text{ in.})$$

$$= \frac{(0.340 \text{ in.})(11.5 \text{ in.})^2}{4} - 2(0.340 \text{ in.})(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.})(1.5 \text{ in.} + 4.5 \text{ in.})$$

$$= 7.67 \text{ in.}^3$$

$$M_n = F_u Z_{net}$$
$({Manual} \text{ Eq. 9-8})$

$$= (65 \text{ ksi})(7.67 \text{ in.}^3)$$

$$= 499 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.75$ | $\Omega_b = 2.00$ |
| $\phi_b M_n = 0.75(499 \text{ kip-in.})$ | $\frac{M_n}{\Omega_b} = \frac{499 \text{ kip-in.}}{2.00}$ |
| $= 374 \text{ kip-in.} > 111 \text{ kip-in.}$ **o.k.** | $= 250 \text{ kip-in.} > 74.1 \text{ kip-in.}$ **o.k.** |

*Weld Size*

Because the flange width of the tee is larger than the width of the HSS, a flare bevel groove weld is required. Taking the outside radius as $R = 2t_w = 2(0.233 \text{ in.}) = 0.466$ in. and using AISC *Specification* Table J2.2, the effective throat thickness of the flare bevel groove weld is $E = \frac{5}{16}R = \frac{5}{16}(0.466 \text{ in.}) = 0.146$ in. This effective throat thickness will be used for subsequent calculations; however, for the detail drawing, a $\frac{5}{16}$ in. weld is specified.

Using AISC *Specification* Table J2.3, the minimum effective throat thickness of the flare bevel groove weld, based on the 0.233 in. thickness of the HSS column, is ⅛ in.

$$E = 0.146 \text{ in.} > \frac{1}{8} \text{ in.}$$

The equivalent fillet weld that provides the same throat dimension is:

$$\left(\frac{D}{16}\right)\left(\frac{1}{\sqrt{2}}\right) = 0.146$$

$$D = 16\sqrt{2}(0.146)$$

$$= 3.30 \text{ sixteenths of an inch}$$

The equivalent fillet weld size is used in the following calculations.

*Weld Ductility*

Check weld ductility using AISC *Manual* Part 9.

Let $b_f = B = 8.00$ in.

$$b = \frac{b_f - 2k_1}{2}$$

$$= \frac{8.00 \text{ in.} - 2(\frac{13}{16} \text{ in.})}{2}$$

$$= 3.19 \text{ in}$$

---

# K-10

$$w_{min} = 0.0155\frac{F_y t_f^2}{b}\left(\frac{b^2}{l^2} + 2\right) \leq (\frac{5}{8})t_{sw}$$
$({Manual} \text{ Eq. 9-51})$

$$= 0.0155\frac{(50 \text{ ksi})(0.560 \text{ in.})^2}{3.19 \text{ in.}}\left[\frac{(3.19 \text{ in.})^2}{(11.5 \text{ in.})^2} + 2\right] \leq (\frac{5}{8})(0.340 \text{ in.})$$

$$= 0.158 \text{ in.} < 0.213\text{in.}$$

0.158 in. = 2.53 sixteenths of an inch

$$D_{min} = 2.53 < 3.30 \text{ sixteenths of an inch}$$ **o.k.**

*Available Weld Shear Strength*

The load is assumed to act concentrically with the weld group (i.e., a flexible support condition).

$a = 0$ and $k = 0$; therefore, $C = 3.71$ from AISC *Manual* Table 8-4, Angle = 0°.

$$R_n = CC_1 Dl$$
$({Manual} \text{ Eq. 8-30})$

$$= 3.71(1.00)(3.30 \text{ sixteenths of an inch})(11.5 \text{ in.})$$

$$= 141 \text{ kips}$$

From AISC *Specification* Section J2.4, the available weld strength is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(141 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{141 \text{ kips}}{2.00}$ |
| $= 106 \text{ kips} > 37.0 \text{ kips}$ **o.k.** | $= 70.5 \text{ kips} > 24.7 \text{ kips}$ **o.k.** |

*Shear Rupture of the HSS at the Weld*

$$t_{min} = \frac{3.09D}{F_u}$$
$({Manual} \text{ Eq. 9-6})$

$$= \frac{3.09(3.30 \text{ sixteenths})}{62 \text{ ksi}}$$

$$= 0.164 \text{ in.} < 0.233 \text{ in.}$$

By inspection, shear rupture of the tee flange at the welds will not control.

Therefore, the weld controls.

---

# K-11

# EXAMPLE K.2 WELDED/BOLTED NARROW TEE CONNECTION TO AN HSS COLUMN

**Given:**

Verify a connection for an ASTM A992/A992M W16×50 beam to an ASTM A500/A500M Grade C HSS8×8×¼ column using an ASTM A992/A992M WT5×24.5 with fillet welds against the flat width of the HSS, as shown in Figure K.2-1. Use 70-ksi weld electrodes. For architectural purposes, assume that the flanges of the WT from the previous example have been stripped down to a width of 5 in. Assuming a flexible support condition, design for the following vertical shear loads:

$P_D = 6.2$ kips
$P_L = 18.5$ kips

Note: This is the same problem as Example K.1 with the exception that a narrow tee will be selected, which will permit fillet welds on the flat of the column. The beam will still be centered on the column centerline; therefore, the tee will be slightly offset.

<diagram>
Figure K.2-1 shows the connection geometry for Example K.2 in both elevation and section A-A views.

**Elevation view:**
- HSS8×8×¼ column shown vertically
- WT5×24.5 tee section (flange stripped as noted) welded to HSS column
- Connection dimensions: 3" offset at top, $l_{eh} = 1.99"$ horizontal edge distance
- Vertical bolt spacing: 3" @ 3" = 9" for 4 holes, total height 11½"
- W16×50 beam connects to tee (beam flanges not shown for clarity)
- 1¼" dimension shown

**Section A-A view:**
- Shows 8" width of HSS column
- (2) ¾" dia. Group 120, thread condition N, std. holes on each side
- 5" dimension shown for connection
- ⅜" and ⅝" return welds at top
- ⅝" fillet welds on sides
</diagram>

*Fig K.2-1. Connection geometry for Example K.2.*

**Solution:**

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Tee
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Column
ASTM A500/A500M Grade C
$F_y = 50$ ksi
$F_u = 62$ ksi

---

# K-12

From AISC *Manual* Tables 1-1, 1-8, and 1-12, the geometric properties are as follows:

W16×50
$t_w = 0.380$ in.
$d = 16.3$ in.
$t_f = 0.630$ in.

HSS8×8×¼
$t = 0.233$ in.
$B = 8.00$ in.

WT5×24.5
$t_{sw} = t_w = 0.340$ in.
$d = 4.99$ in.
$t_f = 0.560$ in.
$k_1 = 1\frac{5}{16}$ in. (see W10×49)

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(6.2 \text{ kips}) + 1.6(18.5 \text{ kips})$ | $P_a = 6.2 \text{ kips} + 18.5 \text{ kips}$ |
| $= 37.0$ kips | $= 24.7$ kips |

The tee stem thickness, tee length, tee stem strength, and beam web bearing strength are verified in Example K.1. The required number of bolts is also determined in Example K.1.

*Maximum Tee Flange Width*

Assume ¼ in. welds and an HSS corner radius equal to 2.25 times the nominal thickness $2.25(\frac{1}{4} \text{ in.}) = \frac{9}{16}$ in. (refer to AISC *Manual* Part 1 discussion).

The recommended minimum shelf dimension for ¼ in. fillet welds from AISC *Manual* Figure 8-13 is ½ in.

Connection offset (centerline of the column to the centerline of the tee stem):

$$\frac{0.380 \text{ in.}}{2} + \frac{0.340 \text{ in.}}{2} = 0.360 \text{ in.}$$

The stripped flange must not exceed the flat face of the tube minus the shelf dimension on each side:

$$b_f \leq 8.00 \text{ in.} - 2(\frac{9}{16} \text{ in.}) - 2(\frac{1}{2} \text{ in.}) - 2(0.360 \text{ in.})$$
5.00 in. < 5.16 in.   **o.k.**

*Minimum Fillet Weld Size*

From AISC *Specification* Table J2.4, the minimum fillet weld size is $\frac{1}{8}$ in. ($D = 2$) for welding to 0.233-in.-thick material.

*Weld Ductility*

The flexible width of the connecting element, $b$, is defined in Figure 9-6(a) of AISC *Manual* Part 9:

---

# K-13

$$b = \frac{b_f - 2k_1}{2}$$

$$= \frac{5.00 \text{ in.} - 2(1\frac{5}{16} \text{ in.})}{2}$$

$$= 1.69 \text{ in.}$$

$$w_{min} = 0.0155\frac{F_y t_f^2}{b}\left(\frac{b^2}{l^2} + 2\right) \leq (\frac{5}{8})t_{sw}$$
$({Manual} \text{ Eq. 9-51})$

$$= 0.0155\frac{(50 \text{ ksi})(0.560 \text{ in.})^2}{1.69 \text{ in.}}\left[\frac{(1.69 \text{ in.})^2}{(11.5 \text{ in.})^2} + 2\right] \leq (\frac{5}{8})(0.340 \text{ in.})$$

$$= 0.291 \text{ in.} > 0.213 \text{ in.}$$; therefore, use $w_{min} = 0.213$ in.

$$D_{min} = (0.213 \text{ in.})(16)$$
$$= 3.41 \text{ sixteenths of an inch}$$

Try a ¼ in. fillet weld as a practical minimum, which is less than the maximum permitted weld size of $t_f - \frac{1}{16}$ in. = 0.560 in. $- \frac{1}{16}$ in. = 0.498 in., in accordance with AISC *Specification* Section J2.2b. Provide ½ in. return welds at the top of the tee to meet the criteria listed in AISC *Specification* Section J2.2b(g).

*Available Weld Shear Strength*

The load is assumed to act concentrically with the weld group (i.e., a flexible support condition).

$a = 0$ and $k = 0$, therefore, $C = 3.71$ from AISC *Manual* Table 8-4, Angle = 0°.

$$R_n = CC_1 Dl$$
$({Manual} \text{ Eq. 8-30})$

$$= 3.71(1.00)(4 \text{ sixteenths of an inch})(11.5 \text{ in.})$$

$$= 171 \text{ kips}$$

From AISC *Specification* Section J2.4, the available fillet weld shear strength is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(171 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{171 \text{ kips}}{2.00}$ |
| $= 128 \text{ kips} > 37.0 \text{ kips}$ | $= 85.5 \text{ kips} > 24.7 \text{ kips}$ |

*Minimum HSS Wall Thickness to Match Weld Strength*

$$t_{min} = \frac{3.09D}{F_u}$$
$({Manual} \text{ Eq. 9-6})$

$$= \frac{3.09(4)}{62 \text{ ksi}}$$

$$= 0.199 \text{ in.} < 0.233 \text{ in.}$$

By inspection, shear rupture of the flange of the tee at the welds will not control. Therefore, the weld controls.

---

# K-14

# EXAMPLE K.3 DOUBLE-ANGLE CONNECTION TO AN HSS COLUMN

**Given:**

Use AISC *Manual* Tables 10-1 and 10-2 to design a double-angle connection for an ASTM A992/A992M W36×231 beam to an ASTM A500/A500M Grade C HSS14×14×½ column, as shown in Figure K.3-1. The angles are ASTM A572/A572M Grade 50 material. Use 70-ksi weld electrodes. The bottom flange cope is required for erection. Use the following vertical shear loads:

$P_D = 37.5$ kips
$P_L = 113$ kips

<diagram>
Figure K.3-1 shows the connection geometry for Example K.3 in both elevation and section A-A views.

**Elevation view:**
- HSS14×14×½ column shown vertically
- 2L4×3½×⅜ × 1'-11½" shop-attached to HSS column
- Connection dimensions: 3½" at top, ½" offset
- Vertical bolt spacing: 7@3" = 21", total height 23⅞"
- W36×231 beam connects to angles (beam flanges not shown for clarity)
- Bottom dimensions: 2⅛" and 1⅝"

**Section A-A view:**
- Shows rectangular HSS column cross-section
- (2) ¾" dia. Group 120, thread condition N, std. holes on each side
- ⅝" and ⅝" return welds at top
- Connection details shown
</diagram>

*Fig K.3-1. Connection geometry for Example K.3.*

**Solution:**

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Column
ASTM A500/A500M Grade C
$F_y = 50$ ksi
$F_u = 62$ ksi

---

# K-15

Angles
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Tables 1-1 and 1-12, the geometric properties are as follows:

W36×231
$t_w = 0.760$ in.
$T = 31\frac{3}{4}$ in.

HSS14×14×½
$t = 0.465$ in.
$B = 14.0$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(37.5 \text{ kips}) + 1.6(113 \text{ kips})$ | $R_a = 37.5 \text{ kips} + 113 \text{ kips}$ |
| $= 226$ kips | $= 151$ kips |

*Available Angle Strength*

AISC *Manual* Table 10-1a includes checks for the limit states of shear yielding, shear rupture, and block shear rupture of the angles.

Use 8 rows of ¾-in.-diameter bolts in standard holes and 2L4×3½×⅜ (SLBB). From AISC *Manual* Table 10-1a:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 362 \text{ kips} > 226 \text{ kips}$ **o.k.** | $\frac{R_n}{\Omega} = 241 \text{ kips} > 151 \text{ kips}$ **o.k.** |

*Available Shear Transfer Strength at Bolt Holes*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength determined per AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the angles at the bolt holes per AISC *Specification* Section J3.11, and (3) the available bearing or tearout strength of the beam web at the bolt holes per AISC *Specification* Section J3.11.

From AISC *Manual* Table 10-1b, the available bolt shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9$ kips | $\frac{r_n}{\Omega} = 11.9$ kips |

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the angle per bolt for ¾-in.-diameter bolts in standard holes is:

---

# K-16

| LRFD | ASD |
|------|-----|
| For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): | For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): |
| $\phi r_n = (49.4 \text{ kip/in.})(\frac{3}{8} \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kip/in.})(\frac{3}{8} \text{ in.})$ |
| $= 18.5$ kips | $= 12.3$ kips |
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kip/in.})(\frac{3}{8} \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(\frac{3}{8} \text{ in.})$ |
| $= 32.9$ kips | $= 21.9$ kips |

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the beam web per bolt for ¾-in.-diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kip/in.})(0.760 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(0.760 \text{ in.})$ |
| $= 66.7$ kips | $= 44.5$ kips |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by two because the bolts are in double shear), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by two because there are two angles), and available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min\begin{Bmatrix} 17.9 \text{ kips}(2) = 35.8 \text{ kips,} \\ 32.9 \text{ kips}(2) = 65.8 \text{ kips,} \\ 66.7 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips}(2) = 23.8 \text{ kips,} \\ 21.9 \text{ kips}(2) = 43.8 \text{ kips,} \\ 44.5 \text{ kips} \end{Bmatrix}$ |
| $= 35.8$ kips | $= 23.8$ kips |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by two because the bolts are in double shear), the available bearing and tearout strength of the angles for an edge bolt (multiplied by two because there are two angles), and available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min\begin{Bmatrix} 17.9 \text{ kips}(2) = 35.8 \text{ kips,} \\ 18.5 \text{ kips}(2) = 37.0 \text{ kips,} \\ 66.7 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips}(2) = 23.8 \text{ kips,} \\ 12.3 \text{ kips}(2) = 24.6 \text{ kips,} \\ 44.5 \text{ kips} \end{Bmatrix}$ |
| $= 35.8$ kips | $= 23.8$ kips |

At the other connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength (multiplied by two because the bolts are in double shear), the available bearing and tearout strength of the angles for a non-edge bolt (multiplied by two because there are two angles), and available bearing and tearout strength of the beam web for a non-edge bolt:

---

# K-17

| LRFD | ASD |
|------|-----|
| $\phi r_{n,other} = \min\begin{Bmatrix} 17.9 \text{ kips}(2) = 35.8 \text{ kips,} \\ 32.9 \text{ kips}(2) = 65.8 \text{ kips,} \\ 66.7 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,other}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips}(2) = 23.8 \text{ kips,} \\ 21.9 \text{ kips}(2) = 43.8 \text{ kips,} \\ 44.5 \text{ kips} \end{Bmatrix}$ |
| $= 35.8$ kips | $= 23.8$ kips |

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = \phi r_{n,top} + \phi r_{n,bot} + \phi r_{n,other}(n-2)$ | $\frac{R_n}{\Omega} = \frac{r_{n,top}}{\Omega} + \frac{r_{n,bot}}{\Omega} + \frac{r_{n,other}}{\Omega}(n-2)$ |
| $= 35.8 \text{ kips} + 35.8 \text{ kips} + 35.8 \text{ kips}(8-2)$ | $= 23.8 \text{ kips} + 23.8 \text{ kips} + 23.8 \text{ kips}(8-2)$ |
| $= 286 \text{ kips} > 226 \text{ kips}$ **o.k.** | $= 190 \text{ kips} > 151 \text{ kips}$ **o.k.** |

*Available Beam Web Strength*

The beam is coped at the bottom flange only, therefore the limit states of shear yielding, shear rupture, and block shear rupture of the beam web do not apply.

*Available Weld Strength*

Obtain the available weld strength from AISC *Manual* Table 10-2 with $\frac{5}{16}$ in. welds (welds B).

| LRFD | ASD |
|------|-----|
| $\phi R_n = 318 \text{ kips} > 226 \text{ kips}$ **o.k.** | $\frac{R_n}{\Omega} = 212 \text{ kips} > 151 \text{ kips}$ **o.k.** |

*Minimum Support Thickness*

The minimum required support thickness using AISC *Manual* Table 10-2 is determined as follows for $F_u = 62$ ksi material.

$$0.238 \text{ in.}\left(\frac{65 \text{ ksi}}{62 \text{ ksi}}\right) = 0.250 \text{ in.} < 0.465 \text{ in.}$$ **o.k.**

*Minimum Angle Thickness*

$$t_{min} = w + \frac{1}{16} \text{ in.}$$, from AISC *Specification* Section J2.2b
$$= \frac{5}{16} \text{ in.} + \frac{1}{16} \text{ in.}$$
$$= \frac{3}{8} \text{ in.}$$

Use ⅜ in. angle thickness to accommodate the welded legs of the double-angle connection.

Use 2L4×3½×⅜×1'-11½″.

*Minimum Angle Length*

As discussed in AISC *Manual* Part 10, it is recommended that the minimum length of a simple shear connection is one-half the $T$-dimension of the beam to be supported. The minimum length of the connection is determined as follows:

---

# K-18

$$l_{min} = \frac{T}{2}$$

$$= \frac{31\frac{3}{4} \text{ in.}}{2}$$

$$= 15.7 \text{ in.} < 23\frac{1}{2} \text{ in.}$$ **o.k.**

*Minimum Column Width*

The workable flat for the HSS column is $11\frac{3}{4}$ in. from AISC *Manual* Table 1-12.

The recommended minimum shelf dimension for $\frac{5}{16}$ in. fillet welds from AISC *Manual* Figure 8-13 is $\frac{9}{16}$ in.

The minimum acceptable width to accommodate the connection is:

$$2(4.00 \text{ in.}) + 0.760 \text{ in.} + 2(\frac{9}{16} \text{ in.}) = 9.89 \text{ in.} < 11\frac{3}{4} \text{ in.}$$ **o.k.**

---

# K-19

# EXAMPLE K.4 UNSTIFFENED SEATED CONNECTION TO AN HSS COLUMN

**Given:**

Use AISC *Manual* Table 10-6 to verify an unstiffened seated connection for an ASTM A992/A992M W21×62 beam to an ASTM A500/A500M Grade C HSS12×12×½ column, as shown in Figure K.4-1. The angles are ASTM A572/A572M Grade 50 material. Use 70-ksi weld electrodes. Use the following vertical shear loads:

$P_D = 9$ kips
$P_L = 27$ kips

<diagram>
Figure K.4-1 shows the connection geometry for Example K.4 with both elevation and section views.

**Elevation view (left side):**
- HSS12×12×½ column shown vertically
- L4×4×¼ top angle location (with optional location noted)
- W21×62 beam (beam flanges not shown for clarity)
- L8×4×⅝ bottom seat angle
- ½" nominal dimension noted, use ¾" for calculations to allow for length underrun
- (2) ¾" dia. Group 120, thread condition N, std. holes shown at both top and bottom angles
- Weld toe only noted for top angle
- $\frac{3}{16}$ dimension shown

**Side view (right side) - Section view:**
- Shows 8" width dimension
- 5½" height dimension for seat angle
- $\frac{5}{16}$ and $\frac{5}{8}$ return welds at top
</diagram>

*Fig K.4-1. Connection geometry for Example K.4.*

**Solution:**

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Column
ASTM A500/A500M Grade C
$F_y = 50$ ksi
$F_u = 62$ ksi

Angles
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

---

# K-20

From AISC *Manual* Tables 1-1 and 1-12, the geometric properties are as follows:

W21×62
$t_w = 0.400$ in.
$t_f = 0.615$ in.
$d = 21.0$ in.
$k_{des} = 1.12$ in.

HSS12×12×½
$t = 0.465$ in.
$B = 12.0$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(9 \text{ kips}) + 1.6(27 \text{ kips})$ | $R_a = 9 \text{ kips} + 27 \text{ kips}$ |
| $= 54.0$ kips | $= 36.0$ kips |

*Seat Angle and Weld Design*

From AISC *Manual* Part 10, the minimum required bearing length, $l_b \, _{min}$, is the length of bearing required for the limit states of web local yielding and web local crippling on the beam, but not less than $k_{des}$.

Using AISC *Manual* Equations 10-1a or 10-1b, the minimum required bearing length for web local yielding is:

| LRFD | ASD |
|------|-----|
| $l_{b,yielding} = \frac{R_u}{\phi F_y t_w} - 2.5k_{des}$ | $l_{b,yielding} = \frac{\Omega R_a}{F_y t_w} - 2.5k_{des}$ |
| $= \frac{54.0 \text{ kips}}{(1.00)(50 \text{ ksi})(0.400 \text{ in.})} - 2.5(1.12 \text{ in.})$ | $= \frac{1.50(36.0 \text{ kips})}{(50 \text{ ksi})(0.400 \text{ in.})} - 2.5(1.12 \text{ in.})$ |
| which results in a negative quantity. | which results in a negative quantity. |

For web local crippling, the maximum bearing length-to-depth ratio is determined as follows (including ¼ in. tolerance to account for possible beam underrun):

$$\left(\frac{l_b}{d}\right)_{max} = \frac{3.25 \text{ in.}}{21.0 \text{ in.}}$$

$$= 0.155 < 0.2$$

Using AISC *Manual* Equations 10-2a or 10-2b, when $l_b/d \leq 0.2$:

---

# K-21

| LRFD | ASD |
|------|-----|
| $l_{b,crippling} = \frac{d}{3}\left[\frac{R_u}{\phi(0.40)t_w^2}\sqrt{\frac{t_w}{EF_y t_f}} - 1\right]\left(\frac{t_f}{t_w}\right)^{1.5}$ | $l_{b,crippling} = \frac{d}{3}\left[\frac{\Omega R_a}{0.40t_w^2}\sqrt{\frac{t_w}{EF_y t_f}} - 1\right]\left(\frac{t_f}{t_w}\right)^{1.5}$ |
| $= \frac{21.0 \text{ in.}}{3}$ | $= \frac{21.0 \text{ in.}}{3}$ |
| $\times\left[\frac{54.0 \text{ kips}}{0.75(0.40)(0.400 \text{ in.})^2}\sqrt{\frac{0.400 \text{ in.}}{(29{,}000 \text{ ksi})(50 \text{ ksi})(0.615 \text{ in.})}} - 1\right]$ | $\times\left[\frac{2.00(36.0 \text{ kips})}{0.40(0.400 \text{ in.})^2}\sqrt{\frac{0.400 \text{ in.}}{(29{,}000 \text{ ksi})(50 \text{ ksi})(0.615 \text{ in.})}} - 1\right]$ |
| $\times\left(\frac{0.615 \text{ in.}}{0.400 \text{ in.}}\right)^{1.5}$ | $\times\left(\frac{0.615 \text{ in.}}{0.400 \text{ in.}}\right)^{1.5}$ |
| which results in a negative quantity. | which results in a negative quantity. |

Therefore, use $l_b \, _{min} = k_{des} = 1.12$ in.

Note: Generally, the value of $l_b/d$ is not initially known, and the larger value determined from the web local crippling equations in the preceding text can be used conservatively to determine the bearing length required for web local crippling.

For this beam and end reaction, the beam web available strength exceeds the required strength (hence the negative bearing lengths) and the lower-bound bearing length controls ($l_b \, _{req} = k_{des} = 1.12$ in.). Thus, $l_b \, _{min} = 1.12$ in.

Try an L8×4×⅝ seat with $\frac{5}{16}$ in. fillet welds.

*Outstanding Angle Leg Available Strength*

From AISC *Manual* Table 10-6 for an 8-in. angle length and $l_b \, _{req} = 1.12$ in. = $1\frac{1}{8}$ in., the outstanding angle leg available strength is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 113 \text{ kips} > 54.0 \text{ kips}$ **o.k.** | $\frac{R_n}{\Omega} = 74.9 \text{ kips} > 36.0 \text{ kips}$ **o.k.** |

*Available Weld Strength*

From AISC *Manual* Table 10-6, for an L8×4 angle and $\frac{5}{16}$ in. weld size, the available weld strength is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 66.7 \text{ kips} > 54.0 \text{ kips}$ **o.k.** | $\frac{R_n}{\Omega} = 44.5 \text{ kips} > 36.0 \text{ kips}$ **o.k.** |

*Minimum HSS Wall Thickness to Match Weld Strength*

$$t_{min} = \frac{3.09D}{F_u}$$
$({Manual} \text{ Eq. 9-6})$

$$= \frac{3.09(5)}{62 \text{ ksi}}$$

$$= 0.249 \text{ in.} < 0.465 \text{ in.}$$

---

# K-22

Because the $t$ of the HSS is greater than $t_{min}$ for the $\frac{5}{16}$ in. weld, no reduction in the weld strength is required to account for the shear in the HSS.

*Connection to Beam and Top Angle (AISC Manual Part 10)*

Use an L4×4×¼ top angle for stability. Use a $\frac{3}{16}$ in. fillet weld across the toe of the angle for attachment to the HSS. Attach both the seat and top angles to the beam flanges with two ¾-in.-diameter Group 120 bolts.

---

# K-23

# EXAMPLE K.5 STIFFENED SEATED CONNECTION TO AN HSS COLUMN

**Given:**

Use AISC *Manual* Tables 10-8 and 10-15 to verify a stiffened seated connection for an ASTM A992/A992M W21×68 beam to an ASTM A500/A500M Grade C HSS14×14×½ column, as shown in Figure K.5-1. Use 70-ksi electrode welds to connect the stiffener, seat plate, and top angle to the HSS. The angle and plate material are ASTM A572/A572M Grade 50.

Use the following vertical shear loads:

$P_D = 20$ kips
$P_L = 60$ kips

<diagram>
Figure K.5-1 shows the connection geometry for Example K.5 with both elevation and side section views.

**Elevation view (left side):**
- HSS14×14×½ column shown vertically
- L4×4×¼ top angle
- ½" nominal dimension noted, use ¾" for calculations to allow for length underrun
- W21×68 beam
- Dimension $l_b$ shown for bearing length
- Dimension $B$ shown
- $l = 2'-0"$ shown
- $W = 7"$ notation for seat width
- $W = \text{seat width}$, $B_{max} = W/2 \geq 2\frac{5}{8}"$

**Side section view (right side):**
- Shows $\frac{3}{16}$ weld toe only at top
- Shows $\frac{3}{16}$ weld toe only or (2) ¾" dia. Group 120, thread condition N, std. holes (as shown)
- 5½" dimension shown
- (2) ¾" dia. Group 120, thread condition N, std. holes shown in stiffener
- PL⅜×7×0'-11½" stiffener plate
- $\frac{5}{16}$ and 5" weld dimensions shown
- $\frac{5}{8}$" dimension
- $\frac{5}{16}$ and $\frac{5}{16}$ welds shown at bottom
- PL⅝×7×2'-0" fit to bear notation
</diagram>

*Fig K.5-1. Connection geometry for Example K.5.*

**Solution:**

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

---

# K-24

Beam
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Column
ASTM A500/A500M Grade C
$F_y = 50$ ksi
$F_u = 62$ ksi

Angles and Plates
ASTM A572/A572 Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Tables 1-1 and 1-12, the geometric properties are as follows:

W21×68
$t_w = 0.430$ in.
$d = 21.1$ in.
$k_{des} = 1.19$ in.

HSS14×14×½
$t = 0.465$ in.
$B = 14.0$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(20 \text{ kips}) + 1.6(60 \text{ kips})$ | $P_a = 20 \text{ kips} + 60 \text{ kips}$ |
| $= 120$ kips | $= 80.0$ kips |

The available strength of connections to rectangular HSS with concentrated loads are determined based on the applicable limit states from Chapter J.

*Stiffener Width, W, Required for Web Local Crippling and Web Local Yielding*

The stiffener width is determined based on web local crippling and web local yielding of the beam, assuming a ¾ in. beam end setback in the calculations. Note that according to AISC *Manual* Part 10, the length of bearing, $l_b$, cannot be less than the beam $k_{des}$.

For web local crippling, assume $l_b/d > 0.2$ and use constants $R_3$ and $R_6$ from AISC *Manual* Table 9-4.

| LRFD | ASD |
|------|-----|
| From AISC *Manual* Equation 9-63a and Table 9-4: | From AISC *Manual* Equation 9-63b and Table 9-4: |
| $W_{min} = \frac{R_u - \phi R_5}{\phi R_6} + \text{setback} \geq k_{des} + \text{setback}$ | $W_{min} = \frac{R_a - R_5 / \Omega}{R_6 / \Omega} + \text{setback} \geq k_{des} + \text{setback}$ |
| $= \frac{120 \text{ kips} - 75.9 \text{ kips}}{7.95 \text{ kip/in.}} + \frac{3}{4} \text{ in.} \geq 1.19 \text{ in.} + \frac{3}{4} \text{ in.}$ | $= \frac{80.0 \text{ kips} - 50.6 \text{ kips}}{5.30 \text{ kip/in.}} + \frac{3}{4} \text{ in.} \geq 1.19 \text{ in.} + \frac{3}{4} \text{ in.}$ |
| $= 6.30 \text{ in.} > 1.94 \text{ in.}$ | $= 6.30 \text{ in.} > 1.94 \text{ in.}$ |

---

# K-25

For web local yielding, use constants $R_1$ and $R_2$ from AISC *Manual* Table 9-4.

| LRFD | ASD |
|------|-----|
| From AISC *Manual* Equation 9-60a and Table 9-4: | From AISC *Manual* Equation 9-60b and Table 9-4: |
| $W_{min} = \frac{R_u - \phi R_1}{\phi R_2} + \text{setback} \geq k_{des} + \text{setback}$ | $W_{min} = \frac{R_a - R_1 / \Omega}{R_2 / \Omega} + \text{setback} \geq k_{des} + \text{setback}$ |
| $= \frac{120 \text{ kips} - 64.0 \text{ kips}}{21.5 \text{ kip/in.}} + \frac{3}{4} \text{ in.} \geq 1.19 \text{ in.} + \frac{3}{4} \text{ in.}$ | $= \frac{80.0 \text{ kips} - 42.6 \text{ kips}}{14.3 \text{ kip/in.}} + \frac{3}{4} \text{ in.} \geq 1.19 \text{ in.} + \frac{3}{4} \text{ in.}$ |
| $= 3.35 \text{ in.} > 1.94 \text{ in.}$ | $= 3.37 \text{ in.} > 1.94 \text{ in.}$ |

The minimum stiffener width, $W_{min}$, for web local crippling controls. The stiffener width of 7 in. is adequate.

Check the assumption that $l_b/d > 0.2$.

$$l_b = 7 \text{ in.} - \frac{3}{4} \text{ in.}$$
$$= 6.25 \text{ in.}$$

$$\frac{l_b}{d} = \frac{6.25 \text{ in.}}{21.1 \text{ in.}}$$

$$= 0.296 > 0.2$$, as assumed

*Weld Strength Requirements for the Seat Plate*

Check the stiffener length, $l = 24$ in., with $\frac{5}{16}$ in. fillet welds. Enter AISC *Manual* Table 10-8, using $W = 7$ in. as verified in the preceding text.

| LRFD | ASD |
|------|-----|
| $\phi R_n = 293 \text{ kips} > 120 \text{ kips}$ **o.k.** | $\frac{R_n}{\Omega} = 195 \text{ kips} > 80.0 \text{ kips}$ **o.k.** |

From AISC *Manual* Part 10, Figure 10-11(b), the minimum length of the seat-plate-to-HSS weld on each side of the stiffener is $0.2l = 4.80$ in. This establishes the minimum weld between the seat plate and stiffener. A 5-in.-long, $\frac{5}{16}$ in. weld on each side of the stiffener is adequate.

*Minimum HSS Wall Thickness to Match Weld Strength*

The minimum HSS wall thickness required to match the shear rupture strength of the base metal to that of the weld is:

$$t_{min} = \frac{3.09D}{F_u}$$
$({Manual} \text{ Eq. 9-6})$

$$= \frac{3.09(5)}{62 \text{ ksi}}$$

$$= 0.249 \text{ in.} < 0.465 \text{ in.}$$

Because the $t$ of the HSS is greater than $t_{min}$ for the $\frac{5}{16}$ in. fillet weld, no reduction in the weld strength to account for shear in the HSS is required.

---

# K-26

*Stiffener Plate Thickness*

From AISC *Manual* Part 10, Table 10-8 discussion, to develop the stiffener-to-seat-plate welds, the minimum stiffener thickness is:

$$t_p \, _{min} = 1.5w$$
$$= 1.5(\frac{5}{16} \text{ in.})$$
$$= 0.469 \text{ in.}$$

Also, from AISC *Manual* Part 10, Table 10-8 Note 2, for a stiffener and beam with $F_y = 50$ ksi, the minimum stiffener thickness is:

$$t_p \, _{min} = \left(\frac{F_y,beam}{F_y,stiffener}\right)t_w$$

$$= \left(\frac{50 \text{ ksi}}{50 \text{ ksi}}\right)(0.430 \text{ in.})$$

$$= 0.430 \text{ in.}$$

The stiffener thickness of ⅝ in. is adequate.

Determine the stiffener length using AISC *Manual* Table 10-15.

The required HSS wall strength factor is:

| LRFD | ASD |
|------|-----|
| $\left(\frac{R_u W}{t^2}\right)_{req} = \frac{(120 \text{ kips})(7 \text{ in.})}{(0.465 \text{ in.})^2}$ | $\left(\frac{R_a W}{t^2}\right)_{req} = \frac{(80.0 \text{ kips})(7 \text{ in.})}{(0.465 \text{ in.})^2}$ |
| $= 3{,}880 \text{ kip/in.}$ | $= 2{,}590 \text{ kip/in.}$ |

To satisfy the minimum, select a stiffener with $l = 24$ in. from AISC *Manual* Table 10-15. The HSS wall strength factor is:

| LRFD | ASD |
|------|-----|
| $\frac{R_u W}{t^2} = 4{,}250 \text{ kip/in.} > 3{,}880 \text{ kip/in.}$ **o.k.** | $\frac{R_a W}{t^2} = 2{,}830 \text{ kip/in.} > 2{,}590 \text{ kip/in.}$ **o.k.** |

Use PL⅝ in.×7 in. × 2 ft 0 in. for the stiffener.

*HSS Width Check*

The minimum width is $0.4l + t_p + 2(2.25t)$; however, because the specified weld length of 5 in. on each side of the stiffener is greater than $0.4l$, the weld length will be used. The nominal wall thickness, $t_{nom}$, is used, as would be used to calculate a workable flat dimension.

$$B = 14.0 \text{ in.} > (2 \text{ welds})(5.00 \text{ in.}) + \frac{5}{8} \text{ in.} + 2(2.25)(\frac{1}{2} \text{ in.})$$

$$= 14.0 \text{ in.} > 12.9 \text{ in.}$$ **o.k.**

---

# K-27

*Seat Plate Dimensions*

Based on the minimum edge distance provided in AISC *Specification* Table J3.4, to accommodate two ¾-in.-diameter, Group 120 bolts on a 5½ in. gage connecting the beam flange to the seat plate, a minimum width of 7½ in. is required. To accommodate the seat-plate-to-HSS weld, the required width is:

$$2(5.00 \text{ in.}) + \frac{5}{8} \text{ in.} = 10.6 \text{ in.}$$

Note: To allow room to start and stop welds, an 11.5 in. width is used.

Use PL⅜ in.×7 in.× 0 ft-11½ in. for the seat plate.

*Top Angle, Bolts, and Welds (AISC Manual Part 10)*

The minimum weld size for the HSS thickness according to AISC *Specification* Table J2.4 is $\frac{3}{16}$ in. The angle thickness should be $\frac{1}{16}$ in. larger.

Use L4×4×¼ with $\frac{3}{16}$ in. fillet welds along the toes of the angle to the beam flange and HSS for stability. Alternatively, two ¾-in.-diameter, Group 120 bolts may be used to connect the leg of the angle to the beam flange.

---

# K-28

# EXAMPLE K.6 SINGLE-PLATE CONNECTION TO A RECTANGULAR HSS COLUMN

**Given:**

Use AISC *Manual* Table 10-10 to verify the design of a single-plate connection for an ASTM A992/A992M W18×35 beam framing into an ASTM A500/A500M Grade C HSS6×6×⅜ column, as shown in Figure K.6-1. Use 70-ksi weld electrodes. The plate material is ASTM A572/A572M Grade 50. Use the following vertical shear loads:

$P_D = 6.5$ kips
$P_L = 19.5$ kips

<diagram>
Figure K.6-1 shows the connection geometry for Example K.6.

The diagram shows:
- HSS6×6×⅜ column
- 3" dimension at top
- ¾" dia. Group 120, thread condition N, std. holes
- PL$\frac{5}{16}$×4½×0'-8½" connection plate
- Bolt spacing: 2@3" = 6", with 8½" total height dimension
- $l_{eh} = 1\frac{1}{4}"$ dimension shown
- W18×35 beam
- $\frac{1}{4}$ and $\frac{1}{4}$ weld dimensions shown
</diagram>

*Fig K.6-1. Connection geometry for Example K.6.*

**Solution:**

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Beam
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Column
ASTM A500/A500M Grade C
$F_y = 50$ ksi
$F_u = 62$ ksi

Plate
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

---

# K-29

From AISC *Manual* Tables 1-1 and 1-12, the geometric properties are as follows:

W18×35
$d = 17.7$ in.
$t_w = 0.300$ in.
$T = 15\frac{1}{2}$ in.

HSS6×6×⅜
$B = H = 6.00$ in.
$t = 0.349$ in.
$b/t = 14.2$

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(6.5 \text{ kips}) + 1.6(19.5 \text{ kips})$ | $R_a = 6.5 \text{ kips} + 19.5 \text{ kips}$ |
| $= 39.0$ kips | $= 26.0$ kips |

*Single-Plate Connection*

As discussed in AISC *Manual* Part 10, a single-plate connection may be used as long as the HSS wall is not classified as a slender element.

$$\frac{b}{t} \leq 1.40\sqrt{\frac{E}{F_y}}$$

$$14.2 \leq 1.40\sqrt{\frac{29{,}000 \text{ ksi}}{50 \text{ ksi}}}$$

$$14.2 < 33.7$$

Therefore, the HSS wall is not slender.

The available strength of the face of the HSS for the limit state of punching shear is determined from AISC *Manual* Part 10 as follows:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $R_u e \leq \frac{\phi F_u t_{des} l_p^2}{5}$ $({Manual} \text{ Eq. 10-10a})$ | $R_a e \leq \frac{F_u t_{des} l_p^2}{5\Omega}$ $({Manual} \text{ Eq. 10-10b})$ |
| $(39.0 \text{ kips})(3 \text{ in.}) \leq \frac{0.75(62 \text{ ksi})(0.349 \text{ in.})(8.50 \text{ in.})^2}{5}$ | $(26.0 \text{ kips})(3 \text{ in.}) \leq \frac{(62 \text{ ksi})(0.349 \text{ in.})(8.50 \text{ in.})^2}{5(2.00)}$ |
| 117 kip-in. < 235 kip-in.   **o.k.** | 78.0 kip-in. < 156 kip-in.   **o.k.** |

Try three rows of bolts and a $\frac{5}{16}$ in. plate thickness with ¼ in. fillet welds. From AISC *Manual* Table 10-9, either the plate or the beam web must satisfy:

---

# K-30

$$t \leq \frac{d}{2} + \frac{1}{16} \text{ in.}$$

$$\frac{5}{16} \text{ in.} \leq \frac{\frac{3}{4} \text{ in.}}{2} + \frac{1}{16} \text{ in.}$$

$$\frac{5}{16} \text{ in.} < 0.438 \text{ in.}$$ **o.k.**

*Single Plate Available Strength*

AISC *Manual* Table 10-10a includes checks for the limit states of shear rupture of the plate, block shear rupture of the plate, and weld shear.

Check three rows of ¾-in.-diameter bolts in standard holes, $\frac{5}{16}$ in. plate thickness, and ¼ in. fillet weld size. From AISC *Manual* Table 10-10a, the weld and single-plate available strength is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 53.7 \text{ kips} > 39.0 \text{ kips}$ **o.k.** | $\frac{R_n}{\Omega} = 35.8 \text{ kips} > 26.0 \text{ kips}$ **o.k.** |

*Available Shear Transfer Strength at Bolt Holes*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength per AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the plate at the bolt holes per AISC *Specification* Section J3.11, and (3) the available bearing or tearout strength of the beam web at the bolt holes per AISC *Specification* Section J3.11.

From AISC *Manual* Table 10-1b, the available bolt shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) in single shear is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9$ kips | $\frac{r_n}{\Omega} = 11.9$ kips |

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the plate per bolt for ¾-in.-diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): | For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): |
| $\phi r_n = (49.4 \text{ kip/in.})(\frac{5}{16} \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kip/in.})(\frac{5}{16} \text{ in.})$ |
| $= 15.4$ kips | $= 10.3$ kips |
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kip/in.})(\frac{5}{16} \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(\frac{5}{16} \text{ in.})$ |
| $= 27.4$ kips | $= 18.3$ kips |

From AISC *Manual* Table 10-1b, the available bearing and tearout strength of the beam web per bolt for ¾-in.-diameter bolts in standard holes is:

---

# K-31

| LRFD | ASD |
|------|-----|
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kip/in.})(0.300 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(0.300 \text{ in.})$ |
| $= 26.3$ kips | $= 17.6$ kips |

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the plate for a non-edge bolt, and available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min\begin{Bmatrix} 17.9 \text{ kips,} \\ 27.4 \text{ kips,} \\ 26.3 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips,} \\ 18.3 \text{ kips,} \\ 17.6 \text{ kips} \end{Bmatrix}$ |
| $= 17.9$ kips | $= 11.9$ kips |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the plate for an edge bolt, and available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min\begin{Bmatrix} 17.9 \text{ kips,} \\ 15.4 \text{ kips,} \\ 26.3 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips,} \\ 10.3 \text{ kips,} \\ 17.6 \text{ kips} \end{Bmatrix}$ |
| $= 15.4$ kips | $= 10.3$ kips |

At the other connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the plate for a non-edge bolt, and available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,other} = \min\begin{Bmatrix} 17.9 \text{ kips,} \\ 27.4 \text{ kips,} \\ 26.3 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,other}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips,} \\ 18.3 \text{ kips,} \\ 17.6 \text{ kips} \end{Bmatrix}$ |
| $= 17.9$ kips | $= 11.9$ kips |

To account for eccentricity, the available shear transfer strength is multiplied by the factor $C/n$. From AISC *Manual* Table 10-10b, for 3 bolts in standard holes:

$$C/n = 0.823$$

The available shear transfer strength at the bolt holes is:

---

# K-32

| LRFD | ASD |
|------|-----|
| $\phi R_n = C/n\left[\phi r_{n,bot} + \phi r_{n,top} + \phi r_{n,other}(n-2)\right]$ | $\frac{R_n}{\Omega} = C/n\left[\frac{r_{n,top}}{\Omega} + \frac{r_{n,bot}}{\Omega} + \frac{r_{n,other}}{\Omega}(n-2)\right]$ |
| $= 0.823\left[15.4 \text{ kips} + 17.9 \text{ kips} + 17.9 \text{ kips}(3-2)\right]$ | $= 0.823\left[11.9 \text{ kips} + 10.3 \text{ kips} + 11.9 \text{ kips}(3-2)\right]$ |
| $= 42.1 \text{ kips} > 39.0 \text{ kips}$ **o.k.** | $= 28.1 \text{ kips} > 26.0 \text{ kips}$ **o.k.** |

Use a PL$\frac{5}{16}$ in.×4½ in. × 0 ft 8½ in.

*Available Beam Web Strength*

Because the beam is not coped, limit states of block shear rupture and shear rupture of the beam are not applicable. The beam web is adequate for the required loading.

*HSS Shear Rupture at Welds*

The minimum HSS wall thickness required to match the shear rupture strength of the HSS wall to that of the weld is:

$$t_{min} = \frac{3.09D}{F_u}$$
$({Manual} \text{ Eq. 9-6})$

$$= \frac{3.09(4)}{62 \text{ ksi}}$$

$$= 0.199 \text{ in.} < t = 0.349 \text{ in.}$$ **o.k.**

---

# K-33

# EXAMPLE K.7 THROUGH-PLATE CONNECTION TO A RECTANGULAR HSS COLUMN

**Given:**

Use AISC *Manual* Table 10-10 to verify a through-plate connection between an ASTM A992/A992M W18×35 beam and an ASTM A500/A500M Grade C HSS6×4×⅛ with the connection to one of the 6 in. faces, as shown in Figure K.7-1. A thin-walled column is used to illustrate the design of a through-plate connection. Use 70-ksi weld electrodes. The plate is ASTM A572/A572M Grade 50 material. Use the following vertical shear loads:

$P_D = 3.3$ kips
$P_L = 9.9$ kips

<diagram>
Figure K.7-1 shows the connection geometry for Example K.7.

The diagram shows:
- HSS6×4×⅛ column with through-plate connection
- 4" and 3" dimensions at top
- PL¼×9 plate passing through HSS column
- 1⅛" dimension shown
- $l_{eh} = 1\frac{1}{4}"$ dimension
- Bolt spacing: 2@3" = 6", with 8½" total height
- W18×35 beam
- ¾" dia. Group 120, thread condition N, std. holes
- $\frac{3}{16}$ and $\frac{3}{16}$ weld dimensions shown
</diagram>

*Fig K.7-1. Connection geometry for Example K.7.*

**Solution:**

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Beam
ASTM A992
$F_y = 50$ ksi
$F_u = 65$ ksi

Column
ASTM A500 Grade C
$F_y = 50$ ksi
$F_u = 62$ ksi

Plate
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

---

# K-34

From AISC *Manual* Tables 1-1 and 1-11, the geometric properties are as follows:

W18×35
$d = 17.7$ in.
$t_w = 0.300$ in.
$T = 15\frac{1}{2}$ in.

HSS6×4×⅛
$B = 4.00$ in.
$H = 6.00$ in.
$t = 0.116$ in.
$h/t = 48.7$
$b/t = 31.5$

*HSS wall slenderness*

From AISC *Manual* Part 10, the limiting width-to-thickness for a nonslender HSS wall is:

$$1.40\sqrt{\frac{E}{F_y}} = 1.40\sqrt{\frac{29{,}000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 33.7$$

Because $h/t = 48.7 > 33.7$, the HSS6×4×⅛ is slender, and a through-plate connection should be used instead of a single-plate connection. Through-plate connections are typically very expensive. When a single-plate connection is not adequate, another type of connection, such as a double-angle connection, may be preferable to a through-plate connection.

AISC *Specification* Chapter K does not contain provisions for the design of through-plate shear connections. The following procedure treats the connection of the through-plate to the beam as a single-plate connection.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(3.3 \text{ kips}) + 1.6(9.9 \text{ kips})$ | $R_a = 3.3 \text{ kips} + 9.9 \text{ kips}$ |
| $= 19.8$ kips | $= 13.2$ kips |

*Portion of the Through-Plate Connection that Resembles a Single Plate*

Try three rows of bolts ($l = 8\frac{1}{2}$ in.) and a ¼ in. plate thickness with $\frac{3}{16}$ in. fillet welds.

$$\frac{T}{2} = \frac{15\frac{1}{2} \text{ in.}}{2}$$

$$= 7.75 \text{ in.} < l = 8\frac{1}{2} \text{ in.}$$ **o.k.**

Note: From AISC *Manual* Table 10-9, either the plate thickness or the beam web thickness must satisfy:

$$t \leq \frac{d}{2} + \frac{1}{16} \text{ in.}$$

$$\frac{1}{4} \text{ in.} \leq \frac{\frac{3}{4} \text{ in.}}{2} + \frac{1}{16} \text{ in.}$$

$$\frac{1}{4} \text{ in.} < 0.438 \text{ in.}$$ **o.k.**

---

# K-35

*Single Plate Available Strength*

AISC *Manual* Table 10-10a includes checks for the limit states of shear rupture of the plate, block shear rupture of the plate, and weld shear.

Check three rows of ¾-in.-diameter bolts in standard holes, ¼ in. plate thickness, and $\frac{3}{16}$ in. fillet weld size. From AISC *Manual* Table 10-10a, the weld and single-plate available strength is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 43.0 \text{ kips} > 19.8 \text{ kips}$ **o.k.** | $\frac{R_n}{\Omega} = 28.6 \text{ kips} > 13.2 \text{ kips}$ **o.k.** |

*Available Shear Transfer Strength at Bolt Holes*

The available shear transfer strength at bolt holes is the sum of the effective strength of individual bolts per the User Note in AISC *Specification* Section J3.7, which is the least of (1) the available bolt shear strength per AISC *Specification* Section J3.7, (2) the available bearing or tearout strength of the plate at the bolt holes per AISC *Specification* Section J3.11, and (3) the available bearing or tearout strength of the beam web at the bolt holes per AISC *Specification* Section J3.11.

From AISC *Manual* Table 10-1b, the available bolt shear strength per bolt for ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) in single shear is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 17.9$ kips | $\frac{r_n}{\Omega} = 11.9$ kips |

From AISC *Manual* Table 10-10b, the available bearing and tearout strength of the plate per bolt for ¾-in.-diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): | For the edge bolt ($l_{ev} = 1\frac{1}{4}$ in.): |
| $\phi r_n = (49.4 \text{ kip/in.})(\frac{1}{4} \text{ in.})$ | $\frac{r_n}{\Omega} = (32.9 \text{ kip/in.})(\frac{1}{4} \text{ in.})$ |
| $= 12.4$ kips | $= 8.23$ kips |
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kip/in.})(\frac{1}{4} \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(\frac{1}{4} \text{ in.})$ |
| $= 22.0$ kips | $= 14.6$ kips |

From AISC *Manual* Table 10-10b, the available bearing and tearout strength of the beam web per bolt for ¾-in.-diameter bolts in standard holes is:

| LRFD | ASD |
|------|-----|
| For the non-edge bolts ($s = 3$ in.): | For the non-edge bolts ($s = 3$ in.): |
| $\phi r_n = (87.8 \text{ kip/in.})(0.300 \text{ in.})$ | $\frac{r_n}{\Omega} = (58.5 \text{ kip/in.})(0.300 \text{ in.})$ |
| $= 26.3$ kips | $= 17.6$ kips |

---

# K-36

At the top connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the plate for a non-edge bolt, and available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,top} = \min\begin{Bmatrix} 17.9 \text{ kips,} \\ 22.0 \text{ kips,} \\ 26.3 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,top}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips,} \\ 14.6 \text{ kips,} \\ 17.6 \text{ kips} \end{Bmatrix}$ |
| $= 17.9$ kips | $= 11.9$ kips |

At the bottom connection bolt, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the plate for an edge bolt, and available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,bot} = \min\begin{Bmatrix} 17.9 \text{ kips,} \\ 12.4 \text{ kips,} \\ 26.3 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,bot}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips,} \\ 8.23 \text{ kips,} \\ 17.6 \text{ kips} \end{Bmatrix}$ |
| $= 12.4$ kips | $= 8.23$ kips |

At the other connection bolts, the available shear transfer strength is the minimum of the available bolt shear strength, the available bearing and tearout strength of the plate for a non-edge bolt, and available bearing and tearout strength of the beam web for a non-edge bolt:

| LRFD | ASD |
|------|-----|
| $\phi r_{n,other} = \min\begin{Bmatrix} 17.9 \text{ kips,} \\ 22.0 \text{ kips,} \\ 26.3 \text{ kips} \end{Bmatrix}$ | $\frac{r_{n,other}}{\Omega} = \min\begin{Bmatrix} 11.9 \text{ kips,} \\ 14.6 \text{ kips,} \\ 17.6 \text{ kips} \end{Bmatrix}$ |
| $= 17.9$ kips | $= 11.9$ kips |

To account for eccentricity, the available shear transfer strength is multiplied by the factor $C/n$. From AISC *Manual* Table 10-10b, for 3 bolts in standard holes:

$$C/n = 0.823$$

The available shear transfer strength at the bolt holes is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = C/n\left[\phi r_{n,bot} + \phi r_{n,top} + \phi r_{n,other}(n-2)\right]$ | $\frac{R_n}{\Omega} = C/n\left[\frac{r_{n,top}}{\Omega} + \frac{r_{n,bot}}{\Omega} + \frac{r_{n,other}}{\Omega}(n-2)\right]$ |
| $= 0.823\left[12.4 \text{ kips} + 17.9 \text{ kips} + 17.9 \text{ kips}(3-2)\right]$ | $= 0.823\left[8.23 \text{ kips} + 11.9 \text{ kips} + 11.9 \text{ kips}(3-2)\right]$ |
| $= 39.7 \text{ kips} > 19.8 \text{ kips}$ **o.k.** | $= 26.4 \text{ kips} > 13.2 \text{ kips}$ **o.k.** |

*Available Beam Web Strength*

Since the beam is not coped, limit states of block shear rupture and shear rupture of the beam are not applicable. The beam web is adequate for the required loading.

---

# K-37

*Required Weld Strength*

The available strength for the welds in this connection is checked at the location of the maximum reaction, which is along the weld line closest to the bolt line. The reaction at this weld line is determined by taking a moment about the weld line farthest from the bolt line.

$a = 3$ in. (distance from bolt line to nearest weld line)

| LRFD | ASD |
|------|-----|
| $V_{fn} = \frac{R_u(B+a)}{B}$ | $V_{fa} = \frac{R_a(B+a)}{B}$ |
| $= \frac{(19.8 \text{ kips})(4.00 \text{ in.} + 3 \text{ in.})}{4.00 \text{ in.}}$ | $= \frac{(13.2 \text{ kips})(4.00 \text{ in.} + 3 \text{ in.})}{4.00 \text{ in.}}$ |
| $= 34.7$ kips | $= 23.1$ kips |

*Available Weld Strength*

The minimum required weld size is determined using AISC *Manual* Part 8.

| LRFD | ASD |
|------|-----|
| $D_{req} = \frac{V_{fn}}{1.392l}$ (from *Manual* Eq. 8-2a) | $D_{req} = \frac{V_{fa}}{0.928l}$ (from *Manual* Eq. 8-2b) |
| $= \frac{34.7 \text{ kips}}{(1.392 \text{ kip/in.})(8.50 \text{ in.})(2)}$ | $= \frac{23.1 \text{ kips}}{(0.928 \text{ kip/in.})(8.50 \text{ in.})(2)}$ |
| $= 1.47 \text{ sixteenths} < 3 \text{ sixteenths}$ **o.k.** | $= 1.46 \text{ sixteenths} < 3 \text{ sixteenths}$ **o.k.** |

*HSS Shear Yielding and Rupture Strength*

The available shear yielding strength of the HSS is determined from AISC *Specification* Section J4.2.

$$A_{gv} = (2 \text{ welds})t$$
$$= (2 \text{ welds})(8.50 \text{ in.})(0.116 \text{ in.})$$
$$= 1.97 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$
$(Spec. \text{ Eq. J4-3})$

$$= 0.60(50 \text{ ksi})(1.97 \text{ in.}^2)$$

$$= 59.1 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
| $\phi R_n = 1.00(59.1 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{59.1 \text{ kips}}{1.50}$ |
| $= 59.1 \text{ kips} > 34.7 \text{ kips}$ **o.k.** | $= 39.4 \text{ kips} > 23.1 \text{ kips}$ **o.k.** |

The available shear rupture strength of the HSS is determined from AISC *Specification* Section J4.2.

$$A_{nv} = A_{gv}$$

$$= 1.97 \text{ in.}^2$$

---

# K-38

$$R_n = 0.60F_u A_{nv}$$
$(Spec. \text{ Eq. J4-4})$

$$= 0.60(62 \text{ ksi})(1.97 \text{ in.}^2)$$

$$= 73.3 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(73.3 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{73.3 \text{ kips}}{2.00}$ |
| $= 55.0 \text{ kips} > 34.7 \text{ kips}$ **o.k.** | $= 36.7 \text{ kips} > 23.1 \text{ kips}$ **o.k.** |

---

# K-39

# EXAMPLE K.8 LONGITUDINAL PLATE LOADED PERPENDICULAR TO THE HSS AXIS ON A ROUND HSS

**Given:**

Verify the local strength of the ASTM A500/A500M Grade C HSS6.000×0.375 tension chord subject to transverse loads, $P_D = 4$ kips and $P_L = 12$ kips, applied through an ASTM A572/A572M Grade 50 plate, as shown in Figure K.8-1.

<diagram>
Figure K.8-1 shows the loading and geometry for Example K.8.

The diagram shows:
- $\mathbb{C}_L$ HSS (centerline of HSS)
- $\mathbb{C}_L$ Plate (centerline of Plate)
- HSS6.000×0.375 round tube shown in cross-section
- PL¼×4×4 plate attached to HSS
- $P_D = 4$ kips and $P_L = 12$ kips loads applied downward through the plate
</diagram>

*Fig K.8-1. Loading and geometry for Example K.8.*

**Solution:**

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Chord
ASTM A500/A500M Grade C
$F_y = 50$ ksi
$F_u = 62$ ksi

Plate
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Table 1-13, the geometric properties are as follows:

HSS6.000×0.375
$D = 6.00$ in.
$t = 0.349$ in.
$D/t = 17.2$

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(4 \text{ kips}) + 1.6(12 \text{ kips})$ | $P_a = 4 \text{ kips} + 12 \text{ kips}$ |
| $= 24.0$ kips | $= 16.0$ kips |

---

# K-40

*Limits of Applicability of AISC Specification Section K2.2, Table K2.1A*

AISC *Specification* Table K2.1A provides the limits of applicability for plate-to-round connections. The applicable limits for this example are:

HSS wall slenderness:
$D/t \leq 50$ for T-connections
$17.2 < 50$ **o.k.**

Material strength:
$F_y \leq 52$ ksi
50 ksi < 52 ksi   **o.k.**

Ductility:
From the note in AISC *Specification* Table K2.1A, ASTM A500/A500M Grade C is acceptable.

*Minimum End Distance*

From AISC *Specification* Section K1.4, the minimum end distance is:

$$\beta = \frac{B_p}{D}$$

$$= \frac{\frac{1}{4} \text{ in.}}{6.00 \text{ in.}}$$

$$= 0.0417 \text{ in.}$$

$$l_{end} \geq D\left(1.25 - \frac{\beta}{2}\right)$$
$(Spec. \text{ Eq. K1-8})$

$$= (6.00 \text{ in.})\left(1.25 - \frac{0.0417}{2}\right)$$

$$= 7.37 \text{ in.}$$

Thus, the edge of the plate must be located a minimum of 7.37 in. from the end of the HSS.

*HSS Plastification Limit State*

The limit state of HSS plastification applies and is determined from AISC *Specification* Table K2.1.

$$R_n \sin\theta = 5.5F_y t^2\left[1 + 0.25\left(\frac{l_p}{D}\right)\right]Q_f$$
$(Spec. \text{ Eq. K2-2a})$

From the AISC *Specification* Section K1.3(a), for an HSS connecting surface in tension, $Q_f = 1.0$.

$$R_n = \frac{5.5(50 \text{ ksi})(0.349 \text{ in.})^2\left[1 + 0.25\left(\frac{4 \text{ in.}}{6.00 \text{ in.}}\right)\right](1.0)}{\sin 90^\circ}$$

$$= 39.1 \text{ kips}$$

The available strength is:

---

# K-41

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
| $\phi R_n = 0.90(39.1 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{39.1 \text{ kips}}{1.67}$ |
| $= 35.2 \text{ kips} > 24.0 \text{ kips}$ **o.k.** | $= 23.4 \text{ kips} > 16.0 \text{ kips}$ **o.k.** |

---

# K-42

# EXAMPLE K.9 RECTANGULAR HSS COLUMN BASE PLATE

**Given:**

An ASTM A500/A500M Grade C HSS6×6×½ column is supporting loads of 40 kips of dead load and 120 kips of live load. The column is supported by a 7 ft 6 in. × 7 ft 6 in. concrete spread footing with $f_c' = 3{,}000$ psi. Verify the ASTM A572/A572M Grade 50 base plate size shown in Figure K.9-1 is adequate for this column.

<diagram>
Figure K.9-1 shows the base plate geometry for Example K.9.

The diagram shows a plan view with:
- HSS6×6×½ column centered on base plate
- PL1×13×1'-1" base plate
- ¾" dia. anchor rods in 1$\frac{5}{16}$" max. dia. holes positioned at four corners
- Dimensions: 6½" × 6½" between anchor rod pairs
- 1½" edge distances on all sides (1½" from edges of plate)
- $\frac{1}{4}$ weld indicated
</diagram>

*Fig K.9-1. Base plate geometry for Example K.9.*

**Solution:**

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Column
ASTM A500/A500M Grade C
$F_y = 50$ ksi
$F_u = 62$ ksi

Base Plate
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Table 1-12, the geometric properties are as follows:

HSS6×6×½
$B = H = 6.00$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(40 \text{ kips}) + 1.6(120 \text{ kips})$ | $P_a = 40 \text{ kips} + 120 \text{ kips}$ |
| $= 240$ kips | $= 160$ kips |

Note: The procedure illustrated here is similar to that presented in AISC Design Guide 1, *Base Plate and Anchor Rod Design* (Fisher and Kloiber, 2006), and AISC *Manual* Part 14.

---

# K-43

Try a base plate which extends $3\frac{1}{2}$ in. from each face of the HSS column, or 13 in. × 13 in.

*Available Strength for the Limit State of Concrete Crushing*

On less than the full area of a concrete support:

$$P_p = 0.85f_c'A_1\sqrt{\frac{A_2}{A_1}} \leq 1.7f_c'A_1$$
$(Spec. \text{ Eq. J8-2})$

$$A_1 = BN$$
$$= (13 \text{ in.})(13 \text{ in.})$$
$$= 169 \text{ in.}^2$$

$$A_2 = \left[(7.5 \text{ ft})(12 \text{ in./ft})\right]^2$$
$$= 8{,}100 \text{ in.}^2$$

$$P_p = 0.85(3 \text{ ksi})(169 \text{ in.}^2)\sqrt{\frac{8{,}100 \text{ in.}^2}{169 \text{ in.}^2}} \leq 1.7(3 \text{ ksi})(169 \text{ in.}^2)$$

$$= 2{,}980 \text{ kips} > 862 \text{ kips}$$

Use $P_p = 862$ kips.

Note: The limit on the right side of AISC *Specification* Equation J8-2 will control when $A_2/A_1$ exceeds 4.0.

| LRFD | ASD |
|------|-----|
| From AISC *Specification* Section J8: | From AISC *Specification* Section J8: |
| $\phi_c = 0.65$ | $\Omega_c = 2.31$ |
| $\phi_c P_p = 0.65(862 \text{ kips})$ | $\frac{P_p}{\Omega_c} = \frac{862 \text{ kips}}{2.31}$ |
| $= 560 \text{ kips} > 240 \text{ kips}$ **o.k.** | $= 373 \text{ kips} > 160 \text{ kips}$ **o.k.** |

*Pressure under Bearing Plate and Required Thickness*

For a rectangular HSS, the distance $m$ or $n$ is determined using 0.95 times the depth and width of the HSS.

$$m = n$$
(from *Manual* Eq. 14-2)

$$= \frac{N - 0.95(B \text{ or } H)}{2}$$

$$= \frac{13 \text{ in.} - 0.95(6.00 \text{ in.})}{2}$$

$$= 3.65 \text{ in.}$$

Note: As discussed in AISC Design Guide 1, the $\lambda n'$ cantilever distance is not used for HSS and pipe.

The critical bending moment is the cantilever moment outside the HSS perimeter. Therefore, $m = n = l$.

---

# K-44

| LRFD | ASD |
|------|-----|
| $f_{pu} = \frac{P_u}{A_1}$ | $f_{pa} = \frac{P_a}{A_1}$ |
| $= \frac{240 \text{ kips}}{169 \text{ in.}^2}$ | $= \frac{160 \text{ kips}}{169 \text{ in.}^2}$ |
| $= 1.42$ ksi | $= 0.947$ ksi |
| $M_u = \frac{f_{pu}l^2}{2}$ | $M_a = \frac{f_{pa}l^2}{2}$ |
| $Z = \frac{t_p^2}{4}$ | $Z = \frac{t_p^2}{4}$ |
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $M_n = M_p = F_y Z$ (from *Spec.* Eq. F11-1) | $M_n = M_p = F_y Z$ (from *Spec.* Eq. F11-1) |
| Note: the upper limit of $1.5F_y S_x$ will provide equivalent results for a rectangular plate. | Note: the upper limit of $1.5F_y S_x$ will provide equivalent results for a rectangular plate. |
| Equating: | Equating: |
| $M_u = \phi_b M_n$ and solving for $t_p$ gives: | $M_a = M_n/\Omega_b$ and solving for $t_p$ gives: |
| $t_p(req) = \sqrt{\frac{2f_{pu}l^2}{\phi_b F_y}}$ | $t_p(req) = \sqrt{\frac{2f_{pa}l^2}{F_y/\Omega_b}}$ |
| $= \sqrt{\frac{2(1.42 \text{ ksi})(3.65 \text{ in.})^2}{0.90(50 \text{ ksi})}}$ | $= \sqrt{\frac{2(0.947 \text{ ksi})(3.65 \text{ in.})^2}{(50 \text{ ksi})/1.67}}$ |
| $= 0.917$ in. | $= 0.918$ in. |
| Or use AISC *Manual* Equation 14-7a: | Or use AISC *Manual* Equation 14-7b: |
| $t_{min} = l\sqrt{\frac{2P_u}{0.90F_y BN}}$ | $t_{min} = l\sqrt{\frac{1.67(2P_a)}{F_y BN}}$ |
| $= (3.65 \text{ in.})\sqrt{\frac{2(240 \text{ kips})}{0.90(50 \text{ ksi})(13 \text{ in.})(13 \text{ in.})}}$ | $= (3.65 \text{ in.})\sqrt{\frac{1.67(2)(160 \text{ kips})}{(50 \text{ ksi})(13 \text{ in.})(13 \text{ in.})}}$ |
| $= 0.917$ in. | $= 0.918$ in. |

Therefore, the PL1 in. × 13 in. × 1 ft 1 in. is adequate.

---

# K-45

# EXAMPLE K.10 RECTANGULAR HSS STRUT END PLATE

**Given:**

Determine the weld leg size, end-plate thickness, and the bolt size required to resist forces of 16 kips from dead load and 50 kips from live load for an ASTM A500/A500M Grade C section, as shown in Figure K.10-1. The end plate is ASTM A572/A572M Grade 50 material. Use 70-ksi weld electrodes.

<diagram>
Figure K.10-1 shows the loading and geometry for Example K.10.

The diagram shows two views:

**Left view (elevation):**
- HSS4×4×¼ strut
- PD = 16 kips and PL = 50 kips loads applied horizontally
- Section A-A cut line shown
- Dimensions: $a = 1\frac{1}{2}"$ and $b = 1\frac{1}{2}"$
- Weld details: $t_1$ and $t_1$ shown

**Right view (Section A-A):**
- (4) ¾" dia. Group 120, std. holes shown at four corners
- Square cross-section view of HSS
</diagram>

*Fig K.10-1. Loading and geometry for Example K.10.*

**Solution:**

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Strut
ASTM A500/A500M Grade C
$F_y = 50$ ksi
$F_u = 62$ ksi

End Plate
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Table 1-12, the geometric properties are as follows:

HSS4×4×¼
$t = 0.233$ in.
$A = 3.37$ in.$^2$

From ASCE/SEI 7, Chapter 2, the required tensile strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(16 \text{ kips}) + 1.6(50 \text{ kips})$ | $P_a = 16 \text{ kips} + 50 \text{ kips}$ |
| $= 99.2$ kips | $= 66.0$ kips |

---

# K-46

*Preliminary Size of the (4) Group 120 Bolts*

| LRFD | ASD |
|------|-----|
| $r_ut = \frac{P_u}{n}$ | $r_{at} = \frac{P_a}{n}$ |
| $= \frac{99.2 \text{ kips}}{4}$ | $= \frac{66.0 \text{ kips}}{4}$ |
| $= 24.8$ kips | $= 16.5$ kips |
| Using AISC *Manual* Table 7-2, try ¾-in.-diameter, Group 120 bolts. | Using AISC *Manual* Table 7-2, try ¾-in.-diameter, Group 120 bolts. |
| $\phi r_n = 29.8$ kips | $\frac{r_n}{\Omega} = 19.9$ kips |

*End-Plate Thickness with Consideration of Prying Action (AISC Manual Part 9)*

$$a' = a + \frac{d}{2} \leq 1.25b + \frac{d}{2}$$
(from *Manual* Eq. 9-23)

$$= 1\frac{1}{2} \text{ in.} + \frac{\frac{3}{4} \text{ in.}}{2} \leq 1.25(1\frac{1}{2} \text{ in.}) + \frac{\frac{3}{4} \text{ in.}}{2}$$

$$= 1.88 \text{ in.} < 2.25 \text{ in.}$$

$$= 1.88 \text{ in.}$$

$$b' = b - \frac{d}{2}$$
$({Manual} \text{ Eq. 9-24})$

$$= 1\frac{1}{2} \text{ in.} - \frac{\frac{3}{4} \text{ in.}}{2}$$

$$= 1.13 \text{ in.}$$

$$\rho = \frac{b'}{a'}$$
$({Manual} \text{ Eq. 9-29})$

$$= \frac{1.13 \text{ in.}}{1.88 \text{ in.}}$$

$$= 0.601$$

From AISC *Specification* Table J3.3:

$$d' = 1\frac{3}{16} \text{ in.}$$

The tributary length per bolt (Packer and Olson, 2023),

$$p = \frac{\text{full plate width}}{\text{number of bolts per side}}$$

$$= \frac{10.0 \text{ in.}}{1}$$

$$= 10.0 \text{ in.}$$

---

# K-47

$$\delta = 1 - \frac{d'}{p}$$
$({Manual} \text{ Eq. 9-28})$

$$= 1 - \frac{1\frac{3}{16} \text{ in.}}{10.0 \text{ in.}}$$

$$= 0.919$$

| LRFD | ASD |
|------|-----|
| $\beta = \frac{1}{\rho}\left(\frac{\phi r_n}{r_{ut}} - 1\right)$ (from *Manual* Eq. 9-35) | $\beta = \frac{1}{\rho}\left(\frac{r_n/\Omega}{r_{at}} - 1\right)$ (from *Manual* Eq. 9-35) |
| $= \frac{1}{0.601}\left(\frac{29.8 \text{ kips}}{24.8 \text{ kips}} - 1\right)$ | $= \frac{1}{0.601}\left(\frac{19.9 \text{ kips}}{16.5 \text{ kips}} - 1\right)$ |
| $= 0.335$ | $= 0.343$ |
| Because $\beta < 1$, from AISC *Manual* Equation 9-36b: | Because $\beta < 1$, from AISC *Manual* Equation 9-36b: |
| $\alpha' = \frac{1}{\delta}\left(\frac{\beta}{1-\beta}\right) \leq 1.0$ | $\alpha' = \frac{1}{\delta}\left(\frac{\beta}{1-\beta}\right) \leq 1.0$ |
| $= \frac{1}{0.919}\left(\frac{0.335}{1-0.335}\right) \leq 1.0$ | $= \frac{1}{0.919}\left(\frac{0.343}{1-0.343}\right) \leq 1.0$ |
| $= 0.548$ | $= 0.568$ |

Use Equation 9-37 for $t_{min}$ in Chapter 9 of the AISC *Manual*, except that $F_u$ is replaced by $F_y$ per the recommendation of Willibald et al. (2003) and Packer and Olson (2023).

| LRFD | ASD |
|------|-----|
| $t_{min} = \sqrt{\frac{4r_{ut}b'}{\phi pF_y(1+\delta\alpha')}}$ (from *Manual* Eq. 9-37a) | $t_{min} = \sqrt{\frac{\Omega 4r_{at}b'}{pF_y(1+\delta\alpha')}}$ (from *Manual* Eq. 9-37b) |
| $= \sqrt{\frac{4(24.8 \text{ kips})(1.13 \text{ in.})}{0.90(10.0 \text{ in.})(50 \text{ ksi})[1+0.919(0.548)]}}$ | $= \sqrt{\frac{1.67(4)(16.5 \text{ kips})(1.13 \text{ in.})}{(10.0 \text{ in.})(50 \text{ ksi})[1+0.919(0.568)]}}$ |
| $= 0.407$ in. | $= 0.405$ in. |
| Use a ½-in.-thick end plate, $t_1 > 0.407$ in., further bolt check for prying is not required. | Use a ½-in.-thick end plate, $t_1 > 0.405$ in., further bolt check for prying is not required. |
| Use (4) ¾-in.-diameter, Group 120 bolts. | Use (4) ¾-in.-diameter, Group 120 bolts. |

*Required Weld Size*

From AISC *Specification* Section J2.4(a)(2), for fillet welds at the end of an HSS loaded in tension:

$$k_{ds} = 1.0$$

$$R_n = F_{nw}A_{we}k_{ds}$$
$(Spec. \text{ Eq. J2-4})$

$$F_{nw} = 0.60F_{EXX}$$
$$= 0.60(70 \text{ ksi})$$
$$= 42.0 \text{ ksi}$$

---

# K-48

$$A_{we} = \left(\frac{\sqrt{2}}{2}\right)\left(\frac{D}{16}\right)l$$

where $D$ is the weld size in sixteenths of an inch (i.e., $D$ is an integer).

$$l = 4(4.00 \text{ in.})$$
$$= 16.0 \text{ in.}$$

Note: This weld length is approximate. A more accurate length could be determined by taking into account the curved corners of the HSS.

From AISC *Specification* Table J2.5:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = \phi F_{nw}A_{we}k_{ds}$ | $\frac{R_n}{\Omega} = \frac{F_{nw}A_{we}k_{ds}}{\Omega}$ |
| $= 0.75(42.0 \text{ ksi})\left(\frac{\sqrt{2}}{2}\right)\left(\frac{D}{16}\right)(16.0 \text{ in.})(1.0)$ | $(42.0 \text{ ksi})\left(\frac{\sqrt{2}}{2}\right)\left(\frac{D}{16}\right)(16.0 \text{ in.})(1.0)$ |
|  | $= \frac{}{2.00}$ |
| Setting $\phi R_n = P_u$ and solving for $D$, | Setting $\frac{R_n}{\Omega} = P_a$ and solving for $D$, |
| $D \geq \frac{(99.2 \text{ kips})(16)}{0.75(42.0 \text{ ksi})\left(\frac{\sqrt{2}}{2}\right)(16.0 \text{ in.})(1.0)}$ | $D \geq \frac{2.00(66.0 \text{ kips})(16)}{(42.0 \text{ ksi})\left(\frac{\sqrt{2}}{2}\right)(16.0 \text{ in.})(1.50)}$ |
| $= 4.45$ | $= 4.44$ |
| $D = 5$ (i.e., a $\frac{5}{16}$ in. weld) | $D = 5$ (i.e., a $\frac{5}{16}$ in. weld) |

*Minimum Weld Size Requirements*

For $t = \frac{1}{4}$ in., the minimum weld size is $\frac{1}{8}$ in. from AISC *Specification* Table J2.4.

*Summary:*

Use a $\frac{5}{16}$ in. weld with ½-in.-thick end plates and (4) ¾-in.-diameter, Group 120 bolts.

---

# K-49

# CHAPTER K DESIGN EXAMPLE REFERENCES

Fisher, J.M. and Kloiber, L.A. (2006), *Base Plate and Anchor Rod Design*, Design Guide 1, 2nd Ed., AISC, Chicago, Ill
Packer, J. and Olson, K. (2023), *Hollow Structural Section Connections*, Design Guide 24, 2nd Ed., AISC, Chicago, Ill.
Willibald, S., Packer, J.A., and Puthli, R.S. (2003), "Design Recommendations for Bolted Rectangular HSS Flange Plate Connections in Axial Tension," *Engineering Journal*, AISC, Vol. 40, No. 1, pp. 15–24.

---

# K-50

---

# A6-1

# APPENDIX 6 MEMBER STABILITY BRACING

This Appendix addresses the minimum strength and stiffness necessary to provide a braced point in a column, beam, or beam-column.

The governing limit states for column and beam design may include flexural, torsional, and flexural-torsional buckling for beams. In order to avoid these limit states, bracing and adequate intermediate bracing for the members may be used. For columns, column unbraced lengths per defined braced points of effectively adequate lateral restraint, such as floor and diaphragms that are part of the lateral force resisting system are provided. For a braced column or beam, the member must be laterally unbraced between two consecutive braced points or between a point of support and a braced point. It is also important to define that when calculations will be made for stiffness and stiffness to provide sufficient braced point must satisfy Specification Appendix 6 provides equations for determining the required strength and stiffness when utilized to provide a braced point in a column or beam. The values returned from Appendix 6 are minimum values for the bracing. Fundamentals of Beam Bracing: Strength and Stiffness (*SSRC, 2001*) and *Design Guide 25: Frame Design Using Web-Open Steel Joists and Joist Girders*, (*AISC, 2010)*; *AISC, Manual of Steel Construction* (fourteen), (*AISC, 2011*); *AISC Steel Design Guide* 25 also provides information on member stability bracing.

# 6.1 GENERAL PROVISIONS FOR COLUMNS AND BEAMS

Lateral columns and beam bracing may be either panel or point, while torsional beam bracing may be panel or point. In addition, it is permissible to provide torsional bracing. This type of bracing must provide sufficient strength and stiffness necessary to prevent twist of the section. Lateral bracing should normally be connected near the compression flange. For double-symmetric I-shaped members subject to flexure, column unbraced the lateral displacement of one end of the segment relative to the other. A point brace (formerly referred to as a nodal brace) is connected to a beam or column at a specific location(s) and restrains the lateral or torsional movement(s) of that beam or column member at those braced points. In addition, bracing systems may include components where, adjacent to columns or beams, are also braced beams subject to double curvature bending. Torsional bracing may be connected anywhere on the cross section in a manner to prevent twist of the section.

The requirements in this section apply to bracing associated with the limit state of flexural buckling. For columns that are subject to torsional buckling (Appendix F, Section F4.3, torsional-flexural buckling (Appendix F, Section F3.3), or webs' flexural buckling (Appendix G) or the limit state of lateral-torsional buckling for beams (*Spec.* Section E3), the designer must satisfy the requirements contained in those sections. In order to design bracing for these limit states, it is necessary to apply Appendix 6 to these limit states; the Commentary to Specification Appendix 6, Section 6.1, Examples of such bracing types are shown in Figures 1-5, 6-1 of *Manual*.

# 6.2 COLUMN BRACING

The requirements in this section apply to bracing associated with the limit state of flexural buckling. For columns that are subject to torsional buckling (Appendix F, Section F3.3), or lateral-torsional buckling (*Spec.* Section E3), the designer must satisfy the requirements of the applicable sections in AISC *Specification* Chapters E and F. For bracing requirements to prevent such column buckling behavior in columns subject to torsional-flexural buckling, reference must be made to the commentary in *Manual*, Section G1 to Chapters 3 (*Yura*, 1999).

Column braces may be panel or point. The type of bracing must be determined before the requirements for strength and stiffness are computed. The relative bracing is recommended by the AISC *Specification* Appendix 6, Section 6.2.2 to be two times the equations for brace stiffness to provide sufficient strength to resist bending stresses occurring along braced points. For point bracing where a single interior point where the bracing is provided, the requirements for strength and bracing stiffness to provide sufficient strength and bracing of the provided.

# 6.3 BEAM BRACING

The requirements in this section apply to bracing of doubly and singly symmetric I-shaped members in flexure within a plane of symmetry and rules that need lateral force. Bracing in build lateral-torsional buckling may be accomplished

---

# A6-2

by a lateral brace, a torsional brace, or a combination of the two to prevent twist of the section. Lateral bracing should normally be connected near the compression flange. For the free ends of cantilevers and near inflection points of braced beams subject to double curvature bending. Torsional bracing may be connected anywhere on the cross section in a manner to prevent twist of the section.

According to AISC *Specification* Section F1(b), the design of members for flexure is based on the assumption that points of support are restrained against rotation about their longitudinal axis. The bracing requirements in Appendix 6 are for intermediate braces in addition to those at the support.

In members subject to double curvature, inflection points are not to be considered as braced points unless bracing is provided at that location. In addition, the bracing nearest the inflection point must be attached to prevent twist, either as a torsional brace or as lateral braces attached to both flanges as described in AISC *Specification* Appendix 6, Section 6.3.1(b).

## 6.3.1 Lateral Bracing

As with column bracing, beam bracing may be panel or point. In addition, it is permissible to provide torsional bracing. This section provides requirements for determining the required lateral brace strength and stiffness for panel and point braces.

For point braces, provision is made in this section to reduce the required brace stiffness when the actual unbraced length is less than the maximum unbraced length for the required flexural strength.

## 6.3.2 Torsional Bracing

This section provides requirements for determining the required bracing flexural strength and stiffness for point and continuous torsional bracing. Torsional bracing can be connected at any cross-section location. However, if the beam has inadequate distortional (out-of-plane) bending stiffness, torsional bracing will be ineffective. Web stiffeners can be provided when necessary to increase the web distortional stiffness for point torsional braces.

As is the case for columns and for lateral beam point braces, it is possible to reduce the required brace stiffness when the required strength of the member is less than the available strength at the provided location of bracing.

Provisions for continuous torsional bracing are also provided. A slab connected to the top flange of a beam in double curvature may provide sufficient continuous torsional bracing as discussed in the Commentary. For this condition there is no unbraced length between braces, so the unbraced length used in the strength and stiffness equations is the maximum unbraced length permitted to provide the required strength in the beam. In addition, for continuous torsional bracing, stiffeners are not permitted to be used to increase web distortional stiffness.

## 6.4 BEAM-COLUMN BRACING

For bracing of beam-columns, the required strength and stiffness are to be determined for the column and beam independently, as specified in AISC *Specification* Appendix 6, Sections 6.2 and 6.3. These values are then to be combined, depending on the type of bracing provided.

---

# A6-3

# EXAMPLE A-6.1 POINT STABILITY BRACING OF A W-SHAPE COLUMN

## Given:

Determine the required strength and the stiffness for intermediate point braces, such that the unbraced length for the column buckling is 12 ft. The column is an ASTM A992/A992M W12×72 with loading and geometry as shown in Figure A-6.1-1. The column is braced laterally and torsionally at its ends with intermediate lateral braces for the *x*- and *y*-axis provided at the one-third points as shown. Thus, the unbraced length for the limit state of flexural-torsional buckling is 36 ft, and the unbraced length for flexural buckling is 12 ft. The column has sufficient strength to support the applied loads with this bracing.

<div style="text-align: center;">
<img src="column_diagram" alt="Column bracing diagram showing:
- Total height: 36'-0"
- Three equal segments of 12'-0" each
- Point loads at top: P_D = 105 kips, P_L = 315 kips
- Lateral braces at 1/3 points (marked with X symbols)
- Fixed base support at bottom">
</div>

*Fig. A-6.1-1. Column bracing geometry for Example A-6.1.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

Column
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

*Required Compressive Strength of Column*

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(105 \text{ kips}) + 1.6(315 \text{ kips})$ | $P_a = 105 \text{ kips} + 315 \text{ kips}$ |
| $= 630$ kips | $= 420$ kips |

*Available Compressive Strength of Column*

From AISC *Manual* Table 4-1a at $L_{cy} = 12$ ft, the available compressive strength of the W12×72 is:

---

# A6-4

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 806 \text{ kips} > 630 \text{ kips}$ **o.k.** | $\frac{P_n}{\Omega_c} = 536 \text{ kips} > 420 \text{ kips}$ **o.k.** |

*Required Point Brace Strength*

From AISC *Specification* Appendix 6, Section 6.2.2, the required point brace strength is:

| LRFD | ASD |
|------|-----|
| $P_r = P_u$ | $P_r = P_a$ |
| $= 630$ kips | $= 420$ kips |
| $P_{br} = 0.01P_r$ (*Spec.* Eq. A-6-3) | $P_{br} = 0.01P_r$ (*Spec.* Eq. A-6-3) |
| $= 0.01(630 \text{ kips})$ | $= 0.01(420 \text{ kips})$ |
| $= 6.30$ kips | $= 4.20$ kips |

*Required Point Brace Stiffness*

From AISC *Specification* Appendix 6, Section 6.2.2, the required point brace stiffness, with an unbraced length adjacent to the point brace $L_{br} = 12$ ft, is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $P_r = P_u$ | $P_r = P_a$ |
| $= 630$ kips | $= 420$ kips |
| $\beta_{br} = \frac{1}{\phi}\left(\frac{8P_r}{L_{br}}\right)$ (*Spec.* Eq. A-6-4a) | $\beta_{br} = \Omega\left(\frac{8P_r}{L_{br}}\right)$ (*Spec.* Eq. A-6-4b) |
| $= \frac{1}{0.75}\left[\frac{8(630 \text{ kips})}{(12 \text{ ft})(12 \text{ in./ft})}\right]$ | $= 2.00\left[\frac{8(420 \text{ kips})}{(12 \text{ ft})(12 \text{ in./ft})}\right]$ |
| $= 46.7$ kip/in. | $= 46.7$ kip/in. |

Determine the maximum permitted unbraced length for the required strength.

Interpolating between values from AISC *Manual* Table 4-1a:

| LRFD | ASD |
|------|-----|
| $L_{cy} = 19.0$ ft for $P_u = 630$ kips | $L_{cy} = 18.9$ ft for $P_a = 420$ kips |

*Calculate the required point brace stiffness for this increased unbraced length*

It is permissible to design the braces to provide the lower stiffness determined using the maximum unbraced length permitted to carry the required strength according to AISC *Specification* Appendix 6, Section 6.2.2.

---

# A6-5

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $P_r = P_u$ | $P_r = P_a$ |
| $= 630$ kips | $= 420$ kips |
| $\beta_{br} = \frac{1}{\phi}\left(\frac{8P_r}{L_{br}}\right)$ (*Spec.* Eq. A-6-4a) | $\beta_{br} = \Omega\left(\frac{8P_r}{L_{br}}\right)$ (*Spec.* Eq. A-6-4b) |
| $= \frac{1}{0.75}\left[\frac{8(630 \text{ kips})}{(19.0 \text{ ft})(12 \text{ in./ft})}\right]$ | $= 2.00\left[\frac{8(420 \text{ kips})}{(18.9 \text{ ft})(12 \text{ in./ft})}\right]$ |
| $= 29.5$ kip/in. | $= 29.6$ kip/in. |

---

# A6-6

# EXAMPLE A-6.2 POINT STABILITY BRACING OF A WT-SHAPE COLUMN

## Given:

Determine the strength and stiffness requirements for the point braces and select a W-shape brace based on *x*-axis flexural buckling for an ASTM A992/A992M WT7×34 column with loading and geometry as shown in Figure A-6.2-1. The unbraced length for this column is 7.5 ft. Bracing about the *y*-axis is provided by the axial resistance of a W-shape connected to the flange of the WT, while bracing about the *x*-axis is provided by the flexural resistance of the same W-shape loaded at the midpoint of a 12-ft-long simple span beam. Assume that the axial strength and stiffness of the W-shape are adequate to brace the *y*-axis of the WT. Also, assume the column is braced laterally and torsionally at its ends and is torsionally braced at one-quarter points by the W-shape braces.

<div style="text-align: center;">
<img src="column_bracing_plan_elevation" alt="Column bracing diagrams showing:
(a) Plan view:
- 6'-0" spacing on each side of W-shape brace
- WT7×34 column cross-section
- W-shape brace

(b) Elevation view:
- Total height: 30'-0"
- Four equal segments of 7'-6" each
- Point loads at top: P_D = 25 kips, P_L = 75 kips
- Lateral braces at quarter points (marked with X symbols)
- Fixed base support at bottom">
</div>

*(a) Plan                    (b) Elevation*

*Fig. A-6.2-1. Column bracing geometry for Example A-6.2.*

## Solution:

From AISC *Manual* Table 2-4, the material properties of the column and brace are as follows:

ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

*Required Compressive Strength of Column*

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(25 \text{ kips}) + 1.6(75 \text{ kips})$ | $P_a = 25 \text{ kips} + 75 \text{ kips}$ |
| $= 150$ kips | $= 100$ kips |

*Available Compressive Strength of Column*

Interpolating between values from AISC *Manual* Table 4-7, the available axial compressive strength of the WT7×34 with $L_{cx} = 7.5$ ft is:

---

# A6-7

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 357 \text{ kips} > 150 \text{ kips}$ **o.k.** | $\frac{P_n}{\Omega_c} = 238 \text{ kips} > 100 \text{ kips}$ **o.k.** |

*Required Point Brace Size*

From AISC *Specification* Appendix 6, Section 6.2.2, the required point brace strength is:

| LRFD | ASD |
|------|-----|
| $P_r = P_u$ | $P_r = P_a$ |
| $= 150$ kips | $= 100$ kips |
| $P_{br} = 0.01P_r$ (*Spec.* Eq. A-6-3) | $P_{br} = 0.01P_r$ (*Spec.* Eq. A-6-3) |
| $= 0.01(150 \text{ kips})$ | $= 0.01(100 \text{ kips})$ |
| $= 1.50$ kips | $= 1.00$ kips |

From AISC *Specification* Appendix 6, Section 6.2.2, the required point brace stiffness is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $P_r = P_u$ | $P_r = P_a$ |
| $= 150$ kips | $= 100$ kips |
| $\beta_{br} = \frac{1}{\phi}\left(\frac{8P_r}{L_{br}}\right)$ (*Spec.* Eq. A-6-4a) | $\beta_{br} = \Omega\left(\frac{8P_r}{L_{br}}\right)$ (*Spec.* Eq. A-6-4b) |
| $= \frac{1}{0.75}\left[\frac{8(150 \text{ kips})}{(7.50 \text{ ft})(12 \text{ in./ft})}\right]$ | $= 2.00\left[\frac{8(100 \text{ kips})}{(7.50 \text{ ft})(12 \text{ in./ft})}\right]$ |
| $= 17.8$ kip/in. | $= 17.8$ kip/in. |

The brace is a simple-span beam loaded at its midspan. Thus, its flexural stiffness can be derived from Case 7 of AISC *Manual* Table 3-22 to be $48EI/L^3$, which must be greater than the required point brace stiffness, β$_{br}$. Also, the flexural strength of the beam, $\phi M_n$ for a compact laterally supported beam, must be greater than the moment resulting from the required brace strength over the beam's simple span, $M_{br} = P_{br}L/4$.

Based on brace stiffness, the minimum required moment of inertia of the beam is:

$$I_{br} = \frac{\beta_{br} L^3}{48E}$$

$$= \frac{(17.8 \text{ kip/in.})(12.0 \text{ ft})^3 (12 \text{ in./ft})^3}{48(29{,}000 \text{ ksi})}$$

$$= 38.2 \text{ in.}^4$$

Based on moment strength for a compact laterally supported beam, the minimum required plastic section modulus is:

---

# A6-8

| LRFD | ASD |
|------|-----|
| $Z_{req} = \frac{M_{br}}{\phi F_y}$ | $Z_{req} = \frac{\Omega M_{br}}{F_y}$ |
| $= \frac{(1.50 \text{ kips})(12.0 \text{ ft})(12 \text{ in./ft})}{0.90(50 \text{ ksi})(4)}$ | $= \frac{1.67(1.00 \text{ kip})(12.0 \text{ ft})(12 \text{ in./ft})}{(50 \text{ ksi})(4)}$ |
| $= 1.20 \text{ in.}^3$ | $= 1.20 \text{ in.}^3$ |

From AISC *Manual* Table 3-2, select a W8×13 member with $Z_x = 11.4 \text{ in.}^3$ and $I_x = 39.6 \text{ in.}^4$

Note that because the live-to-dead load ratio is 3, the LRFD and ASD results are identical.

The required stiffness can be reduced if the maximum permitted unbraced length is used as described in AISC *Specification* Appendix 6, Section 6.2, and also if the actual number of braces are considered, as discussed in the Commentary. The following demonstrates how this affects the design.

Interpolating between values in AISC *Manual* Table 4-7, the maximum permitted unbraced length of the WT7×34 for the required strength is as follows:

| LRFD | ASD |
|------|-----|
| $L_{cx} = 18.6$ ft for $P_u = 150$ kips | $L_{cx} = 18.6$ ft for $P_a = 100$ kips |

From AISC *Specification* Commentary Appendix 6, Section 6.2, determine the reduction factor for three intermediate braces:

$$\frac{2n-1}{2n} = \frac{2(3)-1}{2(3)}$$
(*Spec.* Eq. C-A-6-6)

$$= 0.833$$

Determine the required point brace stiffness for the increased unbraced length and number of braces:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $P_r = P_u$ | $P_r = P_a$ |
| $= 150$ kips | $= 100$ kips |
| $\beta_{br} = 0.833\left[\frac{1}{\phi}\left(\frac{8P_r}{L_{br}}\right)\right]$ (from *Spec.* Eq. A-6-4a) | $\beta_{br} = 0.833\left[\Omega\left(\frac{8P_r}{L_{br}}\right)\right]$ (from *Spec.* Eq. A-6-4b) |
| $= 0.833\left[\frac{1}{0.75}\left[\frac{8(150 \text{ kips})}{(18.6 \text{ ft})(12 \text{ in./ft})}\right]\right]$ | $= 0.833\left[2.00\left[\frac{8(100 \text{ kips})}{(18.6 \text{ ft})(12 \text{ in./ft})}\right]\right]$ |
| $= 5.97$ kip/in. | $= 5.97$ kip/in. |

Determine the required brace size based on this new stiffness requirement.

Based on brace stiffness, the minimum required moment of inertia of the beam is:

---

# A6-9

$$I_{br} = \frac{\beta_{br} L^3}{48E}$$

$$= \frac{(5.97 \text{ kip/in.})(12.0 \text{ ft})^3 (12 \text{ in./ft})^3}{48(29{,}000 \text{ ksi})}$$

$$= 12.8 \text{ in.}^4$$

Based on the unchanged flexural strength for a compact laterally supported beam, the minimum required plastic section modulus, $Z_x$, was determined previously to be 1.20 in.$^3$ From AISC *Manual* Table 1-1, select a W6×12 noncompact member with $Z_x = 8.30 \text{ in.}^3$ and $I_x = 22.1 \text{ in.}^4$

---

# A6-10

# EXAMPLE A-6.3 POINT STABILITY BRACING OF A BEAM—CASE I

## Given:

A walkway in an industrial facility has a span of 28 ft as shown in Figure A-6.3-1. The walkway has a deck of grating which is not sufficient to brace the beams. At midspan, the beams are ASTM A992/A992M W12×22 beams along the walkway edges are braced against twist at the ends as required by AISC *Specification* Section F1(b) and are connected by an L3×3×¼ strut at midspan. The two diagonal ASTM A572/A572M Grade 50 L5×5×⅝ braces are connected to the top flange of the beams at the supports and at the strut at the middle. The strut and brace connections are welded; therefore, bolt slippage does not need to be accounted for in the stiffness calculation. The dead load on each beam is 0.05 kip/ft and the live load is 0.125 kip/ft. Determine if the diagonal braces are strong enough and stiff enough to brace this walkway.

<div style="text-align: center;">
<img src="beam_bracing_plan" alt="Plan view showing:
- Total span: 28'-0"
- Two segments of 14'-0" each
- W12×22 beams at edges
- L5×5×⅝ diagonal braces from support to center strut
- Center strut (L3×3×¼)
- Deck height: 5'-0"">
</div>

*Fig. A-6.3-1. Plan view for Example A-6.3.*

## Solution:

Because the diagonal braces are connected directly to an unyielding support that is independent of the midspan brace point, they are designed as point braces. The strut will be assumed to be sufficiently strong and stiff to force the two beams to buckle together.

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Diagonal braces
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Tables 1-1 and 1-7, the geometric properties are as follows:

Beam
W12×22
$h_o = 11.9$ in.

Diagonal braces
L5×5×⅝
$A = 3.07 \text{ in.}^2$

---

# A6-11

*Required Flexure Strength of Beam*

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.05 \text{ kip/ft}) + 1.6(0.125 \text{ kip/ft})$ | $w_a = 0.05 \text{ kip/ft} + 0.125 \text{ kip/ft}$ |
| $= 0.260$ kip/ft | $= 0.175$ kip/ft |

Determine the required flexural strength for a uniformly loaded simply supported beam using AISC *Manual* Table 3-22, Case 1.

| LRFD | ASD |
|------|-----|
| $M_u = \frac{w_u L^2}{8}$ | $M_a = \frac{w_a L^2}{8}$ |
| $= \frac{(0.260 \text{ kip/ft})(28 \text{ ft})^2}{8}$ | $= \frac{(0.175 \text{ kip/ft})(28 \text{ ft})^2}{8}$ |
| $= 25.5$ kip-ft | $= 17.2$ kip-ft |

It can be shown that the W12×22 beams are adequate with the unbraced length of 14 ft. Both beams need bracing in the same direction simultaneously.

*Required Brace Strength and Stiffness*

From AISC *Specification* Appendix 6, Section 6.3, determine the required point brace strength for each beam as follows, with $C_d = 1.0$ for bending in single curvature.

| LRFD | ASD |
|------|-----|
| $M_r = M_u$ | $M_r = M_a$ |
| $= 25.5$ kip-ft | $= 17.2$ kip-ft |
| $P_{br} = 0.02\left(\frac{M_r C_d}{h_o}\right)$ (*Spec.* Eq. A-6-7) | $P_{br} = 0.02\left(\frac{M_r C_d}{h_o}\right)$ (*Spec.* Eq. A-6-7) |
| $= 0.02\left[\frac{(25.5 \text{ kip-ft})(12 \text{ in./ft})(1.0)}{11.9 \text{ in.}}\right]$ | $= 0.02\left[\frac{(17.2 \text{ kip-ft})(12 \text{ in./ft})(1.0)}{11.9 \text{ in.}}\right]$ |
| $= 0.514$ kip | $= 0.347$ kip |

Because there are two beams to be braced, the total required brace strength is:

| LRFD | ASD |
|------|-----|
| $P_{br} = 2(0.514 \text{ kip})$ | $P_{br} = 2(0.347 \text{ kip})$ |
| $= 1.03$ kips | $= 0.694$ kip |

There are two beams to brace and two braces to share the load. The worst case for design of the braces will be when they are in compression.

By geometry, the diagonal bracing length is

$$L = \sqrt{(14 \text{ ft})^2 + (5 \text{ ft})^2}$$
$$= 14.9 \text{ ft}$$

---

# A6-12

The required brace strength is:

| LRFD | ASD |
|------|-----|
| $P_{br} \cos\theta = P_{br}\left(\frac{5 \text{ ft}}{14.9 \text{ ft}}\right)$ | $P_{br} \cos\theta = P_{br}\left(\frac{5 \text{ ft}}{14.9 \text{ ft}}\right)$ |
| $= 1.03$ kips | $= 0.694$ kip |
| Because there are two braces, the required brace strength is: | Because there are two braces, the required brace strength is: |
| $P_{br} = \frac{1.03 \text{ kips}}{2(5 \text{ ft}/14.9 \text{ ft})}$ | $P_{br} = \frac{0.694 \text{ kip}}{2(5 \text{ ft}/14.9 \text{ ft})}$ |
| $= 1.53$ kips | $= 1.03$ kips |

The required point brace stiffness, with $C_d = 1.0$ for bending in single curvature, is determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $M_r = M_u$ | $M_r = M_a$ |
| $= 25.5$ kip-ft | $= 17.2$ kip-ft |
| $\beta_{br} = \frac{1}{\phi}\left(\frac{10M_r C_d}{L_{br}h_o}\right)$ (*Spec.* Eq. A-6-8a) | $\beta_{br} = \Omega\left(\frac{10M_r C_d}{L_{br}h_o}\right)$ (*Spec.* Eq. A-6-8b) |
| $= \frac{1}{0.75}\left[\frac{10(25.5 \text{ kip-ft})(12 \text{ in./ft})(1.0)}{(14 \text{ ft})(12 \text{ in./ft})(11.9 \text{ in.})}\right]$ | $= 2.00\left[\frac{10(17.2 \text{ kip-ft})(12 \text{ in./ft})(1.0)}{(14 \text{ ft})(12 \text{ in./ft})(11.9 \text{ in.})}\right]$ |
| $= 2.04$ kip/in. | $= 2.06$ kip/in. |

Because there are two beams to be braced, the total required point brace stiffness is:

| LRFD | ASD |
|------|-----|
| $\beta_{br} = 2(2.04 \text{ kip/in.})$ | $\beta_{br} = 2(2.06 \text{ kip/in.})$ |
| $= 4.08$ kip/in. | $= 4.12$ kip/in. |

The beams require bracing in order to have sufficient strength to carry the given load. However, locating that brace at the midspan provides flexural strength greater than the required strength. The maximum unbraced length permitted for the required flexural strength is $L_b = 18.2$ ft from AISC *Manual* Table 6-1, with $C_b = 1.0$. Thus, according to AISC *Specification* Appendix 6, Section 6.3.1b, this length could be used in place of 14 ft to determine the required stiffness. However, because the required stiffness is so small, the 14 ft length will be used here.

For a single brace, the stiffness is:

$$\beta = \frac{AE\cos^2\theta}{L}$$

$$= \frac{(3.07 \text{ in.}^2)(29{,}000 \text{ ksi})(5 \text{ ft}/14.9 \text{ ft})^2}{(14.9 \text{ ft})(12 \text{ in./ft})}$$

$$= 56.1 \text{ kip/in.}$$

---

# A6-13

Because there are two braces, the system stiffness is twice this. Thus,

$$\beta = 2(56.1 \text{ kip/in.})$$
$$= 112 \text{ kip/in.}$$

| LRFD | ASD |
|------|-----|
| $\beta = 112 \text{ kip/in.} > 4.08 \text{ kip/in.}$ **o.k.** | $\beta = 112 \text{ kip/in.} > 4.12 \text{ kip/in.}$ **o.k.** |

*Available Strength of Braces*

The braces may be called upon to act in either tension or compression, depending on which transverse direction the system tries to buckle. Brace compression buckling will control over tension yielding. Therefore, determine the compressive strength of the braces assuming they are eccentrically loaded using AISC *Manual* Table 4-12.

| LRFD | ASD |
|------|-----|
| Interpolating for $L_c = 14.9$ ft: | Interpolating for $L_c = 14.9$ ft: |
| $\phi_c P_n = 17.1 \text{ kips} > 1.53 \text{ kips}$ **o.k.** | $\frac{P_n}{\Omega_c} = 11.6 \text{ kips} > 1.03 \text{ kips}$ **o.k.** |

The L5×5×⅝ braces have sufficient strength and stiffness to act as the point braces for this system.

---

# A6-14

# EXAMPLE A-6.4 POINT STABILITY BRACING OF A BEAM—CASE II

## Given:

A walkway in an industrial facility has a span of 28 ft as shown in Figure A-6.4-1. The walkway has a deck of grating which is not sufficient to brace the beams. The ASTM A992/A992M W12×22 beams are braced against twist at the ends, and they are connected by a strut connected at midspan. At that same point they are braced to an adjacent ASTM A500/A500M Grade C HSS8×8×¼ column by the attachment of a 5 ft long ASTM A572/A572M Grade 50 2L3×3×¼. The brace connections are all welded; therefore, bolt slippage does not need to be accounted for in the stiffness calculation. The adjacent column is not braced at the walkway level but is adequately braced 12 ft below and 12 ft above the walkway level. The dead load on each beam is 0.05 kip/ft and the live load is 0.125 kip/ft. Determine if the bracing system has adequate strength and stiffness to brace this walkway.

<div style="text-align: center;">
<img src="walkway_plan_elevation" alt="Plan view showing:
- Total span: 28'-0"
- Two segments of 14'-0" each
- W12×22 beams
- Center strut with 2L3×3×¼ at top chord
- HSS8×8×¼ column (24'-0" tall) positioned 5'-0" from centerline
- Deck height shown as 5'-0"">
</div>

*Fig. A-6.4-1. Plan view for Example A-6.4.*

## Solution:

Because the bracing system does not interact directly with any other braced point on the beam, the double angle and column constitute a point brace system. The strut will be assumed to be sufficiently strong and stiff to force the two beams to buckle together.

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

HSS column
ASTM A500/A500M Grade C
$F_y = 50$ ksi
$F_u = 62$ ksi

Double-angle brace
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

---

# A6-15

From AISC *Manual* Tables 1-1, 1-12, and 1-15, the geometric properties are as follows:

Beam
W12×22
$h_o = 11.9$ in.

HSS column
HSS8×8×¼
$I = 70.7 \text{ in.}^4$

Double-angle brace
2L3×3×¼
$A = 2.88 \text{ in.}^2$

*Required Flexural Strength of Beam*

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.05 \text{ kip/ft}) + 1.6(0.125 \text{ kip/ft})$ | $w_a = 0.05 \text{ kip/ft} + 0.125 \text{ kip/ft}$ |
| $= 0.260$ kip/ft | $= 0.175$ kip/ft |

Determine the required flexural strength for a uniformly distributed load on the simply supported beam using AISC *Manual* Table 3-22, Case 1, as follows:

| LRFD | ASD |
|------|-----|
| $M_u = \frac{w_u L^2}{8}$ | $M_a = \frac{w_a L^2}{8}$ |
| $= \frac{(0.260 \text{ kip/ft})(28 \text{ ft})^2}{8}$ | $= \frac{(0.175 \text{ kip/ft})(28 \text{ ft})^2}{8}$ |
| $= 25.5$ kip-ft | $= 17.2$ kip-ft |

It can be shown that the W12×22 beams are adequate with the unbraced length of 14 ft. Both beams need bracing in the same direction simultaneously.

*Required Brace Strength and Stiffness*

From AISC *Specification* Appendix 6, Section 6.3.1b, the required brace force for each beam, with $C_d = 1.0$ for bending in single curvature, is determined as follows:

| LRFD | ASD |
|------|-----|
| $M_r = M_u$ | $M_r = M_a$ |
| $= 25.5$ kip-ft | $= 17.2$ kip-ft |
| $P_{br} = 0.02\left(\frac{M_r C_d}{h_o}\right)$ (*Spec.* Eq. A-6-7) | $P_{br} = 0.02\left(\frac{M_r C_d}{h_o}\right)$ (*Spec.* Eq. A-6-7) |
| $= 0.02\left[\frac{(25.5 \text{ kip-ft})(12 \text{ in./ft})(1.0)}{11.9 \text{ in.}}\right]$ | $= 0.02\left[\frac{(17.2 \text{ kip-ft})(12 \text{ in./ft})(1.0)}{11.9 \text{ in.}}\right]$ |
| $= 0.514$ kip | $= 0.347$ kip |

---

# A6-16

Because there are two beams, the total required brace force is:

| LRFD | ASD |
|------|-----|
| $P_{br} = 2(0.514 \text{ kip})$ | $P_{br} = 2(0.347 \text{ kip})$ |
| $= 1.03$ kips | $= 0.694$ kip |

By inspection, the 2L3×3×¼ can carry the required bracing force. The HSS column can also carry the bracing force through bending on a 24 ft long span. It will be shown that the change in length of the 2L3×3×¼ is negligible, and the available brace stiffness will come from the flexural stiffness of the column only.

From AISC *Specification* Appendix 6, Section 6.3.1b, with $C_d = 1.0$ for bending in single curvature, the required brace stiffness is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $M_r = M_u$ | $M_r = M_a$ |
| $= 25.5$ kip-ft | $= 17.2$ kip-ft |
| $\beta_{br} = \frac{1}{\phi}\left(\frac{10M_r C_d}{L_{br}h_o}\right)$ (*Spec.* Eq. A-6-8a) | $\beta_{br} = \Omega\left(\frac{10M_r C_d}{L_{br}h_o}\right)$ (*Spec.* Eq. A-6-8b) |
| $= \frac{1}{0.75}\left[\frac{10(25.5 \text{ kip-ft})(12 \text{ in./ft})(1.0)}{(14 \text{ ft})(12 \text{ in./ft})(11.9 \text{ in.})}\right]$ | $= 2.00\left[\frac{10(17.2 \text{ kip-ft})(12 \text{ in./ft})(1.0)}{(14 \text{ ft})(12 \text{ in./ft})(11.9 \text{ in.})}\right]$ |
| $= 2.04$ kip/in. | $= 2.06$ kip/in. |

The beams require one brace in order to have sufficient strength to carry the given load. However, locating that brace at midspan provides flexural strength greater than the required strength. The maximum unbraced length permitted for the required flexural strength is $L_b = 18.2$ ft from AISC *Manual* Table 6-1, with $C_b = 1.0$. Thus, according to AISC *Specification* Appendix 6, Section 6.3.1b, this length could be used in place of 14 ft to determine the required stiffness.

*Available Stiffness of Brace*

Because the brace stiffness comes from the combination of the axial stiffness of the double-angle member and the flexural stiffness of the column loaded at its midheight, the individual element stiffness will be determined and then combined.

The axial stiffness of the double angle is:

$$\beta = \frac{AE}{L}$$

$$= \frac{(2.88 \text{ in.}^2)(29{,}000 \text{ ksi})}{(5 \text{ ft})(12 \text{ in./ft})}$$

$$= 1{,}390 \text{ kip/in.}$$

The available flexural stiffness of the HSS column with a point load at midspan using AISC *Manual* Table 3-22, Case 7, is:

---

# A6-17

$$\beta = \frac{48EI}{L^3}$$

$$= \frac{48(29{,}000 \text{ ksi})(70.7 \text{ in.}^4)}{(24.0 \text{ ft})^3 (12 \text{ in./ft})^3}$$

$$= 4.12 \text{ kip/in.}$$

The combined stiffness is:

$$\frac{1}{\beta} = \frac{1}{\beta_{angles}} + \frac{1}{\beta_{column}}$$

$$= \frac{1}{1{,}390 \text{ kip/in.}} + \frac{1}{4.12 \text{ kip/in.}}$$

$$= 0.243 \text{ in./kip}$$

Thus, the system stiffness is:

$$\beta = 4.12 \text{ kip/in.}$$

The stiffness of the double-angle member could have reasonably been ignored.

Because the double-angle brace is ultimately bracing two beams, the required stiffness is multiplied by 2:

| LRFD | ASD |
|------|-----|
| $4.12 \text{ kip/in.} \geq 2(2.04 \text{ kip/in.})$ | $4.12 \text{ kip/in.} \geq 2(2.06 \text{ kip/in.})$ |
| $4.12 \text{ kip/in.} > 4.08 \text{ kip/in.}$ **o.k.** | $4.12 \text{ kip/in.} = 4.12 \text{ kip/in.}$ **o.k.** |

The HSS8×8×¼ column is an adequate brace for the beams. However, if the column also carries an axial force, it must be checked for combined forces.

---

# A6-18

# EXAMPLE A-6.5 POINT STABILITY BRACING OF A BEAM WITH REVERSE CURVATURE BENDING

## Given:

A roof system is composed of 26K8 steel joists spaced at 5 ft intervals and supported on ASTM A992/A992M W21×50 girders as shown in Figure A-6.5-1(a). The roof dead load is 33 psf, and the roof live load is 25 psf. Determine the required strength and stiffness of the braces needed to brace the girder at the support and near the inflection point. Bracing for the beam is shown in Figure A-6.5-1(b). Moment diagrams for the beam are shown in Figures A-6.5-1(c) and A-6.5-1(d). Determine the size of single-angle kickers connected to the bottom flange of the girder and the top chord of the joist, as shown in Figure A-6.5-1(e), where the brace force will be taken by a connected rigid diaphragm.

<div style="text-align: center;">
<img src="roof_system_plan" alt="Plan view showing:
- Grid pattern with dimensions 40'-0" typical horizontal spacing
- Various vertical dimensions: 26'-6", 10'-0", 26'-8"(28.8), 26'-6" on left side
- Dimensions 5'-6" marked at corners
- W21×50 girders spanning horizontally
- Support points marked with solid circles
- Hinge points marked with open circles
- Shear splice typical locations
- B sections marked">

*(a) Plan*
</div>

<div style="text-align: center;">
<img src="beam_bracing_section" alt="Section B-B showing:
- Top flange braced at 5'-0" on center
- Bottom flange braced at supports and 10'-0" from supports
- Total span showing: 5'-6" | 10'-0" | 40'-0" | 10'-0" | 5'-6"
- Points A, B, C marked along beam
- Bracing locations marked with X symbols">

*(b) Section B-B: Beam with bracing at top flanges by the steel joists
and at the bottom flanges by the single-angle kickers*
</div>

*Fig. A-6.5-1. Example A-6.5 configuration.*

---

# A6-19

<div style="text-align: center;">
<img src="moment_diagram_full_beam" alt="Moment diagram showing:
- 10'-0" dimension marked on left
- Points A, B, C marked
- Peak moment M = 111w at center
- Inflection point between B and C
- 5.1' distances on each side
- Total span 51'-0"
- End moments M = 88.7w at each support">

*(c) Moment diagram of beam*
</div>

<div style="text-align: center;">
<img src="moment_diagram_detail_BC" alt="Detailed moment diagram between points B and C showing:
- Point B with M = -88.7w
- Varying moments: M = -41.8w, M = -1.20w
- Point C with moments M = 33.2w and M = 61.3w
- Four segments of 2'-6" each (total span detail)
- Hatched shading showing moment variation">

*(d) Moment diagram between points B and C*
</div>

<div style="text-align: center;">
<img src="bracing_configuration" alt="Bracing detail showing:
- 48" width
- 20" height
- W21×50 beam section
- Single-angle kicker
- Steel joist members
- Connection detail with θ angle marked">

*(e) Bracing configuration*
</div>

*Fig. A-6.5-1 (continued). Example A-6.5 configuration.*

## Solution:

Because the braces will transfer their force to a rigid roof diaphragm, they will be treated as point braces.

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

---

# A6-20

Single-angle brace
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From the Steel Joist Institute:

Joist
K-Series
$F_y = 50$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W21×50
$h_o = 20.3$ in.

*Required Flexural Strength of Beam*

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(33 \text{ psf}) + 1.6(25 \text{ psf})$ | $w_a = 33 \text{ psf} + 25 \text{ psf}$ |
| $= 79.6$ psf | $= 58.0$ psf |
| $w_u = \frac{(79.6 \text{ psf})(40 \text{ ft})}{1{,}000 \text{ lb/kip}}$ | $w_a = \frac{(58.0 \text{ psf})(40 \text{ ft})}{1{,}000 \text{ lb/kip}}$ |
| $= 3.18$ kip/ft | $= 2.32$ kip/ft |
| From Figure A-6.5-1(d): | From Figure A-6.5-1(d): |
| $M_{uB} = 88.7(3.18 \text{ kip/ft})$ | $M_{aB} = 88.7(2.32 \text{ kip/ft})$ |
| $= 282$ kip-ft | $= 206$ kip-ft |

*Required Brace Strength and Stiffness*

Determine the required force to brace the bottom flange of the girder with a point brace. The braces at points B and C will be determined based on the moment at B. However, because the brace at C is the closest to the inflection point, its strength and stiffness requirements are greater because they are influenced by the variable $C_d$, which will be equal to 2.0.

From AISC *Specification* Appendix 6, Section 6.3.1b, the required brace force is determined as follows:

| LRFD | ASD |
|------|-----|
| $M_r = M_{uB}$ | $M_r = M_{aB}$ |
| $= 282$ kip-ft | $= 206$ kip-ft |

---

# A6-21

| LRFD | ASD |
|------|-----|
| $P_{br} = 0.02\left(\frac{M_r C_d}{h_o}\right)$ (*Spec.* Eq. A-6-7) | $P_{br} = 0.02\left(\frac{M_r C_d}{h_o}\right)$ (*Spec.* Eq. A-6-7) |
| $= 0.02\left[\frac{(282 \text{ kip-ft})(12 \text{ in./ft})(2.0)}{20.3 \text{ in.}}\right]$ | $= 0.02\left[\frac{(206 \text{ kip-ft})(12 \text{ in./ft})(2.0)}{20.3 \text{ in.}}\right]$ |
| $= 6.67$ kips | $= 4.87$ kips |

Determine the required stiffness of the point brace at point C. The required brace stiffness is a function of the unbraced length. It is permitted to use the maximum unbraced length permitted for the beam based upon the required flexural strength. Thus, determine the maximum unbraced length permitted.

Based on AISC *Specification* Section F1 and the moment diagram shown in Figure A-6.5-1(d), for the beam between points B and C, the lateral-torsional buckling modification factor, $C_b$, is:

$$C_b = \frac{12.5M_{max}}{2.5M_{max} + 3M_A + 4M_B + 3M_C}$$
(*Spec.* Eq. F1-1)

$$= \frac{12.5(-88.7w)}{2.5(-88.7w) + 3(-41.8w) + 4(-1.20w) + 3(33.2w)}$$

$$= 2.46$$

The maximum unbraced length for the required flexural strength can be determined by setting the available flexural strength based on AISC *Specification* Equation F2-3 (lateral-torsional buckling) equal to the required strength and solving for $L_b$ (this is assuming that $L_b > L_r$).

| LRFD | ASD |
|------|-----|
| For a required flexural strength, $M_u = 282$ kip-ft, with $C_b = 2.46$, the unbraced length may be taken as: | For a required flexural strength, $M_a = 206$ kip-ft, with $C_b = 2.46$, the unbraced length may be taken as: |
| $L_b = 22.2$ ft | $L_b = 20.8$ ft |

From AISC *Specification* Appendix 6, Section 6.3.1b, the required brace stiffness is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $M_r = M_{uB}$ | $M_r = M_{aB}$ |
| $= 282$ kip-ft | $= 206$ kip-ft |
| $\beta_{br} = \frac{1}{\phi}\left(\frac{10M_r C_d}{L_{br}h_o}\right)$ (*Spec.* Eq. A-6-8a) | $\beta_{br} = \Omega\left(\frac{10M_r C_d}{L_{br}h_o}\right)$ (*Spec.* Eq. A-6-8b) |
| $= \frac{1}{0.75}\left[\frac{10(282 \text{ kip-ft})(12 \text{ in./ft})(2.0)}{(22.2 \text{ ft})(12 \text{ in./ft})(20.3 \text{ in.})}\right]$ | $= 2.00\left[\frac{10(206 \text{ kip-ft})(12 \text{ in./ft})(2.0)}{(20.8 \text{ ft})(12 \text{ in./ft})(20.3 \text{ in.})}\right]$ |
| $= 16.7$ kip/in. | $= 19.5$ kip/in. |

Because no deformation will be considered in the connections, only the brace itself will be used to provide the required stiffness. The brace is oriented with the geometry as shown in Figure A-6.5-1(e). Thus, the force in the brace is $P_{br}$ /(cosθ) and the stiffness of the brace is $AE$(cos²θ)/$L$. There are two braces at each brace point. One would be in

---

# A6-22

tension and one in compression, depending on the direction that the girder attempts to buckle. For simplicity in design, a single brace will be selected that will be assumed to be in tension. Only the limit state of yielding will be considered. Select a single angle to meet the requirements of strength and stiffness, with a length of:

$$L = \sqrt{(48 \text{ in.})^2 + (20 \text{ in.})^2}$$
$$= 52.0 \text{ in.}$$

*Required Brace Force*

| LRFD | ASD |
|------|-----|
| $F_{br} = \frac{P_{br}}{\cos\theta}$ | $F_{br} = \frac{P_{br}}{\cos\theta}$ |
| $= \frac{6.67 \text{ kips}}{(48.0 \text{ in.}/52.0 \text{ in.})}$ | $= \frac{4.87 \text{ kips}}{(48.0 \text{ in.}/52.0 \text{ in.})}$ |
| $= 7.23$ kips | $= 5.28$ kips |

From AISC *Specification* Section D2(a), the required area based on available tensile strength is determined as follows:

| LRFD | ASD |
|------|-----|
| $A_g = \frac{F_{br}}{\phi F_y}$ (from *Spec.* Eq. D2-1) | $A_g = \frac{\Omega F_{br}}{F_y}$ (from *Spec.* Eq. D2-1) |
| $= \frac{7.23 \text{ kips}}{0.90(50 \text{ ksi})}$ | $= \frac{1.67(5.28 \text{ kips})}{50 \text{ ksi}}$ |
| $= 0.161 \text{ in.}^2$ | $= 0.176 \text{ in.}^2$ |

The required area based on stiffness is:

| LRFD | ASD |
|------|-----|
| $A_g = \frac{\beta_{br} L}{E\cos^2\theta}$ | $A_g = \frac{\beta_{br} L}{E\cos^2\theta}$ |
| $= \frac{(16.7 \text{ kip/in.})(52.0 \text{ in.})}{(29{,}000 \text{ ksi})(48.0 \text{ in.}/52.0 \text{ in.})^2}$ | $= \frac{(19.5 \text{ kip/in.})(52.0 \text{ in.})}{(29{,}000 \text{ ksi})(48.0 \text{ in.}/52.0 \text{ in.})^2}$ |
| $= 0.0351 \text{ in.}^2$ | $= 0.0410 \text{ in.}^2$ |

The strength requirement controls, therefore select an L2×2×⅛ with $A = 0.491 \text{ in.}^2$

At the column at point B, the required strength would be one-half of that at point C, because $C_d = 1.0$ at point B instead of 2.0. However, because the smallest angle available has been selected for the brace, there is no reason to check further at the column, and the same angle will be used there.

---

# A6-23

# EXAMPLE A-6.6 POINT TORSIONAL STABILITY BRACING OF A BEAM

## Given:

A roof system is composed of ASTM A992/A992M W12×40 intermediate beams spaced 5 ft on center supporting a connected roof system that cannot be used as a diaphragm. As shown in Figure A-6.6-1, the beams span 30 ft and are supported on W30×90 girders spanning 60 ft. This is an isolated roof structure with no connections to other structures that could provide lateral support to the girder compression flanges. Thus, the flexural resistance of the attached beams must be used to provide torsional stability bracing to the girders. The roof dead load is 40 psf and the roof live load is 24 psf. Determine if the beams are sufficient to provide point torsional stability bracing.

<div style="text-align: center;">
<img src="roof_system_plan_elevation" alt="Two diagrams showing:
(a) Plan view:
- Grid pattern showing W12×40 beams (typ.) spaced at regular intervals
- W30×90 girders
- Overall dimensions: 60'-0" horizontal, 30'-0" vertical
- 5'-0" typical spacing marked

(b) Point torsional brace connection detail:
- W30×90 girder section
- W12×40 beam connection
- Full depth stiffener shown
- Detail of connection at top flange">
</div>

*(a) Plan                    (b) Point torsional brace connection*

*Fig. A-6.6-1. Roof system configuration*

## Solution:

Because the bracing beams are not connected in a way that would permit them to transfer an axial bracing force, they must behave as point torsional braces if they are to effectively brace the girders.

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam and girder
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W12×40
$t_w = 0.295$ in.
$I_x = 307 \text{ in.}^4$

Girder
W30×90
$t_w = 0.470$ in.
$h_o = 28.9$ in.
$I_t = 115 \text{ in.}^4$

---

# A6-24

*Required Flexural Strength of Girder*

From ASCE/SEI 7, Chapter 2, and using AISC *Manual* Table 3-22, Case 1, the required strength of the girder is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(40 \text{ psf}) + 1.6(24 \text{ psf})$ | $w_a = 40 \text{ psf} + 24 \text{ psf}$ |
| $= 86.4$ psf | $= 64.0$ psf |
| $w_u = \frac{(86.4 \text{ psf})(15 \text{ ft})}{1{,}000 \text{ lb/kip}}$ | $w_a = \frac{(64.0 \text{ psf})(15 \text{ ft})}{1{,}000 \text{ lb/kip}}$ |
| $= 1.30$ kip/ft | $= 0.960$ kip/ft |
| $M_u = \frac{w_u L^2}{8}$ | $M_a = \frac{w_a L^2}{8}$ |
| $= \frac{(1.30 \text{ kip/ft})(60 \text{ ft})^2}{8}$ | $= \frac{(0.960 \text{ kip/ft})(60 \text{ ft})^2}{8}$ |
| $= 585$ kip-ft | $= 432$ kip-ft |

With $C_b = 1.0$, from AISC *Manual* Table 6-1, the maximum unbraced length permitted for the W30×90 based upon required flexural strength is:

| LRFD | ASD |
|------|-----|
| For $M_{uB} = 585$ kip-ft, $L_b = 22.0$ ft | For $M_{aB} = 432$ kip-ft, $L_b = 20.5$ ft |

*Point Torsional Brace Design*

The required flexural strength for a point torsional brace for the girder is determined from AISC *Specification* Appendix 6, Section 6.3.2a. Based on the User Note in *Specification* Section 6.3.2a:

$$I_{yeff} = I_y$$
$$= 115 \text{ in.}^4$$

| LRFD | ASD |
|------|-----|
| $M_r = M_{uB}$ | $M_r = M_{aB}$ |
| $= 585$ kip-ft | $= 432$ kip-ft |

---

# A6-25

| LRFD | ASD |
|------|-----|
| $M_{br} = \frac{3.6L}{\pi EI_{yeff}}\left(\frac{M_r}{C_b}\right)^2\left(\frac{L_{br}}{500h_o}\right) \geq 0.02M_r$ | $M_{br} = \frac{3.6L}{\pi EI_{yeff}}\left(\frac{M_r}{C_b}\right)^2\left(\frac{L_{br}}{500h_o}\right) \geq 0.02M_r$ |
| (*Spec.* Eq. A-6-9) | (*Spec.* Eq. A-6-9) |
| $= \frac{3.6(60 \text{ ft})(12 \text{ in./ft})}{(11)(29{,}000 \text{ ksi})(115 \text{ in.}^4)}$ | $= \frac{3.6(60 \text{ ft})(12 \text{ in./ft})}{(11)(29{,}000 \text{ ksi})(115 \text{ in.}^4)}$ |
| $\times\left[\frac{(585 \text{ kip-ft})(12 \text{ in./ft})}{1.0}\right]^2$ | $\times\left[\frac{(432 \text{ kip-ft})(12 \text{ in./ft})}{1.0}\right]^2$ |
| $\times\left[\frac{(5 \text{ ft})(12 \text{ in./ft})}{500(28.9 \text{ in.})}\right]\left(\frac{1 \text{ ft}}{12 \text{ in.}}\right)$ | $\times\left[\frac{(5 \text{ ft})(12 \text{ in./ft})}{500(28.9 \text{ in.})}\right]\left(\frac{1 \text{ ft}}{12 \text{ in.}}\right)$ |
| $> 0.02(585 \text{ kip-ft})$ | $< 0.02(432 \text{ kip-ft})$ |
| $= 1.20 \text{ kip-ft} < 11.7 \text{ kip-ft}$ | $= 7.88 \text{ kip-ft} < 8.64 \text{ kip-ft}$ |
| Therefore: | Therefore: |
| $M_{br} = 11.7$ kip-ft | $M_{br} = 8.64$ kip-ft |

The required overall point torsional brace stiffness with braces every 5 ft, $n = 11$, and assuming $C_b = 1.0$, is determined in the following.

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 3.00$ |
| $\beta_T = \frac{1}{\phi}\frac{3.6L}{\pi nEI_{yeff}}\left(\frac{M_r}{C_b}\right)^2$ (*Spec.* Eq. A-6-11a) | $\beta_T = \Omega\frac{3.6L}{\pi nEI_{yeff}}\left(\frac{M_r}{C_b}\right)^2$ (*Spec.* Eq. A-6-11b) |
| $= \frac{1}{0.75}\left[\frac{3.6(60 \text{ ft})(12 \text{ in./ft})}{11(29{,}000 \text{ ksi})(115 \text{ in.}^4)}\right]$ | $= 3.00\left[\frac{3.6(60 \text{ ft})(12 \text{ in./ft})}{11(29{,}000 \text{ ksi})(115 \text{ in.}^4)}\right]$ |
| $\times\left[\frac{(585 \text{ kip-ft})(12 \text{ in./ft})}{1.0}\right]^2$ | $\times\left[\frac{(432 \text{ kip-ft})(12 \text{ in./ft})}{1.0}\right]^2$ |
| $= 4{,}640 \text{ kip-in./rad}$ | $= 5{,}700 \text{ kip-in./rad}$ |

The distortional buckling stiffness of the girder web is a function of the web slenderness and the presence of any stiffeners. The web distortional stiffness is:

$$\beta_{sec} = \frac{3.3E}{h_o}\left(\frac{1.5h_o t_w^3}{12} + \frac{t_st b_s^3}{12}\right)$$
(*Spec.* Eq. A-6-12)

Therefore, the distortional stiffness of the girder web alone is:

$$\beta_{sec} = \frac{3.3E}{h_o}\left(\frac{1.5h_o t_w^3}{12}\right)$$

$$= \frac{3.3(29{,}000 \text{ ksi})}{28.9 \text{ in.}}\left[\frac{1.5(28.9 \text{ in.})(0.470 \text{ in.})^3}{12}\right]$$

$$= 1{,}240 \text{ kip-in./rad}$$

---

# A6-26

For AISC *Specification* Equation A-6-10 to give a nonnegative result, the web distortional stiffness given by Equation A-6-12 must be greater than the required point torsional stiffness given by Equation A-6-11. Because the web distortional stiffness of the girder is less than the required point torsional stiffness for both LRFD and ASD, web stiffeners will be required.

Determine the torsional stiffness contributed by the beams. Both girders will buckle in the same direction forcing the beams to bend in reverse curvature. Thus, the flexural stiffness of the beam using AISC *Manual* Table 3-22, Case 9, is:

$$\beta_{Tb} = \frac{6EI}{L}$$

$$= \frac{6(29{,}000 \text{ ksi})(307 \text{ in.}^4)}{(30 \text{ ft})(12 \text{ in./ft})}$$

$$= 148{,}000 \text{ kip-in./rad}$$

Determining the required distortional stiffness of the girder will permit determination of the required stiffener size. The total stiffness is determined by summing the inverse of the distortional and flexural stiffnesses. Thus:

$$\frac{1}{\beta_T} = \frac{1}{\beta_{Tb}} + \frac{1}{\beta_{sec}}$$

Determine the minimum web distortional stiffness required to provide bracing for the girder.

| LRFD | ASD |
|------|-----|
| $\frac{1}{\beta_T} = \frac{1}{\beta_{Tb}} + \frac{1}{\beta_{sec}}$ | $\frac{1}{\beta_T} = \frac{1}{\beta_{Tb}} + \frac{1}{\beta_{sec}}$ |
| $\frac{1}{4{,}640 \text{ kip-in./rad}} = \frac{1}{148{,}000 \text{ kip-in./rad}} + \frac{1}{\beta_{sec}}$ | $\frac{1}{5{,}700 \text{ kip-in./rad}} = \frac{1}{148{,}000 \text{ kip-in./rad}} + \frac{1}{\beta_{sec}}$ |
| $\beta_{sec} = 4{,}790 \text{ kip-in./rad}$ | $\beta_{sec} = 5{,}930 \text{ kip-in./rad}$ |

Determine the required width, $b_s$, of ⅜-in.-thick stiffeners.

$$\beta_{sec} = \frac{3.3E}{h_o}\left(\frac{1.5h_o t_w^3}{12} + \frac{t_{st} b_s^3}{12}\right)$$
(*Spec.* Eq. A-6-12)

Using the total required girder web distortional stiffness and the contribution of the girder web distortional stiffness calculated previously, solve for the required width for ⅜-in.-thick stiffeners:

| LRFD | ASD |
|------|-----|
| $4{,}790 \text{ kip-in./rad} = 1{,}240 \text{ kip-in./rad}$ | $5{,}930 \text{ kip-in./rad} = 1{,}240 \text{ kip-in./rad}$ |
| $+ \frac{3.3(29{,}000 \text{ ksi})}{28.9 \text{ in.}}\left[\frac{(\frac{3}{8} \text{ in.})b_s^3}{12}\right]$ | $+ \frac{3.3(29{,}000 \text{ ksi})}{28.9 \text{ in.}}\left[\frac{(\frac{3}{8} \text{ in.})b_s^3}{12}\right]$ |
| and $b_s = 3.25$ in. | and $b_s = 3.56$ in. |

Therefore, use a 4 in. × ⅜ in. full depth one-sided stiffener at the connection of each beam.

---

# A6-27

*Available Flexural Strength of Beam*

Each beam is connected to a girder web stiffener. Thus, each beam will be coped at the top and bottom as shown in Figure A-6.6-1(b), with a depth at the coped section of 9 in. The available flexural strength of the coped beam is determined using the provisions of AISC *Specification* Sections J4.5 and F11.

$$M_n = M_p = F_y Z \leq 1.5F_y S_x$$
(*Spec.* Eq. F11-1)

For a rectangle, $Z = 1.5S$. Therefore, strength will be controlled by $F_y Z$ and

$$Z = \frac{(0.295 \text{ in.})(9.00 \text{ in.})^2}{4}$$

$$= 5.97 \text{ in.}^3$$

The nominal flexural strength of the beam is:

$$M_n = F_y Z_x$$

$$= \frac{(50 \text{ ksi})(5.97 \text{ in.}^3)}{(12 \text{ in./ft})}$$

$$= 24.9 \text{ kip-ft}$$

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(24.9 \text{ kip-ft})$ | $\frac{M_n}{\Omega_b} = \frac{24.9 \text{ kip-ft}}{1.67}$ |
| $= 22.4 \text{ kip-ft} > 11.7 \text{ kip-ft}$ **o.k.** | $= 14.9 \text{ kip-ft} > 8.64 \text{ kip-ft}$ **o.k.** |

Neglecting any rotation due to the bolts moving in the holes or any influence of the end moments on the strength of the beams, this system has sufficient strength and stiffness to provide point torsional bracing to the girders.

Additional connection design limit states may also need to be checked.

---
