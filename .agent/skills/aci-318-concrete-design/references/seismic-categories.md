# ACI 318-25 Seismic Design Categories

*Quick Reference for Earthquake-Resistant Concrete Design*

---

## Overview

Seismic Design Categories (SDC) are determined by ASCE 7 based on:
1. **Seismicity** of the region (mapped ground motion parameters)
2. **Risk Category** of the structure (I, II, III, or IV)
3. **Site Class** (soil conditions)

ACI 318-25 Chapter 17 provides design requirements based on SDC assignment.

---

## Seismic Design Category Levels

### SDC A - Minimal Seismic Risk
**Seismicity**: Very low ground motion
**Requirements**: Minimal seismic provisions
**Chapter 17 Applies**: **NO**

### SDC B - Low Seismic Risk
**Seismicity**: Low ground motion
**Requirements**: Basic seismic provisions
**Chapter 17 Applies**: **Limited** (only 17.2)

### SDC C - Moderate Seismic Risk
**Seismicity**: Moderate ground motion
**Requirements**: Intermediate seismic provisions
**Chapter 17 Applies**: **YES** (17.2 through 17.9)

### SDC D, E, F - High to Very High Seismic Risk
**Seismicity**: High to very high ground motion
**Requirements**: Comprehensive seismic provisions
**Chapter 17 Applies**: **YES** (Full Chapter 17)

---

## ACI 318-25 Chapter 17 Applicability

| SDC | Chapter 17 | Key Requirements |
|-----|------------|------------------|
| **A** | Not applicable | Design per other chapters only |
| **B** | 17.2 only | Minimum reinforcement, basic detailing |
| **C** | 17.2 - 17.9 | Intermediate moment frames, moderate detailing |
| **D, E, F** | Full Chapter | Special systems, stringent detailing |

---

## Structural System Classification

### For SDC A and B
**Ordinary Systems Permitted**:
- Ordinary moment frames (OMF)
- Ordinary reinforced concrete walls
- Basic detailing per Chapters 7-13

### For SDC C
**Intermediate Systems Required**:
- **Intermediate moment frames (IMF)**
- **Ordinary reinforced concrete structural walls**
- Enhanced detailing requirements

### For SDC D, E, F
**Special Systems Required** (one or more of):
- **Special moment frames (SMF)**
- **Special reinforced concrete structural walls (SRCSW)**
- **Special structural walls with coupling beams**
- Most stringent detailing requirements

---

## Moment Frame Systems

### Ordinary Moment Frames (OMF)
**Permitted**: SDC A, B
**Requirements**:
- Design per Chapters 6, 9, 10
- Minimum Chapter 17.2 requirements (SDC B only)
- No special ductility detailing

### Intermediate Moment Frames (IMF)
**Permitted**: SDC A, B, C
**Requirements** (ACI 318-25 Section 17.6):
- Beam longitudinal reinforcement:
  - Top and bottom reinforcement at joints
  - Positive moment capacity ≥ 1/2 negative capacity
- Transverse reinforcement:
  - Stirrups/hoops at beam ends
  - Spacing requirements
- Column requirements:
  - Transverse reinforcement at beam-column joints
  - Minimum flexural strength requirements

### Special Moment Frames (SMF)
**Permitted**: SDC A, B, C, D, E, F
**Required**: SDC D, E, F (if moment frame system chosen)

**Requirements** (ACI 318-25 Section 17.5):

**Beams** (17.5.2):
- Positive moment strength ≥ 1/2 negative moment strength
- Neither positive nor negative ≥ 1/4 maximum moment at joint
- Hoops required at beam ends (confinement zone)
- Transverse reinforcement spacing limits
- Maximum longitudinal spacing of hoops

**Columns** (17.5.3):
- Strong-column/weak-beam requirement
- Confinement reinforcement at potential plastic hinge regions
- Hoop spacing:
  - d/4 (minimum)
  - 6 × longitudinal bar diameter
  - So per 17.5.3.2 (based on confinement)
- Minimum of 3 hoops at top and bottom

**Beam-Column Joints** (17.5.4):
- Transverse reinforcement throughout joint
- Shear strength verification
- Confinement requirements

---

## Structural Wall Systems

### Ordinary Reinforced Concrete Walls
**Permitted**: SDC A, B, C
**Requirements**:
- Design per Chapter 11
- Minimum Chapter 17.2 requirements
- Basic reinforcement detailing

### Special Reinforced Concrete Structural Walls (SRCSW)
**Permitted**: All SDC
**Required**: SDC D, E, F (if wall system chosen)

**Requirements** (ACI 318-25 Section 17.7):

**General** (17.7.2):
- Distributed reinforcement (horizontal and vertical)
- Minimum reinforcement ratios
- Maximum reinforcement spacing

**Boundary Elements** (17.7.6):
**When Required**:
- Compression zone depth exceeds critical limit
- High axial load + displacement

**Boundary Element Detailing**:
- Confinement by hoops or spirals
- Hoop spacing ≤ min(6", 6 × long. bar dia)
- Extend boundary elements beyond critical compression zone
- Length requirements based on neutral axis depth

**Coupling Beams** (17.7.7):
- Special detailing for beams connecting walls
- Diagonal reinforcement option for high shear demand
- Confinement requirements

---

## Key Detailing Requirements by SDC

### SDC A
- **No Chapter 17 requirements**
- Design per Chapters 1-16, 18-27

### SDC B
**17.2 Requirements**:
- Minimum flexural reinforcement in beams and columns
- Minimum transverse reinforcement
- Development and splicing requirements
- Frame member joint requirements (basic)

### SDC C
**All SDC B Requirements PLUS**:

**Intermediate Moment Frames** (17.6):
- Enhanced beam reinforcement detailing
- Stirrup/hoop requirements at beam ends
- Column transverse reinforcement at joints
- Strong column provisions (modified)

**Walls** (17.9):
- Distributed reinforcement requirements
- Reinforcement ratio limits
- Development and splicing

### SDC D, E, F
**All SDC C Requirements PLUS**:

**Special Moment Frames** (17.5):
- Comprehensive confinement requirements
- Stringent hoop spacing
- Strong-column/weak-beam ratio
- Plastic hinge detailing
- Joint shear verification

**Special Structural Walls** (17.7):
- Boundary element requirements
- Confinement reinforcement
- Coupling beam special detailing
- Shear strength requirements

**Diaphragms** (17.8):
- Enhanced reinforcement requirements
- Collector/chord elements
- Openings and discontinuities

---

## Quick Reference: System Selection

### I need to design a moment-resisting frame:

**SDC A**: Use Ordinary Moment Frame (OMF)
**SDC B**: Use Ordinary Moment Frame (OMF) + 17.2
**SDC C**: Use Intermediate Moment Frame (IMF) per 17.6
**SDC D/E/F**: Use Special Moment Frame (SMF) per 17.5

### I need to design a structural wall:

**SDC A**: Ordinary wall per Chapter 11
**SDC B**: Ordinary wall per Chapter 11 + 17.2
**SDC C**: Ordinary wall per Chapter 11 + 17.9
**SDC D/E/F**: Special Structural Wall per 17.7

---

## Critical Dimensions and Limits

### Special Moment Frame Beams

| Parameter | Requirement | Reference |
|-----------|-------------|-----------|
| Clear span | ≥ 4 × effective depth | 17.5.2.1 |
| Width-to-depth ratio | Width ≥ 0.3 × depth | 17.5.2.1 |
| Width | ≥ 10 in | 17.5.2.1 |
| Width | ≤ column width + 1.5h | 17.5.2.1 |

### Special Moment Frame Columns

| Parameter | Requirement | Reference |
|-----------|-------------|-----------|
| Shortest cross-sectional dimension | ≥ 12 in | 17.5.3.1 |
| Ratio of shortest to perpendicular dimension | ≥ 0.4 | 17.5.3.1 |

### Special Structural Walls

| Parameter | Requirement | Reference |
|-----------|-------------|-----------|
| Thickness | ≥ hw/25 (unsupported) | 11.5.3.1 |
| Thickness | ≥ 4 in | 17.7.2.1 |
| Reinforcement ratio (ρl and ρt) | ≥ 0.0025 | 17.7.2.1 |
| Spacing of distributed reinforcement | ≤ 18 in | 17.7.2.3 |

---

## Boundary Element Triggers (Special Walls)

**Boundary elements required when**:

```
c > lw / (600(δu/hw))
```

Where:
- c = neutral axis depth
- lw = wall length
- δu = design displacement
- hw = wall height

**Alternative**: Use detailed analysis per 17.7.6.2

**If required**:
- Extend beyond c by distance ≥ max(c - 0.1lw, c/2)
- Confine with hoops or spirals
- Continue development into foundation

---

## Confinement Reinforcement Requirements

### Special Moment Frame Columns

**Volumetric Ratio** (ρs):

```
ρs ≥ max(0.09 × fc'/fyh, Ash/sbc × fc'/fyh)
```

**Spacing of Hoops** (s):

```
s ≤ min(d/4, 6db, so)
```

Where so is calculated based on confinement requirements

### Special Structural Wall Boundary Elements

Similar requirements as columns for confined regions

---

## Strong-Column/Weak-Beam Requirement

**For Special Moment Frames** (17.5.3.2):

```
ΣMnc ≥ (6/5) × ΣMnb
```

Where:
- ΣMnc = sum of nominal flexural strengths of columns at joint
- ΣMnb = sum of nominal flexural strengths of beams at joint

**Exception**: Need not be satisfied for:
- Columns with factored axial force < Ag × fc'/10
- Two-story frames meeting specific criteria

---

## Shear Strength Requirements

### Special Moment Frame Beams

**Design shear force**:

```
Ve = (Mpr+ + Mpr-)/ln + wgravity × ln/2
```

Where:
- Mpr = probable moment strength at beam ends
- ln = clear span

### Special Moment Frame Columns

**Design shear force**:

```
Ve = (Mpr,top + Mpr,bottom)/ln
```

### Beam-Column Joints

**Nominal shear strength**:

```
Vn = γ × λ × √fc' × Aj
```

Where:
- γ = joint geometry factor (20, 15, or 12 depending on confinement)
- Aj = effective joint area

---

## Summary Table: SDC Requirements

| SDC | Moment Frames | Structural Walls | Chapter 17 Sections |
|-----|---------------|------------------|---------------------|
| **A** | Ordinary (OMF) | Ordinary | Not applicable |
| **B** | Ordinary (OMF) | Ordinary | 17.2 |
| **C** | Intermediate (IMF) | Ordinary | 17.2, 17.6, 17.9 |
| **D** | Special (SMF) | Special (SRCSW) | 17.2-17.10 (full) |
| **E** | Special (SMF) | Special (SRCSW) | 17.2-17.10 (full) |
| **F** | Special (SMF) | Special (SRCSW) | 17.2-17.10 (full) |

---

## Common Design Flowchart

```
DETERMINE SDC (from ASCE 7)
  ↓
SDC A → No Chapter 17 → Design per Chapters 6-11
  ↓
SDC B → Apply 17.2 → OMF or Ordinary Walls
  ↓
SDC C → Apply 17.2, 17.6, 17.9 → IMF or Ordinary Walls
  ↓
SDC D/E/F → Apply Full Chapter 17 → SMF or SRCSW
  ↓
DETERMINE SYSTEM (Moment Frame vs Wall vs Dual)
  ↓
APPLY DETAILING REQUIREMENTS
  ↓
- Confinement reinforcement
- Boundary elements (if walls)
- Development lengths
- Splices
- Joint reinforcement
  ↓
VERIFY STRENGTH
  ↓
- Strong-column/weak-beam (if SMF)
- Joint shear
- Member shear
- Flexural strength
```

---

## Critical Notes

1. **SDC Determination**: Not part of ACI 318; determined by ASCE 7

2. **Mixed Systems**: Different SDC requirements may apply to different parts of structure

3. **Irregularities**: ASCE 7 may impose additional requirements

4. **Material Requirements**:
   - SDC C, D, E, F: fc' ≥ 3,000 psi
   - SDC D, E, F with lightweight concrete: fc' ≥ 4,000 psi

5. **Reinforcement**:
   - Deformed bars required for primary reinforcement
   - fy ≤ 80,000 psi (typically)

6. **Construction**: Special inspection required for SDC C, D, E, F

---

*For complete requirements, consult ACI 318-25 Chapter 17: Earthquake-Resistant Structures*
