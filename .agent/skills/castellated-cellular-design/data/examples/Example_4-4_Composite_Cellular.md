# Example 4.4: Composite Cellular Beam

<!-- Consolidated from pages 105-117 -->


<!-- Page 105 -->

<!-- Page 105 -->

Bottom tee:

$$\frac{h}{t_w} = \frac{d_{t,bot-net}}{t_{w,bot}}$$

$$= \frac{4.95\text{ in.}}{0.405\text{ in.}}$$

$$= 12.2 < 1.10\sqrt{\frac{1.2(29,000\text{ ksi})}{50\text{ ksi}}} = 29.0$$

Because $h/t_w < 1.10\sqrt{k_v E/F_y}$,

$$C_{v2} = 1.0 \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad (Spec.\text{ Eq. G2-9})$$

$$V_{n,bot} = 0.60F_y\left(d_{t,bot-net}t_{w,bot}\right)C_{v2} \qquad\qquad\qquad\qquad\qquad (from\;Spec.\text{ Eq. G3-1})$$

$$= 0.60(50\text{ ksi})(4.95\text{ in.})(0.405\text{ in.})(1.0)$$

$$= 60.1\text{ kips}$$

Available vertical shear strength at top and bottom tees

| LRFD | ASD |
|------|-----|
| $\phi_v V_{n,top} = 1.00(49.9\text{ kips})$ | $\frac{V_{n,top}}{\Omega_v} = \frac{49.9\text{ kips}}{1.50}$ |
| $= 49.9$ kips | $= 33.3$ kips |
| $\phi_v V_{n,bot} = 1.00(60.1\text{ kips})$ | $\frac{V_{n,bot}}{\Omega_v} = \frac{60.1\text{ kips}}{1.50}$ |
| $= 60.1$ kips | $= 40.1$ kips |

*Check vertical shear at beam gross section*

| LRFD | ASD |
|------|-----|
| $V_u = 44.1$ kips (see Table 4-28) | $V_a = 31.3$ kips (see Table 4-28) |

From AISC *Specification* Section G2.1(b)(1):

$$\frac{h}{t_{w,min}} = \frac{30.5\text{ in.} - (0.950\text{ in.} + 1.15\text{ in.})}{0.350\text{ in.}}$$

$$= 81.1 > 1.10\sqrt{\frac{5.34(29,000\text{ ksi})}{50\text{ ksi}}} = 61.2$$

$$C_{v1} = \frac{1.10\sqrt{k_v E_s F_y}}{h/t_w} \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad (Spec.\text{ Eq. G2-4})$$

$$= \frac{1.10\sqrt{\frac{5.34(29,000\text{ ksi})}{50\text{ ksi}}}}{81.1}$$

$$= 0.755$$

$$V_{n,gross} = 0.60F_y\left(d_{eff,e-min}\right)C_{v1} \qquad\qquad\qquad\qquad\qquad\qquad (Spec.\text{ Eq. G2-1})$$

$$= 0.60(50\text{ ksi})(30.5\text{ in.})(0.350\text{ in.})(0.755)$$

$$= 242\text{ kips}$$


AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 97



<!-- Page 106 -->

<!-- Page 106 -->

| LRFD | ASD |
|------|-----|
| From Table 4-28, | From Table 4-28, |
| $V_{n,net} = 44.1$ kips | $V_{n,net} = 31.3$ kips |
| $V_{n,global} = V_{n,net} + concrete\;shear\;strength$ | $V_{n,global} = V_{n,net} + concrete\;shear\;strength$ |
| $= 44.1$ kips $+ 7.39$ kips | $= 31.3$ kips $+ 4.93$ kips |
| $= 51.5$ kips | $= 36.2$ kips |

From AISC *Specification* Section G1:

$$\frac{h}{t_w} = 81.1 > 2.24\sqrt{\frac{29,000\text{ ksi}}{50\text{ ksi}}} = 53.9$$

Therefore, $\phi_v = 0.90$ and $\Omega_v = 1.67$.

Available vertical shear strength at gross section

| LRFD | ASD |
|------|-----|
| $\phi_v V_{n,gross} = 0.90(242\text{ kips})$ | $\frac{V_{n,gross}}{\Omega_v} = \frac{242\text{ kips}}{1.67}$ |
| $= 218$ kips | $= 145$ kips |

The following is a summary of the beam shear strengths:

| LRFD | ASD |
|------|-----|
| *Horizontal shear* | *Horizontal shear* |
| $V_h/\phi_v V_{n,horiz} = 38.9\text{ kips}/84.0\text{ kips}$ | $V_hΩ_v/V_{n,horiz} = 27.3\text{ kips}/50.3\text{ kips}$ |
| $= 0.463$ **o.k.** | $= 0.543$ **o.k.** |
| *Vertical shear–top tee* | *Vertical shear–top tee* |
| $V_{u,top}/\phi_v V_{n,top} = 20.5\text{ kips}/49.9\text{ kips}$ | $V_{u,top}Ω_v/V_{n,top} = 14.4\text{ kips}/33.3\text{ kips}$ |
| $= 0.411$ **o.k.** | $= 0.432$ **o.k.** |
| *Vertical shear–bottom tee* | *Vertical shear–bottom tee* |
| $V_{u,bot}/\phi_v V_{n,bot} = 27.7\text{ kips}/60.1\text{ kips}$ | $V_{u,bot}Ω_v/V_{n,bot} = 19.5\text{ kips}/40.1\text{ kips}$ |
| $= 0.461$ **o.k.** | $= 0.486$ **o.k.** |
| *Vertical shear–gross section* | *Vertical shear–gross section* |
| $V_u/\phi_v V_{n,gross} = 44.1\text{ kips}/218\text{ kips}$ | $V_aΩ_v/V_{n,gross} = 33.3\text{ kips}/145\text{ kips}$ |
| $= 0.202$ **o.k.** | $= 0.230$ **o.k.** |

*Check deflection*

Deflections are calculated using 90% of the moment of inertia per Section 3.7.


98 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31



<!-- Page 107 -->

<!-- Page 107 -->

The pre-composite dead load deflection is:

$$\Delta_{PDL} = \frac{5wL^4}{384EI_{x,net}(0.90)}$$

$$= \frac{5\left(\frac{0.44\text{ kip/ft}}{12\text{ in./ft}}\right)\left[(50\text{ ft})(12\text{ in./ft})\right]^4}{384(29,000\text{ ksi})\left(1,710\text{ in.}^4\right)(0.90)}$$

$$= 1.39\text{ in.}$$

Live load deflection is:

$$\Delta_{LL} = \frac{5wL^4}{384EI_{x,comp}(0.90)}$$

$$= \frac{5\left(\frac{0.8\text{ kip/ft}}{12\text{ in./ft}}\right)\left[(50\text{ ft})(12\text{ in./ft})\right]^4}{384(29,000\text{ ksi})\left(5,100\text{ in.}^4\right)(0.90)}$$

$$= 0.845\text{ in.}$$

$$= \frac{L}{710}$$

Dead load deflection is:

$$\Delta_{DL} = \frac{5wL^4}{384EI_{x,comp}(0.90)}$$

$$= \frac{5\left(\frac{0.16\text{ kip/ft}}{12\text{ in./ft}}\right)\left[(50\text{ ft})(12\text{ in./ft})\right]^4}{384(29,000\text{ ksi})\left(5,100\text{ in.}^4\right)(0.90)}$$

$$= 0.169\text{ in.}$$

$$= \frac{L}{3,550}$$

Total load deflection is:

$$\Delta_{TL} = \Delta_{LL} + \Delta_{DL}$$

$$= 0.845\text{ in.} + 0.169\text{ in.}$$

$$= 1.01\text{ in.}$$

$$= \frac{L}{590}$$

*Deflection summary*

$$\Delta_{PDL} = 1.39\text{ in.}; \text{therefore, camber } 1\text{ in.}$$

$$\Delta_{LL} < \frac{L}{360} \qquad \textbf{o.k.}$$

$$\Delta_{TL} < \frac{L}{240} \qquad \textbf{o.k.}$$


AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 99



<!-- Page 108 -->

<!-- Page 108 -->


100 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31



<!-- Page 109 -->

<!-- Page 109 -->

Table 4-33. Horizontal Shear Force at Each Opening

| Post<br>Number | $X_i$,<br>ft | ASD |  |  | LRFD |  |  |
|----------------|--------------|------|------|------|------|------|------|
|  |  | $T_{r(i)}$,<br>kips | $T_{r(i+1)}$,<br>kips | $V_{ah} = \Delta T_a$,<br>kips | $T_{u(i)}$,<br>kips | $T_{u(i+1)}$,<br>kips | $V_{uh} = \Delta T_u$,<br>kips |
| 1.00 | 2.73 | 19.0 | 46.3 | 27.3 | 26.9 | 65.8 | 38.9 |
| 2.00 | 5.13 | 46.3 | 70.8 | 24.5 | 65.8 | 101 | 35.2 |
| 3.00 | 7.52 | 70.8 | 92.3 | 21.5 | 101 | 131 | 30.0 |
| 4.00 | 9.92 | 92.3 | 111 | 18.7 | 131 | 158 | 27.0 |
| 5.00 | 12.3 | 111 | 127 | 16.0 | 158 | 181 | 23.0 |
| 6.00 | 14.7 | 127 | 140 | 13.0 | 181 | 199 | 18.0 |
| 7.00 | 17.1 | 140 | 149 | 9.00 | 199 | 213 | 14.0 |
| 8.00 | 19.5 | 149 | 156 | 7.00 | 213 | 223 | 10.0 |
| 9.00 | 21.9 | 156 | 160 | 4.00 | 223 | 228 | 5.00 |
|  |  |  | Maximum: | 27.3 |  | Maximum: | 38.9 |

*Calculate web post buckling flexural strength*

| LRFD | ASD |
|------|-----|
| From Table 4-33, | From Table 4-33, |
| $V_{ah} = 38.9$ kips | $V_{ah} = 27.3$ kips |
| $M_u = 0.90\frac{D_o}{2}V_{ah}$ (from Eq. 3-31) | $M_a = 0.90\frac{D_o}{2}V_{ah}$ (from Eq. 3-31) |
| $= 0.90\left(\frac{20.8\text{ in.}}{2}\right)(38.9\text{ kips})$ | $= 0.90\left(\frac{20.8\text{ in.}}{2}\right)(27.3\text{ kips})$ |
| $= 363$ kip-in. | $= 255$ kip-in. |

*Calculate available flexural strength of web post*

By inspection the top web post will control because the diameter of the web opening is the same as the bottom web post, but the web is thinner.

$$S_{x,webpost-top} = \frac{t_w\left(S - D_o + 0.564D_o\right)^2}{6} \qquad\qquad\qquad\qquad\qquad\qquad (3-32)$$

$$= \frac{(0.350\text{ in.})\left[28.8\text{ in.} - 20.8\text{ in.} + 0.564(20.8\text{ in.})\right]^2}{6}$$

$$= 22.6\text{ in.}^3$$

$$M_e = S_{x,webpost-top}F_y \qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad (from\;Spec.\text{ Eq. F9-3})$$

$$= \left(22.6\text{ in.}^3\right)(50\text{ ksi})$$

$$= 1,130\text{ kip-in.}$$

$$C1 = 5.097 + 0.1464\left(\frac{D_o}{t_w}\right) - 0.00174\left(\frac{D_o}{t_w}\right)^2 \qquad\qquad\qquad\qquad\qquad (3-33)$$

$$= 5.097 + 0.1464\left(\frac{20.8\text{ in.}}{0.350\text{ in.}}\right) - 0.00174\left(\frac{20.8\text{ in.}}{0.350\text{ in.}}\right)^2$$

$$= 7.68$$


94 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31



<!-- Page 110 -->

<!-- Page 110 -->

$$C2 = 1.441 + 0.0625\left(\frac{D_o}{t_w}\right) - 0.000683\left(\frac{D_o}{t_w}\right)^2 \qquad\qquad\qquad\qquad\qquad (3-34)$$

$$= 1.44 + 0.0625\left(\frac{20.8\text{ in.}}{0.350\text{ in.}}\right) - 0.000683\left(\frac{20.8\text{ in.}}{0.350\text{ in.}}\right)^2$$

$$= 2.75$$

$$C3 = 3.645 + 0.0853\left(\frac{D_o}{t_w}\right) - 0.00108\left(\frac{D_o}{t_w}\right)^2 \qquad\qquad\qquad\qquad\qquad (3-35)$$

$$= 3.645 + 0.0853\left(\frac{20.8\text{ in.}}{0.350\text{ in.}}\right) - 0.00108\left(\frac{20.8\text{ in.}}{0.350\text{ in.}}\right)^2$$

$$= 4.91$$

$$\frac{M_{allow}}{M_e} = C1\left(\frac{S}{D_o}\right) - C2\left(\frac{S}{D_o}\right)^2 - C3 \qquad\qquad\qquad\qquad\qquad\qquad (3-36)$$

$$= 7.68\left(\frac{28.8\text{ in.}}{20.8\text{ in.}}\right) - 2.75\left(\frac{28.8\text{ in.}}{20.8\text{ in.}}\right)^2 - 4.91$$

$$= 0.466$$

The available flexural strength is:

| LRFD | ASD |
|------|-----|
| From Equation 3-37a, | From Equation 3-37b, |
| $\phi_b\left(\frac{M_{allow}}{M_e}\right)M_e = 0.90(0.466)(1,130\text{ kip-in.})$ | $\left(\frac{M_{allow}}{M_e}\right)\frac{M_e}{\Omega_b} = 0.466\left(\frac{1,130\text{ kip-in.}}{1.67}\right)$ |
| $= 474$ kip-in. | $= 315$ kip-in. |

*Web Post Buckling Summary*

| LRFD | ASD |
|------|-----|
| $M_u$ = 363 kip-in. | $M_a$ = 255 kip-in. |
| $\phi_b\left(\frac{M_{allow}}{M_e}\right)M_e$ = 474 kip-in. | $\left(\frac{M_{allow}}{M_e}\right)\frac{M_e}{\Omega_b}$ = 315 kip-in. |
| $= 0.766 < 1.0$ **o.k.** | $= 0.810 < 1.0$ **o.k.** |

*Check horizontal and vertical shear*

The available horizontal shear strength is calculated using AISC *Specification* Section J4.2. By inspection, the top section will control because the web is thinner.

| LRFD | ASD |
|------|-----|
| From Table 4-33, | From Table 4-33, |
| $V_{uh} = 38.9$ kips | $V_{ah} = 27.3$ kips |
| From *Spec.* Eq. J4-3, | From *Spec.* Eq. J4-3, |
| $\phi_v V_{n,horiz} = \phi_v 0.60F_y(et_w)$ | $\frac{V_{n,horiz}}{\Omega_v} = \frac{0.60F_y(et_w)}{\Omega_v}$ |
| $= 0.60(50\text{ ksi})\left[(8.00\text{ in.})(0.350\text{in.})\right]$ | $= \frac{0.60(50\text{ ksi})\left[(8.00\text{ in.})(0.350\text{in.})\right]}{1.50}$ |
| $= 84.0$ kips $> 38.9$ kips **o.k.** | $= 50.3$ kips $> 27.3$ kips **o.k.** |


AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 95



<!-- Page 111 -->

<!-- Page 111 -->

# FURTHER READING

Adams, A. (1999). *Composite Design of Castellated Beams*, M.S. Thesis, Virginia Polytechnic Institute, Blacksburg, VA.

Adams, A. (2000). *Castellated Beam Design Procedure—AISI Factored Load Approach*, Smyrna, TN: AISI Steel. Doc. # 2-9808.

AISC (2002). "Experimental Testing of Simply- and Multiply-Supported Castellated Beams," *Engineering Journal*, AISC, Vol. 39, No. 2, 2nd Quarter, pp. 140–146.

AISC (2005). *Specification for Structural Steel Beams with Web Openings*, AISC, Chicago, IL.

ASCE Task Committee on Design Criteria for Composite Structures in Steel and Concrete (1992). "Proceedings on Proposed Specifications for Structural Steel Beams with Web Openings," *Journal of Structural Engineering*, ASCE, Vol. 118, No. 12, December, pp. 3315–3324.

ASTM (2000). *Standard Test Methods & Tension Testing of Metallic Materials*, ASTM International, West Conshohocken, PA.

Bazile, A. (2004). "Influence Test Data to Investigate the Performance of Flexural Beams Subjected to Concentrated Loadings," *Fire Safety Journal*, Vol. 39, Issue 6, pp. 609–750.

Bazile, A. and Texier, J. (2002). "The Behaviour of Perforated Beams in Pure Bending," M.S. Thesis, Polytechnic Institute Montreal, Montreal, Quebec.

Blodgett, O.E. (1966). *Design of Welded Structures—Castellated Steel Beams—Structural Research Report*, Pennsylvania: University of Linaee, James F. Lincoln Arc Welding Foundation, Cleveland, OH.

Boyer, J.F. (1964). *Castellated Beams—New Developments*, Construction Métallique, No. 3, pp. 12–25.

Boller, P.A. and Colson, J.L. (2002). "Smart Thinking," *Civil Engineering*, ASCE, Vol. 72, No. 7, pp. 43–48.

Bonner, M.A., Darwin, D. and Deschey, R.C. (1998). "Deflections of Composite Beams with Web Openings," *SM Report*, No. 48, University of Kansas, Lawrence, KS, No. 10, pp. 1,139–1,147.

Blum, D., Damiatis, T. and Mamis, P.D. (2004). "Steel Section Properties Including Moment of Inertia and Design Based on Experimental Studies and Numerical Analysis," *International Symposium: Proceedings of the 4th International Conference on Steel and Composite Structures*, Volume 8, Montreal, The Netherlands, June 8–10, pp. 1033–1046.

Boyer, J.P. (1964). "Castellated Beams-Modern Steel Construction," AISC, April 30.

Brienza, J. (1996). "Design of Beams with Rectangular Holes Using Novel Concepts in Lateral Buckling of Non-Composite Unequal Castellated and Cellular Beams," *Proceedings of the National Conference*, Univ. of Missouri Rolla, Report 96-10, pp. 9–15.

Brienza, J. (1996). "Experimental Stresses in Wide-Flange Beams with Holes," *Journal of Structural Engineering*, ASCE, Vol. 122, No. 2, pp. 211–219.

Brienza, J. (1990). "Design of Beams with Web Openings," *Structural Stability Research Council*, Annual Meeting, Vol. 56, Theme 05.

Chung, K.F., Liu, T.C.H. and Ko, A.C.H. (2001). "Investigation on Vierendeel Mechanism in Steel Beams with Rectangular Holes," *Journal of Constructional Steel Research*, AISC, Vol. 54, No. 1, pp. 39–57.

Chung, J.Y. and Liu, T.C.H. (2001). "Stress Analysis of Steel Beams with Large Web Openings at Various Shapes and Sizes: An Experimental Study Using Ground Based Holography," *International Journal of Experimental Mechanics*, Vol. 39, No. 5, pp. 1,173–1,200.

Chung, K.F., Liu, T.C.H. and Ko, A.C.H. (1991). "Investigation of Vierendeel Bending Mechanism in Perforated Circular Web Openings," *Journal of Constructional Steel Research*, Vol. 60, No. 1, pp. 1–40.

Chung, J.Y., Liu, T.C.H. and Liu, X.L. (2003). "Shear Resistance of Composite Beams with Large Web Openings in Different Transfer Mechanics," *Journal of Constructional Steel Research*, Vol. 64, No. 5, pp. 1,059–1,069.

Chretien, M. (1982). "Tests of Composite Beams with Web Openings Based on Post-Elastic Analysis," *Structural Engineer*, AISC, Vol. 60B, No. 3, pp. 49–54.

Cimadon, J.H. and Redwood, R.G. (1970). "Plastic Behavior of Plates with Holes," *Journal of Structural Division*, ASCE, Vol. 96, pp. 1,969–1,984.

Cooper, P.B. (1973). "Strength of Steel Beams with Eccentric Web Holes," *Journal of the Structural Division*, ASCE, Vol. 99, No. 3, p. 511.

Cooper, P.B. and Snell, R.B. (1972). "Tests on Beams with Rectangular Web Holes," *Journal of the Structural Division*, ASCE, Vol. 98, No. ST5, pp. 1,265–1,283.

Coulson, J. (1999). "Cellular Beam Design Calculations," SAI Global Limited, Doc. No. 99, p. 43.

Darwin, D. (1990). "Design of Steel and Composite Beams with Web Openings," *Design Guide for Castellated and Castellated Composite Beams*, PhD Dissertation, University of Kansas, Lawrence, KS, No. 26, pp. 1,066–1,078.

Darwin, D. (2000). "Steel and Composite Beams with Web Openings," *Engineering Journal*, AISC, Vol. 31, No. 2, 1st/3rd, pp. 59–69.

Demirdjian, S. (1999). "Simply-Supported Castellated and Composite Beams with Web Openings," *Journal of Structural Engineering*, AISC, Vol. 116, No. 9, pp. 2,315–2,331.

Demirdjian, D. and De Bossé, G. (2004). "Experimental and Behavioral Moment Analysis of a Lightweight Steel Section with Simply Supported Web Openings," *Proceedings of the 2004 International Conference on Noise and Vibration Engineering*, Leuven, Belgium, SMA.

CEN (1990). *Eurocode 3: Design of Steel Structures, Part 1.1: General Rules and Rules for Buildings*, ENV 1993-1-1, British Standards Institution.

CEN (1998). *Eurocode 3: Design of Steel Structures, Part 1.1: General Rules and Rules for Buildings*, prEN 1993-1-1, British Standards Institution, Brussels, Belgium.

Frothier, J.P. and Boissonade, N. (1992). "Experimental and en relie 91-037-U.S. Comite Europeen de Normalisation, Brussels, Belgium.

Frountier, A. (2003). "Design Method for Composite Beams with Large and Closely Spaced Web Openings in Structural Division," ASCE, Vol. 36, pp. 231–248.

Gardner, L. and Daschenko, M.A. (1968). "Moment Analysis of Castellated Steel Beams," *Journal of Institute University of Civil Engineering and Arch-itecture*, Vol. 30, No. 3, pp. 35–45.


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 105*




<!-- Page 112 -->

<!-- Page 112 -->

Chung, J.J. (1993). "Design of Steel Beams with End-Coped," Ph.D. Dissertation, University of Toronto, Toronto, ON, Canada.

Chung, J.J. and Lawson, R.M. (2001). "A Study of Large Web Openings at Various Shapes and Sizes: An Experimental Study Using Ground Based Holography," *Journal of Constructional Steel Research*, Vol. 59, No. 5, pp. 1,177–1,200.

Chung, K.F., Liu, T.C.H. and Ko, A.C.H. (2001). "Investigation of Vierendeel Mechanism in Steel Beams with Circular Web Openings," *Journal of Constructional Steel Research*, Vol. 57, No. 5, pp. 467–490.

Chung, K.F., Liu, T.C.H. and Ko, A.C.H. (2003). "Strength of Composite Beams with Large Web Openings in Transfer Mechanisms," *Journal of Constructional Steel Research*, Vol. 59, No. 5, pp. 1,005–1,024.

Chrétien, M. (1982). "Tests of Composite Beams with Web Openings Based on Post-Elastic Analysis," *The Structural Engineer*, AISC, Vol. 60B, No. 3, pp. 49–54.

Cimadon, J.H. and Redwood, R.G. (1970). "Plastic Behavior of Plates with Holes," *Journal of Structural Division*, ASCE, Vol. 96, pp. 1,969–1,984.

Cooper, P.B. (1973). "Strength of Steel Beams with Eccentric Web Holes," *Journal of Structural Division*, ASCE, Vol. 99, No. 3, p. 511.

Cooper, P.B. and Snell, R.B. (1972). "Tests on Beams with Rectangular Web Holes," *Journal of the Structural Division*, ASCE, Vol. 98, No. ST5, pp. 1,265–1,283.

Coulson, J. (1999). "Cellular Beam Design Calculations," SAI Global Limited, Doc. No. 99, p. 43.

Darwin, D. (1990). "Design of Steel and Composite Beams with Web Openings," *Design Guide for Castellated and Castellated Composite Beams*, PhD Dissertation, University of Kansas, Lawrence, KS, No. 26, pp. 1,066–1,078.

Darwin, D. (2000). "Steel and Composite Beams with Web Openings," *Engineering Journal*, AISC, Vol. 31, No. 2, pp. 59–69.

Demirdjian, S. (1999). "Simply-Supported Castellated and Composite Beams with Web Openings," *Journal of Structural Engineering*, AISC, Vol. 116, No. 9, pp. 2,315–2,331.

Demirdjian, D. and De Bossé, G. (2004). "Experimental and Behavioral Moment Analysis of a Lightweight Steel Section with Simply Supported Web Openings," *Proceedings of the 2004 International Conference on Noise and Vibration Engineering*, Leuven, Belgium, SMA.

Donahey, R.C. (1985). "Web Buckling of Castellated and Litzka Beams," Ph.D. Dissertation, McGill University, Montreal, Quebec, Canada.

Donahey, R.C. and Darwin, D. (1988). "Web Openings in Composite Beams with Rectangular Web Openings," *Proceedings of the 9th International Specialty Conference, Structural Stability Research Council*, University of Missouri-Rolla, Rolla, MO, pp. 363–378.

Gibson, J.E. and Jenkins, W.M. (1957). "Investigation of the Stresses and Deflections in Castellated Beams," *The Structural Engineer*, Vol. 35, pp. 937–942.

Gosch, K. (1975). "Stress Analysis of Castellated Beams," *Proceedings of the Japan Society of Civil Engineers*, Tokyo.

Grünbauer, P., Kato, Y. and Redwood, R.G. (1975). "Stresses and Deflections in Wide-Flange Beams with Holes," *Canadian Journal of Civil Engineers*, Vol. 2, No. 2, pp. 263–271.

Halleux, P. (1967). "Limit Analysis of Castellated Steel Beams," *Acier-Stahl-Steel*.


*106 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*




<!-- Page 113 -->

<!-- Page 113 -->

Hoadley, G. (1970). "Investigations into the Behaviour of Castellated Beams with Rectangular and Circular Holes," *Report to the 3rd Regional Conference on Planning and Development of the 3rd Region*, Szczecin, Vol. 1, pp. 157–166.

Hosain, M.U. (1977). "Optimized Design of Steel Beams with Rectangular Web Openings," *Canadian Journal of Civil Engineering*, Vol. 4, No. 1, pp. 112–119.

Hosseney, I., Hoffman, R.M., Dinehart, D.W., Gross, S.P. and Yost, J.R. (2004). "Experimental Report on the Geometry of Composite Beams with Concentrated Web Openings and Cellular Beams," *Proceedings of the 18th ASCE Conference of Engineering Mechanics*, University of Delaware, Newark, DE.

Hosseney, I., Hoffman, R.M., Dinehart, D.W., Gross, S.P. and Yost, J.R. (2004). "Effect of Cope Geometry on Web Buckling of Coped Beams," *Proceedings of the 2nd Annual AASCE Conference*, Vol. 1, pp. 1-11, Iowa State University, Villanova, PA.

Hosseney, I., Reddy, V., Guzas, S.P. and Yost, J.R. (2006). "Experimental Behavior of Composite Beams with Closely Spaced Web Openings: Effect of Shear Connection Interaction," *Proceedings of the 18th ASCE Conference of Structural Engineering*, ASCE, Aug. 26, Vol. 32, No. 8, pp. 1–14.

Huang, W., Fenwick, P.L., Spence, S.P. and Yost, J.R. (2005). "Finite Element Analysis of the Performance and Modal Properties of Composite," *Proceedings of the 18th International ANSYS Conference*, Pittsburgh, PA.

Husain, M.U., Demirdjian, S. and Speirs, W. (1973). "Composite Steel Beams with Large Web Openings," *Journal of the Structural Division*, ASCE, Vol. 99, No. 10, pp. 2,099–2,117.

Jeon, H., Redwood, R. (1977). "Specified Design Analysis for Beams," *Canadian Journal of Civil Engineering*, Vol. 3, No. 3, p. 8.

Kaizuka, H. (1978). "Numerical Investigations of Composite Cellular Beams with Web Openings," *Journal of Structural Engineering*, ASCE, Vol. 103, No. 6, pp. 1,073–1,089.

Knowles, P.R. (1985). *Design of Castellated Beams: For Use with BS 5950 and BS 449: The Steel Construction Institute*, Publication 100, Berkshire, UK.

Kubowski, J. (1964). "Stresses and Deflections in Castellated Beams," *Proceedings of the Warsaw University of Technology*, No. 17, p. 39.

Lahnert, W.J. (1984). "Analysis, Testing and Design of a Load Deflection Study of Hybrid Castellated Steel Beams," *Proceedings of the 19th University Castellated Beams Conference*, University of Delaware, Newark, DE.

Lalka, R.A. (1998). "Spacing of Connections in Composite Beams with Large Web Openings," PhD-Tested Steel Beams," *Structural Research Report*, Pennsylvania: James F. Lincoln Arc Welding Foundation, Cleveland, OH, Cleveland Steel Structures, St. Louis, MO.

Lawson, R.M. (1984). *Cellular Beams: A Design Guide for Steel Structures, SCI Publication* P100, Berkshire, UK.

Lawson, R.M. (2004). "Developments in Steel Framed Buildings," *Proceedings of the 2nd International Conference on Steel and Composite Structures*, Seoul, Korea.

Liu, T.C.H. and Chung, K.F. (2003). "Steel Beams with Large Web Openings of Various Shapes and Sizes: Finite Element Investigation," *Journal of Constructional Steel Research*, Vol. 59, No. 9, pp. 1,159–1,176.

Liu, T.C.H. and Chung, K.F. (2003). "Steel Beams with Large Web Openings of Various Shapes and Sizes: An Experimental Investigation," *Journal of Constructional Steel Research*, Vol. 59, No. 11.

McCormick, J.D., Gross, S.P., Wenti, R.A. and Maines, C.A. (2004). "Finite Element Analysis and Testing of Non-Composite and of the Non-word Division," AISC, Vol. 97, No. 7, pp. 1,141–1,153.

McGrew, B. (1985). "Design of Castellated Beams," *M.S. Thesis*, University of Idaho, ID, USA.

Milligan, R. (2001). "The Steel Deck Initiative: Modern Steel Construction," AISC, Vol. 41, No. 5, pp. 33–38.

Moorman Valley Structural Steel Company (1962), *Design and Construction of Castellated Beams*, Bridgeville, PA.

Moorman Valley Structural Steel Company (1990), *Castellated Beams*, Bridgeville, PA.

Nair, R.S. (1984). "Structural Design Methods: Influence of Castellated Beams," *Journal of Construction*, June 15, SA, Vol. 122, No. 4, pp. 765-777, Johannesburg, South Africa.

Narayanan, R. and Ooshuizeneaone, N. (1986). "Analysis of Castellated Steel Beams with Rectangular Web Openings," *Plan Blokef Society*, Vol. 2, pp. 261–270.

Nethercot, D.A. (1983). "Buckling of Laterally Unsupported Castellated Beams," *The Structural Engineer*, Research Council Bulletin, Vol. 72, No. 8, pp. 89–101.

Orielis, T. and Nethercot, D.A. (1985). "Web Post Strength in Castellated Steel Beams," *Proceedings of the Institution of Civil Engineering*, Vol. 79, Part 2, pp. 295–312.

O'Neill, R. (1973). "Composite Action Without Shear Connection," *Proceedings of the 2nd International Symposium on Composite Structures*, University of Delaware, Newark, DE.


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 107*




<!-- Page 114 -->

<!-- Page 114 -->

Parr, A. (1992). "Strength and Stiffness of Perforated Beams with Weld Gaps and Lateral Loads," *Proceedings* Annual ISC Symposium, Vol. 45, pp. 44–46, Tulsa: Petroleum.

Parry, G. (1982). "Castellated Beams: Design and Construction of Composite," *Engineering Journal*, AISC, Vol. 24, 4th Quarter, pp. 115–127.

Pavel, S., Hoffman, R.M., Dinehart, D.W., Gross, S.P and Yost, J.R. (2006). "Experimental and Finite Element Study of Castellated Beams," *Proceedings of the Structural Engineers Institute of the American Society of Civil Engineering's 18th International Structural Specialty Conference*, ISSC I, Vol. 47, pp. 225-232.

Pedrajas, A.C. (1983). *Structural Steel Design*, Villanova University, Villanova, PA.

Poirza, G., Martin, P.O., Barrett, L.A. and Thomson, W.R. (2002). "Proposed Effect on Castellated and Composite Beam Section Connections by Use of Web Openings," *Engineering Journal*, AISC, Vol. 39, No. 3, pp. 137–144.

Poirza, G., Martin, P.O. and Rodriguez, J.M. (2003). "Experimental and Computational Effects on the Strength and Behavior of Cellular and Castellated Composite Beams," *Proceedings of Annual Steel Conference*, AISC, Vol. 33, No. 3, pp. 28–33.

Redler, J.M., Dinehart, D.W., Hoffman, R.H., Gross, S.P., Yost, J.R. and Li, P.J. (2005). "Experimental and Finite Element Analysis of Hybrid Composite Castellated Beams under Concentrated Loading and End Coping," *Research Report to ABM Steel Products*, University, Villanova, PA.

Redler, J.M., Dinehart, D.W., Hoffman, R.H., Gross, S.P., Yost, J.R. and Li, P.J. (2006). "Experimental and Analytical Investigation of the Effects of a Cope on the Buckling Behavior of Hybrid Castellated Beams," *Research Report to ABM Steel Products*, University, Villanova, PA.

Redwood, R. (1973). "Tests on Castellated Beams," *Engineering Journal*, AISC, Vol. 10, No. 11.

Redwood, R.G. (1969). "The Plastic Behavior of Castellated Beams," *Proceedings of the Institute of Civil Engineering*, ASCE, Vol. 24, pp. 109-123.

Redwood, R. and Demirdijan, S. (1998). "Castellated Beam Web Buckling in Shear," *Journal of Structural Engineering*, ASCE, Vol. 124, No. 10, pp. 1,205–1,212.

Redwood, R. and Wong, P.K. (1982). "Web Holes in Beam Webs Subjected to Bending and Shear," *Structural Division*, ASCE, Vol. 94, No. 1, pp. 1–18.

Redwood, R. (1983). "Web Holes in Composite Beams with Partial Shear Connection," *Proceedings of the International Structural Engineering Conference*, Toronto, February.

Redwood, R.G. and Shrivastava, S.C. (1980). "Design Recommendations for Steel Beams with Web Holes," *Canadian Journal of Civil Engineering*, AISC, Vol. 7, pp. 642–650.

Redwood, R. (1977). "Supplemental Design Criteria for Beams with Web Holes," *Journal of Structural Engineering*, ASCE, Vol. 103, No. 10, pp. 2,053–2,067.

Redwood, R. (2005). "Castellated Beams: General Investigation and Transference," AISC, Vol. 108, pp. 8.

Redwood, R. (1997). "Castellated Design Procedure for Beams with Web Holes," *Journal of Structural Division*, AISC, No. 4, pp. 120–131.

Redwood, R. (2002). "Experimental and Numerical Analysis of Castellated Beams," *Canadian Journal of Civil Engineering*, Vol. 29, No. 6, pp. 1,044–1,050.

Redwood, R. (1983). "Cellular Beams: Good Lateral Analysis of Beams with Web Openings," *Revue and Beams Column: Stability and Strength*, CRC Press, Boca Raton, FL.

Remmers, R. and Bouwkamp, H. (1979). "Tensile Strength and Mode of Failure of Short Welded Beams with Unannotated Holes," *Journal of the Structural Division*, AISC, Vol. 105, pp. 1,031–1,045.

Servaan, S.L. (1994). "Finite Analysis of Castellated Beams: Comparative and Monitoring," Vol. 50, p. 62.


*108 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*




<!-- Page 115 -->

<!-- Page 115 -->

Servaan, S.L. (1995). "Study of Optimum Expansion Ratio of Castellated Beams," *Proceedings of Institution of Engineers Civil Engineering*, Vol. 86, June, pp. 75–78.

Servaan, S.L. (1996). "Investigation of Deflections in Castellated Beams," *Journal of Construction*, June 15, Vol. 122, No. 4, pp. 765–777, Johannesburg, South Africa.

SCI (2012). *Design Guide on the Use of Fabricated Beams in Accordance with Eurocode 3*, Structural Engineering Committee on Flexural Members of the Structural Division*, AISC, Vol. 94, No. ST12, pp. 2,729–2,750.

Srimani, S.L. (1970). "Suggested Design Method for Fabrication of Castellated and Cellular Beams Capacity with Bending Moments," *Research Report of the Civil Engineering Department of the Council for Scientific and Industrial Research*, Pretoria, South Africa.

Srimani, S.L. and Das, P.K. (1978). "Experimental Study of the Analysis, Testing and Design of a Load Resistance of Buildings in a Civil Engineering Laboratory," *Indian Concrete Journal*, Indian Concrete Institute, Vol. 52, No. 8, pp. 217–219.

Thomoson, FIT (1991). "Swedish Solution for Residential Buildings," *Modern Steel Construction*, AISC, October, pp. 51–54.

Thomoson, B.G. (1987). "Lateral Torsional Buckling of Steel Girder with Moment-Shear Interaction," *Journal of Structural Engineering*, AISC, Vol. 113, No. 2, pp. 379–388.

Thomoson, B.G. and Redwood, R.G. (1976). "Lateral Stability Research Council—*Bulletin Series*, No. 47.

Vora, E.J., Cooper, P.B. and Snell, R.B. (1975). "Strength and Deflection of Plate Girders with Rectangular Holes," *Journal of the Structural Division*, ASCE, Vol. 101, No. 5, pp. 1,283–1,300.

Vora, E.J. and Cooper, P.B. (1978). "The Stability of the Design of Cellular Beams," M.S. Thesis, University of Kwazulu-Natal, School of Civil Engineering, Department of Structural Engineering.

Weiss, S. (1975). "Estimating the Stability of Castellated Steel Beams," *Architecture Rectilinear Leitkogo*, Vol. 33, No. 1.

Witwer, J. (2003). "Local Web Buckling Strength of Coped Steel Beams," *Proceedings of the American Society of Civil Engineering*, ASCE.

Witwer, J. (2004). "Local Web Buckling Strength of Coped Steel Beams," *Journal of Constructional Steel Research*, Vol. 60, pp. 1,313–1,341.

Yam, M. (2004). "Experimental Investigation of the Local Web Buckling Strength of Coped Steel Beams," *Proceedings of the Canadian Society for Civil Engineering*, London, Ontario, June 2–5.

Zaarour, W. and Redwood, R. (1996). "Web Buckling in Thin Web Girders," *Journal of Structural Engineering*, ASCE, Vol. 122, No. 8, pp. 860–866.

Zaarour, W., Mosley, C.P., Gross, S.P and Redwood, R. (2003). "Numerical Investigations (SFEM) of Thin Webbed Castellated Beams," *Journal of Structural Steel Research*, Vol. 62, No. 3, pp. 903–871.

Young, J.R., Hoffman, R.H., Dinehart, D.W. and Gross, S.P. (2003). "An Experimental Investigation of the Effects of Lateral Support Distributions in Non-Composite Castellated Beams with Sinusoidal Web Openings," *Proceedings of the 19th International Conference on Structural Mechanics and Architecture*, Lehigh, PA.

Young, J.R., Hoffman, R.H., Dinehart, D.W. and Gross, S.P. (2006). "An Experimental Investigation of the Effects of Lateral Support Distributions in Non-Composite Cellular Beams with Sinusoidal Web Openings (JICRM)," *Annual Meeting*, Germany, June.

Yuan, J.A., Blowes, P.C. and Ruddis, J.M. (1982). "Beam Action with Web Openings," *Proceedings of the International Conference on Stability of Steel Beams with Web Openings*, ASCE, Vol. 108, No. 7, pp. 313–325.

Yuan, J.A., Blowes, P.C. and Ruddis, J.M. (1982). "Web Crippling of Fastened Plates," *Journal of the American Steel Construction*, AISC, Vol. 123, No. 6, pp. 860–866.

Zeggane, M., Amrine, S.A., Dinehart, D.W., Hoffman, R. (2005). "Thin Webbed Castellated Beams," *Journal of Structural Engineering*, ASCE, Vol. 124, No. 10, pp. 1,205–1,212.


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 109*




<!-- Page 116 -->

<!-- Page 116 -->


*110 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*




<!-- Page 117 -->

<!-- Page 117 -->


*104 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*


