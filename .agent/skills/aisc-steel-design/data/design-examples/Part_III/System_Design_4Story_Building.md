# System Design 4Story Building

**AISC Specification v16.0 - Design Examples**
**Original PDF Pages**: 941-1054 (114 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

System Design Examples

**Examples Included**: ['III-1: Four-Story Building Design']

---

## Table of Contents

- [EXAMPLE III-1 DESIGN OF SELECTED MEMBERS AND LATERAL ANALYSIS OF A FOUR-STORY BUILDING](#example-iii-1-design-of-selected-members-and-lateral-analysis-of-a-four-story-building)

---

# III-1

# Part III
# System Design Examples

---

# III-2

## EXAMPLE III-1 DESIGN OF SELECTED MEMBERS AND LATERAL ANALYSIS OF A FOUR-STORY BUILDING

**INTRODUCTION**

This section illustrates the load determination and selection of representative members that are part of the gravity and lateral frame of a typical four-story building. The design is completed in accordance with the AISC *Specification* and AISC *Manual*. Loading criteria are based on ASCE/SEI 7.

This section includes:
- Analysis and design of a typical steel frame for gravity loads
- Analysis and design of a typical steel frame for lateral loads
- Examples illustrating three methods for checking the stability provisions of AISC *Specification* Chapter C

The building being analyzed in this design example is located in a Midwestern city with moderate wind and seismic loads. The loads are given in the description of the design example. All members are ASTM A992/A992M material.

**CONVENTIONS**

The following conventions are used throughout this example:

1. Beams or columns that have similar, but not necessarily identical, loads are grouped together. This is done because such grouping is generally a more economical practice for design, fabrication, and erection.

2. Certain calculations, such as design loads for snow drift, which might typically be determined using a spreadsheet or structural analysis program, are summarized and then incorporated into the analysis. This simplifying feature allows the design example to illustrate concepts relevant to the member selection process.

3. Two commonly used deflection calculations for uniform loads have been rearranged so that the conventional units in the problem can be directly inserted into the equation for design. They are as follows:

   Simple beam:

   $$\Delta = \frac{5(w \text{ kip/in})(L \text{ in.})^4}{384(29{,}000 \text{ ksi})\left(I \text{ in.}^4\right)}$$

   $$= \frac{(w \text{ kip/ft})(L \text{ ft})^4}{1{,}290\left(I \text{ in.}^4\right)}$$ (Eq. III-1)

   Beam fixed at both ends:

   $$\Delta = \frac{(w \text{ kip/in})(L \text{ in.})^4}{384(29{,}000 \text{ ksi})\left(I \text{ in.}^4\right)}$$

   $$= \frac{(w \text{ kip/ft})(L \text{ ft})^4}{6{,}440\left(I \text{ in.}^4\right)}$$ (Eq. III-2)

---

# III-3

## DESIGN SEQUENCE

The design sequence is presented as follows:

1. General description of the building including geometry, gravity loads, and lateral loads

2. Roof member design and selection

3. Floor member design and selection

4. Column design and selection for gravity loads

5. Wind load determination

6. Seismic load determination

7. Horizontal force distribution to the lateral frames

8. Preliminary column selection for the moment frames and braced frames

9. Seismic load application to lateral systems

10. Stability (*P-Δ*) analysis

---

# III-4

## GENERAL DESCRIPTION OF THE BUILDING

**Geometry**

The design example is a four-story building, consisting of seven bays at 30 ft in the east-west (numbered grids) direction and bays of 45 ft, 30 ft, and 45 ft in the north-south (lettered grids) direction, as shown in Figure III-1. The floor-to-floor height for the four floors is 13 ft 6 in., and the height from the fourth floor to the roof (at the edge of the parapet) is 14 ft 6 in. Based on discussions with fabricators, the same column size will be used for the entire height of the building.

The plans of these floors and the roof are shown on Sheets S2.1 thru S2.3, found at the end of this Part. The exterior of the building is a ribbon window system with brick spandrels supported and back-braced with steel and infilled with metal stud. The spandrel wall extends 2 ft above the elevation of the edge of the roof. The window and spandrel system is shown on design drawing Sheet S4.1.

The roof system is 1½ in. metal deck on open web steel joists. The open web steel joists are supported on steel beams as shown on Sheet S2.3. The roof slopes to interior drains. The middle three bays have a 6-ft-tall screen wall around them and house the mechanical equipment and the elevator over run. This area has steel beams in place of open web steel joists to support the mechanical equipment.

The three elevated floors have 3 in. of normal weight concrete over 3 in. composite deck for a total slab thickness of 6 in. The supporting beams are spaced at 10 ft on center. These beams are carried by composite girders in the east-west direction to the columns. There is a 30 ft by 29 ft opening around the two-story atrium at the entrance. These floor layouts are shown on Sheets S2.1 and S2.2. The first floor is a slab on grade, and the foundation consists of conventional spread footings.

![Building plan layout showing:
- Grid lines numbered 1-8 (east-west) at 30'-0" spacing (7 @ 30'-0")
- Grid lines lettered A-F (north-south) with spacing: 0'-6", 45'-0", 22'-6" (with "Chevron brace" noted), 22'-6", 30'-0", 45'-0", 0'-6"
- "Moment frame, typ." marked on sides
- Compass rose showing N, S, E, W directions
- Total dimensions: 210'-0" (east-west) × 145'-0" (north-south)]

*Fig. III-1. Basic building layout.*

---

# III-5

The building includes both moment frames and braced frames for lateral resistance. The lateral system in the north-south direction consists of chevron braces at the end of the building located adjacent to the stairway. In the east-west direction, there are two-story atrium at the entrance. These floor layouts are shown on Sheets S2.1 and S2.2. The first floor is a slab on grade, and the foundation consists of conventional spread footings.

This building has a penthouse on the roof over 240 sq ft and consequently does not require stairs above the roof in accordance with IBC for occupancy. See Section 3.3.1.2 below. This building also is not required to comply with the height limitation of the special exception for allowable area without fire resistive construction per Section 10.1.6.1 and is allowed unlimited area without fire resistive construction per Section 10.1.6.2.

**Lateral Forces**

The Basic Wind Speed is 107 mph per ASCE 7, Figure 15. Exposure Category B: Flat open terrain is used in an open rural area, it will be classified as Exposure B per ASCE 7, Section 26.7-2. For determining the structural response, a building can be classified as "rigid" when its natural period based on the approximate period formula 12.8-7 is less than 1 s per ASCE 7, Section 6.5.8, with a response factor of Cp (12-6) or as "rigid" if its fundamental period is less than 0.1 s per ASCE 7, Equation 12.8-7, with a response acceleration parameter of SDS of 1.0.

Because the soil properties are not known in sufficient detail to determine the site class, Site Class D shall be used in accordance with ASCE 7, Section 11.4.2, and site response coefficients Fa and Fv shall be obtained from ASCE 7, Tables 11.4-1 through 11.4-2. The risk-targeted maximum considered earthquake spectral response acceleration at short period (Ss) and 1-s period (S1) from ASCE 7, Figures 22-1 through 22-14, to the architect has specified a bonded, non-yielded roof membrane as a result, the roof snow load shall be based per ASCE 7, Section 4-3, where applicable.

**Roof and Floor Loads**

The ground snow load per this site is pₒ = 20 psf per ASCE 7 Risk Category II. The design for flat Snow load of Pf = I × Cs × Ce × pₒ 20 per ASCE 7, Section 7.3.

The basic live load for the floor is 50 psf as required, which exceeds the elevation location, but not exceeding 3½ in elevation for locations 100 ft and exceeding elevation and exceeds pₒ = (20)(0.7) = 14 psf for additional live load shall be required per ASCE 7 × Table 1.3-1.

Floor Loads

Snow drift loads will be encountered around for the architectural elements should not be considered here as a result of reduction, which will result in increased dead roof live shall be reduced based on type of member and area per ASCE 7 provisions for live load reduction.

The basic live load of 50 psf will be used on the building as a result per ASCE 7 Table 1604.3.

A snow load of 24 psf will be used for the block spandrels, supporting steel and metal wall above the four HVAC areas.

---

# III-6

## ROOF MEMBER DESIGN AND SELECTION

Calculate dead load and snow load.

Dead load:

| Roofing | = 5 psf |
|---------|---------|
| Insulation | = 2 psf |
| Deck | = 2 psf |
| Beams | = 3 psf |
| Joists | = 3 psf |
| Misc. | = 5 psf |
| Total | = 20 psf |

Nominal (factored) snow load from ASCE/SEI 7, Sections 7.3 and 7.10:

| Snow | = 24.6 psf |
|------|------------|
| Rain on snow | = 8 psf |
| Total | = 32.6 psf |

Note: In this design, the rain and snow load is greater than the roof live load.

The deck is 1½ in., wide rib, 22 gage, painted roof deck, placed in a pattern of three continuous spans minimum. The typical joist spacing is 6 ft on center. At 6 ft on center, this deck has an allowable total load capacity of 87 psf (from the manufacturer's catalog). The roof diaphragm and roof loads extend 6 in. past the centerline of grid as shown on Sheet S4.1.

From ASCE/SEI 7, Section 7.7, the following drift loads are calculated:

Flat roof snow load: $p_f = 24.6$ psf
Density: $\gamma = 17.9 \text{ lb/ft}^3$

$$h_b = \frac{p_f}{\gamma}$$
$$= \frac{24.6 \text{ psf}}{17.9 \text{ lb/ft}^3}$$
$$= 1.37 \text{ ft}$$

**Summary of Drifts**

The snow drift at the penthouse was calculated for the maximum effect, using the east-west wind and an upwind fetch from the parapet to the centerline of the penthouse. This same drift is conservatively used for wind in the north-south direction. The precise location of the drift will depend upon the details of the penthouse construction, but will not affect the final design in this case. The drift load is applied to Table III-1.

Note that per ASCE/SEI, Section 7.10, the rain-on-snow surcharge applies only to the balanced load case and need not be used in combination with drift or the minimum snow load case, $p_m$. Additionally, the minimum snow load case is considered a separate uniform load case and need not be combined with drift. Therefore, for items without drift, the rain on snow surcharge is applicable.

ASCE/SEI 7-22 specifies ground snow levels at an LRFD load level and uses a factor of 0.7 for ASD design. ASCE/SEI, Commentary Section CC.2.1, proposes that snow loads with a 20-year return period be used for checking deflections. These examples use the ASD load level to check deflections, which is more conservative than the 20-year return period recommended by ASCE 7 but in line with previous design practice.

---

# III-7

| **Table III-1<br>Summary of Drifts** |  |  |  |  |  |
|---------------------------------------|--|--|--|--|--|
|  | **Upwind Roof<br>Length, $l_u$, ft** | **Projection<br>Height, ft** | **Drift Height,<br>$h_d$, ft** | **Max. Drift<br>Load, psf** | **Max. Drift<br>Width, $W$, ft** |
| Side parapet | 121 | 2 | 0.630 | 11.2 | 5.02 |
| End parapet | 211 | 2 | 0.630 | 11.2 | 5.02 |
| Screen wall | 60.5 | 6 | 2.37 | 42.4 | 18.9 |

---

# III-8

## SELECT ROOF JOISTS

Layout loads and size joists.

The 45-ft side joist with the heaviest loads is shown in Figure III-2 with end reactions and maximum moment.

Note: Joists may be specified using ASD or LRFD but are most commonly specified by ASD as shown here.

![Two joist loading diagrams showing:

Case 1 - Balanced snow with drift surcharge loads:
- Parapet on left with distributed loads: 0.0672 kip/ft at edge, wD = 0.120 kip/ft, wS = 0.148 kip/ft
- Screen wall on right with 0.254 kip/ft load
- Support reactions: RD = 2.76 kips, RS = 3.90 kips at A (left); RD = 2.70 kips, RS = 5.40 kips at C (right)
- Span: 6" + 4.52' + 18.9' + remaining to 45'-0" total (continuous bracing)
- Moments: MD = 30.4 kip-ft, MS = 45.3 kip-ft

Case 2 - Balanced snow with rain-on-snow surcharge loads:
- Similar layout with wD = 0.120 kip/ft, wS = 0.196 kip/ft
- Support reactions: RD = 2.76 kips, RS = 4.51 kips at A; RD = 2.70 kips, RS = 4.41 kips at C
- Same span configuration
- Moments: MD = 30.4 kip-ft, MS = 49.6 kip-ft]

*Fig III-2. Joist loading and bracing diagram—ASD.*

From ASCE/SEI 7, Chapter 2, the required shear strength of the joist at grid A and F (opposite hand) is governed by the case of dead load combined with the balanced snow and rain-on-snow surcharge (due to the parapet, the required shear strength of the joist at grid A and F is less than the support reaction):

$$R_a = 2.70 \text{ kip} + 0.7(4.41 \text{ kips})$$
$$= 5.79 \text{ kips}$$

From ASCE/SEI 7, Chapter 2, the required shear strength of the joist at grid C and D (opposite hand) is governed by the case of dead load combined with balanced snow and drift:

$$R_a = 2.70 \text{ kip} + 0.7(5.40 \text{ kips})$$
$$= 6.48 \text{ kips}$$

---

# III-9

From ASCE/SEI 7, Chapter 2, the required flexural strength of the joist is governed by the case of dead load combined with balanced snow and rain-on-snow surcharge:

$$M_a = 30.4 \text{ kip-ft} + 0.7(49.6 \text{ kip-ft})$$
$$= 65.1 \text{ kip-ft}$$

Because the load is not uniform, select a 24KCS4 joist from the Steel Joist Institute (SJI) *Load Tables and Weight Tables for Steel Joists and Joist Girders* (SJI, 2020). This joist has an allowable moment of 92.3 kip-ft, an allowable shear of 8.40 kips, a gross moment of inertia of 453 in.<sup>4</sup> and weighs 16.5 plf.

The first joist away from the end of the building is loaded with snow drift along the length of the member. Based on analysis, a 24KCS4 joist is also acceptable for this uniform load case.

As an alternative to directly specifying the joist sizes on the design document, as done in this example, loading diagrams can be included on the design documents to allow the joist manufacturer to economically design the joists.

The typical 30-ft-long joist in the middle bay will have a uniform load of:

$$w = (6 \text{ ft})\left[20 \text{ psf} + 0.7(32.6 \text{ psf})\right]$$
$$= 257 \text{ plf}$$

$$w_S = (6 \text{ ft})(0.7)(32.6 \text{ psf})$$
$$= 137 \text{ plf}$$

From the SJI load tables, select an 18K5 joist that weighs approximately 7.7 plf and satisfies both strength and deflection requirements.

Note: the first joist away from the screen wall and the first joist away from the end of the building carry snow drift. Based on analysis, an 18K9 joist will be used in these locations.

---

# III-10

## SELECT ROOF BEAMS

Calculate loads and select beams in the mechanical area.

For the beams in the mechanical area, the mechanical units could weigh as much as 60 psf. Use 40 psf additional dead load, which will account for the mechanical units and all stresses in and around the mechanical area. Use 15 psf additional snow load, which will account for any snow drift that could occur in the mechanical area and exceeds the rain-on-snow surcharge. The beams in the mechanical area are spaced at 6 ft on center. Loading is calculated as follows and shown in Figure III-3.

$$w_D = (6 \text{ ft})\left(0.020 \text{ kip/ft}^2 + 0.040 \text{ kip/ft}^2\right)$$
$$= 0.360 \text{ kip/ft}$$

$$w_S = (6 \text{ ft})\left(0.0246 \text{ kip/ft}^2 + 0.015 \text{ kip/ft}^2\right)$$
$$= 0.238 \text{ kip/ft}$$

![Loading diagram showing:
- Distributed loads: wD = 0.360 kip/ft, wS = 0.238 kip/ft
- Simply supported beam with full lateral support
- Span: 30'-0"
- Support points labeled C and D]

*Fig. III-3. Loading and bracing diagram for roof beams in mechanical area.*

From ASCE/SEI 7, Chapter 2, calculate the required strength of the beams in the mechanical area.

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.360 \text{ kip/ft}) + 1.0(0.238 \text{ kip/ft})$ | $w_a = 0.360 \text{ kip/ft} + 0.7(0.238 \text{ kip/ft})$ |
| $= 0.670 \text{ kip/ft}$ | $= 0.527 \text{ kip/ft}$ |
|  |  |
| $R_u = (0.670 \text{ kip/ft})\left(\frac{30 \text{ ft}}{2}\right)$ | $R_a = (0.527 \text{ kip/ft})\left(\frac{30 \text{ ft}}{2}\right)$ |
| $= 10.1 \text{ kips}$ | $= 7.91 \text{ kips}$ |
|  |  |
| $M_u = \frac{(0.670 \text{ kip/ft})(30 \text{ ft})^2}{8}$ | $M_a = \frac{(0.527 \text{ kip/ft})(30 \text{ ft})^2}{8}$ |
| $= 75.4 \text{ kip-ft}$ | $= 59.3 \text{ kip-ft}$ |

As discussed in AISC Design Guide 3, *Serviceability Design Considerations for Steel Buildings* (West et al., 2003), limit deflection to $L/360$ because a plaster ceiling will be used in the lobby area.

$$\frac{L}{360} = \frac{(30 \text{ ft})(12 \text{ in./ft})}{360}$$
$$= 1.00 \text{ in.}$$

---

# III-11

Using the equation for deflection derived previously, the required moment of inertia, $I_x \, req$, can be determined as follows. Use $0.7(24.6 \text{ psf} + 15 \text{ psf}) = 27.7$ psf as an estimate of the service level snow load, including some drifting that could occur in this area, for deflection calculations.

$$I_x \, req = \frac{(6 \text{ ft})\left(0.0277 \text{ kip/ft}^2\right)(30 \text{ ft})^4}{1{,}290(1.00 \text{ in.})}$$ (from Eq. III-1)
$$= 104 \text{ in.}^4$$

From AISC *Manual* Table 3-3, select a beam size with an adequate moment of inertia. Try a W14×22:

$$I_x = 199 \text{ in.}^4 > 104 \text{ in.}^4 \quad \textbf{o.k.}$$

From AISC *Manual* Table 6-1, the available flexural strength and shear strength for a W14×22 is determined as follows. Assume the beam has full lateral support; therefore, $L_b = 0$.

| LRFD | ASD |
|------|-----|
| $\phi_b M_{nx} = 125 \text{ kip-ft} > 75.4 \text{ kip-ft} \quad \textbf{o.k.}$ | $\frac{M_{nx}}{\Omega_b} = 82.8 \text{ kip-ft} > 59.3 \text{ kip-ft} \quad \textbf{o.k.}$ |
|  |  |
| $\phi_v V_n = 94.5 \text{ kips} > 10.1 \text{ kips} \quad \textbf{o.k.}$ | $\frac{V_n}{\Omega_v} = 63.0 \text{ kips} > 7.91 \text{ kips} \quad \textbf{o.k.}$ |

Note: The beams and supporting girders in this area should be rechecked when the final weights and locations for the mechanical units have been determined.

---

# III-12

## SELECT ROOF BEAMS AT THE END (EAST & WEST) OF THE BUILDING

The beams at the ends of the building carry the brick spandrel panel and a small portion of roof load. For these beams, the cladding weight exceeds 25% of the total dead load on the beam. Therefore, per AISC Design Guide 3, limit the vertical deflection due to cladding and initial dead load to $L/600$ or ⅝ in. maximum. In addition, because these beams are supporting brick above and there is continuous glass below, limit the superimposed dead and live load to $L/600$ or 0.3 in. maximum to accommodate the brick and $L/360$ or ¼ in. maximum to accommodate the glass. Therefore, combining the two limitations, limit the superimposed dead and live load deflection to $L/600$ or ¼ in. The superimposed dead load includes all of the dead load that is applied after the cladding has been installed. In calculating the wall loads, the spandrel panel weight is taken as 55 psf. Beam loading is calculated as follows and shown in Figure III-4. Note, the beams are laterally supported by the deck as shown in Detail 4 on Sheet S4.1.

![Loading diagram showing:
- Distributed loads: wD = 0.413 kip/ft + 0.070 kip/ft = 0.483 kip/ft, wS = 0.125 kip/ft
- Simply supported beam with full lateral support
- Span: 22'-6"
- Support points labeled D and E]

*Fig. III-4. Beam loading and bracing diagram for roof beams at east and west ends of building.*

The dead load from the spandrel is:

$$w_D = (7.50 \text{ ft})\left(0.055 \text{ kip/ft}^2\right)$$
$$= 0.413 \text{ kip/ft}$$

The dead load from the roof is equal to:

$$w_D = (3.50 \text{ ft})\left(0.020 \text{ kip/ft}^2\right)$$
$$= 0.070 \text{ kip/ft}$$

Use 8 psf for the initial dead load, which includes the deck, beams, and joists:

$$w_{D(initial)} = (3.50 \text{ ft})\left(0.008 \text{ kip/ft}^2\right)$$
$$= 0.028 \text{ kip/ft}$$

Use 12 psf for the superimposed dead load:

$$w_{D(super)} = (3.50 \text{ ft})\left(0.012 \text{ kip/ft}^2\right)$$
$$= 0.042 \text{ kip/ft}$$

The snow load from the roof conservatively uses the maximum snow drift as a uniform load, considering both side and end parapet drift pressures:

---

# III-13

$$w_S = (3.50 \text{ ft})\left(0.0246 \text{ kip/ft}^2 + 0.0112 \text{ kip/ft}^2\right)$$
$$= 0.125 \text{ kip/ft}$$

From ASCE/SEI 7, Chapter 2, calculate the required strength of the beams at the east and west ends of the roof.

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.483 \text{ kip/ft}) + 1.0(0.125 \text{ kip/ft})$ | $w_a = 0.483 \text{ kip/ft} + 0.7(0.125 \text{ kip/ft})$ |
| $= 0.705 \text{ kip/ft}$ | $= 0.571 \text{ kip/ft}$ |
|  |  |
| $R_u = (0.705 \text{ kip/ft})\left(\frac{22.5 \text{ ft}}{2}\right)$ | $R_a = (0.571 \text{ kip/ft})\left(\frac{22.5 \text{ ft}}{2}\right)$ |
| $= 7.93 \text{ kips}$ | $= 6.42 \text{ kips}$ |
|  |  |
| $M_u = \frac{(0.705 \text{ kip/ft})(22.5 \text{ ft})^2}{8}$ | $M_a = \frac{(0.571 \text{ kip/ft})(22.5 \text{ ft})^2}{8}$ |
| $= 44.6 \text{ kip-ft}$ | $= 36.1 \text{ kip-ft}$ |

Assume the beams are simple spans of 22.5 ft. Calculate the minimum moment of inertia to limit the superimposed dead and ASD level snow (0.7S) load deflection after cladding is installed to $L/600$ or ¼ in.

$$\frac{L}{600} = \frac{(22.5 \text{ ft})(12 \text{ in./ft})}{600} \leq \frac{1}{4} \text{ in.}$$
$$= 0.450 \text{ in.} > \frac{1}{4} \text{ in.}$$

Therefore, limit deflection to ¼ in.

Using the equation for deflection derived previously, the required moment of inertia, $I_x \, req$, can be determined as follows:

$$I_x \, req = \frac{\left[0.042 \text{ kip/ft} + 0.7(0.125 \text{ kip/ft})\right](22.5 \text{ ft})^4}{1{,}290(\frac{1}{4} \text{ in.})}$$ (from Eq. III-1)
$$= 103 \text{ in.}^4$$

Calculate the minimum moment of inertia to limit the cladding and initial dead load deflection to $L/600$ or ⅝ in.

$$\frac{L}{600} = \frac{(22.5 \text{ ft})(12 \text{ in./ft})}{600} \leq \frac{5}{8} \text{ in.}$$
$$= 0.450 \text{ in.} > \frac{5}{8} \text{ in.}$$

Therefore, limit deflection to ⅝ in.

Using the equation for deflection derived previously, the required moment of inertia, $I_x \, req$, can be determined as follows:

$$I_x \, req = \frac{(0.413 \text{ kip/ft} + 0.028 \text{ kip/ft})(22.5 \text{ ft})^4}{1{,}290(\frac{5}{8} \text{ in.})}$$ (from Eq. III-1)
$$= 234 \text{ in.}^4 \quad \textbf{controls}$$

---

# III-14

From AISC *Manual* Table 3-3, select a beam size with an adequate moment of inertia. Try a W16×26:

$$I_x = 301 \text{ in.}^4 > 234 \text{ in.}^4 \quad \textbf{o.k.}$$

From AISC *Manual* Table 6-1, the available flexural strength and shear strength for a W16×26 is determined as follows. The beam has full lateral support; therefore, $L_b = 0$.

| LRFD | ASD |
|------|-----|
| $\phi_b M_{nx} = 166 \text{ kip-ft} > 44.6 \text{ kip-ft} \quad \textbf{o.k.}$ | $\frac{M_{nx}}{\Omega_b} = 110 \text{ kip-ft} > 36.1 \text{ kip-ft} \quad \textbf{o.k.}$ |
|  |  |
| $\phi_v V_n = 106 \text{ kips} > 7.93 \text{ kips} \quad \textbf{o.k.}$ | $\frac{V_n}{\Omega_v} = 70.5 \text{ kips} > 6.42 \text{ kips} \quad \textbf{o.k.}$ |

---

# III-15

## SELECT ROOF BEAMS ALONG THE SIDE (NORTH & SOUTH) OF THE BUILDING

The beams along the side of the building carry the spandrel panel and a substantial roof dead load and live load. For these beams, the cladding weight exceeds 25% of the total dead load on the beam. From AISC Design Guide 3, limit the vertical deflection due to cladding and initial dead load to $L/600$ or ⅝ in. maximum. In addition, because these beams are supporting brick above and there is continuous glass below, limit the superimposed dead and live load deflection to $L/600$ or 0.3 in. maximum to accommodate the brick and $L/360$ or ¼ in. maximum to accommodate the glass. Therefore, combining the two limitations, limit the superimposed dead and live load deflection to $L/600$ or ¼ in. The superimposed dead load includes all of the dead load that is applied after the cladding has been installed. These beams will be part of the moment frames on the side of the building and therefore will be designed as fixed at both ends. The roof dead load and snow load on this edge beam is equal to the joist end dead load and snow load reaction. Treat this as a uniform load and divide by the joist spacing. (Note: treating this as a uniform load is a convenient and reasonable approximation in this case, resulting in a difference in maximum moment of approximately 4% as compared to the moment calculated using concentrated loading from each of the roof joists acting on the beam). Beam loading is calculated as follows, and shown in Figure III-5.

The dead load from the joist end reaction is:

$$w_D = \frac{2.76 \text{ kips}}{6.00 \text{ ft}}$$
$$= 0.460 \text{ kip/ft}$$

From previous calculations, the dead load from the spandrel is:

$$w_D = 0.413 \text{ kip/ft}$$

The snow load from the joist end reaction is:

$$w_S = \frac{4.51 \text{ kips}}{6.00 \text{ ft}}$$
$$= 0.752 \text{ kip/ft}$$

![Loading and bracing diagram showing:
- Distributed loads: wD = 0.460 kip/ft + 0.413 kip/ft = 0.873 kip/ft, wS = 0.752 kip/ft
- Continuous beam with bracing at ends and fifth points
- Span: 30'-0"
- Support points labeled 2 and 3
- Bracing locations shown: "Top and bottom flange brace" at ends, "Top flange brace" at top, "Bottom flange brace" at bottom]

*Fig. III-5. Loading and bracing diagram for roof beams at north and south ends of building.*

---

# III-16

Use 8 psf for initial dead load and 12 psf for superimposed dead load.

$$w_{D(initial)} = \left(22.5 \text{ ft} + 0.5 \text{ ft}\right)\left(0.008 \text{ kip/ft}^2\right)$$
$$= 0.184 \text{ kip/ft}$$

$$w_{D(super)} = \left(22.5 \text{ ft} + 0.5 \text{ ft}\right)\left(0.012 \text{ kip/ft}^2\right)$$
$$= 0.276 \text{ kip/ft}$$

From ASCE/SEI 7, Chapter 2, calculate the required strength of the beams at the roof sides.

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.873 \text{ kip/ft}) + 1.0(0.752 \text{ kip/ft})$ | $w_a = 0.873 \text{ kip/ft} + 0.7(0.752 \text{ kip/ft})$ |
| $= 1.80 \text{ kip/ft}$ | $= 1.40 \text{ kip/ft}$ |
|  |  |
| $R_u = (1.80 \text{ kip/ft})\left(\frac{30 \text{ ft}}{2}\right)$ | $R_a = (1.40 \text{ kip/ft})\left(\frac{30 \text{ ft}}{2}\right)$ |
| $= 27.0 \text{ kips}$ | $= 21.0 \text{ kips}$ |

Using the equation for deflection derived previously, the required moment of inertia, $I_x \, req$, is determined as follows.

To limit the superimposed dead and live load deflection to ¼ in.:

$$I_x \, req = \frac{\left[0.7(0.752 \text{ kip/ft}) + 0.276 \text{ kip/ft}\right](30 \text{ ft})^4}{6{,}440(\frac{1}{4} \text{ in.})}$$ (from Eq. III-2)
$$= 404 \text{ in.}^4 \quad \textbf{controls}$$

To limit the cladding and initial dead load deflection to ⅝ in.:

$$I_x \, req = \frac{(0.413 \text{ kip/ft} + 0.184 \text{ kip/ft})(30.0 \text{ ft})^4}{6{,}440(\frac{5}{8} \text{ in.})}$$ (from Eq. III-2)
$$= 200 \text{ in.}^4$$

From AISC *Manual* Table 3-3, select a beam size with an adequate moment of inertia. Try a W18×35:

$$I_x = 510 \text{ in.}^4 > 404 \text{ in.}^4 \quad \textbf{o.k.}$$

Calculate $C_b$ for compression in the bottom flange braced at the midpoint and supports using AISC *Specification* Equation F1-1. Moments along the span are summarized in Figure III-6.

| LRFD | ASD |
|------|-----|
| From AISC *Manual* Table 3-22, Case 15: | From AISC *Manual* Table 3-22, Case 15: |
|  |  |
| $M_{u \, max} = \frac{(1.80 \text{ kip/ft})(30 \text{ ft})^2}{12}$ | $M_{a \, max} = \frac{(1.40 \text{ kip/ft})(30 \text{ ft})^2}{12}$ |
| $= 135 \text{ kip-ft}$ (at supports) | $= 105 \text{ kip-ft}$ (at supports) |

---

# III-17

| LRFD | ASD |
|------|-----|
| At midpoint: | At midpoint: |
|  |  |
| $M_u = \frac{(1.80 \text{ kip/ft})(30 \text{ ft})^2}{24}$ | $M_a = \frac{(1.40 \text{ kip/ft})(30 \text{ ft})^2}{24}$ |
| $= 67.5 \text{ kip-ft}$ | $= 52.5 \text{ kip-ft}$ |
|  |  |
| At quarter-point of unbraced length: | At quarter-point of unbraced length: |
|  |  |
| $M_{uA} = \left\|\frac{1.80 \text{ kip/ft}}{12}\left[\frac{6(30 \text{ ft})(3.75 \text{ ft}) - (30 \text{ ft})^2}{-6(3.75 \text{ ft})^2}\right]\right\|$ | $M_{aA} = \left\|\frac{1.40 \text{ kip/ft}}{12}\left[\frac{6(30 \text{ ft})(3.75 \text{ ft}) - (30 \text{ ft})^2}{-6(3.75 \text{ ft})^2}\right]\right\|$ |
| $= 46.4 \text{ kip-ft}$ | $= 36.1 \text{ kip-ft}$ |
|  |  |
| At midpoint of unbraced length: | At midpoint of unbraced length: |
|  |  |
| $M_{uB} = \left\|\frac{1.80 \text{ kip/ft}}{12}\left[\frac{6(30 \text{ ft})(7.50 \text{ ft}) - (30 \text{ ft})^2}{-6(7.50 \text{ ft})^2}\right]\right\|$ | $M_{aB} = \left\|\frac{1.40 \text{ kip/ft}}{12}\left[\frac{6(30 \text{ ft})(7.50 \text{ ft}) - (30 \text{ ft})^2}{-6(7.50 \text{ ft})^2}\right]\right\|$ |
| $= 16.9 \text{ kip-ft}$ | $= 13.1 \text{ kip-ft}$ |
|  |  |
| At three-quarter point of unbraced length: | At three-quarter point of unbraced length: |
|  |  |
| $M_{uC} = \left\|\frac{1.80 \text{ kip/ft}}{12}\left[\frac{6(30 \text{ ft})(11.3 \text{ ft}) - (30 \text{ ft})^2}{-6(11.3 \text{ ft})^2}\right]\right\|$ | $M_{aC} = \left\|\frac{1.40 \text{ kip/ft}}{12}\left[\frac{6(30 \text{ ft})(11.3 \text{ ft}) - (30 \text{ ft})^2}{-6(11.3 \text{ ft})^2}\right]\right\|$ |
| $= 55.2 \text{ kip-ft}$ | $= 42.9 \text{ kip-ft}$ |

![Two beam moment diagrams showing:
(a) LRFD: Distributed load wu = 1.80 kip/ft over 30'-0" span, moment diagram showing values 135 at supports, 46.4, 16.9, 55.2 (peak at 67.5), labeled Mu (kip-ft)
(b) ASD: Distributed load wa = 1.40 kip/ft over 30'-0" span, moment diagram showing values 105 at supports, 36.1, 13.1, 42.9 (peak at 52.5), labeled Ma (kip-ft)]

*Fig. III-6. Beam moment diagram.*

---

# III-18

Using AISC *Specification* Equation F1-1:

| LRFD | ASD |
|------|-----|
| $C_b = \frac{12.5M_{max}}{2.5M_{max} + 3M_A + 4M_B + 3M_C}$ | $C_b = \frac{12.5M_{max}}{2.5M_{max} + 3M_A + 4M_B + 3M_C}$ |
|  |  |
| $= \frac{12.5(135 \text{ kip-ft})}{2.5(135 \text{ kip-ft}) + 3(46.4 \text{ kip-ft}) + 4(16.9 \text{ kip-ft}) + 3(55.2 \text{ kip-ft})}$ | $= \frac{12.5(105 \text{ kip-ft})}{2.5(105 \text{ kip-ft}) + 3(36.1 \text{ kip-ft}) + 4(13.1 \text{ kip-ft}) + 3(42.9 \text{ kip-ft})}$ |
| $= 2.38$ | $= 2.38$ |

From AISC *Manual* Table 6-1, for a W18×35 with $L_b = 6$ ft and $C_b = 1.0$ the available flexural strength is determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 229 \text{ kip-ft} > 67.5 \text{ kip-ft} \quad \textbf{o.k.}$ | $\frac{M_n}{\Omega_b} = 152 \text{ kip-ft} > 52.5 \text{ kip-ft} \quad \textbf{o.k.}$ |

From AISC *Manual* Table 6-1, for a W18×35 with $L_b = 15$ ft and using the $C_b$ value calculated previously, the available flexural strength is determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n C_b \leq \phi_b M_p$ | $\frac{M_n}{\Omega_b}C_b \leq \frac{M_p}{\Omega_b}$ |
| $(109 \text{ kip-ft})(2.38) > 249 \text{ kip-ft}$ | $(72.4 \text{ kip-ft})(2.38) > 166 \text{ kip-ft}$ |
| $259 \text{ kip-ft} > 249 \text{ kip-ft}$ | $172 \text{ kip-ft} > 166 \text{ kip-ft}$ |
|  |  |
| Therefore: | Therefore: |
| $\phi_b M_n = 249 \text{ kip-ft} > 135 \text{ kip-ft} \quad \textbf{o.k.}$ | $\frac{M_n}{\Omega_b} = 166 \text{ kip-ft} > 105 \text{ kip-ft} \quad \textbf{o.k.}$ |

From AISC *Manual* Table 6-1, the available shear strength is determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi_v V_n = 159 \text{ kips} > 27.0 \text{ kips} \quad \textbf{o.k.}$ | $\frac{V_n}{\Omega_v} = 106 \text{ kips} > 21.0 \text{ kips} \quad \textbf{o.k.}$ |

Therefore, the W18×35 is acceptable.

Note: This roof beam may need to be upsized during the lateral load analysis to increase the stiffness and strength of the member and improve lateral frame drift performance.

---

# III-19

## SELECT THE ROOF BEAMS ALONG THE INTERIOR LINES OF THE BUILDING

There are three individual beam loadings that occur along grids C and D. The beams from 1 to 2 and 7 to 8 have a uniform snow load except for the snow drift at the parapet. The snow drift from the far ends of the 45 ft joists is negligible. The beams from 2 to 3 and 6 to 7 are the same as the first group, except they have snow drift at the screen wall. The live load deflection is limited to $L/240$ (or 1.50 in.). Joist reactions are divided by the joist spacing and treated as a uniform load, just as they were for the side beams.

$$w_D = \left(0.020 \text{ kip/ft}^2\right)\left(\frac{45 \text{ ft} + 30 \text{ ft}}{2}\right)$$
$$= 0.750 \text{ kip/ft}$$

For snow load only:

$$w_S = \left(0.0246 \text{ kip/ft}^2\right)\left(\frac{45 \text{ ft} + 30 \text{ ft}}{2}\right)$$
$$= 0.923 \text{ kip/ft}$$

For snow with rain-on-snow load:

$$w_S = \left(0.0326 \text{ kip/ft}^2\right)\left(\frac{45 \text{ ft} + 30 \text{ ft}}{2}\right)$$
$$= 1.22 \text{ kip/ft}$$

The loading diagrams with moments and end reactions for the cases with drift are shown in Figure III-7. Note that rain-on-snow surcharge and drift are not required to be simultaneously applied. For the beam at the parapet (grids 1 to 2 and 7 to 8), the case with balanced snow combined with rain-on-snow surcharge controls over the case with balanced snow combined with drift. For the beam at the screen wall (grids 2 to 3 and 6 to 7), the case with the balanced snow combined with drift controls over balanced snow combined with rain-on-snow surcharge.

From ASCE/SEI 7, Chapter 2, the required strength for the beams from grids 1 to 2 and 7 to 8 (opposite hand) is determined as follows:

| LRFD | ASD |
|------|-----|
| $R_u$ (left end) $= 1.2(11.6 \text{ kips}) + 1.0(19.0 \text{ kips})$ | $R_a$ (left end) $= 11.6 \text{ kips} + 0.7(19.0 \text{ kips})$ |
| $= 32.9 \text{ kips}$ | $= 24.9 \text{ kips}$ |
|  |  |
| $R_u$ (right end) $= 1.2(11.2 \text{ kips}) + 1.0(18.3 \text{ kips})$ | $R_a$ (right end) $= 11.2 \text{ kips} + 0.7(18.3 \text{ kips})$ |
| $= 31.7 \text{ kips}$ | $= 24.0 \text{ kips}$ |
|  |  |
| $M_u = 1.2(84.3 \text{ kip-ft}) + 1.0(138 \text{ kip-ft})$ | $M_a = 84.3 \text{ kip-ft} + 0.7(138 \text{ kip-ft})$ |
| $= 239 \text{ kip-ft}$ | $= 181 \text{ kip-ft}$ |

Using the equation for deflection derived previously, the minimum moment of inertia, $I_x \, req$, to limit the live load deflection to 1.50 in., considering a 30 ft simply supported beam and neglecting the modest snow drift is:

$$I_x \, req = \frac{0.7(0.923 \text{ kip/ft})(30 \text{ ft})^4}{1{,}290(1.50 \text{ in.})}$$ (from Eq. III-1)
$$= 270 \text{ in.}^4$$

---

# III-20

From AISC *Manual* Table 3-3, select a beam size with an adequate moment of inertia. Try a W21×44:

$$I_x = 843 \text{ in.}^4 > 270 \text{ in.}^4 \quad \textbf{o.k.}$$

From AISC *Manual* Table 6-1, for a W21×44 with $L_b = 6$ ft and $C_b = 1.0$, the available flexural strength and shear strength are determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 332 \text{ kip-ft} > 239 \text{ kip-ft} \quad \textbf{o.k.}$ | $\frac{M_n}{\Omega_b} = 221 \text{ kip-ft} > 181 \text{ kip-ft} \quad \textbf{o.k.}$ |
|  |  |
| $\phi_v V_n = 217 \text{ kips} > 32.9 \text{ kips} \quad \textbf{o.k.}$ | $\frac{V_n}{\Omega_v} = 145 \text{ kips} > 24.9 \text{ kips} \quad \textbf{o.k.}$ |

![Two loading diagrams showing:

Case 1 - Balanced snow with drift surcharge loads:
- Parapet on left with 0.420 kip/ft load
- Distributed loads: wD = 0.750 kip/ft, wS = 0.923 kip/ft
- Support reactions: RD = 11.6 kips, RS = 15.3 kips at grid 1; RD = 11.2 kips, RS = 13.9 kips at grid 2
- Span: 6" + 4.52' + remaining to 30'-0" total (bracing at fifth points)
- Moments: MD = 84.3 kip-ft, MS = 105 kip-ft

Case 2 - Balanced snow with rain-on-snow surcharge loads:
- Similar layout with wD = 0.750 kip/ft, wS = 1.22 kip/ft
- Support reactions: RD = 11.6 kips, RS = 19.0 kips at grid 1; RD = 11.2 kips, RS = 18.3 kips at grid 2
- Same span configuration
- Moments: MD = 84.3 kip-ft, MS = 138 kip-ft]

*(a) Grids 1 to 2 and 7 to 8*

*Fig. III-7. Roof beam loading and bracing diagram.*

---

# III-21

From ASCE/SEI 7, Chapter 2, the required strength for the beams from grids 2 to 3 and 6 to 7 (opposite hand) is determined as follows:

| LRFD | ASD |
|------|-----|
| $R_u$ (left end) $= 1.2(11.3 \text{ kips}) + 1.0(17.0 \text{ kips})$ | $R_a$ (left end) $= 11.3 \text{ kips} + 0.7(17.0 \text{ kips})$ |
| $= 30.6 \text{ kips}$ | $= 23.2 \text{ kips}$ |
|  |  |
| $R_u$ (right end) $= 1.2(11.3 \text{ kips}) + 1.0(25.7 \text{ kips})$ | $R_a$ (right end) $= 11.3 \text{ kips} + 0.7(25.7 \text{ kips})$ |
| $= 39.3 \text{ kips}$ | $= 29.3 \text{ kips}$ |
|  |  |
| $M_u = 1.2(84.4 \text{ kip-ft}) + 1.0(152 \text{ kip-ft})$ | $M_a = 84.4 \text{ kip-ft} + 0.7(152 \text{ kip-ft})$ |
| $= 253 \text{ kip-ft}$ | $= 191 \text{ kip-ft}$ |

![Two loading diagrams showing:

Case 1 - Balanced snow with drift surcharge loads:
- Distributed loads: wD = 0.750 kip/ft, wS = 0.923 kip/ft
- Screen wall on right with 1.59 kip/ft load
- Support reactions: RD = 11.3 kips, RS = 17.0 kips at grid 2; RD = 11.3 kips, RS = 25.7 kips at grid 3
- Span: 18.9' drift width, total 30'-0" (bracing at fifth points)
- Moments: MD = 84.4 kip-ft, MS = 152 kip-ft

Case 2 - Balanced snow with rain-on-snow surcharge loads:
- Similar layout with wD = 0.750 kip/ft, wS = 1.22 kip/ft
- Support reactions: RD = 11.3 kips, RS = 18.3 kips at grid 2; RD = 11.3 kips, RS = 18.3 kips at grid 3
- Same span configuration
- Moments: MD = 84.4 kip-ft, MS = 137 kip-ft]

*(b) Grids 2 to 3 and 6 to 7*

*Fig. III-7 (continued). Roof beam loading and bracing diagram.*

---

# III-22

From AISC *Manual* Table 6-1, for a W21×44 with $L_b = 6$ ft and $C_b = 1.0$, the available flexural strength and shear strength are determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 332 \text{ kip-ft} > 253 \text{ kip-ft} \quad \textbf{o.k.}$ | $\frac{M_n}{\Omega_b} = 221 \text{ kip-ft} > 191 \text{ kip-ft} \quad \textbf{o.k.}$ |
|  |  |
| $\phi_v V_n = 217 \text{ kips} > 39.3 \text{ kips} \quad \textbf{o.k.}$ | $\frac{V_n}{\Omega_v} = 145 \text{ kips} > 24.9 \text{ kips} \quad \textbf{o.k.}$ |

The third individual beam loading occurs at the beams from 3 to 4, 4 to 5, and 5 to 6. For these beams, there is a uniform snow load outside the screen walled area, except for the snow drift at the parapet ends and the screen wall ends of the 45-ft-long joists. Inside the screen walled area, the beams support the mechanical equipment. The loading diagram is shown in Figure III-8.

$$w_D = \left(\frac{2.70 \text{ kips}}{6 \text{ ft}}\right) + (0.360 \text{ kip/ft})\left(\frac{15 \text{ ft}}{6 \text{ ft}}\right)$$
$$= 1.35 \text{ kip/ft}$$

$$w_S = \left(\frac{5.40 \text{ kips}}{6 \text{ ft}}\right) + (0.238 \text{ kip/ft})\left(\frac{15 \text{ ft}}{6 \text{ ft}}\right)$$
$$= 1.50 \text{ kip/ft}$$

From ASCE/SEI 7, Chapter 2, the required strength for the beams from grids 3 to 4, 4 to 5, and 5 to 6 is determined as follows:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(1.35 \text{ kip/ft}) + 1.0(1.50 \text{ kip/ft})$ | $w_a = 1.35 \text{ kip/ft} + 0.7(1.50 \text{ kip/ft})$ |
| $= 3.12 \text{ kip/ft}$ | $= 2.40 \text{ kip/ft}$ |
|  |  |
| $M_u = \frac{(3.12 \text{ kip/ft})(30 \text{ ft})^2}{8}$ | $M_a = \frac{(2.40 \text{ kip/ft})(30 \text{ ft})^2}{8}$ |
| $= 351 \text{ kip-ft}$ | $= 270 \text{ kip-ft}$ |

![Loading diagram showing:
- Distributed loads: wD = 1.35 kip/ft, wS = 1.50 kip/ft
- Simply supported beam with bracing at ends and fifth points
- Span: 30'-0"
- Support points labeled 3 and 4]

*Fig. III-8. Loading and bracing diagram for roof beams from grid 3 to 4, 4 to 5, and 5 to 6.*

---

# III-23

| LRFD | ASD |
|------|-----|
| $R_u = (3.12 \text{ kip/ft})\left(\frac{30 \text{ ft}}{2}\right)$ | $R_a = (2.40 \text{ kip/ft})\left(\frac{30 \text{ ft}}{2}\right)$ |
| $= 46.8 \text{ kips}$ | $= 36.0 \text{ kips}$ |

Using the equation for deflection derived previously, the minimum moment of inertia, $I_x \, req$, to limit the live load deflection to 1.50 in. is:

$$I_x \, req = \frac{0.7(1.50 \text{ kip/ft})(30 \text{ ft})^4}{1{,}290(1.50 \text{ in.})}$$ (from Eq. III-1)
$$= 440 \text{ in.}^4$$

From AISC *Manual* Table 3-3, select a beam size with an adequate moment of inertia. Try a W21×55:

$$I_x = 1{,}140 \text{ in.}^4 > 440 \text{ in.}^4 \quad \textbf{o.k.}$$

From AISC *Manual* Table 6-1, for a W21×55 with $L_b = 6$ ft and $C_b = 1.0$, the available flexural strength and shear strength are determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 473 \text{ kip-ft} > 351 \text{ kip-ft} \quad \textbf{o.k.}$ | $\frac{M_n}{\Omega_b} = 314 \text{ kip-ft} > 270 \text{ kip-ft} \quad \textbf{o.k.}$ |
|  |  |
| $\phi_v V_n = 234 \text{ kips} > 46.8 \text{ kips} \quad \textbf{o.k.}$ | $\frac{V_n}{\Omega_v} = 156 \text{ kips} > 36.0 \text{ kips} \quad \textbf{o.k.}$ |

---

# III-24

## FLOOR MEMBER DESIGN AND SELECTION

Calculate dead load and live load.

Dead load:

| Slab and deck | = 57 psf |
|---------------|----------|
| Beams (est.) | = 8 psf |
| Misc. (ceiling, mechanical, etc.) | = 10 psf |
| Total | = 75 psf |

Note: The weight of the floor slab and deck was obtained from the manufacturer's literature.

Live load:

Total (can be reduced for area per ASCE/SEI 7) = 80 psf

The floor and deck will be 3 in. of normal weight concrete, $f_c' = 4$ ksi, on 3 in., 20 gage, galvanized, composite deck, laid in a pattern of three or more continuous spans. The total depth of the slab is 6 in. From the Steel Deck Institute *Floor Deck Design Manual* (SDI, 2020), the maximum unshored span for construction with this deck and a three-span condition is 10 ft 6 in. The general layout for the floor beams is 10 ft on center; therefore, the deck does not need to be shored during construction. At 10 ft on center, this deck has an allowable superimposed live load capacity of 143 psf per the manufacturer's literature. In addition, it can be shown that this deck can carry a 2,000 pound load over an area of 2.5 ft by 2.5 ft as required by ASCE/SEI 7, Section 4.4. The floor diaphragm and the floor loads extend 6 in. past the centerline of grid as shown on Sheet S4.1.

---

# III-25

## SELECT FLOOR BEAMS (COMPOSITE AND NONCOMPOSITE)

Note: There are two early and important checks in the design of composite beams. First, select a beam that either does not require camber, or establish a target camber at the start of the design process. A reasonable approximation of the camber is between $L/300$ minimum and $L/180$ maximum (or a maximum of 1½ to 2 in.).

Second, check that the beam is strong enough to safely carry the wet concrete and a 20 psf construction live load [per *Design Loads on Structures During Construction*, ASCE 37-14 (ASCE, 2019)] when designed by the ASCE/SEI 7 load combinations and the provisions of AISC *Specification* Chapter F. The 20 psf construction live load is associated with the ASCE 37-14 "very light duty" construction live load class. An increase in the construction live load will be warranted if other construction live load classes are expected during construction.

## SELECT TYPICAL 45-FT-LONG INTERIOR COMPOSITE BEAM (10 FT ON CENTER)

Find a target moment of inertia for an unshored beam.

$$w_D = (10 \text{ ft})\left(0.057 \text{ kip/ft}^2 + 0.008 \text{ kip/ft}^2\right)$$
$$= 0.650 \text{ kip/ft}$$

Hold deflection to approximately 2 in. maximum to facilitate concrete placement. Using the equation for deflection derived previously, the required moment of inertia is determined as follows:

$$I_{req} = \frac{(0.650 \text{ kip/ft})(45 \text{ ft})^4}{1{,}290(2 \text{ in.})}$$ (from Eq. III-1)
$$= 1{,}030 \text{ in.}^4$$

The construction live load is determined as follows:

$$w_L = (10 \text{ ft})\left(0.020 \text{ kip/ft}^2\right)$$
$$= 0.200 \text{ kip/ft}$$

From ASCE/SEI 7, Chapter 2, the required flexural strength due to wet concrete only is determined as follows:

| LRFD | ASD |
|------|-----|
| $w_u = 1.4(0.650 \text{ kip/ft})$ | $w_a = 0.650 \text{ kip/ft}$ |
| $= 0.910 \text{ kip/ft}$ |  |
|  |  |
| $M_u = \frac{(0.910 \text{ kip/ft})(45 \text{ ft})^2}{8}$ | $M_a = \frac{(0.650 \text{ kip/ft})(45 \text{ ft})^2}{8}$ |
| $= 230 \text{ kip-ft}$ | $= 165 \text{ kip-ft}$ |

From ASCE/SEI 7, Chapter 2, the required flexural strength due to wet concrete and construction live load is determined as follows:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.650 \text{ kip/ft}) + 1.6(0.200 \text{ kip/ft})$ | $w_a = 0.650 \text{ kip/ft} + 0.200 \text{ kip/ft}$ |
| $= 1.10 \text{ kip/ft}$ | $= 0.850 \text{ kip/ft}$ |

---

# III-26

| LRFD | ASD |
|------|-----|
| $M_u = \frac{(1.10 \text{ kip/ft})(45 \text{ ft})^2}{8}$ | $M_a = \frac{(0.850 \text{ kip/ft})(45 \text{ ft})^2}{8}$ |
| $= 278 \text{ kip-ft} \quad \textbf{controls}$ | $= 215 \text{ kip-ft} \quad \textbf{controls}$ |

Use AISC *Manual* Table 3-3 to select a beam with $I_x \geq 1{,}030 \text{ in.}^4$ Select a W21×50, with $I_x = 984 \text{ in.}^4$, close to the target value.

From AISC *Manual* Table 6-1, the available flexural strength for a fully braced, $L_b = 0$ ft, W21×50 is determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 413 \text{ kip-ft} > 278 \text{ kip-ft} \quad \textbf{o.k.}$ | $\frac{M_n}{\Omega_b} = 274 \text{ kip-ft} > 215 \text{ kip-ft} \quad \textbf{o.k.}$ |

Check for possible live load reduction due to area in accordance with ASCE/SEI 7, Section 4.7.2.

From ASCE/SEI 7, Table 4.7-1, for interior beams:

$$K_{LL} = 2$$

The beams are at 10 ft on center, therefore the tributary area is:

$$A_T = (45 \text{ ft})(10 \text{ ft})$$
$$= 450 \text{ ft}^2$$

$$K_{LL}A_T = 2\left(450 \text{ ft}^2\right)$$
$$= 900 \text{ ft}^2$$

Because $K_{LL}A_T \geq 400 \text{ ft}^2$, a reduced live load can be used.

From ASCE/SEI 7, Equation 4.7-1:

$$L = L_o\left(0.25 + \frac{15}{\sqrt{K_{LL}A_T}}\right) \geq 0.50L_o$$

$$= (80 \text{ psf})\left(0.25 + \frac{15}{\sqrt{900 \text{ ft}^2}}\right) > 0.50(80 \text{ psf})$$

$$= 60.0 \text{ psf} > 40.0 \text{ psf}$$

Therefore, use $L = 60.0$ psf.

The beams are at 10 ft on center, therefore the loading is as shown in Figure III-9. Note, the beam is continuously braced by the deck.

From ASCE/SEI 7, Chapter 2, the required strengths are determined as follows:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.750 \text{ kip/ft}) + 1.6(0.600 \text{ kip/ft})$ | $w_a = 0.750 \text{ kip/ft} + 0.600 \text{ kip/ft}$ |
| $= 1.86 \text{ kip/ft}$ | $= 1.35 \text{ kip/ft}$ |

---

# III-27

| LRFD | ASD |
|------|-----|
| $R_u = (1.86 \text{ kip/ft})\left(\frac{45 \text{ ft}}{2}\right)$ | $R_a = (1.35 \text{ kip/ft})\left(\frac{45 \text{ ft}}{2}\right)$ |
| $= 41.9 \text{ kips}$ | $= 30.4 \text{ kips}$ |
|  |  |
| $M_u = \frac{(1.86 \text{ kip/ft})(45 \text{ ft})^2}{8}$ | $M_a = \frac{(1.35 \text{ kip/ft})(45 \text{ ft})^2}{8}$ |
| $= 471 \text{ kip-ft}$ | $= 342 \text{ kip-ft}$ |

The available flexural strength for the composite beam is determined using AISC *Manual* Part 3. Assume initially that $a = 1$ in.

$$Y2 = Y_{con} - \frac{a}{2}$$ (*Manual* Eq. 3-6)
$$= 6.00 \text{ in.} - \frac{1 \text{in.}}{2}$$
$$= 5.50 \text{ in.}$$

Enter AISC *Manual* Table 3-18 for a W21×50 with $Y2 = 5.50$ in. Selecting PNA location 7, with $\Sigma Q_n = 184$ kips, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 598 \text{ kip-ft} > 471 \text{ kip-ft} \quad \textbf{o.k.}$ | $\frac{M_n}{\Omega_b} = 398 \text{ kip-ft} > 342 \text{ kip-ft} \quad \textbf{o.k.}$ |

*Determine effective width, b*

The effective width of the concrete slab is the sum of the effective widths for each side of the beam centerline as determined by the minimum value of the three widths set forth in AISC *Specification* Section I3.1a:

1. one-eighth of the span of the beam, center-to-center of the supports

$$\left(\frac{45 \text{ ft}}{8}\right)(2 \text{ sides}) = 11.3 \text{ ft}$$

![Loading diagram showing:
- Distributed loads: wD = 0.750 kip/ft, wL = 0.600 kip/ft
- Simply supported beam with continuous bracing
- Span: 45'-0"
- Support points labeled A and C]

*Fig. III-9. Loading and bracing diagram for typical interior composite floor beams.*

---

# III-28

2. one-half the distance to the centerline of the adjacent beam

$$\left(\frac{10 \text{ ft}}{2}\right)(2 \text{ sides}) = 10.0 \text{ ft} \quad \textbf{controls}$$

3. distance to the edge of the slab

The latter is not applicable for an interior member.

*Determine the height of the compression block, a*

$$a = \frac{\Sigma Q_n}{0.85f_c'b}$$ (*Manual* Eq. 3-7)

$$= \frac{184 \text{ kips}}{0.85(4 \text{ ksi})(10 \text{ ft})(12 \text{ in./ft})}$$

$$= 0.451 \text{ in.} < 1.00 \text{ in.} \quad \textbf{o.k.}$$

From AISC *Manual* Table 6-1, the available shear strength of the W21×50 bare steel beam is determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi_v V_n = 237 \text{ kips} > 41.9 \text{ kips} \quad \textbf{o.k.}$ | $\frac{V_n}{\Omega_v} = 158 \text{ kips} > 30.4 \text{ kips} \quad \textbf{o.k.}$ |

*Check live load deflection*

$$\frac{L}{360} = \frac{(45 \text{ ft})(12 \text{ in./ft})}{360}$$
$$= 1.50 \text{ in.}$$

Entering AISC *Manual* Table 3-19 for a W21×50, with PNA location 7 and $Y2 = 5.50$ in., provides a lower bound moment of inertia of $I_{LB} = 1{,}730 \text{ in.}^4$ From the equation previously derived, the live load deflection is determined as follows:

$$\Delta_{LL} = \frac{w_L L^4}{1{,}290I_{LB}}$$ (from Eq. III-1)

$$= \frac{(0.600 \text{ kip/ft})(45 \text{ ft})^4}{1{,}290\left(1{,}730 \text{ in.}^4\right)}$$

$$= 1.10 \text{ in.} < 1.50 \text{ in.} \quad \textbf{o.k.}$$

From AISC Design Guide 3, limit the live load deflection using 50% of the (unreduced) design live load, to $L/360$ with a maximum absolute value of 1 in. across the bay. From the equation previously derived, the deflection is determined as follows:

$$\Delta_{LL} = \frac{0.5(0.800 \text{ kip/ft})(45 \text{ ft})^4}{1{,}290\left(1{,}730 \text{ in.}^4\right)} \leq 1 \text{ in.}$$ (from Eq. III-1)

$$= 0.735 \text{ in.} < 1 \text{ in.}$$
$$= 0.735 \text{ in.}$$

$1 \text{ in.} - 0.735 \text{ in.} = 0.265 \text{ in.}$

---

# III-29

Note: Limit the supporting girders to 0.265 in. deflection under the same load case at the connection point of the beam.

*Determine the required number of shear stud connectors*

From AISC *Manual* Table 3-20, using perpendicular deck with one ¾-in.-diameter anchor per rib in normal weight concrete with $f_c' = 4$ ksi in the weak position:

$$Q_n = 17.2 \text{ kips/anchor}$$

$$n = \frac{\Sigma Q_n}{Q_n}$$

$$= \frac{184 \text{ kips}}{17.2 \text{ kips/anchor}}$$

$$= 10.7 \text{ anchors (on each side of maximum moment)}$$

Therefore, 22 studs are required to satisfy strength requirements. However, per AISC *Specification* Commentary Section I3.2d.1, 44 studs are specified to provide sufficient deformation capacity by ensuring a degree of composite action of at least 50%.

From AISC Design Guide 3, limit the wet concrete deflection in a bay to $L/360$, not to exceed 1 in. From the equation previously derived, the wet concrete deflection is determined as follows:

$$\Delta_{DL(wet \, conc)} = \frac{(0.650 \text{ kip/ft})(45 \text{ ft})^4}{1{,}290\left(984 \text{ in.}^4\right)}$$ (from Eq. III-1)

$$= 2.10 \text{ in.}$$

Camber the beam for 80% of the calculated wet deflection.

$$Camber = 0.80(2.10 \text{ in.})$$
$$= 1.68 \text{ in.}$$

Round the calculated value down to the nearest ¼ in.; therefore, specify 1½ in. of camber.

$$2.10 \text{ in.} - 1\frac{1}{2} \text{ in.} = 0.600 \text{ in.}$$

$$1 \text{ in.} - 0.600 \text{ in.} = 0.400 \text{ in.}$$

Note: Limit the supporting girders to 0.400 in. deflection under the same load combination at the connection point of the beam.

---

# III-30

## SELECT TYPICAL 30 FT INTERIOR COMPOSITE (OR NONCOMPOSITE) BEAM (10 FT ON CENTER)

Find a target moment of inertia for an unshored beam.

Determine the required strength to carry wet concrete and construction live load. The dead load from the slab and deck is:

$$w_D = (10 \text{ ft})\left(0.057 \text{ kip/ft}^2 + 0.008 \text{ kip/ft}^2\right)$$
$$= 0.650 \text{ kip/ft}$$

Hold deflection to 1½ in. maximum to facilitate concrete placement. Using the equation for deflection derived previously, the required moment of inertia is determined as follows:

$$I_{req} = \frac{(0.650 \text{ kip/ft})(30 \text{ ft})^4}{1{,}290(1\frac{1}{2} \text{ in.})}$$ (from Eq. III-1)

$$= 272 \text{ in.}^4$$

The construction live load is:

$$w_L = (10 \text{ ft})\left(0.020 \text{ kip/ft}^2\right)$$
$$= 0.200 \text{ kip/ft}$$

From ASCE/SEI 7, Chapter 2, determine the required flexural strength due to wet concrete only.

| LRFD | ASD |
|------|-----|
| $w_u = 1.4(0.650 \text{ kip/ft})$ | $w_a = 0.650 \text{ kip/ft}$ |
| $= 0.910 \text{ kip/ft}$ |  |
|  |  |
| $M_u = \frac{(0.910 \text{ kip/ft})(30 \text{ ft})^2}{8}$ | $M_a = \frac{(0.650 \text{ kip/ft})(30 \text{ ft})^2}{8}$ |
| $= 102 \text{ kip-ft}$ | $= 73.1 \text{ kip-ft}$ |

From ASCE/SEI 7, Chapter 2, determine the required flexural strength due to wet concrete and construction live load.

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.650 \text{ kip/ft}) + 1.6(0.200 \text{ kip/ft})$ | $w_a = 0.650 \text{ kip/ft} + 0.200 \text{ kip/ft}$ |
| $= 1.10 \text{ kip/ft}$ | $= 0.850 \text{ kip/ft}$ |
|  |  |
| $M_u = \frac{(1.10 \text{ kip/ft})(30 \text{ ft})^2}{8}$ | $M_a = \frac{(0.850 \text{ kip/ft})(30 \text{ ft})^2}{8}$ |
| $= 124 \text{ kip-ft} \quad \textbf{controls}$ | $= 95.6 \text{ kip-ft} \quad \textbf{controls}$ |

Use AISC *Manual* Table 3-3 to find a beam with an $I_x \geq 272 \text{ in.}^4$ Select a W16×26, with $I_x = 301 \text{ in.}^4$, which exceeds the target value.

From AISC *Manual* Table 6-1, the available flexural strength for a fully braced, $L_b = 0$ ft, W16×26 is determined as follows:

---

# III-31

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 166 \text{ kip-ft} > 124 \text{ kip-ft} \quad \textbf{o.k.}$ | $\frac{M_n}{\Omega_b} = 110 \text{ kip-ft} > 95.6 \text{ kip-ft} \quad \textbf{o.k.}$ |

Check for possible live load reduction due to area in accordance with ASCE/SEI 7, Section 4.7.2.

From ASCE/SEI 7, Table 4.7-1, for interior beams:

$$K_{LL} = 2$$

The beams are at 10 ft on center, therefore the tributary area is:

$$A_T = (30 \text{ ft})(10 \text{ ft})$$
$$= 300 \text{ ft}^2$$

$$K_{LL}A_T = 2\left(300 \text{ ft}^2\right)$$
$$= 600 \text{ ft}^2$$

Because $K_{LL}A_T \geq 400 \text{ ft}^2$, a reduced live load can be used.

From ASCE/SEI 7, Equation 4.7-1:

$$L = L_o\left(0.25 + \frac{15}{\sqrt{K_{LL}A_T}}\right) \geq 0.50L_o$$

$$= (80 \text{ psf})\left(0.25 + \frac{15}{\sqrt{600 \text{ ft}^2}}\right) > 0.50(80 \text{ psf})$$

$$= 69.0 \text{ psf} > 40.0 \text{ psf}$$

Therefore, use $L = 69.0$ psf.

The beams are at 10 ft on center, therefore the loading is as shown in Figure III-10.

![Loading diagram showing:
- Distributed loads: wD = 0.750 kip/ft, wL = 0.690 kip/ft
- Simply supported beam with continuous bracing
- Span: 30'-0"
- Support points labeled C and D]

*Fig. III-10. Loading and bracing diagram for typical 30 ft interior floor beams.*

---

# III-32

From ASCE/SEI 7, Chapter 2, calculate the required strength.

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.750 \text{ kip/ft}) + 1.6(0.690 \text{ kip/ft})$ | $w_a = 0.750 \text{ kip/ft} + 0.690 \text{ kip/ft}$ |
| $= 2.00 \text{ kip/ft}$ | $= 1.44 \text{ kip/ft}$ |
|  |  |
| $R_u = (2.00 \text{ kip/ft})\left(\frac{30 \text{ ft}}{2}\right)$ | $R_a = (1.44 \text{ kip/ft})\left(\frac{30 \text{ ft}}{2}\right)$ |
| $= 30.0 \text{ kips}$ | $= 21.6 \text{ kips}$ |
|  |  |
| $M_u = \frac{(2.00 \text{ kip/ft})(30 \text{ ft})^2}{8}$ | $M_a = \frac{(1.44 \text{ kip/ft})(30 \text{ ft})^2}{8}$ |
| $= 225 \text{ kip-ft}$ | $= 162 \text{ kip-ft}$ |

The available flexural strength for the composite beam is determined from AISC *Manual* Part 3 as follows. Assume initially that $a = 1$ in.

$$Y2 = Y_{con} - \frac{a}{2}$$ (*Manual* Eq. 3-6)

$$= 6.00 \text{ in.} - \frac{1 \text{ in.}}{2}$$

$$= 5.50 \text{ in.}$$

Enter AISC *Manual* Table 3-18 for a W16×26 with $Y2 = 5.50$ in. Selecting PNA location 7, with $\Sigma Q_n = 96.0$ kips, the available flexural strength is:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 248 \text{ kip-ft} > 225 \text{ kip-ft} \quad \textbf{o.k.}$ | $\frac{M_n}{\Omega_b} = 165 \text{ kip-ft} > 162 \text{ kip-ft} \quad \textbf{o.k.}$ |

*Determine effective width, b*

The effective width of the concrete slab is the sum of the effective widths for each side of the beam centerline as determined by the minimum value of the three widths set forth in AISC *Specification* Section I3.1a:

1. one-eighth of the span of the beam, center-to-center of the supports

$$\left(\frac{30 \text{ ft}}{8}\right)(2 \text{ sides}) = 7.50 \text{ ft} \quad \textbf{controls}$$

2. one-half the distance to the centerline of the adjacent beam

$$\left(\frac{10 \text{ ft}}{2}\right)(2 \text{ sides}) = 10.0 \text{ ft}$$

3. distance to the edge of the slab

The latter is not applicable for an interior member.

---

# III-33

*Determine the height of the compression block, a*

$$a = \frac{\Sigma Q_n}{0.85f_c'b}$$ (*Manual* Eq. 3-7)

$$= \frac{96.0 \text{ kips}}{0.85(4 \text{ ksi})(7.50 \text{ ft})(12 \text{ in./ft})}$$

$$= 0.314 \text{ in.} < 1.00 \text{ in.} \quad \textbf{o.k.}$$

From AISC *Manual* Table 6-1, the available shear strength of the W16×26 bare steel beam is determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi_v V_n = 106 \text{ kips} > 30.0 \text{ kips} \quad \textbf{o.k.}$ | $\frac{V_n}{\Omega_v} = 70.5 \text{ kips} > 21.6 \text{ kips} \quad \textbf{o.k.}$ |

*Check live load deflection*

$$\frac{L}{360} = \frac{(30 \text{ ft})(12 \text{ in./ft})}{360}$$
$$= 1.00 \text{ in.}$$

Entering AISC *Manual* Table 3-19 for a W16×26, with PNA location 7 and $Y2 = 5.50$ in., provides a lower bound moment of inertia of $I_{LB} = 575 \text{ in.}^4$ From the equation previously derived, the live load deflection is determined as follows:

$$\Delta_{LL} = \frac{w_L L^4}{1{,}290I_{LB}}$$ (from Eq. III-1)

$$= \frac{(0.690 \text{ kip/ft})(30 \text{ ft})^4}{1{,}290\left(575 \text{ in.}^4\right)}$$

$$= 0.753 \text{ in.} < 1.00 \text{ in.} \quad \textbf{o.k.}$$

From AISC Design Guide 3, limit the live load deflection, using 50% of the (unreduced) design live load, to $L/360$ with a maximum absolute value of 1 in. across the bay. From the equation previously derived, the deflection is determined as follows:

$$\Delta_{LL} = \frac{0.5(0.800 \text{ kip/ft})(30 \text{ ft})^4}{1{,}290\left(575 \text{ in.}^4\right)}$$ (from Eq. III-1)

$$= 0.437 \text{ in.} < 1 \text{ in.} \quad \textbf{o.k.}$$

$1 \text{ in.} - 0.437 \text{ in.} = 0.563 \text{ in.}$

Note: Limit the supporting girders to 0.563 in. deflection under the same load combination at the connection point of the beam.

*Determine the required number of shear stud connectors*

From AISC *Manual* Table 3-20, using perpendicular deck with one ¾-in.-diameter anchor per rib in normal weight concrete with $f_c' = 4$ ksi in the weak position:

$$Q_n = 17.2 \text{ kips/anchor}$$

---

# III-34

$$n = \frac{\Sigma Q_n}{Q_n}$$

$$= \frac{96.0 \text{ kips}}{17.2 \text{ kips/anchor}}$$

$$= 5.58 \text{ anchors (on each side of maximum moment)}$$

Note: Per AISC *Specification* Section I8.2d, there is a maximum spacing limit of 8(6 in.) = 48 in. (not to exceed 36 in.) between anchors.

Therefore use 12 anchors, uniformly spaced at no more than 36 in. on center. Per AISC *Specification* Commentary Section I3.2d.1, beams with spans not exceeding 30 ft are not susceptible to connector failure due to insufficient connector deformation capacity.

Note: Although the studs may be placed up to 36 in. on center, the steel deck must still be anchored to the supporting member at a spacing not to exceed 18 in. per AISC *Specification* Section I3.2c.

From AISC Design Guide 3, limit the wet concrete deflection in a bay to $L/360$, not to exceed 1 in. From the equation previously derived, the wet concrete deflection is determined as follows:

$$\Delta_{DL(wet \, conc)} = \frac{(0.650 \text{ kip/ft})(30 \text{ ft})^4}{1{,}290\left(301 \text{ in.}^4\right)}$$ (from Eq. III-1)

$$= 1.36 \text{ in.}$$

Camber the beam for 80% of the calculated wet concrete dead load deflection.

$$Camber = 0.80(1.36 \text{ in.})$$
$$= 1.09 \text{ in.}$$

Round the calculated value down to the nearest ¼ in. Therefore, specify 1 in. of camber.

$1.36 \text{ in.} - 1 \text{ in.} = 0.360 \text{ in.}$

$1.00 \text{ in.} - 0.360 \text{ in.} = 0.640 \text{ in.}$

Note: Limit the supporting girders to 0.640 in. deflection under the same load combination at the connection point of the beam.

This beam could also be designed as a noncomposite beam.

Try a W18×35. From AISC *Manual* Table 6-1, the available flexural strength for a fully braced beam, $L_b = 0$ ft, and shear strength are determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 249 \text{ kip-ft} > 225 \text{ kip-ft} \quad \textbf{o.k.}$ | $\frac{M_n}{\Omega_b} = 166 \text{ kip-ft} > 162 \text{ kip-ft} \quad \textbf{o.k.}$ |
|  |  |
| $\phi_v V_n = 159 \text{ kips} > 30.0 \text{ kips} \quad \textbf{o.k.}$ | $\frac{V_n}{\Omega_v} = 106 \text{ kips} > 21.6 \text{ kips} \quad \textbf{o.k.}$ |

---

# III-35

*Check beam deflections*

Check live load deflection. From AISC *Manual* Table 3-3 for a W18×35:

$$I_x = 510 \text{ in.}^4$$

$$\Delta_{LL} = \frac{(0.690 \text{ kip/ft})(30 \text{ ft})^4}{1{,}290\left(510 \text{ in.}^4\right)}$$ (from Eq. III-1)

$$= 0.850 \text{ in.} < 1 \text{ in.} \quad \textbf{o.k.}$$

Based on AISC Design Guide 3, limit the live load deflection, using 50% of the (unreduced) design live load, to $L/360$ with a maximum absolute value of 1 in. across the bay. From the equation previously derived, the deflection is determined as follows:

$$\Delta_{LL} = \frac{0.5(0.800 \text{ kip/ft})(30 \text{ ft})^4}{1{,}290\left(510 \text{ in.}^4\right)}$$ (from Eq. III-1)

$$= 0.492 \text{ in.} < 1 \text{ in.} \quad \textbf{o.k.}$$

$1 \text{ in.} - 0.492 \text{ in.} = 0.508 \text{ in.}$

Note: Limit the supporting girders to 0.508 in. deflection under the same load combination at the connection point of the beam.

Note: Because this beam is stronger than the W16×26 composite beam, no wet concrete strength checks are required in this example.

From AISC Design Guide 3, limit the wet concrete deflection in a bay to $L/360$, not to exceed 1 in. From the equation previously derived, the wet concrete deflection is determined as follows:

$$\Delta_{DL(wet \, conc)} = \frac{(0.650 \text{ kip/ft})(30 \text{ ft})^4}{1{,}290\left(510 \text{ in.}^4\right)}$$ (from Eq. III-1)

$$= 0.800 \text{ in.} < 1 \text{ in.} \quad \textbf{o.k.}$$

Camber the beam for 80% of the calculated wet concrete deflection.

$$Camber = 0.80(0.800 \text{ in.})$$
$$= 0.640 \text{ in.}$$

A good break point to eliminate camber is ⅝ in.; therefore, do not specify a camber for this beam.

$1 \text{ in.} - 0.800 \text{ in.} = 0.200 \text{ in.}$

Note: Limit the supporting girders to 0.200 in. deflection under the same load case at the connection point of the beam.

Therefore, selecting a W18×35 will eliminate both shear studs and cambering. The cost of the extra steel weight may be offset by the elimination of studs and cambering. Local labor and material costs should be checked to make this determination.

---

# III-36

## SELECT TYPICAL NORTH-SOUTH EDGE BEAM

The influence area, $K_{LL}A_T$, for these beams is less than 400 ft²; therefore, no live load reduction can be taken per ASCE/SEI 7, Section 4.7.2.

These beams carry 5.5 ft of dead load and live load as well as a wall load.

The floor dead load is:

$$w = (5.5 \text{ ft})\left(0.075 \text{ kip/ft}^2\right)$$
$$= 0.413 \text{ kip/ft}$$

Use 65 psf for the initial dead load due to the wet concrete:

$$w_{D(initial)} = (5.5 \text{ ft})\left(0.065 \text{ kip/ft}^2\right)$$
$$= 0.358 \text{ kip/ft}$$

Use 10 psf for the superimposed dead load:

$$w_{D(super)} = (5.5 \text{ ft})\left(0.010 \text{ kip/ft}^2\right)$$
$$= 0.055 \text{ kip/ft}$$

The dead load of the wall system at the floor is:

$$w = (7.50 \text{ ft})\left(0.055 \text{ kip/ft}^2\right) + (6.00 \text{ ft})\left(0.015 \text{ kip/ft}^2\right)$$
$$= 0.413 \text{ kip/ft} + 0.090 \text{ kip/ft}$$
$$= 0.503 \text{ kip/ft}$$

The total dead load is:

$$w_D = 0.413 \text{ kip/ft} + 0.503 \text{ kip/ft}$$
$$= 0.916 \text{ kip/ft}$$

The live load is:

$$w_L = (5.5 \text{ ft})\left(0.080 \text{ kip/ft}^2\right)$$
$$= 0.440 \text{ kip/ft}$$

Beam loading is shown in Figure III-11.

Calculate the required strengths from ASCE/SEI 7, Chapter 2:

| LRFD | ASD |
|------|-----|
| $w_u = 1.2(0.916 \text{ kip/ft}) + 1.6(0.440 \text{ kip/ft})$ | $w_a = 0.916 \text{ kip/ft} + 0.440 \text{ kip/ft}$ |
| $= 1.80 \text{ kip/ft}$ | $= 1.36 \text{ kip/ft}$ |

---

# III-37

| LRFD | ASD |
|------|-----|
| $R_u = (1.80 \text{ kip/ft})\left(\frac{22.5 \text{ ft}}{2}\right)$ | $R_a = (1.36 \text{ kip/ft})\left(\frac{22.5 \text{ ft}}{2}\right)$ |
| $= 20.3 \text{ kips}$ | $= 15.3 \text{ kips}$ |
|  |  |
| $M_u = \frac{(1.80 \text{ kip/ft})(22.5 \text{ ft})^2}{8}$ | $M_a = \frac{(1.36 \text{ kip/ft})(22.5 \text{ ft})^2}{8}$ |
| $= 114 \text{ kip-ft}$ | $= 86.1 \text{ kip-ft}$ |

Because these beams are less than 25 ft long, they will be most efficient as noncomposite beams. The beams at the edges of the building carry a brick spandrel panel. For these beams, the cladding weight exceeds 25% of the total dead load on the beam. From AISC Design Guide 3, limit the vertical deflection due to cladding and initial dead load to $L/600$ or ⅝ in. maximum. In addition, because these beams are supporting brick above and there is continuous glass below, limit the superimposed dead and live load deflection to $L/600$ or 0.3 in. maximum to accommodate the brick and $L/360$ or ¼ in. maximum to accommodate the glass. Therefore, combining the two limitations, limit the superimposed dead and live load deflection to ¼ in. The superimposed dead load includes all of the dead load that is applied after the cladding has been installed. Note that it is typically not recommended to camber beams supporting spandrel panels.

Using the equation for deflection derived previously, the minimum moment of inertia, $I_x \, req$, to limit the superimposed dead and live load deflection to ¼ in.

$$I_x \, req = \frac{(0.055 \text{ kip/ft} + 0.440 \text{ kip/ft})(22.5 \text{ ft})^4}{1{,}290(\frac{1}{4} \text{ in.})}$$ (from Eq. III-1)

$$= 393 \text{ in.}^4$$

Using the equation for deflection derived previously, the minimum moment of inertia, $I_x \, req$, to limit the cladding and initial dead load deflection to ⅝ in.

$$I_x \, req = \frac{(0.358 \text{ kip/ft} + 0.503 \text{ kip/ft})(22.5 \text{ ft})^4}{1{,}290(\frac{5}{8} \text{ in.})}$$ (from Eq. III-1)

$$= 456 \text{ in.}^4 \quad \textbf{controls}$$

From AISC *Manual* Table 3-3, find a beam with $I_x \geq 456 \text{ in.}^4$ Select a W18×35 with $I_x = 510 \text{ in.}^4$

![Loading diagram showing:
- Distributed loads: wD = 0.916 kip/ft, wL = 0.440 kip/ft
- Simply supported beam with continuous bracing
- Span: 22'-6"
- Support points labeled D and E]

*Fig. III-11. Loading and bracing diagram for typical north-south floor beams.*

---

# III-38

From AISC *Manual* Table 6-1, the available flexural strength for a fully braced beam, $L_b = 0$ ft, and shear strength are determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 249 \text{ kip-ft} > 114 \text{ kip-ft} \quad \textbf{o.k.}$ | $\frac{M_n}{\Omega_b} = 166 \text{ kip-ft} > 86.1 \text{ kip-ft} \quad \textbf{o.k.}$ |
|  |  |
| $\phi_v V_n = 159 \text{ kips} > 20.3 \text{ kips} \quad \textbf{o.k.}$ | $\frac{V_n}{\Omega_v} = 106 \text{ kips} > 15.3 \text{ kips} \quad \textbf{o.k.}$ |

---

# III-39

## SELECT TYPICAL EAST-WEST EDGE GIRDER

The beams along the sides of the building carry the brick spandrel panel and glass, and dead load and live load from the intermediate floor beams. For these beams, the cladding weight exceeds 25% of the total dead load on the beam. Therefore, per AISC Design Guide 3, limit the vertical deflection due to cladding and initial dead load to $L/600$ or ⅝ in. maximum. In addition, because these beams are supporting brick above and there is continuous glass below, limit the superimposed dead and live load deflection to $L/600$ or 0.3 in. maximum to accommodate the brick and $L/360$ or ¼ in. maximum to accommodate the glass. Therefore, combining the two limitations, limit the superimposed dead and live load deflection to $L/600$ or ¼ in. The superimposed dead load includes all of the dead load that is applied after the cladding has been installed. These beams will be part of the moment frames on the north and south sides of the building and therefore will be designed as fixed at both ends.

Establish the loading.

The dead load reaction from the floor beams is:

$$P_D = (0.750 \text{ kip/ft})\left(\frac{45 \text{ ft}}{2}\right)$$
$$= 16.9 \text{ kips}$$

$$P_{D(initial)} = (0.650 \text{ kip/ft})\left(\frac{45 \text{ ft}}{2}\right)$$
$$= 14.6 \text{ kips}$$

$$P_{D(super)} = (0.100 \text{ kip/ft})\left(\frac{45 \text{ ft}}{2}\right)$$
$$= 2.25 \text{ kips}$$

The uniform dead load along the beam is:

$$w_D = (0.5 \text{ ft})\left(0.075 \text{ kip/ft}^2\right) + 0.503 \text{ kip/ft}$$
$$= 0.541 \text{ kip/ft}$$

$$w_{D(initial)} = (0.5 \text{ ft})\left(0.065 \text{ kip/ft}^2\right)$$
$$= 0.033 \text{ kip/ft}$$

$$w_{D(super)} = (0.5 \text{ ft})\left(0.010 \text{ kip/ft}^2\right)$$
$$= 0.005 \text{ kip/ft}$$

Select typical 30 ft composite (or noncomposite) girders.

Check for possible live load reduction due to area in accordance with ASCE/SEI 7, Section 4.7.2.

From ASCE/SEI 7, Table 4.7-1, for edge beams with cantilevered slabs:

$$K_{LL} = 1$$

However, it is also permissible to calculate the value of $K_{LL}$ based upon influence area. Because the cantilever dimension is small, $K_{LL}$ will be closer to 2 than 1. The calculated value of $K_{LL}$ based upon the influence area is:

---

# III-40

$$K_{LL} = \frac{(45.5 \text{ ft})(30 \text{ ft})}{\left(\frac{45 \text{ ft}}{2} + 0.5 \text{ ft}\right)(30 \text{ ft})}$$

$$= 1.98$$

$$A_T = (30 \text{ ft})(22.5 \text{ ft} + 0.5 \text{ ft})$$
$$= 690 \text{ ft}^2$$

From ASCE/SEI 7, Equation 4.7-1:

$$L = L_o\left(0.25 + \frac{15}{\sqrt{K_{LL}A_T}}\right) \geq 0.50L_o$$

$$= (80 \text{ psf})\left(0.25 + \frac{15}{\sqrt{1.98\left(690 \text{ ft}^2\right)}}\right) > 0.50(80 \text{ psf})$$

$$= 52.5 \text{ psf} > 40.0 \text{ psf}$$

Therefore, use $L = 52.5$ psf.

The live load from the floor beams is:

$$P_L = (0.525 \text{ kip/ft})\left(\frac{45 \text{ ft}}{2}\right)$$
$$= 11.8 \text{ kips}$$

The uniform live load along the beam is:

$$w_L = (0.5 \text{ ft})\left(0.0525 \text{ kip/ft}^2\right)$$
$$= 0.0263 \text{ kip/ft}$$

The loading diagram is shown in Figure III-12.

![Loading and bracing diagram showing:
- Distributed loads: wD = 0.541 kip/ft, wL = 0.0263 kip/ft
- Concentrated loads: PD = 16.9 kips, PL = 11.8 kips at center
- Beam with continuous bracing on top flange, at ends and third points on bottom flange
- Span: 30'-0"
- Support points labeled 2 and 3]

*Fig. III-12. Loading and bracing diagram for typical east-west edge girders.*

---

# III-41

The required moment and end reactions at the floor side beams are determined from a structural analysis of a fixed-end beam and summarized as follows:

| LRFD | ASD |
|------|-----|
| Typical side beam: | Typical side beam: |
|  |  |
| $R_u = 49.5$ kips | $R_a = 37.2$ kips |
|  |  |
| $M_u$ (at ends) $= 313$ kip-ft | $M_a$ (at ends) $= 234$ kip-ft |
|  |  |
| $M_u$ (at center) $= 156$ kip-ft | $M_a$ (at center) $= 117$ kip-ft |

The maximum moment occurs at the support with compression in the bottom flange. The bottom flange is laterally braced at 10 ft on center by the intermediate beams.

Note: During concrete placement, because the deck is parallel to the beam, the beam will not have continuous lateral support. It will be braced at 10 ft on center by the intermediate beams. By inspection, this condition will not control because the maximum moment under full loading causes compression in the bottom flange, which is braced at 10 ft on center.

| LRFD | ASD |
|------|-----|
| Calculate $C_b$ for compression in the bottom flange braced at 10 ft on center. | Calculate $C_b$ for compression in the bottom flange braced at 10 ft on center. |
|  |  |
| $C_b = 2.21$ (from computer output) | $C_b = 2.22$ (from computer output) |
|  |  |
| Select a W21×44. | Select a W21×44. |
|  |  |
| With continuous bracing, $L_b = 0$ ft, from AISC *Manual* Table 6-1: | With continuous bracing, $L_b = 0$ ft, from AISC *Manual* Table 6-1: |
|  |  |
| $\phi_b M_n = 358 \text{ kip-ft} > 156 \text{ kip-ft} \quad \textbf{o.k.}$ | $\frac{M_n}{\Omega_b} = 238 \text{ kip-ft} > 117 \text{ kip-ft} \quad \textbf{o.k.}$ |
|  |  |
| From AISC *Manual* Table 6-1 with $L_b = 10$ ft and $C_b = 2.21$: | From AISC *Manual* Table 6-1 with $L_b = 10$ ft and $C_b = 2.22$: |
|  |  |
| $\phi_b M_n C_b = (264 \text{ kip-ft})(2.21)$ | $\frac{M_n}{\Omega_b}C_b = (176 \text{ kip-ft})(2.22)$ |
| $= 583 \text{ kip-ft}$ | $= 391 \text{ kip-ft}$ |
|  |  |
| From AISC *Specification* Section F2.2, the nominal flexural strength is limited to $M_p$: | From AISC *Specification* Section F2.2, the nominal flexural strength is limited to $M_p$: |
|  |  |
| $\phi_b M_n \leq \phi_b M_p$ | $\frac{M_n}{\Omega_b} \leq \frac{M_p}{\Omega_b}$ |
| $583 \text{ kip-ft} > 358 \text{ kip-ft}$ | $391 \text{ kip-ft} > 238 \text{ kip-ft}$ |
|  |  |
| Therefore: | Therefore: |
|  |  |
| $\phi_b M_n = 358 \text{ kip-ft} > 313 \text{ kip-ft} \quad \textbf{o.k.}$ | $\frac{M_n}{\Omega_b} = 238 \text{ kip-ft} > 234 \text{ kip-ft} \quad \textbf{o.k.}$ |

---

# III-42

From AISC *Manual* Table 6-1, the available shear strength is determined as follows:

| LRFD | ASD |
|------|-----|
| $\phi_v V_n = 217 \text{ kips} > 49.5 \text{ kips} \quad \textbf{o.k.}$ | $\frac{V_n}{\Omega_v} = 145 \text{ kips} > 37.2 \text{ kips} \quad \textbf{o.k.}$ |

Deflections are determined from a structural analysis of a fixed-end beam. For deflection due to cladding and initial dead load:

$$\Delta = 0.295 \text{ in.} < \frac{5}{8} \text{ in.} \quad \textbf{o.k.}$$

For deflection due to superimposed dead and live loads:

$$\Delta = 0.212 \text{ in.} < \frac{1}{4} \text{ in.} \quad \textbf{o.k.}$$

Note that both of the deflection criteria stated previously for the girder and for the locations on the girder where the floor beams are supported have also been met.

Also, as noted previously, it is not typically recommended to camber beams supporting spandrel panels. The W21×44 is adequate for strength and deflection, but may be increased in size to help with moment frame strength or drift control.

---

# III-43

## SELECT TYPICAL EAST-WEST INTERIOR GIRDER

*Establish loads*

The dead load reaction from the floor beams is:

$$P_D = (0.750 \text{ kip/ft})\left(\frac{45 \text{ ft} + 30 \text{ ft}}{2}\right)$$
$$= 28.1 \text{ kips}$$

Check for live load reduction due to area in accordance with ASCE/SEI 7, Section 4.7.2.

From ASCE/SEI 7, Table 4.7-1, for interior beams:

$$K_{LL} = 2$$

$$A_T = (30 \text{ ft})\left(\frac{45 \text{ ft} + 30 \text{ ft}}{2}\right)$$
$$= 1{,}130 \text{ ft}^2$$

Using ASCE/SEI 7, Equation 4.7-1:

$$L = L_o\left(0.25 + \frac{15}{\sqrt{K_{LL}A_T}}\right) \geq 0.50L_o$$

$$= (80 \text{ psf})\left(0.25 + \frac{15}{\sqrt{(2)\left(1{,}130 \text{ ft}^2\right)}}\right) \geq 0.50(80 \text{ psf})$$

$$= 45.2 \text{ psf} > 40.0 \text{ psf}$$

Therefore, use $L = 45.2$ psf.

The live load from the floor beams is:

$$P_L = \left(0.0452 \text{ kip/ft}^2\right)\left(\frac{45 \text{ ft} + 30 \text{ ft}}{2}\right)(10 \text{ ft})$$
$$= 17.0 \text{ kips}$$

The loading is shown in Figure III-13.

![Loading and bracing diagram showing:
- Concentrated loads: PD = 28.1 kips, PL = 17.0 kips at center
- Beam with continuous bracing
- Span: 30'-0"
- Support points labeled 2 and 3]

*Fig. III-13. Loading and bracing diagram for typical interior girder.*

---

# III-44

Note: The dead load for this beam is included in the assumed overall dead load.

From ASCE/SEI 7, Chapter 2, the required strengths are determined as follows:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(28.1 \text{ kips}) + 1.6(17.0 \text{ kips})$ | $R_a = 28.1 \text{ kips} + 17.0 \text{ kips}$ |
| $= 60.9 \text{ kips}$ | $= 45.1 \text{ kips}$ |
|  |  |
| $M_u = (60.9 \text{ kips})(10 \text{ ft})$ | $M_a = (45.1 \text{ kips})(10 \text{ ft})$ |
| $= 609 \text{ kip-ft}$ | $= 451 \text{ kip-ft}$ |

Check for beam requirements when carrying wet concrete. Limit wet concrete deflection to 1½ in.

$$P_D = (0.650 \text{ kip/ft})\left(\frac{45 \text{ ft} + 30 \text{ ft}}{2}\right)$$
$$= 24.4 \text{ kips}$$

$$P_L = (0.200 \text{ kip/ft})\left(\frac{45 \text{ ft} + 30 \text{ ft}}{2}\right)$$
$$= 7.50 \text{ kips}$$

Note: During concrete placement, because the deck is parallel to the beam, the beam will not have continuous lateral support. It will be braced at 10 ft on center by the intermediate beams. Also, during concrete placement, a construction live load of 20 psf will be present. The loading is shown in Figure III-14.

From ASCE/SEI 7, Chapter 2, the required strengths for the typical interior beams with wet concrete only are determined as follows:

| LRFD | ASD |
|------|-----|
| $R_u = 1.4(24.4 \text{ kips})$ | $R_a = 24.4 \text{ kips}$ |
| $= 34.2 \text{ kips}$ |  |
|  |  |
| $M_u = (34.2 \text{ kips})(10 \text{ ft})$ | $M_a = (24.4 \text{ kips})(10 \text{ ft})$ |
| $= 342 \text{ kip-ft}$ | $= 244 \text{ kip-ft}$ |

![Loading and bracing diagram showing:
- Concentrated loads: PD = 24.4 kips, PL = 7.50 kips at center
- Beam braced at third points
- Span: 30'-0"
- Support points labeled 2 and 3]

*Fig. III-14. Loading and bracing diagram for typical interior girder with wet concrete and construction loads.*

---

# III-45

From ASCE/SEI 7, Chapter 2, the required strengths for the typical interior beams with wet concrete and construction live load are determined as follows:

| LRFD | ASD |
|------|-----|
| $R_u = 1.2(24.4 \text{ kips}) + 1.6(7.50 \text{ kips})$ | $R_a = 24.4 \text{ kips} + 7.50 \text{ kips}$ |
| $= 41.3 \text{ kips}$ | $= 31.9 \text{ kips}$ |
|  |  |
| $M_u$ (midspan) $= (41.3 \text{ kips})(10 \text{ ft})$ | $M_a$ (midspan) $= (31.9 \text{ kips})(10 \text{ ft})$ |
| $= 413 \text{ kip-ft}$ | $= 319 \text{ kip-ft}$ |

Assume $I_x \geq 935 \text{ in.}^4$, which is determined based on a wet concrete deflection of 1½ in. From AISC *Manual* Table 3-3, select a W21×68 with $I_x = 1{,}480 \text{ in.}^4$

From AISC *Manual* Table 6-1, verify the available flexural strength and shear strength using $L_b = 10$ ft and $C_b = 1.0$.

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 532 \text{ kip-ft} > 413 \text{ kip-ft} \quad \textbf{o.k.}$ | $\frac{M_n}{\Omega_b} = 354 \text{ kip-ft} > 319 \text{ kip-ft} \quad \textbf{o.k.}$ |
|  |  |
| $\phi_v V_n = 272 \text{ kips} > 41.3 \text{ kips} \quad \textbf{o.k.}$ | $\frac{V_n}{\Omega_v} = 181 \text{ kips} > 31.9 \text{ kips} \quad \textbf{o.k.}$ |

Check W21×68 as a composite beam.

From previous calculations:

| LRFD | ASD |
|------|-----|
| $R_u = 60.9$ kips | $R_a = 45.1$ kips |
|  |  |
| $M_u$ (midspan) $= 609$ kip-ft | $M_a$ (midspan) $= 451$ kip-ft |

From previous calculations, assuming $a = 1$ in.:

$$Y2 = 5.50 \text{ in.}$$

Enter AISC *Manual* Table 3-18 for a W21×68 with $Y2 = 5.50$ in. Selecting PNA location 7 with $\Sigma Q_n = 250$ kips provides an available flexural strength of:

| LRFD | ASD |
|------|-----|
| $\phi_b M_n = 844 \text{ kip-ft} > 609 \text{ kip-ft} \quad \textbf{o.k.}$ | $\frac{M_n}{\Omega_b} = 561 \text{ kip-ft} > 451 \text{ kip-ft} \quad \textbf{o.k.}$ |

From AISC Design Guide 3, limit the wet concrete deflection in a bay to $L/360$, not to exceed 1 in. From AISC *Manual* Table 3-22, Case 9:

---

# III-46

$$\Delta_{DL(wet \, conc)} = \frac{23P_D L^3}{648EI}$$

$$= \frac{23(24.4 \text{ kips})(30 \text{ ft})^3(12 \text{ in./ft})^3}{648(29{,}000 \text{ ksi})\left(1{,}480 \text{ in.}^4\right)}$$

$$= 0.941 \text{ in.}$$

Camber the beam for 80% of the calculated wet concrete deflection.

$$Camber = 0.80(0.941 \text{ in.})$$
$$= 0.753 \text{ in.}$$

Round the calculated value down to the nearest ¼ in.; therefore, specify ¾ in. of camber.

$0.941 \text{ in.} - \frac{3}{4} \text{ in.} = 0.191 \text{ in.} < 0.400 \text{ in.}$

Therefore, the total deflection limit of 1 in. for the bay has been met.

*Determine the effective width, b*

From AISC *Specification* Section I3.1a, the effective width of the concrete slab is the sum of the effective widths for each side of the beam centerline, which shall not exceed:

1. one-eighth of the span of the beam, center-to-center of supports

$$\left(\frac{30 \text{ ft}}{8}\right)(2 \text{ sides}) = 7.50 \text{ ft} \quad \textbf{controls}$$

2. one-half the distance to the centerline of the adjacent beam

$$\left(\frac{45 \text{ ft}}{2} + \frac{30 \text{ ft}}{2}\right) = 37.5 \text{ ft}$$

3. the distance to the edge of the slab

The latter is not applicable for an interior member.

*Determine the height of the compression block, a*

$$a = \frac{\Sigma Q_n}{0.85f_c'b}$$ (*Manual* Eq. 3-7)

$$= \frac{250 \text{ kips}}{0.85(4 \text{ ksi})(7.50 \text{ ft})(12 \text{ in./ft})}$$

$$= 0.817 \text{ in.} < 1 \text{ in.} \quad \textbf{o.k.}$$

From AISC *Manual* Table 6-1, the available shear strength of the W21×68 is determined as follows.

| LRFD | ASD |
|------|-----|
| $\phi_v V_n = 272 \text{ kips} > 60.9 \text{ kips} \quad \textbf{o.k.}$ | $\frac{V_n}{\Omega_v} = 181 \text{ kips} > 45.1 \text{ kips} \quad \textbf{o.k.}$ |

Check live load deflection.

---

# III-47

$$\Delta_{LL} = \frac{L}{360}$$

$$= \frac{(30 \text{ ft})(12 \text{ in./ft})}{360}$$

$$= 1.00 \text{ in.}$$

Entering AISC *Manual* Table 3-19 for a W21×68, with PNA location 7 and $Y2 = 5.50$ in., provides a lower bound moment of inertia of $I_{LB} = 2{,}510 \text{ in.}^4$

$$\Delta_{LL} = \frac{23P_L L^3}{648EI_{LB}}$$

$$= \frac{23(17.0 \text{ kips})(30 \text{ ft})^3(12 \text{ in./ft})^3}{648(29{,}000 \text{ ksi})\left(2{,}510 \text{ in.}^4\right)}$$

$$= 0.387 \text{ in.} < 1.00 \text{ in.} \quad \textbf{o.k.}$$

From AISC Design Guide 3, limit the live load deflection, using 50% of the (unreduced) design live load, to $L/360$ with a maximum absolute value of 1 in. across the bay.

The maximum deflection is:

$$\Delta_{LL} = \frac{23(0.5)(30.0 \text{ kips})(30 \text{ ft})^3(12 \text{ in./ft})^3}{648(29{,}000 \text{ ksi})\left(2{,}510 \text{ in.}^4\right)}$$

$$= 0.341 \text{ in.} < 1.00 \text{ in.} \quad \textbf{o.k.}$$

Check the deflection at the location where the floor beams are supported.

$$\Delta_{LL} = \frac{0.5(30.0 \text{ kips})(120 \text{ in.})}{6(29{,}000 \text{ ksi})\left(2{,}510 \text{ in.}^4\right)}\left[3(360 \text{ in.})(120 \text{ in.}) - 4(120 \text{ in.})^2\right]$$

$$= 0.297 \text{ in.} > 0.265 \text{ in.} \quad \textbf{o.k.}$$

Therefore, the total deflection in the bay is $0.297 \text{ in.} + 0.735 \text{ in.} = 1.03 \text{ in.}$, which is acceptably close to the limit of 1 in, where $\Delta_{LL} = 0.735$ in. is from the 45 ft interior composite beam running north-south.

*Determine the required shear stud connectors*

Using *Manual* Table 3-20, for parallel deck with $w_r/h_r \geq 1.5$, one ¾-in.-diameter stud in normal weight, 4 ksi concrete:

$$Q_n = 21.5 \text{ kips/anchor}$$

$$\frac{\Sigma Q_n}{Q_n} = \frac{250 \text{ kips}}{21.5 \text{ kips/anchor}}$$

$$= 11.6 \text{ anchors (on each side of maximum moment)}$$

Therefore, use a minimum of 24 studs for horizontal shear.

Per AISC *Specification* Section I8.2d, the maximum stud spacing is 36 in.

Because the load is concentrated at third points, the studs are to be arranged as follows:

---

# III-48

Use 12 studs between supports and supported beams at third points. Between supported beams (middle third of span), use 4 studs to satisfy minimum spacing requirements.

Therefore, 28 studs are required in a 12:4:12 arrangement.

Notes: Although the studs may be placed up to 36 in. on center, the steel deck must still be anchored to the supporting member at a spacing not to exceed 18 in. in accordance with AISC *Specification* Section I3.2c.

This W21×68 beam, with full lateral support, is very close to having sufficient available strength to support the imposed loads without composite action. A larger noncomposite beam might be a better solution.

---

# III-49

## COLUMN DESIGN AND SELECTION FOR GRAVITY LOADS

**Estimate column loads**

According to ASCE/SEI 7-22, Sections 2.3.1 and 2.3.6, when snow acts as a companion load and not the principal load in an axial load combination, it shall be taken as the flat roof snow or the sloped roof snow. Similarly, in ASCE/SEI 7-22, Sections 2.4.1 and 2.4.5, when snow acts in combination with other transient loads in ASD combinations, it shall be taken as the flat roof snow or the sloped roof snow. Although combinations with snow as the principal load could govern columns in a structure, for this example, the lowest segment will control and only will control in combinations where snow is not the principal loading. As such, the flat roof snow is used in the column design for this example and rain-on-snow surcharge and drift are not considered. It is also possible that the roof live load may govern.

Roof loads (from previous calculations):

Dead load = 20 psf
Flat roof snow load = $p_f$ = 24.6 psf (LRFD level)
Roof live load = $L_r$ = 20 psf (ASD Level)

Mechanical equipment and screen wall (average):

$$w = 40 \text{ psf}$$

The spandrel panel weight was calculated as 0.413 kip/ft as part of the selection process for the W16×26 roof beams at the east and west ends of the building.

The mechanical room dead load of 0.060 kip/ft² (40 kip/ft² surcharge) was determined as part of the selection process for the W14×22 roof beams at the mechanical area.

Roof live load reduction is considered per ASCE/SEI 7-22, Section 4.8.2, with $R_1$ based on the tributary area to the column and $R_2 = 1$ for a flat roof.

Floor loads (from previous calculations):

Dead load = 75 psf
Live load = 80 psf
Total = 155 psf

Calculate reduction in live loads, analyzed at the base of three floors ($n = 3$) using ASCE/SEI 7, Section 4.7.2. Note that the 6 in. cantilever of the floor slab has been ignored for the calculation of $K_{LL}$ for columns in this building because it has a negligible effect.

Columns: 2A, 2F, 3A, 3F, 4A, 4F, 5A, 5F, 6A, 6F, 7A, 7F
Exterior column without cantilever slabs
$K_{LL} = 4$ (ASCE/SEI 7, Table 4.7-1)
$L_o = 80$ psf
$n = 3$ (three floors supported)

The tributary area at the roof and floors is:

$$A_T = (22.5 \text{ ft} + 0.5 \text{ ft})(30 \text{ ft})$$
$$= 690 \text{ ft}^2$$

---

# III-50

The reduction in uniform roof live loads is determined from ASCE/SEI 7, Section 4.8. Because $A_T \geq 600$ ft²:

$$R_1 = 0.6$$

$$L_r = L_{ro}R_1R_2$$ (ASCE/SEI 7, Eq. 4.8-1)
$$= (20 \text{ psf})(0.6)(1)$$
$$= 12.0 \text{ psf}$$

The reduction in uniform floor live loads is determined from ASCE/SEI 7, Section 4.7.

$$L = L_o\left(0.25 + \frac{15}{\sqrt{K_{LL}nA_T}}\right) \geq 0.4L_o$$ (ASCE/SEI 7, Eq. 4.7-1)

$$= (80 \text{ psf})\left[0.25 + \frac{15}{\sqrt{(4)(3)\left(690 \text{ ft}^2\right)}}\right] > 0.4(80 \text{ psf})$$

$$= 33.2 \text{ psf} > 32.0 \text{ psf}$$

Therefore, use $L = 33.2$ psf.

Columns: 1B, 1E, 8B, 8E
Exterior column without cantilever slabs
$K_{LL} = 4$ (ASCE/SEI 7, Table 4.7-1)
$L_o = 80$ psf
$n = 3$

The tributary area at the roof is:

$$A_T = (3.00 \text{ ft} + 0.5 \text{ ft})(22.5 \text{ ft})$$
$$= 78.8 \text{ ft}^2$$

The tributary area at the floors is:

$$A_T = (5.00 \text{ ft} + 0.5 \text{ ft})(22.5 \text{ ft})$$
$$= 124 \text{ ft}^2$$

The reduction in uniform roof live loads is determined from ASCE/SEI 7, Section 4.8. Because $A_T \leq 200$ ft²:

$$R_1 = 1$$

$$L_r = L_{ro}R_1R_2$$ (ASCE/SEI 7, Eq. 4.8-1)
$$= (20 \text{ psf})(1)(1)$$
$$= 20.0 \text{ psf}$$

The reduction in uniform floor live loads is determined from ASCE/SEI 7, Section 4.7.

---

# III-51

$$L = L_o\left(0.25 + \frac{15}{\sqrt{K_{LL}nA_T}}\right) \geq 0.4L_o$$ (ASCE/SEI 7, Eq. 4.7-1)

$$= (80 \text{ psf})\left[0.25 + \frac{15}{\sqrt{(4)(3)\left(124 \text{ ft}^2\right)}}\right] > 0.4(80 \text{ psf})$$

$$= 51.1 \text{ psf} > 32.0 \text{ psf}$$

Use $L = 51.1$ psf.

Columns: 1A, 1F, 8A, 8F
Corner column without cantilever slabs
$K_{LL} = 4$ (ASCE/SEI 7, Table 4.7-1)
$L_o = 80$ psf
$n = 3$

The tributary area at the roof is:

$$A_T = (15.0 \text{ ft} + 0.5 \text{ ft})(22.5 \text{ ft} + 0.5 \text{ ft}) - \left(\frac{78.8 \text{ ft}^2}{2}\right)$$

$$= 318 \text{ ft}^2$$

The tributary area at the floors is:

$$A_T = (15.0 \text{ ft} + 0.5 \text{ ft})(22.5 \text{ ft} + 0.5 \text{ ft}) - \left(\frac{124 \text{ ft}^2}{2}\right)$$

$$= 295 \text{ ft}^2$$

The reduction in uniform roof live loads is determined from ASCE/SEI 7, Section 4.8. Because 200 ft² < $A_T$ < 600 ft²:

$$R_1 = 1.2 - 0.001A_T$$
$$= 1.2 - 0.001\left(318 \text{ ft}^2\right)$$
$$= 0.882$$

$$L_r = L_{ro}R_1R_2$$ (ASCE/SEI 7, Eq. 4.8-1)
$$= (20 \text{ psf})(0.882)(1)$$
$$= 17.6 \text{ psf}$$

The reduction in uniform floor live loads is determined from ASCE/SEI 7, Section 4.7.

$$L = L_o\left(0.25 + \frac{15}{\sqrt{K_{LL}nA_T}}\right) \geq 0.4L_o$$ (ASCE/SEI 7, Eq. 4.7-1)

$$= (80 \text{ psf})\left[0.25 + \frac{15}{\sqrt{(4)(3)\left(295 \text{ ft}^2\right)}}\right] > 0.4(80 \text{ psf})$$

$$= 40.2 \text{ psf} > 32.0 \text{ psf}$$

---

# III-52

Therefore, use $L = 40.2$ psf.

Columns: 1C, 1D, 8C, 8D
Exterior column without cantilever slabs
$K_{LL} = 4$ (ASCE/SEI 7, Table 4.7-1)
$L_o = 80$ psf
$n = 3$

The tributary area at the roof is:

$$A_T = (15.0 \text{ ft} + 0.5 \text{ ft})\left(\frac{45 \text{ ft} + 30 \text{ ft}}{2}\right) - \left(\frac{78.8 \text{ ft}^2}{2}\right)$$

$$= 542 \text{ ft}^2$$

The tributary area at the floors is:

$$A_T = (15.0 \text{ ft} + 0.5 \text{ ft})\left(\frac{45 \text{ ft} + 30 \text{ ft}}{2}\right) - \left(\frac{124 \text{ ft}^2}{2}\right)$$

$$= 519 \text{ ft}^2$$

The reduction in uniform roof live loads is determined from ASCE/SEI 7, Section 4.8. Because 200 ft² < $A_T$ < 600 ft²:

$$R_1 = 1.2 - 0.001A_T$$
$$= 1.2 - 0.001\left(542 \text{ ft}^2\right)$$
$$= 0.658$$

$$L_r = L_{ro}R_1R_2$$ (ASCE/SEI 7, Eq. 4.8-1)
$$= (20 \text{ psf})(0.658)(1)$$
$$= 13.2 \text{ psf}$$

The reduction in uniform floor live loads is determined from ASCE/SEI 7, Section 4.7.

$$L = L_o\left(0.25 + \frac{15}{\sqrt{K_{LL}nA_T}}\right) \geq 0.4L_o$$ (ASCE/SEI 7, Eq. 4.7-1)

$$= (80 \text{ psf})\left[0.25 + \frac{15}{\sqrt{(4)(3)\left(519 \text{ ft}^2\right)}}\right] > 0.4(80 \text{ psf})$$

$$= 35.2 \text{ psf} > 32.0 \text{ psf}$$

Therefore, use $L = 35.2$ psf.

Columns: 2C, 2D, 3C, 3D, 4C, 4D, 5C, 5D, 6C, 6D, 7C, 7D
Interior column
$K_{LL} = 4$ (ASCE/SEI 7, Table 4.7-1)
$L_o = 80$ psf
$n = 3$

---

# III-53

The tributary area at the roof and floors is:

$$A_T = \left(\frac{45 \text{ ft} + 30 \text{ ft}}{2}\right)(30 \text{ ft})$$

$$= 1{,}125 \text{ ft}^2$$

The reduction in uniform roof live loads is determined from ASCE/SEI 7, Section 4.8. Because $A_T \geq 600$ ft²:

$$R_1 = 0.6$$

$$L_r = L_{ro}R_1R_2$$ (ASCE/SEI 7, Eq. 4.8-1)
$$= (20 \text{ psf})(0.6)(1)$$
$$= 12.0 \text{ psf}$$

The reduction in uniform floor live loads is determined from ASCE/SEI 7, Section 4.7.

$$L = L_o\left(0.25 + \frac{15}{\sqrt{K_{LL}nA_T}}\right) \geq 0.4L_o$$ (ASCE/SEI 7, Eq. 4.7-1)

$$= (80 \text{ psf})\left[0.25 + \frac{15}{\sqrt{(4)(3)\left(1{,}125 \text{ ft}^2\right)}}\right] < 0.4(80 \text{ psf})$$

$$= 30.3 \text{ psf} < 32.0 \text{ psf}$$

Therefore, use $L = 32.0$ psf.

A summary of the column loads at the roof and floors is given in Tables III-2 and III-3.

The spandrel panel weight was calculated as 0.503 kip/ft as part of the selection process for the W18×35 edge beams at the north and south ends of the building.

The column loads are summarized in Table III-4.

---

# III-54

| **Table III-2<br>Summary of Column Loads at the Roof** |  |  |  |  |  |  |  |  |
|--------------------------------------------------------|--|--|--|--|--|--|--|--|
| **Column** | **Loading** |  | **Area,<br>ft²** | **DL,<br>kip/ft²** | **$P_D$,<br>kips** | **SL,<br>kip/ft²** | **$P_S$,<br>kips** | **$L_r$,<br>kip/ft²** | **$P_{Lr}$,<br>kips** |
|  | **Width,<br>ft** | **Length,<br>ft** |  |  |  |  |  |  |
| 2A, 2F, 3A, 3F,<br>4A, 4F, 5A, 5F,<br>6A, 6F, 7A, 7F<br>Exterior wall | 23.0 | 30.0 | 690 | 0.020 | 13.8 | 0.0246 | 17.0 | 0.0120 | 8.28 |
|  |  | 30.0 |  | 0.413 kip/ft | 12.4 |  |  |  |  |
|  |  |  |  |  | **26.2** |  | **17.0** |  | **8.28** |
| 1B, 1E, 8B, 8E<br>Exterior wall | 3.50 | 22.5<br>22.5 | 78.8 | 0.020<br>0.413 kip/ft | 1.58<br>9.29 | 0.0246 | 1.94 | 0.0200 | 1.58 |
|  |  |  |  |  | **10.9** |  | **1.94** |  | **1.58** |
| 1A, 1F, 8A, 8F<br>Exterior wall | 23.0 | 15.5<br>27.3 | 318 | 0.020<br>0.413 kip/ft | 6.36<br>11.3 | 0.0246 | 7.82 | 0.0176 | 5.60 |
|  |  |  |  |  | **17.7** |  | **7.82** |  | **5.60** |
| 1C, 1D, 8C, 8D<br>Exterior wall | 37.5 | 15.5<br>26.3 | 542 | 0.020<br>0.413 kip/ft | 10.8<br>10.9 | 0.0246 | 13.3 | 0.0132 | 7.15 |
|  |  |  |  |  | **21.7** |  | **13.3** |  | **7.15** |
| 2C, 2D, 7C, 7D | 37.5 | 30.0 | 1,125 | 0.020 | 22.5 | 0.0246 | 27.7 | 0.0120 | 13.5 |
| 3C, 3D, 4C,<br>4D, 5C, 5D,<br>6C, 6D | 37.5 | 30.0 | 1,125 | 0.020 | 22.5 | 0.0246 | 27.7 | 0.0120 | 13.5 |
| Mechanical DL | 15.0 | 30.0 | 450 | 0.040 | 18.0 |  |  |  |  |
|  |  |  |  |  | **40.5** |  | **27.7** |  | **13.5** |

| **Table III-3<br>Summary of Column Loads at the Floors** |  |  |  |  |  |  |  |
|----------------------------------------------------------|--|--|--|--|--|--|--|
| **Column** | **Loading** |  | **Area,<br>ft²** | **DL,<br>kip/ft²** | **$P_D$,<br>kips** | **LL,<br>kip/ft²** | **$P_L$,<br>kips** |
|  | **Width,<br>ft** | **Length,<br>ft** |  |  |  |  |  |
| 2A, 2F, 3A, 3F,<br>4A, 4F, 5A, 5F,<br>6A, 6F, 7A, 7F<br>Exterior wall | 23.0 | 30.0 | 690 | 0.075 | 51.8 | 0.0332 | 22.9 |
|  |  | 30.0 |  | 0.503 kip/ft | 15.1 |  |  |
|  |  |  |  |  | **66.9** |  | **22.9** |
| 1B, 1E, 8B, 8E<br>Exterior wall | 5.50 | 22.5<br>22.5 | 124 | 0.075<br>0.503 kip/ft | 9.30<br>11.3 | 0.0511 | 6.34 |
|  |  |  |  |  | **20.6** |  | **6.34** |
| 1A, 1F, 8A, 8F<br>Exterior wall | 23.0 | 15.5<br>27.3 | 295 | 0.075<br>0.503 kip/ft | 22.1<br>13.7 | 0.0402 | 11.9 |
|  |  |  |  |  | **35.8** |  | **11.9** |
| 1C, 1D, 8C, 8D<br>Exterior wall | 37.5 | 15.5<br>26.3 | 519 | 0.075<br>0.503 kip/ft | 38.9<br>13.2 | 0.0352 | 18.3 |
|  |  |  |  |  | **52.1** |  | **18.3** |
| 2C, 2D, 3C, 3D,<br>4C, 4D, 5C, 5D,<br>6C, 6D, 7C, 7D | 37.5 | 30.0 | 1,125 | 0.075 | 84.4 | 0.0320 | 36.0 |

---

# III-55

| **Table III-4<br>Summary of Column Loads** |  |  |  |  |  |
|---------------------------------------------|--|--|--|--|--|
| **Column** | **Floor** | **$P_D$,<br>kips** | **$P_L$,<br>kips** | **$P_S$,<br>kips** | **$P_{Lr}$,<br>kips** |
| 2A, 2F, 3A, 3F, 4A, 4F,<br>5A, 5F, 6A, 6F, 7A, 7F | Roof | 26.2 |  | 17.0 | 8.28 |
|  | 4th | 66.9 | 22.9 |  |  |
|  | 3rd | 66.9 | 22.9 |  |  |
|  | 2nd | 66.9 | 22.9 |  |  |
|  | **Total** | **227** | **68.7** | **17.0** | **8.28** |
| 1B, 1E, 8B, 8E | Roof | 10.9 |  | 1.94 | 1.58 |
|  | 4th | 20.6 | 6.34 |  |  |
|  | 3rd | 20.6 | 6.34 |  |  |
|  | 2nd | 20.6 | 6.34 |  |  |
|  | **Total** | **72.7** | **19.0** | **1.94** | **1.58** |
| 1A, 1F, 8A, 8F | Roof | 17.7 |  | 7.82 | 5.60 |
|  | 4th | 35.8 | 11.9 |  |  |
|  | 3rd | 35.8 | 11.9 |  |  |
|  | 2nd | 35.8 | 11.9 |  |  |
|  | **Total** | **125** | **35.7** | **7.82** | **5.60** |
| 1C, 1D, 8C, 8D | Roof | 21.7 |  | 13.3 | 7.15 |
|  | 4th | 52.1 | 18.3 |  |  |
|  | 3rd | 52.1 | 18.3 |  |  |
|  | 2nd | 52.1 | 18.3 |  |  |
|  | **Total** | **178** | **54.9** | **13.3** | **7.15** |
| 2C, 2D, 7C, 7D | Roof | 22.5 |  | 27.7 | 13.5 |
|  | 4th | 84.4 | 36.0 |  |  |
|  | 3rd | 84.4 | 36.0 |  |  |
|  | 2nd | 84.4 | 36.0 |  |  |
|  | **Total** | **276** | **108** | **27.7** | **13.5** |
| 3C, 3D, 4C, 4D,<br>5C, 5D, 6C, 6D | Roof | 40.5 |  | 27.7 | 13.5 |
|  | 4th | 84.4 | 36.0 |  |  |
|  | 3rd | 84.4 | 36.0 |  |  |
|  | 2nd | 84.4 | 36.0 |  |  |
|  | **Total** | **294** | **108** | **27.7** | **13.5** |

---

# III-56

## SELECT TYPICAL INTERIOR LEANING COLUMNS

**Columns: 3C, 3D, 4C, 4D, 5C, 5D, 6C, 6D**

Elevation of second floor slab: 113.5 ft
Elevation of first floor slab: 100 ft
Column unbraced length: $L_x = L_y = 13.5$ ft

Note: $K_x = K_y = 1.0$ for a leaning column when using the effective length method.

$$L_{cx} = K_x L_x$$
$$= 1.0(13.5 \text{ ft})$$
$$= 13.5 \text{ ft}$$

$$L_{cy} = K_y L_y$$
$$= 1.0(13.5 \text{ ft})$$
$$= 13.5 \text{ ft}$$

From ASCE/SEI 7, Chapter 2, the required axial strength is determined using the following controlling load combinations:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(294 \text{ kips}) + 1.6(108 \text{ kips}) + 0.3(27.7 \text{ kips})$ | $P_a = 294 \text{ kips} + 108 \text{ kips}$ |
| $= 534 \text{ kips}$ | $= 402 \text{ kips}$ |

Using AISC *Manual* Table 4-1a, enter with $L_c = 14.0$ ft (conservative) and proceed across the table until reaching the lightest size that has sufficient available strength at the required unbraced length. Select a W12×65. The available strength in axial compression is:

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 685 \text{ kips} > 534 \text{ kips}$ **o.k.** | $\frac{P_n}{\Omega_c} = 456 \text{ kips} > 402 \text{ kips}$ **o.k.** |

Note: A W14×68 would also be an acceptable selection.

**Columns: 2C, 2D, 7C, 7D**

Elevation of second floor slab: 113.5 ft
Elevation of first floor slab: 100 ft
Column unbraced length: $L_x = L_y = 13.5$ ft

Note: $K_x = K_y = 1.0$ for a leaning column when using the effective length method.

$$L_{cx} = K_x L_x$$
$$= 1.0(13.5 \text{ ft})$$
$$= 13.5 \text{ ft}$$

$$L_{cy} = K_y L_y$$
$$= 1.0(13.5 \text{ ft})$$
$$= 13.5 \text{ ft}$$

---

# III-57

From ASCE/SEI 7, Chapter 2, the required axial strength is determined using the following controlling load combinations:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(276 \text{ kips}) + 1.6(108 \text{ kips}) + 0.3(27.7 \text{ kips})$ | $P_a = 276 \text{ kips} + 108 \text{ kips}$ |
| $= 512 \text{ kips}$ | $= 384 \text{ kips}$ |

Using AISC *Manual* Table 4-1a, enter with $L_c = 14.0$ ft (conservative) and proceed across the table until reaching the lightest size that has sufficient available strength at the required unbraced length. Select a W12×65. The available strength in axial compression is:

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 685 \text{ kips} > 512 \text{ kips}$ **o.k.** | $\frac{P_n}{\Omega_c} = 456 \text{ kips} > 384 \text{ kips}$ **o.k.** |

Note: A W14×68 would also be an acceptable selection. However, W12×65 columns were selected to keep sizes consistent for all interior columns.

---

# III-58

## SELECT TYPICAL EXTERIOR LEANING COLUMNS

**Columns: 1B, 1E, 8B, 8E**

Elevation of second floor slab: 113.5 ft
Elevation of first floor slab: 100 ft
Column unbraced length: $L_x = L_y = 13.5$ ft

Note: $K_x = K_y = 1.0$ for a leaning column when using the effective length method.

$$L_{cx} = K_x L_x$$
$$= 1.0(13.5 \text{ ft})$$
$$= 13.5 \text{ ft}$$

$$L_{cy} = K_y L_y$$
$$= 1.0(13.5 \text{ ft})$$
$$= 13.5 \text{ ft}$$

From ASCE/SEI 7, Chapter 2, the required axial strength is determined using the following controlling load combinations:

| LRFD | ASD |
|------|-----|
| $P_u = 1.2(72.7 \text{ kips}) + 1.6(19.0 \text{ kips}) + 0.5(1.58 \text{ kips})$ | $P_a = 72.7 \text{ kips} + 19.0 \text{ kips}$ |
| $= 118 \text{ kips}$ | $= 91.7 \text{ kips}$ |

Using AISC *Manual* Table 4-1a, enter with $L_c = 14.0$ ft (conservative) and proceed across the table until reaching the lightest size that has sufficient available strength at the required unbraced length. Select a W12×40. The available strength in axial compression is:

| LRFD | ASD |
|------|-----|
| $\phi_c P_n = 304 \text{ kips} > 118 \text{ kips}$ **o.k.** | $\frac{P_n}{\Omega_c} = 202 \text{ kips} > 91.7 \text{ kips}$ **o.k.** |

Note, A W12 column was selected for ease of erection of framing beams (bolted double-angle connections can be used without bolt staggering). Final column selections at the moment and braced frames are illustrated later in this example.

---

# III-59

## WIND LOAD DETERMINATION

Use the Directional Procedure for buildings from ASCE/SEI 7, Chapter 27.

To qualify for the directional wind load procedure, per ASCE/SEI 7, Section 27.1.2, the following conditions must be met:

1. Regular-shaped **o.k.**

2. Does not have response characteristics requiring special considerations **o.k.**

*Define input parameters*

1. Risk category: II from ASCE/SEI 7, Table 1.5-1

2. Basic wind speed: $V = 107$ mph (3-s) from ASCE/SEI 7, Figure 26.5-1B

3. Wind directionality factor: $K_d = 0.85$ from ASCE/SEI, Table 26.6-1

4. Exposure category: C from ASCE/SEI 7, Section 26.7

5. Topographic factor: $K_{zt} = 1.0$ from ASCE/SEI 7, Section 26.8

6. Ground elevation factor: $K_e = 1.00$ from ASCE/SEI 7, Section 26.9

7. Enclosure classification: Enclosed from ASCE/SEI 7, Section 26.12

8. Internal pressure coefficient: $GC_{Pi} = \pm 0.18$ from ASCE/SEI 7, Table 26.13-1

9. Mean roof height: 55.0 ft

Velocity pressure exposure coefficient: $K_h = 1.11$ interpolated from ASCE/SEI 7, Table 26.10-1

Roof angle: $\theta = 0°$

The velocity pressure at the mean roof height is calculated from ASCE/SEI 7, Eq. 26.10-1:

$$q_h = 0.00256 K_h K_{zt} K_e V^2$$ (ASCE/SEI 7, Eq. 26.10-1)
$$= 0.00256(1.11)(1.0)(1.00)(107 \text{ mph})^2$$
$$= 32.5 \text{ psf}$$

The velocity pressure is similarly calculated at the height of each diaphragm level, as shown in Table III-5.

Determine if the building will be classified as a rigid or flexible structure. Because the height of the building is less than 300 ft and the building height is less than four times its effective length, the approximate natural frequency may be calculated per ASCE/SEI 7, Section 26.11.3. For structural steel moment-resisting frame buildings:

$$n_a = 22.2/h^{0.8}$$ (ASCE/SEI 7, Eq. 26.11-2)
$$= 22.2/(55 \text{ ft})^{0.8}$$
$$= 0.90 \text{ Hz}$$

---

# III-60

<table>
<tr><th colspan="4">Summary of Velocity Pressures by Level</th></tr>
<tr>
  <th>Level</th>
  <th>Height above grade<br>ft</th>
  <th>K<sub>h</sub></th>
  <th>q<sub>h</sub><br>psf</th>
</tr>
<tr><td>Top of Parapet</td><td>57.0</td><td>1.12</td><td>q<sub>h</sub> = 32.8</td></tr>
<tr><td>Roof</td><td>55.0</td><td>1.11</td><td>q<sub>h</sub> = 32.5</td></tr>
<tr><td>4th Floor</td><td>40.5</td><td>1.05</td><td>q<sub>h</sub> = 30.7</td></tr>
<tr><td>3rd Floor</td><td>27.0</td><td>0.98</td><td>q<sub>h</sub> = 28.1</td></tr>
<tr><td>2nd Floor</td><td>13.5</td><td>0.85</td><td>q<sub>h</sub> = 24.9</td></tr>
</table>

For structural steel buildings with other lateral force-resisting systems:

$$n = N/a$$ (ASCE/SEI 7, Eq. 26.11-4)
$$= 78/(55 \text{ ft})$$

As indicated in ASCE/SEI 7, Section 26.2, classifies a rigid building as one with a natural frequency greater than or equal to 1 Hz. Therefore, this building is rigid and the calculations may proceed using the simplified building design procedure as outlined in ASCE/SEI 7, Section 26.11.3. For structural steel moment-resisting frame buildings, the gust-effect factor for flexible buildings should be calculated using ASCE/SEI 7, Section 26.11.5, where $n < 1$ Hz. Because this building is rigid, the gust-effect factor for flexible buildings should be calculated using ASCE/SEI 7, Eq. 26.11-10. Although the building has a natural frequency less than 1 Hz, the criteria in ASCE/SEI 7, Section 26.2, which limits the simplified procedure based on height and the fundamental frequency is found to have a fundamental frequency less than 1 Hz, the gust effect factor for flexible buildings should be calculated using ASCE/SEI 7, Section 26.11.5, as shown in the remainder of this example. Therefore, this building should be designed as a flexible building and cannot use the provisions of ASCE/SEI 7, Section 27.4-1 for calculating wind loads.

The load cases from ASCE/SEI 7, Figure 27.3-8, are applicable. It can be shown that for this structure the maximum loading and most critical forces will be developed using Case 2 of ASCE/SEI 7, Figure 27.3-8. The wind force and design pressures applicable to this case will be presented in this example. Wind Case 2 of ASCE/SEI 7, Figure 27.3-8, and will be computed for both the north-south and east-west wind directions. Wind force and design pressures from the MWFRS may be applicable to design of certain building elements.

The parapet wind pressure for MWFRS design is given by ASCE/SEI 7, Section 27.3-4, with $GC_p = +1.5$ for windward parapets and $GC_p = -1.0$ for leeward parapets. The parapet wind pressure are also considered applicable to the mechanical screen wall enclosure (a roof-edge parapet is equivalent to the mechanical screen wall). The parapet wind pressure are as follows:

As a conservative simplification, the leeward wind suction of -6.78 psf will be used for both the north-south and east-west directions.

The MWFRS pressures are determined by ASCE/SEI 7, Section 27.3-1 and Equation 27.3-1, as shown in Table III-6.

---

# III-61

| **Table III-6<br>MWFRS Design Wind Pressures** |  |  |  |  |
|-----------------------------------------------|--|--|--|--|
|  | **Wind in North-South Direction** | **Wind in East-West Direction** |
| *L*/*B* | 0.577 | 1.73 |
| *K<sub>d</sub>* | 0.85 | 0.85 |
| *G* | 0.85 | 0.85 |
| *GC<sub>Pi</sub>* | −0.18 | −0.18 |
| *q<sub>h</sub>*, **psf** | 32.5 | 32.5 |
| **Surface** | **Windward Wall** | **Leeward Wall** | **Windward Wall** | **Leeward Wall** |
| *C<sub>p</sub>* | 0.8 | −0.5 | 0.8 | −0.35 |
| *q*, **psf** | Roof | 32.5 | 32.5 | 32.5 | 32.5 |
|  | 4th Floor | 30.5 | 32.5 | 30.5 | 32.5 |
|  | 3rd Floor | 28.1 | 32.5 | 28.1 | 32.5 |
|  | 2nd Floor | 24.9 | 32.5 | 24.9 | 32.5 |
|  | Roof | 23.8 | −6.78 | 23.8 | −3.25 |
| *p*, **psf** | 4th Floor | 22.6 | −6.78 | 22.6 | −3.25 |
|  | 3rd Floor | 21.2 | −6.78 | 21.2 | −3.25 |
|  | 2nd Floor | 19.4 | −6.78 | 19.4 | −3.25 |

For the windward parapet and screen wall:

$$p_p = q_h K_d \left( GC_{pn} \right)$$ (ASCE/SEI 7, Eq. 27.3-3)
$$= (32.8 \text{ psf})(0.85)(+1.5)$$
$$= +41.8 \text{ psf}$$

For the leeward parapet and screen wall:

$$p_p = q_h K_d \left( GC_{pn} \right)$$ (ASCE/SEI 7, Eq. 27.3-3)
$$= (32.8 \text{ psf})(0.85)(-1.0)$$
$$= -27.9 \text{ psf}$$

*Calculate load on roof diaphragm*

Mechanical screen wall height: 6 ft
Wall height: $0.5[55 \text{ ft} - 3(13.5 \text{ ft})] = 7.25$ ft
Parapet wall height: 2 ft

$$w_{roof,\,parapet} = \left[(23.8 \text{ psf}) - (-6.78 \text{ psf})\right](7.25 \text{ ft}) + \left[(41.8 \text{ psf}) - (-27.9 \text{ psf})\right](2 \text{ ft})$$
$$\hspace{1.5in} \text{wall} \hspace{1.5in} \text{parapet}$$
$$= 222 \text{ plf} + 139 \text{ plf}$$
$$= 361 \text{ plf (at parapet)}$$

---

# III-62

$$w_{roof,\,screen\,wall} = \left[(23.8 \text{ psf}) - (-6.78 \text{ psf})\right](7.25 \text{ ft}) + \left[(41.8 \text{ psf}) - (-27.9 \text{ psf})\right](6 \text{ ft})$$
$$\hspace{1.5in} \text{wall} \hspace{2in} \text{screen wall}$$
$$= 222 \text{ plf} + 418 \text{ plf}$$
$$= 640 \text{ plf (at screen wall)}$$

*Calculate load on fourth floor diaphragm*

Wall height: $0.5(55.0 \text{ ft} - 40.5 \text{ ft}) = 7.25$ ft
$$\hspace{0.6in} 0.5(40.5 \text{ ft} - 27.0 \text{ ft}) = 6.75$ ft
Total wall height at floor: $6.75 \text{ ft} + 7.25 \text{ ft} = 14.0$ ft

$$w_{4^{th}\,floor} = \left[(22.6 \text{ psf}) - (-6.78 \text{ psf})\right](14.0 \text{ ft})$$
$$= 411 \text{ plf}$$

*Calculate load on third floor diaphragm*

Wall height: $0.5(40.5 \text{ ft} - 27.0 \text{ ft}) = 6.75$ ft
$$\hspace{0.6in} 0.5(27.0 \text{ ft} - 13.5 \text{ ft}) = 6.75$ ft
Total wall height at floor: $6.75 \text{ ft} + 6.75 \text{ ft} = 13.5$ ft

$$w_{3^{rd}\,floor} = \left[(21.2 \text{ psf}) - (-6.78 \text{ psf})\right](13.5 \text{ ft})$$
$$= 378 \text{ plf}$$

*Calculate load on second floor diaphragm*

Wall height: $0.5(27.0 \text{ ft} - 13.5 \text{ ft}) = 6.75$ ft
$$\hspace{0.6in} 0.5(13.5 \text{ ft} - 0 \text{ ft}) = 6.75$ ft
Total wall height at floor: $6.75 \text{ ft} + 6.75 \text{ ft} = 13.5$ ft

$$w_{2^{nd}\,floor} = \left[(19.4 \text{ psf}) - (-6.78 \text{ psf})\right](13.5 \text{ ft})$$
$$= 353 \text{ plf}$$

Determine the wind load on each frame at each level.

where
$l$ = length of structure, ft
$b$ = width of structure, ft
$h$ = height of wall at building element, ft

For wind from a north or south direction:

Total load to each frame:

$$P_{W(N-S)} = wl/2$$

Shear in diaphragm:

---

# III-63

$$v_{(N-S)} = \frac{P_{W(N-S)}}{120 \text{ ft}}, \text{ for roof}$$

$$v_{(N-S)} = \frac{P_{W(N-S)}}{90 \text{ ft}}, \text{ for floors (deduction for stair openings)}$$

For wind from an east or west direction:

Total load to each frame:

$$P_{W(E-W)} = \frac{wb}{2}$$

Shear in diaphragm:

$$v_{(E-W)} = \frac{P_{W(E-W)}}{210 \text{ ft}}, \text{ for roof and floors}$$

Table III-7 summarizes the total wind load in each direction acting on a steel frame at each level. The wind load at the ground level has not been included in the chart because it does not affect the steel frame.

The parapet level dimensions exclude the screen wall area, and the screen wall dimensions exclude the parapet area. The floor level dimensions correspond to the outside dimensions of the cladding.

| **Table III-7<br>Summary of Wind Loads at Each Level** |  |  |  |  |  |  |  |  |  |  |
|--------------------------------------------------------|--|--|--|--|--|--|--|--|--|--|
|  | *l*,<br>**ft** | *b*,<br>**ft** | *h*,<br>**ft** | *p*<sub>**windward**</sub>,<br>**psf** | *p*<sub>**leeward**</sub>,<br>**psf** | *w*,<br>**plf** | *P*<sub>*W(N-S)*</sub>,<br>**kips** | *P*<sub>*W(E-W)*</sub>,<br>**kips** | *v*<sub>*(N-S)*</sub>,<br>**plf** | *v*<sub>*(E-W)*</sub>,<br>**plf** |
| Screen | 93.0 | 33.0 | 6.00 | 41.8 | −27.9 | 418 |  |  |  |  |
| Parapet | 120 | 90.0 | 2.00 | 41.8 | −27.9 | 139 | 51.4 | 26.8 | 428 | 128 |
| Roof | 213 | 123 | 7.25 | 23.8 | −6.78 | 222 |  |  |  |  |
| 4th | 213 | 123 | 14.0 | 22.6 | −6.78 | 411 | 43.8 | 25.3 | 487 | 120 |
| 3rd | 213 | 123 | 13.5 | 21.2 | −6.78 | 378 | 40.3 | 23.2 | 448 | 110 |
| 2nd | 213 | 123 | 13.5 | 19.4 | −6.78 | 353 | 37.6 | 21.7 | 418 | 103 |
| Total at Base |  |  |  |  |  |  | 173 | 97.0 |  |  |

---

# III-64

## SEISMIC LOAD DETERMINATION

The floor plan area: 120 ft, column center line to column center line, by 210 ft, column centerline to column center line, with the edge of floor slab or roof deck 6 in. beyond the column center line.

Area = $(121 \text{ ft})(211 \text{ ft})$
$$= 25{,}500 \text{ ft}^2$$

The perimeter cladding system length:

Length = $(2)(123 \text{ ft}) + (2)(213 \text{ ft})$
$$= 672 \text{ ft}$$

The perimeter cladding weight at floors:

<table>
<tr>
  <td>Brick spandrel panel with metal stud backup:</td>
  <td>$(7.50 \text{ ft})(0.055 \text{ kip/ft}^2)$</td>
  <td>$= 0.413 \text{ kip/ft}$</td>
</tr>
<tr>
  <td>Window wall system:</td>
  <td>$(6.00 \text{ ft})(0.015 \text{ kip/ft}^2)$</td>
  <td>$= 0.090 \text{ kip/ft}$</td>
</tr>
<tr>
  <td><strong>Total:</strong></td>
  <td></td>
  <td><strong>0.503 kip/ft</strong></td>
</tr>
</table>

Typical roof dead load (from previous calculations):

Although 40 psf was used to account for the mechanical units and screen wall for the beam and column design, the entire mechanical area will not be uniformly loaded. Use 30% of the uniform 40 psf mechanical area load to determine the total weight of all of the mechanical units and screen wall for the seismic load determination.

<table>
<tr>
  <td>Roof area:</td>
  <td>$(25{,}500 \text{ ft}^2)(0.020 \text{ kip/ft}^2)$</td>
  <td>$= 510 \text{ kips}$</td>
</tr>
<tr>
  <td>Wall perimeter:</td>
  <td>$(672 \text{ ft})(0.413 \text{ kip/ft})$</td>
  <td>$= 278 \text{ kips}$</td>
</tr>
<tr>
  <td>Mechanical area:</td>
  <td>$(2{,}700 \text{ ft}^2)(0.3)(0.040 \text{ kip/ft}^2)$</td>
  <td>$= 32.4 \text{ kips}$</td>
</tr>
<tr>
  <td><strong>Total:</strong></td>
  <td></td>
  <td><strong>820 kips</strong></td>
</tr>
</table>

Typical third and fourth floor dead load:

Note: An additional 10 psf has been added to the floor dead load to account for partitions per ASCE/SEI 7, Section 12.7.2.

<table>
<tr>
  <td>Floor area:</td>
  <td>$(25{,}500 \text{ ft}^2)(0.085 \text{ kip/ft}^2)$</td>
  <td>$= 2{,}170 \text{ kips}$</td>
</tr>
<tr>
  <td>Wall perimeter:</td>
  <td>$(672 \text{ ft})(0.503 \text{ kip/ft})$</td>
  <td>$= 338 \text{ kips}$</td>
</tr>
<tr>
  <td><strong>Total:</strong></td>
  <td></td>
  <td><strong>2,510 kips</strong></td>
</tr>
</table>

Second floor dead load (the floor area is reduced because of the open atrium):

<table>
<tr>
  <td>Floor area:</td>
  <td>$(24{,}700 \text{ ft}^2)(0.085 \text{ kip/ft}^2)$</td>
  <td>$= 2{,}100 \text{ kips}$</td>
</tr>
<tr>
  <td>Wall perimeter:</td>
  <td>$(672 \text{ ft})(0.503 \text{ kip/ft})$</td>
  <td>$= 338 \text{ kips}$</td>
</tr>
<tr>
  <td><strong>Total:</strong></td>
  <td></td>
  <td><strong>2,440 kips</strong></td>
</tr>
</table>

Total dead load of the building:

---

# III-65

<table>
<tr><td>Roof</td><td>820 kips</td></tr>
<tr><td>Fourth floor</td><td>2,510 kips</td></tr>
<tr><td>Third floor</td><td>2,510 kips</td></tr>
<tr><td>Second floor</td><td>2,440 kips</td></tr>
<tr><td><strong>Total</strong></td><td><strong>8,280 kips</strong></td></tr>
</table>

Calculate the seismic forces.

Determine the seismic risk category and importance factors.

Office Building: Risk Category II, from ASCE/SEI 7, Table 1.5-1
Seismic Importance Factor: $I_e = 1.00$, from ASCE/SEI 7, Table 1.5-2

Because the soil properties are not known in sufficient detail to determine the site class, default site conditions are used per ASCE/SEI 7, Section 11.4.2.1. The risk-targeted maximum considered earthquake spectral response acceleration parameters, $S_{MS}$ and $S_{M1}$, are obtained for default site conditions in ASCE/SEI 7, Figures 22-1 through 22-2. The resulting parameters are $S_{MS} = 0.194g$ and $S_{M1} = 0.144g$.

Determine the design earthquake accelerations.

From ASCE/SEI 7, Equation 11.4-1:

$$S_{DS} = \frac{2}{3}S_{MS}$$ (ASCE/SEI 7, Eq. 11.4-1)
$$= \frac{2}{3}(0.194g)$$
$$= 0.129g$$

From ASCE/SEI 7, Equation 11.4-2:

$$S_{D1} = \frac{2}{3}S_{M1}$$ (ASCE/SEI 7, Eq. 11.4-2)
$$= \frac{2}{3}(0.144g)$$
$$= 0.096g$$

Determine the seismic design category from ASCE/SEI 7, Table 11.6-1 and Table 11.6-2.

With $S_{DS} < 0.167g$ and Risk Category II, Seismic Design Category A applies.

With $0.067g \leq S_{D1} < 0.133g$ and Risk Category II, Seismic Design Category B applies.

Select the seismic force-resisting system from ASCE/SEI 7, Table 12.2-1. For Seismic Design Category B, it is permissible to select a structural steel system not specifically detailed for seismic resistance (Item H). The response modification coefficient, *R*, is 3.

Determine the approximate fundamental period, $T_a$.

Building height, $h_n = 55.0$ ft

$C_t = 0.02$ and $x = 0.75$ from ASCE/SEI 7, Table 12.8-2 ("All other structural systems")

From ASCE/SEI 7, Equation 12.8-8:

---

# III-66

$$T_a = C_t h_n^x$$ (ASCE/SEI 7, Eq. 12.8-8)
$$= (0.02)(55.0 \text{ ft})^{0.75}$$
$$= 0.404 \text{ s}$$

Determine the redundancy factor from ASCE/SEI 7, Section 12.3.4.1.

ρ = 1.0, for Seismic Design Category B

From ASCE/SEI 7, Equation 12.4-4a, determine the vertical seismic effect term:

$$E_v = 0.2S_{DS}D$$ (ASCE/SEI 7, Eq. 12.4-4a)
$$= 0.2(0.129g)D$$
$$= 0.0258D$$

Note that per ASCE/SEI 7, Section 12.4.2.2, Exception 2, the vertical seismic load effect, $E_v$, is permitted to be taken as zero for structures in Seismic Design Category B.

From ASCE/SEI 7, Equation 12.4-3, determine the horizontal seismic effect term:

$$E_h = \rho Q_E$$ (ASCE/SEI 7, Eq. 12.4-3)
$$= 1.0(Q_E)$$

The following seismic load combinations are as specified in ASCE/SEI 7, Sections 2.3.6 and 2.4.5, as directed by Section 12.4.2. Where the prescribed seismic load effect, $E = \rho(E_h \pm E_v)$, is combined with the effects of other loads, the following load combinations apply. Note that $L = 0.5L$ for LRFD per ASCE/SEI 7, Section 2.3.6, Exception 1.

| LRFD | ASD |
|------|-----|
| $1.2D + E_v + E_h + L + 0.15S$ | $1.0D + 0.7E_v + 0.7E_h$ |
| $= 1.2D + 0.2S_{DS}D + \rho Q_E + 0.5L + 0.15S$ | $= 1.0D + 0.7(0.2S_{DS}D) + 0.7\rho Q_E$ |
| $= (1.2 + 0.0258)D + 1.0Q_E + 0.5L + 0.15S$ | $= [1.0 + 0.7(0.0258)]D + 0.7(1.0)Q_E$ |
| $= 1.23D + 1.0Q_E + 0.5L + 0.15S$ | $= 1.02D + 0.7Q_E$ |
|  |  |
| $0.9D - E_v + E_h$ | $1.0D + 0.525E_v + 0.525E_h + 0.75L + 0.1S$ |
| $= 0.9D - 0.2S_{DS}D + \rho Q_E$ | $= 1.0D + 0.525(0.2S_{DS}D) + 0.525\rho Q_E + 0.75L + 0.1S$ |
| $= (0.9 - 0.0258)D + 1.0Q_E$ | $= [1.0 + 0.525(0.0258)]D + 0.525(1.0)Q_E + 0.75L$ |
| $= 0.874D + 1.0Q_E$ | $+ 0.1S$ |
|  | $= 1.01D + 0.525Q_E + 0.75L + 0.1S$ |
|  |  |
|  | $0.6D - 0.7E_v + 0.7E_h$ |
|  | $= 0.6D - 0.7(0.2S_{DS}D) + 0.7\rho Q_E$ |
|  | $= [0.6 - 0.7(0.0258)]D + 0.7(1.0)Q_E$ |
|  | $= 0.582D + 0.7Q_E$ |

Where the prescribed seismic load effect with overstrength, $E = \rho(E_h, E_{mh})$, is combined with the effects of other loads, the following load combinations apply.

---

# III-67

The overstrength factor, $\Omega_0$, is determined from ASCE/SEI 7, Table 12.2-1. $\Omega_0 = 3$ for steel systems not specifically detailed for seismic resistance, excluding cantilever column systems.

Determine the horizontal seismic effect term including overstrength.

$$E_{mh} = \Omega_0 Q_E \leq E_{cl}$$ (from ASCE/SEI 7, Eq. 12.4-7)
$$= 3(Q_E)$$

where $Q_E$ is the effect from seismic forces from seismic base shear, $V$, as calculated per ASCE/SEI 7, Section 12.8.1; diaphragm design forces, $F_{px}$, as calculated per ASCE/SEI 7, Section 12.10; or seismic design force, $F_p$, as calculated per Section 13.3.1. The capacity-limited horizontal seismic load effect, $E_{cl}$, is defined in ASCE/SEI 7, Section 11.3.

| LRFD | ASD |
|------|-----|
| $1.2D + E_v + E_{mh} + L + 0.15S$ | $1.0D + 0.7E_v + 0.7E_{mh}$ |
| $= 1.2D + 0.2S_{DS}D + \Omega_0 Q_E + 0.5L + 0.15S$ | $= 1.0D + 0.7(0.2S_{DS}D) + 0.7\Omega_0 Q_E$ |
| $= (1.2 + 0.0258)D + 3Q_E + 0.5L + 0.15S$ | $= [1.0 + 0.7(0.0258)]D + 0.7(3)Q_E$ |
| $= 1.23D + 3.0Q_E + 0.5L + 0.15S$ | $= 1.02D + 2.1Q_E$ |
|  |  |
| $0.9D - E_v + E_{mh}$ | $1.0D + 0.525E_v + 0.525E_{mh} + 0.75L + 0.1S$ |
| $= 0.9D - 0.2S_{DS}D + \Omega_0 Q_E$ | $= 1.0D + 0.525(0.2S_{DS}D) + 0.525\Omega_0 Q_E + 0.75L + 0.1S$ |
| $= (0.9 - 0.0258)D + 3Q_E$ | $= [1.0 + 0.525(0.0258)]D + 0.525(3)Q_E + 0.75L$ |
| $= 0.874D + 3.0Q_E$ | $+ 0.1S$ |
|  | $= 1.01D + 1.58Q_E + 0.75L + 0.1S$ |
|  |  |
|  | $0.6D - 0.7E_v + 0.7E_{mh}$ |
|  | $= 0.6D - 0.7(0.2S_{DS}D) + 0.7\Omega_0 Q_E$ |
|  | $= [0.6 - 0.7(0.0258)]D + 0.7(3)Q_E$ |
|  | $= 0.582D + 2.1Q_E$ |

Calculate the seismic base shear using ASCE/SEI 7, Section 12.8.1. Method 2 is permitted to be used.

Determine the seismic response coefficient, $C_s$, from ASCE/SEI 7, Equation 12.8-3:

$$C_s = \frac{S_{DS}}{\left(\frac{R}{I_e}\right)}$$ (ASCE/SEI 7, Eq. 12.8-3)

$$= \frac{0.129}{\left(\frac{3}{1.00}\right)}$$

$$= 0.0430$$

Let $T_a = T$, as is permitted in Section 12.8.2. From ASCE/SEI 7, Figure 22-14, $T_L = 12$ s $> T$ (midwestern city); therefore, use ASCE/SEI 7, Equation 12.8-4, to determine the upper limit of $C_s$.

---

# III-68

$$C_s = \frac{S_{D1}}{T\left(\frac{R}{I_e}\right)}$$ (ASCE/SEI 7, Eq. 12.8-4)

$$= \frac{0.096}{0.404\left(\frac{3}{1.00}\right)}$$

$$= 0.0792$$

$C_s$ shall not be taken less than:

$$C_s = 0.044S_{DS}I_e \geq 0.01$$ (ASCE/SEI 7, Eq. 12.8-6)
$$= 0.044(0.129)(1.00) < 0.01$$
$$= 0.01$$

Therefore, $C_s = 0.0430$.

Calculate the seismic base shear from ASCE/SEI 7, Section 12.8.1:

$$V = C_s W$$ (ASCE/SEI 7, Eq. 12.8-1)
$$= 0.0430(8{,}280 \text{ kips})$$
$$= 356 \text{ kips}$$

Determine vertical distribution of seismic forces from ASCE/SEI 7, Section 12.8.3.

$$F_x = C_{vx}V$$ (ASCE/SEI 7, Eq. 12.8-12)
$$= C_{vx}(356 \text{ kips})$$

$$C_{vx} = \frac{w_x h_x^k}{\sum\limits_{i=1}^{n} w_i h_i^k}$$ (ASCE/SEI 7, Eq. 12.8-13)

For structures having a period of 0.5 s or less, $k = 1$.

Determine horizontal shear distribution at each level per ASCE/SEI 7, Section 12.8.4.

$$V_x = \sum_{i=x}^{n} F_i$$ (ASCE/SEI, Eq. 12.8-14)

Determine the overturning moment at each level per ASCE/SEI 7, Section 12.8.5.

$$M_x = \sum_{i=x}^{n} F_i(h_i - h_x)$$

The seismic forces at each level are summarized in Table III-8.

Calculate strength and determine rigidity of diaphragms.

Determine the diaphragm design forces from ASCE/SEI 7, Section 12.10.1.1.

---

# III-69

| **Table III-8<br>Summary of Seismic Forces at Each Level** |  |  |  |  |  |  |
|-----------------------------------------------------------|--|--|--|--|--|--|
|  | *w<sub>x</sub>*,<br>**kips** | *h<sub>x</sub>*<sup>k</sup>,<br>**ft** | *w<sub>x</sub>h<sub>x</sub>*<sup>k</sup>, | *C<sub>vx</sub>* | *F<sub>x</sub>*,<br>**kips** | *V<sub>x</sub>*,<br>**kips** | *M<sub>x</sub>*,<br>**kip-ft** |
| Roof | 820 | 55.0 | 45,100 | 0.182 | 64.8 | 64.8 |  |
| 4th | 2,510 | 40.5 | 102,000 | 0.411 | 146 | 211 | 940 |
| 3rd | 2,510 | 27.0 | 67,800 | 0.273 | 97.2 | 308 | 3,790 |
| 2nd | 2,440 | 13.5 | 32,900 | 0.133 | 47.3 | 355 | 7,940 |
| Base | **8,280** |  | **248,000** |  | **355** |  | **12,700** |

$F_{px}$ is the largest of:

1. The force $F_x$ at each level determined by the vertical distribution above

$$\sum_{i=x}^{n} F_i$$

2. $F_{px} = \frac{\sum\limits_{i=x}^{n}}{\sum\limits_{i=x}^{n} w_i} w_{px} \leq 0.4S_{DS}I_e w_{px}$, from ASCE/SEI 7, Equations 12.10-1 and 12.10-3

$$\leq 0.4(0.129)(1.00)w_{px}$$
$$\leq 0.0516w_{px}$$

3. $F_{px} = 0.2S_{DS}I_e w_{px}$, from ASCE/SEI 7, Equation 12.10-2
$$= 0.2(0.129)(1.00)w_{px}$$
$$= 0.0258w_{px}$$

The diaphragm shear forces include the effects of openings in the diaphragm (such as stair shafts).

An accidental torsion using an eccentricity of 5% of the building dimension per ASCE/SEI 7, Section 12.8.4.2.2, was applied. The resulting Torsional Irregularity Ratio (TIR) was calculated per ASCE/SEI 7, Section 12.3.2.1.1, to be less than 1.2. As such, a torsional irregularity is not present per ASCE/SEI 7, Table 12.3-1. Additionally, per ASCE/SEI 7, Section 12.8.4.2.1, accidental torsion does not need to be included in the analysis for a structure assigned to Seismic Design Category B with TIR ≤ 1.4 and with no torsional irregularity.

A summary of the diaphragm forces is given in Table III-9,

where
$F_{px}$ = max(*A*, *B*, *C*)
*A* = force at a level based on the vertical distribution of seismic forces

$$\sum_{i=x}^{n} F_i$$

*B* = $F_{px} = \frac{\sum\limits_{i=x}^{n}}{\sum\limits_{i=x}^{n} w_i} w_{px} \leq 0.4S_{DS}I_e w_{px}$

*C* = $0.2S_{DS}I_e w_{px}$
*L* = the length of the frame connected to the diaphragm (in the N-S or E-W direction)
*V* = shear force in the diaphragm

---

# III-70

| **Table III-9<br>Summary of Diaphragm Forces** |  |  |  |  |  |  |  |  |
|-----------------------------------------------|--|--|--|--|--|--|--|--|
|  | *w<sub>px</sub>*,<br>**kips** | *A*,<br>**kips** | *B*,<br>**kips** | *C*,<br>**kips** | *F<sub>px</sub>*,<br>**kips** | *L<sub>(N-S)</sub>*,<br>**ft** | *L<sub>(E-W)</sub>*,<br>**ft** | *V<sub>(N-S)</sub>*,<br>**plf** | *V<sub>(E-W)</sub>*,<br>**plf** |
| Roof | 820 | 64.8 | 42.3 | 21.2 | 64.8 | 240 | 420 | 270 | 154 |
| 4th | 2,510 | 146 | 130 | 64.8 | 146 | 180 | 420 | 811 | 348 |
| 3rd | 2,510 | 97.2 | 130 | 64.8 | 130 | 180 | 420 | 722 | 310 |
| 2nd | 2,440 | 47.3 | 105 | 63.0 | 105 | 180 | 420 | 583 | 254<sup>[b]</sup> |

[b]This diaphragm shear is increased from the inherent torsion resulting from the atrium opening.

*Roof*

Roof deck: 1½-in.-deep, 22 gage, wide rib
Support fasteners: ⅝ in. puddle welds in 36/5 pattern
Sidelap fasteners: (3) #10 TEK screws
Joist spacing: $s = 6.00$ ft
Diaphragm length: 210 ft
Diaphragm width: $l_v = 120$ ft

By inspection, the critical condition for the diaphragm is loading from the north or south directions.

| LRFD | ASD |
|------|-----|
| From the ASCE/SEI 7 load combinations for strength design, the earthquake load is: | From the ASCE/SEI 7 load combinations for allowable stress design, the earthquake load is: |
| $v_r = E_h$ | $v_r = 0.7E_h$ |
| $= \rho Q_E$ | $= 0.7\rho Q_E$ |
| $= 1.0(0.270 \text{ klf})$ | $= 0.7(1.0)(0.270 \text{ klf})$ |
| $= 0.270 \text{ klf}$ | $= 0.189 \text{ klf}$ |
|  |  |
| The wind load is: | The wind load is: |
| $v_r = 1.0W$ | $v_r = 0.6W$ |
| $= 1.0(0.428 \text{ klf})$ | $= 0.6(0.428 \text{ klf})$ |
| $= 0.428 \text{ klf}$ | $= 0.257 \text{ klf}$ |

From the SDI *Diaphragm Design Manual* (SDI, 2015), the available shear strengths are determined as follows:

For panel buckling strength: $v_n = 3.88$ klf
For connection strength: $v_n = 0.720$ klf

| LRFD | ASD |
|------|-----|
| Panel buckling strength: | Panel buckling strength: |
| $\phi v_n = 0.80(3.88 \text{ klf})$ | $\frac{v_n}{\Omega} = \frac{3.88 \text{ klf}}{2.00}$ |
| $= 3.10 \text{ klf} > 0.428 \text{ klf}$ **o.k.** | $= 1.94 \text{ klf} > 0.257 \text{ klf}$ **o.k.** |

---

# III-71

| LRFD | ASD |
|------|-----|
| Connection strength: | Connection strength: |
|  |  |
| Earthquake | Earthquake |
|  |  |
| $\phi v_n = 0.55(0.720 \text{ klf})$ | $\frac{v_n}{\Omega} = \frac{0.720 \text{ klf}}{3.00}$ |
| $= 0.396 \text{ klf} > 0.270 \text{ klf}$ **o.k.** | $= 0.240 \text{ klf} > 0.189 \text{ klf}$ **o.k.** |
|  |  |
| Wind | Wind |
|  |  |
| $\phi v_n = 0.70(0.720 \text{ klf})$ | $\frac{v_n}{\Omega} = \frac{0.720 \text{ klf}}{2.35}$ |
| $= 0.504 \text{ klf} > 0.428 \text{ klf}$ **o.k.** | $= 0.306 \text{ klf} > 0.257 \text{ klf}$ **o.k.** |

Check diaphragm flexibility.

From the SDI *Diaphragm Design Manual* (SDI, 2015):

$$D_{sx} = 607 \text{ ft}$$
$$K_1 = 0.286 \text{ ft}^{-1}$$
$$K_2 = 870 \text{ kip/in.}$$
$$K_4 = 3.55$$

From SDI *Diaphragm Design Manual*, Section 9:

$$G' = \frac{K_2}{K_4 + \frac{0.3D_{sx}}{s} + 3K_{1}s}$$

$$= \frac{870 \text{ kip/in.}}{3.55 + \frac{0.3(607 \text{ ft})}{6.00 \text{ ft}} + 3\left(\frac{0.286}{\text{ft}}\right)(6.00 \text{ ft})}$$

$$= 22.3 \text{ kip/in.}$$

Seismic loading on diaphragm.

$$w = \frac{64.8 \text{ kips}}{210 \text{ ft}}$$
$$= 0.309 \text{ klf}$$

Calculate the maximum diaphragm deflection.

$$\Delta = \frac{wL^2}{8l_v G'}$$

$$= \frac{(0.309 \text{ klf})(210 \text{ ft})^2}{8(120 \text{ ft})(22.3 \text{ kip/in.})}$$

$$= 0.637 \text{ in.}$$

Story drift = 0.140 in. (from computer output)

---

# III-72

The diaphragm deflection exceeds two times the story drift; therefore, the diaphragm may be considered to be flexible in accordance with ASCE/SEI 7, Section 12.3.1.3.

The roof diaphragm is flexible in the N-S direction, but using a rigid diaphragm distribution is more conservative for the analysis of this building. By similar reasoning, the roof diaphragm will also be treated as a rigid diaphragm in the E-W direction.

*Third and fourth floors*

Floor deck: 3-in.-deep, 22 gage, composite deck with normal weight concrete
Support fasteners: ⅝ in. puddle welds in a 36/4 pattern
Sidelap fasteners: (3) #10 TEK screws
Beam spacing: $s = 10$ ft
Diaphragm length: 210 ft
Diaphragm width: 120 ft
$l_v = 120$ ft − 30 ft = 90 ft, to account for the stairwell

By inspection, the critical condition for the diaphragm is loading from the north or south directions.

| LRFD | ASD |
|------|-----|
| From the ASCE/SEI 7 load combinations for strength design, the earthquake load for the fourth floor is: | From the ASCE/SEI 7 load combinations for strength design, the earthquake load for the fourth floor is: |
|  |  |
| $v_r = E_h$ | $v_r = E_h$ |
| $= \rho Q_E$ | $= 0.7\rho Q_E$ |
| $= 1.0(0.811 \text{ klf})$ | $= 0.7(1.0)(0.811 \text{ klf})$ |
| $= 0.811 \text{ klf}$ | $= 0.568 \text{ klf}$ |
|  |  |
| For the fourth floor, the wind load is: | For the fourth floor, the wind load is: |
|  |  |
| $v_r = 1.0W$ | $v_r = 0.6W$ |
| $= 1.0(0.487 \text{ klf})$ | $= 0.6(0.487 \text{ klf})$ |
| $= 0.487 \text{ klf}$ | $= 0.292 \text{ klf}$ |
|  |  |
| From the ASCE/SEI 7 load combinations for strength design, the earthquake load for the third floor is: | From the ASCE/SEI 7 load combinations for strength design, the earthquake load for the third floor is: |
|  |  |
| $v_r = E_h$ | $v_r = E_h$ |
| $= \rho Q_E$ | $= 0.7\rho Q_E$ |
| $= 1.0(0.722 \text{ klf})$ | $= 0.7(1.0)(0.722 \text{ klf})$ |
| $= 0.722 \text{ klf}$ | $= 0.505 \text{ klf}$ |
|  |  |
| For the third floor, the wind load is: | For the third floor, the wind load is: |
|  |  |
| $v_r = 1.0W$ | $v_r = 0.6W$ |
| $= 1.0(0.448 \text{ klf})$ | $= 0.6(0.448 \text{ klf})$ |
| $= 0.448 \text{ klf}$ | $= 0.269 \text{ klf}$ |

From the SDI *Diaphragm Design Manual* (SDI, 2015), the nominal connection shear strength is $v_n = 5.34$ klf.

---

# III-73

Calculate the available strengths.

| LRFD | ASD |
|------|-----|
| Connection Strength (same for earthquake or wind) (SDI, 2015) | Connection Strength (same for earthquake or wind) (SDI, 2015) |
|  |  |
| $\phi v_n = 0.5(5.34 \text{ klf})$ | $\frac{v_n}{\Omega} = \frac{5.34 \text{ klf}}{3.25}$ |
| $= 2.67 \text{ klf} > 0.811 \text{ klf}$ **o.k.** | $= 1.64 \text{ klf} > 0.568 \text{ klf}$ **o.k.** |

Check diaphragm flexibility.

From the SDI *Diaphragm Design Manual* (SDI, 2015):

$$K_1 = 0.318 \text{ ft}^{-1}$$
$$K_2 = 870 \text{ kip/in.}$$
$$K_3 = 2{,}380 \text{ kip/in.}$$
$$K_4 = 3.54$$

$$G' = \left(\frac{K_2}{K_4 + 3K_{1}s}\right) + K_3$$

$$= \left[\frac{870 \text{ kip/in.}}{3.54 + 3\left(\frac{0.318}{\text{ft}}\right)(10 \text{ ft})}\right] + 2{,}380 \text{ kip/in.}$$

$$= 2{,}450 \text{ kip/in.}$$

*Fourth floor*

Calculate seismic loading on the diaphragm based on the fourth floor seismic load.

$$w = \frac{146 \text{ kips}}{210 \text{ ft}}$$
$$= 0.695 \text{ klf}$$

Calculate the maximum diaphragm deflection on the fourth floor.

$$\Delta = \frac{wL^2}{8l_v G'}$$

$$= \frac{(0.695 \text{ klf})(210 \text{ ft})^2}{8(90 \text{ ft})(2{,}450 \text{ kip/in.})}$$

$$= 0.0174 \text{ in.}$$

*Third floor*

Calculate seismic loading on the diaphragm based on the third floor seismic load.

$$w = \frac{130 \text{ kips}}{210 \text{ ft}}$$
$$= 0.619 \text{ klf}$$

---

# III-74

Calculate the maximum diaphragm deflection on the third floor.

$$\Delta = \frac{wL^2}{8l_v G'}$$

$$= \frac{(0.619 \text{ klf})(210 \text{ ft})^2}{8(90 \text{ ft})(2{,}450 \text{ kip/in.})}$$

$$= 0.0155 \text{ in.}$$

Story drift = 0.268 in. (from computer output)

The diaphragm deflection at the third and fourth floors is less than two times the story drift; therefore, the diaphragm is considered rigid in accordance with ASCE/SEI 7, Section 12.3.1.3. By inspection, the floor diaphragm will also be rigid in the E-W direction.

*Second floor*

Floor deck: 3-in.-deep, 22 gage, composite deck with normal weight concrete
Support fasteners: ⅝ in. puddle welds in a 36/4 pattern
Sidelap fasteners: (3) #10 TEK screws
Beam spacing: $s = 10$ ft
Diaphragm length: 210 ft
Diaphragm width: 120 ft

Because of the atrium opening in the floor diaphragm, an effective diaphragm depth of 75 ft will be used for the deflection calculations.

By inspection, the critical condition for the diaphragm is loading from the north or south directions.

| LRFD | ASD |
|------|-----|
| From the ASCE/SEI 7 load combinations for strength design, the earthquake load is: | From the ASCE/SEI 7 load combinations for strength design, the earthquake load is: |
|  |  |
| $v_r = E_h$ | $v_r = E_h$ |
| $= \rho Q_E$ | $= 0.7\rho Q_E$ |
| $= 1.0(0.583 \text{ klf})$ | $= 0.7(1.0)(0.583 \text{ klf})$ |
| $= 0.583 \text{ klf}$ | $= 0.408 \text{ klf}$ |
|  |  |
| The wind load is: | The wind load is: |
|  |  |
| $v_r = 1.0W$ | $v_r = 0.6W$ |
| $= 1.0(0.418 \text{ klf})$ | $= 0.6(0.418 \text{ klf})$ |
| $= 0.418 \text{ klf}$ | $= 0.251 \text{ klf}$ |

From the SDI *Diaphragm Design Manual* (SDI, 2015), the nominal connection shear strength is: $v_n = 5.34$ klf.

Calculate the available strengths.

---

# III-75

| LRFD | ASD |
|------|-----|
| Connection Strength (same for earthquake or wind) (SDI, 2015) | Connection Strength (same for earthquake or wind) (SDI, 2015) |
|  |  |
| $\phi v_n = 0.50(5.34 \text{ klf})$ | $\frac{v_n}{\Omega} = \frac{5.34 \text{ klf}}{3.25}$ |
| $= 2.67 \text{ klf} > 0.583 \text{ klf}$ **o.k.** | $= 1.64 \text{ klf} > 0.408 \text{ klf}$ **o.k.** |

Check diaphragm flexibility.

From the SDI *Diaphragm Design Manual* (SDI, 2015):

$$K_1 = 0.318 \text{ ft}^{-1}$$
$$K_2 = 870 \text{ kip/in.}$$
$$K_3 = 2{,}380 \text{ kip/in.}$$
$$K_4 = 3.54$$

$$G' = \left(\frac{K_2}{K_4 + 3K_{1}s}\right) + K_3$$

$$= \left[\frac{870 \text{ kip/in.}}{3.54 + 3\left(\frac{0.318}{\text{ft}}\right)(10 \text{ ft})}\right] + 2{,}380 \text{ kip/in.}$$

$$= 2{,}450 \text{ kip/in.}$$

Calculate seismic loading on the diaphragm.

$$w = \frac{105 \text{ kips}}{210 \text{ ft}}$$
$$= 0.500 \text{ klf}$$

Calculate the maximum diaphragm deflection.

$$\Delta = \frac{wL^2}{8bG'}$$

$$= \frac{(0.500 \text{ klf})(210 \text{ ft})^2}{8(75 \text{ ft})(2{,}450 \text{ kip/in.})}$$

$$= 0.0150 \text{ in.}$$

Story drift = 0.210 in. (from computer output)

The diaphragm deflection is less than two times the story drift; therefore, the diaphragm is considered rigid in accordance with ASCE/SEI 7, Section 12.3.1.3. By inspection, the floor diaphragm will also be rigid in the E-W direction.

*Horizontal Shear Distribution and Torsion*

The seismic forces to be applied in the frame analysis in each direction, including the effect of accidental torsion, are shown in Tables III-10 and III-11.

---

# III-76

| **Table III-10<br>Horizontal Shear Distribution Including Accidental Torsion—Grids 1 and 8** |  |  |  |  |  |
|----------------------------------------------------------------------------------------------|--|--|--|--|--|
|  | *F<sub>x</sub>*,<br>**kips** | **Load on Frame** |  | **Load to Grids 1 and 8<br>Accidental Torsion** |  | **Total,<br>kips** |
|  |  | **%** | **kips** | **%** | **kips** |  |
| Roof | 64.8 | 50 | 32.4 | 5 | 3.24 | 35.6 |
| 4th | 146 | 50 | 73.0 | 5 | 7.30 | 80.3 |
| 3rd | 97.2 | 50 | 48.6 | 5 | 4.86 | 53.5 |
| 2nd | 47.3 | 50 | 23.7 | 5 | 2.37 | 26.1 |
| Base |  |  | 178 |  |  | 196 |

| **Table III-11<br>Horizontal Shear Distribution Including Accidental Torsion—Grids A and F** |  |  |  |  |  |
|----------------------------------------------------------------------------------------------|--|--|--|--|--|
|  | *F<sub>x</sub>*,<br>**kips** | **Load on Frame** |  | **Load to Grids A and F<br>Accidental Torsion** |  | **Total,<br>kips** |
|  |  | **%** | **kips** | **%** | **kips** |  |
| Roof | 64.8 | 50 | 32.4 | 5 | 3.24 | 35.6 |
| 4th | 146 | 50 | 73.0 | 5 | 7.30 | 80.3 |
| 3rd | 97.2 | 50 | 48.6 | 5 | 4.86 | 53.5 |
| 2nd | 47.3 | 50.8<sup>[b]</sup> | 24.0 | 5 | 2.37 | 26.4 |
| Base |  |  | 178 |  |  | 196 |

[b]Note: In this example, Grids A and F have both been conservatively designed for the slightly higher load on Grid A due to the atrium opening. The increase in load is calculated in Table III-12.

| **Table III-12** |  |  |  |  |
|------------------|--|--|--|--|
|  | **Area,<br>ft²** | **Mass,<br>kips** | **y-dist,<br>ft** | *M<sub>y</sub>*,<br>**kip-ft** |
| I | 25,500 | 2,170 | 60.5 | 131,000 |
| II | 841 | 71.5 | 90.5 | 6,470 |
| Base | 24,700 | 2,100 |  | 125,000 |

$$y = \frac{125{,}000 \text{ kip-ft}}{2{,}100 \text{ kips}}$$
$$= 59.5 \text{ ft}$$

$$(100\%)\frac{(121 \text{ ft} - 59.5 \text{ ft})}{121 \text{ ft}} = 50.8\%$$

Per ASCE/SEI 7, Section 12.8.4.2.1, accidental torsion is required to be considered when determining if a horizontal irregularity exists. Because the TIR calculated in accordance with ASCE/SEI, Section 12.3.2.1.1, is less than 1.2, a torsional irregularity does not exist. Additionally, not more than 75% of any story's lateral strength below the diaphragm is provided at or on one side of the center of mass per ASCE/SEI 7, Table 12.3-1. Accidental eccentricity is not required to be considered in the design of the structure because this structure is assigned to Seismic Design Category B and does not have a Type 1 horizontal structural irregularity with a TIR > 1.4.

---

# III-77

## MOMENT FRAME MODEL

Grids 1 and 8 were modeled in conventional structural analysis software as two-dimensional models. The second-order analysis program was not written to provide automated features to account for all load effects nor calculated separately, using the "Approximate Second-Order Analysis" method described in AISC Specification Appendix 8. The results produced by this program are used for comparative purposes, other than to state that: a simplified (first-order) approach gives results that were comparable to those derived from the second-order analysis model. The second-order analysis was modeled considering the following: the design of Grids A and F slightly heavier seismic loads accumulate on Grid A after accounting for the atrium area. The models use half-building models (from the centerline of the bays) for computational efficiencies. The models use half the loads and half the inertia to produce the same results in the analysis. To fully understand this, see Example Appendix 1 for a discussion of the modified AISC Specification increases for W14-455 and the W21-68 beams were applied to W24-55 beams. Minimum composite slab are considered in the analysis with the intention that they represent all 16, the flexibility of semi-rigid composite beam-to-column connections is considered. In the design for Seismic Design Category E, for beams ky = 1.

The frame was checked for both wind and seismic story drift limits. Based on the results of the computer analysis, the Building Code Compliance Officer would confirm the building conforms to the Drift Limits described in ASCE/SEI 7, Commentary Section C2.2.3. In addition, the frame meets the 0.025hs, allowable story drift limit given in ASCE/SEI 7, Table 12.12-1, for Category B.

As explained previously for the beams in this example, a significant portion of the stiffness of the composite beam comes from the load cases that follow. The wind, seismic, and reduced loads from bearing columns are modeled and distributed per Example C12. For columns with varying stiffness, the approach minimizes the tendency to accumulate two different load paths for load cases in accordance with Chapter 1 of the Specification.

Also shown in the following models are the simulated of the half-building model gravity loads from the interior leaning columns accumulated in a single leaning column that was connected to the plane portions of the model with horizontal rigid links (a rigid diaphragm). This gravity column is associated with half the weight of the leaning columns. A simplified (first-order) approach given in AISC Specification Appendix 8, the inclusion of the leaning column in unnecessary, but serves to accumulate the leaning column loads and illustrates how these might be bundled in a full structural analysis computer program. That is, in the two-dimensional analysis of a half-building model, nominally loaded, but, roof floor, and seismic loads are shown in Figures III-15 through III-23.

There are five lateral load cases. Two are the wind load and seismic loads per the previous discussion. In addition, the two analysis will be handled by using a rigid diaphragm structure. With the AISC Specification Appendix 8 for the seismic load case uses the assumed notional loads, with loads, and seismic loads are shown in Figures III-15 through III-23.

The same modeling procedures were used in the braced frame analysis. If columns bars are not fixed in construction, they should not be fixed in the analysis.

---

# III-78

**Fig. III-15. Frame layout—Grid A and F.**

Diagram description: Frame elevation showing an 8-bay moment frame with columns numbered 1 through 8. The frame has four floor levels with story heights of 13'-6" each. Beam sizes shown are W18×35 (typ. @ roof) and W24×55 (typ. @ floor) at different levels. Columns labeled as W24x55 and W12x40 at gridlines. Base connections shown with hatching indicating fixed supports.

---

**Fig. III-16. Nominal dead loads—Grid A and F.**

Diagram description: Dead load distribution showing vertical loads applied to the frame at beam-column connections:
- Top level: 17.7 kips at column 1, 26.2 kips at columns 2-7, 17.7 kips at column 8, with total 272 kips at leaning column
- Second level: 35.8 kips at column 1, 66.9 kips at columns 2-7, 35.8 kips at column 8, with total 652 kips at leaning column
- Third level: same as second level (35.8/66.9/35.8 kips, 652 kips total)
- Fourth level: same as second level (35.8/66.9/35.8 kips, 652 kips total)

---

**Fig. III-17. Notional dead loads—Grid A and F.**

Diagram description: Notional dead load distribution showing horizontal loads applied at each floor level:
- Top level: 0.0744 kips at columns 1 and 8, 0.130 kips at columns 2-7
- Second level: 0.165 kips at columns 1 and 8, 0.320 kips at columns 2-7
- Third level: same as second level (0.165/0.320 kips)
- Fourth level: same as second level (0.165/0.320 kips)

---

# III-79

**Fig. III-18. Nominal live loads—Grid A and F.**

Diagram description: Live load distribution showing vertical loads applied to the frame at beam-column connections:
- Top level: 11.9 kips at columns 1 and 8, 22.9 kips at columns 2-7, with total 265 kips at leaning column
- Second level: same as top level (11.9/22.9 kips, 265 kips total)
- Third level: same as top level (11.9/22.9 kips, 265 kips total)

---

**Fig. III-19. Notional live loads—Grid A and F.**

Diagram description: Notional live load distribution showing horizontal loads applied at each floor level:
- Top level: 0.0617 kips at columns 1 and 8, 0.122 kips at columns 2-7
- Second level: same as top level (0.0617/0.122 kips)
- Third level: same as top level (0.0617/0.122 kips)

---

**Fig. III-20. Nominal roof live loads—Grid A and F.**

Diagram description: Roof live load distribution showing vertical loads applied only at the top level:
- 5.60 kips at columns 1 and 8, 8.28 kips at columns 2-7, with total 98.5 kips at leaning column
- No loads at lower floor levels

---

# III-80

**Fig. III-21. Notional roof live loads—Grid A and F.**

Diagram description: Notional roof live load distribution showing horizontal loads applied only at the top level:
- 0.0228 kips at columns 1 and 8, 0.0455 kips at columns 2-7
- No loads at lower floor levels

---

**Fig. III-22. Nominal snow loads—Grid A and F.**

Diagram description: Snow load distribution showing vertical loads applied only at the top level:
- 7.82 kips at columns 1 and 8, 17.0 kips at columns 2-7, with total 197 kips at leaning column
- No loads at lower floor levels

---

**Fig. III-23. Notional snow loads—Grid A and F.**

Diagram description: Notional snow load distribution showing horizontal loads applied only at the top level:
- 0.0438 kips at columns 1 and 8, 0.0903 kips at columns 2-7
- No loads at lower floor levels

---

# III-81

## CALCULATION OF REQUIRED STRENGTH—THREE METHODS

Three methods for checking one of the typical interior column designs at the base of the building are presented below. All three of the methods presented require a second-order analysis (or calculation of required strength direct via computer analysis techniques or by amplifying a first-order analysis). A fourth method called the "First-Order Analysis Method" is also an option. This method does not require a second-order analysis, but it is presented below. For additional guidance on applying any of these methods, see the discussion in AISC *Manual* Part 2 titled Required Strength, Stability, Effective Length, and Second-Order Effects.

## GENERAL INFORMATION FOR ALL THREE METHODS

Seismic load combinations controlled over wind load combinations in the direction of the moment frames in the example building. The frame analysis was run for all LRFD and ASD load combinations; however, only the controlling combinations have been illustrated in the following examples. A lateral load of 0.2% of gravity load was included for all gravity-only load combinations per AISC *Manual* Part 2.

The second-order analysis for all of the following examples were carried out by doing a first-order analysis and then amplifying the results to achieve a set of second-order design forces using the approximate second-order analysis procedure from AISC *Specification* Appendix 8.

**Fig. III-24. Nominal wind loads (1.0W)—Grid A and F.**

Diagram description: Wind load distribution showing horizontal loads applied at each floor level:
- Top level: 1.91 kips at columns 1 and 8, 3.83 kips at columns 2-7
- Second level: 1.81 kips at columns 1 and 8, 3.61 kips at columns 2-7
- Third level: 1.66 kips at columns 1 and 8, 3.31 kips at columns 2-7
- Fourth level: 1.55 kips at columns 1 and 8, 3.10 kips at columns 2-7

---

**Fig. III-25. Seismic loads (1.0Q<sub>E</sub>)—Grid A and F.**

Diagram description: Seismic load distribution showing horizontal loads applied at each floor level:
- Top level: 2.31 kips at columns 1 and 8, 4.63 kips at columns 2-7
- Second level: 5.21 kips at columns 1 and 8, 10.4 kips at columns 2-7
- Third level: 3.47 kips at columns 1 and 8, 6.94 kips at columns 2-7
- Fourth level: 1.71 kips at columns 1 and 8, 3.43 kips at columns 2-7

---

# III-82

## METHOD 1—DIRECT ANALYSIS METHOD

Design for stability by the direct analysis method is found in AISC *Specification* Chapter C. This method requires that both the flexural and axial stiffness are reduced when the lateral loads are applied in the analysis to account for geometric imperfections and inelasticity, per AISC *Specification* Section C2.2b(a). Any general second-order analysis program that considers both *P*-δ and *P*-Δ effects is permitted. The simplified first-order analysis method of AISC *Specification* Appendix 8 is also permitted provided that the *B*₁ and *B*₂ factors are based on the reduced flexural and axial stiffnesses. A summary of the axial loads, moments, and first floor drifts from the first-order analysis is shown in the following. The floor diaphragm deflection in the east-west direction was previously determined to be very small and will thus be neglected in these calculations. Second-order member forces are determined using the approximate procedure of AISC *Specification* Appendix 8.

It was assumed, subject to verification, that *B*₂ is less than 1.7 for each load combination; therefore, per AISC *Specification* Section C2.2b(d), the notional loads were applied to the gravity-only load combinations. The required seismic load combinations, as given in ASCE/SEI 7, Sections 2.3.6 and 2.4.5, were derived previously.

| LRFD | ASD |
|------|-----|
| $1.23D + 1.0Q_E + 0.5L + 0.15S$ | $1.02D + 0.7Q_E$ |
| (Controls column) | (Controls column) |
|  |  |
| From a first-order analysis with notional loads where appropriate and reduced stiffnesses: | From a first-order analysis with notional loads where appropriate and reduced stiffnesses: |
|  |  |
| For interior column design | For interior column design |
|  |  |
| $P_r = 316 \text{ kips}$ | $P_a = 232 \text{ kips}$ |
| $M_{u1} = 134 \text{ kip-ft (from first-order analysis)}$ | $M_{a1} = 94.0 \text{ kip-ft}$ |
| $M_{u2} = 211 \text{ kip-ft (from first-order analysis)}$ | $M_{a2} = 147 \text{ kip-ft}$ |
|  |  |
| First story drift with reduced stiffnesses = 0.650 in. | First story drift with reduced stiffnesses = 0.456 in. |

Note: For ASD, ordinarily the second-order analysis must be carried out under 1.6 times the ASD load combinations and the results must be divided by 1.6 to obtain the required strengths. For this example, second-order analysis by the approximate *B*₁-*B*₂ analysis method is used. This method incorporates the 1.6 multiplier directly in the *B*₁ and *B*₂ amplifiers, such that no other modification is needed.

The required second-order flexural strength, $M_r$, and required axial strength, $P_r$, are determined as follows. For typical interior columns, the gravity-load moments are approximately balanced, therefore, $M_{nt}$ = 0 kip-ft.

Calculate the amplified forces and moments in accordance with AISC *Specification* Appendix 8 at the ground floor. The required second-order flexural strength is determined as follows:

$$M_r = B_1 M_{nt} + B_2 M_{lt}$$ (*Spec.* Eq. A-8-1)

*Determine B₁*

Per AISC *Specification* Appendix 8, Section 8.1.2, note that for members subject to axial compression, *B*₁ may be calculated based on the first-order estimate; therefore:

$$P_r = P_{nt} + P_{lt}$$

where
$P_r$ = required second-order axial strength using LRFD or ASD load combinations

---

# III-83

From AISC *Specification* Appendix 8, Section 8.1.2, the *B*₁ multiplier for the W14×90 column is determined as follows:

| LRFD | ASD |
|------|-----|
| $B_1 = \frac{C_m}{1 - \alpha P_r / P_{e1}} \geq 1$ (*Spec.* Eq. A-8-3) | $B_1 = \frac{C_m}{1 - \alpha P_r / P_{e1}} \geq 1$ (*Spec.* Eq. A-8-3) |
|  |  |
| where | where |
| $P_r = 316 \text{ kips (from first-order computer analysis)}$ | $P_r = 232 \text{ kips (from first-order computer analysis)}$ |
| $I_x = 999 \text{ in.}^4$ | $I_x = 999 \text{ in.}^4$ |
| $\tau_b = 1.0$ [to be verified per *Spec.* Section C2.3(b)] | $\tau_b = 1.0$ [to be verified per *Spec.* Section C2.3(b)] |
| $\alpha = 1.0$ | $\alpha = 1.6$ |
|  |  |
| As discussed in AISC *Specification* Appendix 8, Section 8.1.2, $EI^* = 0.8\tau_b EI$ when using the direct analysis method. | As discussed in AISC *Specification* Appendix 8, Section 8.1.2, $EI^* = 0.8\tau_b EI$ when using the direct analysis method. |
|  |  |
| $P_{e1} = \frac{\pi^2 EI^*}{(L_{c1})^2}$ (*Spec.* Eq. A-8-5) | $P_{e1} = \frac{\pi^2 EI^*}{(L_{c1})^2}$ (*Spec.* Eq. A-8-5) |
|  |  |
| $= \frac{\pi^2 (0.8)(1.0)(29{,}000 \text{ ksi})(999 \text{ in.}^4)}{\left[(1.0)(13.5 \text{ ft})(12 \text{ in./ft})\right]^2}$ | $= \frac{\pi^2 (0.8)(1.0)(29{,}000 \text{ ksi})(999 \text{ in.}^4)}{\left[(1.0)(13.5 \text{ ft})(12 \text{ in./ft})\right]^2}$ |
|  |  |
| $= 8{,}720 \text{ kips}$ | $= 8{,}720 \text{ kips}$ |
|  |  |
| $C_m = 0.6 - 0.4(M_1/M_2)$ (*Spec.* Eq. A-8-4) | $C_m = 0.6 - 0.4(M_1/M_2)$ (*Spec.* Eq. A-8-4) |
| $= 0.6 - 0.4(134 \text{ kip-ft}/211 \text{ kip-ft})$ | $= 0.6 - 0.4(94.0 \text{ kip-ft}/147 \text{ kip-ft})$ |
| $= 0.346$ | $= 0.344$ |
|  |  |
| $B_1 = \frac{0.346}{1 - \frac{1.0(316 \text{ kips})}{8{,}720 \text{ kips}}} < 1$ | $B_1 = \frac{0.344}{1 - \frac{1.6(232 \text{ kips})}{8{,}720 \text{ kips}}} < 1$ |
|  |  |
| $= 0.359 < 1$ | $= 0.359 < 1$ |
|  |  |
| Therefore, use $B_1 = 1$ | Therefore, use $B_1 = 1$ |

*Determine B₂*

| LRFD | ASD |
|------|-----|
| $P_{mf} = 2{,}240 \text{ kips (gravity load in moment frame)}$ | $P_{mf} = 1{,}640 \text{ kips (gravity load in moment frame)}$ |
| $P_{story} = 5{,}410 \text{ kips (from computer output)}$ | $P_{story} = 3{,}920 \text{ kips (from computer output)}$ |
| $\Delta_H = 0.650 \text{ in. (from computer output)}$ | $\Delta_H = 0.456 \text{ in. (from computer output)}$ |
| $\alpha = 1.0$ | $\alpha = 1.6$ |
|  |  |
| $R_M = 1 - 0.15(P_{mf}/P_{story})$ (*Spec.* Eq. A-8-8) | $R_M = 1 - 0.15(P_{mf}/P_{story})$ (*Spec.* Eq. A-8-8) |
|  |  |
| $= 1 - 0.15\left(\frac{2{,}240 \text{ kips}}{5{,}410 \text{ kips}}\right)$ | $= 1 - 0.15\left(\frac{1{,}640 \text{ kips}}{3{,}920 \text{ kips}}\right)$ |
|  |  |
| $= 0.938$ | $= 0.937$ |

---

# III-84

| LRFD | ASD |
|------|-----|
| From previous seismic force distribution calculations: | From previous seismic force distribution calculations: |
|  |  |
| $H = 1.0Q_E$ (Lateral) | $H = 0.7Q_E$ (Lateral) |
| $= 1.0(178 \text{ kips})$ | $= 0.7(178 \text{ kips})$ |
| $= 178 \text{ kips}$ | $= 125 \text{ kips}$ |
|  |  |
| $P_{e\text{-}story} = R_M \frac{HL}{\Delta_H}$ (*Spec.* Eq. A-8-7) | $P_{e\text{-}story} = R_M \frac{HL}{\Delta_H}$ (*Spec.* Eq. A-8-7) |
|  |  |
| $= (0.938)\frac{(178 \text{ kips})(13.5 \text{ ft})(12 \text{ in./ft})}{0.650 \text{ in.}}$ | $= (0.937)\frac{(125 \text{ kips})(13.5 \text{ ft})(12 \text{ in./ft})}{0.456 \text{ in.}}$ |
|  |  |
| $= 41{,}600 \text{ kips}$ | $= 41{,}600 \text{ kips}$ |
|  |  |
| $B_2 = \frac{1}{1 - \frac{\alpha P_{story}}{P_{e\text{-}story}}} \geq 1$ (*Spec.* Eq. A-8-6) | $B_2 = \frac{1}{1 - \frac{\alpha P_{story}}{P_{e\text{-}story}}} \geq 1$ (*Spec.* Eq. A-8-6) |
|  |  |
| $= \frac{1}{1 - \frac{1.0(5{,}410 \text{ kips})}{41{,}600 \text{ kips}}} > 1$ | $= \frac{1}{1 - \frac{1.6(3{,}920 \text{ kips})}{41{,}600 \text{ kips}}} > 1$ |
|  |  |
| $= 1.15 > 1$ | $= 1.18 > 1$ |
|  |  |
| Because *B*₂ < 1.7, it is verified that it was unnecessary to add the notional loads to the lateral loads for this load combination. | Because *B*₂ < 1.7, it is verified that it was unnecessary to add the notional loads to the lateral loads for this load combination. |

*Calculate amplified moment and axial load*

From AISC *Specification* Equation A-8-1, the required second-order flexural strength is determined as follows:

| LRFD | ASD |
|------|-----|
| $M_r = B_1 M_{nt} + B_2 M_{lt}$ | $M_r = B_1 M_{nt} + B_2 M_{lt}$ |
| $= (1.0)(0 \text{ kip-ft}) + (1.15)(211 \text{ kip-ft})$ | $= (1.0)(0 \text{ kip-ft}) + (1.18)(147 \text{ kip-ft})$ |
| $= 242 \text{ kip-ft}$ | $= 173 \text{ kip-ft}$ |

The required second-order axial strength is determined using AISC *Specification* Equation A-8-2 as follows. Note, for a long frame such as this one, the change in load to the interior columns associated with lateral load is negligible.

| LRFD | ASD |
|------|-----|
| $P_{nt} = 316 \text{ kips (from computer analysis)}$ | $P_{nt} = 232 \text{ kips (from computer analysis)}$ |
|  |  |
| $P_r = P_{nt} + B_2 P_{lt}$ | $P_r = P_{nt} + B_2 P_{lt}$ |
| $= 316 \text{ kips} + (1.15)(0 \text{ kips})$ | $= 232 \text{ kips} + (1.18)(0 \text{ kips})$ |
| $= 316 \text{ kips}$ | $= 232 \text{ kips}$ |

Note the flexural and axial stiffnesses of all members in the moment frame were reduced using 0.8*E* in the computer analysis.

Check that the flexural stiffness was adequately reduced for the analysis per AISC *Specification* Section C2.3(b)(1).

---

# III-85

| LRFD | ASD |
|------|-----|
| $\alpha = 1.0$ | $\alpha = 1.6$ |
| $P_r = 316 \text{ kips}$ | $P_r = 232 \text{ kips}$ |
|  |  |
| Because the W14×90 column is nonslender: | Because the W14×90 column is nonslender: |
|  |  |
| $P_{ns} = F_y A_g$ | $P_{ns} = F_y A_g$ |
| $= (50 \text{ ksi})(26.5 \text{ in.}^2)$ | $= (50 \text{ ksi})(26.5 \text{ in.}^2)$ |
| $= 1{,}330 \text{ kips}$ | $= 1{,}330 \text{ kips}$ |
|  |  |
| $\frac{\alpha P_r}{P_{ns}} = \frac{1.0(316 \text{ kips})}{1{,}330 \text{ kips}}$ | $\frac{\alpha P_r}{P_{ns}} = \frac{1.6(232 \text{ kips})}{1{,}330 \text{ kips}}$ |
|  |  |
| $= 0.238$ | $= 0.279$ |
|  |  |
| Because $\alpha P_r / P_{ns} \leq 0.5$: | Because $\alpha P_r / P_{ns} \leq 0.5$: |
|  |  |
| $\tau_b = 1.0$ | $\tau_b = 1.0$ |
|  |  |
| Therefore, the previous assumption is verified. | Therefore, the previous assumption is verified. |

Note: By inspection $\tau_b = 1.0$ for all of the beams in the moment frame.

*Interaction of Flexure and Axial Force*

From AISC *Specification* Section H1, interaction of flexure and axial force are checked as follows. From AISC *Specification* Section C3, *K* = 1.0 using the direct analysis method, therefore:

$$L_c = KL$$
$$= 1.0(13.5 \text{ ft})$$
$$= 13.5 \text{ ft}$$

| LRFD | ASD |
|------|-----|
| From AISC *Manual* Table 6-1, for a W14×90, with $L_c = 13.5$ ft: | From AISC *Manual* Table 6-1, for a W14×90, with $L_c = 13.5$ ft: |
|  |  |
| $P_c = \phi_c P_n$ | $P_c = \frac{P_n}{\Omega_b}$ |
| $= 1{,}040 \text{ kips}$ | $= 690 \text{ kips}$ |
|  |  |
| From AISC *Manual* Table 6-1, for a W14×90, with $L_b = 13.5$ ft: | From AISC *Manual* Table 6-1, for a W14×90, with $L_b = 13.5$ ft: |
|  |  |
| $M_{cx} = \phi_b M_{nx}$ | $M_{cx} = \frac{M_{nx}}{\Omega_b}$ |
| $= 574 \text{ kip-ft}$ | $= 382 \text{ kip-ft}$ |
|  |  |
| $\frac{P_r}{P_c} = \frac{316 \text{ kips}}{1{,}040 \text{ kips}}$ | $\frac{P_r}{P_c} = \frac{232 \text{ kips}}{690 \text{ kips}}$ |
|  |  |
| $= 0.304$ | $= 0.336$ |

---

# III-86

| LRFD | ASD |
|------|-----|
| Because $\frac{P_r}{P_c} \geq 0.2$, use AISC *Specification* Equation H1-1a: | Because $\frac{P_r}{P_c} \geq 0.2$, use AISC *Specification* Equation H1-1a: |
|  |  |
| $\frac{P_r}{P_c} + \left(\frac{8}{9}\right)\left(\frac{M_{rx}}{M_{cx}} + \frac{M_{ry}}{M_{cy}}\right) \leq 1.0$ | $\frac{P_r}{P_c} + \left(\frac{8}{9}\right)\left(\frac{M_{rx}}{M_{cx}} + \frac{M_{ry}}{M_{cy}}\right) \leq 1.0$ |
|  |  |
| $0.304 + \left(\frac{8}{9}\right)\left(\frac{242 \text{ kip-ft}}{574 \text{ kip-ft}} + 0\right) < 1.0$ | $0.336 + \left(\frac{8}{9}\right)\left(\frac{173 \text{ kip-ft}}{382 \text{ kip-ft}} + 0\right) < 1.0$ |
|  |  |
| $0.679 < 1.0$ **o.k.** | $0.739 < 1.0$ **o.k.** |

---

# III-87

## METHOD 2—EFFECTIVE LENGTH METHOD

Required strengths of frame members must be determined from a second-order analysis. In this example, the second-order analysis is performed by amplifying the first order axial and flexural moments in members and connections from an approximate analysis using the provisions of AISC *Specification* Appendix 8. The available strengths of compression members are calculated using effective length factors computed using stability analysis.

A first-order frame analysis is conducted using the load combinations for LRFD or ASD. A minimum lateral load (notional load) equal to 0.2% of the gravity loads is included for any gravity-only load combination as summarized in AISC *Manual* Part 2 titled "Required Strength, Stability, Effective Length, and Second-Order Effects." The required load combinations are given in ASCE/SEI 7.

A summary of the axial loads, moments, and 1st floor drifts from the first-order computer analysis is shown below. The floor diaphragm deflection in the east-west direction was previously determined to be very small and will thus be neglected in these calculations.

| LRFD | ASD |
|------|-----|
| $1.23D + 1.0Q_E + 0.5L + 0.15S$ | $1.02D + 0.7Q_E$ |
| (Controls columns) | (Controls columns) |
|  |  |
| For interior column design: | For interior column design: |
|  |  |
| $P_r = 316 \text{ kips}$ | $P_a = 232 \text{ kips}$ |
| $M_{u1} = 134 \text{ kip-ft (from first-order analysis)}$ | $M_{a1} = 94.0 \text{ kip-ft (from first-order analysis)}$ |
| $M_{u2} = 211 \text{ kip-ft (from first-order analysis)}$ | $M_{a2} = 147 \text{ kip-ft (from first-order analysis)}$ |
|  |  |
| First-order story drift = 0.520 in. | First-order story drift = 0.365 in. |

The required second-order flexural strength, $M_r$, and axial strength, $P_r$, are calculated as follows. For typical interior columns, the gravity load moments are approximately balanced; therefore, $M_{nt}$ = 0 kip-ft.

Calculate the amplified forces and moments in accordance with AISC *Specification* Appendix 8 at the ground floor. The required second-order flexural strength is determined as follows:

$$M_r = B_1 M_{nt} + B_2 M_{lt}$$ (*Spec.* Eq. A-8-1)

*Determine B₁*

Per AISC *Specification* Appendix 8, Section 8.1.2, note that for members subject to axial compression, *B*₁ may be calculated based on the first-order estimate; therefore:

$$P_r = P_{nt} + P_{lt}$$

where
$P_r$ = required second-order axial strength using LRFD or ASD load combinations

From AISC *Specification* Appendix 8, Section 8.1.2, the *B*₁ multiplier for the W14×90 column is determined as follows:

---

# III-88

| LRFD | ASD |
|------|-----|
| $B_1 = \frac{C_m}{1 - \alpha P_r / P_{e1}} \geq 1$ (*Spec.* Eq. A-8-3) | $B_1 = \frac{C_m}{1 - \alpha P_r / P_{e1}} \geq 1$ (*Spec.* Eq. A-8-3) |
|  |  |
| where | where |
| $P_r = 316 \text{ kips (from first-order computer analysis)}$ | $P_r = 232 \text{ kips (from first-order computer analysis)}$ |
| $I_x = 999 \text{ in.}^4$ | $I_x = 999 \text{ in.}^4$ |
| $\tau_b = 1.0$ [to be verified per *Spec.* Section C2.3(b)] | $\tau_b = 1.0$ [to be verified per *Spec.* Section C2.3(b)] |
| $\alpha = 1.0$ | $\alpha = 1.6$ |
|  |  |
| $P_{e1} = \frac{\pi^2 EI^*}{(L_{c1})^2}$ (*Spec.* Eq. A-8-5) | $P_{e1} = \frac{\pi^2 EI^*}{(L_{c1})^2}$ (*Spec.* Eq. A-8-5) |
|  |  |
| $= \frac{\pi^2 (29{,}000 \text{ ksi})(999 \text{ in.}^4)}{\left[(1.0)(13.5 \text{ ft})(12 \text{ in./ft})\right]^2}$ | $= \frac{\pi^2 (29{,}000 \text{ ksi})(999 \text{ in.}^4)}{\left[(1.0)(13.5 \text{ ft})(12 \text{ in./ft})\right]^2}$ |
|  |  |
| $= 10{,}900 \text{ kips}$ | $= 10{,}900 \text{ kips}$ |
|  |  |
| $C_m = 0.6 - 0.4(M_1/M_2)$ (*Spec.* Eq. A-8-4) | $C_m = 0.6 - 0.4(M_1/M_2)$ (*Spec.* Eq. A-8-4) |
| $= 0.6 - 0.4(134 \text{ kip-ft}/211 \text{ kip-ft})$ | $= 0.6 - 0.4(94.0 \text{ kip-ft}/147 \text{ kip-ft})$ |
| $= 0.346$ | $= 0.344$ |
|  |  |
| $B_1 = \frac{0.346}{1 - \frac{1.0(316 \text{ kips})}{10{,}900 \text{ kips}}} < 1$ | $B_1 = \frac{0.344}{1 - \frac{1.6(232 \text{ kips})}{10{,}900 \text{ kips}}} < 1$ |
|  |  |
| $= 0.356 < 1$ | $= 0.356 < 1$ |
|  |  |
| Therefore, use $B_1 = 1$ | Therefore, use $B_1 = 1$ |

*Determine B₂*

| LRFD | ASD |
|------|-----|
| $P_{mf} = 2{,}240 \text{ kips (gravity load in moment frame)}$ | $P_{mf} = 1{,}640 \text{ kips (gravity load in moment frame)}$ |
| $P_{story} = 5{,}410 \text{ kips (from computer output)}$ | $P_{story} = 3{,}920 \text{ kips (from computer output)}$ |
| $\Delta_H = 0.520 \text{ in. (from computer output)}$ | $\Delta_H = 0.365 \text{ in. (from computer output)}$ |
| $\alpha = 1.0$ | $\alpha = 1.6$ |
|  |  |
| $R_M = 1 - 0.15\left(\frac{P_{mf}}{P_{story}}\right)$ (*Spec.* Eq. A-8-8) | $R_M = 1 - 0.15\left(\frac{P_{mf}}{P_{story}}\right)$ (*Spec.* Eq. A-8-8) |
|  |  |
| $= 1 - 0.15\left(\frac{2{,}240 \text{ kips}}{5{,}410 \text{ kips}}\right)$ | $= 1 - 0.15\left(\frac{1{,}640 \text{ kips}}{3{,}920 \text{ kips}}\right)$ |
|  |  |
| $= 0.938$ | $= 0.937$ |
|  |  |
| From previous seismic force distribution calculations: | From previous seismic force distribution calculations: |
|  |  |
| $H = 1.0Q_E$ (Lateral) | $H = 0.7Q_E$ (Lateral) |
| $= 1.0(178 \text{ kips})$ | $= 0.7(178 \text{ kips})$ |
| $= 178 \text{ kips}$ | $= 125 \text{ kips}$ |

---

# III-89

| LRFD | ASD |
|------|-----|
| $P_{e\text{-}story} = R_M \frac{HL}{\Delta_H}$ (*Spec.* Eq. A-8-7) | $P_{e\text{-}story} = R_M \frac{HL}{\Delta_H}$ (*Spec.* Eq. A-8-7) |
|  |  |
| $= 0.938 \frac{(178 \text{ kips})(13.5 \text{ ft})(12 \text{ in./ft})}{0.520 \text{ in.}}$ | $= 0.937 \frac{(125 \text{ kips})(13.5 \text{ ft})(12 \text{ in./ft})}{0.365 \text{ in.}}$ |
|  |  |
| $= 52{,}000 \text{ kips}$ | $= 52{,}000 \text{ kips}$ |
|  |  |
| $B_2 = \frac{1}{1 - \frac{\alpha P_{story}}{P_{e\text{-}story}}} \geq 1$ (*Spec.* Eq. A-8-6) | $B_2 = \frac{1}{1 - \frac{\alpha P_{story}}{P_{e\text{-}story}}} \geq 1$ (*Spec.* Eq. A-8-6) |
|  |  |
| $= \frac{1}{1 - \frac{1.0(5{,}410 \text{ kips})}{52{,}000 \text{ kips}}} > 1$ | $= \frac{1}{1 - \frac{1.6(3{,}920 \text{ kips})}{52{,}000 \text{ kips}}} > 1$ |
|  |  |
| $= 1.12 > 1$ | $= 1.14 > 1$ |
|  |  |
| Note, *B*₂ < 1.5, therefore use of the effective length method is acceptable per AISC *Specification* Appendix 7, Section 7.2.1(b). | Note, *B*₂ < 1.5, therefore use of the effective length method is acceptable per AISC *Specification* Appendix 7, Section 7.2.1(b). |

*Calculate amplified moment and axial load*

From AISC *Specification* Equation A-8-1, the required second-order flexural strength is determined as follows:

| LRFD | ASD |
|------|-----|
| $M_r = B_1 M_{nt} + B_2 M_{lt}$ | $M_r = B_1 M_{nt} + B_2 M_{lt}$ |
| $= (1)(0 \text{ kip-ft}) + (1.12)(211 \text{ kip-ft})$ | $= (1)(0 \text{ kip-ft}) + (1.14)(147 \text{ kip-ft})$ |
| $= 236 \text{ kip-ft}$ | $= 168 \text{ kip-ft}$ |

The required second-order axial strength is determined using AISC *Specification* Equation A-8-2 as follows. Note, for a long frame such as this one, the change in load to the interior columns associated with lateral load is negligible.

| LRFD | ASD |
|------|-----|
| $P_{nt} = 316 \text{ kips (from computer analysis)}$ | $P_{nt} = 232 \text{ kips (from computer analysis)}$ |
|  |  |
| $P_r = P_{nt} + B_2 P_{lt}$ | $P_r = P_{nt} + B_2 P_{lt}$ |
| $= 316 \text{ kips} + (1.12)(0 \text{ kips})$ | $= 232 \text{ kips} + (1.14)(0 \text{ kips})$ |
| $= 316 \text{ kips}$ | $= 232 \text{ kips}$ |

*Determine the Controlling Effective Length*

For out-of-plane buckling in the moment frame, $K_y = 1.0$; therefore:

$$K_y L_y = 1.0(13.5 \text{ ft})$$
$$= 13.5 \text{ ft}$$

For in-plane buckling in the moment frame, use the story stiffness procedure from AISC *Specification* Commentary Appendix 7 to determine $K_x$.

---

# III-90

$$K_2 = \sqrt{\left(\frac{P_{story}}{R_M P_e}\right)\left(\frac{\pi^2 EI}{L^2}\right)\left(\frac{\Delta_H}{HL}\right)} \geq \sqrt{\left(\frac{\pi^2 EI}{L^2}\right)\left(\frac{\Delta_H}{1.7H_{col}L}\right)}$$ (*Spec.* Eq. C-A-7-5)

Simplifying and substituting terms previously calculated results in:

$$K_x = \sqrt{\left(\frac{P_{story}}{R_M}\right)\left(\frac{P_e}{P_r}\right)\left(\frac{ratio}{H}\right)} \geq \sqrt{P_e\left(\frac{ratio}{1.7H_{col}}\right)}$$

where
$P_e = P_{e1}$

$$ratio = \frac{\Delta_H}{L}$$

| LRFD | ASD |
|------|-----|
| $H_{col} = 25.5 \text{ kips (from computer analysis)}$ | $H_{col} = 17.9 \text{ kips (from computer analysis)}$ |
|  |  |
| $P_e = P_{e1}$ | $P_e = P_{e1}$ |
| $= 10{,}900 \text{ kips}$ | $= 10{,}900 \text{ kips}$ |
|  |  |
| $ratio = \frac{\Delta_H}{L}$ | $ratio = \frac{\Delta_H}{L}$ |
|  |  |
| $= \frac{0.520 \text{ in.}}{(13.5 \text{ ft})(12 \text{ in./ft})}$ | $= \frac{0.365 \text{ in.}}{(13.5 \text{ ft})(12 \text{ in./ft})}$ |
|  |  |
| $= 0.00321$ | $= 0.00225$ |
|  |  |
| $K_x = \sqrt{\left(\frac{5{,}410 \text{ kips}}{0.938}\right)\left(\frac{10{,}900 \text{ kips}}{316 \text{ kips}}\right)\left(\frac{0.00321}{178 \text{ kips}}\right)} \geq$ | $K_x = \sqrt{\left(\frac{3{,}920 \text{ kips}}{0.937}\right)\left(\frac{10{,}900 \text{ kips}}{232 \text{ kips}}\right)\left(\frac{0.00225}{125 \text{ kips}}\right)} \geq$ |
|  |  |
| $\sqrt{(10{,}900 \text{ kips})\left[\frac{0.00321}{1.7(25.5 \text{ kips})}\right]}$ | $\sqrt{(10{,}900 \text{ kips})\left[\frac{0.00225}{1.7(17.9 \text{ kips})}\right]}$ |
|  |  |
| $= 1.89 > 0.898$ | $= 1.88 > 0.898$ |
|  |  |
| Therefore, use $K_x = 1.89$. | Therefore, use $K_x = 1.88$. |
|  |  |
| From AISC *Manual* Table 4-1a, for a W14×90: | From AISC *Manual* Table 4-1a, for a W14×90: |
|  |  |
| $r_x/r_y = 1.66$ | $r_x/r_y = 1.66$ |
|  |  |
| $L_{cy\,eq} = \frac{KL_x}{r_x/r_y}$ (from *Manual* Eq. 4-1) | $L_{cy\,eq} = \frac{KL_x}{r_x/r_y}$ (from *Manual* Eq. 4-1) |
|  |  |
| $= \frac{1.89(13.5 \text{ ft})}{1.66}$ | $= \frac{1.88(13.5 \text{ ft})}{1.66}$ |
|  |  |
| $= 15.4 \text{ ft}$ | $= 15.3 \text{ ft}$ |
|  |  |
| Because $L_{cy\,eq} > L_{cy}$, use $L_c = 15.4$ ft. | Because $L_{cy\,eq} > L_{cy}$, use $L_c = 15.3$ ft. |

---

# III-91

*Interaction of Flexure and Axial Force*

From AISC *Specification* Section H1, interaction of flexure and axial force are checked as follows:

| LRFD | ASD |
|------|-----|
| From AISC *Manual* Table 6-1, for a W14×90, with $L_c = 15.4$ ft: | From AISC *Manual* Table 6-1, for a W14×90, with $L_c = 15.3$ ft: |
|  |  |
| $P_c = \phi_c P_n$ | $P_c = \frac{P_n}{\Omega_c}$ |
| $= 992 \text{ kips}$ | $= 663 \text{ kips}$ |
|  |  |
| From AISC *Manual* Table 6-1, for a W14×90, with $L_b = 13.5$ ft: | From AISC *Manual* Table 6-2, for a W14×90, with $L_b = 13.5$ ft: |
|  |  |
| $M_{cx} = \phi_b M_{nx}$ | $M_{cx} = \frac{M_{nx}}{\Omega_b}$ |
| $= 574 \text{ kip-ft}$ | $= 382 \text{ kip-ft}$ |
|  |  |
| $\frac{P_r}{P_c} = \frac{316 \text{ kips}}{992 \text{ kips}}$ | $\frac{P_r}{P_c} = \frac{232 \text{ kips}}{663 \text{ kips}}$ |
|  |  |
| $= 0.319$ | $= 0.350$ |
|  |  |
| Because $\frac{P_r}{P_c} \geq 0.2$, use AISC *Specification* Equation H1-1a: | Because $\frac{P_r}{P_c} \geq 0.2$, use AISC *Specification* Equation H1-1a: |
|  |  |
| $\frac{P_r}{P_c} + \left(\frac{8}{9}\right)\left(\frac{M_{rx}}{M_{cx}} + \frac{M_{ry}}{M_{cy}}\right) \leq 1.0$ | $\frac{P_r}{P_c} + \left(\frac{8}{9}\right)\left(\frac{M_{rx}}{M_{cx}} + \frac{M_{ry}}{M_{cy}}\right) \leq 1.0$ |
|  |  |
| $0.319 + \left(\frac{8}{9}\right)\left(\frac{236 \text{ kip-ft}}{574 \text{ kip-ft}} + 0\right) < 1.0$ | $0.350 + \left(\frac{8}{9}\right)\left(\frac{168 \text{ kip-ft}}{382 \text{ kip-ft}} + 0\right) < 1.0$ |
|  |  |
| $0.684 < 1.0$ **o.k.** | $0.741 < 1.0$ **o.k.** |

---

# III-92

## METHOD 3—SIMPLIFIED EFFECTIVE LENGTH METHOD

A simplification of the effective length method using a method of second-order analysis based upon drift limits and other assumptions is described in AISC *Manual* Part 2 in the section titled "Simplified Determination of Required Strength." A first-order frame analysis is conducted using the load combinations for LRFD or ASD. A minimum lateral load (notional load) equal to 0.2% of the gravity loads is included for any gravity-only load combinations. The floor diaphragm deflection in the east-west direction was previously determined to be very small and will thus be neglected in these calculations.

| LRFD | ASD |
|------|-----|
| $1.23D + 1.0Q_E + 0.5L + 0.15S$ | $1.02D + 0.7Q_E$ |
| (Controls columns) | (Controls columns) |
|  |  |
| For interior column design: | For interior column design: |
|  |  |
| $P_r = 316 \text{ kips}$ | $P_a = 232 \text{ kips}$ |
| $M_{u1} = 134 \text{ kip-ft (from first-order analysis)}$ | $M_{a1} = 94.0 \text{ kip-ft (from first-order analysis)}$ |
| $M_{u2} = 211 \text{ kip-ft (from first-order analysis)}$ | $M_{a2} = 147 \text{ kip-ft (from first-order analysis)}$ |
|  |  |
| First-order first story drift = 0.520 in. | First-order first story drift = 0.365 in. |

Calculate the amplified forces and moments in accordance with AISC *Manual* Part 2 at the ground floor. The following steps are executed.

| LRFD | ASD |
|------|-----|
| *Step 1:* | *Step 1:* |
|  |  |
| Lateral load = 178 kips | Lateral load = 125 kips |
|  |  |
| Deflection due to first-order elastic analysis | Deflection due to first-order elastic analysis |
|  |  |
| $\Delta = 0.520$ in., between first and second floor | $\Delta = 0.365$ in., between first and second floor |
|  |  |
| Floor height = 13.5 ft | Floor height = 13.5 ft |
|  |  |
| Drift ratio = $\frac{(13.5 \text{ ft})(12 \text{ in./ft})}{0.520 \text{ in.}}$ | Drift ratio = $\frac{(13.5 \text{ ft})(12 \text{ in./ft})}{0.365 \text{ in.}}$ |
| $= 312$ | $= 444$ |
|  |  |
| *Step 2:* | *Step 2:* |
|  |  |
| Design story drift limit = *H*/400 | Design story drift limit = *H*/400 |
|  |  |
| Adjusted lateral load = $\left(\frac{312}{400}\right)(178 \text{ kips})$ | Adjusted lateral load = $\left(\frac{444}{400}\right)(125 \text{ kips})$ |
| $= 139 \text{ kips}$ | $= 139 \text{ kips}$ |

---

# III-93

| LRFD | ASD |
|------|-----|
| *Step 3:* | *Step 3:* (for an ASD design the ratio must be multiplied by 1.6) |
|  |  |
| Load ratio = $\frac{\alpha P_{story}}{R_M H}$ | Load ratio = $\frac{\alpha P_{story}}{R_M H}$ |
|  |  |
| $= \frac{(1.0)(5{,}410 \text{ kips})}{(0.938)(139 \text{ kips})}$ | $= \frac{(1.6)(3{,}920 \text{ kips})}{(0.937)(139 \text{ kips})}$ |
|  |  |
| $= 41.5$ | $= 48.2$ |
|  |  |
| From AISC *Manual* Table 2-2: | From AISC *Manual* Table 2-2: |
|  |  |
| $B_2 = 1.11$ | $B_2 = 1.13$ |

Additionally, the design story drift limit used in Step 2 need not be the same as other strength or serviceability drift limits used during the analysis and design of the structure.

*Step 4:*

Multiply all the forces and moment from the first-order analysis by the value of *B*₂ obtained from the table. This presumes that *B*₁ is less than or equal to *B*₂, which is usually the case for members without transverse loading between their ends.

| LRFD | ASD |
|------|-----|
| *Step 5:* | *Step 5:* |
|  |  |
| Because the selection is in the shaded area of the chart (*B*₂ > 1.1), the effective length factor, *K*, must be determined through analysis. From previous analysis, use an effective length of 15.4 ft. | Because the selection is in the shaded area of the chart (*B*₂ > 1.1), the effective length factor, *K*, must be determined through analysis. From previous analysis, use an effective length of 15.3 ft. |
|  |  |
| Multiply both sway and nonsway moments by *B*₂. | Multiply both sway and nonsway moments by *B*₂. |
|  |  |
| $M_r = B_2 (M_{nt} + M_{lt})$ | $M_r = B_2 (M_{nt} + M_{lt})$ |
| $= 1.11(0 \text{ kip-ft} + 211 \text{ kip-ft})$ | $= 1.13(0 \text{ kip-ft} + 147 \text{ kip-ft})$ |
| $= 234 \text{ kip-ft}$ | $= 166 \text{ kip-ft}$ |
|  |  |
| $P_r = B_2 (P_{nt} + P_{lt})$ | $P_r = B_2 (P_{nt} + P_{lt})$ |
| $= 1.11(316 \text{ kips} + 0 \text{ kips})$ | $= 1.13(232 \text{ kips} + 0 \text{ kips})$ |
| $= 351 \text{ kips}$ | $= 262 \text{ kips}$ |
|  |  |
| From AISC *Manual* Table 6-1, for a W14×90, with $L_c = 15.4$ ft: | From AISC *Manual* Table 6-1, for a W14×90, with $L_c = 15.3$ ft: |
|  |  |
| $P_c = \phi_c P_n$ | $P_c = \frac{P_n}{\Omega_c}$ |
| $= 992 \text{ kips}$ | $= 663 \text{ kips}$ |

| LRFD | ASD |
|------|-----|
| From AISC *Manual* Table 6-1, for a W14×90, with | From AISC *Manual* Table 6-1, for a W14×90, with |

---

# III-94

| LRFD | ASD |
|------|-----|
| $L_b = 13.5$ ft: | $L_b = 13.5$ ft: |
|  |  |
| $M_{cx} = \phi_b M_{nx}$ | $M_{cx} = \frac{M_{nx}}{\Omega_b}$ |
| $= 574 \text{ kip-ft}$ | $= 382 \text{ kip-ft}$ |
|  |  |
| $\frac{P_r}{P_c} = \frac{351 \text{ kips}}{992 \text{ kips}}$ | $\frac{P_r}{P_c} = \frac{262 \text{ kips}}{663 \text{ kips}}$ |
|  |  |
| $= 0.354$ | $= 0.395$ |
|  |  |
| Because $\frac{P_r}{P_c} \geq 0.2$, use AISC *Specification* Equation H1-1a: | Because $\frac{P_r}{P_c} \geq 0.2$, use AISC *Specification* Equation H1-1a: |
|  |  |
| $\frac{P_r}{P_c} + \left(\frac{8}{9}\right)\left(\frac{M_{rx}}{M_{cx}} + \frac{M_{ry}}{M_{cy}}\right) \leq 1.0$ | $\frac{P_r}{P_c} + \left(\frac{8}{9}\right)\left(\frac{M_{rx}}{M_{cx}} + \frac{M_{ry}}{M_{cy}}\right) \leq 1.0$ |
|  |  |
| $0.354 + \left(\frac{8}{9}\right)\left(\frac{234 \text{ kip-ft}}{574 \text{ kip-ft}} + 0\right) < 1.0$ | $0.395 + \left(\frac{8}{9}\right)\left(\frac{166 \text{ kip-ft}}{382 \text{ kip-ft}} + 0\right) < 1.0$ |
|  |  |
| $0.716 < 1.0$ **o.k.** | $0.781 < 1.0$ **o.k.** |

---

# III-95

## BEAM ANALYSIS IN THE MOMENT FRAME

The controlling load combinations for the beams in the moment frames are shown in Tables III-13 and III-14 and evaluated for the second floor beam. The dead load, live load, and seismic moments were taken from a computer analysis. These tables summarizes the calculation of *B*₂ for the stories above and below the second floor.

| **Table III-13<br>Summary of *B*₂ Calculation for Controlling Load Combination—First to Second Floor** |  |  |  |
|--------------------------------------------------------------------------------------------------------|--|--|--|
| **1st – 2nd** | **LRFD Combination** | **ASD Combination 1** | **ASD Combination 2** |
|  | $1.23D + 1.0Q_E + 0.5L + 0.15S$ | $1.02D + 0.7Q_E$ | $1.01D + 0.525Q_E + 0.75L + 0.1S$ |
| *H*, kips | 178 | 125 | 93.5 |
| *L*, ft | 13.5 | 13.5 | 13.5 |
| Δ*H*, in. | 0.520 | 0.365 | 0.273 |
| *P<sub>mf</sub>*, kips | 2,240 | 1,640 | 2,000 |
| *R<sub>M</sub>* | 0.938 | 0.937 | 0.938 |
| *P<sub>e-story</sub>*, kips | 52,000 | 52,000 | 52,000 |
| *P<sub>story</sub>*, kips | 5,410 | 3,920 | 4,870 |
| *B*₂ | 1.12 | 1.14 | 1.18 |

| **Table III-14<br>Summary of *B*₂ Calculation for Controlling Load Combination—Second to Third Floor** |  |  |  |
|---------------------------------------------------------------------------------------------------------|--|--|--|
| **2nd – 3rd** | **LRFD Combination** | **ASD Combination 1** | **ASD Combination 2** |
|  | $1.23D + 1.0Q_E + 0.5L + 0.15S$ | $1.02D + 0.7Q_E$ | $1.01D + 0.525Q_E + 0.75L + 0.1S$ |
| *H*, kips | 154 | 108 | 80.9 |
| *L*, ft | 13.5 | 13.5 | 13.5 |
| Δ*H*, in. | 0.658 | 0.460 | 0.345 |
| *P<sub>mf</sub>*, kips | 1,580 | 1,160 | 1,400 |
| *R<sub>M</sub>* | 0.938 | 0.937 | 0.938 |
| *P<sub>e-story</sub>*, kips | 35,600 | 35,500 | 35,600 |
| *P<sub>story</sub>*, kips | 3,810 | 2,770 | 3,410 |
| *B*₂ | 1.12 | 1.14 | 1.18 |

For beam members, the larger of the *B*₂ values from the story above or below is used.

From computer output at the controlling beam:

$$M_{dead} = 153 \text{ kip-ft}$$
$$M_{live} = 80.6 \text{ kip-ft}$$
$$M_{snow} = 0 \text{ kip-ft}$$
$$M_{earthquake} = 140 \text{ kip-ft}$$

---

# III-96

| LRFD | ASD |
|------|-----|
| $B_2 M_{lt} = 1.12(140 \text{ kip-ft})$ | Combination 1: |
| $= 157 \text{ kip-ft}$ | $B_2 M_{lt} = 1.14(140 \text{ kip-ft})$ |
|  | $= 160 \text{ kip-ft}$ |
| $M_u = \left[\begin{array}{l} 1.23(153 \text{ kip-ft}) + 1.0(157 \text{ kip-ft}) \\ + 0.5(80.6 \text{ kip-ft}) \end{array}\right]$ | $M_a = 1.02(153 \text{ kip-ft}) + 0.7(160 \text{ kip-ft})$ |
| $= 385 \text{ kip-ft}$ | $= 268 \text{ kip-ft}$ |
|  |  |
|  | Combination 2: |
|  |  |
|  | $B_2 M_{lt} = 1.18(140 \text{ kip-ft})$ |
|  | $= 165 \text{ kip-ft}$ |
|  |  |
|  | $M_a = \left[\begin{array}{l} 1.01(153 \text{ kip-ft}) + 0.525(165 \text{ kip-ft}) \\ + 0.75(80.6 \text{ kip-ft}) \end{array}\right]$ |
|  | $= 302 \text{ kip-ft}$ |

Calculate $C_b$ for W24×55 beam with compression in the bottom flange braced at 10 ft on center.

| LRFD | ASD |
|------|-----|
| For load combination $1.23D + 1.0Q_E + 0.5L + 0.15S$: | For load combination $1.02D + 0.7Q_E$: |
|  |  |
| From AISC *Manual* Table 6-1 with $L_b = 0$ ft (fully braced): | From AISC *Manual* Table 6-1 with $L_b = 0$ ft (fully braced): |
|  |  |
| $\phi_b M_n = 503 \text{ kip-ft}$ | $\frac{M_n}{\Omega_b} = 334 \text{ kip-ft}$ |
|  |  |
| $C_b = 1.86$ (from computer output) | $C_b = 1.85$ (from computer output) |
|  |  |
| From AISC *Manual* Table 6-1 with $L_b = 10$ ft: | From AISC *Manual* Table 6-1 with $L_b = 10$ ft: |
|  |  |
| $\phi_b M_n C_b \leq \phi_b M_p$ | $\frac{M_n}{\Omega_b} C_b \leq \frac{M_p}{\Omega_b}$ |
| $(386 \text{ kip-ft})(1.86) = 718 \text{ kip-ft} > 503 \text{ kip-ft}$ | $(257 \text{ kip-ft})(1.85) = 475 \text{ kip-ft} > 334 \text{ kip-ft}$ |
|  |  |
| Therefore: | Therefore: |
|  |  |
| $\phi M_n = 503 \text{ kip-ft} > 385 \text{ kip-ft}$ **o.k.** | $\frac{M_n}{\Omega} = 334 \text{ kip-ft} > 268 \text{ kip-ft}$ **o.k.** |

---

# III-97

| LRFD | ASD |
|------|-----|
|  | For load combination $1.01D + 0.525Q_E + 0.75L + 0.1S$: |
|  |  |
|  | From AISC *Manual* Table 6-1 with $L_b = 0$ ft (fully braced): |
|  |  |
|  | $\frac{M_n}{\Omega_b} = 334 \text{ kip-ft}$ |
|  |  |
|  | $C_b = 2.01$ (from computer output) |
|  |  |
|  | From AISC *Manual* Table 6-1 with $L_b = 10$ ft: |
|  |  |
|  | $\frac{M_n}{\Omega_b} C_b \leq \frac{M_p}{\Omega_b}$ |
|  | $(257 \text{ kip-ft})(2.01) = 517 \text{ kip-ft} > 334 \text{ kip-ft}$ |
|  |  |
|  | Therefore: |
|  | $\frac{M_n}{\Omega} = 334 \text{ kip-ft} > 302 \text{ kip-ft}$ **o.k.** |
|  |  |
| From AISC *Manual* Table 6-1, a W24×55 has a design shear strength of 252 kips and an $I_y$ of 1,350 in.⁴ | From AISC *Manual* Table 6-1, a W24×55 has an allowable shear strength of 167 kips and an $I_y$ of 1,350 in.⁴ |

The moments and shears on the roof beams due to the lateral loads were also checked but do not control the design.

The connections of these beams can be designed by one of the techniques illustrated in Part IIB of these design examples.

---

# III-98

## BRACED FRAME ANALYSIS

The braced frames at Grids 1 and 8 were analyzed for the required load combinations. The stability design requirements from Chapter C were applied to this system.

The model layout is shown in Figure III-26. The nominal dead, live, and snow loads with associated notional loads, wind loads, and seismic loads are shown in Figures III-27 and III-28. Based on Table III-4, roof live load will not govern over snow for the columns participating in these braced frames.

**Fig. III-26. Braced frame layout—Grid 1 and 8.**

Diagram description: Braced frame elevation showing a 2-bay structure with diagonal bracing. The frame has four floor levels with story heights of 13'-6" each. Bay width is 30'-0". Columns at gridlines C and D with W12×53 brace members shown in middle two stories. Base connections shown with hatching indicating fixed supports. Pinned connections shown at roof level.

---

# III-99

**Fig. III-27. Dead and live loads.**

Diagram description: Four load diagrams showing:

(a) Nominal dead loads - Vertical loads applied at beam-column connections on 4-story braced frame:
- Top level: 14.5 kips at columns C and D, 421 kips at leaning column, with 0.483 klf distributed load on beam
- Floor levels: 38.4 kips at columns C and D, 1,020 kips at leaning column, with 0.916 klf distributed loads on beams

(b) Notional dead loads - Horizontal loads applied at each floor level:
- All levels: 0.464 kip at columns C and D, 1.12 kips at leaning column

(c) Nominal live loads - Vertical loads applied at beam-column connections:
- Floor levels only (no roof): 10.1 kips at columns C and D, 390 kips at leaning column, with 0.550 klf distributed loads on beams

(d) Notional live loads - Horizontal loads applied at each floor level:
- Floor levels only: 0.427 kips at columns C and D

---

# III-100

**Fig. III-28. Snow, wind, and seismic loads.**

Diagram description: Four load diagrams showing:

(a) Nominal snow loads - Vertical loads applied at roof level only:
- Top level: 11.4 kips at columns C and D, 288 kips at leaning column, with 0.125 klf distributed load on beam

(b) Notional snow loads - Horizontal loads applied at roof level only:
- Top level: 0.315 kip at columns C and D

(c) Wind loads (1.0W) - Horizontal loads applied at each floor level:
- Top level: 25.7 kip at each column
- Second level: 21.9 kips at each column
- Third level: 20.2 kips at each column
- Fourth level: 18.8 kips at each column

(d) Seismic loads (1.0Q<sub>E</sub>) - Horizontal loads applied at each floor level:
- Top level: 16.2 kip at each column
- Second level: 36.5 kips at each column
- Third level: 24.3 kips at each column
- Fourth level: 11.9 kips at each column

---

# III-101

*Second-order analysis by amplified first-order analysis*

In the following, the approximate second-order analysis method from AISC *Specification* Appendix 8 is used to account for second-order effects in the braced frames by amplifying the axial forces in members and connections from a first-order analysis.

A first-order frame analysis is conducted using the load combinations for LRFD and ASD. From this analysis, the critical axial loads, moments, and deflections are obtained.

A summary of the axial loads and first floor drifts from the first-order computer analysis is shown below. The floor diaphragm deflection in the north-south direction was previously determined to be very small and will thus be neglected in these calculations.

The required seismic load combinations, as given in ASCE/SEI 7, Sections 2.3.6 and 2.4.5, were derived previously.

| LRFD | ASD |
|------|-----|
| $1.23D + 1.0Q_E + 0.5L + 0.15S$ | $1.01D + 0.525Q_E + 0.75L + 0.1S$ |
| (Controls columns) | (Controls columns) |
|  |  |
| From first-order analysis. | From first-order analysis. |
|  |  |
| For interior column design: | For interior column design: |
|  |  |
| $P_{nt} = 235 \text{ kips}$ | $P_{nt} = 210 \text{ kips}$ |
| $P_{lt} = 132 \text{ kips}$ | $P_{lt} = 69.5 \text{ kips}$ |
|  |  |
| The moments are negligible. | The moments are negligible. |
|  |  |
| First-order first story drift = 0.173 in. | First-order first story drift = 0.0908 in. |

The required second-order axial strength, $P_r$, is computed as follows:

| LRFD | ASD |
|------|-----|
| $P_r = P_{nt} + B_2 P_{lt}$ (*Spec.* Eq. A-8-2) | $P_r = P_{nt} + B_2 P_{lt}$ (*Spec.* Eq. A-8-2) |
|  |  |
| Determine *B*₂. | Determine *B*₂. |
|  |  |
| $B_2 = \frac{1}{1 - \frac{\alpha P_{story}}{P_{e\text{-}story}}} \geq 1$ (*Spec.* Eq. A-8-6) | $B_2 = \frac{1}{1 - \frac{\alpha P_{story}}{P_{e\text{-}story}}} \geq 1$ (*Spec.* Eq. A-8-6) |
|  |  |
| $P_{story} = 5{,}410 \text{ kips (previously calculated)}$ | $P_{story} = 4{,}870 \text{ kips (previously calculated)}$ |
|  |  |
| $P_{e\text{-}story} = R_M \frac{HL}{\Delta_H}$ (*Spec.* Eq. A-8-7) | $P_{e\text{-}story} = R_M \frac{HL}{\Delta_H}$ (*Spec.* Eq. A-8-7) |
|  |  |
| where | where |
| $H = 178 \text{ kips (from previous calculations)}$ | $H = 93.5 \text{ kips (from previous calculations)}$ |
| $\Delta_H = 0.173 \text{ in. (from computer output)}$ | $\Delta_H = 0.0908 \text{ in. (from computer output)}$ |
| $R_M = 1.0$ for braced frames | $R_M = 1.0$ for braced frames |

---

# III-102

| LRFD | ASD |
|------|-----|
| $P_{e\text{-}story} = (1.0)\left[\frac{(178 \text{ kips})(13.5 \text{ ft})(12 \text{ in./ft})}{0.173 \text{ in.}}\right]$ | $P_{e\text{-}story} = (1.0)\left[\frac{(93.5 \text{ kips})(13.5 \text{ ft})(12 \text{ in./ft})}{0.0908 \text{ in.}}\right]$ |
|  |  |
| $= 167{,}000 \text{ kips}$ | $= 167{,}000 \text{ kips}$ |
|  |  |
| $B_2 = \frac{1}{1 - \frac{1.0(5{,}410 \text{ kips})}{167{,}000 \text{ kips}}} > 1$ | $B_2 = \frac{1}{1 - \frac{1.6(4{,}870 \text{ kips})}{167{,}000 \text{ kips}}} > 1$ |
|  |  |
| $= 1.03 > 1$ | $= 1.05 > 1$ |
|  |  |
| Therefore, use $B_2 = 1.03$. | Therefore, use $B_2 = 1.05$. |
|  |  |
| $P_r = P_{nt} + B_2 P_{lt}$ (*Spec.* Eq. A-8-2) | $P_r = P_{nt} + B_2 P_{lt}$ (*Spec.* Eq. A-8-2) |
| $= 235 \text{ kips} + (1.03)(132 \text{ kips})$ | $= 210 \text{ kips} + (1.05)(69.5 \text{ kips})$ |
| $= 371 \text{ kips}$ | $= 283 \text{ kips}$ |
|  |  |
| From AISC *Manual* Table 6-1 for a W12×53 with $L_c = 13.5$ ft: | From AISC *Manual* Table 6-1 for a W12×53 with $L_c = 13.5$ ft: |
|  |  |
| $P_c = \phi_c P_n$ | $P_c = \frac{P_n}{\Omega_c}$ |
| $= 514 \text{ kips}$ | $= 342 \text{ kips}$ |
|  |  |
| From AISC *Specification* Equation H1-1a: | From AISC *Specification* Equation H1-1a: |
|  |  |
| $\frac{P_r}{P_c} = \frac{371 \text{ kips}}{514 \text{ kips}} \leq 1.0$ | $\frac{P_r}{P_c} = \frac{283 \text{ kips}}{342 \text{ kips}} \leq 1.0$ |
|  |  |
| $= 0.722 < 1.0$ **o.k.** | $= 0.827 < 1.0$ **o.k.** |

Note: Notice that the lower sidesway displacements of the braced frame produce much lower values of *B*₂ than those of the moment frame. Similar results could be expected for the other two methods of analysis.

Although not presented here, second-order effects should be accounted for in the design of the beams and diagonal braces in the braced frames at Grids 1 and 8.

---

# III-103

## ANALYSIS OF DRAG STRUTS

The fourth floor delivers the highest diaphragm force to the braced frames at the ends of the building: $Q_E = 73.0$ kips (from previous calculations). This force is transferred to the braced frame through axial loading of the W18×35 beams at the end of the building.

The gravity dead loads for the edge beams are the floor loading of 75 psf (5.50 ft) plus the exterior wall loading of 0.503 kip/ft, giving a total dead load of 0.916 kip/ft. The gravity live load for these beams is the floor loading of 80 psf (5.50 ft) = 0.440 kip/ft. The resulting moments are $M_D = 58.0$ kip-ft and $M_L = 27.8$ kip-ft.

The required seismic load combinations, as given in ASCE/SEI 7, Sections 2.3.6 and 2.4.5, were derived previously. The controlling load combination for LRFD is $1.23D + 1.0Q_E + 0.5L$. The controlling load combinations for ASD are $1.01D + 0.525Q_E + 0.75L$ or $1.02D + 0.7Q_E$.

| LRFD | ASD |
|------|-----|
| $M_u = 1.23M_D + 0.5M_L$ | $M_a = 1.01M_D + 0.75M_L$ |
| $= 1.23(58.0 \text{ kip-ft}) + 0.5(27.8 \text{ kip-ft})$ | $= 1.01(58.0 \text{ kip-ft}) + 0.75(27.8 \text{ kip-ft})$ |
| $= 85.2 \text{ kip-ft}$ | $= 79.4 \text{ kip-ft}$ |
|  |  |
|  | or |
|  |  |
|  | $M_a = 1.02M_D$ |
|  | $= 1.02(58.0 \text{ kip-ft})$ |
|  | $= 59.2 \text{ kip-ft}$ |
|  |  |
| Load from the diaphragm shear due to earthquake loading | Load from the diaphragm shear due to earthquake loading |
|  |  |
| $F_p = 1.0Q_E$ | $F_p = 0.525Q_E$ |
| $= 1.0(73.0 \text{ kips})$ | $= 0.525(73.0 \text{ kips})$ |
| $= 73.0 \text{ kips}$ | $= 38.3 \text{ kips}$ |
|  |  |
|  | or |
|  |  |
|  | $F_p = 0.7Q_E$ |
|  | $= 0.7(73.0 \text{ kips})$ |
|  | $= 51.1 \text{ kips}$ |

Only the two 45-ft-long segments on either side of the brace can transfer load into the brace, because the stair opening is in front of the brace.

Use AISC *Specification* Section H2 to check the combined bending and axial stresses.

---

# III-104

| LRFD | ASD |
|------|-----|
| $V = \frac{73.0 \text{ kips}}{2(45 \text{ ft})}$ | $V = \frac{38.3 \text{ kips}}{2(45 \text{ ft})}$ |
|  |  |
| $= 0.811 \text{ kip/ft}$ | $= 0.426 \text{ kip/ft}$ |
|  |  |
|  | or |
|  |  |
|  | $V = \frac{51.1 \text{ kips}}{2(45 \text{ ft})}$ |
|  |  |
|  | $= 0.568 \text{ kip/ft}$ |

From AISC *Manual* Table 1-1, for a W18×35:

$$S_x = 57.6 \text{ in.}^3$$

| LRFD | ASD |
|------|-----|
| The top flange bending stress is: | The top flange bending stress is: |
|  |  |
| $f_{rbw} = \frac{M_u}{S_x}$ | $f_{rbw} = \frac{M_a}{S_x}$ |
|  |  |
| $= \frac{(85.2 \text{ kip-ft})(12 \text{ in./ft})}{57.6 \text{ in.}^3}$ | $= \frac{(79.4 \text{ kip-ft})(12 \text{ in./ft})}{57.6 \text{ in.}^3}$ |
|  |  |
| $= 17.8 \text{ ksi}$ | $= 16.5 \text{ ksi}$ |
|  |  |
|  | or |
|  |  |
|  | $f_{rbw} = \frac{M_a}{S_x}$ |
|  |  |
|  | $= \frac{(59.2 \text{ kip-ft})(12 \text{ in./ft})}{57.6 \text{ in.}^3}$ |
|  |  |
|  | $= 12.3 \text{ ksi}$ |

Note: It is often possible to resist the drag strut force using the slab directly. For illustration purposes, this solution will instead use the beam to resist the force independently of the slab. The full cross section can be used to resist the force if the member is designed as a column braced at one flange only (plus any other intermediate bracing present, such as from filler beams). Alternatively, a reduced cross section consisting of the top flange plus a portion of the web can be used. Arbitrarily use the top flange and 8 times an area of the web equal to its thickness times a depth equal to its thickness, as an area to carry the drag strut component.

$$\text{Area} = b_f t_f + 8(t_w)^2$$
$$= (6.00 \text{ in.})(0.425 \text{ in.}) + 8(0.300 \text{ in.})^2$$
$$= 3.27 \text{ in.}^2$$

Ignoring the small segment of the beam between Grid C and D, the axial stress due to the drag strut force is:

---

# III-105

| LRFD | ASD |
|------|-----|
| $f_{ra} = \frac{73.0 \text{ kips}}{2(3.27 \text{ in.}^2)}$ | $f_{ra} = \frac{38.3 \text{ kips}}{2(3.27 \text{ in.}^2)}$ |
|  |  |
| $= 11.2 \text{ ksi}$ | $= 5.86 \text{ ksi}$ |
|  |  |
|  | or |
|  |  |
|  | $f_{ra} = \frac{51.1 \text{ kips}}{2(3.27 \text{ in.}^2)}$ |
|  |  |
|  | $= 7.81 \text{ ksi}$ |

| LRFD | ASD |
|------|-----|
| Using AISC *Specification* Section H2, assuming the top flange is continuously braced: | Using AISC *Specification* Section H2, assuming the top flange is continuously braced: |
|  |  |
| $F_{ca} = \phi_c F_y$ | $F_{ca} = F_y/\Omega_c$ |
| $= 0.90(50 \text{ksi})$ | $= 50 \text{ksi}/1.67$ |
| $= 45.0 \text{ksi}$ | $= 29.9 \text{ksi}$ |
|  |  |
| $F_{cbw} = \phi_b F_y$ | $F_{cbw} = \frac{F_y}{\Omega_b}$ |
| $= 0.90(50 \text{ksi})$ | $= 50 \text{ksi}/1.67$ |
| $= 45.0 \text{ksi}$ | $= 29.9 \text{ ksi}$ |
|  |  |
| $\frac{f_{ra}}{F_{ca}} + \frac{f_{rbw}}{F_{cbw}} \leq 1.0$ (from *Spec.* Eq. H2-1) | $\frac{f_{ra}}{F_{ca}} + \frac{f_{rbw}}{F_{cbw}} \leq 1.0$ (from *Spec.* Eq. H2-1) |
|  |  |
| $\frac{11.2 \text{ksi}}{45.0 \text{ksi}} + \frac{17.8 \text{ksi}}{45.0 \text{ksi}} = 0.644 < 1.0$ **o.k.** | Load Combination 1: |
|  |  |
|  | $\frac{5.86 \text{ksi}}{29.9 \text{ksi}} + \frac{16.5 \text{ksi}}{29.9 \text{ksi}} = 0.748 < 1.0$ **o.k.** |
|  |  |
|  | Load Combination 2: |
|  |  |
|  | $\frac{7.81\text{ksi}}{29.9 \text{ksi}} + \frac{12.3 \text{ksi}}{29.9 \text{ksi}} = 0.673 < 1.0$ **o.k.** |

Note: Because the drag strut load is a horizontal load, the method of transfer into the strut and the extra horizontal load that must be accommodated by the beam end connections should be indicated on the drawings.

---

# III-106

## PART III EXAMPLE REFERENCES

ASCE (2019), *Design Loads on Structures During Construction*, ASCE/SEI 37-14(R2019), American Society of Civil Engineers, Reston, Va.

Geschwindner, L.F. (1994), "A Practical Approach to the Leaning Column," *Engineering Journal*, AISC, Vol. 31, No. 4, pp. 141–149.

SDI (2020), *Floor Deck Design Manual*, 2nd Ed., Steel Deck Institute, Glenshaw, Pa.

SDI (2015), *Diaphragm Design Manual*, 4th Ed., Steel Deck Institute, Glenshaw, Pa.

SJI (2020), *Load Tables and Weight Tables for Steel Joists and Joist Girders*, 45th Ed., Steel Joist Institute, Florence, SC.

West, M.A., Fisher, J.M., and Griffis, L.G. (2003), *Serviceability Design Considerations for Steel Buildings*, Design Guide 3, 2nd Ed., AISC, Chicago, Ill.

---

# III-107

**Fig. III-29. Second floor framing plan.**

Diagram description: Structural framing plan for second floor showing:
- Building dimensions: approximately 210 ft (east-west) × 120 ft (north-south)
- Grid lines numbered 1-8 (east-west) and lettered A-F (north-south)
- Typical bay spacing: 30'-0" between columns in east-west direction, 22'-6" to 23'-0" in north-south direction
- Floor beams: W24×55 (typical) spanning north-south
- Edge beams: W18×35 at building perimeter
- Diagonal bracing at Grids 1 and 8 (W12×53 braces)
- Moment frames at Grids A and F
- Central atrium opening (approximately 30' × 30')
- Stair openings at northeast and northwest corners
- Title block indicating "SECOND FLOOR FRAMING PLAN" with project information
- Scale and drawing notations typical of structural plans

---

# III-108

**Fig. III-30. 3rd & 4th floor framing plan.**

Diagram description: Structural framing plan for third and fourth floors showing:
- Building dimensions: approximately 210 ft (east-west) × 120 ft (north-south)
- Grid lines numbered 1-8 (east-west) and lettered A-F (north-south)
- Typical bay spacing: 30'-0" between columns in east-west direction, 22'-6" to 23'-0" in north-south direction
- Floor beams: W24×55 (typical) spanning north-south
- Edge beams: W18×35 at building perimeter
- Diagonal bracing at Grids 1 and 8 (W12×53 braces)
- Moment frames at Grids A and F
- Central atrium opening (approximately 30' × 30')
- Stair openings at northeast and northwest corners
- Title block indicating "3rd & 4TH FLOOR FRAMING PLAN" with project information
- Scale and drawing notations typical of structural plans

---

# III-109

**Fig. III-31. Roof framing plan.**

Diagram description: Structural framing plan for roof level showing:
- Building dimensions: approximately 210 ft (east-west) × 120 ft (north-south)
- Grid lines numbered 1-8 (east-west) and lettered A-F (north-south)
- Typical bay spacing: 30'-0" between columns in east-west direction, 22'-6" to 23'-0" in north-south direction
- Roof beams: W18×35 (typical) spanning north-south
- Edge beams: W18×35 at building perimeter
- Diagonal bracing at Grids 1 and 8 (W12×53 braces)
- Moment frames at Grids A and F
- Mechanical screen wall enclosure (approximately 30' × 30' in center)
- Stair penthouses at northeast and northwest corners
- Roof deck with typical joist spacing
- Title block indicating "ROOF FRAMING PLAN" with project information
- Scale and drawing notations typical of structural plans
- Parapet indications at building perimeter

---

# III-110

**Fig. III-32. Building sections.**

Diagram description: Multiple building section views showing:

**Top Row (4 sections):**
- Section views through different parts of the building
- Four-story building with story heights of 13'-6" each
- Total building height: 55'-0" to top of parapet
- Column elevations and floor levels clearly marked
- Moment frame connections at Grids A and F
- Diagonal bracing shown at end bays
- Roof mechanical screen wall (6' height)
- Parapet wall (2' height)

**Bottom Row (4 sections):**
- Additional section views showing:
  - Interior column alignments
  - Floor-to-floor heights
  - Foundation depths
  - Mechanical equipment locations
  - Atrium opening sections
  - Lateral force-resisting system details
  - Composite floor deck profiles
  - Beam-to-column connection details

Each section includes:
- Dimension strings for floor heights
- Grid line references
- Member size callouts
- Elevation markers
- Title block with project information
- Scale notations

---

# III-111

**Fig. III-33. Chevron brace elevation & details.**

Diagram description: Structural detail sheet showing chevron (V-shaped) braced frame connections with four main views:

**Left Panel - CHEVRON BRACE ELEVATION:**
- Four-story elevation view showing diagonal W12×53 braces in chevron configuration
- Bay width: 30'-0"
- Story heights: 14'-5" typical
- Work point elevations marked at each floor level
- Base plate and anchor rod connections at foundation
- Brace connections labeled with detail references

**Center-Left Panel - DETAIL 1 (1 1/2" = 1'-0"):**
- Column splice connection detail
- Gusset plate connection for brace-to-column
- Base plate and anchor rod arrangement
- Bolt layout and spacing dimensions
- Connection to foundation

**Center-Right Panel - DETAIL 2 (1 1/2" = 1'-0"):**
- Gusset plate detail at work point
- Brace connection showing W12×53 connection to gusset
- Column splice location relative to floor beam
- Bolt patterns and edge distances

**Right Panel - DETAIL 3 (1 1/2" = 1'-0"):**
- Beam-to-gusset connection detail
- Work point geometry
- Brace-to-gusset plate connection
- Clearance dimensions
- Welding symbols and specifications

**Bottom Row (4 panels):**
All marked "NOT USED" - reserved for additional details if needed

**Title Block:**
- Project: ABLE ENGINEERING
- Drawing title: CHEVRON BRACE ELEVATION & DETAILS
- Sheet number: S5.1
- Date and revision information
- Architect: ABC ARCHITECTS & ASSOCIATES

---

# III-112

[This page intentionally left blank]

---

# III-113

[This page shows a blank graph/grid paper]

---

# Back Cover

**AISC - American Institute of Steel Construction**

**Smarter. Stronger. Steel.**

American Institute of Steel Construction
130 E Randolph St, Ste 2000, Chicago, IL 60601
312.670.2400 | www.aisc.org

Document ID: P901-23

---
