# Chapter F: Flexure

**AISC Specification v16.0 - Design Examples**
**Original PDF Pages**: 163-236 (74 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Design of Members for Flexure

**Examples Included**: ['F.1A~F.14: Flexural member examples']

---

## Table of Contents

- [EXAMPLE F.1-2A W-SHAPE FLEXURAL MEMBER DESIGN IN MAJOR-AXIS BENDING, BRACED AT THIRD POINTS](#example-f1-2a-w-shape-flexural-member-design-in-major-axis-bending,-braced-at-third-points)
- [EXAMPLE F.1-2B W-SHAPE FLEXURAL MEMBER DESIGN IN MAJOR-AXIS BENDING, BRACED AT THIRD POINTS](#example-f1-2b-w-shape-flexural-member-design-in-major-axis-bending,-braced-at-third-points)
- [EXAMPLE F.1-3A W-SHAPE FLEXURAL MEMBER DESIGN IN MAJOR-AXIS BENDING, BRACED AT MIDSPAN](#example-f1-3a-w-shape-flexural-member-design-in-major-axis-bending,-braced-at-midspan)
- [EXAMPLE F.1-3B W-SHAPE FLEXURAL MEMBER DESIGN IN MAJOR-AXIS BENDING, BRACED AT MIDSPAN](#example-f1-3b-w-shape-flexural-member-design-in-major-axis-bending,-braced-at-midspan)
- [EXAMPLE F.2-1A COMPACT CHANNEL FLEXURAL MEMBER, CONTINUOUSLY BRACED](#example-f2-1a-compact-channel-flexural-member,-continuously-braced)
- [EXAMPLE F.2-1B COMPACT CHANNEL FLEXURAL MEMBER, CONTINUOUSLY BRACED](#example-f2-1b-compact-channel-flexural-member,-continuously-braced)
- [EXAMPLE F.2-2A COMPACT CHANNEL FLEXURAL MEMBER WITH BRACING AT ENDS AND FIFTH POINTS](#example-f2-2a-compact-channel-flexural-member-with-bracing-at-ends-and-fifth-points)
- [EXAMPLE F.2-2B COMPACT CHANNEL FLEXURAL MEMBER WITH BRACING AT ENDS AND FIFTH POINTS](#example-f2-2b-compact-channel-flexural-member-with-bracing-at-ends-and-fifth-points)
- [EXAMPLE F.3A W-SHAPE FLEXURAL MEMBER WITH NONCOMPACT FLANGES IN MAJOR-AXIS BENDING](#example-f3a-w-shape-flexural-member-with-noncompact-flanges-in-major-axis-bending)
- [EXAMPLE F.3B W-SHAPE FLEXURAL MEMBER WITH NONCOMPACT FLANGES IN MAJOR-AXIS BENDING](#example-f3b-w-shape-flexural-member-with-noncompact-flanges-in-major-axis-bending)
- [EXAMPLE F.4 W-SHAPE FLEXURAL MEMBER, SELECTION BY MOMENT OF INERTIA FOR MAJOR-AXIS BENDING](#example-f4-w-shape-flexural-member,-selection-by-moment-of-inertia-for-major-axis-bending)
- [EXAMPLE F.5 I-SHAPED FLEXURAL MEMBER IN MINOR-AXIS BENDING](#example-f5-i-shaped-flexural-member-in-minor-axis-bending)
- [EXAMPLE F.6 SQUARE HSS FLEXURAL MEMBER WITH COMPACT FLANGES](#example-f6-square-hss-flexural-member-with-compact-flanges)
- [EXAMPLE F.7A RECTANGULAR HSS FLEXURAL MEMBER WITH NONCOMPACT FLANGES](#example-f7a-rectangular-hss-flexural-member-with-noncompact-flanges)
- [EXAMPLE F.7B RECTANGULAR HSS FLEXURAL MEMBER WITH NONCOMPACT FLANGES](#example-f7b-rectangular-hss-flexural-member-with-noncompact-flanges)
- [EXAMPLE F.8A SQUARE HSS FLEXURAL MEMBER WITH SLENDER FLANGES](#example-f8a-square-hss-flexural-member-with-slender-flanges)
- [EXAMPLE F.8B SQUARE HSS FLEXURAL MEMBER WITH SLENDER FLANGES](#example-f8b-square-hss-flexural-member-with-slender-flanges)
- [EXAMPLE F.9A PIPE FLEXURAL MEMBER](#example-f9a-pipe-flexural-member)
- [EXAMPLE F.9B PIPE FLEXURAL MEMBER](#example-f9b-pipe-flexural-member)
- [EXAMPLE F.10 WT-SHAPE FLEXURAL MEMBER](#example-f10-wt-shape-flexural-member)
- [EXAMPLE F.11A SINGLE-ANGLE FLEXURAL MEMBER WITH BRACING AT ENDS ONLY](#example-f11a-single-angle-flexural-member-with-bracing-at-ends-only)
- [EXAMPLE F.11B SINGLE-ANGLE FLEXURAL MEMBER WITH BRACING AT ENDS AND MIDSPAN](#example-f11b-single-angle-flexural-member-with-bracing-at-ends-and-midspan)
- [EXAMPLE F.11C SINGLE-ANGLE FLEXURAL MEMBER WITH VERTICAL AND HORIZONTAL LOADING](#example-f11c-single-angle-flexural-member-with-vertical-and-horizontal-loading)
- [EXAMPLE F.12 RECTANGULAR BAR IN MAJOR-AXIS BENDING](#example-f12-rectangular-bar-in-major-axis-bending)
- [EXAMPLE F.13 ROUND BAR IN BENDING](#example-f13-round-bar-in-bending)
- [EXAMPLE F.14 PLATE GIRDER FLEXURAL MEMBER](#example-f14-plate-girder-flexural-member)

---

# Chapter F
# Design of Members for Flexure

**INTRODUCTION**

This chapter contains example provisions for calculating the flexural strength of members subject to simple bending about one principal axis. Included are specific provisions for I-shaped members, channels, HSS, box sections, tees, double angles, solid rectangular bars and rounds, and single angles. Also included is a discussion of proportioning limits for members used as beams.

There are selection tables in Parts 3 and 4 of the AISC *Manual* for standard beams in the commonly available yield strengths. These tables give beam spans, uniform loads per unit length of beam, total safe loads, moment of inertia, and other section properties. Also included in Part 4 are tabulated values of beam design properties, factored uniform loads, and available moment for LRFD and ASD, respectively.

Most of the formulas from this chapter are illustrated in the following examples. The design and selection procedures developed in the examples for both LRFD and ASD are applicable to singly symmetric or doubly symmetric shapes.

## F1. GENERAL PROVISIONS

Design and evaluation of flexural members is based on deflection requirements and strength, which is determined as the lesser of the design flexural strength, $\phi_b M_n$, or the allowable flexural strength, $M_n/\Omega_b$,

where

$M_n$ = the lowest nominal flexural strength based on the limit states of yielding, lateral torsional-buckling, and local buckling. (from *Spec.* Eq. F1-1)
$\phi_b = 0.90$ (LRFD)
$\Omega_b = 1.67$ (ASD)

This design approach is followed in all examples.

The term, $L_b$, is used throughout this chapter to describe the length between points which are either braced against lateral displacement of the compression flange or braced against twist of the cross section. Requirements for bracing of the tension flange are based upon specific cases which involve conditions such as point loads at the bottom of the span.

The use of $C_b$ is illustrated in several of the following examples. AISC *Manual* Table 3-1 provides tabulated $C_b$ values for some common sections.

## F2. DOUBLY SYMMETRIC COMPACT I-SHAPED MEMBERS AND CHANNELS BENT ABOUT THEIR MAJOR AXIS

AISC *Specification* Section F2 applies to the design of compact beams and channels. As indicated in F2.1, use Note in the *Specification*, "... The horizontal axis parameter is $\lambda = b_f / 2t_f$. For channels, left out of the left flange and bottom flange in the plane of the web shall be included in design calculations. The strength is based on the limit states of yielding, lateral-torsional buckling, and compression-flange local buckling. Compression-flange local buckling, in the range where the strength is limited by flexural yielding. In this region, the nominal strength is taken as the full plastic moment strength of the section as given by AISC *Specification* Equation F2.1. In the range of the curve in between, local buckling of the compression flange may occur (inelastic-flange local buckling), and is treated using AISC *Specification* Equation F2.2. Between these regions, within the linear region of the curve between $M_p = M_r$ at $L_r$, for the left end of $\lambda = b_f / 2t_f = \lambda_p$ at the right, the strength is limited by inelastic buckling. The strength in this portion of the curve is given by AISC *Specification* Equation F2.2.

---

The curve plotted in Figure F-1 as a heavy solid line represents the case where $C_b = 1.0$, while the heavy dashed line represents the case where $C_b$ exceeds 1.0. The nominal strengths calculated in both AISC *Specification* Equations F2-2 and F2-3 are linearly proportional to $C_b$, but are limited to $M_p$ as shown in the figure.

$$M_n = M_p = F_y Z_x$$
(*Spec.* Eq. F2-1)

$$M_n = C_b\left[M_p - (M_p - 0.7F_y S_x)\left(\frac{L_b - L_p}{L_r - L_p}\right)\right] \leq M_p$$
(*Spec.* Eq. F2-2)

$$M_n = F_{cr}S_x \leq M_p$$
(*Spec.* Eq. F2-3)

where

$$F_{cr} = \frac{C_b \pi^2 E}{\left(\frac{L_b}{r_{ts}}\right)^2}\sqrt{1 + 0.078\frac{Jc}{S_x h_o}\left(\frac{L_b}{r_{ts}}\right)^2}$$
(*Spec.* Eq. F2-4)

The provisions of this section are illustrated in Examples F.1-1A to F.1-3B (W-shape beam) and Examples F.2-1A to F.2-2B (channel).

Inelastic design provisions are given in AISC *Specification* Appendix 1. $L_{pb}$, the maximum unbraced length for prismatic member segments containing plastic hinges is less than $L_p$.

## F3. DOUBLY SYMMETRIC I-SHAPED MEMBERS WITH COMPACT WEBS AND NONCOMPACT OR SLENDER FLANGES BENT ABOUT THEIR MAJOR AXIS

The strength of shapes designed according to this section is limited by local buckling of the compression flange. Only a few standard wide-flange shapes have noncompact flanges. For these sections, the strength reduction for $F_y = 50$ ksi steel varies. The approximate percentages of $M_p$ about the strong axis that can be developed by noncompact members when braced such that $L_b \leq L_p$ are shown as follows:

W21×48 = 99%       W14×99 = 99%       W14×90 = 97%       W12×65 = 98%
W10×12 = 99%       W8×31  = 99%       W8×10  = 99%       W6×15  = 94%
W6×8.5 = 98%

![Diagram: Graph showing nominal flexural strength $M_n$ versus unbraced length $L_b$, with curves labeled Eq. F2-1, Eq. F2-2, and Eq. F2-3. Horizontal line at $0.7F_y S_x$, critical points at $L_p$ and $L_r$, showing "$M_n$ with $C_b = 1.0$" and "$M_n$ with $C_b > 1.0$"]

*Fig. F-1. Nominal flexural strength versus unbraced length.*

---

The strength curve for the flange local buckling limit state, shown in Figure F-2, is similar in nature to that of the lateral-torsional buckling curve. The horizontal axis parameter is $\lambda = b_f / 2t_f$. The flat portion of the curve to the left of $\lambda_{pf}$ is the plastic yielding strength, $M_p$. The curved portion to the right of $\lambda_{rf}$ is the strength limited by elastic buckling of the flange. The linear transition between these two regions is the strength limited by inelastic flange buckling.

$$M_n = M_p = F_y Z_x$$
(*Spec.* Eq. F2-1)

$$M_n = M_p - (M_p - 0.7F_y S_x)\left(\frac{\lambda - \lambda_{pf}}{\lambda_{rf} - \lambda_{pf}}\right)$$
(*Spec.* Eq. F3-1)

$$M_n = \frac{0.9Ek_c S_x}{\lambda^2}$$
(*Spec.* Eq. F3-2)

where

$$k_c = \frac{4}{\sqrt{h/t_w}}$$ and shall not be taken less than 0.35 nor greater than 0.76 for calculation purposes.

The strength reductions due to flange local buckling of the few standard rolled shapes with noncompact flanges are incorporated into the design tables in Part 3 and Part 6 of the AISC *Manual*.

There are no standard I-shaped members with slender flanges. The noncompact flange provisions of this section are illustrated in Examples F.3A and F.3B.

## F4. OTHER I-SHAPED MEMBERS WITH COMPACT OR NONCOMPACT WEBS BENT ABOUT THEIR MAJOR AXIS

This section of the AISC *Specification* applies to doubly symmetric I-shaped members bent about their major axis with noncompact webs and singly symmetric I-shaped members (those having different flanges) with compact or noncompact webs.

## F5. DOUBLY SYMMETRIC AND SINGLY SYMMETRIC I-SHAPED MEMBERS WITH SLENDER WEBS BENT ABOUT THEIR MAJOR AXIS

This section applies to doubly symmetric and singly symmetric I-shaped members bent about their major axis with slender webs, formerly designated as "plate girders".

![Diagram: Graph showing nominal flexural strength $M_n$ versus $\frac{b_f}{2t_f}$, with horizontal line at $M_p$, dashed line at $0.7F_y S_x$, curves labeled Eq. F2-1, Eq. F3-1, and Eq. F3-2, critical points at $\lambda_{pf}$ and $\lambda_{rf}$]

*Fig. F-2. Flange local buckling strength.*

## F6. I-SHAPED MEMBERS AND CHANNELS BENT ABOUT THEIR MINOR AXIS

---

I-shaped members and channels bent about their minor axis are not subject to lateral-torsional buckling. Rolled or built-up shapes may have compact or slender flanges. For these sections, AISC *Specification* Table B4.1b must be consulted for the applicable $\lambda_p$ and $\lambda_r$.

The vast majority of W, M, C, and MC shapes have compact flanges, and can therefore develop the full plastic moment strength of the section as illustrated in Example F.6A. The provisions of this section are illustrated in Example F.6.

## F7. SQUARE AND RECTANGULAR HSS AND BOX SECTIONS

Square and rectangular HSS and box sections have no provisions for yielding, and flange and web local buckling. Lateral-torsional buckling is also possible for rectangular HSS or box sections bent about the strong axis; however, in order for a compact section to be susceptible to lateral-torsional buckling, the web must partially separate from the flange. This is not possible with square or rectangular HSS or welded box sections, which are continuously sealed, and therefore, do not require lateral-torsional buckling checks. The design and selection of rectangular HSS and box sections are illustrated in Examples F.8. The provisions for a rectangular HSS with noncompact flanges are illustrated in Example F.9A, and the provisions for a rectangular HSS with slender flanges are illustrated in Example F.9B. Rectangular HSS members of the same size as those from ASTM A1065/A1065M material, the design wall thickness may be slighty less than the nominal wall thickness.

## F8. HSS AND BOX-SHAPED MEMBERS WITH COMPACT OR NONCOMPACT WEBS BENT ABOUT THE MAJOR AXIS

The definition of HSS encompasses both tube and pipe products. The lateral-torsional buckling limit state does not apply. The limit states of yielding, local buckling, and web local buckling must be evaluated. AISC *Specification* Equation F8-2 is applicable for tubes having noncompact webs of round HSS and rectangular box sections having compact webs. The strengths of these shapes in the AISC *Manual* are calculated using a design wall thickness of 93% of the nominal wall thickness due to rolling tolerance. Design strengths, based on the measured wall thickness of members are specified in the *Specification*. The thicknesses and strengths of tube members in the AISC *Manual* are calculated using wall thickness at 93% of the nominal wall thickness. The strength of tube members obtained from the AISC *Manual* are calculated using a design wall thickness of 93% for rectangular HSS and 87% for round HSS.

## F9. TEES AND DOUBLE ANGLES LOADED IN THE PLANE OF SYMMETRY

The AISC *Specification* defines the nominal flexural strength, $M_n$, of a WT or double angle section loaded in a manner such that a compression in slender flange is in compression due to flexure. This limit state will seldom govern. A check for local buckling of the tee stem is local required unless it is added to the *Specification*, F9.2. The provisions were expanded to include double angles (see Figure F9.2 in the AISC *Specification*). Because the shape behaves similarly should be given to test conditions of tees to avoid undesired fixed-end moments that induce compression in the tension flange and vice versa. The design of a WT section is illustrated in Example F.10.

## F10. SINGLE ANGLES

Section F10 of the AISC *Specification* permits the flexural design of single angles using either the principal axis ($w$-$w$ and $z$-$z$ axis), the geometric axis ($x$-$x$ and $y$-$y$ axis), or unsymmetric bending, where single angles will be loaded laterally causing both geometric axes to deflect. The geometric axis design approach follows the traditional approach, using the geometric axis design provisions. $M$ must be multiplied by 0.80 for use in Equations F10-1, F10-2, and F10-3. The design of a single angle using unsymmetric bending is illustrated in Examples F.11-1A and F.11-1B.

The AISC *Manual* does not include design tables for these shapes. The local buckling limit state does not apply to any legs. With the exception of rectangular box bent about the major axis, solid square, rectangular, and round bars should not be subject to lateral-torsional buckling and are governed by the yielding limit state only. Rectangular bars bent about the minor axis are subject to lateral-torsional buckling and are checked for this limit state with Equations F11-3 and F11-4. Round bars develop the plastic moment.

---

These provisions can be used to check plates and webs of tees in connections. A design example of a rectangular bar in bending is illustrated in Example F.12. A design example of a round bar in bending is illustrated in Example F.13.

## F12. UNSYMMETRICAL SHAPES

Due to the wide range of possible unsymmetrical cross sections, specific lateral-torsional and local buckling provisions are not provided in this *Specification* section. A general template is provided, but appropriate literature investigation and engineering judgment are required for the application of this section.

## F13. PROPORTIONS OF BEAMS AND GIRDERS

This section of the *Specification* includes a limit state check for tensile rupture due to bolt holes in the tension flange of beams, proportioning limits for I-shaped members, detail requirements for cover plates and connection requirements for built-up beams connected side-to-side.

---

# EXAMPLE F.1-1A W-SHAPE FLEXURAL MEMBER DESIGN IN MAJOR-AXIS BENDING, CONTINUOUSLY BRACED

## Given:

Select a W-shape beam for the span and uniform dead and live loads shown in Figure F.1-1A. Limit the member to a maximum nominal depth of 18 in. Limit the live load deflection to $L/360$. The beam is simply supported and continuously braced. The beam is ASTM A992/A992M material.

![Diagram: Simply supported beam with continuous bracing along length, span $L = 35'-0"$, uniform loads $w_D = 0.45$ kip/ft and $w_L = 0.75$ kip/ft, supports at both ends]

*Fig. F.1-1A. Beam loading and bracing diagram.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50$ ksi

From Chapter 2 of ASCE/SEI 7, the required flexural strength is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.45 \text{ kip/ft}) + 1.6(0.75 \text{ kip/ft})$ | $w_a = 0.45 \text{ kip/ft} + 0.75 \text{ kip/ft}$ |
| $= 1.74$ kip/ft | $= 1.20$ kip/ft |
| From AISC *Manual* Table 3-22, Case 1: | From AISC *Manual* Table 3-22, Case 1: |
| $M_u = \frac{w_u L^2}{8}$ | $M_a = \frac{w_a L^2}{8}$ |
| $= \frac{(1.74 \text{ kip/ft})(35 \text{ ft})^2}{8}$ | $= \frac{(1.20 \text{ kip/ft})(35 \text{ ft})^2}{8}$ |
| $= 266$ kip-ft | $= 184$ kip-ft |

*Required Moment of Inertia for Live-Load Deflection Criterion of L/360*

$$\Delta_{max} = \frac{L}{360}$$

$$= \frac{(35 \text{ ft})(12 \text{ in./ft})}{360}$$

$$= 1.17 \text{ in.}$$

Determine the minimum required moment of inertia from AISC *Manual* Table 3-22, Case 1:

---

$$I_{x, req} = \frac{5w_L L^4}{384E\Delta_{max}}$$

$$= \frac{5(0.75 \text{ kip/ft})(35 \text{ ft})^4 (12 \text{ in./ft})^3}{384(29,000 \text{ ksi})(1.17 \text{ in.})}$$

$$= 746 \text{ in.}^4$$

*Beam Selection*

Select a W18×50 from AISC *Manual* Table 3-3.

$$I_x = 800 \text{ in.}^4 > 746 \text{ in.}^4 \quad \textbf{o.k.}$$

Per the User Note in AISC *Specification* Section F2, the section is compact. Because the beam is continuously braced and compact, only the yielding limit state applies.

From AISC *Manual* Table 3-2, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = \phi_b M_{px}$ | $\frac{M_n}{\Omega_b} = \frac{M_{px}}{\Omega_b}$ |
| $= 379$ kip-ft $> 266$ kip-ft **o.k.** | $= 252$ kip-ft $> 184$ kip-ft **o.k.** |

---

# EXAMPLE F.1-1B W-SHAPE FLEXURAL MEMBER DESIGN IN MAJOR-AXIS BENDING, CONTINUOUSLY BRACED

## Given:

Verify the available flexural strength of the ASTM A992/A992M W18×50 beam selected in Example F.1-1A by directly applying the requirements of the AISC *Specification*.

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50$ ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

W18×50
$Z_x = 101$ in.³

The required flexural strength from Example F.1-1A is:

| LRFD | ASD |
|------|-----|
| $M_u = 266$ kip-ft | $M_a = 184$ kip-ft |

*Nominal Flexural Strength*

Per the User Note in AISC *Specification* Section F2, the section is compact. Because the beam is continuously braced and compact, only the yielding limit state applies.

$$M_n = M_p = F_y Z_x$$
(*Spec.* Eq. F2-1)

$$= (50 \text{ ksi})(101 \text{ in.}^3)$$

$$= 5,050 \text{ kip-in. or } 421 \text{ kip-ft}$$

*Available Flexural Strength*

From AISC *Specification* Section F1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(421 \text{ kip-ft})$ | $\frac{M_n}{\Omega_b} = \frac{421 \text{ kip-ft}}{1.67}$ |
| $= 379$ kip-ft $> 266$ kip-ft **o.k.** | $= 252$ kip-ft $> 184$ kip-ft **o.k.** |

---

# F-9

## EXAMPLE F.1-2A W-SHAPE FLEXURAL MEMBER DESIGN IN MAJOR-AXIS BENDING, BRACED AT THIRD POINTS

### Given:

Use the AISC *Manual* tables to verify the available flexural strength of the W18×50 beam size selected in Example F.1-1A for the span and uniform dead and live loads shown in Figure F.1-2A. The beam is simply supported and braced at the ends and third points. The beam is ASTM A992/A992M material.

$$w_D = 0.45 \text{ kip/ft}$$
$$w_L = 0.75 \text{ kip/ft}$$

```
        ↓         ↓         ↓         ↓
        ●         |         |         ●
        |    (bracing at ends and third points)
        |←─────── L = 35'-0" ──────→|
```

*Fig. F.1-2A. Beam loading and bracing diagram.*

### Solution:

The required flexural strength at midspan from Example F.1-1A is:

| LRFD | ASD |
|------|-----|
| $M_u = 266 \text{ kip-ft}$ | $M_a = 184 \text{ kip-ft}$ |

**Unbraced Length**

$$L_b = \frac{35 \text{ ft}}{3}$$
$$= 11.7 \text{ ft}$$

By inspection, the middle segment will govern. From AISC *Manual* Table 3-1, for a uniformly loaded beam braced at the ends and third points, $C_b = 1.01$ in the middle segment. Conservatively, neglect this small adjustment in this case.

**Available Flexural Strength**

Enter AISC *Manual* Table 3-10 and find the intersection of the curve for the W18×50 with an unbraced length of 11.7 ft. Obtain the available strength from the appropriate vertical scale to the left.

From AISC *Manual* Table 3-10, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 302 \text{ kip-ft} > 266 \text{ kip-ft}$ **o.k.** | $\dfrac{M_n}{\Omega_b} = 201 \text{ kip-ft} > 184 \text{ kip-ft}$ **o.k.** |

---

# F-10

## EXAMPLE F.1-2B W-SHAPE FLEXURAL MEMBER DESIGN IN MAJOR-AXIS BENDING, BRACED AT THIRD POINTS

### Given:

Verify the available flexural strength of the W18×50 beam selected in Example F.1-1A with the beam braced at the ends and third points by directly applying the requirements of the AISC *Specification*. The beam is ASTM A992/A992M material.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-1, the geometric properties are as follows:

W18×50
$r_y = 1.65 \text{ in.}$
$S_x = 88.9 \text{ in.}^3$
$J = 1.24 \text{ in.}^4$
$r_{ts} = 1.98 \text{ in.}$
$h_o = 17.4 \text{ in.}$

The required flexural strength from Example F.1-1A is:

| LRFD | ASD |
|------|-----|
| $M_u = 266 \text{ kip-ft}$ | $M_a = 184 \text{ kip-ft}$ |

**Nominal Flexural Strength**

Calculate $C_b$. For the lateral-torsional buckling limit state, the nonuniform moment modification factor can be calculated using AISC *Specification* Equation F1-1. For the center segment of the beam, the required moments for AISC *Specification* Equation F1-1 can be calculated as a percentage of the maximum midspan moment as: $M_{max} = 1.00$, $M_A = 0.972$, $M_B = 1.00$, and $M_C = 0.972$.

$$C_b = \frac{12.5M_{max}}{2.5M_{max} + 3M_A + 4M_B + 3M_C}$$
$$\text{(Spec. Eq. F1-1)}$$

$$= \frac{12.5(1.00)}{2.5(1.00) + 3(0.972) + 4(1.00) + 3(0.972)}$$
$$= 1.01$$

For the end-span beam segments, the required moments for AISC *Specification* Equation F1-1 can be calculated as a percentage of the maximum midspan moment as: $M_{max} = 0.889$, $M_A = 0.306$, $M_B = 0.556$, and $M_C = 0.750$.

$$C_b = \frac{12.5M_{max}}{2.5M_{max} + 3M_A + 4M_B + 3M_C}$$
$$\text{(Spec. Eq. F1-1)}$$

$$= \frac{12.5(0.889)}{2.5(0.889) + 3(0.306) + 4(0.556) + 3(0.750)}$$
$$= 1.46$$

---

# F-11

Thus, the center span, with the higher required strength and lower $C_b$, will govern.

The limiting laterally unbraced length for the limit state of yielding is:

$$L_p = 1.76r_y\sqrt{\frac{E}{F_y}}$$
$$\text{(Spec. Eq. F2-5)}$$

$$= 1.76(1.65 \text{ in.})\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$
$$= 69.9 \text{ in. or } 5.83 \text{ ft}$$

The limiting unbraced length for the limit state of inelastic lateral-torsional buckling, with $c = 1$ from AISC *Specification* Equation F2-8a for doubly symmetric I-shaped members, is:

$$L_r = 1.95r_{ts}\frac{E}{0.7F_y}\sqrt{\frac{J_c}{S_x h_o} + \sqrt{\left(\frac{J_c}{S_x h_o}\right)^2 + 6.76\left(\frac{0.7F_y}{E}\right)^2}}$$
$$\text{(Spec. Eq. F2-6)}$$

$$= 1.95(1.98 \text{ in.})\left[\frac{29,000 \text{ ksi}}{0.7(50 \text{ ksi})}\right]\sqrt{\frac{(1.24 \text{ in.}^4)(1)}{(88.9 \text{ in.}^3)(17.4 \text{ in.})} + \sqrt{\left[\frac{(1.24 \text{ in.}^4)(1)}{(88.9 \text{ in.}^3)(17.4 \text{ in.})}\right]^2 + 6.76\left[\frac{0.7(50 \text{ ksi})}{29,000 \text{ ksi}}\right]^2}}$$
$$= 203 \text{ in. or } 16.9 \text{ ft}$$

$L_b = 11.7 \text{ ft}$ (from Example F.1-2A)

For a compact beam with an unbraced length of $L_p < L_b \leq L_r$, the lesser of either the flexural yielding limit state or the inelastic lateral-torsional buckling limit state controls the nominal strength.

$M_p = 5,050 \text{ kip-in.}$ (from Example F.1-1B)

$$M_n = C_b\left[M_p - (M_p - 0.7F_y S_x)\left(\frac{L_b - L_p}{L_r - L_p}\right)\right] \leq M_p$$
$$\text{(Spec. Eq. F2-2)}$$

$$= 1.01\left\{5,050 \text{ kip-in.} - \left[5,050 \text{ kip-in.} - 0.7(50 \text{ ksi})(88.9 \text{ in.}^3)\right]\left(\frac{11.7 \text{ ft} - 5.83 \text{ ft}}{16.9 \text{ ft} - 5.83 \text{ ft}}\right)\right\} < 5,050 \text{ kip-in.}$$
$$= 4,060 \text{ kip-in.} < 5,050 \text{ kip-in.}$$
$$= 4,060 \text{ kip-in. or } 338 \text{ kip-ft}$$

**Available Flexural Strength**

From AISC *Specification* Section F1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(338 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{338 \text{ kip-ft}}{1.67}$ |
| $= 304 \text{ kip-ft} > 266 \text{ kip-ft}$ **o.k.** | $= 202 \text{ kip-ft} > 184 \text{ kip-ft}$ **o.k.** |

---

# F-12

## EXAMPLE F.1-3A W-SHAPE FLEXURAL MEMBER DESIGN IN MAJOR-AXIS BENDING, BRACED AT MIDSPAN

### Given:

Use the AISC *Manual* tables to verify the available flexural strength of the W18×50 beam size selected in Example F.1-1A for the span and uniform dead and live loads shown in Figure F.1-3A. The beam is simply supported and braced at the ends and midpoint. The beam is ASTM A992/A992M material.

$$w_D = 0.45 \text{ kip/ft}$$
$$w_L = 0.75 \text{ kip/ft}$$

```
        ↓         ↓
        ●         |         ●
        |  (bracing at ends and midpoint)
        |←─────── L = 35'-0" ──────→|
```

*Fig. F.1-3A. Beam loading and bracing diagram.*

### Solution:

The required flexural strength at midspan from Example F.1-1A is:

| LRFD | ASD |
|------|-----|
| $M_u = 266 \text{ kip-ft}$ | $M_a = 184 \text{ kip-ft}$ |

**Unbraced Length**

$$L_b = \frac{35 \text{ ft}}{2}$$
$$= 17.5 \text{ ft}$$

From AISC *Manual* Table 3-1, for a uniformly loaded beam braced at the ends and at the center point, $C_b = 1.30$. There are several ways to make adjustments to AISC *Manual* Table 3-10 to account for $C_b$ greater than 1.0.

**Procedure A**

Available moments from the sloped and curved portions of the plots from AISC *Manual* Table 3-10 may be multiplied by $C_b$, but may not exceed the value of the horizontal portion ($\phi M_p$ for LRFD, $M_p/\Omega$ for ASD).

Obtain the available strength of a W18×50 with an unbraced length of 17.5 ft from AISC *Manual* Table 3-10.

Enter AISC *Manual* Table 3-10 and find the intersection of the curve for the W18×50 with an unbraced length of 17.5 ft. Obtain the available strength from the appropriate vertical scale to the left.

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 222 \text{ kip-ft}$ | $\dfrac{M_n}{\Omega_b} = 148 \text{ kip-ft}$ |
| From AISC *Manual* Table 3-2: | From AISC *Manual* Table 3-2: |
| $\phi_b M_p = 379 \text{ kip-ft}$ (upper limit on $C_b\phi_b M_n$) | $\dfrac{M_p}{\Omega_b} = 252 \text{ kip-ft}$ (upper limit on $C_b\dfrac{M_n}{\Omega_b}$) |

---

# F-13

| LRFD | ASD |
|------|-----|
| Adjust for $C_b$. | Adjust for $C_b$. |
| $1.30(222 \text{ kip-ft}) = 289 \text{ kip-ft}$ | $1.30(148 \text{ kip-ft}) = 192 \text{ kip-ft}$ |
| Check limit. | Check limit. |
| $289 \text{ kip-ft} < \phi_b M_p = 379 \text{ kip-ft}$ **o.k.** | $192 \text{ kip-ft} < \dfrac{M_p}{\Omega_b} = 252 \text{ kip-ft}$ **o.k.** |
| Check available versus required strength. | Check available versus required strength. |
| $289 \text{ kip-ft} > 266 \text{ kip-ft}$ **o.k.** | $192 \text{ kip-ft} > 184 \text{ kip-ft}$ **o.k.** |

**Procedure B**

For preliminary selection, the required strength can be divided by $C_b$ and directly compared to the strengths in AISC *Manual* Table 3-10. Members selected in this way must be checked to ensure that the required strength does not exceed the available plastic moment strength of the section.

Calculate the adjusted required strength.

| LRFD | ASD |
|------|-----|
| $M'_u = \dfrac{266 \text{ kip-ft}}{1.30}$ | $M'_a = \dfrac{184 \text{ kip-ft}}{1.30}$ |
| $= 205 \text{ kip-ft}$ | $= 142 \text{ kip-ft}$ |

Obtain the available strength for a W18×50 with an unbraced length of 17.5 ft from AISC *Manual* Table 3-10.

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 222 \text{ kip-ft} > 205 \text{ kip-ft}$ **o.k.** | $\dfrac{M_n}{\Omega_b} = 148 \text{ kip-ft} > 142 \text{ kip-ft}$ **o.k.** |
| $\phi_b M_p = 379 \text{ kip-ft} > 266 \text{ kip-ft}$ **o.k.** | $\dfrac{M_p}{\Omega_b} = 252 \text{ kip-ft} > 184 \text{ kip-ft}$ **o.k.** |

---

# F-14

## EXAMPLE F.1-3B W-SHAPE FLEXURAL MEMBER DESIGN IN MAJOR-AXIS BENDING, BRACED AT MIDSPAN

### Given:

Verify the available flexural strength of the W18×50 beam selected in Example F.1-1A with the beam braced at the ends and center point by directly applying the requirements of the AISC *Specification*. The beam is ASTM A992/A992M material.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-1, the geometric properties are as follows:

W18×50
$r_{ts} = 1.98 \text{ in.}$
$S_x = 88.9 \text{ in.}^3$
$J = 1.24 \text{ in.}^4$
$h_o = 17.4 \text{ in.}$

The required flexural strength from Example F.1-1A is:

| LRFD | ASD |
|------|-----|
| $M_u = 266 \text{ kip-ft}$ | $M_a = 184 \text{ kip-ft}$ |

**Nominal Flexural Strength**

Calculate $C_b$. The required moments for AISC *Specification* Equation F1-1 can be calculated as a percentage of the maximum midspan moment as: $M_{max} = 1.00$, $M_A = 0.438$, $M_B = 0.750$, and $M_C = 0.938$.

$$C_b = \frac{12.5M_{max}}{2.5M_{max} + 3M_A + 4M_B + 3M_C}$$
$$\text{(Spec. Eq. F1-1)}$$

$$= \frac{12.5(1.00)}{2.5(1.00) + 3(0.438) + 4(0.750) + 3(0.938)}$$
$$= 1.30$$

From AISC *Manual* Table 3-2:

$L_p = 5.83 \text{ ft}$
$L_r = 16.9 \text{ ft}$

From Example F.1-3A:

$L_b = 17.5 \text{ ft}$

For a compact beam with an unbraced length $L_b > L_r$, the limit state of elastic lateral-torsional buckling applies.

---

# F-15

Calculate $F_{cr}$, where $c = 1$ for doubly symmetric I-shapes.

$$F_{cr} = \frac{C_b \pi^2 E}{\left(\frac{L_b}{r_{ts}}\right)^2}\sqrt{1 + 0.078\frac{J_c}{S_x h_o}\left(\frac{L_b}{r_{ts}}\right)^2}$$
$$\text{(Spec. Eq. F2-4)}$$

$$= \frac{1.30\left(\pi^2\right)(29,000 \text{ ksi})}{\left[\frac{(17.5 \text{ ft})(12 \text{ in./ft})}{1.98 \text{ in.}}\right]^2}\sqrt{1 + 0.078\frac{(1.24 \text{ in.}^4)(1)}{(88.9 \text{ in.}^3)(17.4 \text{ in.})}\left[\frac{(17.5 \text{ ft})(12 \text{ in./ft})}{1.98 \text{ in.}}\right]^2}$$

$$= 43.2 \text{ ksi}$$

$M_p = 5,050 \text{ kip-in.}$ (from Example F.1-1B)

$$M_n = F_{cr}S_x \leq M_p$$
$$\text{(Spec. Eq. F2-3)}$$

$$= (43.2 \text{ ksi})(88.9 \text{ in.}^3) < 5,050 \text{ kip-in.}$$
$$= 3,840 \text{ kip-in.} < 5,050 \text{ kip-in.}$$
$$= 3,840 \text{ kip-in. or } 320 \text{ kip-ft}$$

**Available Flexural Strength**

From AISC *Specification* Section F1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(320 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{320 \text{ kip-ft}}{1.67}$ |
| $= 288 \text{ kip-ft} > 266 \text{ kip-ft}$ **o.k.** | $= 192 \text{ kip-ft} > 184 \text{ kip-ft}$ **o.k.** |

---

# F-16

## EXAMPLE F.2-1A COMPACT CHANNEL FLEXURAL MEMBER, CONTINUOUSLY BRACED

### Given:

Using the AISC *Manual* tables, select a channel to serve as a roof edge beam for the span and uniform dead and live loads shown in Figure F.2-1A. The beam is simply supported and continuously braced. Limit the live load deflection to $L/360$. The channel is ASTM A992/A992M material.

$$w_D = 0.23 \text{ kip/ft}$$
$$w_L = 0.69 \text{ kip/ft}$$

```
        |  |  |  |  |  |  |  |
        ●    (continuously braced)    ●
        |←─────── L = 25'-0" ──────→|
```

*Fig. F.2-1A. Beam loading and bracing diagram.*

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From Chapter 2 of ASCE/SEI 7, the required flexural strength is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.23 \text{ kip/ft}) + 1.6(0.69 \text{ kip/ft})$ | $w_a = 0.23 \text{ kip/ft} + 0.69 \text{ kip/ft}$ |
| $= 1.38 \text{ kip/ft}$ | $= 0.920 \text{ kip/ft}$ |
| From AISC *Manual* Table 3-22, Case 1: | From AISC *Manual* Table 3-22, Case 1: |
| $M_u = \dfrac{w_u L^2}{8}$ | $M_a = \dfrac{w_a L^2}{8}$ |
| $= \dfrac{(1.38 \text{ kip/ft})(25 \text{ ft})^2}{8}$ | $= \dfrac{(0.920 \text{ kip/ft})(25 \text{ ft})^2}{8}$ |
| $= 108 \text{ kip-ft}$ | $= 71.9 \text{ kip-ft}$ |

**Beam Selection**

Per the User Note in AISC *Specification* Section F2, all ASTM A992/A992M channels are compact. Because the beam is compact and continuously braced, the yielding limit state governs and $M_b = M_p$.

Try C15×33.9 from AISC *Manual* Table 3-8.

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = \phi_b M_p$ | $\dfrac{M_n}{\Omega_b} = \dfrac{M_p}{\Omega_b}$ |
| $= 191 \text{ kip-ft} > 108 \text{ kip-ft}$ **o.k.** | $= 127 \text{ kip-ft} > 71.9 \text{ kip-ft}$ **o.k.** |

---

# F-17

**Live Load Deflection**

Limit the live load deflection at the center of the beam to $L/360$.

$$\Delta_{max} = \frac{L}{360}$$
$$= \frac{(25 \text{ ft})(12 \text{ in./ft})}{360}$$
$$= 0.833 \text{ in.}$$

For C15×33.9, $I_x = 315 \text{ in.}^4$ from AISC *Manual* Table 1-5.

The maximum deflection is calculated using AISC *Manual* Table 3-22, Case 1:

$$\Delta = \frac{5w_L L^4}{384EI}$$

$$= \frac{5(0.69 \text{ kip/ft})(25 \text{ ft})^4(12 \text{ in./ft})^3}{384(29,000 \text{ ksi})(315 \text{ in.}^4)}$$

$$= 0.664 \text{ in.} < 0.833 \text{ in.}$$ **o.k.**

---

# F-18

## EXAMPLE F.2-1B COMPACT CHANNEL FLEXURAL MEMBER, CONTINUOUSLY BRACED

### Given:

Verify the available flexural strength of the C15×33.9 beam selected in Example F.2-1A by directly applying the requirements of the AISC *Specification*. The channel is ASTM A992/A992M material.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-5, the geometric properties are as follows:

C15×33.9
$Z_x = 50.8 \text{ in.}^3$

The required flexural strength from Example F.2-1A is:

| LRFD | ASD |
|------|-----|
| $M_u = 108 \text{ kip-ft}$ | $M_a = 71.9 \text{ kip-ft}$ |

**Nominal Flexural Strength**

Per the User Note in AISC *Specification* Section F2, all ASTM A992/A992M C- and MC-shapes are compact.

A channel that is continuously braced and compact is governed by the yielding limit state.

$$M_n = M_p = F_y Z_x$$
$$\text{(Spec. Eq. F2-1)}$$

$$= (50 \text{ ksi})(50.8 \text{ in.}^3)$$
$$= 2,540 \text{ kip-in. or } 212 \text{ kip-ft}$$

**Available Flexural Strength**

From AISC *Specification* Section F1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(212 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{212 \text{ kip-ft}}{1.67}$ |
| $= 191 \text{ kip-ft} > 108 \text{ kip-ft}$ **o.k.** | $= 127 \text{ kip-ft} > 71.9 \text{ kip-ft}$ **o.k.** |

---

# F-19

## EXAMPLE F.2-2A COMPACT CHANNEL FLEXURAL MEMBER WITH BRACING AT ENDS AND FIFTH POINTS

### Given:

Use the AISC *Manual* tables to verify the available flexural strength of the C15×33.9 beam selected in Example F.2-1A for the span and uniform dead and live loads shown in Figure F.2-2A. The beam is simply supported and braced at the ends and fifth points. The channel is ASTM A992/A992M material.

$$w_D = 0.23 \text{ kip/ft}$$
$$w_L = 0.69 \text{ kip/ft}$$

```
        ↓    ↓    ↓    ↓    ↓    ↓
        ●         |    |    |         ●
        | (bracing at ends and fifth points) |
        |←────────── L = 25'-0" ──────────→|
```

*Fig. F.2-2A. Beam loading and bracing diagram.*

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

The center segment will govern by inspection.

The required flexural strength at midspan from Example F.2-1A is:

| LRFD | ASD |
|------|-----|
| $M_u = 108 \text{ kip-ft}$ | $M_a = 71.9 \text{ kip-ft}$ |

From AISC *Manual* Table 3-1, with an almost uniform moment across the center segment, $C_b = 1.00$; therefore, no adjustment is required.

**Unbraced Length**

$$L_b = \frac{25 \text{ ft}}{5}$$
$$= 5.00 \text{ ft}$$

Obtain the flexural strength of the C15×33.9 with an unbraced length of 5.00 ft from AISC *Manual* Table 3-11.

Enter AISC *Manual* Table 3-11 and find the intersection of the curve for the C15×33.9 with an unbraced length of 5.00 ft. Obtain the available strength from the appropriate vertical scale to the left.

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 172 \text{ kip-ft} > 108 \text{ kip-ft}$ **o.k.** | $\dfrac{M_n}{\Omega_b} = 115 \text{ kip-ft} > 71.9 \text{ kip-ft}$ **o.k.** |

---

# F-20

## EXAMPLE F.2-2B COMPACT CHANNEL FLEXURAL MEMBER WITH BRACING AT ENDS AND FIFTH POINTS

### Given:

Verify the results from Example F.2-2A by directly applying the requirements of the AISC *Specification*.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-5, the geometric properties are as follows:

C15×33.9
$S_x = 42.0 \text{ in.}^3$

The required flexural strength from Example F.2-1A is:

| LRFD | ASD |
|------|-----|
| $M_u = 108 \text{ kip-ft}$ | $M_a = 71.9 \text{ kip-ft}$ |

**Available Flexural Strength**

Per the User Note in AISC *Specification* Section F2, all ASTM A992/A992M C- and MC-shapes are compact.

From AISC *Manual* Table 3-1, for the center segment of a uniformly loaded beam braced at the ends and the fifth points:

$$C_b = 1.00$$

From AISC *Manual* Table 3-8, for a C15×33.9:

$$L_p = 3.18 \text{ ft}$$
$$L_r = 11.2 \text{ ft}$$

From Example F2-2A:

$$L_b = 5.00 \text{ ft}$$

For a compact channel with $L_p < L_b \leq L_r$, the lesser of the flexural yielding limit state or the inelastic lateral-torsional buckling limit state controls the available flexural strength.

The nominal flexural strength based on the flexural yielding limit state, from Example F.2-1B, is:

$$M_n = M_p$$
$$= 2,540 \text{ kip-in.}$$

---

# F-21

The nominal flexural strength based on the lateral-torsional buckling limit state is:

$$M_n = C_b\left[M_p - (M_p - 0.7F_y S_x)\left(\frac{L_b - L_p}{L_r - L_p}\right)\right] \leq M_p$$
$$\text{(Spec. Eq. F2-2)}$$

$$= 1.00\left\{2,540 \text{ kip-in.} - \left[2,540 \text{ kip-in.} - 0.7(50 \text{ ksi})(42.0 \text{ in.}^3)\right]\left(\frac{5.00 \text{ ft} - 3.18 \text{ ft}}{11.2 \text{ ft} - 3.18 \text{ ft}}\right)\right\} < 2,540 \text{ kip-in.}$$

$$= 2,300 \text{ kip-in.} < 2,540 \text{ kip-in.}$$
$$= 2,300 \text{ kip-in. or } 192 \text{ kip-ft}$$

**Available Flexural Strength**

From AISC *Specification* Section F1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(192 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{192 \text{ kip-ft}}{1.67}$ |
| $= 173 \text{ kip-ft} > 108 \text{ kip-ft}$ **o.k.** | $= 115 \text{ kip-ft} > 71.9 \text{ kip-ft}$ **o.k.** |

---

# F-22

## EXAMPLE F.3A W-SHAPE FLEXURAL MEMBER WITH NONCOMPACT FLANGES IN MAJOR-AXIS BENDING

### Given:

Using the AISC *Manual* tables, select a W-shape beam for the span, uniform dead load, and concentrated live loads shown in Figure F.3A. The beam is simply supported and continuously braced. Also calculate the deflection. The beam is ASTM A992/A992M material.

$$P_L = 18 \text{ kips (at third points)}$$

```
                    ↓         ↓
        |  |  |  |  |  |  |  |  |
        ●    $w_D = 0.05 \text{ kip/ft}$    ●
        |    (continuously braced)    |
        |←─────── L = 40'-0" ──────→|
```

*Fig. F.3A. Beam loading and bracing diagram.*

Note: A beam with noncompact flanges will be selected to demonstrate that the tabulated values of the AISC *Manual* account for flange compactness.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From Chapter 2 of ASCE/SEI 7, the required flexural strength at midspan is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.05 \text{ kip/ft})$ | $w_a = 0.05 \text{ kip/ft}$ |
| $= 0.0600 \text{ kip/ft}$ | |
| $P_u = 1.6(18 \text{ kips})$ | $P_a = 18 \text{ kips}$ |
| $= 28.8 \text{ kips}$ | |
| From AISC *Manual* Table 3-22, Cases 1 and 9: | From AISC *Manual* Table 3-22, Cases 1 and 9: |
| $M_u = \dfrac{w_u L^2}{8} + P_u a$ | $M_a = \dfrac{w_a L^2}{8} + P_u a$ |
| $= \dfrac{(0.0600 \text{ kip/ft})(40 \text{ ft})^2}{8} + (28.8 \text{ kips})\left(\dfrac{40 \text{ ft}}{3}\right)$ | $= \dfrac{(0.05 \text{ kip/ft})(40 \text{ ft})^2}{8} + (18 \text{ kips})\left(\dfrac{40 \text{ ft}}{3}\right)$ |
| $= 396 \text{ kip-ft}$ | $= 250 \text{ kip-ft}$ |

**Beam Selection**

For a continuously braced W-shape, the available flexural strength equals the available plastic flexural strength.

Select the lightest section providing the required strength from the bold entries in AISC *Manual* Table 3-2.

---

# F-23

Try a W21×48.

This beam has a noncompact compression flange at $F_y = 50 \text{ ksi}$ as indicated by footnote "[f]" in AISC *Manual* Table 3-2. This shape is also footnoted in AISC *Manual* Table 1-1.

From AISC *Manual* Table 3-2, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = \phi_b M_{px}$ | $\dfrac{M_n}{\Omega_b} = \dfrac{M_{px}}{\Omega_b}$ |
| $= 398 \text{ kip-ft} > 396 \text{ kip-ft}$ **o.k.** | $= 265 \text{ kip-ft} > 250 \text{ kip-ft}$ **o.k.** |

Note: The value $M_{px}$ in AISC *Manual* Table 3-2 includes the strength reductions due to the shape being noncompact.

**Deflection**

From AISC *Manual* Table 3-2:

$$I_x = 959 \text{ in.}^4$$

The maximum deflection occurs at the center of the beam. From AISC *Manual* Table 3-22, Cases 1 and 9:

$$\Delta = \frac{5w_D L^4}{384EI} + \frac{23P_L L^3}{648EI}$$

$$= \frac{5(0.05 \text{ kip/ft})(40 \text{ ft})^4(12 \text{ in./ft})^3}{384(29,000 \text{ ksi})(959 \text{ in.}^4)} + \frac{23(18 \text{ kips})(40 \text{ ft})^3(12 \text{ in./ft})^3}{648(29,000 \text{ ksi})(959 \text{ in.}^4)}$$

$$= 2.64 \text{ in.}$$

This deflection can be compared with the appropriate deflection limit for the application. Deflection will often be more critical than strength in beam design.

---

# F-24

## EXAMPLE F.3B W-SHAPE FLEXURAL MEMBER WITH NONCOMPACT FLANGES IN MAJOR-AXIS BENDING

### Given:

Verify the results from Example F.3A by directly applying the requirements of the AISC *Specification*.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-1, the geometric properties are as follows:

W21×48
$S_x = 93.0 \text{ in.}^3$
$Z_x = 107 \text{ in.}^3$
$\dfrac{b_f}{2t_f} = 9.47$

The required flexural strength from Example F.3A is:

| LRFD | ASD |
|------|-----|
| $M_u = 396 \text{ kip-ft}$ | $M_a = 250 \text{ kip-ft}$ |

**Flange Slenderness**

$$\lambda = \frac{b_f}{2t_f}$$
$$= 9.47$$

The limiting width-to-thickness ratios for the compression flange are determined from AISC *Specification* Table B4.1b, Case 10:

$$\lambda_{pf} = 0.38\sqrt{\frac{E}{F_y}}$$

$$= 0.38\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$
$$= 9.15$$

$$\lambda_{rf} = 1.0\sqrt{\frac{E}{F_y}}$$

$$= 1.0\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$
$$= 24.1$$

Because $\lambda_{pf} < \lambda < \lambda_{rf}$, the compression flange is noncompact. This could also be determined from the footnote "[f]" in AISC *Manual* Table 1-1.
**Nominal Flexural Strength**

---

# F-25

Because the beam is continuously braced, and therefore not subject to lateral-torsional buckling, the available strength is based on the limit state of compression flange local buckling. From AISC *Specification* Section F3.2:

$$M_n = F_y Z_x$$
$$\text{(Spec. Eq. F2-1)}$$

$$= (50 \text{ ksi})(107 \text{ in.}^3)$$
$$= 5,350 \text{ kip-in. or } 446 \text{ kip-ft}$$

$$M_n = M_p - (M_p - 0.7F_y S_x)\left(\frac{\lambda - \lambda_{pf}}{\lambda_{rf} - \lambda_{pf}}\right)$$
$$\text{(Spec. Eq. F3-1)}$$

$$= 5,350 \text{ kip-in.} - \left[5,350 \text{ kip-in.} - 0.7(50 \text{ ksi})(93.0 \text{ in.}^3)\right]\left(\frac{9.47 - 9.15}{24.1 - 9.15}\right)$$

$$= 5,310 \text{ kip-in. or } 442 \text{ kip-ft}$$

**Available Flexural Strength**

From AISC *Specification* Section F1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(442 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{442 \text{ kip-ft}}{1.67}$ |
| $= 398 \text{ kip-ft} > 396 \text{ kip-ft}$ **o.k.** | $= 265 \text{ kip-ft} > 250 \text{ kip-ft}$ **o.k.** |

Note that these available strengths are identical to the tabulated values in AISC *Manual* Table 3-2, as shown in Example F.3A, which account for the noncompact flange.

---

# F-26

## EXAMPLE F.4 W-SHAPE FLEXURAL MEMBER, SELECTION BY MOMENT OF INERTIA FOR MAJOR-AXIS BENDING

### Given:

Using the AISC *Manual* tables, select a W-shape using the moment of inertia required to limit the live load deflection to 1.00 in. for the span and uniform dead and live loads shown in Figure F.4. The beam is simply supported and continuously braced. The beam is ASTM A992/A992M material.

$$w_D = 0.8 \text{ kip/ft}$$
$$w_L = 2 \text{ kip/ft}$$

```
        |  |  |  |  |  |  |  |  |  |
        ●    (continuously braced)    ●
        |←─────── L = 30'-0" ──────→|
```

*Fig. F.4. Beam loading and bracing diagram.*

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From Chapter 2 of ASCE/SEI 7, the required flexural strength is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.8 \text{ kip/ft}) + 1.6(2 \text{ kip/ft})$ | $w_a = 0.8 \text{ kip/ft} + 2 \text{ kip/ft}$ |
| $= 4.16 \text{ kip/ft}$ | $= 2.80 \text{ kip/ft}$ |
| From AISC *Manual* Table 3-22, Case 1: | From AISC *Manual* Table 3-22, Case 1: |
| $M_u = \dfrac{w_u L^2}{8}$ | $M_a = \dfrac{w_a L^2}{8}$ |
| $= \dfrac{(4.16 \text{ kip/ft})(30 \text{ ft})^2}{8}$ | $= \dfrac{(2.80 \text{ kip/ft})(30 \text{ ft})^2}{8}$ |
| $= 468 \text{ kip-ft}$ | $= 315 \text{ kip-ft}$ |

**Minimum Required Moment of Inertia**

From AISC *Manual* Table 3-22, Case 1, the maximum live load deflection, $\Delta_{max}$, occurs at midspan and is calculated as:

$$\Delta_{max} = \frac{5w_L L^4}{384EI}$$

Rearranging and substituting $\Delta_{max} = 1.00 \text{ in.}$,

---

# F-27

$$I_{req} = \frac{5w_L L^4}{384E\Delta_{max}}$$

$$= \frac{5(2 \text{ kip/ft})(30 \text{ ft})^4(12 \text{ in./ft})^3}{384(29,000 \text{ ksi})(1.00 \text{ in.})}$$

$$= 1,260 \text{ in.}^4$$

**Beam Selection**

Select the lightest section with the required moment of inertia from the bold entries in AISC *Manual* Table 3-3.

Try a W24×55.

$$I_x = 1,350 \text{ in.}^4 > 1,260 \text{ in.}^4$$ **o.k.**

Because the W24×55 is continuously braced and compact, its strength is governed by the yielding limit state and AISC *Specification* Section F2.1.

From AISC *Manual* Table 3-2, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = \phi_b M_{px}$ | $\dfrac{M_n}{\Omega_b} = \dfrac{M_{px}}{\Omega_b}$ |
| $= 503 \text{ kip-ft} > 468 \text{ kip-ft}$ **o.k.** | $= 334 \text{ kip-ft} > 315 \text{ kip-ft}$ **o.k.** |

---

# F-28

## EXAMPLE F.5 I-SHAPED FLEXURAL MEMBER IN MINOR-AXIS BENDING

### Given:

Using the AISC *Manual* tables, select a W-shape beam loaded on its minor axis for the span and uniform dead and live loads shown in Figure F.5. Limit the live load deflection to $L/240$. The beam is simply supported and braced only at the ends. The beam is ASTM A992/A992M material.

$$w_D = 0.667 \text{ kip/ft}$$
$$w_L = 2 \text{ kip/ft}$$

```
        |  |  |  |  |  |  |  |  |  |
        ●    (braced at ends only)    ●
        |←─────── L = 15'-0" ──────→|
```

*Fig. F.5. Beam loading and bracing diagram.*

Note: Although not a common design case, this example is being used to illustrate AISC *Specification* Section F6 (I-shaped members and channels bent about their minor axis).

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From Chapter 2 of ASCE/SEI 7, the required flexural strength is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.667 \text{ kip/ft}) + 1.6(2 \text{ kip/ft})$ | $w_a = 0.667 \text{ kip/ft} + 2 \text{ kip/ft}$ |
| $= 4.00 \text{ kip/ft}$ | $= 2.67 \text{ kip/ft}$ |
| From AISC *Manual* Table 3-22, Case 1: | From AISC *Manual* Table 3-22, Case 1: |
| $M_u = \dfrac{w_u L^2}{8}$ | $M_a = \dfrac{w_a L^2}{8}$ |
| $= \dfrac{(4.00 \text{ kip/ft})(15 \text{ ft})^2}{8}$ | $= \dfrac{(2.67 \text{ kip/ft})(15 \text{ ft})^2}{8}$ |
| $= 113 \text{ kip-ft}$ | $= 75.1 \text{ kip-ft}$ |

**Minimum Required Moment of Inertia**

The maximum live load deflection permitted is:

$$\Delta_{max} = \frac{L}{240}$$
$$= \frac{(15 \text{ ft})(12 \text{ in./ft})}{240}$$
$$= 0.750 \text{ in.}$$

---

# F-29

Determine the minimum required moment of inertia from AISC *Manual* Table 3-22, Case 1:

$$I_{y, req} = \frac{5w_L L^4}{384E\Delta_{max}}$$

$$= \frac{5(2 \text{ kip/ft})(15 \text{ ft})^4(12 \text{ in./ft})^3}{384(29,000 \text{ ksi})(0.750 \text{ in.})}$$

$$= 105 \text{ in.}^4$$

**Beam Selection**

Select the lightest section from the bold entries in AISC *Manual* Table 3-5.

Try a W12×58.

From AISC *Manual* Table 1-1, the geometric properties are as follows:

W12×58
$S_y = 21.4 \text{ in.}^3$
$Z_y = 32.5 \text{ in.}^3$
$I_y = 107 \text{ in.}^4 > 105 \text{ in.}^4$ **o.k.** (for deflection requirement)

**Nominal Flexural Strength**

AISC *Specification* Section F6 applies. Because the W12×58 has compact flanges per the User Note in this Section, the yielding limit state governs the design.

$$M_n = M_p = F_y Z_y \leq 1.6F_y S_y$$
$$\text{(Spec. Eq. F6-1)}$$

$$= (50 \text{ ksi})(32.5 \text{ in.}^3) < 1.6(50 \text{ ksi})(21.4 \text{ in.}^3)$$
$$= 1,630 \text{ kip-in.} < 1,710 \text{ kip-in.}$$
$$= 1,630 \text{ kip-in. or } 136 \text{ kip-ft}$$

**Available Flexural Strength**

From AISC *Specification* Section F1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(136 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{136 \text{ kip-ft}}{1.67}$ |
| $= 122 \text{ kip-ft} > 113 \text{ kip-ft}$ **o.k.** | $= 81.4 \text{ kip-ft} > 75.1 \text{ kip-ft}$ **o.k.** |

---

# F-30

## EXAMPLE F.6 SQUARE HSS FLEXURAL MEMBER WITH COMPACT FLANGES

### Given:

Using the AISC *Manual* tables, select a square HSS beam for the span and uniform dead and live loads shown in Figure F.6. Limit the live load deflection to $L/240$. The beam is simply supported and continuously braced. The HSS is ASTM A500/A500M Grade C material.

$$w_D = 0.145 \text{ kip/ft}$$
$$w_L = 0.435 \text{ kip/ft}$$

```
        |  |  |  |  |  |  |  |
        ●  (continuously braced)  ●
        |←──── L = 7'-6" ────→|
```

*Fig. F.6. Beam loading and bracing diagram.*

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A500/A500M Grade C
$F_y = 50 \text{ ksi}$

From Chapter 2 of ASCE/SEI 7, the required flexural strength is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.145 \text{ kip/ft}) + 1.6(0.435 \text{ kip/ft})$ | $w_a = 0.145 \text{ kip/ft} + 0.435 \text{ kip/ft}$ |
| $= 0.870 \text{ kip/ft}$ | $= 0.580 \text{ kip/ft}$ |
| From AISC *Manual* Table 3-22, Case 1: | From AISC *Manual* Table 3-22, Case 1: |
| $M_u = \dfrac{w_u L^2}{8}$ | $M_a = \dfrac{w_a L^2}{8}$ |
| $= \dfrac{(0.870 \text{ kip/ft})(7.5 \text{ ft})^2}{8}$ | $= \dfrac{(0.580 \text{ kip/ft})(7.5 \text{ ft})^2}{8}$ |
| $= 6.12 \text{ kip-ft}$ | $= 4.08 \text{ kip-ft}$ |

**Minimum Required Moment of Inertia**

The maximum live load deflection permitted is:

$$\Delta_{max} = \frac{L}{240}$$
$$= \frac{(7.5 \text{ ft})(12 \text{ in./ft})}{240}$$
$$= 0.375 \text{ in.}$$

---

# F-31

Determine the minimum required moment of inertia from AISC *Manual* Table 3-22, Case 1:

$$I_{req} = \frac{5w_L L^4}{384E\Delta_{max}}$$

$$= \frac{5(0.435 \text{ kip/ft})(7.5 \text{ ft})^4(12 \text{ in./ft})^3}{384(29,000 \text{ ksi})(0.375 \text{ in.})}$$

$$= 2.85 \text{ in.}^4$$

**Beam Selection**

Select an HSS with a minimum $I_x$ of 2.85 in.<sup>4</sup>, using AISC *Manual* Table 1-12, and having adequate available strength, using AISC *Manual* Table 3-13.

Try an HSS3½×3½×⅛.

From AISC *Manual* Table 1-12,

$$I_x = 2.90 \text{ in.}^4 > 2.85 \text{ in.}^4$$ **o.k.**

From AISC *Manual* Table 3-13, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 7.20 \text{ kip-ft} > 6.12 \text{ kip-ft}$ **o.k.** | $\dfrac{M_n}{\Omega_b} = 4.79 \text{ kip-ft} > 4.08 \text{ kip-ft}$ **o.k.** |

---

# F-32

## EXAMPLE F.7A RECTANGULAR HSS FLEXURAL MEMBER WITH NONCOMPACT FLANGES

### Given:

Using the AISC *Manual* tables, select a rectangular HSS beam for the span and uniform dead and live loads shown in Figure F.7A. Limit the live load deflection to $L/240$. The beam is simply supported and braced at the end points only. A noncompact member was selected here to illustrate the relative ease of selecting noncompact shapes from the AISC *Manual*, as compared to designing a similar shape by applying the AISC *Specification* requirements directly, as shown in Example F.7B. The HSS is ASTM A500/A500M Grade C material.

$$w_D = 0.15 \text{ kip/ft}$$
$$w_L = 0.4 \text{ kip/ft}$$

```
        |  |  |  |  |  |  |  |  |
        ●  (braced at end points only)  ●
        |←────── L = 21'-0" ──────→|
```

*Fig. F.7A. Beam loading and bracing diagram.*

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A500/A500M Grade C
$F_y = 50 \text{ ksi}$

From Chapter 2 of ASCE/SEI 7, the required flexural strength is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.15 \text{ kip/ft}) + 1.6(0.4 \text{ kip/ft})$ | $w_a = 0.15 \text{ kip/ft} + 0.4 \text{ kip/ft}$ |
| $= 0.820 \text{ kip/ft}$ | $= 0.550 \text{ kip/ft}$ |
| From AISC *Manual* Table 3-22, Case 1: | From AISC *Manual* Table 3-22, Case 1: |
| $M_u = \dfrac{w_u L^2}{8}$ | $M_a = \dfrac{w_a L^2}{8}$ |
| $= \dfrac{(0.820 \text{ kip/ft})(21 \text{ ft})^2}{8}$ | $= \dfrac{(0.550 \text{ kip/ft})(21 \text{ ft})^2}{8}$ |
| $= 45.2 \text{ kip-ft}$ | $= 30.3 \text{ kip-ft}$ |

**Minimum Required Moment of Inertia**

The maximum live load deflection permitted is:

$$\Delta_{max} = \frac{L}{240}$$
$$= \frac{(21 \text{ ft})(12 \text{ in./ft})}{240}$$
$$= 1.05 \text{ in.}$$

---

# F-33

Determine the minimum required moment of inertia from AISC *Manual* Table 3-22, Case 1:

$$I_{min} = \frac{5w_L L^4}{384E\Delta_{max}}$$

$$= \frac{5(0.4 \text{ kip/ft})(21 \text{ ft})^4(12 \text{ in./ft})^3}{384(29,000 \text{ ksi})(1.05 \text{ in.})}$$

$$= 57.5 \text{ in.}^4$$

**Beam Selection**

Select a rectangular HSS with a minimum $I_x$ of 57.5 in.<sup>4</sup>, using AISC *Manual* Table 1-11, and having adequate available strength, using AISC *Manual* Table 3-12.

Try an HSS10×6×⅜ oriented in the strong direction. This rectangular HSS section was purposely selected for illustration purposes because it has a noncompact flange. See AISC *Manual* Table 1-12A for compactness criteria.

$$I_x = 74.6 \text{ in.}^4 > 57.5 \text{ in.}^4$$ **o.k.**

From AISC *Manual* Table 3-12, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 59.7 \text{ kip-ft} > 45.2 \text{ kip-ft}$ **o.k.** | $\dfrac{M_n}{\Omega_b} = 39.7 \text{ kip-ft} > 30.3 \text{ kip-ft}$ **o.k.** |

Note: Because AISC *Manual* Table 3-12 does not account for lateral-torsional buckling, it needs to be checked using AISC *Specification* Section F7.4.

As discussed in the User Note to AISC *Specification* Section F7.4, lateral-torsional buckling will not occur in square sections or sections bending about their minor axis. In HSS sizes, deflection limits will often be reached before there is a significant reduction in flexural strength due to lateral-torsional buckling. See Example F.7B for the calculation accounting for lateral-torsional buckling for the HSS10×6×⅜.

---

# F-34

## EXAMPLE F.7B RECTANGULAR HSS FLEXURAL MEMBER WITH NONCOMPACT FLANGES

### Given:

In Example F.7A the required information was easily determined by consulting the tables of the AISC *Manual*. The purpose of the following calculation is to demonstrate the use of the AISC *Specification* to calculate the flexural strength of an HSS member with a noncompact compression flange. The HSS is ASTM A500/A500M Grade C material.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A500/A500M Grade C
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-11, the geometric properties are as follows:

HSS10×6×⅜
$A_g = 5.37 \text{ in.}^2$
$Z_x = 18.0 \text{ in.}^3$
$S_x = 14.9 \text{ in.}^3$
$r_y = 2.52 \text{ in.}$
$J = 73.8 \text{ in.}^4$
$b/t = 31.5$
$h/t = 54.5$

**Flange Compactness**

$$\lambda = b/t$$
$$= 31.5$$

From AISC *Specification* Table B4.1b, Case 17, the limiting width-to-thickness ratios for the flange are:

$$\lambda_p = 1.12\sqrt{\frac{E}{F_y}}$$

$$= 1.12\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$
$$= 27.0$$

$$\lambda_r = 1.40\sqrt{\frac{E}{F_y}}$$

$$= 1.40\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$
$$= 33.7$$

Because $\lambda_p < \lambda < \lambda_r$, the flange is noncompact and AISC *Specification* Equation F7-2 applies.

---

# F-35

**Web Compactness**

$$\lambda = h/t$$
$$= 54.5$$

From AISC *Specification* Table B4.1b, Case 19, the limiting width-to-thickness ratio for the web is:

$$\lambda_p = 2.42\sqrt{\frac{E}{F_y}}$$

$$= 2.42\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 58.3$$

Because $\lambda < \lambda_p$, the web is compact, and the limit state of web local buckling does not apply.

**Nominal Flexural Strength**

**Flange Local Buckling**

From AISC *Specification* Section F7.2(b), the limit state of flange local buckling applies for HSS with noncompact flanges and compact webs.

$$M_p = F_y Z_x$$
$$\text{(from Spec. Eq. F7-1)}$$

$$= (50 \text{ ksi})(18.0 \text{ in.}^3)$$
$$= 900 \text{ kip-in.}$$

$$M_n = M_p - (M_p - F_y S)\left(\frac{\lambda - \lambda_{pf}}{\lambda_{rf} - \lambda_{pf}}\right) \leq M_p$$
$$\text{(Spec. Eq. F7-2)}$$

$$= 900 \text{ kip-in.} - \left[900 \text{ kip-in.} - (50 \text{ ksi})(14.9 \text{ in.}^3)\right]\left[\frac{31.5 - 27.0}{33.7 - 27.0}\right] < 900 \text{ kip-in.}$$

$$= 796 \text{ kip-in.} < 900 \text{ kip-in.}$$
$$= 796 \text{ kip-in. or } 66.3 \text{ kip-ft}$$

**Yielding and Lateral-Torsional Buckling**

Determine the limiting laterally unbraced lengths for the limit state of yielding and the limit state of inelastic lateral-torsional buckling using AISC *Specification* Section F7.4.

$$L_b = (21 \text{ ft})(12 \text{ in./ft})$$
$$= 252 \text{ in.}$$

$$L_p = 0.13Er_y\sqrt{\frac{JA_g}{M_p}}$$
$$\text{(Spec. Eq. F7-12)}$$

$$= 0.13(29,000 \text{ ksi})(2.52 \text{ in.})\frac{\sqrt{(73.8 \text{ in.}^4)(5.37 \text{ in.}^2)}}{900 \text{ kip-in.}}$$

$$= 210 \text{ in.}$$

---

# F-36

$$L_r = 2Er_y\frac{\sqrt{JA_g}}{0.7F_y S_x}$$
$$\text{(Spec. Eq. F7-13)}$$

$$= 2(29,000 \text{ ksi})(2.52 \text{ in.})\frac{\sqrt{(73.8 \text{ in.}^4)(5.37 \text{ in.}^2)}}{0.7(50 \text{ ksi})(14.9 \text{ in.}^3)}$$

$$= 5,580 \text{ in.}$$

For the lateral-torsional buckling limit state, the lateral-torsional buckling modification factor can be calculated using AISC *Specification* Equation F1-1. For the beam, the required moments for AISC *Specification* Equation F1-1 can be calculated as a percentage of the maximum midspan moment as: $M_{max} = 1.00$, $M_A = 0.750$, $M_B = 1.00$, and $M_C = 0.750$.

$$C_b = \frac{12.5M_{max}}{2.5M_{max} + 3M_A + 4M_B + 3M_C}$$
$$\text{(Spec. Eq. F1-1)}$$

$$= \frac{12.5(1.00)}{2.5(1.00) + 3(0.750) + 4(1.00) + 3(0.750)}$$

$$= 1.14$$

Because $L_p < L_b < L_r$, the nominal moment strength considering lateral-torsional buckling is given by:

$$M_n = C_b\left[M_p - (M_p - 0.7F_y S_x)\left(\frac{L_b - L_p}{L_r - L_p}\right)\right] \leq M_p$$
$$\text{(Spec. Eq. F7-10)}$$

$$= 1.14\left\{900 \text{ kip-in.} - \left[900 \text{ kip-in.} - 0.7(50 \text{ ksi})(14.9 \text{ in.}^3)\right]\left(\frac{252 \text{ in.} - 210 \text{ in.}}{5,580 \text{ in.} - 210 \text{ in.}}\right)\right\}$$

$$= 1,020 \text{ kip-in.} > M_p = 900 \text{ kip-in.}$$
$$= 900 \text{ kip-in. or } 75.0 \text{ kip-ft}$$

**Available Flexural Strength**

The nominal strength is controlled by flange local buckling and therefore:

$$M_n = 66.3 \text{ kip-ft}$$

From AISC *Specification* Section F1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(66.3 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{66.3 \text{ kip-ft}}{1.67}$ |
| $= 59.7 \text{ kip-ft}$ | $= 39.7 \text{ kip-ft}$ |

---

# F-37

## EXAMPLE F.8A SQUARE HSS FLEXURAL MEMBER WITH SLENDER FLANGES

### Given:

Using AISC *Manual* tables, verify the strength of an HSS8×8×⅛ beam for the span and uniform dead and live loads shown in Figure F.8A. Limit the live load deflection to $L/240$. The beam is simply supported and continuously braced. The HSS is ASTM A500/A500M Grade C material.

$$w_D = 0.125 \text{ kip/ft}$$
$$w_L = 0.375 \text{ kip/ft}$$

```
        |  |  |  |  |  |  |  |  |
        ●    (continuously braced)    ●
        |←──── L = 21'-0" ────→|
```

*Fig. F.8A. Beam loading and bracing diagram.*

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A500/A500M Grade C
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-12, the geometric properties are as follows:

HSS8×8×⅛
$I = 54.4 \text{ in.}^4$

From Chapter 2 of ASCE/SEI 7, the required flexural strength is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.125 \text{ kip/ft}) + 1.6(0.375 \text{ kip/ft})$ | $w_a = 0.125 \text{ kip/ft} + 0.375 \text{ kip/ft}$ |
| $= 0.750 \text{ kip/ft}$ | $= 0.500 \text{ kip/ft}$ |
| From AISC *Manual* Table 3-22, Case 1: | From AISC *Manual* Table 3-22, Case 1: |
| $M_u = \dfrac{w_u L^2}{8}$ | $M_a = \dfrac{w_a L^2}{8}$ |
| $= \dfrac{(0.750 \text{ kip/ft})(21.0 \text{ ft})^2}{8}$ | $= \dfrac{(0.500 \text{ kip/ft})(21.0 \text{ ft})^2}{8}$ |
| $= 41.3 \text{ kip-ft}$ | $= 27.6 \text{ kip-ft}$ |

From AISC *Manual* Table 3-13, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 46.3 \text{ kip-ft} > 41.3 \text{ kip-ft}$ **o.k.** | $\dfrac{M_n}{\Omega_b} = 30.8 \text{ kip-ft} > 27.6 \text{ kip-ft}$ **o.k.** |

Note that the strengths given in AISC *Manual* Table 3-13 incorporate the effects of noncompact and slender elements.

---

# F-38

**Deflection**

The maximum live load deflection permitted is:

$$\Delta_{max} = \frac{L}{240}$$
$$= \frac{(21.0 \text{ ft})(12 \text{ in./ft})}{240}$$
$$= 1.05 \text{ in.}$$

The maximum deflection is calculated using AISC *Manual* Table 3-22, Case 1:

$$\Delta = \frac{5w_L L^4}{384EI}$$

$$= \frac{5(0.375 \text{ kip/ft})(21.0 \text{ ft})^4(12 \text{ in./ft})^3}{384(29,000 \text{ ksi})(54.4 \text{ in.}^4)}$$

$$= 1.04 \text{ in.} < 1.05 \text{ in.}$$ **o.k.**

---

# F-39

## EXAMPLE F.8B SQUARE HSS FLEXURAL MEMBER WITH SLENDER FLANGES

### Given:

In Example F.8A the available strengths were easily determined from the tables of the AISC *Manual*. The purpose of the following calculation is to demonstrate the use of the AISC *Specification* to calculate the flexural strength of the HSS beam given in Example F.8A. The HSS is ASTM A500/A500M Grade C material.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A500/A500M Grade C
$F_y = 50 \text{ ksi}$

From AISC *Manual* Table 1-12, the geometric properties are as follows:

HSS8×8×⅛
$I = 54.4 \text{ in.}^4$
$Z = 15.7 \text{ in.}^3$
$S = 13.6 \text{ in.}^3$
$t = 0.174 \text{ in.}$
$b/t = 43.0$
$h/t = 43.0$

The required flexural strength from Example F.8A is:

| LRFD | ASD |
|------|-----|
| $M_u = 41.3 \text{ kip-ft}$ | $M_a = 27.6 \text{ kip-ft}$ |

**Flange Slenderness**

The outside corner radii of HSS shapes are taken as 1.5*t* and the design thickness is used in accordance with AISC *Specification* Section B4.1b to check compactness.

Determine the limiting ratio for a slender HSS flange in flexure from AISC *Specification* Table B4.1b, Case 17.

$$\lambda_r = 1.40\sqrt{\frac{E}{F_y}}$$

$$= 1.40\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 33.7$$

$$\lambda = b/t$$
$$= 43.0 > \lambda_r$$ ; therefore, the flange is slender

**Web Slenderness**

Determine the limiting ratio for a compact web in flexure from AISC *Specification* Table B4.1b, Case 19.

---

# F-40

$$\lambda_p = 2.42\sqrt{\frac{E}{F_y}}$$

$$= 2.42\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 58.3$$

$$\lambda = h/t$$
$$= 43.0 < \lambda_p$$ ; therefore, the web is compact and the limit state of web local buckling does not apply

**Nominal Flexural Strength**

**Flange Local Buckling**

For HSS sections with slender flanges and compact webs, AISC *Specification* Section F7.2(c) applies.

$$M_n = F_y S_e$$
$$\text{(Spec. Eq. F7-3)}$$

From AISC *Specification* Section B4.1b(d), the width of the compression flange is determined as follows:

$$b = 8.00 \text{ in.} - 3(0.174 \text{ in.})$$
$$= 7.48 \text{ in.}$$

The effective section modulus, $S_e$, is determined using the effective width of the compression flange as follows, where $b/t_f = b/t = 43.0$:

$$b_e = 1.92t_f\sqrt{\frac{E}{F_y}}\left[1 - \frac{0.38}{b/t_f}\sqrt{\frac{E}{F_y}}\right] \leq b$$
$$\text{(Spec. Eq. F7-4)}$$

$$= 1.92(0.174 \text{ in.})\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}\left[1 - \left(\frac{0.38}{43.0}\right)\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}\right] \leq 7.48 \text{ in.}$$

$$= 6.33 \text{ in.}$$

The ineffective width of the compression flange is:

$$b - b_e = 7.48 \text{ in.} - 6.33 \text{ in.}$$
$$= 1.15 \text{ in.}$$

An exact calculation of the effective moment of inertia and section modulus could be performed taking into account the ineffective width of the compression flange and the resulting neutral axis shift. Alternatively, a simpler but slightly conservative calculation can be performed by removing the ineffective width symmetrically from both the top and bottom flanges.

$$I_{eff} = I - \left(\sum\frac{bt^3}{12} + \sum ad^2\right)$$

$$= 54.4 \text{ in.}^4 - 2\left[\frac{(1.15 \text{ in.})(0.174 \text{ in.})^3}{12} + (1.15 \text{ in.})(0.174 \text{ in.})\left(\frac{8.00 \text{ in.} - 0.174 \text{ in.}}{2}\right)^2\right]$$

$$= 48.3 \text{ in.}^4$$

---

# F-41

The effective section modulus can then be calculated as:

$$S_e = \frac{I_{eff}}{\left(\dfrac{H}{2}\right)}$$

$$= \frac{48.3 \text{ in.}^4}{\left(\dfrac{8.00 \text{ in.}}{2}\right)}$$

$$= 12.1 \text{ in.}^3$$

$$M_n = F_y S_e$$
$$\text{(Spec. Eq. F7-3)}$$

$$= (50 \text{ ksi})(12.1 \text{ in.}^3)$$
$$= 605 \text{ kip-in. or } 50.4 \text{ kip-ft}$$

**Available Flexural Strength**

From AISC *Specification* Section F1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(50.4 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{50.4 \text{ kip-ft}}{1.67}$ |
| $= 45.4 \text{ kip-ft} > 41.3 \text{ kip-ft}$ **o.k.** | $= 30.2 \text{ kip-ft} > 27.6 \text{ kip-ft}$ **o.k.** |

Note that the calculated available strengths are somewhat lower than those in AISC *Manual* Table 3-13 due to the use of the conservative calculation of the effective section modulus. Also, note that per the User Note in AISC *Specification* Section F7.4, lateral-torsional buckling is not applicable to square HSS.

---

# F-42

## EXAMPLE F.9A PIPE FLEXURAL MEMBER

### Given:

Using AISC *Manual* tables, select a Pipe shape with an 8 in. nominal diameter for the span and uniform dead and live loads shown in Figure F.9A. There is no deflection limit for this beam. The beam is simply supported and braced at end points only. The Pipe is ASTM A53/A53M Grade B material.

$$w_D = 0.32 \text{ kip/ft}$$
$$w_L = 0.96 \text{ kip/ft}$$

```
        |  |  |  |  |  |  |  |  |
        ●  (braced at end points only)  ●
        |←────── L = 16'-0" ──────→|
```

*Fig. F.9A. Beam loading and bracing diagram.*

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A53/A53M Grade B
$F_y = 35 \text{ ksi}$

From Chapter 2 of ASCE/SEI 7, the required flexural strength is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.32 \text{ kip/ft}) + 1.6(0.96 \text{ kip/ft})$ | $w_a = 0.32 \text{ kip/ft} + 0.96 \text{ kip/ft}$ |
| $= 1.92 \text{ kip/ft}$ | $= 1.28 \text{ kip/ft}$ |
| From AISC *Manual* Table 3-22, Case 1: | From AISC *Manual* Table 3-22, Case 1: |
| $M_u = \dfrac{w_u L^2}{8}$ | $M_a = \dfrac{w_a L^2}{8}$ |
| $= \dfrac{(1.92 \text{ kip/ft})(16 \text{ ft})^2}{8}$ | $= \dfrac{(1.28 \text{ kip/ft})(16 \text{ ft})^2}{8}$ |
| $= 61.4 \text{ kip-ft}$ | $= 41.0 \text{ kip-ft}$ |

**Pipe Selection**

Select a member from AISC *Manual* Table 3-15 having the required strength.

Select Pipe 8 x-Strong.

From AISC *Manual* Table 3-15, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 81.4 \text{ kip-ft} > 61.4 \text{ kip-ft}$ **o.k.** | $\dfrac{M_n}{\Omega_b} = 54.1 \text{ kip-ft} > 41.0 \text{ kip-ft}$ **o.k.** |

---

# F-43

## EXAMPLE F.9B PIPE FLEXURAL MEMBER

### Given:

The available strength in Example F.9A was easily determined using AISC *Manual* Table 3-15. The following example demonstrates the calculation of the available strength by directly applying the AISC *Specification*.

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A53/A53M Grade B
$F_y = 35 \text{ ksi}$

From AISC *Manual* Table 1-14, the geometric properties are as follows:

Pipe 8 x-Strong
$Z = 31.0 \text{ in.}^3$
$D/t = 18.5$

The required flexural strength from Example F.9A is:

| LRFD | ASD |
|------|-----|
| $M_u = 61.4 \text{ kip-ft}$ | $M_a = 41.0 \text{ kip-ft}$ |

**Slenderness Check**

Determine the limiting diameter-to-thickness ratio for a compact section from AISC *Specification* Table B4.1b Case 20.

$$\lambda_p = 0.07\frac{E}{F_y}$$

$$= 0.07\left(\frac{29,000 \text{ ksi}}{35 \text{ ksi}}\right)$$

$$= 58.0$$

$$\lambda = D/t$$
$$= 18.5 < \lambda_p$$ ; therefore, the section is compact and the limit state of local buckling does not apply

$$\frac{0.45E}{F_y} = \frac{0.45(29,000 \text{ ksi})}{35 \text{ ksi}}$$
$$= 373 > 18.5$$ ; therefore, AISC *Specification* Section F8 applies

**Nominal Flexural Strength**

Based on the limit state of yielding given in AISC *Specification* Section F8.1:

$$M_n = M_p = F_y Z$$
$$\text{(Spec. Eq. F8-1)}$$

$$= (35 \text{ ksi})(31.0 \text{ in.}^3)$$
$$= 1,090 \text{ kip-in. or } 90.4 \text{ kip-ft}$$

---

# F-44

**Available Flexural Strength**

From AISC *Specification* Section F1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(90.4 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{90.4 \text{ kip-ft}}{1.67}$ |
| $= 81.4 \text{ kip-ft} > 61.4 \text{ kip-ft}$ **o.k.** | $= 54.1 \text{ kip-ft} > 41.0 \text{ kip-ft}$ **o.k.** |

---

# F-45

## EXAMPLE F.10 WT-SHAPE FLEXURAL MEMBER

### Given:

Directly applying the requirements of the AISC *Specification*, select a WT beam with a 5 in. nominal depth for the span and uniform dead and live loads shown in Figure F.10. The toe of the stem of the WT is in tension. There is no deflection limit for this member. The beam is simply supported and continuously braced. The WT is ASTM A992/A992M material.

$$w_D = 0.08 \text{ kip/ft}$$
$$w_L = 0.24 \text{ kip/ft}$$

```
        |  |  |  |  |  |  |  |
        ●  (continuously braced)  ●
        |←──── L = 6'-0" ────→|
```

*Fig. F.10. Beam loading and bracing diagram.*

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

From Chapter 2 of ASCE/SEI 7, the required flexural strength is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.08 \text{ kip/ft}) + 1.6(0.24 \text{ kip/ft})$ | $w_a = 0.08 \text{ kip/ft} + 0.24 \text{ kip/ft}$ |
| $= 0.480 \text{ kip/ft}$ | $= 0.320 \text{ kip/ft}$ |
| From AISC *Manual* Table 3-22, Case 1: | From AISC *Manual* Table 3-22, Case 1: |
| $M_u = \dfrac{w_u L^2}{8}$ | $M_a = \dfrac{w_a L^2}{8}$ |
| $= \dfrac{(0.480 \text{ kip/ft})(6 \text{ ft})^2}{8}$ | $= \dfrac{(0.320 \text{ kip/ft})(6 \text{ ft})^2}{8}$ |
| $= 2.16 \text{ kip-ft}$ | $= 1.44 \text{ kip-ft}$ |

Try a WT5×6.

From AISC *Manual* Table 1-8, the geometric properties are as follows:

WT5×6
$d = 4.94 \text{ in.}$
$I_x = 4.35 \text{ in.}^4$
$Z_x = 2.20 \text{ in.}^3$
$S_x = 1.22 \text{ in.}^3$
$b_f = 3.96 \text{ in.}$
$t_f = 0.210 \text{ in.}$
$\overline{y} = 1.36 \text{ in.}$

---

# F-46

$$\frac{b_f}{2t_f} = 9.43$$

**Nominal Flexural Strength**

**Yielding**

From AISC *Specification* Section F9.1, for the limit state of yielding:

$$M_n = M_p$$
$$\text{(Spec. Eq. F9-1)}$$

$$M_y = F_y S_x$$
$$\text{(Spec. Eq. F9-3)}$$

$$= (50 \text{ ksi})(1.22 \text{ in.}^3)$$
$$= 61.0 \text{ kip-in.}$$

$$M_p = F_y Z_x \leq 1.6M_y \text{ (for stems in tension)}$$
$$\text{(Spec. Eq. F9-2)}$$

$$= (50 \text{ ksi})(2.20 \text{ in.}^3) \leq 1.6(61.0 \text{ kip-in.})$$
$$= 110 \text{ kip-in.} > 97.6 \text{ kip-in.}$$
$$= 97.6 \text{ kip-in. or } 8.13 \text{ kip-ft}$$

**Lateral-Torsional Buckling**

From AISC *Specification* Section F9.2, because the WT is continuously braced, the limit state of lateral-torsional buckling does not apply.

**Flange Local Buckling**

The limit state of flange local buckling is checked using AISC *Specification* Section F9.3.

**Flange Slenderness**

$$\lambda = \frac{b_f}{2t_f}$$
$$= 9.43$$

From AISC *Specification* Table B4.1b, Case 10, the limiting width-to-thickness ratio for the flange is:

$$\lambda_{pf} = 0.38\sqrt{\frac{E}{F_y}}$$

$$= 0.38\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 9.15$$

$$\lambda_{rf} = 1.0\sqrt{\frac{E}{F_y}}$$

$$= 1.0\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 24.1$$

---

# F-47

Because $\lambda_{pf} < \lambda < \lambda_{rf}$, the flange is noncompact, and the limit state of flange local buckling will apply.

$$S_{xc} = \frac{I_x}{\overline{y}}$$

$$= \frac{4.35 \text{ in.}^4}{1.36 \text{ in.}}$$

$$= 3.20 \text{ in.}^3$$

From AISC *Specification* Section F9.3, the nominal flexural strength of a tee with a noncompact flange is:

$$M_n = \left[M_p - (M_p - 0.7F_y S_{xc})\left(\frac{\lambda - \lambda_{pf}}{\lambda_{rf} - \lambda_{pf}}\right)\right] \leq 1.6M_y$$
$$\text{(Spec. Eq. F9-14)}$$

$$= \left\{110 \text{ kip-in.} - \left[110 \text{ kip-in.} - 0.7(50 \text{ ksi})(3.20 \text{ in.}^3)\right]\left[\frac{9.43 - 9.15}{24.1 - 9.15}\right]\right\}$$

$$= 110 \text{ kip-in.} > 1.6M_y = 97.6 \text{ kip-in.}$$
$$= 97.6 \text{ kip-in. or } 8.13 \text{ kip-ft}$$

Flexural yielding controls:

$$M_n = 8.13 \text{ kip-ft}$$

**Available Flexural Strength**

From AISC *Specification* Section F1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(8.13 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{8.13 \text{ kip-ft}}{1.67}$ |
| $= 7.32 \text{ kip-ft} > 2.16 \text{ kip-ft}$ **o.k.** | $= 4.87 \text{ kip-ft} > 1.44 \text{ kip-ft}$ **o.k.** |

---

# F-48

## EXAMPLE F.11A SINGLE-ANGLE FLEXURAL MEMBER WITH BRACING AT ENDS ONLY

### Given:

Directly applying the requirements of the AISC *Specification*, select a single angle for the span and uniform dead and live loads shown in Figure F.11A. The vertical leg of the single angle is up and the toe is in compression. There are no horizontal loads. There is no deflection limit for this angle. The beam is simply supported and braced at the end points only. Assume bending about the geometric *x-x* axis and that there is no lateral-torsional restraint. The angle is ASTM A572/A572M Grade 50 material.

$$w_D = 0.05 \text{ kip/ft}$$
$$w_L = 0.15 \text{ kip/ft}$$

```
        |  |  |  |  |  |  |  |
        ●  (braced at end points only)  ●
        |←────── L = 6'-0" ──────→|
```

*Fig. F.11A. Beam loading and bracing diagram.*

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$

From Chapter 2 of ASCE/SEI 7, the required flexural strength is:

| LRFD | ASD |
|------|-----|
| $w_{ux} = 1.2(0.05 \text{ kip/ft}) + 1.6(0.15 \text{ kip/ft})$ | $w_{ax} = 0.05 \text{ kip/ft} + 0.15 \text{ kip/ft}$ |
| $= 0.300 \text{ kip/ft}$ | $= 0.200 \text{ kip/ft}$ |
| From AISC *Manual* Table 3-22, Case 1: | From AISC *Manual* Table 3-22, Case 1: |
| $M_{ux} = \dfrac{w_{ux} L^2}{8}$ | $M_{ax} = \dfrac{w_{ax} L^2}{8}$ |
| $= \dfrac{(0.300 \text{ kip/ft})(6 \text{ ft})^2}{8}$ | $= \dfrac{(0.200 \text{ kip/ft})(6 \text{ ft})^2}{8}$ |
| $= 1.35 \text{ kip-ft}$ | $= 0.900 \text{ kip-ft}$ |

Try an L4×4×¼.

From AISC *Manual* Table 1-7, the geometric properties are as follows:

L4×4×¼
$S_x = 1.03 \text{ in.}^3$

**Nominal Flexural Strength**

**Yielding**

From AISC *Specification* Section F10.1, the nominal flexural strength due to the limit state of flexural yielding is:

---

# F-49

$$M_n = 1.5M_y$$
$$\text{(Spec. Eq. F10-1)}$$

$$= 1.5F_y S_x$$

$$= 1.5(50 \text{ ksi})(1.03 \text{ in.}^3)$$

$$= 77.3 \text{ kip-in. or } 6.44 \text{ kip-ft}$$

**Lateral-Torsional Buckling**

From AISC *Specification* Section F10.2, for single angles bending about a geometric axis with no lateral-torsional restraint, $M_c$ is taken as 0.80 times the yield moment calculated using the geometric section modulus.

$$M_y = 0.80F_y S_x$$

$$= 0.80(50 \text{ ksi})(1.03 \text{ in.}^3)$$

$$= 41.2 \text{ kip-in.}$$

Determine $M_{cr}$.

For bending moment about one of the geometric axes of an equal-leg angle with no axial compression, with no lateral-torsional restraint, and with maximum compression at the toe, use AISC *Specification* Equation F10-5a.

$C_b = 1.14$ from AISC *Manual* Table 3-1

$$M_{cr} = \frac{0.58Eb^4C_b}{L_b^2}\left[\sqrt{1 + 0.88\left(\frac{L_bt}{b^2}\right)^2} - 1\right]$$
$$\text{(Spec. Eq. F10-5a)}$$

$$= \frac{0.58(29,000 \text{ ksi})(4.00 \text{ in.})^4(\frac{1}{4} \text{ in.})(1.14)}{\left[(6 \text{ ft})(12 \text{ in./ft})\right]^2}\left\{\sqrt{1 + 0.88\left[\frac{(6 \text{ ft})(12 \text{ in./ft})(\frac{1}{4} \text{ in.})}{(4.00 \text{ in.})^2}\right]^2} - 1\right\}$$

$$= 107 \text{ kip-in.}$$

$$\frac{M_y}{M_{cr}} = \frac{41.2 \text{ kip-in.}}{107 \text{ kip-in.}}$$
$$= 0.385 < 1.0$$ ; therefore, AISC *Specification* Equation F10-2 is applicable

$$M_n = \left[1.92 - 1.17\sqrt{\frac{M_y}{M_{cr}}}\right]M_y \leq 1.5M_y$$
$$\text{(Spec. Eq. F10-2)}$$

$$= \left[1.92 - 1.17\sqrt{\frac{41.2 \text{ kip-in.}}{107 \text{ kip-in.}}}\right](41.2 \text{ kip-in.}) < 1.5(41.2 \text{ kip-in.})$$

$$= 49.2 \text{ kip-in.} < 61.8 \text{ kip-in.}$$
$$= 49.2 \text{ kip-in. or } 4.10 \text{ kip-ft}$$

**Leg Local Buckling**

AISC *Specification* Section F10.3 applies when the toe of the leg is in compression.

Check slenderness of the leg in compression.

---

# F-50

$$\lambda = b/t$$

$$= \frac{4.00 \text{ in.}}{\frac{1}{4} \text{ in.}}$$

$$= 16.0$$

From AISC *Specification* Table B4.1b, Case 12, the limiting width-to-thickness ratios are:

$$\lambda_p = 0.54\sqrt{\frac{E}{F_y}}$$

$$= 0.54\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 13.0$$

$$\lambda_r = 0.91\sqrt{\frac{E}{F_y}}$$

$$= 0.91\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 21.9$$

Because $\lambda_p < \lambda < \lambda_r$, the leg is noncompact in flexure.

$$S_c = 0.80S_x$$

$$= 0.80(1.03 \text{ in.}^3)$$

$$= 0.824 \text{ in.}^3$$

$$M_n = F_y S_c\left[2.43 - 1.72\left(\frac{b}{t}\right)\sqrt{\frac{F_y}{E}}\right]$$
$$\text{(Spec. Eq. F10-6)}$$

$$= (50 \text{ ksi})(0.824 \text{ in.}^3)\left[2.43 - 1.72(16.0)\sqrt{\frac{50 \text{ ksi}}{29,000 \text{ ksi}}}\right]$$

$$= 53.0 \text{ kip-in. or } 4.42 \text{ kip-ft}$$

The lateral-torsional buckling limit state controls.

$$M_n = 4.10 \text{ kip-ft}$$

**Available Flexural Strength**

From AISC *Specification* Section F1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(4.10 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{4.10 \text{ kip-ft}}{1.67}$ |
| $= 3.69 \text{ kip-ft} > 1.35 \text{ kip-ft}$ **o.k.** | $= 2.46 \text{ kip-ft} > 0.900 \text{ kip-ft}$ **o.k.** |

---

# F-51

## EXAMPLE F.11B SINGLE-ANGLE FLEXURAL MEMBER WITH BRACING AT ENDS AND MIDSPAN

### Given:

Directly applying the requirements of the AISC *Specification*, select a single angle for span and uniform dead and live loads as shown in Figure F.11B. The vertical leg of the single angle is up and the toe is in compression. There are no horizontal loads. There is no deflection limit for this angle. The beam is simply supported and braced at the end points and midspan. Assume bending about the geometric *x-x* axis and that there is lateral-torsional restraint at the midspan and ends only. The angle is ASTM A572/A572M Grade 50 material.

$$w_D = 0.05 \text{ kip/ft}$$
$$w_L = 0.15 \text{ kip/ft}$$

```
        |  |  |  |  |  |  |  |
        ●        |        ●
        |  (braced at end points and midspan)
        |←──── L = 6'-0" ────→|
```

*Fig. F.11B. Beam loading and bracing diagram.*

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$

From Chapter 2 of ASCE/SEI 7, the required flexural strength is:

| LRFD | ASD |
|------|-----|
| $w_{ux} = 1.2(0.05 \text{ kip/ft}) + 1.6(0.15 \text{ kip/ft})$ | $w_{ax} = 0.05 \text{ kip/ft} + 0.15 \text{ kip/ft}$ |
| $= 0.300 \text{ kip/ft}$ | $= 0.200 \text{ kip/ft}$ |
| From AISC *Manual* Table 3-22, Case 1: | From AISC *Manual* Table 3-22, Case 1: |
| $M_{ux} = \dfrac{w_{ux} L^2}{8}$ | $M_{ax} = \dfrac{w_{ax} L^2}{8}$ |
| $= \dfrac{(0.300 \text{ kip/ft})(6 \text{ ft})^2}{8}$ | $= \dfrac{(0.200 \text{ kip/ft})(6 \text{ ft})^2}{8}$ |
| $= 1.35 \text{ kip-ft}$ | $= 0.900 \text{ kip-ft}$ |

Try an L4×4×¼.

From AISC *Manual* Table 1-7, the geometric properties are as follows:

L4×4×¼
$S_x = 1.03 \text{ in.}^3$

**Nominal Flexural Strength**

**Flexural Yielding**

From AISC *Specification* Section F10.1, the nominal flexural strength due to the limit state of flexural yielding is:

---

# F-52

$$M_n = 1.5M_y$$
$$\text{(Spec. Eq. F10-1)}$$

$$= 1.5F_y S_x$$

$$= 1.5(50 \text{ ksi})(1.03 \text{ in.}^3)$$

$$= 77.3 \text{ kip-in. or } 6.44 \text{ kip-ft}$$

**Lateral-Torsional Buckling**

From AISC *Specification* Section F10.2(2)(ii), for single angles with lateral-torsional restraint at the point of maximum moment, $M_c$ is taken as the yield moment calculated using the geometric section modulus.

$$M_y = F_y S_x$$

$$= (50 \text{ ksi})(1.03 \text{ in.}^3)$$

$$= 51.5 \text{ kip-in.}$$

Determine $M_{cr}$.

For bending moment about one of the geometric axes of an equal-leg angle with no axial compression, with lateral-torsional restraint at the point of maximum moment only (at midspan in this case), and with maximum compression at the toe, $M_{cr}$ shall be taken as 1.25 times $M_{cr}$ computed using AISC *Specification* Equation F10-5a.

$C_b = 1.30$ from AISC *Manual* Table 3-1

$$M_{cr} = 1.25\left(\frac{0.58Eb^4C_b}{L_b^2}\right)\left(\sqrt{1 + 0.88\left(\frac{L_bt}{b^2}\right)^2} - 1\right)$$
$$\text{(from Spec. Eq. F10-5a)}$$

$$= 1.25\left[\frac{0.58(29,000 \text{ ksi})(4.00 \text{ in.})^4(\frac{1}{4} \text{ in.})(1.30)}{\left[(3 \text{ ft})(12 \text{ in./ft})\right]^2}\right]\left\{\sqrt{1 + 0.88\left[\frac{(3 \text{ ft})(12 \text{ in./ft})(\frac{1}{4} \text{ in.})}{(4.00 \text{ in.})^2}\right]^2} - 1\right\}$$

$$= 176 \text{ kip-in.}$$

$$\frac{M_y}{M_{cr}} = \frac{51.5 \text{ kip-in.}}{176 \text{ kip-in.}}$$
$$= 0.293 < 1.0$$ ; therefore, AISC *Specification* Equation F10-2 is applicable

$$M_n = \left[1.92 - 1.17\sqrt{\frac{M_y}{M_{cr}}}\right]M_y \leq 1.5M_y$$
$$\text{(Spec. Eq. F10-2)}$$

$$= \left[1.92 - 1.17\sqrt{\frac{51.5 \text{ kip-in.}}{176 \text{ kip-in.}}}\right](51.5 \text{ kip-in.}) < 1.5(51.5 \text{ kip-in.})$$

$$= 66.3 \text{ kip-in.} < 77.3 \text{ kip-in.}$$
$$= 66.3 \text{ kip-in. or } 5.53 \text{ kip-ft}$$

**Leg Local Buckling**

$M_n = 53.0 \text{ kip-in. or } 4.42 \text{ kip-ft}$ (from Example F.11A)

---

# F-53

Note that the available leg local buckling strength calculated in Example F.11A uses a reduced elastic section modulus (0.80$S_c$) because the beam has no lateral-torsional restraint. In this example, the beam is braced at midspan and does not need to use the reduced elastic section modulus; therefore, the leg local buckling strength in this example is conservative.

The leg local buckling limit state controls.

$$M_n = 4.42 \text{ kip-ft}$$

**Available Flexural Strength**

From AISC *Specification* Section F1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(4.42 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{4.42 \text{ kip-ft}}{1.67}$ |
| $= 3.98 \text{ kip-ft} > 1.35 \text{ kip-ft}$ **o.k.** | $= 2.65 \text{ kip-ft} > 0.900 \text{ kip-ft}$ **o.k.** |

---

# F-54

## EXAMPLE F.11C SINGLE-ANGLE FLEXURAL MEMBER WITH VERTICAL AND HORIZONTAL LOADING

### Given:

Directly applying the requirements of the AISC *Specification*, select a single angle for the span and uniform vertical dead and live loads shown in Figure F.11C-1. The horizontal load is a uniform wind load. There is no deflection limit for this angle. The angle is simply supported and braced at the end points only and there is no lateral-torsional restraint. Use load combination 4a from Section 2.3.1 of ASCE/SEI 7 for LRFD and load combination 6a from Section 2.4.1 of ASCE/SEI 7 for ASD. The angle is ASTM A572/A572M Grade 50 material.

```
                        w_D = 0.05 kip/ft
                        w_L = 0.15 kip/ft
                    ↓   ↓   ↓
                        |   |   |     w
        ●               | z |   /
        |  (braced at end points only)  ●
        |                              x ←——  w_W = 0.12 kip/ft
        |←──── L = 6'-0" ────→|
                w    y    z

    (a) Beam bracing diagram     (b) Beam loading
```

*Fig. F.11C-1. Beam loading and bracing diagram.*

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$

From Chapter 2 of ASCE/SEI 7, the required flexural strength is:

| LRFD | ASD |
|------|-----|
| $w_{ux} = 1.2(0.05 \text{ kip/ft}) + 0.15 \text{ kip/ft}$ | $w_{ax} = 0.05 \text{ kip/ft} + 0.75(0.15 \text{ kip/ft})$ |
| $= 0.210 \text{ kip/ft}$ | $= 0.163 \text{ kip/ft}$ |
| $w_{up} = 1.0(0.12 \text{ kip/ft})$ | $w_{ap} = 0.75[0.6(0.12 \text{ kip/ft})]$ |
| $= 0.120 \text{ kip/ft}$ | $= 0.0540 \text{ kip/ft}$ |
| $M_{ux} = \dfrac{w_{ux} L^2}{8}$ | $M_{ax} = \dfrac{w_{ax} L^2}{8}$ |
| $= \dfrac{(0.210 \text{ kip/ft})(6 \text{ ft})^2}{8}$ | $= \dfrac{(0.163 \text{ kip/ft})(6 \text{ ft})^2}{8}$ |
| $= 0.945 \text{ kip-ft}$ | $= 0.734 \text{ kip-ft}$ |

---

# F-55

| LRFD | ASD |
|------|-----|
| $M_{uy} = \dfrac{w_{uy} L^2}{8}$ | $M_{ay} = \dfrac{w_{ay} L^2}{8}$ |
| $= \dfrac{(0.120 \text{ kip/ft})(6 \text{ ft})^2}{8}$ | $= \dfrac{(0.0540 \text{ kip/ft})(6 \text{ ft})^2}{8}$ |
| $= 0.540 \text{ kip-ft}$ | $= 0.243 \text{ kip-ft}$ |

Try an L4×4×¼.

Sign conventions for geometric axes moments are:

| LRFD | ASD |
|------|-----|
| $M_{ux} = -0.945 \text{ kip-ft}$ | $M_{ax} = -0.734 \text{ kip-ft}$ |
| $M_{uy} = 0.540 \text{ kip-ft}$ | $M_{ay} = 0.243 \text{ kip-ft}$ |

As shown in Figure F.11C-2, the principal axes moments are:

| LRFD | ASD |
|------|-----|
| $M_{uw} = M_{ux} \cos\alpha + M_{uy} \sin\alpha$ | $M_{aw} = M_{ax} \cos\alpha + M_{ay} \sin\alpha$ |
| $= (-0.945 \text{kip-ft})(\cos 45°)$ | $= (-0.734 \text{kip-ft})(\cos 45°)$ |
| $+ (0.540 \text{ kip-ft})(\sin 45°)$ | $+ (0.243 \text{ kip-ft})(\sin 45°)$ |
| $= -0.286 \text{ kip-ft}$ | $= -0.347 \text{ kip-ft}$ |
| $M_{uz} = -M_{ux} \sin\alpha + M_{uy} \cos\alpha$ | $M_{az} = -M_{ax} \sin\alpha + M_{ay} \cos\alpha$ |
| $= -(-0.945 \text{kip-ft})(\sin 45°)$ | $= -(-0.734 \text{kip-ft})(\sin 45°)$ |
| $+ (0.540 \text{ kip-ft})(\cos 45°)$ | $+ (0.243 \text{ kip-ft})(\cos 45°)$ |
| $= 1.05 \text{ kip-ft}$ | $= 0.691 \text{ kip-ft}$ |

```
            Y
        α ⌐  | My              Muz = 1.05 kip-ft        Muw = -0.286 kip-ft
    z       A ↑                 Maz = 0.691 kip-ft   A   Maw = -0.347 kip-ft
   Mz       | |      w                         ↗
            | |     ⁄            zc                  ⁄
    x ──────|─|────⁄ Mx     x   ───────────────  ⁄
           B└─────C                        B───────C
    w     y   \  w                            \  w
               \ z                             \ z

    For an equal leg angle, tan α = 1.00 and α = 45°

(a) Positive geometric and principal axes    (b) Principal axis moments
```

*Fig. F.11C-2. Example F.11C single angle geometric and principal axes moments.*

---

# F-56

From AISC *Manual* Table 1-7, the geometric properties are as follows:

L4×4×¼
$A_g = 1.93 \text{ in.}^2$
$S_x = S_y = 1.03 \text{ in.}^3$
$I_x = I_y = 3.00 \text{ in.}^4$
$I_z = 1.19 \text{ in.}^4$
$r_z = 0.783 \text{ in.}$

Additional principal axes properties from the AISC *Shapes Database* are as follows:

$w_B = 1.53 \text{ in.}$
$w_C = 1.39 \text{ in.}$
$z_C = 2.74 \text{ in.}$
$I_w = 4.82 \text{ in.}^4$
$S_{zB} = 0.778 \text{ in.}^3$
$S_{zC} = 0.856 \text{ in.}^3$
$S_{wC} = 1.76 \text{ in.}^3$

**Nominal Flexural Strength—Z-Z Axis**

Note that $M_{uz}$ and $M_{az}$ are positive; therefore, the toes of the angle are in compression.

**Flexural Yielding**

From AISC *Specification* Section F10.1, the nominal flexural strength due to the limit state of flexural yielding is:

$$M_{nz} = 1.5M_y$$
$$\text{(from Spec. Eq. F10-1)}$$

$$= 1.5F_y S_{zB}$$

$$= 1.5(50 \text{ ksi})(0.778 \text{ in.}^3)$$

$$= 58.4 \text{ kip-in. or } 4.87 \text{ kip-ft}$$

**Lateral-Torsional Buckling**

From the User Note in AISC *Specification* Section F10, the limit state of lateral-torsional buckling does not apply for bending about the minor axis.

**Leg Local Buckling**

Check slenderness of outstanding leg in compression.

$$\lambda = b/t$$

$$= \frac{4.00 \text{ in.}}{\frac{1}{4} \text{ in.}}$$

$$= 16.0$$

From AISC *Specification* Table B4.1b, Case 12, the limiting width-to-thickness ratios are:

---

# F-57

$$\lambda_p = 0.54\sqrt{\frac{E}{F_y}}$$

$$= 0.54\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 13.0$$

$$\lambda_{rf} = 0.91\sqrt{\frac{E}{F_y}}$$

$$= 0.91\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 21.9$$

Because $\lambda_p < \lambda < \lambda_r$, the leg is noncompact in flexure.

$$S_c = S_{zC}$$ (toe in compression)

$$= 0.856 \text{ in.}^3$$

$$M_{nz} = F_y S_c\left[2.43 - 1.72\left(\frac{b}{t}\right)\sqrt{\frac{F_y}{E}}\right]$$
$$\text{(Spec. Eq. F10-6)}$$

$$= (50 \text{ ksi})(0.856 \text{ in.}^3)\left[2.43 - 1.72(16.0)\sqrt{\frac{50 \text{ ksi}}{29,000 \text{ ksi}}}\right]$$

$$= 55.1 \text{ kip-in. or } 4.59 \text{ kip-ft}$$

The leg local buckling limit state controls.

$$M_{nz} = 4.59 \text{ kip-ft}$$

**Available Flexural Strength—Z-Z Axis**

From AISC *Specification* Section F1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_{nz} = 0.90(4.59 \text{ kip-ft})$ | $\dfrac{M_{nz}}{\Omega_b} = \dfrac{4.59 \text{ kip-ft}}{1.67}$ |
| $= 4.13 \text{ kip-ft}$ | $= 2.75 \text{ kip-ft}$ |

**Nominal Flexural Strength—W-W Axis**

**Flexural Yielding**

$$M_{nw} = 1.5M_y$$
$$\text{(from Spec. Eq. F10-1)}$$

$$= 1.5F_y S_{wC}$$

$$= 1.5(50 \text{ ksi})(1.76 \text{ in.}^3)$$

$$= 132 \text{ kip-in. or } 11.0 \text{ kip-ft}$$

---

# F-58

**Lateral-Torsional Buckling**

Determine $M_{cr}$.

For bending about the major principal axis of an equal-leg angle without continuous lateral-torsional restraint, use AISC *Specification* Equation F10-4.

$C_b = 1.14$ from *Manual* Table 3-1

From AISC *Specification* Section F10.2(1), $\hat{B}_w = 0$ for equal leg angles.

$$M_{cr} = \frac{9EA_gIC_b}{8L_b}\left[\sqrt{1 + \left(4.4\frac{\hat{B}_wr_z}{L_bt}\right)^2} + 4.4\frac{\hat{B}_wr_z}{L_bt}\right]$$
$$\text{(Spec. Eq. F10-4)}$$

$$= \frac{9(29,000 \text{ ksi})(1.93 \text{ in.}^2)(0.783 \text{ in.})(\frac{1}{4} \text{ in.})(1.14)}{8(6 \text{ ft})(12 \text{ in./ft})}$$

$$\times\left\{\sqrt{1 + \left[4.4\frac{0(0.783 \text{ in.})}{(6 \text{ ft})(12 \text{ in./ft})(\frac{1}{4} \text{ in.})}\right]^2} + 4.4\left[\frac{0(0.783 \text{ in.})}{(6 \text{ ft})(12 \text{ in./ft})(\frac{1}{4} \text{ in.})}\right]\right\}$$

$$= 195 \text{ kip-in.}$$

$$M_y = F_y S_{wC}$$

$$= (50 \text{ ksi})(1.76 \text{ in.}^3)$$

$$= 88.0 \text{ kip-in.}$$

$$\frac{M_y}{M_{cr}} = \frac{88.0 \text{ kip-in.}}{195 \text{ kip-in.}}$$
$$= 0.451 < 1.0$$ , therefore, AISC *Specification* Equation F10-2 is applicable

$$M_{nw} = \left[1.92 - 1.17\sqrt{\frac{M_y}{M_{cr}}}\right]M_y \leq 1.5M_y$$
$$\text{(Spec. Eq. F10-2)}$$

$$= \left[1.92 - 1.17\sqrt{\frac{88.0 \text{ kip-in.}}{195 \text{ kip-in.}}}\right](88.0 \text{ kip-in.}) \leq 1.5(88.0 \text{ kip-in.})$$

$$= 99.8 \text{ kip-in.} < 132 \text{ kip-in.}$$
$$= 99.8 \text{ kip-in. or } 8.32 \text{ kip-ft}$$

**Leg Local Buckling**

From the preceding calculations, the leg is noncompact in flexure.

$$S_c = S_{wC}$$ (toe in compression)
$$= 1.76 \text{ in.}^3$$

---

# F-59

$$M_{nw} = F_y S_c\left[2.43 - 1.72\left(\frac{b}{t}\right)\sqrt{\frac{F_y}{E}}\right]$$
$$\text{(Spec. Eq. F10-6)}$$

$$= (50 \text{ ksi})(1.76 \text{ in.}^3)\left[2.43 - 1.72(16.0)\sqrt{\frac{50 \text{ ksi}}{29,000 \text{ ksi}}}\right]$$

$$= 113 \text{ kip-in. or } 9.42 \text{ kip-ft}$$

The lateral-torsional buckling limit state controls.

$$M_{nw} = 8.32 \text{ kip-ft}$$

**W-Axis Available Flexural Strength**

From AISC *Specification* Section F1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_{nw} = 0.90(8.32 \text{ kip-ft})$ | $\dfrac{M_{nw}}{\Omega_b} = \dfrac{8.32 \text{ kip-ft}}{1.67}$ |
| $= 7.49 \text{ kip-ft}$ | $= 4.98 \text{ kip-ft}$ |

**Combined Loading**

The moment resultant has components about both principal axes; therefore, the combined stress ratio must be checked using the provisions of AISC *Specification* Section H2.

$$\left|\frac{f_{uw}}{F_{cw}} + \frac{f_{ubw}}{F_{cbw}} + \frac{f_{uz}}{F_{cbz}}\right| \leq 1.0$$
$$\text{(Spec. Eq. H2-1)}$$

Note: Rather than convert moments into stresses, it is acceptable to simply use the moments in the interaction equation because the section properties that would be used to convert the moments to stresses are the same in the numerator and denominator of each term. It is also important for the designer to keep track of the signs of the stresses at each point so that the proper sign is applied when the terms are combined. The sign of the moments used to convert geometric axis moments to principal axis moments will indicate which points are in tension and which are in compression, but those signs will not be correct if they are used in the interaction equations directly.

Based on Figure F.11C-2, the required flexural strength and available flexural strength for this beam can be summarized as:

| LRFD | ASD |
|------|-----|
| $M_{uw} = 0.286 \text{ kip-ft}$ | $M_{aw} = 0.347 \text{ kip-ft}$ |
| $\phi_b M_{nw} = 7.49 \text{ kip-ft}$ | $\dfrac{M_{nw}}{\Omega_b} = 4.98 \text{ kip-ft}$ |
| $M_{uz} = 1.05 \text{ kip-ft}$ | $M_{az} = 0.691 \text{ kip-ft}$ |
| $\phi_b M_{nz} = 4.13 \text{ kip-ft}$ | $\dfrac{M_{nz}}{\Omega_b} = 2.75 \text{ kip-ft}$ |

---

# F-60

At point B:

$M_w$ causes no stress at point B; therefore, the stress ratio is set to zero. $M_z$ causes tension at point B; therefore, it will be taken as negative.

| LRFD | ASD |
|------|-----|
| $\left|0 - \dfrac{1.05 \text{ kip-ft}}{4.13 \text{ kip-ft}}\right| = 0.254 \leq 1.0$ **o.k.** | $\left|0 - \dfrac{0.691 \text{ kip-ft}}{2.75 \text{ kip-ft}}\right| = 0.251 \leq 1.0$ **o.k.** |

At point C:

$M_w$ causes tension at point C; therefore, it will be taken as negative. $M_z$ causes compression at point C; therefore, it will be taken as positive.

| LRFD | ASD |
|------|-----|
| $\left|\dfrac{0.286 \text{ kip-ft}}{7.49 \text{ kip-ft}} + \dfrac{1.05 \text{ kip-ft}}{4.13 \text{ kip-ft}}\right| = 0.216 \leq 1.0$ **o.k.** | $\left|\dfrac{0.347 \text{ kip-ft}}{4.98 \text{ kip-ft}} + \dfrac{0.691 \text{ kip-ft}}{2.75 \text{ kip-ft}}\right| = 0.182 \leq 1.0$ **o.k.** |

At point A:

$M_w$ and $M_z$ cause compression at point A; therefore, both will be taken as positive.

| LRFD | ASD |
|------|-----|
| $\left|\dfrac{0.286 \text{ kip-ft}}{7.49 \text{ kip-ft}} + \dfrac{1.05 \text{ kip-ft}}{4.13 \text{ kip-ft}}\right| = 0.292 \leq 1.0$ **o.k.** | $\left|\dfrac{0.347 \text{ kip-ft}}{4.98 \text{ kip-ft}} + \dfrac{0.691 \text{ kip-ft}}{2.75 \text{ kip-ft}}\right| = 0.321 \leq 1.0$ **o.k.** |

Thus, the interaction of stresses at each point is seen to be less than 1.0, and this member is adequate to carry the required load. Although all three points were checked, it was expected that point A would be the controlling point because compressive stresses are additive at this point.

---

# F-61

## EXAMPLE F.12 RECTANGULAR BAR IN MAJOR-AXIS BENDING

### Given:

Directly applying the requirements of the AISC *Specification*, select a rectangular bar for the span and uniform vertical dead and live loads shown in Figure F.12. The beam is simply supported and braced at the end points and midspan. Conservatively use $C_b = 1.0$. Limit the depth of the member to 5 in. The bar is ASTM A572/A572M Grade 50 material.

$$w_D = 0.44 \text{ kip/ft}$$
$$w_L = 1.32 \text{ kip/ft}$$

```
        |  |  |  |  |  |  |  |  |
        ●        |        ●
        |  (braced at end points and midspan)
        |←──── L = 12'-0" ────→|
```

*Fig. F.12. Beam loading and bracing diagram.*

### Solution:

From AISC *Manual* Table 2-5, the material properties are as follows:

ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$

From Chapter 2 of ASCE/SEI 7, the required flexural strength is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.44 \text{ kip/ft}) + 1.6(1.32 \text{ kip/ft})$ | $w_a = 0.44 \text{ kip/ft} + 1.32 \text{ kip/ft}$ |
| $= 2.64 \text{ kip/ft}$ | $= 1.76 \text{ kip/ft}$ |
| From AISC *Manual* Table 3-22, Case 1: | From AISC *Manual* Table 3-22, Case 1: |
| $M_u = \dfrac{w_u L^2}{8}$ | $M_a = \dfrac{w_a L^2}{8}$ |
| $= \dfrac{(2.64 \text{ kip/ft})(12 \text{ ft})^2}{8}$ | $= \dfrac{(1.76 \text{ kip/ft})(12 \text{ ft})^2}{8}$ |
| $= 47.5 \text{ kip-ft}$ | $= 31.7 \text{ kip-ft}$ |

Try a BAR 5 in. × 3 in.

From AISC *Manual* Table 17-25, the geometric properties are as follows:

$$S_x = \frac{bd^2}{6}$$

$$= \frac{(3.00 \text{ in.})(5.00 \text{ in.})^2}{6}$$

$$= 12.5 \text{ in.}^3$$

---

# F-62

$$Z_x = \frac{bd^2}{4}$$

$$= \frac{(3.00 \text{ in.})(5.00 \text{ in.})^2}{4}$$

$$= 18.8 \text{ in.}^3$$

**Nominal Flexural Strength**

**Flexural Yielding**

From AISC *Specification* Section F11.1, for rectangular bars:

$$M_n = M_p = F_y Z \leq 1.5F_y S$$
$$\text{(Spec. Eq. F11-1)}$$

$$= (50 \text{ ksi})(18.8 \text{ in.}^3) > 1.5(50 \text{ ksi})(12.5 \text{ in.}^3)$$

$$= 940 \text{ kip-in.} > 938 \text{ kip-in.}$$
$$= 938 \text{ kip-in. or } 78.2 \text{ kip-ft}$$

**Lateral-Torsional Buckling**

Check limit from AISC *Specification* Section F11.2:

$$\frac{L_bd}{t^2} = \frac{(6 \text{ ft})(12 \text{ in./ft})(5.00 \text{ in.})}{(3.00 \text{ in.})^2}$$

$$= 40.0$$

$$\frac{0.08E}{F_y} = \frac{0.08(29,000 \text{ ksi})}{50 \text{ ksi}}$$

$$= 46.4$$

Because $\dfrac{L_bd}{t^2} \leq \dfrac{0.08E}{F_y}$, the lateral-torsional buckling limit state does not apply.

**Available Flexural Strength**

From AISC *Specification* Section F1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(78.2 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{78.2 \text{ kip-ft}}{1.67}$ |
| $= 70.4 \text{ kip-ft} > 47.5 \text{ kip-ft}$ **o.k.** | $= 46.8 \text{ kip-ft} > 31.7 \text{ kip-ft}$ **o.k.** |

---

# F-63

## EXAMPLE F.13 ROUND BAR IN BENDING

### Given:

Select a round bar for the span and concentrated dead and live loads, at midspan, shown in Figure F.13. The beam is simply supported and braced at the end points only. Conservatively use $C_b = 1.0$. Limit the diameter of the member to 2 in. The weight of the bar is negligible. The bar is ASTM A572/A572M Grade 50 material.

$$P_D = 0.10 \text{ kip}$$
$$P_L = 0.25 \text{ kip}$$

```
                    ↓
        ●           |           ●
        |  (braced at end points only)
        |←──── L = 2'-6" ────→|
```

*Fig. F.13. Beam loading and bracing diagram.*

### Solution:

From AISC *Manual* Table 2-5, the material properties are as follows:

ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$

From Chapter 2 of ASCE/SEI 7 the required flexural strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(0.10 \text{ kip}) + 1.6(0.25 \text{ kip})$ | $P_a = 0.10 \text{ kip} + 0.25 \text{ kip}$ |
| $= 0.520 \text{ kip}$ | $= 0.350 \text{ kip}$ |
| From AISC *Manual* Table 3-22, Case 7: | From AISC *Manual* Table 3-22, Case 7: |
| $M_u = \dfrac{P_u L}{4}$ | $M_a = \dfrac{P_a L}{4}$ |
| $= \dfrac{(0.520 \text{ kip})(2.5 \text{ ft})}{4}$ | $= \dfrac{(0.350 \text{ kip})(2.5 \text{ ft})}{4}$ |
| $= 0.325 \text{ kip-ft}$ | $= 0.219 \text{ kip-ft}$ |

Try a BAR 1-in.-diameter.

From AISC *Manual* Table 17-25, the geometric properties are as follows:

$$S = \frac{\pi d^3}{32}$$

$$= \frac{\pi(1.00 \text{ in.})^3}{32}$$

$$= 0.0982 \text{ in.}^3$$

---

# F-64

$$Z = \frac{d^3}{6}$$

$$= \frac{(1.00 \text{ in.})^3}{6}$$

$$= 0.167 \text{ in.}^3$$

**Nominal Flexural Strength**

**Flexural Yielding**

From AISC *Specification* Section F11.1 for rounds, the nominal flexural strength based on the limit state of flexural yielding is:

$$M_n = M_p = F_y Z \leq 1.6F_y S_x$$
$$\text{(Spec. Eq. F11-2)}$$

$$= (50 \text{ ksi})(0.167 \text{ in.}^3) > 1.6(50 \text{ ksi})(0.0982 \text{ in.}^3)$$

$$= 8.35 \text{ kip-in.} > 7.86 \text{ kip-in.}$$
$$= 7.86 \text{ kip-in. or } 0.655 \text{ kip-ft}$$

**Lateral-Torsional Buckling**

From *AISC Specification* Section F11.2, the limit state of lateral-torsional buckling need not be considered for rounds.

The flexural yielding limit state controls.

$$M_n = 0.655 \text{ kip-ft}$$

**Available Flexural Strength**

From AISC *Specification* Section F1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(0.655 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{0.655 \text{ kip-ft}}{1.67}$ |
| $= 0.590 \text{ kip-ft} > 0.325 \text{ kip-ft}$ **o.k.** | $= 0.392 \text{ kip-ft} > 0.219 \text{ kip-ft}$ **o.k.** |

---

# F-65

## EXAMPLE F.14 PLATE GIRDER FLEXURAL MEMBER

### Given:

Verify the built-up plate girder for the span and loads shown in Figure F.14-1 with a cross section as shown in Figure F.14-2. The beam has a concentrated dead and live load at midspan and a uniformly distributed self weight. The plate girder is simply supported and is laterally braced at quarter and end points. The deflection of the girder is limited to 1 in. The plate girder is ASTM A572/A572M Grade 50 material. The flange-to-web welds will be designed for both continuous and intermittent fillet welds using 70-ksi electrodes.

```
    Bearing stiffener ─┐           $P_D = 240 \text{ kips}$
    Lateral brace, typ. ─┼           $P_L = 160 \text{ kips}$
                         ↓                     $w_D = 0.296 \text{ kip/ft}$
        ●                |                ●                    ●
        |                |                |                    |
       ╞╡              ╞╡╞╡              ╞╡╞╡                ╞╡╞╡
        |←───── 12'-6" ─────→|←───── 12'-6" ─────→|←───── 12'-6" ─────→|←───── 12'-6" ─────→|
        |←──────────────────── L = 50'-0" ────────────────────→|

        Note: Figure is not drawn to scale.
```

*Fig. F.14-1. Beam loading and bracing diagram.*

```
        $b_f = 14"$                    $t_f = 2"$
        ┌────────────┐
        │            │
        │            │                         ││
        │            │                         ││  $t_f = 2"$
        │            │                         ││
        │  $t_w = \frac{1}{2}"$  │           $h = 62"$
        │            │                         ││
        │            │                    $d = 66"$
        │            │                         ││
        │            │                         ││
        └────────────┘                         ││
        $b_f = 14"$                    $t_f = 2"$
```

*Fig. F.14-2. Plate girder geometry.*

### Solution:

From AISC *Manual* Table 2-5, the material properties are as follows:

ASTM A572/A572M Grade 50
$F_y = 50 \text{ ksi}$
$F_u = 65 \text{ ksi}$

---

# F-66

From ASCE/SEI 7, Chapter 2, the required shear and flexural strengths are:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(240 \text{ kips}) + 1.6(160 \text{ kips})$ | $P_a = 240 \text{ kips} + 160 \text{ kips}$ |
| $= 544 \text{ kips}$ | $= 400 \text{ kips}$ |
| $w_u = 1.2(0.296 \text{ kip/ft})$ | $w_a = 0.296 \text{ kip/ft}$ |
| $= 0.355 \text{ kip/ft}$ | |
| From AISC *Manual* Table 3-22, Cases 1 and 7: | From AISC *Manual* Table 3-22, Cases 1 and 7: |
| $V_u = \dfrac{P_u}{2} + \dfrac{w_u L}{2}$ | $V_a = \dfrac{P_a}{2} + \dfrac{w_a L}{2}$ |
| $= \dfrac{544 \text{ kips}}{2} + \dfrac{(0.355 \text{ kip/ft})(50 \text{ ft})}{2}$ | $= \dfrac{400 \text{ kips}}{2} + \dfrac{(0.296 \text{ kip/ft})(50 \text{ ft})}{2}$ |
| $= 281 \text{ kips}$ | $= 207 \text{ kips}$ |
| $M_u = \dfrac{P_u L}{4} + \dfrac{w_u L^2}{8}$ | $M_a = \dfrac{P_a L}{4} + \dfrac{w_a L^2}{8}$ |
| $= \dfrac{(544 \text{ kips})(50 \text{ ft})}{4} + \dfrac{(0.355 \text{ kip/ft})(50 \text{ ft})^2}{8}$ | $= \dfrac{(400 \text{ kips})(50 \text{ ft})}{4} + \dfrac{(0.296 \text{ kip/ft})(50 \text{ ft})^2}{8}$ |
| $= 6,910 \text{ kip-ft}$ | $= 5,090 \text{ kip-ft}$ |

**Proportioning Limits**

The proportioning limits from AISC *Specification* Section F13.2 are evaluated as follows, where $a$ is the clear distance between transverse stiffeners.

$$\frac{a}{h} = \frac{(25 \text{ ft})(12 \text{ in./ft}) - \frac{1}{2} \text{ in.}}{62 \text{ in.}}$$
$$= 4.83$$

Because $a/h > 1.5$, use AISC *Specification* Equation F13-4.

$$\left(\frac{h}{t_w}\right)_{max} = \frac{0.40E}{F_y}$$
$$\text{(Spec. Eq. F13-4)}$$

$$= \frac{0.40(29,000 \text{ ksi})}{50 \text{ ksi}}$$

$$= 232$$

$$\frac{h}{t_w} = \frac{62 \text{ in.}}{\frac{1}{2} \text{ in.}}$$
$$= 124 < 232$$ **o.k.**

From AISC *Specification* Section F13.2, the following limit applies to all built-up I-shaped members:

---

# F-67

$$\frac{h_c t_w}{b_f t_f} = \frac{(62 \text{ in.})(\frac{1}{2} \text{ in.})}{(14 \text{ in.})(2 \text{ in.})} \leq 10$$

$$= 1.11 < 10$$ **o.k.**

**Section Properties**

$$I_x = \sum\frac{bh^3}{12} + \sum Ad^2$$

$$= \frac{(\frac{1}{2} \text{ in.})(62 \text{ in.})^3}{12} + 2\left[\frac{(14 \text{ in.})(2 \text{ in.})^3}{12}\right] + 2\left[(2 \text{ in.})(14 \text{ in.})(32.0 \text{ in.})^2\right]$$

$$= 67,300 \text{ in.}^4$$

$$S_M = S_{xc}$$

$$= \frac{I_x}{(d/2)}$$

$$= \frac{67,300 \text{ in.}^4}{(66 \text{ in.}/2)}$$

$$= 2,040 \text{ in.}^3$$

$$Z_x = \sum A\overline{y}$$

$$= (2)(\frac{1}{2}\text{in.})(31.0 \text{ in.})(31.0 \text{ in.}/2) + (2)(2 \text{ in.})(14 \text{ in.})(32.0 \text{ in.})$$

$$= 2,270 \text{ in.}^3$$

$$J = \sum\frac{bt^3}{3}$$

$$= 2\left[\frac{(14 \text{ in.})(2 \text{ in.})^3}{3}\right] + \frac{(62 \text{ in.})(\frac{1}{2} \text{ in.})^3}{3}$$

$$= 77.3 \text{ in.}^4$$

$$h_o = h + t_f$$
$$= 62 \text{ in.} + 2 \text{ in.}$$
$$= 64.0 \text{ in.}$$

**Deflection**

From AISC *Manual* Table 3-22, Cases 1 and 7, the maximum deflection is:

$$\Delta = \frac{(P_D + P_L)L^3}{48EI} + \frac{5w_DL^4}{384EI}$$

$$= \frac{(240 \text{ kips} + 160 \text{ kips})(50 \text{ ft})^3(12 \text{ in./ft})^3}{48(29,000 \text{ ksi})(67,300 \text{ in.}^4)} + \frac{5(0.296 \text{ kip/ft})(50 \text{ ft})^4(12 \text{ in./ft})^3}{384(29,000 \text{ ksi})(67,300 \text{ in.}^4)}$$

$$= 0.944 \text{ in.} < 1.00 \text{ in.}$$ **o.k.**

---

# F-68

**Web Slenderness**

$$\lambda = \frac{h}{t_w}$$

$$= \frac{62 \text{ in.}}{\frac{1}{2} \text{ in.}}$$

$$= 124$$

From AISC *Specification* Table B4.1b, Case 15, the limiting width-to-thickness ratios for the web are:

$$\lambda_{pw} = 3.76\sqrt{\frac{E}{F_y}}$$

$$= 3.76\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 90.6$$

$$\lambda_{rw} = 5.70\sqrt{\frac{E}{F_y}}$$

$$= 5.70\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 137$$

Because $\lambda_{pw} < \lambda < \lambda_{rw}$, the web is noncompact and AISC *Specification* Section F4 applies.

**Flange Slenderness**

$$\lambda = \frac{b_f}{2t_f}$$

$$= \frac{14 \text{ in.}}{2(2 \text{ in.})}$$

$$= 3.50$$

From AISC *Specification* Table B4.1b, Case 11, the limiting width-to-thickness ratio for a compact flange is:

$$\lambda_{pf} = 0.38\sqrt{\frac{E}{F_y}}$$

$$= 0.38\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 9.15$$

Because $\lambda < \lambda_{pf}$, the flanges are compact.

**Nominal Flexural Strength**

**Compression Flange Yielding**

The web plastification factor is determined using AISC *Specification* Section F4.2(c)(6).

---

# F-69

$$I_{yc} = \frac{t_f b_f^3}{12}$$

$$= \frac{(2 \text{ in.})(14 \text{ in.})^3}{12}$$

$$= 457 \text{ in.}^4$$

$$I_y = 2\left(\frac{t_f b_f^3}{12}\right) + \frac{ht_w^3}{12}$$

$$= 2\left[\frac{(2 \text{ in.})(14 \text{ in.})^3}{12}\right] + \frac{(62 \text{ in.})(\frac{1}{2} \text{ in.})^3}{12}$$

$$= 915 \text{ in.}^4$$

$$\frac{I_{yc}}{I_y} = \frac{457 \text{ in.}^4}{915 \text{ in.}^4}$$
$$= 0.499$$

Because $I_{yc}/I_y > 0.23$, AISC *Specification* Section F4.2(6)(i) applies.

$$M_p = F_y Z_x \leq 1.6F_y S_x$$

$$= (50 \text{ ksi})(2,270 \text{ in.}^3)(1 \text{ ft}/12 \text{ in.}) \leq 1.6(50 \text{ ksi})(2,040 \text{ in.}^3)(1 \text{ ft}/12 \text{ in.})$$

$$= 9,460 \text{ kip-ft} < 13,600 \text{ kip-ft}$$
$$= 9,460 \text{ kip-ft}$$

$$M_{yc} = F_y S_{xc}$$
$$\text{(Spec. Eq. F4-4)}$$

$$= (50 \text{ ksi})(2,040 \text{ kip-in.})(1 \text{ ft}/12 \text{ in.})$$

$$= 8,500 \text{ kip-ft}$$

$$h_c = h$$
$$= 62 \text{ in.}$$

$$\lambda = \frac{h_c}{t_w}$$

$$= \frac{62 \text{ in.}}{\frac{1}{2}\text{in.}}$$

$$= 124 > \lambda_{pw} = 90.6$$ ; therefore use AISC *Specification* Equation F4-9b

$$R_{pc} = \frac{M_p}{M_{yc}} - \left(\frac{M_p}{M_{yc}} - 1\right)\left(\frac{\lambda - \lambda_{pw}}{\lambda_{rw} - \lambda_{pw}}\right) \leq \frac{M_p}{M_{yc}}$$
$$\text{(Spec. Eq. F4-9b)}$$

$$= \frac{9,460 \text{ kip-ft}}{8,500 \text{ kip-ft}} - \left(\frac{9,460 \text{ kip-ft}}{8,500 \text{ kip-ft}} - 1\right)\left(\frac{124 - 90.6}{137 - 90.6}\right) \leq \frac{9,460 \text{ kip-ft}}{8,500 \text{ kip-ft}}$$

$$= 1.03 < 1.11$$
$$= 1.03$$

---

# F-70

The nominal flexural strength is calculated as:

$$M_n = R_{pc}M_{yc}$$
$$\text{(Spec. Eq. F4-1)}$$

$$= (1.03)(8,500 \text{ kip-ft})$$

$$= 8,760 \text{ kip-ft}$$

From AISC *Specification* Section F1.1, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(8,760 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{8,760 \text{ kip-ft}}{1.67}$ |
| $= 7,880 \text{ kip-ft} > 6,910 \text{ kip-ft}$ **o.k.** | $= 5,250 \text{ kip-ft} > 5,090 \text{ kip-ft}$ **o.k.** |

**Lateral-Torsional Buckling**

The middle-unbraced lengths control by inspection. For bracing at quarter points,

$$L_b = (12.5 \text{ ft})(12 \text{ in./ft})$$
$$= 150 \text{ in.}$$

$$a_w = \frac{h_c t_w}{b_{fc}t_{fc}}$$
$$\text{(Spec. Eq. F4-12)}$$

$$= \frac{(62 \text{ in.})(\frac{1}{2} \text{ in.})}{(14 \text{ in.})(2 \text{ in.})}$$

$$= 1.11$$

$$r_t = \frac{b_{fc}}{\sqrt{12\left(1 + \frac{1}{6}a_w\right)}}$$
$$\text{(Spec. Eq. F4-11)}$$

$$= \frac{14.0 \text{ in.}}{\sqrt{12\left[1 + \left(\frac{1.11}{6}\right)\right]}}$$

$$= 3.71 \text{ in.}$$

From AISC *Specification* Equation F4-7:

$$L_p = 1.1r_t\sqrt{\frac{E}{F_y}}$$
$$\text{(Spec. Eq. F4-7)}$$

$$= 1.1(3.71 \text{ in.})\sqrt{\frac{29,000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 98.3 < 150 \text{ in.}$$ ; therefore, lateral-torsional buckling applies

From AISC *Specification* Section F4.2(3):

---

# F-71

$$\frac{S_{xt}}{S_{xc}} = \frac{2,040 \text{ in.}^3}{2,040 \text{ in.}^3}$$
$$= 1.00 > 0.7$$ ; therefore, AISC *Specification* Equation F4-6a applies

$$F_L = 0.7F_y$$
$$\text{(Spec. Eq. F4-6a)}$$

$$= 0.7(50 \text{ ksi})$$

$$= 35.0 \text{ ksi}$$

The limiting unbraced length, $L_r$, is calculated using AISC *Specification* Equation F4-8:

$$L_r = 1.95r_t\frac{E}{F_L}\sqrt{\frac{J}{S_{xc}h_o} + \sqrt{\left(\frac{J}{S_{xc}h_o}\right)^2 + 6.76\left(\frac{F_L}{E}\right)^2}}$$
$$\text{(Spec. Eq. F4-8)}$$

$$= 1.95(3.71 \text{ in.})\left(\frac{29,000 \text{ ksi}}{35.0 \text{ ksi}}\right)\sqrt{\frac{77.3 \text{ in.}^4}{(2,040 \text{ in.}^3)(64.0 \text{ in.})} + \sqrt{\left[\frac{77.3 \text{ in.}^4}{(2,040 \text{ in.}^3)(64.0 \text{ in.})}\right]^2 + 6.76\left(\frac{35.0 \text{ ksi}}{29,000 \text{ ksi}}\right)^2}}$$

$$= 369 \text{ in.}$$

Because $L_p < L_b \leq L_r$, AISC *Specification* Equation F4-2 applies.

The lateral-torsional buckling modification factor is determined by solving for the moment in the beam using statics. Note: The following solution uses LRFD load combinations. Using ASD load combinations will give approximately the same solution for $C_b$.

$M_{max} = 6,910 \text{ kip-ft}$
$M_A = 4,350 \text{ kip-ft}$
$M_B = 5,210 \text{ kip-ft}$
$M_C = 6,060 \text{ kip-ft}$

$$C_b = \frac{12.5M_{max}}{2.5M_{max} + 3M_A + 4M_B + 3M_C}$$
$$\text{(Spec. Eq. F1-1)}$$

$$= \frac{12.5(6,910 \text{ kip-ft})}{2.5(6,910 \text{ kip-ft}) + 3(4,350 \text{ kip-ft}) + 4(5,210 \text{ kip-ft}) + 3(6,060 \text{ kip-ft})}$$

$$= 1.25$$

The nominal flexural strength is calculated as:

$$M_n = C_b\left[R_{pc}M_{yc} - (R_{pc}M_{yc} - F_L S_{xc})\left(\frac{L_b - L_p}{L_r - L_p}\right)\right] \leq R_{pc}M_{yc}$$
$$\text{(Spec. Eq. F4-2)}$$

$$= 1.25\left\{8,760 \text{ kip-ft} - \left[8,760 \text{ kip-ft} - (35.0 \text{ ksi})(2,040 \text{ in.}^3)(1 \text{ ft}/12 \text{ in.})\right]\left(\frac{150 \text{ in.} - 98.3 \text{ in.}}{369 \text{ in.} - 98.3 \text{ in.}}\right)\right\} > 8,760 \text{ kip-ft}$$

$$= 10,300 \text{ kip-ft} > 8,760 \text{ kip-ft}$$
$$= 8,760 \text{ kip-ft}$$

From AISC *Specification* Section F1.1, the available flexural strength is:

---

# F-72

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(8,760 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{8,760 \text{ kip-ft}}{1.67}$ |
| $= 7,880 \text{ kip-ft} > 6,910 \text{ kip-ft}$ **o.k.** | $= 5,250 \text{ kip-ft} > 5,090 \text{ kip-ft}$ **o.k.** |

**Compression Flange Local Buckling**

From AISC *Specification* Section F4.3(a), this limit state does not apply because the flanges are compact.

**Tension Flange Yielding**

From AISC *Specification* Section F4.4(a), because $S_{xt} = S_{xc}$, this limit state does not apply.

**Nominal Shear Strength**

Determine the nominal shear strength without tension field action, using AISC *Specification* Section G2.1. For built-up I-shaped members, determine $C_{v1}$ and $k_v$ from AISC *Specification* Section G2.1(b).

$$\frac{a}{h} = \frac{(25.0 \text{ ft})(12 \text{ in./ft}) - \frac{1}{2} \text{ in.}}{62 \text{ in.}}$$
$$= 4.83 > 3.0$$

From AISC *Specification* Section G2.1(b)(2)(ii):

$$k_v = 5.34$$

$$1.10\sqrt{\frac{k_v E}{F_y}} = 1.10\sqrt{\frac{5.34(29,000 \text{ ksi})}{50 \text{ ksi}}}$$

$$= 61.2$$

Because $h/t_w = 124 > 61.2$, AISC *Specification* Equation G2-4 applies.

$$C_{v1} = \frac{1.10\sqrt{k_v E/F_y}}{h/t_w}$$
$$\text{(Spec. Eq. G2-4)}$$

$$= \frac{61.2}{124}$$

$$= 0.494$$

The nominal shear strength is calculated as follows:

$$V_n = 0.6F_y A_w C_{v1}$$
$$\text{(Spec. Eq. G2-1)}$$

$$= 0.6(50 \text{ ksi})(66 \text{ in.})(\frac{1}{2} \text{ in.})(0.494)$$

$$= 489 \text{ kips}$$

From AISC *Specification* Section G.1, the available shear strength is:

---

# F-73

| LRFD | ASD |
|------|-----|
| $\phi_v = 0.90$ | $\Omega_v = 1.67$ |
| $\phi_v V_n = 0.90(489 \text{ kips})$ | $\dfrac{V_n}{\Omega_v} = \dfrac{489 \text{ kips}}{1.67}$ |
| $= 440 \text{ kips} > 281 \text{ kips}$ **o.k.** | $= 293 \text{ kips} > 207 \text{ kips}$ **o.k.** |

**Flange-to-Web Fillet Weld—Continuous Weld**

Calculate the required shear flow using $VQ/I_x$ because the stress distribution is linearly elastic away from midspan.

$$Q = A\overline{y}$$

$$= b_f t_f\left(\frac{h}{2} + \frac{t_f}{2}\right)$$

$$= (14 \text{ in.})(2 \text{ in.})\left(\frac{62 \text{ in.}}{2} + \frac{2 \text{ in.}}{2}\right)$$

$$= 896 \text{ in.}^3$$

| LRFD | ASD |
|------|-----|
| $R_u = \dfrac{V_u Q}{I_x}$ | $R_a = \dfrac{V_a Q}{I_x}$ |
| $= \dfrac{(281 \text{ kips})(896 \text{ in.}^3)}{67,300 \text{ in.}^4}$ | $= \dfrac{(207 \text{ kips})(896 \text{ in.}^3)}{67,300 \text{ in.}^4}$ |
| $= 3.74 \text{ kip/in.}$ | $= 2.76 \text{ kip/in.}$ |

From AISC *Specification* Table J2.4, the minimum fillet weld size that can be used on the ½-in.-thick web is:

$$w_{min} = \frac{3}{16} \text{ in.}$$

From AISC *Manual* Part 8, the required fillet weld size is:

| LRFD | ASD |
|------|-----|
| $D_{req} = \dfrac{R_u}{1.392(2 \text{ sides})}$ (from *Manual* Eq. 8-2a) | $D_{req} = \dfrac{R_a}{0.928(2 \text{ sides})}$ (from *Manual* Eq. 8-2b) |
| $= \dfrac{3.74 \text{ kip/in.}}{1.392(2 \text{ sides})}$ | $= \dfrac{2.76 \text{ kip/in.}}{0.928(2 \text{ sides})}$ |
| $= 1.34 \text{ sixteenths} < 3 \text{ sixteenths}$ | $= 1.49 \text{ sixteenths} < 3 \text{ sixteenths}$ |
| Use $w = \frac{3}{16} \text{ in.}$ | Use $w = \frac{3}{16} \text{ in.}$ |

From AISC *Specification* Equation J2-2 and Section J4.2, the available shear rupture strength of the web in kip/in. is:

---

# F-74

| LRFD | ASD |
|------|-----|
| $\phi = 0.75$ | $\Omega = 2.00$ |
| $\phi R_n = \phi F_{nBM}A_{BM}$ | $\dfrac{R_n}{\Omega} = \dfrac{F_{nBM}A_{BM}}{\Omega}$ |
| $= \phi 0.60F_u t_w$ | $= \dfrac{0.60F_u t_w}{\Omega}$ |
| $= 0.75(0.60)(65 \text{ ksi})(\frac{1}{2} \text{ in.})$ | $= \dfrac{0.60(65 \text{ ksi})(\frac{1}{2} \text{ in.})}{2.00}$ |
| $= 14.6 \text{ kip/in.} > 3.74 \text{ kip/in.}$ **o.k.** | $= 9.75 \text{ kip/in.} > 2.76 \text{ kip/in.}$ **o.k.** |

**Flange-to-Web Fillet Weld—Intermittent Weld**

The two-sided intermittent weld is designed using the minimum fillet weld size determined previously, $w_{min} = \frac{3}{16} \text{ in.}$, and spaced at 12 in. center-to-center.

| LRFD | ASD |
|------|-----|
| $R_n = \phi R_n$ (from *Manual* Eq. 8-2a) | $R_n = \dfrac{R_n}{\Omega}$ (from *Manual* Eq. 8-2b) |
| $= 1.392D(2 \text{ sides})\left(\dfrac{l_{req}}{s}\right)$ | $= 0.928D(2 \text{ sides})\left(\dfrac{l_{req}}{s}\right)$ |
| Solving for $l_{req}$, | Solving for $l_{req}$, |
| $l_{req} = \dfrac{R_u s}{1.392D(2 \text{ sides})}$ | $l_{req} = \dfrac{R_a s}{0.928D(2 \text{ sides})}$ |
| $= \dfrac{(3.74 \text{ kip/in.})(12 \text{ in.})}{1.392(3 \text{ sixteenths})(2 \text{ sides})}$ | $= \dfrac{(2.76 \text{ kip/in.})(12 \text{ in.})}{0.928(3 \text{ sixteenths})(2 \text{ sides})}$ |
| $= 5.37 \text{ in.}$ | $= 5.95 \text{ in.}$ |
| Use $l = 6 \text{ in.}$ at 12 in. o.c. | Use $l = 6 \text{ in.}$ at 12 in. o.c. |

The limitations for a intermittent fillet weld are checked using AISC *Specification* Section J2.2b(e):

$$l \geq 4D$$
$$6 \text{ in.} \geq 4(\frac{3}{16}\text{in.})$$
$$6 \text{ in.} > 0.75 \text{ in.}$$ **o.k.**

$$l \geq 1\frac{1}{2} \text{ in.}$$
$$6 \text{ in.} > 1\frac{1}{2} \text{ in.}$$ **o.k.**

---
