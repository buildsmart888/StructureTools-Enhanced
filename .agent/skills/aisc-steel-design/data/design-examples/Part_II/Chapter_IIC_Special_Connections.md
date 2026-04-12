# Chapter IIC: Special Connections

**AISC Specification v16.0 - Design Examples**
**Original PDF Pages**: 879-912 (34 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Bracing and Truss Connections

**Examples Included**: ['II.C-1~II.C-3: Special connection examples']

---

## Table of Contents

- [EXAMPLE II.C-1 TRUSS SUPPORT CONNECTION](#example-iic-1-truss-support-connection)
- [EXAMPLE II.C-2 TRUSS SUPPORT CONNECTION](#example-iic-2-truss-support-connection)
- [EXAMPLE II.C-3 HEAVY WIDE-FLANGE COMPRESSION CONNECTION (FLANGES ON THE OUTSIDE)](#example-iic-3-heavy-wide-flange-compression-connection-(flanges-on-the-outside))

---

# IIC-1

# Chapter IIC
# Bracing and Truss Connections

The design of bracing and truss connections is covered in Part 13 of the AISC *Steel Construction Manual*.

---

# IIC-2

## EXAMPLE II.C-1 TRUSS SUPPORT CONNECTION

**Given:**

The truss end connection shown in Figure II.C-1-1 is designed for the required forces shown in Figure II.C-1-2. Verify the following:

a. The connection requirements between the gusset and the column
b. The required gusset size and the weld requirements connecting the diagonal to the gusset

Use 70-ksi electrodes. The top chord and column are ASTM A992/A992M material. The diagonal member, gusset plate, and clip angles are ASTM A572/A572M Grade 50 material.

![Complex truss connection diagram showing:
- Top: W12×50 column with 6⅛" and ½" dimensions
- Left inset: Section A-A showing 4½", 2", 2" and various hole spacing details with 1½" and 1¼" dimensions
- Main diagram: Detailed connection showing:
  - Horizontal line through w.p. notation
  - 2L4×4×⅝×1'-3" members
  - WT8×38.5 section
  - Various angles and dimensions including 2⅝", 1-0", 4", 1⅛"
  - CJP, grind for fit up of angles notation
  - PL½×12×1'-3" gusset plate
  - 2L4×3½×⅜ (LLBB) members
  - Multiple dimensional callouts including 1'-3", 1.63", 8, 12, 91/16"
  - ⅞" dia. Group 120, thread condition N, std. holes notation
  - Various weld symbols (¼, ½)]

*Fig. II.C-1-1. Truss support connection.*

---

# IIC-3

![Force diagram showing:
- Top: "CL column" with horizontal force "131 kips LRFD, 87.2 kips ASD" pointing to "CL chord"
- Middle: "w.p." notation and gusset plate outline
- Left: Vertical force "106 kips LRFD, 70.4 kips ASD"
- Diagonal: Force "168 kips LRFD, 112 kips ASD" pointing to "CL brace"]

*Fig. II.C-1-2. Required forces in members.*

**Solution:**

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

Column and top chord
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Diagonal, gusset plate, and clip angles
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Tables 1-1, 1-7, 1-8, and 1-15, the geometric properties are as follows:

Top chord
WT8×38.5
$d = 8.26$ in.
$t_w = 0.455$ in.
$\overline{y} = 1.63$ in.

Column
W12×50
$d = 12.2$ in.
$t_f = 0.640$ in.
$b_f = 8.08$ in.
$t_w = 0.370$ in.

Diagonal brace
2L4×3½×⅝
$t = ⅝$ in.
$A = 5.36$ in.$^2$
$\overline{x} = 0.947$ in. for single angle

---

# IIC-4

Clip angles
2L4×4×⅝
$t = ⅝$ in.

From Figure II.C-1-2 the required strengths are:

| LRFD | ASD |
|------|-----|
| Brace axial load: | Brace axial load: |
|  |  |
| $R_u = 168$ kips | $R_a = 112$ kips |
|  |  |
| Truss end reaction: | Truss end reaction: |
|  |  |
| $R_u = 106$ kips | $R_a = 70.4$ kips |
|  |  |
| Top chord axial load: | Top chord axial load: |
|  |  |
| $R_u = 131$ kips | $R_a = 87.2$ kips |

*Weld Connecting the Diagonal to the Gusset Plate*

Note: AISC *Specification* Section J1.7, requiring that the center of gravity of the weld group coincide with the center of gravity of the member, does not apply to end connections of statically loaded single-angle, double-angle, and similar members.

From AISC *Specification* Table J2.4, the minimum fillet weld size for ⅝ in. angles attached to a ½-in.-thick gusset plate is:

$w_{min} = \frac{3}{16}$ in.

For ¼ in. fillet welds ($D = 4$), the required weld length is determined from AISC *Manual* Equations 8-2a or 8-2b, as follows:

| LRFD | ASD |
|------|-----|
| $l_{req} = \frac{R_u}{(4 \text{ welds})(1.392 \text{ kip/in.})(D)}$ | $l_{req} = \frac{R_a}{(4 \text{ welds})(0.928 \text{ kip/in.})(D)}$ |
|  |  |
| $= \frac{168 \text{ kips}}{(4 \text{ welds})(1.392 \text{ kip/in.})(4)}$ | $= \frac{112 \text{ kips}}{(4 \text{ welds})(0.928 \text{ kip/in.})(4)}$ |
| $= 7.54$ in. | $= 7.54$ in. |

Use an 8-in.-long ¼ in. fillet weld at the heel and toe of each angle.

*Gusset Shear Rupture at Brace Welds*

The minimum plate thickness to match the shear rupture strength of the welds is determined as follows:

$$t_{min} = \frac{6.19D}{F_u}$$ (*Manual* Eq. 9-7)

$$= \frac{6.19(4)}{65 \text{ ksi}}$$
$$= 0.381$$

---

# IIC-5

Try a ½-in.-thick gusset plate.

*Tensile Strength of the Brace*

From AISC *Specification* Section D2, the available tensile yielding strength of the brace is determined as follows:

$$P_n = F_y A_g$$ (*Spec.* Eq. D2-1)
$$= (50 \text{ ksi})\left(5.36 \text{ in.}^2\right)$$
$$= 268 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi_t = 0.90$ | $\Omega_t = 1.67$ |
|  |  |
| $\phi_t P_n = 0.90(268 \text{ kips})$ | $\frac{P_n}{\Omega_t} = \frac{268 \text{ kips}}{1.67}$ |
| $= 241 \text{ kips} > 168 \text{ kips} \quad \textbf{o.k.}$ | $= 160 \text{ kips} > 112 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section D2, the available tensile rupture strength of the brace is determined as follows:

$$A_n = A_g$$
$$= 5.36 \text{ in.}^2$$

The shear lag factor, $U$, is determined from AISC *Specification* Table D3.1, Case 4:

$$U = \frac{3l^2}{3l^2 + w^2}\left(1 - \frac{\overline{x}}{l}\right)$$

$$= \frac{3(8 \text{ in.})^2}{3(8 \text{ in.})^2 + (4 \text{ in.})^2}\left(1 - \frac{0.947 \text{ in.}}{8 \text{ in.}}\right)$$

$$= 0.814$$

$$A_e = A_n U$$ (*Spec.* Eq. D3-1)
$$= \left(5.36 \text{ in.}^2\right)(0.814)$$
$$= 4.36 \text{ in.}^2$$

$$P_n = F_u A_e$$ (*Spec.* Eq. D2-2)
$$= (65 \text{ ksi})\left(4.36 \text{ in.}^2\right)$$
$$= 283 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi_t = 0.75$ | $\Omega_t = 2.00$ |
|  |  |
| $\phi_t P_n = 0.75(283 \text{ kips})$ | $\frac{P_n}{\Omega_t} = \frac{283 \text{ kips}}{2.00}$ |
| $= 212 \text{ kips} > 168 \text{ kips} \quad \textbf{o.k.}$ | $= 142 \text{ kips} > 112 \text{ kips} \quad \textbf{o.k.}$ |

---

# IIC-6

Use a ½-in.-thick gusset plate. With the brace-to-gusset welds determined, a gusset plate layout as shown in Figure II.C-1-1 can be made.

*Strength of the Bolted Connection—Angles*

From AISC *Specification* Section J3.7 Commentary, the strength of the bolt group is taken as the sum of the individual strengths of the individual fasteners, which may be taken as the lesser of the fastener shear strength per AISC *Specification* Section J3.7, the bearing strength at the bolt hole per AISC *Specification* Section J3.11, or the tearout strength at the bolt hole per AISC *Specification* Section J3.11.

The number of ⅞-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) required for shear only is determined as follows:

| LRFD | ASD |
|------|-----|
| From AISC *Manual* Table 7-1, the available bolt shear strength is: | From AISC *Manual* Table 7-1, the available bolt shear strength is: |
|  |  |
| $\phi r_n = 24.3$ kips/bolt | $\frac{r_n}{\Omega} = 16.2$ kips/bolt |
|  |  |
| $n_{min} = \frac{R_u}{(2 \text{ bolts/row})\phi r_n}$ | $n_{min} = \frac{R_a}{(2 \text{ bolts/row})(r_n/\Omega)}$ |
|  |  |
| $= \frac{106 \text{ kips}}{(2 \text{ bolts/row})(24.3 \text{ kips/bolt})}$ | $= \frac{70.4 \text{ kips}}{(2 \text{ bolts/row})(16.2 \text{ kips/bolt})}$ |
| $= 2.18$ rows | $= 2.17$ rows |

Use 2L4×4×⅝ clip angles with five pairs of bolts. Note the number of rows of bolts is increased to "square off" the gusset plate.

The available bearing strength of the angles per bolt is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration:

$$r_n = 2.4dtF_u$$ (*Spec.* Eq. J3-6a)
$$= 2.4(⅞ \text{ in.})(⅝ \text{ in.})(65 \text{ ksi})$$
$$= 85.3 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(85.3 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{85.3 \text{ kips/bolt}}{2.00}$ |
| $= 63.9$ kips/bolt | $= 42.7$ kips/bolt |

The available tearout strength of the angles at edge bolts is determined from AISC *Specification* Section J3.11a, with $d_h = \frac{15}{16}$ in. for ⅞-in.-diameter bolts from AISC *Specification* Table J3.3, assuming deformation at service load is a design consideration:

$$l_c = l_e - 0.5d_h$$
$$= 1½ \text{ in.} - 0.5(\frac{15}{16} \text{ in.})$$
$$= 1.03 \text{ in.}$$

---

# IIC-7

$$r_n = 1.2l_c tF_u$$ (*Spec.* Eq. J3-6c)
$$= 1.2(1.03 \text{ in.})(⅝ \text{ in.})(65 \text{ ksi})$$
$$= 50.2 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(50.2 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{50.2 \text{ kips/bolt}}{2.00}$ |
| $= 37.7$ kips/bolt | $= 25.1$ kips/bolt |

Therefore, bolt shear controls over bolt bearing or tearout at the edge bolts.

The available tearout strength of the angles at interior bolts is determined from AISC *Specification* Section J3.11a, assuming deformation at service load is a design consideration:

$$l_c = s - d_h$$
$$= 3 \text{ in.} - \frac{15}{16} \text{ in.}$$
$$= 2.06 \text{ in.}$$

$$r_n = 1.2l_c tF_u$$ (*Spec.* Eq. J3-6c)
$$= 1.2(2.06 \text{ in.})(⅝ \text{ in.})(65 \text{ ksi})$$
$$= 100 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi r_n = 0.75(100 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{100 \text{ kips/bolt}}{2.00}$ |
| $= 75.0$ kips/bolt | $= 50.0$ kips/bolt |

Therefore, bolt shear controls over bolt bearing or tearout at the interior bolts.

The column flange thickness is greater than the angle thickness, therefore, the available bearing or tearout strength of the column flange will not control. Because bolt shear controls for all the bolts, the connection is acceptable based on previous calculations.

*Bolt Shear and Tension Interaction—Bolts Connecting Clip Angles to Column*

The eccentric moment about the work point (w.p.) at the faying surface (face of column flange) is determined using an eccentricity equal to half of the column depth.

$$e = \frac{d}{2}$$
$$= \frac{12.2 \text{ in.}}{2}$$
$$= 6.10 \text{ in.}$$

The eccentricity normal to the plane of the faying surface is accounted for using the Case II approach in AISC *Manual* Part 7 for eccentrically loaded bolt groups.

---

# IIC-8

$n' = 4$ bolts (number of bolts above the neutral axis)
$d_m = 9.00$ in. (moment arm between resultant force and resultant compressive force)

The maximum tensile force per bolt is determined using AISC *Manual* Equation 7-14, as follows:

| LRFD | ASD |
|------|-----|
| $r_{ut} = \frac{P_u e}{n' d_m}$ | $r_{ut} = \frac{P_a e}{n' d_m}$ |
|  |  |
| $= \frac{(106 \text{ kips})(6.10 \text{ in.})}{(4 \text{ bolts})(9.00 \text{ in.})}$ | $= \frac{(70.4 \text{ kips})(6.10 \text{ in.})}{(4 \text{ bolts})(9.00 \text{ in.})}$ |
| $= 18.0$ kips/bolt | $= 11.9$ kips/bolt |

The required shear stress per bolt is determined as follows:

$A_b = 0.601$ in.$^2$ (from AISC *Manual* Table 7-1)
$n = 10$ bolts

| LRFD | ASD |
|------|-----|
| $f_{rv} = \frac{R_u}{nA_b}$ | $f_{rv} = \frac{R_a}{nA_b}$ |
|  |  |
| $= \frac{106 \text{ kips}}{(10 \text{ bolts})(0.601 \text{ in.}^2)}$ | $= \frac{70.4 \text{ kips}}{(10 \text{ bolts})(0.601 \text{ in.}^2)}$ |
| $= 17.6$ ksi | $= 11.7$ ksi |

The nominal tensile strength modified to include the effects of shear stress is determined from AISC *Specification* Section J3.8 as follows. From AISC *Specification* Table J3.2:

$F_{nt} = 90$ ksi
$F_{nv} = 54$ ksi

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $F'_{nt} = 1.3F_{nt} - \frac{F_{nt}}{\phi F_{nv}}f_{rv} \leq F_{nt}$ (*Spec.* Eq. J3-3a) | $F'_{nt} = 1.3F_{nt} - \frac{\Omega F_{nt}}{F_{nv}}f_{rv} \leq F_{nt}$ (*Spec.* Eq. J3-3b) |
|  |  |
| $= 1.3(90 \text{ ksi}) - \frac{90 \text{ ksi}}{0.75(54 \text{ ksi})}(17.6 \text{ ksi}) \leq 90 \text{ ksi}$ | $= 1.3(90 \text{ ksi}) - \frac{2.00(90 \text{ ksi})}{54 \text{ ksi}}(11.7 \text{ ksi}) \leq 90 \text{ ksi}$ |
| $= 77.9$ ksi $< 90$ ksi | $= 78.0$ ksi $< 90$ ksi |
|  |  |
| Therefore: | Therefore: |
|  |  |
| $F'_{nt} = 77.9$ ksi | $F'_{nt} = 78.0$ ksi |
|  |  |
| $T_c = \phi F'_{nt} A_b$ (from *Spec.* Eq. J3-2) | $T_c = \frac{F'_{nt}}{\Omega}A_b$ (from *Spec.* Eq. J3-2) |
| $= 0.75(77.9 \text{ ksi})(0.601 \text{ in.}^2)$ | $= \frac{78.0 \text{ ksi}}{2.00}(0.601 \text{ in.}^2)$ |
| $= 35.1$ kips/bolt $> 18.0$ kips/bolt **o.k.** | $= 23.4$ kips/bolt $> 11.9$ kips/bolt **o.k.** |

---

# IIC-9

*Prying Action on Clip Angles*

From AISC *Manual* Part 9, the available tensile strength of the bolts in the outstanding angle legs taking prying action into account is determined as follows:

$$a = \frac{b_f - gage}{2}$$
$$= \frac{8.08 \text{ in.} - 4½ \text{ in.}}{2}$$
$$= 1.79 \text{ in.}$$

Note: $a$ is calculated based on the column flange width in this case because it is less than the double angle width.

$$b = \frac{gage - t_p - t}{2}$$
$$= \frac{4½ \text{ in.} - ½ \text{ in.} - ⅝ \text{ in.}}{2}$$
$$= 1.69 \text{ in.}$$

Note: 1¼ in. entering and tightening clearance from AISC *Manual* Table 7-15 is accommodated, and the column fillet toe is cleared.

$$a' = a + \frac{d}{2} \leq 1.25b + \frac{d}{2}$$ (from *Manual* Eq. 9-23)
$$= 1.79 \text{ in.} + \frac{⅞ \text{ in.}}{2} \leq 1.25(1.69 \text{ in.}) + \frac{⅞ \text{ in.}}{2}$$
$$= 2.23 \text{ in.} < 2.55 \text{ in.} \quad \textbf{o.k.}$$

$$b' = b - \frac{d}{2}$$ (*Manual* Eq. 9-24)
$$= 1.69 \text{ in.} - \frac{⅞ \text{ in.}}{2}$$
$$= 1.25 \text{ in.}$$

$$\rho = \frac{b'}{a'}$$ (*Manual* Eq. 9-29)
$$= \frac{1.25 \text{ in.}}{2.23 \text{ in.}}$$
$$= 0.561$$

$$p = \frac{l}{n}$$
$$= \frac{15 \text{ in.}}{5}$$
$$= 3.00 \text{ in.}$$

Check that $p \leq s$:
$p \leq s$
3.00 in. = 3.00 in. **o.k.**

---

# IIC-10

$$\delta = 1 - \frac{d'}{p}$$ (*Manual* Eq. 9-28)
$$= 1 - \frac{\frac{15}{16} \text{ in.}}{3.00 \text{ in.}}$$
$$= 0.688$$

The angle thickness required to develop the available strength of the bolt with no prying action is determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
|  |  |
| $T_c = 35.1$ kips/bolt (calculated previously) | $T_c = 23.4$ kips/bolt (calculated previously) |
|  |  |
| $t_c = \sqrt{\frac{4T_c b'}{\phi_b pF_u}}$ (*Manual* Eq. 9-30a) | $t_c = \sqrt{\frac{4\Omega_b T_c b'}{pF_u}}$ (*Manual* Eq. 9-30b) |
|  |  |
| $= \sqrt{\frac{4(35.1 \text{ kips/bolt})(1.25 \text{ in.})}{0.90(3.00 \text{ in.})(65 \text{ ksi})}}$ | $= \sqrt{\frac{4(1.67)(23.4 \text{ kips/bolt})(1.25 \text{ in.})}{(3.00 \text{ in.})(65 \text{ ksi})}}$ |
| $= 1.00$ in. | $= 1.00$ in. |

$$\alpha' = \frac{1}{\delta(1+\rho)}\left[\left(\frac{t_c}{t}\right)^2 - 1\right]$$ (*Manual* Eq. 9-38)

$$= \frac{1}{0.688(1+0.561)}\left[\left(\frac{1.00 \text{ in.}}{⅝ \text{ in.}}\right)^2 - 1\right]$$

$$= 1.45$$

Because $\alpha' > 1$, the angles have insufficient strength to develop the bolt strength, therefore:

$$Q = \left(\frac{t}{t_c}\right)^2(1+\delta)$$ (*Manual* Eq. 9-39c)

$$= \left(\frac{⅝ \text{ in.}}{1.00 \text{ in.}}\right)^2(1+0.688)$$

$$= 0.659$$

The available tensile strength per bolt, taking prying action into account, is determined using AISC *Manual* Equation 9-40, as follows:

| LRFD | ASD |
|------|-----|
| $\phi r_n = T_{c, \, adj}$ | $\frac{r_n}{\Omega} = T_{c, \, adj}$ |
| $= QT_c$ | $= QT_c$ |
| $= (0.659)(35.1 \text{ kips/bolt})$ | $= (0.659)(23.4 \text{ kips/bolt})$ |
| $= 23.1$ kips/bolt $> 18.0$ kips/bolt **o.k.** | $= 15.4$ kips/bolt $> 11.9$ kips/bolt **o.k.** |

---

# IIC-11

*Shear Strength of Clip Angles*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the angles is determined as follows:

$$A_{gv} = (2 \text{ angles})lt$$
$$= (2 \text{ angles})(15 \text{ in.})(⅝ \text{ in.})$$
$$= 18.8 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})\left(18.8 \text{ in.}^2\right)$$
$$= 564 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(564 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{564 \text{ kips}}{1.50}$ |
| $= 564 \text{ kips} > 106 \text{ kips} \quad \textbf{o.k.}$ | $= 376 \text{ kips} > 70.4 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.2, the available shear rupture strength of the angles is determined using the net area determined in accordance with AISC *Specification* Section B4.3b.

$$A_{nv} = (2 \text{ angles})\left[l - n\left(d_h + \frac{1}{16} \text{ in.}\right)\right]t$$
$$= (2 \text{ angles})\left[15 \text{ in.} - 5(\frac{15}{16} \text{ in.} + \frac{1}{16} \text{ in.})\right](⅝ \text{ in.})$$
$$= 12.5 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})\left(12.5 \text{ in.}^2\right)$$
$$= 488 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(488 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{488 \text{ kips}}{2.00}$ |
| $= 366 \text{ kips} > 106 \text{ kips} \quad \textbf{o.k.}$ | $= 244 \text{ kips} > 70.4 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture of Clip Angles*

The available strength for the limit state of block shear rupture of the angles is determined as follows.

$$R_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$ (*Spec.* Eq. J4-5)

where

---

# IIC-12

$$A_{gv} = (2 \text{ angles})(l - l_{ev})t$$
$$= (2 \text{ angles})(15 \text{ in.} - 1½ \text{ in.})(⅝ \text{ in.})$$
$$= 16.9 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (2 \text{ angles})(n - 0.5)(d_h + \frac{1}{16} \text{ in.})t$$
$$= 16.9 \text{ in.}^2 - (2 \text{ angles})(5 - 0.5)(\frac{15}{16} \text{ in.} + \frac{1}{16} \text{ in.})(⅝ \text{ in.})$$
$$= 11.3 \text{ in.}^2$$

$$A_{nt} = (2 \text{ angles})\left[l_{eh} - 0.5(d_h + \frac{1}{16} \text{ in.})\right]t$$
$$= (2 \text{ angles})\left[2 \text{ in.} - 0.5(\frac{15}{16} \text{ in.} + \frac{1}{16} \text{ in.})\right](⅝ \text{ in.})$$
$$= 1.88 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and
$$R_n = 0.60(65 \text{ ksi})\left(11.3 \text{ in.}^2\right) + 1.0(65 \text{ ksi})\left(1.88 \text{ in.}^2\right) \leq 0.60(50 \text{ ksi})\left(16.9 \text{ in.}^2\right) + 1.0(65 \text{ ksi})\left(1.88 \text{ in.}^2\right)$$
$$= 563 \text{ kips} < 629 \text{ kips}$$

Therefore:
$R_n = 563$ kips

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(563 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{563 \text{ kips}}{2.00}$ |
| $= 422 \text{ kips} > 106 \text{ kips} \quad \textbf{o.k.}$ | $= 282 \text{ kips} > 70.4 \text{ kips} \quad \textbf{o.k.}$ |

*Prying Action on Column Flange*

Using the same procedure as shown previously for the clip angles, the available tensile strength of the bolts, taking prying action into account, is:

| LRFD | ASD |
|------|-----|
| $T_c = 18.7$ kips $> 18.0$ kips **o.k.** | $T_c = 12.4$ kips $> 11.9$ kips **o.k.** |

*Clip Angle-to-Gusset Plate Connection*

With a top chord slope of ½ in 12, the horizontal welds are unequal length as shown in Figure II.C-1-3. The average horizontal length is used in the following calculations.

$l = 15$ in.

$$kl = \frac{3⅜ \text{ in.} + 2¼ \text{ in.}}{2}$$
$$= 3.06$$

---

# IIC-13

$$k = \frac{kl}{l}$$
$$= \frac{3.06 \text{ in.}}{15 \text{ in.}}$$
$$= 0.204$$

$$xl = \frac{(kl)^2}{l + 2(kl)}$$

$$= \frac{(3.06 \text{ in.})^2}{15 \text{ in.} + 2(3.06 \text{ in.})}$$
$$= 0.443 \text{ in.}$$

$$al + xl = 6.10 \text{ in.} + 4.00 \text{ in.}$$
$$= 10.1 \text{ in.}$$

$$a = \frac{10.1 \text{ in.} - xl}{l}$$
$$= \frac{10.1 \text{ in.} - 0.443 \text{ in.}}{15 \text{ in.}}$$
$$= 0.644$$

By interpolating AISC *Manual* Table 8-8 with Angle = 0°:

$C = 1.50$

![Weld group geometry diagram showing:
- Top: 3⅜" horizontal dimension
- Force Ru pointing right
- Center: Rectangle with dimensions al = 9.66", xl = 0.443", l = 15"
- Bottom: 2¼" horizontal dimension]

*Fig. II.C-1-3. Weld group geometry.*

---

# IIC-14

From AISC *Manual* Table 8-8, the minimum required weld size is determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $D_{min} = \frac{R_u}{(2 \text{ welds})\phi CCil}$ | $D_{min} = \frac{\Omega R_a}{(2 \text{ welds})CCil}$ |
|  |  |
| $= \frac{106 \text{ kips}}{(2 \text{ welds})(0.75)(1.50)(1.0)(15 \text{ in.})}$ | $= \frac{2.00(70.4 \text{ kips})}{2(1.50)(1.0)(15 \text{ in.})}$ |
| $= 3.14$ | $= 3.13$ |
|  |  |
| Use ¼ in. fillet welds. | Use ¼ in. fillet welds. |

From AISC *Specification* Table J2.4, the minimum weld size for ⅝ in. clip angles attached to a ½-in.-thick gusset plate is:

$w_{min} = \frac{3}{16}$ in. < ¼ in. **o.k.**

Note: Using the average of the horizontal weld lengths provides a reasonable solution when the horizontal welds are close in length. A conservative solution can be determined by using the smaller of the horizontal weld lengths as effective for both horizontal welds. For example, use $kl = 2¼$ in., $C = 1.43$, and $D_{min} = 3.29$ sixteenths.

*Tensile Yielding of Gusset Plate on the Whitmore Section*

The gusset plate thickness should match or slightly exceed that of the chord stem. This requirement is satisfied by the ½-in.-thick plate previously selected.

From AISC *Manual* Figure 9-1, the width of the Whitmore section is:

$l_w = 4.00 \text{ in.} + 2(8.00 \text{ in.})\tan 30°$
$= 13.2$ in.

From AISC *Specification* Section J4.1(a), the available tensile yielding strength of the gusset plate is determined as follows:

$$A_g = l_w t$$
$$= (13.2 \text{ in.})(½ \text{ in.})$$
$$= 6.60 \text{ in.}^2$$

$$R_n = F_y A_g$$ (*Spec.* Eq. J4-1)
$$= (50 \text{ ksi})\left(6.60 \text{ in.}^2\right)$$
$$= 330 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi R_n = 0.90(330 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{330 \text{ kips}}{1.67}$ |
| $= 297 \text{ kips} > 168 \text{ kips} \quad \textbf{o.k.}$ | $= 198 \text{ kips} > 112 \text{ kips} \quad \textbf{o.k.}$ |

---

# IIC-15

*Gusset Plate-to-Tee Stem Weld*

The interface forces are:

| LRFD | ASD |
|------|-----|
| Horizontal shear between gusset and WT: | Horizontal shear between gusset and WT: |
|  |  |
| $H_{ub} = 131 \text{ kips} - (4 \text{ bolts})(18.0 \text{ kips/bolt})$ | $H_{ab} = 87.2 \text{ kips} - (4 \text{ bolts})(11.9 \text{ kips/bolt})$ |
| $= 59.0$ kips | $= 39.6$ kips |
|  |  |
| Vertical tension between gusset and WT: | Vertical tension between gusset and WT: |
|  |  |
| $V_{ub} = (106 \text{ kips})\left(\frac{4 \text{ bolts}}{10 \text{ bolts}}\right)$ | $V_{ab} = (70.4 \text{ kips})\left(\frac{4 \text{ bolts}}{10 \text{ bolts}}\right)$ |
| $= 42.4$ kips | $= 28.2$ kips |
|  |  |
| Compression between WT and column: | Compression between WT and column: |
|  |  |
| $C_{ub} = (4 \text{ bolts})(18.0 \text{ kips/bolt})$ | $C_{ab} = (4 \text{ bolts})(11.9 \text{ kips/bolt})$ |
| $= 72.0$ kips | $= 47.6$ kips |
|  |  |
| Summing moments about the face of the column at the workline of the top chord: | Summing moments about the face of the column at the workline of the top chord: |
|  |  |
| $M_{ub} = C_{ub}\left(2½ \text{ in.} + 1.50 \text{ in.}\right)$ | $M_{ab} = C_{ab}\left(2½ \text{ in.} + 1.50 \text{ in.}\right)$ |
| $+ H_{ub}\left(d - \overline{y}\right)$ | $+ H_{ab}\left(d - \overline{y}\right)$ |
| $- V_{ub}\left(\frac{gusset \, width}{2} + setback\right)$ | $- V_{ab}\left(\frac{gusset \, width}{2} + setback\right)$ |
|  |  |
| $= (72.0 \text{ kips})(2½ \text{ in.} + 1.50 \text{ in.})$ | $= (47.6 \text{ kips})(2½ \text{ in.} + 1.50 \text{ in.})$ |
| $+ (59.0 \text{ kips})(8.26 \text{ in.} - 1.63 \text{ in.})$ | $+ (39.6 \text{ kips})(8.26 \text{ in.} - 1.63 \text{ in.})$ |
| $- (42.4 \text{ kips})\left(\frac{15.0 \text{ in.}}{2} + ½ \text{ in.}\right)$ | $- (28.2 \text{ kips})\left(\frac{15.0 \text{ in.}}{2} + ½ \text{ in.}\right)$ |
|  |  |
| $= 340$ kip-in. | $= 227$ kip-in. |

A CJP weld should be used along the interface between the gusset plate and the tee stem. The weld should be ground smooth under the clip angles.

The gusset plate width depends upon the diagonal connection. From a scaled layout, the gusset plate must be 1 ft 3 in. wide.

The gusset plate depth depends upon the connection angles. From a scaled layout, the gusset plate must extend 12 in. below the tee stem.

Use a PL½×12 in.×1 ft 3 in.

*Conclusion*

The connection is found to be adequate as given for the applied loads.

---

# IIC-16

## EXAMPLE II.C-2 TRUSS SUPPORT CONNECTION

**Given:**

Verify the truss support connections, as shown in Figure II.C-2-1, at the following joints:

A. Joint $L_1$
B. Joint $U_1$

Use 70-ksi electrodes. The top and bottom chords are ASTM A992/A992M material. The plate and double angles are ASTM A572/A572M Grade 50 material.

![Complex truss connection diagram showing:
- Top chord WT8×38.5
- Bottom chord WT8×28.5
- Forces: Pu = -30 kips, Pa = -20 kips at top
- Diagonal members: 2L4×3½×⅝ (LLBB) and 2L3½×2½×⅝ (LLBB)
- Gusset plate PL⅝×4×1'-10
- Various dimensions and bolt patterns
- CJP, grind only under angles notation
- Multiple angle measurements and member sizes
- Two joints labeled L1 and U1
- Forces shown: Pu = 104 kips, Pa = 69.2 kips
- Pu = -104 kips, Pa = -69.2 kips
- Detailed connection geometry with dimensions like 3⅛", 6½", 1⅛", 10⅝", etc.]

*Fig. II.C-2-1. Connection geometry for Example II.C-2.*

**Solution:**

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

---

# IIC-17

Top and bottom chord
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Web member, diagonal members, and plate
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Tables 1-7, 1-8, and 1-15, the geometric properties are as follows:

Top Chord
WT8×38.5
$t_w = 0.455$ in.
$d = 8.26$ in.

Bottom Chord
WT8×28.5
$t_w = 0.430$ in.
$d = 8.22$ in.

Diagonal $U_0L_1$
2L4×3½×⅝
$A = 5.36$ in.$^2$
$\overline{x} = 0.947$ in. (for single angle)

Web $U_1L_1$
2L3½×3×⅝
$A = 3.90$ in.$^2$

Diagonal $U_1L_2$
2L3½×2½×⅝
$A = 3.58$ in.$^2$
$\overline{x} = 0.632$ in. (for single angle)

As shown in Figure II.C-2-1, the required forces are:

| LRFD | ASD |
|------|-----|
| Web $U_1L_1$ load: | Web $U_1L_1$ load: |
|  |  |
| $P_u = -104$ kips | $P_a = -69.2$ kips |
|  |  |
| Diagonal $U_0L_1$ load: | Diagonal $U_0L_1$ load: |
|  |  |
| $T_u = +165$ kips | $T_a = +110$ kips |
|  |  |
| Diagonal $U_1L_2$ load: | Diagonal $U_1L_2$ load: |
|  |  |
| $T_u = +114$ kips | $T_a = +76$ kips |

**Solution A:**

---

# IIC-18

*Shear Yielding of Bottom Chord Stem*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the bottom chord at Section A-A (see Figure II.C-2-1) is determined as follows:

$$A_{gv} = dt_w$$
$$= (8.22 \text{ in.})(0.430 \text{ in.})$$
$$= 3.53 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})\left(3.53 \text{ in.}^2\right)$$
$$= 106 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(106 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{106 \text{ kips}}{1.50}$ |
| $= 106 \text{ kips} > 104 \text{ kips} \quad \textbf{o.k.}$ | $= 70.7 \text{ kips} > 69.2 \text{ kips} \quad \textbf{o.k.}$ |

*Welds for Member $U_1L_1$*

Note: AISC *Specification* Section J1.7 requiring that the center of gravity of the weld group coincide with the center of gravity of the member does not apply to end connections of statically loaded single angle, double angle, and similar members.

From AISC *Specification* Table J2.4, the minimum weld size for a $\frac{5}{16}$-in.-thick angle is:

$w_{min} = \frac{3}{16}$ in.

From AISC *Specification* Section J2.2b(b)(2), the maximum weld size is:

$$w_{max} = t - \frac{1}{16} \text{ in.}$$
$$= \frac{5}{16} - \frac{1}{16} \text{ in.}$$
$$= ¼ \text{ in.}$$

Try a $\frac{3}{16}$ in. fillet weld.

The minimum weld length is determined using AISC *Manual* Equation 8-2a or 8-2b:

| LRFD | ASD |
|------|-----|
| $l_{min} = \frac{R_u}{(2 \text{ sides})(2 \text{ welds})(1.392 \text{ kip/in.})D}$ | $l_{min} = \frac{R_a}{(2 \text{ sides})(2 \text{ welds})(0.928 \text{ kip/in.})D}$ |
|  |  |
| $= \frac{104 \text{ kips}}{(2 \text{ sides})(2 \text{ welds})(1.392 \text{ kip/in.})(3)}$ | $= \frac{69.2 \text{ kips}}{(2 \text{ sides})(2 \text{ welds})(0.928 \text{ kip/in.})(3)}$ |
| $= 6.23$ in. | $= 6.21$ in. |
|  |  |
| Use a 6½-in.-long weld at the heel and toe of the angles. | Use a 6½-in.-long weld at the heel and toe of the angles. |

---

# IIC-19

*Shear Rupture Strength of Angles at Welds*

The minimum angle thickness to match the required shear rupture strength of the welds is determined as follows:

$$t_{min} = \frac{3.09D}{F_u}$$ (*Manual* Eq. 9-6)
$$= \frac{3.09(3)}{65 \text{ ksi}}$$
$$= 0.143 \text{ in.} < \frac{5}{16} \text{ in.} \quad \textbf{o.k.}$$

*Shear Rupture Strength of Tee-Stem at Welds*

The minimum tee-stem thickness to match the required shear rupture strength of the welds is determined as follows:

$$t_{min} = \frac{6.19D}{F_u}$$ (*Manual* Eq. 9-7)
$$= \frac{6.19(3)}{65 \text{ ksi}}$$
$$= 0.286 \text{ in.} < 0.430 \text{ in.} \quad \textbf{o.k.}$$

Note, both the top and bottom chords are acceptable for $\frac{3}{16}$ in. fillet welds.

*Welds for Member $U_0L_1$*

From AISC *Specification* Table J2.4, the minimum weld size for a ⅝-in.-thick angle is:

$w_{min} = \frac{3}{16}$ in.

From AISC *Specification* Section J2.2b(b)(2), the maximum weld size is:

$$w_{max} = t - \frac{1}{16} \text{ in.}$$
$$= ⅝ - \frac{1}{16} \text{ in.}$$
$$= \frac{9}{16} \text{ in.}$$

Try a $\frac{3}{16}$ in. fillet weld.

The minimum weld length is determined using AISC *Manual* Equation 8-2a or 8-2b:

| LRFD | ASD |
|------|-----|
| $l_{min} = \frac{R_u}{(2 \text{ sides})(2 \text{ welds})(1.392 \text{ kip/in.})D}$ | $l_{min} = \frac{R_a}{(2 \text{ sides})(2 \text{ welds})(0.928 \text{ kip/in.})D}$ |
|  |  |
| $= \frac{165 \text{ kips}}{(2 \text{ sides})(2 \text{ welds})(1.392 \text{ kip/in.})(3)}$ | $= \frac{110 \text{ kips}}{(2 \text{ sides})(2 \text{ welds})(0.928 \text{ kip/in.})(3)}$ |
| $= 9.88$ in. | $= 9.88$ in. |
|  |  |
| Use a 10-in.-long weld at the heel and toe of the angles. | Use a 10-in.-long weld at the heel and toe of the angles. |

Note: A plate will be welded to the stem of the WT to provide room for the connection. Based on the preceding calculations for the minimum angle and stem thicknesses, by inspection the angles, stems, and stem plate extension have adequate strength.

*Tensile Strength of Diagonal $U_0L_1$*

---

# IIC-20

From AISC *Specification* Section D2, the available tensile yielding strength of the angles is determined as follows:

$$P_n = F_y A_g$$ (*Spec.* Eq. D2-1)
$$= (50 \text{ ksi})\left(5.36 \text{ in.}^2\right)$$
$$= 268 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi_t = 0.90$ | $\Omega_t = 1.67$ |
|  |  |
| $\phi_t P_n = 0.90(268 \text{ kips})$ | $\frac{P_n}{\Omega_t} = \frac{268 \text{ kips}}{1.67}$ |
| $= 241 \text{ kips} > 165 \text{ kips} \quad \textbf{o.k.}$ | $= 160 \text{ kips} > 110 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section D2, the available tensile rupture strength of the angles is determined as follows. The shear lag factor, $U$, is determined using AISC *Specification* Table D3.1, Case 4.

$$U = \frac{3l^2}{3l^2 + w^2}\left(1 - \frac{\overline{x}}{l}\right)$$

$$= \frac{3(10 \text{ in.})^2}{3(10 \text{ in.})^2 + (4 \text{ in.})^2}\left(1 - \frac{0.947 \text{ in.}}{10 \text{ in.}}\right)$$

$$= 0.859$$

$$P_n = F_u A_e$$ (*Spec.* Eq. D2-2)
$$= (65 \text{ ksi})\left(5.36 \text{ in.}^2\right)(0.859)$$
$$= 299 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi_t = 0.75$ | $\Omega_t = 2.00$ |
|  |  |
| $\phi_t P_n = 0.75(299 \text{ kips})$ | $\frac{P_n}{\Omega_t} = \frac{299 \text{ kips}}{2.00}$ |
| $= 224 \text{ kips} > 165 \text{ kips} \quad \textbf{o.k.}$ | $= 150 \text{ kips} > 110 \text{ kips} \quad \textbf{o.k.}$ |

*Block Shear Rupture of Bottom Chord*

The available strength for the limit state of block shear rupture of the chord is determined as follows.

$$R_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$ (*Spec.* Eq. J4-5)

where

$$A_{gv} = A_{nv}$$
$$= (2 \text{ lines})lt_w$$
$$= (2 \text{ lines})(10 \text{ in.})(0.430 \text{ in.})$$
$$= 8.60 \text{ in.}^2$$

---

# IIC-21

$$A_{nt} = (angle \, leg)t$$
$$= (4 \text{ in.})(0.430 \text{ in.})$$
$$= 1.72 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_n = 0.60(65 \text{ ksi})\left(8.60 \text{ in.}^2\right) + 1.0(65 \text{ ksi})\left(1.72 \text{ in.}^2\right) \leq 0.60(50 \text{ ksi})\left(8.60 \text{ in.}^2\right) + 1.0(65 \text{ ksi})\left(1.72 \text{ in.}^2\right)$$
$$= 447 \text{ kips} > 370 \text{ kips}$$

Therefore:
$R_n = 370$ kips

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(370 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{370 \text{ kips}}{2.00}$ |
| $= 278 \text{ kips} > 165 \text{ kips} \quad \textbf{o.k.}$ | $= 185 \text{ kips} > 110 \text{ kips} \quad \textbf{o.k.}$ |

**Solution B:**

*Shear Yielding of Top Chord Stem*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the top chord at Section B-B (see Figure II.C-2-1) is determined as follows:

$$A_{gv} = dt_w$$
$$= (8.26 \text{ in.})(0.455 \text{ in.})$$
$$= 3.76 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})\left(3.76 \text{ in.}^2\right)$$
$$= 113 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(113 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{113 \text{ kips}}{1.50}$ |
| $= 113 \text{ kips} > 74.0 \text{ kips} \quad \textbf{o.k.}$ | $= 75.3 \text{ kips} > 49.2 \text{ kips} \quad \textbf{o.k.}$ |

*Welds for Member $U_1L_1$*

As calculated previously in Solution A, use 6½-in.-long $\frac{3}{16}$ in. fillet welds at the heel and toe of both angles.

*Welds for Member $U_1L_2$*

---

# IIC-22

As determined in previous calculations, the minimum and maximum weld sizes for a $\frac{5}{16}$-in.-thick angle are:

$w_{min} = \frac{3}{16}$ in.
$w_{max} = ¼$ in.

Try a ¼ in. fillet weld.

To avoid having to use a stem extension plate, unequal length welds are provided at the heel and toe of the angle. The minimum weld length for each angle is determined using AISC *Manual* Equation 8-2a or 8-2b:

| LRFD | ASD |
|------|-----|
| $l_{min} = \frac{R_u}{(2 \text{ sides})(1.392 \text{ kip/in.})D}$ | $l_{min} = \frac{R_a}{(2 \text{ sides})(0.928 \text{ kip/in.})D}$ |
|  |  |
| $= \frac{114 \text{ kips}}{(2 \text{ sides})(1.392 \text{ kip/in.})(4)}$ | $= \frac{76 \text{ kips}}{(2 \text{ sides})(0.928 \text{ kip/in.})(4)}$ |
| $= 10.2$ in. | $= 10.2$ in. |

Try 7½ in. of ¼ in. fillet weld at the heel and 4 in. of ¼ in. fillet weld at the toe of each angle.

$$l = 7½ \text{ in.} + 4 \text{ in.}$$
$$= 11.5 \text{ in.} > 10.2 \text{ in.} \quad \textbf{o.k.}$$

*Shear Rupture Strength of Angles at Welds*

The minimum angle thickness to match the required shear rupture strength of the welds is determined as follows:

$$t_{min} = \frac{3.09D}{F_u}$$ (*Manual* Eq. 9-6)
$$= \frac{3.09(4)}{65 \text{ ksi}}$$
$$= 0.190 \text{ in.} < \frac{5}{16} \text{ in.} \quad \textbf{o.k.}$$

*Shear Rupture Strength of Tee-Stem at Welds*

The minimum tee-stem thickness to match the required shear rupture strength of the welds is determined as follows:

$$t_{min} = \frac{6.19D}{F_u}$$ (*Manual* Eq. 9-7)
$$= \frac{6.19(4)}{65 \text{ ksi}}$$
$$= 0.381 \text{ in.} < 0.455 \text{ in.} \quad \textbf{o.k.}$$

*Tensile Strength of Diagonal $U_1L_2$*

From AISC *Specification* Section J4.1(a), the available tensile yielding strength of the angles are determined as follows:

---

# IIC-23

$$R_n = F_y A_g$$ (*Spec.* Eq. J4-1)
$$= (50 \text{ ksi})\left(3.58 \text{ in.}^2\right)$$
$$= 179 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi R_n = 0.90(179 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{179 \text{ kips}}{1.67}$ |
| $= 161 \text{ kips} > 114 \text{ kips} \quad \textbf{o.k.}$ | $= 107 \text{ kips} > 76 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.1(b), the available tensile rupture strength of the angles is determined as follows. The shear lag factor, $U$, is determined using AISC *Specification* Table D3.1, Case 4.

$$l = \frac{l_1 + l_2}{2}$$
$$= \frac{7½ \text{ in.} + 4 \text{ in.}}{2}$$
$$= 5.75 \text{ in.}$$

$$U = \frac{3l^2}{3l^2 + w^2}\left(1 - \frac{\overline{x}}{l}\right)$$

$$= \frac{3(5.75 \text{ in.})^2}{3(5.75 \text{ in.})^2 + (3½ \text{ in.})^2}\left(1 - \frac{0.632 \text{ in.}}{5.75 \text{ in.}}\right)$$

$$= 0.792$$

$$R_n = F_u A_e$$ (*Spec.* Eq. J4-2)
$$= (65 \text{ ksi})\left(3.58 \text{ in.}^2\right)(0.792)$$
$$= 184 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(184 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{184 \text{ kips}}{2.00}$ |
| $= 138 \text{ kips} > 114 \text{ kips} \quad \textbf{o.k.}$ | $= 92.0 \text{ kips} > 76 \text{ kips} \quad \textbf{o.k.}$ |

*Conclusion*

Joints $L_1$ and $U_1$ are found to be adequate as given for the applied loads.

---

# IIC-24

## EXAMPLE II.C-3 HEAVY WIDE-FLANGE COMPRESSION CONNECTION (FLANGES ON THE OUTSIDE)

**Given:**

The truss shown in Figure II.C-3-1 has been designed with ASTM A992/A992M W14 shapes with flanges to the outside of the truss. Beams framing into the top chord and lateral bracing are not shown but can be assumed to be adequate.

Based on multiple load cases, the critical dead and live load forces for this connection are shown in Figure II.C-3-2. A typical top chord connection is shown in Figure II.C-3-1, Detail A. Design this typical connection using 1-in.-diameter, Group 120 slip-critical bolts in standard holes with threads not excluded from the shear plane (thread condition N) with Class A faying surfaces and ASTM A572/A572M Grade 50 gusset plates.

![Truss elevation diagram showing:
- Top: Warren truss with 10 equal spaces totaling 200'-0"
- Depth: 16'-8" at left, 16'-9½" at right
- Point A marked on top chord
- Detail A showing W14×109 top chord, W14×61 web member, W14×61 diagonal
- Plates and bolts to be determined
- Dimensions: ¼", 12", 3⅞", 11", 12", 10"]

*Fig II.C-3-1. Truss layout for Example II.C-3.*

![Force diagrams showing:
Left (Dead Load Force): PD = 24 kips, 262 kips horizontal, 102 kips vertical, 113 kips diagonal
Right (Live Load Force): PL = 24 kips, 345 kips horizontal, 102 kips vertical, 113 kips diagonal]

*Fig. II.C-3-2. Forces at Detail A.*

---

# IIC-25

**Solution:**

From AISC *Manual* Tables 2-4 and 2-5, the material properties are as follows:

W-shapes
ASTM A992/A992M
$F_y = 50$ ksi
$F_u = 65$ ksi

Gusset plates
ASTM A572/A572M Grade 50
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Top chord
W14×109
$d = 14.3$ in.
$b_f = 14.6$ in.
$t_f = 0.860$ in.

Web members
W14×61
$d = 13.9$ in.
$b_f = 10.0$ in.
$t_f = 0.645$ in.

From AISC *Specification* Table J3.3, for 1-in.-diameter bolts with standard holes:

$d_h = 1⅛$ in.

From ASCE/SEI 7, Chapter 2, the required strengths are determined as follows and summarized in Figure II.C-3-3.

| LRFD | ASD |
|------|-----|
| Left top chord: | Left top chord: |
|  |  |
| $P_u = 1.2(262 \text{ kips}) + 1.6(262 \text{ kips})$ | $P_a = 262 \text{ kips} + 262 \text{ kips}$ |
| $= 734$ kips | $= 524$ kips |
|  |  |
| Right top chord: | Right top chord: |
|  |  |
| $P_u = 1.2(345 \text{ kips}) + 1.6(345 \text{ kips})$ | $P_a = 345 \text{ kips} + 345 \text{ kips}$ |
| $= 966$ kips | $= 690$ kips |
|  |  |
| Vertical Web: | Vertical Web: |
|  |  |
| $P_u = 1.2(102 \text{ kips}) + 1.6(102 \text{ kips})$ | $P_a = 102 \text{ kips} + 102 \text{ kips}$ |
| $= 286$ kips | $= 204$ kips |

---

# IIC-26

| LRFD | ASD |
|------|-----|
| Diagonal Web: | Diagonal Web: |
|  |  |
| $P_u = 1.2(113 \text{ kips}) + 1.6(113 \text{ kips})$ | $P_a = 113 \text{ kips} + 113 \text{ kips}$ |
| $= 316$ kips | $= 226$ kips |

Note: In checking equilibrium of vertical forces, $\Sigma F_v \neq 0$, due to the external (loading) forces not included. Refer to Figure II.C-3-2 for the magnitude of external load forces. In most truss designs, member forces only are provided, and force equilibrium of the internal truss forces will not sum to zero.

*Bolt Slip Resistance Strength*

From AISC *Specification* Section J3.9(a), the available slip resistance for the limit state of slip for standard size holes is determined as follows:

$\phi = 1.00$
$\Omega = 1.50$
$\mu = 0.30$ for Class A surface
$D_u = 1.13$
$h_f = 1.0$, no filler is provided
$T_b = 51$ kips, from AISC *Specification* Table J3.1, Group 120
$n_s = 1$, number of slip planes

$$r_n = \mu D_u h_f T_b n_s$$ (*Spec.* Eq. J3-4)
$$= (0.30)(1.13)(1.0)(51 \text{ kips})(1)$$
$$= 17.3 \text{ kips/bolt}$$

| LRFD | ASD |
|------|-----|
| $\phi r_n = 1.00(17.3 \text{ kips/bolt})$ | $\frac{r_n}{\Omega} = \frac{17.3 \text{ kips/bolt}}{1.50}$ |
| $= 17.3$ kips/bolt | $= 11.5$ kips/bolt |

Alternatively, the available bolt slip resistance strength can be determined from AISC *Manual* Table 7-3.

Note: Standard holes are used in both plies for this example. Other hole sizes may be used and should be considered based on the preferences of the fabricator or erector on a case-by-case basis.

![Force diagrams showing:
Left (a) LRFD: -734 kips top, 233 kips right, -286 kips down, 214 kips diagonal, 316 kips diagonal
Right (b) ASD: -524 kips top, 166 kips right, -204 kips down, 153 kips diagonal, 226 kips diagonal]

*Fig. II.C-3-3. Required forces at Detail A.*

---

# IIC-27

*Diagonal Connection*

The required number of bolts is determined as follows:

| LRFD | ASD |
|------|-----|
| $P_u = 316$ kips | $P_a = 226$ kips |
|  |  |
| $n_{req} = \frac{P_u}{\phi r_n}$ | $n_{req} = \frac{\Omega P_a}{r_n}$ |
|  |  |
| $= \frac{316 \text{ kips}}{17.3 \text{ kips/bolt}}$ | $= \frac{226 \text{ kips}}{11.5 \text{ kips/bolt}}$ |
| $= 18.3$ bolts | $= 19.7$ bolts |
|  |  |
| For two lines of bolts on both sides, the required number of rows is: | For two lines of bolts on both sides, the required number of rows is: |
|  |  |
| $\frac{18.3 \text{ bolts}}{(2 \text{ sides})(2 \text{ lines})} = 4.58$ | $\frac{19.7 \text{ bolts}}{(2 \text{ sides})(2 \text{ lines})} = 4.93$ |
|  |  |
| Therefore, use five rows at min. 3 in. spacing. | Therefore, use five rows at min. 3 in. spacing. |

*Whitmore section in gusset plate*

The width of the Whitmore section, $l_w$, is determined as shown in AISC *Manual* Figure 9-1.

$$l_w = gage + 2l\tan 30°$$
$$= 5½ \text{ in.} + 2(12 \text{ in.})(\tan 30°)$$
$$= 19.4 \text{ in.}$$

Try a ⅝-in.-thick plate.

$$A_g = (2 \text{ plates})l_w t$$
$$= (2 \text{ plates})(19.4 \text{ in.})(⅝ \text{ in.})$$
$$= 14.6 \text{ in.}^2$$

From AISC *Specification* Section J4.1(a), the available tensile yielding strength of the gusset plate is determined as follows:

$$R_n = F_y A_g$$ (*Spec.* Eq. J4-1)
$$= (50 \text{ ksi})\left(14.6 \text{ in.}^2\right)$$
$$= 730 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
|  |  |
| $\phi R_n = 0.90(730 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{730 \text{ kips}}{1.67}$ |
| $= 657 \text{ kips} > 316 \text{ kips} \quad \textbf{o.k.}$ | $= 437 \text{ kips} > 226 \text{ kips} \quad \textbf{o.k.}$ |

---

# IIC-28

*Block shear rupture of gusset plate*

The available strength for the limit state of block shear rupture of the gusset plates is determined as follows.

$$R_n = 0.60F_u A_{nv} + U_{bs}F_u A_{nt} \leq 0.60F_y A_{gv} + U_{bs}F_u A_{nt}$$ (*Spec.* Eq. J4-5)

where

$$A_{gv} = (2 \text{ plates})(2 \text{ lines})\left[l_{ev} + (n-1)s\right]t$$
$$= (2 \text{ plates})(2 \text{ lines})\left[2 \text{ in.} + (5-1)(3 \text{ in.})\right](⅝ \text{ in.})$$
$$= 21.0 \text{ in.}^2$$

$$A_{nv} = A_{gv} - (2 \text{ plates})(2 \text{ lines})(5 - 0.5)(d_h + \frac{1}{16} \text{ in.})t$$
$$= 21.0 \text{ in.}^2 - (2 \text{ plates})(2 \text{ lines})(5 - 0.5)(1⅛ \text{ in.} + \frac{1}{16} \text{ in.})(⅝ \text{ in.})$$
$$= 13.0 \text{ in.}^2$$

$$A_{nt} = (2 \text{ plates})\left[gage - (d_h + \frac{1}{16} \text{ in.})\right]t$$
$$= (2 \text{ plates})\left[5½ \text{ in.} - (1⅛ \text{ in.} + \frac{1}{16} \text{ in.})\right](⅝ \text{ in.})$$
$$= 3.23 \text{ in.}^2$$

$$U_{bs} = 1.0$$

and

$$R_n = 0.60(65 \text{ ksi})\left(13.0 \text{ in.}^2\right) + 1.0(65 \text{ ksi})\left(3.23 \text{ in.}^2\right) \leq 0.60(50 \text{ ksi})\left(21.0 \text{ in.}^2\right) + 1.0(65 \text{ ksi})\left(3.23 \text{ in.}^2\right)$$
$$= 717 \text{ kips} < 840 \text{ kips}$$

Therefore:
$R_n = 717$ kips

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(717 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{717 \text{ kips}}{2.00}$ |
| $= 538 \text{ kips} > 316 \text{ kips} \quad \textbf{o.k.}$ | $= 359 \text{ kips} > 226 \text{ kips} \quad \textbf{o.k.}$ |

*Block shear rupture of diagonal flange*

By inspection, block shear rupture on the diagonal flange will not control.

*Strength of bolted connection—gusset plate*

Slip-critical connections must also be designed for the limit states of bearing-type connections. From AISC *Specification* Section J3.7 Commentary, the strength of the bolt group is taken as the sum of the individual strengths of the individual fasteners, which may be taken as the lesser of the fastener shear strength per AISC *Specification* Section J3.7, the bearing strength at the bolt hole per AISC *Specification* Section J3.11, or the tearout strength at the bolt hole per AISC *Specification* Section J3.11.

---

# IIC-29

From AISC *Manual* Table 7-1, the available shear strength per bolt for 1-in.-diameter, Group 120 bolts with threads not excluded from the shear plane (thread condition N) is:

| LRFD | ASD |
|------|-----|
| $\phi r_n = 31.8$ kips/bolt | $\frac{r_n}{\Omega} = 21.2$ kips/bolt |

The available bearing and tearout strength of the gusset plate at the edge bolts is determined using AISC *Manual* Table 7-5, using $l_c = 2$ in.

| LRFD | ASD |
|------|-----|
| $\phi r_n = (84.1 \text{ kip/in.})(⅝ \text{ in.})$ | $\frac{r_n}{\Omega} = (56.1 \text{ kip/in.})(⅝ \text{ in.})$ |
| $= 31.5$ kips/bolt | $= 21.0$ kips/bolt |

Therefore, the bearing or tearout strength controls over bolt shear at the edge bolts.

The available bearing and tearout strength of the gusset plate at the other bolts is determined using AISC *Manual* Table 7-4 with $s = 3$ in.

| LRFD | ASD |
|------|-----|
| $\phi r_n = (110 \text{ kip/in.})(⅝ \text{ in.})$ | $\frac{r_n}{\Omega} = (73.1 \text{ kip/in.})(⅝ \text{ in.})$ |
| $= 41.3$ kips/bolt | $= 27.4$ kips/bolt |

Therefore, bolt shear controls over bearing or tearout at the other bolts.

By inspection the bearing or tearout strength of the beam flange will not control.

The strength of the bolt group in the gusset plate is determined by summing the strength of the individual fasteners as follows:

| LRFD | ASD |
|------|-----|
| $\phi R_n = (2 \text{ sides})(2 \text{ lines})\left[\begin{array}{l}(1 \text{ bolt})(31.5 \text{ kips/bolt}) \\ + (4 \text{ bolts})(31.8 \text{ kips/bolt})\end{array}\right]$ | $\frac{R_n}{\Omega} = (2 \text{ sides})(2 \text{ lines})\left[\begin{array}{l}(1 \text{ bolt})(21.0 \text{ kips/bolt}) \\ + (4 \text{ bolts})(21.2 \text{ kips/bolt})\end{array}\right]$ |
| $= 635 \text{ kips} > 316 \text{ kips} \quad \textbf{o.k.}$ | $= 423 \text{ kips} > 226 \text{ kips} \quad \textbf{o.k.}$ |

*Horizontal Connection*

The required strength of the gusset plate to horizontal member is determined as follows:

| LRFD | ASD |
|------|-----|
| $P_u = 966 \text{ kips} - 734 \text{ kips}$ | $P_a = 690 \text{ kips} - 524 \text{ kips}$ |
| $= 232$ kips | $= 166$ kips |

Using the bolt slip resistance strength determined previously, the required number of rows of bolts is determined as follows:

---

# IIC-30

| LRFD | ASD |
|------|-----|
| $n_{req} = \frac{P_u}{\phi r_n}$ | $n_{req} = \frac{\Omega P_a}{r_n}$ |
|  |  |
| $= \frac{232 \text{ kips}}{17.3 \text{ kips/bolt}}$ | $= \frac{166 \text{ kips}}{11.5 \text{ kips/bolt}}$ |
| $= 13.4$ bolts | $= 14.4$ bolts |
|  |  |
| For two lines of bolts on both sides the required number of rows is: | For two lines of bolts on both sides the required number of rows is: |
|  |  |
| $\frac{13.4 \text{ bolts}}{(2 \text{ sides})(2 \text{ lines})} = 3.35$ | $\frac{14.4 \text{ bolts}}{(2 \text{ sides})(2 \text{ lines})} = 3.60$ |

For members not subject to corrosion the maximum bolt spacing is determined using AISC *Specification* Section J3.5(a):

$$24t_f = 24(⅝ \text{ in.})$$
$$= 9.00 \text{ in.}$$

Due to the geometry of the gusset plate, the use of 4 rows of bolts in the horizontal connection will exceed the maximum bolt spacing; instead use 5 rows of bolts in two lines.

*Shear strength of the gusset plate*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of the gusset plates is determined as follows:

$$A_{gv} = (2 \text{ plates})lt$$
$$= (2 \text{ plates})(32.0 \text{ in.})(⅝ \text{ in.})$$
$$= 24.0 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})\left(24.0 \text{ in.}^2\right)$$
$$= 720 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(720 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{720 \text{ kips}}{1.50}$ |
| $= 720 \text{ kips} > 232 \text{ kips} \quad \textbf{o.k.}$ | $= 480 \text{ kips} > 166 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.2(b), the available shear rupture strength of gusset plates is determined as follows:

$$A_{nv} = (2 \text{ plates})\left[l - n(d_h + \frac{1}{16} \text{ in.})\right]t$$
$$= (2 \text{ plates})\left[32.0 \text{ in.} - 5(1⅛ \text{ in.} + \frac{1}{16} \text{ in.})\right](⅝ \text{ in.})$$
$$= 19.5 \text{ in.}^2$$

---

# IIC-31

$$R_n = 0.60F_u A_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})\left(19.5 \text{ in.}^2\right)$$
$$= 761 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(761 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{761 \text{ kips}}{2.00}$ |
| $= 571 \text{ kips} > 232 \text{ kips} \quad \textbf{o.k.}$ | $= 381 \text{ kips} > 166 \text{ kips} \quad \textbf{o.k.}$ |

*Strength of bolted connection*

By comparison to the preceding calculations for the diagonal connection, bolt bearing or tearout does not control.

*Vertical Connection*

Using the bolt slip resistance strength determined previously, the required number of bolts is determined as follows:

| LRFD | ASD |
|------|-----|
| $P_u = 286$ kips | $P_a = 204$ kips |
|  |  |
| $n_{req} = \frac{P_u}{\phi r_n}$ | $n_{req} = \frac{\Omega P_a}{r_n}$ |
|  |  |
| $= \frac{286 \text{ kips}}{17.3 \text{ kips/bolt}}$ | $= \frac{204 \text{ kips}}{11.5 \text{ kips/bolt}}$ |
| $= 16.5$ bolts | $= 17.7$ bolts |
|  |  |
| For two lines of bolts on both sides, the required number of rows is: | For two lines of bolts on both sides, the required number of rows is: |
|  |  |
| $\frac{16.5 \text{ bolts}}{(2 \text{ sides})(2 \text{ lines})} = 4.12$ | $\frac{17.7 \text{ bolts}}{(2 \text{ sides})(2 \text{ lines})} = 4.43$ |
|  |  |
| Therefore, use 5 rows at min. 3 in. spacing. | Therefore, use 5 rows at min. 3 in. spacing. |

*Shear strength of the gusset plate*

From AISC *Specification* Section J4.2(a), the available shear yielding strength of gusset plates is determined as follows:

$$A_{gv} = (2 \text{ plates})lt$$
$$= (2 \text{ plates})(31¼ \text{ in.})(⅝ \text{ in.})$$
$$= 23.8 \text{ in.}^2$$

$$R_n = 0.60F_y A_{gv}$$ (*Spec.* Eq. J4-3)
$$= 0.60(50 \text{ ksi})\left(23.8 \text{ in.}^2\right)$$
$$= 714 \text{ kips}$$

---

# IIC-32

| LRFD | ASD |
|------|-----|
| $\phi = 1.00$ | $\Omega = 1.50$ |
|  |  |
| $\phi R_n = 1.00(714 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{714 \text{ kips}}{1.50}$ |
| $= 714 \text{ kips} > 286 \text{ kips} \quad \textbf{o.k.}$ | $= 476 \text{ kips} > 204 \text{ kips} \quad \textbf{o.k.}$ |

From AISC *Specification* Section J4.2(b), the available shear rupture strength of the gusset plates is determined as follows:

$$A_{nv} = (2 \text{ plates})\left[l - n(d_h + \frac{1}{16} \text{ in.})\right]t$$
$$= (2 \text{ plates})\left[31¼ \text{ in.} - 7(1⅛ \text{ in.} + \frac{1}{16} \text{ in.})\right](⅝ \text{ in.})$$
$$= 17.6 \text{ in.}^2$$

$$R_n = 0.60F_u A_{nv}$$ (*Spec.* Eq. J4-4)
$$= 0.60(65 \text{ ksi})\left(17.6 \text{ in.}^2\right)$$
$$= 686 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
|  |  |
| $\phi R_n = 0.75(686 \text{ kips})$ | $\frac{R_n}{\Omega} = \frac{686 \text{ kips}}{2.00}$ |
| $= 515 \text{ kips} > 286 \text{ kips} \quad \textbf{o.k.}$ | $= 343 \text{ kips} > 204 \text{ kips} \quad \textbf{o.k.}$ |

*Strength of bolted connection*

By comparison to the preceding calculations for the diagonal connection, bolt bearing does not control.

Note that because of the difference in depths between the top chord and the vertical and diagonal members, ¼ in. loose shims are required on each side of the shallower members.

The final connection design is shown in Figure II.C-3-4.

---

# IIC-33

![Connection layout diagram showing:
- Top: 1" dia. Group 120, slip critical, Class A, std. holes, typ.
- Dimensions: 2'-8" total, 5", 2'-3", 8¾", 2 @ 7" = 1'-2"
- W14×109 truss chord at top right
- 5⅞" and 5⅜" dimensions
- Central gusset plate labeled "PL⅝ gusset plate NS & FS"
- 2'-2" vertical dimension with 4 @ = 1'-0" spacing
- 12" dimension with ¼" notation
- 2'-7¾" dimension
- W14×61 truss vertical member (left)
- W14×61 truss diagonal member (right)
- 11-0" diagonal length
- 12" and 5½" dimensions at bottom
- Multiple bolt patterns and connection details]

*Fig. II.C-3-4. Connection layout for Example II.C-3.*

---

# IIC-34

---
