# Chapter IID: Miscellaneous

**AISC Specification v16.0 - Design Examples**
**Original PDF Pages**: 913-940 (28 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Miscellaneous Connections

**Examples Included**: ['II.D-1~II.D-2: Bearing plates, etc.']

---

## Table of Contents

- [EXAMPLE II.D-1 WT HANGER CONNECTION](#example-iid-1-wt-hanger-connection)
- [EXAMPLE II.D-2 BEAM BEARING PLATE](#example-iid-2-beam-bearing-plate)

---

# IID-1

# Chapter IID
# Miscellaneous Connections

This section contains design examples on connections in the AISC *Steel Construction Manual* that are not covered in other sections of the AISC *Design Examples*.

---

# IID-2

## EXAMPLE II.D-1 WT HANGER CONNECTION

**Given:**

Design a WT hanger connection between a 2L3×3×⅜ tension member and W21x57 beam, as shown in Figure II.D-1-1. The beam and WT hanger are ASTM A992/A992M material. The angles are ASTM A572/A572M Grade 50 material. Use 70-ksi electrodes. The loads in the hanger are:

$P_D = 10$ kips
$P_L = 30$ kips

The required flexural strength of the W21x57 beam at the location of the connection is:

$M_D = 675$ kip-in.
$M_L = 2,280$ kip-in.

Note: the required flexural strength of the W21x57 beam is not only due to loading from the hanger connection.

![Connection diagram showing:
- Top: W21×57 beam
- Center: WT hanger connection with typ. notation
- Bottom: 2L3×3×⅝ angles
- Load arrows: PD = 10 kips, PL = 30 kips
- Right side view showing 3½" dimension]

*Fig. II.D-1-1. Connection Geometry for Example II.D-1*

**Solution:**

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam and WT hanger
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Angles
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

---

# IID-3

From AISC *Manual* Tables 1-1, 1-7, and 1-15, the geometric properties are as follows:

Beam
W21×57
$d = 21.1$ in.
$t_w = 0.405$ in.
$b_f = 6.56$ in.
$t_f = 0.650$ in.
$S_x = 111$ in.$^3$

Angles
2L3×3×⅜
$A = 3.56$ in.$^2$
$\overline{x} = 0.860$ in. (for single angle)

From AISC *Specification* Table J3.3, the hole diameter for ¾-in.-diameter bolts with standard holes is:

$d_h = \frac{13}{16}$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(10 \text{ kips}) + 1.6(30 \text{ kips})$ | $P_a = 10 \text{ kips} + 30 \text{ kips}$ |
| $= 60.0$ kips | $= 40.0$ kips |

*Angle to Tee Stem Weld Design*

Note: AISC *Specification* Section J1.7 requiring that the center of gravity of the weld group coincide with the center of gravity of the member does not apply to end connections of statically loaded single-angle, double-angle, and similar members.

From AISC *Specification* Table J2.4, the minimum weld size for a $\frac{3}{16}$-in.-thick angle is:

$w_{min} = \frac{3}{16}$ in.

From AISC *Specification* Section J2.2b(b)(2), the maximum weld size is:

$$w_{max} = t - \frac{1}{16} \text{ in.}$$
$$= \frac{5}{16} - \frac{1}{16} \text{ in.}$$
$$= ¼ \text{ in.}$$

Try $\frac{3}{16}$ in. fillet welds.

The minimum weld length is determined using AISC *Manual* Equations 8-2a or 8-2b, as follows:

| LRFD | ASD |
|------|-----|
| $l_{min} = \frac{R_u}{(2 \text{ sides})(2 \text{ welds})(1.392 \text{ kip/in.})D}$ | $l_{min} = \frac{R_a}{(2 \text{ sides})(2 \text{ welds})(0.928 \text{ kip/in.})D}$ |
|  |  |
| $= \frac{60.0 \text{ kips}}{(2 \text{ sides})(2 \text{ welds})(1.392 \text{ kip/in.})(3)}$ | $= \frac{40.0 \text{ kips}}{(2 \text{ sides})(2 \text{ welds})(0.928 \text{ kip/in.})(3)}$ |
| $= 3.59$ in. | $= 3.59$ in. |

---

# IID-4

Use a 4-in.-long $\frac{3}{16}$ in. fillet weld at the heel and toe of the angles.

*Shear Strength of Angles*

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the angles is determined as follows:

$$A_{nv} = (2 \text{ angles})(2 \text{ welds})lt$$
$$= (2 \text{ angles})(2 \text{ welds})(4 \text{ in.})(\frac{3}{16} \text{ in.})$$
$$= 5.00 \text{ in.}$$

$$R_n = 0.60F_u A_{nv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(65 \text{ ksi})(5.00 \text{ in.})$$
$$= 195 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(195 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{195 \text{ kips}}{2.00}$ |
| $= 146 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $= 97.5 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

*Tensile Strength of Angles*

From AISC *Specification* Section D2, the available tensile yielding strength of the angles is determined as follows:

$$P_n = F_y A_g$$ (*Spec.* Eq. D2-1)
$$= (50 \text{ ksi})\left(3.56 \text{ in.}^2\right)$$
$$= 178 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi_t = 0.90$ | $\Omega_t = 1.67$ |
|  |  |
| $\phi_t P_n = 0.90(178 \text{ kips})$ | $\frac{P_n}{\Omega_t} = \frac{178 \text{ kips}}{1.67}$ |
| $= 160 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $= 107 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section D2, the available tensile rupture strength of the angles is determined as follows:

$$A_n = A_g$$
$$= 3.56 \text{ in.}^2$$

The shear lag factor, $U$, is determined from AISC *Specification* Table D3.1, Case 4:

---

# IID-5

$$U = \frac{3l^2}{3l^2 + w^2}\left(1 - \frac{\overline{x}}{l}\right)$$

$$= \frac{3(4 \text{ in.})^2}{3(4 \text{ in.})^2 + (3 \text{ in.})^2}\left(1 - \frac{0.860 \text{ in.}}{4 \text{ in.}}\right)$$

$$= 0.661$$

$$A_e = A_n U$$ (*Spec.* Eq. D3-1)
$$= \left(3.56 \text{ in.}^2\right)(0.661)$$
$$= 2.35 \text{ in.}^2$$

$$P_n = F_u A_e$$ (*Spec.* Eq. D2-2)
$$= (65 \text{ ksi})\left(2.35 \text{ in.}^2\right)$$
$$= 153 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi_t = 0.75$ | $\Omega_t = 2.00$ |
|  |  |
| $\phi_t P_n = 0.75(153 \text{ kips})$ | $\frac{P_n}{\Omega_t} = \frac{153 \text{ kips}}{2.00}$ |
| $= 115 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $= 76.5 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

*Preliminary WT Selection Using Beam Gage*

The required tensile strength per bolt is determined as follows:

| LRFD | ASD |
|------|-----|
| $r_{rt} = \frac{P_u}{n}$ | $r_{rt} = \frac{P_a}{n}$ |
|  |  |
| $= \frac{60.0 \text{ kips}}{4 \text{ bolts}}$ | $= \frac{40.0 \text{ kips}}{4 \text{ bolts}}$ |
| $= 15.0$ kips/bolt | $= 10.0$ kips/bolt |

Try four ¾-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N), with a 3½ in. gage. The available bolt tensile strength is determined from AISC *Manual* Table 7-2.

| LRFD | ASD |
|------|-----|
| $\phi r_n = 29.8 \text{ kips/bolt} > 15.0 \text{ kips/bolt} \quad \textbf{o.k.}$ | $\frac{r_n}{\Omega} = 19.9 \text{ kips/bolt} > 10.0 \text{ kips/bolt} \quad \textbf{o.k.}$ |

Try a 9-in.-long WT hanger with bolt rows spaced at 5 in. A trial tributary length per bolt, $p$, is determined using AISC *Manual* Figure 9-4, assuming $b = (3½ \text{ in.} - ½ \text{ in.})/2 = 1.50$ in.

$$p = \min\left\{\begin{array}{l}l_c = 2.00 \text{ in.},\\ 1.75b = 1.75(1.50 \text{ in.}) = 2.63 \text{ in.}\end{array}\right\} + \min\left\{\begin{array}{l}s/2 = 5 \text{ in.}/2 = 2.50 \text{ in.},\\ 1.75b = 1.75(1.50 \text{ in.}) = 2.63 \text{ in}\end{array}\right\}$$
$$= 2.00 \text{ in.} + 2.50 \text{ in.}$$
$$= 4.50 \text{ in.}$$

---

# IID-6

A preliminary hanger connection is determined using AISC *Manual* Table 15-1.

| LRFD | ASD |
|------|-----|
| $2r_{rt} = \frac{P_u}{(2 \text{ rows})p}$ | $2r_{rt} = \frac{P_a}{(2 \text{ rows})p}$ |
|  |  |
| $= \frac{60.0 \text{ kips}}{(2)(4.50 \text{ in.})}$ | $= \frac{40.0 \text{ kips}}{(2)(4.50 \text{ in.})}$ |
| $= 6.67$ kip/in. | $= 4.44$ kip/in. |

From AISC *Manual* Table 15-1, with an assumed $b = 1½$ in., the flange thickness, $t = t_f$, of the WT hanger should be at least $\frac{7}{16}$ in.

The minimum depth WT that can be used is equal to the sum of the weld length plus the weld size plus the $k$-dimension for the selected section ($d \geq 4$ in. + ½ in. + $k =$ 6 in.). Additionally, select a tee with a flange width less than or equal to the width of the beam flange ($b_f \leq 6.56$ in).

From AISC *Manual* Table 1-8, appropriate selections include:

WT6×17.5
WT9×20
WT9×23

Try a WT6×17.5.

From AISC *Manual* Table 1-8, the geometric properties are as follows:

$d = 6.25$ in.
$b_f = 6.56$ in.
$t_f = 0.520$ in.
$t_w = 0.300$ in.

Determine if the flange width is adequate:

From AISC *Specification* Table J3.4, the minimum edge distance for ¾-in.-diameter bolts is 1 in.

$$\frac{b_f - gage}{2} = \frac{6.56 \text{ in.} - 3½ \text{ in.}}{2}$$
$$= 1.53 \text{ in.} > 1 \text{ in.} \quad \textbf{o.k.}$$

*Prying Action*

From AISC *Manual* Part 9, the available tensile strength of the bolts taking prying action into account is determined as follows. Note, "Solution Method 2" is selected for a design that results in the smallest tee flange thickness. The beam flange is thicker than the WT flange; therefore, prying in the WT flange will control over prying in the beam flange.

$$b = \frac{(3½ \text{ in.} - 0.300 \text{ in.})}{2}$$
$$= 1.60 \text{ in.}$$

The tributary length per pair of bolts, $p$, is determined using AISC *Manual* Figure 9-4.

---

# IID-7

$$p = \min\left\{\begin{array}{l}l_c = 2.00 \text{ in.},\\ 1.75b = 1.75(1.60 \text{ in.}) = 2.80 \text{ in.}\end{array}\right\} + \min\left\{\begin{array}{l}s/2 = 5 \text{ in.}/2 = 2.50 \text{ in.},\\ 1.75b = 1.75(1.60 \text{ in.}) = 2.80 \text{ in}\end{array}\right\}$$
$$= 2.00 \text{ in.} + 2.50 \text{ in.}$$
$$= 4.50 \text{ in.}$$

$$a = \frac{b_f - gage}{2}$$
$$= \frac{6.56 \text{ in.} - 3½ \text{ in.}}{2}$$
$$= 1.53 \text{ in.}$$

$$b' = b - \frac{d}{2}$$ (*Manual* Eq. 9-24)
$$= 1.60 \text{ in.} - \left(\frac{¾ \text{ in.}}{2}\right)$$
$$= 1.23 \text{ in.}$$

$$a' = \min\left\{a + \frac{d}{2}, \, 1.25b + \frac{d}{2}\right\}$$ (from *Manual* Eq. 9-23)
$$= \min\left\{1.53 \text{ in.} + \frac{¾ \text{ in.}}{2}, \, 1.25(1.60 \text{ in.}) + \frac{¾ \text{ in.}}{2}\right\}$$
$$= \min\{1.91 \text{ in.}, \, 2.38 \text{ in.}\}$$
$$= 1.91 \text{ in.}$$

$$\rho = \frac{b'}{a'}$$ (*Manual* Eq. 9-29)
$$= \frac{1.23 \text{ in.}}{1.91 \text{ in.}}$$
$$= 0.644$$

From AISC *Manual* Equation 9-35:

| LRFD | ASD |
|------|-----|
| $\beta = \frac{1}{\rho}\left(\frac{T_c}{T_r} - 1\right)$ (*Manual* Eq. 9-35) | $\beta = \frac{1}{\rho}\left(\frac{T_c}{T_r} - 1\right)$ (*Manual* Eq. 9-35) |
|  |  |
| $= \frac{1}{0.644}\left(\frac{29.8 \text{ kips/bolt}}{15.0 \text{ kips/bolt}} - 1\right)$ | $= \frac{1}{0.644}\left(\frac{19.9 \text{ kips/bolt}}{10.0 \text{ kips/bolt}} - 1\right)$ |
| $= 1.53$ | $= 1.54$ |

Because $\beta \geq 1$, use AISC *Manual* Equation 9-36a:

$\alpha' = 1.0$

$$d' = d_h$$
$$= \frac{13}{16} \text{ in.}$$

---

# IID-8

$$\delta = 1 - \frac{d'}{p}$$ (*Manual* Eq. 9-28)
$$= 1 - \frac{\frac{13}{16} \text{ in.}}{4.50 \text{ in.}}$$
$$= 0.819$$

The minimum tee flange thickness is determined as follow:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
|  |  |
| $t_{min} = \sqrt{\frac{4T_r b'}{\phi_b pF_u\left(1 + \delta\alpha'\right)}}$ (*Manual* Eq. 9-37a) | $t_{min} = \sqrt{\frac{4\Omega_b T_r b'}{pF_u\left(1 + \delta\alpha'\right)}}$ (*Manual* Eq. 9-37b) |
|  |  |
| $= \sqrt{\frac{4(15.0 \text{ kips/bolt})(1.23 \text{ in.})}{0.90(4.50 \text{ in.})(65 \text{ ksi})\left[1 + (0.819)(1)\right]}}$ | $= \sqrt{\frac{4(1.67)(10.0 \text{ kips/bolt})(1.23 \text{ in.})}{(4.50 \text{ in.})(65 \text{ ksi})\left[1 + (0.819)(1)\right]}}$ |
| $= 0.393 \text{ in.} < t_f = 0.520 \text{ in.} \quad \textbf{o.k.}$ | $= 0.393 \text{ in.} < t_f = 0.520 \text{ in.} \quad \textbf{o.k.}$ |

Note: As an alternative to the preceding calculations, the designer can use a simplified procedure to select a WT hanger with a flange thick enough to eliminate prying action. The required thickness to eliminate prying action is determined from AISC *Manual* Equation 9-30a or 9-30b, as follows:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
|  |  |
| $t_c = \sqrt{\frac{4T_c b'}{\phi_b pF_u}}$ (*Manual* Eq. 9-30a) | $t_c = \sqrt{\frac{4\Omega_b T_r b'}{pF_u}}$ (*Manual* Eq. 9-30b) |
|  |  |
| $= \sqrt{\frac{4(15.0 \text{ kips/bolt})(1.23 \text{ in.})}{0.90(4.50 \text{ in.})(65 \text{ ksi})}}$ | $= \sqrt{\frac{4(1.67)(10.0 \text{ kips/bolt})(1.23 \text{ in.})}{(4.50 \text{ in.})(65 \text{ ksi})}}$ |
| $= 0.529$ in. | $= 0.530$ in. |

The WT6×17.5 that was selected does not have a sufficient flange thickness to reduce the effect of prying action to an insignificant amount. In this case, the simplified approach requires a WT section with a thicker flange.

*Shear Strength of the WT Flange*

From AISC *Specification* Section J4.2(a), the available shear yield strength of the WT flanges is determined as follows:

$$A_{gv} = (2 \text{ flanges})lt_f$$
$$= (2 \text{ flanges})(9 \text{ in.})(0.520 \text{ in.})$$
$$= 9.36 \text{ in.}$$

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})(9.36 \text{ in.})$$
$$= 281 \text{ kips}$$

---

# IID-9

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(281 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{281 \text{ kips}}{1.50}$ |
| $= 281 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $= 187 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the WT flanges is determined as follows:

$$A_{nv} = (2 \text{ flanges})\left[l - n(d_h + \frac{1}{16} \text{ in.})\right]t_f$$
$$= (2 \text{ flanges})\left[9 \text{ in.} - 2(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.})\right](0.520 \text{ in.})$$
$$= 7.54 \text{ in.}$$

$$R_n = 0.60F_u A_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})(7.54 \text{ in.})$$
$$= 294 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(294 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{294 \text{ kips}}{2.00}$ |
| $= 221 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $= 147 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

*Tensile Yielding of the WT Stem on the Whitmore Section*

As shown in AISC *Manual* Figure 9-1, the Whitmore section defines the effective width of the WT stem. Note that the Whitmore section cannot exceed the actual 9 in. length of the WT.

$$l_w = 3.00 \text{ in.} + 2(4.00 \text{ in.})(\tan 30°) \leq 9.00 \text{ in.}$$
$$= 7.62 \text{ in.} < 9.00 \text{ in.}$$

Therefore:
$l_w = 7.62$ in.

From AISC *Specification* Section J4.1(a), the available tensile yielding strength of the WT stem is determined as follows:

$$A_g = l_w t_w$$
$$= (7.62 \text{ in.})(0.300 \text{ in.})$$
$$= 2.29 \text{ in.}^2$$

$$R_n = F_y A_g$$ (*Spec.* Eq. J4-1)
$$= (50 \text{ ksi})\left(2.29 \text{ in.}^2\right)$$
$$= 115 \text{ kips}$$

---

# IID-10

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi R_n = 0.90(115 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{115 \text{ kips}}{1.67}$ |
| $= 104 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $= 68.9 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

*Shear Rupture of the WT Stem Base Metal*

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the WT stem at the welds is determined as follows:

$$R_n = (2 \text{ planes})0.60F_u l_w t_w$$ (from *Spec.* Eq. J4-4)
$$= (2 \text{ planes})(0.60)(65 \text{ ksi})(4 \text{ in.})(0.300 \text{ in.})$$
$$= 93.6 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(93.6 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{93.6 \text{ kips}}{2.00}$ |
| $= 70.2 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $= 46.8 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture of the WT Stem*

The available strength for the limit state of block shear rupture of the stem assuming a U-shaped tearout relative to the axial load is determined as follows.

$$R_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$ (*Spec.* Eq. J4-5)

where

$$A_{gv} = A_{nv}$$
$$= (2 \text{ lines})lt_w$$
$$= (2 \text{ lines})(4 \text{ in.})(0.300 \text{ in.})$$
$$= 2.40 \text{ in.}^2$$

$$A_{nt} = (leg)t_w$$
$$= (3 \text{ in.})(0.300 \text{ in.})$$
$$= 0.900 \text{ in.}^2$$

$U_{bs} = 1.0$

and

$$R_n = 0.60(65 \text{ ksi})\left(2.40 \text{ in.}^2\right) + 1.0(65 \text{ ksi})\left(0.900 \text{ in.}^2\right) \leq 0.60(50 \text{ ksi})\left(2.40 \text{ in.}^2\right) + 1.0(65 \text{ ksi})\left(0.900 \text{ in.}^2\right)$$
$$= 152 \text{ kips} > 131 \text{ kips}$$

---

# IID-11

Therefore:
$R_n = 131$ kips

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(131 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{131 \text{ kips}}{2.00}$ |
| $= 98.3 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $= 65.5 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

The available strength for the limit state of block shear rupture of the stem assuming an L-shaped tearout relative to the axial load is determined as follows.

$$R_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$ (*Spec.* Eq. J4-5)

where

$$A_{gv} = A_{nv}$$
$$= lt_w$$
$$= (4 \text{ in.})(0.300 \text{ in.})$$
$$= 1.20 \text{ in.}^2$$

$$A_{nt} = \left[leg + \left(\frac{l - leg}{2}\right)\right]t_w$$
$$= \left[3.00 \text{ in.} + \left(\frac{9.00 \text{ in.} - 3.00 \text{ in.}}{2}\right)\right](0.300 \text{ in.})$$
$$= 1.80 \text{ in.}^2$$

$U_{bs} = 1.0$

and

$$R_n = 0.60(65 \text{ ksi})\left(1.20 \text{ in.}^2\right) + 1.0(65 \text{ ksi})\left(1.80 \text{ in.}^2\right) \leq 0.60(50 \text{ ksi})\left(1.20 \text{ in.}^2\right) + 1.0(65 \text{ ksi})\left(1.80 \text{ in.}^2\right)$$
$$= 164 \text{ kips} > 153 \text{ kips}$$

Therefore:
$R_n = 153$ kips

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(153 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{153 \text{ kips}}{2.00}$ |
| $= 115 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ | $= 76.5 \text{ kips} > 40.0 \text{ kips} \quad \textbf{o.k.}$ |

*Strength Reduction of Beam with Bolt Holes in Tension Flange:*

From ASCE/SEI 7, Chapter 2, the required flexural strength of the W21x57 beam at the hanger location is:

---

# IID-12

| LRFD | ASD |
|------|-----|
| $M_u = 1.2(675 \text{ kip-in.}) + 1.6(2,280 \text{ kip-in.})$ | $M_a = 675 \text{ kip-in.} + 2,280 \text{ kip-in.}$ |
| $= 4,460$ kip-in. | $= 2,960$ kip-in. |

From AISC *Specification* Section F13.1, the nominal flexural strength, $M_n$, of beams with bolt holes in the tension flange is limited according to the limit state of tensile rupture of the tension flange. The limit does not apply if $F_u A_{fn} > Y_t F_y A_{fg}$.

where

$$A_{fg} = b_f t_f$$
$$= (6.56 \text{ in.})(0.650 \text{ in.})$$
$$= 4.26 \text{ in.}^2$$

$$A_{fn} = A_{fg} - n(d_h + \frac{1}{16} \text{ in.})t_w$$
$$= 4.26 \text{ in.}^2 - (2 \text{ bolts})(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.})(0.650 \text{ in.})$$
$$= 3.12 \text{ in.}^2$$

Because $F_u/F_n = 50$ ksi/65 ksi = 0.769 < 0.8$, $Y_t = 1.0$

$$F_u A_{fn} = (65 \text{ ksi})(3.12 \text{ in.})$$
$$= 203 \text{ kips}$$

$$Y_t F_y A_{fg} = (1.0)(50 \text{ ksi})(4.26 \text{ in.})$$
$$= 213 \text{ kips}$$

Because $F_u A_{fn} < Y_t F_y A_{fg}$, the nominal flexural strength, $M_n$, at the location of the bolt holes in the beam flange is:

$$M_n = \frac{F_u A_{fn}}{A_{fg}}S_x$$ (*Spec.* Eq. F13-1)

$$= \frac{(65 \text{ ksi})(3.12 \text{ in.}^2)}{4.26 \text{ in.}^2}\left(111 \text{ in.}^3\right)$$
$$= 5,280 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi R_n = 0.90(5,280 \text{ kip-in.})$ | $\frac{R_n}{\Omega} = \frac{5,280 \text{ kip-in.}}{1.67}$ |
| $= 4,750 \text{ kip-in.} > 4,460 \text{ kip-in.} \quad \textbf{o.k.}$ | $= 3,160 \text{ kip-in.} > 2,960 \text{ kip-in.} \quad \textbf{o.k.}$ |

The flexural strength of the W21x57 beam at the tension flange bolt holes is adequate for the required moments.

The final connection design is shown in Figure II.D-1-2.

---

# IID-13

![Connection diagram showing:
- Top: W21×57 beam
- Center: WT6×17.5 hanger with dimensions 9", 5"
- Right side view showing 3½" dimension and ¾" dia. Group 120, thread condition N, std. holes
- Bottom: 2L3×3×⅝ angles with welds 3/16 and 4 typ.
- Load arrows: PD = 10 kips, PL = 30 kips
- 4½ min. notation on left side]

*Fig. II.D-1-2. Final hanger design for Example II.D-1*

---

# IID-14

## EXAMPLE II.D-2 BEAM BEARING PLATE

**Given:**

An ASTM A992/A992M W18×50 beam supported by a 10-in.-thick concrete wall, as shown in Figure II.D-2-1, has the following end reactions:

$R_D = 15$ kips
$R_L = 45$ kips

Verify the following:

A. If a bearing plate is required when the beam is supported by the full wall thickness ($l_b = h = 10$ in)
B. The bearing plate required if $l_b = h = 10$ in. (the full wall thickness)
C. The bearing plate required if $l_b = 6½$ in. and the bearing plate is centered on the thickness of the wall

The concrete has $f_c' = 3$ ksi and the bearing plate is ASTM A572/A572M Grade 50 material.

![Connection diagram showing:
- Left: Side view with bearing plate on concrete wall, dimensions n, kk, n, B, and k marked
- Right: Front view showing W18×50 beam, lb + 2.5k dimension, lb dimension, and h = 10" dimension]

*Fig. II.D-2-1. Connection geometry for Example II.D-2.*

**Solution:**

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Beam
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Bearing plate
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

Concrete wall
$f_c' = 3$ ksi

---

# IID-15

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W18×50
$d = 18.0$ in.
$t_w = 0.355$ in.
$b_f = 7.50$ in.
$t_f = 0.570$ in.
$k_{des} = 0.972$ in.
$k_1 = 1\frac{3}{16}$ in.

From ASCE/SEI, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(15 \text{ kips}) + 1.6(45 \text{ kips})$ | $R_a = 15 \text{ kips} + 45 \text{ kips}$ |
| $= 90.0$ kips | $= 60.0$ kips |

**Solution A:**

*Required Bearing Length*

The required bearing length for the limit state of web local yielding is determined using AISC *Manual* Table 9-4 and AISC *Manual* Equation 9-60a or 9-60b, as follows:

| LRFD | ASD |
|------|-----|
| $\phi R_1 = 43.1$ kips | $R_1/\Omega = 28.8$ kips |
| $\phi R_2 = 17.8$ kip/in. | $R_2/\Omega = 11.8$ kip/in. |
|  |  |
| $l_b \, min = \frac{R_u - \phi R_1}{\phi R_2} \geq k_{des}$ | $l_b \, min = \frac{R_a - R_1/\Omega}{R_2/\Omega} \geq k_{des}$ |
|  |  |
| $= \frac{90.0 \text{ kips} - 43.1 \text{ kips}}{17.8 \text{ kip/in.}} > 0.972 \text{ in.}$ | $= \frac{60.0 \text{ kips} - 28.8 \text{ kips}}{11.8 \text{ kip/in.}} > 0.972 \text{ in.}$ |
| $= 2.63 \text{ in.} > 0.972 \text{ in.}$ | $= 2.64 \text{ in.} > 0.972 \text{ in.}$ |
|  |  |
| Therefore: | Therefore: |
| $l_b \, min = 2.63 \text{ in.} < 10.0 \text{ in.} \quad \textbf{o.k.}$ | $l_b \, min = 2.64 \text{ in.} < 10.0 \text{ in.} \quad \textbf{o.k.}$ |

The required bearing length for the limit state of web local crippling is determined using AISC *Manual* Table 9-4.

$$\frac{l_b}{d} = \frac{10.0 \text{ in.}}{18.0 \text{ in.}}$$
$$= 0.556$$

Because $\frac{l_b}{d} > 0.2$, use AISC *Manual* Table 9-4 and AISC *Manual* Equation 9-63a or 9-63b, as follows:

| LRFD | ASD |
|------|-----|
| $\phi R_5 = 52.0$ kips | $R_5/\Omega = 34.7$ kips |
| $\phi R_6 = 6.30$ kip/in. | $R_6/\Omega = 4.20$ kip/in. |

---

# IID-16

| LRFD | ASD |
|------|-----|
| $l_b \, min = \frac{R_u - \phi R_5}{\phi R_6} \geq k_{des}$ | $l_b \, min = \frac{R_a - R_5/\Omega}{R_6/\Omega} \geq k_{des}$ |
|  |  |
| $= \frac{90.0 \text{ kips} - 52.0 \text{ kips}}{6.30 \text{ kip/in.}} > 0.972 \text{ in.}$ | $= \frac{60.0 \text{ kips} - 34.7 \text{ kips}}{4.20 \text{ kip/in.}} > 0.972 \text{ in.}$ |
| $= 6.03 \text{ in.} > 0.972 \text{ in.}$ | $= 6.02 \text{ in.} > 0.972 \text{ in.}$ |
|  |  |
| Therefore: | Therefore: |
| $l_b \, min = 6.03 \text{ in.} < 10.0 \text{ in.} \quad \textbf{o.k.}$ | $l_b \, min = 6.02 \text{ in.} < 10.0 \text{ in.} \quad \textbf{o.k.}$ |
|  |  |
| Verify $\frac{l_b}{d} > 0.2$: | Verify $\frac{l_b}{d} > 0.2$: |
|  |  |
| $\frac{l_b}{d} = \frac{6.03 \text{ in.}}{18.0 \text{ in.}}$ | $\frac{l_b}{d} = \frac{6.02 \text{ in.}}{18.0 \text{ in.}}$ |
| $= 0.335 > 0.2 \quad \textbf{o.k.}$ | $= 0.334 > 0.2 \quad \textbf{o.k.}$ |

The bearing strength of the concrete is determined from AISC *Specification* Section J8. Note that AISC *Specification* Equation J8-1 is used because $A_2$ is not larger than $A_1$ in this case.

$$A_1 = b_f l_b$$
$$= (7.50 \text{ in.})(10.0 \text{ in.})$$
$$= 75.0 \text{ in.}^2$$

$$P_p = 0.85f_c'A_1$$ (*Spec.* Eq. J8-1)
$$= 0.85(3 \text{ ksi})\left(75.0 \text{ in.}^2\right)$$
$$= 191 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.65$ | $\Omega_c = 2.31$ |
|  |  |
| $\phi_c P_p = 0.65(191 \text{ kips})$ | $\frac{P_p}{\Omega_c} = \frac{191 \text{ kips}}{2.31}$ |
| $= 124 \text{ kips} > 90.0 \text{ kips} \quad \textbf{o.k.}$ | $= 82.7 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ |

*Beam Flange Thickness*

Using the cantilever length from AISC *Manual* Part 14, determine the minimum beam flange thickness required if no bearing plate is provided. The beam flanges along the length, $n$, are assumed to be fixed end cantilevers with a minimum thickness determined using the limit state of flexural yielding.

$$n = \frac{b_f}{2} - k_{des}$$ (from *Manual* Eq. 14-1)
$$= \frac{7.50 \text{ in.}}{2} - 0.972 \text{ in.}$$
$$= 2.78 \text{ in.}$$

---

# IID-17

| LRFD | ASD |
|------|-----|
| The bearing pressure is determined as follows: | The bearing pressure is determined as follows: |
|  |  |
| $f_p = \frac{R_u}{A_1}$ | $f_p = \frac{R_a}{A_1}$ |
|  |  |
| The required flexural strength of the flange is: | The required flexural strength of the flange is: |
|  |  |
| $M_u = \frac{f_p n^2}{2}$ | $M_a = \frac{f_p n^2}{2}$ |
|  |  |
| $= \frac{R_u n^2}{2A_1}$ | $= \frac{R_a n^2}{2A_1}$ |
|  |  |
| The available flexural strength of the flange is: | The available flexural strength of the flange is: |
|  |  |
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi M_n = \phi F_y Z$ | $\frac{M_n}{\Omega} = \frac{F_y Z}{\Omega}$ |
|  |  |
| $= \phi F_y\left(\frac{t^2}{4}\right)$ | $= \frac{F_y}{\Omega}\left(\frac{t^2}{4}\right)$ |
|  |  |
| For $\phi R_n = R_u$ and solving for $t_f$, the minimum flange thickness is determined as follows: | For $R_n/\Omega = R_a$ and solving for $t_f$, the minimum flange thickness is determined as follows: |
|  |  |
| $t_f \, min = \sqrt{\frac{2R_u n^2}{\phi A_1F_y}}$ | $t_f \, min = \sqrt{\frac{\Omega 2R_a n^2}{A_1F_y}}$ |
|  |  |
| $= \sqrt{\frac{2(90.0 \text{ kips})(2.78 \text{ in.})^2}{0.90(75.0 \text{ in.}^2)(50 \text{ ksi})}}$ | $= \sqrt{\frac{1.67(2)(60.0 \text{ kips})(2.78 \text{ in.})^2}{(75.0 \text{ in.}^2)(50 \text{ ksi})}}$ |
|  |  |
| $= 0.642 \text{ in.} > t_f = 0.570 \text{ in.} \quad \textbf{n.g.}$ | $= 0.643 \text{ in.} > t_f = 0.570 \text{ in.} \quad \textbf{n.g.}$ |
|  |  |
| Therefore, a bearing plate is required. | Therefore, a bearing plate is required. |

Note: The designer may assume a bearing width narrower than the beam flange to justify a thinner flange. In this case, the bearing width is constrained by the lower bound concrete bearing strength and the upper bound 0.570 in. flange thickness.

5.43 in. ≤ bearing width ≤ 6.56 in.

**Solution B:**

*Bearing Length*

From Solution A, with $l_b = 10$ in., the web local yielding and web local crippling strengths for the beam are adequate.

*Bearing Plate Design*

The required bearing plate width is determined using AISC *Specification* Equation J8-1 as follows:

---

# IID-18

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.65$ | $\Omega_c = 2.31$ |
|  |  |
| $A_1 \, req = \frac{R_u}{\phi_c 0.85f_c'}$ | $A_1 \, req = \frac{R_a \Omega_c}{0.85f_c'}$ |
|  |  |
| $= \frac{90.0 \text{ kips}}{0.65(0.85)(3 \text{ ksi})}$ | $= \frac{(60.0 \text{ kips})(2.31)}{0.85(3 \text{ ksi})}$ |
| $= 54.3 \text{ in.}^2$ | $= 54.4 \text{ in.}^2$ |
|  |  |
| $B_{req} = \frac{A_1 \, req}{l_b}$ | $B_{req} = \frac{A_1 \, req}{l_b}$ |
|  |  |
| $= \frac{54.3 \text{ in.}^2}{10.0 \text{ in.}}$ | $= \frac{54.4 \text{ in.}^2}{10.0 \text{ in.}}$ |
| $= 5.43$ in. | $= 5.44$ in. |
|  |  |
| Use $B = 8$ in. (selected as the least whole-inch dimension that exceeds $b_f$). | Use $B = 8$ in. (selected as the least whole-inch dimension that exceeds $b_f$). |

From AISC *Manual* Part 14, the bearing plate cantilever dimension is determined as follows:

$$n = \frac{B}{2} - k_{des}$$ (*Manual* Eq. 14-1)
$$= \frac{8 \text{ in.}}{2} - 0.972 \text{ in.}$$
$$= 3.03 \text{ in.}$$

The required thickness of the base plate is determined using the available flexural strength equation previously derived for the required beam flange thickness.

| LRFD | ASD |
|------|-----|
| $t_{min} = \sqrt{\frac{2R_u n^2}{\phi F_y Bl_b}}$ | $t_{min} = \sqrt{\frac{\Omega 2R_a n^2}{F_y Bl_b}}$ |
|  |  |
| $= \sqrt{\frac{2(90.0 \text{ kips})(3.03 \text{ in.})^2}{0.90(50 \text{ ksi})(8 \text{ in.})(10 \text{ in.})}}$ | $= \sqrt{\frac{1.67(2)(60.0 \text{ kips})(3.03 \text{ in.})^2}{(50 \text{ ksi})(8 \text{ in.})(10 \text{ in.})}}$ |
|  |  |
| $= 0.678$ in. | $= 0.678$ in. |
|  |  |
| Use PL¾ in.×10 in.×0 ft 8 in. | Use PL¾ in.×10 in.×0 ft 8 in. |

Note: The calculations for $t_{min}$ are conservative. Taking the strength of the beam flange into consideration results in a thinner required bearing plate or no bearing plate at all.

**Solution C:**

From Solution A, with $l_b = 6½$ in., the web local yielding and web local crippling strengths for the beam are adequate.

*Bearing Plate Design*

Try $B = 8$ in.

---

# IID-24

The strength of the bolt group is determined by summing the strength of the individual fasteners as follows:

| LRFD | ASD |
|------|-----|
| $\phi R_n = (1 \text{ bolt})(30.9 \text{ kips/bolt})$ | $\frac{R_n}{\Omega} = (1 \text{ bolt})(20.6 \text{ kips/bolt})$ |
| $+(1 \text{ bolt})(22.9 \text{ kips/bolt})$ | $+(1 \text{ bolt})(15.3 \text{ kips/bolt})$ |
| $+(4 \text{ bolts})(35.8 \text{ kips/bolt})$ | $+(4 \text{ bolts})(23.9 \text{ kips/bolt})$ |
| $= 197 \text{ kips} > 90.0 \text{ kips} \quad \textbf{o.k.}$ | $= 132 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ |

*Tensile Strength of the Angles*

From AISC *Specification* Section J4.1(a), the available tensile yielding strength of the angles is determined as follows:

$$P_n = F_y A_g$$ (*Spec.* Eq. J4-1)
$$= (50 \text{ ksi})\left(3.56 \text{ in.}^2\right)$$
$$= 178 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi P_n = 0.90(178 \text{ kips})$ | $\frac{P_n}{\Omega} = \frac{178 \text{ kips}}{1.67}$ |
| $= 160 \text{ kips} > 90.0 \text{ kips} \quad \textbf{o.k.}$ | $= 107 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.1(b), the available tensile rupture strength of the angles is determined as follows. The shear lag factor, $U$, is determined using AISC *Specification* Table D3.1, Case 2.

$$U = 1 - \frac{\bar{x}}{l}$$
$$= 1 - \frac{0.860 \text{ in.}}{15.0 \text{ in.}}$$
$$= 0.943$$

$$A_e = A_n U$$ (*Spec.* Eq. D3-1)
$$= \left[A_g - (2 \text{ angles})\left(d_h + \frac{1}{16} \text{ in.}\right)t\right]U$$
$$= \left[3.56 \text{ in.}^2 - (2 \text{ angles})\left(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\left(\frac{5}{16} \text{ in.}\right)\right](0.943)$$
$$= 2.84 \text{ in.}^2$$

$$P_n = F_u A_e$$ (*Spec.* Eq. J4-2)
$$= (65 \text{ ksi})\left(2.84 \text{ in.}^2\right)$$
$$= 185 \text{ kips}$$

---

# IID-25

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi P_n = 0.75(185 \text{ kips})$ | $\frac{P_n}{\Omega} = \frac{185 \text{ kips}}{2.00}$ |
| $= 139 \text{ kips} > 90.0 \text{ kips} \quad \textbf{o.k.}$ | $= 92.5 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture Strength of the Angles*

The available strength for the limit state of block shear rupture of the angles is determined as follows:

$$R_n = 0.60F_u A_{nv} + U_{bs} F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs} F_u A_{nt}$$ (*Spec.* Eq. J4-5)

where

$$A_{gv} = (2 \text{ angles})\left[L_{ev} + (n-1)s\right]t$$
$$= (2 \text{ angles})\left[1\frac{1}{2} \text{ in.} + (6-1)(3 \text{ in.})\right]\left(\frac{5}{16} \text{ in.}\right)$$
$$= 10.3 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (2 \text{ angles})\left(n - 0.5\right)\left(d_h + \frac{1}{16} \text{ in.}\right)t$$
$$= 10.3 \text{ in.}^2 - (2 \text{ angles})\left(6 - 0.5\right)\left(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\left(\frac{5}{16} \text{ in.}\right)$$
$$= 7.29 \text{ in.}^2$$

$$A_{nt} = (2 \text{ angles})\left[L_{eh} - 0.5\left(d_h + \frac{1}{16} \text{ in.}\right)\right]t$$
$$= (2 \text{ angles})\left[1\frac{1}{4} \text{ in.} - 0.5\left(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right]\left(\frac{5}{16} \text{ in.}\right)$$
$$= 0.508 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_n = 0.60(65 \text{ ksi})\left(7.29 \text{ in.}^2\right) + 1.0(65 \text{ ksi})\left(0.508 \text{ in.}^2\right) \leq 0.60(50 \text{ ksi})\left(10.3 \text{ in.}^2\right) + 1.0(65 \text{ ksi})\left(0.508 \text{ in.}^2\right)$$
$$= 317 \text{ kips} < 342 \text{ kips}$$

Therefore:
$$R_n = 317 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(317 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{317 \text{ kips}}{2.00}$ |
| $= 238 \text{ kips} > 90.0 \text{ kips} \quad \textbf{o.k.}$ | $= 159 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ |

*Tensile Strength of the Plate*

From AISC *Specification* Section J4.1(a), the available tensile yielding strength of the plate is determined as follows. By inspection, the Whitmore section, as defined in AISC *Manual* Figure 9-1, includes the entire width of the ½ in. plate.

---

# IID-26

$$A_g = bt$$
$$= (6 \text{ in.})\left(\frac{1}{2} \text{ in.}\right)$$
$$= 3.00 \text{ in.}^2$$

$$R_n = F_y A_g$$ (*Spec.* Eq. J4-1)
$$= (50 \text{ ksi})\left(3.00 \text{ in.}^2\right)$$
$$= 150 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi R_n = 0.90(150 \text{ kips})$ | $\frac{P_n}{\Omega} = \frac{150 \text{ kips}}{1.67}$ |
| $= 135 \text{ kips} > 90.0 \text{ kips} \quad \textbf{o.k.}$ | $= 89.8 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.1(b), the available tensile rupture strength of the plate is determined as follows:

$$A_n = A_g - \left(d_h + \frac{1}{16} \text{ in.}\right)t$$
$$= 3.00 \text{ in.}^2 - \left(\frac{15}{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\left(\frac{1}{2} \text{ in.}\right)$$
$$= 2.50 \text{ in.}^2$$

AISC *Specification* Table D3.1, Case 1, applies in this case because tension load is transmitted directly to the cross-sectional element by fasteners; therefore, $U = 1.0$.

$$A_e = A_n U$$ (*Spec.* Eq. D3-1)
$$= \left(2.50 \text{ in.}^2\right)(1.0)$$
$$= 2.50 \text{ in.}^2$$

$$R_n = F_u A_e$$ (*Spec.* Eq. J4-2)
$$= (65 \text{ ksi})\left(2.50 \text{ in.}^2\right)$$
$$= 163 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(163 \text{ kips})$ | $\frac{P_n}{\Omega} = \frac{163 \text{ kips}}{2.00}$ |
| $= 122 \text{ kips} > 90.0 \text{ kips} \quad \textbf{o.k.}$ | $= 81.5 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture Strength of the Plate*

The available strength for the limit state of block shear rupture of the plate is determined as follows.

$$R_n = 0.60F_u A_{nv} + U_{bs} F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs} F_u A_{nt}$$ (*Spec.* Eq. J4-5)

---

# IID-27

where

$$A_{gv} = \left[L_{ev} + (n-1)s\right]t$$
$$= \left[1\frac{1}{2} \text{ in.} + (6-1)(3 \text{ in.})\right]\left(\frac{1}{2} \text{ in.}\right)$$
$$= 8.25 \text{ in.}^2$$

$$A_{nv} = A_{gv} - \left(n - 0.5\right)\left(d_h + \frac{1}{16} \text{ in.}\right)t$$
$$= 8.25 \text{ in.}^2 - \left(6 - 0.5\right)\left(\frac{15}{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\left(\frac{1}{2} \text{ in.}\right)$$
$$= 5.50 \text{ in.}^2$$

$$A_{nt} = \left[L_{eh} - 0.5\left(d_h + \frac{1}{16} \text{ in.}\right)\right]t$$
$$= \left[3 \text{ in.} - 0.5\left(\frac{15}{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right]\left(\frac{1}{2} \text{ in.}\right)$$
$$= 1.25 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_n = 0.60(65 \text{ ksi})\left(5.50 \text{ in.}^2\right) + 1.0(65 \text{ ksi})\left(1.25 \text{ in.}^2\right) \leq 0.60(50 \text{ ksi})\left(8.25 \text{ in.}^2\right) + 1.0(65 \text{ ksi})\left(1.25 \text{ in.}^2\right)$$
$$= 296 \text{ kips} < 329 \text{ kips}$$

Therefore:
$$R_n = 296 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(296 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{296 \text{ kips}}{2.00}$ |
| $= 222 \text{ kips} > 90.0 \text{ kips} \quad \textbf{o.k.}$ | $= 148 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ |

*Plate-to-Beam Weld*

The applied load is perpendicular to the weld length ($\theta = 90°$), therefore the directional strength factor is determined from AISC *Specification* Equation J2-5. This increase factor due to directional strength is incorporated into the weld strength calculation.

$$k_{dir} = 1.0 + 0.50\sin^{1.5}\theta$$ (*Spec.* Eq. J2-5)
$$= 1.0 + 0.50\sin^{1.5}(90°)$$
$$= 1.50$$

The required fillet weld size is determined using AISC *Manual* Equation 8-2a or 8-2b, as follows:

---

# IID-28

| LRFD | ASD |
|------|-----|
| $D_{req} = \frac{P_u}{nk_{dir}(1.392 \text{ kip/in.})l}$ | $D_{req} = \frac{P_a}{nk_{dir}(0.928 \text{ kip/in.})l}$ |
|  |  |
| $= \frac{90.0 \text{ kips}}{(2 \text{ welds})(1.50)(1.392 \text{ kip/in.})(6 \text{ in.})}$ | $= \frac{60.0 \text{ kips}}{(2 \text{ welds})(1.50)(0.928 \text{ kip/in.})(6 \text{ in.})}$ |
| $= 3.59$ | $= 3.59$ |
|  |  |
| Use ¼ in. fillet welds on each side of the plate. | Use ¼ in. fillet welds on each side of the plate. |

From AISC *Manual* Table J2.4, the minimum fillet weld size is:

$$w_{min} = \frac{3}{16} \text{ in.} < \frac{1}{4} \text{ in.} \quad \textbf{o.k.}$$

*Beam Flange Base Metal Check*

The minimum flange thickness to match the required shear rupture strength of the welds is determined as follows:

$$t_{min} = \frac{3.09D}{F_u}$$ (*Manual* Eq. 9-6)
$$= \frac{3.09(3.59)}{65 \text{ ksi}}$$
$$= 0.171 \text{ in.} < 0.345 \text{ in.} \quad \textbf{o.k.}$$

*Beam Concentrated Forces Check*

From AISC *Specification* Section J10.2, the beam web is checked for the limit state of web local yielding assuming the connection is at a distance from the member end greater than the depth of the member, $d$.

$$R_n = F_{yw}t_w\left(5k_{des} + l_b\right)$$ (*Spec.* Eq. J10-2)
$$= (50 \text{ ksi})(0.250 \text{ in.})\left[5(0.747 \text{ in.}) + 6 \text{ in.}\right]$$
$$= 122 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(122 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{122 \text{ kips}}{1.50}$ |
| $= 122 \text{ kips} > 90.0 \text{ kips} \quad \textbf{o.k.}$ | $= 81.3 \text{ kips} > 60.0 \text{ kips} \quad \textbf{o.k.}$ |

*Conclusion*

The connection is found to be adequate as given for the applied loads.

---
