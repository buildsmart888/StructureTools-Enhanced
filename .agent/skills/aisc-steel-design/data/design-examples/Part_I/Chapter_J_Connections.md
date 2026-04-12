# Chapter J: Connections

**AISC Specification v16.0 - Design Examples**
**Original PDF Pages**: 433-460 (28 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Design of Connections

**Examples Included**: ['J.1~J.6: Connection design examples']

---

## Table of Contents

- [EXAMPLE J.1 FILLET WELD IN LONGITUDINAL SHEAR](#example-j1-fillet-weld-in-longitudinal-shear)
- [EXAMPLE J.2A FILLET WELD LOADED AT AN ANGLE](#example-j2a-fillet-weld-loaded-at-an-angle)
- [EXAMPLE J.2B PARTIAL-JOINT-PENETRATION (PJP) GROOVE WELD LOADED AT AN ANGLE](#example-j2b-partial-joint-penetration-(pjp)-groove-weld-loaded-at-an-angle)
- [EXAMPLE J.3 COMBINED TENSION AND SHEAR IN BEARING-TYPE CONNECTIONS](#example-j3-combined-tension-and-shear-in-bearing-type-connections)
- [EXAMPLE J.4A SLIP-CRITICAL CONNECTION WITH SHORT-SLOTTED HOLES](#example-j4a-slip-critical-connection-with-short-slotted-holes)
- [EXAMPLE J.4B SLIP-CRITICAL CONNECTION WITH LONG-SLOTTED HOLES](#example-j4b-slip-critical-connection-with-long-slotted-holes)
- [EXAMPLE J.5 COMBINED TENSION AND SHEAR IN A SLIP-CRITICAL CONNECTION](#example-j5-combined-tension-and-shear-in-a-slip-critical-connection)
- [EXAMPLE J.6 BASE PLATE BEARING ON CONCRETE](#example-j6-base-plate-bearing-on-concrete)
- [EXAMPLE J.7 CONCENTRATED FORCES FOR BEAM BEARING ON GIRDER](#example-j7-concentrated-forces-for-beam-bearing-on-girder)

---

# J-1

# Chapter J
# Design of Connections

AISC *Specification* Chapter J addresses the design of connections. The chapter's primary focus is the design of welded and bolted connections. Design requirements for fillers, splices, column bases, concentrated forces, anchor rods, and other threaded parts are also covered. See AISC *Specification* Appendix 3 for special requirements for connections subject to fatigue.

---

# J-2

## EXAMPLE J.1 FILLET WELD IN LONGITUDINAL SHEAR

**Given:**

As shown in Figure J.1-1, a ¼-in.-thick × 18-in.-wide plate is fillet welded to a ⅜-in.-thick plate. The plates are ASTM A572/A572M Grade 50 and have been properly sized. Use 70-ksi electrodes.

Confirm that the size and length of the welds shown are adequate to resist the applied loading.

![Diagram showing a welded plate connection. A 28" tall ¼" thick plate (PL¼×18) is fillet welded to a ⅜" thick plate (PL⅜) with ³⁄₁₆" fillet welds 27" long on both sides. Applied loads shown are $P_D = 33$ kips and $P_L = 100$ kips.]

*Fig. J.1-1. Geometry and loading for Example J.1.*

**Solution:**

From AISC *Manual* Table 2-5, the material properties are as follows:

ASTM A572/A572M Grade 50
- $F_y = 50$ ksi
- $F_u = 65$ ksi

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(33 \text{ kips}) + 1.6(100 \text{ kips})$ | $P_a = 33 \text{ kips} + 100 \text{ kips}$ |
| $= 200 \text{ kips}$ | $= 133 \text{ kips}$ |

*Maximum and Minimum Weld Size*

Because the thickness of the overlapping plate is ¼ in., the maximum fillet weld size that can be used without special notation per AISC *Specification* Section J2.2b(b)(2), is a ³⁄₁₆ in. fillet weld. A ³⁄₁₆ in. fillet weld can be deposited in the flat or horizontal position in a single pass (true up to ⁵⁄₁₆ in.).

From AISC *Specification* Table J2.4, the minimum size of the fillet weld, based on a material thickness of ¼ in. is ⅛ in.

---

# J-3

*Weld Strength*

The nominal weld strength per inch of a ³⁄₁₆ in. weld is determined from AISC *Specification* Section J2.4(a). From the User Note in AISC *Specification* Section J2.4, the requirements for strain compatibility are satisfied for this weld and the directional strength increase factor may be used.

$$k_{ds} = 1.0 + 0.50\sin^{1.5}\theta$$
$(Spec. \text{ Eq. J2-5})$

$$= 1.0 + 0.50\sin^{1.5}0°$$

$$= 1.0$$

$$R_n = F_{nw} A_{we} k_{ds}$$
$(Spec. \text{ Eq. J2-4})$

$$= (0.60F_{EXX})A_{we}k_{ds}$$

$$= 0.60(70 \text{ ksi})\left(\frac{3}{16} \text{ in.}\right)(1.0)$$
$$\sqrt{2}$$

$$= 5.57 \text{ kip/in.}$$

From AISC *Specification* Section J2.2b(d), check the weld length to weld size ratio, because this is an end-loaded fillet weld.

$$\frac{l}{w} = \frac{27.0 \text{ in.}}{3}{16} \text{ in.}$$

$$= 144 > 100$$

Therefore, AISC *Specification* Equation J2.1 must be applied.

$$\beta = 1.2 - 0.002(l/w) \leq 1.0$$
$(Spec. \text{ Eq. J2-1})$

$$= 1.2 - 0.002(144) \leq 1.0$$

$$= 0.912 < 1.0$$ **o.k.**

The nominal weld shear rupture strength is:

$$R_n = 0.912(5.57 \text{ kip/in.})(2 \text{ welds})(27 \text{ in.})$$

$$= 274 \text{ kips}$$

From AISC *Specification* Section J2.4, the available shear rupture strength is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(274 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{274 \text{ kips}}{2.00}$ |
| $= 206 \text{ kips} > 200 \text{ kips}$ **o.k.** | $= 137 \text{ kips} > 133 \text{ kips}$ **o.k.** |

The base metal strength is determined from AISC *Specification* Section J2.4(a). The ¼-in.-thick plate controls:

---

# J-4

$$R_n = F_{nBM} A_{BM}$$
$(Spec. \text{ Eq. J2-2})$

$$= 0.60F_u t_p l_{weld}$$

$$= 0.60(65 \text{ ksi})(\frac{1}{4} \text{ in.})(2 \text{ welds})(27 \text{ in.})$$

$$= 527 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(527 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{527 \text{ kips}}{2.00}$ |
| $= 395 \text{ kips} > 200 \text{ kips}$ **o.k.** | $= 264 \text{ kips} > 133 \text{ kips}$ **o.k.** |

---

# J-5

## EXAMPLE J.2A FILLET WELD LOADED AT AN ANGLE

**Given:**

Determine the required length, $l$, of a two-sided fillet weld between a gusset plate and beam flange to resist loads as shown in Figure J.2A-1. The weld is loaded at an angle of 60° relative to the weld longitudinal axis. Assume the beam and the gusset plate thickness and length have been properly sized. Use a 70-ksi electrode.

![Diagram showing a fillet weld connection between a ¾" plate and heavy beam. The weld is loaded at 60° angle with loads $P_D = 50$ kips and $P_L = 150$ kips. Weld sizes shown as ⁵⁄₁₆" on both sides, with W.P. (work point) indicated and length $l$ to be determined.]

*Fig. J.2A-1. Geometry and loading for Example J.2A.*

**Solution:**

From ASCE/SEI 7, Chapter 2, the required tensile strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(50 \text{ kips}) + 1.6(150 \text{ kips})$ | $P_a = 50 \text{ kips} + 150 \text{ kips}$ |
| $= 300 \text{ kips}$ | $= 200 \text{ kips}$ |

Note that from AISC *Specification* Table J2.4, the minimum size of fillet weld, based on a material thickness of ⅝ in. is ¼ in. (assuming the beam flange thickness exceeds ⅝ in.).

*Available Shear Strength of the Fillet Weld Per Inch of Length*

The nominal strength of the fillet weld is determined from AISC *Specification* Section J2.4(a). From the User Note in AISC *Specification* Section J2.4, the requirements for strain compatibility are satisfied for this weld and the directional strength increase factor may be used.

$$k_{ds} = 1.0 + 0.50\sin^{1.5}\theta$$
$(Spec. \text{ Eq. J2-5})$

$$= 1.0 + 0.50\sin^{1.5}60°$$

$$= 1.40$$

$$R_n = F_{nw} A_{we} k_{ds}$$
$(Spec. \text{ Eq. J2-4})$

$$= 0.60F_{EXX} A_{we} k_{ds}$$

$$= 0.60(70 \text{ ksi})\left(\frac{5}{16} \text{ in.}\right)(1.40)$$
$$\sqrt{2}$$

$$= 13.0 \text{ kip/in.}$$

---

# J-6

The available shear strength per inch of weld for fillet welds on both sides of the plate is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(13.0 \text{ kip/in.})(2 \text{ sides})$ | $\frac{R_n}{\Omega} = \left(\frac{13.0 \text{ kip/in.}}{2.00}\right)(2 \text{ sides})$ |
| $= 19.5 \text{ kip/in.}$ | $= 13.0 \text{ kip/in.}$ |

*Required Length of Weld*

| LRFD | ASD |
|------|-----|
| $l = \frac{300 \text{ kips}}{19.5 \text{ kip/in.}}$ | $l = \frac{200 \text{ kips}}{13.0 \text{ kip/in.}}$ |
| $= 15.4 \text{ in.}$ | $= 15.4 \text{ in.}$ |
| Use $l = 16 \text{ in.}$ | Use $l = 16 \text{ in.}$ |

---

# J-7

## EXAMPLE J.2B PARTIAL-JOINT-PENETRATION (PJP) GROOVE WELD LOADED AT AN ANGLE

**Given:**

Determine the required length, $l$, of a two-sided PJP groove weld between a gusset plate and W18×86 beam flange to resist loads as shown in Figure J.2B-1. The weld on each side of the gusset plate has a groove weld size of ¼ in. and is loaded at an angle of 60° relative to the weld longitudinal axis. Assume the beam and the gusset plate thickness and length have been properly sized. The gusset plate is ASTM A572/A572M Grade 50 material, and the beam is ASTM A992/A992M material. Use a 70-ksi electrode.

![Diagram showing a PJP groove weld connection between a ¾" plate and W18×86 beam. The weld is loaded at 60° angle with loads $P_D = 50$ kips and $P_L = 150$ kips. Groove weld size shown as (¼) on both sides, with W.P. (work point) indicated and length $l$ to be determined.]

*Fig. J.2B-1. Geometry and loading for Example J.2B.*

**Solution:**

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

ASTM A992/A992M
- $F_y = 50$ ksi
- $F_u = 65$ ksi

ASTM A572/A572M Grade 50
- $F_y = 50$ ksi
- $F_u = 65$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W18×86
- $t_f = 0.770$ in.

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(50 \text{ kips}) + 1.6(150 \text{ kips})$ | $P_a = 50 \text{ kips} + 150 \text{ kips}$ |
| $= 300 \text{ kips}$ | $= 200 \text{ kips}$ |

---

# J-8

*Minimum Weld Size*

Because the flange thickness is greater than the gusset plate thickness, the minimum weld size is controlled by the gusset plate. From AISC *Specification* Table J2.3, the minimum effective throat for material thickness of ⅝ in. is ¼ in.

*Available Weld Strength*

From AISC *Specification* Section J2.4(a), the nominal strength of the PJP groove weld is determined as follows:

$$R_n = F_{nw} A_{we}$$
$(Spec. \text{ Eq. J2-3})$

From AISC *Specification* Table J2.5, for a PJP groove weld loaded in shear or tension:

$$F_{nw} = 0.60F_{EXX}$$

$$= 0.60(70 \text{ ksi})$$

$$= 42.0 \text{ ksi}$$

The nominal shear or tensile strength of the weld is determined per inch of length:

$$r_n = F_{nw} A_{we}$$
(from *Spec.* Eq. J2-3)

$$= (42.0 \text{ ksi})(\frac{1}{4} \text{ in.})(2 \text{ welds})$$

$$= 21.0 \text{ kip/in.}$$

From AISC *Specification* Table J2.5, the available strength of the weld per inch of length is:

| LRFD | ASD |
|------|-----|
| Shear: | Shear: |
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_{nv} = 0.75(21.0 \text{ kip/in.})$ | $\frac{r_{nv}}{\Omega} = \frac{21.0 \text{ kip/in.}}{2.00}$ |
| $= 15.8 \text{ kip/in.}$ | $= 10.5 \text{ kip/in.}$ |
| Tension: | Tension: |
| $\phi = 0.80$ | $\Omega = 1.88$ |
| $\phi r_{nt} = 0.80(21.0 \text{ kip/in.})$ | $\frac{r_{nt}}{\Omega} = \frac{21.0 \text{ kip/in.}}{1.88}$ |
| $= 16.8 \text{ kip/in.}$ | $= 11.2 \text{ kip/in.}$ |

The required weld length based on the weld strength is determined as follows:

| LRFD | ASD |
|------|-----|
| $l = P_u\sqrt{\left(\frac{\cos\theta}{\phi r_{nv}}\right)^2 + \left(\frac{\sin\theta}{\phi r_{nt}}\right)^2}$ | $l = P_a\sqrt{\left(\frac{\cos\theta}{r_{nv}/\Omega}\right)^2 + \left(\frac{\sin\theta}{r_{nt}/\Omega}\right)^2}$ |
| $= (300 \text{ kips})\sqrt{\left(\frac{\cos 60°}{15.8 \text{ kip/in.}}\right)^2 + \left(\frac{\sin 60°}{16.8 \text{ kip/in.}}\right)^2}$ | $= (200 \text{ kips})\sqrt{\left(\frac{\cos 60°}{10.5 \text{ kip/in.}}\right)^2 + \left(\frac{\sin 60°}{11.2 \text{ kip/in.}}\right)^2}$ |
| $= 18.1 \text{ in.}$ | $= 18.2 \text{ in.}$ |

---

# J-9

Use $l = 18\frac{1}{4}$ in.

*Available Base Metal Strength*

The effective area of the base metal is conservatively assumed to be equal to the effective weld area of the weld, $A_{we}$.

From AISC *Specification* Section J2.4(a), the nominal strength in shear or tension of the base metal at the PJP weld is determined as follows:

$$R_n = F_{nBM} A_{BM}$$
$(Spec. \text{ Eq. J2-2})$

The nominal shear stress of the base metal is determined from AISC *Specification* Section J4.2:

$$F_{nBM} = 0.60F_u$$
(from *Spec.* Eq. J4-4)

$$= 0.60(65 \text{ ksi})$$

$$= 39.0 \text{ ksi}$$

The nominal shear strength of the base metal is determined per inch of length:

$$r_{nv} = F_{nBM} A_{BM}$$
(from *Spec.* Eq. J2-2)

$$= (39.0 \text{ ksi})(\frac{1}{4} \text{ in.})(1 \text{ in.})(2 \text{ welds})$$

$$= 19.5 \text{ kip/in.}$$

The nominal tensile stress of the base metal is determined from AISC *Specification* Section J4.1:

$$F_{nBM} = F_u$$
(from *Spec.* Eq. J4-2)

$$= 65 \text{ ksi}$$

The nominal tensile strength of the base metal is determined per inch of length:

$$r_{nt} = F_{nBM} A_{BM}$$
(from *Spec.* Eq. J2-2)

$$= (65.0 \text{ ksi})(\frac{1}{4} \text{ in.})(1 \text{ in.})(2 \text{ welds})$$

$$= 32.5 \text{ kip/in.}$$

From AISC *Specification* Table J2.5, the available strength of the base metal per inch of length is:

| LRFD | ASD |
|------|-----|
| Shear: | Shear: |
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_{nv} = 0.75(19.5 \text{ kip/in.})$ | $\frac{r_{nv}}{\Omega} = \frac{19.5 \text{ kip/in.}}{2.00}$ |
| $= 14.6 \text{ kip/in.}$ | $= 9.75 \text{ kip/in.}$ |
| Tension: | Tension: |
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi r_{nt} = 0.75(32.5 \text{ kip/in.})$ | $\frac{r_{nt}}{\Omega} = \frac{32.5 \text{ kip/in.}}{2.00}$ |
| $= 24.4 \text{ kip/in.}$ | $= 16.3 \text{ kip/in.}$ |

---

# J-10

The required weld length based on the base metal strength is determined using *Manual* Equation 9-1 as follows:

$$\frac{M_r}{M_c} + \left(\frac{P_r}{P_c}\right)^2 + \left(\frac{V_r}{V_c}\right)^4 \leq 1.0$$
$({Manual} \text{ Eq. 9-1})$

Verify the 18¼ in. length determined for the weld.

| LRFD | ASD |
|------|-----|
| $P_r = P_u \sin\theta$ | $P_r = P_a \sin\theta$ |
| $= (300 \text{ kips})(\sin 60°)$ | $= (200 \text{ kips})(\sin 60°)$ |
| $= 260 \text{ kips}$ | $= 173 \text{ kips}$ |
| $V_r = P_u \cos\theta$ | $V_r = P_a \cos\theta$ |
| $= (300 \text{ kips})(\cos 60°)$ | $= (200 \text{ kips})(\cos 60°)$ |
| $= 150 \text{ kips}$ | $= 100 \text{ kips}$ |
| $P_c = \phi r_{nt} l$ | $P_c = \frac{r_{nt}}{\Omega}l$ |
| $= (24.4 \text{ kip/in.})(18\frac{1}{4} \text{ in.})$ | $= (16.3 \text{ kip/in.})(18\frac{1}{4} \text{ in.})$ |
| $= 445 \text{ kips}$ | $= 297 \text{ kips}$ |
| $V_c = \phi r_{nv} l$ | $V_c = \frac{r_{nv}}{\Omega}l$ |
| $= (14.6 \text{ kip/in.})(18\frac{1}{4} \text{ in.})$ | $= (9.75 \text{ kip/in.})(18\frac{1}{4} \text{ in.})$ |
| $= 266 \text{ kips}$ | $= 178 \text{ kips}$ |
| Note $M_r/M_c = 0$ because the work point is at the weld centerline. | Note $M_r/M_c = 0$ because the work point is at the weld centerline. |
| $\frac{M_r}{M_c} + \left(\frac{P_r}{P_c}\right)^2 + \left(\frac{V_r}{V_c}\right)^4$ | $\frac{M_r}{M_c} + \left(\frac{P_r}{P_c}\right)^2 + \left(\frac{V_r}{V_c}\right)^4$ |
| $= 0 + \left(\frac{260 \text{ kips}}{445 \text{ kips}}\right)^2 + \left(\frac{150 \text{ kips}}{266 \text{ kips}}\right)^4$ | $= 0 + \left(\frac{173 \text{ kips}}{297 \text{ kips}}\right)^2 + \left(\frac{100 \text{ kips}}{178 \text{ kips}}\right)^4$ |
| $= 0.442 < 1$ **o.k.** | $= 0.439 < 1$ **o.k.** |

Therefore, use an 18¼-in.-long weld.

---

# J-11

## EXAMPLE J.3 COMBINED TENSION AND SHEAR IN BEARING-TYPE CONNECTIONS

**Given:**

A ¾ in. diameter, Group 120 bolt with threads not excluded from the shear plane (thread condition N) is subjected to a tension force of 3.5 kips due to dead load and 12 kips due to live load, and a shear force of 1.33 kips due to dead load and 4 kips due to live load. Check the combined stresses according to AISC *Specification* Equations J3-3a and J3-3b.

**Solution:**

From ASCE/SEI 7, Chapter 2, the required tensile and shear strengths are:

| LRFD | ASD |
|------|-----|
| Tension: | Tension: |
| $T_u = 1.2(3.5 \text{ kips}) + 1.6(12 \text{ kips})$ | $T_a = 3.5 \text{ kips} + 12 \text{ kips}$ |
| $= 23.4 \text{ kips}$ | $= 15.5 \text{ kips}$ |
| Shear: | Shear: |
| $V_u = 1.2(1.33 \text{ kips}) + 1.6(4 \text{ kips})$ | $V_a = 1.33 \text{ kips} + 4 \text{ kips}$ |
| $= 8.00 \text{ kips}$ | $= 5.33 \text{ kips}$ |

*Available Tensile Strength*

When a bolt is subject to combined tension and shear, the available tensile strength is determined according to the limit states of tension and shear rupture, from AISC *Specification* Section J3.8 as follows.

From AISC *Specification* Table J3.2, Group 120 bolts:

- $F_{nt} = 90$ ksi
- $F_{nv} = 54$ ksi

From AISC *Manual* Table 7-2, for a ¾ in. diameter bolt:

- $A_b = 0.442 \text{ in.}^2$

The available shear stress is determined as follows and must equal or exceed the required shear stress.

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi F_{nv} = 0.75(54 \text{ ksi})$ | $\frac{F_{nv}}{\Omega} = \frac{54 \text{ ksi}}{2.00}$ |
| $= 40.5 \text{ ksi}$ | $= 27.0 \text{ ksi}$ |
| $f_{rv} = \frac{V_u}{A_b}$ | $f_{rv} = \frac{V_a}{A_b}$ |
| $= \frac{8.00 \text{ kips}}{0.442 \text{ in.}^2}$ | $= \frac{5.33 \text{ kips}}{0.442 \text{ in.}^2}$ |
| $= 18.1 \text{ ksi} < 40.5 \text{ ksi}$ **o.k.** | $= 12.1 \text{ ksi} < 27.0 \text{ ksi}$ **o.k.** |

---

# J-12

The available tensile strength of a bolt subject to combined tension and shear is as follows:

| LRFD | ASD |
|------|-----|
| $F'_{nt} = 1.3F_{nt} - \frac{F_{nt}}{\phi F_{nv}}f_{rv} \leq F_{nt}$ $(Spec. \text{ Eq. J3-3a})$ | $F'_{nt} = 1.3F_{nt} - \frac{\Omega F_{nt}}{F_{nv}}f_{rv} \leq F_{nt}$ $(Spec. \text{ Eq. J3-3b})$ |
| $= 1.3(90 \text{ ksi}) - \frac{90 \text{ ksi}}{40.5 \text{ ksi}}(18.1 \text{ ksi}) \leq 90 \text{ ksi}$ | $= 1.3(90 \text{ ksi}) - \frac{90 \text{ ksi}}{27.0 \text{ ksi}}(12.1 \text{ ksi}) \leq 90 \text{ ksi}$ |
| $= 76.8 \text{ ksi}$ | $= 76.7 \text{ ksi}$ |
| For combined tension and shear, $\phi = 0.75$, from AISC *Specification* Section J3.8. | For combined tension and shear, $\Omega = 2.00$, from AISC *Specification* Section J3.8. |
| $\phi R_n = \phi F'_{nt} A_b$ $(Spec. \text{ Eq. J3-2})$ | $\frac{R_n}{\Omega} = \frac{F'_{nt} A_b}{\Omega}$ $(Spec. \text{ Eq. J3-2})$ |
| $= 0.75(76.8 \text{ ksi})(0.442 \text{ in.}^2)$ | $= \frac{(76.7 \text{ ksi})(0.442 \text{ in.}^2)}{2.00}$ |
| $= 25.5 \text{ kips} > 23.4 \text{ kips}$ **o.k.** | $= 17.0 \text{ kips} > 15.5 \text{ kips}$ **o.k.** |

The effects of combined shear and tensile stresses need not be investigated if either the required shear or tensile stress is less than or equal to 30% of the corresponding available stress per the User Note at the end of AISC *Specification* Section J3.8. In the example herein, both the required shear and tensile stresses exceeded the 30% threshold and evaluation of combined stresses was necessary.

AISC *Specification* Equations J3-3a and J3-3b may be rewritten so as to find a nominal shear stress, $F'_{nv}$, as a function of the required tensile stress, as is shown in AISC *Specification* Commentary Equations C-J3-6a and C-J3-6b.

---

# J-13

## EXAMPLE J.4A SLIP-CRITICAL CONNECTION WITH SHORT-SLOTTED HOLES

**Given:**

Refer to Figure J.4A-1 and select the number of bolts that are required to support the loads shown when the connection plates have (NS/FS) slots transverse to the load and no fillers are provided. Select the number of bolts required for slip resistance only. Washers have been provided in accordance with the RCSC *Specification* Section 6.

![Diagram showing a bolted connection with two plates connected by bolts. Connection plates (NS/FS) with vertical short-slotted holes on left side, members with standard holes on right side. 8 bolts shown in a 4×2 pattern (¾" dia. Group 120, slip-critical, Class A). Applied loads: $P_D = 17$ kips, $P_L = 51$ kips.]

*Fig. J.4A-1. Geometry and loading for Example J.4A.*

**Solution:**

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(17 \text{ kips}) + 1.6(51 \text{ kips})$ | $P_a = 17 \text{ kips} + 51 \text{ kips}$ |
| $= 102 \text{ kips}$ | $= 68.0 \text{ kips}$ |

From AISC *Specification* Section J3.9(a), the available slip resistance for the limit state of slip for standard size and short-slotted holes perpendicular to the direction of the load is determined as follows:

- $\phi = 1.00$
- $\Omega = 1.50$
- $\mu = 0.30$ for Class A surface
- $D_u = 1.13$
- $h_f = 1.0$, no filler is provided
- $T_b = 28$ kips, from AISC *Specification* Table J3.1, Group 120
- $n_s = 2$, number of slip planes

$$R_n = 0.30(1.13)(1.0)(28 \text{ kips})(2)$$
$(Spec. \text{ Eq. J3-4})$

$$= 19.0 \text{ kips/bolt}$$

The available slip resistance per bolt is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 1.00(19.0 \text{ kips/bolt})$ | $\frac{R_n}{\Omega} = \frac{19.0 \text{ kips/bolt}}{1.50}$ |
| $= 19.0 \text{ kips/bolt}$ | $= 12.7 \text{ kips/bolt}$ |

---

# J-14

Note that the available slip resistance per bolt can also be determined using AISC *Manual* Table 7-3.

*Required Number of Bolts*

| LRFD | ASD |
|------|-----|
| $n_b = \frac{P_u}{\phi R_n}$ | $n_b = \frac{P_a}{\left(\frac{R_n}{\Omega}\right)}$ |
| $= \frac{102 \text{ kips}}{19.0 \text{ kips/bolt}}$ | $= \frac{68.0 \text{ kips}}{12.7 \text{ kips/bolt}}$ |
| $= 5.37 \text{ bolts}$ | $= 5.35 \text{ bolts}$ |
| Use 6 bolts | Use 6 bolts |

Note: Slip-critical connections shall be designed to prevent slip and for the limit states of bearing-type connections. To complete the verification of this connection, the limit states of bolt shear, bearing, tearout, tensile yielding, tensile rupture, and block shear rupture must also be checked.

---

# J-15

## EXAMPLE J.4B SLIP-CRITICAL CONNECTION WITH LONG-SLOTTED HOLES

**Given:**

Repeat Example J.4A with the same loads, but assuming that the connection plates have long-slotted holes in the direction of the load as shown in Figure J.4B-1. Washers have been provided in accordance with the RCSC *Specification* Section 6.

![Diagram showing a bolted connection with two plates. Connection plates (NS/FS) with horizontal long-slotted holes on left side, members with standard holes on right side. 8 bolts shown in a 4×2 pattern (¾" dia. Group 120, slip-critical, Class A). Applied loads: $P_D = 17$ kips, $P_L = 51$ kips.]

*Fig. J.4B-1. Geometry and loading for Example J.4B.*

**Solution:**

The required strength from Example J.4A is:

| LRFD | ASD |
|------|-----|
| $P_u = 102 \text{ kips}$ | $P_a = 68.0 \text{ kips}$ |

From AISC *Specification* Section J3.9(c), the available slip resistance for the limit state of slip for long-slotted holes is determined as follows:

- $\phi = 0.70$
- $\Omega = 2.14$
- $\mu = 0.30$ for Class A surface
- $D_u = 1.13$
- $h_f = 1.0$, no filler is provided
- $T_b = 28$ kips, from AISC *Specification* Table J3.1, Group 120
- $n_s = 2$, number of slip planes

$$R_n = \mu D_u h_f T_b n_s$$
$(Spec. \text{ Eq. J3-4})$

$$= 0.30(1.13)(1.0)(28 \text{ kips})(2)$$

$$= 19.0 \text{ kips/bolt}$$

The available slip resistance per bolt is:

| LRFD | ASD |
|------|-----|
| $\phi R_n = 0.70(19.0 \text{ kips/bolt})$ | $\frac{R_n}{\Omega} = \frac{19.0 \text{ kips/bolt}}{2.14}$ |
| $= 13.3 \text{ kips/bolt}$ | $= 8.88 \text{ kips/bolt}$ |

---

# J-16

Note that the available slip resistance per bolt can also be taken from AISC *Manual* Table 7-3.

*Required Number of Bolts*

| LRFD | ASD |
|------|-----|
| $n_b = \frac{P_u}{\phi R_n}$ | $n_b = \frac{P_a}{\left(\frac{R_n}{\Omega}\right)}$ |
| $= \frac{102 \text{ kips}}{13.3 \text{ kips/bolt}}$ | $= \frac{68.0 \text{ kips}}{8.88 \text{ kips/bolt}}$ |
| $= 7.67 \text{ bolts}$ | $= 7.66 \text{ bolts}$ |
| Use 8 bolts | Use 8 bolts |

Note: To complete the verification of this connection, the limit states of bolt shear, bearing, tearout, tensile yielding, tensile rupture, and block shear rupture must be determined.

---

# J-17

## EXAMPLE J.5 COMBINED TENSION AND SHEAR IN A SLIP-CRITICAL CONNECTION

Because the pretension of a bolt in a slip-critical connection is used to create the clamping force that produces the shear strength of the connection, the available shear strength must be reduced for any load that produces tension in the connection.

**Given:**

The slip-critical bolt group shown in Figure J.5-1 is subjected to tension and shear. This example shows the design for bolt slip resistance only and assumes that the beams and plates are adequate to transmit the loads. Determine if the bolts are adequate.

![Diagram showing a tee stub connection with beam. 8 bolts (¾" dia. Group 120, slip-critical, Class A, std. holes) arranged in 2 rows. Loads shown: $P_D = 15$ kips, $P_L = 45$ kips applied at distance 5/4/3 from bolt centerline.]

*Fig. J.5-1. Geometry and loading for Example J.5.*

**Solution:**

From ASCE/SEI 7, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(15 \text{ kips}) + 1.6(45 \text{ kips})$ | $P_a = 15 \text{ kips} + 45 \text{ kips}$ |
| $= 90.0 \text{ kips}$ | $= 60.0 \text{ kips}$ |
| By geometry: | By geometry: |
| $T_u = \frac{4}{5}(90.0 \text{ kips})$ | $T_a = \frac{4}{5}(60.0 \text{ kips})$ |
| $= 72.0 \text{ kips}$ | $= 48.0 \text{ kips}$ |
| $V_u = \frac{3}{5}(90.0 \text{ kips})$ | $V_a = \frac{3}{5}(60.0 \text{ kips})$ |
| $= 54.0 \text{ kips}$ | $= 36.0 \text{ kips}$ |

*Available Bolt Tensile Strength*

The available tensile strength is determined from AISC *Specification* Section J3.7.

From AISC *Specification* Table J3.2 for Group 120 bolts, the nominal tensile stress is $F_{nt} = 90$ ksi. From AISC *Manual* Table 7-2, for a ¾ in. diameter bolt:

---

# J-18

$$A_b = 0.442 \text{ in.}^2$$

The nominal tensile strength is:

$$R_n = F_{nt} A_b$$
(from *Spec.* Eq. J3-1)

$$= (90 \text{ ksi})(0.442 \text{ in.}^2)$$

$$= 39.8 \text{ kips}$$

The available tensile strength is:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(39.8 \text{ kips/bolt}) > \frac{72.0 \text{ kips}}{8 \text{ bolts}}$ | $\frac{R_n}{\Omega} = \frac{39.8 \text{ kips/bolt}}{2.00} > \frac{48.0 \text{ kips}}{8 \text{ bolts}}$ |
| $= 29.9 \text{ kips/bolt} > 9.00 \text{ kips/bolt}$ **o.k.** | $= 19.9 \text{ kips/bolt} > 6.00 \text{ kips/bolt}$ **o.k.** |

Note that the available tensile strength per bolt can also be determined using AISC *Manual* Table 7-2.

*Available Slip Resistance per Bolt*

The available slip resistance for one bolt in standard size holes is determined using AISC *Specification* Section J3.9(a):

- $\phi = 1.00$
- $\Omega = 1.50$
- $\mu = 0.30$ for Class A surface
- $D_u = 1.13$
- $h_f = 1.0$, assuming no more than one filler
- $T_b = 28$ kips, from AISC *Specification* Table J3.1, Group 120
- $n_s = 1$, number of slip planes

| LRFD | ASD |
|------|-----|
| Determine the available slip resistance $(T_u = 0)$ of a bolt: | Determine the available slip resistance $(T_a = 0)$ of a bolt: |
| $\phi R_n = \phi \mu D_u h_f T_b n_s$ (from *Spec.* Eq. J3-4) | $\frac{R_n}{\Omega} = \frac{\mu D_u h_f T_b n_s}{\Omega}$ (from *Spec.* Eq. J3-4) |
| $= 1.00(0.30)(1.13)(1.0)(28 \text{ kips})(1)$ | $= \frac{0.30(1.13)(1.0)(28 \text{ kips})(1)}{1.50}$ |
| $= 9.49 \text{ kips/bolt}$ | $= 6.33 \text{ kips/bolt}$ |

Note that the available slip resistance for one bolt with a Class A faying surface can also be taken from AISC *Manual* Table 7-3.

*Available Slip Resistance of the Connection*

Because the slip-critical connection is subject to combined tension and shear, the available slip resistance is multiplied by a reduction factor provided in AISC *Specification* Section J3.10.

---

# J-19

| LRFD | ASD |
|------|-----|
| Slip-critical combined tension and shear factor: | Slip-critical combined tension and shear factor: |
| $k_{sc} = 1 - \frac{T_u}{D_u T_b n_b} \geq 0$ $(Spec. \text{ Eq. J3-5a})$ | $k_{sc} = 1 - \frac{1.5T_a}{D_u T_b n_b} \geq 0$ $(Spec. \text{ Eq. J3-5b})$ |
| $= 1 - \frac{72.0 \text{ kips}}{1.13(28 \text{ kips})(8)} > 0$ | $= 1 - \frac{1.5(48.0 \text{ kips})}{1.13(28 \text{ kips})(8)} > 0$ |
| $= 0.716$ | $= 0.716$ |
| $\phi R_n = \phi R_n k_{sc} n_b$ | $\frac{R_n}{\Omega} = \frac{R_n}{\Omega} k_{sc} n_b$ |
| $= (9.49 \text{ kips/bolt})(0.716)(8 \text{ bolts})$ | $= (6.33 \text{ kips/bolt})(0.716)(8 \text{ bolts})$ |
| $= 54.4 \text{ kips} > 54.0 \text{ kips}$ **o.k.** | $= 36.3 \text{ kips} > 36.0 \text{ kips}$ **o.k.** |

Note: The bolt group must still be checked for all applicable strength limit states for a bearing-type connection.

---

# J-20

## EXAMPLE J.6 BASE PLATE BEARING ON CONCRETE

**Given:**

As shown in Figure J.6-1, an ASTM A992/A992M column bears on a concrete pedestal with $f_c' = 3$ ksi. The space between the base plate and the concrete pedestal has grout with $f_c' = 4$ ksi. Verify the ASTM A572/A572M Grade 50 base plate will support the following loads in axial compression:

- $P_D = 115$ kips
- $P_L = 345$ kips

![Diagram showing a W12×96 column on a concrete pedestal with base plate. Dimensions shown: 24" concrete pedestal width, 22" base plate width (B), 24" pedestal height, 22" height (N), 12.7" column depth (d), 12.2" flange width ($b_f$).]

*Fig. J.6-1. Geometry for Example J.6.*

**Solution:**

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Column
ASTM A992/A992M
- $F_y = 50$ ksi

Base Plate
ASTM A572/A572M Grade 50
- $F_y = 50$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Column
W12×96
- $d = 12.7$ in.
- $b_f = 12.2$ in.
- $t_f = 0.900$ in.
- $t_w = 0.550$ in.

---

# J-21

From ASCE/SEI 7, Chapter 2, the required compressive strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(115 \text{ kips}) + 1.6(345 \text{ kips})$ | $P_a = 115 \text{ kips} + 345 \text{ kips}$ |
| $= 690 \text{ kips}$ | $= 460 \text{ kips}$ |

*Base Plate Dimensions*

Determine the required base plate area from AISC *Specification* Section J8, conservatively assuming bearing on the full area of the concrete support.

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.65$ | $\Omega_c = 2.31$ |
| $A_{1(req)} = \frac{P_u}{\phi_c 0.85 f_c'}$ (from *Spec.* Eq. J8-1) | $A_{1(req)} = \frac{\Omega_c P_a}{0.85 f_c'}$ (from *Spec.* Eq. J8-1) |
| $= \frac{690 \text{ kips}}{0.65(0.85)(3 \text{ ksi})}$ | $= \frac{2.31(460 \text{ kips})}{0.85(3 \text{ ksi})}$ |
| $= 416 \text{ in.}^2$ | $= 417 \text{ in.}^2$ |

Note: The strength of the grout has conservatively been neglected, as its strength is greater than that of the concrete pedestal.

Try a 22 in. × 22 in. base plate.

Verify $N \geq d + 2(3 \text{ in.})$ and $B \geq b_f + 2(3 \text{ in.})$ for the anchor rod pattern shown in Figure J.6-1:

$$d + 2(3 \text{ in.}) = 12.7 \text{ in.} + 2(3 \text{ in.})$$
$$= 18.7 \text{ in.} < 22 \text{ in.}$$ **o.k.**

$$b_f + 2(3 \text{ in.}) = 12.2 \text{ in.} + 2(3 \text{ in.})$$
$$= 18.2 \text{ in.} < 22 \text{ in.}$$ **o.k.**

Base plate area:

$$A_1 = NB$$
$$= (22 \text{ in.})(22 \text{ in.})$$
$$= 484 \text{ in.}^2 > 417 \text{ in.}^2$$ **o.k.** (conservatively compared to ASD value for $A_{1(req)}$)

Note: A square base plate with a square anchor rod pattern will be used to minimize the chance for field and shop problems.

*Concrete Bearing Strength*

Use AISC *Specification* Equation J8-2 because the base plate covers less than the full area of the concrete support.

Because the pedestal is square and the base plate is a concentrically located square, the full pedestal area is also the geometrically similar area. Therefore:

---

# J-22

$$A_2 = (24 \text{ in.})(24 \text{ in.})$$

$$= 576 \text{ in.}^2$$

The available bearing strength is:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.65$ | $\Omega_c = 2.31$ |
| $\phi_c P_p = \phi_c 0.85 f_c' A_1 \sqrt{\frac{A_2}{A_1}} \leq \phi_c 1.7 f_c' A_1$ | $\frac{P_p}{\Omega_c} = \frac{0.85 f_c' A_1}{\Omega_c} \sqrt{\frac{A_2}{A_1}} \leq \frac{1.7 f_c' A_1}{\Omega_c}$ |
| (from *Spec.* Eq. J8-2) | (from *Spec.* Eq. J8-2) |
| $= 0.65(0.85)(3 \text{ ksi})(484 \text{ in.}^2)\sqrt{\frac{576 \text{ in.}^2}{484 \text{ in.}^2}}$ | $= \frac{0.85(3 \text{ ksi})(484 \text{ in.}^2)}{2.31}\sqrt{\frac{576 \text{ in.}^2}{484 \text{ in.}^2}}$ |
| $\leq 0.65(1.7)(3 \text{ ksi})(484 \text{ in.}^2)$ | $\leq \frac{1.7(3 \text{ ksi})(484 \text{ in.}^2)}{2.31}$ |
| $= 875 \text{ kips} < 1{,}600 \text{ kips, use } 875 \text{ kips}$ | $= 583 \text{ kips} < 1{,}070 \text{ kips, use } 583 \text{ kips}$ |
| $875 \text{ kips} > 690 \text{ kips}$ **o.k.** | $583 \text{ kips} > 460 \text{ kips}$ **o.k.** |

Notes:
1. $A_2/A_1 \leq 4$; therefore, the upper limit in AISC *Specification* Equation J8-2 does not control.
2. As the area of the base plate approaches the area of concrete, the modifying ratio, $\sqrt{A_2/A_1}$, approaches unity and AISC *Specification* Equation J8-2 converges to AISC *Specification* Equation J8-1.

*Required Base Plate Thickness*

The base plate thickness is determined in accordance with AISC *Manual* Part 14.

$$m = \frac{N - 0.95d}{2}$$
$({Manual} \text{ Eq. 14-2})$

$$= \frac{22 \text{ in.} - 0.95(12.7 \text{ in.})}{2}$$

$$= 4.97 \text{ in.}$$

$$n = \frac{B - 0.8b_f}{2}$$
$({Manual} \text{ Eq. 14-3})$

$$= \frac{22 \text{ in.} - 0.8(12.2 \text{ in.})}{2}$$

$$= 6.12 \text{ in.}$$

$$n' = \frac{\sqrt{db_f}}{4}$$
$({Manual} \text{ Eq. 14-4})$

$$= \frac{\sqrt{(12.7 \text{ in.})(12.2 \text{ in.})}}{4}$$

$$= 3.11 \text{ in.}$$

---

# J-23

| LRFD | ASD |
|------|-----|
| $X = \left[\frac{4db_f}{(d+b_f)^2}\right]\frac{P_u}{\phi_c P_p}$ (from *Manual* Eq. 14-6) | $X = \left[\frac{4db_f}{(d+b_f)^2}\right]\frac{\Omega_c P_a}{P_p}$ (from *Manual* Eq. 14-6) |
| $= \left[\frac{4(12.7 \text{ in.})(12.2 \text{ in.})}{(12.7 \text{ in.}+12.2 \text{ in.})^2}\right]\left(\frac{690 \text{ kips}}{875 \text{ kips}}\right)$ | $= \left[\frac{4(12.7 \text{ in.})(12.2 \text{ in.})}{(12.7 \text{ in.}+12.2 \text{ in.})^2}\right]\left(\frac{460 \text{ kips}}{583 \text{ kips}}\right)$ |
| $= 0.788$ | $= 0.789$ |

Conservatively, use the ASD value for $X$.

$$\lambda = \frac{2\sqrt{X}}{1 + \sqrt{1-X}} \leq 1$$
$({Manual} \text{ Eq. 14-5})$

$$= \frac{2\sqrt{0.789}}{1 + \sqrt{1-0.789}} \leq 1$$

$$= 1.22 > 1, \text{ use } \lambda = 1$$

Note: $\lambda$ can always be conservatively taken equal to 1.

$$\lambda n' = 1(3.11 \text{ in.})$$

$$= 3.11 \text{ in.}$$

$$l = \max\{m, n, \lambda n'\}$$

$$= \max\{4.97 \text{ in.}, 6.12 \text{ in.}, 3.11 \text{ in.}\}$$

$$= 6.12 \text{ in.}$$

| LRFD | ASD |
|------|-----|
| $f_{pu} = \frac{P_u}{BN}$ | $f_{pa} = \frac{P_a}{BN}$ |
| $= \frac{690 \text{ kips}}{(22 \text{ in.})(22 \text{ in.})}$ | $= \frac{460 \text{ kips}}{(22 \text{ in.})(22 \text{ in.})}$ |
| $= 1.43 \text{ ksi}$ | $= 0.950 \text{ ksi}$ |
| From AISC *Manual* Equation 14-7a: | From AISC *Manual* Equation 14-7b: |
| $t_{min} = l\sqrt{\frac{2f_{pu}}{0.90F_y}}$ | $t_{min} = l\sqrt{\frac{1.67(2f_{pa})}{F_y}}$ |
| $= (6.12 \text{ in.})\sqrt{\frac{2(1.43 \text{ ksi})}{0.90(50 \text{ ksi})}}$ | $= (6.12 \text{ in.})\sqrt{\frac{1.67(2)(0.950 \text{ ksi})}{50 \text{ ksi}}}$ |
| $= 1.54 \text{ in.}$ | $= 1.54 \text{ in.}$ |

Use PL1⅝ in. × 22 in. × 1 ft 10 in., ASTM A572/A572M Grade 50.

---

# J-24

## EXAMPLE J.7 CONCENTRATED FORCES FOR BEAM BEARING ON GIRDER

**Given:**

A W18×50 beam is supported by a W24×55 girder as shown in Figure J.7-1. Determine the available strength of the W24×55 girder using applicable concentrated force limit states from AISC *Specification* Section J10 to verify if stiffeners are required. The geometry and loading of the girder are shown in Figure J.7-2. Assume the W18×50 beam is acceptable for the applied loads. Both the beam and girder are ASTM A992/A992M material.

![Diagram showing connection geometry with W18×50 beam supported on W24×55 girder. Full depth stiffener (NS/FS) shown at connection point.]

*Fig. J.7-1. Connection geometry for Example J.7.*

![Diagram showing loading on girder. W18×50 beam load ($R_D = 15$ kips, $R_L = 30$ kips) applied at 8'-0" from left support, total span 20'-0" (8'-0" + 12'-0").]

*Fig. J.7-2. Loading diagram for Example J.7.*

**Solution:**

From AISC *Manual* Table 2-4, the material properties are as follows:

Beam and girder
ASTM A992/A992M
- $F_y = 50$ ksi

---

# J-25

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Beam
W18×50
- $b_f = 7.50$ in.
- $t_f = 0.570$ in.

Girder
W24×55
- $b_f = 7.01$ in.
- $d = 23.6$ in.
- $h/t_w = 54.6$
- $k_{des} = 1.01$ in.
- $S_x = 114 \text{ in.}^3$
- $t_f = 0.505$ in.
- $t_w = 0.395$ in.

From ASCE/SEI, Chapter 2, the required strength is:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(15 \text{ kips}) + 1.6(30 \text{ kips})$ | $R_a = 15 \text{ kips} + 30 \text{ kips}$ |
| $= 66.0 \text{ kips}$ | $= 45.0 \text{ kips}$ |

Based on the loading condition, the W24×55 girder will need to be checked for the limit states of web local yielding, web local crippling, and web sidesway buckling.

*Web Local Yielding*

The available web local yielding strength is determined using AISC *Specification* Section J10.2. The concentrated force to be resisted is applied at a distance from the member end that is greater than the full nominal depth of the member. Therefore, AISC *Specification* Equation J10-2 applies.

$$R_n = F_{yw}t_w(5k + l_b)$$
$(Spec. \text{ Eq. J10-2})$

$$= (50 \text{ ksi})(0.395 \text{ in.})[5(1.01 \text{ in.}) + 7.50 \text{ in.}]$$

$$= 248 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
| $\phi R_n = 1.00(248 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{248 \text{ kips}}{1.50}$ |
| $= 248 \text{ kips} > 66.0 \text{ kips}$ **o.k.** | $= 165 \text{ kips} > 45.0 \text{ kips}$ **o.k.** |

Note that the available web local yielding strength can also be determined using AISC *Manual* Table 9-4.

*Web Local Crippling*

The available web local crippling strength is determined using AISC *Specification* Section J10.3. The concentrated compressive force to be resisted is applied at a distance from the member end greater than $d/2$, therefore AISC *Specification* Equation J10-4 applies.

$$Q_f = 1.0 \text{ for wide-flange sections}$$

---

# J-26

$$R_n = 0.80t_w^2\left[1 + 3\left(\frac{l_b}{d}\right)\left(\frac{t_w}{t_f}\right)^{1.5}\right]\sqrt{\frac{EF_{yw}t_f}{t_w}}Q_f$$
$(Spec. \text{ Eq. J10-4})$

$$= (0.80)(0.395 \text{ in.})^2\left[1 + 3\left(\frac{7.50 \text{ in.}}{23.6 \text{ in.}}\right)\left(\frac{0.395 \text{ in.}}{0.505 \text{ in.}}\right)^{1.5}\right]\sqrt{\frac{(29{,}000 \text{ ksi})(50 \text{ ksi})(0.505 \text{ in.})}{0.395 \text{ in.}}}(1.0)$$

$$= 282 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = 0.75(282 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{282 \text{ kips}}{2.00}$ |
| $= 212 \text{ kips} > 66.0 \text{ kips}$ **o.k.** | $= 141 \text{ kips} > 45.0 \text{ kips}$ **o.k.** |

Note that the available web local crippling strength can also be determined using AISC *Manual* Table 9-4.

*Web Sidesway Buckling*

The available web sidesway buckling strength is determined using AISC *Specification* Section J10.4. The required flexural strength of the girder is determined using AISC *Manual* Table 3-22, Case 8:

| LRFD | ASD |
|------|-----|
| $M_u = \frac{P_u ab}{l}$ | $M_a = \frac{P_a ab}{l}$ |
| $= \frac{(66.0 \text{ kips})(8 \text{ ft})(12 \text{ ft})}{20 \text{ ft}}(12 \text{ in./ft})$ | $= \frac{(45.0 \text{ kips})(8 \text{ ft})(12 \text{ ft})}{20 \text{ ft}}(12 \text{ in./ft})$ |
| $= 3{,}800 \text{ kip-in.}$ | $= 2{,}590 \text{ kip-in.}$ |

Because the beam is bolted to the top flange of the girder, the compression flange is restrained against rotation and AISC *Specification* Section J10.4(a) applies. Checking the limit from AISC *Specification* Section J10.4(a), where $L_b$ is the largest laterally unbraced length along either flange at the point of load:

$$\frac{(h/t_w)}{(L_b/b_f)} = \frac{54.6}{20 \text{ ft}(12 \text{ in./ft})/7.01 \text{ in.}}$$

$$= 1.59 < 2.3$$

Therefore, the limit state of web sidesway buckling applies. The yield moment of the girder is determined as follows:

$$M_y = F_y S_x$$

$$= (50 \text{ ksi})(114 \text{ in.}^3)$$

$$= 5{,}700 \text{ kip-in.}$$

| LRFD | ASD |
|------|-----|
| $\alpha_s = 1.0$ | $\alpha_s = 1.50$ |
| $\alpha_s M_u = 1.0(3{,}800 \text{ kip-in.})$ | $\alpha_s M_a = 1.5(2{,}590 \text{ kip-in.})$ |
| $= 3{,}800 \text{ kip-in.} < 5{,}700 \text{ kip-in.}$ | $= 3{,}890 \text{ kip-in.} < 5{,}700 \text{ kip-in}$ |

---

# J-27

| LRFD | ASD |
|------|-----|
| Because $\alpha_s M_u < M_y$: | Because $\alpha_s M_a < M_y$: |
| $C_r = 960{,}000$ ksi | $C_r = 960{,}000$ ksi |

$$h = t_w(h/t_w)$$

$$= (0.395 \text{ in.})(54.6)$$

$$= 21.6 \text{ in.}$$

$$R_n = \frac{C_r t_w^3 t_f}{h^2}\left[1 + 0.4\left(\frac{h/t_w}{L_b/b_f}\right)^3\right]$$
$(Spec. \text{ Eq. J10-6})$

$$= \frac{(960{,}000 \text{ ksi})(0.395 \text{ in.})^3(0.505 \text{ in.})}{(21.6 \text{ in.})^2}\left[1 + 0.4(1.59)^3\right]$$

$$= 167 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.85$ | $\Omega = 1.76$ |
| $\phi R_n = 0.85(167 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{167 \text{ kips}}{1.76}$ |
| $= 142 \text{ kips} > 66.0 \text{ kips}$ | $= 94.9 \text{ kips} > 45.0 \text{ kips}$ |

*Summary*

Stiffeners are not required for the W24×55 girder due to loading from the W18×50 beam.

---

# J-28

---
