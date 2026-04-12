# Chapter 5: Design of Embedded Base Connections

*Source: AISC Design Guide 1 - Base Connection Design for Steel Structures (3rd Edition)*

*Pages 141-150*

---

<!-- SOURCE: Page 141 -->

$$e_{crit,y} = \frac{B}{2} - \frac{P}{2q_{max}}$$ (from Eq. 4-53)

Using $N = B = 14.0$ in.,

$$e_{crit} = \frac{N}{2} - \frac{P}{2q_{max}}$$ (from Eq. 4-53)

$$= \frac{14.0 \text{ in.}}{2} - \frac{90.0 \text{ kip}}{(2)(61.9 \text{ kip/in.})}$$

$= 6.27$ in.

The eccentricity in the strong-axis direction may be calculated as:

$$e_x = \frac{M_{ux}}{P_u}$$ (from Eq. 4-37)

$$= \frac{700 \text{ kip-in.}}{90.0 \text{ kips}}$$

$= 7.78$ in.

The eccentricity in the weak-axis direction may be calculated as:

$$e_y = \frac{M_{uy}}{P_u}$$ (from Eq. 4-37)

$$= \frac{450 \text{ kip-in.}}{90.0 \text{ kips}}$$

$= 5.00$ in.

This indicates that this is a high-moment condition in the strong-axis direction, and a low-moment condition in the weak-axis direction.

3. Determine bearing length, $Y$, and anchor rod tension, $T_u$, due to bending in the strong-axis direction.

$$Y = \left(f + \frac{N}{2}\right) \pm \sqrt{\left(f + \frac{N}{2}\right)^2 - \frac{2P_u(e_x + f)}{q_{max}}}$$ (from Eq. 4-58)

$$= \left(5.50 \text{ in.} + \frac{14.0 \text{ in.}}{2}\right) \pm \sqrt{\left(5.50 \text{ in.} + \frac{14.0 \text{ in.}}{2}\right)^2 - \frac{2(90.0 \text{ kips})(7.78 \text{ in.} + 5.50 \text{ in.})}{61.9 \text{ kip/in.}}}$$

$= 12.5$ in. $\pm 10.8$ in.

$= 1.70$ in.

$$T_u = q_{max}Y - P_u$$ (from Eq. 4-55)

$$= (61.9 \text{ kip/in.})(1.70 \text{ in.}) - 90.0 \text{ kips}$$

$= 15.2$ kips

A trial anchor size and base plate thickness may be estimated for this condition, and then upsized anticipating additional loading from weak-axis bending.

4. Determine trial anchor rod size.

If two anchor rods are used on each face of the column, the force per rod is 7.60 kips. From Table 4-1, the design tensile strength of a ⅞-in.-diameter ASTM F1554 Grade 55 anchor rod is 12.7 kips. This size may be used conservatively, recognizing that the calculated anchor force does not include weak-axis bending, whose magnitude is approximately equal to that of strong-axis bending. It is assumed here that the embedment of the anchor rod is designed to prevent pullout and other concrete limit states.

---

AISC DESIGN GUIDE 1, 3rd EDITION / BASE CONNECTION DESIGN / 131

Downloaded by eva heo (mellowoutt28@gmail.com)

<!-- SOURCE: Page 142 -->

5. Determine trial base plate thickness.

For this, consider base plate yielding at both the bearing and tension interface due to strong-axis bending. For the bearing interface, determine $m$ and $n$:

$$m = \frac{N - 0.95d}{2}$$ (4-10)

$$= \frac{14.0 \text{ in.} - 0.95(8.50 \text{ in.})}{2}$$

$= 2.96$ in.

$$n = \frac{B - 0.8b_f}{2}$$ (4-11)

$$= \frac{14.0 \text{ in.} - 0.8(8.11 \text{ in.})}{2}$$

$= 3.76$ in.

Because $n > m$ and for Grade 50 material,

$$t_{pl(req)} = 1.49n\sqrt{\frac{f_{pl(max)}}{F_y}}$$ (from Eq. 4-51a)

This indicates bending along a yield line parallel to the web, without considering the additional effective width outlined in Appendix B.

$$t_{pl(req)} = 1.49(3.76 \text{ in.})_a\sqrt{\frac{4.42 \text{ ksi}}{50 \text{ ksi}}}$$

$= 1.67$ in.

For the tension interface,

$$t_{pl(req)} = 2.11\sqrt{\frac{T_ux}{BF_y}}$$ (4-62a)

where

$$x = f - \frac{d}{2} + \frac{t_f}{2}$$ (4-61)

$$= 5.50 \text{ in.} - \frac{8.50 \text{ in.}}{2} + \frac{0.685 \text{ in.}}{2}$$

$= 1.59$ in.

Thus,

$$t_{pl(req)} = 2.11\sqrt{\frac{(15.2 \text{ kips})(1.59 \text{ in.})}{(14.0 \text{ in.})(50 \text{ ksi})}}$$

$= 0.392$ in.

Base plate yielding at the bearing interface governs. Select a base plate of the following dimensions.

$B = N = 14.0$ in. and $t_p = 1¾$ in.

6. Estimate the moment strength of the base connection in each direction of bending.

Note that because the anchors and plate thickness are selected conservatively with respect to the induced loading in them, the strength of the connection in each direction needs to be determined based on the selected dimensions.

---

132 / BASE CONNECTION DESIGN / AISC DESIGN GUIDE 1, 3rd EDITION

Downloaded by eva heo (mellowoutt28@gmail.com)

<!-- SOURCE: Page 143 -->

For strong-axis bending:

Connection capacity due to anchor rod failure will be achieved when:

$$T_u = 2(12.7 \text{ kips})$$

$= 25.4$ kips

$$T_u = q_{max}Y - P_u$$ (from Eq. 4-55)

Thus,

$$Y = \frac{T_u + P_u}{q_{max}}$$

$$= \frac{25.4 \text{ kips} + 90.0 \text{ kips}}{61.9 \text{ kip/in.}}$$

$= 1.86$ in.

Because,

$$Y = \left(f + \frac{N}{2}\right) \pm \sqrt{\left(f + \frac{N}{2}\right)^2 - \frac{2P_u(e_x + f)}{q_{max}}}$$ (from Eq. 4-58)

A value of $e_x = 9.30$ in. may be determined by setting $Y = 1.86$ in.

This results in the moment capacity in the strong-axis direction due to yielding of the anchors as:

$$M_{x,P_u}^{Anchors} = e_x P_u$$

$$= (9.30 \text{ in.})(90.0 \text{ kips})$$

$= 837$ kip-in.

Note that although the connection may be classified as low moment for weak-axis bending for the given moment, the moment capacity in weak-axis bending assumes that axial load is held constant and the moment is increased to its capacity. In this context, because the plate is square with a symmetrical anchor layout, failure will be obtained under the high-moment condition such that $M_{x,P_u}^{Anchors} = M_{y,P_u}^{Anchors} = 837$ kip-in.

In strong-axis bending for the bearing interface, the maximum possible moment in the base plate is:

$$\frac{f_{pl(max)}Nn^2}{2} = \frac{(4.42 \text{ ksi})(14.0 \text{ in.})(3.76 \text{ in.})^2}{2}$$

$= 437$ kip-in.

This assumes the stress, $f_{pl(max)}$, is developed under the entire base plate. The moment capacity of the yield line is:

$$\phi F_y \frac{Nt_p^2}{4} = (0.90)(50 \text{ ksi})\frac{(14.0 \text{ in.})(1¾ \text{ in.})^2}{4}$$

$= 482$ kip-in.

This indicates that base plate yielding at the bearing interface is not possible.

The connection capacity due to base plate yielding at the tension interface may be calculated by setting $t_{pl(req)} = 1¾$ in. in the following equation:

$$t_{pl(req)} = 2.11\sqrt{\frac{T_ux}{BF_y}}$$ (4-62a)

---

AISC DESIGN GUIDE 1, 3rd EDITION / BASE CONNECTION DESIGN / 133

Downloaded by eva heo (mellowoutt28@gmail.com)

<!-- SOURCE: Page 144 -->

This results in $T_u = 303$ kips, which is significantly greater than the capacity of the anchors (25.4 kips), indicating that plate yielding at the tension interface will not govern. The moment capacity in the strong-axis direction is thus governed by anchor rod failure, such that:

$$M_{x,P_u} = M_{x,P_u}^{Anchors} = 837 \text{ kip-in.}$$

In the weak-axis direction, the moment capacity due to failure of the anchors has already been determined as $M_{y,P_u}^{Anchors} =$ 837 kip-in. Also, as for strong-axis bending, yielding of the base plate at the bearing interface is not possible, because the yield line is identical to that for strong-axis bending. The weak-axis strength due to yielding of the base plate at the tension interface may be determined by setting $t_{pl(req)} = 1¾$ in. in the following equation:

$$t_{pl(req)} = 2.11\sqrt{\frac{T_uy}{NF_y}}$$

The term $y$ corresponds to the cantilever distance from the yield line to the anchors and may be taken as $y = n - 1.50$ in., where 1.50 in. is the edge distance of the anchor holes. Consequently,

$$1.75 \text{ in.} = 2.11\sqrt{\frac{T_u(3.76 \text{ in.} - 1.50 \text{ in.})}{(14.0 \text{ in.})(50 \text{ ksi})}}$$

This results in $T_u = 213$ kips, which is significantly higher than the capacity of the anchors (25.4 kips), indicating that yielding of the base plate will not govern. As a result, yielding of the anchors will control the connection strength in the weak-axis direction.

$$M_{y,P_u} = M_{y,P_u}^{Anchors} = 837 \text{ kip-in.}$$

Once the moment strength in each direction is determined, the interaction equation may be used.

$$\left(\frac{M_{ux}}{M_{x,P_u}}\right)^2 + \left(\frac{M_{uy}}{M_{y,P_u}}\right)^2 = \left(\frac{700 \text{ kip-in.}}{837 \text{ kip-in.}}\right)^2 + \left(\frac{450 \text{ kip-in.}}{837 \text{ kip-in.}}\right)^2$$ (from Eq. 4-69)

$$= 0.988 \leq 1$$

This is an acceptable design. Note that other limit states for concrete have not been considered here and must be addressed as they are for base connections under uniaxial bending and compression.

**EXAMPLE 4.7-15—Anchor Reinforcement Design**

Anchor reinforcement to preclude concrete breakout in tension is designed in this example. The anchor reinforcement is designed to transfer the entire required strength across the concrete breakout cone plane.

**Given:**

Four ⅞-in.-diameter ASTM F1554 Grade 36 anchor rods with a heavy hex nut and 4.00 in. × 4.00 in. spacing are embedded in the center of a 20.0-in.-square concrete column. The concrete column has a specified compressive strength of concrete, $f_c' =$ 4,000 psi. Any required anchorage reinforcement will consist of two bars, Grade 60 $(f_y = 60,000 \text{ psi})$ ASTM A615M deformed bars.

It is required to confirm if the concrete will have adequate concrete breakout strength in tension to resist the required strengths. If the concrete breakout strength in tension is less than the required strength, determine the anchor reinforcement configuration necessary to preclude concrete breakout in tension and to resist the required strength. Finally, confirm that the anchorage will have adequate side-face blowout strength.

Verification of the steel anchor rod capacity and pullout capacity are addressed in Example 4.7-3.

The required strengths due to axial tensile loads is:

$$P_u = 70.0 \text{ kips (uplift)}$$

---

134 / BASE CONNECTION DESIGN / AISC DESIGN GUIDE 1, 3rd EDITION

Downloaded by eva heo (mellowoutt28@gmail.com)

<!-- SOURCE: Page 145 -->

**Solution:**

*Determine the concrete breakout strength in tension*

As the anchors are installed in a 20.0-in.-square concrete column, the concrete breakout strength would be limited by the column cross section. With an 8.00 in. maximum edge distance, the effective $h_{ef}$ need only be 8.00 in./1.5 = 5.33 to have the breakout cone area equal the column cross-sectional area. Based on the procedure in ACI 318, Section 17.6.2.1.2, this leads to:

$$h_{ef} = \max(c_{a,max}/1.5, y/3)$$

$$= \max(8.00 \text{ in.}/1.5, \ 4 \text{ in.}/3)$$

$$= \max(5.33 \text{ in.}, \ 1.33 \text{ in.})$$

$= 5.33$ in.

$$A_{Nc} = (1.5h_{ef} + s_1 + 1.5h_{ef})(1.5h_{ef} + s_2 + 1.5h_{ef})$$

$$= [1.5(5.33 \text{ in.}) + (4.00 \text{ in.}) + 1.5(5.33 \text{ in.})][1.5(5.33 \text{ in.}) + (4.00 \text{ in.}) + 1.5(5.33 \text{ in.})]$$

$= 400$ in.$^2$

$$A_{Nco} = 9h_{ef}^2$$ (ACI 318, Eq. 17.6.2.1.4)

$$= 9(5.33 \text{ in.})^2$$

$= 256$ in.$^2$

Because the tensile load is concentric with the anchor group, $e'_N = 0$ in.

$$\Psi_{ec,N} = \frac{1}{\left[1 + \frac{e'_N}{1.5h_{ef}}\right]} \leq 1$$ (ACI 318, Eq. 17.6.2.3.1)

$$= \frac{1}{\left[1 + \frac{0 \text{ in.}}{1.5(5.33 \text{ in.})}\right]} \leq 1$$

$= 1.00$

Because the edge distance equals $1.5h_{ef}$, the edge distance factor is calculated per ACI 318, Section 17.6.2.4.1, as:

$$\Psi_{ed,N} = 1.0$$

Because no analysis was performed, consider the concrete to be cracked at service load levels, use $\Psi_{c,N} = 1.0$, in accordance with ACI 318, Section 17.6.2.5.1(b).

For cast-in anchors, the factor representing breakout splitting is determined as $\Psi_{cp,N} = 1.0$ per ACI 318, Section 17.6.2.6.2.

From ACI 318, Section 17.6.2.2, $k_c = 24$ for cast-in anchors and for $h_{ef} < 11.0$ in.,

$$N_b = k_c\lambda_a\sqrt{f_c'h_{ef}}^{1.5}$$ (ACI 318, Eq. 17.6.2.2.1)

$$= (24)(1.0)\sqrt{4,000 \text{ psi}}(5.33 \text{ in.})^{1.5}\left(\frac{1 \text{ kip}}{1,000 \text{ lbf}}\right)$$

$= 18.7$ kips

---

AISC DESIGN GUIDE 1, 3rd EDITION / BASE CONNECTION DESIGN / 135

Downloaded by eva heo (mellowoutt28@gmail.com)

<!-- SOURCE: Page 146 -->

![Diagram showing anchor and reinforcement details for Example 4.7-15. The diagram includes:
- Top view showing a 20 in. × 20 in. concrete column with 4 anchor rods arranged in a 4" × 4" pattern, with 8" edge distances on all sides
- Side elevation showing the anchor rods extending through the column with embedment depth annotations
- Notation indicating ⅞" diameter ASTM F1554 Grade 36 anchor rods
- (2) #6 ASTM A615/A615M Grade 60 deformed bar anchor rod reinforcement in addition to reinforcement in the column (not shown)
- Concrete breakout plane indicated with dimension annotations
- Various dimensional annotations including embedment depths and spacings
- Plan view at bottom showing the 4-anchor arrangement with 6" spacing and reinforcement bar placement]

*Fig. 4-36. Anchor and reinforcement detailed in Example 4.7-15.*

---

136 / BASE CONNECTION DESIGN / AISC DESIGN GUIDE 1, 3rd EDITION

Downloaded by eva heo (mellowoutt28@gmail.com)

<!-- SOURCE: Page 147 -->

$$N_{cbg} = \frac{A_{Nc}}{A_{Nco}}\Psi_{ec,N}\Psi_{ed,N}\Psi_{c,N}\Psi_{cp,N}N_b$$ (ACI 318, Eq. 17.6.2.1b)

$$= \left(\frac{400 \text{ in.}^2}{256 \text{ in.}^2}\right)(1.0)(1.0)(1.0)(1.0)(18.7 \text{ kips})$$

$= 29.2$ kips

Because no supplementary reinforcement was specified, $\phi = 0.70$ per ACI 318, Table 17.5.3(b), and

$$\phi N_{cbg} = 0.70(29.2 \text{ kips})$$

$$= 20.4 \text{ kips} < 70.0 \text{ kips} \quad \textbf{n.g.}$$

Thus, it is necessary to transfer the anchor load to the column using anchor reinforcement.

*Determine the anchor reinforcement required to preclude concrete breakout in tension*

The required area of steel is determined according to ACI 318, Sections 17.5.2.1 and 17.5.3, as:

$$\phi = 0.75$$ (ACI 318, Section 17.5.3)

$$A_{s,req} = \frac{R_u}{\phi f_y}$$

$$= \frac{70.0 \text{ kips}}{0.75(60 \text{ ksi})}$$

$= 1.56$ in.$^2$

Use 4-#6 bars, and consider these bars are only being used and designed as anchor reinforcement.

$$A_s = (4 \text{ bars})\left(0.44 \frac{\text{in.}^2}{\text{bar}}\right)$$

$$= 1.76 \text{ in.}^2 > 1.56 \text{ in.}^2 \quad \textbf{o.k.}$$

With the bars located as shown in Figure 4-36, the horizontal distance, $g$, from the center of the anchor to the center of the reinforcing steel is determined by:

$$g = (2.00 \text{ in.})\sqrt{2}$$

$= 2.83$ in.

The reinforcing steel used as anchor reinforcement must be developed in accordance with ACI 318, Section 17.5.2.1(a), on both sides of the concrete breakout surface using the development length calculated per ACI 318, Chapter 25. The development length for hooks, $l_{dh}$, will be used above the breakout plane, and the development length for unhooked bars, $l_d$, will be used below the breakout plane.

For normal-weight concrete, and #6 ASTM A615/A615M Grade 60 uncoated, hooked reinforcement, with a center-to-center spacing greater than 6$d_b$ and side cover normal to the plane of the hook greater than or equal to 6$d_b$, the development factors are given in ACI 318, Table 25.4.3.2.

The basic development length for bars with standard hooks is then given by ACI 318, Section 25.4.3.1.

$$l_{dh} = \left(\frac{f_y\Psi_e\Psi_c\Psi_r\Psi_o}{55\lambda\sqrt{f_c'}}\right)d_b^{1.5}$$

$$\lambda = 1.0$$

$$\Psi_e = 1.0$$

$$\Psi_r = 1.0$$

---

AISC DESIGN GUIDE 1, 3rd EDITION / BASE CONNECTION DESIGN / 137

Downloaded by eva heo (mellowoutt28@gmail.com)

<!-- SOURCE: Page 148 -->

$$\Psi_o = 1.0$$

$$\Psi_c = \frac{f_c'}{15,000} + 0.6$$

$$= \frac{4,000 \text{ psi}}{15,000 \text{ psi}} + 0.6$$

$= 0.867$

Therefore,

$$l_{dh} = \left[\frac{(60,000 \text{psi})(1.0)(1.0)(1.0)(0.867)}{55(1.0)\sqrt{4,000 \text{ psi}}}\right](0.750 \text{ in.})^{1.5}$$

$= 9.71$ in.

The additional limits of ACI 318, Section 25.4.3.1, items (b) and (c), do not govern and are given by:

$$l_{dh} = 8d_b$$

$$= 8(0.750 \text{ in.})$$

$= 6.00$ in.

$$l_{dh} = 6.00 \text{ in.}$$

Therefore, the minimum required embedment length is illustrated in Figure 4-36 and calculated by:

$$h_{ef} = l_{dh} + g\left(\frac{1}{1.5}\right) + c_c$$

$$= 9.71 \text{ in} + (2.83 \text{ in.})\left(\frac{1}{1.5}\right) + 2.00 \text{ in.}$$

$= 13.6$ in.

Select a 14.0 in. embedment for the anchors.

For normal-weight concrete, with the effect of transverse reinforcement neglected, and #6 ASTM A615/A615M Grade 60 uncoated, vertical reinforcement, the development factors are given in ACI 318, Table 25.4.2.5.

The basic development length is then given by ACI 318-19(22), Section 25.4.2.4,

$$L_d = \left[\frac{3}{40}\frac{f_y}{\lambda\sqrt{f_c'}}\left(\frac{c_b + K_{tr}}{d_b}\right)\right]d_b$$ (ACI 318, Eq. 25.4.2.4a)

$$\lambda = 1.0$$

$$\Psi_s = 1.0$$

$$\Psi_g = 1.0$$

$$\Psi_e = 0.8$$

$$\Psi_t = 1.0$$

$$K_{tr} = 0$$

The confinement term based on the spacing and cover dimensions shown in Figure 4-36 is calculated by:

$$c_b = \min\left\{\begin{array}{l}6.00 \text{ in.},\\(2.00 \text{ in.} + 2.00 \text{ in.} + 2.00 \text{ in.} + 2.00 \text{ in.})/2\end{array}\right\}$$

$$= \min\left\{\begin{array}{l}6.00 \text{ in.},\\4.00 \text{ in.}\end{array}\right\}$$

$= 4.00$ in.

---

138 / BASE CONNECTION DESIGN / AISC DESIGN GUIDE 1, 3rd EDITION

Downloaded by eva heo (mellowoutt28@gmail.com)

<!-- SOURCE: Page 149 -->

$$\left(\frac{c_b + K_{tr}}{d_b}\right) = \left(\frac{4.00 \text{ in.} + 0}{0.750 \text{ in.}}\right) \leq 2.5$$

$$= 5.33 \leq 2.5$$

$= 2.5$

Therefore,

$$L_d = \left[\frac{3}{40}\left(\frac{60,000 \text{ psi}}{1.00\sqrt{4,000 \text{ psi}}}\right)\left(\frac{(1.0)(1.0)(0.8)(1.0)}{2.5}\right)\right](0.750 \text{ in.})$$

$= 17.1$ in.

The required development length may be reduced in accordance with ACI 318, Section 25.4.10, in cases where the requirements contained therein are satisfied. For this example, the prohibitions contained in ACI 318, Section 25.4.10.2, are not applicable. Therefore, a reduction in development length may be considered if the development length is not—in any case— reduced to less than 12 in. per ACI 318, Section 25.4.2.1(b).

$$l_e = l_d\frac{A_{s,required}}{A_{s,provided}}$$

$$= (17.1 \text{ in.})\left(\frac{1.56 \text{ in.}^2}{1.76 \text{ in.}^2}\right)$$

$$= 15.2 \text{ in.} > 12.0 \text{ in.} \quad \textbf{o.k.}$$

where $l_e$ is the effective steel reinforcement development length required below the potential concrete failure plane.

The total length of the anchor rod reinforcement can then be calculated based on $l_d$ and the dimensions shown in Figure 4-36 as:

$$l_{reinf} = h_{ef} - c_c - g\left(\frac{1}{1.5}\right) + l_e$$

$$= 14.0 \text{ in.} - 2.00 \text{ in.} - 2.83 \text{ in}\left(\frac{1}{1.5}\right) + 15.2 \text{ in.}$$

$= 25.3$ in.

Select a 26.0 in. length for the anchor rod reinforcement. The anchor reinforcement shown in Figure 4-36 is adequate to preclude the concrete breakout in tension.

*Confirm the anchorage concrete side face blowout capacity.*

$$h_{ef} = 14.0 \text{ in.}$$

$$c_{a1} = \left(\frac{20.0 \text{ in.} - 4.00 \text{ in.}}{2}\right)$$

$= 8.00$ in.

$$2.5c_{a1} = 2.5(8.00 \text{ in.})$$

$= 20.0$ in.

Because $h_{ef} < 2.5c_{a1}$, concrete side-face blowout is not applicable per ACI 318, Section 17.6.4.

---

AISC DESIGN GUIDE 1, 3rd EDITION / BASE CONNECTION DESIGN / 139

Downloaded by eva heo (mellowoutt28@gmail.com)

<!-- SOURCE: Page 150 -->

---

140 / BASE CONNECTION DESIGN / AISC DESIGN GUIDE 1, 3rd EDITION

Downloaded by eva heo (mellowoutt28@gmail.com)

