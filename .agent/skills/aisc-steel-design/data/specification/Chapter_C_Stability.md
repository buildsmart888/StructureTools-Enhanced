# Chapter C: Stability

**AISC 360-22 Specification for Structural Steel Buildings**
**Original PDF Pages**: 94-99 (6 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Design for Stability

**Description**: Direct analysis method and stability requirements

---

# CHAPTER C
# DESIGN FOR STABILITY

This chapter addresses requirements for the design of structures for stability. The direct analysis method is presented herein.

The chapter is organized as follows:

- C1. General Stability Requirements
- C2. Calculation of Required Strengths
- C3. Calculation of Available Strengths

**User Note:** Alternative methods for the design of structures for stability are provided in Appendices 1 and 7. Appendix 1 provides alternatives that allow consideration of member imperfections and/or inelasticity directly within the analysis and provides for a more detailed evaluation of the limit states. Appendix 7 provides the effective length method and a first-order elastic method.

## C1. GENERAL STABILITY REQUIREMENTS

Stability shall be provided for the structure as a whole and for each of its elements. The effects of the following on the stability of the structure and structural elements shall be considered: (a) flexural, shear, and axial member deformations, and all other component and connection deformations that contribute to displacements of the structure; (b) second-order effects (including $P$-Δ and $P$-δ effects); (c) geometric imperfections; (d) stiffness reductions due to inelasticity, including the effect of partial yielding of the cross section which may be accentuated by the presence of residual stresses; and (e) uncertainty in system, member, and connection strength and stiffness. All load-dependent effects shall be calculated at a level of loading corresponding to LRFD load combinations or 1.6 times ASD load combinations.

Any rational method of design for stability that considers all of the listed effects is permitted; this includes the methods identified in Sections C1.1 and C1.2.

**User Note:** See Commentary Section C1 and Table C-C1.1 for an explanation of how requirements (a) through (e) of Section C1 are satisfied in the methods of design listed in Sections C1.1 and C1.2.

### 1. Direct Analysis Method of Design

The direct analysis method of design is permitted for all structures and can be based on either elastic or inelastic analysis. For design by elastic analysis, required strengths shall be calculated in accordance with Section C2 and the calculation of available strengths in accordance with Section C3. For design by advanced analysis, the provisions of Appendix 1, Section 1.1, and Section 1.2 or 1.3, shall be satisfied.

---

## CALCULATION OF REQUIRED STRENGTHS [Sect. C2.]

### 2. Alternative Methods of Design

The effective length method and the first-order analysis method, both defined in Appendix 7, are based on elastic analysis and are permitted as alternatives to the direct analysis method for structures that satisfy the limitations specified in that appendix.

## C2. CALCULATION OF REQUIRED STRENGTHS

For the direct analysis method of design, the required strengths of components of the structure shall be determined from an elastic analysis conforming to Section C2.1. The analysis shall include consideration of initial imperfections in accordance with Section C2.2 and adjustments to stiffness in accordance with Section C2.3.

### 1. General Analysis Requirements

The analysis of the structure shall conform to the following requirements:

(a) The analysis shall consider flexural, shear, and axial member deformations, and all other component and connection deformations that contribute to displacements of the structure. The analysis shall incorporate reductions in all stiffnesses that are considered to contribute to the stability of the structure, as specified in Section C2.3.

(b) The analysis shall be a second-order analysis that considers both $P$-Δ and $P$-δ effects, except that it is permissible to neglect the effect of $P$-δ on the response of the structure when the following conditions are satisfied: (1) the structure supports loads primarily through nominally vertical columns, walls, or similar frames; (2) the ratio of maximum second-order drift to maximum first-order drift (both determined for LRFD load combinations or 1.6 times ASD load combinations, with stiffnesses adjusted as specified in Section C2.3) in all stories is equal to or less than 1.7; and (3) no more than one-third of the total gravity load on the structure is supported by columns that are part of moment-resisting frames in the direction of translation being considered. It is necessary in all cases to consider $P$-δ effects in the evaluation of individual members subjected to compression and flexure.

**User Note:** A $P$-Δ-only second-order analysis (one that neglects the effects of $P$-δ on the response of the structure) is permitted under the conditions listed. In this case, the requirement for considering $P$-δ effects in the evaluation of individual members can be satisfied by applying the $B_1$ multiplier defined in Appendix 8, Section 8.1.2, to the required flexural strength of the member.

Use of the approximate method of second-order analysis provided in Appendix 8, Section 8.1, is permitted.

(c) The analysis shall consider all gravity and other applied loads that may influence the stability of the structure.

---

## CALCULATION OF REQUIRED STRENGTHS [Sect. C2.

**User Note:** It is important to include in the analysis all gravity loads, including loads on leaning columns and other elements that are not part of the lateral force-resisting system.

(d) For design by LRFD, the second-order analysis shall be carried out under LRFD load combinations. For design by ASD, the second-order analysis shall be carried out under 1.6 times the ASD load combinations, and the results shall be divided by 1.6 to obtain the required strengths of components.

### 2. Consideration of Initial System Imperfections

The effect of initial imperfections in the position of points of intersection of members at the stability of the structure shall be taken into account either by direct modeling of these imperfections in the analysis as specified in Section C2.2a or by the application of notional loads as specified in Section C2.2b.

**User Note:** The imperfections required to be considered in this section are imperfections in the locations of points of intersection of members (system imperfections). In typical building structures, the important imperfection of this type is the out-of-plumbness of columns. Consideration of initial out-of-straightness of individual members (member imperfections) is not required in the structural analysis when using the provisions of this section; it is accounted for in the compression member design provisions of Chapter E and need not be considered explicitly in the analysis as long as it is within the limits specified in the *Code of Standard Practice*. Appendix 1, Section 1.2, provides an extension to the direct analysis method that includes modeling of member imperfections (initial out-of-straightness) within the structural analysis.

### 2a. Direct Modeling of Imperfections

In all cases, it is permissible to account for the effect of initial system imperfections by including the imperfections directly in the analysis. The structure shall be analyzed with points of intersection of members displaced from their nominal locations. The magnitude of the initial displacements shall be the maximum permitted by the design in the design; the pattern of initial displacements shall be such that it provides the greatest destabilizing effect.

**User Note:** Initial displacements similar in configuration to both displacements due to loading and anticipated buckling modes should be considered for modeling of imperfections. The magnitude of the initial displacements should be based on permissible construction tolerances, as specified in the *Code of Standard Practice* or other governing requirements, or on actual imperfections if known.

In the analysis of structures that support gravity loads primarily through nominally vertical columns, walls, or frames, where the ratio of maximum second-order story drift to maximum first-order story drift (both determined for LRFD load combinations or 1.6 times ASD load combinations, with stiffnesses adjusted as specified in Section C2.3) in all stories is equal to or less than 1.7, it is permissible to include

---

## CALCULATION OF REQUIRED STRENGTHS [Sect. C2.]

initial system imperfections in the analysis for gravity-only load combinations and not in the analysis for load combinations that include applied lateral loads.

### 2b. Use of Notional Loads to Represent Imperfections

For structures that support gravity loads primarily through nominally vertical columns, walls, or frames, it is permissible to use notional loads to represent the effects of initial system imperfections in the position of points of intersection of members in accordance with the requirements of this section. The notional load shall be applied to a model of the structure based on its nominal geometry.

**User Note:** In general, the notional load concept is applicable to all types of structures and to imperfections in the positions of both points of intersection of members and points along members, but the specific requirements in Sections C2.2b(a) through C2.2b(d) are applicable only for the particular class of structure and type of system imperfection identified here.

(a) Notional loads shall be applied as lateral loads at all levels. The notional loads shall be additive to other lateral loads and shall be applied in all load combinations, except as indicated in Section C2.2b(d). The magnitude of the notional loads shall be

$$N_i = 0.002\alpha Y_i$$ (C2-1)

where

$\alpha = 1.0$ (LRFD); $\alpha = 1.6$ (ASD)
$N_i$ = notional load applied at level $i$, kips (N)
$Y_i$ = gravity load applied at level $i$ from the LRFD load combination or ASD load combination, as applicable, kips (N)

**User Note:** The use of notional loads can lead to additional (generally small) fictitious base shears in the structure. The correct horizontal reactions at the foundation may be obtained by applying an additional horizontal force at the base of the structure, equal and opposite in direction to the sum of all notional loads, distributed among vertical load-carrying elements in the same proportion as the gravity load supported by those elements. The notional loads can also lead to additional overturning effects, which are not fictitious.

(b) The notional load at any level, $N_i$, shall be distributed over that level in the same manner as the gravity load at the level. The notional loads shall be applied in the direction that provides the greatest destabilizing effect.

**User Note:** For most building structures, the requirement regarding notional load direction may be satisfied as follows: for load combinations that do not include lateral loading, consider two alternative orthogonal directions of notional load application, in a positive and a negative sense in each of the two directions, in the same direction at all levels; for load combinations that include lateral loading, apply all notional loads in the direction of the resultant of all lateral loads in the combination.

---

## CALCULATION OF REQUIRED STRENGTHS [Sect. C2.

(c) The notional load coefficient of 0.002 in Equation C2-1 is based on a nominal initial story out-of-plumbness ratio of 1/500; where the use of a different maximum out-of-plumbness is justified, it is permissible to adjust the notional load coefficient proportionally.

**User Note:** An out-of-plumbness of 1/500 represents the maximum tolerance on column plumbness specified in the *Code of Standard Practice*. In some cases, other specified tolerances, such as those on the plan location of columns, will govern and will require a tighter plumbness tolerance.

(d) For structures in which the ratio of maximum second-order drift to maximum first-order drift (both determined for LRFD load combinations or 1.6 times ASD load combinations, with stiffnesses adjusted as specified in Section C2.3) in all stories is equal to or less than 1.7, it is permissible to apply the notional load, $N_i$, only in gravity-only load combinations and not in combinations that include other lateral loads.

### 3. Adjustments to Stiffness

The analysis of the structure to determine the required strengths of components shall use reduced stiffnesses, as follows:

(a) A factor of 0.80 shall be applied to all stiffnesses that are considered to contribute to the stability of the structure. It is permissible to apply this reduction factor to all stiffnesses in the structure.

**User Note:** Applying the stiffness reduction to some members and not others can, in some cases, result in artificial distortion of the structure under load and possible unintended redistribution of forces. This can be avoided by applying the reduction to all members, including those that do not contribute to the stability of the structure.

(b) An additional factor, the stiffness reduction parameter, $\tau_b$, shall be applied to the flexural stiffnesses of all members whose flexural stiffnesses are considered to contribute to the stability of the structure. For noncomposite members, $\tau_b$ shall be defined as follows (see Section I1.5 for the definition of $\tau_b$ for composite members):

(1) When $\alpha P_r / P_{ns} \leq 0.5$

$$\tau_b = 1.0$$ (C2-2a)

(2) When $\alpha P_r / P_{ns} > 0.5$

$$\tau_b = 4(\alpha P_r / P_{ns})[1 - (\alpha P_r / P_{ns})]$$ (C2-2b)

where

$\alpha = 1.0$ (LRFD); $\alpha = 1.6$ (ASD)
$P_r$ = required axial compressive strength using LRFD or ASD load combinations, kips (N)

---

## CALCULATION OF AVAILABLE STRENGTHS [Sect. C3.]

$P_{ns}$ = cross-section compressive strength; for nonslender-element sections, $P_{ns} = F_y A_g$, and for slender-element sections, $P_{ns} = F_y A_e$, where $A_e$ is as defined in Section E7 with $F_n = F_y$, kips (N)

**User Note:** Taken together, Sections (a) and (b) require the use of 0.8$\tau_b$ times the nominal elastic flexural stiffness and 0.8 times other nominal elastic stiffnesses for structural steel members in the analysis.

(c) In structures to which Section C2.2b is applicable, in lieu of using $\tau_b < 1.0$, where $\alpha P_r / P_{ns} > 0.5$, it is permissible to use $\tau_b = 1.0$ for all noncomposite members if a notional load equal to $0.001\alpha Y_i$ [where $Y_i$ is as defined in Section C2.2b(a)] is applied at all levels, in the direction specified in Section C2.2b(b), in all load combinations. These notional loads shall be added to those required to account for the effects of initial imperfections in the position of points of intersection of members and shall not be subject to the provisions of Section C2.2b(d).

(d) Where components composed of materials other than structural steel are considered to contribute to the stability of the structure, and the governing codes and specifications for the other materials require greater reductions in stiffness, such greater stiffness reductions shall be applied to those components.

## C3. CALCULATION OF AVAILABLE STRENGTHS

For the direct analysis method of design, the available strengths of members and connections shall be calculated in accordance with the provisions of Chapters D through K, as applicable, with no further consideration of overall structure stability. The effective length for flexural buckling of all members shall be taken as the unbraced length unless a smaller value is justified by rational analysis.

Bracing intended to define the unbraced lengths of members shall have sufficient stiffness and strength to control member movement at the braced points.

**User Note:** Methods of satisfying this bracing requirement are provided in Appendix 6. The requirements of Appendix 6 are not applicable to bracing that is included in the design of the lateral force-resisting system of the overall structure.

---
