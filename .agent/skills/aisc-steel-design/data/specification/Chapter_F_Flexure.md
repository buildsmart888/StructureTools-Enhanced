# Chapter F: Flexure

**AISC 360-22 Specification for Structural Steel Buildings**
**Original PDF Pages**: 118-142 (25 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Design of Members for Flexure

**Description**: Bending strength and lateral-torsional buckling

---

# CHAPTER F
# DESIGN OF MEMBERS FOR FLEXURE

This chapter applies to members subjected to simple bending about one principal axis. For simple bending, the member is loaded in a plane parallel to a principal axis that passes through the shear center or is restrained against twisting at load points and supports.

The chapter is organized as follows:

- F1. General Provisions
- F2. Doubly Symmetric Compact I-Shaped Members and Channels Bent About Their Major Axis
- F3. Doubly Symmetric I-Shaped Members with Compact Webs and Noncompact or Slender Flanges Bent About Their Major Axis
- F4. Other I-Shaped Members with Compact or Noncompact Webs Bent About Their Major Axis
- F5. Doubly Symmetric and Singly Symmetric I-Shaped Members with Slender Webs Bent About Their Major Axis
- F6. I-Shaped Members and Channels Bent About Their Minor Axis
- F7. Square and Rectangular HSS and Box Sections
- F8. Round HSS
- F9. Tees and Double Angles Loaded in the Plane of Symmetry
- F10. Single Angles
- F11. Rectangular Bars and Rounds
- F12. Unsymmetrical Shapes
- F13. Proportions of Beams and Girders

**User Note:** For cases not included in this chapter, the following sections apply:
- Chapter G Design provisions for shear
- H1–H3 Members subjected to biaxial flexure or to combined flexure and axial force
- H3 Members subjected to flexure and torsion
- Appendix 3 Members subjected to fatigue

For guidance in determining the appropriate sections of this chapter to apply, Table User Note F1.1 may be used.

---

## DESIGN OF MEMBERS FOR FLEXURE [Chap. F.]

| **TABLE USER NOTE F1.1**<br/>**Selection Table for the Application**<br/>**of Chapter F Sections** |
|---|

| **Section in<br/>Chapter F** | **Cross<br/>Section** | **Flange<br/>Slenderness** | **Web<br/>Slenderness** | **Limit<br/>States** |
|---|---|---|---|---|
| F2 | [I-section and channel diagrams] | C | C | Y, LTB |
| F3 | [I-section diagram] | NC, S | C | LTB, FLB |
| F4 | [Two I-section diagrams] | C, NC, S | C, NC | CFY, LTB,<br/>FLB, TFY |
| F5 | [Two I-section diagrams] | C, NC, S | S | CFY, LTB,<br/>FLB, TFY |
| F6 | [I-section and channel diagrams] | C, NC, S | NA | Y, FLB |
| F7 | [Rectangular HSS diagram] | C, NC, S | C, NC, S | Y, FLB, WLB,<br/>LTB |
| F8 | [Round HSS diagram] | NA | NA | Y, LB |
| F9 | [Tee and double-tee diagrams] | C, NC, S | NA | Y, LTB, FLB,<br/>WLB |
| F10 | [Angle diagrams] | NA | NA | Y, LTB, LLB |
| F11 | [Round and rectangular bar diagrams] | NA | NA | Y, LTB |
| F12 | Unsymmetrical shapes,<br/>other than single angles | NA | NA | All limit<br/>states |

C = compact; CFY = compression flange yielding; FLB = flange local buckling; LB = local buckling; LLB = leg local buckling; LTB = lateral-torsional buckling; NC = noncompact; S = slender; TFY = tension flange yielding; WLB = web local buckling; Y = yielding; NA = not applicable

---

## GENERAL PROVISIONS [Sect. F1.

## F1. GENERAL PROVISIONS

The design flexural strength, $\phi_b M_n$, and the allowable flexural strength, $M_n/\Omega_b$, shall be determined as follows:

(a) For all provisions in this chapter

$$\phi_b = 0.90 \text{ (LRFD)} \qquad \Omega_b = 1.67 \text{ (ASD)}$$

and the nominal flexural strength, $M_n$, shall be determined according to Sections F2 through F13.

(b) The provisions in this chapter are based on the assumption that points of support for beams and girders are restrained against rotation about their longitudinal axis.

(c) For singly symmetric members in single curvature and all doubly symmetric members

The lateral-torsional buckling modification factor, $C_b$, for nonuniform moment diagrams when both ends of the segment are braced is determined as follows:

$$C_b = \frac{12.5M_{max}}{2.5M_{max} + 3M_A + 4M_B + 3M_C}$$ (F1-1)

where

$M_{max}$ = absolute value of maximum moment in the unbraced segment, kip-in. (N-mm)

$M_A$ = absolute value of moment at quarter point of the unbraced segment, kip-in. (N-mm)

$M_B$ = absolute value of moment at centerline of the unbraced segment, kip-in. (N-mm)

$M_C$ = absolute value of moment at three-quarter point of the unbraced segment, kip-in. (N-mm)

**User Note:** For doubly symmetric members with no transverse loading between brace points, Equation F1-1 reduces to 1.0 for the case of equal end moments of opposite sign (uniform moment), 2.27 for the case of equal end moments of the same sign (reverse curvature bending), and to 1.67 when one end moment equals zero. For singly symmetric members, a more detailed analysis for $C_b$ is presented in the Commentary. The Commentary provides additional equations for $C_b$ that provide improved characterization of the effects of a variety of member boundary conditions.

For cantilevers where warping is prevented at the support and where the free end is unbraced, $C_b = 1.0$.

(d) In singly symmetric members subjected to reverse curvature bending, the lateral-torsional buckling strength shall be checked for both flanges. The available flexural strength shall be greater than or equal to the maximum required moment causing compression within the flange under consideration.

---

## DOUBLY SYMMETRIC COMPACT I-SHAPED MEMBERS AND CHANNELS [Sect. F2.]

## F2. DOUBLY SYMMETRIC COMPACT I-SHAPED MEMBERS AND CHANNELS BENT ABOUT THEIR MAJOR AXIS

This section applies to doubly symmetric I-shaped members and channels bent about their major axis, having compact webs and compact flanges as defined in Section B4.1 for flexure.

**User Note:** For $F_y = 50$ ksi (345 MPa), all current ASTM A6/A6M W, S, M, C, and MC shapes except W21×48, W14×99, W14×90, W12×65, W10×12, W8×31, W8×10, W6×15, W6×9, W6×8.5, and M4×6 have compact flanges. For $F_y \leq 70$ ksi (485 MPa), all current ASTM A6/A6M W, S, M, HP, C, and MC shapes have compact webs.

The nominal flexural strength, $M_n$, shall be the lower value obtained according to the limit states of yielding (plastic moment) and lateral-torsional buckling.

### 1. Yielding

$$M_n = M_p = F_y Z_x$$ (F2-1)

where

$F_y$ = specified minimum yield stress of the type of steel being used, ksi (MPa)
$Z_x$ = plastic section modulus about the x-axis, in.$^3$ (mm$^3$)

### 2. Lateral-Torsional Buckling

(a) When $L_b \leq L_p$, the limit state of lateral-torsional buckling does not apply.

(b) When $L_p < L_b \leq L_r$

$$M_n = C_b\left[M_p - \left(M_p - 0.7F_y S_x\right)\left(\frac{L_b - L_p}{L_r - L_p}\right)\right] \leq M_p$$ (F2-2)

(c) When $L_b > L_r$

$$M_n = F_{cr} S_x \leq M_p$$ (F2-3)

where

$L_b$ = length between points that are either braced against lateral displacement of the compression flange or braced against twist of the cross section, in. (mm)

$F_{cr}$ = critical stress, ksi (MPa)

$$= \frac{C_b \pi^2 E}{\left(\frac{L_b}{r_{ts}}\right)^2}\sqrt{1 + 0.078\frac{Jc}{S_x h_o}\left(\frac{L_b}{r_{ts}}\right)^2}$$ (F2-4)

$E$ = modulus of elasticity of steel
= 29,000 ksi (200 000 MPa)

$J$ = torsional constant, in.$^4$ (mm$^4$)

$S_x$ = elastic section modulus taken about the x-axis, in.$^3$ (mm$^3$)

$h_o$ = distance between the flange centroids, in. (mm)

---

## DOUBLY SYMMETRIC COMPACT I-SHAPED MEMBERS AND CHANNELS [Sect. F2.

**User Note:** The square root term in Equation F2-4 may be conservatively taken as equal to 1.0.

**User Note:** Equations F2-3 and F2-4 provide identical solutions to the following expression for lateral-torsional buckling of doubly symmetric members that has been presented in past editions of this Specification:

$$M_{cr} = C_b\frac{\pi}{L_b}\sqrt{EI_y GJ + \left(\frac{\pi E}{L_b}\right)^2 I_y C_w}$$

The advantage of Equations F2-3 and F2-4 is that the form is very similar to the expression for lateral-torsional buckling of singly symmetric I-shaped members given in Equations F4-3 and F4-5.

$L_p$, the limiting laterally unbraced length for the limit state of yielding, in. (mm), is

$$L_p = 1.76r_y\sqrt{\frac{E}{F_y}}$$ (F2-5)

$L_r$, the limiting unbraced length for the limit state of inelastic lateral-torsional buckling, in. (mm), is

$$L_r = 1.95r_{ts}\frac{E}{0.7F_y}\sqrt{\frac{Jc}{S_x h_o} + \sqrt{\left(\frac{Jc}{S_x h_o}\right)^2 + 6.76\left(\frac{0.7F_y}{E}\right)^2}}$$ (F2-6)

where

$r_y$ = radius of gyration about y-axis, in. (mm)

$$r_{ts}^2 = \frac{I_y C_w}{S_x}$$ (F2-7)

and the coefficient $c$ is determined as follows:

(1) For doubly symmetric I-shapes

$$c = 1$$ (F2-8a)

(2) For channels

$$c = \frac{h_o}{2}\sqrt{\frac{I_y}{C_w}}$$ (F2-8b)

where

$I_y$ = moment of inertia about the y-axis, in.$^4$ (mm$^4$)

**User Note:**
For doubly symmetric I-shapes with rectangular flanges, $C_w = \frac{I_y h_o^2}{4}$, and, thus, Equation F2-7 becomes

---

## DOUBLY SYMMETRIC I-SHAPED MEMBERS WITH COMPACT WEBS [Sect. F3.]

$$r_{ts}^2 = \frac{I_y h_o}{2S_x}$$

$r_{ts}$ may be approximated accurately to conservatively as the radius of gyration of the compression flange plus one-sixth of the web:

$$r_{ts} = \frac{b_f}{\sqrt{12\left(1 + \frac{1}{6}\frac{ht_w}{b_f t_f}\right)}}$$

## F3. DOUBLY SYMMETRIC I-SHAPED MEMBERS WITH COMPACT WEBS AND NONCOMPACT OR SLENDER FLANGES BENT ABOUT THEIR MAJOR AXIS

This section applies to doubly symmetric I-shaped members bent about their major axis having compact webs and noncompact or slender flanges as defined in Section B4.1 for flexure.

**User Note:** The following shapes have noncompact flanges for $F_y = 50$ ksi (345 MPa): W21×48, W14×99, W14×90, W12×65, W10×12, W8×31, W8×10, W6×15, W6×9, W6×8.5, and M4×6. All other ASTM A6/A6M W, S, and M shapes have compact flanges for $F_y \leq 50$ ksi (345 MPa).

The nominal flexural strength, $M_n$, shall be the lower value obtained according to the limit states of lateral-torsional buckling and compression flange local buckling.

### 1. Lateral-Torsional Buckling

For lateral-torsional buckling, the provisions of Section F2.2 shall apply.

### 2. Compression Flange Local Buckling

(a) For sections with noncompact flanges

$$M_n = M_p - \left(M_p - 0.7F_y S_x\right)\left(\frac{\lambda - \lambda_{pf}}{\lambda_{rf} - \lambda_{pf}}\right)$$ (F3-1)

(b) For sections with slender flanges

$$M_n = \frac{0.9Ek_c S_x}{\lambda^2}$$ (F3-2)

where

$k_c = \frac{4}{\sqrt{h/t_w}}$ and shall not be taken as less than 0.35 nor greater than 0.76 for calculation purposes

$h$ = distance as defined in Section B4.1b, in. (mm)
$t_w$ = thickness of the web, in. (mm)

---

## DOUBLY SYMMETRIC I-SHAPED MEMBERS WITH COMPACT WEBS [Sect. F3.

$$\lambda = \frac{b_f}{2t_f}$$

$b_f$ = width of the flange, in. (mm)

$t_f$ = thickness of the flange, in. (mm)

$\lambda_{pf} = \lambda_p$, the limiting width-to-thickness ratio for a compact flange as defined in Table B4.1b

$\lambda_{rf} = \lambda_r$, the limiting width-to-thickness ratio for a noncompact flange as defined in Table B4.1b

## F4. OTHER I-SHAPED MEMBERS WITH COMPACT OR NONCOMPACT WEBS BENT ABOUT THEIR MAJOR AXIS

This section applies to doubly symmetric I-shaped members bent about their major axis with noncompact webs and singly symmetric I-shaped members with webs attached to the mid-width of the flanges, bent about their major axis, with compact or noncompact webs, as defined in Section B4.1 for flexure.

**User Note:** I-shaped members for which this section is applicable may be designed conservatively using Section F5.

The nominal flexural strength, $M_n$, shall be the lowest value obtained according to the limit states of compression flange yielding, lateral-torsional buckling, compression flange local buckling, and tension flange yielding.

### 1. Compression Flange Yielding

$$M_n = R_{pc} M_{yc}$$ (F4-1)

where

$M_{yc}$ = yield moment in the compression flange, kip-in. (N-mm)
= $F_y S_{xc}$

$R_{pc}$ = web plastification factor, determined in accordance with Section F4.2(c)(6)

$S_{xc}$ = elastic section modulus referred to compression flange, in.$^3$ (mm$^3$)

### 2. Lateral-Torsional Buckling

(a) When $L_b \leq L_p$, the limit state of lateral-torsional buckling does not apply.

(b) When $L_p < L_b \leq L_r$

$$M_n = C_b\left[R_{pc}M_{yc} - \left(R_{pc}M_{yc} - F_L S_{xc}\right)\left(\frac{L_b - L_p}{L_r - L_p}\right)\right] \leq R_{pc}M_{yc}$$ (F4-2)

(c) When $L_b > L_r$

$$M_n = F_{cr}S_{xc} \leq R_{pc}M_{yc}$$ (F4-3)

where

(1) $M_{yc}$, the yield moment in the compression flange, kip-in. (N-mm), is

$$M_{yc} = F_y S_{xc}$$ (F4-4)

---

## OTHER I-SHAPED MEMBERS WITH COMPACT OR NONCOMPACT WEBS [Sect. F4.]

(2) $F_{cr}$, the critical stress, ksi (MPa), is

$$F_{cr} = \frac{C_b \pi^2 E}{\left(\frac{L_b}{r_t}\right)^2}\sqrt{1 + 0.078\frac{J}{S_{xc}h_o}\left(\frac{L_b}{r_t}\right)^2}$$ (F4-5)

For $\frac{I_{yc}}{I_y} \leq 0.23$, $J$ shall be taken as zero,

where

$I_{yc}$ = moment of inertia of the compression flange about the y-axis, in.$^4$ (mm$^4$)

(3) $F_L$, nominal compression flange stress above which the inelastic buckling limit states apply, ksi (MPa), is determined as follows:

(i) When $\frac{S_{xt}}{S_{xc}} \geq 0.7$

$$F_L = 0.7F_y$$ (F4-6a)

(ii) When $\frac{S_{xt}}{S_{xc}} < 0.7$

$$F_L = F_y\frac{S_{xt}}{S_{xc}} \geq 0.5F_y$$ (F4-6b)

where

$S_{xt}$ = elastic section modulus referred to tension flange, in.$^3$ (mm$^3$)

(4) $L_p$, the limiting laterally unbraced length for the limit state of yielding, in. (mm), is

$$L_p = 1.1r_t\sqrt{\frac{E}{F_y}}$$ (F4-7)

(5) $L_r$, the limiting unbraced length for the limit state of inelastic lateral-torsional buckling, in. (mm), is

$$L_r = 1.95r_t\frac{E}{F_L}\sqrt{\frac{J}{S_{xc}h_o} + \sqrt{\left(\frac{J}{S_{xc}h_o}\right)^2 + 6.76\left(\frac{F_L}{E}\right)^2}}$$ (F4-8)

(6) $R_{pc}$, the web plastification factor, is determined as follows:

(i) When $I_{yc} / I_y > 0.23$

(a) When $\frac{h_c}{t_w} \leq \lambda_{pw}$

$$R_{pc} = \frac{M_p}{M_{yc}}$$ (F4-9a)

---

## OTHER I-SHAPED MEMBERS WITH COMPACT OR NONCOMPACT WEBS [Sect. F4.

(b) When $\frac{h_c}{t_w} > \lambda_{pw}$

$$R_{pc} = \left[\frac{M_p}{M_{yc}} - \left(\frac{M_p}{M_{yc}} - 1\right)\left(\frac{\lambda - \lambda_{pw}}{\lambda_{rw} - \lambda_{pw}}\right)\right] \leq \frac{M_p}{M_{yc}}$$ (F4-9b)

(ii) When $I_{yc} / I_y \leq 0.23$

$$R_{pc} = 1.0$$ (F4-10)

where

$M_p = F_y Z_x \leq 1.6F_y S_x$

$h_c$ = twice the distance from the centroid to the following: the inside face of the compression flange less the fillet or corner radius, for rolled shapes; the nearest line of fasteners at the compression flange or the inside face of the compression flange when welds are used, for built-up sections, in. (mm)

$$\lambda = \frac{h_c}{t_w}$$

$\lambda_{pw} = \lambda_p$, the limiting width-to-thickness ratio for a compact web as defined in Table B4.1b

$\lambda_{rw} = \lambda_r$, the limiting width-to-thickness ratio for a noncompact web as defined in Table B4.1b

(7) $r_t$, the effective radius of gyration for lateral-torsional buckling, in. (mm), is determined as follows:

(i) For I-shapes with a rectangular compression flange

$$r_t = \frac{b_{fc}}{\sqrt{12\left(1 + \frac{1}{6}a_w\right)}}$$ (F4-11)

where

$$a_w = \frac{h_c t_w}{b_{fc} t_{fc}}$$ (F4-12)

$b_{fc}$ = width of compression flange, in. (mm)
$t_{fc}$ = thickness of compression flange, in. (mm)
$t_w$ = thickness of web, in. (mm)

(ii) For I-shapes with a channel cap or a cover plate attached to the compression flange

$r_t$ = radius of gyration of the flange components in flexural compression plus one-third of the web area in compression due to application of major-axis bending moment alone, in. (mm)

---

## OTHER I-SHAPED MEMBERS WITH COMPACT OR NONCOMPACT WEBS [Sect. F4.]

### 3. Compression Flange Local Buckling

(a) For sections with compact flanges, the limit state of local buckling does not apply.

(b) For sections with noncompact flanges

$$M_n = R_{pc}M_{yc} - \left(R_{pc}M_{yc} - F_L S_{xc}\right)\left(\frac{\lambda - \lambda_{pf}}{\lambda_{rf} - \lambda_{pf}}\right)$$ (F4-13)

(c) For sections with slender flanges

$$M_n = \frac{0.9Ek_c S_{xc}}{\lambda^2}$$ (F4-14)

where

$F_L$ is defined in Equations F4-6a and F4-6b

$R_{pc}$ is the web plastification factor, determined by Equation F4-9a, F4-9b, or F4-10

$k_c = \frac{4}{\sqrt{h/t_w}}$ and shall not be taken as less than 0.35 nor greater than 0.76 for calculation purposes

$$\lambda = \frac{b_{fc}}{2t_{fc}}$$

$\lambda_{pf} = \lambda_p$, the limiting width-to-thickness ratio for a compact flange as defined in Table B4.1b

$\lambda_{rf} = \lambda_r$, the limiting width-to-thickness ratio for a noncompact flange as defined in Table B4.1b

### 4. Tension Flange Yielding

(a) When $S_{xt} \geq S_{xc}$, the limit state of tension flange yielding does not apply.

(b) When $S_{xt} < S_{xc}$

$$M_n = R_{pt}M_{yt}$$ (F4-15)

where

$M_{yt}$ = yield moment in the tension flange, kip-in. (N-mm)
= $F_y S_{xt}$

$R_{pt}$, the web plastification factor corresponding to the tension flange yielding limit state, is determined as follows:

(1) When $I_{yc}/I_y > 0.23$

(i) When $\frac{h_c}{t_w} \leq \lambda_{pw}$

$$R_{pt} = \frac{M_p}{M_{yt}}$$ (F4-16a)

(ii) When $\frac{h_c}{t_w} > \lambda_{pw}$

$$R_{pt} = \left[\frac{M_p}{M_{yt}} - \left(\frac{M_p}{M_{yt}} - 1\right)\left(\frac{\lambda - \lambda_{pw}}{\lambda_{rw} - \lambda_{pw}}\right)\right] \leq \frac{M_p}{M_{yt}}$$ (F4-16b)

---

## OTHER I-SHAPED MEMBERS WITH COMPACT OR NONCOMPACT WEBS [Sect. F4.

(2) When $I_{yc}/I_y \leq 0.23$

$$R_{pt} = 1.0$$ (F4-17)

where

$M_p = F_y Z_x \leq 1.6F_y S_x$

$$\lambda = \frac{h}{t_w}$$

$\lambda_{pw} = \lambda_p$, the limiting width-to-thickness ratio for a compact web as defined in Table B4.1b

$\lambda_{rw} = \lambda_r$, the limiting width-to-thickness ratio for a noncompact web as defined in Table B4.1b

## F5. DOUBLY SYMMETRIC AND SINGLY SYMMETRIC I-SHAPED MEMBERS WITH SLENDER WEBS BENT ABOUT THEIR MAJOR AXIS

This section applies to doubly symmetric and singly symmetric I-shaped members with slender webs attached to the mid-width of the flanges and bent about their major axis as defined in Section B4.1 for flexure.

The nominal flexural strength, $M_n$, shall be the lowest value obtained according to the limit states of compression flange yielding, lateral-torsional buckling, compression flange local buckling, and tension flange yielding.

### 1. Compression Flange Yielding

$$M_n = R_{pg}F_y S_{xc}$$ (F5-1)

### 2. Lateral-Torsional Buckling

$$M_n = R_{pg}F_{cr}S_{xc}$$ (F5-2)

(a) When $L_b \leq L_p$, the limit state of lateral-torsional buckling does not apply.

(b) When $L_p < L_b \leq L_r$

$$F_{cr} = C_b\left[F_y - \left(0.3F_y\right)\left(\frac{L_b - L_p}{L_r - L_p}\right)\right] \leq F_y$$ (F5-3)

(c) When $L_b > L_r$

$$F_{cr} = \frac{C_b \pi^2 E}{\left(\frac{L_b}{r_t}\right)^2} \leq F_y$$ (F5-4)

where

$L_p$ is defined by Equation F4-7

$$L_r = \pi r_t\sqrt{\frac{E}{0.7F_y}}$$ (F5-5)

---

## I-SHAPED MEMBERS AND CHANNELS BENT ABOUT THEIR MINOR AXIS [Sect. F6.]

$r_t$ = effective radius of gyration for lateral-torsional buckling as defined in Section F4, in. (mm)

$R_{pg}$, the bending strength reduction factor, is

$$R_{pg} = 1 - \frac{a_w}{1{,}200 + 300a_w}\left(\frac{h_c}{t_w} - 5.7\sqrt{\frac{E}{F_y}}\right) \leq 1.0$$ (F5-6)

$a_w$ is defined by Equation F4-12, but shall not exceed 10

### 3. Compression Flange Local Buckling

$$M_n = R_{pg}F_{cr}S_{xc}$$ (F5-7)

(a) For sections with compact flanges, the limit state of compression flange local buckling does not apply.

(b) For sections with noncompact flanges

$$F_{cr} = F_y - \left(0.3F_y\right)\left(\frac{\lambda - \lambda_{pf}}{\lambda_{rf} - \lambda_{pf}}\right)$$ (F5-8)

(c) For sections with slender flanges

$$F_{cr} = \frac{0.9Ek_c}{\left(\frac{b_f}{2t_f}\right)^2}$$ (F5-9)

where

$k_c = \frac{4}{\sqrt{h/t_w}}$ and shall not be taken as less than 0.35 nor greater than 0.76 for calculation purposes

$$\lambda = \frac{b_{fc}}{2t_{fc}}$$

$\lambda_{pf} = \lambda_p$, the limiting width-to-thickness ratio for a compact flange as defined in Table B4.1b

$\lambda_{rf} = \lambda_r$, the limiting width-to-thickness ratio for a noncompact flange as defined in Table B4.1b

### 4. Tension Flange Yielding

(a) When $S_{xt} \geq S_{xc}$, the limit state of tension flange yielding does not apply.

(b) When $S_{xt} < S_{xc}$

$$M_n = F_y S_{xt}$$ (F5-10)

## F6. I-SHAPED MEMBERS AND CHANNELS BENT ABOUT THEIR MINOR AXIS

This section applies to I-shaped members and channels bent about their minor axis.

The nominal flexural strength, $M_n$, shall be the lower value obtained according to the limit states of yielding (plastic moment) and flange local buckling.

---

## I-SHAPED MEMBERS AND CHANNELS BENT ABOUT THEIR MINOR AXIS [Sect. F6.

### 1. Yielding

$$M_n = M_p = F_y Z_y \leq 1.6F_y S_y$$ (F6-1)

where

$S_y$ = elastic section modulus taken about the y-axis, in.$^3$ (mm$^3$)
$Z_y$ = plastic section modulus taken about the y-axis, in.$^3$ (mm$^3$)

### 2. Flange Local Buckling

(a) For sections with compact flanges, the limit state of flange local buckling does not apply.

**User Note:** For $F_y = 50$ ksi (345 MPa), all current ASTM A6/A6M W, S, M, C, and MC shapes except W21×48, W14×99, W14×90, W12×65, W10×12, W8×31, W8×10, W6×15, W6×9, W6×8.5, and M4×6 have compact flanges.

(b) For sections with noncompact flanges

$$M_n = M_p - \left(M_p - 0.70F_y S_y\right)\left(\frac{\lambda - \lambda_{pf}}{\lambda_{rf} - \lambda_{pf}}\right)$$ (F6-2)

(c) For sections with slender flanges

$$M_n = F_{cr} S_y$$ (F6-3)

where

$$F_{cr} = \frac{0.70E}{\left(\frac{b}{t_f}\right)^2}$$ (F6-4)

$b$ = for flanges of I-shaped members, half the full flange width, $b_f$ ; for flanges of channels, the full nominal dimension of the flange, in. (mm)

$t_f$ = thickness of the flange, in. (mm)

$$\lambda = \frac{b}{t_f}$$

$\lambda_{pf} = \lambda_p$, the limiting width-to-thickness ratio for a compact flange as defined in Table B4.1b

$\lambda_{rf} = \lambda_r$, the limiting width-to-thickness ratio for a noncompact flange as defined in Table B4.1b

## F7. SQUARE AND RECTANGULAR HSS AND BOX SECTIONS

This section applies to square and rectangular HSS, and box sections bent about either axis, having compact, noncompact, or slender webs or flanges, as defined in Section B4.1 for flexure.

The nominal flexural strength, $M_n$, shall be the lowest value obtained according to the limit states of yielding (plastic moment), flange local buckling, web local buckling, and lateral-torsional buckling under pure flexure.

---

## SQUARE AND RECTANGULAR HSS AND BOX SECTIONS [Sect. F7.]

### 1. Yielding

$$M_n = M_p = F_y Z$$ (F7-1)

where

$Z$ = plastic section modulus about the axis of bending, in.$^3$ (mm$^3$)

### 2. Flange Local Buckling

(a) For compact sections, the limit state of flange local buckling does not apply.

(b) For sections with noncompact flanges

$$M_n = M_p - \left(M_p - F_y S\right)\left(\frac{\lambda - \lambda_{pf}}{\lambda_{rf} - \lambda_{pf}}\right) \leq M_p$$ (F7-2)

where

$S$ = elastic section modulus about the axis of bending, in.$^3$ (mm$^3$)

$$\lambda = \frac{b}{t_f}$$

$b$ = width of compression flange as defined in Section B4.1b, in. (mm)
$t_f$ = thickness of the flange, in. (mm)
$\lambda_{pf} = \lambda_p$, the limiting width-to-thickness ratio for a compact flange as defined in Table B4.1b

$\lambda_{rf} = \lambda_r$, the limiting width-to-thickness ratio for a noncompact flange as defined in Table B4.1b

(c) For sections with slender flanges

$$M_n = F_y S_e$$ (F7-3)

where

$S_e$ = effective section modulus determined with the effective width, $b_e$, of the compression flange taken as follows:

(1) For HSS

$$b_e = 1.92t_f\sqrt{\frac{E}{F_y}}\left(1 - \frac{0.38}{b/t_f}\sqrt{\frac{E}{F_y}}\right) \leq b$$ (F7-4)

(2) For box sections

$$b_e = 1.92t_f\sqrt{\frac{E}{F_y}}\left(1 - \frac{0.34}{b/t_f}\sqrt{\frac{E}{F_y}}\right) \leq b$$ (F7-5)

### 3. Web Local Buckling

(a) For compact sections, the limit state of web local buckling does not apply.

(b) For sections with noncompact webs

$$M_n = M_p - \left(M_p - F_y S\right)\left(\frac{\lambda - \lambda_{pw}}{\lambda_{rw} - \lambda_{pw}}\right) \leq M_p$$ (F7-6)

---

## SQUARE AND RECTANGULAR HSS AND BOX SECTIONS [Sect. F7.

where

$$\lambda = \frac{h}{t_w}$$

$h$ = depth of web, as defined in Section B4.1b, in. (mm)
$t_w$ = thickness of the web, in. (mm)
$\lambda_{pw} = \lambda_p$, the limiting width-to-thickness ratio for a compact web as defined in Table B4.1b

$\lambda_{rw} = \lambda_r$, the limiting width-to-thickness ratio for a noncompact web as defined in Table B4.1b

(c) For sections with slender webs and compact or noncompact flanges

$$M_n = R_{pg}F_y S$$ (F7-7)

where

$R_{pg}$ is defined by Equation F5-6 with $a_w = 2ht_w/(bt_f)$

**User Note:** Box sections with slender webs and slender flanges are not addressed in this Specification.

**User Note:** There are no HSS with slender webs.

### 4. Lateral-Torsional Buckling

(a) When $L_b \leq L_p$, the limit state of lateral-torsional buckling does not apply.

(b) When $L_p < L_b \leq L_r$

$$M_n = C_b\left[M_p - \left(M_p - 0.7F_y S_x\right)\left(\frac{L_b - L_p}{L_r - L_p}\right)\right] \leq M_p$$ (F7-8)

(c) When $L_b > L_r$

$$M_n = 2EC_b\frac{\sqrt{JA_g}}{L_b/r_y} \leq M_p$$ (F7-9)

where

$A_g$ = gross area of member, in.$^2$ (mm$^2$)

$L_p$, the limiting laterally unbraced length for the limit state of yielding, in. (mm), is

$$L_p = 0.13Er_y\sqrt{\frac{JA_g}{M_p}}$$ (F7-10)

$L_r$, the limiting laterally unbraced length for the limit state of inelastic lateral-torsional buckling, in. (mm), is

$$L_r = 2Er_y\frac{\sqrt{JA_g}}{0.7F_y S_x}$$ (F7-11)

---

## TEES AND DOUBLE ANGLES LOADED IN THE PLANE OF SYMMETRY [Sect. F9.]

**User Note:** Lateral-torsional buckling will not occur in square sections or sections bending about their minor axis. In HSS sizes, deflection will usually control before there is a significant reduction in flexural strength due to lateral-torsional buckling. The same is true for box sections, and lateral-torsional buckling will usually only be a consideration for sections with high depth-to-width ratios.

## F8. ROUND HSS

This section applies to round HSS having $D/t$ ratios of less than $\frac{0.45E}{F_y}$.

The nominal flexural strength, $M_n$, shall be the lower value obtained according to the limit states of yielding (plastic moment) and local buckling.

### 1. Yielding

$$M_n = M_p = F_y Z$$ (F8-1)

### 2. Local Buckling

(a) For compact sections, the limit state of flange local buckling does not apply.

(b) For noncompact sections

$$M_n = \left[\frac{0.021E}{\left(\frac{D}{t}\right)} + F_y\right]S$$ (F8-2)

(c) For sections with slender walls

$$M_n = F_{cr}S$$ (F8-3)

where

$D$ = outside diameter of round HSS, in. (mm)

$$F_{cr} = \frac{0.33E}{\left(\frac{D}{t}\right)^2}$$ (F8-4)

$t$ = design wall thickness of HSS member, in. (mm)

## F9. TEES AND DOUBLE ANGLES LOADED IN THE PLANE OF SYMMETRY

This section applies to tees and double angles loaded in the plane of symmetry.

The nominal flexural strength, $M_n$, shall be the lowest value obtained according to the limit states of yielding (plastic moment), lateral-torsional buckling, flange local buckling, and local buckling of tee stems and double angle web legs.

### 1. Yielding

$$M_n = M_p$$ (F9-1)

---

## TEES AND DOUBLE ANGLES LOADED IN THE PLANE OF SYMMETRY [Sect. F9.

where

(a) For tee stems and web legs in tension

$$M_p = F_y Z_x \leq 1.6M_y$$ (F9-2)

where

$M_y$ = yield moment about the axis of bending, kip-in. (N-mm)
= $F_y S_x$ (F9-3)

(b) For tee stems in compression

$$M_p = M_y$$ (F9-4)

(c) For double angles with web legs in compression

$$M_p = 1.5M_y$$ (F9-5)

### 2. Lateral-Torsional Buckling

(a) For stems and web legs in tension

(1) When $L_b \leq L_p$, the limit state of lateral-torsional buckling does not apply.

(2) When $L_p < L_b \leq L_r$

$$M_n = M_p - \left(M_p - M_y\right)\left(\frac{L_b - L_p}{L_r - L_p}\right)$$ (F9-6)

(3) When $L_b > L_r$

$$M_n = M_{cr}$$ (F9-7)

where

$$L_p = 1.76r_y\sqrt{\frac{E}{F_y}}$$ (F9-8)

$$L_r = 1.95\left(\frac{E}{F_y}\right)\sqrt{\frac{I_y J}{S_x}}\sqrt{2.36\left(\frac{F_y}{E}\right)\frac{dS_x}{J} + 1}$$ (F9-9)

$$M_{cr} = \frac{1.95E}{L_b}\sqrt{I_y J}\left(B + \sqrt{1 + B^2}\right)$$ (F9-10)

$$B = 2.3\left(\frac{d}{L_b}\right)\sqrt{\frac{I_y}{J}}$$ (F9-11)

$d$ = depth of tee or width of web leg in tension, in. (mm)

(b) For stems and web legs in compression anywhere along the unbraced length, $M_{cr}$ is given by Equation F9-10 with

$$B = -2.3\left(\frac{d}{L_b}\right)\sqrt{\frac{I_y}{J}}$$ (F9-12)

where

$d$ = depth of tee or width of web leg in compression, in. (mm)

---

## TEES AND DOUBLE ANGLES LOADED IN THE PLANE OF SYMMETRY [Sect. F9.]

(1) For tee stems

$$M_n = M_{cr} \leq M_y$$ (F9-13)

(2) For double-angle web legs, $M_n$ shall be determined using Equations F10-2 and F10-3 with $M_{cr}$ determined using Equation F9-10 and $M_y$ determined using Equation F9-3.

### 3. Flange Local Buckling of Tees and Double-Angle Legs

(a) For tee flanges

(1) For sections with a compact flange in flexural compression, the limit state of flange local buckling does not apply.

(2) For sections with a noncompact flange in flexural compression

$$M_n = \left[M_p - \left(M_p - 0.7F_y S_{xc}\right)\left(\frac{\lambda - \lambda_{pf}}{\lambda_{rf} - \lambda_{pf}}\right)\right] \leq 1.6M_y$$ (F9-14)

(3) For sections with a slender flange in flexural compression

$$M_n = \frac{0.7ES_{xc}}{\left(\frac{b_f}{2t_f}\right)^2}$$ (F9-15)

where

$S_{xc}$ = elastic section modulus referred to the compression flange, in.$^3$ (mm$^3$)

$$\lambda = \frac{b_f}{2t_f}$$

$\lambda_{pf} = \lambda_p$, the limiting width-to-thickness ratio for a compact flange as defined in Table B4.1b

$\lambda_{rf} = \lambda_r$, the limiting width-to-thickness ratio for a noncompact flange as defined in Table B4.1b

(b) For double-angle flange legs

The nominal flexural strength, $M_n$, for double angles with the flange legs in compression shall be determined in accordance with Section F10.3, with $S_c$ referred to the compression flange.

### 4. Local Buckling of Tee Stems and Double-Angle Web Legs in Flexural Compression

(a) For tee stems

$$M_n = F_{cr}S_x$$ (F9-16)

where

$S_x$ = elastic section modulus taken about the x-axis, in.$^3$ (mm$^3$)
$F_{cr}$, the critical stress, is determined as follows:

(1) When $\frac{d}{t_w} \leq 0.84\sqrt{\frac{E}{F_y}}$

---

## TEES AND DOUBLE ANGLES LOADED IN THE PLANE OF SYMMETRY [Sect. F9.

$$F_{cr} = F_y$$ (F9-17)

(2) When $0.84\sqrt{\frac{E}{F_y}} < \frac{d}{t_w} \leq 1.52\sqrt{\frac{E}{F_y}}$

$$F_{cr} = \left(1.43 - 0.515\frac{d}{t_w}\sqrt{\frac{F_y}{E}}\right)F_y$$ (F9-18)

(3) When $\frac{d}{t_w} > 1.52\sqrt{\frac{E}{F_y}}$

$$F_{cr} = \frac{1.52E}{\left(\frac{d}{t_w}\right)^2}$$ (F9-19)

(b) For double-angle web legs

The nominal flexural strength, $M_n$, for double angles with the web legs in compression shall be determined in accordance with Section F10.3, with $S_c$ taken as the elastic section modulus.

## F10. SINGLE ANGLES

This section applies to single angles with and without continuous lateral restraint along their length.

Single angles with continuous lateral-torsional restraint along the length are permitted to be designed on the basis of geometric axis (x, y) bending. Single angles without continuous lateral-torsional restraint along the length shall be designed using the provisions for principal axis bending except where the provision for bending about a geometric axis is permitted.

If the moment resultant has components about both principal axes, with or without axial load, or the moment is about one principal axis and there is axial load, the combined stress ratio shall be determined using the provisions of Section H2.

**User Note:** For geometric axis design, use section properties computed about the x- and y-axis of the angle, parallel and perpendicular to the legs. For principal axis design, use section properties computed about the major and minor principal axes of the angle.

The nominal flexural strength, $M_n$, shall be the lowest value obtained according to the limit states of yielding (plastic moment), lateral-torsional buckling, and leg local buckling.

**User Note:** For bending about the minor principal axis, only the limit states of yielding and leg local buckling apply.

---

## SINGLE ANGLES [Sect. F10.]

### 1. Yielding

$$M_n = 1.5M_y$$ (F10-1)

### 2. Lateral-Torsional Buckling

For single angles without continuous lateral-torsional restraint along the length

(a) When $\frac{M_y}{M_{cr}} \leq 1.0$

$$M_n = \left(1.92 - 1.17\sqrt{\frac{M_y}{M_{cr}}}\right)M_y \leq 1.5M_y$$ (F10-2)

(b) When $\frac{M_y}{M_{cr}} > 1.0$

$$M_n = \left(0.92 - \frac{0.17M_{cr}}{M_y}\right)M_{cr}$$ (F10-3)

where

$M_{cr}$, the elastic lateral-torsional buckling moment, is determined as follows:

(1) For bending about the major principal axis of single angles

$$M_{cr} = \frac{9EA_g r_z lC_b}{8L_b}\left[\sqrt{1 + \left(4.4\frac{\beta_w r_z}{L_b t}\right)^2} + 4.4\frac{\beta_w r_z}{L_b t}\right]$$ (F10-4)

where

$C_b$ is computed using Equation F1-1 with a maximum value of 1.5
$A_g$ = gross area of angle, in.$^2$ (mm$^2$)
$L_b$ = laterally unbraced length of member, in. (mm)
$r_z$ = radius of gyration about the minor principal axis, in. (mm)
$t$ = thickness of angle leg, in. (mm)
$\beta_w$ = section property for single angles about major principal axis, in. (mm).
$\beta_w$ is positive with short legs in compression and negative with long legs in compression for unequal-leg angles, and zero for equal-leg angles. If the long leg is in compression anywhere along the unbraced length of the member, the negative value of $\beta_w$ shall be used.

**User Note:** The equation for $\beta_w$ and values for common angle sizes are listed in the Commentary.

(2) For bending about one of the geometric axes of an equal-leg angle with no axial compression

(i) With no lateral-torsional restraint

(a) With maximum compression at the toe

$$M_{cr} = \frac{0.58Eb^4tC_b}{L_b^2}\left[\sqrt{1 + 0.88\left(\frac{L_b t}{b^2}\right)^2} - 1\right]$$ (F10-5a)

---

## SINGLE ANGLES [Sect. F10.

(b) With maximum tension at the toe

$$M_{cr} = \frac{0.58Eb^4tC_b}{L_b^2}\left[\sqrt{1 + 0.88\left(\frac{L_b t}{b^2}\right)^2} + 1\right]$$ (F10-5b)

where

$M_y$ shall be taken as 0.80 times the yield moment calculated using the geometric section modulus.

$b$ = width of leg, in. (mm)

(ii) With lateral-torsional restraint at the point of maximum moment only:

$M_{cr}$ shall be taken as 1.25 times $M_{cr}$ computed using Equation F10-5a or F10-5b.

$M_y$ shall be taken as the yield moment calculated using the geometric section modulus.

**User Note:** $M_n$ may be taken as $M_y$ for single angles with their vertical leg toe in compression, and having a span-to-depth ratio less than or equal to

$$\frac{1.64E}{F_y}\sqrt{\left(\frac{t}{b}\right)^2 - 1.4\frac{F_y}{E}}$$

### 3. Leg Local Buckling

The limit state of leg local buckling applies when the toe of the leg is in compression.

(a) For compact sections, the limit state of leg local buckling does not apply.

(b) For sections with noncompact legs

$$M_n = F_y S_c\left[2.43 - 1.72\left(\frac{b}{t}\right)\sqrt{\frac{F_y}{E}}\right]$$ (F10-6)

(c) For sections with slender legs

$$M_n = F_{cr} S_c$$ (F10-7)

where

$$F_{cr} = \frac{0.71E}{\left(\frac{b}{t}\right)^2}$$ (F10-8)

$S_c$ = elastic section modulus to the toe in compression relative to the axis of bending, in.$^3$ (mm$^3$). For bending about one of the geometric axes of an equal-leg angle with no lateral-torsional restraint, $S_c$ shall be 0.80 of the geometric axis section modulus.

$b$ = full width of leg in compression, in. (mm)

---

## UNSYMMETRICAL SHAPES [Sect. F12.]

## F11. RECTANGULAR BARS AND ROUNDS

This section applies to rectangular bars bent about either geometric axis, and rounds.

The nominal flexural strength, $M_n$, shall be the lower value obtained according to the limit states of yielding (plastic moment) and lateral-torsional buckling.

### 1. Yielding

For rectangular bars

$$M_n = M_p = F_y Z \leq 1.5F_y S_x$$ (F11-1)

For rounds

$$M_n = M_p = F_y Z \leq 1.6F_y S_x$$ (F11-2)

### 2. Lateral-Torsional Buckling

(a) For rectangular bars with $\frac{L_b d}{t^2} \leq \frac{0.08E}{F_y}$ bent about their major axis, rectangular bars bent about their minor axis, and rounds, the limit state of lateral-torsional buckling does not apply.

(b) For rectangular bars with $\frac{0.08E}{F_y} < \frac{L_b d}{t^2} \leq \frac{1.9E}{F_y}$ bent about their major axis

$$M_n = C_b\left[1.52 - 0.274\left(\frac{L_b d}{t^2}\right)\frac{F_y}{E}\right]M_y \leq M_p$$ (F11-3)

where

$L_b$ = length between points that are either braced against lateral displacement of the compression region, or between points braced to prevent twist of the cross section, in. (mm)

(c) For rectangular bars with $\frac{L_b d}{t^2} > \frac{1.9E}{F_y}$ bent about their major axis

$$M_n = F_{cr}S_x \leq M_p$$ (F11-4)

where

$$F_{cr} = \frac{1.9EC_b}{\frac{L_b d}{t^2}}$$ (F11-5)

## F12. UNSYMMETRICAL SHAPES

This section applies to all unsymmetrical shapes except single angles.

The nominal flexural strength, $M_n$, shall be the lowest value obtained according to the limit states of yielding (yield moment), lateral-torsional buckling, and local buckling where

$$M_n = F_n S_{min}$$ (F12-1)

---

## UNSYMMETRICAL SHAPES [Sect. F12.

where

$S_{min}$ = minimum elastic section modulus relative to the axis of bending, in.$^3$ (mm$^3$)

**User Note:** The design provisions within this section can be overly conservative for certain shapes, unbraced lengths, and moment diagrams. To improve economy, the provisions of Appendix 1.3 are recommended as an alternative for determining the nominal flexural strength of members of unsymmetrical shape.

### 1. Yielding

$$F_n = F_y$$ (F12-2)

### 2. Lateral-Torsional Buckling

$$F_n = F_{cr} \leq F_y$$ (F12-3)

where

$F_{cr}$ = lateral-torsional buckling stress for the section as determined by analysis, ksi (MPa)

**User Note:** In the case of Z-shaped members, it is recommended that $F_{cr}$ be taken as $0.5F_{cr}$ of a channel with the same flange and web properties.

### 3. Local Buckling

$$F_n = F_{cr} \leq F_y$$ (F12-4)

where

$F_{cr}$ = local buckling stress for the section as determined by analysis, ksi (MPa)

## F13. PROPORTIONS OF BEAMS AND GIRDERS

### 1. Strength Reductions for Members with Bolt Holes in the Tension Flange

This section applies to rolled or built-up shapes and cover-plated beams with standard and oversized bolt holes or short- and long-slotted bolt holes parallel to the direction of load, proportioned on the basis of flexural strength of the gross section.

In addition to the limit states specified in other sections of this chapter, the nominal flexural strength, $M_n$, shall be limited according to the limit state of tensile rupture of the tension flange.

(a) When $F_u A_{fn} \geq Y_t F_y A_{fg}$, the limit state of tensile rupture does not apply.

(b) When $F_u A_{fn} < Y_t F_y A_{fg}$, the nominal flexural strength, $M_n$, at the location of the holes in the tension flange shall not be taken as greater than

$$M_n = \frac{F_u A_{fn}}{A_{fg}}S_x$$ (F13-1)

where

$A_{fg}$ = gross area of tension flange, calculated in accordance with Section B4.3a, in.$^2$ (mm$^2$)

---

## PROPORTIONS OF BEAMS AND GIRDERS [Sect. F13.]

$A_{fn}$ = net area of tension flange, calculated in accordance with Section B4.3b, in.$^2$ (mm$^2$)
$F_u$ = specified minimum tensile strength, ksi (MPa)
$S_x$ = minimum elastic section modulus taken about the x-axis, in.$^3$ (mm$^3$)
$Y_t = 1.0$ for $F_y/F_u \leq 0.8$
= 1.1 otherwise

### 2. Proportioning Limits for I-Shaped Members

Singly symmetric I-shaped members shall satisfy the following limit:

$$0.1 \leq \frac{I_{yc}}{I_y} \leq 0.9$$ (F13-2)

Singly and doubly symmetric I-shaped members with slender webs shall satisfy the following limits:

(a) When $\frac{a}{h} \leq 1.5$

$$\left(\frac{h}{t_w}\right)_{max} = 12.0\sqrt{\frac{E}{F_y}}$$ (F13-3)

(b) When $\frac{a}{h} > 1.5$

$$\left(\frac{h}{t_w}\right)_{max} = \frac{0.40E}{F_y}$$ (F13-4)

where

$a$ = clear distance between transverse stiffeners, in. (mm)

In unstiffened girders, $h/t_w$ shall not exceed 260. The ratio of 2 times the web area in compression to the compression flange area, $a_w$, as defined by Equation F4-12, shall not exceed 10.

### 3. Cover Plates

(a) For members with cover plates, the following provisions apply: Flanges of welded beams or girders are permitted to be varied in thickness or width by splicing a series of plates or by the use of cover plates.

(b) High-strength bolts or welds connecting flange to web, or cover plate to flange, shall be proportioned to resist the total horizontal shear resulting from bending forces on the girder. The longitudinal distribution of these bolts or intermittent welds shall be in proportion to the intensity of the shear.

(c) However, the longitudinal spacing shall not exceed the maximum specified for compression or tension members in Section E6 or D4, respectively. Bolts or welds connecting flange to web shall also be proportioned to transmit to the web any loads applied directly to the flange, unless provision is made to transmit such loads by direct bearing.

(d) Partial-length cover plates shall be extended beyond the theoretical cutoff point and the extended portion shall be attached to the beam or girder by high-strength

---

## PROPORTIONS OF BEAMS AND GIRDERS [Sect. F13.

bolts in a slip-critical connection or fillet welds. The attachment shall, at the applicable strength given in Section J2.2, J3.9, or B3.11, develop the cover plate's portion of the flexural strength in the beam or girder at the theoretical cutoff point.

(e) For welded cover plates, the welds connecting the cover plate termination to the beam or girder shall be continuous welds along both edges of the cover plate in the length $a'$, defined in the following, and shall develop the cover plate's portion of the available strength of the beam or girder at the distance $a'$ from the end of the cover plate.

(1) When there is a continuous weld equal to or larger than three-fourths of the plate thickness across the end of the plate

$$a' = w$$ (F13-5)

where

$w$ = width of cover plate, in. (mm)

(2) When there is a continuous weld smaller than three-fourths of the plate thickness across the end of the plate

$$a' = 1.5w$$ (F13-6)

(3) When there is no weld across the end of the plate

$$a' = 2w$$ (F13-7)

### 4. Built-Up Beams

Where two or more beams or channels are used side by side to form a flexural member, they shall be connected together in compliance with Section E6.2. When concentrated loads are carried from one beam to another or distributed between the beams, diaphragms having sufficient stiffness to distribute the load shall be welded or bolted between the beams.

---
