# Chapter I: Composite

**AISC 360-22 Specification for Structural Steel Buildings**
**Original PDF Pages**: 157-188 (32 pages)
**Generated**: 2025-11-09

---

## Chapter Overview

Design of Composite Members

**Description**: Steel-concrete composite design

---

# CHAPTER I
# DESIGN OF COMPOSITE MEMBERS

This chapter addresses composite members composed of rolled or built-up structural steel shapes or HSS and structural concrete acting together, and steel beams supporting a reinforced concrete slab so interconnected that the beams and the slab act together to resist bending. Simple and continuous composite beams with steel headed stud anchors, and encased and filled beams, constructed with or without temporary shores, are included. This chapter also addresses concrete filled composite plate shear walls composed of structural steel plates, ties, steel anchors, and structural concrete acting together.

The chapter is organized as follows:

I1. General Provisions
I2. Axial Force
I3. Flexure
I4. Shear
I5. Combined Flexure and Axial Force
I6. Load Transfer
I7. Composite Diaphragms and Collector Beams
I8. Steel Anchors

## I1. GENERAL PROVISIONS

In determining load effects in members and connections of a structure that includes composite members, consideration shall be given to the effective cross sections at the time each increment of load is applied.

### 1. Concrete and Steel Reinforcement

The design, detailing, and material properties related to the concrete and reinforcing steel portions of composite construction shall comply with the reinforced concrete design specifications stipulated by the applicable building code. Additionally, the provisions of the *Building Code Requirements for Structural Concrete* (ACI 318) and the *Metric Building Code Requirements for Structural Concrete* (ACI 318M), subsequently referred to in Chapter I collectively as ACI 318, shall apply with the following exceptions and limitations:

(a) Concrete and steel reinforcement material limitations shall be as specified in Section I1.3.

(b) Longitudinal and transverse reinforcement requirements shall be as specified in Sections I2 and I3 in addition to those specified in ACI 318.

Concrete and steel reinforcement components designed in accordance with ACI 318 shall be based on a level of loading corresponding to LRFD load combinations.

---

**User Note:** It is the intent of this Specification that the concrete and reinforcing steel portions of composite concrete members are designed and detailed utilizing the provisions of ACI 318 as modified by this Specification. All requirements specific to composite steel members are covered in this Specification.

Note that the design basis for ACI 318 is strength design. Designers using ASD for steel must be conscious of the different load factors.

### 2. Nominal Strength of Composite Sections

The nominal strength of composite sections shall be determined in accordance with either the plastic stress distribution method, the strain compatibility method, the elastic stress distribution method, or the effective stress-strain method as defined in this section.

The tensile strength of the concrete shall be neglected in the determination of the nominal strength of composite members.

Local buckling effects shall be evaluated for filled composite members, as defined in Section I1.4. Local buckling effects need not be evaluated for encased composite members or composite plate shear walls meeting the requirements of this chapter.

#### 2a. Plastic Stress Distribution Method

For the plastic stress distribution method, the nominal strength shall be computed assuming that steel components have reached a stress of $F_y$ in either tension or compression, and concrete components in compression due to axial force and/or flexure have reached a stress of $0.85f_c'$, where $f_c'$ is the specified compressive strength of concrete, ksi (MPa). For round HSS filled with concrete, a stress of $0.95f_c'$ is permitted to be used for concrete components in compression due to axial force and/or flexure to account for the effects of concrete confinement.

#### 2b. Strain Compatibility Method

For the strain compatibility method, a linear distribution of strains across the section shall be assumed, with the maximum concrete compressive strain equal to 0.003 in./in. (mm/mm). The stress-strain relationships for steel and concrete shall be obtained from tests or from published results.

**User Note:** The strain compatibility method can be used to determine nominal strength for irregular sections and for cases where the steel does not exhibit elasto-plastic behavior. General guidelines for the strain compatibility method for encased members subjected to axial load, flexure, or both are given in AISC Design Guide 6, *Load and Resistance Factor Design of W-Shapes Encased in Concrete*.

#### 2c. Elastic Stress Distribution Method

For the elastic stress distribution method, the nominal strength shall be determined from the superposition of elastic stresses for the limit state of yielding or concrete crushing.

---

#### 2d. Effective Stress-Strain Method

For the effective stress-strain method, the nominal strength shall be computed assuming strain compatibility and effective stress-strain relationships for structural steel, reinforcing steel, and concrete components accounting for the effects of local buckling, yielding, interaction, and concrete confinement.

### 3. Material Limitations

For concrete, structural steel, and reinforcing steel in composite systems, the following limitations shall be met unless the design is based on the requirements of Appendix 2:

(a) For the determination of the available strength, concrete shall have a specified compressive strength, $f_c'$, of not less than 3 ksi (21 MPa) and not more than 10 ksi (69 MPa) for normal weight concrete and not less than 3 ksi (21 MPa) nor more than 6 ksi (41 MPa) for lightweight concrete.

(b) The specified minimum yield stress of structural steel used in calculating the strength of composite members shall not exceed 75 ksi (525 MPa).

(c) The specified minimum yield stress of reinforcing bars used in calculating the strength of composite members shall not exceed 80 ksi (550 MPa).

The design of filled composite members constructed from materials with strengths above the limits noted in this section shall be in accordance with Appendix 2.

**User Note:** Appendix 2 includes equations for determining the available strength of rectangular filled composite members with either the specified minimum yield stress of structural steel exceeding 75 ksi (525 MPa) but less than 100 ksi (690 MPa) or specified compressive strength, $f_c'$, exceeding 10 ksi (69 MPa) but less than 15 ksi (100 MPa).

### 4. Classification of Filled Composite Sections for Local Buckling

For compression, filled composite sections are classified as compact composite, noncompact composite, or slender-element composite sections. For a section to qualify as compact composite, the maximum width-to-thickness ratio, $\lambda$, of its compression steel elements shall not exceed the limiting width-to-thickness ratio, $\lambda_p$, from Table I1.1a. If the maximum width-to-thickness ratio of one or more steel compression elements exceeds $\lambda_p$, but does not exceed $\lambda_r$ from Table I1.1a, the filled composite section is noncompact composite. If the maximum width-to-thickness ratio of any compression steel element exceeds $\lambda_r$, the section is slender-element composite. The maximum permitted width-to-thickness ratio shall be as specified in Table I1.1a.

For flexure, filled composite sections are classified as compact composite, noncompact composite, or slender-element composite sections. For a section to qualify as compact composite, the maximum width-to-thickness ratio of its compression steel elements shall not exceed the limiting width-to-thickness ratio, $\lambda_p$, from Table I1.1b. If the maximum width-to-thickness ratio of one or more steel compression elements

---

<!-- Table: I1.1a - Limiting Width-to-Thickness Ratios for Compression Steel Elements in Composite Members Subjected to Axial Compression -->

<table>
  <thead>
    <tr>
      <th colspan="5" style="text-align: center;"><strong>TABLE I1.1a</strong><br><strong>Limiting Width-to-Thickness Ratios for<br>Compression Steel Elements in Composite<br>Members Subjected to Axial Compression<br>for Use with Section I2.2</strong></th>
    </tr>
    <tr>
      <th>Description of<br>Element</th>
      <th>Width-to-<br>Thickness<br>Ratio</th>
      <th>$\lambda_p$<br>Compact<br>Composite/<br>Noncompact<br>Composite</th>
      <th>$\lambda_r$<br>Noncompact<br>Composite/<br>Slender-<br>Element<br>Composite</th>
      <th>Maximum<br>Permitted</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Walls of rectangular<br>HSS and box sections<br>of uniform thickness</td>
      <td>$b/t$</td>
      <td>$2.26\sqrt{\frac{E}{F_y}}$</td>
      <td>$3.00\sqrt{\frac{E}{F_y}}$</td>
      <td>$5.00\sqrt{\frac{E}{F_y}}$</td>
    </tr>
    <tr>
      <td>Round HSS</td>
      <td>$D/t$</td>
      <td>$\frac{0.15E}{F_y}$</td>
      <td>$\frac{0.19E}{F_y}$</td>
      <td>$\frac{0.31E}{F_y}$</td>
    </tr>
  </tbody>
</table>

**Table summary**: Limiting width-to-thickness ratios for compression steel elements in composite members subjected to axial compression. Includes compact, noncompact, and slender element classifications for rectangular HSS and round HSS.

<!-- Table: I1.1b - Limiting Width-to-Thickness Ratios for Compression Steel Elements in Composite Members Subjected to Flexure -->

<table>
  <thead>
    <tr>
      <th colspan="5" style="text-align: center;"><strong>TABLE I1.1b</strong><br><strong>Limiting Width-to-Thickness Ratios for<br>Compression Steel Elements in Composite<br>Members Subjected to Flexure<br>for Use with Section I3.4</strong></th>
    </tr>
    <tr>
      <th>Description of<br>Element</th>
      <th>Width-to-<br>Thickness<br>Ratio</th>
      <th>$\lambda_p$<br>Compact<br>Composite/<br>Noncompact<br>Composite</th>
      <th>$\lambda_r$<br>Noncompact<br>Composite/<br>Slender-<br>Element<br>Composite</th>
      <th>Maximum<br>Permitted</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Flanges of rectangular<br>HSS and box sections<br>of uniform thickness</td>
      <td>$b/t$</td>
      <td>$2.26\sqrt{\frac{E}{F_y}}$</td>
      <td>$3.00\sqrt{\frac{E}{F_y}}$</td>
      <td>$5.00\sqrt{\frac{E}{F_y}}$</td>
    </tr>
    <tr>
      <td>Webs of rectangular<br>HSS and box sections<br>of uniform thickness</td>
      <td>$h/t$</td>
      <td>$3.00\sqrt{\frac{E}{F_y}}$</td>
      <td>$5.70\sqrt{\frac{E}{F_y}}$</td>
      <td>$5.70\sqrt{\frac{E}{F_y}}$</td>
    </tr>
    <tr>
      <td>Round HSS</td>
      <td>$D/t$</td>
      <td>$\frac{0.09E}{F_y}$</td>
      <td>$\frac{0.31E}{F_y}$</td>
      <td>$\frac{0.31E}{F_y}$</td>
    </tr>
  </tbody>
</table>

**Table summary**: Limiting width-to-thickness ratios for compression steel elements in composite members subjected to flexure. Includes compact, noncompact, and slender element classifications for flanges, webs, and round HSS.

exceeds $\lambda_p$, but does not exceed $\lambda_r$ from Table I1.1b, the section is noncompact composite. If the width-to-thickness ratio of any steel element exceeds $\lambda_r$, the section is slender-element composite. The maximum permitted width-to-thickness ratio shall be as specified in Table I1.1b.

Refer to Section B4.1b for definitions of width, $b$ and $D$, and thickness, $t$, for rectangular and round HSS sections and box sections of uniform thickness.

---

**User Note:** All current ASTM A500/A500M Grade C square HSS sections are compact composite according to the limits of Table I1.1a and Table I1.1b, except HSS7×7×⅜, HSS8×8×⅜, HSS10×10×⅜, HSS12×12×⁹⁄₁₆, HSS14×14×⅜, HSS16×16×⅜, HSS18×18×⁹⁄₁₆, and HSS20×20×⁹⁄₁₆, which are noncompact composite for both axial compression and flexure, and HSS9×9×⅛ and HSS18×18×¼, which are slender-element composite for both axial compression and flexure.

All current ASTM A1085/A1085M square HSS are compact composite except for HSS8×8×⅛, HSS 9×9×⅛, HSS 12×12×⁵⁄₁₆, HSS16×16×⅛, HSS18×18×¼, HSS18×18×⁵⁄₁₆, and HSS 20×20×⁵⁄₁₆, which are noncompact composite for both axial compression and flexure.

All current ASTM A500/A500M Grade C round HSS sections are compact composite according to the limits of Table I1.1a and Table I1.1b for both axial compression and flexure, with the exception of HSS6.625×0.125, HSS9.625×0.125, HSS9.625×0.188, HSS10.75×0.188, HSS12.750×0.188, HSS12.750×0.250, HSS13.375×0.188, HSS13.375×0.250, HSS14.000×0.188, HSS14.000×0.250, HSS16.000×0.250, HSS16.000×0.312, HSS18.000×0.250, HSS18.000×0.313, HSS20.000×0.250, HSS20.000×0.313, HSS22.000×0.375, HSS20.000×0.313, HSS22.000×0.375, HSS24.000×0.313, HSS24.000×0.375, HSS26.000×0.375, HSS26.000×0.500, HSS28.000×0.375, and HSS28.000×0.500, which are noncompact composite for flexure, and HSS26.000×0.313, which is noncompact for compression and flexure.

### 5. Stiffness for Calculation of Required Strengths

For the direct analysis method of design, the required strengths of encased composite members, filled composite members, and composite plate shear walls shall be determined using the provisions of Section C2 and the following requirements:

(a) The nominal flexural stiffness of encased and filled composite members subjected to net compression shall be taken as the effective stiffness of the composite section, $(EI)_{eff}$, as defined in Section I2.

(b) The nominal axial stiffness of encased and filled composite members subjected to net compression shall be taken as the summation of the elastic axial stiffnesses of each component.

(c) The stiffness of encased and filled composite members subjected to net tension shall be taken as the stiffness of the bare steel members in accordance with Chapter C.

(d) The stiffness reduction parameter, $\tau_b$, shall be taken as 0.8 for encased and filled composite members.

---

**User Note:** Taken together, the stiffness reduction factors require the use of $0.64(EI)_{eff}$ for the flexural stiffness and 0.8 times the nominal axial stiffness of encased composite members and filled composite members subjected to net compression in the analysis.

Stiffness values appropriate for the calculation of deflections and for use with the effective length method are discussed in the Commentary.

(e) The flexural stiffness, $(EI)_{eff}$, axial stiffness, $(EA)_{eff}$, and shear stiffness, $(GA)_{eff}$, of composite plate shear walls shall account for the extent of concrete cracking under LRFD load combinations or 1.6 times the ASD load combinations. It is permitted to use the following to estimate effective stiffness:

$$(EI)_{eff} = E_s I_s + 0.35E_c I_c$$ (I1-1)

$$(EA)_{eff} = E_s A_s + 0.45E_c A_c$$ (I1-2)

$$(GA)_{eff} = G_s A_{sw} + G_c A_c$$ (I1-3)

where

$A_c$ = area of concrete, in.$^2$ (mm$^2$)

$A_s$ = area of steel section, in.$^2$ (mm$^2$)

$A_{sw}$ = area of steel plates in the direction of in-plane shear, in.$^2$ (mm$^2$)

$E_c$ = modulus of elasticity of concrete
    = $w_c^{1.5}\sqrt{f_c'}$, ksi $(0.043w_c^{1.5}\sqrt{f_c'}$, MPa)

$E_s$ = modulus of elasticity of steel
    = 29,000 ksi (200 000 MPa)

$G_c$ = shear modulus of concrete
    = $0.4E_c$

$G_s$ = shear modulus of steel
    = 11,200 ksi (77 200 MPa)

$I_c$ = moment of inertia of the concrete section about the elastic neutral axis of the composite section, in.$^4$ (mm$^4$)

$I_s$ = moment of inertia of steel shape about the elastic neutral axis of the composite section, in.$^4$ (mm$^4$)

$w_c$ = weight of concrete per unit volume $(90 \leq w_c \leq 155 \text{ lb/ft}^3$ or $1\,500 \leq w_c \leq 2\,500 \text{ kg/m}^3)$

(f) The stiffness reduction parameter, $\tau_b$, shall be taken as 1.0 for composite plate shear walls.

### 6. Requirements for Composite Plate Shear Walls

The steel plates shall comprise at least 1% but no more than 10% of the total composite cross-sectional area. The opposing steel plates shall be connected to each other using ties consisting of bars, structural shapes, or built-up members. For filled composite plate shear walls, the steel plates shall be anchored to the concrete using ties or steel anchors. Walls without flange (closure) plates or boundary elements are not permitted.

---

### 6a. Slenderness Requirement

The slenderness ratio of the plates, $b/t$, shall be limited as follows:

$$\frac{b}{t} \leq 1.2\sqrt{\frac{E}{F_y}}$$ (I1-4)

where

$b$ = largest clear distance between rows of steel anchors or ties, in. (mm)

$t$ = thickness of plate, in. (mm)

### 6b. Tie Bar Requirement

The bars shall have spacing no greater than 1.0 times the wall thickness, $t_{sc}$. The tie bar spacing to plate thickness ratio, $s_t/t$, shall be limited as follows:

$$\frac{s_t}{t} \leq 1.0\sqrt{\frac{E_s}{2\alpha + 1}}$$ (I1-5)

$$\frac{s_t}{t} \leq 0.38\sqrt{\frac{E_s}{2\alpha + 1}}$$ (I1-5M)

$$\alpha = 1.7\left(\frac{t_{sc}}{t} - 2\right)\left(\frac{t}{d_{tie}}\right)^4$$ (I1-6)

where

$d_{tie}$ = effective diameter of the tie bar, in. (mm)

$s_t$ = largest clear spacing of the ties, in. (mm)

$t$ = thickness of plate, in. (mm)

$t_{sc}$ = thickness of composite plate shear wall, in. (mm)

## I2. AXIAL FORCE

This section applies to encased composite members, filled composite members, and composite plate shear walls subjected to axial force.

### 1. Encased Composite Members

#### 1a. Limitations

For encased composite members, the following limitations shall be met:

(a) The cross-sectional area of the steel core shall comprise at least 1% of the total composite cross section.

(b) Concrete encasement of the steel core shall be reinforced with continuous longitudinal bars and transverse reinforcement consisting of ties, hoops, and/or spirals.

    Detailing and placement of longitudinal reinforcement, including bar spacing and concrete cover requirements, shall conform to ACI 318.

    Transverse reinforcement where specified as ties or hoops shall consist of a minimum of either a No. 3 (10 mm) bar spaced at a maximum of 12 in. (300 mm) on center, or a No. 4 (13 mm) bar or larger spaced at a maximum of 16 in.

---

(400 mm) on center. Deformed wire or welded wire reinforcement of equivalent area is permitted.

Maximum spacing of ties or hoops shall not exceed 0.5 times the smaller column dimension.

(c) The minimum reinforcement ratio for continuous longitudinal reinforcement, $\rho_{sr}$, shall be 0.004, where $\rho_{sr}$ is given by

$$\rho_{sr} = \frac{A_{sr}}{A_g}$$ (I2-1)

where

$A_g$ = gross area of composite member, in.$^2$ (mm$^2$)

$A_{sr}$ = area of continuous longitudinal reinforcing bars, in.$^2$ (mm$^2$)

(d) The maximum reinforcement ratio for continuous longitudinal reinforcement, $\rho_{sr}$, shall meet ACI 318 with the gross area of concrete, $A_g$, assumed in the calculations.

**User Note:** Refer to ACI 318 for additional longitudinal and transverse steel provisions. Refer to Section I4 for shear requirements.

#### 1b. Compressive Strength

The design compressive strength, $\phi_c P_n$, and allowable compressive strength, $P_n/\Omega_c$, of doubly symmetric axially loaded encased composite members shall be determined for the limit state of flexural buckling based on member slenderness as follows:

$$\phi_c = 0.75 \text{ (LRFD)} \qquad \Omega_c = 2.00 \text{ (ASD)}$$

(a) When $\frac{P_{no}}{P_e} \leq 2.25$

$$P_n = P_{no}\left(0.658^{\frac{P_{no}}{P_e}}\right)$$ (I2-2)

(b) When $\frac{P_{no}}{P_e} > 2.25$

$$P_n = 0.877P_e$$ (I2-3)

where

$P_e$ = elastic critical buckling load determined in accordance with Chapter C or Appendix 7, kips (N)

    = $\frac{\pi^2(EI)_{eff}}{L_c^2}$ (I2-4)

$(EI)_{eff}$ = effective stiffness of composite section, kip-in.$^2$ (N-mm$^2$)

    = $E_s I_s + E_s I_{sr} + C_1 E_c I_c$ (I2-5)

$C_1$ = coefficient for calculation of effective rigidity of an encased composite compression member

    = $0.25 + 3\left(\frac{A_s + A_{sr}}{A_g}\right) \leq 0.7$ (I2-6)

$E_c$ = modulus of elasticity of concrete

    = $w_c^{1.5}\sqrt{f_c'}$, ksi $(0.043w_c^{1.5}\sqrt{f_c'}$, MPa)

---

$f_c'$ = specified compressive strength of concrete, ksi (MPa)

$w_c$ = weight of concrete per unit volume $(90 \leq w_c \leq 155 \text{ lb/ft}^3$ or $1\,500 \leq w_c \leq 2\,500 \text{ kg/m}^3)$

$E_s$ = modulus of elasticity of steel
    = 29,000 ksi (200 000 MPa)

$I_c$ = moment of inertia of the concrete section about the elastic neutral axis of the composite section, in.$^4$ (mm$^4$)

$I_s$ = moment of inertia of steel shape about the elastic neutral axis of the composite section, in.$^4$ (mm$^4$)

$I_{sr}$ = moment of inertia of reinforcing bars about the elastic neutral axis of the composite section, in.$^4$ (mm$^4$)

$L_c$ = effective length of the member, in. (mm)
    = $KL$

$K$ = effective length factor

$L$ = laterally unbraced length of the member, in. (mm)

$P_{no}$ = nominal axial compressive strength without consideration of length effects, kips (N)

    = $F_y A_s + F_{sr} A_{sr} + 0.85 f_c' A_c$ (I2-7)

$A_c$ = area of concrete, in.$^2$ (mm$^2$)

$A_s$ = cross-sectional area of structural steel section, in.$^2$ (mm$^2$)

$F_y$ = specified minimum yield stress of structural steel section, ksi (MPa)

$F_{yr}$ = specified minimum yield stress of reinforcing steel, ksi (MPa)

The available compressive strength need not be less than that determined for the bare steel member in accordance with Chapter E.

#### 1c. Tensile Strength

The available tensile strength of axially loaded encased composite members shall be determined for the limit state of yielding as

$$P_n = F_y A_s + F_{yr} A_{sr}$$ (I2-8)

$$\phi_t = 0.90 \text{ (LRFD)} \qquad \Omega_t = 1.67 \text{ (ASD)}$$

#### 1d. Load Transfer

Load transfer requirements for encased composite members shall be determined in accordance with Section I6.

#### 1e. Detailing Requirements

For encased composite members, the following detailing requirements shall be met:

(a) Clear spacing between the steel core and longitudinal reinforcing bars shall be a minimum of 1.5 longitudinal reinforcing bar diameters, but not less than 1.5 in. (38 mm).

(b) If the composite cross section is built up from two or more encased steel shapes, the shapes shall be interconnected with lacing, tie plates, or comparable components to prevent buckling of individual shapes due to loads applied prior to hardening of the concrete.

---

**User Note:** Refer to ACI 318 for additional longitudinal and transverse reinforcing steel requirements. Refer to Section I4 for requirements for members subjected to shear. The requirements of Section I2.1.1e are not applicable to composite plate shear walls.

### 2. Filled Composite Members

#### 2a. Limitations

For filled composite members, the following limitations shall be met:

(a) The cross-sectional area of the structural steel section shall comprise at least 1% of the total composite cross section.

(b) Filled composite members shall be classified for local buckling according to Section I1.4.

(c) Minimum longitudinal reinforcement is not required. If longitudinal reinforcement is provided, internal transverse reinforcement is not required for strength; however, minimum internal transverse reinforcement shall be provided. Transverse reinforcement where specified as ties or hoops shall consist of a minimum of either a No. 3 (10 mm) bar spaced at a maximum of 12 in. (300 mm) on center, or a No. 4 (13 mm) bar or larger spaced at a maximum of 16 in. (400 mm) on center. Deformed wire or welded wire reinforcement of equivalent area is permitted.

(d) If longitudinal reinforcing steel is provided for strength, the maximum reinforcement ratio $\rho_{sr}$ shall be based on ACI 318 requirements for 0.8 times the gross area of concrete.

**User Note:** Refer to ACI 318 for additional longitudinal and transverse steel provisions. Refer to Section I4 and Section I4 Commentary for shear on filled composite members.

#### 2b. Compressive Strength

The available compressive strength of axially loaded doubly symmetric filled composite members shall be determined for the limit state of flexural buckling in accordance with Section I2.1b with the following modifications:

(a) For compact composite sections

$$P_{no} = P_p$$ (I2-9a)

where

$P_p$ = plastic axial compressive strength, kips (N)

    = $F_y A_s + C_2 f_c'\left(A_c + A_{sr}\frac{E_s}{E_c}\right)$ (I2-9b)

$C_2 = 0.85$ for rectangular sections and $0.95$ for round sections

(b) For noncompact composite sections

$$P_{no} = P_p - \frac{P_p - P_y}{\left(\lambda_r - \lambda_p\right)^2}\left(\lambda - \lambda_p\right)^2$$ (I2-9c)

---

where

$\lambda_p$ and $\lambda_r$ are width-to-thickness ratios determined from Table I1.1a.

$P_p$ is determined from Equation I2-9b.

$$P_y = F_y A_s + 0.7 f_c'\left(A_c + A_{sr}\frac{E_s}{E_c}\right)$$ (I2-9d)

(c) For slender composite sections

$$P_{no} = F_n A_s + 0.7 f_c'\left(A_c + A_{sr}\frac{E_s}{E_c}\right)$$ (I2-9e)

where

the critical buckling stress for the structural steel section of filled composite members, $F_n$, is determined as follows:

(1) For rectangular filled sections

$$F_n = \frac{9E_s}{\lambda^2}$$ (I2-10)

(2) For round filled sections

$$F_n = \frac{0.72F_y}{\left[\left(\frac{D}{t}\right)\frac{F_y}{E_s}\right]^{0.2}}$$ (I2-11)

See Section I1.4 for definitions of maximum width-to-thickness ratio, $\lambda$; width, $D$; and thickness, $t$, for rectangular and round HSS and box sections of uniform thickness.

The effective stiffness of the composite section, $(EI)_{eff}$, for all sections shall be

$$(EI)_{eff} = E_s I_s + E_s I_{sr} + C_3 E_c I_c$$ (I2-12)

where

$C_3$ = coefficient for calculation of effective rigidity of a filled composite compression member

    = $0.45 + 3\left(\frac{A_s + A_{sr}}{A_g}\right) \leq 0.9$ (I2-13)

The available compressive strength need not be less than that determined for the bare steel member in accordance with Chapter E.

#### 2c. Tensile Strength

The available tensile strength of axially loaded filled composite members shall be determined for the limit state of yielding as

$$P_n = A_s F_y + A_{sr} F_{yr}$$ (I2-14)

$$\phi_t = 0.90 \text{ (LRFD)} \qquad \Omega_t = 1.67 \text{ (ASD)}$$

#### 2d. Load Transfer

Load transfer requirements for filled composite members shall be determined in accordance with Section I6.

---

#### 2e. Detailing Requirements

Clear spacing between the inside of the structural steel section and longitudinal reinforcing steel, where provided, shall be a minimum of 1.5 reinforcing bar diameters, but not less than 1.5 in. (38 mm).

### 3. Composite Plate Shear Walls

#### 3a. Compressive Strength

The available compressive strength of axially loaded composite plate shear walls shall be determined for the limit state of flexural buckling in accordance with Section I2.1b. The value of flexural stiffness from Section I1.5 shall be used along with $P_{no}$ determined as follows:

$$P_{no} = F_y A_s + 0.85 f_c' A_c$$ (I2-15)

$$\phi_c = 0.90 \text{ (LRFD)} \qquad \Omega_c = 1.67 \text{ (ASD)}$$

#### 3b. Tensile Strength

The available tensile strength of axially loaded composite plate shear walls shall be determined for the limit state of yielding as

$$P_n = A_s F_y$$ (I2-16)

$$\phi_t = 0.90 \text{ (LRFD)} \qquad \Omega_t = 1.67 \text{ (ASD)}$$

## I3. FLEXURE

This section applies to three types of composite members subjected to flexure: composite beams with steel anchors consisting of steel headed stud anchors or steel channel anchors, encased members, and filled members.

### 1. General

#### 1a. Effective Width

The effective width of the concrete slab shall be the sum of the effective widths for each side of the beam centerline, each of which shall not exceed

(a) one-eighth of the beam span, center-to-center of supports;

(b) one-half the distance to the centerline of the adjacent beam; or

(c) the distance to the edge of the slab.

#### 1b. Strength During Construction

When temporary shores are not used during construction, the structural steel section alone shall have sufficient strength to support all loads applied prior to the concrete attaining 75% of its specified strength, $f_c'$. The available flexural strength of the steel section shall be determined in accordance with Chapter F.

---

### 2. Composite Beams with Steel Headed Stud or Steel Channel Anchors

#### 2a. Positive Flexural Strength

The design positive flexural strength, $\phi_b M_n$, and allowable positive flexural strength, $M_n/\Omega_b$, shall be determined for the limit state of yielding as follows:

$$\phi_b = 0.90 \text{ (LRFD)} \qquad \Omega_b = 1.67 \text{ (ASD)}$$

(a) When $h/t_w \leq 3.76\sqrt{E/F_y}$

$M_n$ shall be determined from the plastic stress distribution on the composite section for the limit state of yielding (plastic moment).

**User Note:** All current ASTM A6/A6M W, S, and HP shapes satisfy the limit given in Section I3.2a(a) for $F_y \leq 70$ ksi (485 MPa).

(b) When $h/t_w > 3.76\sqrt{E/F_y}$

$M_n$ shall be determined from the superposition of elastic stresses, considering the effects of shoring, for the limit state of yielding (yield moment).

#### 2b. Negative Flexural Strength

The available negative flexural strength shall be determined for the structural steel section alone, in accordance with the requirements of Chapter F.

Alternatively, the available negative flexural strength shall be determined from the plastic stress distribution for the composite section, for the limit state of yielding (plastic moment), with

$$\phi_b = 0.90 \text{ (LRFD)} \qquad \Omega_b = 1.67 \text{ (ASD)}$$

provided that the following limitations are met:

(a) The steel beam is compact and is braced in accordance with Chapter F.

(b) Steel headed stud or steel channel anchors connect the slab to the steel beam in the negative moment region.

(c) The slab longitudinal reinforcement parallel to the steel beam, within the effective width of the slab, meets the development length requirements.

**User Note:** To check compactness of a composite beam in negative flexure, Case 10 in Table B4.1b is appropriate to use for flanges, and Case 15 of Table B4.1b is appropriate to use for webs.

#### 2c. Composite Beams with Formed Steel Deck

**1. General**

The available flexural strength of composite construction consisting of concrete slabs on formed steel deck connected to steel beams shall be determined

---

by the applicable portions of Sections I3.2a and I3.2b, with the following requirements:

(a) The nominal rib height shall not be greater than 3 in. (75 mm). The average width of concrete rib or haunch, $w_r$, shall not be less than 2 in. (50 mm), but shall not be taken in calculations as more than the minimum clear width near the top of the steel deck.

(b) The concrete slab shall be connected to the steel beam with steel headed stud anchors welded either through the deck or directly to the steel cross section. Steel headed stud anchors, after installation, shall extend not less than 1½ in. (38 mm) above the top of the steel deck and there shall be at least ½ in. (13 mm) of specified concrete cover above the top of the steel headed stud.

(c) The slab thickness above the steel deck shall be not less than 2 in. (50 mm).

(d) Steel deck shall be anchored to all supporting members at a spacing not to exceed 18 in. (450 mm). Such anchorage shall be provided by steel headed stud anchors, a combination of steel headed stud anchors and arc spot (puddle) welds, or other devices specified by the design documents and specifications issued for construction.

**2. Deck Ribs Oriented Perpendicular to Steel Beam**

Concrete below the top of the steel deck shall be neglected in determining composite section properties and in calculating $A_c$ for deck *ribs* oriented perpendicular to the steel beams.

**3. Deck Ribs Oriented Parallel to Steel Beam**

Concrete below the top of the steel deck is permitted to be included in determining composite section properties and in calculating $A_c$.

Formed steel deck ribs over supporting beams are permitted to be split longitudinally and separated to form a concrete haunch.

When the nominal depth of steel deck is 1½ in. (38 mm) or greater, the average width, $w_r$, of the supported haunch or rib shall be not less than 2 in. (50 mm) for the first steel headed stud anchor in the transverse row plus four diameters for each additional steel headed stud anchor.

#### 2d. Load Transfer Between Steel Beam and Concrete Slab

**1. Load Transfer for Positive Flexural Strength**

The entire horizontal shear at the interface between the steel beam and the concrete slab shall be assumed to be transferred by steel headed stud or steel channel anchors, except for concrete-encased beams as defined in Section I3.3. For composite action with concrete subjected to flexural compression, the nominal shear force between the steel beam and the concrete slab transferred by steel anchors, $V'$, between the point of maximum positive moment and the point of zero moment shall be determined as the lowest value in accordance with the limit states of concrete crushing, tensile yielding of the steel section, or the shear strength of the steel anchors:

---

(a) Concrete crushing

$$V' = 0.85f_c'A_c$$ (I3-1a)

(b) Tensile yielding of the steel section

$$V' = F_yA_s$$ (I3-1b)

(c) Shear strength of steel headed stud or steel channel anchors

$$V' = \Sigma Q_n$$ (I3-1c)

where

$A_c$ = area of concrete slab within effective width, in.$^2$ (mm$^2$)

$A_s$ = cross-sectional area of structural steel section, in.$^2$ (mm$^2$)

$\Sigma Q_n$ = sum of nominal shear strengths of steel headed stud or steel channel anchors between the point of maximum positive moment and the point of zero moment, kips (N)

The effect of ductility (slip capacity) of the shear connection at the interface of the concrete slab and the steel beam shall be considered.

**2. Load Transfer for Negative Flexural Strength**

In continuous composite beams where longitudinal reinforcing steel in the negative moment regions is considered to act compositely with the steel beam, the total horizontal shear between the point of maximum negative moment and the point of zero moment shall be determined as the lower value in accordance with the following limit states:

(a) For the limit state of tensile yielding of the slab longitudinal reinforcement

$$V' = F_{yr}A_{sr}$$ (I3-2a)

where

$A_{sr}$ = area of developed longitudinal reinforcing steel within the effective width of the concrete slab, in.$^2$ (mm$^2$)

$F_{yr}$ = specified minimum yield stress of the reinforcing steel, ksi (MPa)

(b) For the limit state of shear strength of steel headed stud or steel channel anchors

$$V' = \Sigma Q_n$$ (I3-2b)

### 3. Encased Composite Members

#### 3a. Limitations

For encased composite members, the following limitations shall be met:

(a) The available flexural strength of concrete-encased members shall be determined as follows:

$$\phi_b = 0.90 \text{ (LRFD)} \qquad \Omega_b = 1.67 \text{ (ASD)}$$

The nominal flexural strength, $M_n$, shall be determined using one of the following methods:

(1) The superposition of elastic stresses on the composite section, considering the effects of shoring for the limit state of yielding (yield moment).

---

(2) The plastic stress distribution on the steel section alone, for the limit state of yielding (plastic moment) on the steel section.

(3) The plastic stress distribution on the composite section or the strain-compatibility method, for the limit state of yielding (plastic moment) on the composite section. For concrete-encased members, steel anchors shall be provided.

(b) The total cross-sectional area of the steel core shall comprise at least 1% of the total composite cross section.

(c) Concrete encasement of the steel core shall be reinforced with continuous longitudinal bars and transverse reinforcement (stirrups, ties, hoops, or spirals).

    Detailing of longitudinal reinforcement, including bar spacing and concrete cover requirements, shall conform to ACI 318.

    Transverse reinforcement that consists of stirrups, ties, or hoops shall be a minimum of a No. 3 (10 mm) bar spaced at a maximum of 12 in. (300 mm) on center, or a No. 4 (13 mm) bar or larger spaced at a maximum of 16 in. (400 mm) on center. Deformed wire or welded wire reinforcement of equivalent area is permitted.

(d) The minimum reinforcement ratio for continuous longitudinal reinforcement, $\rho_{sr}$, shall be 0.004, where $\rho_{sr}$ is given by

$$\rho_{sr} = \frac{A_{sr}}{A_g}$$ (I3-3)

where

$A_g$ = gross area of composite member, in.$^2$ (mm$^2$)

$A_{sr}$ = area of continuous longitudinal reinforcing bars, in.$^2$ (mm$^2$)

(e) Composite beam members with $P_n < 0.10P_p$ shall be tension controlled as defined in ACI 318. The determination of $P_n$ shall include the area of both the structural steel section and the longitudinal reinforcement.

**User Note:** The effect of this limitation is to restrict the reinforcement ratio to provide ductile behavior in case of an overload. Refer to ACI 318 for additional longitudinal and transverse steel provisions. Refer to Section I4 for shear requirements.

#### 3b. Detailing Requirements

Clear spacing between the steel core and longitudinal reinforcing steel shall be a minimum of 1.5 reinforcing bar diameters, but not less than 1.5 in. (38 mm).

### 4. Filled Composite Members

#### 4a. Limitations

For filled composite members, the following limitations shall be met:

(a) Filled composite sections shall be classified for local buckling according to Section I1.4.

---

(b) The total cross-sectional area of the structural steel section shall comprise at least 1% of the total composite cross section.

(c) Longitudinal reinforcement is not required.

    Where longitudinal reinforcement is provided, the minimum reinforcement ratio for continuous longitudinal reinforcement, $\rho_{sr}$, shall be 0.004, where $\rho_{sr}$ is given by

$$\rho_{sr} = \frac{A_{sr}}{A_g}$$ (I3-4)

    If longitudinal reinforcement is provided, internal transverse reinforcement is not required for strength; however, minimum internal transverse reinforcement shall be provided. The minimum transverse reinforcement shall be hoops and ties or hoops alone consisting of a minimum of either a No. 3 (10 mm) bar spaced at a maximum of 12 in. (300 mm) on center, or a No. 4 (13 mm) bar or larger spaced at a maximum of 16 in. (400 mm) on center. Deformed wire or welded wire reinforcement of equivalent area is permitted.

(d) Composite beam members with $P_n < 0.10P_p$ shall be tension controlled as defined in ACI 318. The determination of $P_n$ shall include the area of both the structural steel section and the longitudinal reinforcement.

**User Note:** The effect of this limitation is to restrict the longitudinal reinforcement ratio to provide ductile behavior in case of an overload. Refer to ACI 318 for additional provisions for the longitudinal and transverse steel reinforcement. Refer to Section I4 for shear requirements. The limitations and requirements of Section I3.4a are not applicable to composite plate shear walls.

#### 4b. Flexural Strength

The available flexural strength of filled composite members shall be determined as follows:

$$\phi_b = 0.90 \text{ (LRFD)} \qquad \Omega_b = 1.67 \text{ (ASD)}$$

The nominal flexural strength, $M_n$, shall be determined as follows:

(a) For compact composite sections

$$M_n = M_p$$ (I3-5a)

where

$M_p$ = moment corresponding to plastic stress distribution over the composite cross section, kip-in. (N-mm)

(b) For noncompact composite sections

$$M_n = M_p - \left(M_p - M_y\right)\left(\frac{\lambda - \lambda_p}{\lambda_r - \lambda_p}\right)$$ (I3-5b)

where

$\lambda$, $\lambda_p$, and $\lambda_r$ are width-to-thickness ratios determined from Table I1.1b.

---

$M_y$ = yield moment corresponding to yielding of the tension flange and first yield of the compression flange, kip-in. (N-mm). The capacity at first yield shall be calculated assuming a linear elastic stress distribution with the maximum concrete compressive stress limited to $0.7f_c'$ and the maximum steel stress limited to $F_y$.

(c) For slender-element composite sections, $M_n$ shall be determined as the first yield moment. The compression flange stress shall be limited to the critical buckling stress, $F_n$, determined using Equation I2-10 or I2-11. The concrete stress distribution shall be linear elastic with the maximum compressive stress limited to $0.70f_c'$.

#### 4c. Detailing Requirements

Clear spacing between the inside of the steel section and longitudinal reinforcing steel where provided shall be a minimum of 1.5 reinforcing bar diameters, but not less than 1.5 in. (38 mm).

### 5. Composite Plate Shear Walls

The available flexural strength of composite plate shear walls shall be determined in accordance with Section I1.2, where

$$\phi_b = 0.90 \text{ (LRFD)} \qquad \Omega_b = 1.67 \text{ (ASD)}$$

## I4. SHEAR

### 1. Encased Composite Members

The design shear strength, $\phi_v V_n$, and allowable shear strength, $V_n/\Omega_v$, of encased composite members shall be determined based on one of the following:

(a) The available shear strength of the structural steel section alone as specified in Chapter G.

(b) The available shear strength of the reinforced concrete portion (concrete plus transverse reinforcement) alone as defined by ACI 318 with

$$\phi_v = 0.75 \text{ (LRFD)} \qquad \Omega_v = 2.00 \text{ (ASD)}$$

(c) The nominal shear strength of the structural steel section, as defined in Chapter G, plus the nominal strength of the transverse reinforcement, as defined by ACI 318, with a combined resistance or safety factor of

$$\phi_v = 0.75 \text{ (LRFD)} \qquad \Omega_v = 2.00 \text{ (ASD)}$$

### 2. Filled Composite Members

The design shear strength, $\phi_v V_n$, and allowable shear strength, $V_n/\Omega_v$, of filled composite members shall be determined as follows:

$$\phi_v = 0.90 \text{ (LRFD)} \qquad \Omega_v = 1.67 \text{ (ASD)}$$

The nominal shear strength, $V_n$, shall include the contributions of the structural steel section and concrete infill as follows:

---

$$V_n = 0.6A_vF_y + 0.06K_cA_c\sqrt{f_c'}$$ (I4-1)

where

$A_v$ = shear area of the steel portion of a composite member. The shear area for a round section is equal to $2A_s/\pi$, and for a rectangular section is equal to the sum of the area of webs in the direction of in-plane shear, in.$^2$ (mm$^2$)

$A_c$ = area of concrete infill, in.$^2$ (mm$^2$)

$K_c$ = 1 for members with shear span-to-depth, $(M_u/V_u)/d$, greater than or equal to 0.7, where $M_u$ and $V_u$ are equal to the maximum required flexural and shear strengths, respectively, along the member length, and $d$ is equal to the member depth in the direction of bending

    = 10 for members with rectangular compact composite cross sections and $(M_u/V_u)/d$ less than 0.5

    = 9 for members with round compact composite cross sections and $(M_u/V_u)/d$ less than 0.5

    = 1 for members having other than compact composite cross sections, for all values of $(M_u/V_u)/d$

Linear interpolation between these $K_c$ values shall be used for members with compact composite cross sections and with $(M_u/V_u)/d$ between 0.5 and 0.7.

**User Note:** For most members, $K_c$ will be equal to 1.0. Low shear span-to-depth ratios may occur in connection design (panel zones) or other special situations, for which higher values of $K_c$ (> 1.0) are more appropriate.

### 3. Composite Beams with Formed Steel Deck

The available shear strength of composite beams with formed steel deck with steel headed stud or steel channel anchors shall be determined based upon the properties of the steel section alone in accordance with Chapter G.

### 4. Composite Plate Shear Walls

The design in-plane shear strength, $\phi_v V_n$, and allowable shear strength, $V_n/\Omega_v$, of composite plate shear walls shall be determined as follows:

$$\phi_v = 0.90 \text{ (LRFD)} \qquad \Omega_v = 1.67 \text{ (ASD)}$$

The nominal shear strength, $V_n$, shall account for the contributions of the structural steel section and concrete infill as follows:

$$V_n = \frac{K_s + K_{sc}}{\sqrt{3K_s^2 + K_{sc}^2}}A_{sw}F_y$$ (I4-2)

where

$A_{sw}$ = area of steel plates in the direction of in-plane shear, in.$^2$ (mm$^2$)

$K_s$ = $G_sA_{sw}$ (I4-3)

$G_s$ = shear modulus of steel
    = 11,200 ksi (77 200 MPa)

$$K_{sc} = \frac{0.7(E_cA_c)(E_sA_{sw})}{4E_cA_{sw} + E_sA_c}$$ (I4-4)

---

## I5. COMBINED FLEXURE AND AXIAL FORCE

The interaction between flexure and axial forces in composite members shall account for stability as required by Chapter C. The available compressive strength and the available flexural strength shall be determined as defined in Sections I2 and I3, respectively. To account for the influence of length effects on the axial strength of the member, the nominal axial strength of the member shall be determined in accordance with Section I2.

(a) For encased composite members and for filled composite members with compact composite sections, the interaction between axial force and flexure shall be based on the interaction equations of Section H1.1 or one of the methods defined in Section I1.2.

(b) For filled composite members with noncompact composite or slender-element composite sections, the interaction between axial force and flexure shall be based either on the interaction equations of Section H1.1, the method defined in Section I1.2d, or Equations I5-1a and b.

    (1) When $\frac{P_r}{P_c} \geq c_p$

$$\frac{P_r}{P_c} + \frac{1-c_p}{c_m}\left(\frac{M_r}{M_c}\right) \leq 1.0$$ (I5-1a)

    (2) When $\frac{P_r}{P_c} < c_p$

$$\left(\frac{1-c_m}{c_p}\right)\left(\frac{P_r}{P_c}\right) + \frac{M_r}{M_c} \leq 1.0$$ (I5-1b)

where

**For design according to Section B3.1 (LRFD)**

$M_r$ = required flexural strength, determined in accordance with Section I1.5, using LRFD load combinations, kip-in. (N-mm)

$M_c$ = design flexural strength determined in accordance with Section I3, kip-in. (N-mm)
    = $\phi_b M_n$

$P_r$ = required axial strength, determined in accordance with Section I1.5 using LRFD load combinations, kips (N)

$P_c$ = design axial strength, determined in accordance with Section I2, kips (N)
    = $\phi_c P_n$

$\phi_c$ = resistance factor for compression
    = 0.75

$\phi_b$ = resistance factor for flexure
    = 0.90

---

**For design according to Section B3.2 (ASD)**

$M_r$ = required flexural strength, determined in accordance with Section I1.5, using ASD load combinations, kip-in. (N-mm)

$M_c$ = allowable flexural strength, determined in accordance with Section I3, kip-in. (N-mm)
    = $M_n/\Omega_b$

$P_r$ = required axial strength, determined in accordance with Section I1.5 using ASD load combinations, kips (N)

$P_c$ = allowable axial strength, determined in accordance with Section I2, kips (N)
    = $P_n/\Omega_c$

$\Omega_b$ = safety factor for flexure
    = 1.67

$\Omega_c$ = safety factor for compression
    = 2.00

$c_m$ and $c_p$ are determined from Table I5.1

$$c_sr = \frac{A_cF_y + A_{sr}F_{yr}}{A_cf_c'}$$ (I5-2)

(c) For composite plate shear walls, the interaction between axial force and flexure shall be based on the methods defined in Section I1.2.

## I6. LOAD TRANSFER

### 1. General Requirements

When external forces are applied to an axially loaded encased or filled composite member, the introduction of force to the member and the transfer of longitudinal shear within the member shall be assessed in accordance with the requirements for force allocation presented in this section.

The available strength of the applicable force transfer mechanisms as determined in accordance with Section I6.3 shall equal or exceed the required shear force to be transferred, $V_r'$, as determined in accordance with Section I6.2. Force transfer mechanisms shall be located within the load transfer region as determined in accordance with Section I6.4.

### 2. Force Allocation

Force allocation shall be determined based upon the distribution of external force in accordance with the following requirements.

**User Note:** Bearing strength provisions for externally applied forces are provided in Section J8. For filled composite members, the term $\sqrt{A_2/A_1}$ in Equation J8-2 may be taken equal to 2.0 due to confinement effects.

---

<!-- Table: I5.1 - Coefficients for Use with Equations I5-1a and I5-1b -->

<table>
  <thead>
    <tr>
      <th colspan="4" style="text-align: center;"><strong>TABLE I5.1</strong><br><strong>Coefficients <em>c<sub>p</sub></em> and <em>c<sub>m</sub></em> for Use with<br>Equations I5-1a and I5-1b</strong></th>
    </tr>
    <tr>
      <th rowspan="2"><strong>Filled Composite<br>Member Type</strong></th>
      <th rowspan="2" style="text-align: center;"><em>c<sub>p</sub></em></th>
      <th colspan="2" style="text-align: center;"><em>c<sub>m</sub></em></th>
    </tr>
    <tr>
      <th style="text-align: center;">when <em>c<sub>sr</sub></em> ≥ 0.5</th>
      <th style="text-align: center;">when <em>c<sub>sr</sub></em> < 0.5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Rectangular</td>
      <td style="text-align: center;">$c_p = \frac{0.17}{c_{sr}^{0.4}}$</td>
      <td style="text-align: center;">$c_m = \frac{1.06}{c_{sr}^{0.31}} \leq 1.0$</td>
      <td style="text-align: center;">$c_m = \frac{0.90}{c_{sr}^{0.36}} \leq 1.67$</td>
    </tr>
    <tr>
      <td>Round HSS</td>
      <td style="text-align: center;">$c_p = \frac{0.27}{c_{sr}^{0.4}}$</td>
      <td style="text-align: center;">$c_m = \frac{1.10}{c_{sr}^{0.08}} \leq 1.0$</td>
      <td style="text-align: center;">$c_m = \frac{0.95}{c_{sr}^{0.35}} \leq 1.67$</td>
    </tr>
  </tbody>
</table>

**Table summary**: Coefficients $c_p$ and $c_m$ for filled composite members (rectangular and round HSS) for use with interaction equations I5-1a and I5-1b, with different values depending on $c_{sr}$.

#### 2a. External Force Applied to Steel Section

When the entire external force is applied directly to the steel section, the force required to be transferred to the concrete, $V_r'$, shall be determined as

$$V_r' = P_r\left(1 - F_yA_s/P_{no}\right)$$ (I6-1)

where

$P_{no}$ = nominal axial compressive strength without consideration of length effects, determined by Equation I2-7 for encased composite members, and Equation I2-9a or Equation I2-9c, as applicable, for compact composite or noncompact composite filled composite members, kips (N)

$P_r$ = required external force applied to the composite member, kips (N)

**User Note:** Equation I6-1 does not apply to slender filled composite members for which the external force is applied directly to the concrete fill in accordance with Section I6.2b, or concurrently to the steel and concrete, in accordance with Section I6.2c.

#### 2b. External Force Applied to Concrete

When the entire external force is applied directly to the concrete encasement or concrete fill, the force required to be transferred to the steel, $V_r'$, shall be determined as follows:

(a) For encased or filled composite members that are compact composite or noncompact composite

$$V_r' = P_r\left(F_yA_s/P_{no}\right)$$ (I6-2a)

(b) For slender filled composite members

$$V_r' = P_r\left(F_nA_s/P_{no}\right)$$ (I6-2b)

where

$F_n$ = critical buckling stress for structural steel sections of filled composite members determined using Equation I2-10 or Equation I2-11, as applicable, ksi (MPa)

---

$P_{no}$ = nominal axial compressive strength without consideration of length effects, determined by Equation I2-7 for encased composite members, and Equation I2-9a, Equation I2-9c, or Equation I2-9e for filled composite members, kips (N)

#### 2c. External Force Applied Concurrently to Steel and Concrete

When the external force is applied concurrently to the steel section and concrete encasement or concrete fill, $V_r'$ shall be determined as the force required to establish equilibrium of the cross section.

**User Note:** The Commentary provides an acceptable method of determining the longitudinal shear force required for equilibrium of the cross section.

### 3. Force Transfer Mechanisms

The available strength of the force transfer mechanisms of direct bond interaction, shear connection, and direct bearing shall be determined in accordance with this section. Use of the force transfer mechanism providing the largest nominal strength is permitted. Force transfer mechanisms shall not be superimposed.

The force transfer mechanism of direct bond interaction shall not be used for encased composite members or for filled composite members where bond failure would result in uncontrolled slip.

#### 3a. Direct Bearing

Where force is transferred in an encased or filled composite member by direct bearing from internal bearing mechanisms, the available bearing strength of the concrete for the limit state of concrete crushing shall be determined as

$$R_n = 1.7f_c'A_1$$ (I6-3)

$$\phi_B = 0.65 \text{ (LRFD)} \qquad \Omega_B = 2.31 \text{ (ASD)}$$

where

$A_1$ = loaded area of concrete, in.$^2$ (mm$^2$)

**User Note:** An example of force transfer via an internal bearing mechanism is the use of internal steel plates within a filled composite member.

#### 3b. Shear Connection

Where force is transferred in an encased or filled composite member by shear connectors, the available shear strength of steel headed stud or steel channel anchors shall be determined as

$$R_v = \Sigma Q_{sv}$$ (I6-4)

where

$\Sigma Q_{sv}$ = sum of available shear strengths, $\phi_v Q_{nv}$ (LRFD) or $Q_{nv}/\Omega_v$ (ASD), as applicable, of steel headed stud or steel channel anchors, determined in accordance with Section I8.3a or Section I8.3d, respectively, placed within the load introduction length as defined in Section I6.4, kips (N)

---

#### 3c. Direct Bond Interaction

Where force is transferred in a filled composite member by direct bond interaction, the available bond strength between the steel and concrete shall be determined as follows:

$$R_b = \eta_b L_m F_m$$ (I6-5)

$$\phi_d = 0.50 \text{ (LRFD)} \qquad \Omega_d = 3.00 \text{ (ASD)}$$

where

$D$ = outside diameter of round HSS, in. (mm)

$F_m$ = nominal bond stress, ksi (MPa)
    = $12t/H^2 \leq 0.1$, ksi $(2\,100t/H^2 \leq 0.7$ MPa) for rectangular cross sections
    = $30t/D^2 \leq 0.2$, ksi $(5\,300t/D^2 \leq 1.4$ MPa) for round cross sections

$H$ = maximum transverse dimension of rectangular steel member, in. (mm)

$L_m$ = load introduction length, determined in accordance with Section I6.4, in. (mm)

$\eta_b$ = normalized bond strength, kips (N)

$p_b$ = perimeter of the steel-concrete bond interface within the composite cross section, in. (mm)

$t$ = design wall thickness of HSS member as defined in Section B4.2, in. (mm)

### 4. Detailing Requirements

#### 4a. Encased Composite Members

Force transfer mechanisms shall be distributed within the load introduction length, which shall not exceed a distance of two times the minimum transverse dimension of the encased composite member above and below the load transfer region. Anchors utilized to transfer shear shall be placed on at least two faces of the structural steel shape in a generally symmetric configuration about the steel shape axis.

Steel anchor spacing, both within and outside of the load introduction length, shall conform to Section I8.3e.

#### 4b. Filled Composite Members

Force transfer mechanisms shall be distributed within the load introduction length, which shall not exceed a distance of two times the minimum transverse dimension of a rectangular steel member or two times the diameter of a round steel member both above and below the load transfer region. For the specific case of load applied to the concrete of a filled composite member containing no internal longitudinal reinforcement, the load introduction length shall extend beyond the load transfer region in only the direction of the applied force. Steel anchor spacing within the load introduction length shall conform to Section I8.3e.

## I7. COMPOSITE DIAPHRAGMS AND COLLECTOR BEAMS

Composite slab diaphragms and collector beams shall be designed and detailed to transfer loads between the diaphragm, the diaphragm's boundary members and collector elements, and elements of the lateral force-resisting system.

**User Note:** Design guidelines for composite diaphragms and collector beams can be found in the Commentary.

---

## I8. STEEL ANCHORS

### 1. General

The diameter of a steel headed stud anchor, $d_{sa}$, shall be ¾ in. (19 mm) or less, except where anchors are utilized solely for shear transfer in solid slabs, in which case, ⅞-in.- (22-mm-) and 1-in.- (25-mm-) diameter anchors are permitted. Additionally, $d_{sa}$ shall not be greater than 2.5 times the thickness of the base metal to which it is welded, unless it is welded to a flange directly over a web.

Section I8.2 applies to a composite flexural member where steel anchors are embedded in a solid concrete slab or in a slab cast on a formed steel deck. Section I8.3 applies to all other cases.

### 2. Steel Anchors in Composite Beams

The length of steel headed stud anchors shall not be less than four stud diameters from the base of the steel headed stud anchor to the top of the stud head after installation.

#### 2a. Strength of Steel Headed Stud Anchors

The nominal shear strength of one steel headed stud anchor embedded in a solid concrete slab or in a composite slab with decking shall be determined as follows:

$$Q_n = 0.5A_{sa}\sqrt{f_c'E_c} \leq R_g R_p A_{sa}F_u$$ (I8-1)

where

$A_{sa}$ = cross-sectional area of steel headed stud anchor, in.$^2$ (mm$^2$)

$E_c$ = modulus of elasticity of concrete
    = $w_c^{1.5}\sqrt{f_c'}$, ksi $(0.043w_c^{1.5}\sqrt{f_c'}$, MPa)

$F_u$ = specified minimum tensile strength of a steel headed stud anchor, ksi (MPa)

$R_g$ = 1.0 for the following:
    - (a) One steel headed stud anchor welded in a steel deck rib with the deck oriented perpendicular to the steel shape
    - (b) Any number of steel headed stud anchors welded in a row directly to the steel shape
    - (c) Any number of steel headed stud anchors welded in a row through steel deck with the deck oriented parallel to the steel shape and the ratio of the average rib width to rib depth ≥ 1.5

    = 0.85 for the following:
    - (a) Two steel headed stud anchors welded in a steel deck rib with the deck oriented perpendicular to the steel shape
    - (b) One steel headed stud anchor welded through steel deck with the deck oriented parallel to the steel shape and the ratio of the average rib width to rib depth < 1.5

    = 0.7 for three or more steel headed stud anchors welded in a steel deck rib with the deck oriented perpendicular to the steel shape

$R_p$ = 0.75 for the following:
    - (a) Steel headed stud anchors welded directly to the steel shape

---

- (b) Steel headed stud anchors welded in a composite slab with the deck oriented perpendicular to the beam and $e_{mid-ht} \geq 2$ in. (50 mm)
- (c) Steel headed stud anchors welded through steel deck, or steel sheet used as girder filler material and embedded in a composite slab with the deck oriented parallel to the beam

    = 0.6 for steel headed stud anchors welded in a composite slab with deck oriented perpendicular to the beam and $e_{mid-ht} < 2$ in. (50 mm)

$e_{mid-ht}$ = distance from the edge of steel headed stud anchor shank to the steel deck web, measured at mid-height of the deck rib, and in the load bearing direction of the steel headed stud anchor (in other words, in the direction of maximum moment for a simply supported beam), in. (mm)

**User Note:** The table below presents values for $R_g$ and $R_p$ for several cases. Available strengths for steel headed stud anchors can be found in the AISC *Steel Construction Manual*.

<!-- Table: Condition values for Rg and Rp -->

| **Condition** | $R_g$ | $R_p$ |
|---------------|-------|-------|
| No decking | 1.0 | 0.75 |
| Decking oriented parallel to the steel shape<br>$\frac{w_r}{h_r} \geq 1.5$ | 1.0 | 0.75 |
| $\frac{w_r}{h_r} < 1.5$ | 0.85$^{[a]}$ | 0.75 |
| Decking oriented perpendicular to the steel shape<br>Number of steel headed stud anchors occupying the same decking rib:<br>1<br>2<br>3 or more | 1.0<br>0.85<br>0.7 | 0.6$^{[b]}$<br>0.6$^{[b]}$<br>0.6$^{[b]}$ |

$h_r$ = nominal rib height, in. (mm)

$w_r$ = average width of concrete rib or haunch (as defined in Section I3.2c), in. (mm)

$^{[a]}$For a single steel headed stud anchor

$^{[b]}$This value may be increased to 0.75 when $e_{mid-ht} \geq 2$ in. (50 mm).

**Table summary**: Values for reduction factors $R_g$ and $R_p$ for steel headed stud anchors based on deck orientation and configuration.

#### 2b. Strength of Steel Channel Anchors

The nominal shear strength of one hot-rolled channel anchor embedded in a solid concrete slab shall be determined as

$$Q_n = 0.3(t_f + 0.5t_w)l_a\sqrt{f_c'E_c}$$ (I8-2)

where

$l_a$ = length of channel anchor, in. (mm)

$t_f$ = thickness of channel anchor flange, in. (mm)

$t_w$ = thickness of channel anchor web, in. (mm)

The strength of the channel anchor shall be developed by welding the channel to the beam flange for a force equal to $Q_n$, considering eccentricity on the anchor.

---

#### 2c. Required Number of Steel Anchors

The number of anchors required between the section of maximum bending moment, positive or negative, and the adjacent section of zero moment shall be equal to the horizontal shear as determined in Sections I3.2d.1 and I3.2d.2 divided by the nominal shear strength of one steel anchor as determined from Section I8.2a or Section I8.2b. The number of steel anchors required between any concentrated load and the nearest point of zero moment shall be sufficient to develop the maximum moment required at the concentrated load point.

#### 2d. Detailing Requirements

Steel anchors in composite beams shall meet the following requirements:

(a) Steel anchors required on each side of the point of maximum bending moment, positive or negative, shall be distributed uniformly between that point and the adjacent points of zero moment, unless specified otherwise on the design documents and specifications issued for construction.

(b) Steel anchors shall have at least 1 in. (25 mm) of lateral concrete cover in the direction perpendicular to the shear force, except for anchors installed in the ribs of formed steel decks.

(c) The minimum distance from the center of a steel anchor to a free edge in the direction of the shear force shall be 8 in. (200 mm) if normal weight concrete is used and 10 in. (250 mm) if lightweight concrete is used. The provisions of ACI 318, Chapter 17, are permitted to be used in lieu of these values.

(d) Minimum center-to-center spacing of steel headed stud anchors shall be four diameters in any direction. For composite beams that do not contain infill located within formed steel deck oriented perpendicular to the beam span, an additional minimum spacing limit of six diameters along the longitudinal axis of the beam shall apply.

(e) The maximum center-to-center spacing of steel anchors shall not exceed eight times the total slab thickness or 36 in. (900 mm).

### 3. Steel Anchors in Composite Components

This section shall apply to the design of cast-in-place steel headed stud anchors and steel channel anchors in composite components.

The provisions of the applicable building code or ACI 318, Chapter 17, are permitted to be used in lieu of the provisions in this section.

**User Note:** The steel headed stud anchor strength provisions in this section are applicable to anchors located primarily in the load transfer (connection) region of composite columns and beam-columns, concrete-encased and filled composite beams, composite coupling beams, and composite walls, where the steel and concrete are working compositely within a member. They are not intended for hybrid construction where the steel and concrete are not working compositely, such as with embed plates.

---

Section I8.2 specifies the strength of steel anchors embedded in a solid concrete slab or in a concrete slab with formed steel deck in a composite beam.

Limit states for the steel shank of the anchor and for concrete breakout in shear are covered directly in this section. Additionally, the spacing and dimensional limitations provided in these provisions preclude the limit states of concrete pryout for anchors loaded in shear and concrete breakout for anchors loaded in tension as defined by ACI 318, Chapter 17.

For normal weight concrete: Steel headed stud anchors subjected to shear only shall not be less than four stud diameters in length from the base of the steel headed stud to the top of the stud head after installation. Steel headed stud anchors subjected to tension or interaction of shear and tension shall not be less than eight stud diameters in length from the base of the stud to the top of the stud head after installation.

For lightweight concrete: Steel headed stud anchors subjected to shear only shall not be less than seven stud diameters in length from the base of the steel headed stud to the top of the stud head after installation. Steel headed stud anchors subjected to tension shall not be less than ten stud diameters in length from the base of the stud to the top of the stud head after installation. The nominal strength of steel headed stud anchors subjected to interaction of shear and tension for lightweight concrete shall be determined as stipulated by the applicable building code or ACI 318, Chapter 17.

Steel headed stud anchors subjected to tension or interaction of shear and tension shall have a diameter of the head greater than or equal to 1.6 times the diameter of the shank.

**User Note:** The following table presents values of minimum steel headed stud anchor $h/d_{sa}$ ratios for each condition covered in this Specification.

<!-- Table: Loading Condition vs Concrete Type -->

| **Loading<br>Condition** | **Normal Weight<br>Concrete** | **Lightweight<br>Concrete** |
|--------------------------|-------------------------------|----------------------------|
| Shear | $h/d_{sa} \geq 5$ | $h/d_{sa} \geq 7$ |
| Tension | $h/d_{sa} \geq 8$ | $h/d_{sa} \geq 10$ |
| Shear and tension | $h/d_{sa} \geq 8$ | NA$^{[a]}$ |

$h/d_{sa}$ = ratio of steel headed stud anchor shank length to the top of the stud head-to-shank diameter

$^{[a]}$Refer to ACI 318, Chapter 17, for the calculation of interaction effects of anchors embedded in lightweight concrete.

**Table summary**: Minimum $h/d_{sa}$ ratios for steel headed stud anchors in normal weight and lightweight concrete under different loading conditions.

#### 3a. Shear Strength of Steel Headed Stud Anchors in Composite Components

Where concrete breakout strength in shear is not an applicable limit state, the design shear strength, $\phi_v Q_{nv}$, and allowable shear strength, $Q_{nv}/\Omega_v$, of one steel headed stud anchor shall be determined as

---

$$Q_{nv} = F_uA_{sa}$$ (I8-3)

$$\phi_v = 0.65 \text{ (LRFD)} \qquad \Omega_v = 2.31 \text{ (ASD)}$$

where

$A_{sa}$ = cross-sectional area of a steel headed stud anchor, in.$^2$ (mm$^2$)

$F_u$ = specified minimum tensile strength of a steel headed stud anchor, ksi (MPa)

$Q_{nv}$ = nominal shear strength of a steel headed stud anchor, kips (N)

Where concrete breakout strength in shear is an applicable limit state, the available shear strength of one steel headed stud anchor shall be determined by one of the following:

(a) Where anchor reinforcement is developed in accordance with ACI 318 on both sides of the concrete breakout surface for the steel headed stud anchor, the minimum of the steel nominal shear strength from Equation I8-3 and the nominal strength of the anchor reinforcement shall be used for the nominal shear strength, $Q_{nv}$, of the steel headed stud anchor.

(b) As stipulated by the applicable building code or ACI 318, Chapter 17.

**User Note:** If concrete breakout strength in shear is an applicable limit state (for example, where the breakout prism is not restrained by an adjacent steel plate, flange, or web), appropriate anchor reinforcement is required for the provisions of this section to be used. Alternatively, the provisions of the applicable building code or ACI 318, Chapter 17, may be used.

#### 3b. Tensile Strength of Steel Headed Stud Anchors in Composite Components

Where the distance from the center of an anchor to a free edge of concrete in the direction perpendicular to the height of the steel headed stud anchor is greater than or equal to 1.5 times the height of the steel headed stud anchor measured to the top of the stud head, and where the center-to-center spacing of steel headed stud anchors is greater than or equal to three times the height of the steel headed stud anchor measured to the top of the stud head, the available tensile strength of one steel headed stud anchor shall be determined as

$$Q_{nt} = F_uA_{sa}$$ (I8-4)

$$\phi_t = 0.75 \text{ (LRFD)} \qquad \Omega_t = 2.00 \text{ (ASD)}$$

where

$Q_{nt}$ = nominal tensile strength of steel headed stud anchor, kips (N)

Where the distance from the center of an anchor to a free edge of concrete in the direction perpendicular to the height of the steel headed stud anchor is less than 1.5 times the height of the steel headed stud anchor measured to the top of the stud head, or where the center-to-center spacing of steel headed stud anchors is less than three times the height of the steel headed stud anchor measured to the top of the stud head, the nominal tensile strength of one steel headed stud anchor shall be determined by one of the following:

---

(a) Where anchor reinforcement is developed in accordance with ACI 318 on both sides of the concrete breakout surface for the steel headed stud anchor, the minimum of the steel nominal tensile strength from Equation I8-4 and the nominal strength of the anchor reinforcement shall be used for the nominal tensile strength, $Q_{nt}$, of the steel headed stud anchor.

(b) As stipulated by the applicable building code or ACI 318, Chapter 17.

**User Note:** Supplemental confining reinforcement is recommended around the anchors for steel headed stud anchors subjected to tension or interaction of shear and tension to avoid edge effects or effects from closely spaced anchors. See the Commentary and ACI 318 for guidelines.

#### 3c. Strength of Steel Headed Stud Anchors for Interaction of Shear and Tension in Composite Components

Where concrete breakout strength in shear is not a governing limit state, and where the distance from the center of an anchor to a free edge of concrete in the direction perpendicular to the height of the steel headed stud anchor is greater than or equal to 1.5 times the height of the steel headed stud anchor measured to the top of the stud head, and where the center-to-center spacing of steel headed stud anchors is greater than or equal to three times the height of the steel headed stud anchor measured to the top of the stud head, the nominal strength for interaction of shear and tension of one steel headed stud anchor shall be determined as

$$\left(\frac{Q_{rt}}{Q_{ct}}\right)^{5/3} + \left(\frac{Q_{rv}}{Q_{cv}}\right)^{5/3} \leq 1.0$$ (I8-5)

where

$Q_{ct}$ = available tensile strength, determined in accordance with Section I8.3b, kips (N)

$Q_{cv}$ = available shear strength, determined in accordance with Section I8.3a, kips (N)

$Q_{rt}$ = required tensile strength, kips (N)

$Q_{rv}$ = required shear strength, kips (N)

Where concrete breakout strength in shear is a governing limit state, or where the distance from the center of an anchor to a free edge of concrete in the direction perpendicular to the height of the steel headed stud anchor is less than 1.5 times the height of the steel headed stud anchor measured to the top of the stud head, or where the center-to-center spacing of steel headed stud anchors is less than three times the height of the steel headed stud anchor measured to the top of the stud head, the nominal strength for interaction of shear and tension of one steel headed stud anchor shall be determined by one of the following:

(a) Where anchor reinforcement is developed in accordance with ACI 318 on both sides of the concrete breakout surface for the steel headed stud anchor, the minimum of the steel nominal shear strength from Equation I8-3 and the nominal

---

strength of the anchor reinforcement shall be used for the nominal shear strength, $Q_{nv}$, of the steel headed stud anchor, and the minimum of the steel nominal shear strength from Equation I8-4 and the nominal strength of the anchor reinforcement shall be used for the nominal tensile strength, $Q_{nt}$, of the steel headed stud anchor for use in Equation I8-5.

(b) As stipulated by the applicable building code or ACI 318, Chapter 17.

#### 3d. Shear Strength of Steel Channel Anchors in Composite Components

The available shear strength of steel channel anchors shall be based on the provisions of Section I8.2b with the following resistance factor and safety factor:

$$\phi_v = 0.75 \text{ (LRFD)} \qquad \Omega_v = 2.00 \text{ (ASD)}$$

#### 3e. Detailing Requirements in Composite Components

Steel anchors in composite components shall meet the following requirements:

(a) Minimum concrete cover to steel anchors shall be in accordance with ACI 318 provisions for concrete protection of headed shear stud reinforcement.

(b) Minimum center-to-center spacing of steel headed stud anchors shall be four diameters in any direction.

(c) The maximum center-to-center spacing of steel headed stud anchors shall not exceed 32 times the shank diameter.

(d) The maximum center-to-center spacing of steel channel anchors shall be 24 in. (600 mm).

**User Note:** Detailing requirements provided in this section are absolute limits. See Sections I8.3a, I8.3b, and I8.3c for additional limitations required to preclude edge and group effect considerations.

### 4. Performance-Based Alternative for the Design of Shear Connection

In lieu of shear connection prescribed by, and the corresponding strength determined in accordance with, Sections I8.1 and I8.2, it is permitted to use an alternate form of shear connection and determine its strength through testing, provided its performance requirements are established in accordance with Sections I8.4a through I8.4d and satisfy the approval requirements of the authority having jurisdiction. The geometric limitations of Sections I3.2c, I8.1, and I8.2 do not apply to the performance evaluated by Section I8.4.

#### 4a. Test Standard

Shear connection strength, slip capacity, and stiffness shall be established in accordance with AISI S923. An alternative test protocol may be used in the evaluation when approved by the authority having jurisdiction.

---

#### 4b. Nominal and Available Strength

When determining available strength of a flexural member, the nominal tested strength of shear connection, $Q_{nv}$, shall be taken as 0.85 times the mean tested strength determined in accordance with Section I8.4a. When required, the design shear strength, $\phi_v Q_{nv}$, and the allowable shear strength, $Q_{nv}/\Omega_v$, shall be determined in accordance with Section I8.3a. Alternatively, it is permitted to take $\phi_v$ as the mean tested strength provided that $\phi_v Q_{nv}$ or $Q_{nv}/\Omega_v$, as applicable, is determined on the basis of a reliability analysis.

**User Note:** An approach for establishing available strength using test data is provided in Chapter K of AISI *North American Specification for the Design of Cold-Formed Steel Structural Members*, with Supplement 2.

#### 4c. Shear Connection Slip Capacity

The nominal shear connection slip capacity shall be taken as the average shear connection slip corresponding to each specific tested shear connection configuration. Shear connection slip capacity shall be measured at no less than 5% of the postpeak strength.

#### 4d. Acceptance Criteria

The design using tested properties of the shear connection per Section I8.4a through Section I8.4c shall be limited to the geometric and material parameters tested. The nominal performance characteristics are permitted to be used in design provided either conditions (1), (2), and (3) are satisfied, or condition (4) is met.

(1) The maximum permitted coefficient of variation corresponding to each tested configuration of shear connection does not exceed 0.09 established over four replicate tests, or 0.13 established over nine replicate tests. It is permitted, for this purpose, to establish the number of tests using all tests of the same type of shear connection that exhibit the same failure mode.

(2) The nominal shear connection slip capacity is at least 0.25 in. (6 mm).

(3) The minimum shear elastic stiffness of the shear connection shall not be less than 2,000 kips/in. (350 N/mm).

(4) Shear connections corresponding to the values of coefficient of variation, shear connection slip capacity, and elastic stiffness, other than those stipulated in conditions (1), (2), and (3), shall be deemed acceptable, provided their effect is captured in the design. In lieu of using in an analysis the shear connection elastic stiffness determined per this section, it is permitted to establish the stiffness of a composite section, incorporating shear connection evaluated by this section, directly through testing in accordance with AISI S924. When stiffness of a composite section is established in accordance with AISI S924, it shall be a mean tested value established based on at least three tests.

---
