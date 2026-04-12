# Chapter I: Composite Members

**AISC Specification v16.0 - Design Examples**
**Original PDF Pages**: 297-432 (136 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Design of Composite Members

**Examples Included**: ['I.1~I.13: Composite design examples']

---

## Table of Contents

- [EXAMPLE I.1 COMPOSITE BEAM DESIGN](#example-i1-composite-beam-design)
- [EXAMPLE I.2 COMPOSITE GIRDER DESIGN](#example-i2-composite-girder-design)
- [EXAMPLE I.12 STEEL ANCHORS IN COMPOSITE COMPONENTS](#example-i12-steel-anchors-in-composite-components)
- [EXAMPLE I.13 COMPOSITE COLLECTOR BEAM DESIGN](#example-i13-composite-collector-beam-design)

---

# I-1

# Chapter I
# Design of Composite Members

## I1. GENERAL PROVISIONS

Design, detailing, and material properties related to the concrete and steel reinforcing portions of composite members are governed by ACI 318 (ACI, 2019) as modified with composite-specific provisions by the AISC *Specification*.

The available strength of composite sections may be calculated by one of four methods: the plastic stress distribution method, the strain-compatibility method, the elastic method, or the effective stress-strain method. The composite design tables in Volume 2 of this document are based on the plastic stress distribution method.

Filled composite sections are classified for local buckling according to the slenderness of the compression steel elements as illustrated in AISC *Specification* Tables I1.1a and I1.1b, and Examples I.3, I.4, I.6, and I.7. Local buckling effects do not need to be considered for encased composite members.

Terminology used within the Examples for filled composite section geometry is illustrated in Figure I-1.

## I2. AXIAL FORCE

The available compressive strength of a composite member is based on a summation of the strengths of all the components of the column, with reductions applied for member slenderness and local buckling effects where applicable.

For tension members, the concrete tensile strength is ignored and only the strength of the steel member and properly connected reinforcing is permitted to be used in the calculation of available tensile strength.

The available compressive strength tables for filled composite sections are given in Volume 2 of this document and reflect the requirements given in AISC *Specification* Sections I2.1 and I2.2. The design of filled composite compression and tension members is presented in Examples I.4 and I.5, respectively.

The design of encased composite compression and tension members is presented in Examples I.9 and I.10, respectively. There are no tables in the AISC *Manual* for the design of these members.

Note that the AISC *Specification* stipulates that the available compressive strength need not be less than that specified for the bare steel member.

## I3. FLEXURE

The design of typical composite beams with steel anchors is illustrated in Examples I.1 and I.2. AISC *Manual* Table 3-18 provides available flexural strengths for composite W-shape beams, Table 3-19 provides lower-bound moments of inertia for plastic composite sections, and Table 3-20 provides shear strengths of steel headed stud anchors utilized for composite action in composite beams.

The design of filled composite members for flexure is illustrated in Examples I.6 and I.7, and the design of encased composite members for flexure is illustrated in Example I.11.

## I4. SHEAR

For composite beams with formed steel deck, the available shear strength is based upon the properties of the steel section alone in accordance with AISC *Specification* Chapter G as illustrated in Examples I.1 and I.2.

---

# I-2

For composite members, the shear strength includes the contribution of the steel portion plus the concrete infill. The calculation of shear strength for filled composite members is illustrated in Examples I.6 and I.7.

For encased members, either the shear strength of the steel section alone, the steel section plus the reinforced concrete shear are permitted to be used in the calculation of available shear strength.

The calculation of shear strength for encased composite members is illustrated in Example I.11.

Design for combined shear force and flexure may be accomplished using either the strain compatibility method or the plastic stress distribution method. These procedures are referenced in AISC *Specification* Chapter I for both composite and filled composite members. AISC *Specification* Section I1.4 addresses flexure and axial force, and AISC *Specification* Section I2.1c addresses flexure and axial force transfer mechanisms—how the force is transferred between the two materials in a column. The latter specification has several requirements to ensure that the concrete and steel portions of the section act in various the reinforced concrete; and force transfer mechanisms—how the force is transferred between the two materials in a column. The Commentary, and each of these procedures is demonstrated for filled composite members in Example I.9 and encased composite members in Example I.11.

To assist in developing the interaction curves illustrated within the design examples, a series of equations is provided in AISC *Specification* Section I2.1, along with a diagram illustrating the various stresses on the interaction diagram in AISC *Specification* Commentary Figure C-I2.2a. These equations do not restrict the design procedure to filled or encased composite members, but are only one possible set of choices; alternative methods are identified in the Commentary. When design values derive from these prescribed, the appropriate intersection equations can be derived from these preset equations.

## I5. LOAD TRANSFER

The AISC *Specification* has several requirements to ensure that the concrete and steel portions of the section act as a single unit. Such requirements include the provision of horizontal shear connection, tie bars for column-to-column moment connections (Section I8.2a), and other details that address the issue of load transfer between steel and concrete. These requirements are demonstrated for filled composite members in Example I.9 and encased composite members in Example I.11.

## I6. COMPOSITE DIAPHRAGMS AND COLLECTOR BEAMS

The Commentary provides guidance on design methodologies for both composite diaphragms and composite collector beams.

## I7. STEEL ANCHORS

AISC *Specification* Section I8 addresses the strength of steel anchors in composite beams and is composite-specific provisions. It is listed in AISC *Specification* Section I8.3(a). These provisions do not apply to typical composite columns and must also consider the shear strength along the steel flange/base metal interface as demonstrated in Example I.1 and more fully explained in AISC *Specification* User Note in Section I8.2a. The interaction due to these provisions is demonstrated for filled composite members in Example I.10. The User Note provided at the beginning of AISC *Specification* Section I8.1 These provisions do not apply to typical composite beams and must either comply with ACI 318 provisions (ACI, 2019), or the provisions of load strength of headed studs placed within the load introduction length of composite columns is demonstrated in Examples I.9 and I.10.

---

# I-3

![Diagram showing terminology for filled composite sections. Two cross-sections are shown - a rectangular HSS and a round HSS, with various dimensional labels and definitions]

**Definitions:**

$B$ = Overall width of section parallel to the axis of bending, in.

$H$ = Overall height of section perpendicular to the axis of bending, in.

$b$ = Width of stiffened compression element, in.
    = $B - 3t$ per AISC *Specification* Section B4.1b(d)

$b_i$ = Inside width of section, in.
    = $B - 2t$

$d$ = Outside diameter of round HSS, in.

$h$ = Width of stiffened compression element, in.
    = $H - 3t$ per AISC *Specification* Section B4.1b(d)

$h_i$ = Inside diameter of round HSS, in.
    = $d - 2t$

$h_i$ = Inside height of section, in.
    = $H - 2t$

$r_i$ = 0.5$t$ for $b/t$ and $h/t$, in.

$r_i$ = 1.0$t$ for all area, section modulus, and moment of inertia calculations, in.

$t$ = 0.93$t_{nom}$, in. ($t = t_{nom}$ for ASTM A1065/A1065M or A1085/A1085M material)

*Fig. I-1. Terminology used for filled members.*

---

# I-4

## EXAMPLE I.1 COMPOSITE BEAM DESIGN

### Given:

A typical bay of a composite floor system is illustrated in Figure I.1-1. Select an appropriate ASTM A992/A992M W-shaped beam and determine the required number of ¾-in.-diameter steel headed stud anchors. The beam will not be shored during construction.

![Plan view and section showing a composite floor system with dimensions 3 @ 10'-0" = 30'-0" vertically and 45'-0" horizontally. Section A-A shows a 7½" total depth normal weight slab on 18 gage composite deck with 4½" and 3" dimensions marked]

*Fig. I.1-1. Composite bay and beam section.*

To achieve a two-hour fire rating without the application of spray applied fire protection material to the composite deck, 4½ in. of normal weight (145 lb/ft³) concrete will be placed above the top of the deck. The concrete has a specified compressive strength, $f_c' = 4 \text{ ksi}$.

Applied loads are given in the following:

Dead Loads:
Pre-composite:
Slab = 75 lb/ft² (in accordance with metal deck manufacturer's data)
Self-weight = 5 lb/ft² (assumed uniform load to account for beam weight)

Composite (applied after composite action has been achieved):
Miscellaneous = 10 lb/ft² (HVAC, ceiling, floor covering, etc.)

Live Loads:
Pre-composite:
Construction = 25 lb/ft² (temporary loads during concrete placement)

---

# I-5

Composite (applied after composite action has been achieved):
Non-reducible = 100 lb/ft² (assembly occupancy)

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

**Applied Loads**

For slabs that are to be placed at a constant elevation, AISC Design Guide 3 (West et al., 2003) recommends an additional 10% of the nominal slab weight be applied to account for concrete ponding due to deflections resulting from the wet weight of the concrete during placement. For the slab under consideration, this would result in an additional load of 8 lb/ft²; however, for this design the slab will be placed at a constant thickness, and thus, no additional weight for concrete ponding is required.

For pre-composite construction live loading, 25 lb/ft² will be applied in accordance with recommendations from *Design Loads on Structures During Construction*, ASCE/SEI 37 (ASCE, 2014), for a light duty operational class that includes concrete transport and placement by hose and finishing with hand tools.

**Composite Deck and Anchor Requirements**

Check composite deck and anchor requirements stipulated in AISC *Specification* Sections I1.3, I3.2c, and I8.

1. Concrete Strength: 3 ksi ≤ $f_c' \leq 10 \text{ ksi}$ (for normal weight concrete) (*Spec.* Section I1.3)
   $f_c' = 4 \text{ ksi}$ **o.k.**

2. Rib height: $h_r \leq 3 \text{ in.}$ (*Spec.* Section I3.2c)
   $h_r = 3 \text{ in.}$ **o.k.**

3. Average rib width: $w_r \geq 2 \text{ in.}$ (*Spec.* Section I3.2c)
   $w_r = 6 \text{ in.}$ (from deck manufacturer's literature) **o.k.**

4. Use steel headed stud anchors ¾ in. or less in diameter. (*Spec.* Section I8.1)
   Use ¾ in. diameter steel headed stud anchors per problem statement. **o.k.**

5. Steel headed stud anchor diameter: $d_{sa} \leq 2.5t_f$ (*Spec.* Section I8.1)

   In accordance with AISC *Specification* Section I8.1, this limit only applies if steel headed stud anchors are not welded to the flange directly over the web. The ¾-in.-diameter anchors will be placed in pairs transverse to the web in some locations, thus this limit must be satisfied. Select a beam size with a minimum flange thickness of 0.300 in., as determined in the following:

   $$t_f \geq \frac{d_{sa}}{2.5}$$

   $$\geq \frac{\frac{3}{4} \text{ in.}}{2.5}$$

   $$\geq 0.300 \text{ in.}$$

6. In accordance with AISC *Specification* I3.2c, steel headed stud anchors, after installation, shall extend not less than 1½ in. above the top of the steel deck. A minimum anchor length of 4½ in. is required to meet this

---

# I-6

requirement for 3 in. deep deck. From steel headed stud anchor manufacturer's data, a standard stock length of 4⅝ in. is selected. Using a ¼ in. length reduction to account for burn off during anchor installation through the deck yields a final installed length of 4½ in. **o.k.**

7. Minimum length of stud anchors = $4d_{sa}$ (*Spec.* Section I8.2)
   4½ in. > 4(¾ in.) = 3.00 in. **o.k.**

8. In accordance with AISC *Specification* Section I3.2c, there shall be at least ½ in. of specified concrete cover above the top of the headed stud anchors.

   As discussed in AISC *Specification* Commentary to Section I3.2c, it is advisable to provide greater than ½ in. minimum cover to assure anchors are not exposed in the final condition, particularly for intentionally cambered beams.

   7½ in. - 4½ in. = 3.00 in. > ½ in. **o.k.**

9. In accordance with AISC *Specification* Section I3.2c, slab thickness above steel deck shall not be less than 2 in.

   4½ in. > 2 in. **o.k.**

**Design for Pre-Composite Condition**

**Construction (Pre-Composite) Loads**

The beam is uniformly loaded by its tributary width as follows:

$$w_D = \left[(10 \text{ ft})(75 \text{ lb/ft}^2 + 5 \text{ lb/ft}^2)\right](1 \text{ kip}/1{,}000 \text{ lb})$$

$$= 0.800 \text{ kip/ft}$$

$$w_L = \left[(10 \text{ ft})(25 \text{ lb/ft}^2)\right](1 \text{ kip}/1{,}000 \text{ lb})$$

$$= 0.250 \text{ kip/ft}$$

**Construction (Pre-Composite) Flexural Strength**

From ASCE/SEI 7, Chapter 2, the required flexural strength is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.800 \text{ kip/ft}) + 1.6(0.250 \text{ kip/ft})$ | $w_a = 0.800 \text{ kip/ft} + 0.250 \text{ kip/ft}$ |
| $= 1.36 \text{ kip/ft}$ | $= 1.05 \text{ kip/ft}$ |
| $M_u = \dfrac{w_u L^2}{8}$ | $M_a = \dfrac{w_a L^2}{8}$ |
| $= \dfrac{(1.36 \text{ kip/ft})(45 \text{ ft})^2}{8}$ | $= \dfrac{(1.05 \text{ kip/ft})(45 \text{ ft})^2}{8}$ |
| $= 344 \text{ kip-ft}$ | $= 266 \text{ kip-ft}$ |

---

# I-7

**Beam Selection**

Assume that attachment of the deck perpendicular to the beam provides adequate bracing to the compression flange during construction, thus the beam can develop its full plastic moment capacity. The required plastic section modulus, $Z_x$, is determined as follows, from AISC *Specification* Equation F2-1:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $Z_{x,min} = \dfrac{M_u}{\phi_b F_y}$ | $Z_{x,min} = \dfrac{\Omega_b M_a}{F_y}$ |
| $= \dfrac{(344 \text{ kip-ft})(12 \text{ in./ft})}{0.90(50 \text{ ksi})}$ | $= \dfrac{1.67(266 \text{ kip-ft})(12 \text{ in./ft})}{50 \text{ ksi}}$ |
| $= 91.7 \text{ in.}^3$ | $= 107 \text{ in.}^3$ |

From AISC *Manual* Table 3-2, select a W21×50 with a $Z_x$ value of 110 in.³

Note that for the member size chosen, the self-weight on a pounds per square foot basis is 50 plf /10 ft = 5.00 psf ; thus the initial self-weight assumption is adequate.

From AISC *Manual* Table 1-1, the geometric properties are as follows:

W21×50
$A = 14.7 \text{ in.}^2$
$t_f = 0.535 \text{ in.}$
$I_x = 984 \text{ in.}^4$
$d = 20.8 \text{ in.}$
$\dfrac{h}{t_w} = 49.4$

**Pre-Composite Deflections**

AISC Design Guide 3 recommends deflections due to concrete plus self-weight not exceed the minimum of $L/360$ or 1.0 in.

From AISC *Manual* Table 3-22, Case 1:

$$\Delta_{nc} = \frac{5w_D L^4}{384EI}$$

Substituting for the moment of inertia of the non-composite section, $I = 984 \text{ in.}^4$, yields a dead load deflection of:

$$\Delta_{nc} = \frac{5(0.800 \text{ kip/ft})(1 \text{ ft}/12 \text{ in.})\left[(45 \text{ ft})(12 \text{ in./ft})\right]^4}{384(29{,}000 \text{ ksi})(984 \text{ in.}^4)}$$

$$= 2.59 \text{ in.}$$

$$= L/208 > L/360$$ **n.g.**

---

# I-8

Pre-composite deflections exceed the recommended limit. One possible solution is to increase the member size. A second solution is to induce camber into the member. For this example, the second solution is selected, and the beam will be cambered to reduce the net pre-composite deflections.

Reducing the estimated simple span deflections to 80% of the calculated value to reflect the partial restraint of the end connections as recommended in AISC Design Guide 3 yields a camber of:

Camber = 0.8(2.59 in.)
       = 2.07 in.

Rounding down to the nearest ¼ in. increment yields a specified camber of 2 in.

Select a W21×50 with 2 in. of camber.

**Design for Composite Condition**

**Required Flexural Strength**

Using tributary area calculations, the total uniform loads (including pre-composite dead loads in addition to dead and live loads applied after composite action has been achieved) are determined as:

$$w_D = \left[(10 \text{ ft})(75 \text{ lb/ft}^2 + 5 \text{ lb/ft}^2 + 10 \text{ lb/ft}^2)\right](1 \text{ kip}/1{,}000 \text{ lb})$$

$$= 0.900 \text{ kip/ft}$$

$$w_L = \left[(10 \text{ ft})(100 \text{ lb/ft}^2)\right](1 \text{ kip}/1{,}000 \text{ lb})$$

$$= 1.00 \text{ kip/ft}$$

From ASCE/SEI 7, Chapter 2, the required flexural strength is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.900 \text{ kip/ft}) + 1.6(1.00 \text{ kip/ft})$ | $w_a = 0.900 \text{ kip/ft} + 1.00 \text{ kip/ft}$ |
| $= 2.68 \text{ kip/ft}$ | $= 1.90 \text{ kip/ft}$ |
| $M_u = \dfrac{w_u L^2}{8}$ | $M_a = \dfrac{w_a L^2}{8}$ |
| $= \dfrac{(2.68 \text{ kip/ft})(45 \text{ ft})^2}{8}$ | $= \dfrac{(1.90 \text{ kip/ft})(45 \text{ ft})^2}{8}$ |
| $= 678 \text{ kip-ft}$ | $= 481 \text{ kip-ft}$ |

**Determine effective width, b**

The effective width of the concrete slab is the sum of the effective widths to each side of the beam centerline as determined by the minimum value of the three widths set forth in AISC *Specification* Section I3.1a:

1. one-eighth of the beam span, center-to-center of supports

   $$\frac{45 \text{ ft}}{8}(2 \text{ sides}) = 11.3 \text{ ft}$$

---

# I-9

2. one-half the distance to the centerline of the adjacent beam

   $$\frac{10 \text{ ft}}{2}(2 \text{ sides}) = 10.0 \text{ ft}$$ **controls**

3. distance to the edge of the slab

   The latter is not applicable for an interior member.

**Available Flexural Strength**

According to AISC *Specification* Section I3.2a, the nominal flexural strength shall be determined from the plastic stress distribution on the composite section when $h/t_w \leq 3.76\sqrt{E/F_y}$.

$$3.76\sqrt{\frac{E}{F_y}} = 3.76\sqrt{\frac{29{,}000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 90.6 > 49.4$$

Therefore, use the plastic stress distribution to determine the nominal flexural strength.

According to the User Note in AISC *Specification* Section I3.2a, this check is generally unnecessary as all current W-shapes satisfy this limit for $F_y \leq 70 \text{ ksi}$.

Flexural strength can be determined using AISC *Manual* Table 3-18 or calculated directly using the provisions of AISC *Specification* Chapter I. This design example illustrates the use of the *Manual* table only. For an illustration of the direct calculation procedure, refer to Design Example I.2.

To utilize AISC *Manual* Table 3-18, the distance from the compressive concrete flange force to beam top flange, Y2, must first be determined as illustrated by *Manual* Figure 3-3. Fifty percent composite action $\left[\sum Q_n = 0.50\left(A_s F_y\right)\right]$ is used to calculate a trial value of the compression block depth, $a_{trial}$, for determining Y2 as follows:

$$a_{trial} = \frac{\sum Q_n}{0.85 f_c' b}$$
$$({\text{from } Manual \text{ Eq. 3-7}})$$

$$= \frac{0.50\left(A_s F_y\right)}{0.85 f_c' b}$$

$$= \frac{0.50(14.7 \text{ in.}^2)(50 \text{ ksi})}{0.85(4 \text{ ksi})(10.0 \text{ ft})(12 \text{ in./ft})}$$

$$= 0.901 \text{ in.} \rightarrow \text{use } 1 \text{ in.}$$

Note that a trial value of $a = 1 \text{ in.}$ is a common starting point in many design problems.

$$Y2 = Y_{con} - \frac{a_{trial}}{2}$$
$$({\text{from } Manual. \text{ Eq } 3\text{-}6})$$

where
$Y_{con}$ = distance from top of steel beam to top of slab, in.
       = 7.50 in.

$$Y2 = 7.50 \text{ in.} - \frac{1 \text{ in.}}{2}$$

$$= 7.00 \text{ in.}$$

---

# I-10

Enter AISC *Manual* Table 3-18 with the required strength and Y2 = 7.00 in. to select a plastic neutral axis location for the W21×50 that provides sufficient available strength.

Selecting PNA location 5 (BFL) with $\sum Q_n = 386 \text{ kips}$ provides a flexural strength of:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 769 \text{ kip-ft} > 678 \text{ kip-ft}$ **o.k.** | $\dfrac{M_n}{\Omega_b} = 512 \text{ kip-ft} > 481 \text{ kip-ft}$ **o.k.** |

Based on the available flexural strength provided in Table 3-18, the required PNA location for ASD and LRFD design methodologies differ. This discrepancy is due to the live to dead load ratio in this example, which is not equal to the ratio of 3 at which ASD and LRFD design methodologies produce equivalent results as discussed in AISC *Specification* Commentary Section B3.2. The selected PNA location 5 is acceptable for ASD design, and more conservative for LRFD design.

The actual value for the compression block depth, $a$, is determined as follows:

$$a = \frac{\sum Q_n}{0.85 f_c' b}$$
$$({Manual \text{ Eq. 3-7}})$$

$$= \frac{386 \text{ kips}}{0.85(4 \text{ ksi})(10.0 \text{ ft})(12 \text{ in./ft})}$$

$$= 0.946 \text{ in.} < a_{trial} = 1 \text{ in.}$$ **o.k.**

**Live Load Deflection**

Deflections due to live load applied after composite action has been achieved will be limited to $L/360$ under the design live load as required by Table 1604.3 of the *International Building Code* (IBC) (ICC, 2021), or 1 in. using a 50% reduction in design live load as recommended by AISC Design Guide 3.

Deflections for composite members may be determined using the lower bound moment of inertia provided by *Specification* Commentary Equation C-I3-1 and tabulated in AISC *Manual* Table 3-19. The *Specification* Commentary also provides an alternate method for determining deflections of a composite member through the calculation of an effective moment of inertia. This design example illustrates the use of the *Manual* table. For an illustration of the direct calculation procedure for each method, refer to Design Example I.2.

Entering Table 3-19, for a W21×50 with PNA location 5 and Y2 = 7.00 in., provides a lower bound moment of inertia of $I_{LB} = 2{,}520 \text{ in.}^4$

Inserting $I_{LB}$ into AISC *Manual* Table 3-22, Case 1, to determine the live load deflection under the full design live load for comparison to the IBC limit yields:

$$\Delta_s = \frac{5w_L L^4}{384EI_{LB}}$$

$$= \frac{5(1.00 \text{ kip/ft})(1 \text{ ft}/12 \text{ in.})\left[(45 \text{ ft})(12 \text{ in./ft})\right]^4}{384(29{,}000 \text{ ksi})(2{,}520 \text{ in.}^4)}$$

$$= 1.26 \text{ in.}$$

$$= L/429 < L/360$$ **o.k.**

---

# I-11

Performing the same check with 50% of the design live load for comparison to the AISC Design Guide 3 limit yields:

$$\Delta_s = 0.50(1.26 \text{ in.})$$

$$= 0.630 \text{ in.} < 1 \text{ in.}$$ **o.k.**

**Steel Anchor Strength**

Steel headed stud anchor strengths are tabulated in AISC *Manual* Table 3-20 for typical conditions. Conservatively assuming that all anchors are placed in the weak position, the strength for ¾-in.-diameter anchors in normal weight concrete with $f_c' = 4 \text{ ksi}$ and deck oriented perpendicular to the beam is:

1 anchor per rib: $Q_n = 17.2 \text{ kips/anchor}$
2 anchors per rib: $Q_n = 14.6 \text{ kips/anchor}$

**Number and Spacing of Anchors**

Deck flutes are spaced at 12 in. on center according to the deck manufacturer's literature. The minimum number of deck flutes along each half of the 45 ft long beam, assuming the first flute begins a maximum of 12 in. from the support line at each end, is:

$$n_{flutes} = n_{spaces} + 1$$

$$= \frac{45 \text{ ft} - 2(12 \text{ in.})(1 \text{ ft}/12 \text{ in.})}{2(1 \text{ ft per space})} + 1$$

$$= 22.5 \rightarrow \text{use } 22 \text{ flutes}$$

According to AISC *Specification* Section I8.2c, the number of steel headed stud anchors required between the section of maximum bending moment and the nearest point of zero moment is determined by dividing the required horizontal shear, $\sum Q_n$, by the nominal shear strength per anchor, $Q_n$. Assuming one anchor per flute:

$$n_{anchors} = \frac{\sum Q_n}{Q_n}$$

$$= \frac{386 \text{ kips}}{17.2 \text{ kips/anchor}}$$

$$= 22.4 \rightarrow \text{place } 23 \text{ anchors on each side of the beam centerline}$$

As the number of anchors exceeds the number of available flutes by one, place two anchors in the first flute. The revised horizontal shear capacity of the anchors taking into account the reduced strength for two anchors in one flute is:

$$\sum Q_n = 2(14.6 \text{ kips}) + 21(17.2 \text{ kips})$$

$$= 390 \text{ kips} > 386 \text{ kips}$$ **o.k.**

**Steel Anchor Ductility Check—Prescriptive Procedure**

As discussed in AISC *Specification* Commentary to Section I3.2d.1, beams are not susceptible to connector failure due to insufficient deformation capacity if they meet one or more of the following conditions:

1. Beams with span not exceeding 30 ft;
2. Beams with a degree of composite action of at least 50%; or
3. Beams with an average nominal shear connector capacity of at least 16 kips per foot along their shear span, corresponding to a ¾-in.-diameter steel headed stud anchor placed at 12 in. spacing on average.

---

# I-12

The span is 45 ft, which exceeds the 30 ft limit. The percent composite action is:

$$\frac{\sum Q_n}{\min\left\{0.85 f_c' A_c, F_y A_s\right\}} = \frac{390 \text{ kips}}{\min\left\{0.85(4 \text{ ksi})(10.0 \text{ ft})(12 \text{ in./ft})(4.5 \text{ in.}), (50 \text{ ksi})(14.7 \text{ in.}^2)\right\}}(100)$$

$$= \frac{390 \text{ kips}}{735 \text{ kips}}(100)$$

$$= 53.1\%$$

which exceeds the minimum degree of composite action of 50%. The average shear connector capacity is:

$$\frac{(42 \text{ anchors})(17.2 \text{ kips/anchor}) + (4 \text{ anchors})(14.6 \text{ kips/anchor})}{45 \text{ ft}} = 17.4 \text{ kip/ft}$$

which exceeds the minimum capacity of 16 kips per foot. Because at least one of the conditions has been met (in fact, two have been met), the shear connectors meet the ductility requirements.

**Steel Anchor Ductility Check—Analytical Procedure**

As discussed in AISC *Specification* Commentary to Section I3.2d.1, the steel anchor ductility can also be checked analytically. An analytical check can be performed by nonlinear modeling or by an alternative analysis approach. One alternative analysis approach based on Oehlers and Sved (1995) is illustrated here.

For composite beams with steel stud anchors meeting the requirements of AISC *Specification* Chapter I, experimental data indicate that a slip capacity ($S_u$) of 0.25 in. is safe and reasonable.

$S_u = 0.25 \text{ in.}$

Stiffness factors $K_1$ and $K_2$ are calculated in accordance with Oehlers and Sved (1995), where $h_s$ and $h_c$ are the distances from the geometric centroid of the steel beam and concrete deck, respectively, to the top of the steel beam:

$$K_1 = \frac{h_s + h_c}{E_s I_s + E_c I_c}$$

$$K_2 = \frac{(h_s + h_c)^2}{E_s I_s + E_c I_c} + \frac{1}{E_s A_s} + \frac{1}{E_c A_c}$$

$$h_s = \frac{d}{2}$$

$$= \frac{20.8 \text{ in.}}{2}$$

$$= 10.4 \text{ in.}$$

$$A_s = A$$

$$= 14.7 \text{ in.}^2$$

$$I_s = I_x$$

$$= 984 \text{ in.}^4$$

---

# I-13

$$h_c = \frac{4.50 \text{ in.}}{2} + 3.00 \text{ in.}$$

$$= 5.25 \text{ in.}$$

$$A_c = b(4.50 \text{ in.})$$

$$= 10.0 \text{ ft}(12 \text{ in./ft})(4.50 \text{ in.})$$

$$= 540 \text{ in.}^2$$

$$I_c = \frac{b(4.50 \text{ in.})^3}{12}$$

$$= \frac{10.0 \text{ ft}(12 \text{ in./ft})(4.50 \text{ in.})^3}{12}$$

$$= 911 \text{ in.}^4$$

$$E_c = w_c^{1.5}\sqrt{f_c'}$$

$$= \left(145 \text{ lb/ft}^3\right)^{1.5}\sqrt{4 \text{ ksi}}$$

$$= 3{,}490 \text{ ksi}$$

$$K_1 = \frac{h_s + h_c}{E_s I_s + E_c I_c}$$

$$= \frac{10.4 \text{ in.} + 5.25 \text{ in.}}{(29{,}000 \text{ ksi})(984 \text{ in.}^4) + (3{,}490 \text{ ksi})(911 \text{ in.}^4)}$$

$$= 493 \times 10^{-9} \frac{1}{\text{kip-in.}}$$

$$K_2 = \frac{(h_s + h_c)^2}{E_s I_s + E_c I_c} + \frac{1}{E_s A_s} + \frac{1}{E_c A_c}$$

$$= \frac{(10.4 \text{ in.} + 5.25 \text{ in.})^2}{(29{,}000 \text{ ksi})(984 \text{ in.}^4) + (3{,}490 \text{ ksi})(911 \text{ in.}^4)} + \frac{1}{(29{,}000 \text{ ksi})(14.7 \text{ in.}^2)} + \frac{1}{(3{,}490 \text{ ksi})(540 \text{ in.}^2)}$$

$$= 10.6 \times 10^{-6} \frac{1}{\text{kip}}$$

Mujagic et al. (2015) provides equations for flexural strength limited by shear ductility for various cases, which have been derived from the theory from Oehlers and Sved (1995). For a uniformly loaded beam:

$$M_{n,sc} = \frac{3S_u + 0.75\sum Q_n LK_2}{LK_1}$$

$$= \frac{3(0.25 \text{ in.})(1 \text{ ft}/12 \text{ in.}) + 0.75(390 \text{ kips})(45 \text{ ft})\left(10.6 \times 10^{-6} \frac{1}{\text{kip}}\right)}{45 \text{ ft}\left(493 \times 10^{-9} \frac{1}{\text{kip-in.}}\right)(12 \text{ in./ft})}$$

$$= 759 \text{ kip-ft}$$

---

# I-14

| LRFD | ASD |
|------|-----|
| $\phi_b M_{n,sc} = 0.90(759 \text{ kip-ft})$ | $\dfrac{M_{n,sc}}{\Omega_b} = \dfrac{759 \text{ kip-ft}}{1.67}$ |
| $= 683 \text{ kip-ft} > 678 \text{ kip-ft}$ **o.k.** | $= 454 \text{ kip-ft} < 481 \text{ kip-ft}$ **n.g.** |

For LRFD, the beam is strong enough when ductility is considered. However, by this analytical procedure, for ASD, the beam is not strong enough when ductility is considered. This discrepancy is due to differences between the two methodologies, which results in a more conservative design for ASD for this beam, as described previously in this example.

To satisfy the ductility requirements for ASD using this analytical procedure, use three additional anchors for a total of 26 anchors on each side of the beam midspan. In this configuration, place two anchors in the last four flutes and one anchor in each remaining flute:

$$\sum Q_n = 8(14.6 \text{ kips}) + 18(17.2 \text{ kips})$$

$$= 426 \text{ kips}$$

$$M_{n,sc} = \frac{3S_u + 0.75\sum Q_n LK_2}{LK_1}$$

$$= \frac{3(0.25 \text{ in.})(1 \text{ ft}/12 \text{ in.}) + 0.75(426 \text{ kips})(45 \text{ ft})\left(10.6 \times 10^{-6} \frac{1}{\text{kip}}\right)}{45 \text{ ft}\left(493 \times 10^{-9} \frac{1}{\text{kip-in.}}\right)(12 \text{ in./ft})}$$

$$= 807 \text{ kip-ft}$$

| LRFD | ASD |
|------|-----|
| $\phi_b M_{n,sc} = 0.9(807 \text{ kip-ft})$ | $\dfrac{M_{n,sc}}{\Omega_b} = \dfrac{807 \text{ kip-ft}}{1.67}$ |
| $= 726 \text{ kip-ft} > 678 \text{ kip-ft}$ **o.k.** | $= 483 \text{ kip-ft} > 481 \text{ kip-ft}$ **o.k.** |

While the analytical procedure indicates that 26 anchors are needed to satisfy the ductility requirements for ASD, 23 anchors can be used, as was previously determined using the prescriptive method.

**Anchor Layout**

The final anchor pattern chosen is illustrated in Figure I.1-2.

Review steel headed stud anchor spacing requirements of AISC *Specification* Sections I8.2d and I3.2c.

1. Maximum anchor spacing along beam [Section I8.2d(c)]:

   $$8t_{slab} = 8(7.50 \text{ in.})$$

   $$= 60.0 \text{ in.}$$

   or

   36 in.

The maximum anchor spacing permitted is 36 in.

$$36 \text{ in.} > 12 \text{ in.}$$ **o.k.**

---

# I-15

2. Minimum anchor spacing along beam [Section I8.2d(d)]:

   $$4d_{sa} = 4(\frac{3}{4} \text{ in.})$$

   $$= 3.00 \text{ in.} < 12 \text{ in.}$$ **o.k.**

3. Minimum transverse spacing between anchor pairs [Section I8.2d(d)]:

   $$4d_{sa} = 4(\frac{3}{4} \text{ in.})$$

   $$= 3.00 \text{ in.} \leq 3.00 \text{ in.}$$ **o.k.**

4. Minimum distance to free edge in the direction of the horizontal shear force:

   AISC *Specification* Section I8.2d requires that the distance from the center of an anchor to a free edge in the direction of the shear force be a minimum of 8 in. for normal weight concrete slabs.

5. Maximum spacing of deck attachment:

   AISC *Specification* Section I3.2c.1(d) requires that steel deck be anchored to all supporting members at a maximum spacing of 18 in. The stud anchors are welded through the metal deck at a maximum spacing of 12 inches in this example, thus this limit is met without the need for additional puddle welds or mechanical fasteners.

**Available Shear Strength**

According to AISC *Specification* Section I4.3, the beam should be assessed for available shear strength as a bare steel beam using the provisions of Chapter G.

Applying the loads previously determined for the governing ASCE/SEI 7 load combinations and using available shear strengths from AISC *Manual* Table 3-2 for a W21×50 yields the following:

| LRFD | ASD |
|------|-----|
| $V_u = \dfrac{w_u L}{2}$ | $V_a = \dfrac{w_a L}{2}$ |
| $= \dfrac{(2.68 \text{ kips/ft})(45 \text{ ft})}{2}$ | $= \dfrac{(1.90 \text{ kips/ft})(45 \text{ ft})}{2}$ |
| $= 60.3 \text{ kips}$ | $= 42.8 \text{ kips}$ |
| $\phi_v V_n = 237 \text{ kips} > 60.3 \text{ kips}$ **o.k.** | $\dfrac{V_n}{\Omega_v} = 158 \text{ kips} > 42.8 \text{ kips}$ **o.k.** |

**Serviceability**

Depending on the intended use of this bay, vibrations might need to be considered. Refer to AISC Design Guide 11 (Murray et al., 2016) for additional information.

**Summary**

From Figure I.1-2, the total number of stud anchors used is equal to $(2)(2 + 21) = 46$. A plan layout illustrating the final beam design is provided in Figure I.1-3. A W21×50 with 2 in. of camber and 46, ¾-in.-diameter by 4⅝-in.-long steel headed stud anchors is adequate to resist the imposed loads.

---

# I-16

![Steel headed stud anchor layout diagram showing plan view with girders, beam, deck (not shown for clarity), and anchor placement. Shows 2 anchors in first flute on each end, 21 spaces @ 12" (21 single anchors) in middle section, and 2 spaces @ 6" at center. Dimensions marked include 12" from supports and 3" minimum clearance. Note indicates "Modify to coordinate with deck layout"]

*Fig. I.1-2. Steel headed stud anchor layout.*

![Plan layout showing final beam design with two W21×50 c = 2" (46) beams spaced at 3 @ 10'-0" = 30'-0" center-to-center, with 45'-0" span]

*Fig. I.1-3. Plan layout of final beam design.*

---

# I-17

## EXAMPLE I.2 COMPOSITE GIRDER DESIGN

### Given:

Two typical bays of a composite floor system are illustrated in Figure I.2-1. Select an appropriate ASTM A992/A992M W-shaped girder and determine the required number of steel headed stud anchors. The girder will not be shored during construction. Use steel headed stud anchors made from ASTM A29/A29M material, with $F_u = 65 \text{ ksi}$.

![Plan and section view showing composite floor system. Plan shows 45'-0" spans with 3 @ 10'-0" = 30'-0" spacing, girder to be designed, and W21×50 (46) typ. composite beam per Example I.1. Section A-A shows 7½" total depth normal weight slab on 18 gage composite deck with 4½" slab above deck, 3" deck depth, and $w_r = 6$"]

*Fig. I.2-1. Composite bay and girder section.*

To achieve a two-hour fire rating without the application of spray applied fire protection material to the composite deck, 4½ in. of normal weight (145 lb/ft³) concrete will be placed above the top of the deck. The concrete has a specified compressive strength, $f_c' = 4 \text{ ksi}$.

Applied loads are given in the following:

Dead Loads:
Pre-composite:
Slab = 75 lb/ft² (in accordance with metal deck manufacturer's data)
Self-weight = 80 lb/ft (trial girder weight)
           = 50 lb/ft (beam weight from Design Example I.1)

Composite (applied after composite action has been achieved):
Miscellaneous = 10 lb/ft² (HVAC, ceiling, floor covering, etc.)

---

# I-18

Live Loads:
Pre-composite:
Construction = 25 lb/ft² (temporary loads during concrete placement)

Composite (applied after composite action has been achieved):
Non-reducible = 100 lb/ft² (assembly occupancy)

### Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A992/A992M
$F_y = 50 \text{ ksi}$

**Applied Loads**

For slabs that are to be placed at a constant elevation, AISC Design Guide 3 recommends an additional 10% of the nominal slab weight be applied to account for concrete ponding due to deflections resulting from the wet weight of the concrete during placement. For the slab under consideration, this would result in an additional load of 8 lb/ft²; however, for this design the slab will be placed at a constant thickness, and thus, no additional weight for concrete ponding is required.

For pre-composite construction live loading, 25 lb/ft² will be applied in accordance with recommendations from *Design Loads on Structures During Construction*, ASCE/SEI 37 (ASCE, 2014), for a light duty operational class that includes concrete transport and placement by hose and finishing with hand tools.

**Composite Deck and Anchor Requirements**

Check composite deck and anchor requirements stipulated in AISC *Specification* Sections I1.3, I3.2c, and I8.

1. Concrete strength: 3 ksi ≤ $f_c' \leq 10 \text{ ksi}$ (for normal weight concrete) (*Spec.* Section I1.3)
   $f_c' = 4 \text{ ksi}$ **o.k.**

2. Rib height: $h_r \leq 3 \text{ in.}$ (*Spec.* Section I3.2c)
   $h_r = 3 \text{ in.}$ **o.k.**

3. Average rib width: $w_r \geq 2 \text{ in.}$ (*Spec.* Section I3.2c)
   $w_r = 6 \text{ in.}$ (See Figure I.2-1) **o.k.**

4. Use steel headed stud anchors ¾ in. or less in diameter. (*Spec.* Section I8.1)
   Select ¾-in.-diameter steel anchors. **o.k.**

5. Steel headed stud anchor diameter: $d_{sa} \leq 2.5t_f$ (*Spec.* Section I8.1)

   In accordance with AISC *Specification* Section I8.1, this limit only applies if steel headed stud anchors are not welded to the flange directly over the web. The ¾-in.-diameter anchors will be attached in a staggered pattern, thus this limit must be satisfied. Select a girder size with a minimum flange thickness of 0.300 in., as determined in the following:

---

# I-19

$$t_f \geq \frac{d_{sa}}{2.5}$$

$$\geq \frac{\frac{3}{4} \text{ in.}}{2.5}$$

$$\geq 0.300 \text{ in.}$$

6. In accordance with AISC *Specification* I3.2c, steel headed stud anchors, after installation, shall extend not less than 1½ in. above the top of the steel deck. A minimum anchor length of 4½ in. is required to meet this requirement for 3-in.-deep deck. From steel headed stud anchor manufacturer's data, a standard stock length of 4⅝ in. is selected. Using a $\frac{1}{16}$ in. length reduction to account for burn off during anchor installation directly to the girder flange yields a final installed length of 4¹⁄₁₆ in.

   $$4\frac{1}{16} \text{ in.} > 4\frac{1}{2} \text{ in.}$$ **o.k.**

7. Minimum length of stud anchors = $4d_{sa}$ (*Spec.* Section I8.2)

   $$4\frac{1}{16} \text{ in.} > 4(\frac{3}{4} \text{ in.}) = 3.00 \text{ in.}$$ **o.k.**

8. In accordance with AISC *Specification* Section I3.2c, there shall be at least ½ in. of specified concrete cover above the top of the headed stud anchors.

   As discussed in the *Specification* Commentary to Section I3.2c, it is advisable to provide greater than ½ in. minimum cover to assure anchors are not exposed in the final condition.

   $$7\frac{1}{2} \text{ in.} - 4\frac{1}{16} \text{ in.} = 2\frac{7}{16} \text{ in.} > \frac{1}{2} \text{ in.}$$ **o.k.**

9. In accordance with AISC *Specification* Section I3.2c, slab thickness above steel deck shall not be less than 2 in.

   $$4\frac{1}{2} \text{ in.} > 2 \text{ in.}$$ **o.k.**

**Design for Pre-Composite Condition**

**Construction (Pre-Composite) Loads**

The girder will be loaded at third points by the supported beams. Determine point loads using tributary areas.

$$P_D = \left[(45 \text{ ft})(10 \text{ ft})(75 \text{ lb/ft}^2) + (45 \text{ ft})(50 \text{ lb/ft})\right](1 \text{ kip}/1{,}000 \text{ lb})$$

$$= 36.0 \text{ kips}$$

$$P_L = \left[(45 \text{ ft})(10 \text{ ft})(25 \text{ lb/ft}^2)\right](1 \text{ kip}/1{,}000 \text{ lb})$$

$$= 11.3 \text{ kips}$$

**Construction (Pre-Composite) Flexural Strength**

From ASCE/SEI 7, Chapter 2, the required flexural strength is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(36.0 \text{ kips}) + 1.6(11.3 \text{ kips})$ | $P_a = 36.0 \text{ kips} + 11.3 \text{ kips}$ |
| $= 61.3 \text{ kips}$ | $= 47.3 \text{ kips}$ |

---

# I-20

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(80 \text{ lb/ft})(1 \text{ kip}/1{,}000 \text{ lb})$ | $w_a = (80 \text{ lb/ft})(1 \text{ kip}/1{,}000 \text{ lb})$ |
| $= 0.0960 \text{ kip/ft}$ | $= 0.0800 \text{ kip/ft}$ |
| $M_u = P_u a + \dfrac{w_u L^2}{8}$ | $M_a = P_a a + \dfrac{w_a L^2}{8}$ |
| $= (61.3 \text{ kips})(10 \text{ ft}) + \dfrac{(0.0960 \text{ kip/ft})(30 \text{ ft})^2}{8}$ | $= (47.3 \text{ kips})(10 \text{ ft}) + \dfrac{(0.0800 \text{ kip/ft})(30 \text{ ft})^2}{8}$ |
| $= 624 \text{ kip-ft}$ | $= 482 \text{ kip-ft}$ |

**Girder Selection**

Based on the required flexural strength under construction loading, a trial member can be selected utilizing AISC *Manual* Table 3-2. For the purposes of this example, the unbraced length of the girder prior to hardening of the concrete is taken as the distance between supported beams (one-third of the girder length).

Try a W24×76

$$L_b = 10 \text{ ft}$$
$$L_p = 6.78 \text{ ft}$$
$$L_r = 19.5 \text{ ft}$$

| LRFD | ASD |
|------|-----|
| $\phi_b BF = 22.6 \text{ kips}$ | $BF/\Omega_b = 15.1 \text{ kips}$ |
| $\phi_b M_{px} = 750 \text{ kip-ft}$ | $M_{px}/\Omega_b = 499 \text{ kip-ft}$ |
| $\phi_b M_{rx} = 462 \text{ kip-ft}$ | $M_{rx}/\Omega_b = 307 \text{ kip-ft}$ |

Because $L_p < L_b < L_r$, use AISC *Manual* Equations 3-4a and 3-4b with $C_b = 1.0$ within the center girder segment in accordance with AISC *Manual* Table 3-1:

| LRFD | ASD |
|------|-----|
| From AISC *Manual* Equation 3-4a: | From AISC *Manual* Equation 3-4b: |
| $\phi_b M_n = C_b\left[\phi_b M_{px} - \phi_b BF(L_b - L_p)\right] \leq \phi_b M_{px}$ | $\dfrac{M_n}{\Omega_b} = C_b\left[\dfrac{M_{px}}{\Omega_b} - \dfrac{BF}{\Omega_b}(L_b - L_p)\right] \leq \dfrac{M_{px}}{\Omega_b}$ |
| $= 1.0\left[750 \text{ kip-ft} - (22.6 \text{ kips})(10 \text{ ft} - 6.78 \text{ ft})\right]$ | $= 1.0\left[499 \text{ kip-ft} - (15.1 \text{ kips})(10 \text{ ft} - 6.78 \text{ ft})\right]$ |
| $\leq 750 \text{ kip-ft}$ | $\leq 499 \text{ kip-ft}$ |
| $= 677 \text{ kip-ft} < 750 \text{ kip-ft}$ | $= 450 \text{ kip-ft} < 499 \text{ kip-ft}$ |
| $= 677 \text{ kip-ft}$ | $= 450 \text{ kip-ft}$ |
| $\phi_b M_n \geq M_u$ | $\dfrac{M_n}{\Omega_b} \geq M_a$ |
| $677 \text{ kip-ft} > 624 \text{ kip-ft}$ **o.k.** | $450 \text{ kip-ft} < 482 \text{ kip-ft}$ **n.g.** |

For this example, the relatively low live load to dead load ratio results in a lighter member when LRFD methodology is employed. When ASD methodology is employed, a heavier member is required, and it can be shown that a W24×84 is adequate for pre-composite flexural strength. This example uses a W24×76 member to illustrate the determination

---

# I-21

of flexural strength of the composite section using both LRFD and ASD methodologies; however, this is done for comparison purposes only, and calculations for a W24×84 as required to provide a satisfactory ASD design. Calculations for the heavier section are not shown as they would essentially be a duplication of the calculations provided for the W24×76 member.

Note that for the member size chosen, 76 lb/ft < 80 lb/ft, thus the initial weight assumption is adequate.

From AISC *Manual* Table 1-1, the geometric properties are as follows:

W24×76
$A = 22.4 \text{ in.}^2$
$I_x = 2{,}100 \text{ in.}^4$
$b_f = 8.99 \text{ in.}$
$t_f = 0.680 \text{ in.}$
$d = 23.9 \text{ in.}$
$\dfrac{h}{t_w} = 49.0$

**Pre-Composite Deflections**

AISC Design Guide 3 recommends deflections due to concrete plus self-weight not exceed the minimum of $L/360$ or 1.0 in.

From the superposition of AISC *Manual* Table 3-22, Cases 1 and 9:

$$\Delta_{nc} = \frac{23P_D L^3}{648EI} + \frac{5w_D L^4}{384EI}$$

Substituting for the moment of inertia of the non-composite section, $I = 2{,}100 \text{ in.}^4$, yields a dead load deflection of:

$$\Delta_{nc} = \frac{23(36.0 \text{ kips})\left[(30 \text{ ft})(12 \text{ in./ft})\right]^3}{648(29{,}000 \text{ ksi})(2{,}100 \text{ in.}^4)} + \frac{5(0.0760 \text{ kip/ft})(1 \text{ ft}/12 \text{ in.})\left[(30 \text{ ft})(12 \text{ in./ft})\right]^4}{384(29{,}000 \text{ ksi})(2{,}100 \text{ in.}^4)}$$

$$= 1.00 \text{ in.}$$

$$\approx L/360$$ **o.k.**

Pre-composite deflections barely meet the recommended value. Although technically acceptable, judgment leads one to consider ways to minimize pre-composite deflections. One possible solution is to increase the member size. A second solution is to introduce camber into the member. For this example, the second solution is selected, and the girder will be cambered to reduce pre-composite deflections.

Reducing the estimated simple span deflections to 80% of the calculated value to reflect the partial restraint of the end connections as recommended in AISC Design Guide 3 yields a camber of:

Camber = 0.80(1.00 in.)
       = 0.800 in.

Rounding down to the nearest ¼ in. increment yields a specified camber of ¾ in.

Select a W24×76 with ¾ in. of camber.

---

# I-22

## Design for Composite Flexural Strength

**Required Flexural Strength**

Using tributary area calculations, the total applied point loads (including pre-composite dead loads in addition to dead and live loads applied after composite action has been achieved) are determined as:

$$P_D = \left[(45 \text{ ft})(10 \text{ ft})(75 \text{ lb/ft}^2 + 10 \text{ lb/ft}^2) + (45 \text{ ft})(50 \text{ lb/ft})\right](1 \text{ kip}/1{,}000 \text{ lb})$$

$$= 40.5 \text{ kips}$$

$$P_L = \left[(45 \text{ ft})(10 \text{ ft})(100 \text{ lb/ft}^2)\right](1 \text{ kip}/1{,}000 \text{ lb})$$

$$= 45.0 \text{ kips}$$

The required flexural strength diagram is illustrated in Figure I.2-2:

From ASCE/SEI 7, Chapter 2, the required flexural strength is:

| LRFD | ASD |
|------|-----|
| $P_r = P_u$ | $P_r = P_a$ |
| $= 1.2(40.5 \text{ kips}) + 1.6(45.0 \text{ kips})$ | $= 40.5 \text{ kips} + 45.0 \text{ kips}$ |
| $= 121 \text{ kips}$ | $= 85.5 \text{ kips}$ |
| $w_u = 1.2(0.0760 \text{ kip/ft})$ | $w_a = 0.0760 \text{ kip/ft}$ (from self weight) |
| $= 0.0912 \text{ kip/ft}$ (from self weight) | |

![Required flexural strength diagram showing simply supported beam with two point loads $P_r$ at third points (a = 10'-0" from each support), total span 30'-0", with moment diagram below showing $M_{r1}$, $M_{r2}$, $M_{r3}$ forming triangular shape with peak $M_r$ (kip-ft) at center]

*Fig. I.2-2. Required flexural strength diagram.*

---

# I-23

| LRFD | ASD |
|------|-----|
| From AISC *Manual* Table 3-22, Case 1 and 9: | From AISC *Manual* Table 3-22, Case 1 and 9: |
| $M_{r1} = M_{r3}$ | $M_{r1} = M_{r3}$ |
| $= P_u a + \dfrac{w_u a}{2}(L - a)$ | $= P_a a + \dfrac{w_a a}{2}(L - a)$ |
| $= (121 \text{ kips})(10 \text{ ft})$ | $= (85.5 \text{ kips})(10 \text{ ft})$ |
| $+ \dfrac{(0.0912 \text{ kip/ft})(10 \text{ ft})}{2}(30 \text{ ft} - 10 \text{ ft})$ | $+ \dfrac{(0.0760 \text{ kip/ft})(10 \text{ ft})}{2}(30 \text{ ft} - 10 \text{ ft})$ |
| $= 1{,}220 \text{ kip-ft}$ | $= 863 \text{ kip-ft}$ |
| $M_{r2} = P_u a + \dfrac{w_u L^2}{8}$ | $M_{r2} = P_a a + \dfrac{w_a L^2}{8}$ |
| $= (121 \text{ kips})(10 \text{ ft}) + \dfrac{(0.0912 \text{ kip/ft})(30 \text{ ft})^2}{8}$ | $= (85.5 \text{ kips})(10 \text{ ft}) + \dfrac{(0.0760 \text{ kip/ft})(30 \text{ ft})^2}{8}$ |
| $= 1{,}220 \text{ kip-ft}$ | $= 864 \text{ kip-ft}$ |

**Determine Effective Width, b**

The effective width of the concrete slab is the sum of the effective widths to each side of the beam centerline as determined by the minimum value of the three conditions set forth in AISC *Specification* Section I3.1a:

1. one-eighth of the girder span center-to-center of supports

   $$\frac{30 \text{ ft}}{8}(2 \text{ sides}) = 7.50 \text{ ft}$$ **controls**

2. one-half the distance to the centerline of the adjacent girder

   $$\frac{45 \text{ ft}}{2}(2 \text{ sides}) = 45.0 \text{ ft}$$

3. distance to the edge of the slab

   The latter is not applicable for an interior member.

**Available Flexural Strength**

According to AISC *Specification* Section I3.2a, the nominal flexural strength shall be determined from the plastic stress distribution on the composite section when $h/t_w \leq 3.76\sqrt{E/F_y}$.

$$3.76\sqrt{\frac{E}{F_y}} = 3.76\sqrt{\frac{29{,}000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 90.6 > 49.0$$

Therefore, use the plastic stress distribution to determine the nominal flexural strength.

According to the User Note in AISC *Specification* Section I3.2a, this check is generally unnecessary as all current W-shapes satisfy this limit for $F_y \leq 70 \text{ ksi}$.

---

# I-24

AISC *Manual* Table 3-18 can be used to facilitate the calculation of flexural strength for composite beams. Alternately, the available flexural strength can be determined directly using the provisions of AISC *Specification* Chapter I. Both methods will be illustrated for comparison in the following calculations.

**Method 1: AISC Manual**

To utilize AISC *Manual* Table 3-18, the distance from the compressive concrete flange force to beam top flange, Y2, must first be determined as illustrated by *Manual* Figure 3-3. Fifty percent composite action $\left[\sum Q_n = 0.50\left(A_s F_y\right)\right]$ is used to calculate a trial value of the compression block depth, $a_{trial}$, for determining Y2 as follows:

$$a_{trial} = \frac{\sum Q_n}{0.85 f_c' b}$$
$$({\text{from } Manual \text{ Eq. 3-7}})$$

$$= \frac{0.50\left(A_s F_y\right)}{0.85 f_c' b}$$

$$= \frac{0.50(22.4 \text{ in.}^2)(50 \text{ ksi})}{0.85(4 \text{ ksi})(7.50 \text{ ft})(12 \text{ in./ft})}$$

$$= 1.83 \text{ in.}$$

$$Y2 = Y_{con} - \frac{a_{trial}}{2}$$
$$({\text{from } Manual. \text{ Eq. } 3\text{-}6})$$

where
$Y_{con}$ = distance from top of steel beam to top of slab
       = 7.50 in.

$$Y2 = 7.50 \text{ in.} - \frac{1.83 \text{ in.}}{2}$$

$$= 6.59 \text{ in.}$$

Enter AISC *Manual* Table 3-18 with the required strength and Y2 = 6.59 in. to select a plastic neutral axis location for the W24×76 that provides sufficient available strength. Based on the available flexural strength provided in Table 3-18, the required PNA location for ASD and LRFD design methodologies differ. This discrepancy is due to the live-to-dead load ratio in this example, which is not equal to the ratio of 3 at which ASD and LRFD design methodologies produce equivalent results as discussed in AISC *Specification* Commentary Section B3.2.

Selecting PNA location 5 (BFL) with $\sum Q_n = 509 \text{ kips}$ provides a flexural strength of:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 1{,}240 \text{ kip-ft} > 1{,}220 \text{ kip-ft}$ **o.k.** | $\dfrac{M_n}{\Omega_b} = 823 \text{ kip-ft} < 864 \text{ kip-ft}$ **n.g.** |

The selected PNA location 5 is acceptable for LRFD design, but inadequate for ASD design. For ASD design, it can be shown that a W24×76 is adequate if a higher composite percentage of approximately 60% is employed. However, as discussed previously, this beam size is not adequate for construction loading and a larger section is necessary when designing utilizing ASD.

The actual value for the compression block depth, $a$, for the chosen PNA location is determined as follows:

---

# I-25

$$a = \frac{\sum Q_n}{0.85 f_c' b}$$
$$(Manual \text{ Eq. 3-7})$$

$$= \frac{509 \text{ kips}}{0.85(4 \text{ ksi})(7.50 \text{ ft})(12 \text{ in./ft})}$$

$$= 1.66 \text{ in.} < a_{trial} = 1.83 \text{ in.}$$ **o.k. for LRFD design**

**Method 2: Direct Calculation**

According to AISC *Specification* Commentary Section I3.2a, the number and strength of steel headed stud anchors will govern the compressive force, C, for a partially composite beam. The composite percentage is based on the minimum of the limit states of concrete crushing and steel yielding as follows:

1. Concrete crushing

   $A_c$ = Area of concrete slab within effective width. Assume that the deck profile is 50% void and 50% concrete fill.

   $$= b_{eff}\left(4\frac{1}{2} \text{ in.}\right) + (b_{eff}/2)(3 \text{ in.})$$

   $$= (7.50 \text{ ft})(12 \text{ in./ft})(4\frac{1}{2} \text{ in.}) + \left[\frac{(7.50 \text{ ft})(12 \text{ in./ft})}{2}\right](3 \text{ in.})$$

   $$= 540 \text{ in.}^2$$

   $$C = 0.85 f_c' A_c$$
   $$(\text{Spec. Comm. Eq. C-I3-7})$$

   $$= 0.85(4 \text{ ksi})(540 \text{ in.}^2)$$

   $$= 1{,}840 \text{ kips}$$

2. Steel yielding

   $$C = F_y A_s$$
   $$(\text{Spec. Comm. Eq. C-I3-6})$$

   $$= (50 \text{ ksi})(22.4 \text{ in.}^2)$$

   $$= 1{,}120 \text{ kips}$$

3. Shear transfer

   Fifty percent is used as a trial percentage of composite action as follows:

   $$C = \sum Q_n$$
   $$(\text{Spec. Comm. Eq. C-I3-8})$$

   $$= 50\%\left(\min\left\{\frac{1{,}840 \text{ kips}}{1{,}120 \text{ kips}}\right\}\right)$$

   $$= 560 \text{ kips to achieve 50\% composite action}$$

**Location of the Plastic Neutral Axis**

The plastic neutral axis (PNA) is located by determining the axis above and below which the sum of horizontal forces is equal. This concept is illustrated in Figure I.2-3, assuming the trial PNA location is within the top flange of the girder.

---

# I-26

$$\Sigma F_{above\ PNA} = \Sigma F_{below\ PNA}$$

$$C + xb_f F_y = (A_s - b_f x)F_y$$

Solving for $x$:

$$x = \frac{A_s F_y - C}{2b_f F_y}$$

$$= \frac{(22.4 \text{ in.}^2)(50 \text{ ksi}) - 560 \text{ kips}}{2(8.99 \text{ in.})(50 \text{ ksi})}$$

$$= 0.623 \text{ in.} < t_f = 0.680 \text{ in.}$$; therefore, the PNA is in the flange

Determine the nominal moment resistance of the composite section following the procedure in AISC *Specification* Commentary Section I3.2a, as illustrated in Figure C-I3.3.

$$a = \frac{C}{0.85 f_c' b}$$
$$(\text{Spec. Comm. Eq. C-I3-9})$$

$$= \frac{560 \text{ kips}}{0.85(4 \text{ ksi})(7.50 \text{ ft})(12 \text{ in./ft})}$$

$$= 1.83 \text{ in.} < 4.50 \text{ in.}$$ (above top of deck)

$$d_1 = t_{slab} - \frac{a}{2}$$

$$= 7.50 \text{ in.} - \frac{1.83 \text{ in.}}{2}$$

$$= 6.59 \text{ in.}$$

![Diagram showing plastic neutral axis location with PNA in top flange, showing compressive force C and dimensions d1=6.59", d2=0.312", d3=12.0", and forces xbfFy and (As-bfx)Fy]

*Fig. I.2-3. Plastic neutral axis location.*

---

# I-27

$$d_2 = \frac{x}{2}$$

$$= \frac{0.623 \text{ in.}}{2}$$

$$= 0.312 \text{ in.}$$

$$d_3 = \frac{d}{2}$$

$$= \frac{23.9 \text{ in.}}{2}$$

$$= 12.0 \text{ in.}$$

$$P_y = A_s F_y$$

$$= (22.4 \text{ in.}^2)(50 \text{ ksi})$$

$$= 1{,}120 \text{ kips}$$

$$M_n = C(d_1 + d_2) + P_y(d_3 - d_2)$$
$$(\text{Spec. Comm. Eq. C-I3-10})$$

$$= (560 \text{ kips})(6.59 \text{ in.} + 0.312 \text{ in.}) + (1{,}120 \text{ kips})(12.0 \text{ in.} - 0.312 \text{ in.})$$

$$= 17{,}000 \text{ kip-in. or } 1{,}420 \text{ kip-ft}$$

Note that Equation C-I3-10 is based on the summation of moments about the centroid of the compression force in the steel; however, the same answer may be obtained by summing moments about any arbitrary point.

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(1{,}420 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{1{,}420 \text{ kip-ft}}{1.67}$ |
| $= 1{,}280 \text{ kip-ft} > 1{,}220 \text{ kip-ft}$ **o.k.** | $= 850 \text{ kip-ft} < 864 \text{ kip-ft}$ **n.g.** |

As was determined previously using the *Manual* Tables, a W24×76 with 50% composite action is acceptable when LRFD methodology is employed, while for ASD design the beam is inadequate at this level of composite action.

Continue with the design using a W24×76 with 50% composite action.

**Steel Anchor Strength**

Steel headed stud anchor strengths are tabulated in AISC *Manual* Table 3-20 for typical conditions and may be calculated according to AISC *Specification* Section I8.2a as follows:

$$A_{sa} = \frac{\pi d_{sa}^2}{4}$$

$$= \frac{\pi(\frac{3}{4} \text{ in.})^2}{4}$$

$$= 0.442 \text{ in.}^2$$

$$f_c' = 4 \text{ ksi}$$

---

# I-28

$$E_c = w_c^{1.5}\sqrt{f_c'}$$

$$= \left(145 \text{ lb/ft}^3\right)^{1.5}\sqrt{4 \text{ ksi}}$$

$$= 3{,}490 \text{ ksi}$$

$R_g = 1.0$, stud anchors welded directly to the steel shape within the slab haunch

$R_p = 0.75$, stud anchors welded directly to the steel shape

$F_u = 65 \text{ ksi}$

$$Q_n = 0.5A_{sa}\sqrt{f_c' E_c} \leq R_g R_p A_{sa}F_u$$
$$(\text{Spec. Eq. I8-1})$$

$$= 0.5(0.442 \text{ in.}^2)\sqrt{(4 \text{ ksi})(3{,}490 \text{ ksi})} \leq (1.0)(0.75)(0.442 \text{ in.}^2)(65 \text{ ksi})$$

$$= 26.1 \text{ kips} > 21.5 \text{ kips}$$

Use $Q_n = 21.5 \text{ kips}$.

**Number and Spacing of Anchors**

According to AISC *Specification* Section I8.2c, the number of steel headed stud anchors required between any concentrated load and the nearest point of zero moment shall be sufficient to develop the maximum moment required at the concentrated load point.

From Figure I.2-2, the moment at the concentrated load points, $M_{r1}$ and $M_{r3}$, is approximately equal to the maximum beam moment, $M_{r2}$. The number of anchors between the beam ends and the point loads should therefore be adequate to develop the required compressive force associated with the maximum moment, C, previously determined to be 560 kips.

$$N_{anchors} = \frac{\sum Q_n}{Q_n}$$

$$= \frac{C}{Q_n}$$

$$= \frac{560 \text{ kips}}{21.5 \text{ kips/anchor}}$$

$$= 26 \text{ anchors from each end to concentrated load points}$$

In accordance with AISC *Specification* Section I8.2d, anchors between point loads should be spaced at a maximum of:

$8t_{slab} = 60.0 \text{ in.}$

or 36 in. **controls**

For beams with deck running parallel to the span such as the one under consideration, spacing of the stud anchors is independent of the flute spacing of the deck. Single anchors can therefore be spaced as needed along the beam length, provided a minimum longitudinal spacing of six anchor diameters in accordance with AISC *Specification* Section I8.2d is maintained. Anchors can also be placed in aligned or staggered pairs, provided a minimum transverse spacing of four stud diameters = 3 in. is maintained. For this design, it was chosen to use pairs of anchors along each end of the girder to meet strength requirements and single anchors along the center section of the girder to meet maximum spacing requirements as illustrated in Figure I.2-4.

---

# I-29

AISC *Specification* Section I8.2d requires that the distance from the center of an anchor to a free edge in the direction of the shear force be a minimum of 8 in. for normal weight concrete slabs. For simply supported composite beams, this provision could apply to the distance between the slab edge and the first anchor at each end of the beam. Assuming the slab edge is coincident to the centerline of support, Figure I.2-4 illustrates an acceptable distance of 9 in., though in this case the column flange would prevent breakout and negate the need for this check. The slab edge is often uniformly supported by a column flange or pier cap in typical composite construction, thus preventing the possibility of a concrete breakout failure and nullifying the edge distance requirement as discussed in AISC *Specification* Commentary Section I8.3.

For this example, the minimum number of headed stud anchors required to meet the maximum spacing limit previously calculated is used within the middle third of the span. AISC *Specification* Section I3.2c.1(d) requires that steel deck be anchored to all supporting members at a maximum spacing of 18 in. Additionally, *Standard for Composite Steel Floor Deck-Slabs*, ANSI/SDI C-2017 (SDI, 2017), requires deck attachment at an average of 16 in. but no more than 18 in.

From the previous discussion and Figure I.2-4, the total number of stud anchors used is equal to $(13)(2) + 3 + (13)(2) = 55$. A plan layout illustrating the final girder design is provided in Figure I.2-5.

![Plan view diagram showing steel headed stud anchor layout with columns, beams (W14x90), girder, and deck. Shows 13 anchor pairs at 9" spacing on each end, 3 single anchors in 4 equal spaces in middle, with 3" minimum clearance and total spacing layout marked]

*Fig. I.2-4. Steel headed stud anchor layout.*

![Plan layout showing final girder design with W21×50 c = 2" (46) beams and W24×76 c = ¾" (26) and (3) girders arranged in a grid pattern, with dimensions 3 @ 10'-0" = 30'-0" vertically and 45'-0" horizontally]

*Fig. I.2-5. Plan layout of final girder design.*

---

# I-30

**Steel Anchor Ductility Check**

As discussed in AISC *Specification* Commentary Section I3.2d.1, beams are not susceptible to connector failure due to insufficient deformation capacity if they meet one or more of the following conditions:

(1) Beams with span not exceeding 30 ft;
(2) Beams with a degree of composite action of at least 50%; or
(3) Beams with an average nominal shear connector capacity of at least 16 kips per foot along their span, corresponding to a ¾ in. diameter steel headed stud anchor placed at 12 in. spacing on average.

The span is 30 ft, which meets the 30 ft limit. The percent composite action is:

$$\frac{\sum Q_n}{\min\left\{0.85 f_c' A_c, F_y A_s\right\}} = \frac{560 \text{ kips}}{\min\left\{0.85(4 \text{ ksi})(540 \text{ in.}^2), (50 \text{ ksi})(22.4 \text{ in.}^2)\right\}}(100)$$

$$= \frac{560 \text{ kips}}{1{,}120 \text{ kips}}(100)$$

$$\equiv 50.0\%$$

which meets the minimum degree of composite action of 50%. The average shear connector capacity is:

$$\frac{(55 \text{ anchors})(21.5 \text{ kips/anchor})}{30 \text{ ft}} = 39.4 \text{ kip/ft}$$

which exceeds the minimum capacity of 16 kips per foot. Because at least one of the conditions has been met (in fact, all three have been met), the shear connectors meet the ductility requirements.

**Live Load Deflection Criteria**

Deflections due to live load applied after composite action has been achieved will be limited to $L/360$ under the design live load as required by Table 1604.3 of the *International Building Code* (IBC) (ICC, 2021), or 1 in. using a 50% reduction in design live load as recommended by AISC Design Guide 3.

Deflections for composite members may be determined using the lower bound moment of inertia provided in AISC *Specification* Commentary Equation C-I3-1 and tabulated in AISC *Manual* Table 3-19. The *Specification* Commentary also provides an alternate method for determining deflections through the calculation of an effective moment of inertia. Both methods are acceptable and are illustrated in the following calculations for comparison purposes:

Method 1: Calculation of the lower bound moment of inertia, $I_{LB}$

$$I_{LB} = I_x + A_s(Y_{ENA} - d_3)^2 + \left(\frac{\sum Q_n}{F_y}\right)(2d_3 + d_1 - Y_{ENA})^2$$
$$({\text{from } Spec. \text{ Comm. Eq. C-I3-1}})$$

Variables $d_1$ and $d_3$ in AISC *Specification* Commentary Equation C-I3-1 are determined using the same procedure previously illustrated for calculating nominal flexural resistance. However, for the determination of $I_{LB}$, the nominal strength of steel anchors is calculated between the point of maximum positive moment and the point of zero moment as opposed to between the concentrated load and point of zero moment previously. The maximum moment is located at the center of the span, and it can be seen from Figure I.2-4 that 27 anchors are located between the midpoint of the beam and each end.

$$\Sigma Q_n = (27 \text{ anchors})(21.5 \text{ kips/anchor})$$

$$= 581 \text{ kips}$$

---

# I-31

$$a = \frac{C}{0.85 f_c' b}$$
$$(\text{Spec. Eq. C-I3-9})$$

$$= \frac{\sum Q_n}{0.85 f_c' b}$$

$$= \frac{581 \text{ kips}}{0.85(4 \text{ ksi})(7.50 \text{ ft})(12 \text{ in./ft})}$$

$$= 1.90 \text{ in.}$$

$$d_1 = t_{slab} - \frac{a}{2}$$

$$= 7.50 \text{ in.} - \frac{1.90 \text{ in.}}{2}$$

$$= 6.55 \text{ in.}$$

$$x = \frac{A_s F_y - \sum Q_n}{2b_f F_y}$$

$$= \frac{(22.4 \text{ in.}^2)(50 \text{ ksi}) - 581 \text{ kips}}{2(8.99 \text{ in.})(50 \text{ ksi})}$$

$$= 0.600 \text{ in.} < t_f = 0.680 \text{ in.}$$; therefore, the PNA is within the flange

$$d_3 = \frac{d}{2}$$

$$= \frac{23.9 \text{ in.}}{2}$$

$$= 12.0 \text{ in.}$$

The distance from the top of the steel section to the elastic neutral axis, $Y_{ENA}$, for use in Equation C-I3-1 is calculated using the procedure provided in AISC *Specification* Commentary Section I3.2 as follows:

$$Y_{ENA} = \frac{A_s d_3 + \left(\dfrac{\sum Q_n}{F_y}\right)(2d_3 + d_1)}{A_s + \left(\dfrac{\sum Q_n}{F_y}\right)}$$
$$(\text{Spec. Comm. Eq. C-I3-2})$$

$$= \frac{(22.4 \text{ in.}^2)(12.0 \text{ in.}) + \left(\dfrac{581 \text{ kips}}{50 \text{ ksi}}\right)\left[2(12.0 \text{ in.}) + 6.55 \text{ in.}\right]}{22.4 \text{ in.}^2 + \left(\dfrac{581 \text{ kips}}{50 \text{ ksi}}\right)}$$

$$= 18.3 \text{ in.}$$

Substituting these values into AISC *Specification* Commentary Equation C-I3-1 yields the following lower bound moment of inertia:

$$I_{LB} = 2{,}100 \text{ in.}^4 + (22.4 \text{ in.}^2)(18.3 \text{ in.} - 12.0 \text{ in.})^2 + \left(\frac{581 \text{ kips}}{50 \text{ ksi}}\right)\left[2(12.0 \text{ in.}) + 6.55 \text{ in.} - 18.3 \text{ in.}\right]^2$$

$$= 4{,}730 \text{ in.}^4$$

Alternately, this value can be determined directly from AISC *Manual* Table 3-19 as illustrated in Design Example I.1.

---

# I-32

Method 2: Calculation of the equivalent moment of inertia, $I_{equiv}$

An alternate procedure for determining a moment of inertia for the deflection calculation of the composite section is presented in AISC *Specification* Commentary Section I3.2 and in the following:

Determine the transformed moment of inertia, $I_{tr}$

The effective width of the concrete below the top of the deck may be approximated with the deck profile resulting in a 50% effective width as depicted in Figure I.2-6. The effective width, $b_{eff} = (7.50 \text{ ft})(12 \text{ in./ft}) = 90.0 \text{ in.}$

Transformed slab widths are calculated as follows:

$$n = \frac{E_s}{E_c}$$

$$= \frac{29{,}000 \text{ ksi}}{3{,}490 \text{ ksi}}$$

$$= 8.31$$

$$b_{tr1} = \frac{b_{eff}}{n}$$

$$= \frac{90.0 \text{ in.}}{8.31}$$

$$= 10.8 \text{ in.}$$

$$b_{tr2} = \frac{0.5b_{eff}}{n}$$

$$= \frac{0.5(90.0 \text{ in.})}{8.31}$$

$$= 5.42 \text{ in.}$$

![Diagram showing effective concrete width with dimensions: beff = 90.0", 0.5beff = 45.0", heights of 4½" and 3", and areas A1 and A2 marked on an I-beam cross-section]

*Fig. I.2-6. Effective concrete width.*

---

# I-33

The transformed model is illustrated in Figure I.2-7.

Determine the elastic neutral axis of the transformed section (assuming fully composite action) and calculate the transformed moment of inertia using the information provided in Table I.2-1 and Figure I.2-7. For this problem, a trial location for the elastic neutral axis (ENA) is assumed to be within the depth of the composite deck.

$\Sigma A_i$ about elastic neutral axis = 0

$$\left(48.6 \text{ in.}^2\right)(2.25 \text{ in.} + x) + (5.42 \text{ in.}^2)\left(\frac{x^2}{2}\right) + (22.4 \text{ in.}^2)(x - 15.0 \text{ in.}) = 0$$

Solving for $x$:

$$x = 2.88 \text{ in.}$$

Verify trial location:

$$2.88 \text{ in.} < h_r = 3 \text{ in.}$$; therefore, the elastic neutral axis is within the composite deck.

Utilizing the parallel axis theorem and substituting for $x$ yields:

$$I_{tr} = \Sigma I + \Sigma A y^2$$

$$= 82.0 \text{ in.}^4 + (0.452 \text{ in.}^2)(2.88 \text{ in.})^3 + 2{,}100 \text{ in.}^4 + (48.6 \text{ in.}^2)(2.25 \text{ in.} + 2.88 \text{ in.})^2 + (15.6 \text{ in.}^2)\left(\frac{2.88 \text{ in.}}{2}\right)^2$$

$$+ (22.4 \text{ in.}^2)(2.88 \text{ in.} - 15.0 \text{ in.})^2$$

$$= 6{,}790 \text{ in.}^4$$

Determine the equivalent moment of inertia, $I_{equiv}$

$$\Sigma Q_n = 581 \text{ kips (previously determined in Method 1)}$$

![Diagram showing transformed area model with dimensions: btr1 = 10.8", btr2 = 5.42", heights of 4½" and 3", elastic neutral axis (ENA) marked with +y direction, and areas A1 and A2 on an I-beam cross-section]

*Fig. I.2-7. Transformed area model.*

---

# I-34

<table>
<caption>Table I.2-1. Properties for Elastic Neutral Axis Determination of Transformed Section</caption>
<thead>
<tr>
<th>Part</th>
<th>A<sub>i</sub><br/>in.<sup>2</sup></th>
<th>y<sub>i</sub><br/>in.</th>
<th>I<sub>i</sub><br/>in.<sup>4</sup></th>
</tr>
</thead>
<tbody>
<tr>
<td>A<sub>1</sub></td>
<td>48.6</td>
<td>2.25 + x</td>
<td>82.0</td>
</tr>
<tr>
<td>A<sub>2</sub></td>
<td>5.42x</td>
<td>x/2</td>
<td>0.452x<sup>3</sup></td>
</tr>
<tr>
<td>W24×76</td>
<td>22.4</td>
<td>x − 15.0</td>
<td>2,100</td>
</tr>
</tbody>
</table>

$C_f$ = compression force for fully composite beam previously determined to be controlled by $A_s F_y$
    = 1,120 kips

$$I_{equiv} = I_x + \sqrt{(\Sigma Q_n/C_f)(I_{tr} - I_x)}$$
$$(\text{Spec. Comm. Eq. C-I3-3})$$

$$= 2{,}100 \text{ in.}^4 + \sqrt{(581 \text{ kips}/1{,}120 \text{ kips})(6{,}790 \text{ in.}^4 - 2{,}100 \text{ in.}^4)}$$

$$= 5{,}480 \text{ in.}^4$$

**Comparison of Methods and Final Deflection Calculation**

$I_{LB}$ was determined to be 4,730 in.<sup>4</sup> and $I_{equiv}$ was determined to be 5,480 in.<sup>4</sup> $I_{LB}$ will be used for the remainder of this example.

From AISC *Manual* Table 3-22, Case 9:

$$\Delta_{LL} = \frac{23P_L L^3}{648EI_{LB}}$$

$$= \frac{23(45.0 \text{ kips})\left[(30 \text{ ft})(12 \text{ in./ft})\right]^3}{648(29{,}000 \text{ ksi})(4{,}730 \text{ in.}^4)}$$

$$= 0.543 \text{ in.} < 1 \text{ in. (for AISC Design Guide 3 limit)}$$ **o.k.**

(50% reduction in design live load as allowed by Design Guide 3 was not necessary to meet this limit)

$$\approx L/663 < L/360$$ (for IBC 2021 Table 1604.3 limit) **o.k.**

**Available Shear Strength**

According to AISC *Specification* Section I4.3, the girder should be assessed for available shear strength as a bare steel beam using the provisions of Chapter G.

Applying the loads previously determined for the governing load combination of ASCE/SEI 7 and obtaining available shear strengths from AISC *Manual* Table 3-2 for a W24×76 yields the following:

| LRFD | ASD |
|------|-----|
| $V_u = 121 \text{ kips} + (0.0912 \text{ kip/ft})\left(\dfrac{30 \text{ ft}}{2}\right)$ | $V_a = 85.5 \text{ kips} + (0.0760 \text{ kip/ft})\left(\dfrac{30 \text{ ft}}{2}\right)$ |
| $= 122 \text{ kips}$ | $= 86.6 \text{ kips}$ |
| $\phi_v V_n = 315 \text{ kips} > 122 \text{ kips}$ **o.k.** | $\dfrac{V_n}{\Omega_v} = 210 \text{ kips} > 86.6 \text{ kips}$ **o.k.** |

---

# I-35

**Serviceability**

Depending on the intended use of this bay, vibrations might need to be considered. See AISC Design Guide 11 (Murray et al., 2016) for additional information.

It has been observed that cracking of composite slabs can occur over girder lines. The addition of top reinforcing steel transverse to the girder span will aid in mitigating this effect.

**Summary**

Using LRFD design methodology, it has been determined that a W24×76 with $\frac{3}{4}$ in. of camber and 55, $\frac{3}{4}$-in.-diameter by $4\frac{5}{8}$-in.-long steel headed stud anchors as depicted in Figure I.2-4, is adequate for the imposed loads and deflection criteria. Using ASD design methodology, a W24×84 with a steel headed stud anchor layout determined using a procedure analogous to the one demonstrated in this example would be required.

---

# I-36

# EXAMPLE I.3 FILLED COMPOSITE MEMBER FORCE ALLOCATION AND LOAD TRANSFER

## Given:

Refer to Figure I.3-1.

**Part I:** For each loading condition (a) through (c) determine the required longitudinal shear force, $V_r'$, to be transferred between the steel section and concrete fill.

**Part II:** For loading condition (a), investigate the force transfer mechanisms of direct bearing, shear connection, and direct bond interaction.

The composite member consists of an ASTM A500/A500M, Grade C, HSS with normal weight (145 lb/ft³) concrete fill having a specified concrete compressive strength, $f_c' = 5$ ksi. Use ASTM A572/A572M Grade 50 material for the bearing plate.

Applied loading, $P_r$, for each condition illustrated in Figure I.3-1 is composed of the following nominal loads:

$P_D = 32$ kips
$P_L = 84$ kips

![Diagram showing HSS10×6×⅜ section with B = 6", H = 10", and three loading conditions:
(a) External force to steel only
(b) External force to concrete only
(c) External force to both materials concurrently with rigid cap plate
All sections show PT applied vertically downward to different components]

*Fig. I.3-1. Filled composite member in compression.*

---

# I-37

## Solution:

## Part I—Force Allocation

From AISC *Manual* Table 2-4, the material properties are as follows:

ASTM A500/A500M Grade C
$F_y = 50$ ksi

From AISC *Manual* Table 1-11 and Figure I.3-1, the geometric properties are as follows:

HSS10×6×⅜
$A_s = 10.4$ in.²
$H = 10.0$ in.
$B = 6.00$ in.
$t_{nom} = \frac{3}{8}$ in. (nominal wall thickness)
$t = 0.349$ in. (design wall thickness in accordance with AISC *Specification* Section B4.2)
$h/t = 25.7$
$b/t = 14.2$

Calculate the concrete area using geometry compatible with that used in the calculation of the steel area in AISC *Manual* Table 1-11 (taking into account the design wall thickness and an outside corner radii of two times the design wall thickness in accordance with AISC *Manual* Part 1), as follows:

$h_i = H - 2t$
$= 10.0$ in. $- 2(0.349$ in.$)$
$= 9.30$ in.

$b_i = B - 2t$
$= 6.00$ in. $- 2(0.349$ in.$)$
$= 5.30$ in.

$A_c = b_i h_i - t^2(4 - \pi)$
$= (5.30 \text{ in.})(9.30 \text{ in.}) - (0.349 \text{ in.})^2(4 - \pi)$
$= 49.2$ in.²

From ASCE/SEI 7, Chapter 2, the required compressive strength is:

| LRFD | ASD |
|------|-----|
| $P_r = P_u$ | $P_r = P_a$ |
| $= 1.2(32 \text{ kips}) + 1.6(84 \text{ kips})$ | $= 32 \text{ kips} + 84 \text{ kips}$ |
| $= 173$ kips | $= 116$ kips |

**Composite Section Strength for Force Allocation**

In order to determine the composite section strength for force allocation, the member is first classified as compact, noncompact, or slender in accordance with AISC *Specification* Table I1.1a.

**Governing Width-to-Thickness Ratio**

---

# I-38

$$\lambda = \frac{h}{t}$$
$$= 25.7$$

The limiting width-to-thickness ratio for a compact compression steel element in a composite member subject to axial compression is:

$$\lambda_p = 2.26\sqrt{\frac{E}{F_y}}$$
$$(Spec. \text{ Table I1.1a})$$

$$= 2.26\sqrt{\frac{29{,}000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 54.4 > 25.7$$; therefore the HSS wall is compact

The nominal axial compressive strength without consideration of length effects, $P_{no}$, used for force allocation calculations is therefore determined as:

$$P_{no} = P_p$$
$$(Spec. \text{ Eq. I2-9a})$$

$$P_p = F_y A_s + C_2 f_c'\left(A_c + A_{sr}\frac{E_s}{E_c}\right)$$
$$(Spec. \text{ Eq. I2-9b})$$

where
$C_2 = 0.85$ for rectangular sections
$A_{sr} = 0$ in.² when no reinforcing steel is present within the HSS

$$P_{no} = F_y A_s + C_2 f_c'\left(A_c + A_{sr}\frac{E_s}{E_c}\right)$$

$$= (50 \text{ ksi})(10.4 \text{ in.}^2) + 0.85(5 \text{ ksi})(49.2 \text{ in.}^2 + 0 \text{ in.}^2)$$

$$= 729 \text{ kips}$$

**Transfer Force for Condition (a)**

Refer to Figure I.3-1(a). For this condition, the entire external force is applied to the steel section only, and the provisions of AISC *Specification* Section I6.2a apply.

$$V_r' = P_r\left(1 - \frac{F_y A_s}{P_{no}}\right)$$
$$(Spec. \text{ Eq. I6-1})$$

$$= P_r\left[1 - \frac{(50 \text{ ksi})(10.4 \text{ in.}^2)}{729 \text{ kips}}\right]$$

$$= 0.287P_r$$

| LRFD | ASD |
|------|-----|
| $V_r' = 0.287(173 \text{ kips})$ | $V_r' = 0.287(116 \text{ kips})$ |
| $= 49.7$ kips | $= 33.3$ kips |

---

# I-39

**Transfer Force for Condition (b)**

Refer to Figure I.3-1(b). For this condition, the entire external force is applied to the concrete fill only, and the provisions of AISC *Specification* Section I6.2b apply.

$$V_r' = P_r\left(\frac{F_y A_s}{P_{no}}\right)$$
$$(Spec. \text{ Eq. I6-2a})$$

$$= P_r\left[\frac{(50 \text{ ksi})(10.4 \text{ in.}^2)}{729 \text{ kips}}\right]$$

$$= 0.713P_r$$

| LRFD | ASD |
|------|-----|
| $V_r' = 0.713(173 \text{ kips})$ | $V_r' = 0.713(116 \text{ kips})$ |
| $= 123$ kips | $= 82.7$ kips |

**Transfer Force for Condition (c)**

Refer to Figure I.3-1(c). For this condition, external force is applied to the steel section and concrete fill concurrently, and the provisions of AISC *Specification* Section I6.2c apply.

AISC *Specification* Commentary Section I6.2 states that when loads are applied to both the steel section and concrete fill concurrently, $V_r'$ can be taken as the difference in magnitudes between the portion of the external force applied directly to the steel section and that required by Equation I6-2a and b. Using the plastic distribution approach employed in AISC *Specification* Equations I6-1 and I6-2a, this concept can be written in equation form as follows:

$$V_r' = \left|P_{rs} - P_r\left(\frac{A_s F_y}{P_{no}}\right)\right|$$
$$(Eq. 1)$$

where
$P_{rs}$ = portion of external force applied directly to the steel section, kips

Note that this example assumes the external force imparts compression on the composite element as illustrated in Figure I.3-1. If the external force would impart tension on the composite element, consult the AISC *Specification* Commentary for discussion.

Currently the *Specification* provides no specific requirements for determining the distribution of the applied force for the determination of $P_{rs}$, so it is left to engineering judgment. For a bearing plate condition such as the one represented in Figure I.3-1(c), one possible method for determining the distribution of applied forces is to use an elastic distribution based on the material axial stiffness ratios as follows:

$$E_c = w_c^{1.5}\sqrt{f_c'}$$

$$= (145 \text{ lb/ft}^3)^{1.5}\sqrt{5 \text{ ksi}}$$

$$= 3{,}900 \text{ ksi}$$

---

# I-40

$$P_{rs} = \left(\frac{E_s A_s}{E_s A_s + E_c A_c}\right)P_r$$

$$= \left[\frac{(29{,}000 \text{ ksi})(10.4 \text{ in.}^2)}{(29{,}000 \text{ ksi})(10.4 \text{ in.}^2) + (3{,}900 \text{ ksi})(49.2 \text{ in.}^2)}\right]P_r$$

$$= 0.611P_r$$

Substituting the results into Equation 1 yields:

$$V_r' = \left|0.611P_r - P_r\left(\frac{A_s F_y}{P_{no}}\right)\right|$$

$$= \left|0.611P_r - P_r\left[\frac{(10.4 \text{ in.}^2)(50 \text{ ksi})}{729 \text{ kips}}\right]\right|$$

$$= 0.102P_r$$

| LRFD | ASD |
|------|-----|
| $V_r' = 0.102(173 \text{ kips})$ | $V_r' = 0.102(116 \text{ kips})$ |
| $= 17.6$ kips | $= 11.8$ kips |

An alternate approach would be the use of a plastic distribution method whereby the load is partitioned to each material in accordance with their contribution to composite section strength given in Equation I2-9b. This method eliminates the need for longitudinal shear transfer, provided the local bearing strength of the concrete and steel are adequate to resist the forces resulting from this distribution.

**Additional Discussion**

• The design and detailing of the connections required to deliver external forces to the composite member should be performed according to the applicable provisions of AISC *Specification* Chapters J and K. Note that for checking bearing strength on concrete confined by a steel HSS or box member, the $\sqrt{A_2/A_1}$ term in Equation J8-2 may be taken as 2.0 according to the User Note in *Specification* Section I6.2.

• The connection cases illustrated by Figure I.3-1 are idealized conditions representative of the mechanics of actual connections. For instance, a standard shear connection welded to the face of an HSS column is an example of a condition where all external force is applied directly to the steel section only. Note that the connection configuration can also impact the strength of the force transfer mechanism as illustrated in Part II of this example.

## Solution:

## Part II—Load Transfer

The required longitudinal force to be transferred, $V_r'$, determined in Part I condition (a) will be used to investigate the three applicable force transfer mechanisms of AISC *Specification* Section I6.3: direct bearing, shear connection, and direct bond interaction. As indicated in the *Specification*, these force transfer mechanisms may not be superimposed; however, the mechanism providing the greatest nominal strength may be used.

---

# I-41

**Direct Bearing**

**Trial Layout of Bearing Plate**

For investigating the direct bearing load transfer mechanism, the external force is delivered directly to the HSS section by standard steel connections on each end member illustrated in Figure I.3-2. One method for utilizing direct bearing in this instance is through the use of an internal bearing plate. Given the small clearance within the HSS section under consideration, internal access for welding is limited to the open ends of the HSS; therefore, the HSS section will be spliced at the bearing plate location. Additionally, it is a practical consideration that no more than 50% of the internal width of the HSS section be obstructed by the bearing plate in order to facilitate concrete placement. It is essential that concrete mix proportions and installation of concrete fill produce a bearing plate that projects above and below the projecting plate. Based on these considerations, the trial bearing plate layout depicted in Figure I.3-2 was selected using an internal plate protrusion, $L_p$, of 1.0 in.

**Location of Bearing Plate**

The bearing plate is placed within the load introduction length discussed in AISC *Specification* Section I6.4b. The load introduction length is defined as two times the minimum transverse dimension of the HSS both above and below the load transfer region. The load transfer region is defined in *Specification* Commentary Section I6.4 as the depth of the connection. For the configuration under consideration, the bearing plate should be located within $2(B = 6$ in.$) = 12$ in. of the bottom of the shear connection. From Figure I.3-2, the location of the bearing plate is 6 in. from the bottom of the shear connection and is therefore adequate.

**Available Strength for the Limit State of Direct Bearing**

The contact area between the bearing plate and concrete, $A_1$, may be determined as follows:

$$A_1 = A_c - (b_i - 2L_p)(h_i - 2L_p)$$
$$(Eq. 2)$$

where
$L_p$ = typical protrusion of bearing plate inside HSS
$= 1.0$ in.

![Diagram showing internal bearing plate configuration with HSS10×6×⅜, including top/concrete interface, bearing plate labeled D-D, and cross-section view showing concrete fill, bearing plate with typical 4-sided protrusion Lp, dimensions bi and hi]

*Fig. I.3-2. Internal bearing plate configuration.*

---

# I-42

Substituting for the appropriate geometric properties previously determined in Part I into Equation 2 yields:

$$A_1 = 49.2 \text{ in.}^2 - [5.30 \text{ in.} - 2(1.0 \text{ in.})][9.30 \text{ in.} - 2(1.0 \text{ in.})]$$

$$= 25.1 \text{ in.}^2$$

The available strength for the direct bearing force transfer mechanism is:

$$R_n = 1.7 f_c' A_1$$
$$(Spec. \text{ Eq. I6-3})$$

$$= 1.7(5 \text{ ksi})(25.1 \text{ in.}^2)$$

$$= 213 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.65$ | $\Omega_b = 2.31$ |
| $\phi_b R_n = 0.65(213 \text{ kips})$ | $\dfrac{R_n}{\Omega_b} = \dfrac{213 \text{ kips}}{2.31}$ |
| $= 138 \text{ kips} > V_r' = 49.7 \text{ kips} \quad \textbf{o.k.}$ | $= 92.2 \text{ kips} > V_r' = 33.3 \text{ kips} \quad \textbf{o.k.}$ |

**Required Thickness of Internal Bearing Plate**

There are several methods available for determining the bearing plate thickness. For round HSS sections with circular bearing plate openings, a closed-form elastic solution such as those found in *Roark's Formulas for Stress and Strain* (Young and Budynas, 2002) may be used. Alternately, the use of computational methods such as finite element analysis may be employed.

For this example, yield line theory can be employed to determine a plastic collapse mechanism of the plate. In this case, the walls of the HSS lack sufficient stiffness and strength to develop plastic hinges at the perimeter of the bearing plate. Utilizing only the plate material located within the HSS walls, and ignoring the HSS corner radii, the yield line pattern is as depicted in Figure I.3-3.

![Diagram showing yield line pattern with dimensions bi and hi marked, Lp (typ. 4 sides) labeled, an open section, and yield line (typ.) indicated]

*Fig. I.3-3. Yield line pattern.*

---

# I-43

Utilizing the results of the yield line analysis with $F_y = 50$ ksi plate material, the plate thickness may be determined as follows:

| LRFD | ASD |
|------|------|
| $\phi = 0.90$ | $\Omega = 1.67$ |
| $t_p = \sqrt{\frac{w_u}{2\phi F_y}\left[L_p(b_i + h_i) - \frac{8L_p^2}{3}\right]}$ | $t_p = \sqrt{\frac{\Omega w_a}{2F_y}\left[L_p(b_i + h_i) - \frac{8L_p^2}{3}\right]}$ |
| where | where |
| $w_u$ = bearing pressure on plate determined using LRFD load combinations | $w_a$ = bearing pressure on plate determined using ASD load combinations |
| $= \dfrac{V_r'}{A_1}$ | $= \dfrac{V_r'}{A_1}$ |
| $= \dfrac{49.7 \text{ kips}}{25.1 \text{ in.}^2}$ | $= \dfrac{33.3 \text{ kips}}{25.1 \text{ in.}^2}$ |
| $= 1.98$ ksi | $= 1.33$ ksi |
| $t_p = \sqrt{\frac{1.98 \text{ ksi}}{2(0.90)(50 \text{ ksi})}\left[\times(1.0 \text{ in.})(5.30 \text{ in.} + 9.30 \text{ in.}) - \frac{8(1.0 \text{ in.})^2}{3}\right]}$ | $t_p = \sqrt{\frac{(1.67)(1.33 \text{ ksi})}{2(50 \text{ ksi})}\left[\times(1.0 \text{ in.})(5.30 \text{ in.} + 9.30 \text{ in.}) - \frac{8(1.0 \text{ in.})^2}{3}\right]}$ |
| $= 0.512$ in. | $= 0.515$ in. |

Thus, select a ⅝-in.-thick bearing plate.

**Splice Weld**

The HSS is in compression due to the imposed loads, therefore the splice weld indicated in Figure I.3-2 is sized according to the minimum weld size requirements of Chapter J. Should net section uplift or flexure be applied in other loading conditions, the splice should be designed to resist these forces using the applicable provisions of AISC *Specification* Chapters J and K.

**Shear Connection**

Shear connection involves the use of steel headed stud or channel anchors placed within the HSS section to transfer the required longitudinal shear force. Use of the shear connection mechanism for force transfer in filled HSS is usually limited to large HSS sections and built-up box shapes, and is not practical for the composite member in question. Consultation with the fabricators regarding their specific capabilities is recommended to determine the feasibility of shear connection for HSS and box members. Should shear connection be a feasible load transfer mechanism, AISC *Specification* Section I6.3b in conjunction with the steel anchors in composite component provisions of Section I8.3 apply.

**Direct Bond Interaction**

The use of direct bond interaction for load transfer is limited to filled HSS and depends upon the location of the load transfer point within the length of the member being considered (end or interior) as well as the number of faces to which load is being transferred.

---

# I-44

From AISC *Specification* Section I6.3c, the nominal bond strength for a rectangular section is:

$$R_n = p_b L_{in} F_{in}$$
$$(Spec. \text{ Eq. I6-5})$$

where
$p_b$ = perimeter of the steel-concrete bond interface within the composite cross section, in.

$$= (2)(10.0 \text{ in.} + 6.00 \text{ in.}) - (8)[(2)(0.349 \text{ in.})] + (4)\left[\frac{\pi(0.349 \text{ in.})}{2}\right]$$

$$= 28.6 \text{ in.}$$

$L_{in}$ = load introduction length, determined in accordance with AISC *Specification* Section I6.4

$$= 2[\min\{B, H\}]$$

$$= 2(6.00 \text{ in.})$$

$$= 12.0 \text{ in.}$$

$$F_{in} = \frac{12t}{H^2} \leq 0.1, \text{ ksi (for a rectangular cross section)}$$

$$= \frac{12(0.349 \text{ in.})}{(10.0 \text{ in.})^2} \leq 0.1 \text{ ksi}$$

$$= 0.0419 \text{ ksi}$$

For the design of this load transfer mechanism, two possible cases will be considered:

Case 1: End Condition—Load Transferred to Member from Four Sides Simultaneously

For this case the member is loaded at an end condition (the composite member only extends to one side of the point of force transfer). Force is applied to all four sides of the section simultaneously thus allowing the full perimeter of the section to be mobilized for bond strength.

From AISC *Specification* Equation I6-5:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.50$ | $\Omega_b = 3.00$ |
| $\phi_b R_n = \phi_b p_b L_{in} F_{in}$ | $\dfrac{R_n}{\Omega_b} = \dfrac{p_b L_{in} F_{in}}{\Omega_b}$ |
| $= 0.50(28.6 \text{ in.})(12.0 \text{ in.})(0.0419 \text{ ksi})$ | $= \dfrac{(28.6 \text{ in.})(12.0 \text{ in.})(0.0419 \text{ ksi})}{3.00}$ |
| $= 7.19 \text{ kips} < V_r' = 49.7 \text{ kips} \quad \textbf{n.g.}$ | $= 4.79 \text{ kips} < V_r' = 33.3 \text{ kips} \quad \textbf{n.g.}$ |

Bond strength is inadequate and another force transfer mechanism such as direct bearing must be used to meet the load transfer provisions of AISC *Specification* Section I6.

Alternately, the detail could be revised so that the external force is applied to both the steel section and concrete fill concurrently as schematically illustrated in Figure I.3-1(c). Comparing bond strength to the load transfer requirements for concurrent loading determined in Part I of this example yields:

---

# I-45

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.50$ | $\Omega_b = 3.00$ |
| $\phi_b R_n = 7.19 \text{ kips} < V_r' = 17.6 \text{ kips} \quad \textbf{n.g.}$ | $\dfrac{R_n}{\Omega_b} = 4.79 \text{ kips} < V_r' = 11.8 \text{ kips} \quad \textbf{n.g.}$ |

Bond strength remains inadequate and another force transfer mechanism such as direct bearing must be used to meet the load transfer provisions of AISC *Specification* Section I6.

Case 2: Interior Condition—Load Transferred to Three Faces

For this case the composite member is loaded from three sides away from the end of the member (the composite member extends to both sides of the point of load transfer) as indicated in Figure I.3-4.

Longitudinal shear forces to be transferred at each face of the HSS are calculated using the relationship to external forces determined in Part I of this example for condition (a) shown in Figure I.3-1, and the applicable ASCE/SEI 7 load combinations as follows:

| LRFD | ASD |
|------|-----|
| Face 1: | Face 1: |
| $P_{r1} = P_u$ | $P_{r1} = P_a$ |
| $= 1.2(2 \text{ kips}) + 1.6(6 \text{ kips})$ | $= 2 \text{ kips} + 6 \text{ kips}$ |
| $= 12.0$ kips | $= 8.00$ kips |
| $V_{r1}' = 0.287P_{r1}$ | $V_{r1}' = 0.287P_{r1}$ |
| $= 0.287(12.0 \text{ kips})$ | $= 0.287(8.00 \text{ kips})$ |
| $= 3.44$ kips | $= 2.30$ kips |

![Diagram showing HSS10×6×⅜ member with load transfer from three faces. Left view shows elevation with E markers. Right view shows Section E-E with Face 1 (PD = 2 kips, PL = 6 kips), Face 2 (PD = 15 kips, PL = 39 kips), and Face 3 (PD = 15 kips, PL = 39 kips)]

*Fig. I.3-4. Case 2 load transfer.*

---

# I-46

| LRFD | ASD |
|------|-----|
| Faces 2 and 3: | Faces 2 and 3: |
| $P_{r2-3} = P_u$ | $P_{r2-3} = P_a$ |
| $= 1.2(15 \text{ kips}) + 1.6(39 \text{ kips})$ | $= 15 \text{ kips} + 39 \text{ kips}$ |
| $= 80.4$ kips | $= 54.0$ kips |
| $V_{r2-3}' = 0.287P_{r2-3}$ | $V_{r2-3}' = 0.287P_{r2-3}$ |
| $= 0.287(80.4 \text{ kips})$ | $= 0.287(54.0 \text{ kips})$ |
| $= 23.1$ kips | $= 15.5$ kips |

Load transfer at each face of the section is checked separately for the longitudinal shear at that face using Equation I6-5 as follows:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.50$ | $\Omega_b = 3.00$ |
| Face 1: | Face 1: |
| $p_b = 6.00 \text{ in.} - (2 \text{ corners})(2)(0.349 \text{ in.})$ | $p_b = 6.00 \text{ in.} - (2 \text{ corners})(2)(0.349 \text{ in.})$ |
| $= 4.60$ in. | $= 4.60$ in. |
| $\phi_b R_{n1} = 0.50(4.60 \text{ in.})(12.0 \text{ in.})(0.0419 \text{ ksi})$ | $\dfrac{R_{n1}}{\Omega_b} = \dfrac{(4.60 \text{ in.})(12.0 \text{ in.})(0.0419 \text{ ksi})}{3.00}$ |
| $= 1.16 \text{ kips} < V_{r1}' = 3.44 \text{ kips} \quad \textbf{n.g.}$ | $= 0.771 \text{ kip} < V_{r1}' = 2.30 \text{ kips} \quad \textbf{n.g.}$ |
| Faces 2 and 3: | Faces 2 and 3: |
| $p_b = 10.0 \text{ in.} - (2 \text{ corners})(2)(0.349 \text{ in.})$ | $p_b = 10.0 \text{ in.} - (2 \text{ corners})(2)(0.349 \text{ in.})$ |
| $= 8.60$ in. | $= 8.60$ in. |
| $\phi_b R_{n2-3} = 0.50(8.60 \text{ in.})(12.0 \text{ in.})(0.0419 \text{ ksi})$ | $\dfrac{R_{n2-3}}{\Omega_b} = \dfrac{(8.60 \text{ in.})(12.0 \text{ in.})(0.0419 \text{ ksi})}{3.00}$ |
| $= 2.16 \text{ kips} < V_{r2-3}' = 23.1 \text{ kips} \quad \textbf{n.g.}$ | $= 1.44 \text{ kips} < V_{r2-3}' = 15.5 \text{ kips} \quad \textbf{n.g.}$ |

The calculations indicate that the bond strength is inadequate for all faces, thus an alternate means of load transfer such as the use of internal bearing plates as demonstrated previously in this example is necessary.

As demonstrated by this example, direct bond interaction provides limited available strength for transfer of longitudinal shears and is generally only acceptable for lightly loaded columns or columns with low shear transfer requirements, such as those with loads applied to both concrete fill and steel encasement simultaneously.

---

# I-47

# EXAMPLE I.4 FILLED COMPOSITE MEMBER IN AXIAL COMPRESSION

## Given:

Determine if the filled composite member illustrated in Figure I.4-1 is adequate for the indicated dead and live loads. Table 4-B in Volume 2 of this document will be used in this example.

The composite member consists of an ASTM A500/A500M Grade C HSS with normal weight (145 lb/ft³) concrete fill having a specified concrete compressive strength, $f_c' = 5$ ksi.

![Diagram showing filled composite member with HSS10×6×⅜ section (B = 6", H = 10") with x-x and y-y axes marked. Elevation view shows L = 14'-0" column height with PD = 32 kips and PL = 84 kips applied at top, and pinned base support at bottom]

*Fig. I.4-1. Filled composite member section and applied loading.*

## Solution:

From AISC *Manual* Table 2-4, the material properties are:

ASTM A500/A500M Grade C
$F_y = 50$ ksi

From ASCE/SEI 7, Chapter 2, the required compressive strength is:

| LRFD | ASD |
|------|-----|
| $P_r = P_u$ | $P_r = P_a$ |
| $= 1.2(32 \text{ kips}) + 1.6(84 \text{ kips})$ | $= 32 \text{ kips} + 84 \text{ kips}$ |
| $= 173$ kips | $= 116$ kips |

**Method 1: AISC Tables**

The most direct method of calculating the available compressive strength is through the use of Table 4-B (Volume 2 of this document). A $K$ factor of 1.0 is used for a pin-ended member. Because the unbraced length is the same in both the $x$-$x$ and $y$-$y$ directions, and $I_x$ exceeds $I_y$, $y$-$y$ axis buckling will govern.

Entering Table 4-B with $L_{cy} = KL_y = 14$ ft yields:

---

# I-48

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 368 \text{ kips} > 173 \text{ kips} \quad \textbf{o.k.}$ | $\dfrac{P_n}{\Omega_c} = 245 \text{ kips} > 116 \text{ kips} \quad \textbf{o.k.}$ |

**Method 2: AISC Specification Calculations**

As an alternate to using Table 4-B, the available compressive strength can be calculated directly using the provisions of AISC *Specification* Chapter I.

From AISC *Manual* Table 1-11 and Figure I.4-1, the geometric properties of an HSS10×6×⅜ are as follows:

$A_s = 10.4$ in.²
$H = 10.0$ in.
$B = 6.00$ in.
$t_{nom} = \frac{3}{8}$ in. (nominal wall thickness)
$t = 0.349$ in. (design wall thickness)
$h/t = 25.7$
$b/t = 14.2$
$I_{xx} = 137$ in.⁴
$I_{yy} = 61.8$ in.⁴

As shown in Figure I-1, internal clear distances are determined as:

$h_i = H - 2t$
$= 10.0$ in. $- 2(0.349$ in.$)$
$= 9.30$ in.

$b_i = B - 2t$
$= 6.00$ in. $- 2(0.349$ in.$)$
$= 5.30$ in.

From Design Example I.3, the area of concrete, $A_c$, equals 49.2 in.² The steel and concrete areas can be used to calculate the gross cross-sectional area as follows:

$A_g = A_s + A_c$
$= 10.4$ in.² $+ 49.2$ in.²
$= 59.6$ in.²

Calculate the concrete moment of inertia using geometry compatible with that used in the calculation of the steel area in AISC *Manual* Table 1-11 (taking into account the design wall thickness and outside corner radii of two times the design wall thickness in accordance with AISC *Manual* Part 1), the following equations may be used, based on the terminology given in Figure I-1 in the introduction to these examples.

For bending about the $x$-$x$ axis:

---

# I-49

$$I_{cx} = \frac{(B - 4t)h_i^3}{12} + \frac{t(H - 4t)^3}{6} + \frac{(9\pi^2 - 64)t^4}{36\pi} + \pi t^2\left(\frac{H - 4t}{2} + \frac{4t}{3\pi}\right)^2$$

$$= \frac{[6.00 \text{ in.} - 4(0.349 \text{ in.})](9.30 \text{ in.})^3}{12} + \frac{(0.349 \text{ in.})[10.0 \text{ in.} - 4(0.349 \text{ in.})]^3}{6} + \frac{(9\pi^2 - 64)(0.349 \text{ in.})^4}{36\pi}$$

$$+ \pi(0.349 \text{ in.})^2\left[\frac{10.0 \text{ in.} - 4(0.349 \text{ in.})}{2} + \frac{4(0.349 \text{ in.})}{3\pi}\right]^2$$

$$= 353 \text{ in.}^4$$

For bending about the $y$-$y$ axis:

$$I_{cy} = \frac{(H - 4t)b_i^3}{12} + \frac{t(B - 4t)^3}{6} + \frac{(9\pi^2 - 64)t^4}{36\pi} + \pi t^2\left(\frac{B - 4t}{2} + \frac{4t}{3\pi}\right)^2$$

$$= \frac{[10.0 \text{ in.} - 4(0.349 \text{ in.})](5.30 \text{ in.})^3}{12} + \frac{(0.349 \text{ in.})[6.00 \text{ in.} - 4(0.349 \text{ in.})]^3}{6} + \frac{(9\pi^2 - 64)(0.349 \text{ in.})^4}{36\pi}$$

$$+ \pi(0.349 \text{ in.})^2\left[\frac{6.00 \text{ in.} - 4(0.349 \text{ in.})}{2} + \frac{4(0.349 \text{ in.})}{3\pi}\right]^2$$

$$= 115 \text{ in.}^4$$

**Limitations of AISC Specification Sections I1.3 and I2.2a**

(1) Concrete Strength: $3 \text{ ksi} \leq f_c' \leq 10$ ksi
$f_c' = 5$ ksi **o.k.**

(2) Specified minimum yield stress of structural steel: $F_y \leq 75$ ksi
$F_y = 50$ ksi **o.k.**

(3) Cross-sectional area of steel section: $A_s \geq 0.01A_g$

$10.4 \text{ in.}^2 \geq (0.01)(59.6 \text{ in.}^2)$

$> 0.596 \text{ in.}^2 \quad \textbf{o.k.}$

There are no minimum longitudinal reinforcement requirements in the AISC *Specification* within filled composite members; therefore, the area of reinforcing bars, $A_{sr}$, for this example is zero.

**Classify Section for Local Buckling**

In order to determine the strength of the composite section subject to axial compression, the member is first classified as compact, noncompact, or slender in accordance with AISC *Specification* Table I1.1a.

$$\lambda_p = 2.26\sqrt{\frac{E}{F_y}}$$

$$= 2.26\sqrt{\frac{29{,}000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 54.4$$

---

# I-50

$$\lambda_{controlling} = \max\begin{cases} h/t = 25.7, \\ b/t = 14.2 \end{cases}$$

$$= 25.7$$

$\lambda_{controlling} \leq \lambda_p$; therefore, the section is compact

**Available Compressive Strength**

The nominal axial compressive strength for compact sections without consideration of length effects, $P_{no}$, is determined from AISC *Specification* Section I2.2b as:

$$P_{no} = P_p$$
$$(Spec. \text{ Eq. I2-9a})$$

$$P_p = F_y A_s + C_2 f_c'\left(A_c + A_{sr}\frac{E_s}{E_c}\right)$$
$$(Spec. \text{ Eq. I2-9b})$$

where
$C_2 = 0.85$ for rectangular sections

$$P_{no} = (50 \text{ ksi})(10.4 \text{ in.}^2) + 0.85(5 \text{ ksi})(49.2 \text{ in.}^2 + 0 \text{ in.}^2)$$

$$= 729 \text{ kips}$$

Because the unbraced length is the same in both the $x$-$x$ and $y$-$y$ directions, the column will buckle about the weaker $y$-$y$ axis (the axis having the lower moment of inertia). $I_{cy}$ and $I_{yy}$ will therefore be used for calculation of length effects in accordance with AISC *Specification* Sections I2.2b and I2.1b as follows:

$$C_3 = 0.45 + 3\left(\frac{A_s + A_{sr}}{A_g}\right) \leq 0.9$$
$$(Spec. \text{ Eq. I2-13})$$

$$= 0.45 + 3\left(\frac{10.4 \text{ in.}^2 + 0 \text{ in.}^2}{59.6 \text{ in.}^2}\right) \geq 0.9$$

$$= 0.973 > 0.9$$
$$= 0.9$$

$$E_c = w_c^{1.5}\sqrt{f_c'}$$

$$= (145 \text{ lb/ft}^3)^{1.5}\sqrt{5 \text{ ksi}}$$

$$= 3{,}900 \text{ ksi}$$

$$(EI)_{eff} = E_s I_{sy} + E_c I_{sr} + C_3 E_c I_{cy}$$
(from $Spec.$ Eq. I2-12)

$$= (29{,}000 \text{ ksi})(61.8 \text{ in.}^4) + 0 \text{ kip-in.}^2 + 0.9(3{,}900 \text{ ksi})(115 \text{ in.}^4)$$

$$= 2{,}200{,}000 \text{ kip-in.}^2$$

$$P_e = \pi^2(EI)_{eff}/L_c^2$$
$$(Spec. \text{ Eq. I2-4})$$

where $L_c = KL$ and $K = 1.0$ for a pin-ended member

---

# I-51

$$P_e = \frac{\pi^2(2{,}200{,}000 \text{ kip-in.}^2)}{[(1.0)(14 \text{ ft})(12 \text{ in./ft})]^2}$$

$$= 769 \text{ kips}$$

$$\frac{P_{no}}{P_e} = \frac{729 \text{ kips}}{769 \text{ kips}}$$

$$= 0.948 < 2.25$$

Therefore, use AISC *Specification* Equation I2-2.

$$P_n = P_{no}\left(0.658^{\frac{P_{no}}{P_e}}\right)$$
$$(Spec. \text{ Eq. I2-2})$$

$$= (729 \text{ kips})(0.658)^{0.948}$$

$$= 490 \text{ kips}$$

Check the adequacy of the composite column for the required axial compressive strength:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.75$ | $\Omega_c = 2.00$ |
| $\phi_c P_n = 0.75(490 \text{ kips})$ | $\dfrac{P_n}{\Omega_c} = \dfrac{490 \text{ kips}}{2.00}$ |
| $= 368 \text{ kips} > 173 \text{ kips} \quad \textbf{o.k.}$ | $= 245 \text{ kips} > 116 \text{ kips} \quad \textbf{o.k.}$ |

The values match those tabulated in Table 4-B.

**Available Compressive Strength of Bare Steel Section**

Due to the differences in resistance and safety factors between composite and noncomposite column provisions, it is possible to calculate a lower available compressive strength for a composite column than one would calculate for the corresponding bare steel section. However, in accordance with AISC *Specification* Section I2.2b, the available compressive strength need not be less than that calculated for the bare steel member in accordance with Chapter E.

From AISC *Manual* Table 4-3, for an HSS10×6×⅜, $KL_y = 14$ ft:

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 331 \text{ kips} < 368 \text{ kips}$ | $\dfrac{P_n}{\Omega_c} = 220 \text{ kips} < 245 \text{ kips}$ |

Thus, the composite section strength controls and is adequate for the required axial compressive strength as previously demonstrated.

**Force Allocation and Load Transfer**

Load transfer calculations for external axial forces should be performed in accordance with AISC *Specification* Section I6. The specific application of the load transfer provisions is dependent upon the configuration and detailing of the connecting elements. Expanded treatment of the application of load transfer provisions is provided in Design Example I.3.

---

# I-52

# EXAMPLE I.5 FILLED COMPOSITE MEMBER IN AXIAL TENSION

## Given:

Determine if the filled composite member illustrated in Figure I.5-1 is adequate for the indicated dead load compression and wind load tension. The entire load is applied to the steel section.

![Diagram showing filled composite member with HSS10×6×⅜ section and elevation view showing L = 14'-0" column height with PD = -32 kips and PW = 100 kips applied at top, and pinned base support at bottom]

*Fig. I.5-1. Filled composite member section and applied loading.*

The composite member consists of an ASTM A500/A500M, Grade C, HSS with normal weight (145 lb/ft³) concrete fill having a specified concrete compressive strength, $f_c' = 5$ ksi.

## Solution:

From AISC *Manual* Table 2-4, the material properties are:

ASTM A500/A500M Grade C
$F_y = 50$ ksi

From AISC *Manual* Table 1-11, the geometric properties are as follows:

HSS10×6×⅜
$A_s = 10.4$ in.²

There are no minimum requirements for longitudinal reinforcement in the AISC *Specification*; therefore, it is common industry practice to use filled shapes without longitudinal reinforcing, thus $A_{sr} = 0$.

From ASCE/SEI 7, Chapter 2, the required tensile strength is (taking compression as negative and tension as positive):

| LRFD | ASD |
|------|-----|
| Governing Uplift Load Combination = $0.9D + 1.0W$ | Governing Uplift Load Combination = $0.6D + 0.6W$ |
| $P_r = P_t$ | $P_r = P_a$ |
| $= 0.9(-32 \text{ kips}) + 1.0(100 \text{ kips})$ | $= 0.6(-32 \text{ kips}) + 0.6(100 \text{ kips})$ |
| $= 71.2$ kips | $= 40.8$ kips |

---

# I-53

**Available Tensile Strength**

Available tensile strength for a filled composite member is determined in accordance with AISC *Specification* Section I2.2c.

$$P_n = A_s F_y + A_{sr} F_{ysr}$$
$$(Spec. \text{ Eq. I2-14})$$

$$= (10.4 \text{ in.}^2)(50 \text{ ksi}) + (0 \text{ in.}^2)(60 \text{ ksi})$$

$$= 520 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi_t = 0.90$ | $\Omega_t = 1.67$ |
| $\phi_t P_n = 0.90(520 \text{ kips})$ | $\dfrac{P_n}{\Omega_t} = \dfrac{520 \text{ kips}}{1.67}$ |
| $= 468 \text{ kips} > 71.2 \text{ kips} \quad \textbf{o.k.}$ | $= 311 \text{ kips} > 40.8 \text{ kips} \quad \textbf{o.k.}$ |

For filled composite HSS members with no internal longitudinal reinforcing, the values for available tensile strength may also be taken directly from AISC *Manual* Table 5-4. The values calculated here match those for the limit state of tensile yielding shown in Table 5-4.

**Force Allocation and Load Transfer**

Load transfer calculations are not required for filled composite members in axial tension that do not contain longitudinal reinforcement and the load is transferred directly to the steel section, such as the one under investigation, as only the steel section resists tension.

---

# I-54

# EXAMPLE I.6 FILLED COMPOSITE MEMBER IN COMBINED AXIAL COMPRESSION, FLEXURE, AND SHEAR

## Given:

Using AISC design tables, determine if the filled composite member illustrated in Figure I.6-1 is adequate for the indicated axial forces, shears, and moments that have been determined in accordance with the direct analysis method of AISC *Specification* Chapter C for the controlling ASCE/SEI 7 load combinations.

![Diagram showing filled composite member with HSS10×6×⅜ section (B = 6", H = 10") with x-x and y-y axes marked. Elevation (FBD) shows L = 14'-0" column height with forces and moments at top (Pr, Mr, Vr) and bottom (Vr, Pr, Mr). Table shows LRFD and ASD values: Pr (kips): 129/98.2, Mr (kip-ft): 120/54, Vr (kips): 17.1/10.3]

*Fig. I.6-1. Filled composite member section and member forces.*

The composite member consists of an ASTM A500/A500M, Grade C, HSS with normal weight (145 lb/ft³) concrete fill having a specified concrete compressive strength, $f_c' = 5$ ksi.

## Solution:

From AISC *Manual* Table 2-4, the material properties are:

ASTM A500/A500M Grade C
$F_y = 50$ ksi

From AISC *Manual* Table 1-11 and Figure I.6-1, the geometric properties are as follows:

HSS10×6×⅜
$H = 10.0$ in.
$B = 6.00$ in.
$t_{nom} = \frac{3}{8}$ in. (nominal wall thickness)
$t = 0.349$ in. (design wall thickness)
$h/t = 25.7$
$b/t = 14.2$
$A_s = 10.4$ in.²
$I_{xx} = 137$ in.⁴
$I_{yy} = 61.8$ in.⁴
$Z_{xx} = 33.8$ in.³

---

# I-55

Additional geometric properties used for composite design are determined in Design Examples I.3 and I.4 as follows:

$h_i = 9.30$ in. clear distance between HSS walls (longer side)
$b_i = 5.30$ in. clear distance between HSS walls (shorter side)
$A_c = 49.2$ in.² cross-sectional area of concrete fill
$A_g = 59.6$ in.² gross cross-sectional area of composite member
$A_{sr} = 0$ in.² area of longitudinal reinforcement
$E_c = 3{,}900$ ksi modulus of elasticity of concrete
$I_{cx} = 353$ in.⁴ moment of inertia of concrete fill about the $x$-$x$ axis
$I_{cy} = 115$ in.⁴ moment of inertia of concrete fill about the $y$-$y$ axis

**Limitations of AISC Specification Sections I1.3 and I2.2a**

(1) Concrete Strength: $3 \text{ ksi} \leq f_c' \leq 10$ ksi
$f_c' = 5$ ksi **o.k.**

(2) Specified minimum yield stress of structural steel: $F_y \leq 75$ ksi
$F_y = 50$ ksi **o.k.**

(3) Cross-sectional area of steel section: $A_s \geq 0.01A_g$

$10.4 \text{ in.}^2 \geq (0.01)(59.6 \text{ in.}^2)$

$> 0.596 \text{ in.}^2 \quad \textbf{o.k.}$

**Classify Section for Local Buckling**

The composite member in question was shown to be compact for pure compression in Example I.4 in accordance with AISC *Specification* Table I1.1a. The section must also be classified for local buckling due to flexure in accordance with *Specification* Table I1.1b; however, because the limits for members subject to flexure are equal to or less stringent than those for members subject to compression, the member is compact for flexure.

**Interaction of Axial Force and Flexure**

The interaction between axial forces and flexure in composite members is governed by AISC *Specification* Section I5 that, for compact members, permits the use of the methods of Section I1.2 with the option to use the interaction equations of Section H1.1.

The strain compatibility method is a generalized approach that allows for the construction of an interaction diagram based upon the strain concepts used for reinforced concrete design. The application of the strain compatibility method is required for irregular/nonsymmetrical sections, and its general application may be found in reinforced concrete design texts and will not be discussed further here.

Plastic stress distribution methods are discussed in AISC *Specification* Commentary Section I5, which provides three acceptable procedures for compact filled composite members. The first procedure, Method 1, invokes the interaction equations of Section H1. The second procedure, Method 2, involves the construction of a piecewise-linear interaction curve using the plastic strength equations provided in AISC *Manual* Table 6-3. The third procedure, Method 2—Simplified, is a reduction of the piecewise-linear interaction curve that allows for the use of less conservative interaction equations than those presented in Chapter H (refer to AISC *Specification* Commentary Figure C-I5.3).

For this design example, each of the three applicable plastic stress distribution procedures are reviewed and compared.

---

# I-56

**Method 1: Interaction Equations of Section H1**

The most direct and conservative method of assessing interaction effects is through the use of the interaction equations of AISC *Specification* Section H1.1. For HSS shapes, both the available compressive and flexural strengths can be determined from Table 4-B (included in Volume 2 of this document). In accordance with the direct analysis method, the required axial strength and the unbraced length in the same axis both for $x$-$x$ and $y$-$y$ directions, and $L_c$ exceeds $L_b$, the applied moment about that axis is indicated in Figure I6-1.

Entering Table 4-B with $L_{cy} = L_{by} = 14$ ft yields:

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 368$ kips | $P_n/\Omega_c = 245$ kips |
| $M_{rx}/\Omega_b = 97.4$ kip-ft | $M_{rx}/\Omega_b = 97.4$ kip-ft |
| $P_r/P_c = \dfrac{129 \text{ kips}}{368 \text{ kips}} = 0.351 > 0.2$ | $P_r/P_a = \dfrac{98.2 \text{ kips}}{245 \text{ kips}} = 0.401 > 0.2$ |

Therefore, use AISC *Specification* Equation H1-1a.

$$\frac{P_r}{P_c} + \frac{8}{9}\left(\frac{M_r}{M_c}\right) \leq 1.0$$
(from Spec. Eq. H1-1a)

$$\frac{P_r}{P_{AP}} + \frac{M_u}{M_{CP}} \leq 1.0$$

$$\frac{129 \text{ kips}}{368 \text{ kips}} + \frac{8}{9}\left(\frac{120 \text{ kip-ft}}{141 \text{ kip-ft}}\right) \leq 1.0$$

$$0.948 < 1.0 \quad \textbf{o.k.}$$

| LRFD | ASD |
|------|-----|
| Therefore, use AISC *Specification* Equation H1-1a. | Therefore, use AISC *Specification* Equation H1-1a. |
| $\dfrac{P_r}{P_{AP}} + \dfrac{8}{9}\left(\dfrac{M_r}{M_{Cx}}\right) \leq 1.0$ (from Spec. Eq. H1-1a) | $\dfrac{P_r}{P_c/\Omega_c} + \dfrac{8}{9}\left(\dfrac{M_u}{M_{Cx}/\Omega_b}\right) \leq 1.0$ (from Spec. Eq. H1-1a) |
| $\dfrac{129 \text{ kips}}{368 \text{ kips}} + \dfrac{8}{9}\left(\dfrac{120 \text{ kip-ft}}{141 \text{ kip-ft}}\right) \leq 1.0$ | $\dfrac{98.2 \text{ kips}}{245 \text{ kips}} + \dfrac{8}{9}\left(\dfrac{54 \text{ kip-ft}}{93.4 \text{ kip-ft}}\right) \leq 1.0$ |
| $0.948 < 1.0 \quad \textbf{o.k.}$ | $0.914 < 1.0 \quad \textbf{o.k.}$ |

Using LRFD methodology, Method 1 indicates that the section is inadequate for the applied loads. The designer can then select larger HSS shapes, reselect the structural system, or consider the use of other methods to the conservative design method used in Method 2. The use of Method 2 is illustrated in the following section. Using ASD methodology, Method 1 indicates that the section is adequate for the applied loads.

The procedures for constructing the interaction diagram using the plastic stress distribution model is illustrated graphically in Figure I.6-2 using a 4-step process.

Referencing Figure I.6-2, the nominal strength interaction surface A, B, C, D, E is first determined using the equations on which *Manual* Table 6-3 is based. The axial force and moment at each control point are calculated without consideration of slenderness reduction at each point. The resulting forces and moments are then used to construct the stress surface A', B', C', D', E'. The appropriate resistance or safety factors are then applied to create the design surface A", B", C", D", E" for LRFD and AISC-1 for ASD. These steps are illustrated graphically in the following sketches and calculations. The examples then illustrate how the applied axial force and moment at the governing load combinations within the design surface. These steps are illustrated in detail in the following calculation.

Step 1: Construct nominal strength interaction surface A, B, C, D, E without length effects.

Using the equations provided in AISC *Manual* Table 6-3 for bending about the $x$-$x$ axis yields:

---

# I-57

Point A (pure axial compression):

$$P_A = F_y A_s + 0.85 f_c' A_c$$

$$= (50 \text{ ksi})(10.4 \text{ in.}^2) + 0.85(5 \text{ ksi})(49.2 \text{ in.}^2)$$

$$= 729 \text{ kips}$$

$$M_A = 0 \text{ kip-ft}$$

Point D (maximum nominal moment strength):

$$P_D = \frac{0.85 f_c' A_c}{2}$$

$$= \frac{0.85(5 \text{ ksi})(49.2 \text{ in.}^2)}{2}$$

$$= 105 \text{ kips}$$

$$Z_{sx} = 33.8 \text{ in.}^3$$

$$r_i = t$$
$$= 0.349 \text{ in.}$$

$$Z_c = \frac{b_i h_i^2}{4} - 0.429r_i^2 h_i + 0.192r_i^3$$

$$= \frac{(5.30 \text{ in.})(9.30 \text{ in.})^2}{4} - 0.429(0.349 \text{ in.})^2(9.30 \text{ in.}) + 0.192(0.349 \text{ in.})^3$$

$$= 114 \text{ in.}^3$$

![Interaction diagram showing compressive strength vs flexural strength with multiple curves including material strength (strength equations), slenderness (column curve), and design points labeled A through E with their prime and double-prime variations. Shows slenderness reduction λ = A'/A]

*Fig. I.6-2. Interaction diagram for composite beam-column—Method 2.*

---

# I-58

$$M_D = F_y Z_{sx} + \frac{0.85 f_c' Z_c}{2}$$

$$= \left[(50 \text{ ksi})(33.8 \text{ in.}^3) + \frac{0.85(5 \text{ ksi})(114 \text{ in.}^3)}{2}\right]\left(\frac{1}{12 \text{ in./ft}}\right)$$

$$= 161 \text{ kip-ft}$$

Point B (pure flexure):

$$P_B = 0 \text{ kips}$$

$$h_n = \frac{0.85 f_c' A_c}{2(0.85 f_c' b_i + 4F_y t)} \leq \frac{h_i}{2}$$

$$= \frac{0.85(5 \text{ ksi})(49.2 \text{ in.}^2)}{2[0.85(5 \text{ ksi})(5.30 \text{ in.}) + 4(50 \text{ ksi})(0.349 \text{ in.})]} \leq \frac{9.30 \text{ in.}}{2}$$

$$= 1.13 \text{ in.} < 4.65 \text{ in.}$$
$$= 1.13 \text{ in.}$$

$$Z_{sn} = 2th_n^2$$

$$= 2(0.349 \text{ in.})(1.13 \text{ in.})^2$$

$$= 0.891 \text{ in.}^3$$

$$Z_{cn} = b_i h_n^2$$

$$= (5.30 \text{ in.})(1.13 \text{ in.})^2$$

$$= 6.77 \text{ in.}^3$$

$$M_B = M_D - F_y Z_{sn} - 0.85 f_c'\left(\frac{Z_{cn}}{2}\right)$$

$$= 161 \text{ kip-ft} - (50 \text{ ksi})(0.891 \text{ in.}^3)\left(\frac{1}{12 \text{ in./ft}}\right) - 0.85(5 \text{ ksi})\left(\frac{6.77 \text{ in.}^3}{2}\right)\left(\frac{1}{12 \text{ in./ft}}\right)$$

$$= 156 \text{ kip-ft}$$

Point C (intermediate point):

$$P_C = 0.85 f_c' A_c$$

$$= 0.85(5 \text{ ksi})(49.2 \text{ in.}^2)$$

$$= 209 \text{ kips}$$

$$M_C = M_B$$
$$= 156 \text{ kip-ft}$$

Point E (optional):

Point E is an optional point that helps better define the interaction curve.

---

# I-59

$$h_E = \frac{h_n}{2} + \frac{H}{4}, \text{ where } h_n = 1.13 \text{ in. from Point B}$$

$$= \frac{1.13 \text{ in.}}{2} + \frac{10.0 \text{ in.}}{4}$$

$$= 3.07 \text{ in.}$$

$$P_E = \frac{0.85 f_c' A_c}{2} + 0.85 f_c' b_i h_E + 4F_y th_E$$

$$= \frac{0.85(5 \text{ ksi})(49.2 \text{ in.}^2)}{2} + 0.85(5 \text{ ksi})(5.30 \text{ in.})(3.07 \text{ in.}) + 4(50 \text{ ksi})(0.349 \text{ in.})(3.07 \text{ in.})$$

$$= 388 \text{ kips}$$

$$Z_{sE} = b_i h_E^2$$

$$= (5.30 \text{ in.})(3.07 \text{ in.})^2$$

$$= 50.0 \text{ in.}^3$$

$$Z_{cE} = 2th_E^2$$

$$= 2(0.349 \text{ in.})(3.07 \text{ in.})^2$$

$$= 6.58 \text{ in.}^3$$

$$M_E = M_D - F_y Z_{sE} - \frac{0.85 f_c' Z_{cE}}{2}$$

$$= 161 \text{ kip-ft} - (50 \text{ ksi})(6.58 \text{ in.}^3)\left(\frac{1}{12 \text{ in./ft}}\right) - \left[\frac{0.85(5 \text{ ksi})(50.0 \text{ in.}^3)}{2}\right]\left(\frac{1}{12 \text{ in./ft}}\right)$$

$$= 125 \text{ kip-ft}$$

The calculated points are plotted to construct the nominal strength interaction surface without length effects as depicted in Figure I.6-3.

Step 2: Construct nominal strength interaction surface $A'$, $B'$, $C'$, $D'$, $E'$ with length effects.

The slenderness reduction factor, $\lambda$, is calculated for Point A using AISC *Specification* Section I2.2 in accordance with *Specification* Commentary Section I5.

$$P_{no} = P_A$$
$$= 729 \text{ kips}$$

$$C_3 = 0.45 + 3\left(\frac{A_s + A_{sr}}{A_g}\right) \leq 0.9$$
$$(Spec. \text{ Eq. I2-13})$$

$$= 0.45 + 3\left(\frac{10.4 \text{ in.}^2 + 0 \text{ in.}^2}{59.6 \text{ in.}^2}\right) \leq 0.9$$

$$= 0.973 > 0.9$$
$$= 0.9$$

---

# I-60

$$(EI)_{eff} = E_s I_{sy} + E_c I_{sr} + C_3 E_c I_{cy}$$
(from $Spec.$ Eq. I2-12)

$$= (29{,}000 \text{ ksi})(61.8 \text{ in.}^4) + 0 + 0.9(3{,}900 \text{ ksi})(115 \text{ in.}^4)$$

$$= 2{,}200{,}000 \text{ kip-in.}^2$$

$$P_e = \pi^2(EI)_{eff}/L_c^2$$, where $L_c = KL$ and $K = 1.0$ in accordance with the direct analysis method
$$(Spec. \text{ Eq. I2-4})$$

$$= \frac{\pi^2(2{,}200{,}000 \text{ kip-in.}^2)}{[(14 \text{ ft})(12 \text{ in./ft})]^2}$$

$$= 769 \text{ kips}$$

$$\frac{P_{no}}{P_e} = \frac{729 \text{ kips}}{769 \text{ kips}}$$

$$= 0.948 < 2.25$$

Use AISC *Specification* Equation I2-2.

$$P_n = P_{no}\left(0.658^{\frac{P_{no}}{P_e}}\right)$$
$$(Spec. \text{ Eq. I2-2})$$

$$= (729 \text{ kips})(0.658)^{0.948}$$

$$= 490 \text{ kips}$$

![Graph showing nominal strength interaction surface without length effects. X-axis shows Flexural Strength (kip-ft) from 0 to 180, Y-axis shows Compressive Strength (kips) from 0 to 800. Points A, B, C, D, and E are marked on a downward sloping curve labeled "Nominal Strength (without length effects)"]

*Fig. I.6-3. Nominal strength interaction surface without length effects.*

---

# I-61

From AISC *Specification* Commentary Section I5:

$$\lambda = \frac{P_n}{P_{no}}$$

$$= \frac{490 \text{ kips}}{729 \text{ kips}}$$

$$= 0.672$$

In accordance with AISC *Specification* Commentary Section I5, the same slenderness reduction is applied to each of the remaining points on the interaction surface as follows:

$$P_{A'} = \lambda P_A$$
$$= 0.672(729 \text{ kips})$$
$$= 490 \text{ kips}$$

$$P_{B'} = \lambda P_B$$
$$= 0.672(0 \text{ kip})$$
$$= 0 \text{ kip}$$

$$P_{C'} = \lambda P_C$$
$$= 0.672(209 \text{ kips})$$
$$= 140 \text{ kips}$$

$$P_{D'} = \lambda P_D$$
$$= 0.672(105 \text{ kips})$$
$$= 70.6 \text{ kips}$$

$$P_{E'} = \lambda P_E$$
$$= 0.672(388 \text{ kips})$$
$$= 261 \text{ kips}$$

The modified axial strength values are plotted with the flexural strength values previously calculated to construct the nominal strength interaction surface including length effects. These values are superimposed on the nominal strength surface not including length effects for comparison purposes in Figure I.6-4.

Step 3: Construct design interaction surface $A''$, $B''$, $C''$, $D''$, $E''$ and verify member adequacy.

The final step in the Method 2 procedure is to reduce the interaction surface for design using the appropriate resistance or safety factors.

---

# I-62

| LRFD | ASD |
|------|-----|
| Design compressive strength: | Allowable compressive strength: |
| $\phi_c = 0.75$ | $\Omega_c = 2.00$ |
| $P_{X''} = \phi_c P_{X'}$, where $X = A, B, C, D,$ or E | $P_{X''} = P_{X'}/\Omega_c$, where $X = A, B, C, D,$ or E |
| $P_{A''} = 0.75(490 \text{ kips})$ | $P_{A''} = 490 \text{ kips}/2.00$ |
| $= 368$ kips | $= 245$ kips |
| $P_{B''} = 0.75(0 \text{ kip})$ | $P_{B''} = 0 \text{ kip}/2.00$ |
| $= 0$ kip | $= 0$ kip |
| $P_{C''} = 0.75(140 \text{ kips})$ | $P_{C''} = 140 \text{ kips}/2.00$ |
| $= 105$ kips | $= 70.0$ kips |
| $P_{D''} = 0.75(70.6 \text{ kips})$ | $P_{D''} = 70.6 \text{ kips}/2.00$ |
| $= 53.0$ kips | $= 35.3$ kips |
| $P_{E''} = 0.75(261 \text{ kips})$ | $P_{E''} = 261 \text{ kips}/2.00$ |
| $= 196$ kips | $= 131$ kips |

![Graph showing nominal strength interaction surfaces with and without length effects. X-axis shows Flexural Strength (kip-ft) from 0 to 180, Y-axis shows Compressive Strength (kips) from 0 to 800. Two curves are shown: "Nominal Strength (without length effects)" and "Nominal Strength (with length effects)". Points A, A', E, E', C, C', D, D', B, B' are marked on both curves.]

*Fig. I.6-4. Nominal strength interaction surfaces (with and without length effects).*

---

# I-63

| LRFD | ASD |
|------|-----|
| Design flexural strength: | Allowable flexural strength: |
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $M_{X''} = \phi_b M_X$, where $X = A, B, C, D,$ or E | $M_{X''} = M_X/\Omega_b$, where $X = A, B, C, D,$ or E |
| $M_{A''} = 0.90(0 \text{ kip-ft})$ | $M_{A''} = 0 \text{ kip-ft}/1.67$ |
| $= 0$ kip-ft | $= 0$ kip-ft |
| $M_{B''} = 0.90(156 \text{ kip-ft})$ | $M_{B''} = 156 \text{ kip-ft}/1.67$ |
| $= 140$ kip-ft | $= 93.4$ kip-ft |
| $M_{C''} = 0.90(156 \text{ kip-ft})$ | $M_{C''} = 156 \text{ kip-ft}/1.67$ |
| $= 140$ kip-ft | $= 93.4$ kip-ft |
| $M_{D''} = 0.90(161 \text{ kip-ft})$ | $M_{D''} = 161 \text{ kip-ft}/1.67$ |
| $= 145$ kip-ft | $= 96.4$ kip-ft |
| $M_{E''} = 0.90(125 \text{ kip-ft})$ | $M_{E''} = 125 \text{ kip-ft}/1.67$ |
| $= 113$ kip-ft | $= 74.9$ kip-ft |

The available strength values for each design method can now be plotted. These values are superimposed on the nominal strength surfaces (with and without length effects) previously calculated for comparison purposes in Figure I.6-5.

By plotting the required axial and flexural strength values determined for the governing load combinations on the available strength surfaces indicated in Figure I.6-5, it can be seen that both ASD ($M_a$, $P_a$) and LRFD ($M_u$, $P_u$) points lie within their respective design surfaces. The member in question is therefore adequate for the applied loads.

Designers should carefully review the proximity of the available strength values in relation to point $D''$ on Figure I.6-5 as it is possible for point $D''$ to fall outside of the nominal strength curve, thus resulting in an unsafe design. This possibility is discussed further in AISC *Specification* Commentary Section I5 and is avoided through the use of Method 2—Simplified as illustrated in the following section.

**Method 2: Simplified**

The simplified version of Method 2 involves the removal of points D″ and E″ from the Method 2 interaction surface leaving only points A″, B″, and C″ as illustrated in the comparison of the two methods in Figure I.6-6.

Reducing the number of interaction points allows for a bilinear interaction check defined by AISC *Specification* Commentary Equations C-I5-1a and C-I5-1b to be performed. Using the available strength values previously calculated in conjunction with the Commentary equations, interaction ratios are determined as follows:

---

# I-64

| LRFD | ASD |
|------|-----|
| $P_r = P_u$ | $P_r = P_a$ |
| $= 129$ kips | $= 98.2$ kips |
| $P_r \geq P_{C''}$ | $P_r \geq P_{C''}$ |
| $\geq 105$ kips | $\geq 70.0$ kips |
| Therefore, use AISC *Specification* Commentary Equation C-I5-1b. | Therefore, use AISC *Specification* Commentary Equation C-I5-1b. |
| $\dfrac{P_r - P_C''}{P_A - P_C''} + \dfrac{M_u}{M_C''} \leq 1.0$ (from $Spec.$ Eq. C-I5-1b) | $\dfrac{P_r - P_{C''}}{P_{A''} - P_{C''}} + \dfrac{M_a}{M_{C''}} \leq 1.0$ (from $Spec.$ Eq. C-I5-1b) |
| which for LRFD equals: | which for ASD equals: |
| $\dfrac{P_u - P_{C''}}{P_{A''} - P_{C''}} + \dfrac{M_u}{M_{C''}} \leq 1.0$ | $\dfrac{P_a - P_{C''}}{P_{A''} - P_{C''}} + \dfrac{M_a}{M_{C''}} \leq 1.0$ |
| $\dfrac{129 \text{ kips} - 105 \text{ kips}}{368 \text{ kips} - 105 \text{ kips}} + \dfrac{120 \text{ kip-ft}}{140 \text{ kip-ft}} \leq 1.0$ | $\dfrac{98.2 \text{ kips} - 70.0 \text{ kips}}{245 \text{ kips} - 70.0 \text{ kips}} + \dfrac{54 \text{ kip-ft}}{93.4 \text{ kip-ft}} \leq 1.0$ |
| $0.948 < 1.0 \quad \textbf{o.k.}$ | $0.739 < 1.0 \quad \textbf{o.k.}$ |

Thus, the member is adequate for the applied loads.

![Graph showing available and nominal interaction surfaces. X-axis shows Flexural Strength (kip-ft) from 0 to 180, Y-axis shows Compressive Strength (kips) from 0 to 800. Multiple curves and points are shown including nominal strength curves (with and without length effects), LRFD and ASD design curves, and points labeled A through E with various prime notations. A point marked with X shows Mu, Pu location.]

*Fig. I.6-5. Available and nominal interaction surfaces.*

---

# I-65

**Comparison of Methods**

The composite member was found to be inadequate using Method 1—Chapter H interaction equations, but was found to be adequate using both Method 2 and Method 2—Simplified procedures. A comparison between the methods is most easily made by overlaying the design curves from each method as illustrated in Figure I.6-7 for LRFD design.

From Figure I.6-7, the conservative nature of the Chapter H interaction equations can be seen. Method 2 provides the highest available strength; however, the Method 2—Simplified procedure also provides a good representation of the complete design curve. By using the design tables in Table 2 of this document to determine the available strength of the composite member in compression and flexure (Points $A''$ and $B''$ respectively), the modest additional effort required to calculate the available compressive strength at Point $C''$ can result in appreciable gains in member strength when using Method 2—Simplified as opposed to Method 1.

![First graph showing comparison of Method 2 and Method 2-Simplified with compressive strength (kips) on y-axis (0-400) and flexural strength (kip-ft) on x-axis (0-160). Shows curves for LRFD Method 2, ASD Method 2, LRFD Method 2-Simplified, and ASD Method 2-Simplified, with points A", E", C", D", B" marked and a point for Mu, Pu indicated]

*Fig. I.6-6. Comparison of Method 2 and Method 2—Simplified.*

![Second graph showing comparison of interaction methods (LRFD) with same axes. Shows curves for LRFD Method 2, LRFD Method 2-Simplified, and Method 1-Ch. H Interaction, with points A", E", C", D", B" marked]

*Fig. I.6-7. Comparison of interaction methods (LRFD).*

---

# I-66

**Available Shear Strength**

The available shear strength is determined using AISC *Specification* Section I4.2. From Design Example I.3, the area of concrete, $A_c$, equals 49.2 in.² The shear area of the steel section is determined as follows:

$$h = H - 3t$$
$$= 10.0 \text{ in.} - 3(0.349 \text{ in.})$$
$$= 8.95 \text{ in.}$$

$$A_v = 2ht$$
$$= 2(8.95 \text{ in.})(0.349 \text{ in.})$$
$$= 6.25 \text{ in.}^2$$

Determine the shear span-to-depth:

| LRFD | ASD |
|------|-----|
| $\dfrac{(M_u/V_u)}{d} = \dfrac{[120 \text{ kip-ft}(12 \text{ in./ft})/17.1 \text{ kips}]}{10 \text{ in.}}$ | $\dfrac{(M_a/V_a)}{d} = \dfrac{[54 \text{ kip-ft}(12 \text{ in./ft})/10.3 \text{ kips}]}{10 \text{ in.}}$ |
| $= 8.42$ | $= 6.29$ |
| Because $(M_u/V_u)/d > 0.7$: | Because $(M_a/V_a)/d > 0.7$: |
| $K_v = 1$ | $K_v = 1$ |

$$V_n = 0.6A_v F_y + 0.06K_v A_c\sqrt{f_c'}$$
$$(Spec. \text{ Eq. I4-1})$$

$$= 0.6(6.25 \text{ in.}^2)(50 \text{ ksi}) + 0.06(1)(49.2 \text{ in.}^2)\sqrt{5 \text{ ksi}}$$

$$= 188 \text{ kips} + 6.60 \text{ kips}$$
$$= 195 \text{ kips}$$

The available shear strength is:

| LRFD | ASD |
|------|-----|
| $\phi_v = 0.90$ | $\Omega_v = 1.67$ |
| $\phi_v V_n = 0.90(195 \text{ kips})$ | $\dfrac{V_n}{\Omega_v} = \dfrac{195 \text{ kips}}{1.67}$ |
| $= 176 \text{ kips} > 17.1 \text{ kips} \quad \textbf{o.k.}$ | $= 117 \text{ kips} > 10.3 \text{ kips} \quad \textbf{o.k.}$ |

**Force Allocation and Load Transfer**

Load transfer calculations for applied axial forces should be performed in accordance with AISC *Specification* Section I6. The specific application of the load transfer provisions is dependent upon the configuration and detailing of the connecting elements. Expanded treatment of the application of load transfer provisions is provided in Design Example I.3.

---

# I-67

# EXAMPLE I.7 FILLED COMPOSITE BOX COLUMN WITH NONCOMPACT/SLENDER ELEMENTS

## Given:

Determine the required ASTM A572/A572M Grade 50 plate thickness of the filled composite box column illustrated in Figure I.7-1 to resist the indicated axial forces, shears, and moments that have been determined in accordance with the direct analysis method of AISC *Specification* Chapter C for the controlling ASCE/SEI 7 load combinations. The core is composed of normal weight (145 lb/ft³) concrete fill having a specified concrete compressive strength, $f_c' = 7$ ksi.

![Diagram showing composite box column section with B = 30", H = 30", interior stiffeners as required, with x-x and y-y axes marked. Two section views shown - actual section and analytical model. Elevation (FBD) shows L = 30'-0" column height with forces Pr, Mr, Vr at top and bottom. Table shows LRFD and ASD values: Pr (kips): 1,310/1,370, Mr (kip-ft): 552/248, Vr (kips): 36.8/22.1]

*Fig. I.7-1. Composite box column section and member forces.*

## Solution:

From AISC *Manual* Table 2-5, the material properties are:

ASTM A572/A572M Grade 50
$F_y = 50$ ksi

**Trial Size 1 (Noncompact)**

For ease of calculation, the contribution of the plate extensions to the member strength will be ignored as illustrated by the analytical model in Figure I.7-1.

**Trial Plate Thickness and Geometric Section Properties of the Composite Member**

Select a trial plate thickness, $t$, of $\frac{1}{2}$ in. Note that the design wall thickness reduction of AISC *Specification* Section B4.2 applies only to electric-resistance-welded HSS members and does not apply to built-up sections such as the one under consideration.

The calculated geometric properties of the 30 in. by 30 in. steel box column are:

---

# I-68

$B = 30$ in.
$H = 30$ in.
$A_g = 900$ in.²
$A_c = 841$ in.²
$A_s = 59.0$ in.²

$b_i = B - 2t$
$= 30$ in. $- 2(\frac{1}{2}$ in.$)$
$= 29.0$ in.

$h_i = H - 2t$
$= 30$ in. $- 2(\frac{1}{2}$ in.$)$
$= 29.0$ in.

$$E_c = w_c^{1.5}\sqrt{f_c'}$$

$$= (145 \text{ lb/ft}^3)^{1.5}\sqrt{7 \text{ ksi}}$$

$$= 4{,}620 \text{ ksi}$$

$$I_{gx} = \frac{BH^3}{12}$$

$$= \frac{(30 \text{ in.})(30 \text{ in.})^3}{12}$$

$$= 67{,}500 \text{ in.}^4$$

$$I_{cx} = \frac{b_i h_i^3}{12}$$

$$= \frac{(29.0 \text{ in.})(29.0 \text{ in.})^3}{12}$$

$$= 58{,}900 \text{ in.}^4$$

$$I_{sx} = I_{gx} - I_{cx}$$

$$= 67{,}500 \text{ in.}^4 - 58{,}900 \text{ in.}^4$$

$$= 8{,}600 \text{ in.}^4$$

**Limitations of AISC Specification Sections I1.3 and I2.2a**

(1) Concrete Strength: $3 \text{ ksi} \leq f_c' \leq 10$ ksi
$f_c' = 7$ ksi **o.k.**

(2) Specified minimum yield stress of structural steel: $F_y \leq 75$ ksi
$F_y = 50$ ksi **o.k.**

---

# I-69

(3) Cross-sectional area of steel section: $A_s \geq 0.01A_g$

$59.0 \text{ in.}^2 \geq (0.01)(900 \text{ in.}^2)$

$> 9.00 \text{ in.}^2 \quad \textbf{o.k.}$

**Classify Section for Local Buckling**

Classification of the section for local buckling is performed in accordance with AISC *Specification* Table I1.1a for compression and Table I1.1b for flexure. As noted in *Specification* Section I1.4, the definitions of width, depth, and thickness used in the evaluation of slenderness are provided in Section B4.1b.

For box columns, the widths of the stiffened compression elements used for slenderness checks, $b$ and $h$, are equal to the clear distances between the column walls, $b_i$ and $h_i$. The slenderness ratios are determined as follows:

$$\lambda = \frac{b_i}{t} = \frac{h_i}{t}$$

$$= \frac{29.0 \text{ in.}}{\frac{1}{2} \text{ in.}}$$

$$= 58.0$$

Classify section for local buckling in steel elements subject to axial compression from AISC *Specification* Table I1.1a:

$$\lambda_p = 2.26\sqrt{\frac{E}{F_y}}$$

$$= 2.26\sqrt{\frac{29{,}000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 54.4$$

$$\lambda_r = 3.00\sqrt{\frac{E}{F_y}}$$

$$= 3.00\sqrt{\frac{29{,}000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 72.2$$

$\lambda_p \leq \lambda \leq \lambda_r$; therefore, the section is noncompact for compression

According to AISC *Specification* Section I1.4, if any side of the section in question is noncompact or slender, then the entire section is treated as noncompact or slender. For the square section under investigation; however, this distinction is unnecessary as all sides are equal in length.

Classification of the section for local buckling in elements subject to flexure is performed in accordance with AISC *Specification* Table I1.1b. Note that flanges and webs are treated separately; however, for the case of a square section, only the most stringent limitations, those of the flange, need be applied. Noting that the flange limitations for bending are the same as those for compression,

$\lambda_p \leq \lambda \leq \lambda_r$; therefore, the section is noncompact for flexure

---

# I-70

**Available Compressive Strength**

Compressive strength for noncompact filled composite members is determined in accordance with AISC *Specification* Section I2.2b(b).

$$P_p = F_y A_s + C_2 f_c'\left(A_c + A_{sr}\frac{E_s}{E_c}\right)$$, where $C_2 = 0.85$ for rectangular sections
$$(Spec. \text{ Eq. I2-9b})$$

$$= (50 \text{ ksi})(59.0 \text{ in.}^2) + 0.85(7 \text{ ksi})(841 \text{ in.}^2 + 0 \text{ in.}^2)$$

$$= 7{,}950 \text{ kips}$$

$$P_y = F_y A_s + 0.7 f_c'\left(A_c + A_{sr}\frac{E_s}{E_c}\right)$$
$$(Spec. \text{ Eq. I2-9d})$$

$$= (50 \text{ ksi})(59.0 \text{ in.}^2) + 0.7(7 \text{ ksi})(841 \text{ in.}^2 + 0 \text{ in.}^2)$$

$$= 7{,}070 \text{ kips}$$

$$P_{no} = P_p - \frac{P_p - P_y}{(\lambda_r - \lambda_p)^2}(\lambda - \lambda_p)^2$$
$$(Spec. \text{ Eq. I2-9c})$$

$$= 7{,}950 \text{ kips} - \left[\frac{7{,}950 \text{ kips} - 7{,}070 \text{ kips}}{(72.2 - 54.4)^2}\right](58.0 - 54.4)^2$$

$$= 7{,}910 \text{ kips}$$

$$C_3 = 0.45 + 3\left(\frac{A_s + A_{sr}}{A_g}\right) \leq 0.9$$
$$(Spec. \text{ Eq. I2-13})$$

$$= 0.45 + 3\left(\frac{59.0 \text{ in.}^2 + 0 \text{ in.}^2}{900 \text{ in.}^2}\right) < 0.9$$

$$= 0.647 < 0.9$$
$$= 0.647$$

$$(EI)_{eff} = E_s I_s + E_c I_{sr} + C_3 E_c I_c$$
$$(Spec. \text{ Eq. I2-12})$$

$$= (29{,}000 \text{ ksi})(8{,}600 \text{ in.}^4) + 0 \text{ kip-in.}^2 + 0.647(4{,}620 \text{ ksi})(58{,}900 \text{ in.}^4)$$

$$= 425{,}000{,}000 \text{ kip-in.}^2$$

$$P_e = \pi^2(EI)_{eff}/L_c^2$$, where $L_c = KL$ and $K = 1.0$ in accordance with the direct analysis method
$$(Spec. \text{ Eq. I2-4})$$

$$= \frac{\pi^2(425{,}000{,}000 \text{ kip-in.}^2)}{[(30 \text{ ft})(12 \text{ in./ft})]^2}$$

$$= 32{,}400 \text{ kips}$$

$$\frac{P_{no}}{P_e} = \frac{7{,}910 \text{ kips}}{32{,}400 \text{ kips}}$$

$$= 0.244 < 2.25$$

Therefore, use AISC *Specification* Equation I2-2.

---

# I-71

$$P_n = P_{no}\left(0.658^{\frac{P_{no}}{P_e}}\right)$$
$$(Spec. \text{ Eq. I2-2})$$

$$= (7{,}910 \text{ kips})(0.658)^{0.244}$$

$$= 7{,}140 \text{ kips}$$

According to AISC *Specification* Section I2.2b, the compressive strength need not be less than that specified for the bare steel member as determined by *Specification* Chapter E. It can be shown that the nominal compressive strength of the bare steel for this section is equal to 1,980 kips, thus the strength of the composite section controls.

The available compressive strength is:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.75$ | $\Omega_c = 2.00$ |
| $\phi_c P_n = 0.75(7{,}140 \text{ kips})$ | $\dfrac{P_n}{\Omega_c} = \dfrac{7{,}140 \text{ kips}}{2.00}$ |
| $= 5{,}360$ kips | $= 3{,}570$ kips |

**Available Flexural Strength**

Flexural strength of noncompact filled composite members is determined in accordance with AISC *Specification* Section I3.4b(b):

$$M_n = M_p - (M_p - M_y)\frac{(\lambda - \lambda_p)}{(\lambda_r - \lambda_p)}$$
$$(Spec. \text{ Eq. I3-5b})$$

In order to utilize Equation I3-3b, both the plastic moment strength of the section, $M_p$, and the yield moment strength of the section, $M_y$, must be calculated.

**Plastic Moment Strength**

The first step in determining the available flexural strength of a noncompact section is to calculate the moment corresponding to the plastic stress distribution over the composite cross section, $M_p$. This concept is illustrated graphically in AISC *Specification* Commentary Figure C-I3.8(a) and follows the force distribution depicted in Figure I.7-2 and detailed in Table I.7-1.

---

# I-72

<table>
<caption><b>Table I.7-1. Plastic Moment Equations</b></caption>
<thead>
<tr>
<th>Component</th>
<th>Force</th>
<th>Moment Arm</th>
</tr>
</thead>
<tbody>
<tr>
<td>Compression in steel flange</td>
<td>$C_1 = b_i t_f F_y$</td>
<td>$y_{C1} = a_p - \dfrac{t_f}{2}$</td>
</tr>
<tr>
<td>Compression in concrete</td>
<td>$C_2 = 0.85f_c'(a_p - t_f)b_i$</td>
<td>$y_{C2} = \dfrac{a_p - t_f}{2}$</td>
</tr>
<tr>
<td>Compression in steel web</td>
<td>$C_3 = a_p 2t_w F_y$</td>
<td>$y_{C3} = \dfrac{a_p}{2}$</td>
</tr>
<tr>
<td>Tension in steel web</td>
<td>$T_1 = (H - a_p)2t_w F_y$</td>
<td>$y_{T1} = \dfrac{H - a_p}{2}$</td>
</tr>
<tr>
<td>Tension in steel flange</td>
<td>$T_2 = b_i t_f F_y$</td>
<td>$y_{T2} = H - a_p - \dfrac{t_f}{2}$</td>
</tr>
<tr>
<td colspan="3">where:<br/>
$a_p = \dfrac{2F_y Ht_w + 0.85f_c' b_i t_f}{4t_w F_y + 0.85f_c' b_i}$<br/>
$M_p = \sum(\text{force})(\text{moment arm})$</td>
</tr>
</tbody>
</table>

Using the equations provided in Table I.7-1 for the section in question results in the following:

$$a_p = \frac{2(50 \text{ ksi})(30 \text{ in.})(\frac{1}{2} \text{ in.}) + 0.85(7 \text{ ksi})(29.0 \text{ in.})(\frac{1}{2} \text{ in.})}{4(\frac{1}{2} \text{ in.})(50 \text{ ksi}) + 0.85(7 \text{ ksi})(29.0 \text{ in.})}$$

$$= 5.82 \text{ in.}$$

![Diagram showing plastic moment stress blocks and force distribution for a box section. Left shows cross-section with dimensions bi = B - 2tw, tf, tw, ap, H - ap, and H. Middle shows stress distribution with steel stress Fy and concrete stress 0.85fc'. Right shows resultant forces C1, C2, C3, T1, T2 with moment arms yC1, yC2, yC3, yT1, yT2 relative to plastic neutral axis]

*Figure I.7-2. Plastic moment stress blocks and force distribution.*

---

# I-73

| Force | Moment Arm | Force × Moment Arm |
|-------|------------|-------------------|
| $C_1 = (29.0 \text{ in.})(\frac{1}{2} \text{ in.})(50 \text{ ksi})$ | $y_{C1} = 5.82 \text{ in.} - \dfrac{\frac{1}{2} \text{ in.}}{2}$ | $C_1y_{C1} = 4{,}040$ kip-in. |
| $= 725$ kips | $= 5.57$ in. | |
| $C_2 = 0.85(7 \text{ ksi})(5.82 \text{ in.} - \frac{1}{2} \text{ in.})(29.0 \text{ in.})$ | $y_{C2} = \dfrac{5.82 \text{ in.} - \frac{1}{2} \text{ in.}}{2}$ | $C_2y_{C2} = 2{,}440$ kip-in. |
| $= 918$ kips | $= 2.66$ in. | |
| $C_3 = (5.82 \text{ in.})(2)(\frac{1}{2} \text{ in.})(50 \text{ ksi})$ | $y_{C3} = \dfrac{5.82 \text{ in.}}{2}$ | $C_3y_{C3} = 847$ kip-in. |
| $= 291$ kips | $= 2.91$ in. | |
| $T_1 = (30 \text{ in.} - 5.82 \text{ in.})(2)(\frac{1}{2} \text{ in.})(50 \text{ ksi})$ | $y_{T1} = \dfrac{30 \text{ in.} - 5.82 \text{ in.}}{2}$ | $T_1y_{T1} = 14{,}600$ kip-in. |
| $= 1{,}210$ kips | $= 12.1$ in. | |
| $T_2 = (29.0 \text{ in.})(\frac{1}{2} \text{ in.})(50 \text{ ksi})$ | $y_{T2} = 30 \text{ in.} - 5.82 \text{ in.} - \dfrac{\frac{1}{2} \text{ in.}}{2}$ | $T_2y_{T2} = 17{,}300$ kip-in. |
| $= 725$ kips | $= 23.9$ in. | |
| $M_p = \sum(\text{force})(\text{moment arm})$ | | |
| $= \dfrac{4{,}040 \text{ kip-in.} + 2{,}440 \text{ kip-in.} + 847 \text{ kip-in.} + 14{,}600 \text{ kip-in.} + 17{,}300 \text{ kip-in.}}{12 \text{ in./ft}}$ | | |
| $= 3{,}270$ kip-ft | | |

**Yield Moment Strength**

The next step in determining the available flexural strength of a noncompact filled member is to determine the yield moment strength. The yield moment is defined in AISC *Specification* Section I3.4b(b) as the moment corresponding to first yield of the compression flange calculated using a linear elastic stress distribution with a maximum concrete compressive stress of $0.7 f_c'$. This concept is illustrated diagrammatically in *Specification* Commentary Figure C-I3.8(b) and follows the force distribution depicted in Figure I.7-3 and detailed in Table I.7-2.

![Diagram showing yield moment stress blocks and force distribution for a box section. Left shows cross-section with dimensions bi = B - 2tw, tf, tw, ay, H - 2ay, and H. Middle shows stress distribution with steel stress Fy, concrete stress 0.70fc'. Right shows resultant forces C1, C2, C3, T1, T2, T3 with moment arms yC1, yC2, yC3, yT1, yT2, yT3 relative to inelastic neutral axis]

*Figure I.7-3. Yield moment stress blocks and force distribution.*

---

# I-74

<table>
<caption><b>Table I.7-2. Yield Moment Equations</b></caption>
<thead>
<tr>
<th>Component</th>
<th>Force</th>
<th>Moment Arm</th>
</tr>
</thead>
<tbody>
<tr>
<td>Compression in steel flange</td>
<td>$C_1 = b_i t_f F_y$</td>
<td>$y_{C1} = a_y - \dfrac{t_f}{2}$</td>
</tr>
<tr>
<td>Compression in concrete</td>
<td>$C_2 = 0.35f_c'(a_y - t_f)b_i$</td>
<td>$y_{C2} = \dfrac{2(a_y - t_f)}{3}$</td>
</tr>
<tr>
<td>Compression in steel web</td>
<td>$C_3 = a_y 2t_w 0.5F_y$</td>
<td>$y_{C3} = \dfrac{2a_y}{3}$</td>
</tr>
<tr>
<td rowspan="2">Tension in steel web</td>
<td>$T_1 = a_y 2t_w 0.5F_y$</td>
<td>$y_{T1} = \dfrac{2a_y}{3}$</td>
</tr>
<tr>
<td>$T_2 = (H - 2a_y)2t_w F_y$</td>
<td>$y_{T2} = \dfrac{H}{2}$</td>
</tr>
<tr>
<td>Tension in steel flange</td>
<td>$T_3 = b_i t_f F_y$</td>
<td>$y_{T3} = H - a_y - \dfrac{t_f}{2}$</td>
</tr>
<tr>
<td colspan="3">where:<br/>
$a_y = \dfrac{2F_y Ht_w + 0.35f_c' b_i t_f}{4t_w F_y + 0.35f_c' b_i}$<br/>
$M_y = \sum(\text{force})(\text{moment arm})$</td>
</tr>
</tbody>
</table>

Using the equations provided in Table I.7-2 for the section in question results in the following:

$$a_y = \frac{2(50 \text{ ksi})(30 \text{ in.})(\frac{1}{2} \text{ in.}) + 0.35(7 \text{ ksi})(29.0 \text{ in.})(\frac{1}{2} \text{ in.})}{4(\frac{1}{2} \text{ in.})(50 \text{ ksi}) + 0.35(7 \text{ ksi})(29.0 \text{ in.})}$$

$$= 8.98 \text{ in.}$$

| Force | Moment Arm | Force × Moment Arm |
|-------|------------|-------------------|
| $C_1 = (29.0 \text{ in.})(\frac{1}{2} \text{ in.})(50 \text{ ksi})$ | $y_{C1} = 8.98 \text{ in.} - \dfrac{\frac{1}{2} \text{ in.}}{2}$ | $C_1y_{C1} = 6{,}330$ kip-in. |
| $= 725$ kips | $= 8.73$ in. | |
| $C_2 = 0.35(7 \text{ ksi})(8.98 \text{ in.} - \frac{1}{2} \text{ in.})(29.0 \text{ in.})$ | $y_{C2} = \dfrac{2(8.98 \text{ in.} - \frac{1}{2} \text{ in.})}{3}$ | $C_2y_{C2} = 3{,}410$ kip-in. |
| $= 603$ kips | $= 5.65$ in. | |
| $C_3 = (8.98 \text{ in.})(2)(\frac{1}{2} \text{ in.})(0.5)(50 \text{ ksi})$ | $y_{C3} = \dfrac{2(8.98 \text{ in.})}{3}$ | $C_3y_{C3} = 1{,}350$ kip-in. |
| $= 225$ kips | $= 5.99$ in. | |
| $T_1 = (8.98 \text{ in.})(2)(\frac{1}{2} \text{ in.})(0.5)(50 \text{ ksi})$ | $y_{T1} = \dfrac{2(8.98 \text{ in.})}{3}$ | $T_1y_{T1} = 1{,}350$ kip-in. |
| $= 225$ kips | $= 5.99$ in. | |
| $T_2 = [30 \text{ in.} - 2(8.98 \text{ in.})](2)(\frac{1}{2} \text{ in.})(50 \text{ ksi})$ | $y_{T2} = \dfrac{30 \text{ in.}}{2}$ | $T_2y_{T2} = 9{,}030$ kip-in. |
| $= 602$ kips | $= 15.0$ in. | |
| $T_3 = (29.0 \text{ in.})(\frac{1}{2} \text{ in.})(50 \text{ ksi})$ | $y_{T3} = 30 \text{ in.} - 8.98 \text{ in.} - \dfrac{\frac{1}{2} \text{ in.}}{2}$ | $T_3y_{T3} = 15{,}100$ kip-in. |
| $= 725$ kips | $= 20.8$ in. | |
| $M_y = \sum(\text{force})(\text{moment arm})$ | | |
| $\dfrac{6{,}330 \text{ kip-in.} + 3{,}410 \text{ kip-in.} + 1{,}350 \text{ kip-in.} + 1{,}350 \text{ kip-in.} + 9{,}030 \text{ kip-in.} + 15{,}100 \text{ kip-in.}}{12 \text{ in./ft}}$ | | |
| $= 3{,}050$ kip-ft | | |

---

# I-75

Now that both $M_p$ and $M_y$ have been determined, Equation I3-5b may be used in conjunction with the flexural slenderness values previously calculated to determine the nominal flexural strength of the composite section as follows:

$$M_n = M_p - (M_p - M_y)\frac{(\lambda - \lambda_p)}{(\lambda_r - \lambda_p)}$$
$$(Spec. \text{ Eq. I3-5b})$$

$$= 3{,}270 \text{ kip-ft} - (3{,}270 \text{ kip-ft} - 3{,}050 \text{ kip-ft})\left(\frac{58.0 - 54.4}{72.2 - 54.4}\right)$$

$$= 3{,}230 \text{ kip-ft}$$

The available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(3{,}230 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{3{,}230 \text{ kip-ft}}{1.67}$ |
| $= 2{,}910$ kip-ft | $= 1{,}930$ kip-ft |

**Interaction of Flexure and Compression**

Design of members for combined forces is performed in accordance with AISC *Specification* Section I5. For filled composite members with noncompact or slender sections, interaction may be determined in accordance with Section H1.1 as follows:

| LRFD | ASD |
|------|-----|
| $P_r = 1{,}310$ kips | $P_a = 1{,}370$ kips |
| $M_u = 552$ kip-ft | $M_a = 248$ kip-ft |
| $\dfrac{P_r}{P_c} = \dfrac{P_u}{\phi_c P_n}$ | $\dfrac{P_r}{P_c} = \dfrac{P_a}{P_n/\Omega_c}$ |
| $= \dfrac{1{,}310 \text{ kips}}{5{,}360 \text{ kips}}$ | $= \dfrac{1{,}370 \text{ kips}}{3{,}570 \text{ kips}}$ |
| $= 0.244 > 0.2$ | $= 0.384 > 0.2$ |
| Therefore, use AISC *Specification* Equation H1-1a. | Therefore, use AISC *Specification* Equation H1-1a. |
| $\dfrac{P_u}{\phi_c P_n} + \dfrac{8}{9}\left(\dfrac{M_u}{\phi_b M_n}\right) \leq 1.0$ (from $Spec.$ Eq. H1-1a) | $\dfrac{P_a}{P_n/\Omega_c} + \dfrac{8}{9}\left(\dfrac{M_a}{M_n/\Omega_b}\right) \leq 1.0$ (from $Spec.$ Eq. H1-1a) |
| $0.244 + \dfrac{8}{9}\left(\dfrac{552 \text{ kip-ft}}{2{,}910 \text{ kip-ft}}\right) \leq 1.0$ | $0.384 + \dfrac{8}{9}\left(\dfrac{248 \text{ kip-ft}}{1{,}930 \text{ kip-ft}}\right) \leq 1.0$ |
| $0.413 < 1.0 \quad \textbf{o.k.}$ | $0.498 < 1.0 \quad \textbf{o.k.}$ |

The composite section is adequate; however, as there is available strength remaining for the trial plate thickness chosen, re-analyze the section to determine the adequacy of a reduced plate thickness.

**Trial Size 2 (Slender)**

---

# I-76

The calculated geometric section properties using a reduced plate thickness of $t = \frac{1}{4}$ in. are:

$B = 30$ in.
$H = 30$ in.
$A_g = 900$ in.²
$A_c = 870$ in.²
$A_s = 29.8$ in.²

$b_i = B - 2t$
$= 30$ in. $- 2(\frac{1}{4}$ in.$)$
$= 29.5$ in.

$h_i = H - 2t$
$= 30$ in. $- 2(\frac{1}{4}$ in.$)$
$= 29.5$ in.

$$E_c = w_c^{1.5}\sqrt{f_c'}$$

$$= (145 \text{ lb/ft}^3)^{1.5}\sqrt{7 \text{ ksi}}$$

$$= 4{,}620 \text{ ksi}$$

$$I_{gx} = \frac{BH^3}{12}$$

$$= \frac{(30 \text{ in.})(30 \text{ in.})^3}{12}$$

$$= 67{,}500 \text{ in.}^4$$

$$I_{cx} = \frac{b_i h_i^3}{12}$$

$$= \frac{(29.5 \text{ in.})(29.5 \text{ in.})^3}{12}$$

$$= 63{,}100 \text{ in.}^4$$

$$I_{sx} = I_{gx} - I_{cx}$$

$$= 67{,}500 \text{ in.}^4 - 63{,}100 \text{ in.}^4$$

$$= 4{,}400 \text{ in.}^4$$

**Limitations of AISC Specification Sections I1.3 and I2.2a**

(1) Concrete Strength: $3 \text{ ksi} \leq f_c' \leq 10$ ksi
$f_c' = 7$ ksi **o.k.**

(2) Specified minimum yield stress of structural steel: $F_y \leq 75$ ksi
$F_y = 50$ ksi **o.k.**

---

# I-77

(3) Cross sectional area of steel section: $A_s \geq 0.01A_g$

$29.8 \text{ in.}^2 \geq (0.01)(900 \text{ in.}^2)$

$> 9.00 \text{ in.}^2 \quad \textbf{o.k.}$

**Classify Section for Local Buckling**

As noted previously, the definitions of width, depth, and thickness used in the evaluation of slenderness are provided in AISC *Specification* Section B4.1b.

For a box column, the slenderness ratio is determined as the ratio of clear distance-to-wall thickness:

$$\lambda = \frac{b_i}{t} = \frac{h_i}{t}$$

$$= \frac{29.5 \text{ in.}}{\frac{1}{4} \text{ in.}}$$

$$= 118$$

Classify section for local buckling in steel elements subject to axial compression from AISC *Specification* Table I1.1a. As determined previously, $\lambda_r = 72.2$.

$$\lambda_{max} = 5.00\sqrt{\frac{E}{F_y}}$$

$$= 5.00\sqrt{\frac{29{,}000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 120$$

$\lambda_r \leq \lambda \leq \lambda_{max}$; therefore, the section is slender for compression

Classification of the section for local buckling in elements subject to flexure occurs separately per AISC *Specification* Table I1.1b. Because the flange limitations for bending are the same as those for compression,

$\lambda_r \leq \lambda \leq \lambda_{max}$; therefore, the section is slender for flexure

**Available Compressive Strength**

Compressive strength for a slender filled member is determined in accordance with AISC *Specification* Section I2.2b(c).

$$F_n = \frac{9E_s}{\lambda^2}$$
$$(Spec. \text{ Eq. I2-10})$$

$$= \frac{9(29{,}000 \text{ ksi})}{(118)^2}$$

$$= 18.7 \text{ ksi}$$

$$P_{no} = F_n A_s + 0.7 f_c'\left(A_c + A_{sr}\frac{E_s}{E_c}\right)$$
$$(Spec. \text{ Eq. I2-9e})$$

$$= (18.7 \text{ ksi})(29.8 \text{ in.}^2) + 0.7(7 \text{ ksi})(870 \text{ in.}^2 + 0 \text{ in.}^2)$$

$$= 4{,}820 \text{ kips}$$

---

# I-78

$$C_3 = 0.45 + 3\left(\frac{A_s + A_{sr}}{A_g}\right) \leq 0.9$$
$$(Spec. \text{ Eq. I2-13})$$

$$= 0.45 + 3\left(\frac{29.8 \text{ in.}^2 + 0 \text{ in.}^2}{900 \text{ in.}^2}\right) \leq 0.9$$

$$= 0.549 < 0.9$$
$$= 0.549$$

$$(EI)_{eff} = E_s I_s + E_c I_{sr} + C_3 E_c I_c$$
$$(Spec. \text{ Eq. I2-12})$$

$$= (29{,}000 \text{ ksi})(4{,}400 \text{ in.}^4) + 0 \text{ kip-in.}^2 + 0.549(4{,}620 \text{ ksi})(63{,}100 \text{ in.}^4)$$

$$= 288{,}000{,}000 \text{ kip-in.}^2$$

$$P_e = \pi^2(EI)_{eff}/L_c^2$$, where $L_c = KL$ and $K = 1.0$ in accordance with the direct analysis method
$$(Spec. \text{ Eq. I2-4})$$

$$= \frac{\pi^2(288{,}000{,}000 \text{ kip-in.}^2)}{[(30 \text{ ft})(12 \text{ in./ft})]^2}$$

$$= 21{,}900 \text{ kips}$$

$$\frac{P_{no}}{P_e} = \frac{4{,}820 \text{ kips}}{21{,}900 \text{ kips}}$$

$$= 0.220 < 2.25$$

Therefore, use AISC *Specification* Equation I2-2.

$$P_n = P_{no}\left(0.658^{\frac{P_{no}}{P_e}}\right)$$
$$(Spec. \text{ Eq. I2-2})$$

$$= (4{,}820 \text{ kips})(0.658)^{0.220}$$

$$= 4{,}400 \text{ kips}$$

According to AISC *Specification* Section I2.2b the compressive strength need not be less than that determined for the bare steel member using *Specification* Chapter E. It can be shown that the nominal compressive strength of the bare steel for this section is equal to 541 kips, thus the strength of the composite section controls.

The available compressive strength is:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.75$ | $\Omega_c = 2.00$ |
| $\phi_c P_n = 0.75(4{,}400 \text{ kips})$ | $\dfrac{P_n}{\Omega_c} = \dfrac{4{,}400 \text{ kips}}{2.00}$ |
| $= 3{,}300$ kips | $= 2{,}200$ kips |

**Available Flexural Strength**

Flexural strength of slender filled composite members is determined in accordance with AISC *Specification* Section I3.4b(c). The nominal flexural strength is determined as the first yield moment, $M_{cr}$, corresponding to a flange compression stress of $F_n$ using a linear elastic stress distribution with a maximum concrete compressive stress of

---

# I-79

$0.7 f_c'$. This concept is illustrated diagrammatically in *Specification* Commentary Figure C-I3.8(c) and follows the force distribution depicted in Figure I.7-4 and detailed in Table I.7-3.

<table>
<caption><b>Table I.7-3. First Yield Moment Equations</b></caption>
<thead>
<tr>
<th>Component</th>
<th>Force</th>
<th>Moment Arm</th>
</tr>
</thead>
<tbody>
<tr>
<td>Compression in steel flange</td>
<td>$C_1 = b_i t_f F_n$</td>
<td>$y_{C1} = a_{cr} - \dfrac{t_f}{2}$</td>
</tr>
<tr>
<td>Compression in concrete</td>
<td>$C_2 = 0.35f_c'(a_{cr} - t_f)b_i$</td>
<td>$y_{C2} = \dfrac{2(a_{cr} - t_f)}{3}$</td>
</tr>
<tr>
<td>Compression in steel web</td>
<td>$C_3 = a_{cr} 2t_w 0.5F_n$</td>
<td>$y_{C3} = \dfrac{2a_{cr}}{3}$</td>
</tr>
<tr>
<td>Tension in steel web</td>
<td>$T_1 = (H - a_{cr})2t_w 0.5F_y$</td>
<td>$y_{T1} = \dfrac{2(H - a_{cr})}{3}$</td>
</tr>
<tr>
<td>Tension in steel flange</td>
<td>$T_2 = b_i t_f F_y$</td>
<td>$y_{T2} = H - a_{cr} - \dfrac{t_f}{2}$</td>
</tr>
<tr>
<td colspan="3">where:<br/>
$a_{cr} = \dfrac{F_y Ht_w + (0.35f_c' + F_n - F_n)b_i t_f}{t_w(F_n + F_y) + 0.35f_c' b_i}$<br/>
$M_{cr} = \sum(\text{force})(\text{moment arm})$</td>
</tr>
</tbody>
</table>

Using the equations provided in Table I.7-3 for the section in question results in the following:

$$a_{cr} = \frac{(50 \text{ ksi})(30 \text{ in.})(\frac{1}{4} \text{ in.}) + [0.35(7 \text{ ksi}) + 50 \text{ ksi} - 18.7 \text{ ksi}](29.5 \text{ in.})(\frac{1}{4} \text{ in.})}{(\frac{1}{4} \text{ in.})(18.7 \text{ ksi} + 50 \text{ ksi}) + 0.35(7 \text{ ksi})(29.5 \text{ in.})}$$

$$= 6.97 \text{ in.}$$

![Diagram showing first yield moment stress blocks and force distribution for a box section. Left shows cross-section with dimensions bi = B - 2tw, tf, tw, acr, H - acr, and H. Middle shows stress distribution with steel stress Fy and 0.70fc', concrete stress 0.70fc'. Right shows resultant forces C1, C2, C3, T1, T2 with moment arms yC1, yC2, yC3, yT1, yT2 relative to elastic neutral axis]

*Figure I.7-4. First yield moment stress blocks and force distribution.*

---

# I-80

| Force | Moment Arm | Force × Moment Arm |
|-------|------------|-------------------|
| $C_1 = (29.5 \text{ in.})(\frac{1}{4} \text{ in.})(18.7 \text{ ksi})$ | $y_{C1} = 6.97 \text{ in.} - \dfrac{\frac{1}{4} \text{ in.}}{2}$ | $C_1y_{C1} = 945$ kip-in. |
| $= 138$ kips | $= 6.85$ in. | |
| $C_2 = 0.35(7 \text{ ksi})(6.97 \text{ in.} - \frac{1}{4} \text{ in.})(29.5 \text{ in.})$ | $y_{C2} = \dfrac{2(6.97 \text{ in.} - \frac{1}{4} \text{ in.})}{3}$ | $C_2y_{C2} = 2{,}180$ kip-in. |
| $= 486$ kips | $= 4.48$ in. | |
| $C_3 = (6.97 \text{ in.})(2)(\frac{1}{4} \text{ in.})(0.5)(18.7 \text{ ksi})$ | $y_{C3} = \dfrac{2(6.97 \text{ in.})}{3}$ | $C_3y_{C3} = 152$ kip-in. |
| $= 32.6$ kips | $= 4.65$ in. | |
| $T_1 = (30 \text{ in.} - 6.97 \text{ in.})(2)(\frac{1}{4} \text{ in.})(0.5)(50 \text{ ksi})$ | $y_{T1} = \dfrac{2(30 \text{ in.} - 6.97 \text{ in.})}{3}$ | $T_1y_{T1} = 4{,}440$ kip-in. |
| $= 288$ kips | $= 15.4$ in. | |
| $T_2 = (29.5 \text{ in.})(\frac{1}{4} \text{ in.})(50 \text{ ksi})$ | $y_{T2} = 30 \text{ in.} - 6.97 \text{ in.} - \dfrac{\frac{1}{4} \text{ in.}}{2}$ | $T_2y_{T2} = 8{,}450$ kip-in. |
| $= 369$ kips | $= 22.9$ in. | |
| $M_{cr} = \sum(\text{force component})(\text{moment arm})$ | | |
| $= \dfrac{945 \text{ kip-in.} + 2{,}180 \text{ kip-in.} + 152 \text{ kip-in.} + 4{,}440 \text{ kip-in.} + 8{,}450 \text{ kip-in.}}{12 \text{ in./ft}}$ | | |
| $= 1{,}350$ kip-ft | | |

The available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $M_n = 0.90(1{,}350 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{1{,}350 \text{ kip-ft}}{1.67}$ |
| $= 1{,}220$ kip-ft | $= 808$ kip-ft |

**Interaction of Flexure and Compression**

The interaction of flexure and compression may be determined in accordance with AISC *Specification* Section H1.1 as follows:

| LRFD | ASD |
|------|-----|
| $P_u = 1{,}310$ kips | $P_a = 1{,}370$ kips |
| $M_u = 552$ kip-ft | $M_a = 248$ kip-ft |
| $\dfrac{P_r}{P_c} = \dfrac{P_u}{\phi_c P_n}$ | $\dfrac{P_r}{P_c} = \dfrac{P_a}{P_n/\Omega_c}$ |
| $= \dfrac{1{,}310 \text{ kips}}{3{,}300 \text{ kips}}$ | $= \dfrac{1{,}370 \text{ kips}}{2{,}200 \text{ kips}}$ |
| $= 0.397 > 0.2$ | $= 0.623 > 0.2$ |

---

# I-81

| LRFD | ASD |
|------|-----|
| Therefore, use AISC *Specification* Equation H1-1a. | Therefore, use AISC *Specification* Equation H1-1a. |
| $\dfrac{P_u}{\phi_c P_n} + \dfrac{8}{9}\left(\dfrac{M_u}{\phi_b M_n}\right) \leq 1.0$ (from $Spec.$ Eq. H1-1a) | $\dfrac{P_a}{P_n/\Omega_c} + \dfrac{8}{9}\left(\dfrac{M_a}{M_n/\Omega_b}\right) \leq 1.0$ (from $Spec.$ Eq. H1-1a) |
| $0.397 + \dfrac{8}{9}\left(\dfrac{552 \text{ kip-ft}}{1{,}220 \text{ kip-ft}}\right) \leq 1.0$ | $0.623 + \dfrac{8}{9}\left(\dfrac{248 \text{ kip-ft}}{808 \text{ kip-ft}}\right) \leq 1.0$ |
| $0.799 < 1.0 \quad \textbf{o.k.}$ | $0.896 < 1.0 \quad \textbf{o.k.}$ |

Thus, a plate thickness of $\frac{1}{4}$ in. is adequate.

Note that in addition to the design checks performed for the composite condition, design checks for other load stages should be performed as required by AISC *Specification* Section I1. These checks should take into account the effect of hydrostatic loads from concrete placement, as well as the strength of the steel section alone prior to composite action.

**Available Shear Strength**

The available shear strength is determined using AISC *Specification* Section I4.2. The area of concrete, $A_c$, equals 870 in.² The shear area of the steel section is determined as follows:

$$h = H - 3t$$
$$= 30.0 \text{ in.} - 3(\frac{1}{4} \text{ in.})$$
$$= 29.3 \text{ in.}$$

$$A_v = 2ht$$
$$= 2(29.3 \text{ in.})(\frac{1}{4} \text{ in.})$$
$$= 14.7 \text{ in.}^2$$

Determine the shear span-to-depth:

| LRFD | ASD |
|------|-----|
| $\dfrac{(M_u/V_u)}{d} = \dfrac{[552 \text{ kip-ft}(12 \text{ in./ft})/36.8 \text{ kips}]}{30 \text{ in.}}$ | $\dfrac{(M_a/V_a)}{d} = \dfrac{[248 \text{ kip-ft}(12 \text{ in./ft})/22.1 \text{ kips}]}{30 \text{ in.}}$ |
| $= 6.00$ | $= 4.49$ |
| Because $(M_u/V_u)/d > 0.7$: | Because $(M_a/V_a)/d > 0.7$: |
| $K_v = 1$ | $K_v = 1$ |

$$V_n = 0.6A_v F_y + 0.06K_v A_c\sqrt{f_c'}$$
$$(Spec. \text{ Eq. I4-1})$$

$$= 0.6(14.7 \text{ in.}^2)(50 \text{ ksi}) + 0.06(1)(870 \text{ in.}^2)\sqrt{7 \text{ ksi}}$$

$$= 441 \text{ kips} + 138 \text{ kips}$$
$$= 579 \text{ kips}$$

The available shear strength is:

---

# I-82

| LRFD | ASD |
|------|-----|
| $\phi_v = 0.90$ | $\Omega_v = 1.67$ |
| $\phi_v V_n = 0.90(579 \text{ kips})$ | $\dfrac{V_n}{\Omega_v} = \dfrac{579 \text{ kips}}{1.67}$ |
| $= 521 \text{ kips} > 36.8 \text{ kips} \quad \textbf{o.k.}$ | $= 347 \text{ kips} > 22.1 \text{ kips} \quad \textbf{o.k.}$ |

**Force Allocation and Load Transfer**

Load transfer calculations for applied axial forces should be performed in accordance with AISC *Specification* Section I6. The specific application of the load transfer provisions is dependent upon the configuration and detailing of the connecting elements. Expanded treatment of the application of load transfer provisions is provided in Example I.3.

**Summary**

It has been determined that a 30 in. × 30 in. composite box column composed of $\frac{1}{4}$-in.-thick plate is adequate for the imposed loads.

---

# I-83

# EXAMPLE I.8 ENCASED COMPOSITE MEMBER FORCE ALLOCATION AND LOAD TRANSFER

## Given:

Refer to Figure I.8-1.

**Part I:** For each loading condition (a) through (c), determine the required longitudinal shear force, $V_r'$, to be transferred between the embedded steel section and concrete encasement.

**Part II:** For loading condition (b), investigate the force transfer mechanisms of direct bearing and shear connection.

The composite member consists of an ASTM A992/A992M W-shape encased by normal weight (145 lb/ft³) reinforced concrete having a specified concrete compressive strength, $f_c' = 5$ ksi.

Deformed reinforcing bars conform to ASTM A615/A615M with a minimum yield stress, $F_{yr}$, of 60 ksi.

Applied loading, $P_r$, for each condition illustrated in Figure I.8-1 is composed of the following loads:

$P_D = 260$ kips
$P_L = 780$ kips

![Diagram showing encased composite member with W10×45 section, (8)#8 BARS, dimensions h1 = 24", h2 = 24", and three loading conditions:
(a) External force to steel only - showing PT applied to steel section
(b) External force to concrete only - showing PT applied to concrete
(c) External force to both materials concurrently - showing PT applied to rigid cap plate on top of combined section
Sections (a) thru (c) shown at bottom]

*Fig. I.8-1. Encased composite member in compression.*

---

# I-84

## Solution:

## Part I—Force Allocation

From AISC *Manual* Table 2-4, the steel material properties are:

ASTM A992/A992M
$F_y = 50$ ksi

From AISC *Manual* Table 1-1 and Figure I.8-1, the geometric properties of the encased W10×45 are as follows:

$A_s = 13.3$ in.²
$b_f = 8.02$ in.
$t_f = 0.620$ in.
$t_w = 0.350$ in.
$d = 10.1$ in.
$h_1 = 24$ in.
$h_2 = 24$ in.

Additional geometric properties of the composite section used for force allocation and load transfer are calculated as follows:

$$A_g = h_1 h_2$$
$$= (24 \text{ in.})(24 \text{ in.})$$
$$= 576 \text{ in.}^2$$

$A_{sri} = 0.79$ in.² for a No. 8 bar

$$A_{sr} = \sum_{i=1}^{n} A_{sri}$$

$$= 8(0.79 \text{ in.}^2)$$

$$= 6.32 \text{ in.}^2$$

$$A_c = A_g - A_s - A_{sr}$$

$$= 576 \text{ in.}^2 - 13.3 \text{ in.}^2 - 6.32 \text{ in.}^2$$

$$= 556 \text{ in.}^2$$

where
$A_c$ = cross-sectional area of concrete encasement, in.²
$A_g$ = gross cross-sectional area of composite section, in.²
$A_{sri}$ = cross-sectional area of reinforcing bar $i$, in.²
$A_{sr}$ = cross-sectional area of continuous reinforcing bars, in.²
$n$ = number of continuous reinforcing bars in composite section

From ASCE/SEI 7, Chapter 2, the required strength is:

---

# I-85

| LRFD | ASD |
|------|-----|
| $P_r = P_u$ | $P_r = P_a$ |
| $= 1.2(260 \text{ kips}) + 1.6(780 \text{ kips})$ | $= 260 \text{ kips} + 780 \text{ kips}$ |
| $= 1{,}560$ kips | $= 1{,}040$ kips |

**Composite Section Strength for Force Allocation**

In accordance with AISC *Specification* Section I6, force allocation calculations are based on the nominal axial compressive strength of the encased composite member without length effects, $P_{no}$. This section strength is defined in Section I2.1b as:

$$P_{no} = F_y A_s + F_{ysr} A_{sr} + 0.85 f_c' A_c$$
$$(Spec. \text{ Eq. I2-7})$$

$$= (50 \text{ ksi})(13.3 \text{ in.}^2) + (60 \text{ ksi})(6.32 \text{ in.}^2) + 0.85(5 \text{ ksi})(556 \text{ in.}^2)$$

$$= 3{,}410 \text{ kips}$$

**Transfer Force for Condition (a)**

Refer to Figure I.8-1(a). For this condition, the entire external force is applied to the steel section only, and the provisions of AISC *Specification* Section I6.2a apply.

$$V_r' = P_r\left(1 - \frac{F_y A_s}{P_{no}}\right)$$
$$(Spec. \text{ Eq. I6-1})$$

$$= P_r\left[1 - \frac{(50 \text{ ksi})(13.3 \text{ in.}^2)}{3{,}410 \text{ kips}}\right]$$

$$= 0.805P_r$$

| LRFD | ASD |
|------|-----|
| $V_r' = 0.805(1{,}560 \text{ kips})$ | $V_r' = 0.805(1{,}040 \text{ kips})$ |
| $= 1{,}260$ kips | $= 837$ kips |

**Transfer Force for Condition (b)**

Refer to Figure I.8-1(b). For this condition, the entire external force is applied to the concrete encasement only, and the provisions of AISC *Specification* Section I6.2b apply.

$$V_r' = P_r\left(\frac{F_y A_s}{P_{no}}\right)$$
$$(Spec. \text{ Eq. I6-2a})$$

$$= P_r\left[\frac{(50 \text{ ksi})(13.3 \text{ in.}^2)}{3{,}410 \text{ kips}}\right]$$

$$= 0.195P_r$$

| LRFD | ASD |
|------|-----|
| $V_r' = 0.195(1{,}560 \text{ kips})$ | $V_r' = 0.195(1{,}040 \text{ kips})$ |
| $= 304$ kips | $= 203$ kips |

---

# I-86

**Transfer Force for Condition (c)**

Refer to Figure I.8-1(c). For this condition, external force is applied to the steel section and concrete encasement concurrently, and the provisions of AISC *Specification* Section I6.2c apply.

AISC *Specification* Commentary Section I6.2 states that when loads are applied to both the steel section and concrete encasement concurrently, $V_r'$ can be taken as the difference in magnitudes between the portion of the external force applied directly to the steel section and that required by Equation I6-2a. This concept can be written in equation form as follows:

$$V_r' = \left|P_{rs} - P_r\left(\frac{F_y A_s}{P_{no}}\right)\right|$$
$$(Eq. 1)$$

where
$P_{rs}$ = portion of external force applied directly to the steel section, kips

Currently, the *Specification* provides no specific requirements for determining the distribution of the applied force for the determination of $P_{rs}$, so it is left to engineering judgment. For a bearing plate condition such as the one represented in Figure I.8-1(c), one possible method for determining the distribution of applied forces is to use an elastic distribution based on the material axial stiffness ratios as follows:

$$E_c = w_c^{1.5}\sqrt{f_c'}$$

$$= (145 \text{ lb/ft}^3)^{1.5}\sqrt{5 \text{ ksi}}$$

$$= 3{,}900 \text{ ksi}$$

$$P_{rs} = \left(\frac{E_s A_s}{E_s A_s + E_c A_c + E_{sr} A_{sr}}\right)P_r$$

$$= \left[\frac{(29{,}000 \text{ ksi})(13.3 \text{ in.}^2)}{(29{,}000 \text{ ksi})(13.3 \text{ in.}^2) + (3{,}900 \text{ ksi})(556 \text{ in.}^2) + (29{,}000 \text{ ksi})(6.32 \text{ in.}^2)}\right]P_r$$

$$= 0.141P_r$$

Substituting the results into Equation 1 yields:

$$V_r' = \left|0.141P_r - P_r\left(\frac{F_y A_s}{P_{no}}\right)\right|$$

$$= \left|0.141P_r - P_r\left[\frac{(50 \text{ ksi})(13.3 \text{ in.}^2)}{3{,}410 \text{ kips}}\right]\right|$$

$$= 0.0540P_r$$

| LRFD | ASD |
|------|-----|
| $V_r' = 0.0540(1{,}560 \text{ kips})$ | $V_r' = 0.0540(1{,}040 \text{ kips})$ |
| $= 84.2$ kips | $= 56.2$ kips |

An alternate approach would be use of a plastic distribution method whereby the load is partitioned to each material in accordance with their contribution to the composite section strength given in Equation I2-4. This method eliminates

---

# I-87

the need for longitudinal shear transfer, provided the local bearing strength of the concrete and steel are adequate to resist the forces resulting from this distribution.

**Additional Discussion**

• The design and detailing of the connections required to deliver external forces to the composite member should be performed according to the applicable provisions of AISC *Specification* Chapters J and K.

• The connection cases illustrated by Figure I.8-1 are idealized conditions representative of the mechanics of actual connections. For instance, a standard angle connection welded to the flange of an encased W-shape is an example of a condition where it may be assumed that all external force is applied directly to the steel section only.

## Solution:

## Part II—Load Transfer

The required longitudinal force to be transferred, $V_r'$, determined in Part I condition (b) is used to investigate the applicable force transfer mechanisms of AISC *Specification* Section I6.3: direct bearing and shear connection. As indicated in the *Specification*, these force transfer mechanisms may not be superimposed; however, the mechanism providing the greatest available strength is allowed. Force transfer using direct bond interaction is not applicable for encased composite members because the variability of column sections and connection configurations makes confirmation of end-bearing impractical; thus, direct bond interaction is limited to filled HSS members as described in Section I6.3c.

**Direct Bearing**

**Determination of Bearing Plates**

One method of utilizing direct bearing as a load transfer mechanism is through the use of internal bearing plates placed between the flanges of the W-shape as indicated in Figure I.8-2.

Internal bearing plates should be located within a load introduction length as discussed in AISC *Specification* Section I6.4b. The load introduction length is two times the least overall dimension of the composite member measured above and below the point of force transfer. Because the composite member only extends to one side of the point of force transfer, the steel anchors are located within $2h_2 = 48$ in. of the top of the composite member.

For rectangular sections, the area of concrete available to resist local bearing strength of the concrete and steel are adequate to resist the forces resulting from this distribution. Local bearing strength should be evaluated with consideration of the effects and magnitude of bearing stresses and confinement provided by the load transfer mechanism used. This can be accomplished through the bearing plate spacing of $24$ in. as $t = 7$ in. in accordance with AISC *Specification* Section I8.2b. Because the composite member area is adequately proportioned to utilize the full bearing capacity of the plates, where multiple sets of bearing plates are used, the distance to the first group of plates above the point of load transfer shall be used in place of the load introduction length when determining the nominal bearing strength. This concept is illustrated diagrammatically in AISC *Specification* Commentary Figure C-I3.8(a) and follows the force distribution depicted in Figure I.8-2.

---

# I-88

$$a = \frac{b_f - t_w}{2}$$

$$= \frac{8.02 \text{ in.} - 0.350 \text{ in.}}{2}$$

$$= 3.84 \text{ in.}$$

$$b = d - 2t_f$$

$$= 10.1 \text{ in.} - 2(0.620 \text{ in.})$$

$$= 8.86 \text{ in.}$$

$c =$ width of clipped corners
$= \frac{3}{4}$ in.

![Diagram showing composite member with internal bearing plates. Elevation view shows h2 = 24", load introduction length, 2h2 = 48", with Pr at top, concrete column above, T/Slab section, encased W10 section, and section A-A marker. Cross-section A-A shows dimensions b, a, with ¾" clipped corners (typ.) and concrete encasement]

*Fig. I.8-2. Composite member with internal bearing plates.*

Note: Reinforcing bars not shown for clarity.

---

# I-89

$$A_1 = \left[2ab - 2c^2\right](\text{number of bearing plate sets})$$

$$= \left[2(3.84 \text{ in.})(8.86 \text{ in.}) - 2(\frac{3}{4} \text{ in.})^2\right](2)$$

$$= 134 \text{ in.}^2$$

The available strength for the direct bearing force transfer mechanism is:

$$R_n = 1.7 f_c' A_1$$
$$(Spec. \text{ Eq. I6-3})$$

$$= 1.7(5 \text{ ksi})(134 \text{ in.}^2)$$

$$= 1{,}140 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.65$ | $\Omega_b = 2.31$ |
| $\phi_b R_n = 0.65(1{,}140 \text{ kips})$ | $\dfrac{R_n}{\Omega_b} = \dfrac{1{,}140 \text{ kips}}{2.31}$ |
| $= 741 \text{ kips} > V_r' = 304 \text{ kips} \quad \textbf{o.k.}$ | $= 494 \text{ kips} > V_r' = 203 \text{ kips} \quad \textbf{o.k.}$ |

Thus, two sets of bearing plates are adequate. From these calculations, it can be seen that one set of bearing plates are adequate for force transfer purposes; however, the use of two sets of bearing plates serves to reduce the bearing plate thickness calculated in the following section.

**Required Bearing Plate Thickness**

There are several methods available for determining the bearing plate thickness. For rectangular plates supported on three sides, elastic solutions for plate stresses, such as those found in *Roark's Formulas for Stress and Strain* (Young and Budynas, 2002), may be used in conjunction with AISC *Specification* Section F12 for thickness calculations. Alternately, yield line theory or computational methods such as finite element analysis may be employed.

For this example, yield line theory is employed. Results of the yield line analysis depend on an assumption of column flange strength versus bearing plate strength in order to estimate the fixity of the bearing plate to column flange connection. In general, if the thickness of the bearing plate is less than the column flange thickness, fixity and plastic hinging can occur at this interface; otherwise, this condition is conservative. Ignoring the fillets of the W-shape and clipped corners on the bearing plate, the yield line pattern chosen for the fixed condition is depicted in Figure I.8-3. Note that the simplifying assumption of $45°$ yield lines illustrated in Figure I.8-3 has been shown to provide reasonably accurate results (Park and Gamble, 2000), and that this yield line pattern is only valid where $b \geq 2a$.

The plate thickness using $F_y = 50$ ksi material may be determined as:

| LRFD | ASD |
|------|-----|
| $\phi = 0.90$ | $\Omega = 1.67$ |
| If $t_p \geq t_f$: | If $t_p \geq t_f$: |
| $t_p = \sqrt{\dfrac{2a^2 w_u(3b - 2a)}{3\phi F_y(4a + b)}}$ | $t_p = \sqrt{\left(\dfrac{2\Omega}{3F_y}\right)\left[\dfrac{a^2 w_a(3b - 2a)}{(4a + b)}\right]}$ |

---

# I-90

| LRFD | ASD |
|------|-----|
| If $t_p < t_f$: | If $t_p < t_f$: |
| $t_p = \sqrt{\dfrac{2a^2 w_u(3b - 2a)}{3\phi F_y(6a + b)}}$ | $t_p = \sqrt{\left(\dfrac{2\Omega}{3F_y}\right)\left[\dfrac{a^2 w_a(3b - 2a)}{(6a + b)}\right]}$ |
| where | where |
| $w_u$ = bearing pressure on plate determined | $w_a$ = bearing pressure on plate determined |
| using LRFD load combinations | using ASD load combinations |
| $= \dfrac{V_r'}{A_1}$ | $= \dfrac{V_r'}{A_1}$ |
| $= \dfrac{304 \text{ kips}}{134 \text{ in.}^2}$ | $= \dfrac{203 \text{ kips}}{134 \text{ in.}^2}$ |
| $= 2.27$ ksi | $= 1.51$ ksi |
| Assuming $t_p \geq t_f$ | Assuming $t_p \geq t_f$ |
| $t_p = \sqrt{\dfrac{2(3.84 \text{ in.})^2(2.27 \text{ ksi})}{\times[3(8.86 \text{ in.}) - 2(3.84 \text{ in.})]}{3(0.90)(50 \text{ ksi})[4(3.84 \text{ in.}) + 8.86 \text{ in.}]}}$ | $t_p = \sqrt{\dfrac{2(1.67)(3.84 \text{ in.})^2(1.51 \text{ ksi})}{\times[3(8.86 \text{ in.}) - 2(3.84 \text{ in.})]}{3(50 \text{ ksi})[4(3.84 \text{ in.}) + 8.86 \text{ in.}]}}$ |
| $= 0.622$ in. | $= 0.622$ in. |
| Select a ⅝ in. plate | Select a ⅝ in. plate |
| $t_p = \frac{5}{8}$ in. $> t_f = 0.620$ in. **assumption o.k.** | $t_p = \frac{5}{8}$ in. $> t_f = 0.620$ in. **assumption o.k.** |

Thus, select ⅝-in.-thick bearing plates.

![Diagram showing internal bearing plate yield line pattern (fixed condition). Square plate with dimensions a on all four sides and b in center, showing 45° yield lines (typ.) forming a pattern around the perimeter]

*Fig. I.8-3. Internal bearing plate yield line pattern (fixed condition).*

---

# I-91

**Bearing Plate to Encased Steel Member Weld**

The bearing plates should be connected to the encased steel member using welds designed in accordance with AISC *Specification* Chapter J to develop the full strength of the plate. For fillet welds, a weld size of $\frac{5}{16}$ will serve to develop the strength of either a 36 or 50 ksi plate as discussed in AISC *Manual* Part 10.

**Shear Connection**

Shear connection involves the use of steel headed stud or channel anchors placed on at least two faces of the steel shape in a generally symmetric configuration to transfer the required longitudinal shear force. For this example, $\frac{3}{4}$-in.-diameter × $4\frac{5}{16}$-in.-long steel headed stud anchors composed of ASTM A29/A29M material with $F_u = 65$ ksi are selected.

**Available Shear Strength of Steel Headed Stud Anchors**

The available shear strength of an individual steel headed stud anchor is determined in accordance with the composite component provisions of AISC *Specification* Section I8.3 as directed by Section I6.3b.

$$Q_{nv} = F_u A_{sa}$$
$$(Spec. \text{ Eq. I8-3})$$

$$A_{sa} = \frac{\pi(\frac{3}{4} \text{ in.})^2}{4}$$

$$= 0.442 \text{ in.}^2$$

| LRFD | ASD |
|------|-----|
| $\phi_s = 0.65$ | $\Omega_s = 2.31$ |
| $\phi_s Q_{nv} = 0.65(65 \text{ ksi})(0.442 \text{ in.}^2)$ | $\dfrac{Q_{nv}}{\Omega_s} = \dfrac{(65 \text{ ksi})(0.442 \text{ in.}^2)}{2.31}$ |
| $= 18.7$ kips per steel headed stud anchor | $= 12.4$ kips per steel headed stud anchor |

**Required Number of Steel Headed Stud Anchors**

The number of steel headed stud anchors required to transfer the longitudinal shear is calculated as follows:

| LRFD | ASD |
|------|-----|
| $n_{anchors} = \dfrac{V_r'}{\phi_s Q_{nv}}$ | $n_{anchors} = \dfrac{V_r'}{Q_{nv}/\Omega_s}$ |
| $= \dfrac{304 \text{ kips}}{18.7 \text{ kips}}$ | $= \dfrac{203 \text{ kips}}{12.4 \text{ kips}}$ |
| $= 16.3$ steel headed stud anchors | $= 16.4$ steel headed stud anchors |

With anchors placed in pairs on each flange, select 20 anchors to satisfy the symmetry provisions of AISC *Specification* Section I6.4a.

**Placement of Steel Headed Stud Anchors**

Steel headed stud anchors are placed within the load introduction length in accordance with AISC *Specification* Section I6.4a. Because the composite member only extends to one side of the point of force transfer, the steel anchors are located within $2h_2 = 48$ in. of the top of the composite member.

---

# I-92

Placing two anchors on each flange provides four anchors per group, and maximum stud spacing within the load introduction length is determined as:

$$s_{max} = \frac{\text{load introduction length} - \text{distance to first anchor group from upper end of encased shape}}{\left[\dfrac{\text{total number of anchors}}{\text{number of anchors per group}}\right] - 1}$$

$$= \frac{48 \text{ in.} - 6 \text{ in.}}{\left[\dfrac{20 \text{ anchors}}{4 \text{ anchors per group}}\right] - 1}$$

$$= 10.5 \text{ in.}$$

Use 10 in. spacing beginning 6 in. from top of encased member.

In addition to anchors placed within the load introduction length, anchors must also be placed along the remainder of the composite member at a maximum spacing of 32 times the anchor shank diameter = 24 in. in accordance with AISC *Specification* Sections I6.4a and I8.3e.

The chosen anchor layout and spacing is illustrated in Figure I.8-4.

**Steel Headed Stud Anchor Detailing Limitations of AISC Specification Sections I6.4a, I8.1, and I8.3**

Steel headed stud anchor detailing limitations are reviewed in this section with reference to the anchor configuration provided in Figure I.8-4 for anchors having a shank diameter, $d_{sa} = \frac{3}{4}$ in. Note that these provisions are specific to the detailing of the anchors themselves and that additional limitations for the structural steel, concrete, and reinforcing components of composite members should be reviewed as demonstrated in Design Example I.9.

(1) Anchors must be placed on at least two faces of the steel shape in a generally symmetric configuration:

Anchors are located in pairs on both faces. **o.k.**

(2) Maximum anchor diameter: $d_{sa} \leq 2.5(t_f)$

$\frac{3}{4}$ in. $< 2.5(0.620$ in.$) = 1.55$ in. **o.k.**

(3) Minimum steel headed stud anchor height-to-diameter ratio: $h/d_{sa} \geq 5$

The minimum ratio of installed anchor height (base to top of head), $h$, to shank diameter, $d_{sa}$, must meet the provisions of AISC *Specification* Section I8.3 as summarized in the User Note table at the end of the section. For shear in normal weight concrete the limiting ratio is five. As previously discussed, a $4\frac{5}{16}$-in.-long anchor was selected from anchor manufacturer's data. As the $h/d_{sa}$ ratio is based on the installed length, a length reduction for burn off during installation of ⅜ in. is taken to yield the installed length of 4 in.

$$\frac{h}{d_{sa}} = \frac{4 \text{ in.}}{\frac{3}{4} \text{ in.}}$$

$$= 5.33 > 5 \quad \textbf{o.k.}$$

(4) Minimum lateral clear concrete cover = 1½ in.

From AWS D1.1/D1.1M (AWS, 2020) Figure 9.1, the head diameter of a ¾ in. diameter stud anchor is equal to 1.25 in.

---

# I-93

$$\text{lateral clear cover} = \left(\frac{h_1}{2}\right) - \left(\frac{\text{lateral spacing between anchor centerlines}}{2}\right) - \left(\frac{\text{anchor head diameter}}{2}\right)$$

$$= \left(\frac{24 \text{ in.}}{2}\right) - \left(\frac{4 \text{ in.}}{2}\right) - \left(\frac{1.25 \text{ in.}}{2}\right)$$

$$= 9.38 \text{ in.} > 1\frac{1}{2} \text{ in.} \quad \textbf{o.k.}$$

![Detailed elevation and section views of composite member with steel anchors. Elevation shows h2 = 24", Pr at top, concrete column above, T/Slab section, encased W10, load introduction length 2h2 = 48" with 4 @ 10" anchor pairs spaced at 6" intervals, single anchors outside of load introduction length (typ.), and section B-B markers. Section B-B shows ¾"×4⅝" steel headed stud anchors in pairs (4 @ 10" Anchor pairs) with 2" spacing, embedded in 24" (typ.) concrete encasement]

*Fig. I.8-4. Composite member with steel anchors.*

Note: Reinforcing bars not shown for clarity.

---

# I-94

(5) Minimum anchor spacing:

$$s_{min} = 4d_{sa}$$
$$= 4(\frac{3}{4} \text{ in.})$$
$$= 3.00 \text{ in.}$$

In accordance with AISC *Specification* Section I8.3e, this spacing limit applies in any direction.

$s_{transverse} = 4$ in. $> s_{min}$ **o.k.**
$s_{longitudinal} = 10$ in. $> s_{min}$ **o.k.**

(6) Maximum anchor spacing:

$$s_{max} = 32d_{sa}$$
$$= 32(\frac{3}{4} \text{ in.})$$
$$= 24.0 \text{ in.}$$

In accordance with AISC *Specification* Section I6.4a, the spacing limits of Section I8.3e apply to steel anchor spacing both within and outside of the load introduction region.

$s = 24.0$ in. $\leq s_{max}$ **o.k.**

(7) Clear cover above the top of the steel headed stud anchors:

AISC *Specification* Section I8.3e specifies that the minimum concrete cover to steel anchors shall be in accordance with ACI 318 provisions for concrete protection of headed shear stud reinforcement. From ACI 318 (ACI, 2019), Sections 20.5.1.3.1 and 20.5.1.3.6, for concrete columns the specified clear cover is 1½ in.

$$\text{clear cover above anchor} = \frac{h_2}{2} - \frac{d}{2} - \text{installed anchor length}$$

$$= \frac{24 \text{ in.}}{2} - \frac{10.1 \text{ in.}}{2} - 4 \text{ in.}$$

$$= 2.95 \text{ in.} > 1\frac{1}{2} \text{ in.} \quad \textbf{o.k.}$$

**Concrete Breakout**

AISC *Specification* Section I8.3a states that in order to use Equation I8-3 for shear strength calculations as previously demonstrated, concrete breakout strength in shear must not be an applicable limit state. If concrete breakout is deemed to be an applicable limit state, the *Specification* provides two alternate paths; either the concrete breakout strength can be determined explicitly using ACI 318, Chapter 17, in accordance with *Specification* Section I8.3a(b), or anchor reinforcement can be provided to resist the entire shear force as discussed in *Specification* Section I8.3a(a).

Determining whether concrete breakout is a viable failure mode is left to the engineer. According to AISC *Specification* Commentary Section I8.3, "it is important that it be deemed by the engineer that a concrete breakout failure mode in shear is directly avoided through having the edges perpendicular to the line of force supported, and the edges parallel to the line of force sufficiently distant that concrete breakout through a side edge is not deemed viable."

For the composite member being designed, no free edge exists in the direction of shear transfer along the length of the column, and concrete breakout in this direction is not an applicable limit state. However, it is still incumbent upon the engineer to review the possibility of concrete breakout through a side edge parallel to the line of force.

---

# I-95

One method for explicitly performing this check is through the use of the provisions of ACI 318, Chapter 17, as follows:

ACI 318, Section 17.7.2.1(c), specifies that concrete breakout shall be checked for shear force parallel to the edge of a group of anchors using twice the value for the nominal breakout strength provided by ACI 318, Equation 17.7.2.1b, when the shear force in question acts perpendicular to the edge.

For the composite member being designed, symmetrical concrete breakout planes form to each side of the encased shape, one of which is illustrated in Figure I.8-5.

$\phi = 0.75$ for anchors governed by concrete breakout with supplemental reinforcement (provided by tie reinforcement) in accordance with ACI 318, Section 17.5.3

$$V_{cbg} = 2\left[\frac{A_{VC}}{A_{VCo}}\Psi_{ec,V}\Psi_{ed,V}\Psi_{c,V}\Psi_{h,V}V_b\right]$$ for shear force parallel to an edge
$$(ACI 318, Eq. 17.7.2.1b)$$

$$A_{VCo} = 4.5(c_{a1})^2$$
$$(ACI 318, Eq. 17.7.2.1.3)$$

$$= 4.5(10 \text{ in.})^2$$

$$= 450 \text{ in.}^2$$

$A_{VC} = (15$ in. $+ 40$ in. $+15$ in.$)(24$ in.$)$, from Figure I.8-5
$= 1{,}680$ in.²

![Diagram showing concrete breakout check for shear force parallel to an edge. Elevation view shows load introduction length = 48" with hatched breakout plane at ca1 = 15" and 1.5ca1 = 15" sections, total 40" span. Section A-A shows 12" dimension, 2" spacing, ca1 = 10" measurement, with hatched breakout area and "Line of anchors under consideration" label. Notes indicate reinforcing bars not shown for clarity.]

*Fig. I.8-5. Concrete breakout check for shear force parallel to an edge.*

---

# I-96

$\Psi_{ec,V} = 1.0$ no eccentricity
$\Psi_{ed,V} = 1.0$ in accordance with ACI 318, Section 17.7.2.4.1
$\Psi_{c,V} = 1.4$ compression-only member assumed uncracked
$\Psi_{h,V} = 1.0$

$$V_b = 8\left(\frac{l_e}{d_a}\right)^{0.2}\sqrt{d_a}\lambda_a\sqrt{f_c'(c_{a1})}^{1.5}$$
$$(ACI 318, Eq. 17.7.2.2.2)$$

where
$l_e = 4$ in. $-\frac{3}{8}$ in. anchor head thickness from AWS D1.1/D1.1M, Figure 9.1
$= 3.63$ in. (per ACI 318, Section 17.7.2.2.1, $l_e \leq 8d_a = 6.00$ in. **o.k.**)
$d_a = \frac{3}{4}$ in. anchor diameter
$\lambda = 1.0$ from ACI 318, Section 19.2.4.3, for normal weight concrete
$\lambda_a = 1.0\lambda$ from ACI 318, Section 17.2.4.1, for normal weight concrete

Note the limitations of ACI 17.7.2.2.2 must be checked. These limitations have been shown to be acceptable for this example.

$$V_b = 8\left(\frac{3.63 \text{ in.}}{\frac{3}{4} \text{ in.}}\right)^{0.2}\sqrt{\frac{3}{4} \text{ in.}}(1.0)\left[\frac{\sqrt{5{,}000 \text{ psi}}}{1{,}000 \text{ lb/kip}}\right](10 \text{ in.})^{1.5}$$

$$= 21.2 \text{ kips}$$

$$V_{cbg} = 2\left[\frac{1{,}680 \text{ in.}^2}{450 \text{ in.}^2}(1.0)(1.0)(1.4)(1.0)(21.2 \text{ kips})\right]$$

$$= 222 \text{ kips}$$

$$\phi V_{cbg} = 0.75(222 \text{ kips})$$
$$= 167 \text{ kips per breakout plane}$$

$$\phi V_{cbg} = (2 \text{ breakout planes})(167 \text{ kips/plane})$$
$$= 334 \text{ kips}$$

$$\phi V_{cbg} > V_r' = 304 \text{ kips} \quad \textbf{o.k.}$$

Thus, concrete breakout along an edge parallel to the direction of the longitudinal shear transfer is not a controlling limit state, and Equation I8-3 is appropriate for determining available anchor strength.

Encased beam-column members with reinforcing detailed in accordance with the AISC *Specification* have demonstrated adequate confinement in tests to prevent concrete breakout along a parallel edge from occurring; however, it is still incumbent upon the engineer to review the project-specific detailing used for susceptibility to this limit state.

If concrete breakout was determined to be a controlling limit state, transverse reinforcing ties could be analyzed as anchor reinforcement in accordance with AISC *Specification* Section I8.3a(a), and tie spacing through the load introduction length adjusted as required to prevent breakout. Alternately, the steel headed stud anchors could be relocated to the web of the encased member where breakout is prevented by confinement between the column flanges.

---

# I-97

# EXAMPLE I.9 ENCASED COMPOSITE MEMBER IN AXIAL COMPRESSION

## Given:

Determine if the encased composite member illustrated in Figure I.9-1 is adequate for the indicated dead and live loads.

![Diagram showing encased composite member section and elevation. Section shows W10×45 with h1 = 24", (8)#8 BARS, #3@12" ties, dimensions 2½" edges, 9½" centers, h2 = 24", x-x and y-y axes. Elevation shows L = 14'-0" column with PD = 260 kips, PL = 780 kips at top and pinned base.]

*Fig. I.9-1. Encased composite member section and applied loading.*

The composite member consists of an ASTM A992/A992M W-shape encased by normal weight (145 lb/ft³) reinforced concrete having a specified concrete compressive strength, $f_c' = 5$ ksi.

Deformed reinforcing bars conform to ASTM A615/A615M with a minimum yield stress, $F_{yr}$, of 60 ksi.

**Solution:**

From AISC *Manual* Table 2-4, the steel material properties are:

ASTM A992/A992M
$F_y = 50$ ksi

From AISC *Manual* Table 1-1, Figure I.9-1, and Design Example I.8, geometric and material properties of the composite section are:

$A_s = 13.3$ in.² $b_f = 8.02$ in. $t_f = 0.620$ in. $d = 10.1$ in.
$h_1 = 24$ in. $h_2 = 24$ in. $I_{sx} = 248$ in.⁴ $I_{sy} = 53.4$ in.⁴
$A_g = 576$ in.² $A_{sri} = 0.790$ in.² $A_{sr} = 6.32$ in.² $A_c = 556$ in.²
$E_c = 3{,}900$ ksi

The moment of inertia of the reinforcing bars about the elastic neutral axis of the composite section, $I_{sr}$, is required for composite member design and is calculated as follows:

$d_b = 1$ in. for the diameter of a No. 8 bar

---

# I-98

$$I_{sri} = \frac{\pi d_b^4}{64}$$

$$= \frac{\pi(1 \text{ in.})^4}{64}$$

$$= 0.0491 \text{ in.}^4$$

$$I_{sr} = \sum_{i=1}^{n} I_{sri} + \sum_{i=1}^{n} A_{sri}e_i^2$$

$$= 8(0.0491 \text{ in.}^4) + 6(0.79 \text{ in.}^2)(9.50 \text{ in.})^2 + 2(0.79 \text{ in.}^2)(0 \text{ in.})^2$$

$$= 428 \text{ in.}^4$$

where
$A_{sri}$ = cross-sectional area of reinforcing bar $i$, in.²
$I_{sri}$ = moment of inertia of reinforcing bar $i$ about its elastic neutral axis, in.⁴
$I_{sr}$ = moment of inertia of the reinforcing bars about the elastic neutral axis of the composite section, in.⁴
$d_b$ = nominal diameter of reinforcing bar, in.
$e_i$ = eccentricity of reinforcing bar $i$ with respect to the elastic neutral axis of the composite section, in.
$n$ = number of reinforcing bars in composite section

Note that the elastic neutral axis for each direction of the section in question is located at the $x$-$x$ and $y$-$y$ axes illustrated in Figure I.9-1, and that the moment of inertia calculated for the longitudinal reinforcement is valid about either axis due to symmetry.

The moment of inertia values for the concrete about each axis are determined as:

$$I_{cx} = I_{gx} - I_{sx} - I_{srx}$$

$$= \frac{(24 \text{ in.})^4}{12} - 248 \text{ in.}^4 - 428 \text{ in.}^4$$

$$= 27{,}000 \text{ in.}^4$$

$$I_{cy} = I_{gy} - I_{sy} - I_{sry}$$

$$= \frac{(24 \text{ in.})^4}{12} - 53.4 \text{ in.}^4 - 428 \text{ in.}^4$$

$$= 27{,}200 \text{ in.}^4$$

**Classify Section for Local Buckling**

In accordance with AISC *Specification* Section I1.2, local buckling effects need not be considered for encased composite members, thus all encased sections are treated as compact sections for strength calculations.

**Material and Detailing Limitations**

According to the User Note at the end of AISC *Specification* Section I1.1, the intent of the *Specification* is to implement the noncomposite detailing provisions of ACI 318 in conjunction with the composite-specific provisions of *Specification* Chapter I. Detailing provisions may be grouped into material related limits, transverse reinforcement provisions, and longitudinal and structural steel reinforcement provisions as illustrated in the following discussion.

Material limits are provided in AISC *Specification* Sections I1.1(b) and I1.3 as follows:

---

# I-99

(1) Concrete strength: $3 \text{ ksi} \leq f_c' \leq 10$ ksi
$f_c' = 5$ ksi **o.k.**

(2) Specified minimum yield stress of structural steel: $F_y \leq 75$ ksi
$F_y = 50$ ksi **o.k.**

(3) Specified minimum yield stress of reinforcing bars: $F_{yr} \leq 80$ ksi
$F_{yr} = 60$ ksi **o.k.**

Transverse reinforcement limitations are provided in AISC *Specification* Section I1.1(b), I2.1a(b), and ACI 318 as follows:

(1) Tie size and spacing limitations:

The AISC *Specification* requires that either lateral ties or spirals be used for transverse reinforcement. Where lateral ties are used, a minimum of either No. 3 bars are spaced at a maximum of 12 in. on center or No. 4 bars or larger spaced at a maximum of 16 in. on center are required.

No. 3 lateral ties at 12 in. o.c. are provided. **o.k.**

The User Note in AISC *Specification* Section I1.1 states that "It is the intent of this Specification that the concrete and reinforcing steel portions of composite concrete members are designed and detailed utilizing the provisions of ACI 318 as modified by this Specification. All requirements specific to composite members are covered in this Specification." It is unnecessary to meet the reinforcement provisions of ACI 318 when designing composite columns using the provisions of AISC *Specification* Chapter I.

(2) Additional tie size limitation:

No. 4 ties or larger are required where No. 11 or larger bars are used as longitudinal reinforcement in accordance with ACI 318, Section 25.7.2.2(b).

No. 3 lateral ties are provided for No. 8 longitudinal bars. **o.k.**

(3) Maximum tie spacing should not exceed 0.5 times the least column dimension:

$$s_{max} = 0.5 \min\begin{cases}
h_1 = 24 \text{ in.} \\
h_2 = 24 \text{ in.}
\end{cases}$$

$$= 12.0 \text{ in.}$$

$s = 12.0$ in. $\leq s_{max}$ **o.k.**

(4) Concrete cover:

ACI 318, Section 20.5.1.3.1, contains concrete cover requirements. For concrete not exposed to weather or in contact with ground, the required cover for column ties is 1½ in.

$$\text{cover} = 2.5 \text{ in.} - \frac{d_b}{2} - \text{diameter of No. 3 tie}$$

$$= 2.5 \text{ in.} - \frac{1}{2} \text{ in.} - \frac{3}{8} \text{ in.}$$

$$= 1.63 \text{ in.} > 1\frac{1}{2} \text{ in.} \quad \textbf{o.k.}$$

(5) Provide ties as required for lateral support of longitudinal bars:

---

# I-100

AISC *Specification* Commentary Section I2.1a references ACI 318 for additional transverse tie requirements. In accordance with ACI 318, Section 25.7.2.3 and Figure R25.7.2.3a, ties are required to support longitudinal bars located farther than 6 in. clear on each side from a supported bar. For corner bars, support is typically provided by the main perimeter ties. For intermediate bars, Figure I.9-1 illustrates one method for providing support through the use of a diamond-shaped tie.

Longitudinal and structural steel reinforcement limits are provided in AISC *Specification* Sections I1.1, I2.1, and ACI 318 as follows:

(1) Structural steel minimum reinforcement ratio: $A_s/A_g \geq 0.01$

$$\frac{A_s}{A_g} = \frac{13.3 \text{ in.}^2}{576 \text{ in.}^2} \geq 0.01$$

$$= 0.0231 > 0.01 \quad \textbf{o.k.}$$

An explicit maximum reinforcement ratio for the encased steel shape is not provided in the AISC *Specification*; however, a range of 8 to 12% has been noted in the literature to result in economic composite members for the resistance of gravity loads (Leon and Hajjar, 2008).

(2) Minimum longitudinal reinforcement ratio: $A_{sr}/A_g \geq 0.004$

$$\frac{A_{sr}}{A_g} = \frac{6.32 \text{ in.}^2}{576 \text{ in.}^2} \geq 0.004$$

$$= 0.0110 > 0.004 \quad \textbf{o.k.}$$

As discussed in AISC *Specification* *Commentary* Section I2.1a(3), only continuously developed longitudinal reinforcement is included in the minimum reinforcement ratio, so longitudinal restraining bars and other discontinuous longitudinal reinforcement is excluded. Note that this limitation is used in lieu of the minimum ratio provided in ACI 318 as discussed in *Specification* Commentary Section I1.1.

(3) Maximum longitudinal reinforcement ratio: $A_{sr}/A_g \leq 0.08$

$$\frac{A_{sr}}{A_g} = \frac{6.32 \text{ in.}^2}{576 \text{ in.}^2} \leq 0.08$$

$$= 0.0110 < 0.08 \quad \textbf{o.k.}$$

This longitudinal reinforcement limitation is provided in ACI 318, Section 10.6.1.1. It is recommended that all longitudinal reinforcement, including discontinuous reinforcement not used in strength calculations, be included in this ratio as it is considered a practical limitation to mitigate reinforcing congestion. If longitudinal reinforcement is lap spliced as opposed to mechanically coupled, this limit is effectively reduced to 4% in areas away from the splice location.

(4) Minimum number of longitudinal bars:

ACI 318, Section 10.7.3.1, requires a minimum of four longitudinal bars within rectangular or circular members with ties and six bars for columns utilizing spiral ties. The intent for rectangular sections is to provide a minimum of one bar in each corner, so irregular geometries with multiple corners require additional longitudinal bars.

8 bars provided. **o.k.**

(5) Clear spacing between longitudinal bars:

---

# I-101

ACI 318, Section 25.2.3, requires a clear distance between bars of $1.5d_b$ or 1½ in.

$$s_{min} = \max\begin{cases}
1.5d_b = 1\frac{1}{2} \text{ in.} \\
1\frac{1}{2} \text{ in.}
\end{cases}$$

$$= 1\frac{1}{2}\text{in. clear}$$

$s = 9.50$ in. $-1.00$ in.
$= 8.50$ in. $> 1\frac{1}{2}$ in. **o.k.**

Note that ACI 318, Section 25.2.3, also specifies a minimum clear distance between bars equal to $(4/3)d_{agg}$. For the purposes of this example, it is assumed that this limit will not control.

(6) Clear spacing between longitudinal bars and the steel core:

AISC *Specification* Section I2.1e requires a minimum clear spacing between the steel core and longitudinal reinforcement of 1.5 reinforcing bar diameters, but not less than 1½ in.

$$s_{min} = \max\begin{cases}
1.5d_b = 1\frac{1}{2} \text{ in.} \\
1\frac{1}{2} \text{ in.}
\end{cases}$$

$$= 1\frac{1}{2} \text{ in. clear}$$

Closest reinforcing bars to the encased section are the center bars adjacent to each flange:

$$s = \frac{h_2}{2} - \frac{d}{2} - 2.5 \text{ in.} - \frac{d_b}{2}$$

$$= \frac{24 \text{ in.}}{2} - \frac{10.1 \text{ in.}}{2} - 2.5 \text{ in.} - \frac{1 \text{ in.}}{2}$$

$$= 3.95 \text{ in.} > s_{min} = 1\frac{1}{2} \text{ in.} \quad \textbf{o.k.}$$

(7) Concrete cover for longitudinal reinforcement:

ACI 318, Section 20.5.1.3, provides concrete cover requirements for reinforcement. The cover requirements for column ties and primary reinforcement are the same, and the tie cover was previously determined to be acceptable, thus the longitudinal reinforcement cover is acceptable by inspection.

From ASCE/SEI, Chapter 2, the required compressive strength is:

| LRFD | ASD |
|------|-----|
| $P_r = P_u$ | $P_r = P_a$ |
| $= 1.2(260 \text{ kips}) + 1.6(780 \text{ kips})$ | $= 260 \text{ kips} + 780 \text{ kips}$ |
| $= 1{,}560$ kips | $= 1{,}040$ kips |

**Available Compressive Strength**

The nominal axial compressive strength without consideration of length effects, $P_{no}$, is determined from AISC *Specification* Section I2.1b as:

---

# I-102

$$P_{no} = F_y A_s + F_{ysr} A_{sr} + 0.85 f_c' A_c$$
$$(Spec. \text{ Eq. I2-7})$$

$$= (50 \text{ ksi})(13.3 \text{ in.}^2) + (60 \text{ ksi})(6.32 \text{ in.}^2) + 0.85(5 \text{ ksi})(556 \text{ in.}^2)$$

$$= 3{,}410 \text{ kips}$$

Because the unbraced length is the same in both the $x$-$x$ and $y$-$y$ directions, the column will buckle about the axis having the smaller effective composite section stiffness, $(EI)_{eff}$. Noting the moment of inertia values determined previously for the concrete and reinforcing steel are similar about each axis, the column will buckle about the weaker axis of the steel shape by inspection. $I_{cy}$, $I_{sy}$, and $I_{sry}$ are therefore used for calculation of length effects in accordance with AISC *Specification* Section I2.1b as follows:

$$C_1 = 0.25 + 3\left(\frac{A_s + A_{sr}}{A_g}\right) \leq 0.7$$
$$(Spec. \text{ Eq. I2-6})$$

$$= 0.25 + 3\left(\frac{13.3 \text{ in.}^2 + 6.32 \text{ in.}^2}{576 \text{ in.}^2}\right) \leq 0.7$$

$$= 0.352 < 0.7$$; therefore $C_1 = 0.352$

$$(EI)_{eff} = E_s I_{sy} + E_s I_{sry} + C_1 E_c I_{cy}$$
(from $Spec.$ Eq. I2-5)

$$= (29{,}000 \text{ ksi})(53.4 \text{ in.}^4) + (29{,}000 \text{ ksi})(428 \text{ in.}^4)$$

$$+ 0.352(3{,}900 \text{ ksi})(27{,}200 \text{ in.}^4)$$

$$= 51{,}300{,}000 \text{ kip-in.}^2$$

$$P_e = \pi^2(EI)_{eff}/L_c^2$$, where $L_c = KL$ and $K = 1.0$ for a pin-ended member
$$(Spec. \text{ Eq. I2-4})$$

$$= \frac{\pi^2(51{,}300{,}000 \text{ kip-in.}^2)}{[(1.0)(14 \text{ ft})(12 \text{ in./ft})]^2}$$

$$= 17{,}900 \text{ kips}$$

$$\frac{P_{no}}{P_e} = \frac{3{,}410 \text{ kips}}{17{,}900 \text{ kips}}$$

$$= 0.191 < 2.25$$

Therefore, use AISC *Specification* Equation I2-2.

$$P_n = P_{no}\left(0.658^{\frac{P_{no}}{P_e}}\right)$$
$$(Spec. \text{ Eq. I2-2})$$

$$= (3{,}410 \text{ kips})(0.658)^{0.191}$$

$$= 3{,}150 \text{ kips}$$

Check adequacy of the composite column for the required axial compressive strength:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.75$ | $\Omega_c = 2.00$ |

---

# I-103

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 0.75(3{,}150 \text{ kips})$ | $\dfrac{P_n}{\Omega_c} = \dfrac{3{,}150 \text{ kips}}{2.00}$ |
| $= 2{,}360 \text{ kips} > 1{,}560 \text{ kips} \quad \textbf{o.k.}$ | $= 1{,}580 \text{ kips} > 1{,}040 \text{ kips} \quad \textbf{o.k.}$ |

**Available Compressive Strength of Composite Section Versus Bare Steel Section**

Due to the differences in resistance and safety factors between composite and noncomposite column provisions, it is possible in rare instances to calculate a lower available compressive strength for an encased composite column than one would calculate for the corresponding bare steel section. However, in accordance with AISC *Specification* Section I2.1b, the available compressive strength need not be less than that calculated for the bare steel member in accordance with Chapter E.

From AISC *Manual* Table 4-1a:

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 359 \text{ kips} < 2{,}360 \text{ kips}$ | $\dfrac{P_n}{\Omega_c} = 239 \text{ kips} < 1{,}580 \text{ kips}$ |

Thus, the composite section strength controls and is adequate for the required axial compressive strength as previously demonstrated.

**Force Allocation and Load Transfer**

Load transfer calculations for external axial forces should be performed in accordance with AISC *Specification* Section I6. The specific application of the load transfer provisions is dependent upon the configuration and detailing of the connecting elements. Expanded treatment of the application of load transfer provisions for encased composite members is provided in Design Example I.8.

**Typical Detailing Convention**

Designers are directed to AISC Design Guide 6 (Griffis, 1992) for additional discussion and typical details of encased composite columns not explicitly covered in this example.

---

# I-104

# EXAMPLE I.10 ENCASED COMPOSITE MEMBER IN AXIAL TENSION

## Given:

Determine if the encased composite member illustrated in Figure I.10-1 is adequate for the indicated dead load compression and wind load tension. The entire load is applied to the encased steel section.

![Diagram showing encased composite member section and elevation. Section shows W10×45 with h1 = 24", (8)#8 BARS, #3@12" ties, dimensions 2½" edges, 9½" centers, h2 = 24", x-x and y-y axes. Elevation shows L = 14'-0" column with PD = -260 kips, PW = 980 kips at top and pinned base.]

*Fig. I.10-1. Encased composite member section and applied loading.*

The composite member consists of an ASTM A992/A992M W-shape encased by normal weight (145 lb/ft³) reinforced concrete having a specified concrete compressive strength, $f_c' = 5$ ksi.

Deformed reinforcing bars conform to ASTM A615/A615M with a minimum yield stress, $F_{yr}$, of 60 ksi.

**Solution:**

From AISC *Manual* Table 2-4, the steel material properties are:

ASTM A992/A992M
$F_y = 50$ ksi

From AISC *Manual* Table 1-1 and Figure I.10-1, the relevant properties of the composite section are:

$A_s = 13.3$ in.²
$A_{sr} = 6.32$ in.² (area of eight No. 8 bars)

**Material and Detailing Limitations**

Refer to Design Example I.9 for a check of material and detailing limitations specified in AISC *Specification* Chapter I for encased composite members.

Taking compression as negative and tension as positive, from ASCE/SEI 7, Chapter 2, the required strength is:

---

# I-105

| LRFD | ASD |
|------|-----|
| Governing uplift load combination = $0.9D + 1.0W$ | Governing uplift load combination = $0.6D + 0.6W$ |
| $P_r = P_u$ | $P_r = P_a$ |
| $= 0.9(-260 \text{ kips}) + 1.0(980 \text{ kips})$ | $= 0.6(-260 \text{ kips}) + 0.6(980 \text{ kips})$ |
| $= 746$ kips | $= 432$ kips |

**Available Tensile Strength**

Available tensile strength for an encased composite member is determined in accordance with AISC *Specification* Section I2.1c.

$$P_n = F_y A_s + F_{ysr} A_{sr}$$
$$(Spec. \text{ Eq. I2-8})$$

$$= (50 \text{ ksi})(13.3 \text{ in.}^2) + (60 \text{ ksi})(6.32 \text{ in.}^2)$$

$$= 1{,}040 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi_t = 0.90$ | $\Omega_t = 1.67$ |
| $\phi_t P_n = 0.90(1{,}040 \text{ kips})$ | $\dfrac{P_n}{\Omega_t} = \dfrac{1{,}040 \text{ kips}}{1.67}$ |
| $= 936 \text{ kips} > 746 \text{ kips} \quad \textbf{o.k.}$ | $= 623 \text{ kips} > 432 \text{ kips} \quad \textbf{o.k.}$ |

**Force Allocation and Load Transfer**

In cases where all of the tension is applied to either the reinforcing steel or the encased steel shape, and the available strength of the reinforcing steel or encased steel shape by itself is adequate, no additional load transfer calculations are required.

In cases, such as the one under consideration, where the available strength of both the reinforcing steel and the encased steel shape are needed to provide adequate tension resistance, AISC *Specification* Section I6 can be modified for tensile load transfer requirements by replacing the $P_{no}$ term in Equations I6-1 and I6-2 with the nominal tensile strength, $P_n$, determined from Equation I2-8.

For external tensile force applied to the encased steel section:

$$V_r' = P_r\left(1 - \frac{F_y A_s}{P_n}\right)$$
$$(Spec. \text{ Eq. C-I6-1})$$

For external tensile force applied to the longitudinal reinforcement of the concrete encasement:

$$V_r' = P_r\left(\frac{F_y A_s}{P_n}\right)$$
$$(Spec. \text{ Eq. C-I6-2})$$

where
$P_n$ = nominal tensile strength of encased composite member from Equation I2-8, kips
$P_r$ = required external tensile force applied to the composite member, kips

---

# I-106

Per the problem statement, the entire external force is applied to the encased steel section, thus, AISC *Specification* Equation C-I6-1 is used as follows:

$$V_r' = P_r\left[1 - \frac{(50 \text{ ksi})(13.3 \text{ in.}^2)}{1{,}040 \text{ kips}}\right]$$

$$= 0.361P_r$$

| LRFD | ASD |
|------|-----|
| $V_r' = 0.361(746 \text{ kips})$ | $V_r' = 0.361(432 \text{ kips})$ |
| $= 269$ kips | $= 156$ kips |

The longitudinal shear force must be transferred between the encased steel shape and longitudinal reinforcing using the force transfer mechanisms of direct bearing or shear connection in accordance with AISC *Specification* Section I6.3 as illustrated in Example I.8.

---

# I-107

# EXAMPLE I.11 ENCASED COMPOSITE MEMBER IN COMBINED AXIAL COMPRESSION, FLEXURE, AND SHEAR

## Given:

Determine if the encased composite member illustrated in Figure I.11-1 is adequate for the indicated axial forces, shears, and moments that have been determined in accordance with the direct analysis method of AISC *Specification* Chapter C for the controlling ASCE/SEI 7 load combinations.

![Diagram showing encased composite member section and elevation. Section shows W10×45 with h1 = 24", (8)#8 BARS, #3@12" ties, dimensions 2½" edges, 9½" centers, h2 = 24", x-x and y-y axes. Elevation (FBD) shows L = 14'-0" column with forces Pr, Mr, Vr at top and bottom. Table shows LRFD and ASD values: Pr (kips): 1,170/879, Mr (kip-ft): 670/302, Vr (kips): 95.7/57.4]

*Fig. I.11-1. Encased composite member section and member forces.*

The composite member consists of an ASTM A992/A992M W-shape encased by normal weight (145 lb/ft³) reinforced concrete having a specified concrete compressive strength, $f_c' = 5$ ksi.

Deformed reinforcing bars conform to ASTM A615/A615M with a minimum yield stress, $F_{yr}$, of 60 ksi.

**Solution:**

From AISC *Manual* Table 2-4, the steel material properties are:

ASTM A992/A992M
$F_y = 50$ ksi

---

# I-108

From AISC *Manual* Table 1-1, Figure I.11-1, and Examples I.8 and I.9, the geometric and material properties of the composite section are:

$A_s = 13.3$ in.² $d = 10.1$ in. $h_1 = 24$ in. $I_{sy} = 53.4$ in.⁴
$A_g = 576$ in.² $b_f = 8.02$ in. $h_2 = 24$ in. $I_{sx} = 27{,}000$ in.⁴
$A_c = 556$ in.² $t_f = 0.620$ in. $E_c = 3{,}900$ ksi $I_{cy} = 27{,}200$ in.⁴
$A_{sr} = 6.32$ in.² $t_w = 0.350$ in. $Z_{sx} = 54.9$ in.³ $I_{sr} = 428$ in.⁴
$c = 2\frac{1}{2}$ in. $S_{sx} = 49.1$ in.³

The area of continuous reinforcing located at the centerline of the composite section, $A_{crs}$, is determined from Figure I.11-1 as follows:

$$A_{crs} = 2(A_{sri})$$

$$= 2(0.79 \text{ in.}^2)$$

$$= 1.58 \text{ in.}^2$$

where
$A_{sri}$ = area of reinforcing bar $i$ at centerline of composite section
$= 0.79$ in.² for a No. 8 bar

For the section under consideration, $A_{crs}$ is equal about both the $x$-$x$ and $y$-$y$ axis.

**Classify Section for Local Buckling**

In accordance with AISC *Specification* Section I1.2, local buckling effects need not be considered for encased composite members, thus all encased sections are treated as compact sections for strength calculations.

**Material and Detailing Limitations**

Refer to Design Example I.9 for a check of material and detailing limitations.

**Interaction of Axial Force and Flexure**

Interaction between flexure and axial forces in composite members is governed by AISC *Specification* Section I5, which permits the use of the methods of Section I1.2.

The strain compatibility method is a generalized approach that allows for the construction of an interaction diagram based upon the same concepts used for reinforced concrete design. Application of the strain compatibility method is required for irregular/nonsymmetrical sections, and its general implementation may be found in reinforced concrete design texts and will not be discussed further here.

Plastic stress distribution methods are discussed in AISC *Specification* Commentary Section I5, which provides four procedures applicable to encased composite members. The first procedure, Method 1, invokes the interaction equations of Section H1. The second procedure, Method 2, involves the construction of a piecewise-linear interaction curve using the plastic strength equations provided in AISC *Manual* Table 6-2a. The third procedure, Method 2—Simplified, is a reduction of the piecewise-linear interaction curve that allows for the use of less conservative interaction equations than those presented in Chapter H. The fourth and final procedure, Method 3, utilizes AISC Design Guide 6 (Griffis, 1992).

For this design example, three of the available plastic stress distribution procedures are reviewed and compared. Method 3 is not demonstrated as it is not applicable to the section under consideration due to the area of the encased steel section being smaller than the minimum limit of 4% of the gross area of the composite section provided in the earlier *Specification* upon which Design Guide 6 is based.

---

# I-109

**Method 1—Interaction Equations of Section H1**

The most direct and conservative method of assessing interaction effects is through the use of the interaction equations of AISC *Specification* Section H1. Unlike other HSS shapes, the available compressive and flexural strengths of encased members are not tabulated in the AISC *Manual* due to the large variety of possible combinations. Calculations must therefore be performed explicitly using the provisions of Chapter I.

**Available Compressive Strength**

The available compressive strength is calculated as illustrated in Example I.9.

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 2{,}360$ kips | $\dfrac{P_n}{\Omega_c} = 1{,}580$ kips |

**Nominal Flexural Strength**

The applied moment illustrated in Figure I.11-1 is resisted by the flexural strength of the composite section about its strong ($x$-$x$) axis. The strength of the section in pure flexure is determined using the equations of AISC *Manual* Table 6-2a for Point B. Note that the calculation of the flexural strength at Point B first requires calculation of the flexural strength at Point D as follows:

$$Z_r = (A_{sr} - A_{crs})\left(\frac{h_2}{2} - c\right)$$

$$= (6.32 \text{ in.}^2 - 1.58 \text{ in.}^2)\left(\frac{24 \text{ in.}}{2} - 2\frac{1}{2} \text{ in.}\right)$$

$$= 45.0 \text{ in.}^3$$

$$Z_c = \frac{h_1 h_2^2}{4} - Z_s - Z_r$$

$$= \frac{(24 \text{ in.})(24 \text{ in.})^2}{4} - 54.9 \text{ in.}^3 - 45.0 \text{ in.}^3$$

$$= 3{,}360 \text{ in.}^3$$

$$M_D = F_y Z_s + F_{yr} Z_r + 0.85 f_c'\left(\frac{Z_c}{2}\right)$$

$$= \left[(50 \text{ ksi})(54.9 \text{ in.}^3) + (60 \text{ ksi})(45.0 \text{ in.}^3) + 0.85(5 \text{ ksi})\left(\frac{3{,}360 \text{ in.}^3}{2}\right)\right]$$

$$= 12{,}600 \text{ kip-in.}$$

Assuming $h_n$ is within the flange $\left(\frac{d}{2} - t_f < h_n \leq \frac{d}{2}\right)$:

---

# I-110

$$h_n = \frac{0.85 f_c'(A_c + A_s - db_f + A_{crs}) - 2F_y(A_s - db_f) - 2F_{yr}A_{crs}}{2\left[0.85 f_c'(h_1 - b_f) + 2F_y b_f\right]}$$

$$= \frac{\left\{0.85(5 \text{ ksi})\left[556 \text{ in.}^2 + 13.3 \text{ in.}^2 - (10.1 \text{ in.})(8.02 \text{ in.}) + 1.58 \text{ in.}^2\right]\right.}{\left.-2(50 \text{ ksi})\left[13.3 \text{ in.}^2 - (10.1 \text{ in.})(8.02 \text{ in.})\right] - 2(60 \text{ ksi})(1.58 \text{ in.}^2)\right\}}$$

$$\frac{}{2\left[0.85(5 \text{ ksi})(24 \text{ in.} - 8.02 \text{ in.}) + 2(50 \text{ ksi})(8.02 \text{ in.})\right]}$$

$$= 4.98 \text{ in.}$$

Check assumption:

$$\left(\frac{10.1 \text{ in.}}{2} - 0.620 \text{ in.}\right) \leq h_n \leq \frac{10.1 \text{ in.}}{2}$$

$4.43$ in. $< h_n = 4.98$ in. $< 5.05$ in. assumption **o.k.**

$$Z_{sn} = Z_s - b_f\left(\frac{d}{2} - h_n\right)\left(\frac{d}{2} + h_n\right)$$

$$= 54.9 \text{ in.}^3 - (8.02 \text{ in.})\left(\frac{10.1 \text{ in.}}{2} - 4.98 \text{ in.}\right)\left(\frac{10.1 \text{ in.}}{2} + 4.98 \text{ in.}\right)$$

$$= 49.3 \text{ in.}^3$$

$$Z_{cn} = h_1 h_n^2 - Z_{sn}$$

$$= (24 \text{ in.})(4.98 \text{ in.})^2 - 49.3 \text{ in.}^3$$

$$= 546 \text{ in.}^3$$

$$M_B = M_D - F_y Z_{sn} - 0.85 f_c'\left(\frac{Z_{cn}}{2}\right)$$

$$= \left[12{,}600 \text{ kip-in.} - (50 \text{ ksi})(49.3 \text{ in.}^3) - 0.85(5 \text{ ksi})\left(\frac{546 \text{ in.}^3}{2}\right)\right]\left(\frac{1}{12 \text{ in./ft}}\right)$$

$$= 748 \text{ kip-ft}$$

**Available Flexural Strength**

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $\phi_b M_n = 0.90(748 \text{ kip-ft})$ | $\dfrac{M_n}{\Omega_b} = \dfrac{748 \text{ kip-ft}}{1.67}$ |
| $= 673$ kip-ft | $= 448$ kip-ft |

---

# I-111

**Interaction of Axial Compression and Flexure**

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 2{,}360$ kips | $P_n/\Omega_c = 1{,}580$ kips |
| $\phi_b M_n = 673$ kip-ft | $M_n/\Omega_b = 448$ kip-ft |
| $\dfrac{P_r}{P_c} = \dfrac{P_u}{\phi_c P_n}$ | $\dfrac{P_r}{P_c} = \dfrac{P_a}{P_n/\Omega_c}$ |
| $= \dfrac{1{,}170 \text{ kips}}{2{,}360 \text{ kips}}$ | $= \dfrac{879 \text{ kips}}{1{,}580 \text{ kips}}$ |
| $= 0.496 > 0.2$ | $= 0.556 > 0.2$ |
| Therefore, use AISC *Specification* Equation H1-1a. | Therefore, use AISC *Specification* Equation H1-1a. |
| $\dfrac{P_u}{\phi_c P_n} + \dfrac{8}{9}\left(\dfrac{M_u}{\phi_b M_n}\right) \leq 1.0$ (from $Spec.$ Eq. H1-1a) | $\dfrac{P_a}{P_n/\Omega_c} + \dfrac{8}{9}\left(\dfrac{M_a}{M_n/\Omega_b}\right) \leq 1.0$ (from $Spec.$ Eq. H1-1a) |
| $0.496 + \dfrac{8}{9}\left(\dfrac{670 \text{ kip-ft}}{673 \text{ kip-ft}}\right) \leq 1.0$ | $0.556 + \dfrac{8}{9}\left(\dfrac{302 \text{ kip-ft}}{448 \text{ kip-ft}}\right) \leq 1.0$ |
| $1.38 > 1.0 \quad \textbf{n.g.}$ | $1.16 > 1.0 \quad \textbf{n.g.}$ |

Method 1 indicates that the section is inadequate for the applied loads. The designer can elect to choose a new section that passes the interaction check or re-analyze the current section using a less conservative design method such as Method 2. The use of Method 2 is illustrated in the following section.

**Method 2—Interaction Curves from the Plastic Stress Distribution Model**

The procedure for creating an interaction curve using the plastic stress distribution model is illustrated graphically in AISC *Specification* Commentary Figure C-I5.2, and repeated here.

![Interaction diagram showing plastic stress distribution curves. Vertical axis labeled P with points A, A', A" marked, showing "Reduction for slenderness, A' = λA" and "Reduction for design, A'' = ϕA' or A'/Ω". Horizontal axis labeled M with points B, B', B", C, C', C", D, D', D" marked. Diagram shows "λ = slenderness reduction = A'/A"]

*Fig. C-I5.2. Interaction diagram for composite beam-columns—Method 2.*

---

# I-112

Referencing Figure C-I5.2, the nominal strength interaction surface A, B, C, D is first determined using the equations of AISC *Manual* Table 6-2a for bending about the $x$-$x$ axis. This curve represents the composite column member strength without consideration of length effects. A slenderness reduction factor, $\lambda$, is then calculated and applied to each point to create surface $A'$, $B'$, $C'$, $D'$. The appropriate resistance or safety factors are then applied to create the design surface $A''$, $B''$, $C''$, $D''$ for LRFD and ASD, respectively. Finally, the required axial and flexural strengths from the applicable load combinations of ASCE/SEI 7 are plotted on the design surface. The member is then deemed acceptable for the applied loading if all points fall within the design surface. These steps are illustrated in detail in the following calculations.

Step 1: Construct nominal strength interaction surface A, B, C, D without length effects.

Using the equations provided in AISC *Manual* Table 6-2a for bending about the $x$-$x$ axis yields:

Point A (pure axial compression):

$$P_A = F_y A_s + F_{yr} A_{sr} + 0.85 f_c' A_c$$

$$= (50 \text{ ksi})(13.3 \text{ in.}^2) + (60 \text{ ksi})(6.32 \text{ in.}^2) + 0.85(5 \text{ ksi})(556 \text{ in.}^2)$$

$$= 3{,}410 \text{ kips}$$

$$M_A = 0 \text{ kip-ft}$$

Point D (maximum nominal moment strength):

$$P_D = \frac{0.85 f_c' A_c}{2}$$

$$= \frac{0.85(5 \text{ ksi})(556 \text{ in.}^2)}{2}$$

$$= 1{,}180 \text{ kips}$$

Calculation of $M_D$ was demonstrated previously in Method 1.

$$M_D = 12{,}600 \text{ kip-in.}$$
$$= 1{,}050 \text{ kip-ft}$$

Point B (pure flexure):

$$P_B = 0 \text{ kips}$$

Calculation of $M_B$ was demonstrated previously in Method 1.

$$M_B = 748 \text{ kip-ft}$$

Point C (intermediate point):

$$P_C = 0.85 f_c' A_c$$

$$= 0.85(5 \text{ ksi})(556 \text{ in.}^2)$$

$$= 2{,}360 \text{ kips}$$

$$M_C = M_B$$
$$= 748 \text{ kip-ft}$$

---

# I-113

The calculated points are plotted to construct the nominal strength interaction surface without length effects as depicted in Figure I.11-2.

Step 2: Construct nominal strength interaction surface $A'$, $B'$, $C'$, $D'$ with length effects.

The slenderness reduction factor, $\lambda$, is calculated for Point A using AISC *Specification* Section I2.1 in accordance with AISC *Specification* Commentary Section I5.

Because the unbraced length is the same in both the $x$-$x$ and $y$-$y$ directions, the column will buckle about the axis having the smaller effective composite section stiffness, $(EI)_{eff}$. Noting the moment of inertia values for the concrete and reinforcing steel are similar about each axis, the column will buckle about the weak axis of the steel shape by inspection. $I_{cy}$, $I_{sy}$, and $I_{sry}$ are therefore used for calculation of length effects in accordance with AISC *Specification* Section I2.1b.

$$P_{no} = P_A$$
$$= 3{,}410 \text{ kips}$$

$$C_1 = 0.25 + 3\left(\frac{A_s + A_{sr}}{A_g}\right) \leq 0.7$$
$$(Spec. \text{ Eq. I2-6})$$

$$= 0.25 + 3\left(\frac{13.3 \text{ in.}^2 + 6.32 \text{ in.}^2}{576 \text{ in.}^2}\right) \leq 0.7$$

$$= 0.352 < 0.7$$; therefore $C_1 = 0.352$

$$(EI)_{eff} = E_s I_{sy} + E_s I_{sry} + C_1 E_c I_{cy}$$
(from $Spec.$ Eq. I2-5)

$$= (29{,}000 \text{ ksi})(53.4 \text{ in.}^4) + (29{,}000 \text{ ksi})(428 \text{ in.}^4) + 0.352(3{,}900 \text{ ksi})(27{,}200 \text{ in.}^4)$$

$$= 51{,}300{,}000 \text{ kip-in.}^2$$

![Graph showing nominal strength interaction surface without length effects. Vertical axis shows Compressive Strength (kips) from 0 to 4,000, horizontal axis shows Flexural Strength (kip-ft) from 0 to 1,200. Curve shows points A, C, D, B with dashed line labeled "Nominal Strength (without length effects)" connecting them in descending order from A to B.]

*Fig. I.11-2. Nominal strength interaction surface without length effects.*

---

# I-114

$$P_e = \pi^2(EI)_{eff}/L_c^2$$, where $L_c = KL$ and $K = 1.0$
$$(Spec. \text{ Eq. I2-4})$$

in accordance with the direct analysis method

$$= \frac{\pi^2(51{,}300{,}000 \text{ kip-in.}^2)}{[(1.0)(14 \text{ ft})(12 \text{ in./ft})]^2}$$

$$= 17{,}900 \text{ kips}$$

$$\frac{P_{no}}{P_e} = \frac{3{,}410 \text{ kips}}{17{,}900 \text{ kips}}$$

$$= 0.191 < 2.25$$

Therefore, use AISC *Specification* Equation I2-2.

$$P_n = P_{no}\left(0.658^{\frac{P_{no}}{P_e}}\right)$$
$$(Spec. \text{ Eq. I2-2})$$

$$= (3{,}410 \text{ kips})(0.658)^{0.191}$$

$$= 3{,}150 \text{ kips}$$

$$\lambda = \frac{P_n}{P_{no}}$$

$$= \frac{3{,}150 \text{ kips}}{3{,}410 \text{ kips}}$$

$$= 0.924$$

In accordance with AISC *Specification* Commentary Section I5, the same slenderness reduction is applied to each of the remaining points on the interaction surface as follows:

$$P_{A'} = \lambda P_A$$
$$= 0.924(3{,}410 \text{ kips})$$
$$= 3{,}150 \text{ kips}$$

$$P_{B'} = \lambda P_B$$
$$= 0.924(0 \text{ kip})$$
$$= 0 \text{ kip}$$

$$P_{C'} = \lambda P_C$$
$$= 0.924(2{,}360 \text{ kips})$$
$$= 2{,}180 \text{ kips}$$

$$P_{D'} = \lambda P_D$$
$$= 0.924(1{,}180 \text{ kips})$$
$$= 1{,}090 \text{ kips}$$

---

# I-115

The modified axial strength values are plotted with the flexural strength values previously calculated to construct the nominal strength interaction surface $A'$, $B'$, $C'$, $D'$ with length effects. These values are superimposed on the nominal strength surface not including length effects for comparison purposes in Figure I.11-3.

The consideration of length effects results in a vertical reduction of the nominal strength curve as illustrated by Figure I.11-3. This vertical movement creates an unsafe zone between points $D$ and $D'$ where flexural capacities of the nominal strength (with length effects) curve exceed the section capacity. Application of resistance or safety factors reduces this unsafe zone as illustrated in the following step; however, designers should be cognizant of the potential for unsafe designs with loads approaching the predicted flexural capacity of the section. Alternately, the use of Method 2—Simplified eliminates this possibility altogether.

Step 3: Construct design interaction surface $A''$, $B''$, $C''$, $D''$ and verify member adequacy.

The final step in the Method 2 procedure is to reduce the interaction surface for design using the appropriate resistance or safety factors.

The available compressive and flexural strengths are determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.75$ | $\Omega_c = 2.00$ |
| $P_{X''} = \phi_c P_{X'}$, where $X = A, B, C,$ or $D$ | $P_{X''} = \frac{P_{X'}}{\Omega_c}$, where $X = A, B, C,$ or $D$ |
| $P_{A''} = 0.75(3{,}150 \text{ kips})$ | $P_{A''} = 3{,}150 \text{ kips}/2.00$ |
| $= 2{,}360 \text{ kips}$ | $= 1{,}580 \text{ kips}$ |
| $P_{B''} = 0.75(0 \text{ kip})$ | $P_{B''} = 0 \text{ kip}/2.00$ |
| $= 0 \text{ kip}$ | $= 0 \text{ kip}$ |
| $P_{C''} = 0.75(2{,}180 \text{ kips})$ | $P_{C''} = 2{,}180 \text{ kips}/2.00$ |
| $= 1{,}640 \text{ kips}$ | $= 1{,}090 \text{ kips}$ |
| $P_{D''} = 0.75(1{,}090 \text{ kips})$ | $P_{D''} = 1{,}090 \text{ kips}/2.00$ |
| $= 818 \text{ kips}$ | $= 545 \text{ kips}$ |

---

# I-116

| LRFD | ASD |
|------|-----|
| $\phi_b = 0.90$ | $\Omega_b = 1.67$ |
| $M_{X''} = \phi_b M_X$, where $X = A, B, C,$ or $D$ | $M_{X''} = \frac{M_X}{\Omega_b}$, where $X = A, B, C,$ or $D$ |
| $M_{A''} = 0.90(0 \text{ kip-ft})$ | $M_{A''} = 0 \text{ kip-ft}/1.67$ |
| $= 0 \text{ kip-ft}$ | $= 0 \text{ kip-ft}$ |
| $M_{B''} = 0.90(748 \text{ kip-ft})$ | $M_{B''} = 748 \text{ kip-ft}/1.67$ |
| $= 673 \text{ kip-ft}$ | $= 448 \text{ kip-ft}$ |
| $M_{C''} = 0.90(748 \text{ kip-ft})$ | $M_{C''} = 748 \text{ kip-ft}/1.67$ |
| $= 673 \text{ kip-ft}$ | $= 448 \text{ kip-ft}$ |
| $M_{D''} = 0.90(1{,}050 \text{ kip-ft})$ | $M_{D''} = 1{,}050 \text{ kip-ft}/1.67$ |
| $= 945 \text{ kip-ft}$ | $= 629 \text{ kip-ft}$ |

The available strength values for each design method can now be plotted. These values are superimposed on the nominal strength surfaces (with and without length effects) previously calculated for comparison purposes in Figure I.11-4.

By plotting the required axial and flexural strength values on the available strength surfaces indicated in Figure I.11-4, it can be seen that both ASD $(M_a,P_a)$ and LRFD $(M_u,P_u)$ points lie within their respective design surfaces. The member in question is therefore adequate for the applied loads.

![Graph showing compressive strength (kips) vs flexural strength (kip-ft). Two curves are shown: "Nominal Strength (without length effects)" starting at point A (~3500 kips) and descending through points C, D, B to about 800 kip-ft; and "Nominal Strength (with length effects)" starting at point A' (~3000 kips) and descending through points C', D', B' similarly. Vertical axis ranges from 0 to 4,000 kips, horizontal axis from 0 to 1,200 kip-ft.]

*Fig. I.11-3. Nominal strength interaction surfaces (with and without length effects).*

---

# I-117

As discussed previously in Step 2 as well as in AISC *Specification* Commentary Section I5, when reducing the flexural strength of Point D for length effects and resistance or safety factors, an unsafe situation could result whereby additional flexural strength is permitted at a lower axial compressive strength than predicted by the cross section capacity of the member. This effect is highlighted in the magnified portion of Figure I.11-4, where LRFD design point $D''$ closely approaches the nominal strength curve. Designs falling outside the nominal strength curve are unsafe and not permitted.

*Method 2—Simplified*

The unsafe zone discussed in the previous section for Method 2 is avoided in the Method 2—Simplified procedure by the removal of Point $D''$ from the Method 2 interaction surface $A''$, $B''$, and $C''$ as illustrated in Figure I.11-5. Reducing the number of interaction points also allows for a bilinear interaction check defined by AISC *Specification* Commentary Equations C-I5-1a and C-I5-1b to be performed.

Using the available strength values previously calculated in conjunction with the Commentary equations, interaction ratios are determined as follows:

| LRFD | ASD |
|------|-----|
| $P_r = P_u$ | $P_r = P_a$ |
| $= 1{,}170 \text{ kips} < P_{c''} = 1{,}640 \text{ kips}$ | $= 879 \text{ kips} < P_{c''} = 1{,}090 \text{ kips}$ |
| Therefore, use AISC *Specification* Commentary Equation C-I5-1a. | Therefore, use AISC *Specification* Commentary Equation C-I5-1a. |
| $\frac{M_r}{M_{cx''}} = \frac{M_u}{M_{C''}} \leq 1.0$ (from *Spec.* Comm. Eq. C-I5-1a) | $\frac{M_r}{M_{cx''}} = \frac{M_a}{M_{C''}} \leq 1.0$ (from *Spec.* Comm. Eq. C-I5-1a) |
| $\frac{670 \text{ kip-ft}}{673 \text{ kip-ft}} \leq 1.0$ | $\frac{302 \text{ kip-ft}}{448 \text{ kip-ft}} \leq 1.0$ |
| $0.996 \leq 1.0$ **o.k.** | $0.674 \leq 1.0$ **o.k.** |

![Graph showing compressive strength (kips) vs flexural strength (kip-ft). Multiple curves shown including "Nominal Strength (without length effects)", "Nominal Strength (with length effects)", "LRFD—Design", and "ASD—Design". Points labeled A, A', A'', B, B', B'', C, C', C'', D, D', D''. Design points $M_u, P_u$ and $M_a, P_a$ are marked. A magnified circular inset shows detail around point D''. Vertical axis ranges from 0 to 4,000 kips, horizontal axis from 0 to 1,200 kip-ft.]

*Fig. I.11-4. Available and nominal interaction surfaces.*

Thus, the member is adequate for the applied loads.

---

# I-118

*Comparison of Methods*

The composite member was found to be inadequate using Method 1—Chapter H interaction equations, but was found to be adequate using both Method 2 and Method 2—Simplified procedures. A comparison between the methods is most easily made by overlaying the design curves from each method as illustrated in Figure I.11-6 for LRFD design.

From Figure I.11-6, the conservative nature of the Chapter H interaction equations can be seen. Method 2 provides the highest available strength; however, Method 2—Simplified procedure also provides a good representation of the design curve. The procedure in AISC *Manual* Table 6-2a for calculating the flexural strength of Point $C''$ first requires the calculation of the flexural strength for Point $D''$. The computational effort required for the Method 2—Simplified procedure, which utilizes Point $C''$, is therefore not greatly reduced from Method 2.

*Available Shear Strength*

According to AISC *Specification* Section I4.1, there are three acceptable options for determining the available shear strength of an encased composite member:

(1) Option 1—Available shear strength of the steel section alone in accordance with AISC *Specification* Chapter G.

(2) Option 2—Available shear strength of the reinforced concrete portion alone per ACI 318.

(3) Option 3—Available shear strength of the steel section, in addition to the reinforcing steel ignoring the contribution of the concrete.

![Graph showing compressive strength (kips) vs flexural strength (kip-ft). Two curves labeled "LRFD—Method 2" and "ASD—Method 2—Simplified" with points A'', C'', D'', B'' marked. Design points $M_u, P_u$ and $M_a, P_a$ are shown. "LRFD Method 2—Simplified" and "ASD Method 2—Simplified" labels with B'' points indicated. Vertical axis ranges from 0 to 2,500 kips, horizontal axis from 0 to 1,000 kip-ft.]

*Fig. I.11-5. Comparison of Method 2 and Method 2—Simplified.*

Option 1—Available Shear Strength of Steel Section

---

# I-119

A W10×45 member meets the criteria of AISC *Specification* Section G2.1(a) according to the User Note at the end of the section. As demonstrated in Design Example I.9, No. 3 ties at 12 in. on center as illustrated in Figure I.11-1 satisfy the minimum detailing requirements of the *Specification*. The nominal shear strength may therefore be determined as:

$$C_{v1} = 1.0$$
$$(Spec. \text{ Eq. G2-2})$$

$$A_w = dt_w$$

$$= (10.1 \text{ in.})(0.350 \text{ in.})$$

$$= 3.54 \text{ in.}^2$$

$$V_n = 0.6F_y A_w C_{v1}$$
$$(Spec. \text{ Eq. G2-1})$$

$$= 0.6(50 \text{ ksi})(3.54 \text{ in.}^2)(1.0)$$

$$= 106 \text{ kips}$$

The available shear strength of the steel section is:

| LRFD | ASD |
|------|-----|
| $\phi_v = 1.00$ | $\Omega_v = 1.50$ |
| $\phi_v V_n = 1.00(106 \text{ kips})$ | $\frac{V_n}{\Omega_v} = \frac{106 \text{ kips}}{1.50}$ |
| $= 106 \text{ kips} > 95.7 \text{ kips}$ **o.k.** | $= 70.7 \text{ kips} > 57.4 \text{ kips}$ **o.k.** |

Note: AISC *Manual* Table 6-1 may also be used to obtain the available shear strength.

![Graph showing compressive strength (kips) vs flexural strength (kip-ft). Three curves shown: top curve labeled "LRFD—Method 2" starting at A'', middle dashed curve labeled "Method 1—Chapter H Interaction", bottom curve showing "LRFD Method 2—Simplified". Points labeled C'', D'', B'' with design point $M_u, P_u$ marked. Vertical axis ranges from 0 to 2,500 kips, horizontal axis from 0 to 1,000 kip-ft.]

*Fig. I.11-6. Comparison of interaction methods (LRFD).*

---

# I-120

Option 2—Available Shear Strength of the Reinforced Concrete (Concrete and Transverse Steel Reinforcement)

The available shear strength of the steel section alone has been shown to be sufficient; however, the amount of transverse reinforcement required for shear resistance in accordance with AISC *Specification* Section I4.1(b) will be determined for demonstration purposes.

*Tie Requirements for Shear Resistance*

The nominal concrete shear strength is determined from ACI 318, Table 22.5.5.1. It is assumed that $A_c \geq A_{c,min}$.

$$V_c = \left[2\lambda\sqrt{f_c'} + \frac{N_u}{6A_g}\right]b_w d$$

where
- $\lambda = 1.0$ for normal weight concrete from ACI 318, Section 19.2.4.3
- $b_w = h_1$
- $d =$ distance from extreme compression fiber to centroid of longitudinal tension reinforcement
  - $= 24 \text{ in.} - 2\frac{1}{2} \text{ in.}$
  - $= 21.5 \text{ in.}$
- $N_u = 0$ (conservatively assumed)

$$V_c = \left[2(1.0)\sqrt{5{,}000 \text{ psi} + 0}\right](24 \text{ in.})(21.5 \text{ in.})\left(\frac{1 \text{ kip}}{1{,}000 \text{ lb}}\right)$$

$$= 73.0 \text{ kips}$$

The tie requirements for shear resistance are determined from ACI 318, Chapter 22, and AISC *Specification* Section I4.1(b), as follows:

| LRFD | ASD |
|------|-----|
| $\phi_v = 0.75$ | $\Omega_v = 2.00$ |
| $\frac{A_v}{s} = \frac{V_u - \phi_v V_c}{\phi_v f_{yr} d}$ (from ACI 318, Eq. R22.5.8.5) | $\frac{A_v}{s} = \frac{V_a - (V_c / \Omega_v)}{f_{yr} d / \Omega_v}$ (from ACI 318, Eq. R22.5.8.5) |
| $= \frac{95.7 \text{ kips} - 0.75(73.0 \text{ kips})}{0.75(60 \text{ ksi})(21.5 \text{ in.})}$ | $\frac{}{} = \frac{57.4 \text{ kips} - \left(\frac{73.0 \text{ kips}}{2.00}\right)}{(60 \text{ ksi})(21.5 \text{ in.}) / 2.00}$ |
| $= 0.0423 \text{ in.}$ | $= 0.0324 \text{ in.}$ |
| Using two legs of No. 3 ties with $A_v = 0.11 \text{ in.}^2$ from ACI 318, Appendix B: | Using two legs of No. 3 ties with $A_v = 0.11 \text{ in.}^2$ from ACI 318, Appendix B: |
| $\frac{2(0.11 \text{ in.}^2)}{s} = 0.0423 \text{ in.}$ | $\frac{2(0.11 \text{ in.}^2)}{s} = 0.0324 \text{ in.}$ |
| $s = 5.20 \text{ in.}$ | $s = 6.79 \text{ in.}$ |

---

# I-121

| LRFD | ASD |
|------|-----|
| Using two legs of the No. 4 ties with $A_v = 0.20 \text{ in.}^2$: | Using two legs of the No. 4 ties with $A_v = 0.20 \text{ in.}^2$: |
| $\frac{2(0.20 \text{ in.}^2)}{s} = 0.0423 \text{ in.}$ | $\frac{2(0.20 \text{ in.}^2)}{s} = 0.0324 \text{ in.}$ |
| $s = 9.46 \text{ in.}$ | $s = 12.3 \text{ in.}$ |
| From ACI 318, Section 10.7.6.5.2, the maximum spacing is: | From ACI 318, Section 10.7.6.5.2, the maximum spacing is: |
| $s_{max} = \frac{d}{2} \leq 24 \text{ in.}$ | $s_{max} = \frac{d}{2} \leq 24 \text{ in.}$ |
| $= \frac{21.5 \text{ in.}}{2} \leq 24 \text{ in.}$ | $= \frac{21.5 \text{ in.}}{2} \leq 24 \text{ in.}$ |
| $= 10.8 \text{ in.}$ | $= 10.8 \text{ in.}$ |
| Use No. 3 ties at 5 in. o.c. or No. 4 ties at 9 in. o.c. | Use No. 3 ties at 6 in. o.c. or No. 4 ties at 10 in. o.c. |

*Minimum Reinforcing Limits*

Check that the minimum shear reinforcement is provided as required by ACI 318, Section 10.6.2.2.

$$\frac{A_{v,min}}{s} = 0.75\sqrt{f_c'}\left(\frac{b_w}{f_{yr}}\right) \geq \frac{50b_w}{f_{yr}}$$
(ACI 318, Section 10.6.2.2)

$$= \frac{0.75\sqrt{5{,}000 \text{ psi}}(24 \text{ in.})}{60{,}000 \text{ psi}} \geq \frac{50(24 \text{ in.})}{60{,}000 \text{ psi}}$$

$$= 0.0212 \text{ in.} > 0.0200 \text{ in.}$$

| LRFD | ASD |
|------|-----|
| $\frac{A_v}{s} = 0.0423 \text{ in.} > 0.0212 \text{ in.}$ **o.k.** | $\frac{A_v}{s} = 0.0324 \text{ in.} > 0.0212 \text{ in.}$ **o.k.** |

*Maximum Reinforcing Limits*

From ACI 318, Section 10.7.6.5.2, maximum stirrup spacing is reduced to the lesser of $d/4$ or 12 in. if $V_s > 4\sqrt{f_c'}b_w d$.
If No. 4 ties at 9 in. on center are selected:

$$V_s = \frac{A_v f_{yr} d}{s}$$
(ACI 318, Eq. 22.5.8.5.3)

$$= \frac{2(0.20 \text{ in.}^2)(60 \text{ ksi})(21.5 \text{ in.})}{9 \text{ in.}}$$

$$= 57.3 \text{ kips}$$

$$V_{s,max} = 4\sqrt{f_c'}b_w d$$

$$= 4\sqrt{5{,}000 \text{ psi}}(24 \text{ in.})(21.5 \text{ in.})\left(\frac{1 \text{ kip}}{1{,}000 \text{ lb}}\right)$$

$$= 146 \text{ kips} > 57.3 \text{ kips}$$

---

# I-122

Therefore, the stirrup spacing is acceptable.

*Option 3—Determine Available Shear Strength of the Steel Section plus Reinforcing Steel*

The third procedure combines the shear strength of the reinforcing steel with that of the encased steel section, ignoring the contribution of the concrete. AISC *Specification* Section I4.1(c) provides a combined resistance and safety factor for this procedure. Note that the combined resistance and safety factor takes precedence over the factors in Chapter G used for the encased steel section alone in Option 1. The amount of transverse reinforcement required for shear resistance is determined as follows:

*Tie Requirements for Shear Resistance*

The nominal shear strength of the encased steel section was previously determined to be:

$$V_{n,steel} = 106 \text{ kips}$$

The tie requirements for shear resistance are determined from ACI 318, Chapter 22, and AISC *Specification* Section I4.1(c), as follows:

| LRFD | ASD |
|------|-----|
| $\phi_v = 0.75$ | $\Omega_v = 2.00$ |
| $\frac{A_v}{s} = \frac{V_u - \phi_v V_{n,steel}}{\phi_v f_{yr} d}$ | $\frac{A_v}{s} = \frac{V_a - (V_{n,steel} / \Omega_v)}{f_{yr} d / \Omega_v}$ |
| $= \frac{95.7 \text{ kips} - 0.75(106 \text{ kips})}{0.75(60 \text{ ksi})(21.5 \text{ in.})}$ | $= \frac{57.4 \text{ kips} - (106 \text{ kips}/2.00)}{(60 \text{ ksi})(21.5 \text{ in.}) / 2.00}$ |
| $= 0.0167 \text{ in.}$ | $= 0.00682 \text{ in.}$ |

As determined in Option 2, the minimum value of $A_v/s = 0.0212$, and the maximum tie spacing for shear resistance is 10.8 in. Using two legs of No. 3 ties for $A_v$:

$$\frac{2(0.11 \text{ in.}^2)}{s} = 0.0212 \text{ in.}$$

$$s = 10.4 \text{ in.} < s_{max} = 10.8 \text{ in.}$$

Use No. 3 ties at 10 in. o.c.

*Summary and Comparison of Available Shear Strength Calculations*

The use of the steel section alone is the most expedient method for calculating available shear strength and allows the use of a tie spacing which may be greater than that required for shear resistance by ACI 318. Where the strength of the steel section alone is not adequate, Option 3 will generally result in reduced tie reinforcement requirements as compared to Option 2.

*Force Allocation and Load Transfer*

Load transfer calculations should be performed in accordance with AISC *Specification* Section I6. The specific application of the load transfer provisions is dependent upon the configuration and detailing of the connecting elements. Expanded treatment of the application of load transfer provisions for encased composite members is provided in Design Example I.8 and AISC Design Guide 6.

---

# I-123

## EXAMPLE I.12 STEEL ANCHORS IN COMPOSITE COMPONENTS

**Given:**

Select an appropriate ¾-in.-diameter, AWS D1.1/D1.1M Type B steel headed stud anchor to resist the dead and live loads indicated in Figure I.12-1. The anchor is part of a composite system that may be designed using the steel anchor in composite components provisions of AISC *Specification* Section I8.3.

![Diagram showing a cross-section of HSS wall with concrete fill. A steel headed stud anchor is embedded in the concrete, with loads indicated: $P_D = 3$ kips, $P_L = 7.5$ kips vertically, and $V_D = 2$ kips, $V_L = 5$ kips horizontally. Height H is marked on the right side.]

*Fig. I.12-1. Steel headed stud anchor and applied loading.*

The steel headed stud anchor is encased by normal weight (145 lb/ft³) reinforced concrete having a specified concrete compressive strength, $f_c' = 5$ ksi. In accordance with AISC *Manual* Part 2, headed stud anchors shall be in accordance with AWS D1.1/D1.1M with a specified tensile stress, $F_u$, of 65 ksi.

The anchor is located away from edges such that concrete breakout in shear is not a viable limit state, and the nearest anchor is located 24 in. away. The concrete is considered to be uncracked.

**Solution:**

*Minimum Anchor Length*

AISC *Specification* Section I8.3 provides minimum length-to-shank diameter ratios for anchors subjected to shear, tension, and interaction of shear and tension in both normal weight and lightweight concrete. These ratios are also summarized in the User Note provided within Section I8.3. For normal weight concrete subject to shear and tension, $h/d_{sa} \geq 8$; thus:

$$h \geq 8d_{sa}$$

$$\geq 8(\frac{3}{4} \text{ in.})$$

$$\geq 6.00 \text{ in.}$$

This length is measured from the base of the steel headed stud anchor to the top of the head after installation. From anchor manufacturer's data, a standard stock length of 6⅝ in. is selected. Using a ⅛ in. length reduction to account for burn off during installation yields a final installed length of 6.00 in.

6.00 in. = 6.00 in. **o.k.**

Select a ¾-in.-diameter × 6⅞-in.-long headed stud anchor.

---

# I-124

*Required Shear and Tensile Strength*

From ASCE/SEI 7, Chapter 2, the required shear and tensile strengths are:

| LRFD | ASD |
|------|-----|
| Governing load combination for interaction<br>$= 1.2D + 1.6L$ | Governing load combination for interaction<br>$= D + L$ |
| $Q_{uv} = 1.2(2 \text{ kips}) + 1.6(5 \text{ kips})$ | $Q_{av} = 2 \text{ kips} + 5 \text{ kips}$ |
| $= 10.4 \text{ kips (shear)}$ | $= 7.00 \text{ kips (shear)}$ |
| $Q_{ut} = 1.2(3 \text{ kips}) + 1.6(7.5 \text{ kips})$ | $Q_{at} = 3 \text{ kips} + 7.5 \text{ kips}$ |
| $= 15.6 \text{ kips (tension)}$ | $= 10.5 \text{ kips (tension)}$ |

*Available Shear Strength*

Per the problem statement, concrete breakout is not considered to be an applicable limit state. AISC *Specification* Equation I8-3 may therefore be used to determine the available shear strength of the steel headed stud anchor as follows:

$$Q_{nv} = F_u A_{sa}$$
$(Spec. \text{ Eq. I8-3})$

where
- $A_{sa} =$ cross-sectional area of steel headed stud anchor

$$= \frac{\pi(\frac{3}{4} \text{ in.})^2}{4}$$

$$= 0.442 \text{ in.}^2$$

$$Q_{nv} = (65 \text{ ksi})(0.442 \text{ in.}^2)$$

$$= 28.7 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi_v = 0.65$ | $\Omega_v = 2.31$ |
| $\phi_v Q_{nv} = 0.65(28.7 \text{ kips})$ | $\frac{Q_{nv}}{\Omega_v} = \frac{28.7 \text{ kips}}{2.31}$ |
| $= 18.7 \text{ kips}$ | $= 12.4 \text{ kips}$ |

Alternately, available shear strengths can be selected directly from Table I.12-1 located at the end of this example.

*Available Tensile Strength*

The nominal tensile strength of a steel headed stud anchor is determined using AISC *Specification* Equation I8-4 provided the edge and spacing limitations of AISC *Specification* Section I8.3b are met as follows:

(1) Minimum distance from centerline of anchor to free edge: $1.5h = 1.5(6.00 \text{ in.}) = 9.00 \text{ in.}$

There are no free edges, therefore this limitation does not apply.

---

# I-125

(2) Minimum distance between centerlines of adjacent anchors: $3h = 3(6.00 \text{ in.}) = 18.0 \text{ in.}$

18.0 in. < 24 in. **o.k.**

*Specification* Equation I8-4 may therefore be used as follows:

$$Q_{nt} = F_u A_{sa}$$
$(Spec. \text{ Eq. I8-4})$

$$= (65 \text{ ksi})(0.442 \text{ in.}^2)$$

$$= 28.7 \text{ kips}$$

| LRFD | ASD |
|------|-----|
| $\phi_t = 0.75$ | $\Omega_t = 2.00$ |
| $\phi_t Q_{nt} = 0.75(28.7 \text{ kips})$ | $\frac{Q_{nt}}{\Omega_t} = \frac{28.7 \text{ kips}}{2.00}$ |
| $= 21.5 \text{ kips}$ | $= 14.4 \text{ kips}$ |

Alternately, available tensile strengths can be selected directly from Table I.12-1 located at the end of this example.

*Interaction of Shear and Tension*

The detailing limits on edge distances and spacing imposed by AISC *Specification* Section I8.3c for shear and tension interaction are the same as those previously reviewed separately for tension and shear alone. Tension and shear interaction is checked using *Specification*, Equation I8-5 which can be written in terms of LRFD and ASD design as follows:

| LRFD | ASD |
|------|-----|
| $\left(\frac{Q_{ut}}{\phi_t Q_{nt}}\right)^{5/3} + \left(\frac{Q_{uv}}{\phi_v Q_{nv}}\right)^{5/3} \leq 1.0$ (from *Spec.* Eq. I8-5) | $\left(\frac{Q_{at}}{Q_{nt}/\Omega_t}\right)^{5/3} + \left(\frac{Q_{av}}{Q_{nv}/\Omega_v}\right)^{5/3} \leq 1.0$ (from *Spec.* Eq. I8-5) |
| $\left(\frac{15.6 \text{ kips}}{21.5 \text{ kips}}\right)^{5/3} + \left(\frac{10.4 \text{ kips}}{18.7 \text{ kips}}\right)^{5/3} = 0.962$ | $\left(\frac{10.5 \text{ kips}}{14.4 \text{ kips}}\right)^{5/3} + \left(\frac{7.00 \text{ kips}}{12.4 \text{ kips}}\right)^{5/3} = 0.976$ |
| $0.962 < 1.0$ **o.k.** | $0.976 < 1.0$ **o.k.** |

Thus, a ¾-in.-diameter × 6⅞-in.-long headed stud anchor is adequate for the applied loads.

*Limits of Application*

The application of the steel anchors in composite component provisions have strict limitations as summarized in the User Note provided at the beginning of AISC *Specification* Section I8.3. These provisions do not apply to typical composite beam designs nor do they apply to hybrid construction where the steel and concrete do not resist loads together via composite action, such as with embed plates. This design example is intended solely to illustrate the calculations associated with an isolated anchor that is part of an applicable composite system.

*Available Strength Table*

Table I.12-1 provides available shear and tension strengths for standard Type B steel headed stud anchors conforming to the requirements of AWS D1.1/D1.1M for use in composite components.

---

# I-126

**Table I.12-1**
**Steel Headed Stud Anchor Available Strengths**

| **Anchor<br>Shank<br>Diameter** | $A_{sa}$ | $Q_{nv}/\Omega_v$ | $\phi_v Q_{nv}$ | $Q_{nt}/\Omega_t$ | $\phi_t Q_{nt}$ |
|------|------|------|------|------|------|
| **in.** | **in.²** | **kips** | **kips** | **kips** | **kips** |
|  |  | **ASD** | **LRFD** | **ASD** | **LRFD** |
| ½ | 0.196 | 5.52 | 8.30 | 6.38 | 9.57 |
| ⅝ | 0.307 | 8.63 | 13.0 | 9.97 | 15.0 |
| ¾ | 0.442 | 12.4 | 18.7 | 14.4 | 21.5 |
| ⅞ | 0.601 | 16.9 | 25.4 | [a] | [a] |
| 1 | 0.785 | 22.1 | 33.2 | 25.5 | 38.3 |
| **ASD** | **LRFD** | [a] ⅞-in.-diameter anchors conforming to AWS D1.1/D1.1M, Figure 9.1, do<br>not meet the minimum head-to-shank diameter ratio of 1.6 as required for<br>tensile resistance per AISC *Specification* Section I8.3. |
| $\Omega_v = 2.31$ | $\phi_v = 0.65$ |  |
| $\Omega_t = 2.00$ | $\phi_t = 0.75$ |  |

---

# I-127

## EXAMPLE I.13 COMPOSITE COLLECTOR BEAM DESIGN

**Given:**

Determine if the composite beam designed in Example I.1 is adequate to serve as a collector beam for the transfer of wind-induced compression forces in combination with gravity loading as indicated in Figure I.13. Applied forces were generated from an elastic analysis, and stability will be accounted for using the effective length method of design.

$$w_D = 0.9 \text{ kip/ft}$$
$$w_L = 1 \text{ kip/ft}$$
$$w_w = 0.556 \text{ kip/ft}$$

![Diagram showing a composite collector beam elevation. The beam spans 45'-0" with a pin support on the left and roller support on the right. Distributed loads $w_D = 0.9$ kip/ft and $w_L = 1$ kip/ft are shown on the left half, and $w_w = 0.556$ kip/ft on the right half. Hatching indicates fixed support at left end.]

*Fig. I.13. Composite collector beam and applied loading elevation.*

**Solution:**

From AISC *Manual* Table 1-1, the geometric properties are as follows:

W21×50
- $A = 14.7 \text{ in.}^2$
- $I_x = 984 \text{ in.}^4$
- $I_y = 24.9 \text{ in.}^4$
- $J = 1.14 \text{ in.}^4$
- $b_f = 6.53 \text{ in.}$
- $d = 20.8 \text{ in.}$
- $r_x = 8.18 \text{ in.}$
- $r_y = 1.30 \text{ in.}$
- $t_w = 0.380 \text{ in.}$
- $h/2t_f = 6.1$
- $h_o = 49.4$
- $h_o = 20.3 \text{ in.}$

Refer to Example I.1 for additional information regarding strength and serviceability requirements associated with pre-composite and composite gravity load conditions.

*Required Compressive Strength*

From ASCE/SEI 7, Chapter 2, the required axial strength for the governing load combination, including wind, is:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2D + 1.0W + L$ | $P_a = D + 0.75L + 0.75(0.6W)$ |
| $= 1.2(0 \text{ kips}) + 1.0(0.556 \text{ kip/ft})(45 \text{ ft}) + 0 \text{ kips}$ | $= 0 \text{ kips} + 0.75(0 \text{ kips})$ |
| $= 25.0 \text{ kips}$ | $+ 0.75(0.6)(0.556 \text{ kip/ft})(45 \text{ ft})$ |
|  | $= 11.3 \text{ kips}$ |

*Available Compressive Strength (General)*

The collector element is conservatively treated as a bare steel member for the determination of available compressive strength as discussed in AISC *Specification* Commentary Section I7. The effective length factor, $K$, for a pin-ended member is taken as 1.0 in accordance with Table C-A-7.1. Potential limit states are flexural buckling about both the minor and major axes and torsional buckling.

Lateral movement is assumed to be braced by the composite slab; thus weak-axis flexural buckling will not govern by inspection because $L_{cy} = (KL)_y = 0$.

---

# I-128

The member is slender for compression as indicated in AISC *Manual* Table 1-1; thus strong-axis flexural buckling strength is determined in accordance with AISC *Specification* Section E7 for members with slender elements for $L_{cx} = (KL)_x = 45.0 \text{ ft}$.

The composite slab will prevent the member from twisting about its shear center, thus torsional buckling is not a valid limit state; however, constrained-axis torsional buckling may occur as discussed in AISC *Specification* Commentary Section E4 with $L_{cz} = (KL)_z = 1.0(45 \text{ ft}) = 45.0 \text{ ft}$.

Compute the available compressive strengths for the limit states of strong-axis flexural buckling and constrained-axis torsional buckling to determine the controlling strength.

*Strong-Axis Flexural Buckling*

Calculate the critical stress about the strong axis, $F_{ex}$, in accordance with AISC *Specification* Section E3 as directed by *Specification* Section E7 for members with slender elements.

$$\frac{L_{cx}}{r_x} = \frac{(45.0 \text{ ft})(12 \text{ in./ft})}{8.18 \text{ in.}}$$

$$= 66.0$$

$$4.71\sqrt{\frac{E}{F_y}} = 4.71\sqrt{\frac{29{,}000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 113 > 66.0; \text{ therefore, use AISC } Specification \text{ Equation E3-2}$$

$$F_{ex} = \frac{\pi^2 E}{\left(\frac{L_{cx}}{r_x}\right)^2}$$
(from *Spec.* Eq. E3-4)

$$= \frac{\pi^2(29{,}000 \text{ ksi})}{(66.0)^2}$$

$$= 65.7 \text{ ksi}$$

$$F_{nx} = \left(0.658^{\frac{F_y}{F_{ex}}}\right)F_y$$
(from *Spec.* Eq. E3-2)

$$= \left(0.658^{\frac{50 \text{ ksi}}{65.7 \text{ ksi}}}\right)(50 \text{ ksi})$$

$$= 36.4 \text{ ksi}$$

Classify each component of the wide-flange member for local buckling.

Flange local buckling classification as determined from AISC *Specification* Table B4.1a, Case 1:

$$\lambda_f = 0.56\sqrt{\frac{E}{F_y}}$$

$$= 0.56\sqrt{\frac{29{,}000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 13.5$$

---

# I-129

$$\lambda = \frac{b_f}{2t_f}$$

$$= 6.10 < 13.5; \text{ therefore, the flanges are nonslender and fully effective}$$

Web local buckling classification as determined from AISC *Specification* Table B4.1a, Case 5:

$$\lambda_r = 1.49\sqrt{\frac{E}{F_y}}$$

$$= 1.49\sqrt{\frac{29{,}000 \text{ ksi}}{50 \text{ ksi}}}$$

$$= 35.9$$

$$\lambda = \frac{h}{t_w}$$

$$= 49.4 > 35.9; \text{ therefore, the web is slender}$$

To evaluate the impact of web slenderness on strong-axis flexural buckling, determine if a reduced effective web width, $h_e$, is required in accordance with AISC *Specification* Section E7.1 as follows:

$$\lambda_r\sqrt{\frac{F_y}{F_{nx}}} = 35.9\sqrt{\frac{50 \text{ ksi}}{36.4 \text{ ksi}}}$$

$$= 42.1 < \lambda = 49.4; \text{ therefore, use AISC } Specification \text{ Equation E7-3 to determine } h_e$$

The effective width imperfection adjustment factors, $c_1$ and $c_2$, are selected from AISC *Specification* Table E7.1, Case (a):

$$c_1 = 0.18$$
$$c_2 = 1.31$$

$$F_{el} = \left(c_2\frac{\lambda_r}{\lambda}\right)^2 F_y$$
$(Spec. \text{ Eq. E7-5})$

$$= \left[1.31\left(\frac{35.9}{49.4}\right)\right]^2(50 \text{ ksi})$$

$$= 45.3 \text{ ksi}$$

$$h = \left(\frac{h}{t_w}\right)t_w$$

$$= (49.4)(0.380 \text{ in.})$$

$$= 18.8 \text{ in.}$$

$$h_e = h\left[1 - c_1\sqrt{\frac{F_{el}}{F_y}}\right]\sqrt{\frac{F_{el}}{F_y}}$$
(from *Spec.* Eq. E7-3)

$$= (18.8 \text{ in.})\left[1 - 0.18\sqrt{\frac{45.3 \text{ ksi}}{36.4 \text{ ksi}}}\right]\sqrt{\frac{45.3 \text{ ksi}}{36.4 \text{ ksi}}}$$

$$= 16.8 \text{ in.}$$

---

# I-130

Calculate the effective area of the section:

$$A_e = A - (h - h_e)t_w$$

$$= 14.7 \text{ in.}^2 - (18.8 \text{ in.} - 16.8 \text{ in.})(0.380 \text{ in.})$$

$$= 13.9 \text{ in.}^2$$

Calculate the nominal compressive strength:

$$P_{nx} = F_{nx} A_e$$
(from *Spec.* Eq. E7-1)

$$= (36.4 \text{ ksi})(13.9 \text{ in.}^2)$$

$$= 506 \text{ kips}$$

Calculate the available compressive strength:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.90$ | $\Omega_c = 1.67$ |
| $\phi_c P_n = 0.90(506 \text{ kips})$ | $\frac{P_n}{\Omega_c} = \frac{506 \text{ kips}}{1.67}$ |
| $= 455 \text{ kips}$ | $= 303 \text{ kips}$ |

*Constrained-Axis Torsional Buckling*

Assuming the composite slab provides a lateral bracing point at the top flange of the beam, the constrained-axis buckling stress, $F_{ez}$, can be determined using AISC *Specification* Equation E4-10 as follows:

The distance to the bracing point from the shear center along the minor $(y-y)$ axis is:

$$y_o = \frac{d}{2}$$

$$= \frac{20.8 \text{ in.}}{2}$$

$$= 10.4 \text{ in.}$$

The distance to the bracing point from the shear center along the major $(x-x)$ axis is:

$$x_o = 0$$

$$r_o^2 = r_x^2 + r_y^2 + y_o^2 + x_o^2$$
$(Spec. \text{ Eq. E4-11})$

$$= (8.18 \text{ in.})^2 + (1.30 \text{ in.})^2 + (10.4 \text{ in.})^2 + (0 \text{ in.})^2$$

$$= 177 \text{ in.}^2$$

$$L_{cz} = (KL)_z$$

$$= (45.0 \text{ ft})(12 \text{ in./ft})$$

$$= 540 \text{ in.}$$

---

# I-131

$$F_{ez} = \left[\frac{\pi^2 EI_y}{L_{cz}^2}\left(\frac{h_o^2}{4} + y_o^2\right) + GJ\right]\frac{1}{Ar_o^2}$$
(from *Spec.* Eq. E4-10)

$$= \left[\frac{\pi^2(29{,}000 \text{ ksi})(24.9 \text{ in.}^4)}{[(45.0 \text{ ft})(12 \text{ in./ft})]^2}\left[\frac{(20.3 \text{ in.})^2}{4} + (10.4 \text{ in.})^2\right] + (11{,}200 \text{ ksi})(1.14 \text{ in.}^4)\right\}$$

$$\times \frac{1}{(14.7 \text{ in.}^2)(177 \text{ in.}^2)}$$

$$= 6.89 \text{ ksi}$$

To evaluate the impact of web slenderness on constrained-axis torsional buckling, determine if a reduced effective web width, $h_e$, is required in accordance with AISC *Specification* Section E7.1 as follows:

$$\lambda_r\sqrt{\frac{F_y}{F_{ez}}} = 35.9\sqrt{\frac{50 \text{ ksi}}{6.89 \text{ ksi}}}$$

$$= 96.7 > \lambda = 46.4; \text{ therefore use AISC } Specification \text{ Equation E7-2}$$

$$h_e = h$$
(from *Spec.* Eq. E7-2)

Thus the full steel area may be used without reduction and the available compressive strength for constrained axis buckling is calculated as follows:

$$\frac{F_y}{F_{ez}} = \frac{50 \text{ ksi}}{6.89 \text{ ksi}}$$

$$= 7.26 > 2.25, \text{ therefore, use AISC } Specification \text{ Equation E3-3}$$

$$F_{nz} = 0.877F_{ez}$$
(from *Spec.* Eq. E3-3)

$$= 0.877(6.89 \text{ ksi})$$

$$= 6.04 \text{ ksi}$$

The nominal compressive strength is calculated with no reduction for slenderness, $A_e = A$, as follows:

$$P_{nz} = F_{nz} A_e$$
(from *Spec.* Eq. E7-1)

$$= (6.04 \text{ ksi})(14.7 \text{ in.}^2)$$

$$= 88.8 \text{ kips}$$

The available compressive strength is determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi_c = 0.90$ | $\Omega_c = 1.67$ |
| $\phi_c P_{nz} = 0.90(88.8 \text{ kips})$ | $\frac{P_{nz}}{\Omega_c} = \frac{88.8 \text{ kips}}{1.67}$ |
| $= 79.9 \text{ kips}$ | $= 53.2 \text{ kips}$ |

Note that it may be possible to utilize the flexural stiffness and strength of the slab as a continuous torsional restraint, resulting in increased constrained-axis torsional buckling capacity; however, that exercise is beyond the scope of this design example.

---

# I-132

A summary of the available compressive strength for each of the viable limit states is as follows:

| LRFD | ASD |
|------|-----|
| Strong-axis flexural buckling: | Strong-axis flexural buckling: |
| $\phi_c P_{nx} = 455 \text{ kips}$ | $\frac{P_{nx}}{\Omega_c} = 303 \text{ kips}$ |
| Constrained-axis torsional buckling: | Constrained-axis torsional buckling: |
| $\phi_c P_{nz} = 79.9 \text{ kips}$ **controls** | $\frac{P_{nz}}{\Omega_c} = 53.2 \text{ kips}$ **controls** |

*Required First-Order Flexural Strength*

From ASCE/SEI 7, Chapter 2, the required first-order flexural strength for the governing load combination including wind is:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2D + 1.0W + L$ | $w_a = D + 0.75L + 0.75(0.6W)$ |
| $= 1.2(0.9 \text{ kip/ft}) + 1.0(0 \text{ kip/ft}) + 1 \text{ kip/ft}$ | $= 0.9 \text{ kip/ft} + 0.75(1 \text{ kip/ft}) + 0.75(0.6)(0 \text{ kip/ft})$ |
| $= 2.08 \text{ kip/ft}$ | $= 1.65 \text{ kip/ft}$ |
| $M_u = \frac{w_u L^2}{8}$ | $M_a = \frac{w_a L^2}{8}$ |
| $= \frac{(2.08 \text{ kip/ft})(45 \text{ ft})^2}{8}$ | $= \frac{(1.65 \text{ kip/ft})(45 \text{ ft})^2}{8}$ |
| $= 527 \text{ kip-ft}$ | $= 418 \text{ kip-ft}$ |

*Required Second-Order Flexural Strength*

The effective length method is utilized to consider stability for this element as permitted by AISC *Specification* Section C1.2 and Appendix 7.2. The addition of axial load will magnify the required first-order flexural strength due to member slenderness $(P-\delta)$ effects. This magnified moment (second-order analysis) can be approximated utilizing the procedure provided in AISC *Specification* Appendix 8 as permitted by Section C2.1b.

Calculate the elastic critical buckling strength of the member in the plane of bending (in this case about the strong-axis of the beam) from AISC *Specification* Appendix 8, Section 8.1.2. For the effective length method, $EI^*$ is taken as $EI$ in accordance with Appendix 8.1.2, and the effective length, $L_{c3}$ is taken as $(KL)_y$ in accordance with Appendix 7.2.3. As illustrated previously, $K$ is taken as 1.0 for a pin-ended member. Conservatively using the bare steel beam moment of inertia, the buckling strength is calculated as follows:

$$P_{e1} = \frac{\pi^2 EI^*}{(L_{c1})^2}$$
$(Spec. \text{ Eq. A-8-5})$

$$= \frac{\pi^2 EI}{(KL)_y^2}$$ (for the effective length method)

$$= \frac{\pi^2(29{,}000 \text{ ksi})(984 \text{ in.}^4)}{[(45.0 \text{ ft})(12 \text{ in./ft})]^2}$$

$$= 966 \text{ kips}$$

---

# I-133

For beam-columns subject to transverse loading between supports, the value of $C_m$ is taken as 1.0 as permitted by AISC *Specification* Appendix 8, Section 8.1.2, and $B_1$ is calculated from *Specification* Equation A-8-3 as follows:

| LRFD | ASD |
|------|-----|
| $B_1 = \frac{C_m}{1 - \alpha P_r / P_{e1}} \geq 1$ | $B_1 = \frac{C_m}{1 - \alpha P_r / P_{e1}} \geq 1$ |
| $= \frac{1.0}{1 - 1.0\left(\frac{25.0 \text{ kips}}{966 \text{ kips}}\right)} \geq 1$ | $= \frac{1.0}{1 - 1.6\left(\frac{11.3 \text{ kips}}{966 \text{ kips}}\right)} \geq 1$ |
| $= 1.03$ | $= 1.02$ |

Noting that the first-order moment is induced by vertical dead and live loading, it is classified as a non-translational moment, $M_{nt}$, in accordance with AISC *Specification* Section 8.1. The required second-order flexural strength is therefore calculated using AISC *Specification* Equation A-8-1 as:

| LRFD | ASD |
|------|-----|
| $M_u = B_1 M_{nt} + B_2 M_{lt}$ | $M_a = B_1 M_{nt} + B_2 M_{lt}$ |
| $= 1.03(527 \text{ kip-ft}) + 0$ | $= 1.02(418 \text{ kip-ft}) + 0$ |
| $= 543 \text{ kip-ft}$ | $= 426 \text{ kip-ft}$ |

*Available Flexural Strength*

The available flexural strength of the composite beam is calculated in Example I.1 as:

| LRFD | ASD |
|------|-----|
| $\phi_b M_{nx} = 769 \text{ kip-ft}$ | $\frac{M_{nx}}{\Omega_b} = 512 \text{ kip-ft}$ |

*Interaction of Axial Force and Flexure*

Interaction between axial forces and flexure in composite collector beams is addressed in AISC *Specification* Commentary Section I7, which states that the non-composite axial strength and the composite flexural strength may be used with the interaction equations provided in Chapter H as a reasonable simplification for design purposes. This procedure is illustrated as follows:

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 79.9 \text{ kips}$ | $\frac{P_n}{\Omega_c} = 53.2 \text{ kips}$ |
| $\phi_b M_{nx} = 769 \text{ kip-ft}$ | $\frac{M_{nx}}{\Omega_b} = 512 \text{ kip-ft}$ |
| $\frac{P_r}{P_c} = \frac{P_u}{\phi_c P_n}$ | $\frac{P_r}{P_c} = \frac{P_a}{P_n/\Omega_c}$ |
| $= \frac{25.0 \text{ kips}}{79.9 \text{ kips}}$ | $= \frac{11.3 \text{ kips}}{53.2 \text{ kips}}$ |
| $= 0.313 > 0.2$ | $= 0.212 > 0.2$ |

---

# I-134

| LRFD | ASD |
|------|-----|
| Therefore, use AISC *Specification* Equation H1-1a. | Therefore, use AISC *Specification* Equation H1-1a. |
| $\frac{P_r}{\phi_c P_n} + \frac{8}{9}\left(\frac{M_u}{\phi_b M_{nx}}\right) \leq 1.0$ | $\frac{P_r}{P_n/\Omega_c} + \frac{8}{9}\left(\frac{M_a}{M_{nx}/\Omega_b}\right) \leq 1.0$ |
| $0.313 + \frac{8}{9}\left(\frac{543 \text{ kip-ft}}{769 \text{ kip-ft}}\right) \leq 1.0$ | $0.212 + \frac{8}{9}\left(\frac{426 \text{ kip-ft}}{512 \text{ kip-ft}}\right) \leq 1.0$ |
| $0.941 < 1.0$ **o.k.** | $0.952 < 1.0$ **o.k.** |

The collector element is adequate to resist the imposed loads.

*Load Introduction Effects*

AISC *Specification* Commentary Section I7 indicates that the effect of the vertical offset between the plane of the diaphragm and the collector element should be investigated. It has been shown that the resulting eccentricity between the plane of axial load introduction in the slab and the centroid of the beam connections does not result in any additional flexural demand, assuming the axial load is introduced uniformly along the length of the beam; however, this eccentricity will result in additional shear reactions (Burmeister and Jacobs, 2008). The additional shear reaction assuming an eccentricity of $d/2$ is calculated as follows:

| LRFD | ASD |
|------|-----|
| $V_{u,add} = \frac{P_u d}{2L}$ | $V_{a,add} = \frac{P_a d}{2L}$ |
| $= \frac{(25.0 \text{ kips})(20.8 \text{ in.})}{2(45 \text{ ft})(12 \text{ in./ft})}$ | $= \frac{(11.3 \text{ kips})(20.8 \text{ in.})}{2(45 \text{ ft})(12 \text{ in./ft})}$ |
| $= 0.481 \text{ kips}$ | $= 0.218 \text{ kips}$ |

As can be seen from these results, the additional vertical shear due to the axial collector force is quite small and in most instances will be negligible versus the governing shear resulting from gravity-only load combinations.

*Shear Connection*

AISC *Specification* Commentary Section I7 notes that it is not required to superimpose the horizontal shear due to lateral forces with the horizontal shear due to flexure for the determination of steel anchor requirements, thus the summation of nominal strengths for all steel anchors and their length may be used for axial force transfer. Specific resistance and safety factors for this condition are not provided in Section I8.2 because they are implicitly accounted for within the system resistance and safety factors used for the determination of the available flexural strength of the beam. Until additional research becomes available, a conservative approach is to apply the composite component factors from *Specification* Section I8.3 to the nominal steel anchor strength determined from *Specification* Section I8.2.

From Example I.1, the strength for ¾-in.-diameter anchors in normal weight concrete with $f_c' = 4$ ksi and deck oriented perpendicular to the beam is:

- 1 anchor per rib: $Q_n = 17.2$ kips/anchor
- 2 anchors per rib: $Q_n = 14.6$ kips/anchor

Over the entire beam length, there are 42 anchors in positions with one anchor per rib and four anchors in positions with two anchors per rib, thus the total available strength for diaphragm shear transfer is:

---

# I-135

| LRFD | ASD |
|------|-----|
| $\phi_v = 0.65$ | $\Omega_v = 2.31$ |
| $\phi_v P_n = 0.65\left[\frac{42(17.2 \text{ kips/anchor})}{+ 4(14.6 \text{ kips/anchor})}\right]$ | $\frac{P_n}{\Omega_v} = \frac{42(17.2 \text{ kips/anchor}) + 4(14.6 \text{ kips/anchor})}{2.31}$ |
| $= 508 \text{ kips} > 25.0 \text{ kips}$ **o.k.** | $= 338 \text{ kips} > 11.3 \text{ kips}$ **o.k.** |

Note that the longitudinal available shear strength of the diaphragm itself (consisting of the composite deck and concrete fill) will often limit the amount of force that can be introduced into the collector beam and should also be evaluated as part of the overall design.

*Summary*

A W21×50 collector with 46, ¾-in.-diameter by 4⅝-in.-long, steel headed stud anchors is adequate to resist the imposed loads.

---

# I-136

## CHAPTER I DESIGN EXAMPLE REFERENCES

ACI 318 (2019), *Building Code Requirements for Structural Concrete and Commentary*, ACI 318-19 and ACI 318M-19; American Concrete Institute, Farmington Hills, Mich.

ASCE (2014), *Design Loads on Structures During Construction*, ASCE/SEI 37-14, American Society of Civil Engineers, Reston, Va.

AWS (2020), *Structural Welding Code—Steel*, AWS D1.1/D1.1M:2020, American Welding Society, Miami, Fla.

Burmeister, A. and Jacobs, W.P. (2008), "Unified Proof: Horizontal Floor Diaphragm Load Effects on Composite Beam Design," *Modern Steel Construction*, AISC, December.

Griffis, L.G. (1992), *Load and Resistance Factor Design of W-Shapes Encased in Concrete*, Design Guide 6, AISC, Chicago, Ill.

ICC (2021), *International Building Code*, International Code Council, Country Club Hills, Ill.

Leon, R.T. and Hajjar, J.F. (2008), "Limit State Response of Composite Columns and Beam-Columns Part 2: Application of Design Provisions for the 2005 AISC Specification," *Engineering Journal*, AISC, Vol. 45, No. 1, pp. 21–46.

Mujagic, J.R., Easterling, W.S., Bennett, J.S., and Varma, A.H. (2015), "Assessment of Shear Connection Ductility in Composite Beams—Implications on the U.S. Design Practice," Report No. CE/VPI-15/12, Virginia Polytechnic Institute and State University, Blacksburg, Va.

Murray, T.M., Allen, D.E., and Ungar, E.E., and Davis, D.B. (2016), *Vibrations of Steel-Framed Structural Systems Due to Human Activity*, Design Guide 11, 2nd Ed., AISC, Chicago, Ill.

Oehlers, D.J. and Sved, G. (1995), "Flexural Strength of Composite Beams with Limited Slip Capacity Shear Connectors," *Journal of Structural Engineering*, ASCE, Vol. 121, No. 6, pp. 932–938.

Park, R. and Gamble, W.L. (2000), *Reinforced Concrete Slabs*, 2nd Ed., John Wiley & Sons, New York, N.Y.

SDI (2017), *Standard for Composite Steel Floor Deck-Slabs*, ANSI/SDI C-2017, Glenshaw, Pa.

West, M.A., Fisher, J.M., and Griffis, L.G. (2003), *Serviceability Design Consideration for Steel Buildings*, Design Guide 3, 2nd Ed., AISC, Chicago, Ill.

Young, W.C. and Budynas, R.C. (2002), *Roark's Formulas for Stress and Strain*, 7th Ed., McGraw-Hill, New York, N.Y.

---
