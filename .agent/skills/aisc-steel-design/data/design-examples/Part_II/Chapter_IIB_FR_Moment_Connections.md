# Chapter IIB: FR Moment Connections

**AISC Specification v16.0 - Design Examples**
**Original PDF Pages**: 849-878 (30 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Fully Restrained (FR) Moment Connections

**Examples Included**: ['II.B-1~II.B-2: FR moment connection examples']

---

## Table of Contents

- [EXAMPLE II.B-1 BOLTED FLANGE-PLATED FR MOMENT CONNECTION (BEAM-TO-COLUMN FLANGE)](#example-iib-1-bolted-flange-plated-fr-moment-connection-(beam-to-column-flange))
- [EXAMPLE II.B-2 WELDED FLANGE-PLATED FR MOMENT CONNECTION (BEAM-TO-COLUMN FLANGE)](#example-iib-2-welded-flange-plated-fr-moment-connection-(beam-to-column-flange))
- [EXAMPLE II.B-3 DIRECTLY WELDED FLANGE FR MOMENT CONNECTION (BEAM-TO-COLUMN FLANGE)](#example-iib-3-directly-welded-flange-fr-moment-connection-(beam-to-column-flange))

---

# IIB-1

# Chapter IIB
# Fully Restrained (FR) Moment Connections

The design of fully restrained (FR) moment connections is covered in Part 11 of the AISC *Manual*.

---

# IIB-2

## EXAMPLE II.B-1 BOLTED FLANGE-PLATED FR MOMENT CONNECTION (BEAM-TO-COLUMN FLANGE)

**Given:**

Verify a bolted flange-plated FR moment connection between an ASTM A992/A992M W18×50 beam and an ASTM A992/A992M W14×99 column flange, as shown in Figure II.B-1-1, to transfer the following beam end reactions:

Vertical shear:
$V_D = 7$ kips
$V_L = 21$ kips

Strong-axis moment:
$M_D = 42$ kip-ft
$M_L = 126$ kip-ft

Use 70-ksi electrodes. The flange and web plates are ASTM A572/A572M Grade 50 material. Check the column for stiffening requirements.

![Connection diagram showing W14×99 column with W18×50 beam connected via flange plates. Left side shows elevation view with dimensions: 2" spacing, 3@3"=9" bolt pattern, 1½" edges. Includes (8) ⅞" dia. Group 120 bolts with thread condition N in standard holes, PL¾×7×1'-0½" flange plates top and bottom, (3) ⅞" dia. Group 120 bolts with thread condition N in standard holes for web connection, PL⅜×5×0'-9" web plate. Right side shows plan view with gage lines and bolt layout. Note indicates "Shim top or bottom as required."]

*Fig. II.B-1-1. Connection geometry for Example II.B-1.*

---

# IIB-3

**Solution:**

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Beam and column
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Plates
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W18×50
$d$ = 18.0 in.
$b_f$ = 7.50 in.
$t_f$ = 0.570 in.
$t_w$ = 0.355 in.
$S_x = 88.9$ in.$^3$

Column
W14×99
$d$ = 14.2 in.
$b_f$ = 14.6 in.
$t_f$ = 0.780 in.

From AISC *Specification* Table J3.3, the hole diameter for a ⅞-in.-diameter bolt with standard holes is:

$$d_h = \frac{15}{16} \text{ in.}$$

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(7 \text{ kips}) + 1.6(21 \text{ kips})$ | $R_a = 7 \text{ kips} + 21 \text{ kips}$ |
| $= 42.0$ kips | $= 28.0$ kips |
|  |  |
| $M_u = 1.2(42 \text{ kip-ft}) + 1.6(126 \text{ kip-ft})$ | $M_a = 42 \text{ kip-ft} + 126 \text{ kip-ft}$ |
| $= 252$ kip-ft | $= 168$ kip-ft |

*Flexural Strength of Beam*

From AISC *Specification* Section F13.1, the available flexural strength of the beam is limited according to the limit state of tensile rupture of the tension flange. The gross area of the flange is determined in accordance with AISC *Specification* Section B4.3a.

$$A_{fg} = b_f t_f$$
$$= (7.50 \text{ in.})(0.570 \text{ in.})$$
$$= 4.28 \text{ in.}^2$$

---

# IIB-4

The net area of the flange is determined in accordance with AISC *Specification* Section B4.3b.

$$A_{fn} = A_{fg} - (2 \text{ bolts})\left(d_h + \frac{1}{16} \text{ in.}\right)t_f$$
$$= 4.28 \text{ in.}^2 - (2 \text{ bolts})\left(\frac{15}{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)(0.570 \text{ in.})$$
$$= 3.14 \text{ in.}^2$$

$$\frac{F_y}{F_u} = \frac{50 \text{ ksi}}{65 \text{ ksi}}$$
$$= 0.769 < 0.8; \text{ therefore, } Y_t = 1.0$$

$$F_u A_{fn} = (65 \text{ ksi})\left(3.14 \text{ in.}^2\right)$$
$$= 204 \text{ kips}$$

$$Y_t F_y A_{fg} = 1.0(50 \text{ ksi})\left(4.28 \text{ in.}^2\right)$$
$$= 214 \text{ kips} > 204 \text{ kips}$$

Therefore, the nominal flexural strength, $M_n$, at the location of the bolt holes in the tension flange is not greater than:

$$M_n = \frac{F_u A_{fn}}{A_{fg}}S_x$$ (*Spec.* Eq. F13-1)
$$= \left(\frac{204 \text{ kips}}{4.28 \text{ in.}^2}\right)\left(88.9 \text{ in.}^3\right)$$
$$= 4,240 \text{ kip-in. or } 353 \text{ kip-ft}$$

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
|  |  |
| $\phi_b M_n = 0.90(353 \text{ kip-ft})$ | $\frac{M_n}{\Omega_b} = \frac{353 \text{ kip-ft}}{1.67}$ |
| $= 318 \text{ kip-ft} > 252 \text{ kip-ft} \quad \textbf{o.k.}$ | $= 211 \text{ kip-ft} > 168 \text{ kip-ft} \quad \textbf{o.k.}$ |

Note: The available flexural strength of the beam may be less than that determined based on AISC *Specification* Equation F13-1. Other applicable provisions in AISC *Specification* Chapter F should be checked to possibly determine a lower value for the available flexural strength of the beam.

*Single-Plate Web Connection*

*Strength of the bolted connection*

From AISC *Specification* Section J3.7 Commentary, the strength of the bolt group is taken as the sum of the strengths of the individual fasteners, which may be taken as the lesser of the fastener shear strength per AISC *Specification* Section J3.7, the bearing strength at the bolt hole per AISC *Specification* Section J3.11, or the tearout strength at the bolt hole per AISC *Specification* Section J3.11.

From AISC *Manual* Table 7-1, the available shear strength per bolt for ⅞-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

---

# IIB-5

| LRFD | ASD |
|------|-----|
| $\phi r_n = 24.3$ kips/bolt | $\frac{r_n}{\Omega} = 16.2$ kips/bolt |

The available bearing strength of the plate per bolt is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration:

$$r_n = 2.4dt_p F_u$$ (*Spec.* Eq. J3-6a)
$$= 2.4\left(⅞ \text{ in.}\right)\left(⅜ \text{ in.}\right)(65 \text{ ksi})$$
$$= 51.2 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(51.2 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{51.2 \text{ kips/bolt}}{2.00}$ |
| $= 38.4$ kips/bolt | $= 25.6$ kips/bolt |

The available tearout strength of the plate at the interior bolts is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration.

$$l_c = s - d_h$$
$$= 3 \text{ in.} - \frac{15}{16} \text{ in.}$$
$$= 2.06 \text{ in.}$$

$$r_n = 1.2l_c t_p F_u$$ (*Spec.* Eq. J3-6c)
$$= 1.2(2.06 \text{ in.})\left(⅜ \text{ in.}\right)(65 \text{ ksi})$$
$$= 60.3 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(60.3 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{60.3 \text{ kips/bolt}}{2.00}$ |
| $= 45.2$ kips/bolt | $= 30.2$ kips/bolt |

Therefore, bolt shear controls over bearing or tearout at interior bolts.

The available tearout strength of the plate at the edge bolt is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration.

$$l_c = l_{ev} - 0.5\left(d_h\right)$$
$$= 1½ \text{ in.} - 0.5\left(\frac{15}{16} \text{ in.}\right)$$
$$= 1.03 \text{ in.}$$

$$r_n = 1.2l_c t_p F_u$$ (*Spec.* Eq. J3-6c)
$$= 1.2(1.03 \text{ in.})\left(⅜ \text{ in.}\right)(65 \text{ ksi})$$
$$= 30.1 \text{ kips/bolt}$$

---

# IIB-6

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(30.1 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{30.1 \text{ kips/bolt}}{2.00}$ |
| $= 22.6$ kips/bolt | $= 15.1$ kips/bolt |

The available bearing strength of the beam web per bolt is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration:

$$r_n = 2.4dt_w F_u$$ (*Spec.* Eq. J3-6a)
$$= 2.4\left(⅞ \text{ in.}\right)(0.355 \text{ in.})(65 \text{ ksi})$$
$$= 48.5 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(48.5 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{48.5 \text{ kips/bolt}}{2.00}$ |
| $= 36.4$ kips/bolt | $= 24.3$ kips/bolt |

Because there are no edge bolts in the beam web, all bolts are considered interior bolts to determine the available tearout strength. The available tearout strength of the beam web is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration.

$$l_c = s - d_h$$
$$= 3 \text{ in.} - \frac{15}{16} \text{ in.}$$
$$= 2.06 \text{ in.}$$

$$r_n = 1.2l_c t_w F_u$$ (*Spec.* Eq. J3-6c)
$$= 1.2(2.06 \text{ in.})(0.355 \text{ in.})(65 \text{ ksi})$$
$$= 57.0 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(57.0 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{57.0 \text{ kips/bolt}}{2.00}$ |
| $= 42.8$ kips/bolt | $= 28.5$ kips/bolt |

Therefore, tearout of the plate controls over bolt shear or bearing at the edge bolt. The other bolts are controlled by bolt shear.

The strength of the bolt group in the plate is determined by summing the strength of the individual fasteners as follows:

| LRFD | ASD |
|------|-----|
| $\phi R_n = (1 \text{ bolt})(22.6 \text{ kips/bolt})$ | $\frac{R_n}{\Omega} = (1 \text{ bolt})(15.1 \text{ kips/bolt})$ |
| $+ (2 \text{ bolts})(24.3 \text{ kips/bolt})$ | $+ (2 \text{ bolts})(16.2 \text{ kips/bolt})$ |
| $= 71.2 \text{ kips} > 42.0 \text{ kips} \quad \textbf{o.k.}$ | $= 47.5 \text{ kips} > 28.0 \text{ kips} \quad \textbf{o.k.}$ |

---

# IIB-7

*Shear strength of the web plate*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the plate is determined as follows:

$$A_{gv} = lt$$
$$= (9 \text{ in.})\left(⅜ \text{ in.}\right)$$
$$= 3.38 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})\left(3.38 \text{ in.}^2\right)$$
$$= 101 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(101 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{101 \text{ kips}}{1.50}$ |
| $= 101 \text{ kips} > 42.0 \text{ kips} \quad \textbf{o.k.}$ | $= 67.3 \text{ kips} > 28.0 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the plate is determined as follows:

$$A_{nv} = \left[l - n\left(d_h + \frac{1}{16} \text{ in.}\right)\right]t$$
$$= \left[9 \text{ in.} - (3 \text{ bolts})\left(\frac{15}{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right]\left(⅜ \text{ in.}\right)$$
$$= 2.25 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})\left(2.25 \text{ in.}^2\right)$$
$$= 87.8 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(87.8 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{87.8 \text{ kips}}{2.00}$ |
| $= 65.9 \text{ kips} > 42.0 \text{ kips} \quad \textbf{o.k.}$ | $= 43.9 \text{ kips} > 28.0 \text{ kips} \quad \textbf{o.k.}$ |

*Block shear rupture of the web plate*

The nominal strength for the limit state of block shear rupture is given by AISC *Specification* Section J4.3.

$$R_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$ (*Spec.* Eq. J4-5)

The available block shear rupture strength of the web plate is determined as follows, using AISC *Manual* Tables 9-3a, 9-3b, 9-3c, and AISC *Specification* Equation J4-5, with $n = 3$, $l_{eh} = 2$ in., $l_{ev} = 1½$ in., and $U_{bs} = 1.0$.

---

# IIB-8

| LRFD | ASD |
|------|-----|
| Tension rupture component from AISC *Manual* Table 9-3a: | Tension rupture component from AISC *Manual* Table 9-3a: |
|  |  |
| $\frac{\phi F_u A_{nt}}{t} = 73.1$ kip/in. | $\frac{F_u A_{nt}}{\Omega t} = 48.8$ kip/in. |
|  |  |
| Shear yielding component from AISC *Manual* Table 9-3b: | Shear yielding component from AISC *Manual* Table 9-3b: |
|  |  |
| $\frac{\phi 0.60F_y A_{gv}}{t} = 169$ kip/in. | $\frac{0.60F_y A_{gv}}{\Omega t} = 113$ kip/in. |
|  |  |
| Shear rupture component from AISC *Manual* Table 9-3c: | Shear rupture component from AISC *Manual* Table 9-3c: |
|  |  |
| $\frac{\phi 0.60F_u A_{nv}}{t} = 146$ kip/in. | $\frac{0.60F_u A_{nv}}{\Omega t} = 97.5$ kip/in. |
|  |  |
| The design block shear rupture strength is: | The allowable block shear rupture strength is: |
|  |  |
| $\phi R_n = \phi 0.60F_u A_{nv} + \phi U_{bs}F_u A_{nt}$ | $\frac{R_n}{\Omega} = \frac{0.60F_u A_{nv}}{\Omega} + \frac{U_{bs}F_u A_{nt}}{\Omega}$ |
| $\leq \phi 0.60F_y A_{gv} + \phi U_{bs}F_u A_{nt}$ | $\leq \frac{0.60F_y A_{gv}}{\Omega} + \frac{U_{bs}F_u A_{nt}}{\Omega}$ |
| $= (⅜ \text{ in.})\left[146 \text{ kip/in.} + (1.0)(73.1 \text{ kip/in.})\right]$ | $= (⅜ \text{ in.})\left[97.5 \text{ kip/in.} + (1.0)(48.8 \text{ kip/in.})\right]$ |
| $\leq (⅜ \text{ in.})\left[169 \text{ kip/in.} + (1.0)(73.1 \text{ kip/in.})\right]$ | $\leq (⅜ \text{ in.})\left[113 \text{ kip/in.} + (1.0)(48.8 \text{ kip/in.})\right]$ |
| $= 82.2 \text{ kips} < 90.8 \text{ kips}$ | $= 54.9 \text{ kips} < 60.7 \text{ kips}$ |
|  |  |
| Therefore: | Therefore: |
|  |  |
| $\phi R_n = 82.2 \text{ kips} > 42.0 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 54.9 \text{ kips} > 28.0 \text{ kips} \quad \textbf{o.k.}$ |

*Weld shear strength of the web plate to the column flange*

The available weld strength is determined using AISC *Manual* Equations 8-2a or 8-2b, with the assumption that the weld is in direct shear (the incidental moment in the web plate due to eccentricity is absorbed by the flange plates).

$$D = 4 \text{ (for a ¼ in. fillet weld)}$$

| LRFD | ASD |
|------|-----|
| $\phi R_n = (2 \text{ welds})(1.392 \text{ kip/in.})Dl$ | $\phi R_n = (2 \text{ welds})(0.928 \text{ kip/in.})Dl$ |
| $= (2 \text{ welds})(1.392 \text{ kip/in.})(4)(9 \text{ in.})$ | $= (2 \text{ welds})(0.928 \text{ kip/in.})(4)(9 \text{ in.})$ |
| $= 100 \text{ kips} > 42.0 \text{ kips} \quad \textbf{o.k.}$ | $= 66.8 \text{ kips} > 28.0 \text{ kips} \quad \textbf{o.k.}$ |

---

# IIB-9

*Column flange rupture strength at welds*

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the column flange is determined as follows:

$$A_{nv} = (2 \text{ welds})lt_f$$
$$= (2 \text{ welds})(9 \text{ in.})(0.780 \text{ in.})$$
$$= 14.0 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})\left(14.0 \text{ in.}^2\right)$$
$$= 546 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(546 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{546 \text{ kips}}{2.00}$ |
| $= 410 \text{ kips} > 42.0 \text{ kips} \quad \textbf{o.k.}$ | $= 273 \text{ kips} > 28.0 \text{ kips} \quad \textbf{o.k.}$ |

*Flange Plate Connection*

*Flange force*

The moment arm between flange forces, $d_m$, used for verifying the fastener strength is equal to the depth of the beam. This dimension represents the faying surface between the flange of the beam and the tension plate.

| LRFD | ASD |
|------|-----|
| $P_{uf} = \frac{M_u}{d_m}$ (from *Manual* Eq. 11-1) | $P_{af} = \frac{M_a}{d_m}$ (from *Manual* Eq. 11-1) |
|  |  |
| $= \frac{(252 \text{ kip-ft})(12 \text{ in./ft})}{18.0 \text{ in.}}$ | $= \frac{(168 \text{ kip-ft})(12 \text{ in./ft})}{18.0 \text{ in.}}$ |
| $= 168$ kips | $= 112$ kips |

*Strength of the bolted connection*

From AISC *Specification* Section J3.7 Commentary, the strength of the bolt group is the sum of the strengths of the individual fasteners, which may be taken as the lesser of the fastener shear strength per AISC *Specification* Section J3.7, the bearing strength at the bolt hole per AISC *Specification* Section J3.11, or the tearout strength at the bolt hole per AISC *Specification* Section J3.11.

From AISC *Manual* Table 7-1, the available shear strength per bolt for ⅞-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 24.3$ kips/bolt | $\frac{r_n}{\Omega} = 16.2$ kips/bolt |

The available bearing strength of the plate per bolt is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration:

---

# IIB-10

$$r_n = 2.4dt_p F_u$$ (*Spec.* Eq. J3-6a)
$$= 2.4\left(⅞ \text{ in.}\right)\left(¾ \text{ in.}\right)(65 \text{ ksi})$$
$$= 102 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(102 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{102 \text{ kips/bolt}}{2.00}$ |
| $= 76.5$ kips/bolt | $= 51.0$ kips/bolt |

The available tearout strength of the plate at the interior bolts is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration.

$$l_c = s - d_h$$
$$= 3 \text{ in.} - \frac{15}{16} \text{ in.}$$
$$= 2.06 \text{ in.}$$

$$r_n = 1.2l_c t_p F_u$$ (*Spec.* Eq. J3-6c)
$$= 1.2(2.06 \text{ in.})\left(¾ \text{ in.}\right)(65 \text{ ksi})$$
$$= 121 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(121 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{121 \text{ kips/bolt}}{2.00}$ |
| $= 90.8$ kips/bolt | $= 60.5$ kips/bolt |

Therefore, bolt shear controls over bearing or tearout of the plate at interior bolts.

The available tearout strength of the plate at the edge bolt is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration.

$$l_c = l_{ev} - 0.5\left(d_h\right)$$
$$= 1½ \text{ in.} - 0.5\left(\frac{15}{16} \text{ in.}\right)$$
$$= 1.03 \text{ in.}$$

$$r_n = 1.2l_c t_p F_u$$ (*Spec.* Eq. J3-6c)
$$= 1.2(1.03 \text{ in.})\left(¾ \text{ in.}\right)(65 \text{ ksi})$$
$$= 60.3 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(60.3 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{60.3 \text{ kips/bolt}}{2.00}$ |
| $= 45.2$ kips/bolt | $= 30.2$ kips/bolt |

---

# IIB-11

Therefore, bolt shear controls over bearing or tearout of the plate at edge bolts.

The available bearing strength of the flange per bolt is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration:

$$r_n = 2.4dt_b F_u$$ (*Spec.* Eq. J3-6a)
$$= 2.4\left(⅞ \text{ in.}\right)(0.570 \text{ in.})(65 \text{ ksi})$$
$$= 77.8 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(77.8 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{77.8 \text{ kips/bolt}}{2.00}$ |
| $= 58.4$ kips/bolt | $= 38.9$ kips/bolt |

The available tearout strength of the flange at the interior bolts is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration.

$$l_c = s - d_h$$
$$= 3 \text{ in.} - \frac{15}{16} \text{ in.}$$
$$= 2.06 \text{ in.}$$

$$r_n = 1.2l_c t_b F_u$$ (*Spec.* Eq. J3-6c)
$$= 1.2(2.06 \text{ in.})(0.570 \text{ in.})(65 \text{ ksi})$$
$$= 91.6 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(91.6 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{91.6 \text{ kips/bolt}}{2.00}$ |
| $= 68.7$ kips/bolt | $= 45.8$ kips/bolt |

Therefore, bolt shear controls over bearing or tearout of the flange at interior bolts.

The available tearout strength of the flange at the edge bolt is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration.

$$l_c = l_{ev} - 0.5\left(d_h\right)$$
$$= 1½ \text{ in.} - 0.5\left(\frac{15}{16} \text{ in.}\right)$$
$$= 1.03 \text{ in.}$$

$$r_n = 1.2l_c t_b F_u$$ (*Spec.* Eq. J3-6c)
$$= 1.2(1.03 \text{ in.})(0.570 \text{ in.})(65 \text{ ksi})$$
$$= 45.8 \text{ kips/bolt}$$

---

# IIB-12

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(45.8 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{45.8 \text{ kips/bolt}}{2.00}$ |
| $= 34.4$ kips/bolt | $= 22.9$ kips/bolt |

Therefore, bolt shear controls over bearing or tearout of the flange at edge bolts.

The strength of the bolt group in the beam web is determined by summing the strength of the individual fasteners as follows:

| LRFD | ASD |
|------|-----|
| $\phi R_n = (8 \text{ bolts})(24.3 \text{ kips/bolt})$ | $\frac{R_n}{\Omega} = (8 \text{ bolts})(16.2 \text{ kips/bolt})$ |
| $= 194 \text{ kips} > 168 \text{ kips} \quad \textbf{o.k.}$ | $= 130 \text{ kips} > 112 \text{kips} \quad \textbf{o.k.}$ |

*Tensile strength of the flange plate*

The moment arm between flange forces, $d_m$, used for verifying the tensile strength of the flange plate is equal to the depth of the beam plus one plate thickness. This represents the distance between the centerlines of the flange plates at the top and bottom of the beam. From AISC *Manual* Equation 11-1, the flange force is:

| LRFD | ASD |
|------|-----|
| $P_{uf} = \frac{M_u}{d_m}$ (from *Manual* Eq. 11-1) | $P_{af} = \frac{M_a}{d_m}$ (from *Manual* Eq. 11-1) |
|  |  |
| $= \frac{(252 \text{ kip-ft})(12 \text{ in./ft})}{18.0 \text{ in.} + ¾ \text{ in.}}$ | $= \frac{(168 \text{ kip-ft})(12 \text{ in./ft})}{18.0 \text{ in.} + ¾ \text{ in.}}$ |
| $= 161$ kips | $= 108$ kips |

From AISC *Specification* Section J4.1(a), the available tensile yield strength of the flange plate is determined as follows:

$$A_g = bt$$
$$= (7 \text{ in.})\left(¾ \text{ in.}\right)$$
$$= 5.25 \text{ in.}^2$$

$$R_n = F_y A_g$$ (*Spec.* Eq. J4-1)
$$= (50 \text{ ksi})\left(5.25 \text{ in.}^2\right)$$
$$= 263 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi R_n = 0.90(263 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{263 \text{ kips}}{1.67}$ |
| $= 237 \text{ kips} > 161 \text{ kips} \quad \textbf{o.k.}$ | $= 157 \text{ kips} > 108 \text{ kips} \quad \textbf{o.k.}$ |

---

# IIB-13

From AISC *Specification* Section J4.1(b), the available tensile rupture strength of the flange plate is determined as follows:

$$A_n = \left[b - n\left(d_h + \frac{1}{16}\text{ in.}\right)\right]t$$
$$= \left[7 \text{ in.} - (2 \text{ bolts})\left(\frac{15}{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right]\left(¾ \text{ in.}\right)$$
$$= 3.75 \text{ in.}^2$$

Table D3.1, Case 1, applies in this case because the tension load is transmitted directly to the cross-sectional element by fasteners; therefore, $U = 1.0$.

$$A_e = A_n U$$ (*Spec.* Eq. D3-1)
$$= \left(3.75 \text{ in.}^2\right)(1.0)$$
$$= 3.75 \text{ in.}^2$$

$$R_n = F_u A_e$$ (*Spec.* Eq. J4-2)
$$= (65 \text{ ksi})\left(3.75 \text{ in.}^2\right)$$
$$= 244 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(244 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{244 \text{ kips}}{2.00}$ |
| $= 183 \text{ kips} > 161 \text{ kips} \quad \textbf{o.k.}$ | $= 122 \text{ kips} > 108 \text{ kips} \quad \textbf{o.k.}$ |

*Block shear rupture of the flange plate*

There are three cases for which block shear rupture of the flange plate must be checked. Case 1, as shown in Figure II.B-1-2(a), is the tearout of the block between the two rows of bolt holes in the flange plate; for this case $l_{eh} = 1½$ in. and $l_{ev} = 1½$ in. Case 2, as shown in Figure II.B-1-2(b), involves the tearout of the block between the two rows of the holes in the flange plate. AISC *Manual* Tables 9-3a, 9-3b, and 9-3c may be adapted for this calculation by considering the 4 in. width to be comprised of two, 2 in. sections, where $l_{eh} = 2$ in. and $l_{ev} = 1½$ in. Case 1 is more critical than the Case 2 because $l_{eh}$ is smaller. Case 3, as shown in Figure II.B-1-2(c), involves a shear failure through one row of bolts and a tensile failure through the two bolts closest to the column. Therefore, Case 1 and Case 3 will be verified.

![Three diagrams showing different block shear rupture cases. (a) Case 1 shows 3@3" = 9" bolt spacing with 1½" edge distances and 4" width. (b) Case 2 shows similar layout with hatched failure region. (c) Case 3 shows 3@3" = 9" with 1½" spacing and hatched L-shaped failure region.]

*Fig. II.B-1-2. Three cases for block shear rupture.*

---

# IIB-14

*Flange plate block shear rupture—Case 1*

The nominal strength for the limit state of block shear rupture is given by AISC *Specification* Section J4.3.

$$R_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$ (*Spec.* Eq. J4-5)

The available block shear rupture strength of the flange plate is determined as follows, using AISC *Manual* Tables 9-3a, 9-3b, 9-3c, and AISC *Specification* Equation J4-5, with $n = 4$, $l_{eh} = l_{ev} = 1½$ in., and $U_{bs} = 1.0$.

| LRFD | ASD |
|------|-----|
| Tension rupture component from AISC *Manual* Table 9-3a: | Tension rupture component from AISC *Manual* Table 9-3a: |
|  |  |
| $\frac{\phi F_u A_{nt}}{t} = 48.8$ kip/in. | $\frac{F_u A_{nt}}{\Omega t} = 32.5$ kip/in. |
|  |  |
| Shear yielding component from AISC *Manual* Table 9-3b: | Shear yielding component from AISC *Manual* Table 9-3b: |
|  |  |
| $\frac{\phi 0.60F_y A_{gv}}{t} = 236$ kip/in. | $\frac{0.60F_y A_{gv}}{\Omega t} = 158$ kip/in. |
|  |  |
| Shear rupture component from AISC *Manual* Table 9-3c: | Shear rupture component from AISC *Manual* Table 9-3c: |
|  |  |
| $\frac{\phi 0.60F_u A_{nv}}{t} = 205$ kip/in. | $\frac{0.60F_u A_{nv}}{\Omega t} = 137$ kip/in. |
|  |  |
| The design block shear rupture strength is: | The allowable block shear rupture strength is: |
|  |  |
| $\phi R_n = \phi 0.60F_u A_{nv} + \phi U_{bs}F_u A_{nt}$ | $\frac{R_n}{\Omega} = \frac{0.60F_u A_{nv}}{\Omega} + \frac{U_{bs}F_u A_{nt}}{\Omega}$ |
| $\leq \phi 0.60F_y A_{gv} + \phi U_{bs}F_u A_{nt}$ | $\leq \frac{0.60F_y A_{gv}}{\Omega} + \frac{U_{bs}F_u A_{nt}}{\Omega}$ |
| $= (2 \text{ planes})\left(¾ \text{ in.}\right)\left[\begin{matrix}205 \text{ kip/in.} \\ + 1.0(48.8 \text{ kip/in.})\end{matrix}\right]$ | $= (2 \text{ planes})\left(¾ \text{ in.}\right)\left[\begin{matrix}137 \text{ kip/in.} \\ + 1.0(32.5 \text{ kip/in.})\end{matrix}\right]$ |
| $\leq (2 \text{ planes})\left(¾ \text{ in.}\right)\left[\begin{matrix}236 \text{ kip/in.} \\ + 1.0(48.8 \text{ kip/in.})\end{matrix}\right]$ | $\leq (2 \text{ planes})\left(¾ \text{ in.}\right)\left[\begin{matrix}158 \text{ kip/in.} \\ + 1.0(32.5 \text{ kip/in.})\end{matrix}\right]$ |
| $= 381 \text{ kips} < 427 \text{ kips}$ | $= 254 \text{ kips} < 286 \text{ kips}$ |
|  |  |
| Therefore: | Therefore: |
|  |  |
| $\phi R_n = 381 \text{ kips} > 161 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 254 \text{ kips} > 108 \text{ kips} \quad \textbf{o.k.}$ |

*Flange plate block shear rupture—Case 3*

Because AISC *Manual* Table 9-3a does not include a large enough edge distance, the nominal strength for the limit state of block shear rupture is calculated by directly applying the provisions of AISC *Specification* Section J4.3.

---

# IIB-15

$$R_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$ (*Spec.* Eq. J4-5)

where

$$A_{gv} = \left[\left(n - 1\right)s + l_{ev}\right]t$$
$$= \left[\left(4 - 1\right)(3 \text{ in.}) + 1½ \text{ in.}\right]\left(¾ \text{ in.}\right)$$
$$= 7.88 \text{ in.}^2$$

$$A_{nv} = A_{gv} - \left(n - 0.5\right)\left(d_h + \frac{1}{16}\text{ in.}\right)t$$
$$= 7.88 \text{ in.}^2 - \left(4 - 0.5\right)\left(\frac{15}{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\left(¾ \text{ in.}\right)$$
$$= 5.26 \text{ in.}^2$$

$$A_{nt} = \left[gage + l_{eh} - 1.5\left(d_h + \frac{1}{16} \text{ in.}\right)\right]t$$
$$= \left[4 \text{ in.} + 1½ \text{ in.} - 1.5\left(\frac{15}{16} \text{ in.} + \frac{1}{16} \text{ in.}\right)\right]\left(¾ \text{ in.}\right)$$
$$= 3.00 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_n = 0.60(65 \text{ ksi})\left(5.26\text{ in.}^2\right) + 1.0(65 \text{ ksi})\left(3.00 \text{ in.}^2\right) \leq 0.60(50 \text{ ksi})\left(7.88 \text{ in.}^2\right) + 1.0(65 \text{ ksi})\left(3.00 \text{ in.}^2\right)$$
$$= 400 \text{ kips} < 431 \text{ kips}$$

Therefore:

$$R_n = 400 \text{ kips}$$

From AISC *Specification* Section J4.3, the available strength for the limit state of block shear rupture of the plate is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(400 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{400 \text{ kips}}{2.00}$ |
| $= 300 \text{ kips} > 161 \text{ kips} \quad \textbf{o.k.}$ | $= 200 \text{ kips} > 108 \text{ kips} \quad \textbf{o.k.}$ |

*Beam flange block shear rupture*

The nominal strength for the limit state of block shear rupture is given by AISC *Specification* Section J4.3.
$$R_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$ (*Spec.* Eq. J4-5)

The available block shear rupture strength of the beam flange involves the tearout of the two blocks outside the two rows of bolt holes in the flanges. Conservatively use the flange forces that were found for the fastener checks. From AISC *Manual* Tables 9-3a, 9-3b, 9-3c, and AISC *Specification* Equation J4-5, with $n = 4$, $l_{eh} = 1¾$ in., $l_{ev} = 1¼$ in. (reduced ¼ in. to account for beam underrun), and $U_{bs} = 1.0$:

---

# IIB-16

| LRFD | ASD |
|------|-----|
| Tension rupture component from AISC *Manual* Table 9-3a: | Tension rupture component from AISC *Manual* Table 9-3a: |
|  |  |
| $\frac{\phi F_u A_{nt}}{t} = 60.9$ kip/in. | $\frac{F_u A_{nt}}{\Omega t} = 40.6$ kip/in. |
|  |  |
| Shear yielding component from AISC *Manual* Table 9-3b: | Shear yielding component from AISC *Manual* Table 9-3b: |
|  |  |
| $\frac{\phi 0.60F_y A_{gv}}{t} = 231$ kip/in. | $\frac{0.60F_y A_{gv}}{\Omega t} = 154$ kip/in. |
|  |  |
| Shear rupture component from AISC *Manual* Table 9-3c: | Shear rupture component from AISC *Manual* Table 9-3c: |
|  |  |
| $\frac{\phi 0.60F_u A_{nv}}{t} = 197$ kip/in. | $\frac{0.60F_u A_{nv}}{\Omega t} = 132$ kip/in. |
|  |  |
| The design block shear rupture strength is: | The allowable block shear rupture strength is: |
|  |  |
| $\phi R_n = \phi 0.60F_u A_{nv} + \phi U_{bs}F_u A_{nt}$ | $\frac{R_n}{\Omega} = \frac{0.60F_u A_{nv}}{\Omega} + \frac{U_{bs}F_u A_{nt}}{\Omega}$ |
| $\leq \phi 0.60F_y A_{gv} + \phi U_{bs}F_u A_{nt}$ | $\leq \frac{0.60F_y A_{gv}}{\Omega} + \frac{U_{bs}F_u A_{nt}}{\Omega}$ |
| $= (2 \text{ planes})(0.570 \text{ in.})\left[\begin{matrix}197 \text{ kip/in.} \\ + (1.0)(60.9 \text{ kip/in.})\end{matrix}\right]$ | $= (2 \text{ planes})(0.570 \text{ in.})\left[\begin{matrix}132 \text{ kip/in.} \\ + (1.0)(40.6 \text{ kip/in.})\end{matrix}\right]$ |
| $\leq (2 \text{ planes})(0.570 \text{ in.})\left[\begin{matrix}231 \text{ kip/in.} \\ + (1.0)(60.9 \text{ kip/in.})\end{matrix}\right]$ | $\leq (2 \text{ planes})(0.570 \text{ in.})\left[\begin{matrix}154 \text{ kip/in.} \\ + (1.0)(40.6 \text{ kip/in.})\end{matrix}\right]$ |
| $= 294 \text{ kips} < 333 \text{ kips}$ | $= 197 \text{ kips} < 222 \text{ kips}$ |
|  |  |
| Therefore: | Therefore: |
|  |  |
| $\phi R_n = 294 \text{ kips} > 168 \text{ kips} \quad \textbf{o.k.}$ | $\frac{R_n}{\Omega} = 197 \text{ kips} > 112 \text{ kips} \quad \textbf{o.k.}$ |

*Fillet weld to supporting column flange*

The applied load is perpendicular to the weld length ($\theta = 90°$); therefore, the directional strength factor is determined from AISC *Specification* Equation J2-5. This increase factor due to directional strength is incorporated into the weld strength calculation.

$$k_{de} = 1.0 + 0.50\sin^{1.5}\theta$$ (*Spec.* Eq. J2-5)
$$= 1.0 + 0.50\sin^{1.5}(90°)$$
$$= 1.50$$

The required fillet weld size is determined using AISC *Manual* Equations 8-2a or 8-2b as follows:

---

# IIB-17

| LRFD | ASD |
|------|-----|
| $D_{min} = \frac{P_{uf}}{nk_{de}(1.392 \text{ kip/in.})l}$ | $D_{min} = \frac{P_{af}}{nk_{de}(0.928 \text{ kip/in.})l}$ |
|  |  |
| $= \frac{161 \text{ kips}}{(2 \text{ welds})(1.50)(1.392 \text{ kip/in.})(7 \text{ in.})}$ | $= \frac{108 \text{ kips}}{(2 \text{ welds})(1.50)(0.928 \text{ kip/in.})(7 \text{ in.})}$ |
| $= 5.51$ sixteenths of an inch | $= 5.54$ sixteenths of an inch |

Use a ⅜ in. fillet weld on both sides of the flange plate.

*Compression Flange Plate and Connection*

From AISC *Specification* Section J4.4, the available strength of the flange plate in compression is determined as follows:

$$K = 0.65, \text{ from AISC } Specification \text{ Commentary Table C-A-7.1}$$
$$L = 3.00 \text{ in. (the distance between adjacent bolt holes)}$$

$$r = \sqrt{\frac{I}{A}}$$
$$= \sqrt{\frac{(7 \text{ in.})\left(¾ \text{ in.}\right)^3/12}{(7 \text{ in.})\left(¾ \text{ in.}\right)}}$$
$$= 0.217 \text{ in.}$$

$$\frac{L_c}{r} = \frac{KL}{r}$$
$$= \frac{0.65(3.00 \text{ in.})}{0.217 \text{ in.}}$$
$$= 8.99$$

Because $L_c/r \leq 25$:

$$P_n = F_y A_g$$ (*Spec.* Eq. J4-6)
$$= (50 \text{ ksi})(7 \text{ in.})\left(¾ \text{ in.}\right)$$
$$= 263 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi P_n = 0.90(263 \text{ kips})$ | $\frac{P_n}{\Omega} = \frac{263 \text{ kips}}{1.67}$ |
| $= 237 \text{ kips} > 161 \text{ kips} \quad \textbf{o.k.}$ | $= 157 \text{ kips} > 108 \text{ kips} \quad \textbf{o.k.}$ |

The compression flange plate will be identical to the tension flange plate; a ¾ in.×7 in. plate with eight bolts in two rows of four bolts on a 4 in. gage and ⅜ in. fillet welds to the supporting column flange.

Note: The bolt bearing and shear checks are the same as for the tension flange plate and have been found to be adequate in prior calculations. Tension due to load reversal must also be considered in the design of the fillet weld to the supporting column flange. The result is the same as previously calculated for the top flange connection plate.

---

# IIB-18

*Flange Local Bending of Column*

From AISC *Specification* Section J10.1, the available strength of the column for the limit state of flange local bending is determined as follows:

$$0.15b_f = 0.15(14.6 \text{ in.})$$
$$= 2.19 \text{ in.}$$

The length of loading (i.e., plate width) is 7 in., which is greater than $0.15b_f$. Thus, flange local bending needs to be checked.

Assume the concentrated force to be resisted is applied at a distance from the column end greater than $10t_f$.

$$10t_f = 10(0.780 \text{ in.})$$
$$= 7.80 \text{ in.}$$

$$R_n = 6.25F_y t_f^2$$ (*Spec.* Eq. J10-1)
$$= 6.25(50 \text{ ksi})(0.780 \text{ in.})^2$$
$$= 190 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi R_n = 0.90(190 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{190 \text{ kips}}{1.67}$ |
| $= 171 \text{ kips} > 161 \text{ kips} \quad \textbf{o.k.}$ | $= 114 \text{ kips} > 108 \text{ kips} \quad \textbf{o.k.}$ |

*Web Local Yielding of Column*

Assume the concentrated force to be resisted is applied at a distance from the column end that is greater than the depth of the column. The available strength of the column for the limit state of web local yielding is determined from AISC *Manual* Table 9-4 and AISC *Manual* Equation 9-61a or 9-61b, with $l_b = t = ¾$ in.

| LRFD | ASD |
|------|-----|
| $\phi R_1 = 83.7$ kips | $\frac{R_1}{\Omega} = 55.8$ kips |
|  |  |
| $\phi R_2 = 24.3$ kip/in. | $\frac{R_2}{\Omega} = 16.2$ kip/in. |
|  |  |
| $\phi R_n = 2\left(\phi R_1\right) + l_b\left(\phi R_2\right)$ | $\frac{R_n}{\Omega} = 2\left(\frac{R_1}{\Omega}\right) + l_b\left(\frac{R_2}{\Omega}\right)$ |
| $= 2(83.7 \text{ kips}) + (¾ \text{ in.})(24.3 \text{ kip/in.})$ | $= 2(55.8 \text{ kips}) + (¾ \text{ in.})(16.2 \text{ kip/in.})$ |
| $= 186 \text{ kips} > 161 \text{ kips} \quad \textbf{o.k.}$ | $= 124 \text{ kips} > 108 \text{ kips} \quad \textbf{o.k.}$ |

*Web Local Crippling*

Assume the concentrated force to be resisted is applied at a distance from the column end that is greater than or equal to one-half of the column depth. The available strength of the column for the limit state of web local crippling is determined from AISC *Manual* Table 9-4 and AISC *Manual* Equation 9-64a or 9-64b, with $l_b = t = ¾$ in.

---

# IIB-19

| LRFD | ASD |
|------|-----|
| $\phi R_3 = 108$ kips | $\frac{R_3}{\Omega} = 71.8$ kips |
| $\phi R_4 = 11.2$ kip/in. | $\frac{R_4}{\Omega} = 7.44$ kip/in. |
|  |  |
| $\phi R_n = 2\left[\phi R_3 + l_b\left(\phi R_4\right)\right]$ | $\frac{R_n}{\Omega} = 2\left[\frac{R_3}{\Omega} + l_b\left(\frac{R_4}{\Omega}\right)\right]$ |
| $= 2\left[108 \text{ kips} + (¾ \text{ in.})(11.2 \text{ kip/in.})\right]$ | $= 2\left[71.8 \text{ kips} + (¾ \text{ in.})(7.44 \text{ kip/in.})\right]$ |
| $= 233 \text{ kips} > 161 \text{ kips} \quad \textbf{o.k.}$ | $= 155 \text{ kips} > 108 \text{ kips} \quad \textbf{o.k.}$ |

Note: Web compression buckling (AISC *Specification* Section J10.5) must be checked if another beam is framed into the opposite side of the column at this location.

Web panel zone shear (AISC *Specification* Section J10.6) should also be checked for this column.

For further information, see AISC Design Guide 13, *Stiffening of Wide-Flange Columns at Moment Connections: Wind and Seismic Applications* (Carter, 1999).

---

# IIB-20

## EXAMPLE II.B-2 WELDED FLANGE-PLATED FR MOMENT CONNECTION (BEAM-TO-COLUMN FLANGE)

**Given:**

Verify a welded flange-plated FR moment connection between an ASTM A992/A992M W18×50 beam and an ASTM A992/A992M W14×99 column flange, as shown in Figure II.B-2-1, to transfer the following beam end reactions:

Vertical shear:
$V_D = 7$ kips
$V_L = 21$ kips

Strong-axis moment:
$M_D = 42$ kip-ft
$M_L = 126$ kip-ft

Use 70-ksi electrodes. The flange and web plates are ASTM A572/A572M Grade 50 material. Assume the top flange of the beam is in the tension condition due to moment.

![Connection diagram showing W14×99 column with W18×50 beam connected via welded flange plates. Top view shows cross-section with 5/16 and 7/16 fillet welds. Bottom elevation view shows PL1×6×0'-10½" top flange plate, (3) ⅞" dia. Group 120 bolts with thread condition N in standard holes for web connection, PL⅜×5×0'-9" web plate, and PL¾×8¾×1'-2½" bottom flange plate with 5/16 and 12½ typ. fillet welds. Note indicates "Shim top or bottom as required."]

*Fig. II.B-2-1. Connection geometry for Example II.B-2.*

---

# IIB-21

**Solution:**

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Beam and column
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Plates
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W18×50
$d$ = 18.0 in.
$b_f$ = 7.50 in.
$t_f$ = 0.570 in.
$t_w$ = 0.355 in.
$Z_x = 101$ in.$^3$

Column
W14×99
$d = 14.2$ in.
$b_f = 14.6$ in.
$t_f = 0.780$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(7 \text{ kips}) + 1.6(21 \text{ kips})$ | $R_a = 7 \text{ kips} + 21 \text{ kips}$ |
| $= 42.0$ kips | $= 28.0$ kips |
|  |  |
| $M_u = 1.2(42 \text{ kip-ft}) + 1.6(126 \text{ kip-ft})$ | $M_a = 42 \text{ kip-ft} + 126 \text{ kip-ft}$ |
| $= 252$ kip-ft | $= 168$ kip-ft |

*Single-Plate Web Connection*

The single-plate web connection and beam web strength were verified in Example II.B-1.

*Tension Flange Plate and Connection*

*Tensile yielding of the flange plate*

The top flange plate is specified as a PL1 in. × 6 in. × 0 ft 10½ in. The top beam flange width is $b_f = 7.50$ in. This provides a shelf dimension of 1.50 in. on both sides of the plate for welding.

The moment arm between flange plate forces, $d_m$, used for verifying the plate strength is equal to the depth of the beam plus half the thickness of each of the flange plates. This represents the distance between the centerlines of the flange plates at the top and bottom of the beam.

---

# IIB-22

$$d_m = 18.0 \text{ in.} + \frac{¾ \text{ in.}}{2} + \frac{1 \text{ in.}}{2}$$
$$= 18.9 \text{ in.}$$

From AISC *Manual* Equation 11-1, the flange force is:

| LRFD | ASD |
|------|-----|
| $P_{uf} = \frac{M_u}{d_m}$ (from *Manual* Eq. 11-1) | $P_{af} = \frac{M_a}{d_m}$ (from *Manual* Eq. 11-1) |
|  |  |
| $= \frac{(252 \text{ kip-ft})(12 \text{ in./ft})}{18.9 \text{ in.}}$ | $= \frac{(168 \text{ kip-ft})(12 \text{ in./ft})}{18.9 \text{ in.}}$ |
| $= 160$ kips | $= 107$ kips |

From AISC *Specification* Section J4.1(a), the available tensile yield strength of the flange plate is determined as follows:

$$R_n = F_y A_g$$ (*Spec.* Eq. J4-1)
$$= (50 \text{ ksi})(6 \text{ in.})(1 \text{ in.})$$
$$= 300 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi R_n = 0.90(300 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{300 \text{ kips}}{1.67}$ |
| $= 270 \text{ kips} > 160 \text{ kips} \quad \textbf{o.k.}$ | $= 180 \text{ kips} > 107 \text{ kips} \quad \textbf{o.k.}$ |

*Fillet weld strength for top flange plate to beam flange*

The moment arm between flange forces, $d_m$, used for verifying the fillet weld strength is equal to the depth of the beam. This dimension represents the faying surface between the flange of the beam and the tension plate. From AISC *Manual* Equation 11-1, the flange force is:

| LRFD | ASD |
|------|-----|
| $P_{uf} = \frac{M_u}{d_m}$ (from *Manual* Eq. 11-1) | $P_{af} = \frac{M_a}{d_m}$ (from *Manual* Eq. 11-1) |
|  |  |
| $= \frac{(252 \text{ kip-ft})(12 \text{ in./ft})}{18.0 \text{ in.}}$ | $= \frac{(168 \text{ kip-ft})(12 \text{ in./ft})}{18.0 \text{ in.}}$ |
| $= 168$ kips | $= 112$ kips |

A $\frac{5}{16}$ in. fillet weld is specified ($D = 5$). The available strength may be calculated using the provisions from AISC *Specification* Section J2.4(b). The available shear strength of the fillet weld may be calculated using AISC *Specification* Table J2.5.

$$F_{nw} = 0.60F_{EXX}$$
$$= 0.60(70 \text{ ksi})$$
$$= 42.0 \text{ ksi}$$

The length of the longitudinally loaded welds is determined taking into consideration a ¼ in. tolerance to account for possible beam underrun and a weld termination equal to the weld size.

---

# IIB-23

$$l = 10½ \text{ in.} - 1 \text{ in. (setback)} - ¼ \text{ in. (underrun)} - \frac{5}{16} \text{ in. (weld termination)}$$
$$= 8.94 \text{ in.}$$

$$A_{wel} = (2 \text{ welds})\left(\frac{\sqrt{2}}{2}\right)\left(\frac{D}{16}\right)l$$

$$= (2 \text{ welds})\left(\frac{\sqrt{2}}{2}\right)\left(\frac{5}{16}\right)(8.94 \text{ in.})$$

$$= 3.95 \text{ in.}^2$$

$$A_{wet} = \left(\frac{\sqrt{2}}{2}\right)\left(\frac{D}{16}\right)l$$

$$= \left(\frac{\sqrt{2}}{2}\right)\left(\frac{5}{16}\right)(6 \text{ in.})$$

$$= 1.33 \text{ in.}^2$$

The combined strength of the fillet weld group is:

$$R_n = 0.85F_{nw}A_{wel} + 1.5F_{nw}A_{wet}$$ (*Spec.* Eq. J2-6)
$$= 0.85(42.0 \text{ ksi})\left(3.95 \text{ in.}^2\right) + 1.5(42.0 \text{ ksi})\left(1.33 \text{ in.}^2\right)$$
$$= 225 \text{ kips}$$

Therefore:

$$R_n = 225 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(225 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{225 \text{ kips}}{2.00}$ |
| $= 169 \text{ kips} > 168 \text{ kips} \quad \textbf{o.k.}$ | $= 113 \text{ kips} > 112 \text{ kips} \quad \textbf{o.k.}$ |

*Connecting elements rupture strength at top flange welds*

At the top flange connection, the minimum base metal thickness to match the shear rupture strength of the weld is determined as follows:

$$t_{min} = \frac{3.09D}{F_u}$$ (*Manual* Eq. 9-6)

$$= \frac{3.09(5)}{65 \text{ ksi}}$$
$$= 0.238 \text{ in.}$$

For the beam flange:
0.238 in. < 0.570 in. **o.k.**

For the top flange plate:
0.238 in. < 1.00 in. **o.k.**

---

# IIB-24

*Fillet weld at top flange plate to column flange*

The applied load is perpendicular to the weld length ($\theta = 90°$), therefore the directional strength factor is determined from AISC *Specification* Equation J2-5. This increase factor due to directional strength is incorporated into the weld strength calculation.

$$k_{de} = 1.0 + 0.50\sin^{1.5}\theta$$ (*Spec.* Eq. J2-5)
$$= 1.0 + 0.50\sin^{1.5}(90°)$$
$$= 1.50$$

The available strength of fillet welds is determined using AISC *Manual* Equation 8-2a or 8-2b, as follows:

| LRFD | ASD |
|------|-----|
| $D_{min} = \frac{P_{uf}}{nk_{de}\left(1.392 \text{ kip/in.}\right)l}$ | $D_{min} = \frac{P_{af}}{nk_{de}\left(0.928 \text{ kip/in.}\right)l}$ |
|  |  |
| $= \frac{160 \text{ kips}}{(2 \text{ welds})(1.50)(1.392 \text{ kip/in.})(6 \text{ in.})}$ | $= \frac{107 \text{ kips}}{(2 \text{ welds})(1.50)(0.928 \text{ kip/in.})(6 \text{ in.})}$ |
| $= 6.39$ | $= 6.41$ |
|  |  |
| Use a $\frac{7}{16}$ in. fillet weld on both sides of the plate. | Use a $\frac{7}{16}$ in. fillet weld on both sides of the plate. |

*Compression Flange Plate and Connection*

*Flange plate compressive strength*

The bottom flange plate is specified as a PL¾×8¾×1′-2½″. The bottom flange width is $b_f = 7.50$ in. This provides a shelf dimension of $\frac{5}{8}$ in. on both sides of the plate for welding.

Assume an underrun dimension of ¼ in. and an additional ½ in. to the start of the weld.

$K = 0.65$ from AISC *Specification* Commentary Table C-A-7.1
$L = 1.75$ in.

$$r = \sqrt{\frac{I}{A}}$$

$$= \sqrt{\frac{(8¾ \text{ in.})(¾ \text{ in.})^3/12}{(8¾ \text{ in.})(¾ \text{ in.})}}$$

$$= 0.217 \text{ in.}$$
$$\frac{L_c}{r} = \frac{KL}{r}$$
$$= \frac{0.65(1.75 \text{ in.})}{0.217 \text{ in.}}$$
$$= 5.24 < 25$$

Because $L_c/r \leq 25$:

$$P_n = F_y A_g$$ (*Spec.* Eq. J4-6)
$$= (50 \text{ ksi})(8¾ \text{ in.})(¾ \text{ in.})$$
$$= 328 \text{ kips}$$

---

# IIB-25

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi P_n = 0.90(328 \text{ kips})$ | $\frac{P_n}{\Omega} = \frac{328 \text{ kips}}{1.67}$ |
| $= 295 \text{ kips} > 160 \text{ kips} \quad \textbf{o.k.}$ | $= 196 \text{ kips} > 107 \text{ kips} \quad \textbf{o.k.}$ |

*Fillet weld strength for bottom flange plate to beam flange*

The required weld length is determined using AISC *Manual* Equation 8-2a or 8-2b, as follows:

| LRFD | ASD |
|------|-----|
| $l_{min} = \frac{P_{uf}}{n\left(1.392 \text{ kip/in.}\right)D}$ | $l_{min} = \frac{P_{af}}{n\left(0.928 \text{ kip/in.}\right)D}$ |
|  |  |
| $= \frac{168 \text{ kips}}{(2 \text{ welds})(1.392 \text{ kip/in.})(5)}$ | $= \frac{112 \text{ kips}}{(2 \text{ welds})(0.928 \text{ kip/in.})(5)}$ |
| $= 12.1 \text{ in.}$ | $= 12.1 \text{ in.}$ |
|  |  |
| Use 12½-in.-long $\frac{5}{16}$ in. fillet welds. | Use 12½-in.-long $\frac{5}{16}$ in. fillet welds. |

*Beam bottom flange rupture strength at welds*

$$A_{nv} = (2 \text{ welds})t_f l$$
$$= (2 \text{ welds})(0.570 \text{ in.})(12½ \text{ in.})$$
$$= 14.3 \text{ in.}^3$$

$$R_n = 0.60F_u A_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})\left(14.3 \text{ in.}^2\right)$$
$$= 558 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(558 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{558 \text{ kips}}{2.00}$ |
| $= 419 \text{ kips} > 168 \text{ kips} \quad \textbf{o.k.}$ | $= 279 \text{ kips} > 112 \text{ kips} \quad \textbf{o.k.}$ |

*Fillet weld at bottom flange plate to column flange*

The applied load is perpendicular to the weld length ($\theta = 90°$) therefore the directional strength factor is determined from AISC *Specification* Equation J2-5. This increase factor due to directional strength is incorporated into the weld strength calculation.

$$k_{de} = 1.0 + 0.50\sin^{1.5}\theta$$ (*Spec.* Eq. J2-5)
$$= 1.0 + 0.50\sin^{1.5}(90°)$$
$$= 1.50$$

The available strength of fillet welds is determined using AISC *Manual* Equation 8-2a or 8-2b as follows:

---

# IIB-26

| LRFD | ASD |
|------|-----|
| $D_{min} = \frac{P_{uf}}{nk_{de}\left(1.392 \text{ kip/in.}\right)l}$ | $D_{min} = \frac{P_{af}}{nk_{de}\left(0.928 \text{ kip/in.}\right)l}$ |
|  |  |
| $= \frac{160 \text{ kips}}{(2 \text{ welds})(1.50)(1.392 \text{ kip/in.})(8¾ \text{ in.})}$ | $= \frac{107 \text{ kips}}{(2 \text{ welds})(1.50)(0.928 \text{ kip/in.})(8¾ \text{ in.})}$ |
| $= 4.38$ sixteenths | $= 4.39$ sixteenths |
|  |  |
| Use $\frac{5}{16}$ in. fillet welds. | Use $\frac{5}{16}$ in. fillet welds. |

See Example II.B-1 for checks of the column under concentrated forces. For further information, see AISC Design Guide 13 *Stiffening of Wide-Flange Columns at Moment Connections: Wind and Seismic Applications* (Carter, 1999).

*Conclusion*

The connection is found to be adequate as given for the applied loads.

---

# IIB-27

## EXAMPLE II.B-3 DIRECTLY WELDED FLANGE FR MOMENT CONNECTION (BEAM-TO-COLUMN FLANGE)

**Given:**

Verify a directly welded flange FR moment connection between an ASTM A992/A992M W18×50 beam and an ASTM A992/A992M W14×99 column flange, as shown in Figure II.B-3-1, to transfer the following beam end reactions:

Vertical shear:
$V_D = 7$ kips
$V_L = 21$ kips

Strong-axis moment:
$M_D = 42$ kip-ft
$M_L = 126$ kip-ft

The web plate is ASTM A572/A572M Grade 50 material. Use 70-ksi electrodes. Check the column for stiffening requirements.

![Connection diagram showing W14×99 column with W18×50 beam. Top view shows cross-section with ½" gap dimension. Front elevation view shows:
- CJP, both flanges marking at top
- W14×99 column section
- 3" horizontal dimension
- 2@3" = 6" vertical spacing notation
- (3) ⅞" dia. Group 120, thread condition N, std. holes notation
- PL⅜×5×0'-9" web plate
- W18×50 beam with ¼" and ¼" gap markings]

*Fig. II.B-3-1. Connection geometry for Example II.B-3.*

**Solution:**

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Beam and column
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

---

# IIB-28

Plate
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(7 \text{ kips}) + 1.6(21 \text{ kips})$ | $R_a = 7 \text{ kips} + 21 \text{ kips}$ |
| $= 42.0$ kips | $= 28.0$ kips |
|  |  |
| $M_u = 1.2(42 \text{ kip-ft}) + 1.6(126 \text{ kip-ft})$ | $M_a = 42 \text{ kip-ft} + 126 \text{ kip-ft}$ |
| $= 252$ kip-ft | $= 168$ kip-ft |

The single-plate web connection was verified in Example II.B-1.

*Weld of Beam Flange to Column*

A complete-joint-penetration groove weld will transfer the entire flange force in tension and compression. It is assumed that the beam is adequate for the applied moment and will carry the tension and compression forces through the flanges.

See Example II.B-1 for checks of the column under concentrated forces. For further information, see AISC Design Guide 13 *Stiffening of Wide-Flange Columns at Moment Connections: Wind and Seismic Applications* (Carter, 1999).

*Conclusion*

The connection is found to be adequate as given for the applied loads.

---

# IIB-29

## CHAPTER IIB DESIGN EXAMPLE REFERENCES

Carter, C.J. (1999), *Stiffening of Wide-Flange Columns at Moment Connections: Wind and Seismic Applications*, Design Guide 13, AISC, Chicago, Ill.

---

# IIB-30

---
