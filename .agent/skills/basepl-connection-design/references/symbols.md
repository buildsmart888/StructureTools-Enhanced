# Notation and Symbols

*Standard notation used in AISC Design Guide 1: Base Connection Design*

## Geometric Parameters

### Base Plate Dimensions
- **B** = base plate width (perpendicular to bending axis), in.
- **N** = base plate length (parallel to bending axis), in.
- **t_pl** = base plate thickness, in.
- **A_bp** = base plate area = N × B, in.²

### Column Dimensions
- **d** = column depth, in.
- **b_f** = column flange width, in.
- **t_f** = column flange thickness, in.
- **t_w** = column web thickness, in.

### Bearing and Anchor Layout
- **m** = cantilever dimension from column flange edge to plate edge, in.
- **n** = cantilever dimension perpendicular to m, in.
- **λ** = cantilever dimension parameter
- **Y** = equivalent bearing length, in.
- **f** = distance from anchor rod centerline to column face, in.

### Concrete Foundation
- **A1** = base plate area in contact with concrete, in.²
- **A2** = maximum area of supporting concrete geometrically similar to A1, in.²
- **h_ef** = effective embedment depth of anchor rods, in.

## Load Parameters

### Applied Loads (Factored for LRFD, Service for ASD)
- **P_u** = factored axial load (LRFD), kips
- **P_a** = service axial load (ASD), kips
- **P_r** = required axial load (generic for LRFD or ASD), kips
- **M_u** = factored moment (LRFD), kip-in.
- **M_a** = service moment (ASD), kip-in.
- **M_r** = required moment (generic), kip-in.
- **V_u** = factored shear (LRFD), kips
- **V_a** = service shear (ASD), kips
- **V_r** = required shear (generic), kips

### Eccentricity
- **e** = eccentricity = M_r / P_r, in.
- **e_crit** = critical eccentricity (boundary between small/large moment), in.
- **ε** = distance from bearing resultant to plate centerline, in.

### Internal Forces
- **T_u** = factored anchor rod tension force (LRFD), kips
- **T_a** = service anchor rod tension force (ASD), kips
- **T_r** = required anchor rod tension (generic), kips
- **C** = compression force in bearing, kips
- **q** = resultant bearing force per unit width = f_p × B, kips/in.
- **q_max** = maximum resultant bearing force per unit width, kips/in.

## Stress Parameters

### Bearing Stress
- **f_p** = bearing stress between base plate and concrete/grout, ksi
- **f_p(max)** = maximum bearing stress, ksi
- **f'_c** = specified compressive strength of concrete, psi (or ksi)
- **f'_g** = specified compressive strength of grout, psi (or ksi)

### Steel Stresses
- **F_y** = specified minimum yield stress of base plate steel, ksi
- **F_u** = specified minimum tensile strength of steel, ksi
- **F_ya** = specified minimum yield stress of anchor rod, ksi
- **F_uta** = specified minimum tensile strength of anchor rod, ksi

## Resistance and Capacity Parameters

### Concrete Bearing (ACI 318)
- **φ_c** = resistance factor for concrete (LRFD) = 0.65
- **Ω_c** = safety factor for concrete (ASD) = 2.31
- **φP_p** = available bearing strength on concrete (LRFD), kips
- **P_p/Ω_c** = allowable bearing strength on concrete (ASD), kips

### Steel Design
- **φ** = resistance factor (LRFD)
  - φ = 0.90 for tension yielding
  - φ = 0.75 for tension rupture
  - φ = 0.75 for shear
  - φ = 1.00 for bearing on concrete
- **Ω** = safety factor (ASD)
  - Ω = 1.67 for tension yielding
  - Ω = 2.00 for tension rupture
  - Ω = 2.00 for shear
  - Ω = 1.50 for bearing on concrete

### Anchor Rod Capacity
- **φN_sa** = available steel strength of anchor in tension (LRFD), kips
- **N_sa/Ω** = allowable steel strength of anchor in tension (ASD), kips
- **φN_cb** = available concrete breakout strength in tension (LRFD), kips
- **N_cb/Ω** = allowable concrete breakout strength in tension (ASD), kips

## Friction and Shear Transfer

### Friction Parameters
- **μ** (or **μ_friction**) = coefficient of friction
  - μ = 0.55 for steel on grout
  - μ = 0.55 for steel on concrete
- **φV_f** = available shear friction resistance (LRFD), kips
- **V_f/Ω** = allowable shear friction resistance (ASD), kips

### Shear Lug
- **V_bearing** = shear resistance by bearing on concrete, kips
- **V_steel** = shear resistance of steel lug, kips

## Geometric Ratios and Factors

### Confinement
- **√(A2/A1)** = confinement factor (maximum value = 2.0)
  - Used to increase bearing strength when base plate is smaller than supporting concrete

### Plate Bending Parameters
- **λ** = geometric parameter for plate bending
- **δ_b** = parameter for base plate design
- **l** = cantilever length for plate bending calculations, in.

## Material Properties

### Concrete
- **E_c** = modulus of elasticity of concrete, ksi
- **β** = ratio of long side to short side of anchor pattern

### Grout
- **f'_g** = specified compressive strength of grout (typically ≥ f'_c), psi

### Anchor Rods (ASTM F1554)
- **Grade 36**: F_ya = 36 ksi, F_uta = 58 ksi
- **Grade 55**: F_ya = 55 ksi, F_uta = 75 ksi
- **Grade 105**: F_ya = 105 ksi, F_uta = 125 ksi

## Dimensional Constraints

### Tolerances
- **± 1/4 in.** = typical anchor rod placement tolerance
- **± 1/2 in.** = maximum anchor rod placement tolerance
- **1 in. minimum** = typical grout thickness
- **3 in. maximum** = typical grout thickness

### Clearances
- **d_h** = anchor rod hole diameter, in.
  - Typical: d_h = d_b + 1/4 in. (where d_b = anchor rod diameter)
  - Maximum: d_h = d_b + 1/2 in.

## Weld Parameters

### Weld Size
- **w** = weld size (leg dimension for fillet welds), in.
- **D** = weld size parameter for column-to-base-plate welds

### Weld Strength
- **F_EXX** = electrode classification number (tensile strength), ksi
  - E70: F_EXX = 70 ksi
  - E80: F_EXX = 80 ksi

## Load Combinations

### LRFD Load Combinations (per ASCE 7)
- **1.4D**
- **1.2D + 1.6L + 0.5(L_r or S or R)**
- **1.2D + 1.6(L_r or S or R) + (L or 0.5W)**
- **1.2D + 1.0W + L + 0.5(L_r or S or R)**
- **1.2D + 1.0E + L + 0.2S**
- **0.9D + 1.0W**
- **0.9D + 1.0E**

Where:
- **D** = dead load
- **L** = live load
- **L_r** = roof live load
- **S** = snow load
- **R** = rain load
- **W** = wind load
- **E** = seismic load

### ASD Load Combinations (per ASCE 7)
- **D**
- **D + L**
- **D + (L_r or S or R)**
- **D + 0.75L + 0.75(L_r or S or R)**
- **D + (0.6W or 0.7E)**
- **D + 0.75L + 0.75(0.6W) + 0.75(L_r or S or R)**
- **D + 0.75L + 0.75(0.7E) + 0.75S**
- **0.6D + 0.6W**
- **0.6D + 0.7E**

## Subscripts and Conventions

### Subscripts
- **u** = factored (ultimate) values for LRFD
- **a** = service (allowable) values for ASD
- **r** = required (generic for either LRFD or ASD)
- **n** = nominal strength
- **y** = yield
- **u** (in F_u) = ultimate (tensile strength)
- **max** = maximum value
- **min** = minimum value
- **reqd** = required
- **avail** = available
- **p** (in f_p) = plate (bearing pressure)
- **pl** = plate
- **c** = concrete
- **g** = grout

### Design Method Indicators
- **φ** prefix = LRFD resistance factor
- **/Ω** suffix = ASD safety factor divisor
- **LRFD**: Load and Resistance Factor Design
- **ASD**: Allowable Strength Design

## Special Notation

### Moment Classification
- **Small moment case**: e ≤ e_crit (no anchor rod tension required)
- **Large moment case**: e > e_crit (anchor rods required for tension)

### Axes Convention
- **Strong axis**: Bending about column's strong axis (parallel to web)
- **Weak axis**: Bending about column's weak axis (parallel to flanges)
- **Biaxial**: Bending about both axes simultaneously

### Sign Conventions
- **Tension**: Positive (+) for uplift forces
- **Compression**: Positive (+) for bearing forces
- **Moment**: Positive when causing tension on one side
- **Shear**: Direction indicated by context

## References to Specifications

- **AISC Specification**: ANSI/AISC 360 (Specification for Structural Steel Buildings)
- **ACI 318**: Building Code Requirements for Structural Concrete
- **ASCE 7**: Minimum Design Loads for Buildings and Other Structures
- **ASTM F1554**: Standard Specification for Anchor Bolts, Steel, 36, 55, and 105-ksi Yield Strength
- **ASTM A307**: Standard Specification for Carbon Steel Bolts, Studs, and Threaded Rod
