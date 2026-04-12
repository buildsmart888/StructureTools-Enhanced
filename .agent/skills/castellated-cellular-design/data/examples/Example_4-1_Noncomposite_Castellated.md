# Example 4.1: Noncomposite Castellated Beam

<!-- Consolidated from pages 51-70 -->


<!-- Page 51 -->

<!-- Page 51 -->

$$Z_{x-net} = 2A_{tee-crit}\frac{d_{eff-crit}}{2}$$ (from Eq. 4-11)

$$= 2\left(1.51\text{ in.}^2\right)\left(\frac{16.0\text{ in.}}{2}\right)$$

$$= 24.2\text{ in.}^3$$

*Beam gross section properties*

$$A_{gross} = A_{net} + D_o t_w$$ (4-23)

$$= 2.76\text{ in.}^2 + (12.3\text{ in.})(0.200\text{ in.})$$

$$= 5.22\text{ in.}^2$$

$$I_{x-gross} = I_{x-net} + \frac{t_w D_o^3}{12}$$ (4-24)

$$= 189\text{ in.}^4 + \frac{(0.200\text{ in.})(12.3\text{ in.})^3}{12}$$

$$= 220\text{ in.}^4$$

$$S_{x-gross} = \frac{I_{x-gross}}{\left(\frac{d_g}{2}\right)}$$ (4-14)

$$= \frac{220\text{ in.}^4}{\left(\frac{17.6\text{ in.}}{2}\right)}$$

$$= 25.0\text{ in.}^3$$

*Check Vierendeel bending*

The governing load cases are:

| LRFD | ASD |
|------|-----|
| Load case 1: | $w = D + L$ |
| $w = 1.4D$ | $= 139\text{ lb/ft} + 100\text{ lb/ft}$ |
| $= 1.4(139\text{ lb/ft})$ | $= 239\text{ lb/ft}$ |
| $= 195\text{ lb/ft}$ | |
| Load case 2: | |
| $w = 1.2D + 1.6L$ | |
| $= 1.2(139\text{ lb/ft}) + 1.6(100\text{ lb/ft})$ | |
| $= 327\text{ lb/ft}$ **governs** | |

Calculate global shear and moment at each opening to be used to calculate local internal forces (axial and flexural) at each opening. The results are presented in Table 4-9.

Calculate the axial force and Vierendeel moment in the top and bottom tees resulting from the global shear and global moment, respectively. The results are shown in Table 4-10.

Local axial force:

$$P_r = \frac{M_r}{d_{eff-crit}}$$ (from Eq. 3-1)


*44 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*



<!-- Page 52 -->

<!-- Page 52 -->

| Table 4-9. Global Shear and Moment at Each Opening |
|-----------------------------------------------------|

<table>
<tr>
<th rowspan="2">Opening<br>No.</th>
<th rowspan="2">X<sub>n</sub><br>ft</th>
<th colspan="4">Global Shear</th>
<th colspan="4">Global Moment</th>
</tr>
<tr>
<th>D<sub>s</sub><br>kips</th>
<th>L<sub>s</sub><br>kips</th>
<th colspan="2">V<sub>r</sub><br>kips</th>
<th>D<sub>s</sub><br>kip-ft</th>
<th>L<sub>s</sub><br>kip-ft</th>
<th colspan="2">M<sub>r</sub><br>kip-ft</th>
</tr>
<tr>
<th></th>
<th></th>
<th></th>
<th></th>
<th>ASD</th>
<th>LRFD</th>
<th></th>
<th></th>
<th>ASD</th>
<th>LRFD</th>
</tr>
<tr>
<td>End</td>
<td>0.00</td>
<td>2.78</td>
<td>2.00</td>
<td>4.78</td>
<td>6.54</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
<td>0.00</td>
</tr>
<tr>
<td>1</td>
<td>0.885</td>
<td>2.66</td>
<td>1.91</td>
<td>4.57</td>
<td>6.25</td>
<td>2.41</td>
<td>1.73</td>
<td>4.14</td>
<td>5.66</td>
</tr>
<tr>
<td>2</td>
<td>2.28</td>
<td>2.46</td>
<td>1.77</td>
<td>4.24</td>
<td>5.79</td>
<td>5.98</td>
<td>4.30</td>
<td>10.3</td>
<td>14.1</td>
</tr>
<tr>
<td>3</td>
<td>3.68</td>
<td>2.27</td>
<td>1.63</td>
<td>3.90</td>
<td>5.33</td>
<td>9.28</td>
<td>6.68</td>
<td>16.0</td>
<td>21.8</td>
</tr>
<tr>
<td>4</td>
<td>5.07</td>
<td>2.08</td>
<td>1.49</td>
<td>3.57</td>
<td>4.88</td>
<td>12.3</td>
<td>8.86</td>
<td>21.2</td>
<td>29.0</td>
</tr>
<tr>
<td>5</td>
<td>6.47</td>
<td>1.88</td>
<td>1.35</td>
<td>3.23</td>
<td>4.42</td>
<td>15.1</td>
<td>10.8</td>
<td>25.9</td>
<td>35.4</td>
</tr>
<tr>
<td>6</td>
<td>7.87</td>
<td>1.69</td>
<td>1.21</td>
<td>2.90</td>
<td>3.97</td>
<td>17.6</td>
<td>12.6</td>
<td>30.2</td>
<td>41.3</td>
</tr>
<tr>
<td>7</td>
<td>9.26</td>
<td>1.49</td>
<td>1.07</td>
<td>2.57</td>
<td>3.51</td>
<td>19.8</td>
<td>14.2</td>
<td>34.0</td>
<td>46.5</td>
</tr>
<tr>
<td>8</td>
<td>10.7</td>
<td>1.30</td>
<td>0.934</td>
<td>2.23</td>
<td>3.05</td>
<td>21.7</td>
<td>15.6</td>
<td>37.4</td>
<td>51.1</td>
</tr>
<tr>
<td>9</td>
<td>12.1</td>
<td>1.11</td>
<td>0.795</td>
<td>1.90</td>
<td>2.60</td>
<td>23.4</td>
<td>16.8</td>
<td>40.3</td>
<td>55.0</td>
</tr>
<tr>
<td>10</td>
<td>13.4</td>
<td>0.911</td>
<td>0.655</td>
<td>1.57</td>
<td>2.14</td>
<td>24.8</td>
<td>17.9</td>
<td>42.7</td>
<td>58.3</td>
</tr>
<tr>
<td>11</td>
<td>14.8</td>
<td>0.717</td>
<td>0.516</td>
<td>1.23</td>
<td>1.69</td>
<td>26.0</td>
<td>18.7</td>
<td>44.6</td>
<td>61.0</td>
</tr>
<tr>
<td>12</td>
<td>16.2</td>
<td>0.523</td>
<td>0.376</td>
<td>0.899</td>
<td>1.23</td>
<td>26.8</td>
<td>19.3</td>
<td>46.1</td>
<td>63.0</td>
</tr>
<tr>
<td>13</td>
<td>17.6</td>
<td>0.329</td>
<td>0.236</td>
<td>0.565</td>
<td>0.773</td>
<td>27.4</td>
<td>19.7</td>
<td>47.1</td>
<td>64.4</td>
</tr>
<tr>
<td>14</td>
<td>19.0</td>
<td>0.135</td>
<td>0.097</td>
<td>0.232</td>
<td>0.317</td>
<td>27.7</td>
<td>20.0</td>
<td>47.7</td>
<td>65.2</td>
</tr>
<tr>
<td>Bm. CL</td>
<td>20.0</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>27.8</td>
<td>20.0</td>
<td>47.8</td>
<td>65.4</td>
</tr>
</table>

Local Vierendeel moment:

$$M_{vr} = \frac{V_r}{2}\left(\frac{D_o}{4}\right)$$ (from Eq. 3-3)

*Calculate the available shear and flexural strength of top and bottom tees at critical section*

Determine the limiting flange width-to-thickness ratio from AISC *Specification* Table B4.1b, Case 10:

$$\lambda_p = 0.38\sqrt{\frac{E}{F_y}}$$

$$= 0.75\sqrt{\frac{29,000\text{ ksi}}{50\text{ ksi}}}$$

$$= 9.15$$

$$\lambda = \frac{b}{t}$$

$$= \frac{b_f}{2t_f}$$

$$= \frac{3.97\text{ in.}}{2(0.225\text{ in.})}$$

$$= 8.82 < 9.15$$

Because $\lambda < \lambda_p$, the flanges of the tee are compact; therefore, it is not necessary to check flange local buckling when calculating the available flexural strength.


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 45*



<!-- Page 53 -->

<!-- Page 53 -->

| Table 4-10. Local Axial Force and Vierendeel Moment at Each Opening |
|----------------------------------------------------------------------|

<table>
<tr>
<th rowspan="2">Opening<br>No.</th>
<th rowspan="2">X<sub>n</sub><br>ft</th>
<th colspan="4">Axial Forces</th>
<th colspan="4">Vierendeel Moments</th>
</tr>
<tr>
<th colspan="2">Global Moment<br>M<sub>r</sub><br>kip-ft</th>
<th colspan="2">Local Axial Force<br>P<sub>r</sub><br>kips</th>
<th colspan="2">Global Shear<br>V<sub>r</sub><br>kips</th>
<th colspan="2">Local Vierendeel Moment<br>M<sub>vr</sub><br>kip-in.</th>
</tr>
<tr>
<th></th>
<th></th>
<th>ASD</th>
<th>LRFD</th>
<th>ASD</th>
<th>LRFD</th>
<th>ASD</th>
<th>LRFD</th>
<th>ASD</th>
<th>LRFD</th>
</tr>
<tr>
<td>End</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>4.78</td>
<td>6.54</td>
<td>7.35</td>
<td>10.1</td>
</tr>
<tr>
<td>1</td>
<td>0.885</td>
<td>4.14</td>
<td>5.66</td>
<td>3.10</td>
<td>4.24</td>
<td>4.57</td>
<td>6.25</td>
<td>7.00</td>
<td>9.57</td>
</tr>
<tr>
<td>2</td>
<td>2.28</td>
<td>10.3</td>
<td>14.1</td>
<td>7.71</td>
<td>10.5</td>
<td>4.24</td>
<td>5.79</td>
<td>6.49</td>
<td>8.87</td>
</tr>
<tr>
<td>3</td>
<td>3.68</td>
<td>16.0</td>
<td>21.8</td>
<td>12.0</td>
<td>16.4</td>
<td>3.90</td>
<td>5.33</td>
<td>5.97</td>
<td>8.17</td>
</tr>
<tr>
<td>4</td>
<td>5.07</td>
<td>21.2</td>
<td>29.0</td>
<td>15.9</td>
<td>21.7</td>
<td>3.57</td>
<td>4.88</td>
<td>5.46</td>
<td>7.47</td>
</tr>
<tr>
<td>5</td>
<td>6.47</td>
<td>25.9</td>
<td>35.4</td>
<td>19.4</td>
<td>26.6</td>
<td>3.23</td>
<td>4.42</td>
<td>4.95</td>
<td>6.77</td>
</tr>
<tr>
<td>6</td>
<td>7.87</td>
<td>30.2</td>
<td>41.3</td>
<td>22.6</td>
<td>31.0</td>
<td>2.90</td>
<td>3.97</td>
<td>4.44</td>
<td>6.07</td>
</tr>
<tr>
<td>7</td>
<td>9.26</td>
<td>34.0</td>
<td>46.5</td>
<td>25.5</td>
<td>34.9</td>
<td>2.57</td>
<td>3.51</td>
<td>3.93</td>
<td>5.37</td>
</tr>
<tr>
<td>8</td>
<td>10.7</td>
<td>37.4</td>
<td>51.1</td>
<td>28.0</td>
<td>38.3</td>
<td>2.23</td>
<td>3.05</td>
<td>3.42</td>
<td>4.68</td>
</tr>
<tr>
<td>9</td>
<td>12.1</td>
<td>40.3</td>
<td>55.0</td>
<td>30.2</td>
<td>41.3</td>
<td>1.90</td>
<td>2.60</td>
<td>2.91</td>
<td>3.98</td>
</tr>
<tr>
<td>10</td>
<td>13.4</td>
<td>42.7</td>
<td>58.3</td>
<td>32.0</td>
<td>43.7</td>
<td>1.57</td>
<td>2.14</td>
<td>2.40</td>
<td>3.28</td>
</tr>
<tr>
<td>11</td>
<td>14.8</td>
<td>44.6</td>
<td>61.0</td>
<td>33.5</td>
<td>45.7</td>
<td>1.23</td>
<td>1.69</td>
<td>1.89</td>
<td>2.58</td>
</tr>
<tr>
<td>12</td>
<td>16.2</td>
<td>46.1</td>
<td>63.0</td>
<td>34.6</td>
<td>47.3</td>
<td>0.899</td>
<td>1.23</td>
<td>1.38</td>
<td>1.88</td>
</tr>
<tr>
<td>13</td>
<td>17.6</td>
<td>47.1</td>
<td>64.4</td>
<td>35.3</td>
<td>48.3</td>
<td>0.565</td>
<td>0.773</td>
<td>0.865</td>
<td>1.18</td>
</tr>
<tr>
<td>14</td>
<td>19.0</td>
<td>47.7</td>
<td>65.2</td>
<td>35.8</td>
<td>48.9</td>
<td>0.232</td>
<td>0.317</td>
<td>0.355</td>
<td>0.485</td>
</tr>
<tr>
<td>Bm. CL</td>
<td>20.0</td>
<td>47.8</td>
<td>65.4</td>
<td>35.8</td>
<td>49.0</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
<td>0.000</td>
</tr>
</table>

Determine the limiting stem width-to-thickness ratio, $\lambda_s$, from AISC *Specification* Table B4.1a, Case 4:

$$\lambda_r = 0.75\sqrt{\frac{E}{F_y}}$$

$$= 0.75\sqrt{\frac{29,000\text{ ksi}}{50\text{ ksi}}}$$

$$= 18.1$$

$$\lambda = \frac{d_{t-crit}}{t_w}$$

$$= \frac{3.31\text{ in.}}{0.200\text{ in.}}$$

$$= 16.6 < 18.1$$

Because $\lambda < \lambda_r$, the tee stem is nonslender; therefore, it is not necessary to consider AISC *Specification* Section E7 when calculating the available compressive strength.

*Calculate available axial (compression) strength of tee*

*Flexural buckling*

Determine which $L_c/r$ ratio controls

From Section 3.2.2.1, $L = D_o/2$ for cellular beams.


*46 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*



<!-- Page 54 -->

<!-- Page 54 -->

$$\frac{L_c}{r_x} = \frac{K_x\left(D_o/2\right)}{r_x}$$

$$= \frac{0.65(6.15\text{ in.})}{1.00\text{ in.}}$$

$$= 4.00$$

$$\frac{L_c}{r_y} = \frac{K_y\left(D_o/2\right)}{r_y}$$

$$= \frac{1.0(6.15\text{ in.})}{0.881\text{ in.}}$$

$$= 6.98$$ **governs**

Calculate the elastic buckling stress, $F_e$, from AISC *Specification* Section E3:

$$F_e = \frac{\pi^2 E}{\left(\frac{L_c}{r}\right)^2}$$ (*Spec.* Eq. E3-4)

$$= \frac{\pi^2(29,000\text{ ksi})}{(6.98)^2}$$

$$= 5,870\text{ ksi}$$

From AISC *Specification* Section E3:

$$4.71\sqrt{\frac{E}{F_y}} = 4.71\sqrt{\frac{29,000\text{ ksi}}{50\text{ ksi}}}$$

$$= 113$$

Because, $\frac{L_c}{r} = 6.98 < 113$, AISC *Specification* Equation E3-2 is used to calculate $F_{cr}$:

$$F_{cr} = \left(0.658^{\frac{F_y}{F_e}}\right)F_y$$ (*Spec.* Eq. E3-2)

$$= \left[0.658^{\left(\frac{50\text{ ksi}}{5,870\text{ ksi}}\right)}\right]50\text{ ksi}$$

$$= 49.8\text{ ksi}$$

$$P_n = F_{cr}A_{tee-crit}$$ (from *Spec.* Eq. E3-1)

$$= (49.8\text{ ksi})(1.51\text{ in.}^2)$$

$$= 75.2\text{ kips}$$

*Flexural-torsional buckling*

The nominal compressive strength is determined based on the limit state of flexural-torsional buckling using AISC *Specification* Equation E4-1:

$$P_n = F_{cr}A_{tee-crit}$$ (from *Spec.* Eq. E4-1)

The critical stress, $F_{cr}$, is determined according to AISC *Specification* Equation E3-2, using the torsional or flexural-torsional elastic buckling stress, $F_e$, determined from:


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 47*



<!-- Page 55 -->

<!-- Page 55 -->

$$F_e = \left(\frac{F_{ey} + F_{ez}}{2H}\right)\left[1 - \sqrt{1 - \frac{4F_{ey}F_{ez}H}{(F_{ey} + F_{ez})^2}}\right]$$ (*Spec.* Eq. E4-3)

$$F_{ey} = \frac{\pi^2 E}{\left(\frac{L_{cy}}{r_y}\right)^2}$$ (*Spec.* Eq. E4-6)

$$= \frac{\pi^2(29,000\text{ ksi})}{\left(\frac{6.15\text{ in.}}{0.881\text{ in.}}\right)^2}$$

$$= 5,870\text{ ksi}$$

$$F_{ez} = \left[\frac{\pi^2 EC_w}{(L_{cz})^2} + GJ\right]\frac{1}{A_{tee-crit}\bar{r}_o^2}$$ (from *Spec.* Eq. E4-7)

From the User Note in AISC *Specification* Section E4, for tees, $C_w$ is omitted when calculating $F_{ez}$ and $x_o$ is taken as 0.

$$\bar{r}_o^2 = x_o^2 + y_o^2 + \frac{I_x + I_y}{A_e}$$ (*Spec.* Eq. E4-9)

$$= y_o^2 + \frac{I_{x-tee-crit} + I_y}{A_{tee-crit}}$$

$$= (2.42\text{ in.})^2 + \frac{1.52\text{ in.}^4 + 1.18\text{ in.}^4}{1.51\text{ in.}^2}$$

$$= 7.64\text{ in.}^2$$

$$F_{ez} = \left[\frac{\pi^2(29,000\text{ ksi})}{(6.15\text{ in.})^2} + (11,200\text{ ksi})(0.023\text{ in.}^4)\right]\frac{1}{(1.51\text{ in.}^2)(7.64\text{ in.}^2)}$$

$$= 678\text{ ksi}$$

$$H = 1 - \frac{x_o^2 + y_o^2}{\bar{r}_o^2}$$ (*Spec.* Eq. E4-8)

$$= 1 - \frac{(2.42\text{ in.})^2}{7.65\text{ in.}^2}$$

$$= 0.233$$

$$F_e = \left[\frac{5,870\text{ ksi} + 678\text{ ksi}}{2(0.233)}\right]\left[1 - \sqrt{1 - \frac{4(5,870\text{ ksi})(678\text{ ksi})(0.233)}{(5,870\text{ ksi} + 678\text{ ksi})^2}}\right]$$

$$= 622\text{ ksi}$$

$$F_{cr} = \left(0.658^{\frac{F_y}{F_e}}\right)F_y$$ (*Spec.* Eq. E3-2)

$$= \left(0.658^{\frac{50\text{ ksi}}{622\text{ ksi}}}\right)(50\text{ ksi})$$

$$= 48.3\text{ ksi}$$

$$P_n = F_{cr}A_{tee-crit}$$

$$= (48.3\text{ ksi})(1.51\text{ in.}^2)$$

$$= 72.9\text{ kips}$$


*48 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*



<!-- Page 56 -->

<!-- Page 56 -->

The available compressive strength of the tee is:

| LRFD | ASD |
|------|-----|
| From Table 4-10, | From Table 4-10, |
| $P_r = 49.0\text{ kips}$ | $P_r = 35.8\text{ kips}$ |
| $P_n = \phi_c P_n$ | $P_n = \frac{P_n}{\Omega_c}$ |
| $= 0.90(72.9\text{ kips})$ | $= \frac{72.9\text{ kips}}{1.67}$ |
| $= 65.6\text{ kips} > 49.0\text{ kips}$ **o.k.** | $= 43.7\text{ kips} > 35.8\text{ kips}$ **o.k.** |

*Calculate available flexural strength of tee*

*Yielding*

Yielding of the tee with the stem in compression is calculated using AISC *Specification* Section F9.1

$$M_n = M_y$$ (*Spec.* Eq. F9-4)

$$M_y = F_y S_{x-bot}$$ (from *Spec.* Eq. F9-3)

$$= (50\text{ ksi})(0.598\text{ in.}^3)$$

$$= 29.9\text{ kip-in.}$$

*Lateral-torsional buckling*

Because $L_b = 0$, the limit state of lateral-torsional buckling does not apply.

*Flange local buckling*

Per AISC *Specification* Section F9.3(a), the limit state of flange local buckling does not apply because the flange is compact.

*Local buckling of tee stems*

The nominal flexural strength for local buckling of the tee stem in flexural compression , $M_n$, is determined using AISC *Specification* Section F9.4:

$$M_n = F_{cr}S_x$$ (*Spec.* Eq. F9-16)

Because $d/t_w < 0.84\sqrt{\frac{E}{F_y}}$, the critical stress, $F_{cr}$, is determined using AISC *Specification* Equation F9-17:

$$F_{cr} = F_y$$

And thus,

$$M_n = (50\text{ ksi})(0.598\text{ in.}^3)$$

$$= 29.9\text{ kip-in.}$$


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 49*



<!-- Page 57 -->

<!-- Page 57 -->

The available flexural strength of the tee is:

| LRFD | ASD |
|------|-----|
| From Table 4-10, | From Table 4-10, |
| $M_{vr} = 8.17\text{ kip-in.}$ | $M_{vr} = 5.97\text{ kip-in.}$ |
| $M_n = \phi_b M_n$ | $M_n = \frac{M_n}{\Omega_b}$ |
| $= 0.90(29.9\text{ kip-in.})$ | $= \frac{29.9\text{ kip-in.}}{1.67}$ |
| $= 26.9\text{ kip-in.} > 8.17\text{ kip-in.}$ **o.k.** | $= 17.9\text{ kip-in.} > 5.97\text{ kip-in.}$ **o.k.** |

*Check tees for combined axial and flexural loads*

LRFD results are presented in Table 4-11, and the ASD results are presented in Table 4-12.

From Tables 4-11 and 4-12, the Vierendeel bending is summarized as follows:

| LRFD | ASD |
|------|-----|
| $I_{max} = 0.759 < 1.0$ **o.k.** | $I_{max} = 0.835 < 1.0$ **o.k.** |

*Check web post buckling*

From Section 3.4.2, use Equation 3-30 to calculate the horizontal shear, $V_{eh}$:

$$V_{eh} = \left|T_{t(x)} - T_{t(x+1)}\right|$$ (3-30)

Table 4-13 presents the horizontal shear at each gross section for web post buckling.

*Calculate web post buckling flexural strength*

From Section 3.4.2, use Equation 3-31 to calculate the required flexural strength in the web post.

| LRFD | ASD |
|------|-----|
| From Table 4-13, | From Table 4-13, |
| $V_{eh} = 6.26\text{ kips}$ | $V_{eh} = 4.61\text{ kips}$ |
| $M_u = 0.90\frac{D_o}{2}V_{eh}$ (3-31) | $M_a = 0.90\frac{D_o}{2}V_{eh}$ (3-31) |
| $= 0.90\left(\frac{12.3\text{ in.}}{2}\right)(6.26\text{ kips})$ | $= 0.90\left(\frac{12.3\text{ in.}}{2}\right)(4.61\text{ kips})$ |
| $= 34.6\text{ kip-in.}$ | $= 25.5\text{ kip-in.}$ |

*Calculate available flexural strength of web post*

From Section 3.4.2, use Equation 3-32 to calculate the elastic moment, $M_e$:

$$M_e = \frac{t_w(S - D_o + 0.564D_o)^2}{6}F_y$$ (3-32)

$$= \frac{(0.200\text{ in.})[16.8\text{ in.} - 12.3\text{ in.} + 0.564(12.3\text{ in.})]^2}{6}(50\text{ ksi})$$

$$= 218\text{ kip-in.}$$


*50 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*



<!-- Page 58 -->

<!-- Page 58 -->

<table>
<tr>
<th colspan="13">Table 4-11. LRFD Interaction Check</th>
</tr>
<tr>
<th rowspan="2">Opening<br>No.</th>
<th rowspan="2">X<sub>n</sub><br>ft</th>
<th colspan="3">Local Forces on Tee</th>
<th colspan="3">LRFD Interaction Check</th>
<th colspan="5"></th>
</tr>
<tr>
<th>P<sub>r</sub><br>kips</th>
<th>M<sub>vr-in.</sub><br>kip-in.</th>
<th>P<sub>r</sub>/P<sub>n</sub></th>
<th>M1-14</th>
<th>M1-1b</th>
<th>Interaction*</th>
</tr>
<tr>
<td>End</td>
<td>0.000</td>
<td>0.000</td>
<td>10.1</td>
<td>0.000</td>
<td>0.376</td>
<td>0.000</td>
<td>0.000</td>
</tr>
<tr>
<td>1</td>
<td>0.885</td>
<td>4.24</td>
<td>9.57</td>
<td>0.065</td>
<td>0.356</td>
<td>0.387</td>
<td>0.387</td>
</tr>
<tr>
<td>2</td>
<td>2.28</td>
<td>10.5</td>
<td>8.87</td>
<td>0.155</td>
<td>0.448</td>
<td>0.407</td>
<td>0.407</td>
</tr>
<tr>
<td>3</td>
<td>3.68</td>
<td>16.4</td>
<td>8.17</td>
<td>0.241</td>
<td>0.611</td>
<td>0.524</td>
<td>0.611</td>
</tr>
<tr>
<td>4</td>
<td>5.07</td>
<td>21.7</td>
<td>7.47</td>
<td>0.318</td>
<td>0.719</td>
<td>0.596</td>
<td>0.719</td>
</tr>
<tr>
<td>5</td>
<td>6.47</td>
<td>26.6</td>
<td>6.77</td>
<td>0.391</td>
<td>0.615</td>
<td>0.447</td>
<td>0.615</td>
</tr>
<tr>
<td>6</td>
<td>7.87</td>
<td>31.0</td>
<td>6.07</td>
<td>0.456</td>
<td>0.667</td>
<td>0.404</td>
<td>0.667</td>
</tr>
<tr>
<td>7</td>
<td>9.26</td>
<td>34.9</td>
<td>5.37</td>
<td>0.513</td>
<td>0.719</td>
<td>0.457</td>
<td>0.719</td>
</tr>
<tr>
<td>8</td>
<td>10.7</td>
<td>38.3</td>
<td>4.68</td>
<td>0.564</td>
<td>0.719</td>
<td>0.506</td>
<td>0.719</td>
</tr>
<tr>
<td>9</td>
<td>12.1</td>
<td>41.3</td>
<td>3.98</td>
<td>0.608</td>
<td>0.759</td>
<td>0.452</td>
<td>0.759</td>
</tr>
<tr>
<td>10</td>
<td>13.4</td>
<td>43.7</td>
<td>3.28</td>
<td>0.644</td>
<td>0.753</td>
<td>0.444</td>
<td>0.753</td>
</tr>
<tr>
<td>11</td>
<td>14.8</td>
<td>45.7</td>
<td>2.58</td>
<td>0.671</td>
<td>0.759</td>
<td>0.433</td>
<td>0.759</td>
</tr>
<tr>
<td>12</td>
<td>16.2</td>
<td>47.3</td>
<td>1.88</td>
<td>0.694</td>
<td>0.744</td>
<td>0.385</td>
<td>0.744</td>
</tr>
<tr>
<td>13</td>
<td>17.6</td>
<td>48.3</td>
<td>1.18</td>
<td>0.712</td>
<td>0.734</td>
<td>0.400</td>
<td>0.734</td>
</tr>
<tr>
<td>14</td>
<td>19.0</td>
<td>48.9</td>
<td>0.485</td>
<td>0.720</td>
<td>0.738</td>
<td>0.378</td>
<td>0.738</td>
</tr>
<tr>
<td>Bm. CL</td>
<td>20.0</td>
<td>49.0</td>
<td>0.000</td>
<td>0.720</td>
<td>0.720</td>
<td>0.360</td>
<td>0.720</td>
</tr>
<tr>
<td colspan="11">*Reflects H1-1a limit state of eccentric loading condition</td>
<td colspan="2">I<sub>max</sub> = <b>0.759</b></td>
</tr>
</table>

<table>
<tr>
<th colspan="13">Table 4-12. ASD Interaction Check</th>
</tr>
<tr>
<th rowspan="2">Opening<br>No.</th>
<th rowspan="2">X<sub>n</sub><br>ft</th>
<th colspan="3">Local Forces on Tee</th>
<th colspan="3">ASD Interaction Check</th>
<th colspan="5"></th>
</tr>
<tr>
<th>P<sub>r</sub><br>kips</th>
<th>M<sub>vr-in.</sub><br>kip-in.</th>
<th>P<sub>r</sub>/P<sub>n</sub></th>
<th>H1-1a</th>
<th>H1-1b</th>
<th>Interaction*</th>
</tr>
<tr>
<td>End</td>
<td>0.000</td>
<td>0.000</td>
<td>7.35</td>
<td>0.000</td>
<td>0.410</td>
<td>0.000</td>
<td>0.000</td>
</tr>
<tr>
<td>1</td>
<td>0.885</td>
<td>3.10</td>
<td>7.00</td>
<td>0.071</td>
<td>0.426</td>
<td>0.426</td>
<td>0.426</td>
</tr>
<tr>
<td>2</td>
<td>2.28</td>
<td>7.71</td>
<td>6.51</td>
<td>0.171</td>
<td>0.564</td>
<td>0.449</td>
<td>0.549</td>
</tr>
<tr>
<td>3</td>
<td>3.68</td>
<td>12.0</td>
<td>6.00</td>
<td>0.265</td>
<td>0.563</td>
<td>0.405</td>
<td>0.563</td>
</tr>
<tr>
<td>4</td>
<td>5.07</td>
<td>15.9</td>
<td>5.46</td>
<td>0.350</td>
<td>0.655</td>
<td>0.500</td>
<td>0.655</td>
</tr>
<tr>
<td>5</td>
<td>6.47</td>
<td>19.4</td>
<td>4.97</td>
<td>0.420</td>
<td>0.677</td>
<td>0.493</td>
<td>0.677</td>
</tr>
<tr>
<td>6</td>
<td>7.87</td>
<td>22.6</td>
<td>4.45</td>
<td>0.492</td>
<td>0.723</td>
<td>0.500</td>
<td>0.723</td>
</tr>
<tr>
<td>7</td>
<td>9.26</td>
<td>25.5</td>
<td>3.97</td>
<td>0.558</td>
<td>0.780</td>
<td>0.500</td>
<td>0.780</td>
</tr>
<tr>
<td>8</td>
<td>10.7</td>
<td>28.0</td>
<td>3.42</td>
<td>0.622</td>
<td>0.814</td>
<td>0.502</td>
<td>0.814</td>
</tr>
<tr>
<td>9</td>
<td>12.1</td>
<td>30.2</td>
<td>2.91</td>
<td>0.670</td>
<td>0.835</td>
<td>0.497</td>
<td>0.835</td>
</tr>
<tr>
<td>10</td>
<td>13.4</td>
<td>32.0</td>
<td>2.43</td>
<td>0.707</td>
<td>0.838</td>
<td>0.489</td>
<td>0.838</td>
</tr>
<tr>
<td>11</td>
<td>14.8</td>
<td>33.5</td>
<td>1.91</td>
<td>0.742</td>
<td>0.835</td>
<td>0.477</td>
<td>0.835</td>
</tr>
<tr>
<td>12</td>
<td>16.2</td>
<td>34.6</td>
<td>1.40</td>
<td>0.765</td>
<td>0.843</td>
<td>0.455</td>
<td>0.843</td>
</tr>
<tr>
<td>13</td>
<td>17.6</td>
<td>35.3</td>
<td>0.882</td>
<td>0.782</td>
<td>0.830</td>
<td>0.440</td>
<td>0.830</td>
</tr>
<tr>
<td>14</td>
<td>19.0</td>
<td>35.8</td>
<td>0.360</td>
<td>0.792</td>
<td>0.810</td>
<td>0.416</td>
<td>0.810</td>
</tr>
<tr>
<td>Bm. CL</td>
<td>20.0</td>
<td>35.8</td>
<td>0.000</td>
<td>0.794</td>
<td>0.794</td>
<td>0.397</td>
<td>0.794</td>
</tr>
<tr>
<td colspan="11">*Reflects H1-1a limit state of eccentric loading condition</td>
<td colspan="2">I<sub>max</sub> = <b>0.835</b></td>
</tr>
</table>


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 51*



<!-- Page 59 -->

<!-- Page 59 -->

| Table 4-13. ASD and LRFD Web Post Buckling Check |
|---------------------------------------------------|

<table>
<tr>
<th rowspan="2">Post<br>No.</th>
<th rowspan="2">X<sub>n</sub><br>ft</th>
<th colspan="3">ASD</th>
<th colspan="3">LRFD</th>
</tr>
<tr>
<th>T<sub>r(1)s</sub><br>kips</th>
<th>T<sub>r(1+1)s</sub><br>kips</th>
<th>V<sub>ehs</sub><br>kips</th>
<th>T<sub>r(1)s</sub><br>kips</th>
<th>T<sub>r(1+1)s</sub><br>kips</th>
<th>V<sub>ehs</sub><br>kips</th>
</tr>
<tr>
<td>1</td>
<td>1.58</td>
<td>3.10</td>
<td>7.71</td>
<td>4.61</td>
<td>10.5</td>
<td>4.24</td>
<td>6.26</td>
</tr>
<tr>
<td>2</td>
<td>2.98</td>
<td>7.71</td>
<td>12.0</td>
<td>4.29</td>
<td>16.4</td>
<td>10.5</td>
<td>5.90</td>
</tr>
<tr>
<td>3</td>
<td>4.38</td>
<td>12.0</td>
<td>15.9</td>
<td>3.90</td>
<td>21.7</td>
<td>16.4</td>
<td>5.30</td>
</tr>
<tr>
<td>4</td>
<td>5.77</td>
<td>15.9</td>
<td>19.4</td>
<td>3.50</td>
<td>26.6</td>
<td>21.7</td>
<td>4.90</td>
</tr>
<tr>
<td>5</td>
<td>7.17</td>
<td>19.4</td>
<td>22.6</td>
<td>3.30</td>
<td>31.0</td>
<td>26.6</td>
<td>4.40</td>
</tr>
<tr>
<td>6</td>
<td>8.56</td>
<td>22.6</td>
<td>25.5</td>
<td>2.80</td>
<td>34.9</td>
<td>31.0</td>
<td>3.90</td>
</tr>
<tr>
<td>7</td>
<td>9.96</td>
<td>25.5</td>
<td>28.0</td>
<td>2.50</td>
<td>38.3</td>
<td>34.9</td>
<td>3.40</td>
</tr>
<tr>
<td>8</td>
<td>11.4</td>
<td>28.0</td>
<td>30.2</td>
<td>2.20</td>
<td>41.3</td>
<td>38.3</td>
<td>3.00</td>
</tr>
<tr>
<td>9</td>
<td>12.8</td>
<td>30.2</td>
<td>32.0</td>
<td>1.60</td>
<td>43.7</td>
<td>41.3</td>
<td>2.40</td>
</tr>
<tr>
<td>10</td>
<td>14.1</td>
<td>32.0</td>
<td>33.5</td>
<td>1.50</td>
<td>45.7</td>
<td>43.7</td>
<td>2.00</td>
</tr>
<tr>
<td>11</td>
<td>15.5</td>
<td>33.5</td>
<td>34.6</td>
<td>1.20</td>
<td>47.3</td>
<td>45.7</td>
<td>1.60</td>
</tr>
<tr>
<td>12</td>
<td>16.9</td>
<td>34.6</td>
<td>35.3</td>
<td>0.700</td>
<td>48.3</td>
<td>47.3</td>
<td>1.00</td>
</tr>
<tr>
<td>13</td>
<td>18.3</td>
<td>35.3</td>
<td>35.8</td>
<td>0.500</td>
<td>48.9</td>
<td>48.3</td>
<td>0.600</td>
</tr>
<tr>
<td>14</td>
<td>19.7</td>
<td>35.8</td>
<td>35.8</td>
<td>0.000</td>
<td>49.0</td>
<td>48.9</td>
<td>0.100</td>
</tr>
<tr>
<td colspan="5">Maximum</td>
<td>4.61</td>
<td colspan="2">Maximum</td>
<td>6.26</td>
</tr>
</table>

$$C1 = 5.097 + 0.1464\left(\frac{D_o}{t_w}\right) - 0.00174\left(\frac{D_o}{t_w}\right)^2$$ (3-33)

$$= 5.097 + 0.1464\left(\frac{12.3\text{ in.}}{0.200\text{ in.}}\right) - 0.00174\left(\frac{12.3\text{ in.}}{0.200\text{ in.}}\right)^2$$

$$= 7.54$$

$$C2 = 1.441 + 0.0625\left(\frac{D_o}{t_w}\right) - 0.000683\left(\frac{D_o}{t_w}\right)^2$$ (3-34)

$$= 1.441 + 0.0625\left(\frac{12.3\text{ in.}}{0.200\text{ in.}}\right) - 0.000683\left(\frac{12.3\text{ in.}}{0.200\text{ in.}}\right)^2$$

$$= 2.70$$

$$C3 = 3.645 + 0.0853\left(\frac{D_o}{t_w}\right) - 0.00108\left(\frac{D_o}{t_w}\right)^2$$ (3-35)

$$= 3.645 + 0.0853\left(\frac{12.3\text{ in.}}{0.200\text{ in.}}\right) - 0.00108\left(\frac{12.3\text{ in.}}{0.200\text{ in.}}\right)^2$$

$$= 4.81$$

$$\frac{M_{allow}}{M_e} = C1\left(\frac{S}{D_o}\right) - C2\left(\frac{S}{D_o}\right)^2 - C3$$ (3-36)

$$= 7.54\left(\frac{16.8\text{ in.}}{12.3\text{ in.}}\right) - 2.70\left(\frac{16.8\text{ in.}}{12.3\text{ in.}}\right)^2 - 4.81$$

$$= 0.450$$


*52 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*



<!-- Page 60 -->

<!-- Page 60 -->

The available flexural strength is:

| LRFD | ASD |
|------|-----|
| From Equation 3-37a, | From Equation 3-37b, |
| $\phi_b\left(\frac{M_{allow}}{M_e}\right)M_e = 0.90(0.450)(218\text{ kip-in.})$ | $\frac{M_{allow}}{M_e}\left(\frac{M_e}{\Omega_b}\right) = 0.450\left(\frac{218\text{ kip-in.}}{1.67}\right)$ |
| $= 88.3\text{ kip-in.} > M_u = 34.6\text{ kip-in.}$ **o.k.** | $= 58.7\text{ kip-in.} > M_a = 25.5\text{ kip-in.}$ **o.k.** |

*Check horizontal and vertical shear*

The available horizontal shear strength is calculated using AISC *Specification* Section J4.2.

| LRFD | ASD |
|------|-----|
| From Table 4-13, | From Table 4-13, |
| $V_{eh} = 6.26\text{ kips}$ | $V_{eh} = 4.61\text{ kips}$ |
| $\phi_v V_{n-horiz} = \phi_v 0.6F_y(et_w)$ (from *Spec.* Eq. J4-3) | $\frac{V_{n-horiz}}{\Omega_v} = \frac{0.6F_y(et_w)}{\Omega_v}$ (from *Spec.* Eq. J4-3) |
| $= 0.6(50\text{ ksi})[(4.50\text{ in.})(0.200\text{ in.})]$ | $= \frac{0.6(50\text{ ksi})[(4.50\text{ in.})(0.200\text{ in.})]}{1.50}$ |
| $= 27.0\text{ kips} > 6.26\text{ kips}$ **o.k.** | $= 18.0\text{ kips} > 4.61\text{ kips}$ **o.k.** |

*Check vertical shear at beam net section*

From AISC *Specification* Section G3:

$$\frac{h}{t_w} = \frac{d_{t-net}}{t_w}$$

$$= \frac{2.65\text{ in.}}{0.200\text{ in.}}$$

$$= 13.3$$

$$1.10\sqrt{\frac{k_v E}{F_y}} = 1.10\sqrt{\frac{1.2(29,000\text{ ksi})}{50\text{ ksi}}}$$

$$= 29.0$$

Because $h/t_w < 1.10\sqrt{k_v E/F_y}$

$$C_{v2} = 1.0$$ (*Spec.* Eq. G2-9)

The available vertical shear strength at the net section is calculated using AISC *Specification* Equation G2-3.

| LRFD | ASD |
|------|-----|
| From Table 4-10, | From Table 4-10, |
| $V_n = 6.25\text{ kips}$ | $V_n = 4.57\text{ kips}$ |
| From *Spec.* Eq. G2-3, | From *Spec.* Eq. G2-3, |
| $\phi V_{n-net} = \phi 0.6F_y(2d_{t-net}t_w)C_{v2}$ | $\frac{V_{n-net}}{\Omega_v} = \frac{0.6F_y(2d_{t-net}t_w)C_{v2}}{\Omega_v}$ |
| $= 1.00(0.6)(50\text{ ksi})(2)(2.65\text{ in.})(0.200\text{ in.})(1.0)$ | $= \frac{0.6(50\text{ ksi})(2)(2.65\text{ in.})(0.200\text{ in.})(1.0)}{1.50}$ |
| $= 31.8\text{ kips} > 6.25\text{ kips}$ **o.k.** | $= 21.2\text{ kips} > 4.57\text{ kips}$ **o.k.** |


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 53*



<!-- Page 61 -->

<!-- Page 61 -->

*Check vertical shear at beam gross section*

From AISC *Specification* Section G2.1(b)(1)

$$\frac{h}{t_w} = \frac{17.6 \text{ in.} - 2(0.525 \text{ in.})}{0.200 \text{ in.}}$$

$$= 82.8$$

$$1.10\sqrt{\frac{k_v E}{F_y}} = 1.10\sqrt{\frac{5.34(29,000 \text{ ksi})}{50 \text{ ksi}}}$$

$$= 61.2$$

Because $h/t_w > 61.2$,

$$C_{v1} = \frac{1.10\sqrt{k_v E/F_y}}{h/t_w}$$ (*Spec.* Eq. G2-4)

$$= \frac{1.10\sqrt{5.34(29,000 \text{ ksi})/50 \text{ ksi}}}{82.8}$$

$$= 0.739$$

From AISC *Specification* Section G1, because $h/t_w > 2.24\sqrt{E/F_y} = 53.9$

$$\phi_v = 0.90 \text{ (LRFD)} \qquad \Omega_v = 1.67 \text{ (ASD)}$$

| LRFD | ASD |
|------|-----|
| From Table 4-10, | From Table 4-10, |
| $V_u = 6.54$ kips | $V_a = 4.78$ kips |
| From *Spec.* Eq. G2-1, | From *Spec.* Eq. G2-1, |
| $\phi_v V_{n-gross} = \phi_v 0.6F_y (d_g t_w) C_{v1}$ | $\frac{V_{n-gross}}{\Omega_v} = \frac{0.6F_y (d_g t_w) C_{v1}}{\Omega_v}$ |
| $= 0.90(0.6)(50 \text{ ksi})(17.6 \text{ in.})(0.200 \text{ in.})(0.739)$ | $= \frac{0.6(50 \text{ ksi})(17.6 \text{ in.})(0.200 \text{ in.})(0.739)}{1.67}$ |
| $= 70.2 \text{ kips} > 6.54 \text{ kips} \quad \textbf{o.k.}$ | $= 46.7 \text{ kips} > 4.78 \text{ kips} \quad \textbf{o.k.}$ |

The following is a summary of the beam shear strengths:

| LRFD | ASD |
|------|-----|
| *Horizontal shear* | *Horizontal shear* |
| $V_{uh}/\phi_v V_{n-horiz} = 6.26 \text{ kips}/27.0 \text{ kips}$ | $V_{ah}\Omega_v/V_{n-horiz} = 4.61 \text{ kips}/18.0 \text{ kips}$ |
| $= 0.232 < 1.0 \quad \textbf{o.k.}$ | $= 0.256 < 1.0 \quad \textbf{o.k.}$ |
| *Vertical shear—net section* | *Vertical shear—net section* |
| $V_u/\phi_v V_{n-net} = 6.25 \text{ kips}/31.8 \text{ kips}$ | $V_a \Omega_v/V_{n-net} = 4.57 \text{ kips}/21.2 \text{ kips}$ |
| $= 0.197 < 1.0 \quad \textbf{o.k.}$ | $= 0.216 < 1.0 \quad \textbf{o.k.}$ |


*54 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*




<!-- Page 62 -->

<!-- Page 62 -->

| LRFD | ASD |
|------|-----|
| *Vertical shear—gross section* | *Vertical shear—gross section* |
| $V_u/\phi_v V_{n-gross} = 6.54 \text{ kips}/70.2 \text{ kips}$ | $V_a \Omega_v/V_{n-gross} = 4.78 \text{ kips}/46.7 \text{ kips}$ |
| $= 0.093 < 1.0 \quad \textbf{o.k.}$ | $= 0.102 < 1.0 \quad \textbf{o.k.}$ |

*Check Deflection*

Deflections are calculated using 90% of the moment of inertia as discussed in Section 3.7.

From AISC *Manual* Table 3-23, Case 1, the live load and dead load deflections are:

$$\Delta_{LL} = \frac{5wl^4}{384EI_{xnet}(0.90)}$$

$$= \frac{5(0.1 \text{ kip/ft})(1 \text{ ft}/12 \text{ in.})[(40 \text{ ft})(12 \text{ in./ft})]^4}{384(29,000 \text{ ksi})(190 \text{ in.}^4)(0.90)}$$

$$= 1.16 \text{ in.}$$

$$= \frac{L}{410} > \frac{L}{240} \quad \textbf{o.k.}$$

$$\Delta_{DL} = \frac{5wl^4}{384EI_{xnet}(0.90)}$$

$$= \frac{5(0.139 \text{ kip/ft})(1 \text{ ft}/12 \text{ in.})[(40 \text{ ft})(12 \text{ in./ft})]^4}{384(29,000 \text{ ksi})(190 \text{ in.}^4)(0.90)}$$

$$= 1.61 \text{ in.}$$

Because $\Delta_{DL} = 1.61$ in., a 1½-in. camber is required.

Total load deflection is:

$$\Delta_{TL} = \Delta_{LL} + \Delta_{DL}$$

$$= 1.16 \text{ in.} + 1.61 \text{ in.}$$

$$= 2.77 \text{ in.}$$

$$= \frac{L}{172} > \frac{L}{180} \quad \textbf{n.g.}$$

This beam does not meet the deflection criteria. Either a larger section (LB18×16) should be considered, or the cutting pattern could be modified to increase the stiffness of the section.

**Example 4.3—Composite Castellated Beam Design**

**Given:**

A 50-ft-long floor beam with simple supports, shown in Figure 4-5, will be evaluated as a composite castellated section subject to uniform loading.

| Beam span: | 50 ft |
|------------|-------|
| Beam spacing: | 8 ft |
| Trial beam: | Asymmetric Section: W21×44 (top) + W21×57 (bottom) → CB30×44/57 |


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 55*




<!-- Page 63 -->

<!-- Page 63 -->

| Loading: | Live load = 100 psf |
|----------|---------------------|
|          | Dead load = 75 psf (not including beam self-weight) |
|          | Metal deck and concrete weight = 55 psf |
|          | Total load = 800 lb/ft + 600 lb/ft + 51 lb/ft |
|          | = 1,450 lb/ft |
| Deflection limits: | $L/360$ live load, $L/240$ total load |
| Bracing: | Beam is fully braced by concrete deck, $L_b = 0$ |
| Material: | ASTM A992 |
| Metal deck: | depth = 2 in., rib width = 6 in., flutes perpendicular to beam |
| Studs: | diameter = ¾ in., height = 4 in., $F_u = 65$ ksi |
| Concrete: | $f'_c = 3,000$ psi, $w_c = 145$ lb/ft³, $t_c = 3$ in. (5 in. total deck thickness) |
| Connections: | Assume that connections exist on either end to provide stability during construction (prior to deck being attached) and that the connections are sufficiently rigid to prevent web post buckling at the first web post on each end. Assume that the beam has been checked in its pre-composite stage for the wet concrete weight and construction loads. |

**Solution:**

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992
$F_y = 50$ ksi
$F_u = 65$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

Top Root Beam:
W21×44
$A = 13.0 \text{ in.}^2$ $\quad d_{top} = 20.7$ in. $\quad t_w = 0.350$ in. $\quad b_f = 6.50$ in. $\quad t_f = 0.450$ in.
$S_x = 81.6 \text{ in.}^3$ $\quad Z_x = 95.4 \text{ in.}^3$ $\quad I_x = 843 \text{ in.}^4$

Bottom Root Beam:
W21×57
$A = 16.7 \text{ in.}^2$ $\quad d_{bot} = 21.1$ in. $\quad t_w = 0.405$ in. $\quad b_f = 6.56$ in. $\quad t_f = 0.650$ in.
$S_x = 111 \text{ in.}^3$ $\quad Z_x = 129 \text{ in.}^3$ $\quad I_x = 1,170 \text{ in.}^4$

[DIAGRAM DESCRIPTION: The figure shows a structural framing layout and composite castellated beam details for Example 4.3. The layout shows a 50'-0" beam span between gridlines 1 and 2, with Gridlines A and B spaced at 4 spaces at 8'-0" = 32'-0" (W21×44 sections) and W21×57 at the bottom. The beam is labeled as CB30×44/57, typ. A 2" metal deck with 3" concrete topping ($w_c$=145 pcf, $f'_c$=3,000 psi) is shown. The right side of the figure shows detailed cross-sections of the beam components: the top shows W21×44 (top) + W21×57 (bot.) sections with labeled dimensions including $e$, $S$, $\theta_{top}$, $\theta_{bot}$, $d_t$, $d_g$, $h_{top}$, $h_{bot}$, and waste material. The bottom shows the CB30×44/57 composite section with corresponding dimensions and the concrete topping details, including dimensions for $b_{eff}$, $t_c$, $t_c + h_r$, $t_{c,total}$, and $b_{rib,bot}$.]

*Fig. 4-5. Structural framing layout and composite castellated beam nomenclature for Example 4.3.*


*56 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*




<!-- Page 64 -->

<!-- Page 64 -->

Resultant shape section properties for the CB30×44/57 are determined as follows:

The values of $e$, $b$ and $d_t$ are designated based on the depth of the root beam section and a trial opening size.

$$e = 8.00 \text{ in.}$$

$$b = 5.50 \text{ in.}$$

$$d_t = 5.50 \text{ in.}$$

$$h_{top} = d_{top} - 2d_t$$ (from Eq. 4-1)

$$= 20.7 \text{ in.} - 2(5.50 \text{ in.})$$

$$= 9.70 \text{ in.}$$

$$h_{bot} = d_{bot} - 2d_t$$ (from Eq. 4-1)

$$= 21.1 \text{ in.} - 2(5.50 \text{ in.})$$

$$= 10.1 \text{ in.}$$

$$h_o = h_{top} + h_{bot}$$ (from Eq. 4-2)

$$= 9.70 \text{ in.} + 10.1 \text{ in.}$$

$$= 19.8 \text{ in.}$$

$$d_g = h_o + 2d_t$$ (4-3)

$$= 19.8 \text{ in.} + 2(5.50 \text{ in.})$$

$$= 30.8 \text{ in.}$$

$$\theta_{top} = \tan^{-1}\left(\frac{h_{top}}{b}\right)$$ (from Eq. 4-4)

$$= \tan^{-1}\left(\frac{9.70 \text{ in.}}{5.50 \text{ in.}}\right)$$

$$= 60.4°$$

$$\theta_{bot} = \tan^{-1}\left(\frac{h_{bot}}{b}\right)$$ (from Eq. 4-4)

$$= \tan^{-1}\left(\frac{10.1 \text{ in.}}{5.50 \text{ in.}}\right)$$

$$= 61.4°$$

$$S = 2e + 2b$$ (4-5)

$$= 2(8.00 \text{ in.}) + 2(5.50 \text{ in.})$$

$$= 27.0 \text{ in.}$$

*Calculate section properties of top and bottom tee and beam*

Relevant cross sections are provided in Figure 4-6, and the section properties for the top and bottom tees are reported in Tables 4-14 and 4-15, respectively.

*Beam net section properties*

$$A_{net} = A_{tee-top} + A_{tee-bot}$$ (3-7)

$$= 4.70 \text{ in.}^2 + 6.22 \text{ in.}^2$$

$$= 10.9 \text{ in.}^2$$

$$\overline{y}_{bs} = \frac{A_{tee-top}(d_t + h_o + \overline{y}_{tee-top}) + A_{tee-bot}\overline{y}_{tee-bot}}{A_{net}}$$ (4-25)

$$= \frac{4.70 \text{ in.}^2(5.50 \text{ in.} + 19.8 \text{ in.} + 4.24 \text{ in.}) + (6.22 \text{ in.}^2)(1.19 \text{ in.})}{10.9 \text{ in.}^2}$$

$$= 13.4 \text{ in.}$$


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 57*




<!-- Page 65 -->

<!-- Page 65 -->

| Table 4-14. Top Tee Section Properties at Center of Opening |
|--------------------------------------------------------------|
| $A_{tee-top} = 4.70 \text{ in.}^2$ | $x = 5.14 \text{ in.}$ | $r_x = 1.61 \text{ in.}$ | $r_y = 1.48 \text{ in.}$ |
| $\overline{y}_{tee-top} = 4.24 \text{ in.}$ | $S_{x-top} = 9.63 \text{ in.}^3$ | $S_{c-bot} = 2.86 \text{ in.}^3$ | $Z_x = 5.07 \text{ in.}^3$ |
| $I_{x-tee-top} = 12.1 \text{ in.}^4$ | $I_y = 10.3 \text{ in.}^4$ | $J = 0.266 \text{ in.}^4$ | $y_o = 4.01 \text{ in.}$ |
| Note: The fillet radius is assumed to be zero in the section properties calculations. |

| Table 4-15. Bottom Tee Section Properties at Center of Opening |
|-----------------------------------------------------------------|
| $A_{tee-bot} = 6.22 \text{ in.}^2$ | $x = 0.475 \text{ in.}$ | $r_x = 1.51 \text{ in.}$ | $r_y = 1.57 \text{ in.}$ |
| $\overline{y}_{tee-bot} = 1.19 \text{ in.}$ | $S_{x-top} = 3.29 \text{ in.}^3$ | $S_{c-bot} = 11.9 \text{ in.}^3$ | $Z_x = 5.95 \text{ in.}^3$ |
| $I_{x-tee-bot} = 14.2 \text{ in.}^4$ | $I_y = 15.3 \text{ in.}^4$ | $J = 0.685 \text{ in.}^4$ | $y_o = 0.870 \text{ in.}$ |
| Note: The fillet radius is assumed to be zero in the section properties calculations. |

$$\overline{y}_o = d_g - \overline{y}_{bs}$$ (4-26)

$$= 30.8 \text{ in.} - 13.4 \text{ in.}$$

$$= 17.4 \text{ in.}$$

$$d_{eff,c} = d_g - [(d_t - \overline{y}_{tee-top}) + \overline{y}_{tee-bot}]$$ (4-27)

$$= 30.8 \text{ in.} - [(5.50 \text{ in.} - 4.24 \text{ in.}) + 1.19 \text{ in.}]$$

$$= 28.4 \text{ in.}$$

$$I_{x-net} = I_{x-tee-top} + A_{tee-tot}[\overline{y}_{bs} - (d_t - \overline{y}_{tee-top})]^2 + I_{x-tee-bot} + A_{tee-bot}(\overline{y}_{bs} - \overline{y}_{tee-bot})^2$$ (4-28)

$$= 12.1 \text{ in.}^4 + (4.70 \text{ in.}^2)[17.4 \text{ in.} - (5.50 \text{ in.} - 4.24 \text{ in.})]^2 + 14.2 \text{ in.}^4 + (6.22 \text{ in.}^2)(13.4 \text{ in.} - 1.19 \text{ in.})^2$$

$$= 2,180 \text{ in.}^4$$

[DIAGRAM DESCRIPTION: The figure shows cross-sectional views of tee sections and composite sections. On the left are detailed dimensions of the Top Tee-W21×44 and Bottom Tee-W21×57 sections with various measurements labeled (5.50", 1.48", 5.14", 3.14", 0.350", 0.405", 6.50", 6.56", PNA, ENA positions). In the center is the Net Section showing the combined tee sections with dimensions (5.50", 1.46", 17.4", 13.4", 28.1", 19.8", 30.8") and labeled ENA positions. On the right is the Composite Section showing a 96" wide concrete topping with dimensions and labeled ENA positions.]

*Fig. 4-6. Tee, net and composite sections for castellated beam for Example 4.3.*


*58 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*




<!-- Page 66 -->

<!-- Page 66 -->

$$S_{x-net-top} = \frac{I_{x-net}}{\overline{y}_o}$$ (4-29)

$$= \frac{2,180 \text{ in.}^4}{17.4 \text{ in.}}$$

$$= 125 \text{ in.}^3$$

$$S_{x-net-bot} = \frac{I_{x-net}}{\overline{y}_{bs}}$$ (4-30)

$$= \frac{2,180 \text{ in.}^4}{13.4 \text{ in.}}$$

$$= 163 \text{ in.}^3$$

*Composite section properties in accordance with* The Structural Engineer's Handbook (*Gaylord and Gaylord, 1992*)

$$n = \frac{E_s}{E_c}$$ (4-31)

$$= \frac{29,000,000 \text{ psi}}{33(145 \text{ pcf})^{1.5}\sqrt{3,000 \text{ psi}}}$$

$$= 9.19$$

$$b_{eff,c} = \min\{Span/4, Spacing\}$$ (3-4)

$$= \min\left\{\frac{50 \text{ ft}}{4}, \frac{8 \text{ ft} + 8 \text{ ft}}{2}\right\}(12 \text{ in./ft})$$

$$= 96.0 \text{ in.}$$

$$A_c = b_{eff,c} t_c$$ (4-32)

$$= (96.0 \text{ in.})(3.00 \text{ in.})$$

$$= 288 \text{ in.}^2$$

$$A_{ctr} = \frac{A_c}{n}$$ (4-33)

$$= \frac{288 \text{ in.}^2}{9.19}$$

$$= 31.3 \text{ in.}^2$$

$$K_c = \frac{A_{ctr}}{A_{ctr} + A_{net}}$$ (4-34)

$$= \frac{31.3 \text{ in.}^2}{31.3 \text{ in.}^2 + 10.9 \text{ in.}^2}$$

$$= 0.741$$

$$e_c = h_r + \frac{t_c}{2}$$ (4-35)

$$= 2.00 \text{ in.} + \frac{3.00 \text{ in.}}{2}$$

$$= 3.50 \text{ in.}$$


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 59*




<!-- Page 67 -->

<!-- Page 67 -->

Assuming that the neutral axis is in the concrete.

$$y_{cc} = \left(\frac{A_{net} t_c}{A_{ctr}}\right)\left[\sqrt{1 + \frac{2A_{ctr}}{A_{net}t_c}\left(\overline{y}_{bs} + e_c + \frac{t_c}{2}\right)} - 1\right]$$ (4-36)

$$= \left[\frac{(10.9 \text{ in.}^2)(3.00 \text{ in.})}{31.3 \text{ in.}^2}\right]\left[\sqrt{1 + \frac{2(31.3 \text{ in.}^2)}{(10.9 \text{ in.}^2)(3.00 \text{ in.})}\left(17.4 \text{ in.} + 3.50 \text{ in.} + \frac{3.00 \text{ in.}}{2}\right)} - 1\right]$$

$$= 5.87 \text{ in.}$$

$$t_c + h_r = 3.00 \text{ in.} + 2.00 \text{ in.}$$

$$= 5.00 \text{ in.} < 5.87 \text{ in.}$$

Because $t_c + h_r < y_{cc}$, the neutral axis is in the steel.

$$\overline{y}_c = (\overline{y}_{bs} + e_c)K_c$$ (4-37)

$$= (17.4 \text{ in.} + 3.50 \text{ in.})0.741$$

$$= 15.5 \text{ in.}$$

$$I_{x-comp} = (\overline{y}_{bs} + e_c)\overline{y}_c A_{net} + I_{x-net} + \frac{A_{ctr}t_c^2}{12}$$ (4-38)

$$= (17.4 \text{ in.} + 3.50 \text{ in.})(15.5 \text{ in.})(10.9 \text{ in.}^2) + 2,180 \text{ in.}^4 + \frac{(31.3 \text{ in.}^2)(3.50 \text{ in.})^2}{12}$$

$$= 5,740 \text{ in.}^4$$

$$S_{x-comp-conc} = \frac{I_{x-comp}}{\overline{y}_{bs} - \overline{y}_c + e_c + 0.5t_c}$$ (4-39)

$$= \frac{5,740 \text{ in.}^4}{17.4 \text{ in.} - 15.5 \text{ in.} + 3.50 \text{ in.} + 0.5(3.00 \text{ in.})}$$

$$= 832 \text{ in.}^3$$

$$S_{x-comp-steel} = \frac{I_{x-comp}}{\overline{y}_{bs} + \overline{y}_c}$$ (4-40)

$$= \frac{5,740 \text{ in.}^4}{13.4 \text{ in.} + 15.5 \text{ in.}}$$

$$= 199 \text{ in.}^3$$

For the first iteration,

$$d_{eff,c-comp} = d_g - \overline{y}_{tee-bot} + h_r + 0.5t_c$$ (3-8)

$$= 30.8 \text{ in.} - 1.19 \text{ in.} + 2.00 \text{ in.} + 0.5(3.00 \text{ in.})$$

$$= 33.1 \text{ in.}$$

*Check Vierendeel bending*

The governing load cases are:


*60 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*




<!-- Page 68 -->

<!-- Page 68 -->

| Table 4-16. Global Shear and Moment at Each Opening |
|------------------------------------------------------|

| | | | Global Net Shear | | | Global Moment | |
|---|---|---|---|---|---|---|---|
| | | | | $V_{resist}$ | | | $M_u$ |
| **Opening<br>No.** | $X_0$<br>ft | $D_s$<br>kips | $L_s$<br>kips | **ASD** | **LRFD** | $D_s$<br>kips | $L_s$<br>kips | **ASD** | **LRFD** |
| End | 0.000 | 16.3 | 20.0 | 31.3 | 44.1 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1 | 1.46 | 15.3 | 18.8 | 29.2 | 41.1 | 23.0 | 28.3 | 51.3 | 72.9 |
| 2 | 3.71 | 13.9 | 17.0 | 26.0 | 36.5 | 55.8 | 68.7 | 125 | 177 |
| 3 | 5.96 | 12.4 | 15.2 | 22.7 | 31.8 | 85.4 | 105 | 190 | 270 |
| 4 | 8.21 | 10.9 | 13.4 | 19.4 | 27.2 | 112 | 137 | 249 | 353 |
| 5 | 10.5 | 9.46 | 11.6 | 16.2 | 22.6 | 135 | 165 | 300 | 426 |
| 6 | 12.7 | 8.00 | 9.83 | 12.9 | 17.9 | 154 | 190 | 344 | 488 |
| 7 | 15.0 | 6.53 | 8.03 | 9.64 | 13.3 | 170 | 210 | 380 | 540 |
| 8 | 17.2 | 5.07 | 6.23 | 6.38 | 8.66 | 184 | 226 | 409 | 581 |
| 9 | 19.5 | 3.61 | 4.43 | 3.11 | 4.03 | 193 | 238 | 431 | 612 |
| 10 | 21.7 | 2.14 | 2.63 | 0.000 | 0.000 | 200 | 246 | 445 | 633 |
| 11 | 24.0 | 0.678 | 0.833 | 0.000 | 0.000 | 203 | 250 | 452 | 643 |
| Bm. CL | 25.0 | 0.000 | 0.000 | 0.000 | 0.000 | 203 | 250 | 453 | 644 |

Note: The shear force shown is the net shear force; i.e., the shear strength of the concrete has been subtracted from the global shear force on the beam.

| LRFD | ASD |
|------|-----|
| Load case 1: | $w = D + L$ |
| $w = 1.4D$ | $= 651 \text{ lb/ft} + 800 \text{ lb/ft}$ |
| $= 1.4(651 \text{ lb/ft})$ | $= 1,450 \text{ lb/ft}$ |
| $= 911 \text{ lb/ft}$ | |
| Load case 2: | |
| $w = 1.2D + 1.6L$ | |
| $= 1.2(651 \text{ lb/ft}) + 1.6(800 \text{ lb/ft})$ | |
| $= 2,060 \text{ lb/ft} \quad \textbf{governs}$ | |

*Calculate the available shear strength of the concrete deck:*

| LRFD | ASD |
|------|-----|
| $V_c = \phi_{cv} V_{nc}$ | (3-15a) | $V_c = \frac{V_{nc}}{\Omega_{cv}}$ | (3-15b) |
| $V_{nc} = 4\sqrt{f'_c(3)}(h_r + t_c)t_c$ | (3-14) | $V_{nc} = 4\sqrt{f'_c(3)}(h_r + t_c)t_c$ | (3-14) |
| $= \frac{4\sqrt{3,000 \text{ psi (3)}}(2.00 \text{ in.} + 3.00 \text{ in.})(3.00 \text{ in.})}{1,000 \text{ lb/kip}}$ | | $= \frac{4\sqrt{3,000 \text{ psi (3)}}(2.00 \text{ in.} + 3.00 \text{ in.})(3.00 \text{ in.})}{1,000 \text{ lb/kip}}$ | |
| $= 9.85$ kips | | $= 9.85$ kips | |
| $V_c = 0.75(9.85 \text{ kips})$ | | $V_c = \frac{9.85 \text{ kips}}{2.00}$ | |
| $= 7.39$ kips | | $= 4.93$ kips | |

Calculate the global shear and moment at each opening to be used to calculate local internal forces (axial and flexural) at each opening. These values are presented in Table 4-16.


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 61*




<!-- Page 69 -->

<!-- Page 69 -->

| Table 4-17. Local Axial Force at Each Opening |
|------------------------------------------------|

| | | | | **ASD** | | | | **ASD** | | |
|---|---|---|---|---|---|---|---|---|---|---|
| **Opening<br>Number** | $X_0$<br>ft | $M_u$<br>kip-ft | $F_{tee}$<br>kips | $K_{cv-bs}$<br>n/c | $F_{c(i)}$<br>kips | $T_{c(i)}$<br>kips | $K_{open}$<br>n/c | $F_{web}$<br>kips | $T_{web}$<br>kips |
| End | 0.000 | 0.000 | 30.8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1 | 1.46 | 51.3 | 33.1 | 0.188 | 43.2 | 1.04 | 0.177 | 43.2 | 1.00 |
| 2 | 3.71 | 125 | 45.3 | 0.161 | 43.2 | 1.04 | 0.177 | 43.2 | 1.00 |
| 3 | 5.96 | 190 | 60.0 | 0.326 | 66.7 | 1.04 | 0.177 | 43.2 | 1.00 |
| 4 | 8.21 | 249 | 72.3 | 0.161 | 66.7 | 1.04 | 0.177 | 43.2 | 1.00 |
| 5 | 10.5 | 300 | 109 | 0.444 | 105 | 1.04 | 0.477 | 105 | 1.00 |
| 6 | 12.7 | 344 | 125 | 0.209 | 120 | 1.04 | 0.464 | 120 | 1.00 |
| 7 | 15.0 | 380 | 138 | 0.723 | 171 | 1.04 | 0.773 | 186 | 1.00 |
| 8 | 17.2 | 409 | 148 | 0.600 | 143 | 1.04 | 0.565 | 143 | 1.00 |
| 9 | 19.5 | 431 | 156 | 0.597 | 212 | 1.04 | 0.619 | 212 | 1.00 |
| 10 | 21.7 | 445 | 162 | 0.600 | 156 | 1.04 | 0.617 | 156 | 1.00 |
| 11 | 24.0 | 452 | 164 | 0.975 | 158 | 1.04 | 0.647 | 158 | 1.00 |
| 12 | 24.0 | 643 | 233 | 0.952 | 226 | 1.01 | 0.953 | 226 | 1.00 |
| Bm. CL | 25.0 | 644 | 234 | 0.954 | 226 | 1.01 | 0.953 | 226 | 1.00 |

| | | | | **LRFD** | | | | **LRFD** | | |
|---|---|---|---|---|---|---|---|---|---|---|
| **Opening<br>Number** | $X_0$<br>ft | $M_u$<br>kip-ft | $F_{tee}$<br>kips | $K_{cv-bs}$<br>n/c | $F_{c(i)}$<br>kips | $T_{c(i)}$<br>kips | $K_{open}$<br>n/c | $F_{web}$<br>kips | $T_{web}$<br>kips |
| End | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| 1 | 1.46 | 72.9 | 26.6 | 0.190 | 23.3 | 1.05 | 0.163 | 23.3 | 1.00 |
| 2 | 3.71 | 177 | 63.8 | 0.524 | 94.1 | 1.04 | 0.394 | 94.1 | 1.00 |
| 3 | 5.96 | 270 | 98.0 | 0.524 | 123 | 1.04 | 0.504 | 123 | 1.00 |
| 4 | 8.21 | 353 | 128 | 0.524 | 141 | 1.04 | 0.504 | 123 | 1.00 |
| 5 | 10.5 | 426 | 155 | 0.524 | 171 | 1.04 | 0.698 | 171 | 1.00 |
| 6 | 12.7 | 488 | 177 | 0.723 | 171 | 1.04 | 0.773 | 186 | 1.00 |
| 7 | 15.0 | 540 | 196 | 0.600 | 199 | 1.04 | 0.773 | 186 | 1.00 |
| 8 | 17.2 | 581 | 211 | 0.981 | 215 | 1.01 | 0.953 | 212 | 1.00 |
| 9 | 19.5 | 612 | 222 | 0.997 | 212 | 1.00 | 0.619 | 212 | 1.00 |
| 10 | 21.7 | 633 | 230 | 0.597 | 212 | 1.01 | 0.976 | 212 | 1.00 |
| 11 | 24.0 | 643 | 233 | 0.985 | 226 | 1.01 | 0.953 | 226 | 1.00 |
| 12 | 24.0 | 643 | 233 | 0.954 | 226 | 1.01 | 0.953 | 226 | 1.00 |
| Bm. CL | 25.0 | 644 | 234 | 0.954 | 226 | 1.01 | 0.953 | 226 | 1.00 |

Calculate the local axial force in the top and bottom tees resulting from the global moment. These values are shown in Table 4-17. In the first flute at each edge is where no shear studs will be applied. Because the connection allows the compression force in the concrete flange, this projection needs to be checked as a part of the design.

Local axial force:

For the first iteration, recalculate $d_{eff,c-comp}$ each time:

$$T_{c(i+1)} = \frac{M_{u(i+1)}}{d_{eff,c-comp}}$$ (3-9)


*62 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31*




<!-- Page 70 -->

<!-- Page 70 -->

Recalculate effective concrete depth,

$$X_c = \frac{T_{(i)}}{0.85 f'_c b_{eff,c}}$$ (3-10)

Recalculate $d_{eff,c-comp}$

$$d_{eff,c-comp} = d_g - \overline{y}_{tee-bot} + t_c + h_r - \frac{X_c}{2}$$ (from Eq. 3-8)

Recalculate until the difference ≤ 1%

$$T_{i(i+1)} = \frac{M_{u(i+1)}}{d_{eff,c-comp}}$$ (3-9)

The next step is to calculate the number of studs for full composite action and shear stud density along the length of the beam. This will be used to calculate composite percentage at each web opening. If sufficient studs are not present to resist the compression force in the concrete ($T_{i(i+1)}$ in Table 4-17), an additional force, $T_w$, will be resisted by the top tee section.

From AISC *Specification* Section I2d.1, consider the limit states of concrete crushing and tensile yielding of the steel section to determine the number of studs for full composite action.

Concrete crushing:

$$V' = 0.85 f'_c A_c$$ (*Spec.* Eq. I3-1a)

$$= 0.85(3 \text{ ksi})(288 \text{ in.}^2)$$

$$= 734 \text{ kips}$$

Tensile yielding of the steel section:

$$V' = F_y A_{net}$$ (from *Spec.* Eq. I3-1b)

$$= (50 \text{ ksi})(10.9 \text{ in.}^2)$$

$$= 545 \text{ kips} \quad \textbf{controls}$$

From AISC *Manual* Table 3-21 for a ¾-in.-diameter shear stud,

$$Q_n = 21.0 \text{ kips/stud}$$

$$N = \frac{V'}{Q}$$

$$= \frac{545 \text{ kips}}{21.0 \text{ kips/stud}}$$

$$= 26 \text{ studs}$$

Between the point of maximum moment and the end of the beam, 26 studs need to be provided. Because the point of maximum moment is at the center of the beam, 52 studs are required over the length of the beam. The flutes of the deck are 12 in. on center; therefore, one additional stud will be placed in the first flute of the deck at each end. When two studs per rib are present, $Q_n =$ 18.3 kips. Investigate if providing an additional stud in the first flute provides adequate shear resistance.

$$V_{provided} = (1 \text{ stud})(2 \text{ studs/rib})Q_n + (24 \text{ studs})(1 \text{ stud/rib})Q_n$$

$$= (1)(2)(18.3 \text{ kips}) + (24)(1)(21.0 \text{ kips})$$

$$= 541 \text{ kips} < 545 \text{ kips} \quad \textbf{n.g.}$$

Double the number of studs in the second flute from each end.

$$V_{provided} = (2 \text{ studs})(2 \text{ studs/rib})Q_n + (23 \text{ studs})(1 \text{ stud/rib})Q_n$$

$$= (2)(2)(18.3 \text{ kips}) + (23)(1)(21.0 \text{ kips})$$

$$= 556 \text{ kips} > 545 \text{ kips} \quad \textbf{o.k.}$$


*AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 63*


