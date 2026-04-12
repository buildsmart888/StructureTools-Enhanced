# Limit States Checklist by Member Type

Comprehensive checklist of all limit states to verify for each structural steel member type per AISC 360-22.

---

## How to Use This Checklist

For each member type, check **all applicable limit states**. Not every limit state applies to every situation - use engineering judgment to determine which checks are relevant.

**Notation**:
- ✓ = Check required for most designs
- ○ = Check required only in specific situations
- AISC Section = Reference to AISC 360-22 Specification

---

## 1. W-Shape Beams (Flexural Members)

### A. Flexure (AISC Chapter F)

**For Compact Sections with Full Lateral Bracing**:
- [ ] **Yielding** (F2.1) - ✓ Always check
  - `Mn = Mp = FyZx ≤ 1.5FySx`
  - φb = 0.90 (LRFD), Ωb = 1.67 (ASD)

**For Members with Unbraced Length Lb**:
- [ ] **Lateral-Torsional Buckling (LTB)** (F2.2) - ✓ If Lb > Lp
  - Check Lb vs Lp and Lr
  - If Lp < Lb ≤ Lr: Inelastic LTB
  - If Lb > Lr: Elastic LTB
  - Apply Cb modification factor if moment gradient exists

**For Non-Compact or Slender Sections**:
- [ ] **Flange Local Buckling (FLB)** (F3.1) - ○ If λ > λpf
  - Check flange width-thickness ratio: bf/2tf
  - Reduce Mn if flange is non-compact or slender

- [ ] **Web Local Buckling (WLB)** (F3.2) - ○ If λ > λpw
  - Check web height-thickness ratio: h/tw
  - Reduce Mn if web is non-compact or slender

**For Beams with Holes in Tension Flange**:
- [ ] **Tension Flange Rupture** (F13.1) - ○ If holes in tension flange
  - `Mn = FuAfn` where Afn = net flange area
  - φb = 0.75 (LRFD), Ωb = 2.00 (ASD)

**For Beams with Concentrated Forces**:
- [ ] **Compression Flange Local Buckling** (F13.2) - ○ If concentrated force on flange
  - Check compression flange at point of loading

### B. Shear (AISC Chapter G)

- [ ] **Shear Yielding** (G2.1) - ✓ Always check
  - `Vn = 0.6FyAwCv1` where Aw = dtw
  - φv = 1.00 (LRFD), Ωv = 1.50 (ASD)

- [ ] **Shear Buckling** (G2.2) - ○ If h/tw > 2.24√(E/Fy)
  - Web is slender - apply Cv reduction
  - Typically not an issue for W-shapes (most are h/tw < limit)

### C. Deflection (AISC Chapter L)

- [ ] **Live Load Deflection** (Table L-2) - ✓ Always check
  - Floor beams: L/360 (typical), L/480 (plaster/brittle finishes)
  - Roof beams: L/360 (ordinary), L/240 (ponding)

- [ ] **Total Deflection (DL + LL)** (Table L-2) - ○ Check for appearance
  - Typical limit: L/240

- [ ] **Vibration** (Appendix 1) - ○ If rhythmic activities or sensitive equipment
  - Floor natural frequency > 3 Hz (typical)
  - Acceleration limits per intended use

### D. Local Effects (AISC Chapter J)

- [ ] **Web Local Yielding** (J10.2) - ✓ If concentrated loads
  - At interior supports and point loads
  - `Rn = (5k + lb)Fytw`

- [ ] **Web Crippling** (J10.3) - ✓ If concentrated loads
  - At beam ends and interior supports
  - `Rn = 0.80tw²[1 + 3(lb/d)(tw/tf)^1.5]√(EFytf/tw)`

- [ ] **Web Compression Buckling** (J10.5) - ○ If large concentrated compression
  - Check if d/tw > limit
  - May require stiffeners

- [ ] **Web Sidesway Buckling** (J10.4) - ○ If compression flange not braced at load point
  - Rare - only when top flange not braced and compression force applied

### E. Composite Action (if applicable)

- [ ] **Composite Flexural Strength** (I3.2) - ○ If composite with concrete slab
  - Calculate composite Mp based on PNA location
  - Check shear stud capacity

- [ ] **Construction Stage Strength** (I2.1) - ○ If unshored construction
  - Steel beam alone must carry wet concrete + construction loads

---

## 2. W-Shape Columns (Compression Members)

### A. Compression (AISC Chapter E)

- [ ] **Flexural Buckling** (E3) - ✓ Always check both axes
  - Check x-x axis: KLx/rx
  - Check y-y axis: KLy/ry
  - Calculate Pn = FcrAg where Fcr based on slenderness

- [ ] **Local Buckling** (E7) - ○ If non-compact or slender elements
  - Flange local buckling: Check bf/2tf against λr
  - Web local buckling: Check h/tw against λr
  - Reduce Pn if elements are slender

### B. Combined Axial and Flexure (AISC Chapter H)

**For Pr/Pc ≥ 0.2**:
- [ ] **H1.1 Interaction Check** - ✓ If significant moment and axial
  - `(Pr/Pc) + (8/9)(Mrx/Mcx + Mry/Mcy) ≤ 1.0`

**For Pr/Pc < 0.2**:
- [ ] **H1.1 Alternative Check** - ✓ If small axial, large moment
  - `(Pr/2Pc) + (Mrx/Mcx + Mry/Mcy) ≤ 1.0`

**Amplification Factors**:
- [ ] **B1 Factor** (C-A-3) - ✓ Account for second-order effects (P-δ)
  - `B1 = Cm/(1 - αPr/Pe1) ≥ 1.0`

- [ ] **B2 Factor** (C-A-7.2) - ○ If story sway (use Direct Analysis instead)
  - `B2 = 1/(1 - αΔPstory/ΔHL) ≥ 1.0`

**Moment Magnification**:
- [ ] **Apply B1 to non-sway moments** - ✓ For all columns
- [ ] **Apply B2 to sway moments** - ○ If second-order analysis not used

### C. Local Effects (AISC Chapter J)

- [ ] **Base Plate Bearing on Concrete** (J8) - ✓ At column base
  - `Rn = 0.85f'cA1√(A2/A1)` ≤ `1.7f'cA1`
  - φ = 0.65 (LRFD), Ω = 2.31 (ASD)

- [ ] **Base Plate Bending** (J8) - ✓ At column base
  - Check base plate thickness for bearing pressure
  - Minimum thickness to prevent bending failure

---

## 3. HSS (Hollow Structural Sections)

### A. Tension (AISC Chapter D)

- [ ] **Tensile Yielding** (D2) - ✓ Always check
  - `Pn = FyAg`
  - φt = 0.90 (LRFD), Ωt = 1.67 (ASD)

- [ ] **Tensile Rupture** (D2) - ○ If holes or effective area < gross area
  - `Pn = FuAe` where Ae = effective net area
  - φt = 0.75 (LRFD), Ωt = 2.00 (ASD)

### B. Compression (AISC Chapter E)

- [ ] **Flexural Buckling** (E4) - ✓ For round HSS
  - Check KL/r (same as W-shapes)
  - Round HSS: Same rx = ry (equal in all directions)

- [ ] **Flexural Buckling** (E3) - ✓ For rectangular HSS
  - Check strong and weak axes (usually same for square HSS)

- [ ] **Local Buckling** (E7.2) - ○ If slender sections
  - Flange: Check b/t for rectangular HSS
  - Wall: Check D/t for round HSS
  - Reduce Pn if slender

### C. Flexure (AISC Chapter F)

**For Compact Round HSS**:
- [ ] **Yielding** (F7.1) - ✓ Always check
  - `Mn = Mp = FyZ`

- [ ] **Local Buckling** (F7.2) - ○ If D/t > λp
  - Check wall slenderness: D/t
  - Reduce Mn if non-compact or slender

**For Rectangular HSS**:
- [ ] **Yielding** (F8.1) - ✓ Always check
  - `Mn = Mp = FyZx`

- [ ] **Flange Local Buckling** (F8.2) - ○ If b/t > λpf
  - Check flange width-thickness ratio
  - Reduce Mn if non-compact or slender

- [ ] **Web Local Buckling** (F8.3) - ○ If h/t > λpw
  - Check web depth-thickness ratio
  - Reduce Mn if non-compact or slender

### D. Torsion (AISC Chapter H4)

- [ ] **Torsional Strength** (H4) - ○ If torsion present
  - HSS very efficient in torsion (closed section)
  - `Tn = FcrC` where C = torsional constant
  - Rarely governs for HSS

---

## 4. Plate Girders

### A. Flexure (AISC Chapter F)

- [ ] **Yielding** (F5.1) - ✓ Always check
  - Check both compression and tension flanges
  - `Mn = RpgFySxc` ≤ `1.6FySxc` (compression flange)

- [ ] **Lateral-Torsional Buckling** (F5.2) - ✓ If unbraced length Lb > 0
  - Similar to W-shapes but use Sxc (compression flange)
  - Check Lb vs Lp, Lr

- [ ] **Compression Flange Local Buckling** (F5.3) - ○ If compression flange slender
  - Check bf/2tf
  - Reduce Mn if slender

- [ ] **Tension Flange Yielding** (F5.4) - ✓ Always check
  - `Mn = RpgFySxt` where Sxt = section modulus to tension flange
  - Ensures tension flange doesn't yield first

### B. Shear (AISC Chapter G)

- [ ] **Shear Yielding** (G2.1) - ✓ Always check
  - `Vn = 0.6FyAwCv`
  - For plate girders, h/tw often > 2.24√(E/Fy), so Cv < 1.0

- [ ] **Shear Buckling** (G2.2) - ✓ If web is slender
  - Plate girders almost always have slender webs
  - Calculate Cv based on h/tw and a/h
  - May require transverse stiffeners

**If Transverse Stiffeners Provided**:
- [ ] **Stiffener Spacing** (G2.2) - ○ If stiffeners provided
  - Check a/h ratio
  - Optimize for maximum Cv

- [ ] **Stiffener Design** (G3.1) - ○ If stiffeners provided
  - Check stiffener moment of inertia: Ist
  - Check stiffener spacing: a
  - Detail stiffener connection to web

### C. Special Considerations

- [ ] **Tension Field Action** (G3.2) - ○ If desired for efficiency
  - Increases shear capacity beyond shear buckling
  - Requires transverse stiffeners
  - More complex analysis

- [ ] **Bearing Stiffeners** (G2.3) - ○ At concentrated loads
  - Required if web local yielding/crippling exceeded
  - Design as columns: Check axial + local buckling

---

## 5. Angles (Single and Double)

### A. Tension Members (AISC Chapter D)

- [ ] **Tensile Yielding** (D2) - ✓ Always check
  - `Pn = FyAg`

- [ ] **Tensile Rupture** (D2) - ✓ Always check (angles almost always have holes)
  - `Pn = FuAe`
  - Calculate Ae based on shear lag (U factor, Table D3.1)
  - Single angle: U = 1 - (x̄/L) ≥ 0.60
  - Double angles: U based on connection type

- [ ] **Block Shear Rupture** (J4.3) - ✓ At bolted connections
  - Check tension rupture + shear yielding
  - Check tension yielding + shear rupture
  - Use minimum

### B. Compression Members (AISC Chapter E)

**Single Angles**:
- [ ] **Flexural Buckling** (E5) - ✓ About geometric axes
  - Check x-x and y-y axes separately
  - Use effective length K based on connection type

- [ ] **Flexural-Torsional Buckling** (E5) - ✓ Always check for single angles
  - Critical for single angles (unsymmetric section)
  - `Pn = FcrAg` where Fcr based on flexural-torsional buckling
  - Often governs over flexural buckling

**Double Angles**:
- [ ] **Flexural Buckling** (E6) - ✓ About both axes
  - If back-to-back: Check as built-up member (E6)
  - If separated: Check effective slenderness including a/ri

- [ ] **Local Buckling** (E7) - ○ If slender legs
  - Check leg slenderness: b/t
  - Reduce Pn if slender

### C. Flexure (AISC Chapter F)

- [ ] **Yielding** (F10) - ✓ About minor axis (usually)
  - `Mn = 1.5My = 1.5FyZy` (compact sections)

- [ ] **Local Buckling** (F10) - ○ If slender leg
  - Check leg slenderness b/t
  - Reduce Mn if slender

---

## 6. Trusses

### A. Member Design

**Top Chord** (usually compression):
- [ ] **All compression checks from Section 2** - ✓
  - Flexural buckling (in-plane and out-of-plane)
  - Local buckling
  - Combined axial + moment if continuous top chord

**Bottom Chord** (usually tension):
- [ ] **All tension checks from Section 5A** - ✓
  - Tensile yielding
  - Tensile rupture (net area at connections)
  - Block shear rupture

**Web Members** (tension or compression):
- [ ] **Check as tension or compression member** - ✓
  - Diagonal braces: Usually compression (check flexural buckling)
  - Vertical members: Check based on loading direction

### B. Connections

- [ ] **Gusset Plate Yielding** (J4.1) - ✓ At all connections
  - Check gusset plate in tension (Whitmore section)
  - Check gusset plate in compression (Whitmore section + buckling)

- [ ] **Gusset Plate Buckling** (J4.4) - ✓ At compression member connections
  - Check gusset plate buckling
  - Provide sufficient thickness or edge stiffeners

- [ ] **Block Shear** (J4.3) - ✓ At all bolted connections
  - Critical for end connections

---

## 7. Connections (General)

### A. Bolted Connections (AISC Chapter J)

**Bolts in Shear**:
- [ ] **Bolt Shear Strength** (J3.7) - ✓ Always check
  - Single shear or double shear
  - φ = 0.75 (LRFD), Ω = 2.00 (ASD)

**Bolts in Tension**:
- [ ] **Bolt Tensile Strength** (J3.7) - ✓ If tension present
  - Check nominal tensile strength Fnt × Ab
  - φ = 0.75 (LRFD), Ω = 2.00 (ASD)

**Bolts in Combined Shear and Tension**:
- [ ] **Interaction Check** (J3.8) - ✓ If both present
  - Check elliptical interaction equation
  - Or use Table J3.2 (conservative)

**Bearing on Material**:
- [ ] **Bolt Bearing on Holes** (J3.11) - ✓ Always check
  - Check bearing and tear-out
  - `Rn = 1.2LctFu ≤ 2.4dtFu` (standard holes)

**Slip-Critical**:
- [ ] **Slip Resistance** (J3.9) - ○ If slip-critical required
  - Class A or B surface condition
  - φ = 1.00 (LRFD at service), Ω = 1.50 (ASD at service)

### B. Welded Connections (AISC Chapter J)

**Fillet Welds**:
- [ ] **Fillet Weld Shear Strength** (J2.4) - ✓ Always check
  - `Rn = FnwwAwe`
  - Fnww = 0.60FEXX (for all directions)
  - φ = 0.75 (LRFD), Ω = 2.00 (ASD)

- [ ] **Base Metal Shear Strength** (J4) - ✓ Check against weld strength
  - `Rn = 0.6FyABM` or `0.6FuABM`
  - Often governs for thin material with large weld

**Complete Joint Penetration (CJP) Groove Welds**:
- [ ] **CJP Weld Strength** (J2.4) - ✓ Match base metal
  - Designed to match base metal strength
  - Check tension, compression, shear as for base metal

**Partial Joint Penetration (PJP) Groove Welds**:
- [ ] **PJP Weld Strength** (J2.4) - ✓ Based on effective throat
  - Calculate effective throat based on joint type
  - Check tension (perpendicular to axis), shear, compression

### C. Shear Connections (AISC Chapter J)

**Single-Plate (Shear Tab)**:
- [ ] **Bolt Shear** - ✓
- [ ] **Bolt Bearing** - ✓
- [ ] **Plate Shear Yielding** (J4.2) - ✓
  - `Rn = 0.6FyAgv`
- [ ] **Plate Shear Rupture** (J4.2) - ✓
  - `Rn = 0.6FuAnv`
- [ ] **Block Shear** (J4.3) - ✓

**Double-Angle Connection**:
- [ ] **All bolt checks** - ✓
- [ ] **Angle leg shear yielding** - ✓
- [ ] **Angle leg shear rupture** - ✓
- [ ] **Block shear** - ✓

**End-Plate Connection**:
- [ ] **Bolt tension** - ✓ (moment connection)
- [ ] **End plate bending** (flexural yielding) - ✓
- [ ] **End plate prying action** (J3.9) - ✓
- [ ] **Bolt shear** (if shear present) - ✓

---

## 8. Base Plates

- [ ] **Concrete Bearing** (J8) - ✓ Always check
  - `Pp = 0.85f'cA1√(A2/A1)` ≤ `1.7f'cA1`
  - A1 = base plate area, A2 = supporting concrete area

- [ ] **Base Plate Bending** (J8) - ✓ Always check
  - Check cantilever distance from column face
  - Required thickness: `tp,req = l√(2Pu/(0.9FyBN))`

- [ ] **Anchor Rod Tension** (J9) - ✓ If uplift or moment
  - Check anchor rod tensile strength
  - Check anchor rod embedment/development (ACI 318)

- [ ] **Anchor Rod Shear** (J9) - ○ If shear present
  - Check anchor rod shear strength
  - Provide shear lug if shear exceeds capacity

---

## 9. Braced Frame Connections

**For SCBF (Special Concentrically Braced Frames)**:

- [ ] **Brace Strength** (AISC 341 F2.3) - ✓
  - Design for expected strength: RyFyAg (tension), 1.1RyPn (compression)

- [ ] **Gusset Plate Design** (AISC 341 F2.6c) - ✓
  - Check 2tp linear limit (gusset plate free edge)
  - Check gusset buckling (Thornton or Whitmore method)
  - Check block shear
  - Check net section rupture

- [ ] **Brace Connection Ductility** (AISC 341 F2.6c) - ✓
  - Ensure connection capacity > brace expected strength
  - Φ = 1.0, Ω = 1.0 for seismic (no resistance factors)

- [ ] **Column Strength at Connection** - ✓
  - Check column local effects (web crippling, yielding)
  - Provide stiffeners if needed

**For OCBF (Ordinary Concentrically Braced Frames)**:
- [ ] Similar checks but with AISC 360 only (not AISC 341 requirements)

---

## Summary Checklist by Design Phase

### Preliminary Design
- [ ] Select member type (W-shape, HSS, plate girder, etc.)
- [ ] Select steel grade (A992, A500, A572, etc.)
- [ ] Estimate size based on span/load
- [ ] Check basic strength (flexure, axial, shear)

### Detailed Design
- [ ] Verify all applicable limit states from above
- [ ] Check deflection and serviceability
- [ ] Design connections
- [ ] Check local effects (web crippling, bearing, etc.)

### Final Checks
- [ ] Verify all AISC limit states satisfied
- [ ] Check constructability (clearances, bolt spacing, etc.)
- [ ] Confirm material availability
- [ ] Review details with fabricator

---

**Last Updated**: 2025-11-10
**Reference**: AISC 360-22 Specification for Structural Steel Buildings
**Note**: This checklist is comprehensive but not exhaustive. Always consult AISC 360-22 for specific provisions and use engineering judgment.
