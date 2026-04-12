# Chapter C: Stability

**AISC Specification v16.0 - Design Examples**
**Original PDF Pages**: 19-36 (18 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Design for Stability

**Examples Included**: ['C.1A: Direct Analysis Method', 'C.1B: Effective Length Method', 'C.2: First-Order Method']

---

# Chapter C
# Design for Stability

---

## C1. GENERAL STABILITY REQUIREMENTS

The AISC *Specification* requires that the designer account for both the stability of the structural system as a whole and the stability of individual elements. Thus, the lateral analysis used to assess stability must include consideration of the combined effect of gravity and lateral loads, as well as member inelasticity, out-of-plumbness, out-of-straightness, and the resulting second-order effects (including *P*-Δ and *P*-δ effects). The effects of "leaning columns" must also be considered, as illustrated in the examples in this chapter and in the four-story building design example in Part III of this document.

*P*-Δ and *P*-δ effects are illustrated in AISC *Specification* Commentary Figure C-C2.1. Methods for addressing stability, including *P*-Δ and *P*-δ effects, are provided in AISC *Specification* Section C2 and Appendix 7.

---

## C2. CALCULATION OF REQUIRED STRENGTHS

The calculation of required strengths is illustrated in the examples in this chapter and in the four-story building design example in Part III of these *Design Examples*.

---

## C3. CALCULATION OF AVAILABLE STRENGTHS

The calculation of available strengths is illustrated in the four-story building design example in Part III of these *Design Examples*.

---


---

# EXAMPLE C.1A DESIGN OF A MOMENT FRAME BY THE DIRECT ANALYSIS METHOD

---

## Given:

Determine the required strengths and effective length factors for the columns in the moment frame shown in Figure C.1A-1 for the maximum gravity load combination, using LRFD and ASD. The uniform load, *w*<sub>D</sub>, includes beam self-weight and an allowance for column self-weight. Use the direct analysis method. All members are ASTM A992/A992M material.

Columns are unbraced between the footings and roof in the *x*-*x* and *y*-*y* axes and have pinned bases.

```
wD = 0.400 kip/ft
wL = 1.20 kip/ft
```

![Moment Frame Elevation Diagram](diagram)

**Structural Layout:**
- 5 columns labeled A, B, C, D, E
- Column spacing: 30'-0" (four bays)
- Height: 20'-0"
- Interior columns: W12×65
- Beam: W18×40

*Fig. C.1A-1. Example C.1A moment frame elevation.*

---

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

**ASTM A992/A992M**
*F*<sub>y</sub> = 50 ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

**W12×65**
*A*<sub>g</sub> = 19.1 in.²

The beams from grid lines A to B and C to E and the columns at A, D, and E are pinned at both ends and do not contribute to the lateral stability of the frame. There are no *P*-Δ effects to consider in these members and they may be designed using *L*<sub>c</sub> = *L*.

The moment frame between grid lines B and C is the source of lateral stability and therefore will be evaluated using the provisions of Chapter C of the AISC *Specification*. Although the columns at grid lines A, D, and E do not contribute to lateral stability, the forces required to stabilize them must be considered in the moment-frame analysis. The entire frame from grid line A to E could be modeled, but in this case the model is simplified as shown in Figure C.1A-2, in which the stability loads from the three "leaning" columns are combined into a single representative column.

From Chapter 2 of ASCE/SEI 7, the maximum gravity load combinations are:

---


---

---

## Load Combinations

| LRFD | ASD |
|------|-----|
| *w*<sub>u</sub> = 1.2*D* + 1.6*L* | *w*<sub>a</sub> = *D* + *L* |
| = 1.2(0.400 kip/ft) + 1.6(1.20 kip/ft) | = 0.400 kip/ft + 1.20 kip/ft |
| = 2.40 kip/ft | = 1.60 kip/ft |

Per AISC *Specification* Section C2.1(d), for LRFD, perform a second-order analysis and member strength checks using the LRFD load combinations. For ASD, perform a second-order analysis using 1.6 times the ASD load combinations and divide the analysis results by 1.6 for the ASD member strength checks.

---

### *Frame analysis gravity loads*

The uniform gravity loads to be considered in a second-order analysis on the beam from B to C are:

| LRFD | ASD |
|------|-----|
| *w'*<sub>u</sub> = 2.40 kip/ft | *w'*<sub>a</sub> = 1.6(1.60 kip/ft) |
| | = 2.56 kip/ft |

Concentrated gravity loads to be considered in a second-order analysis on the columns at B and C contributed by adjacent beams are:

| LRFD | ASD |
|------|-----|
| *P'*<sub>u</sub> = *w'*<sub>u</sub>*l* / 2 | *P'*<sub>a</sub> = *w'*<sub>a</sub>*l* / 2 |
| = (2.40 kip/ft)(30.0 ft) / 2 | = (2.56 kip/ft)(30.0 ft) / 2 |
| = 36.0 kips | = 38.4 kips |

---

### *Concentrated gravity loads on the representative "leaning" column*

The load in this column accounts for all gravity loading that is stabilized by the moment frame, but is not directly applied to it.

| LRFD | ASD |
|------|-----|
| *P'*<sub>UL</sub> = (60.0 ft)(2.40 kip/ft) | *P'*<sub>aL</sub> = (60.0 ft)(2.56 kip/ft) |
| = 144 kips | = 154 kips |

---

### *Frame analysis notional loads*

Per AISC *Specification* Section C2.2, frame out-of-plumbness must be accounted for either by explicit modeling of the design out-of-plumbness or by the application of notional loads. Notional loads will be used in this example.

From AISC *Specification* Equation C2-1, the notional loads are:

---


---

---

## Notional Load Calculations

| LRFD | ASD |
|------|-----|
| α = 1.0 | α = 1.6 |
| *Y*<sub>i</sub> = (120 ft)(2.40 kip/ft) | *Y*<sub>i</sub> = (120 ft)(1.60 kip/ft) |
| = 288 kips | = 192 kips |
| *N*<sub>i</sub> = 0.002α*Y*<sub>i</sub>     (*Spec.* Eq. C2-1) | *N*<sub>i</sub> = 0.002α*Y*<sub>i</sub>     (*Spec.* Eq. C2-1) |
| = 0.002(1.0)(288 kips) | = 0.002(1.6)(192 kips) |
| = 0.576 kip | = 0.614 kip |

---

## *Summary of applied frame loads*

The applied loads are shown in Figure C.1A-2.

![Applied Loads Diagram](diagram)

| LRFD | ASD |
|------|-----|
| ![LRFD Load Diagram showing: 36.0 kips at both sides, 144 kips at leaning column, 2.40 kip/ft distributed load, 0.576 kip lateral load] | ![ASD Load Diagram showing: 38.4 kips at both sides, 154 kips at leaning column, 2.56 kip/ft distributed load, 0.614 kip lateral load] |

*Fig. C.1A-2. Applied loads on the analysis model.*

---

## Stiffness Reduction and Analysis

Per AISC *Specification* Section C2.3, conduct the analysis using 80% of the nominal stiffnesses to account for the effects of residual stresses. Assume, subject to verification, that α*P*<sub>r</sub> / *P*<sub>ns</sub> is not greater than 0.5; therefore, no additional stiffness reduction is required (τ<sub>b</sub> = 1.0).

Half of the gravity load is carried by the columns of the moment-resisting frame. Because the gravity load supported by the moment-resisting frame columns exceeds one-third of the total gravity load tributary to the frame, per AISC *Specification* Section C2.1(b), the effects of *P*-δ and *P*-Δ must be considered in the frame analysis. This example uses analysis software that accounts for both *P*-Δ and *P*-δ effects. (If the software used does not account for *P*-δ effects, this may be accomplished by subdividing the columns between the footing and beam.)

Figures C.1A-3 and C.1A-4 show results from a first-order and a second-order analysis, respectively. (The first-order analysis is shown for reference only.) In each case, the drift is the average of drifts at grid lines B and C.

---


---

---

## *First-order results*

| LRFD | ASD<br>(Reactions and moments divided by 1.6) |
|------|------|
| Δ<sub>1st</sub> = 0.181 in. | Δ<sub>1st</sub> = 0.193 in. (prior to dividing by 1.6) |
| ![Diagram showing moments 113 kip-ft and 124 kip-ft at top, reactions 5.64 kips and 6.21 kips at top, axial forces 71.6 kips and 72.4 kips at bottom] | ![Diagram showing moments 75.2 kip-ft and 82.8 kip-ft at top, reactions 3.76 kips and 4.14 kips at top, axial forces 47.7 kips and 48.3 kips at bottom] |

*Fig. C.1A-3. Results of first-order analysis.*

---

## *Second-order results*

| LRFD | ASD<br>(Reactions and moments divided by 1.6) |
|------|------|
| Δ<sub>2nd</sub> = 0.290 in. | Δ<sub>2nd</sub> = 0.321 in. (prior to dividing by 1.6) |
| Drift ratio: | Drift ratio: |
| Δ<sub>2nd</sub> / Δ<sub>1st</sub> = 0.290 in. / 0.181 in.<br>= 1.60 | Δ<sub>2nd</sub> / Δ<sub>1st</sub> = 0.321 in. / 0.193 in.<br>= 1.66 |
| ![Diagram showing moments 109 kip-ft and 127 kip-ft at top, reactions 5.52 kips and 6.26 kips at top, axial forces 71.4 kips and 72.6 kips at bottom] | ![Diagram showing moments 72.2 kip-ft and 84.8 kip-ft at top, reactions 3.68 kips and 4.18 kips at top, axial forces 47.6 kips and 48.4 kips at bottom] |

*Fig. C.1A-4. Results of second-order analysis.*

---

## Verification Calculations

Check the assumption that α*P*<sub>r</sub> / *P*<sub>ns</sub> ≤ 0.5 on the column on grid line C.

Because a W12×65 column contains no elements that are slender for uniform compression,

*P*<sub>ns</sub> = *F*<sub>y</sub> *A*<sub>g</sub>

= (50 ksi)(19.1 in.²)

= 955 kips

---


---

---

## Verification of Stiffness Assumption

| LRFD | ASD |
|------|-----|
| α*P*<sub>r</sub> / *P*<sub>ns</sub> = 1.0(72.6 kips) / 955 kips | α*P*<sub>r</sub> / *P*<sub>ns</sub> = 1.6(48.4 kips) / 955 kips |
| = 0.0760 ≤ 0.5   **o.k.** | = 0.0811 ≤ 0.5   **o.k.** |

The stiffness assumption used in the analysis, τ<sub>b</sub> = 1.0, is verified.

Note that the drift ratio, 1.60 (LRFD) or 1.66 (ASD), does not exceed the recommended limit of 2.5 from AISC *Specification* Commentary Section C1.

---

## Discussion

The required axial compressive strength in the columns is 72.6 kips (LRFD) or 48.4 kips (ASD). The required bending moment diagram is linear, varying from zero at the bottom to 127 kip-ft (LRFD) or 84.8 kip-ft (ASD) at the top. These required strengths apply to both columns because the notional load must be applied in each direction.

Although the second-order sway multiplier (drift ratio) is fairly large at 1.60 (LRFD) or 1.66 (ASD), the change in bending moment is small because the only sway moments are those produced by the small notional loads. For load combinations with significant gravity and lateral loadings, the increase in bending moments is larger.

Per AISC *Specification* Section C3, the effective length for flexural buckling of all members is taken as the unbraced length (*K* = 1.0):

*L*<sub>cx</sub> = 20.0 ft

*L*<sub>cy</sub> = 20.0 ft

---


---

# EXAMPLE C.1B DESIGN OF A MOMENT FRAME BY THE EFFECTIVE LENGTH METHOD

---

## Given:

Repeat Example C.1A using the effective length method.

Determine the required strengths and effective length factors for the columns in the moment frame shown in Figure C.1B-1 for the maximum gravity load combination, using LRFD and ASD. Use the effective length method.

Columns are unbraced between the footings and roof in the *x*-*x* and *y*-*y* axes and have pinned bases.

```
wD = 0.400 kip/ft
wL = 1.20 kip/ft
```

![Moment Frame Elevation Diagram](diagram)

**Structural Layout:**
- 5 columns labeled A, B, C, D, E
- Column spacing: 30'-0" (four bays)
- Height: 20'-0"
- Interior columns: W12×65
- Beam: W18×40

*Fig. C.1B-1. Example C.1B moment frame elevation.*

---

## Solution:

From AISC *Manual* Table 1-1, the geometric properties are as follows:

**W12×65**
*I*<sub>x</sub> = 533 in.⁴

The beams from grid lines A to B and C to E and the columns at A, D, and E are pinned at both ends and do not contribute to the lateral stability of the frame. There are no *P*-Δ effects to consider in these members and they may be designed using *L*<sub>c</sub> = *L*.

The moment frame between grid lines B and C is the source of lateral stability and therefore will be evaluated using the provisions of Chapter C of the AISC *Specification*. Although the columns at grid lines A, D, and E do not contribute to lateral stability, the forces required to stabilize them must be considered in the moment-frame analysis. The entire frame from grid line A to E could be modeled, but in this case the model is simplified as shown in Figure C.1B-2, in which the stability loads from the three "leaning" columns are combined into a single representative column.

---

## Effective Length Method Requirements

Check the limitations for the use of the effective length method given in AISC *Specification* Appendix 7, Section 7.2.1:

(a) The structure supports gravity loads primarily through nominally vertical columns, walls, or frames.

(b) The ratio of maximum second-order drift to the maximum first-order drift (both determined for LRFD load combinations or 1.6 times ASD load combinations, with stiffness not adjusted as specified in AISC *Specification* Section C2.3) in all stories will be assumed to be no greater than 1.5, subject to verification in the following.

---


---

---

## Load Combinations (continued)

From Chapter 2 of ASCE/SEI 7, the maximum gravity load combinations are:

| LRFD | ASD |
|------|-----|
| *w*<sub>u</sub> = 1.2*D* + 1.6*L* | *w*<sub>a</sub> = *D* + *L* |
| = 1.2(0.400 kip/ft) + 1.6(1.20 kip/ft) | = 0.400 kip/ft + 1.20 kip/ft |
| = 2.40 kip/ft | = 1.60 kip/ft |

Per AISC *Specification* Appendix 7, Section 7.2.2, the analysis must conform to the requirements of AISC *Specification* Section C2.1, with the exception of the stiffness reduction required by the provisions of Section C2.1(a).

Per AISC *Specification* Section C2.1(d), for LRFD perform a second-order analysis and member strength checks using the LRFD load combinations. For ASD, perform a second-order analysis at 1.6 times the ASD load combinations and divide the analysis results by 1.6 for the ASD member strength checks.

---

### *Frame analysis gravity loads*

The uniform gravity loads to be considered in a second-order analysis on the beam from B to C are:

| LRFD | ASD |
|------|-----|
| *w'*<sub>u</sub> = 2.40 kip/ft | *w'*<sub>a</sub> = 1.6(1.60 kip/ft) |
| | = 2.56 kip/ft |

Concentrated gravity loads to be considered in a second-order analysis on the columns at B and C contributed by adjacent beams are:

| LRFD | ASD |
|------|-----|
| *P'*<sub>u</sub> = *w'*<sub>u</sub>*l* / 2 | *P'*<sub>a</sub> = *w'*<sub>a</sub>*l* / 2 |
| = (2.40 kip/ft)(30.0 ft) / 2 | = (2.56 kip/ft)(30.0 ft) / 2 |
| = 36.0 kips | = 38.4 kips |

---

### *Concentrated gravity loads on the representative "leaning" column*

The load in this column accounts for all gravity loading that is stabilized by the moment frame, but not directly applied to it.

| LRFD | ASD |
|------|-----|
| *P'*<sub>uL</sub> = (60.0 ft)(2.40 kip/ft) | *P'*<sub>aL</sub> = (60.0 ft)(2.56 kip/ft) |
| = 144 kips | = 154 kips |

---

### *Frame analysis notional loads*

Per AISC *Specification* Appendix 7, Section 7.2.2, frame out-of-plumbness must be accounted for by the application of notional loads in accordance with AISC *Specification* Section C2.2h. Note that notional loads need to only be applied to the gravity load combinations per AISC *Specification* Section C2.2h(d) when the requirement that Δ<sub>2nd</sub> / Δ<sub>1st</sub> ≤ 1.7 (using stiffness adjusted as specified in Section C2.3) is satisfied. Per the User Note in AISC *Specification* Appendix 7, Section 7.2.2, Section C2.2h(d) will be satisfied in all cases where the effective length method is applicable, and therefore the notional load need only be applied in gravity-only load cases.

---


---

---

## Notional Loads Calculation

From AISC *Specification* Equation C2-1, the notional loads are:

| LRFD | ASD |
|------|-----|
| α = 1.0 | α = 1.6 |
| *Y*<sub>i</sub> = (120 ft)(2.40 kip/ft) | *Y*<sub>i</sub> = (120 ft)(1.60 kip/ft) |
| = 288 kips | = 192 kips |
| *N*<sub>i</sub> = 0.002α*Y*<sub>i</sub>     (*Spec.* Eq. C2-1) | *N*<sub>i</sub> = 0.002α*Y*<sub>i</sub>     (*Spec.* Eq. C2-1) |
| = 0.002(1.0)(288 kips) | = 0.002(1.6)(192 kips) |
| = 0.576 kip | = 0.614 kip |

---

## *Summary of applied frame loads*

The applied loads are shown in Figure C.1B-2.

![Applied Loads Diagram](diagram)

| LRFD | ASD |
|------|-----|
| ![LRFD Load Diagram showing: 36.0 kips at both sides, 144 kips at leaning column, 2.40 kip/ft distributed load, 0.576 kip lateral load] | ![ASD Load Diagram showing: 38.4 kips at both sides, 154 kips at leaning column, 2.56 kip/ft distributed load, 0.614 kip lateral load] |

*Fig. C.1B-2. Applied loads on the analysis model.*

---

## Analysis

Per AISC *Specification* Appendix 7, Section 7.2.2, conduct the analysis using the full nominal stiffnesses.

Half of the gravity load is carried by the columns of the moment-resisting frame. Because the gravity load supported by the moment-resisting frame columns exceeds one-third of the total gravity load tributary to the frame, per AISC *Specification* Section C2.1(b), the effects of *P*-δ on the response of the structure must be considered in the frame analysis. This example uses analysis software that accounts for both *P*-Δ and *P*-δ effects. (If the software used does not account for *P*-δ effects, this may be accomplished by subdividing columns between the footing and beam.)

Figures C.1B-3 and C.1B-4 show results from a first-order and second-order analysis, respectively. In each case, the drift is the average of drifts at grid lines B and C.

---


---

---

## *First-order results*

| LRFD | ASD<br>(Reactions and moments divided by 1.6) |
|------|------|
| Δ<sub>1st</sub> = 0.145 in. | Δ<sub>1st</sub> = 0.155 in. (prior to dividing by 1.6) |
| ![Diagram showing moments 113 kip-ft and 124 kip-ft at top, reactions 5.64 kips and 6.21 kips at top, axial forces 71.6 kips and 72.4 kips at bottom] | ![Diagram showing moments 75.2 kip-ft and 82.8 kip-ft at top, reactions 3.76 kips and 4.14 kips at top, axial forces 47.7 kips and 48.3 kips at bottom] |

*Fig. C.1B-3. Results of first-order analysis.*

---

## *Second-order results*

| LRFD | ASD<br>(Reactions and moments divided by 1.6) |
|------|------|
| Δ<sub>2nd</sub> = 0.204 in. | Δ<sub>2nd</sub> = 0.223 in. (prior to dividing by 1.6) |
| Drift ratio: | Drift ratio: |
| Δ<sub>2nd</sub> / Δ<sub>1st</sub> = 0.204 in. / 0.145 in.<br>= 1.41 | Δ<sub>2nd</sub> / Δ<sub>1st</sub> = 0.223 in. / 0.155 in.<br>= 1.44 |
| ![Diagram showing moments 110 kip-ft and 126 kip-ft at top, reactions 5.56 kips and 6.24 kips at top, axial forces 71.5 kips and 72.5 kips at bottom] | ![Diagram showing moments 73.1 kip-ft and 84.1 kip-ft at top, reactions 3.70 kips and 4.16 kips at top, axial forces 47.6 kips and 48.4 kips at bottom] |

*Fig. C.1B-4. Results of second-order analysis.*

---

## Verification

The assumption that the ratio of the maximum second-order drift to the maximum first-order drift is no greater than 1.5 is verified; therefore, the effective length method may be permitted.

Although the second-order sway multiplier is fairly large at approximately 1.41 (LRFD) or 1.44 (ASD), the change in bending moment is small because the only sway moments for this load combination are those produced by the small notional loads. For load combinations with significant gravity and lateral loadings, the increase in bending moments is larger.

Calculate the in-plane effective length factor, *K*<sub>x</sub>, using the "story stiffness approach" and Equation C-A-7-5 presented in AISC *Specification* Commentary Appendix 7, Section 7.2. With *K*<sub>x</sub> = *K*<sub>2</sub>:

---


---

---

## Effective Length Factor Calculation

$$K_x = \sqrt{\frac{P_{story}}{R_M P_r} \left(\frac{\pi^2 EI}{L^2}\right) \left(\frac{\Delta_H}{HL}\right)} \geq \sqrt{\frac{\pi^2 EI}{L^2} \left(\frac{\Delta_H}{1.7 H_{col} L}\right)}$$
(*Spec.* Eq. C-A-7-5)

---

Calculate the total load in all columns, *P*<sub>story</sub>, as follows:

| LRFD | ASD |
|------|-----|
| *P*<sub>story</sub> = (2.40 kip/ft)(120 ft) | *P*<sub>story</sub> = (1.60 kip/ft)(120 ft) |
| = 288 kips | = 192 kips |

---

Calculate the coefficient to account for the influence of *P*-δ on *P*-Δ, *R*<sub>M</sub>, as follows, using AISC *Specification* Commentary Appendix 7, Equation C-A-7-6:

| LRFD | ASD |
|------|-----|
| *P*<sub>mf</sub> = 71.5 kips + 72.5 kips | *P*<sub>mf</sub> = 47.6 kips + 48.4 kips |
| = 144 kips | = 96.0 kips |
| *R*<sub>M</sub> = 1 − 0.15(*P*<sub>mf</sub> / *P*<sub>story</sub>)     (*Spec.* Eq. C-A-7-6) | *R*<sub>M</sub> = 1 − 0.15(*P*<sub>mf</sub> / *P*<sub>story</sub>)     (*Spec.* Eq. C-A-7-6) |
| = 1 − 0.15(144 kips / 288 kips) | = 1 − 0.15(96.0 kips / 192 kips) |
| = 0.925 | = 0.925 |

---

Calculate the Euler buckling strength of one moment frame.

$$\frac{\pi^2 EI_x}{L^2} = \frac{\pi^2 (29,000 \text{ ksi})(533 \text{ in.}^4)}{[(20.0 \text{ ft})(12 \text{ in./ft})]^2}$$

= 2,650 kips

---

From AISC *Specification* Commentary Equation C-A-7-5, for the column at line C:

---


---

---

## Effective Length Factor Calculation (continued)

| LRFD | ASD |
|------|-----|
| $$K_x = \sqrt{\frac{P_{story}}{R_M P_r} \left(\frac{\pi^2 EI}{L^2}\right) \left(\frac{\Delta_H}{HL}\right)}$$ | $$K_x = \sqrt{\frac{1.6 P_{story}}{R_M (1.6) P_r} \left(\frac{\pi^2 EI}{L^2}\right) \left(\frac{\Delta_H}{HL}\right)}$$ |
| $$\geq \sqrt{\frac{\pi^2 EI}{L^2} \left(\frac{\Delta_H}{1.7 H_{col} L}\right)}$$ | $$\geq \sqrt{\frac{\pi^2 EI}{L^2} \left(\frac{\Delta_H}{1.7(1.6) H_{col} L}\right)}$$ |
| $$= \sqrt{\frac{288 \text{ kips}}{(0.925)(72.5 \text{ kips})} (2,650 \text{ kips})}$$ | $$= \sqrt{\frac{1.6(192 \text{ kips})}{0.925(1.6)(48.4 \text{ kips})} (2,650 \text{ kips})}$$ |
| $$\times \frac{0.145 \text{ in.}}{(0.576 \text{ kip})(20.0 \text{ ft})(12 \text{ in./ft})}$$ | $$\times \frac{0.155 \text{ in.}}{(0.614 \text{ kip})(20.0 \text{ ft})(12 \text{ in./ft})}$$ |
| $$> \sqrt{(2,650 \text{ kips})}$$ | $$> \sqrt{(2,650 \text{ kips})}$$ |
| $$\times \frac{0.145 \text{ in.}}{1.7(6.21 \text{ kips})(20.0 \text{ ft})(12 \text{ in./ft})}$$ | $$\times \frac{0.155 \text{ in.}}{1.7(1.6)(4.14 \text{ kips})(20.0 \text{ ft})(12 \text{ in./ft})}$$ |
| = 3.45 > 0.389 | = 3.46 > 0.390 |
| Use *K*<sub>x</sub> = 3.45 | Use *K*<sub>x</sub> = 3.46 |

---

Note that the column loads are multiplied by 1.6 for ASD in Equation C-A-7-5. In the calculations above, the *H*<sub>col</sub> values used include the shear in the column from both the gravity and lateral loads. To obtain more precise results, the designer may follow the commentary to AISC *Specification* Appendix 7, Section 7.2, which states that the *H*<sub>col</sub> term is the shear produced by the lateral forces used to compute Δ*H*.

With *K*<sub>x</sub> = 3.46 and *K*<sub>y</sub> = 1.00, the column available strengths can be verified for the given member sizes for the second-order forces (calculations not shown), using the following effective lengths:

*L*<sub>cx</sub> = *K*<sub>x</sub> *L*<sub>x</sub>
= 3.46(20.0 ft)
= 69.2 ft

*L*<sub>cy</sub> = *K*<sub>y</sub> *L*<sub>y</sub>
= 1.00(20.0 ft)
= 20.0 ft

---


---

# EXAMPLE C.1C DESIGN OF A MOMENT FRAME BY THE FIRST-ORDER METHOD

---

## Given:

Repeat Example C.1A using the first-order analysis method.

Determine the required strengths and effective length factors for the columns in the moment frame shown in Figure C.1C-1 for the maximum gravity load combination, using LRFD and ASD. Use the first-order analysis method as given in AISC *Specification* Appendix 7, Section 7.3.

Columns are unbraced between the footings and roof in the *x*- and *y*-axes and have pinned bases.

```
wD = 0.400 kip/ft
wL = 1.20 kip/ft
```

![Moment Frame Elevation Diagram](diagram)

**Structural Layout:**
- 5 columns labeled A, B, C, D, E
- Column spacing: 30'-0" (four bays)
- Height: 20'-0"
- Interior columns: W12×65
- Beam: W18×40

*Fig. C.1C-1. Example C.1C moment frame elevation.*

---

## Solution:

From AISC *Manual* Table 2-4, the material properties are as follows:

**ASTM A992/A992M**
*F*<sub>y</sub> = 50 ksi

From AISC *Manual* Table 1-1, the geometric properties are as follows:

**W12×65**
*A*<sub>g</sub> = 19.1 in.²

**W18×40**
*I*<sub>x</sub> = 612 in.⁴

The beams from grid lines A to B and C to E and the columns at A, D, and E are pinned at both ends and do not contribute to the lateral stability of the frame. There are no *P*-Δ effects to consider in these members and they may be designed using *L*<sub>c</sub>=*L*.

The moment frame between grid lines B and C is the source of lateral stability and will be designed using the provisions of AISC *Specification* Appendix 7, Section 7.3. Although the columns at grid lines A, D, and E do not contribute to lateral stability, the forces required to stabilize them must be considered in the moment-frame analysis. These members need not be included in the analysis model, except that the forces in the "leaning" columns must be included in the calculation of notional loads.

Check the limitations for the use of the first-order analysis method given in AISC *Specification* Appendix 7, Section 7.3.1:

---


---

---

## First-Order Method Requirements

(a) The structure supports gravity loads primarily through nominally vertical columns, walls, or frames.

(b) The required axial compressive strength of nominally vertical members in moment frames subject to bending is subject to the limitation given in AISC *Specification* Equation A-7-1.

(c) The ratio of maximum second-order drift to the maximum first-order drift (both determined for LRFD load combinations or 1.6 times ASD load combinations, with stiffnesses not adjusted as specified in AISC *Specification* Section C2.3) in all stories will be assumed to be no greater than 1.5, subject to verification.

(d) The required axial compressive strength of all members whose flexural stiffnesses are considered to contribute to the lateral stability of the structure will be assumed to be no more than 50% of the cross-section strength, subject to verification.

Per AISC *Specification* Appendix 7, Section 7.3.2, the required strengths are determined from a first-order analysis using notional loads determined in the following, along with a *B*<sub>1</sub> multiplier to account for second-order effects, as determined from Appendix 8.

---

## *Loads*

From Chapter 2 of ASCE/SEI 7, the maximum gravity load combinations are:

| LRFD | ASD |
|------|-----|
| *w*<sub>u</sub> = 1.2*D* + 1.6*L* | *w*<sub>a</sub> = *D* + *L* |
| = 1.2(0.400 kip/ft) + 1.6(1.20 kip/ft) | = 0.400 kip/ft + 1.20 kip/ft |
| = 2.40 kip/ft | = 1.60 kip/ft |

Concentrated gravity loads to be considered on the columns at B and C contributed by adjacent beams are:

| LRFD | ASD |
|------|-----|
| *P*<sub>u</sub> = *w*<sub>u</sub>*l* / 2 | *P*<sub>a</sub> = *w*<sub>a</sub>*l* / 2 |
| = (2.40 kip/ft)(30.0 ft) / 2 | = (1.60 kip/ft)(30.0 ft) / 2 |
| = 36.0 kips | = 24.0 kips |

Using AISC *Specification* Appendix 7, Section 7.3.2(a), frame out-of-plumbness is accounted for by the application of an additional lateral load.

From AISC *Specification* Appendix Equation A-7-3, the additional lateral load is determined as follows:

| LRFD | ASD |
|------|-----|
| α = 1.0 | α = 1.6 |
| *Y*<sub>i</sub> = (120 ft)(2.40 kip/ft) | *Y*<sub>i</sub> = (120 ft)(1.60 kip/ft) |
| = 288 kips | = 192 kips |
| Δ = 0 in. (no drift for this load combination) | Δ = 0 in. (no drift for this load combination) |
| *L* = (20.0 ft)(12 in./ft) | *L* = (20.0 ft)(12 in./ft) |
| = 240 in. | = 240 in. |

---


---

---

## Notional Load Calculation

| LRFD | ASD |
|------|-----|
| *N*<sub>i</sub> = 2.1α(Δ/*L*)*Y*<sub>i</sub> ≥ 0.0042*Y*<sub>i</sub>     (*Spec.* Eq. A-7-3) | *N*<sub>i</sub> = 2.1α(Δ/*L*)*Y*<sub>i</sub> ≥ 0.0042*Y*<sub>i</sub>     (*Spec.* Eq. A-7-3) |
| = 2.1[(1.0)(0 in. / 240 in.)](288 kips) | = 2.1[(1.6)(0 in. / 240 in.)](192 kips) |
| > 0.0042(288 kips) | > 0.0042(192 kips) |
| = 0 kip < 1.21 kips | = 0 kip < 0.806 kip |
| Use *N*<sub>i</sub> = 1.21 kips | Use *N*<sub>i</sub> = 0.806 kip |

---

## *Summary of applied frame loads*

The applied loads are shown in Figure C.1C-2.

![Applied Loads Diagram](diagram)

| LRFD | ASD |
|------|-----|
| ![LRFD Load Diagram showing: 36.0 kips at both sides, 2.40 kip/ft distributed load, 1.21 kips lateral load] | ![ASD Load Diagram showing: 24.0 kips at both sides, 1.60 kip/ft distributed load, 0.806 kip lateral load] |

*Fig. C.1C-2. Applied loads on the analysis model.*

---

## First-Order Analysis Results

Conduct the analysis using the full nominal stiffnesses, as indicated in AISC *Specification* Commentary Appendix 7, Section 7.3.

Using analysis software, the first-order results shown in Figure C.1C-3 are obtained:

| LRFD | ASD |
|------|-----|
| Δ<sub>1st</sub> = 0.304 in. | Δ<sub>1st</sub> = 0.203 in. |
| ![Diagram showing moments 106 kip-ft and 131 kip-ft at top, reactions 5.32 kips and 6.53 kips at top, axial forces 71.2 kips and 72.8 kips at bottom] | ![Diagram showing moments 70.9 kip-ft and 87.1 kip-ft at top, reactions 3.55 kips and 4.35 kips at top, axial forces 47.5 kips and 48.5 kips at bottom] |

*Fig. C.1C-3. Results of first-order analysis.*

Check the assumption that the ratio of the second-order drift to the first-order drift does not exceed 1.5. *B*<sub>2</sub> can be used to check this limit. Calculate *B*<sub>2</sub> per Appendix 8, Section 8.1.3 using the results of the first-order analysis.

---


---

---

## Second-Order Effects Calculation

| LRFD | ASD |
|------|-----|
| *P*<sub>mf</sub> = 2(36.0 kips) + (30.0 ft)(2.40 kip/ft) | *P*<sub>mf</sub> = 2(24.0 kips) + (30.0 ft)(1.60 kip/ft) |
| = 144 kips | = 96.0 kips |
| *P*<sub>story</sub> = 144 kips + 4(36.0 kips) | *P*<sub>story</sub> = 96.0 kips + 4(24.0 kips) |
| = 288 kips | = 192 kips |
| *R*<sub>M</sub> = 1 − 0.15(*P*<sub>mf</sub> / *P*<sub>story</sub>)     (*Spec.* Eq. A-8-8) | *R*<sub>M</sub> = 1 − 0.15(*P*<sub>mf</sub> / *P*<sub>story</sub>)     (*Spec.* Eq. A-8-8) |
| = 1 − 0.15(144 kips/288 kips) | = 1 − 0.15(96.0 kips/192 kips) |
| = 0.925 | = 0.925 |
| Δ*H* = 0.304 in. | Δ*H* = 0.203 in. |
| *H* = 6.53 kips − 5.32 kips | *H* = 4.35 kips − 3.55 kips |
| = 1.21 kips | = 0.800 kip |
| *L* = (20 ft)(12 in./ft) | *L* = (20 ft)(12 in./ft) |
| = 240 in. | = 240 in. |
| *P*<sub>e_story</sub> = *R*<sub>M</sub> *HL* / Δ*H*     (*Spec.* Eq. A-8-7) | *P*<sub>e_story</sub> = *R*<sub>M</sub> *HL* / Δ*H*     (*Spec.* Eq. A-8-7) |
| = 0.925[(1.21 kips)(240 in.)] / 0.304 in. | = 0.925[(0.800 kip)(240 in.)] / 0.203 in. |
| = 884 kips | = 875 kips |
| α = 1.0 | α = 1.6 |
| $$B_2 = \frac{1}{1 - \frac{\alpha P_{story}}{P_{e\_story}}} \geq 1$$     (*Spec.* Eq. A-8-6) | $$B_2 = \frac{1}{1 - \frac{\alpha P_{story}}{P_{e\_story}}} \geq 1$$     (*Spec.* Eq. A-8-6) |
| $$= \frac{1}{1 - \frac{1.0(288 \text{ kips})}{884 \text{ kips}}} \geq 1$$ | $$= \frac{1}{1 - \frac{1.6(192 \text{ kips})}{875 \text{ kips}}} \geq 1$$ |
| = 1.48 > 1 | = 1.54 > 1 |

---

## Discussion

When a structure with a live-to-dead load ratio of 3 is analyzed by a first-order analysis, the required strength for LRFD will always be 1.5 times the required strength for ASD. However, when a second-order analysis is used, this ratio is not maintained. This is due to the use of the amplification factor, α, which is set equal to 1.6 for ASD, in order to capture the worst case scenario for any live-to-dead load ratio. Thus, in this example the limitation for applying the first-order analysis method, that the ratio of the maximum second-order drift to maximum first-order drift is not greater than 1.5, is verified for LRFD but is not verified for ASD. Therefore, for this example the first-order method is invalid for ASD and will proceed with LRFD only.

Check the assumption that α*P*<sub>r</sub> ≤ 0.5*P*<sub>ns</sub> and, therefore, the first-order analysis method is permitted.

Because the W12×65 column does not contain elements that are slender for compression,

*P*<sub>ns</sub> = *F*<sub>y</sub> *A*<sub>g</sub>

---


---

---

## Verification Calculations

0.5*P*<sub>ns</sub> = 0.5*F*<sub>y</sub> *A*<sub>g</sub>

= 0.5(50 ksi)(19.1 in.²)

= 478 kips

α*P*<sub>r</sub> = 1.0(72.8 kips)

= 72.8 kips < 478 kips   **o.k.** (LRFD only)

---

Check the assumption that α*P*<sub>r</sub> ≤ 0.08*P*<sub>e</sub> and, therefore, the first-order analysis method is permitted.

α = 1.0 (LRFD)

α*P*<sub>r</sub> = 1.0(1.21 kips)
= 1.21 kips

$$0.08P_e = 0.08\left(\frac{\pi^2 EI}{L^2}\right)$$

$$= 0.08\left\{\frac{\pi^2 (29,000 \text{ ksi})(612 \text{ in.}^4)}{[(30 \text{ ft})(12 \text{ in./ft})]^2}\right\}$$

= 108 kips > 1.21 kips   **o.k.** (LRFD only)

---

The assumption that the first-order analysis method can be used is verified for LRFD.

Although the second-order sway multiplier is 1.48, the change in bending moment is small because the only sway moments are those produced by the small notional loads. For load combinations with significant gravity and lateral loadings, the increase in bending moments is larger.

The column strengths can be verified after using the *B*<sub>1</sub> amplification given in Appendix 8, Section 8.1.2 to account for second-order effects (calculations not shown here). In the direction of sway, the effective length factor is taken equal to 1.00, and the column effective lengths are as follows:

*L*<sub>cx</sub> = 20.0 ft
*L*<sub>cy</sub> = 20.0 ft

---


---

**Status:** Blank page

**Content:** None

---


---
