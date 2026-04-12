# Chapter D: Tension Members

**AISC Specification v16.0 - Design Examples**
**Original PDF Pages**: 37-64 (28 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Design of Members for Tension

**Examples Included**: ['D.1~D.8: Various tension member types']

---

## Table of Contents

- [EXAMPLE D.7 PIN-CONNECTED TENSION MEMBER](#example-d7-pin-connected-tension-member)
- [EXAMPLE D.8 EYEBAR TENSION MEMBER](#example-d8-eyebar-tension-member)
- [EXAMPLE D.9 PLATE WITH STAGGERED BOLTS](#example-d9-plate-with-staggered-bolts)

---

# Chapter D
# Design of Members for Tension

---

## D1. SLENDERNESS LIMITATIONS

AISC *Specification* Section D1 does not establish a slenderness limit for tension members but recommends limiting *L*/*r* to a maximum of 300. This is not an absolute requirement. Rods are specifically excluded from this recommendation.

---

## D2. TENSILE STRENGTH

Both tensile yielding strength and tensile rupture strength must be considered for the design of tension members. It is not unusual for tensile rupture strength to govern the design of a tension member, particularly for small members with holes or heavier sections with multiple rows of holes.

For preliminary design, tables are provided in Part 5 of the AISC *Manual* for W-shapes, L-shapes, WT-shapes, rectangular HSS, square HSS, round HSS, pipe, and 2L. The calculations in these tables for available tensile rupture strength assume an effective area, *A*<sub>e</sub>, of 0.75*A*<sub>g</sub>. The gross area, *A*<sub>g</sub>, is the total cross-sectional area of the member. If the actual effective area is greater than 0.75*A*<sub>g</sub>, the tabulated values will be conservative and calculations can be performed to obtain higher strengths. If the actual effective area is less than 0.75*A*<sub>g</sub>, the tabulated values will be unconservative and calculations are necessary to determine the available strength.

---

## D3. EFFECTIVE NET AREA

In computing net area, *A*<sub>n</sub>, AISC *Specification* Section B4.3b requires that an extra ⅟₁₆ in. be added to the bolt hole diameter. A computation of the effective area for a chain of holes is presented in Example D.9.

Unless all elements of the cross section are connected, *A*<sub>e</sub> = *A*<sub>n</sub>*U*, where *U* is a reduction factor to account for shear lag. The appropriate values of *U* can be obtained from AISC *Specification* Table D3.1.

---

## D4. BUILT-UP MEMBERS

The limitations for connections of built-up members are discussed in Section D4 of the AISC *Specification*.

---

## D5. PIN-CONNECTED MEMBERS

An example of a pin-connected member is given in Example D.7.

---

## D6. EYEBARS

An example of an eyebar is given in Example D.8. The strength of an eyebar meeting the dimensional requirements of AISC *Specification* Section D6 is governed by tensile yielding of the body.

---


---

# EXAMPLE D.1 W-SHAPE TENSION MEMBER

---

## Given:

Select an ASTM A992/A992M W-shape with 8 in. nominal depth to carry a dead load of 30 kips and a live load of 90 kips in tension. The member is 25.0 ft long. Verify the member strength by both LRFD and ASD with the bolted end connection as shown in Figure D.1-1. Verify that the member satisfies the recommended slenderness limit. Assume that connection limit states do not govern.

![Connection Geometry Diagram](diagram)

**Connection Details:**
- ¾" dia. bolts in standard holes
- 1¼" edge distance
- 3 @ 3" spacing
- W8 section
- *P*<sub>D</sub> = 30 kips
- *P*<sub>L</sub> = 90 kips

*Fig D.1-1. Connection geometry for Example D.1.*

---

## Solution:

From Chapter 2 of ASCE/SEI 7, the required tensile strength is:

| LRFD | ASD |
|------|-----|
| *P*<sub>u</sub> = 1.2(30 kips) + 1.6(90 kips) | *P*<sub>a</sub> = 30 kips + 90 kips |
| = 180 kips | = 120 kips |

From AISC *Manual* Table 5-1, try a W8×21.

From AISC *Manual* Table 2-4, the material properties are as follows:

**ASTM A992/A992M**
*F*<sub>y</sub> = 50 ksi
*F*<sub>u</sub> = 65 ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

**W8×21**
*A*<sub>g</sub> = 6.16 in.²
*b*<sub>f</sub> = 5.27 in.
*t*<sub>f</sub> = 0.400 in.
*d* = 8.28 in.
*r*<sub>y</sub> = 1.26 in.

The WT-shape corresponding to a W8×21 is a WT4×10.5. From AISC *Manual* Table 1-8, the geometric properties are as follows:

**WT4×10.5**
*ȳ* = 0.831 in.

---


---

---

From AISC *Specification* Table J3.3, the hole diameter for ¾ in. diameter bolts in standard holes is:

*d*<sub>h</sub> = ¹³⁄₁₆ in.

---

## *Tensile Yielding*

From AISC *Manual* Table 5-1, the available tensile yielding strength of a W8×21 is:

| LRFD | ASD |
|------|-----|
| ϕ*t* *P*<sub>n</sub> = 277 kips > 180 kips   **o.k.** | *P*<sub>n</sub> / Ω<sub>t</sub> = 184 kips > 120 kips   **o.k.** |

---

## *Tensile Rupture*

Verify the table assumption that *A*<sub>e</sub> / *A*<sub>g</sub> ≥ 0.75 for this connection.

From the description of the element in AISC *Specification* Table D3.1, Case 7, calculate the shear lag factor, *U*, as the larger of the values from AISC *Specification* Section D3, Table D3.1 Case 2 and Case 7.

From AISC *Specification* Section D3, for open cross sections, *U* need not be less than the ratio of the gross area of the connected element(s) to the member gross area.

$$U = \frac{2b_f t_f}{A_g}$$

$$= \frac{2(5.27 \text{ in.})(0.400 \text{ in.})}{6.16 \text{ in.}^2}$$

= 0.684

Case 2: Determine *U* based on two WT-shapes per AISC *Specification* Commentary Figure C-D3.1, with *x̄* = *ȳ* = 0.831 in. and where *l* is the length of connection.

$$U = 1 - \frac{\overline{x}}{l}$$

$$= 1 - \frac{0.831 \text{ in.}}{9.00 \text{ in.}}$$

= 0.908

Case 7:

*b*<sub>f</sub> = 5.27 in.

$$\frac{2}{3}d = \frac{2}{3}(8.28 \text{ in.})$$
= 5.52 in.

Because the flange is connected with three or more fasteners per line in the direction of loading and *b*<sub>f</sub> < ⅔*d* :

*U* = 0.85

Therefore, use the larger *U* = 0.908.

Calculate *A*<sub>n</sub> using AISC *Specification* Section B4.3b.

---


---

---

## Net Area and Effective Area Calculation

$$A_n = A_g - 4(d_h + \frac{1}{16} \text{ in.}) t_f$$

$$= 6.16 \text{ in.}^2 - 4(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.})(0.400 \text{ in.})$$

= 4.76 in.²

Calculate *A*<sub>e</sub> using AISC *Specification* Section D3.

$$A_e = A_n U$$     (*Spec.* Eq. D3-1)

$$= (4.76 \text{ in.}^2)(0.908)$$

= 4.32 in.²

$$\frac{A_e}{A_g} = \frac{4.32 \text{ in.}^2}{6.16 \text{ in.}^2}$$

= 0.701 < 0.75

Because *A*<sub>e</sub> / *A*<sub>g</sub> < 0.75 , the tensile rupture strength from AISC *Manual* Table 5-1 is not valid. The available tensile rupture strength is determined using AISC *Specification* Section D2 as follows:

*P*<sub>n</sub> = *F*<sub>u</sub> *A*<sub>e</sub>     (*Spec.* Eq. D2-2)

= (65 ksi)(4.32 in.²)

= 281 kips

| LRFD | ASD |
|------|-----|
| ϕ*t* = 0.75 | Ω*t* = 2.00 |
| ϕ*t* *P*<sub>n</sub> = 0.75(281 kips) | *P*<sub>n</sub> / Ω*t* = 281 kips / 2.00 |
| = 211 kips > 180 kips   **o.k.** | = 141 kips > 120 kips   **o.k.** |

Note that the W8×21 available tensile strength is governed by the tensile rupture limit state at the end connection versus the tensile yielding limit state.

See Chapter J for illustrations of connection limit state checks.

---

## *Check Recommended Slenderness Limit*

$$\frac{L}{r} = \frac{(25.0 \text{ ft})(12 \text{ in./ft})}{1.26 \text{ in.}}$$

= 238 < 300 from AISC *Specification* Section D1   **o.k.**

---


---

# EXAMPLE D.2 SINGLE-ANGLE TENSION MEMBER

---

## Given:

Verify the tensile strength of an ASTM A572/A572M Gr. 50 L4×4×½ with one line of four ¾ in. diameter bolts in standard holes, as shown in Figure D.2-1. The member carries a dead load of 20 kips and a live load of 60 kips in tension. Additionally, calculate at what length this tension member would cease to satisfy the recommended slenderness limit. Assume that connection limit states do not govern.

![Connection Geometry Diagram](diagram)

**Connection Details:**
- L4×4×½
- ¾" dia. bolts in standard holes
- 1½" edge distance
- 3 @ 3" spacing
- *P*<sub>D</sub> = 20 kips
- *P*<sub>L</sub> = 60 kips

*Fig. D.2-1. Connection geometry for Example D.2.*

---

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

**ASTM A572/A572M Gr. 50**
*F*<sub>y</sub> = 50 ksi
*F*<sub>u</sub> = 65 ksi

From AISC *Manual* Table 1-7, the geometric properties are as follows:

**L4×4×½**
*A*<sub>g</sub> = 3.75 in.²
*r*<sub>z</sub> = 0.776 in.
*x̄* = 1.18 in.

From AISC *Specification* Table J3.3, the hole diameter for ¾ in. diameter bolts in standard holes is:

*d*<sub>h</sub> = ¹³⁄₁₆ in.

From Chapter 2 of ASCE/SEI 7, the required tensile strength is:

| LRFD | ASD |
|------|-----|
| *P*<sub>u</sub> = 1.2(20 kips) + 1.6(60 kips) | *P*<sub>a</sub> = 20 kips + 60 kips |
| = 120 kips | = 80.0 kips |

---

## *Tensile Yielding*

The available tensile yielding strength is determined using AISC *Specification* Section D2 as follows:

*P*<sub>n</sub> = *F*<sub>y</sub> *A*<sub>g</sub>     (*Spec.* Eq. D2-1)

= (50 ksi)(3.75 in.²)

= 188 kips

---


---

---

| LRFD | ASD |
|------|-----|
| ϕ*t* = 0.90 | Ω*t* = 1.67 |
| ϕ*t* *P*<sub>n</sub> = 0.90(188 kips) | *P*<sub>n</sub> / Ω*t* = 188 kips / 1.67 |
| = 169 kips > 120 kips   **o.k.** | = 113 kips > 80.0 kips   **o.k.** |

---

## *Tensile Rupture*

From the description of the element in AISC *Specification* Table D3.1 Case 8, calculate the shear lag factor, *U*, as the larger of the values from AISC *Specification* Section D3, Table D3.1 Case 2 and Case 8.

From AISC *Specification* Section D3, for open cross sections, *U* need not be less than the ratio of the gross area of the connected element(s) to the member gross area. Half of the member is connected, therefore, the minimum value of *U* is:

*U* = 0.500

Case 2, where *l* is the length of connection and *ȳ* = *x̄* :

$$U = 1 - \frac{\overline{x}}{l}$$

$$= 1 - \frac{1.18 \text{ in.}}{9.00 \text{ in.}}$$

= 0.869

Case 8, with four or more fasteners per line in the direction of loading:

*U* = 0.80

Therefore, use the larger *U* = 0.869.

Calculate *A*<sub>n</sub> using AISC *Specification* Section B4.3b.

$$A_n = A_g - (d_h + \frac{1}{16} \text{ in.}) t$$

$$= 3.75 \text{ in.} - (\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.})(\frac{1}{2} \text{ in.})$$

= 3.31 in.²

Calculate *A*<sub>e</sub> using AISC *Specification* Section D3.

$$A_e = A_n U$$     (*Spec.* Eq. D3-1)

$$= (3.31 \text{ in.}^2)(0.869)$$

= 2.88 in.²

The available tensile rupture strength is determined using AISC *Specification* Section D2 as follows:

*P*<sub>n</sub> = *F*<sub>u</sub> *A*<sub>e</sub>     (*Spec.* Eq. D2-2)

= (65 ksi)(2.88 in.²)

= 187 kips

---


---

---

| LRFD | ASD |
|------|-----|
| ϕ*t* = 0.75 | Ω*t* = 2.00 |
| ϕ*t* *P*<sub>n</sub> = 0.75(187 kips) | *P*<sub>n</sub> / Ω*t* = 187 kips / 2.00 |
| = 140 kips > 120 kips   **o.k.** | = 93.5 kips > 80.0 kips   **o.k.** |

The L4×4×½ available tensile strength is governed by the tensile rupture limit state.

---

## *Recommended L*<sub>max</sub>

Using AISC *Specification* Section D1:

*L*<sub>max</sub> = 300*r*<sub>z</sub>

$$= 300\left(\frac{0.776 \text{ in.}}{12 \text{ in./ft}}\right)$$

= 19.4 ft

Note: The *L*/*r* limit is a recommendation, not a requirement.

See Chapter J for illustrations of connection limit state checks.

---


---

# EXAMPLE D.3 WT-SHAPE TENSION MEMBER

---

## Given:

An ASTM A992/A992M WT6×20 member has a length of 30 ft and carries a dead load of 40 kips and a live load of 120 kips in tension. As shown in Figure D3-1, the end connection is fillet welded on each side for 16 in. Verify the member tensile strength by both LRFD and ASD. Assume that the gusset plate and the weld are satisfactory.

![Connection Geometry Diagram](diagram)

**Connection Details:**
- WT6×20
- Gusset plate
- 16" weld length on each side
- 17" total connection length
- *P*<sub>D</sub> = 40 kips
- *P*<sub>L</sub> = 120 kips

*Fig. D.3-1. Connection geometry for Example D.3.*

---

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

**ASTM A992/A992M**
*F*<sub>y</sub> = 50 ksi
*F*<sub>u</sub> = 65 ksi

From AISC *Manual* Table 1-8, the geometric properties are as follows:

**WT6×20**
*A*<sub>g</sub> = 5.84 in.²
*b*<sub>f</sub> = 8.01 in.
*t*<sub>f</sub> = 0.515 in.
*r*<sub>x</sub> = 1.57 in.
*ȳ* = 1.09 in.

From Chapter 2 of ASCE/SEI 7, the required tensile strength is:

| LRFD | ASD |
|------|-----|
| *P*<sub>u</sub> = 1.2(40 kips) + 1.6(120 kips) | *P*<sub>a</sub> = 40 kips + 120 kips |
| = 240 kips | = 160 kips |

---

## *Tensile Yielding*

Check the tensile yielding limit state using AISC *Manual* Table 5-3.

| LRFD | ASD |
|------|-----|
| ϕ*t* *P*<sub>n</sub> = 263 kips > 240 kips   **o.k.** | *P*<sub>n</sub> / Ω*t* = 175 kips > 160 kips   **o.k.** |

---


---

---

## *Tensile Rupture*

Check the tensile rupture limit state using AISC *Manual* Table 5-3.

| LRFD | ASD |
|------|-----|
| ϕ*t* *P*<sub>n</sub> = 214 kips < 240 kips   **n.g.** | *P*<sub>n</sub> / Ω*t* = 142 kips < 160 kips   **n.g.** |

The tabulated available rupture strengths don't work and may be conservative for this case; therefore, calculate the exact solution.

Calculate *U* as the larger of the values from AISC *Specification* Section D3 and Table D3.1 Case 4.

From AISC *Specification* Section D3, for open cross sections, *U* need not be less than the ratio of the gross area of the connected element(s) to the member gross area.

$$U = \frac{b_f t_f}{A_g}$$

$$= \frac{(8.01 \text{ in.})(0.515 \text{ in.})}{5.84 \text{ in.}^2}$$

= 0.706

Case 4, where *l* is the length of the connection and *x̄* = *ȳ* :

$$U = \frac{3l^2}{3l^2 + w^2}\left(1 - \frac{\overline{x}}{l}\right)$$

$$= \left[\frac{3(16.0 \text{ in.})^2}{3(16.0 \text{ in.})^2 + (8.01 \text{ in.})^2}\right]\left(1 - \frac{1.09 \text{ in.}}{16.0 \text{ in.}}\right)$$

= 0.860

Therefore, use *U* = 0.860.

Calculate *A*<sub>n</sub> using AISC *Specification* Section B4.3b. Because there are no reductions due to bolt holes or notches:

*A*<sub>n</sub> = *A*<sub>g</sub>
= 5.84 in.²

Calculate *A*<sub>e</sub> using AISC *Specification* Section D3.

$$A_e = A_n U$$     (*Spec.* Eq. D3-1)

$$= (5.84 \text{ in.}^2)(0.860)$$

= 5.02 in.²

The available tensile rupture strength is determined using AISC *Specification* Section D2 as follows:

---


---

---

## Tensile Rupture Strength (continued)

*P*<sub>n</sub> = *F*<sub>u</sub> *A*<sub>e</sub>     (*Spec.* Eq. D2-2)

= (65 ksi)(5.02 in.²)

= 326 kips

| LRFD | ASD |
|------|-----|
| ϕ*t* = 0.75 | Ω*t* = 2.00 |
| ϕ*t* *P*<sub>n</sub> = 0.75(326 kips) | *P*<sub>n</sub> / Ω*t* = 326 kips / 2.00 |
| = 245 kips > 240 kips   **o.k.** | = 163 kips > 160 kips   **o.k.** |

Alternately, the available tensile rupture strengths can be determined by modifying the tabulated values. The available tensile rupture strengths published in the tension member selection tables are based on the assumption that *A*<sub>e</sub> = 0.75*A*<sub>g</sub>. The actual available strengths can be determined by adjusting the values from AISC *Manual* Table 5-3 as follows:

| LRFD | ASD |
|------|-----|
| $$\phi_t P_n = (214 \text{ kips})\left(\frac{A_e}{0.75 A_g}\right)$$ | $$\frac{P_n}{\Omega_t} = (142 \text{ kips})\left(\frac{A_e}{0.75 A_g}\right)$$ |
| $$= (214 \text{ kips})\left[\frac{5.02 \text{ in.}^2}{0.75(5.84 \text{ in.}^2)}\right]$$ | $$= (142 \text{ kips})\left[\frac{5.02 \text{ in.}^2}{0.75(5.84 \text{ in.}^2)}\right]$$ |
| = 245 kips > 240 kips   **o.k.** | = 163 kips > 160 kips   **o.k.** |

---

## *Recommended Slenderness Limit*

$$\frac{L}{r_x} = \frac{(30.0 \text{ ft})(12 \text{ in./ft})}{1.57 \text{ in.}}$$

= 229 < 300 from AISC *Specification* Section D1   **o.k.**

Note: The *L*/*r*<sub>x</sub> limit is a recommendation, not a requirement.

See Chapter J for illustrations of connection limit state checks.

---


---

# EXAMPLE D.4 RECTANGULAR HSS TENSION MEMBER

---

## Given:

Verify the tensile strength of an ASTM A500/A500M Grade C HSS6×4×⅜ with a length of 30 ft. The member is carrying a dead load of 40 kips and a live load of 110 kips in tension. As shown in Figure D.4-1, the end connection is a fillet welded ½-in.-thick single concentric gusset plate with a weld length of 16 in. Assume that the gusset plate and weld are satisfactory.

![Connection Geometry Diagram](diagram)

**Connection Details:**
- HSS6×4×⅜
- ½" thick gusset plate
- 16" weld length
- 17" total connection length
- *P*<sub>D</sub> = 40 kips
- *P*<sub>L</sub> = 110 kips

*Fig. D.4-1. Connection geometry for Example D.4.*

---

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

**ASTM A500 Grade C, rectangular HSS**
*F*<sub>y</sub> = 50 ksi
*F*<sub>u</sub> = 62 ksi

From AISC *Manual* Table 1-11, the geometric properties are as follows:

**HSS6×4×⅜**
*A*<sub>g</sub> = 6.18 in.²
*r*<sub>x</sub> = 1.55 in.
*t* = 0.349 in.

From Chapter 2 of ASCE/SEI 7, the required tensile strength is:

| LRFD | ASD |
|------|-----|
| *P*<sub>u</sub> = 1.2(40 kips) + 1.6(110 kips) | *P*<sub>a</sub> = 40 kips + 110 kips |
| = 224 kips | = 150 kips |

---

## *Tensile Yielding*

Check the tensile yielding limit state using AISC *Manual* Table 5-4.

| LRFD | ASD |
|------|-----|
| ϕ*t* *P*<sub>n</sub> = 278 kips > 224 kips   **o.k.** | *P*<sub>n</sub> / Ω*t* = 185 kips > 150 kips   **o.k.** |

---


---

---

## *Tensile Rupture*

Check the tensile rupture limit state using AISC *Manual* Table 5-4.

| LRFD | ASD |
|------|-----|
| ϕ*t* *P*<sub>n</sub> = 216 kips < 224 kips   **n.g.** | *P*<sub>n</sub> / Ω*t* = 144 kips < 150 kips   **n.g.** |

The tabulated available rupture strengths may be conservative in this case; therefore, calculate the exact solution.

Calculate *U* from AISC *Specification* Section D3 and Table D3.1 Case 5.

$$b = \frac{B - t_p}{2}$$

$$= \frac{4 \text{ in.} - \frac{1}{2} \text{ in.}}{2}$$

= 1.75 in.

$$\overline{x} = b - \frac{2b^2 + tH - 2t^2}{2H + 4b - 4t}$$

$$= 1.75 \text{ in.} - \frac{2(1.75 \text{ in.})^2 + (0.349 \text{ in.})(6 \text{ in.}) - 2(0.349 \text{ in.})^2}{2(6 \text{ in.}) + 4(1.75 \text{ in.}) - 4(0.349 \text{ in.})}$$

= 1.30 in.

$$U = 1 - \frac{\overline{x}}{l}$$

$$= 1 - \frac{1.30 \text{ in.}}{16.0 \text{ in.}}$$

= 0.919

Allowing for a ⅟₁₆ in. gap in fit-up between the HSS and the gusset plate:

$$A_n = A_g - 2(t_p + \frac{1}{16} \text{ in.}) t$$

$$= 6.18 \text{ in.}^2 - 2(\frac{1}{2} \text{ in.} + \frac{1}{16} \text{ in.})(0.349 \text{ in.})$$

= 5.79 in.²

Calculate *A*<sub>e</sub> using AISC *Specification* Section D3.

$$A_e = A_n U$$     (*Spec.* Eq. D3-1)

$$= (5.79 \text{ in.}^2)(0.919)$$

= 5.32 in.²

The available tensile rupture strength is determined using AISC *Specification* Section D2 as follows:

*P*<sub>n</sub> = *F*<sub>u</sub> *A*<sub>e</sub>     (*Spec.* Eq. D2-2)

= (62 ksi)(5.32 in.²)

= 330 kips

---


---

---

| LRFD | ASD |
|------|-----|
| ϕ*t* = 0.75 | Ω*t* = 2.00 |
| ϕ*t* *P*<sub>n</sub> = 0.75(330 kips) | *P*<sub>n</sub> / Ω*t* = 330 kips / 2.00 |
| = 248 kips > 224 kips   **o.k.** | = 165 kips > 150 kips   **o.k.** |

The HSS available tensile strength is governed by the tensile rupture limit state.

---

## *Recommended Slenderness Limit*

$$\frac{L}{r} = \frac{(30.0 \text{ ft})(12 \text{ in./ft})}{1.55 \text{ in.}}$$

= 232 < 300 from AISC *Specification* Section D1   **o.k.**

Note: The *L*/*r* limit is a recommendation, not a requirement.

See Chapter J for illustrations of connection limit state checks.

---


---

# EXAMPLE D.5 ROUND HSS TENSION MEMBER

---

## Given:

Verify the tensile strength of an ASTM A500/A500M Grade C HSS6.000×0.500 with a length of 30 ft. The member carries a dead load of 40 kips and a live load of 120 kips in tension. As shown in Figure D.5-1, the end connection is a fillet welded ½-in.-thick single concentric gusset plate with a weld length of 16 in. Assume that the gusset plate and weld are satisfactory.

![Connection Geometry Diagram](diagram)

**Connection Details:**
- HSS6.000×0.500
- ½" thick gusset plate
- 16" weld length
- 17" total connection length
- *P*<sub>D</sub> = 40 kips
- *P*<sub>L</sub> = 120 kips

*Fig. D.5-1. Connection geometry for Example D.5.*

---

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

**ASTM A500 Grade C, round HSS**
*F*<sub>y</sub> = 50 ksi
*F*<sub>u</sub> = 62 ksi

From AISC *Manual* Table 1-13, the geometric properties are as follows:

**HSS6.000×0.500**
*A*<sub>g</sub> = 8.09 in.²
*r* = 1.96 in.
*t* = 0.465 in.

From Chapter 2 of ASCE/SEI 7, the required tensile strength is:

| LRFD | ASD |
|------|-----|
| *P*<sub>u</sub> = 1.2(40 kips) + 1.6(120 kips) | *P*<sub>a</sub> = 40 kips + 120 kips |
| = 240 kips | = 160 kips |

---

## *Tensile Yielding*

Check the tensile yielding limit state using AISC *Manual* Table 5-6.

| LRFD | ASD |
|------|-----|
| ϕ*t* *P*<sub>n</sub> = 364 kips > 240 kips   **o.k.** | *P*<sub>n</sub> / Ω*t* = 242 kips > 160 kips   **o.k.** |

---


---

---

## *Tensile Rupture*

Check the tensile rupture limit state using AISC *Manual* Table 5-6.

| LRFD | ASD |
|------|-----|
| ϕ*t* *P*<sub>n</sub> = 282 kips > 240 kips   **o.k.** | *P*<sub>n</sub> / Ω*t* = 188 kips > 160 kips   **o.k.** |

Check that *A*<sub>e</sub> / *A*<sub>g</sub> ≥ 0.75 as assumed in the table.

Determine *U* from AISC *Specification* Table D3.1 Case 5.

*l* = 16 in.
*D* = 6.00 in.
*t*<sub>p</sub> = ½ in.

$$\theta = \frac{\pi}{2} - \sin^{-1}\left(\frac{t_p/2}{D/2}\right)$$

$$= \frac{\pi}{2} - \sin^{-1}\left(\frac{\frac{1}{2} \text{ in.}/2}{6.00 \text{ in.}/2}\right)$$

= 1.49 rad

$$\overline{x} = \frac{R \sin \theta}{\theta} - \frac{1}{2}t_p$$

$$= \frac{(3.00 \text{ in.})(\sin 1.49)}{1.49} - \frac{1}{2}(\frac{1}{2} \text{ in.})$$

= 1.76 in.

$$U = \left[1 + \left(\frac{\overline{x}}{l}\right)^{3.2}\right]^{-10}$$

$$= \left[1 + \left(\frac{1.76 \text{ in.}}{16 \text{ in.}}\right)^{3.2}\right]^{-10}$$

= 0.991

Allowing for a ⅟₁₆ in. gap in fit-up between the HSS and the gusset plate,

$$A_n = A_g - 2(t_p + \frac{1}{16} \text{ in.}) t$$

$$= 8.09 \text{ in.}^2 - 2(\frac{1}{2} \text{ in.} + \frac{1}{16} \text{ in.})(0.465 \text{ in.})$$

= 7.57 in.²

Calculate *A*<sub>e</sub> using AISC *Specification* Section D3.

$$A_e = A_n U$$     (*Spec.* Eq. D3-1)

$$= (7.57 \text{ in.}^2)(0.991)$$

= 7.50 in.²

---


---

---

## Effective Area Verification

$$\frac{A_e}{A_g} = \frac{7.50 \text{ in.}^2}{8.09 \text{ in.}^2}$$

= 0.927 > 0.75   **o.k.**

Because AISC *Manual* Table 5-6 provides an overly conservative estimate of the available tensile rupture strength for this example, calculate *P*<sub>n</sub> using AISC *Specification* Section D2.

*P*<sub>n</sub> = *F*<sub>u</sub> *A*<sub>e</sub>     (Spec. Eq. D2-2)

= (62 ksi)(7.50 in.²)

= 465 kips

| LRFD | ASD |
|------|-----|
| ϕ*t* = 0.75 | Ω*t* = 2.00 |
| ϕ*t* *P*<sub>n</sub> = 0.75(465 kips) | *P*<sub>n</sub> / Ω*t* = 465 kips / 2.00 |
| = 349 kips > 240 kips   **o.k.** | = 233 kips > 160 kips   **o.k.** |

The HSS available strength is governed by the tensile rupture limit state.

---

## *Recommended Slenderness Limit*

$$\frac{L}{r} = \frac{(30.0 \text{ ft})(12 \text{ in./ft})}{1.96 \text{ in.}}$$

= 184 < 300 from AISC *Specification* Section D1   **o.k.**

Note: The *L*/*r* limit is a recommendation, not a requirement.

See Chapter J for illustrations of connection limit state checks.

---


---

# EXAMPLE D.6 DOUBLE-ANGLE TENSION MEMBER

---

## Given:

An ASTM A572/A572M Gr. 50 2L4×4×½ (¾ in. separation) has one line of eight ¾ in. diameter bolts in standard holes and is 25 ft in length as shown in Figure D.6-1. The double angle is carrying a dead load of 40 kips and a live load of 120 kips in tension. Verify the member tensile strength. Assume that the gusset plate and bolts are satisfactory.

![Connection Geometry Diagram](diagram)

**Connection Details:**
- ⅝" thick gusset plate
- 2L4×4×½
- 7 @ 3" spacing
- 1½" edge distance
- ¾" dia. bolts in standard holes
- *P*<sub>D</sub> = 40 kips
- *P*<sub>L</sub> = 120 kips

*Fig. D.6-1. Connection geometry for Example D.6.*

---

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

**ASTM A572/A572M Gr. 50**
*F*<sub>y</sub> = 50 ksi
*F*<sub>u</sub> = 65 ksi

From AISC *Manual* Tables 1-7 and 1-15, the geometric properties are as follows:

**L4×4×½**
*x̄* = 1.18 in.

**2L4×4×½ (** *s* **= ¾ in.)**
*A*<sub>g</sub> = 7.50 in.²
*r*<sub>y</sub> = 1.83 in.
*r*<sub>x</sub> = 1.21 in.

From AISC *Specification* Table J3.3, the hole diameter for ¾ in. diameter bolts in standard holes is:

*d*<sub>h</sub> = ¹³⁄₁₆ in.

From Chapter 2 of ASCE/SEI 7, the required tensile strength is:

| LRFD | ASD |
|------|-----|
| *P*<sub>u</sub> = 1.2(40 kips) + 1.6(120 kips) | *P*<sub>a</sub> = 40 kips + 120 kips |
| = 240 kips | = 160 kips |

---


---

---

## *Tensile Yielding*

Check the tensile yielding limit state using AISC *Manual* Table 5-8.

| LRFD | ASD |
|------|-----|
| ϕ*t* *P*<sub>n</sub> = 338 kips > 240 kips   **o.k.** | *P*<sub>n</sub> / Ω*t* = 225 kips > 160 kips   **o.k.** |

---

## *Tensile Rupture*

Determine the available tensile rupture strength using AISC *Specification* Section D2. Calculate *U* as the larger of the values from AISC *Specification* Section D3, Table D3.1 Case 2 and Case 8.

From AISC *Specification* Section D3, for open cross sections, *U* need not be less than the ratio of the gross area of the connected element(s) to the member gross area. Half of the member is connected, therefore, the minimum *U* value is:

*U* = 0.50

From Case 2, where *l* is the length of connection:

$$U = 1 - \frac{\overline{x}}{l}$$

$$= 1 - \frac{1.18 \text{ in.}}{21.0 \text{ in.}}$$

= 0.944

From Case 8, with four or more fasteners per line in the direction of loading:

*U* = 0.80

Therefore, use *U* = 0.944.

Calculate *A*<sub>n</sub> using AISC *Specification* Section B4.3b.

$$A_n = A_g - 2(d_h + \frac{1}{16} \text{ in.}) t$$

$$= 7.50 \text{ in.}^2 - 2(\frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.})(\frac{1}{2} \text{ in.})$$

= 6.63 in.²

Calculate *A*<sub>e</sub> using AISC *Specification* Section D3.

$$A_e = A_n U$$     (*Spec.* Eq. D3-1)

$$= (6.63 \text{ in.}^2)(0.944)$$

= 6.26 in.²

The available tensile rupture strength is determined using AISC *Specification* Section D2 as follows:

*P*<sub>n</sub> = *F*<sub>u</sub> *A*<sub>e</sub>     (*Spec.* Eq. D2-2)

= (65 ksi)(6.26 in.²)

= 407 kips

---


---

---

| LRFD | ASD |
|------|-----|
| ϕ*t* = 0.75 | Ω*t* = 2.00 |
| ϕ*t* *P*<sub>n</sub> = 0.75(407 kips) | *P*<sub>n</sub> / Ω*t* = 407 kips / 2.00 |
| = 305 kips > 240 kips   **o.k.** | = 204 kips > 160 kips   **o.k.** |

Note that AISC *Manual* Table 5-8 could also be conservatively used because *A*<sub>e</sub> ≥ 0.75*A*<sub>g</sub>.

The double-angle available tensile strength is governed by the tensile rupture limit state.

---

## *Recommended Slenderness Limit*

$$\frac{L}{r_x} = \frac{(25.0 \text{ ft})(12 \text{ in./ft})}{1.21 \text{ in.}}$$

= 248 < 300  from AISC *Specification* Section D1   **o.k.**

Note: From AISC *Specification* Section D4, the longitudinal spacing of connectors between components of built-up members should preferably limit the slenderness ratio in any component between the connectors to a maximum of 300.

See Chapter J for illustrations of connection limit state checks.

---


---

---

## EXAMPLE D.7 PIN-CONNECTED TENSION MEMBER

---

### Given:

An ASTM A572/A572M Gr. 50 pin-connected tension member with the dimensions shown in Figure D.7-1 carries a dead load of 4 kips and a live load of 12 kips in tension. The diameter of the pin is 1 in., in a ⅟₃₂-in.-oversized hole. Assume that the pin itself is adequate. Verify the member tensile strength.

![Connection Geometry Diagram](diagram)

**Connection Details:**
- *w* = 4.25"
- Approx. *A*<sub>sf</sub>
- *c* = 2.50"
- *B* = 2.25"
- *a* = *t*<sub>h</sub>/2
- *d*<sub>h</sub> = 1.03"
- *b* = 1.61"
- ½" thick
- *P*<sub>D</sub> = 4 kips
- *P*<sub>L</sub> = 12 kips

*Fig. D.7-1. Connection geometry for Example D.7.*

---

### Solution:

From AISC *Manual* Table 2-5, the material properties are as follows:

**Plate**
ASTM A572/A572M Gr. 50
*F*<sub>y</sub> = 50 ksi
*F*<sub>u</sub> = 65 ksi

The geometric properties of the plate are as follows:

*a* = 2.25 in.
*b* = 1.61 in.
*c* = 2.50 in.
*d* = 1.00 in.
*d*<sub>h</sub> = 1.03 in.
*t* = ½ in.
*w* = 4.25 in.

The requirements given in AISC *Specification* Sections D5.2(a) and D5.2(b) are satisfied by the given geometry. Requirements given in AISC *Specification* Sections D5.2(c) and D5.2(d) are checked as follows:

$$b_e = 2t + 0.63 \le b$$

$$= 2(\frac{1}{2} \text{ in.}) + 0.63 \le 1.61 \text{ in.}$$

= 1.63 in. > 1.61 in.

---


---

---

Therefore, use *b*<sub>e</sub> = 1.61 in.

$$a \ge 1.33b_e$$

2.25 in. > 1.33(1.61 in.)

2.25 in. > 2.14 in.   **o.k.**

$$w \ge 2b_e + d$$

4.25 in. > 2(1.61 in.) + 1.00 in.

4.25 in. > 4.22 in.   **o.k.**

$$c \ge a$$

2.50 in. > 2.25 in.   **o.k.**

From Chapter 2 of ASCE/SEI 7, the required tensile strength is:

| LRFD | ASD |
|------|-----|
| *P*<sub>u</sub> = 1.2(4 kips) + 1.6(12 kips) | *P*<sub>a</sub> = 4 kips + 12 kips |
| = 24.0 kips | = 16.0 kips |

From AISC *Specification* Section D5.1, the available tensile strength is the lower value determined according to the limit states of tensile rupture, shear rupture, bearing, and yielding.

---

## *Tensile Rupture*

Calculate the available tensile rupture strength on the effective net area.

$$P_n = F_u (2tb_e)$$     (*Spec.* Eq. D5-1)

$$= (65 \text{ ksi})(2)(\frac{1}{2} \text{ in.})(1.61 \text{ in.})$$

= 105 kips

From AISC *Specification* Section D5.1(a), the available tensile rupture strength is:

| LRFD | ASD |
|------|-----|
| ϕ*t* = 0.75 | Ω*t* = 2.00 |
| ϕ*t* *P*<sub>n</sub> = 0.75(105 kips) | *P*<sub>n</sub> / Ω*t* = 105 kips / 2.00 |
| = 78.8 kips > 24.0 kips   **o.k.** | = 52.5 kips > 16.0 kips   **o.k.** |

---

## *Shear Rupture*

From AISC *Specification* Section D5.1(b), the area on the shear failure path is:

$$A_{sf} = 2t\left(a + \frac{d}{2}\right)$$

$$= 2(\frac{1}{2} \text{ in.})\left[2.25 \text{ in.} + \left(\frac{1.00 \text{ in.}}{2}\right)\right]$$

= 2.75 in.²

---


---

---

Because *d*<sub>h</sub> − *d* ≤ ⅟₃₂ in.

*C*<sub>r</sub> = 1.0

$$P_n = 0.6C_r F_u A_{sf}$$     (*Spec.* Eq. D5-2)

$$= 0.6(1.0)(65 \text{ ksi})(2.75 \text{ in.}^2)$$

= 107 kips

From AISC *Specification* Section D5.1(b), the available shear rupture strength is:

| LRFD | ASD |
|------|-----|
| ϕ*sf* = 0.75 | Ω*sf* = 2.00 |
| ϕ*sf* *P*<sub>n</sub> = 0.75(107 kips) | *P*<sub>n</sub> / Ω*sf* = 107 kips / 2.00 |
| = 80.3 kips > 24.0 kips   **o.k.** | = 53.5 kips > 16.0 kips   **o.k.** |

---

## *Bearing*

Determine the available bearing strength using AISC *Specification* Section J7(a).

$$A_{pb} = td$$

$$= (\frac{1}{2} \text{ in.})(1.00 \text{ in.})$$

= 0.500 in.²

$$R_n = 1.8F_y A_{pb}$$     (*Spec.* Eq. J7-1)

$$= 1.8(50 \text{ ksi})(0.500 \text{ in.}^2)$$

= 45.0 kips

From AISC *Specification* Section J7, the available bearing strength is:

| LRFD | ASD |
|------|-----|
| ϕ = 0.75 | Ω = 2.00 |
| ϕ*P*<sub>n</sub> = 0.75(45.0 kips) | *P*<sub>n</sub> / Ω = 45.0 kips / 2.00 |
| = 33.8 kips > 24.0 kips   **o.k.** | = 22.5 kips > 16.0 kips   **o.k.** |

---

## *Tensile Yielding*

Determine the available tensile yielding strength using AISC *Specification* Section D2(a).

$$A_g = wt$$

$$= (4.25 \text{ in.})(\frac{1}{2} \text{ in.})$$

= 2.13 in.²

From AISC *Specification* Section D2, the available tensile yielding strength is:

---


---

---

$$P_n = F_y A_g$$     (*Spec.* Eq. D2-1)

$$= (50 \text{ ksi})(2.13 \text{ in.}^2)$$

= 107 kips

| LRFD | ASD |
|------|-----|
| ϕ*t* = 0.90 | Ω*t* = 1.67 |
| ϕ*t* *P*<sub>n</sub> = 0.90(107 kips) | *P*<sub>n</sub> / Ω*t* = 107 kips / 1.67 |
| = 96.3 kips > 24.0 kips   **o.k.** | = 64.1 kips > 16.0 kips   **o.k.** |

The available tensile strength is governed by the bearing strength limit state.

---


---

---

## EXAMPLE D.8 EYEBAR TENSION MEMBER

---

### Given:

A ⅝-in.-thick, ASTM A572/A572M Gr. 50 eyebar member as shown in Figure D.8-1, carries a dead load of 25 kips and a live load of 15 kips in tension. The pin diameter, *d*, is 3 in. Verify the member tensile strength.

![Connection Geometry Diagram](diagram)

**Connection Details:**
- 7.50"
- dia. = 3.00"
- *b* = 2.23"
- *d*<sub>h</sub> = 3.03"
- *R* = 8.00"
- *t* = ⅝"
- *w* = 3.00"
- *P*<sub>D</sub> = 25 kips
- *P*<sub>L</sub> = 15 kips

*Fig. D.8-1. Connection geometry for Example D.8.*

---

### Solution:

From AISC *Manual* Table 2-5, the material properties are as follows:

**Plate**
ASTM A572/A572M Gr. 50
*F*<sub>y</sub> = 50 ksi
*F*<sub>u</sub> = 65 ksi

The geometric properties of the eyebar are as follows:

*R* = 8.00 in.
*b* = 2.23 in.
*d* = 3.00 in.
*d*<sub>h</sub> = 3.03 in.
*d*<sub>head</sub> = 7.50 in.
*t* = ⅝ in.
*w* = 3.00 in.

Check the dimensional requirement using AISC *Specification* Section D6.1.

$$w \le 8t$$

3.00 in. < 8(⅝ in.)

3.00 in. < 5.00 in.   **o.k.**

Check the dimensional requirements using AISC *Specification* Section D6.2.

---


---

---

$$t \ge \frac{1}{2} \text{ in.}$$

⅝ in. > ½ in.   **o.k.**

$$d \ge \frac{7}{8}w$$

$$3.00 \text{ in.} > \frac{7}{8}(3.00 \text{ in.})$$

3.00 in. > 2.63 in.   **o.k.**

$$d_h \le d + \frac{1}{32} \text{ in.}$$

3.03 in. = 3.00 in. + ⅟₃₂ in.

3.03 in. = 3.03 in.   **o.k.**

$$R \ge d_{head}$$

8.00 in. > 7.50 in.   **o.k.**

$$\frac{2}{3}w < b \le \frac{3}{4}w$$

$$\frac{2}{3}(3.00 \text{ in.}) < 2.23 \text{ in.} < \frac{3}{4}(3.00 \text{ in.})$$

2.00 in. < 2.23 in. < 2.25 in.   **o.k.**

From Chapter 2 of ASCE/SEI 7, the required tensile strength is:

| LRFD | ASD |
|------|-----|
| *P*<sub>u</sub> = 1.2(25 kips) + 1.6(15 kips) | *P*<sub>a</sub> = 25 kips + 15 kips |
| = 54.0 kips | = 40.0 kips |

---

## *Tensile Yielding*

Determine the available tensile yielding strength using AISC *Specification* Section D2 at the eyebar body (at *w*).

$$A_g = wt$$

$$= (3.00 \text{ in.})(⅝ \text{ in.})$$

= 1.88 in.²

From AISC *Specification* Section D2, the available tensile yielding strength is:

$$P_n = F_y A_g$$     (*Spec.* Eq. D2-1)

$$= (50 \text{ ksi})(1.88 \text{ in.}^2)$$

= 94.0 kips

---


---

---

| LRFD | ASD |
|------|-----|
| ϕ*t* = 0.90 | Ω*t* = 1.67 |
| ϕ*t* *P*<sub>n</sub> = 0.90(94.0 kips) | *P*<sub>n</sub> / Ω*t* = 94.0 kips / 1.67 |
| = 84.6 kips > 54.0 kips   **o.k.** | = 56.3 kips > 40.0 kips   **o.k.** |

The eyebar tension member available strength is governed by the tensile yielding limit state.

Note: The eyebar detailing limitations ensure that the tensile yielding limit state at the eyebar body will control the strength of the eyebar itself. The pin should also be checked for shear yielding, and, if the material strength is less than that of the eyebar, the bearing limit state should also be checked.

---


---

---

## EXAMPLE D.9 PLATE WITH STAGGERED BOLTS

---

### Given:

Compute *A*<sub>n</sub> and *A*<sub>e</sub> for a 14-in.-wide and ½-in.-thick plate subject to tensile loading with staggered holes as shown in Figure D.9-1.

![Connection Geometry Diagram](diagram)

**Connection Details:**
- ½" thick
- *s* = 2½"
- ¾" bolts in ¹³⁄₁₆" holes
- Points labeled A, B, C, D, E, F, G
- 3" spacing vertically
- 2" edge distance
- Tension load *P* applied

*Fig. D.9-1. Connection geometry for Example D.9.*

---

### Solution:

Calculate the net hole diameter using AISC *Specification* Section B4.3b.

$$d_{net} = d_h + \frac{1}{16} \text{ in.}$$

$$= \frac{13}{16} \text{ in.} + \frac{1}{16} \text{ in.}$$

= 0.875 in.

Compute the net width for all possible paths across the plate. Because of symmetry, many of the net widths are identical and need not be calculated.

$$w = 14.0 \text{ in.} - \Sigma d_{net} + \Sigma \frac{s^2}{4g}$$ from AISC *Specification* Section B4.3b.

Line A-B-E-F:

$$w = 14 \text{ in.} - 2(0.875 \text{ in.})$$

= 12.3 in.

Line A-B-C-D-E-F:

$$w = 14 \text{ in.} - 4(0.875 \text{ in.}) + \frac{(2\frac{1}{2} \text{ in.})^2}{4(3 \text{ in.})} + \frac{(2\frac{1}{2} \text{ in.})^2}{4(3 \text{ in.})}$$

= 11.5 in.

---


---

---

Line A-B-C-D-G:

$$w = 14 \text{ in.} - 3(0.875 \text{ in.}) + \frac{(2\frac{1}{2} \text{ in.})^2}{4(3 \text{ in.})}$$

= 11.9 in.

Line A-B-D-E-F:

$$w = 14 \text{ in.} - 3(0.875 \text{ in.}) + \frac{(2\frac{1}{2} \text{ in.})^2}{4(7 \text{ in.})} + \frac{(2\frac{1}{2} \text{ in.})^2}{4(3 \text{ in.})}$$

= 12.1 in.

Line A-B-C-D-E-F controls the width, *w*, therefore:

$$A_n = wt$$

$$= (11.5 \text{ in.})(\frac{1}{2} \text{ in.})$$

= 5.75 in.²

Determine *U* from AISC *Specification* Table D3.1.

From AISC *Specification* Table D3.1 Case 1, because tension load is transmitted to all elements by the fasteners,

*U* = 1.0

$$A_e = A_n U$$     (*Spec.* Eq. D3-1)

$$= (5.75 \text{ in.}^2)(1.0)$$

= 5.75 in.²

---


---
