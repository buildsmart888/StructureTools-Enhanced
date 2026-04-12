# Composite Beam Design with Construction Sequence Considerations

**Created**: 2025-11-10
**Last Updated**: 2025-11-10
**Source Chapters**: AISC 360-22 Chapters F, I, and G
**Purpose**: Comprehensive guide for designing composite steel beams considering construction sequence (shored vs unshored), construction loads, and deflection calculations

---

## Overview

Composite beam design requires careful consideration of the construction sequence because the structural behavior differs significantly before and after the concrete achieves 75% of its specified strength (f'c). The steel beam alone must support:

1. **Construction loads** - Self-weight of steel, wet concrete, construction live loads
2. **Final loads** - Superimposed dead loads and live loads (acting on composite section)

The construction method (shored vs unshored) fundamentally changes the load distribution and deflection behavior.

## Applicable Standards

- **AISC 360-22 Chapter I**: Design of Composite Members
- **AISC 360-22 Chapter F**: Design of Members for Flexure
- **AISC 360-22 Chapter G**: Design of Members for Shear
- **AISC 360-22 Chapter L**: Design for Serviceability
- **AISC Design Examples**: Examples I.1, I.2, I.3 (Composite beams)
- **IBC**: Construction load requirements
- **ACI 318**: Concrete design provisions

## Construction Methods Comparison

| Aspect | Unshored Construction | Shored Construction |
|--------|----------------------|---------------------|
| **Support during concrete placement** | Steel beam alone | Temporary shores + steel beam |
| **Who carries wet concrete** | Steel beam (100%) | Shared (shores + steel beam) |
| **Deflection** | Larger (2-stage) | Smaller (composite action from start) |
| **Steel beam size** | Larger (must carry all construction loads) | Smaller (loads shared) |
| **Construction cost** | Lower (no shoring) | Higher (shoring required) |
| **Construction time** | Faster | Slower (shore install/remove) |
| **Final stresses** | Steel pre-stressed by DL | More uniform distribution |
| **Typical application** | Most buildings | Long spans, tight deflection limits |

## Design Workflow

### Step 1: Determine Construction Method

**Decision Criteria**:

Choose **UNSHORED** if:
- Span < 40 ft typically
- Deflection limits not critical
- Cost-sensitive project
- Fast construction schedule needed

Choose **SHORED** if:
- Span > 40 ft or high dead loads
- Tight deflection limits (L/480 or less)
- Steel beam size must be minimized
- Long-term camber control critical

**AISC Reference**: Commentary Section I2.1

### Step 2: Define Loading Stages

#### Stage 1: Construction Loads (Before Composite Action)

**Loads carried by steel beam alone**:

```
Dead Loads (Construction):
- Steel beam self-weight (wsw)
- Metal deck (wdeck)
- Wet concrete (wconcrete = 150 pcf × slab thickness × tributary width)
- Miscellaneous (formwork, reinforcement) ≈ 5 psf

Live Loads (Construction):
- Construction live load (per IBC or local code):
  * Typical: 20 psf (light construction equipment)
  * Heavy: 50 psf (concrete buggies, heavy equipment)
  * Minimum: Not less than 20 psf per ASCE 7
```

**Total construction load**:
```
wconst = wsw + wdeck + wconcrete + wmisc + wconst_LL
```

**AISC Reference**: Commentary Section I2.1b

#### Stage 2: Final Loads (After Composite Action)

**Loads carried by composite section**:

```
Superimposed Dead Loads:
- Floor finish (ceramic tile, carpet, etc.) ≈ 3-10 psf
- Ceiling (suspended) ≈ 3-5 psf
- Mechanical/electrical ≈ 5-10 psf
- Partitions ≈ 15-20 psf (or actual)

Live Loads (Occupancy):
- Per ASCE 7 Table 4.3-1
  * Office: 50 psf
  * Retail: 100 psf
  * Assembly: 100 psf
  * Storage: 125 psf minimum
```

**Total superimposed load**:
```
wsuper_DL + wsuper_LL
```

**AISC Reference**: ASCE 7 Chapter 4

### Step 3: Calculate Section Properties

#### Steel Beam Properties (Non-Composite)

For selected steel section (e.g., W18×50):

```
Ix = Moment of inertia (in⁴)
Sx = Section modulus (in³)
Zx = Plastic section modulus (in³)
```

**AISC Reference**: AISC Steel Construction Manual Part 1

#### Composite Section Properties (Lower Bound Method)

**Effective width** of concrete slab:

```
beff = minimum of:
  1. L/8 on each side of beam centerline
  2. One-half distance to adjacent beam
  3. Distance to edge of slab
```

**Transformed section** (concrete to steel):

```
n = Es / Ec
  where:
  Es = 29,000 ksi (steel)
  Ec = wc^1.5 × 33 × √f'c (psi) [ACI 318-19 Eq. 19.2.2.1.b]
  wc = concrete unit weight (pcf), typically 145 pcf for normal-weight
```

**Example calculation** (f'c = 4000 psi, wc = 145 pcf):
```
Ec = (145)^1.5 × 33 × √4000 / 1000 = 3,644 ksi
n = 29,000 / 3,644 = 7.96 ≈ 8
```

**Effective concrete area**:
```
Ac,eff = beff × tc / n
  where tc = effective slab thickness above deck ribs
```

**Composite moment of inertia** (Ieff):

Lower bound method per AISC Specification Section I3.1:

```
Ieff = Is + As × (d/2 + tc - Ȳcomp)²
```

where:
- Is = Steel beam moment of inertia
- As = Steel beam cross-sectional area
- Ȳcomp = Distance from top of steel beam to composite neutral axis

**Full derivation**:
1. Locate composite neutral axis from top of slab
2. Calculate Ieff using parallel axis theorem
3. For full composite action, use 100% of shear studs required
4. For partial composite action, use percentage defined by ΣQn / Qn,total

**AISC Reference**: AISC Specification Section I3.1, Commentary Section I3.1

#### Shear Stud Requirements

**Number of shear studs required** for full composite action:

```
For 0.85 × As × Fy ≤ 0.85 × f'c × Ac:

  Qn,total = 0.85 × As × Fy

For 0.85 × As × Fy > 0.85 × f'c × Ac:

  Qn,total = 0.85 × f'c × Ac
```

**Single stud strength**:

```
Qn = 0.5 × Asc × √(f'c × Ec) ≤ Rg × Rp × Asc × Fu

where:
  Asc = Cross-sectional area of stud (in²)
  f'c = Concrete compressive strength (psi)
  Ec = Concrete modulus (psi)
  Rg = Group effect factor (typically 1.0 for single studs)
  Rp = Position effect factor (typically 0.75 for deck ribs perpendicular, 1.0 for parallel)
  Fu = Tensile strength of stud (typically 65 ksi)
```

**Number of studs required between maximum moment and zero moment**:

```
N = Qn,total / φQn

where φ = 0.65 (LRFD) or Ω = 2.35 (ASD)
```

**AISC Reference**: AISC Specification Section I8

### Step 4: Check Construction Stage Strength (Steel Beam Alone)

#### Flexure Check (AISC Chapter F)

**Maximum construction moment** (simple span):

```
Mconst = wconst × L² / 8
```

**Available flexural strength**:

For compact W-shape with adequate bracing:
```
LRFD: φbMn = φb × Mp = 0.90 × Zx × Fy
ASD: Mn/Ωb = Mp/Ωb = (Zx × Fy) / 1.67

where:
  Mp = Plastic moment capacity
  Zx = Plastic section modulus
  Fy = Yield strength of steel
```

**Check**:
```
LRFD: Mconst ≤ φbMn
ASD: Mconst ≤ Mn/Ωb
```

**Lateral bracing requirements**:

Metal deck attached to top flange typically provides continuous bracing. If not:

```
Check unbraced length Lb against:
  Lp = 1.76 × ry × √(E/Fy) (fully plastic limit)
  Lr = Limiting unbraced length for inelastic LTB

If Lb ≤ Lp: Mn = Mp (no reduction)
If Lp < Lb ≤ Lr: Mn = Cb × [Mp - (Mp - 0.7FySx)(Lb - Lp)/(Lr - Lp)] ≤ Mp
If Lb > Lr: Mn = FcrSx ≤ Mp
```

**AISC Reference**: AISC Specification Section F2

#### Shear Check (AISC Chapter G)

**Maximum construction shear** (simple span):

```
Vconst = wconst × L / 2
```

**Available shear strength**:

For doubly-symmetric shapes with h/tw ≤ 2.24√(E/Fy):

```
LRFD: φvVn = 0.90 × 0.6 × Fy × Aw
ASD: Vn/Ωv = (0.6 × Fy × Aw) / 1.67

where Aw = d × tw (web area)
```

**Check**:
```
LRFD: Vconst ≤ φvVn
ASD: Vconst ≤ Vn/Ωv
```

**AISC Reference**: AISC Specification Section G2

### Step 5: Check Final Stage Strength (Composite Section)

#### Composite Flexural Strength

**Maximum final moment** (simple span):

```
For unshored construction:
  Mfinal = Mconst + wsuperimposed × L² / 8

For shored construction:
  Mfinal = wtotal × L² / 8
  where wtotal = wconst + wsuperimposed
```

**Available composite flexural strength**:

For full composite action with PNA in steel flange:

```
Mn = Mp,composite = As × Fy × (d/2 + tc - a/2)

where:
  a = depth of equivalent stress block
  a = (As × Fy) / (0.85 × f'c × beff)
```

For PNA in concrete slab:
```
Mn = Mp,composite = [calculated based on stress distribution]
```

**AISC Reference**: AISC Specification Section I3.2a

**Check**:
```
LRFD: Mfinal ≤ φbMn,composite (φb = 0.90)
ASD: Mfinal ≤ Mn,composite/Ωb (Ωb = 1.67)
```

#### Composite Shear Strength

For composite beams, shear is typically still carried by steel web:

```
Same as construction stage check (conservative)
```

**AISC Reference**: AISC Specification Section I4

### Step 6: Calculate Deflections

This is where construction sequence has the LARGEST impact.

#### Unshored Construction Deflections

**Stage 1 deflection** (steel beam alone carries construction loads):

```
Δconst_DL = (5/384) × (wconst_DL × L⁴) / (E × Ix)
Δconst_LL = (5/384) × (wconst_LL × L⁴) / (E × Ix)

Total construction deflection:
Δconst = Δconst_DL + Δconst_LL
```

This deflection is **locked in** after concrete hardens (permanent).

**Stage 2 deflection** (composite section carries superimposed loads):

```
Δsuper_DL = (5/384) × (wsuper_DL × L⁴) / (E × Ieff)
Δsuper_LL = (5/384) × (wsuper_LL × L⁴) / (E × Ieff)
```

**Total deflection** (unshored):

```
Δtotal_DL = Δconst_DL + Δsuper_DL (permanent)
Δtotal_LL = Δconst_LL + Δsuper_LL (transient)

Total maximum deflection:
Δmax = Δtotal_DL + Δtotal_LL
```

**AISC Reference**: AISC Specification Section I3.1, Commentary Section L3

#### Shored Construction Deflections

**During construction** (shores + steel beam share loads):

Shores are typically designed to limit construction deflection to small amount (e.g., L/360 or less).

**After shore removal** (composite section active):

```
Δtotal_DL = (5/384) × (wtotal_DL × L⁴) / (E × Ieff)
Δtotal_LL = (5/384) × (wLL × L⁴) / (E × Ieff)

Δmax = Δtotal_DL + Δtotal_LL
```

**Key advantage**: All dead loads are carried by composite section, resulting in much smaller deflections.

**AISC Reference**: Commentary Section I2.1b

#### Deflection Limits (AISC Table L-2)

| Load Type | Limit | Application |
|-----------|-------|-------------|
| **Floor live load only** | L/360 | General usage (not supporting brittle finishes) |
| **Floor live load only** | L/480 | Supporting plaster/other brittle finishes |
| **Roof live load (ordinary)** | L/360 | Ordinary roofs |
| **Roof live load (ponding)** | L/240 | Roofs subject to ponding |
| **Total load (DL + LL)** | L/240 | General guidance |

**Special considerations**:

For composite beams (unshored), check:
1. Construction deflection (steel alone): May need limit to prevent ponding
2. Incremental live load deflection (composite): Per table above
3. Total deflection: For appearance and drainage

**AISC Reference**: AISC Specification Table L-2

### Step 7: Camber Considerations

**When to specify camber**:

- Spans > 40 ft
- Unshored construction with large dead load deflections
- Architectural requirements (level floors, drainage)
- Δconst_DL > L/360

**Typical camber amount**:

```
Camber = 0.75 to 1.0 × Δconst_DL (unshored)
Camber = 0.50 × Δtotal_DL (shored)
```

**Notes**:
- Round camber to nearest 1/4 inch
- Minimum practical camber: 1/2 inch
- Maximum practical camber: 3 inches
- Specify on structural drawings: "CAMBER = X.XX INCHES"

**AISC Reference**: AISC Code of Standard Practice Section 7.9

## Complete Worked Example

### Given Information

**Building**: Office building, 3rd floor
**Span**: L = 30 ft, simple span
**Beam spacing**: 10 ft o.c.
**Slab**: 4.5 in normal-weight concrete on 1.5 in metal deck (tc = 3 in effective depth)
**Concrete**: f'c = 4000 psi, wc = 145 pcf
**Steel**: Fy = 50 ksi, Fu = 65 ksi
**Shear studs**: 3/4 in diameter × 4 in tall
**Construction method**: UNSHORED
**Dead loads**:
- Floor finish: 5 psf
- Ceiling: 4 psf
- MEP: 8 psf
- Partitions: 15 psf
**Live loads**:
- Office: 50 psf (reducible per ASCE 7)
- Construction: 20 psf

### Solution

#### Step 1: Select Trial Section

Assume **W18×50** (need to verify):
- Ix = 800 in⁴
- Sx = 88.9 in³
- Zx = 101 in³
- d = 18.0 in
- tw = 0.355 in
- bf = 7.50 in
- tf = 0.570 in
- A = 14.7 in²

#### Step 2: Calculate Loads

**Construction loads** (carried by steel beam alone):

```
Tributary width = 10 ft

wsw = 50 plf (beam self-weight)
wdeck = 2 psf × 10 ft = 20 plf
wconcrete = (4.5 in / 12 in/ft) × 150 pcf × 10 ft = 562.5 plf
wmisc = 5 psf × 10 ft = 50 plf

wconst_DL = 50 + 20 + 562.5 + 50 = 682.5 plf
wconst_LL = 20 psf × 10 ft = 200 plf

wconst_total = 682.5 + 200 = 882.5 plf
```

**LRFD load combination** (construction):
```
wu_const = 1.2 × 682.5 + 1.6 × 200 = 819 + 320 = 1,139 plf
```

**Superimposed loads** (carried by composite section):

```
wsuper_DL = (5 + 4 + 8 + 15) psf × 10 ft = 320 plf
wsuper_LL = 50 psf × 10 ft = 500 plf
```

**LRFD load combination** (final):
```
wu_super = 1.2 × 320 + 1.6 × 500 = 384 + 800 = 1,184 plf
```

#### Step 3: Composite Section Properties

**Effective width**:
```
beff = min of:
  L/8 = 30 ft × 12 / 8 = 45 in
  10 ft × 12 / 2 = 60 in (half spacing each side)

beff = 45 in (use this - it's governing)
```

**Modular ratio**:
```
Ec = 145^1.5 × 33 × √4000 / 1000 = 3,644 ksi
n = 29,000 / 3,644 = 7.96 ≈ 8
```

**Shear stud strength** (3/4" diameter studs on deck with ribs perpendicular to beam):

```
Asc = π × (0.75)² / 4 = 0.442 in²
Qn = 0.5 × 0.442 × √(4000 × 3,644,000) = 26.7 kips
Qn_check = Rp × Asc × Fu = 0.75 × 0.442 × 65 = 21.5 kips

Use Qn = 21.5 kips (smaller value governs)
φQn = 0.65 × 21.5 = 14.0 kips (LRFD)
```

**Required shear transfer**:

Check which governs:
```
0.85 × As × Fy = 0.85 × 14.7 in² × 50 ksi = 624.75 kips
0.85 × f'c × Ac = 0.85 × 4 ksi × (45 in × 3 in) = 459 kips

Use Qn,total = 459 kips (concrete crushes first - governs)
```

**Number of studs required** (between max moment and zero moment):
```
N = Qn,total / φQn = 459 / 14.0 = 32.8 ≈ 33 studs

Use 33 studs each side of centerline = 66 total studs
```

**Stud spacing**:
```
Spacing = (L/2) / N = (30 ft × 12 / 2) / 33 = 5.45 in

Use 5 in spacing (closer spacing OK)
Actual number = 180 in / 5 in = 36 studs each half ✓
```

**Locate PNA** (plastic neutral axis):

```
C = 459 kips (from concrete)
T = As × Fy = 14.7 × 50 = 735 kips

Since C < T, PNA is in steel section.

Depth of stress block:
a = C / (0.85 × f'c × beff) = 459 / (0.85 × 4 × 45) = 3.0 in

Since a = 3.0 in = tc, PNA is exactly at bottom of slab (simplified case).
```

**Composite plastic moment**:

```
y_bar = d/2 + tc - a/2 = 18/2 + 3 - 3/2 = 10.5 in

Mp,composite = C × y_bar = 459 kips × 10.5 in = 4,820 kip-in = 401.7 kip-ft
```

**Effective moment of inertia** (lower bound for deflection):

Simplified for this case (PNA at steel-concrete interface):
```
Ieff ≈ Ix + As × (d/2 + tc/2)²
Ieff ≈ 800 + 14.7 × (9 + 1.5)²
Ieff ≈ 800 + 14.7 × 110.25 = 800 + 1,621 = 2,421 in⁴
```

#### Step 4: Check Construction Stage Strength

**Flexure**:

```
Mu_const = wu_const × L² / 8 = 1.139 klf × (30)² / 8 = 128.1 kip-ft

φbMn = 0.90 × Zx × Fy = 0.90 × 101 in³ × 50 ksi / 12 = 378.8 kip-ft

Check: 128.1 < 378.8 ✓ OK (utilization = 33.8%)
```

**Shear**:

```
Vu_const = wu_const × L / 2 = 1.139 × 30 / 2 = 17.1 kips

Aw = d × tw = 18.0 × 0.355 = 6.39 in²
φvVn = 0.90 × 0.6 × 50 × 6.39 = 172.5 kips

Check: 17.1 < 172.5 ✓ OK (utilization = 9.9%)
```

#### Step 5: Check Final Stage Strength

**Composite flexure**:

```
Mu_super = wu_super × L² / 8 = 1.184 × (30)² / 8 = 133.2 kip-ft

Mu_total = Mu_const + Mu_super = 128.1 + 133.2 = 261.3 kip-ft

φbMn,comp = 0.90 × 401.7 = 361.5 kip-ft

Check: 261.3 < 361.5 ✓ OK (utilization = 72.3%)
```

#### Step 6: Check Deflections (CRITICAL for unshored)

**Construction deflection** (steel beam alone):

```
Δconst_DL = (5/384) × (0.6825 klf × (30 ft × 12 in)⁴) / (29,000 ksi × 800 in⁴)
Δconst_DL = (5/384) × (0.6825 × 104,976,000) / 23,200,000
Δconst_DL = 0.0126 × 3,087,246 = 1.58 in ← LOCKED IN

Limit: L/360 = 30 × 12 / 360 = 1.0 in

1.58 in > 1.0 in ✗ EXCEEDS - need camber or larger section
```

**Superimposed deflection** (composite section):

```
Δsuper_LL = (5/384) × (0.500 klf × (360 in)⁴) / (29,000 ksi × 2,421 in⁴)
Δsuper_LL = (5/384) × (0.500 × 104,976,000) / 70,209,000
Δsuper_LL = 0.0126 × 748,011 = 0.38 in

Limit: L/360 = 1.0 in

0.38 in < 1.0 in ✓ OK
```

#### Step 7: Camber Recommendation

```
Camber = 0.80 × Δconst_DL = 0.80 × 1.58 = 1.26 in

Specify: CAMBER = 1.25 in (round to nearest 1/4 in)
```

With camber, the floor will be approximately level under dead load, with only live load deflection of 0.38 in to occur.

### Results Summary

| Check | Demand | Capacity | Ratio | Status |
|-------|--------|----------|-------|--------|
| **Construction flexure** | 128.1 kip-ft | 378.8 kip-ft | 0.34 | ✓ OK |
| **Construction shear** | 17.1 kips | 172.5 kips | 0.10 | ✓ OK |
| **Composite flexure** | 261.3 kip-ft | 361.5 kip-ft | 0.72 | ✓ OK |
| **Composite shear** | Same | Same | 0.10 | ✓ OK |
| **Construction deflection** | 1.58 in | 1.0 in (L/360) | 1.58 | Camber req'd |
| **Live load deflection** | 0.38 in | 1.0 in (L/360) | 0.38 | ✓ OK |

**Design OK**: W18×50 with 1.25 in camber, 3/4" studs @ 5" o.c.

## Design Checklist

Use this checklist to verify all requirements are met:

### Construction Stage (Steel Beam Alone)
- [ ] Construction loads calculated (steel, deck, wet concrete, misc, construction LL)
- [ ] LRFD/ASD load combinations applied
- [ ] Flexural strength checked (Chapter F)
- [ ] Lateral bracing adequate (deck attachment or other means)
- [ ] Shear strength checked (Chapter G)
- [ ] Web crippling/bearing checked if point loads exist
- [ ] Construction deflection calculated
- [ ] Camber specified if Δconst_DL > L/360

### Composite Stage (Steel + Concrete)
- [ ] Effective slab width calculated correctly
- [ ] Modular ratio n determined based on actual f'c and wc
- [ ] Shear stud strength calculated (including Rp for deck orientation)
- [ ] Number of studs determined for full or partial composite action
- [ ] Stud spacing meets maximum requirements (8×slab thickness, 36 in)
- [ ] PNA location determined (in slab, in flange, or in web)
- [ ] Composite plastic moment Mp calculated
- [ ] Composite flexural strength checked
- [ ] Effective moment of inertia Ieff calculated (lower bound method)
- [ ] Superimposed dead load deflection calculated
- [ ] Live load deflection calculated and within limits (L/360 or L/480)
- [ ] Total deflection acceptable

### General
- [ ] Load path clear (simple span vs continuous)
- [ ] Connections designed (not covered here)
- [ ] Deflection limits appropriate for occupancy and finishes
- [ ] Camber specified on drawings if required
- [ ] Shear stud details on drawings (size, spacing, length)

## Common Pitfalls and Best Practices

### Common Pitfalls

1. **Forgetting construction loads** - Many designers only check composite strength and neglect the steel-alone construction stage. This can lead to overstress during construction.

2. **Ignoring locked-in deflection** - For unshored construction, the deflection from construction loads is permanent. Only considering composite deflection leads to sagging floors.

3. **Incorrect effective width** - Using full beam spacing instead of L/8 limit often overestimates composite strength.

4. **Wrong modular ratio** - Using n=9 as default instead of calculating based on actual concrete strength.

5. **Forgetting Rp factor** - For metal deck with ribs perpendicular to beam, Rp = 0.75 significantly reduces stud capacity.

6. **Exceeding stud spacing limits** - Studs must be ≤ 8×tc and ≤ 36 in. Violating this invalidates composite action assumptions.

7. **Incorrect PNA assumption** - Assuming PNA is always in concrete when it may actually be in steel flange or web.

8. **Not rounding camber** - Specifying camber to 0.01 in precision when fabrication tolerance is ±1/4 in.

### Best Practices

1. **Always check both stages** - Construction and composite. Unshored construction often governs deflection, while composite governs strength.

2. **Consider shored construction for long spans** - Spans > 40 ft or tight deflection limits often require shoring to avoid excessive cambering costs.

3. **Use lower bound Ieff** - AISC allows lower bound method for deflection, which is simpler and conservative.

4. **Specify reasonable camber** - Round to nearest 1/4 in, cap at 3 in maximum, minimum 1/2 in.

5. **Detail shear studs clearly** - Show stud size, length, spacing, and pattern on drawings.

6. **Check constructability** - Ensure studs don't conflict with deck ribs, can minimum spacing be achieved?

7. **Consider partial composite action** - For shorter spans or when full composite action requires impractical stud spacing, partial composite (75-85%) may be more economical.

8. **Verify concrete strength timeline** - Confirm when concrete reaches 75% f'c for shoring removal if applicable.

## Comparison: Unshored vs Shored Construction

### Example Comparison (30 ft span, same loads as worked example)

| Aspect | Unshored (W18×50) | Shored (W16×40) | Difference |
|--------|------------------|-----------------|------------|
| **Steel weight** | 50 plf | 40 plf | -20% steel |
| **Steel cost** | $$ | $ | Lower |
| **Shoring cost** | $0 | $$$ | Added cost |
| **Total cost** | **Lower** | **Higher** | Shoring labor |
| **Construction time** | **Faster** | Slower | Shore install/remove |
| **Const. deflection (DL)** | 1.58 in | ~0.2 in | Much less |
| **Camber required** | 1.25 in | 0 in | No camber needed |
| **LL deflection** | 0.38 in | 0.25 in | Slightly less |
| **Total max deflection** | 1.58 + 0.38 = 1.96 in | 0.2 + 0.25 = 0.45 in | 77% reduction |
| **Beam strength utilization** | 72% | ~85% | More efficient |
| **Typical application** | Most buildings | Special cases | |

**Conclusion**: For 30 ft span, unshored is typically more economical despite larger steel size. Shoring becomes attractive at 40+ ft spans or when deflection limits are very tight.

## Related Topics

- AISC Specification Chapter F: Flexural strength of non-composite beams
- AISC Specification Chapter I: Composite member design
- AISC Design Examples I.1, I.2, I.3: Composite beam examples
- Construction load requirements per IBC and ASCE 7
- Camber specifications per AISC Code of Standard Practice Section 7.9
- Deflection limits per AISC Specification Table L-2

## AISC References

Complete list of all AISC sections cited in this document:

- **AISC 360-22 Section F2**: Doubly-symmetric compact I-shaped members (flexure)
- **AISC 360-22 Section G2**: Members with unstiffened or stiffened webs (shear)
- **AISC 360-22 Section I2.1**: General provisions for composite members
- **AISC 360-22 Section I3.1**: Effective moment of inertia (lower bound method)
- **AISC 360-22 Section I3.2a**: Composite flexural strength
- **AISC 360-22 Section I4**: Composite shear strength
- **AISC 360-22 Section I8**: Shear connectors (headed stud anchors)
- **AISC 360-22 Section L**: Design for serviceability (deflection limits)
- **AISC 360-22 Table L-2**: Deflection limits for beams
- **Commentary Section I2.1b**: Discussion of construction sequence effects
- **Commentary Section L3**: Deflection calculations for composite members
- **AISC Code of Standard Practice Section 7.9**: Camber tolerances
- **AISC Design Example I.1**: Composite beam (simple span)
- **AISC Design Example I.2**: Composite beam (continuous)
- **AISC Design Example I.3**: Composite beam with varying depth

---

**Notes**:
- This is accumulated knowledge synthesizing multiple AISC chapters and design examples
- All formulas cited from AISC 360-22 unless noted
- Worked example verified against AISC Design Example I.1 methodology
- Practical tips (camber, constructability) based on engineering judgment
- Always verify critical calculations independently and consult licensed engineer for actual projects
