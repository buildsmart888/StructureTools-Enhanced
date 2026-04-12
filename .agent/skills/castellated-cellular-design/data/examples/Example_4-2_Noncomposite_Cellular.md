# Example 4.2: Noncomposite Cellular Beam

<!-- Consolidated from pages 71-88 -->


<!-- Page 71 -->

<!-- Page 71 -->

Therefore, 54 studs are required over the entire length of the beam.

Next, calculate an average stud density over the length of the beam, $q$, and use this value to determine the amount of concrete that has been developed at the web opening that is being examined for Vierendeel bending.

$$q = \frac{(2)V_{provided}}{Beam\ span}$$

$$= \frac{(2)(556 \text{ kips})}{50 \text{ ft}}$$

$$= 22.2 \text{ kips/ft}$$

The next step is to calculate the amount of concrete that has been developed by the studs between the end of the beam and the opening under consideration and to then determine if the section at the top tee of the web opening is strong enough to resist the chord force $T_{1(i+2)}$ noted in Table 4-17. If the force $T_{1(i+2)}$ is less than the amount of concrete developed, consider the beam fully composite at that opening—i.e., the concrete has the strength to resist the chord force $T_{1(i+2)}$ and the previous assumption is valid. If this is not the case, take the difference between $T_{1+2}$ and $\Delta Q_c$ as a force, $T_{o,}$ in the top tee of the castellated section and recalculate the force on the bottom tee as $T_{1-new,}$ to account for the fact that the section is not acting fully composite.

The compression force to be resisted by the top tee at its centroid is then

$$T_o = M_t \left[ \frac{1 - q(X_i)}{T_{1(i+2)}} \right] \frac{1}{d_{effec}}$$
(3-12)

The revised tension force to be resisted by bottom tee at its centroid is then

$$T_{1-new} = qX_i + T_o$$
(3-13)

The revised local axial forces at each opening are reported in Table 4-18. In this case, all the web openings were fully composite because enough concrete was developed at each opening to fully resist the global moment. The assumption that the concrete takes all the compression and the bottom tee resists all the tension is valid. Therefore, the forces $T_{1(i)}$ from Table 4-17.

If fewer than 54 studs had been used, the results would have been different. In the case of 30 studs, the shear stud density, $q$, is 12.6 kip/ft. The results would require that the first seven holes be considered as partially composite and the revised top and bottom tee forces be accounted for. These results are shown in Table 4-19 but will not be used in the rest of the example.

Calculate the local moment on the top and bottom tees resulting from the net shear force passing through the web opening. The local moments at each opening are presented in Table 4-20.

Top tee local Vierendeel moment:

$$M_{vt-top} = V_{net} \frac{A_{net-top}}{A_{net}} \left(\frac{e}{2}\right)$$
(from Eq. 3-2)

Bottom tee local Vierendeel moment:

$$M_{vt-bot} = V_{net} \frac{A_{net-bot}}{A_{net}} \left(\frac{e}{2}\right)$$
(from Eq. 3-2)

*Calculate the available shear and flexural strength of top and bottom tees*

Determine the limiting flange width-to-thickness ratio from AISC *Specification* Table B4.1b, Case 10:

$$\lambda_p = 0.38 \sqrt{\frac{E}{F_y}}$$

$$= 0.38 \sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 9.15$$


*64 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*




<!-- Page 72 -->

<!-- Page 72 -->

| Table 4-18. Revised Local Axial Force at Each Opening (LRFD) |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| **Opening Number** | $X_i,$ ft | $T_1 = T_{1(i+2)},$ kips | $qX_i,$ kips | **Composite Status** | $T_o,$ kips | $T_{1-new},$ kips |
| End | 0.000 | 0.000 | 0.000 | N/A | N/A | N/A |
| 1 | 1.46 | 25.3 | 32.4 | Full | 0.000 | 25.3 |
| 2 | 3.71 | 61.4 | 82.4 | Full | 0.000 | 61.4 |
| 3 | 5.96 | 94.1 | 132 | Full | 0.000 | 94.1 |
| 4 | 8.21 | 123 | 182 | Full | 0.000 | 123 |
| 5 | 10.5 | 149 | 233 | Full | 0.000 | 149 |
| 6 | 12.7 | 171 | 282 | Full | 0.000 | 171 |
| 7 | 15.0 | 189 | 333 | Full | 0.000 | 189 |
| 8 | 17.2 | 204 | 382 | Full | 0.000 | 204 |
| 9 | 19.5 | 215 | 433 | Full | 0.000 | 215 |
| 10 | 21.7 | 222 | 482 | Full | 0.000 | 222 |
| 11 | 24.0 | 226 | 533 | Full | 0.000 | 226 |
| Bm. CL | 25.0 | 226 | 555 | Full | 0.000 | 226 |

| Table 4-19. Local Axial Force at Each Opening for 30 Studs (LRFD) |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| **Opening Number** | $X_i,$ ft | $T_1,$ kips | $qX_i,$ kips | **Composite Status** | $T_o,$ kips | $T_{1-new},$ kips |
| End | 0.000 | 0.000 | 0.000 | N/A | 0.000 | 0.000 |
| 1 | 1.46 | 25.3 | 18.4 | Partial | 8.43 | 26.8 |
| 2 | 3.71 | 61.4 | 46.7 | Partial | 17.9 | 64.6 |
| 3 | 5.96 | 94.1 | 75.1 | Partial | 23.1 | 98.2 |
| 4 | 8.21 | 123 | 103 | Partial | 24.0 | 127 |
| 5 | 10.5 | 149 | 132 | Partial | 20.7 | 152 |
| 6 | 12.7 | 171 | 160 | Partial | 13.0 | 173 |
| 7 | 15.0 | 189 | 189 | Partial | 0.885 | 189 |
| 8 | 17.2 | 204 | 217 | Full | 0.000 | 204 |
| 9 | 19.5 | 215 | 246 | Full | 0.000 | 215 |
| 10 | 21.7 | 222 | 273 | Full | 0.000 | 222 |
| 11 | 24.0 | 226 | 302 | Full | 0.000 | 226 |
| Bm. CL | 25.0 | 226 | 315 | Full | 0.000 | 226 |

The width-to-thickness ratio for the top flange is:

$$\lambda = \frac{b}{t}$$

$$= \frac{b_f}{2t_f}$$

$$= \frac{6.50 \text{ in.}}{2(0.450 \text{ in.})}$$

$$= 7.22 < 9.15$$


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 65*




<!-- Page 73 -->

<!-- Page 73 -->

| Table 4-20. Local Vierendeel Moment at Each Opening |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  | **ASD** |  |  | **LRFD** |  |  |
| **Opening Number** | $X_i,$ ft | $V_n,$ kips | $M_{vt-top},$ kip-in. | $M_{vt-bot},$ kip-in. | $V_u,$ kips | $M_{vt-top},$ kip-in. | $M_{vt-bot},$ kip-in. |
| End | 0.000 | 31.3 | 54.0 | 71.4 | 44.1 | 76.1 | 101 |
| 1 | 1.46 | 29.2 | 50.3 | 66.6 | 41.1 | 70.7 | 93.7 |
| 2 | 3.71 | 26.0 | 44.6 | 59.2 | 36.5 | 62.7 | 83.2 |
| 3 | 5.96 | 22.7 | 39.0 | 51.7 | 31.8 | 54.8 | 72.6 |
| 4 | 8.21 | 19.4 | 33.4 | 44.3 | 27.2 | 46.8 | 62.0 |
| 5 | 10.5 | 16.2 | 27.8 | 36.9 | 22.6 | 38.8 | 51.5 |
| 6 | 12.7 | 12.9 | 22.2 | 29.4 | 17.9 | 30.8 | 40.9 |
| 7 | 15.0 | 9.64 | 16.6 | 22.0 | 13.3 | 22.9 | 30.3 |
| 8 | 17.2 | 6.38 | 11.0 | 14.5 | 8.66 | 14.9 | 19.7 |
| 9 | 19.5 | 3.11 | 5.35 | 7.10 | 4.03 | 6.92 | 9.18 |
| 10 | 21.7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 11 | 24.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Bm. CL | 25.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

The width-to-thickness ratio for the bottom flange is:

$$\lambda = \frac{b}{t}$$

$$= \frac{b_f}{2t_f}$$

$$= \frac{6.56 \text{ in.}}{2(0.650 \text{ in.})}$$

$$= 5.05 < 9.15$$

Because $\lambda < \lambda_p$, the flanges of both the top and bottom tees are compact; therefore, it is not necessary to check flange local buckling when calculating the available flexural strength.

Determine the limiting stem width-to-thickness ratio, $\lambda_r$, from AISC *Specification* Table B4.1a, Case 4:

$$\lambda_r = 0.75 \sqrt{\frac{E}{F_y}}$$

$$= 0.75 \sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 18.1$$

The width-to-thickness ratio for the top stem is:

$$\lambda = \frac{d_t}{t_w}$$

$$= \frac{5.50 \text{ in.}}{0.350 \text{ in.}}$$

$$= 15.7 < 18.1$$


*66 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*




<!-- Page 74 -->

<!-- Page 74 -->

The width-to-thickness ratio for the bottom stem is:

$$\lambda = \frac{d_t}{t_w}$$

$$= \frac{5.50 \text{ in.}}{0.405 \text{ in.}}$$

$$= 13.6 < 18.1$$

Because $\lambda < \lambda_r$, both top and bottom tee stems are nonslender, therefore, it is not necessary to consider AISC *Specification* Section E7 when calculating the available compressive strength.

It is not necessary to calculate the available compressive strength of the top or bottom tee in this example because all openings are fully composite, and therefore, all compression is taken by the concrete flange. If compression did exist in the top or bottom tee, the available compressive strength would be calculated as shown in Example 4.1.

*Calculate available tensile strength of bottom tee*

$$P_n = F_y A_{net-bot}$$
(from *Spec.* Eq. D2-1)

$$= (50 \text{ ksi})(6.22 \text{ in.}^2)$$

$$= 311 \text{ kips}$$

*Calculate available flexural strength of tee*

*Yielding*

For tee stems in compression:

$$M_{p-top} = M_y$$
(from *Spec.* Eq. F9-4)

$$M_y \quad = F_y S_{x-bot}$$
(from *Spec.* Eq. F9-3)

$$= (50 \text{ ksi})(2.86 \text{ in.}^3)$$

$$= 143 \text{ kip-in.}$$

$$M_{p-bot} = M_y$$
(from *Spec.* Eq. F9-4)

$$M_y \quad = F_y S_{x-top}$$
(from *Spec.* Eq. F9-3)

$$= (50 \text{ ksi})(3.29 \text{ in.}^3)$$

$$= 165 \text{ kip-in.}$$

In both cases, the stem is assumed to be in compression; this will be conservative for the bottom tee. It is possible to take advantage of this to calculate a higher value for the available flexural strength of the bottom tee because the stem is in tension.

*Lateral-torsional buckling*

For lateral-torsional buckling of the top tee:

$$B_{top} = -2.3 \left(\frac{d}{L_b}\right) \sqrt{\frac{I_y}{J}}$$
(*Spec.* Eq. F9-12)

$$= -2.3 \left(\frac{5.50 \text{ in.}}{8.00 \text{ in.}}\right) \sqrt{\frac{10.3 \text{ in.}^4}{0.266 \text{ in.}^4}}$$

$$= -9.84$$


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 67*




<!-- Page 75 -->

<!-- Page 75 -->

$$M_{cr-top} = \frac{1.95E}{L_b} \sqrt{I_y J} \left[ B + \sqrt{1 + B^2} \right]$$
(*Spec.* Eq. F9-10)

$$= \frac{1.95(29,000 \text{ ksi})}{8.00 \text{ in.}} \sqrt{(10.3 \text{ in.}^4)(0.266 \text{ in.}^4)} \left[ -9.84 + \sqrt{1 + (-9.84)^2} \right]$$

$$= 596 \text{ kip-in.}$$

For lateral-torsional buckling of the bottom tee:

$$B_{bot} = -2.3 \left(\frac{d}{L_b}\right) \sqrt{\frac{I_y}{J}}$$
(*Spec.* Eq. F9-12)

$$= -2.3 \left(\frac{5.50 \text{ in.}}{8.00 \text{ in.}}\right) \sqrt{\frac{15.3 \text{ in.}^4}{0.685 \text{ in.}^4}}$$

$$= -7.47$$

$$M_{cr-bot} = \frac{1.95E}{L_b} \sqrt{I_y J} \left[ B + \sqrt{1 + B^2} \right]$$
(*Spec.* Eq. F9-10)

$$= \frac{1.95(29,000 \text{ ksi})}{8.00 \text{ in.}} \sqrt{(15.3 \text{ in.}^4)(0.685 \text{ in.}^4)} \left[ -7.47 + \sqrt{1 + (-7.47)^2} \right]$$

$$= 1,550 \text{ kip-in.}$$

*Flange local buckling*

Per AISC *Specification* Section F9.3(a), the limit state of flange local buckling does not apply because the flanges are compact.

*Local buckling of tee stems*

The nominal flexural strength for local buckling of the tee stem in flexural compression, $M_n$, is determined using AISC *Specification* Section F9.4:

$$M_n = F_{cr} S_x$$
(*Spec.* Eq. F9-16)

Because $d/t_w < 0.84 \sqrt{\frac{E}{F_y}}$, the critical stress, $F_{cr}$, is determined using AISC *Specification* Equation F9-17:

$$F_{cr} = F_y$$
(*Spec.* Eq. F9-17)

And thus,

For the top tee:

$$M_{n-top} = F_y S_{x-bot}$$

$$= (50 \text{ ksi})(2.86 \text{ in.}^3)$$

$$= 143 \text{ kip-in.}$$

For the bottom tee:

$$M_{n-bot} = F_y S_{x-top}$$

$$= (50 \text{ ksi})(3.29 \text{ in.}^3)$$

$$= 165 \text{ kip-in.}$$


*68 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*




<!-- Page 76 -->

<!-- Page 76 -->

The available tensile and flexural strengths of the tee are:

| **LRFD** | **ASD** |
|---|---|
| *Available tensile strength—bottom tee* | *Available tensile strength—bottom tee* |
| $P_t = \phi_t P_n$ | $P_t = \frac{P_n}{\Omega_t}$ |
| $= 0.90(311 \text{ kips})$ | $= \frac{311 \text{ kips}}{1.67}$ |
| $= 280 \text{ kips}$ | $= 186 \text{ kips}$ |
| *Available flexural strength—top tee* | *Available flexural strength—top tee* |
| $M_n = \phi_b M_{p-top}$ | $M_n = \frac{M_{p-top}}{\Omega_b}$ |
| $= 0.90(143 \text{ kip-in.})$ | $= \frac{143 \text{ kip-in.}}{1.67}$ |
| $= 129 \text{ kip-in.}$ | $= 85.6 \text{ kip-in.}$ |
| *Available flexural strength—bottom tee* | *Available flexural strength—bottom tee* |
| $M_n = \phi_b M_{p-bot}$ | $M_n = \frac{M_{p-bot}}{\Omega_b}$ |
| $= 0.90(165 \text{ kip-in.})$ | $= \frac{165 \text{ kip-in.}}{1.67}$ |
| $= 149 \text{ kip-in.}$ | $= 98.8 \text{ kip-in.}$ |

*Check tees for combined axial and flexural loads*

The interaction values for each opening are presented in Table 4-21.

From Table 4-21, the composite Vierendeel bending is summarized as follows:

| **LRFD** | **ASD** |
|---|---|
| *Top tee* | *Top tee* |
| $I_{max} = 0.549 < 1.0 \quad \textbf{o.k.}$ | $I_{max} = 0.586 < 1.0 \quad \textbf{o.k.}$ |
| *Bottom tee* | *Bottom tee* |
| $I_{max} = 0.858 < 1.0 \quad \textbf{o.k.}$ | $I_{max} = 0.911 < 1.0 \quad \textbf{o.k..}$ |

*Check web post buckling*

It is necessary to check both the top and bottom web posts for buckling in this case. Although the top web post is thinner and is therefore more likely to buckle first, the value of $2h/e$ is different for the top and bottom web posts, and it is therefore necessary to investigate both web posts.

*Calculate vertical and horizontal shear and resultant moment at each gross section for web post buckling check*

Table 4-22 presents the vertical shear force at each opening, and Table 4-23 presents the horizontal shear force at each web post.

From Section 3.4.1a, calculate the horizontal shear, $V_{rh}$, using Equation 3-19:

$$V_{rh} = |T_{r(i)} - T_{r(i+1)}|$$
(3-19)


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 69*




<!-- Page 77 -->

<!-- Page 77 -->

| Table 4-21. Interaction Values at Each Opening for LRFD and ASD |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| **Opening Number** | $X_i,$ ft | $P_t,$ kips | $M_{vt-top},$ kip-in. | $M_n,$ kip-in. | $P_n,$ kips | $M_{vt-bot},$ kip-in. | $P_t,$ kips | Spec. Eq. H1-1a | Spec. Eq. H1-1b | Interaction* |
| End | 0.000 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| 1 | 1.46 | 0.000 | 70.7 | 129 | 0.549 | 93.7 | 280 | 0.853 | 0.678 | 0.678 |
| 2 | 3.71 | 0.000 | 62.7 | 129 | 0.486 | 83.2 | 280 | 0.756 | 0.609 | 0.609 |
| 3 | 5.96 | 0.000 | 54.8 | 129 | 0.425 | 94.3 | 72.6 | 0.759 | 0.699 | 0.772 |
| 4 | 8.21 | 0.000 | 83.2 | 129 | 0.363 | 123 | 62.0 | 0.843 | 0.659 | 0.813 |
| 5 | 10.5 | 0.000 | 46.8 | 129 | 0.301 | 149 | 51.5 | 0.932 | 0.719 | 0.932 |
| 6 | 12.7 | 0.000 | 30.8 | 129 | 0.239 | 171 | 40.9 | 0.610 | 0.456 | 0.456 |
| 7 | 15.0 | 0.000 | 22.9 | 129 | 0.178 | 189 | 30.3 | 0.478 | 0.358 | 0.358 |
| 8 | 17.2 | 0.000 | 14.9 | 129 | 0.116 | 204 | 19.7 | 0.376 | 0.282 | 0.282 |
| 9 | 19.5 | 0.000 | 6.92 | 129 | 0.054 | 215 | 9.18 | 0.767 | 0.622 | 0.622 |
| 10 | 21.7 | 0.000 | 0.000 | 129 | 0.000 | 222 | 0.000 | 0.793 | 0.397 | 0.793 |
| 11 | 24.0 | 0.000 | 0.000 | 129 | 0.000 | 226 | 0.000 | 0.809 | 0.403 | 0.809 |
| Bm. CL | 25.0 | 0.000 | 0.000 | 129 | 0.000 | 226 | 0.000 | 0.807 | 0.404 | 0.807 |

| **ASD** |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
| **Opening Number** | $X_i,$ ft | $P_t,$ kips | $M_{vt-top},$ kip-in. | $M_n,$ kip-in. | $P_n,$ kips | $M_{vt-bot},$ kip-in. | $P_t,$ kips | Spec. Eq. H1-1a | Spec. Eq. H1-1b | Interaction* |
| **Top Tee** |  |  |  |  |  |  |  |  |  |  |
| End | 0.000 | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| 1 | 1.46 | 0.000 | 70.7 | 85.6 | 0.586 | 17.8 | 60.6 | 0.699 | 0.697 | 0.724 |
| 2 | 3.71 | 0.000 | 54.6 | 85.6 | 0.525 | 43.3 | 59.2 | 0.732 | 0.708 | 0.766 |
| 3 | 5.96 | 0.000 | 62.7 | 85.6 | 0.461 | 86.7 | 51.7 | 0.785 | 0.754 | 0.817 |
| 4 | 8.21 | 0.000 | 83.4 | 85.6 | 0.390 | 86.7 | 44.3 | 0.465 | 0.665 | 0.665 |
| 5 | 10.5 | 0.000 | 27.8 | 85.6 | 0.324 | 120 | 36.9 | 0.581 | 0.664 | 0.665 |
| 6 | 12.7 | 0.000 | 22.2 | 85.6 | 0.259 | 120 | 29.4 | 0.474 | 0.551 | 0.551 |
| 7 | 15.0 | 0.000 | 16.6 | 85.6 | 0.193 | 133 | 22.0 | 0.712 | 0.911 | 0.579 |
| 8 | 17.2 | 0.000 | 11.0 | 85.6 | 0.128 | 143 | 14.5 | 0.337 | 0.698 | 0.551 |
| 9 | 19.5 | 0.000 | 5.35 | 85.6 | 0.063 | 151 | 7.10 | 0.333 | 0.393 | 0.699 |
| 10 | 21.7 | 0.000 | 0.000 | 85.6 | 0.000 | 156 | 0.000 | 0.836 | 0.418 | 0.836 |
| 11 | 24.0 | 0.000 | 0.000 | 85.6 | 0.000 | 156 | 0.000 | 0.849 | 0.425 | 0.849 |
| Bm. CL | 25.0 | 0.000 | 0.000 | 85.6 | 0.000 | 159 | 0.000 | 0.907 | 0.404 | 0.911 |


*70 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*




<!-- Page 78 -->

<!-- Page 78 -->

| Table 4-22. Vertical Shear Force at Each Opening |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  | **ASD** |  |  | **LRFD** |  |  |
| **Post Number** | $X_i,$ ft | $V_{r(i-1)},$ kips | $V_{r(i+1)},$ kips | $V_{r(i)},$ kips | $V_{r(i-1)},$ kips | $V_{r(i+1)},$ kips | $V_{r(i)},$ kips |
| 1 | 2.58 | 29.2 | 26.0 | 21.5 | 41.1 | 36.5 | 38.8 |
| 2 | 4.83 | 26.0 | 22.7 | 19.2 | 36.5 | 31.8 | 34.2 |
| 3 | 7.08 | 22.7 | 19.4 | 16.8 | 31.8 | 27.2 | 29.5 |
| 4 | 9.33 | 19.4 | 16.2 | 14.4 | 27.2 | 22.6 | 24.9 |
| 5 | 11.6 | 16.2 | 12.9 | 12.1 | 22.6 | 17.9 | 20.3 |
| 6 | 13.8 | 12.9 | 9.64 | 9.72 | 17.9 | 13.3 | 15.6 |
| 7 | 16.1 | 9.64 | 6.38 | 7.35 | 13.3 | 8.66 | 11.0 |
| 8 | 18.3 | 6.38 | 3.11 | 4.99 | 8.66 | 4.03 | 6.34 |
| 9 | 20.6 | 3.11 | 0.000 | 2.63 | 4.03 | 0.000 | 2.01 |
| 10 | 22.8 | 0.000 | 0.000 | 0.339 | 0.000 | 0.000 | 0.000 |
| 11 | 24.5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
|  | Maximum: | 29.2 |  | Maximum: | 41.1 |  | Maximum: | 38.8 |

| Table 4-23. Horizontal Shear Force at Each Web Post |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
|  |  | **ASD** |  |  | **LRFD** |  |  |
| **Opening Number** | $X_i,$ ft | $T_{r(i)},$ kips | $T_{r(i+1)},$ kips | $V_{rh} = \Delta T_r,$ kips | $T_{r(i)},$ kips | $T_{r(i+1)},$ kips | $V_{rh} = \Delta T_r,$ kips |
| End | 0.000 | 0.000 |  |  |  |  |  |
| 1 | 1.46 | 17.8 | 43.3 | 25.5 | 25.3 | 61.6 | 36.3 |
| 2 | 3.71 | 43.3 | 66.2 | 22.9 | 61.6 | 94.3 | 32.7 |
| 3 | 5.96 | 66.2 | 86.7 | 20.5 | 94.3 | 123 | 28.7 |
| 4 | 8.21 | 86.7 | 105 | 18.3 | 123 | 149 | 26.0 |
| 5 | 10.5 | 105 | 120 | 15.0 | 149 | 171 | 22.0 |
| 6 | 12.7 | 120 | 133 | 13.0 | 171 | 189 | 18.0 |
| 7 | 15.0 | 133 | 143 | 10.0 | 189 | 204 | 15.0 |
| 8 | 17.2 | 143 | 151 | 8.00 | 204 | 215 | 11.0 |
| 9 | 19.5 | 151 | 156 | 5.00 | 215 | 222 | 7.00 |
| 10 | 21.7 | 156 | 158 | 2.00 | 222 | 226 | 4.00 |
| 11 | 24.0 | 158.4 | 158.7 | 0.300 | 225.9 | 226.3 | 0.400 |
| Bm. CL | 25.0 | 159 |  |  | 226 |  |  |


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 71*




<!-- Page 79 -->

<!-- Page 79 -->

*Calculate web post buckling flexural strength*

| **LRFD** | **ASD** |
|---|---|
| From Table 4-23, | From Table 4-23, |
| $V_{rh} \quad = 36.3 \text{ kips}$ | $V_{rh} \quad = 25.5 \text{ kips}$ |
| $M_{vt-top} = V_{rh} h_{top}$ | (from Eq. 3-20) | $M_{vt-top} = V_{rh} h_{top}$ | (from Eq. 3-20) |
| $\quad = (36.3 \text{ kips})(9.70 \text{ in.})$ | $\quad = (25.5 \text{ kips})(9.70 \text{ in.})$ |
| $\quad = 352 \text{ kip-in.}$ | $\quad = 247 \text{ kip-in.}$ |
| $M_{vt-bot} = V_{rh} h_{bot}$ | (from Eq. 3-21) | $M_{vt-bot} = V_{rh} h_{bot}$ | (from Eq. 3-21) |
| $\quad = (36.3 \text{ kips})(10.1 \text{ in.})$ | $\quad = (25.5 \text{ kips})(10.1 \text{ in.})$ |
| $\quad = 367 \text{ kip-in.}$ | $\quad = 258 \text{ kip-in.}$ |

*Calculate available flexural strength of web post*

*Top web post*

$$M_p \quad = 0.25t_w (e + 2b)^2 F_y$$
(3-22)

$$= 0.25(0.350 \text{ in.})\left[8.00 \text{ in.} + 2(5.50 \text{ in.})\right]^2 (50 \text{ ksi})$$

$$= 1,580 \text{ kip-in.}$$

$$\frac{2h_{top}}{e} = \frac{2(9.70 \text{ in.})}{8.00 \text{ in.}}$$

$$= 2.43$$

$$\frac{e}{t_w} \quad = \frac{8.00 \text{ in.}}{0.350 \text{ in.}}$$

$$= 22.9$$

For $\theta = 60°$

For $e/t_w = 10$

$$\frac{M_{ocr}}{M_p} = 0.587(0.917)^{-\frac{2h_{top}}{e}}$$
(3-26)

$$= 0.587(0.917)^{2.43}$$

$$= 0.476 < 0.493$$

For $e/t_w = 20$

$$\frac{M_{ocr}}{M_p} = 1.96(0.699)^{-\frac{2h_{top}}{e}}$$
(3-27)

$$= 1.96(0.699)^{2.43}$$

$$= 0.821 > 0.493$$

For $e/t_w = 30$

$$\frac{M_{ocr}}{M_p} = 2.55(0.574)^{-\frac{2h_{top}}{e}}$$
(3-28)

$$= 2.55(0.574)^{2.43}$$

$$= 0.662 > 0.493$$


*72 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*




<!-- Page 80 -->

<!-- Page 80 -->

For $e/t_w = 22.9$, use

$$\frac{M_{ocr}}{M_p} = 0.476$$

*Bottom web post*

$$M_p \quad = 0.25t_w (e + 2b)^2 F_y$$
(3-22)

$$= 0.25(0.405 \text{ in.})\left[8.00 \text{ in.} + 2(5.50 \text{ in.})\right]^2 (50 \text{ ksi})$$

$$= 1,830 \text{ kip-in.}$$

$$\frac{2h_{bot}}{e} = \frac{2(10.1 \text{ in.})}{8.00 \text{ in.}}$$

$$= 2.53$$

$$\frac{e}{t_w} \quad = \frac{8.00 \text{ in.}}{0.405 \text{ in.}}$$

$$= 19.8$$

For $e/t_w = 10$

$$\frac{M_{ocr}}{M_p} = 0.587(0.917)^{-\frac{2h_{bot}}{e}}$$
(3-26)

$$= 0.587(0.917)^{2.53}$$

$$= 0.471 < 0.493$$

For $e/t_w = 20$

$$\frac{M_{ocr}}{M_p} = 1.96(0.699)^{-\frac{2h_{bot}}{e}}$$
(3-27)

$$= 1.96(0.699)^{2.53}$$

$$= 0.792 > 0.493$$

For $e/t_w = 30$

$$\frac{M_{ocr}}{M_p} = 2.55(0.574)^{-\frac{2h_{bot}}{e}}$$
(3-28)

$$= 2.55(0.574)^{2.53}$$

$$= 0.626 > 0.493$$

For $e/t_w = 19.8$, use

$$\frac{M_{ocr}}{M_p} = 0.471$$


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 73*




<!-- Page 81 -->

<!-- Page 81 -->

From Equation 3-29a and 3-29b, the available flexural strength is

| LRFD | ASD |
|------|-----|
| *Top web post* | *Top web post* |
| $\phi_b \left( \frac{M_{ocr}}{M_p} \right) M_{p-top} = 0.90(0.476)(1,580 \text{ kip-in.})$ | $\frac{1}{\Omega_b} \left( \frac{M_{ocr}}{M_p} \right) M_{p-top} = \frac{1}{1.67}(0.476)(1,580 \text{ kip-in.})$ |
| $= 677 \text{ kip-in.}$ | $= 450 \text{ kip-in.}$ |
| $I_{max-top} = \frac{352 \text{ kip-in.}}{677 \text{ kip-in.}}$ | $I_{max} = \frac{247 \text{ kip-in.}}{450 \text{ kip-in.}}$ |
| $= 0.520 < 1.0$ **o.k.** | $= 0.549 < 1.0$ **o.k.** |
| *Bottom web post* | *Bottom web post* |
| $\phi_b \left( \frac{M_{ocr}}{M_p} \right) M_{p-bot} = 0.90(0.471)(1,830 \text{ kip-in.})$ | $\frac{1}{\Omega_b} \left( \frac{M_{ocr}}{M_p} \right) M_{p-bot} = \frac{1}{1.67}(0.471)(1,830 \text{ kip-in.})$ |
| $= 776 \text{ kip-in.}$ | $= 516 \text{ kip-in.}$ |
| $I_{max-bot} = \frac{366 \text{ kip-in.}}{776 \text{ kip-in.}}$ | $I_{max} = \frac{257 \text{ kip-in.}}{516 \text{ kip-in.}}$ |
| $= 0.472 < 1.0$ **o.k.** | $= 0.498 < 1.0$ **o.k.** |

*Check horizontal shear*

The available horizontal shear strength is calculated using AISC *Specification* Section J4.2. By inspection, the top section will control because the web is thinner.

| LRFD | ASD |
|------|-----|
| From Table 4-23, | From Table 4-23, |
| $V_n = 36.3 \text{ kips}$ | $V_n = 25.5 \text{ kips}$ |
| From *Spec.* Eq. J4-3, | From *Spec.* Eq. J4-3, |
| $\phi_v V_{n-horiz} = \phi_v 0.6 F_y (et_w)$ | $\frac{V_{n-horiz}}{\Omega_v} = \frac{0.6F_y (et_w)}{\Omega_v}$ |
| $= 1.00(0.6)(50 \text{ ksi})[(8.00 \text{ in.})(0.350 \text{ in.})]$ | $= \frac{0.6(50 \text{ ksi})[(8.00 \text{ in.})(0.350 \text{ in.})]}{1.50}$ |
| $= 84.0 \text{ kips} > 36.3 \text{ kips}$ **o.k.** | $= 56.0 \text{ kips} > 25.5 \text{ kips}$ **o.k.** |

*Check vertical shear*

The concrete shear strength will be disregarded when checking vertical shear for the net and gross sections. The concrete shear strength will be added to the net shear force.


*74 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*



<!-- Page 82 -->

<!-- Page 82 -->

Check vertical shear at the beam net section:

| LRFD | ASD |
|------|-----|
| From Table 4-16, | From Table 4-16, |
| $V_{u-net} = 41.1 \text{ kips}$ | $V_{u-net} = 29.2 \text{ kips}$ |
| $V_{u-global} = V_{u-net} + concrete\ shear\ strength$ | $V_{u-global} = V_{u-net} + concrete\ shear\ strength$ |
| $= 41.1 \text{ kips} + 7.39 \text{ kips}$ | $= 29.2 \text{ kips} + 4.93 \text{ kips}$ |
| $= 48.5 \text{ kips}$ | $= 34.1 \text{ kips}$ |

The shear force between the top and bottom tees will be divided based on their relative areas.

| LRFD | ASD |
|------|-----|
| $V_{u-top} = V_{u-global} \left( \frac{A_{tee-top}}{A_{net}} \right)$ | $V_{u-top} = V_{u-global} \left( \frac{A_{tee-top}}{A_{net}} \right)$ |
| $= (48.5 \text{ kips}) \left( \frac{4.70 \text{ in.}^2}{10.9 \text{ in.}^2} \right)$ | $= (34.1 \text{ kips}) \left( \frac{4.70 \text{ in.}^2}{10.9 \text{ in.}^2} \right)$ |
| $= 20.9 \text{ kips}$ | $= 14.7 \text{ kips}$ |
| $V_{u-bot} = V_{u-global} \left( \frac{A_{tee-bot}}{A_{net}} \right)$ | $V_{u-bot} = V_{u-global} \left( \frac{A_{tee-bot}}{A_{net}} \right)$ |
| $= (48.5 \text{ kips}) \left( \frac{6.22 \text{ in.}^2}{10.9 \text{ in.}^2} \right)$ | $= (34.1 \text{ kips}) \left( \frac{6.22 \text{ in.}^2}{10.9 \text{ in.}^2} \right)$ |
| $= 27.7 \text{ kips}$ | $= 19.5 \text{ kips}$ |

*Check vertical shear at top and bottom tees*

From AISC *Specification* Section G3,

Top tee:

$$\frac{h}{t_w} = \frac{d_{t-top}}{t_{w-top}}$$

$$= \frac{5.50 \text{ in.}}{0.350 \text{ in.}}$$

$$= 15.7 < 1.10 \sqrt{\frac{1.2(29,000 \text{ ksi})}{50 \text{ ksi}}} = 29.0$$

Because $h/t_w < 1.10\sqrt{k_v E/F_y}$,

$$C_{v2} = 1.0$$ (*Spec.* Eq. G2-9)

$$V_{n-top} = 0.60 F_y (d_{t-top} t_{w-top}) C_{v2}$$ (from *Spec.* Eq. G3-1)

$$= 0.60(50 \text{ ksi})(5.50 \text{ in.})(0.350 \text{ in.})(1.0)$$

$$= 57.8 \text{ kips}$$


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 75*



<!-- Page 83 -->

<!-- Page 83 -->

Bottom tee:

$$\frac{h}{t_w} = \frac{d_{t-bot}}{t_{w-bot}}$$

$$= \frac{5.50 \text{ in.}}{0.405 \text{ in.}}$$

$$= 13.6 < 1.10 \sqrt{\frac{1.2(29,000 \text{ ksi})}{50 \text{ ksi}}} = 29.0$$

Because $h/t_w < 1.10\sqrt{k_v E/F_y}$,

$$C_{v2} = 1.0$$ (*Spec.* Eq. G2-9)

$$V_{n-bot} = 0.60 F_y (d_{t-bot} t_{w-bot}) C_{v2}$$ (from *Spec.* Eq. G3-1)

$$= 0.60(50 \text{ ksi})(5.50 \text{ in.})(0.405 \text{ in.})(1.0)$$

$$= 66.8 \text{ kips}$$

*Available vertical shear strength at top and bottom tees*

| LRFD | ASD |
|------|-----|
| $\phi_v V_{n-top} = 1.00(57.8 \text{ kips})$ | $\frac{V_{n-top}}{\Omega_v} = \frac{57.8 \text{ kips}}{1.50}$ |
| $= 57.8 \text{ kips}$ | $= 38.5 \text{ kips}$ |
| $\phi_v V_{n-bot} = 1.00(66.8 \text{ kips})$ | $\frac{V_{n-bot}}{\Omega_v} = \frac{66.8 \text{ kips}}{1.50}$ |
| $= 66.8 \text{ kips}$ | $= 44.5 \text{ kips}$ |

*Check vertical shear at beam gross section*

| LRFD | ASD |
|------|-----|
| $V_{u-net} = 44.1 \text{ kips}$ (see Table 4-16) | $V_{u-net} = 31.3 \text{ kips}$ (see Table 4-16) |
| $V_{u-global} = V_{u-net} + \ concrete\ shear\ strength$ | $V_{u-global} = V_{u-net} + \ concrete\ shear\ strength$ |
| $= 44.1 \text{ kips} + 7.39 \text{ kips}$ | $= 31.3 \text{ kips} + 4.93 \text{ kips}$ |
| $= 51.5 \text{ kips}$ | $= 36.2 \text{ kips}$ |

From AISC *Specification* Section G2.1(b)(1):

$$\frac{h}{t_{w-min}} = \frac{30.8 \text{ in.} - (0.950 \text{ in.} + 1.15 \text{ in.})}{0.350 \text{ in.}}$$

$$= 82.0$$

$$C_{v1} = \frac{1.10\sqrt{k_v E/F_y}}{h/t_w}$$ (*Spec.* Eq. G2-4)

$$= \frac{1.10\sqrt{5.34(29,000 \text{ ksi})/(50 \text{ksi})}}{82.0}$$

$$= 0.747$$

$$V_{n-gross} = 0.60 F_y (d_{t-g-min}) C_{v1}$$ (from *Spec.* Eq. G2-1)

$$= 0.60(50 \text{ ksi})(30.8 \text{ in.})(0.350 \text{ in.})(0.747)$$

$$= 242 \text{ kips}$$


*76 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*



<!-- Page 84 -->

<!-- Page 84 -->

From AISC *Specification* Section G1:

$$\frac{h}{t_w} = 82.0 > 2.24 \sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}} = 53.9$$

Therefore, $\phi_v = 0.90$ and $\Omega_v = 1.67$.

*Available vertical shear strength at gross section*

| LRFD | ASD |
|------|-----|
| $\phi_v V_{n-gross} = 0.90(242 \text{ kips})$ | $\frac{V_{n-gross}}{\Omega_v} = \frac{242 \text{ kips}}{1.67}$ |
| $= 218 \text{ kips}$ | $= 145 \text{ kips}$ |

The following is a summary of the beam shear strengths:

| LRFD | ASD |
|------|-----|
| *Horizontal shear* | *Horizontal shear* |
| $V_n/\phi_v V_{n-horiz} = 36.3 \text{ kips}/84.0 \text{ kips}$ | $V_u\Omega_v/V_{n-horiz} = 25.5 \text{ kips}/56.0 \text{ kips}$ |
| $= 0.432$ **o.k.** | $= 0.455$ **o.k.** |
| *Vertical shear–top tee* | *Vertical shear–top tee* |
| $V_{u-top}/\phi_v V_{n-top} = 20.9 \text{ kips}/57.8 \text{ kips}$ | $V_{u-top}\Omega_v/V_{n-top} = 14.7 \text{ kips}/38.5 \text{ kips}$ |
| $= 0.362$ **o.k.** | $= 0.382$ **o.k.** |
| *Vertical shear–bottom tee* | *Vertical shear–bottom tee* |
| $V_{u-bot}/\phi_v V_{n-bot} = 27.7 \text{ kips}/66.8 \text{ kips}$ | $V_{u-bot}\Omega_v/V_{n-bot} = 19.5 \text{ kips}/44.5 \text{ kips}$ |
| $= 0.415$ **o.k.** | $= 0.438$ **o.k.** |
| *Vertical shear–gross section* | *Vertical shear–gross section* |
| $V_{u-global}/\phi_v V_{n-gross} = 51.5 \text{ kips}/218 \text{ kips}$ | $V_{u-global}\Omega_v/V_{n-gross} = 36.2 \text{ kips}/145 \text{ kips}$ |
| $= 0.236$ **o.k.** | $= 0.250$ **o.k.** |

*Check deflection*

Deflections are calculated using 90% of the moment of inertia per Section 3.7.

The pre-composite dead load deflection is:

$$\Delta_{PDL} = \frac{5wL^4}{384EI_{x-top}(0.90)}$$

$$= \frac{5\left(\frac{0.44 \text{ kip/ft}}{12 \text{ in./ft}}\right)[(50 \text{ ft})(12 \text{ in./ft})]^4}{384(29,000 \text{ ksi})(2,180 \text{ in.}^4)(0.90)}$$

$$= 1.09 \text{ in.}$$


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 77*



<!-- Page 85 -->

<!-- Page 85 -->

Live load deflection is:

$$\Delta_{LL} = \frac{5wL^4}{384EI_{x-comp}(0.90)}$$

$$= \frac{5\left(\frac{0.8 \text{ kip/ft}}{12 \text{ in./ft}}\right)[(50 \text{ ft})(12 \text{ in./ft})]^4}{384(29,000 \text{ ksi})(5,740 \text{ in.}^4)(0.90)}$$

$$= 0.749 \text{ in.}$$

$$= \frac{L}{800}$$

Dead load deflection is:

$$\Delta_{DL} = \frac{5wL^4}{384EI_{x-comp}\phi}$$

$$= \frac{5\left(\frac{0.16 \text{ kip/ft}}{12 \text{ in./ft}}\right)[(50 \text{ ft})(12 \text{ in./ft})]^4}{384(29,000 \text{ ksi})(5,740 \text{ in.}^4)(0.90)}$$

$$= 0.150 \text{ in.}$$

$$= \frac{L}{4,000}$$

Total load deflection is:

$$\Delta_{TL} = \Delta_{LL} + \Delta_{DL}$$

$$= 0.749 \text{ in.} + 0.150 \text{ in.}$$

$$= 0.899 \text{ in.}$$

$$= \frac{L}{667}$$

*Deflection summary*

$$\Delta_{PDL} = 1.09 \text{ in.}$$; therefore, camber 1 in.

$$\Delta_{LL} \leq \frac{L}{360}$$ **o.k.**

$$\Delta_{TL} \leq \frac{L}{240}$$ **o.k.**

## Example 4.4—Composite Cellular Beam Design

### Given:

Evaluate the same beam from Example 4.3 using a cellular beam instead of a castellated beam, as shown in Figure 4-7. As in the noncomposite cellular beam, a rectangular opening will be approximated for Vierendeel bending.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$


*78 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*



<!-- Page 86 -->

<!-- Page 86 -->

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Top root beam
W21×44
$A = 13.0 \text{ in.}^2$ $d_{top} = 20.7 \text{ in.}$ $t_w = 0.350 \text{ in.}$ $b_f = 6.50 \text{ in.}$ $t_f = 0.450 \text{ in.}$ $I_x = 843 \text{ in.}^4$
$S_x = 81.6 \text{ in.}^3$ $Z_x = 95.4 \text{ in.}^3$

Bottom root beam
W21×57
$A = 16.7 \text{ in.}^2$ $d_{bot} = 21.1 \text{ in.}$ $t_w = 0.405 \text{ in.}$ $b_f = 6.56 \text{ in.}$ $t_f = 0.650 \text{ in.}$ $I_x = 1,170 \text{ in.}^4$
$S_x = 111 \text{ in.}^3$ $Z_x = 129 \text{ in.}^3$

Resultant shape properties for the LB30×44/57 are determined as follows:

The values of $D_o$ and $S$ are designated based on the depth of the original beam section and a trial opening size.

$$D_o = 20.8 \text{ in.}$$

$$S = 28.8 \text{ in.}$$

$$e = S - D_o$$ (4-16)

$$= 8.00 \text{ in.}$$

$$loss = \frac{D_o}{2} - \sqrt{\left(\frac{D_o}{2}\right)^2 - \left(\frac{S - D_o}{2}\right)^2}$$ (4-17)

$$= \frac{20.8 \text{ in.}}{2} - \sqrt{\left(\frac{20.8 \text{ in.}}{2}\right)^2 - \left(\frac{28.8 \text{ in.} - 20.8 \text{ in.}}{2}\right)^2}$$

$$= 0.802 \text{ in.}$$

$$d_{t-top-net} = \frac{1}{2}\left[d_{top} - \left(\frac{D_o}{2} + loss\right)\right]$$ (4-41)

$$= \frac{1}{2}\left[20.7 \text{ in.} - \left(\frac{20.8 \text{ in.}}{2} + 0.802 \text{ in.}\right)\right]$$

$$= 4.75 \text{ in.}$$

![Structural framing layout and composite cellular beam nomenclature for Example 4.4. The figure shows three views: a plan view of the beam layout between columns 1 and 2, a detailed cross-section of the cellular beam showing the circular openings and dimensions, and elevation views showing the beam depth and component dimensions. Key dimensions include 50'-0" span, LB30×44/57 typ., W21×44 (top) + W21×57 (bot), with various dimensional annotations including $S$, $e$, $D_o$, $d$, $d_{t-top}$, $d_{t-bot}$, $b_f$, $t_f$, and $t_w$ for both top and bottom sections.]

*Fig. 4-7. Structural framing layout and composite cellular beam nomenclature for Example 4.4.*


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 79*



<!-- Page 87 -->

<!-- Page 87 -->

$$d_{t-bot-net} = \frac{1}{2}\left[d_{bot} - \left(\frac{D_o}{2} + loss\right)\right]$$ (4-42)

$$= \frac{1}{2}\left[21.1 \text{ in.} - \left(\frac{20.8 \text{ in.}}{2} + 0.802 \text{ in.}\right)\right]$$

$$= 4.95 \text{ in.}$$

$$d_g = d_{t-top-net} + D_o + d_{t-bot-net}$$ (4-43)

$$= 4.75 \text{ in.} + 20.8 \text{ in.} + 4.95 \text{ in.}$$

$$= 30.5 \text{ in.}$$

$$y = \sqrt{(0.5D_o)^2 - (0.225D_o)^2}$$ (4-20)

$$= \sqrt{[(0.5)(20.8 \text{ in.})]^2 - [(0.225)(20.8 \text{ in.})]^2}$$

$$= 9.29 \text{ in.}$$

$$d_{t-top-crit} = \frac{D_o}{2} - y + d_{t-top-net}$$ (from Eq. 4-21)

$$= \frac{20.8 \text{ in.}}{2} - 9.29 \text{ in.} + 4.75 \text{ in.}$$

$$= 5.86 \text{ in.}$$

$$d_{t-bot-crit} = \frac{D_o}{2} - y + d_{t-bot-net}$$ (from Eq. 4-21)

$$= \frac{(20.8 \text{ in.})}{2} - 9.29 \text{ in.} + 4.95 \text{ in.}$$

$$= 6.06 \text{ in.}$$

*Check limits of applicability*

According to Section 3.4, the design procedures for web post buckling are only applicable if the following conditions concerning the cutting pattern are met: $1.08 < S/D_o < 1.5$ and $1.25 < d_g/D_o < 1.75$.

$$\frac{S}{D_o} = \frac{28.8 \text{ in.}}{20.8 \text{ in.}}$$

$$= 1.38 < 1.5$$ **o.k.**

$$\frac{d_g}{D_o} = \frac{30.5 \text{ in.}}{20.8 \text{ in.}}$$

$$= 1.47 < 1.75$$ **o.k.**

*Calculate section properties of top and bottom tees and beam*

Relevant cross sections are provided in Figure 4-8, and the section properties for the top and bottom tees are reported in Tables 4-24 through 4-27.

*Beam net section properties at center of opening*

$$A_{net} = A_{tee-top} + A_{tee-bot}$$ (3-7)

$$= 444 \text{ in.}^2 + 6.01 \text{ in.}^2$$

$$= 10.5 \text{ in.}^2$$

$$\overline{y}_{bs} = \frac{A_{tee-top}(d_g - \overline{y}_{tee-top}) + A_{tee-bot}\overline{y}_{tee-bot}}{A_{net}}$$ (from Eq. 4-25)

$$= \frac{(4.44 \text{ in.}^2)(30.5 \text{ in.} - 3.73 \text{ in.}) + (6.01 \text{ in.}^2)(1.05 \text{ in.})}{10.5 \text{ in.}^2}$$

$$= 11.9 \text{ in.}$$


*80 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*



<!-- Page 88 -->

<!-- Page 88 -->

![Figure 4-8 showing detailed cross-sectional views of cellular beam components with dimensions. The figure includes:

Top row: Two detailed cross-sections labeled "At Net Section" and "At Net Section" showing PNA and ENA positions with specific measurements (4.76", 6.50", 0.450", 3.73", 4.42", 4.96", 0.650", 3.92", 4.50", 0.405", 6.56")

Middle row: Two sections labeled "At Critical Section Top Tee-W21×44" and "At Critical Section Bottom Tee-W21×57" showing PNA and ENA positions with detailed dimensions (5.87", 6.50", 0.450", 4.49", 5.50", 6.07", 6.56", 0.350", 4.71", 5.56")

Bottom row: Three sections showing "At Net Section", "At Critical Section", and "Composite Section at Critical Steel Section". The composite section shows a cross-beam with dimensions 96", 3", Δ_d markings, and notes "ENA of composite section" and "ENA of steel section".]

*Fig. 4-8. Tee, net and composite section for cellular beam for Example 4.4.*


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 81*

