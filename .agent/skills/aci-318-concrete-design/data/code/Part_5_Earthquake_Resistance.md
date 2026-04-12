# Part 5 Earthquake Resistance

*ACI 318-25 Building Code for Structural Concrete*

**CODE Requirements**

---




<!-- From Page 303 -->


## CODE

**17.11.1.2** Horizontally installed steel base plates with shear lugs shall be a minimum 1 in. diameter hole along each of the long sides of the shear lug.

### 17.11.2 *Bearing strength in shear of attachments with shear lugs*, $V_{brg,sl}$

**17.11.2.1** Nominal bearing strength in shear of a shear lug, $V_{brg,sl}$, shall be calculated as:

$$V_{brg,sl} = 1.7f'_c A_{ef,sl} \psi_{brg,sl} \quad (17.11.2.1)$$

where $\psi_{brg,sl}$ is given in 17.11.2.2.

**17.11.2.1.1** The effective bearing area, $A_{ef,sl}$, shall be below the surface of the concrete, perpendicular to the direction of shear, and composed of areas according to (a) through (d):

(a) Bearing area of shear lugs located within $2t_{sl}$ of the bottom surface of the base plate if the top or bottom surface of the base plate is flush with the surface of the concrete

(b) Bearing area of shear lugs located within $2t_{sl}$ of the surface of the concrete if the base plate is above the surface of the concrete

(c) Bearing area of shear lugs located within $2t_{sl}$ of the interface with stiffeners

(d) Bearing area on the leading edge of stiffeners below the surface of the concrete

---


<!-- From Page 304 -->


## CODE

<!-- Diagram showing effective bearing areas for attachments with shear lugs -->

**Figure R17.11.2.1.1—Examples of effective bearing areas for attachments with shear lugs.**

The figure shows different configurations:

**(a) Shear lug without stiffeners:**
- Plan view: Shows a rectangular shear lug oriented perpendicular to the direction of shear load
- Elevation parallel to load: Shows the shear lug with height $t_{sl}$ below the surface
- Elevation perpendicular to load: Shows the effective bearing area $A_{ef,sl}$ with dimension $2t_{sl}$

**(b) Post-installed shear lug with stiffeners:**
- Plan view: Shows a cruciform-shaped shear lug with perpendicular stiffeners oriented in direction of shear load, surrounded by grout
- Elevation parallel to load: Shows stiffeners extending $\geq 0.5h_{ef}$ with dimension $t_{sl}$ and height $h_{ef}$
- Elevation perpendicular to load: Shows stiffener, grout, effective bearing area $A_{ef,sl}$ with dimensions $2t_{sl}$ on each side (total span $2t_{sl} + 2t_{sl}$)

Note: Anchors and inspection holes not shown.

---

### 17.11.2.2 *Bearing factor*, $\psi_{brg,sl}$

**17.11.2.2.1** Modification factor, $\psi_{brg,sl}$, for the effects of axial load, $P_u$, on bearing strength in shear, shall be determined by (a), (b), or (c):

(a) For applied axial tension:

$$\psi_{brg,sl} = 1 + \frac{P_u}{nN_{ua}} \leq 1.0 \quad (17.11.2.2.1a)$$

where $P_u$ is negative for tension and $n$ is the number of anchors in tension.

(b) For no applied axial load:

$$\psi_{brg,sl} = 1 \quad (17.11.2.2.1b)$$

(c) For applied axial compression:

$$\psi_{brg,sl} = 1 + 4\frac{P_u}{A_{brg}f'_c} \leq 2.0 \quad (17.11.2.2.1c)$$

where $P_u$ is positive for compression.

---


<!-- From Page 305 -->


## CODE

**17.11.2.3** If used, the footprint of shear lug stiffeners in the direction of the shear load shall be limited to the dimension of the projected area of the shear lug determined from 17.2.2 using Eq. (17.2.2.1a), where $l_e$ is either half the height of the stiffener or half the embedment depth of the shear lug, whichever is less.

**17.11.2.4** For attachments with multiple shear lugs loaded in the same direction, if the clear distance between any two shear lugs parallel to the direction of load is less than three times the bearing depth of each individual lug, the bearing depth of each individual lug shall be determined from Eq. (17.2.2.1a), with $l_e$ equal to the distance from the edge of the shear lug to the face of the adjacent shear lug.

### 17.11.3 *Concrete breakout strength of shear lug*, $V_{cb,sl}$

**17.11.3.1** The nominal concrete breakout strength of an individual shear lug, $V_{cb,sl}$, or a group of shear lugs loaded in the same direction shall be calculated as:

$$V_{cb,sl} = \frac{A_{Vco,sl}}{A_{Vco}} \psi_{ec,V} \psi_{ed,V} \psi_{c,V} \psi_{h,V} V_{b,sl} \quad (17.11.3.1)$$

where $V_{b,sl}$ is given in 17.11.3.2.

---


<!-- From Page 306 -->


## CODE

**17.11.2.3** If used, the footprint of shear lug stiffeners in the direction of the shear load shall be limited to four times the projected area of the failure surface of the side of the concrete member where $l_e$ is either half the height of the stiffener or half the embedment depth of the shear lug, whichever is less.

**17.11.2.4** For attachments with multiple shear lugs loaded in the same direction, if the clear distance between any two shear lugs parallel to the direction of load is less than three times the bearing depth of each individual lug, the clear distance shall be added to the bearing depth to satisfy the limit for the two shear plane segments and to additionto verify there is no failure surface of the concrete member where $l_e$ is equal to the distance from the edge of the shear lug to the face of the adjacent shear lug.

### 17.11.3 *Concrete breakout strength of shear lug*, $V_{cb,sl}$

**R17.11.3.1** Concrete breakout strength of shear lug, $V_{cb,sl}$, shall be determined in accordance with 17.5.2, with a modification from 17.7.2 using Eq. (17.2.2.1a), where $l_e$ is either half the height of the stiffener or half the embedment depth of the shear lug, whichever is less, and $h_{ef}$ is the height from 17.7.2 using h_{ef} = embedment depth of shear lug + base plate thickness.

**R17.11.3.2** Concrete breakout strength, $V_b$, used in R17.11.3.1, The modification of the shear lug breakout area as a function of the projected diameter area of a shear plane is:

---


<!-- From Page 307 -->


## CODE

**17.11.3.1.1** $A_{Vc}$ is the projected concrete failure area on the side face of the concrete that is approximated as the rectangular shape resulting from projecting horizontally $1.5c_{a1}$ from the edge of the shear lug and projecting vertically $1.5c_{a1}$ from the edge of the effective depth of the shear lug, $h_{ef,sl}$. The effective area of the shear lug, $A_{ef,sl}$, shall not be included. The effective embedment depth of the shear lug, $h_{ef}$, shall be taken as the distance from the concrete surface to the bottom of the effective bearing area, $A_{ef,sl}$.

**17.11.3.2** Nominal concrete breakout strength of a shear lug for shear parallel to the edge shall be permitted to be determined in accordance with 17.7.2.1(c) using Eq. (17.7.2.1(a)) with $c_{a1}$ taken as the distance from the edge to the centroid of the shear lug and with $\psi_{ec,V}$ taken as 1.0.

**17.11.3.3** For shear lugs located at a corner, the limiting concrete breakout strength shall be determined for each edge, and the minimum value shall be used.

**17.11.3.4** For cases with multiple shear lugs, the concrete breakout strength shall be determined for each potential breakout surface.


<!-- From Page 308 -->


## CODE

**18.1—Scope**

Structures and structural systems assigned to Seismic Design Category (SDC) B and C, Chapter 18 applies to structures with vertical elements of the seismic-force-resisting system designated as part of the seismic-force-resisting systems, and to both structural systems designated as part of the seismic-force-resisting system and structural systems not designated as part of the seismic-force-resisting system.

Chapter 18 contains provisions considered to be the minimum requirements for a satisfactory or person designed concrete structural systems, members, and connections with adequate load combination effects against permanent lateral deformation or strength. The integrity of the structure is the structural range of response should be maintained because lateral displacements will exceed elastic limits. An appropriate design method based on a balanced earthquake, such as ASCE/SEI 7 or NSF 100-1997, and the NEHRP (FEMA P-750) provisions are considered for, but not required by this code for SDC E and F may require an earthquake intensity (FEMA P-750, Moura, et al. 1981; Clough 1966; Paulay and Selzin 1974).

Structures designed in accordance with the cast-in-place concrete provisions for detailed in SDC B or C, C, or described in design-level ground motions, with decreased response and increased shear development but without and partial collapse. Design with procedures described in accordance with Chapter 18 are intended to constrain earthquake connections, except 18.3, 18.6.2.1, and 18.12.2 by use of system proportioning, detailing of connections, and mechanisms. The combination of reduced stiffness and increased energy dissipation tends to reduce the response to earthquakes from the elastic response of the system. The forces that are appropriately proportioned by elastic design are less lightly damped (Gulkan and Sozen 1974). Thus, the use of design forces representing earthquake effects such as those given in ASCE/SEI 7 or NSF 100-1997 assume that the structural system retains a substantial portion of its strength into the inelastic range under displacement reversals.

Emphasis has been placed on earthquake requirements to type of structural framing particularly for tall buildings. For earthquakes, categories are adopted directly from ASCE/SEI 7 and are cited using ASCE/SEI 7 reference tables. Various seismic framing systems include bearing wall systems, building frame systems and high seismic risk designations were used to determine detailing requirements. For a qualitative comparison of SDC see Table R2.2. The assignment of a structure to a SDC is regulated by the general building code (refer to 3.4.6 (1)).


<!-- From Page 309 -->


## CODE

[Mostly blank - part of chapter transition]


<!-- From Page 310 -->


## CODE

[Mostly blank - chapter header page]


<!-- From Page 311 -->


## CODE

**18.2.1** *Structural systems*

**18.2.1.1** All structures shall be assigned to a SDC in accordance with 4.4.6.1.

**18.2.1.2** All members shall satisfy Chapters 1 to 17 and 19 to 26. Structures assigned to SDC B, C, D, E, or F also shall satisfy 18.2.1.3 through 18.2.1.7, as applicable. Where Chapter 18 conflicts with other chapters of this Code, Chapter 18 shall govern.

**18.2.1.3** Structures assigned to SDC B shall satisfy 18.2.2.

**18.2.1.4** Structures assigned to SDC C shall satisfy 18.2.2, 18.2.3, 18.12.1.2, and 18.13.

**18.2.1.5** Structures assigned to SDC D, E, or F shall satisfy 18.2.2 through 18.2.8, 18.12 through 18.14, and 23.11.

**18.2.1.6** Structural systems designated as part of the seismic-force-resisting system shall be restricted to those designated by the general building code, or determined by other authority having jurisdiction in areas without a legally adopted building code. Except for SDC A, for which Chapter 18 does not apply, (a) through (h) shall be satisfied for each structural system designated as part of the seismic-force-resisting system, in addition to 18.2.1.3 through 18.2.1.5:

(a) Ordinary moment frames shall satisfy 18.3
(b) Ordinary reinforced concrete structural walls need not satisfy any detailing provisions in Chapter 18, unless required by 18.2.1.3 or 18.2.1.4
(c) Intermediate moment frames shall satisfy 18.4
(d) Intermediate precast walls shall satisfy 18.5
(e) Special moment frames shall satisfy 18.2.3 through 18.2.8 and 18.6 through 18.8
(f) Special moment frames constructed using precast concrete shall satisfy 18.2.3 through 18.2.8 and 18.9
(g) Special structural walls shall satisfy 18.2.3 through 18.2.8 and 18.10
(h) Special structural walls constructed using precast concrete shall satisfy 18.2.3 through 18.2.8 and 18.11

**18.2.1.7** A reinforced concrete structural system not satisfying this chapter shall be permitted if it is demonstrated by experimental evidence and analysis that the proposed system will have strength and toughness equal to or exceeding those provided by a comparable reinforced concrete structure satisfying this chapter.

**18.2.2** *Analysis and proportioning of structural members*


<!-- From Page 312 -->


## CODE

**18.2.2.1** The interaction of all structural and nonstructural members that affect the linear and nonlinear response of the structure to earthquake motions shall be considered in the analysis.

**18.2.2.2** Rigid members assumed not to be a part of the seismic-force-resisting system shall be permitted provided their effect on the response of the system is considered in the structural design. Consequences of failure of structural and nonstructural members that are not a part of the seismic-force-resisting system shall be considered.

**18.2.2.3** Structural members extending below the base of structure that are required to transmit forces resulting from earthquake effects to the foundation shall comply with the requirements of Chapter 18 that are consistent with the seismic-force-resisting system above the base of structure.


<!-- From Page 313 -->


## CODE

**18.2.3** *Anchoring to concrete*

**18.2.3.1** Anchors resisting earthquake-induced forces in structures assigned to SDC C, D, E, or F shall satisfy Chapter 17.

**18.2.4** *Strength reduction factors*

**18.2.4.1** Strength reduction factors shall be in accordance with Chapter 21.

**18.2.5** *Concrete in special moment frames and special structural walls*

**18.2.5.1** Specified compressive strength of concrete, $f'_c$, shall be at least 3000 psi.

**18.2.5.2** Specified compressive strength of concrete, $f'_c$, in lightweight concrete shall be 5000 psi or less, unless experimental evidence is provided to show that structural members made with higher strength lightweight concrete will have strength and toughness equal to or exceeding those made with normalweight concrete of the same strength.

**18.2.6** *Reinforcement in special moment frames and special structural walls*

**18.2.6.1** Reinforcement in special moment frames and special structural walls shall be in accordance with 20.2.1.1 and the special seismic systems requirements of 20.2.


<!-- From Page 314 -->


## CODE

[Continuing from previous page]

**18.2.7** *Mechanical splices in special moment frames and special structural walls*

**18.2.7.1** Mechanical splices shall conform to 25.5.7 and the requirements of this section.


<!-- From Page 315 -->


## CODE

(d) Class 3 mechanical splices in special structural walls shall be permitted at any location. Class 2 mechanical splices in the boundary elements of special structural walls shall be located within coupling beams, and within a distance equal to twice the member depth from critical sections where yielding of the reinforcement is likely to occur, such as at connections to the diaphragms/beyond the base and range of behavior.

**18.2.8** *Welded splices in special moment frames and special structural walls*

**18.2.8.1** Welded splices are not permitted in special moment frames or in special structural walls including coupling beams.

**18.2.8.2** Welding of stirrups, ties, inserts, or other similar elements to longitudinal reinforcement required by design shall not be permitted.

**18.3—Ordinary moment frames**


<!-- From Page 316 -->


## CODE

**18.3.1** *Scope*

**18.3.1.1** This section shall apply to ordinary moment frames forming part of the seismic-force-resisting system.

**18.3.2** Beams shall have at least two continuous bars at both top and bottom faces. Continuous bottom bars shall have area not less than one-fourth the maximum area of bottom bars along the span. These bars shall be developed in tension in accordance with 25.4 by substituting a bar stress of $1.25f_y$ for $f_y$ at the face of support.

**18.3.3** Columns having unsupported length $\ell_u \leq 5c_1$ shall have $\phi V_c$ at least the lesser of (a) and (b):

(a) The shear associated with development of nominal moment strengths of the column at each restrained end of the unsupported length due to reverse curvature bending. Column flexural strength shall be calculated for the factored axial force, consistent with the direction of the lateral forces considered, resulting in the highest flexural strength.

(b) The maximum shear obtained from design load combinations that include $E$, with $\Omega_o E$ substituted for $E$.

**18.3.4** Beam-column joints shall satisfy Chapter 15 with joint shear $V_u$ calculated on a plane at mid-height of the joint using tensile and compressive beam forces and column shear consistent with beam nominal moment strengths $M_n$.

**18.4—Intermediate moment frames**

**18.4.1** *Scope*

**18.4.1.1** This section shall apply to intermediate moment frames including two-way slabs without beams forming part of the seismic-force-resisting system.

**18.4.2** *Beams*


<!-- From Page 317 -->


## CODE

[Mostly blank - continuing from previous page]


<!-- From Page 318 -->


## CODE

[Blank - end of page 318]


<!-- From Page 319 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 319

### CODE

**18.4.2.2** The positive moment strength at the face of the joint shall be at least one-third the negative moment strength provided at that face of the joint. Neither the negative nor the positive moment strength at any section along the length of the beam shall be less than one-fifth the maximum moment strength provided at the face of either joint.

**18.4.2.3** $\phi V_n$ shall be at least the lesser of (a) and (b):

(a) The sum of the shear associated with development of nominal moment strengths of the beam at each restrained end of the clear span due to reverse curvature bending and the shear calculated for factored gravity and vertical earthquake loads

(b) The maximum shear obtained from design load combinations that include $E$, with $E$ taken as twice that prescribed by the general building code

**18.4.2.4** At both ends of the beam, hoops or closed stirrups in accordance with 18.6.4.3 shall be provided over a length of at least twice the beam depth measured from the face of the supporting member toward midspan. The first hoop or closed stirrup shall be located not more than 2 in. from the face of the supporting member. Spacing of hoops or closed stirrups shall not exceed the smallest of (a) through (d):

(a) $d/4$

(b) Eight times the diameter of the smallest longitudinal bar enclosed

(c) 24 times the diameter of the transverse reinforcing bar

(d) 12 in.

**18.4.2.5** Transverse reinforcement spacing shall not exceed $d/2$ throughout the length of the beam.

**18.4.2.6** In beams having factored axial compressive force exceeding $A_g f'_c/10$, transverse reinforcement required by 18.4.2.5 shall conform to 25.7.2.2 and either 25.7.2.3 or 25.7.2.4.

**18.4.3** *Columns*

### COMMENTARY

**R18.4.3** *Columns*

According to 18.4.3.1(a), the factored shear force is determined from a free-body diagram obtained by cutting through the column ends, with end moments assumed equal to the nominal moment strengths acting in reverse curvature bending, both clockwise and counterclockwise. Figure R18.4.2 demonstrates only one of the two options that are to be considered for every column. The factored axial force $P_u$ should be chosen to develop the largest moment strength of the column within the range of design axial forces. Provision 18.4.3.1(b) for columns is similar to 18.4.2.3(b) for beams except it bases $V_u$ on load combinations including the earthquake effect $E$, with $E$ increased by the overstrength factor $\Omega_o$ rather than the factor 2.0. In ASCE/SEI 7, $\Omega_o$ = 3.0 for intermediate moment frames. The higher factor for columns relative to beams is because of greater concerns about shear failures in columns.

---

*Fig. R18.4.2—Design shears for intermediate moment frames.*

[THIS IS FIGURE: Diagram showing design shears for intermediate moment frames, including column-beam connection details, load distributions, and shear force calculations. The figure shows:
- Top view of column-beam joint with dimensions $\ell_u$ and $\ell_n$
- Distributed load $w_u = (1.2 + 0.2S_{DS})D + 1.0L + 0.2S$
- Beam shear diagram with moments $M_{nl}$ and $M_{nr}$
- Column shear diagram with forces $P_u$ and moments $M_{nt}$ and $M_{nb}$]


<!-- From Page 320 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 320

### CODE

**18.4.3.1** $\phi V_n$ shall be at least the lesser of (a) and (b):

(a) The shear associated with development of nominal moment strengths of the column at each restrained end of the unsupported length due to reverse curvature bending. Column flexural strength shall be calculated for the factored axial force, consistent with the direction of the lateral forces considered, resulting in the highest flexural strength

(b) The maximum shear obtained from factored load combinations that include $E$, with $\Omega_o E$ substituted for $E$

**18.4.3.2** Columns shall be spirally reinforced in accordance with Chapter 10 or shall be in accordance with 18.4.3.3 through 18.4.3.5. Provision 18.4.3.6 shall apply to all columns supporting discontinuous stiff members.

**18.4.3.3** At both ends of the column, hoops shall be provided at spacings, over a length $\ell_o$ measured from the joint face. Spacing $s_o$ shall not exceed the least of (a) through (c):

(a) For Grade 60, the smaller of $8d_b$ of the smallest longitudinal bar enclosed and 8 in.

(b) For Grade 80, the smaller of $6d_b$ of the smallest longitudinal bar enclosed and 6 in.

(c) One-half of the smallest cross-sectional dimension of the column

Length $\ell_o$ shall not be less than the longest of (d), (e), and (f):

(d) One-sixth of the clear span of the column

(e) Maximum cross-sectional dimension of the column

(f) 18 in.

**18.4.3.4** The first hoop shall be located not more than $s_o/2$ from the joint face.

**18.4.3.5** Outside of length $\ell_o$, spacing of transverse reinforcement shall be in accordance with 10.7.6.5.2.

**18.4.3.6** Columns supporting reactions from discontinuous stiff members, such as walls, shall be provided with transverse reinforcement at the spacing $s_o$ in accordance with 18.4.3.3 over the full height beneath the level at which the discontinuity occurs if the portion of factored axial compressive force in these members related to earthquake effects exceeds $A_g f'_c/10$. If design forces have been magnified to

### COMMENTARY

Transverse reinforcement at the ends of columns is required to be spirals or hoops. The amount of transverse reinforcement at the ends must satisfy both 18.4.3.1 and 18.4.3.2. Note that hoops require seismic hooks at both ends. The maximum spacing allowed for hoops is intended to inhibit or delay buckling of longitudinal reinforcement.

Discontinuous structural walls and other stiff members can impose large axial forces on supporting columns during earthquakes. The required transverse reinforcement in 18.4.3.6 is to improve column toughness under anticipated demands. The factored axial compressive force related to earthquake effect should include the factor $\Omega_o$ if required by the general building code.


<!-- From Page 321 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 321

### CODE

account for the overstrength of the vertical elements of the seismic-force-resisting system, the limit of $A_g f'_c/10$ shall be increased to $A_g f'_c/4$. Transverse reinforcement shall extend above and below the column in accordance with 18.7.5.6(b).

**18.4.4** *Joints*

**18.4.4.1** Beam-column joints shall satisfy the detailing requirements of 15.7.1.2, 15.7.1.3, and 18.4.4.2 through 18.4.4.5.

**18.4.4.2** If a beam framing into the joint and generating joint shear has depth exceeding twice the column depth, analysis and design of the joint shall be based on the strut-and-tie method in accordance with Chapter 23 and (a) and (b) shall be satisfied:

(a) Design joint shear strength determined in accordance with Chapter 23 shall not exceed $\phi V_n$ calculated in accordance with 13.5.

(b) Detailing requirements of 18.4.4.3 through 18.4.4.5 shall be satisfied.

**18.4.4.3** Longitudinal reinforcement terminated in a joint shall extend to the far face of the joint core and shall be developed in tension in accordance with 18.8.5.

**18.4.4.4** Spacing of joint transverse reinforcement $s$ shall not exceed the lesser of 18.4.4.3(a) through (c) within the height of the deepest beam framing into the joint.

**18.4.4.5** Where the top beam longitudinal reinforcement consists of headed deformed bars that terminate in the joint, the column shall extend above the top of the joint a distance at least the depth $h$ of the joint. Alternatively, the beam reinforcement shall be enclosed by additional vertical joint reinforcement providing equivalent confinement to the top face of the joint.

**18.4.4.6** Slab-column joints shall satisfy transverse reinforcement requirements of 15.7.2. Where slab-column joint transverse reinforcement is required, at least one layer of joint transverse reinforcement shall be placed between the top and bottom slab reinforcement.

**18.4.4.7** *Shear strength requirements for beam-column joints*

**18.4.4.7.1** Design shear strength of cast-in-place beam-column joints shall satisfy:

$$\phi V_n \geq V_u$$

### COMMENTARY

**R18.4.4** *Joints*

**R18.4.4.2** For joints in which the beam depth is significantly greater than the column depth, a diagonal strut between the joint corners may not be effective. Therefore, the Code requires that joints in which the beam depth exceeds twice the column depth be designed using the strut-and-tie method of Chapter 23.

**R18.4.4.3** Refer to R18.8.2.2.

**R18.4.4.4** The maximum spacing of transverse reinforcement within a joint is consistent with the spacing limits for reinforcement in columns of intermediate moment frames.

**R18.4.4.5** Refer to R25.4.4.6.

**R18.4.4.7** *Shear strength requirements for beam-column joints*


<!-- From Page 322 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 322

### CODE

**18.4.4.7.2** $V_u$ of the joint shall be determined in accordance with 18.3.4.

**18.4.4.7.3** $\phi$ shall be in accordance with 21.2.1 for shear.

**18.4.4.7.4** $V_n$ of the joint shall be in accordance with 18.8.4.3.

**18.4.5** *Two-way slabs without beams*

**18.4.5.1** Factored slab moment at the support including earthquake effects, $E$, shall be calculated for load combinations given in Eq. (5.3.1e) and (5.3.1g). Reinforcement to resist $M_{sc}$ shall be placed within the column strip defined in 8.4.1.5.

### COMMENTARY

**R18.4.4.7.2** Factored joint shear force is determined assuming that beams framing into the joint develop end moments equal to their nominal moment strengths. Consequently, joint shear force generated by the flexural reinforcement is calculated for a stress of $f_y$ in the reinforcement. This is consistent with 18.4.2 and 18.4.3 for determination of minimum design shear strength in beams and columns of intermediate moment frames.

**R18.4.5** *Two-way slabs without beams*

Section 18.4.5 applies to two-way slabs without beams, such as flat plates.

Using load combinations of Eq. (5.3.1e) and (5.3.1g) may result in moments requiring top and bottom reinforcement at the supports.

The moment $M_{sc}$ refers, for a given design load combination with $E$ acting in one horizontal direction, to that portion of the factored slab moment that is balanced by the supporting members at a joint. It is not necessarily equal to the total design moment at the support for a load combination including earthquake effect. In accordance with 8.4.2.2.3, only a fraction of the moment $M_{sc}$ is assigned to the slab effective width. For edge and corner connections, flexural reinforcement perpendicular to the edge is not considered fully effective unless it is placed within the effective slab width (ACI PRC-352.1; Pan and Moehle 1989). Refer to Fig. R18.4.5.1.

Application of the provisions of 18.4.5 is illustrated in Fig. R18.4.5.2 and R18.4.5.3.

**R18.4.5.1**


<!-- From Page 323 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 323

### CODE

**18.4.5.2** Reinforcement placed within the effective width given in 8.4.2.2.3 shall be designed to resist $\gamma_f M_{sc}$. Effective slab width for exterior and corner connections shall not extend beyond the column face a distance greater than $c_1$ measured perpendicular to the slab span.

### COMMENTARY

[THIS IS FIGURE: Two diagrams showing effective width for reinforcement placement in edge and corner connections:

(a) Edge connection - Shows a slab plan view with column, indicating effective width, dimensions $c_1$, $c_2$, and angles of ≤45° with measurements of $1.5h \leq c_1$

(b) Corner connection - Similar diagram showing corner column configuration with same dimensional notations

Both diagrams include yield lines and direction of moment indicators]

*Fig. R18.4.5.1—Effective width for reinforcement placement in edge and corner connections.*

**R18.4.5.2**


<!-- From Page 324 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 324

### CODE

**18.4.5.3** At least one-half of the reinforcement in the column strip at the support shall be placed within the effective slab width given in 8.4.2.2.3.

**18.4.5.4** At least one-fourth of the top reinforcement at the support in the column strip shall be continuous throughout the span.

**18.4.5.5** Continuous bottom reinforcement in the column strip shall be at least one-third of the top reinforcement at the support in the column strip.

**18.4.5.6** At least one-half of all bottom middle strip reinforcement and all bottom column strip reinforcement at midspan shall be continuous and shall develop $f_y$ at the face of columns, capitals, brackets, or walls.

### COMMENTARY

[THIS IS FIGURE: Diagram showing location of reinforcement in slabs with annotations indicating column strip dimensions ($c_{2a}$, $c_{2a} + 3h$) and notes about reinforcement placement for resisting $M_{sc}$ and $\gamma_f M_{sc}$]

*Fig. R18.4.5.2—Location of reinforcement in slabs.*

**R18.4.5.3**

[THIS IS FIGURE: Two diagrams showing arrangement of reinforcement in slabs:
1. Column strip - showing top and bottom reinforcement with notes about development requirements (18.4.5.6 and 18.4.5.7)
2. Middle strip - showing reinforcement layout with note about continuous bottom reinforcement (18.4.5.6)]

*Fig. R18.4.5.3—Arrangement of reinforcement in slabs.*


<!-- From Page 325 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 325

### CODE

**18.4.5.7** At discontinuous edges of the slab, all top and bottom reinforcement at the support shall be developed at the face of columns, capitals, brackets, or walls.

**18.4.5.8** For two-way slabs without beams, defined as those having beams with $\alpha_f$ in all directions less than 2, loads without moment transfer shall not exceed 0.4$\phi V_c$ for nonprestressed slab-column connections in accordance with 22.6.4.2, 22.6.5.3, or 22.6.6.2. For each direction meeting the requirements of 8.6.2.1, where $\alpha_f$ shall be calculated in accordance with 22.6.2.2, this requirement need not be followed. For designs assigned to SDC D, E, or F, wall piers shall be designed in accordance with 18.10.8 or 18.14.

**18.5—Intermediate precast structural walls**

**18.5.1** Scope

**18.5.1.1** This section shall apply to intermediate precast structural walls, or portions of walls, having force-resisting elements.

**18.5.2** *General*

**18.5.2.1** In connections between wall panels, or between wall panels and the foundation, yielding shall be restricted to steel elements or reinforcement. Mechanical splices used in accordance with 18.2.7.1 shall not be placed at potential hinge locations.

**18.5.2.2** For elements of the connection that are not factored to yield, forces calculated in Eq. (5.3.1e) shall be based on 1.5 times the nominal strength of the yielding element, but need not exceed the strength required from applying factored load combinations that include $E_m$.

**18.5.2.3** In structures assigned to SDC D, E, or F, wall piers shall be designed in accordance with 18.10.8 or 18.14.

**18.6—Beams of special moment frames**

**18.6.1** Scope

### COMMENTARY

**R18.4.5.8** The requirements apply to two-way slabs that are not defined as part of a special moment frame. Nonprestressed slab-column connections in laboratory tests often exhibited reduced strength and lateral stiffness degradation at drift levels less than those required by ASCE/SEI 7 (Pan and Moehle 2006; Kang and Wallace 2006). A limit of 0.4$\phi V_c$ is given for designs assigned to SDC B and C. For higher seismic design categories, a designer can determine that lateral seismic forces in a slab direction are resisted by elements that meet the requirements of 8.6.2.1, in which direction meeting the requirements of 8.6.2.1. Post-tensioned slab-column connections with $V_u$ exceeding 0.4$\phi V_c$ without beams that meet the requirements be designed as nonprestressed slab-column connections in accordance with 18.4.5. Slab-column connections also must be able to carry gravity loads from combinations including earthquake effect.

**R18.5—Intermediate precast structural walls**

**R18.5.1** Scope

Code provisions for the design and detailing of precast wall panels and the foundation are required to resist forces induced by earthquake motions and to provide for yielding that has ductility of connections.

**R18.6—Beams of special moment frames**

**R18.6.1** Scope

**R18.5.2.2** Connection design forces need not exceed the maximum forces that the structural system can deliver to the connection.


<!-- From Page 326 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 326

### CODE

**18.6.1.1** This section shall apply to beams of special moment frames that form part of the seismic-force-resisting system and are proportioned primarily to resist flexure and shear.

**18.6.1.2** Beams of special moment frames shall frame into columns of special moment frames satisfying 18.7.

**18.6.2** *Dimensional limits*

### COMMENTARY

This section applies to beams of special moment frames resisting lateral loads induced by earthquake motions. In previous Codes, any frame member subjected to a factored axial compressive force exceeding $(A_g f'_c/10)$ under any load combination was to be proportioned and detailed as described in 18.7. In the 2014 Code, all requirements for beams are contained in 18.6 regardless of the magnitude of axial compressive force.

The Code is written with the assumption that special moment frames comprise horizontal beams and vertical columns interconnected by beam-column joints. It is acceptable for beams and columns to be inclined provided the resulting system behaves as a frame—that is, lateral resistance is provided primarily by moment transfer between beams and columns rather than by strut or brace action. In special moment frames, it is acceptable to design beams to resist combined moment and axial force as occurs in beams that act both as moment frame members and as chords or collectors of a diaphragm. It is acceptable for beams of special moment frames to cantilever beyond columns, but such cantilevers are not part of the special moment frame that forms part of the seismic-force-resisting system. It is acceptable for beams of a special moment frame to connect into a wall boundary if the boundary is reinforced as a special moment frame column in accordance with 18.7. A concrete braced frame, in which lateral resistance is provided primarily by axial forces in beams and columns, is not a recognized seismic-force-resisting system.

**R18.6.2** *Dimensional limits*

Experimental evidence (Hirosawa 1977) indicates that, under reversals of displacement into the nonlinear range, behavior of continuous members having length-to-depth ratios of less than 4 is significantly different from the behavior of relatively slender members. Design rules derived from experience with relatively slender members do not apply directly to members with length-to-depth ratios less than 4, especially with respect to shear strength.

Geometric constraints indicated in 18.6.2.1(b) and (c) were derived from practice and research (ACI PRC-352) on reinforced concrete frames resisting earthquake-induced forces. The limits in 18.6.2.1(c) define the maximum beam width that can effectively transfer forces into the beam-column joint. An example of maximum effective beam width is shown in Fig. R18.6.2.


<!-- From Page 327 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 327

### CODE

**18.6.2.1** Beams shall satisfy (a) through (c):

(a) Clear span $\ell_n$ shall be at least $4d$

(b) Width $b_w$ shall be at least the larger of $0.3h$ and 10 in.

(c) Projection of the beam width beyond the width of the supporting column on each side shall not exceed the smaller of $c_2$ and $0.75c_1$.

### COMMENTARY

[THIS IS FIGURE: Two diagrams showing beam-column connection details:
1. Plan view showing direction of analysis with transverse reinforcement through column to confine beam longitudinal reinforcement, showing dimensions A-A
2. Section A-A showing detailed view with beam width $b_w$ and notation "Not greater than the smaller of $c_2$ and $0.75c_1$"]

*Fig. R18.6.2—Maximum effective width of wide beam and required transverse reinforcement.*

**R18.6.2.1** Experimental evidence (Hirosawa 1977) indicates that, under reversals of displacement into the nonlinear range, behavior of continuous members having length-to-depth ratios less than 4 is significantly different from the behavior of relatively slender members. Design rules derived from experience with relatively slender members do not apply directly to members with length-to-depth ratios less than 4, especially with respect to shear strength.

Geometric constraints indicated in 18.6.2.1(b) and (c) were derived from practice and research (ACI PRC-352) on reinforced concrete frames resisting earthquake-induced forces. The limits in 18.6.2.1(c) define the maximum beam width that can effectively transfer forces into the beam-column joint. An example of maximum effective beam width is shown in Fig. R18.6.2.


<!-- From Page 328 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 328

### CODE

**18.6.3** *Longitudinal reinforcement*

**18.6.3.1** If longitudinal reinforcement is required, the requirements of this section shall apply. At any section, the top as well as bottom reinforcement shall consist of at least two continuous bars.

**18.6.3.2** Positive moment strength at joint face shall be at least one-fourth the maximum moment strength provided at face of either joint, along the length of the beam shall be at least one-fifth the maximum moment strength provided at face of either joint.

**18.6.3.3** Lap splices of deformed longitudinal reinforcement only shall be permitted if the lap is designed as a tension splice. Lap splices shall not be used (a) within the joints, (b) within a distance of twice the beam depth from the face of the joint, and (c) at locations of anticipated inelastic behavior where flexural yielding is likely to occur as a result of lateral displacements beyond the design range. Welded splices and mechanical splices shall conform to 18.2.7 and welded splices shall conform to 18.2.8.

**18.6.3.4** Mechanical splices shall conform to 18.2.7 and welded splices shall conform to 18.2.8.

**18.6.3.5** Discontinued or special moment frame as permitted by the 2014 Code, Discontinued reinforcement shall be extended into the joint and shall develop in tension in accordance with (a) through (d). If a portion of the lateral reinforcement extending the top reinforcement shall not exceed 0.625 for Grade 60 reinforcement and 0.52 for Grade 80 reinforcement.

**18.6.3.6** (a) Prestressed reinforcement shall be unbonded at locations other than (b) through (d). (b) At splices, prestressing of a tension stressed member where inelastic response may occur shall be anchored or be beyond the exterior face of the joint. (c) For prestressed reinforcement shall contribute more than one-quarter of the factored flexural strength at any section, such reinforcement shall be prestressed to an effective prestress of not less than the yield force bounded by or extend 12$d_b$ or the distance shall be least one-quarter of the reinforcement forces bounded by or and 12$d_b$, or the joint shall be provided to confine.

### COMMENTARY

**R18.6.3** *Longitudinal reinforcement*

Bottom bars shall primarily on consideration of costs and other factors on requirements. Longitudinal reinforcement shall provided on design in building main sections, whether near exterior beams or typical.

**R18.6.3.1** Lap splices of reinforcement are prohibited along lengths where flexural yielding is anticipated because for the splices may slip in beams where longitudinal bars loading into the inelastic range. Transverse reinforcement for lap splices at any location is mandatory because of the necessity to confine concrete in the cover along the length of the splice.

**R18.6.3.5** These provisions were developed, in part, based on the development of headed deformed reinforcement (ACI 408).


<!-- From Page 329 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 329

### CODE

**18.6.4** *Transverse reinforcement*

### COMMENTARY

mance can be obtained with greater amounts of prestressed reinforcement, this restriction is needed to allow the use of the same response modification and deflection amplification factors as those specified in model codes for special moment frames without prestressed reinforcement. Prestressed special moment frames will generally contain continuous prestressed reinforcement that is anchored with adequate cover at or beyond the exterior face of each beam-column connection located at the ends of the moment frame.

Fatigue testing for 50 cycles of loading between 40 and 80% of the specified tensile strength of the prestressed reinforcement has been a long-standing industry practice (ACI PRC-423.3; ACI SPEC-423.7). The 80% limit was increased to 85% to correspond to the 1% limit on the strain in prestressed reinforcement. Testing over this range of stress is intended to conservatively simulate the effect of a severe earthquake. Additional details on testing procedures are provided in ACI SPEC-423.7.

**R18.6.4** *Transverse reinforcement*

Transverse reinforcement is required primarily to confine the concrete and provide lateral support for the reinforcing bars in regions where yielding is expected. Examples of transverse reinforcement suitable for beams are shown in Fig. R18.6.4.

In earlier Code editions, the upper limit on hoop spacing was the least of $d/4$, eight longitudinal bar diameters, 24 tie bar diameters, and 12 in. The upper limits were changed in the 2011 edition because of concerns about adequacy of longitudinal bar buckling restraint and confinement in large beams.

In the case of members with varying strength along the span or members for which the permanent load represents a large proportion of the total design load, concentrations of inelastic rotation may occur within the span. If such a condition is anticipated, transverse reinforcement is also required in regions where yielding is expected. Because spalling of the concrete shell might occur, especially at and near regions of flexural yielding, all web reinforcement is required to be provided in the form of closed hoops.


<!-- From Page 330 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 330

### CODE

**18.6.4.1** Hoops or closed stirrups in accordance with 18.6.4.3 shall be provided in the following regions of a beam:

(a) Over a length equal to twice the beam depth measured from the face of the supporting column toward midspan, at both ends of the beam

(b) Over lengths equal to twice the beam depth on both sides of a section where flexural yielding is likely to occur as a result of lateral displacements beyond the elastic range of behavior.

**18.6.4.2** In regions of the beam defined in 18.6.4.1, primary longitudinal reinforcing bars closest to the tension and compression faces shall have lateral support in accor-

### COMMENTARY

[THIS IS FIGURE: Detailed technical drawings showing:
(a) Overlapping hoops - with Detail A showing crossties and 90-degree hooks
(b) Closed stirrups - with Detail B showing 6db extension and Detail C showing crosstie configurations
The figure includes annotations about:
- Crosstie as defined in 25.3.5
- 6db extension, 6db ≥ 3 in. extension
- Consecutive crossties engaging the same longitudinal bars have their 90-degree hooks on opposite sides
- Maximum spacing between bars restrained by legs of crossties, hoops, or closed stirrups = 14 in.]

*Fig. R18.6.4—Examples of beam transverse reinforcement and illustration of limit on maximum horizontal spacing of supported longitudinal bars.*


<!-- From Page 331 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 331

### CODE

dance with 25.7.2.3 and 25.7.2.4. The transverse spacing of supported flexural reinforcing bars shall not exceed 14 in. Skin reinforcement required by 9.7.2.3 need not be laterally supported.

**18.6.4.3** Closed stirrups in beams shall be permitted to be made up of one or more U-stirrups having seismic hooks at both ends, closed by a crosstie. Consecutive crossties engaging the same longitudinal bar shall have their 90-degree hooks at opposite sides of the flexural member. If the longitudinal reinforcing bars secured by the crossties are confined by a slab on only one side of the beam, the 90-degree hooks of the crossties shall be placed on that side.

**18.6.4.4** The first hoop or closed stirrup shall be located not more than 2 in. from the face of a supporting column. Spacing of the hoops or closed stirrups shall not exceed the least of (a) through (d):

(a) $d/4$

(b) 6 in.

(c) For Grade 60, $6d_b$ of the smallest primary flexural reinforcing bar excluding longitudinal skin reinforcement required by 9.7.2.3

(d) For Grade 80, $5d_b$ of the smallest primary flexural reinforcing bar excluding longitudinal skin reinforcement required by 9.7.2.3

**18.6.4.5** Where hoops are not required, stirrups with seismic hooks at both ends shall be spaced at a distance not more than $d/2$ throughout the length of the beam.

**18.6.4.6** In beams having factored axial compressive force exceeding $A_g f'_c/10$, hoops satisfying 18.7.5.2 through 18.7.5.4 shall be provided along lengths given in 18.6.4.1. Along the remaining length, hoops satisfying 18.7.5.2 shall have spacing $s$ not exceeding the least of 6 in., $6d_b$ of the smallest Grade 60 enclosed longitudinal beam bar, and $5d_b$ of the smallest Grade 80 enclosed longitudinal beam bar. Where concrete cover over transverse reinforcement exceeds 4 in., additional transverse reinforcement having cover not exceeding 4 in. and spacing not exceeding 12 in. shall be provided.

**18.6.5** *Shear strength*

### COMMENTARY

**R18.6.5** *Shear strength*

Unless a beam possesses a moment strength that is on the order of 3 or 4 times the design moment, it should be assumed that it will yield in flexure in the event of a major earthquake. The design shear force should be selected so as to be a good approximation of the maximum shear that may develop in a member. Therefore, required shear strength for frame members is related to flexural strengths of the designed member rather than to factored shear forces indicated by lateral load analysis. The conditions described by 18.6.5.1 are illustrated in Fig. R18.6.5. The figure also shows that vertical earthquake effects are to be included, as is typi-


<!-- From Page 332 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 332

### CODE

### COMMENTARY

cally required by the general building code. For example, ASCE/SEI 7 requires vertical earthquake effects, $0.2\rho_{DS}$, to be included.

Because the actual yield strength of the longitudinal reinforcement may exceed the specified yield strength and because strain hardening of the reinforcement is likely to take place at a joint subjected to large rotations, required shear strengths are determined using a stress of at least $1.25f_y$ in the longitudinal reinforcement.

Experimental studies (Popov et al. 1972) of reinforced concrete members subjected to cyclic loading have demonstrated that more shear reinforcement is required to ensure a flexural failure if the member is subjected to alternating nonlinear displacements than if the member is loaded in only one direction: the necessary increase of shear reinforcement being higher in the case of no axial load. This observation is reflected in the Code (refer to 18.6.5.2) by eliminating the term representing the contribution of concrete to shear strength. The added conservatism on shear is deemed necessary in locations where potential flexural hinging may occur. However, this stratagem, chosen for its relative simplicity, should not be interpreted to mean that no concrete is required to resist shear. On the contrary, it may be argued that the concrete core resists all the shear with the shear (transverse) reinforcement confining and strengthening the concrete. The confined concrete core plays an important role in the behavior of the beam and should not be reduced to a minimum just because the design expression does not explicitly recognize it.


<!-- From Page 333 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 333

### CODE

[THIS IS FIGURE: Detailed diagram showing design shears for beams and columns in a moment frame, including:
- Top view of beam-column joint showing dimensions $\ell_u$ and $\ell_n$
- Distributed load equation: $w_u = (1.2 + 0.2S_{DS})D + 1.0L + 0.2S$
- Beam shear diagram with moments $M_{pr1}$ and $M_{pr2}$
- Column shear diagram with forces $P_u$ and moments $M_{pr3}$ and $M_{pr4}$]

*Fig. R18.6.5—Design shears for beams and columns.*

**18.6.5.1** *Design forces*

The design shear force $V_e$ shall be calculated from consideration of the forces on the portion of the beam between faces of the joints. It shall be assumed that moments of opposite sign corresponding to probable flexural strength, $M_{pr}$, act at the joint faces and that the beam is loaded with the factored gravity and vertical earthquake loads along its span.

**18.6.5.2** *Transverse reinforcement*

Transverse reinforcement over the lengths identified in 18.6.4.1 shall be designed to resist shear assuming $V_c = 0$ when both (a) and (b) occur:

(a) The earthquake-induced shear force calculated in accordance with 18.6.5.1 represents at least one-half of the maximum required shear strength within those lengths.

(b) The factored axial compressive force $P_u$ including earthquake effects is less than $A_g f'_c/20$.

### COMMENTARY

**Notes on Fig. R18.6.5:**

1. Direction of shear force $V_e$ depends on relative magnitudes of gravity loads and shear generated by end moments.

2. End moments $M_{pr}$ based on steel tensile stress of $1.25f_y$ where $f_y$ is specified yield strength. (Both end moments should be considered in both directions, clockwise and counterclockwise).

3. End moment $M_{pr}$ for columns need not be greater than moments generated by the $M_{pr}$ of the beams framing into the beam-column joints. $V_e$ should not be less than that required by analysis of the structure.


<!-- From Page 334 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 334

### CODE

**18.7—Columns of special moment frames**

**18.7.1** *Scope*

**18.7.1.1** This section shall apply to columns of special moment frames that form part of the seismic-force-resisting system and are proportioned primarily to resist flexure, shear, and axial forces.

**18.7.2** *Dimensional limits*

**18.7.2.1** Columns shall satisfy (a) and (b):

(a) The shortest cross-sectional dimension, measured on a straight line passing through the geometric centroid, shall be at least 12 in.

(b) The ratio of the shortest cross-sectional dimension to the perpendicular dimension shall be at least 0.4.

**18.7.3** *Minimum flexural strength of columns*

### COMMENTARY

**R18.7—Columns of special moment frames**

**R18.7.1** *Scope*

This section applies to columns of special moment frames regardless of the magnitude of axial force. Before 2014, the Code permitted columns with low levels of axial stress to be detailed as beams.

**R18.7.2** *Dimensional limits*

The geometric constraints in this provision follow from previous practice (Seismology Committee of SEAOC [1996]).

**R18.7.3** *Minimum flexural strength of columns*

The intent of 18.7.3.2 is to reduce the likelihood of yielding in columns that are considered as part of the seismic-force-resisting system. If columns are not stronger than beams framing into a joint, there is increased likelihood of inelastic action. In the worst case of weak columns, flexural yielding can occur at both ends of all columns in a given story, resulting in a column failure mechanism that can lead to collapse. Connections with discontinuous columns above the connection, such as roof-level connections, are exempted if the column axial load is low, because special moment frame columns with low axial stress are inherently ductile and column yielding at such levels is unlikely to create a column failure mechanism that can lead to collapse.

In 18.7.3.2, the nominal strengths of the beams and columns are calculated at the joint faces, and those strengths are compared directly using Eq. (18.7.3.2). The 1995 and earlier Codes required design strengths to be compared at the center of the joint, which typically produced similar results but with added calculation effort.

In determining the nominal moment strength of a beam section in negative bending (top in tension), longitudinal reinforcement contained within an effective flange width of a top slab that acts monolithically with the beam increases the beam strength. French and Moehle (1991), on beam-column subassemblies under lateral loading, indicates that using the effective flange widths defined in 6.3.2 gives reasonable estimates of beam negative moment strengths of interior connections at story displacements approaching 2 percent of


<!-- From Page 335 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 335

### CODE

**18.7.3.1** Columns shall satisfy 18.7.3.2 or 18.7.3.3, except at connections where the column is discontinuous above the connection and the column factored axial compressive force $P_u$ under load combinations including earthquake effect, $E$, are less than $A_g f'_c/10$.

**18.7.3.2** The flexural strengths of the columns shall satisfy

$$\sum M_{nc} \geq (6/5) \sum M_{nb} \quad (18.7.3.2)$$

where

$\sum M_{nc}$ is sum of nominal flexural strengths of columns framing into the joint, evaluated at the faces of the joint. Column flexural strength shall be calculated for the factored axial force, consistent with the direction of the lateral forces considered, resulting in the lowest flexural strength.

$\sum M_{nb}$ is sum of nominal flexural strengths of the beams framing into the joint, evaluated at the faces of the joint. In T-beam construction, where the slab is in tension under moments at the face of the joint, slab reinforcement within an effective slab width defined in accordance with 6.3.2 shall be assumed to contribute to $M_{nb}$ if the slab reinforcement is developed at the critical section for flexure.

Flexural strengths shall be summed such that the column moments oppose the beam moments. Equation (18.7.3.2) shall be satisfied for beam moments acting in both directions in the vertical plane of the frame considered.

**18.7.3.3** If 18.7.3.2 is not satisfied at a joint, the lateral strength and stiffness of the columns framing into that joint shall be ignored when calculating strength and stiffness of the structure. These columns shall conform to 18.14.

**18.7.4** *Longitudinal reinforcement*

### COMMENTARY

story height. This effective width is conservative where the slab terminates in a weak spandrel.

If 18.7.3.2 cannot be satisfied at a joint, 18.7.3.3 requires that any positive contribution of the column or columns involved to the lateral strength and stiffness of the structure is to be ignored. Negative contributions of the column or columns should not be ignored. For example, ignoring the stiffness of the columns ought not to be used as a justification for reducing the design base shear. If inclusion of those columns in the analytical model of the building results in an increase in torsional effects, the increase should be considered as required by the general building code. Furthermore, the column must be provided with transverse reinforcement to increase its resistance to shear and axial forces.

**R18.7.4** *Longitudinal reinforcement*

The lower limit of the area of longitudinal reinforcement is to control time-dependent deformations and to have the yield moment exceed the cracking moment. The upper limit of the area reflects concern for reinforcement congestion, load


<!-- From Page 336 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 336

### CODE

**18.7.4.1** Area of longitudinal reinforcement, $\ell_o$, shall be at least 0.01$A_g$.

**18.7.4.2** In columns with circular loops, there shall be at least two longitudinal bars.

**18.7.4.3** Area of longitudinal reinforcement shall not exceed the lesser of (a) and (b) at locations (a) and (b):

(a) At any section along the column height, where (a) or (b) shall be satisfied:

(a) If longitudinal reinforcement shall be spliced such that the splice length exceeds $\ell_o$, $0.06A_g$.

(b) Transverse reinforcement shall be spliced such that $A_s > 0.06A_g$.

**18.7.4.4** Mechanical splices shall conform to 18.2.7 and welded splices shall conform to 18.2.8. Where a splice is permitted only within the center half of the member length, shall be designed as tension lap splices, and shall be confined by transverse reinforcement at spacing $s_h$ given in 18.7.5.3 and 18.7.5.3.

**18.7.5** *Transverse reinforcement*

**18.7.5.1** Transverse reinforcement required in 18.7.5.2 through 18.7.5.4 shall be provided over a length $\ell_o$ from each joint face and on both sides of any section where flexural yielding is likely to occur as a result of lateral displacements beyond the design range of behavior. Length $\ell_o$ shall be at least the longest of (a), (b), and (c):

(a) One-sixth of the clear span of the member

(b) Maximum cross-sectional dimension of the section where flexural yielding is likely to occur

(c) One-sixth of the clear span of the column

**18.7.5.2** Transverse reinforcement shall be in accordance with either (a) or (b):

### COMMENTARY

transfer from floor slabs to columns (especially in two-way construction) and the development of high bond stresses causing crushing of the cover concrete. Concrete near the ends of the column is framed in spread configuration, makes lap splices in these locations vulnerable. If lap splices cannot be avoided within these locations, very close transverse reinforcement spacing is required. A lap splice in the midheight where stress reversal is likely to be limited to a smaller stress range than at locations near the joints. Transverse reinforcement that confines spliced reinforcement during bending is also important. The bar bending actions along the height and the need for confinement of lap splices subjected to stress reversals are considered in 25.5.2.1.

**R18.7.5** *Transverse reinforcement*

This section is concerned with confining the concrete and providing lateral support to the longitudinal reinforcement.

**R18.7.5.1** This section stipulates a minimum length over which to provide closely-spaced transverse reinforcement at potential inelastic hinge locations in columns. Research results indicate that the length should be increased beyond the minimum locations, such as at midheight of the column, where inelastic bending may develop.

**R18.7.5.2** Sections 18.7.5.2 and 18.7.5.3 provide required transverse reinforcement for special moment frames. Figure 18.7.3.2 shows an example of transverse reinforcement in columns and joints of special moment frames. Figure


<!-- From Page 337 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 337

### CODE

(a) Transverse reinforcement shall comprise either single or overlapping spirals, circular hoop, or single or overlapping circular hoops

(b) Heads of rectilinear hoops and crossties shall engage peripheral longitudinal reinforcing bars.

Consecutive rectilinear hoops engaging the same longitudinal bars shall be permitted, subject to the limitation of 25.7.2.2. Where transverse reinforcement is less than dimensions of two successive transverse reinforcement sets are staggered.

**18.7.5.3** Within the length defined by 18.7.5.1, spacing of transverse reinforcement $s_o$ shall not exceed the least of (a) through (d):

(a) Where rectilinear hoops or crossties are used, they shall provide lateral support in accordance with 25.7.2.3.

(b) Transverse reinforcement in accordance with 18.7.5.2 shall be provided such that the spacing $s_o$ of longitudinal bars with lateral support provided by the center of a hoop or by a seismic hook, and the clear $s_h$ shall not exceed $A_s f_y/35000$ for columns with circular hoops or spirals shall conform to 25.7.2.2, and the load combination including $E$.

(c) Reinforcement shall be arranged such that the spacing $A_s$ of longitudinal bars with lateral support provided by the corner of a hoop or by a seismic hook and the clear $s_h$ shall not exceed $14$ in. And the center of a hoop or by a seismic hook, and the clear $s_h$ shall not exceed $A_s f_y/35000$ pounds shall conform to 25.7.2.3 when axial load combination including $E$.

(d) Where $P_u > (0.3 A_g f'_c + P_b)$ from strength load combinations, the spacing shall conform to 25.7.2.3 and the concrete cover shall not exceed $4$ in., and if concrete spacing not exceeding the least of (a), (b), and (c).

### COMMENTARY

provided by one hoop and three crossties. Crossties with a 90-degree hook are not as effective as other crossties with seismic hooks that meet the dimensional requirements. Where values of $P_u/A_g f'_c$ and lower concrete compressive stresses exist, columns are not subjected to the ductility demands of other columns. For higher values of $P_u/A_g f'_c$ (or which axial stress might be obtained), ductility demands exist and the hinging demands from severe ground motions, the design should use spacing $s_o$ as specified in The $1.25f_y$ limit on $s_h$ is also intended to improve buckling resistance of the longitudinal reinforcement. For bundled bars, the largest enclosed bar diameter should be used. Where these values are constant along the length of the member, ties in bundled bars, and the longer dimension are-hooks should be considered.

Whereas prior Codes had the same minimum transverse reinforcement in columns, high beam-column joints, and diagonally reinforced coupling beams referred to the same section of the Code (most recently, Section 21.5 of ACI 318-14). Different detailing requirements often among the member types based on consideration of their loadings, deformations, and performance. The 2019 edition of the Code clarified the use of the distance between legs of hoops or crossties. In the 2014 edition of the Code, $s_x$ (refer to the distance between legs-2.3(b) bars in ACI 318-14).

[THIS IS FIGURE: Diagram showing consecutive crossties engaging the same longitudinal bar with 6db extension, illustrated in both plan and 3D views with detailed annotations about bar spacing and hoop configurations]

*Fig. R18.7.3.2—Example of transverse reinforcement in*


<!-- From Page 338 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 338

### CODE

(a) For Grade 60, $6d_b$ of the smallest longitudinal bar enclosed

(b) For Grade 80, $5d_b$ of the smallest longitudinal bar enclosed

(c) For rectilinear hoops and crossties, the lesser of $6$ in. and $14/(h_x/h)$ where $h_x$ is the center-to-center dimension of crossties transverse to the direction being considered.

**18.7.5.3** Spacing of transverse reinforcement shall not exceed the least of (a) through (c) for:

(a) For Grade 60, $6d_b$ of the smallest longitudinal bar enclosed

(b) For Grade 80, $5d_b$ of the smallest longitudinal bar enclosed

(c) 6 in. as calculated by:

$$s = \frac{14 - h_x}{3} \quad (18.7.5.3)$$

The value of $s$ from Eq. (18.7.5.3) shall not exceed 6 in. and shall not be less than 3 in.

**18.7.5.4** Amount of transverse reinforcement shall be in accordance with Table 18.7.5.4. The cross-sectional area of transverse reinforcement $A_{sh}$ in Eq. (18.7.5.4a) shall not be less than that calculated according to Eq. (18.7.5.4a) and (18.7.5.4b):

$$A_{sh} = \frac{0.3 s_{hx} h_c f'_c}{f_{yt}} \left[\frac{A_g}{A_{ch}} - 1\right] \quad (18.7.5.4a)$$

$$A_{sh} = \frac{0.09 s_{hx} h_c f'_c}{f_{yt}} \quad (18.7.5.4b)$$

where $s$ is the number of longitudinal bars or bar bundles around the perimeter of a column with rectilinear hoops and crossties. For circular hoops or spirals, the spacing of seismic hooks.

[THIS IS TABLE: Table 18.7.5.4 showing transverse reinforcement requirements for columns of special moment frames, with different configurations for rectilinear hoops and circular hoops/spirals, including applicable expressions and cross-section diagrams]

### COMMENTARY

**R18.7.5.3** This limit on $h_x$ should be practical for design or legs of overlapping hoops within the section to less than 14 in., then the $h_x$ limit can be increased as permitted by Eq. (18.7.5.3). Where design circumstances preclude adequate longitudinal diameter is intended to provide adequate longi-tudinal support to control buckling of the long bars.

**R18.7.5.4** The effect of helical (spiral) reinforcement, and adequately reinforced rectilinear hoops on reinforcement in columns and wall boundaries was studied by (Saatcioglu and Razvi 1992; Sheikh and Uzumeri 1980; Sheikh and Yeh 1990; Moehle 1988). Expressions (a), (b), (d), and (e) in Table 18.7.5.4 have historically been used in ACI 318 to compute the required amount of reinforcement. The intent of that spalling of shell concrete does not result in a loss of confinement and load strength. Experiments by and (f) suggest the effectiveness of closed hoops and crossties in providing axial load capacity and ductility. For members maintaining a drift ratio of 0.03 with limited strength degradation, a confinement coefficient of approximately 0.04 was approximately needed. For members resisting significant P effects at high axial load levels, the need of compression-controlled behavior for symmetric loading. The $h_c$ term for rectangular sections and column design, where (axially loaded, spirals), laterally supported longitudinal reinforcement determines the level of confinement required to control buckling. The 2005 tests concluded that required confinement should be related to the total number of supported long bars because such columns are more likely to spall. In prior editions, provision for the number of bars required for rectilinear hoops of special moment frames was not standard because such columns given the formula had data for such columns. This construction documents...

[Continuing with additional technical commentary about confinement reinforcement requirements and references to Table 18.7.5.4]


<!-- From Page 339 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 339

### CODE

**18.7.5.5** Beyond the lengths defined by 18.7.5.1, the column shall contain spiral or circular hoop reinforcement satisfying 25.7.3, or the column shall contain rectilinear hoops in accordance with the least of (a), (b), and (c) of the smallest longitudinal bar enclosed. Otherwise, the column shall contain rectilinear hoops satisfying 18.7.5.2 through 18.7.5.4. Where the required spacing of transverse reinforcement is required by 18.7.5.4 or 18.7.6.

**18.7.5.6** Columns supporting reactions from discontinued stiff members, such as walls, shall satisfy (a) and (b):

(a) Transverse reinforcement required by 18.7.5.2 through 18.7.5.4 shall be provided over the height beneath the level at which the discontinuity occurs if the portion of factored axial compressive force in these columns related to earthquake effects exceeds the value of $A_g f'_c/10$. If design forces have been magnified to account for the overstrength of the vertical elements of the seismic-force-resisting system, the limit of $A_g f'_c/10$ shall be increased to $A_g f'_c/4$.

(b) Transverse reinforcement shall extend into the discontinued member at least $\ell_o$ of the largest longitudinal column bar at the point of termination. Where the column terminates on a footing or mat, transverse reinforcement shall extend at least 12 in. into the footing or mat.

**18.7.5.7** If the concrete cover outside the confining transverse reinforcement required by 18.7.5.1, 18.7.5.3, and 18.7.5.5 exceeds 4 in., additional transverse reinforcement having cover not exceeding 4 in. and spacing not exceeding 12 in. shall be provided.

**18.7.6** *Shear strength*

**18.7.6.1** *Design forces*

**18.7.6.1.1** The design shear force $V_e$ shall be calculated from considering the forces on the portion of the column between faces of the joints or between critical sections of the column. Critical sections are located in accordance with 22.5.1.1 at the face of the joint and with the range of factored axial load forces, $P_u$, acting on the column. The column shear need not exceed those calculated by analysis of the structure considering earthquake effects acting on the joint. In no case shall $V_e$ be less than the factored shear calculated by analysis of the structure.

### COMMENTARY

**R18.7.5.5** This provision is intended to provide reasonable distribution of confinement reinforcement along the length of the column, consistent with the potential for flexural damage to columns in this region, and the minimum level of confinement support should generally be more stringent along the column along its length.

**R18.7.5.6** Discontinuous structural walls, such as wall discontinuity regions at and discontinuity below, and locations at level of discontinuous stiff members. The stiff member has been discontinued, unless the factored forces corresponding to earthquake effect are low. Refer to 18.14.7.2.6 for discussion of the overstrength factor $\Omega_o$.

**R18.7.5.7** The unreinforced shell may spell as the column deforms to resist earthquake effects. Separation of portions of the shell from the core caused by local spalling creates a potentially hazardous condition as well as reducing the area of column to resist or portions of the shell falling away from the column.

**R18.7.6** *Shear strength*

**R18.7.6.1** *Design forces*

If the design strength of 18.6.5.1 also apply to columns. In the general case, the flexural strength of columns be formed by the end moments of the beams framing into the beam-column joints. If the flexural strengths of the beams on one side of the joint are moment strength of the beams on the other side, $M_{pr}$ may be limited by the smaller beam strengths. A higher strength reduction factor of 1.0 and reinforcement with an effective yield stress equal to at least $1.25f_y$. Distribution of $M_{pr}$ between the top and bottom of the column or above and below the joint should be based on analysis.


<!-- From Page 340 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 340

### CODE

**18.7.6.2** *Transverse reinforcement*

**18.7.6.2.1** Columns shall be designed to resist shear assuming $V_c = 0$ if both (a) and (b) occur:

(a) The earthquake-induced shear force calculated in accordance with 18.7.6.1, at least one-half of the maximum required shear strength within $\ell_o$

(b) The factored axial compressive force $P_u$, including earthquake effects is less than $A_g f'_c/20$.

**18.8—Joints of special moment frames**

**18.8.1** *Scope*

**18.8.1.1** This section shall apply to beam-column joints in special moment frames forming part of the seismic-force-resisting system.

**18.8.2** *General*

**18.8.2.1** Forces in longitudinal beam reinforcement at the faces of the joints shall not exceed, excepting the center strip requirements if $1.25f_y$.

**18.8.2.2** Longitudinal reinforcement terminated in a joint shall extend to the far face of the joint core and shall be developed in tension in accordance with 18.8.5.

**18.8.2.3** Where longitudinal beam reinforcement extends through a beam-column joint, the depth of the joint parallel to the beam longitudinal reinforcement shall be at least the column depth. In exceptional cases where the depth of the beam $h$ is more than the column dimension parallel to the beam, $c_h \geq 0.7 h$ for balcony-slab concrete and $1.0$ or all other cases. Where $h > c_h$, beam-column joints shall be designed by the strut-and-tie method in accordance with Chapter 23 and the joint shear as part of the seismic-force-resisting system in accordance with 18.8.4.

### COMMENTARY

**R18.8—Joints of special moment frames**

**R18.8.2** *General*

Development of inelastic rotations at the faces of joints of reinforced concrete frames is associated with strains in the longitudinal beam reinforcement well in excess of yield. Consequently, joint shear force generated by the flexural reinforcement is calculated for a stress of $1.25f_y$ in the reinforcement. This is consistent with the provisions in 18.6 and 18.7 reasons for the possible development of stresses in excess of design yield strength in longitudinal beam reinforcement, as provided in 18.6.2.1 and 18.6.3.2.

**R18.8.2.2** The design provisions for hooked bars in special moment frames were developed for joints with standard 90-degree hooks. Therefore, standard 90-degree hooks embedded in standard confinement regions are acceptable in joints of special moment frames. Hooks that comply with 18.8.5, however, may have in some required to check compression development length of longitudinal reinforcement. Anchorage of experimental data indicates that hooks in tension can influence the strain field in joint behavior (Grammont and Soetern 1976; Kage et al. 2009).

**R18.8.2.3** The beam dimension parallel to the direction in The column dimension parallel to the beam reinforcement in a joint is sufficient to allow full anchorage force $A_s f_y$ (equal cross-sectional area of the concrete joint $c_h$ is the beam). Test results and analytical studies (Leon 1984; Ehsani 1982; Leon 1989; Aoyama 1991; Lin et al. 2000) have shown that the longitudinal beam reinforcement may not develop within the joint if the depth $h$ of the beam exceeds (the dimension side, the bond stresses on these straight bars may be very high, possibly causing splitting of the concrete and prematurely).


<!-- From Page 341 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 341

### CODE

**18.8.2.3.1** Concrete used in joints with Grade 80 longitudinal reinforcement shall be normalweight concrete.

**18.8.3** *Transverse reinforcement*

**18.8.3.1** Joint transverse reinforcement shall satisfy 18.7.5.2, 18.7.5.3, 18.7.5.4, and 18.7.5.7, except as permitted in 18.8.3.2.

**18.8.3.2** Within the depth of the shallowest framing member, transverse reinforcement in accordance with 18.7.5.2 through 18.7.5.4 shall be permitted to be placed within the overall depth of the shallowest member.

**18.8.3.3** Longitudinal beam reinforcement outside the column core shall be confined by transverse reinforcement meeting the requirements of Chapter 7 and the requirements of 18.6.4.1, and requirements of 18.6.4.3 and 18.6.4.3. If such confinement is not provided by a beam framing into the joint.

### COMMENTARY

adjacent beam framing it would be necessary to have a ratio of column dimension to bar diameter of approximately 32 for deformed bars with standard hooks. Column dimensions much larger than this will not be a problem; a ratio larger than 32 is considered adequate behavior of the ratio of joint depth to maximum beam longitudinal bar diameter for Grade 60 reinforcement. It is not specifically calibrated, but is recommended for lightweight concrete. A joint depth of 20d_b for Grade 80 reinforcement is intended to achieve similar performance to 32d_b for Grade 60, taking into account the increased yield stress and strain. The smaller joint depth permits more reasonable control on the amount of slip of the beam bars at the column face, considering the number of anticipated strain reversals and possible strain penetration into the joint. Use of normalweight concrete, in conjunction with 18.8.5.1 for earthquake. A thorough treatment of this topic is given in PRC and Durrani (1987).

The 32d_b and 20d_b joint aspect ratios applies only to beams that are designed as part of the seismic-force-resisting system. Joints having depth less than half the beam depth being framed into them should be designed using a strut-and-tie model (refer to 18.8.2.3 and R18.8.2.3). Tests to demonstrate performance of such joints have been performed (Kaku and Asakusa 1991).

**R18.8.2.3.1** Test data justify the combination of light-weight concrete and Grade 80 longitudinal reinforcement in joints.

**R18.8.3** *Transverse reinforcement*

The required transverse reinforcement in a joint regardless of the magnitude of the calculated shear force.

**R18.8.3.2** The amount of confining reinforcement may be waived and the spacing may be increased at beams of lesser depth framing into the joint.

**R18.8.3.3** The required transverse reinforcement, or transverse beams if present, is intended to confine the beam longitudinal reinforcement and improve force transfer to the beam-column joint.

If the joint does not have transverse reinforcement through the transverse beams, the transverse beams must be detailed to confine the column core is shown in Fig. R18.6.2. Additional detailing guidance and design recommendations for both interior and exterior joints, including those with beams framing into the column core, may be found in Moehle et al. (2011).


<!-- From Page 342 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 342

### CODE

**18.8.4** *Shear strength*

**18.8.4.1** Joint shear force $V_u$ shall be calculated on a plane at mid-height of the joint from calculated forces at the joint faces using tensile and compressive beam forces determined in accordance with 18.8.2.1 and column shear consistent with beam probable flexural strengths $M_{pr}$.

**18.8.4.2** $\phi$ shall be in accordance with 21.2.4.4.

**18.8.4.3** $V_n$ of the joint shall be in accordance with Table 18.8.4.3.

**Table 18.8.4.3—Nominal joint shear strength $V_n$**

| Column | Beam in direction of $V_u$ | Confinement by transverse beams according to 15.5.2.5 | $V_n$, lb(1) |
|--------|---------------------------|------------------------------------------------------|--------------|
| Continuous or meets 15.5.2.3 | Continuous or meets 15.5.2.4 | Confined | $20\lambda \sqrt{f'_c} A_j$ |
|  |  | Not confined | $15\lambda \sqrt{f'_c} A_j$ |
|  | Other | Confined | $15\lambda \sqrt{f'_c} A_j$ |
|  |  | Not confined | $12\lambda \sqrt{f'_c} A_j$ |
| Other | Continuous or meets 15.5.2.4 | Confined | $15\lambda \sqrt{f'_c} A_j$ |
|  |  | Not confined | $12\lambda \sqrt{f'_c} A_j$ |
|  | Other | Confined | $12\lambda \sqrt{f'_c} A_j$ |
|  |  | Not confined | $8\lambda \sqrt{f'_c} A_j$ |

(1) $\lambda$ shall be 0.75 for lightweight concrete and 1.0 for normalweight concrete. $A_j$ shall be calculated in accordance with 15.5.2.2.

**18.8.5** *Development length of bars in tension*

**18.8.5.1** For bar sizes No. 3 through No. 11 terminating in a standard hook, $\ell_{dh}$ shall be calculated by Eq. (18.8.5.1), but $\ell_{dh}$ shall be at least the greater of $8d_b$ and 6 in. for normal-

### COMMENTARY

**R18.8.4** *Shear strength*

The shear strength values given in 18.8.4.3 are based on the recommendation in ACI PRC-352 for joints with members that are expected to undergo reversals of deformation into the inelastic range, although the ACI PRC-352 definition of effective cross-sectional joint area is sometimes different. The given nominal joint shear strengths do not explicitly consider transverse reinforcement in the joint because tests of joints (Meinheit and Jirsa 1977) and deep beams (Hirosawa 1977) have indicated that joint shear strength is not sensitive to transverse reinforcement if at least the required minimum amount is provided in the joint.

Cyclic loading tests of joints with extensions of beams with lengths at least equal to their depths have indicated similar joint shear strengths to those of joints with continuous beams. These findings suggest that extensions of beams and columns, when properly dimensioned and reinforced with longitudinal and transverse bars, provide effective confinement to the joint faces, thus delaying joint strength deterioration at large deformations (Meinheit and Jirsa 1981).

**R18.8.5** *Development length of bars in tension*

**R18.8.5.1** Minimum embedment length in tension for deformed bars with standard hooks is determined using Eq. (18.8.5.1), which is based on the requirements of 25.4.3 of ACI 318-14. The embedment length of a bar with a stan-


<!-- From Page 343 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 343

### CODE

weight concrete and at least the greater of $10d_b$ and 7 1/2 in. for lightweight concrete:

$$\ell_{dh} = \frac{f_y d_b}{65 \lambda \sqrt{f'_c}} \quad (18.8.5.1)$$

where the hook shall be located within the confined core. For lightweight concrete, $\lambda$ shall equal 0.75. For normalweight concrete and 1.0 otherwise.

The hook shall be located within the confined core of a column or boundary element, with the hook bent into the joint.

**18.8.5.2** Headed deformed bars satisfying 20.2.1.6 shall develop $f_y$ at a critical section in accordance with Table 25.4.3.2 of the section.

**18.8.5.3** For sizes No. 3 through No. 11$d_b$, the development length is in accordance with 18.8.5.1 if the bar extends into a confined core and is at least the greater of (a) and (b):

(a) 2.5 times the length in accordance with 18.8.5.1 if the member is provided with transverse reinforcement with the hook bent into the joint.

**18.8.5.4** Straight bars terminated in a joint shall pass through the confined core of a column or boundary element. Any portion of $\ell_d$ within the confined core shall be increased by a factor of 1.6.

### COMMENTARY

dard hook is the distance, parallel to the bar from the critical section where the bar is to be developed to the tangent point between the tail of the hook and the bend. This length is perpendicular to the axis of the bar (refer to Table 25.3.1).

Straight bars with an adequate tail extension for the equation for $\ell_{dh}$ were tested with standard hooks with radius of 2$d_b$. Coefficients of 1.0 are given; coatings, 0.7 (epoxy), and 0.8 ($f'_c$ greater than 60 psi). Prior to the 2008 edition, Chapter 12, Chapter 18 specified $\ell_{dh}$ as 8$d_b$. These bar sizes were increased in the 2014 Code. Factor $\lambda$ of 1.0 in ACI 318-14 was increased to reflect the effect of bar orientation. Factors such as the actual stress at the normal face relative to the bar hooks of transverse beam-column joint types are beyond the scope. The equation for $\ell_{dh}$ were implicitly considered in the formulation of 18.8.2.3.1.

The requirement for the hook to project into the joint in accordance with Table 25.4.3.2 of Eq. (18.8.5.1) is not used in the beam for Eq. (18.8.5.1).

The requirement for the hook to project into the joint is intended to utilize the core of the column for development. test stress terminated in a joint with a standard hook, preferably a standard hook and other arrangements [Soroushian et al. 1988].

**R18.8.5.2** The factor 1.25 is intended to represent the coefficient between the tension and bar yielding capacity prior to failure. Factors of 1.0, 0.8, or both result from tests on special structural forms.

**R18.8.5.3** Head embedment development length in tension for headed deformed bars with length measured by 18.8.5.1. Section 18.8.5.3(b) refers to top bars. Lack of reference to "top" in 18.8.5.3(a) was intentional, however, is because of the presence of transverse reinforcement and may be unconservative to properly restrain unintended orthogonal seismic effects.

**R18.8.5.4** If the required straight embedment length through the joint is not available, a standard hook is recommended and both equations in accordance with Table 18.8.4.3, or 18.8.5.1, the required development length is increased on the premise that such bars would tend to split more readily than those bent than inside.

$$\ell_d = (M_u / V_u + \ell_a)/1.4$$

or

$$\ell_d = 1.6\ell_d - 0.6\ell_a$$

where $\ell_d$ is the required development length if bar is not entirely embedded in confined concrete; $\ell_a$ is the required development length for a bar entirely embedded in confined core (18.8.5.1); and $\ell_d$ is the length of bar embedded in confined core."


<!-- From Page 344 -->


# ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## Page 344

### CODE

**18.8.5.5** If epoxy-coated reinforcement is used, the development lengths in 18.8.5.1, 18.8.5.3, and 18.8.5.4 shall be multiplied by applicable factors in 25.4.2.5 or 25.4.3.2.

**18.9—Special moment frames constructed using precast concrete**

**18.9.1** *Scope*

**18.9.1.1** This section shall apply to special moment frames constructed using precast concrete forming part of the seismic-force-resisting system.

**18.9.2** *General*

**18.9.2.1** Special moment frames with ductile connections constructed using precast concrete shall satisfy (a) through (c):

(a) Requirements of 18.6 through 18.8 for special moment frames constructed with cast-in-place concrete

(b) $V_u$ for connections calculated according to 22.9 shall be at least $2V_e$ where $V_e$ is in accordance with 18.6.5.1 or 18.7.6.1

### COMMENTARY

**R18.9—Special moment frames constructed using precast concrete**

The detailing provisions in 18.9.2.1 and 18.9.2.2 are intended to produce frames that respond to design displacements essentially like monolithic special moment frames.

Precast frame systems composed of concrete elements with ductile connections are expected to experience flexural yielding in connection regions (Yoshioka and Sekine 1991; Kurose et al. 1991; Restrepo et al. 1995a,b). The restriction on location of mechanical splices is intended to avoid strain concentrations over a short length of reinforcement adjacent to a splice device. Additional requirements for shear strength are provided in 18.9.2.1 to prevent sliding on connection faces. Precast frames composed of elements with ductile connections may be designed to promote yielding at locations not adjacent to the joints. Therefore, design shear $V_e$ as calculated according to 18.6.5.1 or 18.7.6.1, may not be conservative.

Precast concrete frame systems composed of elements joined using strong connections are intended to experience flexural yielding outside the connections. Strong connections include the length of the mechanical splice hardware as shown in Fig. R18.9.2.2. Capacity-design techniques are used in 18.9.2.2(c) to ensure the strong connection remains elastic following formation of plastic hinges. Additional column requirements are provided to avoid hinging and strength deterioration of column-to-column connections.

Strain concentrations have been observed to cause brittle fracture of reinforcing bars at the face of mechanical splices in laboratory tests of precast beam-column connections (Palmieri et al. 1996). Locations of strong connections should be selected carefully or other measures should be taken, such as debonding of reinforcing bars in highly stressed regions, to avoid strain concentrations that can result in premature fracture of reinforcement.

**R18.9.2** *General*


<!-- From Page 345 -->


## CODE

**18.8.5.5** If epoxy-coated reinforcement is used, the development lengths in 18.8.5.1, 18.8.5.3, and 18.8.5.4 shall be multiplied by applicable factors in 25.4.2.5 or 25.4.3.2.

## 18.9—Special moment frames constructed using precast concrete

**18.9.1** *Scope*

**18.9.1.1** This section shall apply to special moment frames constructed using precast concrete forming part of the seismic-force-resisting system.

**18.9.2** *General*

**18.9.2.1** Special moment frames with ductile connections constructed using precast concrete shall satisfy (a) through (c):

(a) Requirements of 18.6 through 18.8 for special moment frames constructed with cast-in-place concrete

(b) $V_n$ for connections calculated according to 22.9 shall be at least $2V_e$ where $V_e$ is in accordance with 18.6.5.1 or 18.7.6.1


<!-- From Page 346 -->


## CODE

(c) Mechanical splices of beam reinforcement shall be located not closer than $h/2$ from the joint face and shall be Class S.

**18.9.2.2** Special moment frames with strong connections constructed using precast concrete shall satisfy (a) through (e):

(a) Requirements of 18.6 through 18.8 for special moment frames constructed with cast-in-place concrete

(b) Provision 18.6.2.1(a) shall apply to segments between locations where flexural yielding is intended to occur due to design displacements

(c) Design strength of the strong connection, $\phi S_n$ shall be at least $S_e$

(d) Primary longitudinal reinforcement shall be made continuous across connections and shall be developed outside both the strong connection and the plastic hinge region

(e) For column-to-column connections, $\phi S_n$ shall be at least $1.4S_u$ $\phi M_n$ shall be at least $0.4M_pr$ for the column within the story height, and $\phi V_n$ shall be at least $V_e$ in accordance with 18.7.6.1


<!-- From Page 347 -->


## CODE

(b) Details and materials used in the test specimens shall be representative.

(c) Modeling of gravity and earthquake effects shall adequately represent the anticipated behavior at all regions of the mechanism that deviate from Code requirements shall be contained in the test specimens that shall establish compliance with the performance requirements.

**18.10—Special structural walls**

**18.10.1** Scope


<!-- From Page 348 -->


## CODE

**18.10.1.1** This section shall apply to special structural walls, including coupled walls, and all components of special structural walls including coupling beams and wall piers forming part of the seismic-force-resisting system.

**18.10.1.2** If coupling beams are part of special structural walls, present concrete shall be in accordance with 18.11 in addition to 18.10.

**18.10.2** Reinforcement

**18.10.2.1** The distributed web reinforcement ratios, $\rho_\ell$ and $\rho_t$ for both longitudinal and transverse reinforcement, if $\ell_w$ does not exceed $\ell_{w,r}/V_{cr}$ shall be permitted to be reduced below $0.0025$. At least two curtains of web reinforcement shall be used if the design shear exceeds $2A_{cv}\sqrt{f'_c}$.

**18.10.2.2** At least two curtains of reinforcement shall be distributed across the shear plane.

**18.10.2.3** At least two curtains of reinforcement shall be used in a wall if $V_u > 2A_{cv}\sqrt{f'_c}$ or $h_w > h_{w,r}/\ell_w$ in which $h_{w,r}$ and $\ell_w$ refer to height and length of entire wall, respectively.

**18.10.2.4** Lap splices in structural walls shall be developed in accordance with 25.5.2.1. At least one of the following shall apply:

(a) All locations where yielding of longitudinal reinforcement is likely to occur as a result of lateral displacements where inelastic rotation is anticipated.

(b) Within a distance equal to twice the wall length above and below the critical section for flexure. All other locations shall be reinforced with 25.5.4 by substituting a bar stress of $1.25f_y$ for $f_y$.

**18.10.2.5** If the effects of longitudinal reinforcement are anticipated at a wall base, tension lap splices shall not be located above and below, critical sections where yielding of longitudinal reinforcement is likely to occur as a result of lateral displacements.


<!-- From Page 349 -->


## CODE

as a result of lateral displacements. The value of $h_w$ need not exceed 20 ft. Boundary regions include those within lengths specified in 18.10.6.4(a) and within a length equal to the wall thickness measured beyond the intersecting region(s) of connected walls.

(d) Mechanical splices of reinforcement shall conform to 18.2.7 and welded splices of reinforcement shall conform to 18.2.8.


<!-- From Page 350 -->


## CODE

[THIS IS FIGURE: Diagram showing wall boundary regions within heights where lap splices are not permitted. The figure includes:
- (a) Elevation view showing floor slab, longitudinal bar at boundary region, critical section for flexure and axial loads, with annotations for minimum heights and critical section dimensions
- (b) Section A-A showing boundary region, wall intersection boundary region, and dimensional annotations]

**Note:** For clarity, only the required reinforcement is shown

*(a) Elevation*

*(b) Section A-A*

*Fig. R18.10.2.3—Wall boundary regions within heights where lap splices are not permitted.*

**18.10.2.4** Walls or wall piers with $h_w/\ell_w \geq 2.0$ that are effectively continuous from the base to the structure or of wall and are designed to have a single critical section for


<!-- From Page 351 -->


## CODE

flexure and axial loads shall have longitudinal reinforcement at the ends of a vertical wall segment that satisfies (a) through (c):

(a) Longitudinal reinforcement ratio within $0.15\ell_w$ from the end of a vertical wall segment, and over a width equal to the wall thickness, shall be at least 6 bars.

(b) The longitudinal reinforcement required by 18.10.2.4(a) shall extend above and below the critical section at least the greater of $\ell_w$ and $M_u/3V_u$.

(c) No more than 50% of the reinforcement required by 18.10.2.4(a) shall be terminated at any one section.


<!-- From Page 352 -->


## CODE

**18.10.3** *Design forces*

**18.10.3.1** Design shear forces for horizontal wall segments, including coupling beams, shall be in accordance with 18.10.7.

**18.10.3.2** Design shear forces for wall piers shall be in accordance with 18.10.8.

**18.10.3.3** Design shear forces for parts of walls not covered by 18.10.3.1 or 18.10.3.2 shall be in accordance with the requirements of 18.10.3.3.1 through 18.10.3.3.5.


<!-- From Page 353 -->


## CODE

**18.10.3.3.4** If the general building code includes provisions to account for overstrength of the seismic-force-resisting system, it shall be permitted to take $\Omega_v$ equal to $\Omega_o$.

**18.10.3.3.5** $\Omega_o \omega_v = \Omega_o$, it shall be permitted to take $\Omega_v \omega_v$ as the redundancy factor not continued in the general building code equal to 1.0 for determination of $E_h$.

**18.10.4** *Shear strength*


<!-- From Page 354 -->


## CODE

**18.10.4.1** $V_n$ shall be calculated by:

$$V_n = (\alpha_c \lambda \sqrt{f'_c} + \rho_t f_y)A_{cv}$$ (18.10.4.1)

where

$\alpha_c = 3$ for $h_w/\ell_w \leq 1.5$

$\alpha_c = 2$ for $h_w/\ell_w \geq 2.0$

It shall be permitted to linearly interpolate the value of $\alpha_c$ between 3 and 2 for $1.5 < h_w/\ell_w < 2.0$. The value of $f'_c$ used in Eq. (18.10.4.1) and in 18.10.4.4 and 18.10.4.5 shall not exceed 12,000 psi.

**18.10.4.2** In 18.10.4.1, the value of ratio $h_w/\ell_w$ used to calculate $V_n$ for segments of a wall shall be the greater of the ratios for the entire wall and the segment of wall considered.

**18.10.4.3** Walls shall have distributed shear reinforcement in two orthogonal directions in the plane of the wall. If $h_w/\ell_w$ does not exceed 2.0, reinforcement ratio $\rho_\ell$ shall be at least the reinforcement ratio $\rho_t$.

**18.10.4.4** $V_n$ shall not be taken greater than the sum of $\alpha_{cpl}8\sqrt{f'_c}A_{cv}$ for all vertical wall segments sharing a common lateral force. For any one of the individual vertical wall segments, $V_n$ shall not be taken greater than $\alpha_{cpl}10\sqrt{f'_c}A_{cvs}$ where $A_{cvs}$ is the area of concrete section of the individual vertical wall segment considered. The term $\alpha_{cpl}$ is determined as

$$0.7\left(1 + \frac{(h_w + h_d)t_{cf}}{A_{cs}}\right)^2 \leq 1.2$$ (18.10.4.4)

where $h_d$ is determined according to 18.10.5.2 and $A_{cs}$ shall be taken as $A_{cw}$ or $A_{cvs}$ as applicable. The value of $\alpha_{cpl}$ need not be taken less than 1.0. It shall be permitted to take $\alpha_{cpl} =$ 1.0.


<!-- From Page 355 -->


## CODE

**18.10.4.5** For horizontal wall segments and coupling beams, $V_n$ shall not be taken greater than $10\sqrt{f'_c}A_{cv}$ where $A_{cv}$ is the area of concrete section of a horizontal wall segment or coupling beam.


<!-- From Page 356 -->


## CODE

**18.10.6.2** Walls or wall piers with $h_w/\ell_w \geq 2.0$ that are effectively continuous from the base to top of wall and designed to have a single critical section for flexure and axial loads shall satisfy (a) and (b):

(a) Special boundary elements are required at boundaries of the wall in accordance with 18.10.6.4 where the maximum extreme fiber compressive stress, corresponding to factored forces including earthquake effects, calculated for a linearly elastic, uncracked section in accordance with ASCE/SEI 7 Section 16.3.2, exceeds $0.2f'_c$.

(b) Where special boundary elements are required by (a) and correspond to the largest positive term related to earthquake effects, corresponding to factored forces calculated in accordance with ASCE/SEI 7 Section 16.3.2,

$$\frac{c}{\ell_w} = \frac{\delta_u}{h_w} \left(\frac{\ell_w}{600}\right) + \frac{1.5\ell_w}{h_w}$$ (18.10.6.2b)

and

The value of $\delta_u/h_w$ in Eq. (18.10.6.2b) need not be taken less than 0.015.


<!-- From Page 357 -->


## CODE

**18.10.6.3** Structural walls not designed in accordance with 18.10.6.2 shall have special boundary elements at boundaries of walls in accordance with 18.10.6.4 where the maximum extreme fiber compressive stress, corresponding to factored forces including earthquake effects, calculated for a linearly elastic, uncracked section in accordance with ASCE/SEI 7 Section 16.3.2, exceeds $0.2f'_c$. Stresses shall be calculated for the loadings, including patterns of loading, that result in maximum compressive stress at the boundary element. Good detailing practice is to arrange the reinforcement in such a manner that the special boundary elements can meet the cross-section properties. For walls with flanges, an effective flange width equal to the smaller of (i) the actual flange width and (ii) a width equal to 25% of the wall length shall be permitted to be discretized where the calculated compressive stress exceeds $0.2f'_c$. Stresses shall be calculated for the loading, including patterns of loading, that result in maximum compressive stress at the boundary element considered.

**18.10.6.4** If special boundary elements are required by 18.10.6.2 or 18.10.6.3, the following shall be satisfied:

(a) Boundary elements shall extend horizontally from the extreme compression fiber a distance not less than the greater of $c - 0.1\ell_w$ and $c/2$, where the neutral axis depth c refers to the value of c calculated for the factored axial force and nominal moment strength consistent with the displacement capacity associated with design displacement $\Delta$ according to 18.10.6.4(a). Where flanges are present, the boundary element shall extend a minimum of 12 in. into the web.

(b) The boundary element transverse reinforcement shall extend vertically from the critical section a distance not less than $\ell_w$; above the critical section where $\ell_w$ is the length of the boundary element that is parallel to the direction of loading.

(c) Boundary element transverse reinforcement shall extend vertically from the critical section in the direction of decreasing moment a height above and below the point of maximum flexure, $\ell_u$. At a height above the critical section, a nominal stress in the boundary element transverse reinforcement shall be provided by a seismic hook at a corner or offset a minimum of $\sqrt{3}h_{sx}$ from the face of the core of the confined zone perpendicular to the plane of the hook.

(d) Where the critical section occurs at the wall base, the boundary element transverse reinforcement shall extend into the supporting member at least the development length specified at 25.4.2.3. At the first row of transverse reinforcement in the boundary element shall extend above the wall base a height specified in (b).

(e) Where special boundary elements are required in 18.10.6.2 or 18.10.6.3 at wall edges, the tie, transverse reinforcement at $s_h$ shall extend into boundary elements $\ell_u$, at a higher lateral force, or at lap splices, unless a greater length is required by 25.7.2.5. The limits on spacing between transverse reinforcement and conforming to 18.10.6.4(a) The limit for the special boundary elements, where the special boundary elements at least 12 in. into the flexuring zone, or a pit cap, unless a greater length is required by 18.10.6.4. The provisions of the special boundary element transverse reinforcement is permitted to be discontinued where the calculated compressive stress is less than $0.15f'_c$. Where transverse reinforcement is reduced or discontinued.

develop $f_y$ in tension at the face of the confined core of the boundary web reinforcement, or the boundary element is considered within boundary web reinforcement, if shall be permitted to the horozontal web reinforcement to extend into confinement inside the boundary web reinforcement does not apply if the maximum extreme fiber compressive stress, corresponding to factored forces including earthquake effects, calculated for a linearly elastic section, does not exceed $0.15f'_c$ or shall at $\ell_y$ and $\ell_{yt}$ for the horozontal web reinforcement is not to be permitted


<!-- From Page 358 -->


## CODE

keep legs shall not exceed $h_x$ and adjacent hoops shall overlap.

(f) If the flexure, the maximum extreme fiber compressive stress is with a total minimum area of steel at least $0.6\sqrt{f'_c}/f_y$ (and if flanges at least $c_y$ is required for $f_c$ shall be detailed and reinforced in accordance with Table 18.10.6.4(a).

**Requirements for detailing and reinforcement for special boundary elements**

| Provision | Column of | || |
|---|---|---|---|---|
| $a_{sw}/A_g$ for design | Extent of boundary | $0.1\ell_w \geq c$ | (a) |  |
| | | $0.6\ell_c \geq c_y$ | (a,b) |  |
| | | $0.8\ell_c \geq \ell_w$ | (c,d) |  |
| $a_{sw}/A_g$ for axial and flexural strength and ductility | Concrete within the thickness of the floor system or horizontal diaphragm | Not special elements section and including that floor levels section a vertical spacing up to exceed 12 in. | (b) | Considering the 18.7.5.1 and 18.7.5.2 stressing for (a) in that section (b) in that section (c) below and above |
| (a) Concrete within a thickness of the floor system or horizontal diaphragm according to 18.7.5.1 and 18.7.5.2 is not necessary to be considered as part of the lateral system of the wall (see (c)).

(b) For a distance above and below the critical section height to be calculated to include 18.7.5.1 and 18.7.5.2 boundary elements to resist earthquake forces according to 18.7.5.1 and 18.7.5.2 along the horizontal dimension of the special boundary element shall have a vertical spacing not to exceed 12 in. Where members of other lateral members or above critical horizontal conditions are more than other end, with the intersection of members, all web reinforcement shall extend along the other end, with the intersection of the wall.

(c) Over the length or height along which the compression stress exceeds $0.15f'c$ from the base stress and a seismic hook at the other end, and at the boundary elements within $h_x$.

(d) Where the critical section occurs at the wall base, the boundary element shall extend into the wall and a hook at the other end, at a height higher than developed.

(e) At locations of load or higher than transverse reinforcement $\ell_y$ in tension at the face of the continued core of the boundary web reinforcement, or the boundary web reinforcement does not apply if the horizontal web reinforcement, it shall be extended to the horizontal web reinforcement, the special boundary elements corresponding to factored forces including earthquake effects calculated for a lateral elastic uncracked section does not apply if maximum extreme fiber compressive stress to at the horizontal web reinforcement $h_{sx}$ at $\ell_y$ and $\ell_{yt}$ for the horizontal web reinforcement, is to be developed by the horizontal web reinforcement does not have to be continuous at the boundary web reinforcement, if the maximum stress corresponding to factored forces including earthquake effects may to the boundary web reinforcement. It shall be permitted


<!-- From Page 359 -->


## CODE

to the horizontal web reinforcement to extend into the special boundary elements and be determined for $\ell_y$ or less along $h_x$ at (1) and (3).

(g) If a flange is provided within depth $c$ with a total compression force at least $0.6f_c$ shall be provided as per section $c_y$ or less in accordance with Table 18.10.6.4(a).

**Requirements for detailing and reinforcement for special boundary elements**

| Provision | Extent of special boundary elements | | |
|---|---|---|---|
| $a_{sh}/b_c$ for design | Greater of | $c-0.1\ell_w$ | (a) |
| | | $c/2$ |  |
| $\ell_w$ for axial strength and ductility | At least wall thickness or $h_x \geq 12$ in. the design concrete section and including that consideration in accordance 18.7.5.1 and 18.7.5.2 |  |  |
| Vertical extent elements | Above critical section | Wall pier | Wall |
| | Below critical section | $\ell_u$ |  |
| | Extending into foundation or support | Concrete $\ell_d$ per 25.4.2.3 | (d) |

(a) Concrete within the thickness of the floor system or horizontal diaphragm need not be considered as part of the special structural wall if 18.7.5.1 and 18.7.5.2 are satisfied in accordance with that section.

(b) For a distance above and below the critical section height, the horizontal dimension of the special boundary element shall be vertical spacing not to exceed 12 in. Where members framing horizontal boundaries are discontinued; the minimum lateral dimension of the special boundary element at the point of discontinuity shall be at least 12 in. unless a greater length is required by 18.7.5.2. Boundary elements shall extend into the diaphragm and hooked at the other end, at a height not less than that greater than the point of intersection with the other end, and extend along the diaphragm a distance to develop $f_y$ in tension.

(c) Over the height or length along which special boundary elements shall extend from the base critical section according to 21.2.3.2, the lower limit of 0.005 applies, and special boundary elements are required as long as the base sections according to 21.2.3.1 stress exceeds $0.15f'_c$ and below special boundary elements shall exceed 12 in.

(d) Where the critical section occurs at the wall base, the boundary elements shall extend into the support a sufficient length to develop $f_y$ in tension at the face of the support. If the special boundary element does not extend above the wall pier, the vertical length of boundaries elements above and below the boundary element shall extend into the support at least the distance required by 25.4.2.3 and upward from the top of the support a height not to exceed $\ell_y$.

(e) Transverse reinforcement in special boundary elements at wall piers shall be anchored to develop $f_y$ in tension at the face of the confined core of the special boundary element according to 25.4.2.3 and extend not less than $\ell_d$ below. Special boundary elements need to be discontinued where the special boundary element is enclosed by the horizontal web reinforcement. It shall be permitted for the horizontal web reinforcement to extend into the special boundary element and be detailed for $\ell_y$ and $\ell_{yt}$ at (1) and (3), respectively. If the maximum extreme fiber compressive stress corresponding to factored forces including earthquake effects calculated for a linearly elastic uncracked section is less than $0.15f'_c$, refer to (c) for locations where special boundary elements are required and (d) for required boundary elements according to 18.10.6.4(a).


<!-- From Page 360 -->


# CODE


<!-- From Page 361 -->


# CODE


<!-- From Page 362 -->


# CODE


<!-- From Page 363 -->


# CODE


<!-- From Page 364 -->


# CODE


<!-- From Page 365 -->


# CODE


<!-- From Page 366 -->


# CODE

Horizontal beam reinforcement at wall does not develop $f_y$


<!-- From Page 367 -->


# CODE

Horizontal beam reinforcement at wall does not develop $f_y$

Maximum spacing in accordance with Table 18.10.7.4

$A_{vd}$ = total area of reinforcement in each group of diagonal bars

**Note:**
For clarity, only part of the required reinforcement is shown on each side of the line of symmetry.

Wall boundary reinforcement


<!-- From Page 368 -->


# CODE

integrity of nonstructural components and their connections to the structure.

**18.10.7.3** Coupling beams not governed by 18.10.7.1 or 18.10.7.2 shall be reinforced in accordance with (a) or (b):

(a) Two intersecting groups of diagonally placed bars symmetrical about the midspan

(b) Longitudinal and transverse reinforcement satisfying (i) through (iii):

(i) 18.6.3 and 18.6.4, with the wall boundary interpreted as being a column.

(ii) Transverse reinforcement proportioned to satisfy the shear strength requirements of 18.6.5.

(iii) Spacing of transverse reinforcement not exceeding the limits in Table 18.10.7.4.

**18.10.7.4** Coupling beams reinforced with two intersecting groups of diagonally placed bars symmetrical about the midspan shall satisfy (a), (b), and either (c) or (d), and the requirements of 9.9 need not be satisfied:

(a) $V_n$ shall be calculated by

$$V_n = 2A_{vd}f_y\sin\alpha \leq 10\sqrt{f'_c}A_{cv} \quad (18.10.7.4)$$

where $\alpha$ is the angle between the diagonal bars and the longitudinal axis of the coupling beam.

(b) Each group of diagonal bars shall consist of a minimum of four bars provided in two or more layers.

(c) Each group of diagonal bars shall be enclosed by rectilinear transverse reinforcement having out-to-out dimensions of at least $b_w/2$ in the direction parallel to $b_w$ and $b_w/3$ along the other sides, where $b_w$ is the web width of the coupling beam. The transverse reinforcement shall be in accordance with 18.7.5.2(a) through (c) and shall provide lateral support to the diagonal reinforcement in accordance with 25.7.2.2 and 25.7.2.3. Reinforcement shall be arranged such that spacing of diagonal bars laterally supported by the corner of a crosstie or a hoop leg shall not exceed 14 in. around the perimeter of each group of diagonal bars, with $A_{sh}$ not less than the greater of (i) and (ii):

(i) $0.09s b_w \frac{f'_c}{f_{yt}}$

(ii) $0.3sb_w\left(\frac{A_g}{A_{ch}} - 1\right)\frac{f'_c}{f_{yt}}$

In calculating $A_g$ for each group of diagonal bars, the concrete cover in 20.5.1 shall be assumed on all four sides of each group of diagonal bars. The transverse reinforcement shall have spacing measured parallel to the diagonal bars satisfying 18.7.5.3(d) and not exceeding the limits in Table 18.10.7.4, and shall have spacing of crossties or legs of hoops measured perpendicular to the diagonal bars not exceeding 14 in. The transverse reinforcement shall continue through the intersection of the diagonal bars. At the intersec-


<!-- From Page 369 -->


# CODE

tion, it is permitted to modify the arrangement of the transverse reinforcement provided the spacing and volume ratio requirements are satisfied. Additional longitudinal and transverse reinforcement shall be distributed around the beam perimeter with total area in each direction of at least $0.002b_ws$ and spacing not exceeding 12 in.

(d) Transverse reinforcement shall be provided for the entire beam cross section in accordance with 18.7.5.2(a) through (c) with $A_{sh}$ not less than the greater of (i) and (ii):

(i) $0.09sb_w\frac{f'_c}{f_{yt}}$

(ii) $0.3sb_w\left(\frac{A_g}{A_{ch}} - 1\right)\frac{f'_c}{f_{yt}}$

Longitudinal spacing of transverse reinforcement shall not exceed the limits in Table 18.10.7.4. Spacing of crossties or legs of hoops both vertically and horizontally in the plane of the beam cross section shall not exceed 8 in. Each crosstie and each hoop leg shall engage a longitudinal bar of equal or greater diameter. It shall be permitted to configure hoops as specified in 18.6.4.3.

**Table 18.10.7.4—Maximum spacing of transverse reinforcement in coupling beams**

| Grade of diagonal or primary flexural reinforcement | Maximum spacing of transverse reinforcement<sup>(1)</sup> |
|-----------------------------------------------------|----------------------------------------------------------|
| 60 | Lesser of: | $6d_b$<br>6 in. |
| 80 | Lesser of: | $5d_b$<br>6 in. |
| 100 | Lesser of: | $4d_b$<br>6 in. |

<sup>(1)</sup>$d_b$ is the diameter of the smallest diagonal bar or primary flexural reinforcing bar.

**18.10.7.5** Design shear force $V_e$ of coupling beams shall be permitted to be redistributed to coupling beams at adjacent floor levels provided (a) through (d) are satisfied:

(a) Coupling beams sharing redistributed forces shall be vertically aligned within a special structural wall.

(b) Coupling beams sharing redistributed forces shall have $\ell_n/h \geq 2$.

(c) The maximum redistribution of $V_e$ from any beam shall not exceed 20% of the value determined from analysis.

(d) The sum of $\phi V_n$ of coupling beams sharing redistributed demands shall be equal to or greater than the sum of $V_e$ in those beams.


<!-- From Page 370 -->


# CODE


<!-- From Page 371 -->


# CODE

**18.10.8** *Wall piers*


<!-- From Page 372 -->


<!-- Page 372 -->

This page appears to be blank or contains only minimal content. Based on the image provided, there is no visible text content to transcribe from page 372.

---

*372        ACI CODE-318-25: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY*

American Concrete Institute – Copyrighted © Material – www.concrete.org
Licensee=University of Texas Revised Sub Account|5620001114, User=Chen, Chang-Jui
Not for Resale, 03/28/2025 08:01:15 MDT


<!-- From Page 373 -->


## CODE

**18.10.8.1** Wall piers shall satisfy the special moment frame requirements for columns of 18.7.4, 18.7.5, and 18.7.6, with joint faces taken as the top and bottom of the clear height of the wall pier. Alternatively, wall piers with $(\ell_w/h_w) > 2.5$ shall satisfy (a) through (f):

(a) Design shear force shall be calculated in accordance with 18.7.6.1 with joint faces taken as the top and bottom of the clear height of the wall pier. If the general building code includes provisions to account for overstrength of the seismic-force-resisting system, the design shear force need not exceed $\Omega$ times the factored shear calculated by analysis of the structure for earthquake load effects.

(b) $V_n$ and distributed shear reinforcement shall satisfy 18.10.4.

(c) Transverse reinforcement shall be hoops except it shall be permitted to use single-leg horizontal reinforcement parallel to $\ell_w$ where only one curtain of distributed shear reinforcement is provided. Single-leg horizontal reinforcement shall have 180-degree bends at each end that engage wall pier boundary longitudinal reinforcement.

(d) Vertical spacing of transverse reinforcement shall not exceed 6 in.

(e) Transverse reinforcement shall extend at least 12 in. above and below the clear height of the wall pier.

(f) Special boundary elements shall be provided if required by 18.10.6.3.

**18.10.8.2** For wall piers at the edge of a wall, horizontal reinforcement shall be provided in adjacent wall segments above and below the wall pier and be designed to transfer the design shear force from the wall pier into the adjacent wall segments.

## **18.10.9** *Ductile coupled walls*

**18.10.9.1** Ductile coupled walls shall satisfy the requirements of this section.

**18.10.9.2** Individual walls shall satisfy $h_{nw}/\ell_w \geq 2$ and the applicable provisions of 18.10 for special structural walls.

**18.10.9.3** Coupling beams shall satisfy 18.10.7 and (a) through (c) in the direction considered.

(a) Coupling beams shall have $\ell_n/h \geq 2$ at all levels of the building.

(b) All coupling beams at a floor level shall have $\ell_n/h \leq 5$ in at least 90% of the levels of the building.


<!-- From Page 374 -->


## CODE

(c) The requirements of 18.10.2.5 shall be satisfied at both ends of all coupling beams.

## **18.10.10** *Construction joints*

**18.10.10.1** Construction joints in structural walls shall be specified according to 26.5.6, and contact surfaces shall be roughened consistent with condition (b) of Table 22.9.4.2.

## **18.10.11** *Discontinuous walls*

**18.10.11.1** Columns supporting discontinuous structural walls shall be reinforced in accordance with 18.7.5.6.

## **18.11—Special structural walls constructed using precast concrete**

**18.11.1** *Scope*

**18.11.1.1** This section shall apply to special structural walls constructed using precast concrete forming part of the seismic-force-resisting system.

## **18.11.2** *General*

**18.11.2.1** Special structural walls constructed using precast concrete shall satisfy 18.10 and 18.5.2, except 18.10.2.4 shall not apply for precast walls where deformation demands are concentrated at the panel joints.

**18.11.2.2** Special structural walls constructed using precast concrete and unbonded post-tensioning tendons and not satisfying the requirements of 18.11.2.1 are permitted provided they satisfy the requirements of ACI CODE-550.6.

## **18.12—Diaphragms and trusses**

**18.12.1** *Scope*


<!-- From Page 375 -->


## CODE

**18.12.1.1** This section shall apply to diaphragms and collectors forming part of the seismic-force-resisting system in structures assigned to SDC D, E, or F and to SDC C if 18.12.1.2 applies.

**18.12.1.2** Section 18.12.11 shall apply to diaphragms constructed using precast concrete members and forming part of the seismic-force-resisting system for structures assigned to SDC C, D, E, or F.

**18.12.1.3** Section 18.12.12 shall apply to structural trusses forming part of the seismic-force-resisting system in structures assigned to SDC D, E, or F.

## **18.12.2** *Design forces*

**18.12.2.1** The earthquake design forces for diaphragms shall be obtained from the general building code using the applicable provisions and load combinations.


<!-- From Page 376 -->


## CODE

## **18.12.3** *Seismic load path*

**18.12.3.1** All diaphragms and their connections shall be designed and detailed to provide for transfer of forces to collector elements and to the vertical elements of the seismic-force-resisting system.

**18.12.3.2** Elements of a structural diaphragm system that are used primarily to span between and used to transfer diaphragm shear or flexural forces around openings or other discontinuities shall satisfy the requirements for collectors in 18.12.7.6 and 18.12.7.7.


<!-- From Page 377 -->


## CODE

## **18.12.4** *Cast-in-place noncomposite topping slab diaphragms*

**18.12.4.1** A cast-in-place noncomposite topping slab diaphragm shall be permitted as a structural diaphragm if (a) and (b) are satisfied and the slab surface on which the topping slab is placed is clean, free of laitance, and roughened.

(a) $h \geq 2$ in.

(b) $h \geq \ell_u/180$ for topping slabs placed over floor or roof elements, or for cast-in-place slabs placed over floor or roof systems with precast elements. The precast floor or roof system must provide concrete or permanent composite topping slabs placed over floor or roof elements in accordance with 18.12.1 (pre-1963), except for structural diaphragms designed on a strength basis.

## **18.12.5** *Cast-in-place noncomposite topping slab*

**18.12.5.1** A cast-in-place noncomposite topping slab diaphragm forming part of the seismic-force-resisting system in a floor or roof system shall be permitted as a structural diaphragm in structures assigned to SDC D, E, or F if (a) through (c) are satisfied and the slab surface on which the topping slab is placed is clean, free of laitance, and roughened.

(a) $h \geq 2\frac{1}{2}$ in.

(b) Concrete slabs and composite topping slabs placed on steel decking shall be designed in accordance with 18.7. Except for post-tensioned slabs, reinforcement for flexural strength need not be confined, nor is it required to be placed on or within elements or on composite steel deck where topping slab is placed on composite steel deck with the precast elements to resist the design shear; and

(c) The requirements of 18.12.2.3 shall be satisfied.

## **18.12.6** *Minimum thickness of diaphragms*

**18.12.6.1** Concrete slabs and composite topping slabs forming part of the seismic-force-resisting system in a floor or roof system for a building assigned to SDC D, E, or F shall be at least 2 in. thick, and shall be reinforced with distributed transverse reinforcement spaced at no more than 3 times the slab thickness at each face, with at least one curtain of reinforcement.

**18.12.7** *Reinforcement*

**18.12.7.1** Reinforcement provided for diaphragm shall be in conformance with 18.7. Except for post-tensioned slabs, reinforcement for flexural strength need not be confined, nor is it required to be placed on or within elements placed at their ends, nor does other topping slab placed on precast floor elements need to be provided for shear strength shall be continuous and shall be distributed uniformly across the depth.

**18.12.7.2** Bonded tendons used as reinforcement to resist design moments in accordance with post-tensioning. For each strength analysis shall be in conformance with 18.7, except that if one post-tensioned slab is placed parallel to design and two perpendicular to the design, the requirements would apply to those perpendicular tendons that do not exceed 0.0000 psi. Decompression from unbonded tendons should not exceed these requirements and shall be satisfied.


<!-- From Page 379 -->


# ACI CODE–319-19: BUILDING CODE FOR STRUCTURAL CONCRETE—CODE REQUIREMENTS AND COMMENTARY

## LEFT COLUMN

18.12.7.3 All reinforcement used to resist collector forces, for eccentric shear, or flexural tension shall be developed or spliced for $f_y$ in tension.

18.12.7.4 Class $C$ or Class $S$ mechanical splices are regarded where mechanical splices are used in the plastic hinge region. Mechanical splices should be placed in elements of the seismic-force-resisting system.

18.12.7.5 Longitudinal reinforcement for collectors shall not exceed the maximum steel ratio permitted by the average tensile length ratio over the average length of the collectors, except that where the value of $l_n$ to $h$ is less than 6, anywhere the value of $l_n$ to $h$ is less than 6, anywhere the value of $l_n$ to $h$ are considered where in vertical collector begins shall be considered where the vertical element has the vertical element has the vertical collector begins.

18.12.7.6 Collector elements with compressive stresses greater than $0.2f'_c$ at the vertical element connection to the diaphragm or where the compressive stress of those points equals or exceeds the spacing limits of 18.7.3 (a) shall be confined at the connections to the diaphragm by special moment frame boundary elements or by special structural wall boundary elements that satisfy 18.10.6.4. Where such confinement cannot be achieved due to potential discontinuity of a section where the calculated compressive strains on the cross-section in the hoop direction are a minimum.

18.12.7.7 Collector elements are permitted to be governed by the horizontal reinforcement requirements based on the overlength of the vertical elements of the seismic-force-resisting system, the limits of $l_w$ to $h$ shall be permitted to be taken as the average for all vertical components of the seismic-force-resisting system.

### Table 18.12.7a—Transverse reinforcement for collector reinforcement

| Confinement reinforcement | Applicable expression |
|---------------------------|----------------------|
| $ρ_{st}$ for spiral or circular reinforcement | $0.45\left(\frac{A_g}{A_{ch}} - 1\right)\frac{f'_c}{f_{yh}}$ | (a)
| $ρ_s$ for rectilinear reinforcement | Greater of | (b)

18.12.7.7 Longitudinal reinforcement detailing for collector elements at splices and anchorage zones shall meet 18.6.5 and 18.7.4.

## RIGHT COLUMN

### R18.12.7.3 COMMENTARY

R18.12.7.3 For ductility when forces on the designed collector element exceed nominal strength at connections or reinforcement in diaphragm or splice length is increased, development of splice length for the collector reinforcement should also be reduced.

R18.12.7.4 Although the $f_y$ factor is to be applied to the design flexural reinforcement by the connection between the collector elements and the vertical elements of the seismic-force-resisting system, significant yielding or reinforcement at the connection may occur due to cyclic displacements, such that it is likely to exceed the calculated design values after consideration has been given for the effects of inelastic deformations, plastic hinges should be considered over several stories, when yielding by integration over different levels of reinforcement along the height is considered over different reinforcement over several stories.

R18.12.7.5 Table 20.12.2.2(a) permits the maximum design longitudinal reinforcement for flexural members at a collector for example, at not over critical sections. The average stress at the collector is limited to control diaphragm cracking similar to beams. For small aspect ratios of length-to-depth, the moment capacity at $l_n$ to $h$ less than 6 may have the capacity of the collector is designed for $f_y$ high/moderate and should be reinforced using reinforcement ratio to develop.

R18.12.7.6 In documents such as the NEHRP Provi­sions (FEMA 750), ATC-76-02 and -76-03, TBI-17, and the ASCE 7-16 seismic design provisions, collector elements of diaphragms are designed for forces amplified by a factor $Ω_o$ to account for the overstrength in the vertical elements that the diaphragm is coupled to. To be consistent with the design, provision 18.12.7.6 includes confinement for collector forces, depending on the document selected and on the type of seismic-force-resisting system. In some documents, the same special moment frame boundary or special structural wall $Ω_o$ is specified by the elements of the vertical seismic-force-resisting system.

R18.12.7.6 is intended to reflect that special forces are typically loaded based on gross section of the structural diaphragm, even at all levels within other documents, whether or not the diaphragm is pre-qualified to cross section. The force is also design to develop an ultimate limit state in design strength at all limits to be assumed to indicate that integrity of the entire structure depends to a fair which relies upon such cross section to meet the reinforcement requirements based on the seismic force controls reinforcement is required at each location to provide the reinforcement for the flexure and the reinforcement.

R18.12.7.7 This section is intended to reduce the possi­bility of the buckling and provide adequate bar development where collectors are attached with lap splices.


<!-- From Page 380 -->


## CODE

**18.12.9.1** $V_n$ of diaphragms shall not exceed:

$$V_n = A_{cv}(2\lambda\sqrt{f'_c} + \rho_t f_y)$$
(18.12.9.1)

For cast-in-place topping slab diaphragms on precast floor or roof members, $A_{cv}$ shall be calculated using only the thickness of topping slab for noncomposite topping slab diaphragms and the combined thickness of cast-in-place and precast elements for composite topping slab diaphragms. For composite topping slab diaphragms, the value of $f_c'$ used to calculate $V_n$ shall not exceed the lesser of $f_c'$ for the precast members and $f_c'$ for the topping slab.

**18.12.9.2** $V_n$ of diaphragms shall not exceed $8\sqrt{f'_c}A_{cv}$.

**18.12.9.3** Above joints between precast elements in noncomposite and composite cast-in-place topping slab diaphragms, $V_n$ shall not exceed:

$$V_n = A_{vf}f_y\mu$$
(18.12.9.3)

where $A_{vf}$ is the total area of shear friction reinforcement within the topping slab, including both distributed and boundary reinforcement, that is oriented perpendicular to joints in the precast system and coefficient of friction, $\mu$, is 1.0λ, where λ is given in 19.2.4. At least one-half of $A_{vf}$ shall be uniformly distributed along the length of the potential shear plane. The area of distributed reinforcement in the topping slab shall satisfy 24.4.3.2 in each direction.

**18.12.9.4** Above joints between precast elements in noncomposite and composite cast-in-place topping slab diaphragms, $V_n$ shall not exceed the limits in 22.9.4.4, where $A_c$ is calculated using only the thickness of the topping slab.


<!-- From Page 381 -->


## CODE

### 18.12.10 *Construction joints*

**18.12.10.1** Construction joints in diaphragms shall be specified according to 26.5.6, and contact surfaces shall be roughened consistent with condition (b) of Table 22.9.4.2.

### 18.12.11 *Precast concrete diaphragms*

**18.12.11.1** Diaphragms and collectors constructed using precast concrete members with composite topping slab and not satisfying 18.12.4, and untopped precast concrete diaphragms, are permitted provided they satisfy the requirements of ACI CODE-550.5. Cast-in-place noncomposite topping slab diaphragms shall satisfy 18.12.5 and 18.12.6.

**18.12.11.2** Connections and reinforcement at joints used in the construction of precast concrete diaphragms satisfying 18.12.11.1 shall have been tested in accordance with ACI CODE-550.4.

**18.12.11.3** Extrapolation of data on connections and reinforcement at joints used to project details that result in larger construction tolerances than those used to qualify connections in accordance with ACI CODE-550.4 shall not be permitted.

### 18.12.12 *Structural trusses*

**18.12.12.1** Structural truss elements with compressive stresses exceeding $0.2f_c'$ at any section shall have transverse reinforcement, in accordance with 18.7.5.2, 18.7.5.3, 18.7.5.7, and Table 18.12.12.1, over the length of the element.


<!-- From Page 382 -->


## CODE

**Table 18.12.12.1—Transverse reinforcement for structural trusses**

| Transverse reinforcement | Applicable expressions |  |
|---|---|---|
| $A_{sh}s/b_c$ for rectilinear hoop | Greater of: | $0.3\left(\frac{f'_c}{A_g} - 1\right)\frac{f'_c}{f_{yt}}$ | (a) |
|  |  | $0.09\frac{f'_c}{f_{yt}}$ | (b) |
| $\rho_s$ for spiral or circular hoop | Greater of: | $0.45\left(\frac{A_g}{A_c} - 1\right)\frac{f'_c}{f_{yt}}$ | (c) |
|  |  | $0.12\frac{f'_c}{f_{yt}}$ | (d) |

**18.12.12.2** All continuous reinforcement in structural truss elements shall be developed or spliced for $f_y$ in tension.

### 18.13—Foundations
**18.13.1** *Scope*

**18.13.1.1** This section shall apply to foundations resisting earthquake-induced forces or transferring earthquake-induced forces between structure and ground.

**18.13.1.2** The provisions in this section for piles, drilled piers, caissons, and slabs-on-ground shall supplement other applicable Code design and construction criteria, including 1.4.7 and 1.4.8.

### 18.13.2 *Footings, foundation mats, and pile caps*

**18.13.2.1** The provisions of this section shall apply to structures assigned to SDC D, E, or F.

**18.13.2.2** Longitudinal reinforcement of columns and structural walls resisting forces induced by earthquake effects shall extend into the footing, mat, or pile cap, and shall develop $f_y$ in tension at the interface.

**18.13.2.3** Columns designed assuming fixed-end conditions at the foundation shall comply with 18.13.2.2 and, if hooks are required, longitudinal reinforcement resisting flexure shall have 90-degree hooks near the bottom of the


<!-- From Page 383 -->


## CODE

foundation with the flexural reinforcement extended inward the center axis.

**18.13.2.4** Columns or boundary elements of special structural walls shall extend into the footing, mat, or pile cap, and shall be provided with transverse reinforcement in accordance with 18.7.5.2 through 18.7.5.4 or provided below the top of the footing. This reinforcement shall extend into the column or boundary element at least the development length $\ell_d$ of the largest longitudinal bar in the column or boundary element longitudinal reinforcement.

**18.13.2.5** Ties or spirals shall extend into columns or boundary elements of special structural walls at, or columns, for at least the development length $\ell_d$ provided in 25.4 or 25.6 but need not exceed the length of the lap of the doweled or extended-load combinations, and shall be at least that required in 18.7.5.2 through 18.13.1.4 as well.

**18.13.2.6** Tie or spiral-confining transverse reinforcement walls shall be in accordance with 18.13.2.4.

**18.13.2.7** For structures assigned to SDC D, E, or F, grade designed to resist the full compressive strength of the footing beams below shall be confined in accordance with both (a) and (b):

(a) Transverse reinforcement satisfying 18.7.5.2 through 18.7.5.4 shall be provided within a distance $\ell_n$ of each face of a joint is not less capable of providing lateral support, or at all top of walls.

(b)18.13.2.4 Grade beams and slabs-on-ground

### 18.13.3 *Grade beams and slabs-on-ground*

**18.13.3.1** For structures assigned to SDC D, E, or F, grade beams and beams that are part of a mat foundation selected to resist forces resulting from earthquake effects, or the structural system shall be in accordance with 18.4.6.

**18.13.3.2** For structures assigned to SDC D, E, or F, slab-on-ground that resist or plane earthquakes forces from columns or structural walls shall be uniformly reinforced in two directions. Reinforcement shall be continuous and anchored to develop $f_y$ in tension at all sections. Openings in the slab-on-ground in a structural wall shall clearly indicate the slabs-on-ground is a structural diaphragm or acts as a flexural supporting system.

### 18.13.4 *Foundation systems tie*

**18.13.4.1** For structures assigned to SDC C, D, E, or F, individual pile caps, piers, or caissons shall be interconnected by ties in accordance with 18.13.4.2, unless it can be


<!-- From Page 384 -->


## CODE

shown it can be demonstrated that equivalent restraint is provided otherwise.

**18.13.4.2** For structures assigned to SDC D, E, or F, individual pile caps, piers, or caissons shall be interconnected by ties in accordance with (a) or (b) if not interconnected by beams, slabs, or mats that satisfy 18.13.3.2 and seismic ties.

**18.13.4.3** Where required, foundation seismic ties shall satisfy (a), (b), and (c):

(a) At least two orthogonal ties shall connect each column, edge column, to slab(s) or beam(s) where required equal to 0.5 times the greater of the pile cap or column factored axial dead load from factored axial dead plus factored live loads in tension unless a greater value is required by (b), (c), or (d).
(b) Foundation elements below the slabs-on-ground or below the top of a mat shall satisfy tie requirements in (a) reinforced by component rock, load collector walls, foundation elements and mat members.

Proportioning and detailing foundation in including collector.

**18.13.4.4** For structures assigned to SDC D, E or F, grade beams assigned in a tied on a horizontal foundation mat system shall follow the column flexural in buildings assigned dead reinforcement that shall be developed within or beyond the supported column or structural within the pile cap or caisson, or pile cap should be interconnected other than in (a) Confine tie ties shall follow the seismic inter-column direction of the grade beam shall be at least equal to the clear spacing between contained at a spacing not to exceed the larger of 8d, times the smallest orthogonal cross-sectional dimension and 12 in.

### 18.13.5 *Deep foundations*

**18.13.5.1** This section shall apply to the following types of deep foundations:

(a) Piles or caissons constructed on-applied piles
(b) Metal cased concrete piles
(c) Partially filled or partially concrete piles
(d) Uncased, cast-in-place piles

**18.13.5.2** For structures assigned to SDC C, D, E, or F, piles, piers, or caissons resisting tensile loads shall have the design tensile strength shall be accordance with that evaluated by appropriate design tension forces.

**18.13.5.3** For structures assigned to SDC C, D, E, or F, the maximum longitudinal and transverse reinforcement shall be in accordance with 18.13.5.7 to develop the full pile, pier, or caisson capacity.


<!-- From Page 385 -->


## CODE

over the entire unsupported length for the portion of deep foundations within the top 30 ft of soil and that is not restrained against buckling throughout this length.

**18.13.5.4** For structures assigned to SDC C, D, E, or F, hoops, spirals, and ties in deep foundation members shall be members with hoops or spirals.

**18.13.5.5** For structures assigned to SDC C, D, E, or F, hooked in line Code 18, if concrete deep foundation members shall have transverse reinforcement in accordance with (a) and (b) longitudinal reinforcement in the top and bottom portion within diameters above and below the interfaces between members with the embedment portion and free member portions per pile (18.7.5.2.

**18.13.5.6** For structures assigned to SDC D, E, or F in buildings with pile caps, piers, or caissons extend minimum construction, concrete piles, pier or caissons, and foundation elements except from the foundation into grade beams at intermediate levels than the footing shall be provided with ties unless confined with hoops or spirals.

**18.13.5.7** *Uncased cast-in-place drilled or augered concrete piles or piers*

**18.13.5.7.1** For structures assigned to SDC C, D, E, or F, reinforcement shall be provided in uncased cast-in-place drilled or augered concrete piles or piers per (a) through (d) and in accordance with the requirements in Table 18.13.5.7.1.


<!-- From Page 386 -->


## CODE

(a) Longitudinal reinforcement shall extend from the top of pile or pier to a depth below the interface sufficient to develop the reinforcement in accordance with Chapter 25.

(b) For structures assigned to SDC C, transverse reinforcement shall satisfy (i) and (ii):

(i) Spiral or circular hoops shall be provided in accordance with 18.7.5.4 for a distance from the underside of the cap to at least three pile diameters below the pile cap or grade beam and a minimum of four pile diameters below the bottom of the footing, pile cap, or grade beam.

(ii) Spacing of transverse reinforcement satisfying 18.7.5.4 shall not exceed 12 in.

(c) For structures assigned to SDC D or E, transverse reinforcement shall satisfy (i) and (ii):

(i) Spiral or circular hoops shall be provided in accordance with 18.7.5.4 from the underside of the cap to at least five pile diameters below the pile cap or grade beam and a minimum of five pile diameters below the bottom of the footing, pile cap, or grade beam, and throughout the full length over which the design shear force exceeds $\phi V_c$ calculated in accordance with 22.5. For locations where the design shear force exceeds $\phi V_c$, spiral or circular hoops shall be provided to the limits specified in Table 18.13.5.7.1. In all cases, spiral or circular hoops shall extend from the bottom of the footing, pile cap, or grade beam to a depth where the design moment is less than the cracking moment.

(ii) Spacing of spiral or circular hoops shall not exceed the least of 6 in., 6 times the diameter of the smallest longitudinal reinforcement, and one-half the least cross-sectional pile diameter for the full length specified in (i).

(d) For structures assigned to SDC F, transverse reinforcement shall satisfy (i) and (ii):

(i) Confinement reinforcement consisting of spiral or circular hoops shall be provided in accordance with 18.7.5.4 throughout the length of the pile.

(ii) Spacing of confinement reinforcement shall satisfy 18.7.5.3.


<!-- From Page 387 -->


## CODE

**Table 18.13.5.7.1—Transverse reinforcement for uncased cast-in-place or augered concrete piles or piers**

| | SDC C | SDC D and E | SDC F |
|---|---|---|---|
| Minimum longitudinal reinforcement ratio | $0.005A_g$ | Minimum reinforcement of $0.01A_g$ if the gross area of the pile or pier, as applicable | Minimum reinforcement of $0.01A_g$ if the gross area of the pile or pier, as applicable |
| | Greater of: Length of six through pile or (ii) 5 ft lengths of the pile cap or grade beam | Greater of: Length of six through pile or (ii) 5 ft lengths of the pile cap or grade beam | Full length of pile except in accordance with (18.13.5.7) |
| Minimum reinforced pile length | (i) Percent length of pile extending below the pile cap or grade beam | (ii) Percent length of pile - distance in accordance with (c)(i) of 18.13.5.7 | |
| Spacing of transverse reinforcement zone | 12 in. | Least of (i) 6 in., (ii) six times the diameter of the smallest longitudinal reinforcement (iii) One half the least dimension of the pile cap | |
| Maximum spacing of transverse confinement | Provide transverse reinforcement | | Throughout pile cross section diameter times (6) in. |
| | | | Minimum less 8 times the diameter spiral bar pins length of six pile diameters below the top of the pile cap or minimum eight pile diameters below beam of pile cap or grade beam |
| Limits on location of transverse confinement | (a) N/A | Closed hoop at specific with 18.7.5.4 | Less than where the requirement of 18.13.5.7 (c) Class 3.9 and 5.8 meet in 18.13.5.7(ii) |
| Type of transverse reinforcement and spacing shall be provided for the reinforced pile length | Closed hoop or spirals with 18.7.5.4 | Less than where the requirement of Tables 18.13.5.7 (c) Class 1.9 and less 1.9 dia. distance - 3 in. diameter | Less than where the requirement of Tables 18.13.5.7 Class (c) 3.9 and 5.8 meet in 18.13.5.7(ii) |
| | Spacing and diameter limit on spirals or hoops | Maximum spacing of 12 in. is permitted beyond the confined zone | Spacing shall not exceed the least of six through (c) Maximum - 3 in. diameter |

*If the pile undergoes calculated as slow and it early reinforcement shall be permitted to be increased a length above the pile cap to the lesser of percent of the pile length and 7 ft. but the required pile minimum below the requirements of this table shall be reduced to minimum transverse where the foundation element factor is designed to withstand minimum reinforcement above then. For the portions of the pile cap pile percent 50 percent transverse reinforcement length confinement and below the allowable load. Spacing in this instance applies if you want it. More force if you are extending below pile or above hoops in the foundation then the minimum. Maximum reinforced length and not to be less than the requirements for SDC D, E and F less Class D.*

**18.13.5.7.2** Splices of longitudinal and transverse reinforcement shall be provided along minimum reinforced length of the pile or pier in accordance with 18.2.7 and 25.5.7.1.

**18.13.5.7.3** Longitudinal reinforcement shall extend at least one development length, calculated for $f_y$ in tension, from the bottom of the pile cap, grade beam, or mat, as given in Table 18.13.5.7.1 as the distance from the bottom of the pile, pile cap, grade beam, or mat, to $\ell_d$.

### 18.13.5.8 *Metal-cased concrete piles*

**18.13.5.8.1** For structures assigned to SDC C, D, E, or F, metal-cased concrete piles shall have minimum reinforced longitudinal reinforcement lengths for metal-cased concrete piles shall be the greater of, or uncased concrete piles in 18.13.5.7.

**18.13.5.8.2** Metal-cased concrete piles shall have a spiralwelded metal casing of a thickness not less than 0.075 in.


<!-- From Page 388 -->


## CODE

(No. 14 gauge) that is adequately protected from possible deleterious action due to soil conditions, dropping over excavation support, or similar concerns by having records of soil conditions.

### 18.13.5.9 *Precast concrete piles*

**18.13.5.9.1** For structures assigned to SDC C, D, E, or F, the provisions for precast should have longitudinal reinforcement ratio of 0.01 and shall have transverse reinforcement in accordance with a minimum length inside the pile capped to two times the pile or the pile capped to pile two times the pile cap to be provided reinforcement bars should be confined within 6 in. of the reinforcement

### 18.13.5.10 *Precast concrete piles*

**18.13.5.10.1** For precast concrete driven piles, the length of shear force reinforcement provided shall be within at least six pile diameters up to 20 percent of the total driven pile.

**18.13.5.10.2** Precast nonprestressed concrete piles, for SDC, C, D, E, or F reinforcement force shall through (a) and (b):

(a) Longitudinal reinforcement shall be enclosed within a transverse reinforcement spiral of SDC F, shall extend from top to 20 in. diameter piles, and No. 4 closed ties or 1/2 in. diameter spirals, for larger diameter piles.

(b) Where at least one-third of the pile length is embedded in the soil so that the pile will be laterally restrained throughout this length from the bottom of the pile cap shall not exceed the lesser of 8 times the diameter of the smallest longitudinal bar and 6 in.

(d) Transverse reinforcement shall be provided throughout the length of the pile at a spacing not exceeding 8 in.

**18.13.5.10.3** For structures assigned to SDC D, E, or F, precast nonprestressed concrete piles shall satisfy the requirements of 18.7.5.2, 18.7.5.3, 18.7.5.7, and Table 18.12.12.1 throughout the length of the pile.

**18.13.5.10.4** For precast concrete piles in SDC D, E, or F in Table 18.13.5.7.1.

**18.13.5.10.4** For structures assigned to SDC C, precast prestressed concrete piles shall satisfy (a) and (b):

(a) The effective confinement consists of spirals or closed ties satisfying (i) and (ii) of at least 0.007 in the transverse reinforcement, $s_c$, to the upper 20 ft shall not be less than that


<!-- From Page 389 -->


## CODE

calculated by Eq. (18.13.5.10.4a) or calculated from a spiral reinforced analysis by Eq. (18.13.5.10.4b)

$$0.45\left(\frac{f'_c}{f_y}\right)$$
(18.13.5.10.4a)

$$0.04\left[\left(\frac{f'_c}{f_y}\right)\left(e^{-3.95} + \frac{3M_u}{P_u D}\right)\right]$$
(18.13.5.10.4b)

and $s_c$ shall not be taken as greater than 100,000 psi.

(b) A minimum of one-half of the volumetric ratio of spiral reinforcement required by Eq. (18.13.5.10.4a) or calculated from a spiral reinforced analysis by Eq. (18.13.5.10.4b) shall be provided for the remainder of the length of the pile.

**18.13.5.10.5** For structures assigned to SDC D, E, or F, precast prestressed concrete piles shall satisfy (a) through (g) and the ductile pile region shall be detailed as the length of pile measured from the bottom of the pile cap to the point of zero curvature, assumed at one-half of the pile length not less than 8 ft. If the total pile length to the end of 35 ft in the soil, this portion shall be taken as the entire pile length.

(a) The effective confinement consists of spirals or closed ties satisfying (i) and (ii) of at least 0.012 in the transverse reinforcement shall not exceed the least of 2 in. and 4 times the diameter of the smallest longitudinal bar.

(b) Spiral reinforcement shall be spliced by lapping one full turn by welding, or by the use of a mechanical splice satisfying 25.5.7.1. Lap splices or welded splices for deformed bars shall satisfy 25.5 and mechanical connections of deformed bars shall comply with 25.5.7.

(c) If the transverse confinement consists of spirals, at the bottom of the pile cap, grade beam, or mat, the transverse reinforcement, $s_c$, in the ductile pile region shall not be less than that calculated by Eq. (18.13.5.10.5a) or calculated from a spiral reinforced analysis by Eq. (18.13.5.10.5b), and the required volumetric ratio shall be permitted to be obtained by providing an inner and outer spiral

$$0.5\left(\frac{f'_c}{f_y}\right)$$
(18.13.5.10.5a)

$$0.016\left[\left(\frac{f'_c}{f_y}\right)\left(e^{-3.95} + \frac{3M_u}{P_u D}\right)\right]$$
(18.13.5.10.5b)

and $s_c$ shall not be taken as greater than 100,000 psi.

(d) Outside of the ductile region, spiral confinement reinforcement shall be provided with a volumetric ratio not less than one-half of that required within the ductile pile region. Spiral spacing shall be at least 3 in. in the ductile region and shall comply with Table 18.13.5.7.1 outside.

(e) If transverse confinement consists of rectangular closed ties, the cross-sectional area of transverse reinforcement in accordance with the area per leg of rectangular closed ties shall be at least 0.25 times the greater of Eq. (18.13.5.10.5c) and Eq. (18.13.5.10.5d). The hoops and crossties shall be equivalents in accordance


<!-- From Page 390 -->


## CODE

bars not less than No. 3 in size, and rectangular hoop ends shall terminate with seismic hooks.

$$A_{sh} = 0.3A_{ch}\left(\frac{f'_c}{f_{yt}}\right)\left(\frac{A_g}{A_{ch}} - 1\right)\left(e^{-0.5} + \frac{3M_u}{P_u D}\right)$$
(18.13.5.10.5c)

$$A_{sh} = 0.12s h_c\left(\frac{f'_c}{f_{yt}}\right)\left(e^{-0.5} + \frac{3M_u}{P_u D}\right)$$
(18.13.5.10.5d)

and $s_c$ shall not be taken as greater than 100,000 psi.

**18.13.5.10.6** For structures assigned to SDC D, E, or F, the maximum factored axial load that can be applied to precast prestressed piles shall be the product of a combination of factored axial dead load and live load in accordance with the following values:

(a) 0.35P $f'_cA_g$ for square piles with side dimension of 14 in. or less

(b) 0.4P $f'_cA_g$ for square piles with side dimension greater than 14 in.

(c) 0.4P $f'_cA_g$ for circular or octagonal piles greater than 16 in. diameter

(d) 0.5P $f'_cA_g$ for circular or octagonal piles greater than 24 in. diameter

### 18.13.6 *Anchorage of piles, piers, and caissons*

**18.13.6.1** For structures assigned to SDC C, D, E, or F, piles shall be extended into the pile cap or mat foundation resisting tension loads shall be detailed to transfer tension forces to piles within the pile cap or mat foundation elements.

**18.13.6.2** For structures assigned to SDC C, D, E, or F, extension of prestressed reinforcement shall be detailed to transfer forces to the pile cap by embedding the pile reinforcement to the pile cap or mat foundation shall be in accordance based on a connection capacity equal to 1.25 times the nominal tensile strength shall be developed within the footing, as defined here, the compression development length is used if the pile is in compression. In the case of uplift, the tension development capacity shall be used to establish the connection reinforcement.

**18.13.6.3** For structures assigned to SDC D, E, or F, design shear at the connection at the base of the column and between pile cap or mat foundation and precast pile by reinforcement provided across the joint shall be developed by using a length of embedment or a mechanical device based on 1.25 $\times$ of the bar.


<!-- From Page 391 -->


## CODE

**18.14—Members not designated as part of the seismic-force-resisting system**

### 18.14.1 *Scope*

**18.14.1.1** This section shall apply to members not designated as a part of the seismic-force-resisting system in structures assigned to SDC C, D, E, or F.

### 18.14.2 *Design actions*

**18.14.2.1** Members not designated as part of the seismic-force-resisting system shall be evaluated for gravity load effects, effects of design displacements and shears resulting from seismic acting simultaneously with the design displacement δ.

### 18.14.3 *Cast-in-place beams, columns, and joints*

**18.14.3.1** Cast-in-place beams, columns, and joints satisfying 18.14.2.1 and 18.3.2 or 18.14.3, or 18.14.5.1 shall be designed for factored gravity loads and shear acting simultaneously with the design displacement δ. If factored moments subjected to the design displacement δ exceed the factored gravity loads, 18.2.8, the ductility demands shall be determined using the provisions of this chapter.

**18.14.3.2** Where the induced moments and shears do not exceed the design moment and shear strength of the frame member (a) through (d) shall be satisfied:

(a) Flexural strength at any section of beams reinforcement shall be provided in accordance with Chapter 11 factored axial force exceeds $A_g f'_c / 10$. The transverse reinforcement shall be hoops satisfying 18.7.5.2 at a spacing not to exceed $d/2$ over the full span of the smallest enclosed longitudinal bar and $d/4$.


<!-- From Page 392 -->


## CODE

(b) Columns shall satisfy 18.7.5.1 and 18.7.6. Spiral reinforcement satisfying 18.7.5.3 or hoop reinforcement satisfying 18.7.5.2 shall be provided (i) at both ends of the column over a length equal to one-sixth of the clear height of the column with spacing not to exceed the lesser of $h_c$ of $b_c$ of the smallest enclosed longitudinal bar and 6 in. Transverse reinforcement not less than the minimum given in (i) shall be provided over a height $\ell_o$ as defined in 18.7.5.1, from each joint face.

(c) In regions with factored compression exceeding $0.35f'_c A_g$, transverse reinforcement shall satisfy the minimum amount of transverse confinement provided shall be for rectangular hoops, ties and the greater of Table 18.7.5.4 spirals (d) and (e).

(d) In regions with factored axial compression that is one-half the greater of Table 18.7.5.4 spirals (d) and (e), transverse reinforcement shall be provided over the regions over the full height of the column.

(e) Joints shall satisfy Chapter 15.

**18.14.3.3** Where the induced moments or shears exceed the strength of the frame member, actions in (a) through (c) shall be satisfied:

(a) Materials, mechanical splices, and welded splices shall satisfy Chapter 26 and deformed bar development 18.2.8 through 18.2.9.

(b) Systems shall satisfy 18.14.3.3 and 18.6.5.

(c) Hoops and crossties shall satisfy 18.7.1.4, 18.7.1.7, and 18.7.1.8 and not be satisfied.

(d) Joints shall satisfy 18.8.4.1.

### 18.14.4 *Precast beams and columns*

**18.14.4.1** Precast concrete frame members assumed not to contribute to lateral resistance shall satisfy this connection. Beams shall satisfy (a) through (d):

(a) Flexural strength at any section of beams exceeds $A_g f'_c / 10$, the entire column shall be designed in accordance with 18.14.3.

(b) Structural integrity reinforcement in accordance with 7.13.

(c) Hoops shall be provided over a length that shall be at least 2 in. longer than determined from 18.2.8.

### 18.14.5 *Slab-column connections*

**18.14.5.1** For slab-column connections of two-way slabs without beams, slab shear reinforcement satisfying the provisions of Chapter 8 shall be detailed to satisfy flexural strength in accordance with 18.14.3.2 or 18.14.3.3 and the following conditions:


<!-- From Page 393 -->


## CODE

(a) Nonprestressed slabs where $\lambda s\sqrt{f'_c} > 0.035 - 0.12(Nu/Ag)$ ....
(1) Conforming to 18.14.3.2, and
(2) Slab reinforcement meeting the requirements of 8.6.5.7.

(b) Prestressed slabs where $\lambda s\sqrt{f'_c} > 0.028 - 0.12(Nu/Ag)$ ... shall only include from $0.5\ell_c$ The value of $(\lambda s\sqrt{f'_c})$ shall be taken at the greater of the values of the adhesion stress from at both faces for analysis with the 18.14.3.2, the combined prestressed slabs consistent with 20.6.1, and for unbonded post-tensioned slabs, the value of $f_{ps}$ shall be taken as zero when tension strains.

**18.14.5.2** The shear reinforcement requirements of 18.14.5.1 for prestressed slabs shall not be used.

(a) Where $\lambda s\sqrt{f'_c} \le 0.01$ for unbonded post-tensioned slabs with bonded reinforcement meeting the requirements of 8.6.5.8 over the full slab thickness.

(b) Where the slab effective depth $d$ is at least 10 in. and $v_u$ of slab sections within the slab thickness from the face of the support does not exceed $\phi(3 + 3V_c)$ of the slab.

### 18.14.6 *Wall piers*

**18.14.6.1** Wall piers not defined as columns or structural walls that are subjected to in-plane forces due to gravity loading or design drift shall satisfy the requirements of 18.14.3.2 as specified in the seismic-force-resisting system, it shall be permitted to calculate the design shear values using $V_c$ and $V_s$ in accordance with Chapter 11.


<!-- From Page 394 -->


## CODE

# CHAPTER 19—CONCRETE: DESIGN AND DURABILITY REQUIREMENTS

### 19.1—Scope

**19.1.1** This chapter shall apply to concrete, including:
(a) Concrete used for design
(b) Concrete used for durability

**19.1.2** This chapter shall apply to durability requirements for gravel used for bonded tendons in accordance with 19.4.

### 19.2—Concrete design properties

**19.2.1** *Design strength for concrete in design*

**19.2.1.1** The value of $f'_c$ shall be in accordance with (a) through (c).

(a) Table 19.2.1.1.
(b) Specified compressive strength of concrete shall be both normalweight and lightweight concrete.
(c) Design of composite members in accordance with 19.2.1.
(d) Unless otherwise specified, $f'_c$ shall be based on 28-day tests.

Concrete mixtures proportioned with $f'_c$ greater than 15,000 psi, and special structural walls, and their foundations, shall not exceed 8000 psi, except where shown by test data or analysis that performance is satisfactory. Concrete mixtures shall provide strength and toughness equal to or exceeding other methods in accordance with 26.4.

**Table 19.2.1.1—Limits for** $f'_c$

| Application | Minimum $f'_c$ psi |
|---|---|
| Gravel | 2500 |
| Foundation on reinforced cast-in-place reinforcement | 2500 |
| Foundation on Reinforced cast (Slab piers and occupancy) | 2500 |
| Prestressed concrete cast using low-relaxation tendons | |
| Foundation cast using other than low-relaxation tendons, | 3000 |
| Other than foundation and (Slab pier and occupancy) | |
| Prestressed reinforcement (all) Post-tensioned (all) | 3000 |
| Special moment frames with flat Grade 60 or 80 reinforcement | 3000 |
| Special moment frames with other than Grade 60 or 80 | 4000 |
| Special structural walls | 3000 |
| Diaphragm and collectors for structures in SDC C | |
| Diaphragm and collectors for structures in SDC D, E, or F | 4000 |
| Diaphragm and trusses in SDC C, D, E, or F | 3000 |

**19.2.1.2** The specified compressive strength shall be used for proportioning of concrete mixtures in 26.4.3 and for design calculations in accordance with this Code.

**19.2.1.3** Unless otherwise specified, $f'_c$ shall be based on 28-day tests. For design, tests, test ages for $f'_c$ shall be indicated in the construction documents.