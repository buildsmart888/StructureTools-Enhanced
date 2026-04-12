# Example 4.3: Composite Castellated Beam

<!-- Consolidated from pages 89-104 -->


<!-- Page 89 -->

<!-- Page 89 -->

| **Table 4-24. Top Tee Section Properties at Center of Opening** |
|---|
| $A_{tee-top} = 4.44 \text{ in.}^2$ | $x = 4.42 \text{ in.}$ | $r_x = 1.35 \text{ in.}$ | $r_y = 1.53 \text{ in.}$ |
| $y_{tee-top} = 3.73 \text{ in.}$ | $S_{x-top} = 7.76 \text{ in.}^3$ | $S_{x-bot} = 2.16 \text{ in.}^3$ | $Z_x = 3.83 \text{ in.}^3$ |
| $I_{x-tee-top} = 8.03 \text{ in.}^4$ | $I_y = 10.3 \text{ in.}^4$ | $J = 0.255 \text{ in.}^4$ | $y_o = 3.50 \text{ in.}$ |

Note: The fillet radius is assumed to be zero in the section properties calculations.

| **Table 4-25. Bottom Tee Section Properties at Center of Opening** |
|---|
| $A_{tee-bot} = 6.01 \text{ in.}^2$ | $x = 0.458 \text{ in.}$ | $r_x = 1.32 \text{ in.}$ | $r_y = 1.60 \text{ in.}$ |
| $y_{tee-bot} = 1.05 \text{ in.}$ | $S_{x-top} = 2.68 \text{ in.}^3$ | $S_{x-bot} = 10.0 \text{ in.}^3$ | $Z_x = 4.91 \text{ in.}^3$ |
| $I_{x-tee-bot} = 10.5 \text{ in.}^4$ | $I_y = 15.3 \text{ in.}^4$ | $J = 0.673 \text{ in.}^4$ | $y_o = 0.72 \text{ in.}$ |

Note: The fillet radius is assumed to be zero in the section properties calculations.

| **Table 4-26. Top Tee Section Properties at Critical Section** |
|---|
| $A_{crit-top} = 4.82 \text{ in.}^2$ | $x = 5.50 \text{ in.}$ | $y = 4.49 \text{ in.}$ | $\overline{y}_{crit-top} = 1.38 \text{ in.}$ |
| $S_{x-top} = 10.6 \text{ in.}^3$ | $S_{x-bot} = 3.25 \text{ in.}^3$ | $Z_x = 5.76 \text{ in.}^3$ | $J = 0.271 \text{ in.}^4$ |
| $I_{x-crit-top} = 14.6 \text{ in.}^4$ | $I_y = 10.3 \text{ in.}^4$ | $r_x = 1.74 \text{ in.}$ | $r_y = 1.46 \text{ in.}$ |

Note: The fillet radius is assumed to be zero in the section properties calculations.

| **Table 4-27. Bottom Tee Section Properties at Critical Section** |
|---|
| $A_{crit-bot} = 6.46 \text{ in.}^2$ | $x = 0.492 \text{ in.}$ | $y = 4.71 \text{ in.}$ | $\overline{y}_{crit-bot} = 1.36 \text{ in.}$ |
| $S_{x-top} = 4.01 \text{ in.}^3$ | $S_{x-bot} = 13.9 \text{ in.}^3$ | $Z_x = 7.17 \text{ in.}^3$ | $J = 0.698 \text{ in.}^4$ |
| $I_{x-crit-bot} = 18.9 \text{ in.}^4$ | $I_y = 15.3 \text{ in.}^4$ | $r_x = 1.71 \text{ in.}$ | $r_y = 1.54 \text{ in.}$ |

Note: The fillet radius is assumed to be zero in the section properties calculations.

$$\overline{y}_t = d_g - \overline{y}_{bs}$$ (4-26)

$$= 30.5 \text{ in.} - 11.9 \text{ in.}$$

$$= 18.6 \text{ in.}$$

$$d_{effec} = d_g - (\overline{y}_{tee-top} + \overline{y}_{tee-bot})$$ (from Eq. 4-27)

$$= 30.5 \text{ in.} - (3.73 \text{ in.} + 1.05 \text{ in.})$$

$$= 25.7 \text{ in.}$$

$$I_{x-net} = I_{x-tee-top} + A_{tee-top}(d_g - \overline{y}_{bs} - \overline{y}_{crit-top})^2 + I_{x-tee-bot} + A_{tee-bot}(\overline{y}_{bs} - \overline{y}_{tee-bot})^2$$ (from Eq. 4-28)

$$= 8.03 \text{ in.}^4 + (4.44 \text{ in.}^2)(30.5 \text{ in.} - 11.9 \text{ in.} - 3.73 \text{ in.})^2 + 10.5 \text{ in.}^4 + (6.01 \text{ in.}^2)(11.9 \text{ in.} - 1.05 \text{ in.})^2$$

$$= 1,710 \text{ in.}^4$$

$$S_{x-net-top} = \frac{I_{x-net}}{\overline{y}_t}$$ (4-29)

$$= \frac{1,710 \text{ in.}^4}{18.6 \text{ in.}}$$

$$= 91.9 \text{ in.}^3$$


*82 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*



<!-- Page 90 -->

<!-- Page 90 -->

$$S_{x-net-bot} = \frac{I_{x-net}}{\overline{y}_{bs}}$$ (4-30)

$$= \frac{1,710 \text{ in.}^4}{11.9 \text{ in.}}$$

$$= 144 \text{ in.}^3$$

*Beam critical net section properties at center of opening*

$$A_{net-crit} = A_{crit-top} + A_{crit-bot}$$ (from Eq. 4-6)

$$= 4.83 \text{ in.}^2 + 6.46 \text{ in.}^2$$

$$= 11.3 \text{ in.}^2$$

$$\overline{y}_{bs} = \frac{A_{crit-top}(d_g - \overline{y}_{crit-top}) + A_{crit-bot}\overline{y}_{crit-bot}}{A_{net}}$$ (from Eq. 4-25)

$$= \frac{(4.83 \text{ in.}^2)(30.5 \text{ in.} - 1.38 \text{ in.}) + (6.46 \text{ in.}^2)(1.36 \text{ in.})}{11.3 \text{ in.}^2}$$

$$= 13.2 \text{ in.}$$

$$\overline{y}_t = d_g - \overline{y}_{bs}$$ (4-26)

$$= 30.5 \text{ in.} - 13.2 \text{ in.}$$

$$= 17.3 \text{ in.}$$

$$d_{effec} = d_g - (\overline{y}_{crit-top} + \overline{y}_{crit-bot})$$ (from Eq. 4-27)

$$= 30.5 \text{ in.} - (1.38 \text{ in.} + 1.36 \text{ in.})$$

$$= 27.8 \text{ in.}$$

$$I_{x-net-crit} = I_{x-crit-top} + A_{crit-top}(d_g - \overline{y}_{bs} - \overline{y}_{crit-top})^2 + I_{x-crit-bot} + A_{crit-bot}(\overline{y}_{bs} - \overline{y}_{crit-bot})^2$$ (4-46)

$$= 14.6 \text{ in.}^4 + (4.82 \text{ in.}^2)(30.5 \text{ in.} - 13.2 \text{ in.} - 1.38 \text{ in.})^2 + 18.9 \text{ in.}^4 + (6.46 \text{ in.}^2)(13.2 \text{ in.} - 1.36 \text{ in.})^2$$

$$= 2,160 \text{ in.}^4$$

$$S_{x-crit-top} = \frac{I_{x-net-crit}}{\overline{y}_t}$$ (from Eq. 4-29)

$$= \frac{2,160 \text{ in.}^4}{17.3 \text{ in.}}$$

$$= 125 \text{ in.}^3$$

$$S_{x-crit-bot} = \frac{I_{x-net-crit}}{\overline{y}_{bs}}$$ (from Eq. 4-30)

$$= \frac{2,160 \text{ in.}^4}{13.2 \text{ in.}}$$

$$= 163 \text{ in.}^3$$

*Composite section properties at critical section in accordance with* The Structural Engineer's Handbook

$$n = \frac{E_c}{E_s}$$ (4-31)

$$= \frac{29,000,000 \text{ psi}}{33(145 \text{ pcf})^{1.5}\sqrt{3,000 \text{ ksi}}}$$

$$= 9.19$$


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 83*



<!-- Page 91 -->

<!-- Page 91 -->

$$b_{effec} = \min \left\{ Span/4, Spacing \right\}$$ (3-4)

$$= \min \left\{ \frac{50 \text{ ft}}{4}, \frac{8 \text{ ft} + 8 \text{ ft}}{2} \right\} (12 \text{ in./ft})$$

$$= 96.0 \text{ in.}$$

$$A_c = b_{effec} t_c$$ (4-32)

$$= (96.0 \text{ in.})(3.00 \text{ in.})$$

$$= 288 \text{ in.}^2$$

$$A_{ctr} = \frac{A_c}{n}$$ (4-33)

$$= \frac{288 \text{ in.}^2}{9.19}$$

$$= 31.3 \text{ in.}^2$$

$$K_c = \frac{A_{ctr}}{A_{ctr} + A_{net-crit}}$$ (from Eq. 4-34)

$$= \frac{31.3 \text{ in.}^2}{31.3 \text{ in.}^2 + 11.3 \text{ in.}^2}$$

$$= 0.735$$

$$e_c = h_r + \frac{t_c}{2}$$ (4-35)

$$= 2.00 \text{ in.} + \frac{3.00 \text{ in.}}{2}$$

$$= 3.50 \text{ in.}$$

Assuming that the neutral axis is in the concrete,

$$y_{cc} = \left( \frac{A_{net-crit} t_c}{A_{ctr}} \right) \left[ \sqrt{1 + \frac{2A_{ctr}}{A_{net-crit} t_c} \left( \overline{y}_h + e_c + \frac{t_c}{2} \right)} - 1 \right]$$ (from Eq. 4-36)

$$= \left[ \frac{(11.3 \text{ in.}^2)(3.00 \text{ in.})}{31.3 \text{ in.}^2} \right] \left[ \sqrt{1 + \frac{2(31.3 \text{ in.}^2)}{(11.3 \text{ in.}^2)(3.00 \text{ in.})} \left( 17.3 \text{ in.} + 3.50 \text{ in.} + \frac{3.00 \text{ in.}}{2} \right)} - 1 \right]$$

$$= 5.94 \text{ in.}$$

Because $t_c + h_r = 5.00$ in. $< y_{cc}$, the neutral axis is in the steel.

$$\overline{y}_c = (\overline{y}_h + e_c) K_c$$ (4-37)

$$= (17.3 \text{ in.} + 3.50 \text{ in.})(0.735)$$

$$= 15.3 \text{ in.}$$

$$I_{x-comp-crit} = (\overline{y}_h + e_c) \overline{y}_c A_{net-crit} + I_{x-net-crit} + \frac{A_{ctr} t_c^2}{12}$$ (from Eq. 4-38)

$$= (17.3 \text{ in.} + 3.50 \text{ in.})(15.3 \text{ in.})(11.3 \text{ in.}^2) + 2,160 \text{ in.}^4 + \frac{(31.3 \text{ in.}^2)(3.50 \text{ in.})^2}{12}$$

$$= 5,790 \text{ in.}^4$$

$$S_{x-comp-conc} = \frac{I_{x-comp-crit}}{\overline{y}_h - \overline{y}_c + e_c + 0.5t_c}$$ (from Eq. 4-39)

$$= \frac{5,790 \text{ in.}^4}{17.3 \text{ in.} - 15.3 \text{ in.} + 3.50 \text{ in.} + 0.5(3.00 \text{ in.})}$$

$$= 827 \text{ in.}^3$$


*84 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*




<!-- Page 92 -->

<!-- Page 92 -->

$$S_{x-comp-steel} = \frac{I_{x-comp-crit}}{\overline{y}_{ht} + \overline{y}_c}$$ (from Eq. 4-40)

$$= \frac{5,790 \text{ in.}^4}{13.2 \text{ in.} + 15.3 \text{ in.}}$$

$$= 203 \text{ in.}^3$$

For the first iteration,

$$d_{effec-comp} = d_o - \overline{y}_{crit-bot} + h_r + 0.5t_c$$ (Eq. 3-8)

$$= 30.5 \text{ in.} - 1.36 \text{ in.} + 2.00 \text{ in.} + 0.5(3.00 \text{ in.})$$

$$= 32.6 \text{ in.}$$

*Composite section properties at net section per the* Structural Engineer's Handbook

$$y_{cc} = \left( \frac{A_{net} t_c}{A_{ctr}} \right) \left[ \sqrt{1 + \frac{2A_{ctr}}{A_{net} t_c} \left( \overline{y}_h + e_c + \frac{t_c}{2} \right)} - 1 \right]$$ (from Eq. 4-36)

$$= \left[ \frac{(10.5 \text{ in.}^2)(3.00 \text{ in.})}{31.3 \text{ in.}^2} \right] \left[ \sqrt{1 + \frac{2(31.3 \text{ in.}^2)}{(10.5 \text{ in.}^2)(3.00 \text{ in.})} \left( 17.4 \text{ in.} + 3.50 \text{ in.} + \frac{3.00 \text{ in.}}{2} \right)} - 1 \right]$$

$$= 5.76 \text{ in.}$$

$$t_c + h_r = 3.00 \text{ in.} + 2.00 \text{ in.}$$

$$= 5.00 \text{ in.} < 5.76 \text{ in.}$$

$$\overline{y}_c = (\overline{y}_h + e_c) K_c$$ (4-37)

$$= (17.4 \text{ in.} + 3.50 \text{ in.})(0.735)$$

$$= 15.3 \text{ in.}$$

$$I_{x-comp} = (\overline{y}_h + e_c) \overline{y}_c A_{net} + I_{x-net} + \frac{A_{ctr} t_c^2}{12}$$ (4-38)

$$= (17.4 \text{ in.} + 3.50 \text{ in.})(15.3 \text{ in.})(10.5 \text{ in.}^2) + 1,710 \text{ in.}^4 + \frac{(31.3 \text{ in.}^2)(3.50 \text{ in.})^2}{12}$$

$$= 5,100 \text{ in.}^4$$

*Check Vierendeel bending*

The governing load cases are:

| LRFD | ASD |
|------|-----|
| Load case 1: | $w = D + L$ |
| $w = 1.4D$ | $= 651$ lb/ft $+ 800$ lb/ft |
| $= 1.4(651$ lb/ft$)$ | $= 1,450$ lb/ft **governs** |
| $= 911$ lb/ft | |
| Load case 2: | |
| $w = 1.2D + 1.6L$ | |
| $= 1.2(651$ lb/ft$) + 1.6(800$ lb/ft$)$ | |
| $= 2,060$ lb/ft **governs** | |


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 85*




<!-- Page 93 -->

<!-- Page 93 -->

**Table 4-28. Global Shear and Moment at Each Opening**

| | | | **Global Shear** | | | **Global Moment** | | |
|----------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| | | | | $V_{kreneis}$ | | | | $M_n$ |
| **Opening<br>No.** | $X_n$<br>ft | $D_s$<br>kips | $L_s$<br>kips | **ASD** | **LRFD** | $D_s$<br>kips | $L_s$<br>kips | **ASD** | **LRFD** |
| End | 0.000 | 16.3 | 20.0 | 31.3 | 44.1 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1 | 1.53 | 15.3 | 18.8 | 29.1 | 41.0 | 24.1 | 29.7 | 53.8 | 76.5 |
| 2 | 3.93 | 13.7 | 16.9 | 25.6 | 36.0 | 58.8 | 72.4 | 131 | 186 |
| 3 | 6.32 | 12.1 | 14.9 | 22.2 | 31.1 | 89.8 | 110 | 200 | 285 |
| 4 | 8.72 | 10.6 | 13.0 | 18.7 | 26.2 | 117 | 144 | 261 | 371 |
| 5 | 11.1 | 9.03 | 11.1 | 15.2 | 21.2 | 141 | 173 | 313 | 445 |
| 6 | 13.5 | 7.47 | 9.19 | 11.7 | 16.3 | 160 | 197 | 358 | 508 |
| 7 | 15.9 | 5.92 | 7.28 | 8.26 | 11.3 | 176 | 217 | 393 | 559 |
| 8 | 18.3 | 4.36 | 5.36 | 4.79 | 6.41 | 189 | 232 | 421 | 598 |
| 9 | 20.7 | 2.80 | 3.44 | 1.31 | 1.47 | 197 | 243 | 440 | 625 |
| 10 | 23.1 | 1.24 | 1.53 | 0.000 | 0.000 | 202 | 249 | 451 | 640 |
| Bm. CL | 25.0 | 0.000 | 0.000 | 0.000 | 0.000 | 203 | 250 | 453 | 644 |

Note: The shear force shown is the net shear force; i.e., the shear strength of the concrete has been subtracted from the global shear force on the beam.

Calculate the available shear strength of the concrete deck:

| LRFD | ASD |
|------|-----|
| $V_c = \phi_{cv} V_{nc}$ | (3-15a) $V_c = \frac{V_{nc}}{\Omega_{cv}}$ | (3-15b) |
| $V_{nc} = 4\sqrt{f_c'}(3)(h_r + t_c)t_c$ | (3-14) $V_{nc} = 4\sqrt{f_c'}(3)(h_r + t_c)t_c$ | (3-14) |
| $= \frac{4\sqrt{3,000 \text{ psi}}(3)(2.00 \text{ in.} + 3.00 \text{ in.})(3.00 \text{ in.})}{1,000 \text{ lb/kip}}$ | | $= \frac{4\sqrt{3,000 \text{ psi}}(3)(2.00 \text{ in.} + 3.00 \text{ in.})(3.00 \text{ in.})}{1,000 \text{ lb/kip}}$ |
| $= 9.85$ kips | | $= 9.85$ kips |
| $V_c = 0.75(9.85 \text{ kips})$ | | $V_c = \frac{9.85 \text{ kips}}{2.00}$ |
| $= 7.39$ kips | | $= 4.93$ kips |

Calculate the global shear and moment at each opening to be used to calculate local internal forces (axial and flexural) at each opening. These results are presented in Table 4-28.

Calculate the local axial force in the top and bottom tees resulting from the global moment. These values are presented in Table 4-29.

As in castellated composite beams, assume that the concrete flange takes all the compression and that the bottom tee takes all the tension force. Once again, this is a valid assumption assuming that sufficient studs exist at a given opening to have developed the concrete flange. It is necessary to check the validity of this assumption.

Local axial force:

For the first iteration, recalculate $d_{effec-comp}$ each time

$$T_{1(i)} = \frac{M_{r(i)}}{d_{effec-comp}}$$ (3-9)


*86 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*




<!-- Page 94 -->

<!-- Page 94 -->

**Table 4-29. Local Axial Force at Each Opening**

| | | | | **ASD** | | | | | **LRFD** | | |
|----------|-------|-------|--------|----------|----------|----------|----------|----------|----------|----------|----------|
| **Opening<br>Number** | $X_n$<br>ft | $M_n$<br>kip-ft | $T_{1(i)}$,<br>kips | $X_{ci(s+1)}$<br>in. | $T_{1(s+1)}$<br>kips | $\frac{T_{1(i)}}{T_{1(s+1)}}$ | $X_{ci(s+2)}$<br>in. | $T_{1(s+2)}$<br>kips | $\frac{T_{1(i)}}{T_{1(s+2)}}$ |
| End | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1 | 1.53 | 53.8 | 19.8 | 0.081 | 18.9 | 1.05 | 0.077 | 18.9 | 1.00 |
| 2 | 3.93 | 131 | 48.4 | 0.198 | 46.3 | 1.05 | 0.189 | 46.3 | 1.00 |
| 3 | 6.32 | 200 | 73.7 | 0.301 | 70.6 | 1.04 | 0.289 | 70.6 | 1.00 |
| 4 | 8.72 | 261 | 96.1 | 0.393 | 92.3 | 1.04 | 0.377 | 92.2 | 1.00 |
| 5 | 11.1 | 313 | 115 | 0.471 | 111 | 1.04 | 0.453 | 111 | 1.00 |
| 6 | 13.5 | 358 | 132 | 0.538 | 127 | 1.04 | 0.517 | 127 | 1.00 |
| 7 | 15.9 | 393 | 145 | 0.591 | 139 | 1.04 | 0.570 | 139 | 1.00 |
| 8 | 18.3 | 421 | 155 | 0.633 | 149 | 1.04 | 0.610 | 149 | 1.00 |
| 9 | 20.7 | 440 | 162 | 0.662 | 156 | 1.04 | 0.638 | 156 | 1.00 |
| 10 | 23.1 | 451 | 166 | 0.678 | 160 | 1.04 | 0.654 | 160 | 1.00 |
| Bm. CL | 25.0 | 453 | 167 | 0.682 | 161 | 1.04 | 0.658 | 161 | 1.00 |

| | | | | **LRFD** | | | | | | |
|----------|-------|-------|--------|----------|----------|----------|----------|----------|----------|----------|
| **Opening<br>Number** | $X_n$<br>ft | $M_n$<br>kip-ft | $T_{1(i)}$,<br>kips | $X_{ci(s+1)}$<br>in. | $T_{1(s+1)}$<br>kips | $\frac{T_{1(i)}}{T_{1(s+1)}}$ | $X_{ci(s+2)}$<br>in. | $T_{1(s+2)}$<br>kips | $\frac{T_{1(i)}}{T_{1(s+2)}}$ |
| End | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1 | 1.53 | 76.5 | 28.1 | 0.115 | 26.9 | 1.05 | 0.110 | 26.9 | 1.00 |
| 2 | 3.93 | 186 | 68.7 | 0.281 | 65.7 | 1.05 | 0.269 | 65.7 | 1.00 |
| 3 | 6.32 | 285 | 105 | 0.428 | 100 | 1.05 | 0.410 | 100 | 1.00 |
| 4 | 8.72 | 371 | 137 | 0.558 | 131 | 1.05 | 0.536 | 131 | 1.00 |
| 5 | 11.1 | 445 | 164 | 0.669 | 158 | 1.04 | 0.645 | 158 | 1.00 |
| 6 | 13.5 | 508 | 187 | 0.764 | 180 | 1.04 | 0.737 | 180 | 1.00 |
| 7 | 15.9 | 559 | 206 | 0.840 | 199 | 1.04 | 0.812 | 199 | 1.00 |
| 8 | 18.3 | 598 | 220 | 0.899 | 213 | 1.03 | 0.870 | 213 | 1.00 |
| 9 | 20.7 | 625 | 230 | 0.940 | 223 | 1.03 | 0.910 | 223 | 1.00 |
| 10 | 23.1 | 640 | 236 | 0.963 | 228 | 1.03 | 0.933 | 228 | 1.00 |
| Bm. CL | 25.0 | 644 | 237 | 0.969 | 230 | 1.03 | 0.939 | 230 | 1.00 |

Recalculate the effective concrete depth

$$X_c = \frac{T_{1(i)}}{0.85 f_c' b_{effec}}$$ (3-10)

Recalculate $d_{effec-comp}$

$$d_{effec-comp} = d_o - \overline{y}_{bot-bot-crit} + t_c + h_r - \frac{X_c}{2}$$ (from Eq. 3-8)

Recalculate until the difference $≤ 1\%$

$$T_{1(s+1)} = \frac{M_{r(s+1)}}{d_{effec-comp}}$$ (3-9)


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 87*




<!-- Page 95 -->

<!-- Page 95 -->

**Table 4-30. Revised Local Axial Force at Each Opening (LRFD)**

| **Opening<br>Number** | $X_n$<br>ft | $T_1 = T_{1(s+2)}$,<br>kips | $(q)(X_i)$,<br>kips | **Composite<br>Status** | $T_{ov}$<br>kips | $T_{1-new}$,<br>kips |
|----------|-------|----------|----------|----------|----------|----------|
| End | 0.000 | 0.000 | 0.000 | N/A | N/A | N/A |
| 1 | 1.53 | 26.9 | 34.1 | Full | 0.000 | 26.9 |
| 2 | 3.93 | 65.8 | 87.4 | Full | 0.000 | 65.8 |
| 3 | 6.32 | 101 | 141 | Full | 0.000 | 101 |
| 4 | 8.72 | 131 | 194 | Full | 0.000 | 131 |
| 5 | 11.1 | 158 | 247 | Full | 0.000 | 158 |
| 6 | 13.5 | 181 | 301 | Full | 0.000 | 181 |
| 7 | 15.9 | 199 | 354 | Full | 0.000 | 199 |
| 8 | 18.3 | 213 | 407 | Full | 0.000 | 213 |
| 9 | 20.7 | 223 | 461 | Full | 0.000 | 223 |
| 10 | 23.1 | 228 | 514 | Full | 0.000 | 228 |
| CL | 25.0 | 230 | 556 | Full | 0.000 | 230 |

The same number of studs as those used in Example 4.3 has been selected; therefore, the same number of studs and stud density is applicable. The number of studs for full composite action is 54 across the length of the beam and the shear stud density = 22.3 kip/ft. Also, as in Example 4.3, the next step is to calculate the amount of concrete that has been developed by the studs between the end of the beam and the opening under consideration and determine whether or not that section of the beam is fully or partially composite. If it is determined to be not fully composite, calculate the added force so that the net steel section is required to resist, $T_{ov}$ and $T_{1-new}$ (refer to Example 4.3 for further explanation). Table 4-30 shows the axial force at each opening.

The compression force to be resisted by the top tee at its centroid is:

$$T_t = M_t \left[ \frac{1 - \left( \frac{(q)(X_i)}{T_{1(s+2)}} \right)}{d_{effec}} \right]$$ (3-12)

The revised tensile force to be resisted by the bottom tee at its centroid is then:

$$T_{1-new} = qX_i + T_o$$ (3-13)

Calculate the local moment on the top and bottom tees resulting from the net shear force passing through the web opening. These results are presented in Table 4-31.

Top tee local Vierendeel moment:

$$M_{vt-top} = V_{net} \left( \frac{A_{crit-top}}{A_{net-crit}} \right) \frac{D_o}{4}$$ (from Eq. 3-2)

Bottom tee local Vierendeel moment:

$$M_{vt-bot} = V_{net} \left( \frac{A_{crit-bot}}{A_{net-crit}} \right) \frac{D_o}{4}$$ (from Eq. 3-3)


*88 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*




<!-- Page 96 -->

<!-- Page 96 -->

**Table 4-31. Local Vierendeel Moment at Each Opening**

| | | **ASD** | | | **LRFD** | | |
|----------|-------|-------|----------|----------|-------|----------|----------|
| **Opening<br>Number** | $X_n$<br>ft | $V_{vt}$<br>kips | $M_{vt-top}$,<br>kip-in. | $M_{vt-bot}$,<br>kip-in. | $V_{vt}$<br>kips | $M_{vt-top}$,<br>kip-in. | $M_{vt-bot}$,<br>kip-in. |
| End | 0.000 | 31.3 | 69.4 | 93.0 | 44.1 | 97.8 | 131 |
| 1 | 1.53 | 29.1 | 65.7 | 87.0 | 41.0 | 92.4 | 122 |
| 2 | 3.93 | 25.6 | 57.9 | 76.6 | 36.0 | 81.3 | 108 |
| 3 | 6.32 | 22.2 | 50.0 | 66.2 | 31.1 | 70.2 | 92.9 |
| 4 | 8.72 | 18.7 | 42.2 | 55.8 | 26.2 | 59.0 | 78.2 |
| 5 | 11.1 | 15.2 | 34.3 | 45.5 | 21.2 | 47.9 | 63.4 |
| 6 | 13.5 | 11.7 | 26.5 | 35.1 | 16.3 | 36.7 | 48.6 |
| 7 | 15.9 | 8.26 | 18.6 | 24.7 | 11.3 | 25.6 | 33.9 |
| 8 | 18.3 | 4.79 | 10.8 | 14.3 | 6.41 | 14.5 | 19.1 |
| 9 | 20.7 | 1.31 | 2.97 | 3.93 | 1.47 | 3.32 | 4.40 |
| 10 | 23.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| CL | 25.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

*Calculate the available shear and flexural strength of top and bottom tees at the critical section*

Determine the limiting flange width-to-thickness ratio from AISC *Specification* Table B4.1b, Case 10:

$$\lambda_p = 0.38 \sqrt{\frac{E}{F_y}}$$

$$= 0.38 \sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 9.15$$

The width-to-thickness ratio for the top flange is:

$$\lambda = \frac{b}{t}$$

$$= \frac{b_f}{2t_f}$$

$$= \frac{6.50 \text{ in.}}{2(0.450 \text{ in.})}$$

$$= 7.22 < 9.15$$

The width-to-thickness ratio for the bottom flange is:

$$\lambda = \frac{b}{t}$$

$$= \frac{b_f}{2t_f}$$

$$= \frac{6.56 \text{ in.}}{2(0.650 \text{ in.})}$$

$$= 5.05 < 9.15$$

Because $\lambda < \lambda_p$, the flanges of both the top and bottom tees are compact; therefore, it is not necessary to check flange local buckling when calculating the available flexural strength.


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 89*




<!-- Page 97 -->

<!-- Page 97 -->

Determine the limiting stem width-to-thickness ratio, $\lambda_r$, from AISC *Specification* Table B4.1a, Case 4:

$$\lambda_r = 0.75 \sqrt{\frac{E}{F_y}}$$

$$= 0.75 \sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 18.1$$

The width-to-thickness ratio for the top stem is:

$$\lambda = \frac{d_{hop-crit}}{t_w}$$

$$= \frac{5.87 \text{ in.}}{0.35 \text{ in.}}$$

$$= 16.8 < 18.1$$

The width-to-thickness ratio for the bottom stem is:

$$\lambda = \frac{d_{bot-crit}}{t_w}$$

$$= \frac{6.07 \text{ in.}}{0.405 \text{ in.}}$$

$$= 15.0 < 18.1$$

Because $\lambda < \lambda_r$, both top and bottom tee stems are nonslender; therefore, it is not necessary to consider AISC *Specification* Section E7 when calculating the available compressive strength.

It is not necessary to calculate the available compressive strength of top or bottom tee in this example because all openings are fully composite, and therefore, all compression is taken by the concrete flange. If compression did exist in top or bottom tee, the available compressive strength would be calculated as shown in Example 4.2.

*Calculate available tensile strength of bottom tee*

$$P_n = F_y A_{crit-bot}$$ (from *Spec.* Eq. D2-1)

$$= (50 \text{ ksi})(6.46 \text{ in.}^2)$$

$$= 323 \text{ kips}$$

*Calculate available flexural strength of tee*

*Yielding*

For tee stems in compression:

$$M_{p-top} = M_y$$ (from *Spec.* Eq. F9-4)

$$M_y \quad = F_y S_{x-bot}$$ (from *Spec.* Eq. F9-3)

$$= (50 \text{ ksi})(3.25 \text{ in.}^3)$$

$$= 163 \text{ kip-in.}$$

$$M_{p-bot} = M_y$$ (from *Spec.* Eq. F9-4)

$$M_y \quad = F_y S_{x-top}$$ (from *Spec.* Eq. F9-3)

$$= (50 \text{ ksi})(4.01 \text{ in.}^3)$$

$$= 201 \text{ kip-in.}$$

In both cases the stem is assumed to be in compression, this will be conservative for the bottom tee. It is possible to take advantage of this to calculate a higher value for the available flexural strength of the bottom tee because the stem is in tension.


*90 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*




<!-- Page 98 -->

<!-- Page 98 -->

*Lateral-Torsional Buckling*

For lateral-torsional buckling of the top tee:

$$B_{top} = -2.3 \left( \frac{d}{L_b} \right) \sqrt{\frac{I_y}{J}}$$ (*Spec.* Eq. F9-12)

$$= -2.3 \left( \frac{5.86 \text{ in.}}{10.4 \text{ in.}} \right) \sqrt{\frac{10.3 \text{ in.}^4}{0.255 \text{ in.}^4}}$$

$$= -8.24$$

$$M_{cr-top} = \frac{1.95E}{L_b} \sqrt{I_y J} \left( B + \sqrt{1 + B^2} \right)$$ (*Spec.* Eq. F9-10)

$$= \frac{1.95(29,000 \text{ ksi})}{10.4 \text{ in.}} \sqrt{(10.3 \text{ in.}^4)(0.255 \text{ in.}^4)} \left[ -8.24 + \sqrt{1 + (-8.24)^2} \right]$$

$$= 534 \text{ kip-in.}$$

For lateral-torsional buckling of the bottom tee:

$$B_{bot} = -2.3 \left( \frac{d}{L_b} \right) \sqrt{\frac{I_y}{J}}$$ (*Spec.* Eq. F9-12)

$$= -2.3 \left( \frac{6.06 \text{ in.}}{10.4 \text{ in.}} \right) \sqrt{\frac{15.3 \text{ in.}^4}{0.673 \text{ in.}^4}}$$

$$= -6.39$$

$$M_{cr-bot} = \frac{1.95E}{L_b} \sqrt{I_y J} \left( B + \sqrt{1 + B^2} \right)$$ (*Spec.* Eq. F9-10)

$$= \frac{1.95(29,000 \text{ ksi})}{10.4 \text{ in.}} \sqrt{(15.3 \text{ in.}^4)(0.673 \text{ in.}^4)} \left[ -6.39 + \sqrt{1 + (-6.39)^2} \right]$$

$$= 1,350 \text{ kip-in.}$$

*Flange local buckling*

According to AISC *Specification* Section F9.3(a), the limit state of flange local buckling does not apply because the flanges are compact.

*Local buckling of tee stems*

The nominal flexural strength for local buckling of the tee stem in flexural compression, $M_n$, is determined using AISC *Specification* Section F9.4:

$$M_n = F_{cr} S_x$$ (*Spec.* Eq. F9-16)

Because $d/t_w < 0.84 \sqrt{\frac{E}{F_y}}$, the critical stress, $F_{cr}$, is determined using AISC *Specification* Equation F9-17:

$$F_{cr} = F_y$$ (*Spec.* Eq. F9-17)

And thus:

For the top tee:

$$M_{n-top} = F_y S_{x-bot}$$

$$= (50 \text{ ksi})(3.25 \text{ in.}^3)$$

$$= 163 \text{ kip-in.}$$


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 91*




<!-- Page 99 -->

<!-- Page 99 -->

For the bottom tee:

$$M_{n-bot} = F_y S_{x-top}$$

$$= (50 \text{ ksi})(4.01 \text{ in.}^3)$$

$$= 201 \text{ kip-in.}$$

The available tensile and flexural strengths of the tee are:

| LRFD | ASD |
|------|-----|
| *Available tensile strength—bottom tee* | *Available tensile strength—bottom tee* |
| $P_c = \phi_t P_n$ | $P_c = \frac{P_n}{\Omega_t}$ |
| $= 0.90(323 \text{ kips})$ | $= \frac{323 \text{ kips}}{1.67}$ |
| $= 291 \text{ kips}$ | $= 193 \text{ kips}$ |
| | |
| *Available flexural strength—top tee* | *Available flexural strength—top tee* |
| $M_c = \phi_b M_n$ | $M_c = \frac{M_n}{\Omega_b}$ |
| $= 0.90(163 \text{ kip-in.})$ | $= \frac{163 \text{ kip-in.}}{1.67}$ |
| $= 147 \text{ kip-in.}$ | $= 97.6 \text{ kip-in.}$ |
| | |
| *Available flexural strength—bottom tee* | *Available flexural strength—bottom tee* |
| $M_c = \phi_b M_n$ | $M_c = \frac{M_n}{\Omega_b}$ |
| $= 0.90(201 \text{ kip-in.})$ | $= \frac{201 \text{ kip-in.}}{1.67}$ |
| $= 181 \text{ kip-in.}$ | $= 120 \text{ kip-in.}$ |

*Check tees for combined axial and flexural loads*

The interaction values for each opening are presented in Table 4-32.

From Table 4-32, the composite Vierendeel bending is summarized as follows:

| LRFD | ASD |
|------|-----|
| *Top tee* | *Top tee* |
| $I_{max} = 0.631 < 1.0$ **o.k.** | $I_{max} = 0.674 < 1.0$ **o.k.** |
| *Bottom tee* | *Bottom tee* |
| $I_{max} = 0.861 < 1.0$ **o.k.** | $I_{max} = 0.911 < 1.0$ **o.k.** |

*Check web post buckling*

*Calculate horizontal shear and resultant moment at each gross section for web post buckling*

Table 4-33 presents the horizontal shear force at each opening.


*92 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*




<!-- Page 100 -->

<!-- Page 100 -->

**Table 4-32. Interaction Values at Each Opening for LRFD and ASD**

| | | | **LRFD** | | | | | | | |
|----------|-------|-------|----------|----------|-------|----------|----------|----------|----------|----------|
| | | | **Top Tee** | | | | **Bottom Tee** | | | |
| **Opening<br>Number** | $X_n$<br>ft | $P_T$,<br>kips | $M_{vt-top}$,<br>kip-in. | $\frac{M_{vt}}{M_c}$ | $P_T$,<br>kips | $M_{vt-bot}$,<br>kip-in. | $\frac{P_r}{P_c}$ | *Spec.*<br>Eq.<br>**H1-1a** | *Spec.*<br>Eq.<br>**H1-1b** | **Interaction*** |
| End | 0.000 | N/A | N/A | NA | N/A | N/A | N/A | N/A | N/A | N/A |
| 1 | 1.53 | 0.000 | 92.4 | 0.631 | 26.9 | 122 | 0.093 | 0.696 | 0.726 | 0.726 |
| 2 | 3.93 | 0.000 | 81.3 | 0.555 | 65.8 | 108 | 0.226 | 0.757 | 0.711 | 0.757 |
| 3 | 6.32 | 0.000 | 70.2 | 0.479 | 101 | 92.9 | 0.346 | 0.805 | 0.689 | 0.805 |
| 4 | 8.72 | 0.000 | 59.0 | 0.403 | 131 | 78.2 | 0.452 | 0.838 | 0.660 | 0.838 |
| 5 | 11.1 | 0.000 | 47.9 | 0.327 | 158 | 63.4 | 0.544 | 0.857 | 0.624 | 0.857 |
| 6 | 13.5 | 0.000 | 36.7 | 0.251 | 181 | 48.6 | 0.621 | 0.861 | 0.581 | 0.861 |
| 7 | 15.9 | 0.000 | 25.6 | 0.175 | 199 | 33.9 | 0.684 | 0.851 | 0.530 | 0.851 |
| 8 | 18.3 | 0.000 | 14.5 | 0.099 | 213 | 19.1 | 0.733 | 0.827 | 0.473 | 0.827 |
| 9 | 20.7 | 0.000 | 3.32 | 0.023 | 223 | 4.40 | 0.766 | 0.788 | 0.408 | 0.788 |
| 10 | 23.1 | 0.000 | 0.000 | 0.000 | 228 | 0.000 | 0.785 | 0.785 | 0.393 | 0.785 |
| Bm. CL | 25.0 | 0.000 | 0.000 | 0.000 | 230 | 0.000 | 0.790 | 0.790 | 0.395 | 0.790 |
| | | | | $I_{max}$: | **0.631** | | | | $I_{max}$: | **0.861** |

| | | | **ASD** | | | | | | | |
|----------|-------|-------|----------|----------|-------|----------|----------|----------|----------|----------|
| | | | **Top Tee** | | | | **Bottom Tee** | | | |
| **Opening<br>Number** | $X_n$<br>ft | $P_T$,<br>kips | $M_{vt-top}$,<br>kip-in. | $\frac{M_{vt}}{M_c}$ | $P_T$,<br>kips | $M_{vt-bot}$,<br>kip-in. | $\frac{P_r}{P_c}$ | *Spec.*<br>Eq.<br>**H1-1a** | *Spec.*<br>Eq.<br>**H1-1b** | **Interaction*** |
| End | 0.00 | N/A | N/A | NA | N/A | N/A | N/A | N/A | N/A | N/A |
| 1 | 1.53 | 0.000 | 65.7 | 0.674 | 19.0 | 87.0 | 0.098 | 0.743 | 0.775 | 0.775 |
| 2 | 3.93 | 0.000 | 57.9 | 0.594 | 46.3 | 76.6 | 0.239 | 0.807 | 0.759 | 0.807 |
| 3 | 6.32 | 0.000 | 50.0 | 0.513 | 70.8 | 66.2 | 0.366 | 0.857 | 0.735 | 0.857 |
| 4 | 8.72 | 0.000 | 42.2 | 0.433 | 92.3 | 55.8 | 0.477 | 0.891 | 0.704 | 0.891 |
| 5 | 11.1 | 0.000 | 34.3 | 0.352 | 111 | 45.5 | 0.574 | 0.911 | 0.666 | 0.911 |
| 6 | 13.5 | 0.000 | 26.5 | 0.272 | 127 | 35.1 | 0.655 | 0.915 | 0.620 | 0.915 |
| 7 | 15.9 | 0.000 | 18.6 | 0.191 | 140 | 24.7 | 0.721 | 0.904 | 0.567 | 0.904 |
| 8 | 18.3 | 0.000 | 10.8 | 0.111 | 149 | 14.3 | 0.772 | 0.878 | 0.505 | 0.878 |
| 9 | 20.7 | 0.000 | 2.97 | 0.03 | 156 | 3.93 | 0.807 | 0.837 | 0.436 | 0.837 |
| 10 | 23.1 | 0.000 | 0.000 | 0.000 | 160 | 0.000 | 0.827 | 0.780 | 0.360 | 0.780 |
| Bm. CL | 25.0 | 0.000 | 0.000 | 0.000 | 161 | 0.000 | 0.832 | 0.723 | 0.293 | 0.723 |
| | | | | $I_{max}$: | **0.674** | | | | $I_{max}$: | **0.915** |

* Reflects bold face value of controlling interaction equation.


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 93*




<!-- Page 101 -->

<!-- Page 101 -->

# SYMBOLS

| Symbol | Description |
|--------|-------------|
| $A$ | Cross-sectional area, in.$^2$ (mm$^2$) |
| $A_c$ | Area of concrete in compression, in.$^2$ (mm$^2$) |
| $A_{net}$ | Combined area of top and bottom tees, in.$^2$ (mm$^2$) |
| $A_{tee}$ | Area of tee section, in.$^2$ (mm$^2$) |
| $B$ | Factor for lateral-torsional buckling in tee |
| $C_v$ | Web shear coefficient |
| $C_1$ | Axial force in concrete of a composite section, kips (N) |
| $D_o$ | Opening diameter, in. (mm) |
| $E$ | Modulus of elasticity of steel = 29,000 ksi (200 000 MPa) |
| $ENA$ | Elastic neutral axis |
| $G$ | Shear modulus of elasticity of steel = 11,200 ksi (77 200 MPa) |
| $F_{cr}$ | Critical stress, ksi (MPa) |
| $F_{cry}$ | Critical stress about the minor axis, ksi (MPa) |
| $F_{crz}$ | Critical torsional buckling stress, ksi (MPa) |
| $F_e$ | Elastic critical buckling stress, ksi (MPa) |
| $H$ | Flexural constant |
| $I_x$ | Moment of inertia about $x$-axis, in.$^4$ (mm$^4$) |
| $I_y$ | Moment of inertia about $y$-axis, in.$^4$ (mm$^4$) |
| $J$ | Torsional constant, in.$^4$ (mm$^4$) |
| $K_x$ | Effective length factor with respect to $x$-axis |
| $K_y$ | Effective length factor with respect to $y$-axis |
| $L$ | Length of compression member, in. (mm) |
| $L_b$ | Distance between lateral braces, in. (mm) |
| $M_c$ | Allowable flexural strength (ASD), kip-in. (N-mm) |
| $M_e$ | Design flexural strength (LRFD), kip-in. (N-mm) |
| $M_{cr}$ | Nominal flexural strength based on lateral-torsional buckling limit state, kip-in. (N-mm) |
| $M_e$ | Elastic bending moment of web post, kip-in. (N-mm) |
| $M_{nl}$ | Nominal flexural strength based on flange local buckling limit state, kip-in. (N-mm) |
| $M_n$ | Nominal flexural strength, kip-in. (N-mm) |

| Symbol | Description |
|--------|-------------|
| $M_{ncr}$ | Critical moment for lateral buckling, kip-in. (N-mm) |
| $M_p$ | Plastic bending moment, kip-in. (N-mm) |
| $M_r$ | Required flexural strength using load combinations, kip-in. (N-mm) |
| $M_{vf}$ | Required flexural strength in tee, kip-in. (N-mm) |
| $N$ | Number of shear studs between the point of maximum moment and end of beam |
| $N_s$ | Total number of studs across the length of the beam |
| $P_c$ | Allowable axial compressive strength (ASD), kips (N) |
| $P_e$ | Design axial compressive strength (LRFD), kips (N) |
| $P_n$ | Nominal axial compressive strength (LRFD), kips (N) |
| $PNA$ | Plastic neutral axis |
| $P_r$ | Required axial strength of tee using load combinations, kips (N) |
| $Q_n$ | Nominal strength of one stud shear connector, kips (N) |
| $R$ | Radius of cellular opening, in. (mm) |
| $S$ | Spacing of openings, in. (mm) |
| $S_x$ | Elastic section modulus about $x$-axis, in.$^3$ (mm$^3$) |
| $S_{x,tee}$ | Section modulus of tee about $x$-axis, in.$^3$ (mm$^3$) |
| $T_i$ | Axial force at centerline of opening $(i)$, kips (N) |
| $T_{i+1}$ | Axial force at centerline of opening $(i + 1)$, kips (N) |
| $T_{r(i)}$ | Required axial force in tee at opening $(i)$, kips (N) |
| $T_{r(i+1)}$ | Required axial force in tee at opening $(i + 1)$, kips (N) |
| $T_o$ | Axial force in top tee, kips (N) |
| $T_1$ | Axial force in bottom tee, kips (N) |
| $T_{1,new}$ | Axial force in bottom tee for partial composite action, kips (N) |
| $T_{u(i)}$ | Axial force in tee at opening $(i)$ (LRFD), kips (N) |
| $T_{u(i+1)}$ | Axial force in tee at opening $(i + 1)$ (LRFD), kips (N) |


AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 101



<!-- Page 102 -->

<!-- Page 102 -->

| Symbol | Description |
|--------|-------------|
| $V$ | Global shear, kips (N) |
| $V'$ | Total horizontal shear force between point of max positive moment and the point of zero moment, kips (N) |
| $V_{allow}$ | Allowable horizontal shear strength (ASD), kips (N) |
| $V_{a,global}$ | Service shear force (ASD), kips (N) |
| $V_{n,global}$ | Required global shear strength (ASD), kips (N) |
| $V_{n,net}$ | Net service shear force resisted by beam (ASD), kips (N) |
| $V_c$ | Shear strength of concrete deck, kips (N) |
| $V_h$ | Horizontal shear force at neutral axis, kips (N) |
| $V_{ha}$ | Required horizontal shear force at neutral axis (ASD), kips (N) |
| $V_{hu}$ | Required horizontal shear force at neutral axis (LRFD), kips (N) |
| $V_i$ | Global shear force at opening $(i)$, kips (N) |
| $V_{i+1}$ | Global shear force at opening $(i + 1)$, kips (N) |
| $V_n$ | Nominal shear strength, kips (N) |
| $V_{net}$ | Net shear force resisted by beam, kips (N) |
| $V_{n,global}$ | Ultimate shear force (LRFD), kips (N) |
| $V_{n,global}$ | Required global shear strength (LRFD), kips (N) |
| $V_{n,net}$ | Net ultimate shear force (LRFD), kips (N) |
| $V_{u(i)}$ | Required shear strength at opening $(i)$, kips (N) |
| $V_{u(i+1)}$ | Required shear strength at opening $(i + 1)$, kips (N) |
| $X_i$ | Distance from end of beam to center of the opening being analyzed, in. (mm) |
| $Y_c$ | Depth of concrete used to resist global moment, in. (mm) |
| $Z_x$ | Plastic section modulus about $x$-axis, in.$^3$ (mm$^3$) |
| $a$ | Length of end web post, in. (mm) |
| $b$ | Horizontal length = $0.5h_o/\tan\theta$, in. (mm) |
| $b_{effe}$ | Effective width of concrete slab, in. (mm) |
| $b_f$ | Flange width, in. (mm) |
| $d$ | Full nominal depth of tee, in. (mm) |
| $d_{effe}$ | Distance between centroids of top and bottom tees, in. (mm) |
| $d_{effe1-comp}$ | Effective depth of composite section, in. (mm) |
| $d_g$ | Depth of expanded beam, in. (mm) |

| Symbol | Description |
|--------|-------------|
| $d_t$ | Depth of tee, in. (mm) |
| $e$ | Length of tee section, also length of solid web section along centerline, in. (mm) |
| $e'$ | Minimum diagonal distance from the corner of the cope to the first opening, in. (mm) |
| $f_c'$ | Compressive strength of concrete, ksi (MPa) |
| $h$ | Half height of castellated opening, in. (mm) |
| $h_o$ | Height of opening of castellated beam, in. (mm) |
| $h_r$ | Height of deck ribs, in. (mm) |
| $i$ | Reference number for castellated or cellular opening |
| $k_v$ | Web plate buckling coefficient |
| $q$ | Shear stud density, kip/ft (N/mm) |
| $r_{min}$ | Minimum radius of gyration of tee, in. (mm) |
| $r_o$ | Polar radius of gyration about the shear center, in. (mm) |
| $r_x$ | Radius of gyration about $x$-axis, in. (mm) |
| $r_y$ | Radius of gyration about $y$-axis, in. (mm) |
| $t_c$ | Thickness of concrete above deck ribs, in. (mm) |
| $t_f$ | Flange thickness, in. (mm) |
| $y_c$ | Distance from top of concrete to centroid of compression block, in. (mm) |
| $\overline{y}_{tee,bot}$ | Distance from bottom fiber to centroid of bottom tee, in. (mm) |
| $\overline{y}_{tee,top}$ | Distance from top fiber to centroid of top tee, in. (mm) |
| $w_o$ | $e + 2h$, in. (mm) |
| $\Delta_{DL}$ | Dead load deflection |
| $\Delta_{LL}$ | Live load deflection |
| $\Delta_{PDL}$ | Pre-dead load deflection |
| $\Delta_{TL}$ | Total load deflection |
| $\phi_b$ | Resistance factor for flexure |
| $\phi_c$ | Resistance factor for compression |
| $\phi_t$ | Resistance factor for tension |
| $\phi_v$ | Resistance factor for shear |
| $\Omega_b$ | Safety factor for flexure |
| $\Omega_v$ | Safety factor for shear |
| $\theta$ | Angle of hexagonal cut, degrees |


102 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31



<!-- Page 103 -->

<!-- Page 103 -->

# REFERENCES

Aglan, A. and Redwood, R. (1974), "Web Buckling in Cas-
tellated Beams," Proceedings of the Department of Civil
Engineering and Applied Mechanics, McGill University,
Montreal, Canada.

American Institute of Steel Construction (AISC) (2016a),
ANSI/AISC 360-16, American Institute of Steel Con-
struction, Chicago, IL.

American Institute of Steel Construction (AISC) (2016b),
Steel Construction Manual, 15th Edition, American Insti-
tute of Steel Construction, Chicago, IL.

Altifillisch, M.D., Cooke, R.B. and Toprac, A.A. (1957), "An
Investigation of Welded Open-Web Expanded Beams,"
Welding Research—Supplement to The Welding Journal,
AWS, Vol. No. 36, 2, February.

Aminian, P., Niroomandi, A., Gandomi, A.H. and Alavi, A.H.
(2012), "New Design Equations for Assessment of Load
ting of Cellular Beams," University of Azerbijn, Turszik.

Blodgett, O.W. (1966), Design of Welded Structures, James F.
Lincoln Arc Welding Foundation, Cleveland, OH.

Bradley, T.P. (2001), "Stability of Castellated Beams Dur-
ing Erection," Final Report Submitted to Cives Steel Institute,
Civil Engineering Department, Blacksburg, VA.

Chusieog, C.H., Tseng, E.M. and Aguilar, C. (2004),
"Analysis and Design Recommendations for Castellated
Beams," MS Thesis, University of North Texas, Vol. 3, No. 1.
Dar, P.K. and Swinant, S.E. (1994), Handbook on Welding
of Castellated Beams, Capitol Mechanical Engineering
Associates, Inc., Houston, TX.

Nethercot, D.A. (1985), "Elastic Lateral Buckling of Beams,"
Steel Design Guide No. 3, AISC, Chicago, IL.

Hosain, M.U., Cheng, E.M. and Agaplar, C. (2004),
"Analysis and Design of Castellated and Composite Beams,"
Journal of the American Institute of Steel Construction,
Dar, P.K. and Swinant, S.E. (1994), Handbook on the Design
of Castellated Beams, Capitol Mechanical Engineering
Associates, Inc., Houston, TX.

Nethercot, D.A. (1985), "Elastic Lateral Buckling of Beams,"
"Web Encroaching in Castellated Beams," American Institute
of Steel Construction, Chicago, IL.

Yam, L.C.P. and Cheng, J.J.R. (1993), "Behavior and Design
of Gusset Plates in Compression," Journal of Structural
Engineering, ASCE, Vol. 119, No. 5, pp. 1361-1378.

Estrada, H., Jimenez, J.J. and Aguinaga, E. (2006), "Cost
Optimization Analysis for Composite Castellated Beams,"
Proceedings of the Seventeenth Engineering National
Congress Mexican Institute of Civil Engineers, Vol. 1, No.
4, Querétaro, México, pp. 261-265.

Hosain, M.U., Cheng, W.K. and Neis, V.V. (1974), "Dapped
End Bolted Connections for Open Web Steel Joists,"
the Strength of Cellular and Castellated Beams," Engi-
neering Journal, AISC, Vol. 11, No. 2, pp. 50-55.

Hosain, M.U., Cheng, W.K. and Neis, V.V. (1974), "Dapped
End Bolted Connections for Open Web Steel Joists," Engi-
neering Journal, AISC, Vol. 11, No. 3, pp. 97-103.

Kerdal, D. and Nethercot, D.A. (1984), "Failure Modes
for Castellated Beams," Journal of Constructional Steel
Research, Vol. 4, No. 4, pp. 295-315.

Kim, B., Li, L., Edmonds, A. and Kroe, K. (2016), "Lateral-
tional Buckling of Castellated and Cellular Beams," Proceed-
ings of the Institution of Civil Engineers, Vol. 90, No. 3,
pp. 321-336.

Knowles, P.R., D.E. and Giger, E.A. and Davis, D.B.
(2016), "Integration of SixFinned Structural Systems
Due to Human Activities", Design Guide 11, 2nd Ed., AISC,
Chicago, IL.

Redwood, R.G. and Shrivastava, S.C. (1980), "Design
Recommendations for Steel Beams with Web Holes,"
Canadian Journal of Civil Engineering, No. 2, pp. 642-
650.

Reddy, G.L., Marla, J.P., Eisenstein, S.A. and Abdulrahm,
M. (2011), Fire Resistance of Steel-Framed Buildings,
ASCE, New York.

Ward, J.K. (1990), "Design of Composite and Non-Compos-
ite Cellular Beams," SCI, Silwood Park, Ascot, UK.


AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 103



<!-- Page 104 -->

<!-- Page 104 -->

*Check vertical shear*

The concrete shear strength will be disregarded when checking vertical shear for the net and gross sections. The concrete shear strength will be added to the net shear force.

*Check vertical shear at the beam net section:*

| LRFD | ASD |
|------|-----|
| From Table 4-31, | From Table 4-31, |
| $V_{n,net} = 41.0$ kips | $V_{n,net} = 29.1$ kips |
| $V_{n,global} = V_{n,net} + concrete\;shear\;strength$ | $V_{n,global} = V_{n,net} + concrete\;shear\;strength$ |
| $= 41.0$ kips $+ 7.39$ kips | $= 29.1$ kips $+ 4.93$ kips |
| $= 48.4$ kips | $= 34.0$ kips |

The shear force between the top and bottom tees will be divided based on their relative areas.

| LRFD | ASD |
|------|-----|
| $V_{n,top} = V_{n,global}\left(\frac{A_{tee,top}}{A_{net}}\right)$ | $V_{n,top} = V_{n,global}\left(\frac{A_{tee,top}}{A_{net}}\right)$ |
| $= \left(48.4\text{ kips}\right)\left(\frac{4.44\text{ in.}^2}{10.5\text{ in.}^2}\right)$ | $= \left(34.0\text{ kips}\right)\left(\frac{4.44\text{ in.}^2}{10.5\text{ in.}^2}\right)$ |
| $= 20.5$ kips | $= 14.4$ kips |
| $V_{n,bot} = V_{n,global}\left(\frac{A_{tee,bot}}{A_{net}}\right)$ | $V_{n,bot} = V_{n,global}\left(\frac{A_{tee,bot}}{A_{net}}\right)$ |
| $= \left(48.4\text{ kips}\right)\left(\frac{6.01\text{ in.}^2}{10.5\text{ in.}^2}\right)$ | $= \left(34.0\text{ kips}\right)\left(\frac{6.01\text{ in.}^2}{10.5\text{ in.}^2}\right)$ |
| $= 27.7$ kips | $= 19.5$ kips |

From AISC *Specification* Section G3:

Top tee:

$$\frac{h}{t_w} = \frac{d_{t,top-net}}{t_{w,top}}$$

$$= \frac{4.75\text{ in.}}{0.350\text{ in.}}$$

$$= 13.6 < 1.10\sqrt{\frac{1.2(29,000\text{ ksi})}{50\text{ ksi}}} = 29.0$$

Because $h/t_w < 1.10\sqrt{k_v E/F_y}$,

$$C_{v2} = 1.0 \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad (Spec.\text{ Eq. G2-9})$$

$$V_{n,top} = 0.60F_y\left(d_{t,top-net}t_{w,top}\right)C_{v2} \qquad\qquad\qquad\qquad\qquad (from\;Spec.\text{ Eq. G3-1})$$

$$= 0.60(50\text{ ksi})(4.75\text{ in.})(0.350\text{ in.})(1.0)$$

$$= 49.9\text{ kips}$$


96 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31

