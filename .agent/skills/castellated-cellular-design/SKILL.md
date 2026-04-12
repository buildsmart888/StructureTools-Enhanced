---
name: castellated-cellular-design
description: "AISC Design Guide 31 (Castellated and Cellular Beam Design) 검색 및 구조계산 수행, 설계 워크플로우 제공. 허니컴보, 비렌딜굽힘, 웹포스트좌굴, CB/LB 설계 관련 질문에 즉시 활성화. 공식 추출, 예제 매칭, 기하학 계산, 용어 설명, 기호 정의 지원."
---

# AISC Design Guide 31: Castellated and Cellular Beam Design Expert

Use this skill when users ask questions about castellated beams, cellular beams, honeycomb beams, Vierendeel bending, web post buckling, hexagonal or circular web openings, or any structural design queries related to AISC Design Guide 31.

## Trigger Keywords

**English**: castellated beam, cellular beam, honeycomb beam, web opening, hexagonal opening, circular opening, Vierendeel bending, Vierendeel moment, web post buckling, web post, AISC DG31, Design Guide 31, CB beam, LB beam, composite castellated, composite cellular, beam with openings, perforated beam, expanded beam, fabricated beam with openings

**Korean**: 허니컴보, 캐스텔레이티드보, 셀룰러보, 육각형개구부, 원형개구부, 웹개구부, 비렌딜모멘트, 비렌딜굽힘, 웹포스트좌굴, 웹포스트, 개구부보, 천공보, 확장보, 합성캐스텔레이티드보, 합성셀룰러보

## Tools Required

- **Grep**: Search for keywords in Design Guide 31 documents
- **Read**: Read specific chapters, examples, and reference files
- **Glob**: Pattern matching to find files
- **Bash**: Execute Python scripts for searches and calculations
- **Write**: (Optional) Save calculation results or reports

## Document Structure

This skill provides access to **comprehensive castellated and cellular beam design documentation**:

### 1. Chapter 1: Introduction
**Location**: `data/design-guide/Chapter_1_Introduction.md`

**Purpose**: Understand **what** castellated and cellular beams are - history, manufacturing, nomenclature

**Contents**:
- **1.1 History**: Evolution from castellated (1910s) to cellular (1980s) beams
- **1.2 Manufacturing Methods**: Cutting patterns, expansion ratios, fabrication techniques
  - Castellated: Hexagonal cutting pattern with 60° angles
  - Cellular: Circular cutting pattern with CNC precision
- **1.3 Nomenclature and Geometry**:
  - CB (Castellated Beam) terminology: dg (depth), e (expansion ratio), s (spacing), a (hole width)
  - LB (Long-span/Cellular Beam) terminology: do (opening diameter), So (center-to-center spacing)
  - Tee sections, web posts, top and bottom chords

### 2. Chapter 2: Use Cases and Applications
**Location**: `data/design-guide/Chapter_2_Use_Cases.md`

**Purpose**: Learn **when and why** to use castellated/cellular beams

**Topics**:
- **2.1 Typical Applications**: Parking garages, residential buildings, commercial buildings
- **2.2 Advantages**:
  - Increased depth without added weight (20-50% depth increase)
  - MEP integration through openings
  - Material efficiency, architectural appeal
- **2.3 Special Considerations**:
  - Deflection reduction (90% effective Ix)
  - Complex failure modes (Vierendeel, web post buckling)
  - Fabrication costs vs material savings
  - Composite vs noncomposite behavior

### 3. Chapter 3: Design Procedures
**Location**: `data/design-guide/Chapter_3_Design_Procedures.md`

**Purpose**: **How to design** - formulas, procedures, limit states

**Sections**:
- **3.1 General Principles**: Limit states, LRFD and ASD methods, AISC Specification integration
- **3.2 Flexural Strength**:
  - Vierendeel mechanism (unique to web openings)
  - Moment redistribution, plastic hinge formation
- **3.3 Web Post Buckling**:
  - Critical spacing criteria
  - Slenderness limits (h/tw, s/h ratios)
  - Elastic and inelastic buckling
- **3.4 Shear Strength**:
  - Tee section shear capacity
  - Web post shear resistance
- **3.5 Lateral-Torsional Buckling**: Modified procedures for reduced Iy
- **3.6 Deflection**:
  - Effective moment of inertia (Ieff ≈ 0.9 Ix)
  - Vierendeel deformation effects
  - Simplified calculation methods
- **3.7 Composite Action**: Interaction with concrete slab, shear connector design
- **3.8 Special Checks**: End reactions, connection design, opening reinforcement

### 4. Design Examples (Chapter 4)
**Location**: `data/examples/`

**Purpose**: See **worked examples** with complete step-by-step calculations

**Examples**:
- **Example 4.1**: Noncomposite Castellated Beam (CB)
  - File: `Example_4-1_Noncomposite_Castellated.md`
  - Given beam, determine capacity
  - All limit states checked (Vierendeel, web post, shear, LTB, deflection)

- **Example 4.2**: Noncomposite Cellular Beam (LB)
  - File: `Example_4-2_Noncomposite_Cellular.md`
  - Circular openings vs hexagonal
  - Geometry differences highlighted

- **Example 4.3**: Composite Castellated Beam (CB)
  - File: `Example_4-3_Composite_Castellated.md`
  - Concrete slab interaction
  - Positive moment region design

- **Example 4.4**: Composite Cellular Beam (LB)
  - File: `Example_4-4_Composite_Cellular.md`
  - Full composite action
  - Deflection calculations with composite properties

**Key Distinction**:
- **Chapter 1** → "What is a castellated/cellular beam?" "How are they made?"
- **Chapter 2** → "When should I use them?" "What are the advantages?"
- **Chapter 3** → "How do I design them?" "What formulas do I use?"
- **Examples** → "Show me a complete calculation step-by-step"

## Reference Files

This skill includes comprehensive reference materials:

- `references/symbols.md`: Complete symbols table (mathematical notation for DG31)
- `references/glossary.md`: Technical terms and definitions (Vierendeel, web post, etc.)
- `references/abbreviations.md`: CB, LB, DG31, AISC, LRFD, ASD, etc.
- `references/examples-index.md`: Complete example index (4 examples with cross-references)
- `references/failure-modes-guide.md`: **Quick reference for all failure modes** (Vierendeel, web post, shear, LTB)
- `references/geometry-guide.md`: **Geometric relationships and calculation formulas** (CB vs LB)
- `references/design-workflow-summary.md`: **Step-by-step design process flowchart**
- `references/bibliography.md`: Research papers, historical references, AISC publications

## Automation Scripts

Python scripts are available in `scripts/` directory:
- `smart_search.py`: Category-aware keyword search (planned)
- `formula_finder.py`: Extract formulas with context (planned)
- `example_matcher.py`: Match user queries to appropriate examples (planned)
- `geometry_calculator.py`: **CB/LB geometry calculations** (opening sizes, spacing, depths) (planned)
- `vierendeel_calculator.py`: **Vierendeel moment and stress calculations** (planned)
- `web_post_checker.py`: **Web post buckling verification** (planned)

---

# Workflow by Query Type

## 1. Formula Query (공식 질의)

**User Intent**: Find a specific formula or equation from AISC Design Guide 31.

**Example Queries**:
- "What is the formula for Vierendeel moment in castellated beams?"
- "Show me the web post buckling equation"
- "허니컴보의 비렌딜모멘트 공식을 알려줘"
- "웹포스트 좌굴 검토식은?"

**Quick Process**:
1. Identify topic (Vierendeel → Section 3.2, web post → Section 3.3, deflection → Section 3.6, etc.)
2. Grep relevant section in `data/design-guide/Chapter_3_Design_Procedures.md`
3. Extract formula with variable definitions from `references/symbols.md`
4. **Note beam type dependency**: Check if formula differs for CB vs LB
5. **Note composite vs noncomposite**: Different formulas may apply
6. Present with AISC DG31 citation (e.g., "AISC Design Guide 31, Section 3.2")

**Keywords**: formula, equation, 공식, 계산식, expression

---

## 2. Design Example Query (예제 질의)

**User Intent**: See a step-by-step worked example of a castellated or cellular beam design.

**Example Queries**:
- "Show me how to design a castellated beam"
- "I need an example of cellular beam design with composite action"
- "허니컴보 설계 예제를 보여줘"
- "합성 셀룰러보 계산 과정은?"

**Quick Process**:
1. Check `references/examples-index.md` for example number
2. Identify appropriate example:
   - **Example 4.1**: Noncomposite Castellated (CB)
   - **Example 4.2**: Noncomposite Cellular (LB)
   - **Example 4.3**: Composite Castellated (CB)
   - **Example 4.4**: Composite Cellular (LB)
3. Read from corresponding file in `data/examples/`
4. Present step-by-step with complete calculations
5. Note specific considerations:
   - Opening geometry (hexagonal vs circular)
   - Composite action (if applicable)
   - All limit states checked

**Keywords**: example, 예제, how to, step-by-step, 설계과정, worked example

---

## 3. Calculation Query (계산 질의)

**User Intent**: Perform structural calculations using AISC DG31 formulas.

**Example Queries**:
- "Calculate Vierendeel moment: W16x26 castellated, e=1.5, span=30ft"
- "Check web post buckling: spacing=18in, height=24in, tw=0.25in"
- "캐스텔레이티드보 W18x35, 확장비 1.4, 처짐을 계산해줘"
- "웹포스트 좌굴 검토: 간격 450mm, 높이 600mm"

**Quick Process**:
1. **Identify beam type** - CB (castellated) or LB (cellular)
2. **Identify composite action** - composite or noncomposite
3. **Gather geometry**:
   - Parent section (W-shape)
   - Expansion ratio (e) or opening diameter (do)
   - Spacing (s or So)
   - Span length (L)
4. Find formula from Chapter 3 (use Formula Query workflow)
5. Find similar example from Chapter 4 for methodology
6. Generate Python code following example structure
7. Execute and validate against AISC DG31 limits

**Critical Checks**:
- ✅ Beam type specified (CB or LB)
- ✅ Composite action clarified
- ✅ Opening geometry defined (hexagonal or circular)
- ✅ Spacing verified (not too close → web post buckling)
- ✅ Deflection reduction applied (Ieff ≈ 0.9 Ix)
- ✅ All failure modes checked (Vierendeel, web post, shear, LTB)

**Keywords**: calculate, compute, determine, 계산, 산정, 구해줘, check, verify

---

## 4. Geometry/Nomenclature Query (기하학/용어 질의)

**User Intent**: Understand geometric relationships and terminology for castellated/cellular beams.

**Example Queries**:
- "What is the expansion ratio for castellated beams?"
- "How do you calculate the expanded depth dg?"
- "Explain web post geometry"
- "확장비가 뭐야?"
- "웹포스트 높이를 어떻게 구하나요?"

**Quick Process**:
1. Check `references/geometry-guide.md` for quick reference
2. Check `references/glossary.md` for term definitions
3. If not found, search Chapter 1.3 (Nomenclature) in `Chapter_1_Introduction.md`
4. Present definition with diagram references
5. **Distinguish CB vs LB geometry**:
   - **CB (Castellated)**: hexagonal, expansion ratio (e), opening width (a), height (ho)
   - **LB (Cellular)**: circular, opening diameter (do), center spacing (So)
6. Provide calculation formulas from geometry-guide.md

**Common Geometric Terms**:
- **e (expansion ratio)**: Typical 1.3-1.5 for CB, ratio of final depth to parent depth
- **dg (expanded depth)**: dg = e × d (parent depth)
- **s (spacing)**: Center-to-center distance between openings
- **do (opening diameter)**: For cellular beams (LB)
- **Web post**: Solid portion between openings (critical for buckling)
- **Tee sections**: Top and bottom chords formed by cutting

**Keywords**: geometry, nomenclature, expansion ratio, 기하학, 형상, 확장비, web post, opening

---

## 5. Comparison Query (비교 질의)

**User Intent**: Compare castellated vs cellular, or composite vs noncomposite designs.

**Example Queries**:
- "Castellated vs cellular beams - which should I use?"
- "Compare composite and noncomposite cellular beams"
- "허니컴보와 셀룰러보의 차이는?"
- "합성보와 비합성보 중 어느 것이 유리한가?"

**Quick Process**:
1. Identify comparison type:
   - **CB vs LB** (beam type)
   - **Composite vs noncomposite** (slab interaction)
   - **Opening shapes** (hexagonal vs circular)
2. Search Chapter 2 for advantages/disadvantages
3. Use `references/geometry-guide.md` for geometric differences
4. Present in comparison table format
5. Reference examples for practical context

**CB (Castellated) vs LB (Cellular) Comparison**:

| Feature | Castellated Beam (CB) | Cellular Beam (LB) | Notes |
|---------|----------------------|-------------------|-------|
| **Opening Shape** | Hexagonal (60° angles) | Circular | LB easier for MEP routing |
| **Fabrication** | Zig-zag cut, weld together | CNC circular cuts | CB more traditional |
| **Expansion Ratio** | Typically 1.3-1.5 | Typically 1.25-1.4 | CB generally higher |
| **Stress Concentration** | Higher at corners | Lower (smooth edges) | LB advantage |
| **Vierendeel Effect** | More pronounced | Less pronounced | LB simpler analysis |
| **Web Post Shape** | Diamond/hexagonal | Rectangular | Affects buckling |
| **Typical Applications** | Moderate spans | Long spans | LB name origin |
| **MEP Integration** | Good | Excellent | Circular better for ducts |

**Composite vs Noncomposite Comparison**:

| Feature | Composite | Noncomposite | Notes |
|---------|-----------|--------------|-------|
| **Strength** | Higher (concrete contributes) | Lower (steel only) | Composite 30-50% stronger |
| **Deflection** | Lower (higher stiffness) | Higher | Composite critical advantage |
| **Complexity** | More complex (shear studs) | Simpler | Analysis and construction |
| **Cost** | Higher initial | Lower initial | Composite better long-term |
| **Applications** | Buildings with slabs | Exposed beams | Typical context |
| **Shear Connectors** | Required | N/A | Design consideration |

**Keywords**: compare, difference, vs, 차이, 비교, advantage, disadvantage

---

## 6. Failure Mode Query (파괴모드 질의)

**User Intent**: Understand failure mechanisms specific to castellated/cellular beams.

**Example Queries**:
- "What is Vierendeel bending?"
- "Explain web post buckling"
- "What failure modes do I need to check for honeycomb beams?"
- "비렌딜굽힘이 뭐야?"
- "웹포스트 좌굴은 왜 중요한가요?"

**Quick Process**:
1. Check `references/failure-modes-guide.md` for quick reference
2. Search Chapter 3 for detailed design procedures
3. Present failure mode with:
   - **Mechanism description**
   - **Why it's unique to web openings**
   - **Design check procedure**
   - **Formula reference**
4. Cross-reference to examples showing the check

**Critical Failure Modes for CB/LB**:

1. **Vierendeel Bending** (Section 3.2):
   - **Mechanism**: Local moments at opening corners due to shear transfer across opening
   - **Unique to**: Beams with web openings (no continuous web to resist shear)
   - **Check**: Combined stress at tee sections (flange + Vierendeel moment)
   - **Formula**: MV = V × eT (Vierendeel moment from shear)

2. **Web Post Buckling** (Section 3.3):
   - **Mechanism**: Compression strut between openings buckles like a column
   - **Unique to**: Closely spaced openings (s/h ratio critical)
   - **Check**: Slenderness ratio, critical stress
   - **Formula**: λ = (h/tw) × √(Fy/E) (web post slenderness)

3. **Shear Strength** (Section 3.4):
   - **Mechanism**: Tee section shear capacity at opening
   - **Different from**: Solid web shear (reduced area)
   - **Check**: Tee web shear capacity
   - **Formula**: Vn = 0.6 × Fy × Aw (tee web area)

4. **Lateral-Torsional Buckling** (Section 3.5):
   - **Mechanism**: Similar to solid beams but reduced Iy affects capacity
   - **Modified for**: Reduced web area (openings)
   - **Check**: Modified LTB equations with reduced Iy
   - **Formula**: Standard AISC Chapter F with adjusted properties

5. **Deflection** (Section 3.6):
   - **Mechanism**: Vierendeel deformation adds to beam deflection
   - **Critical for**: Low E/I ratio, service loads
   - **Check**: Use effective Ix (typically 90% of gross)
   - **Formula**: Δ = (5wL⁴)/(384 × E × Ieff) where Ieff ≈ 0.9 Ix

6. **Local Web Yielding** (Section 3.8):
   - **Mechanism**: High stresses at opening corners
   - **Check**: Opening reinforcement if needed
   - **Common at**: End reactions, concentrated loads

**Keywords**: failure mode, Vierendeel, web post buckling, 파괴모드, 비렌딜, 좌굴, mechanism

---

## 7. Application/Use Case Query (적용사례 질의)

**User Intent**: Understand where and when to use castellated/cellular beams.

**Example Queries**:
- "When should I use castellated beams?"
- "What are typical applications for cellular beams?"
- "Are honeycomb beams suitable for parking garages?"
- "허니컴보를 어디에 사용하나요?"
- "셀룰러보의 장단점은?"

**Quick Process**:
1. Search Chapter 2 (Use Cases) for applications
2. Reference Section 2.2 (Advantages) and 2.3 (Considerations)
3. Present typical applications with design considerations
4. Note when **NOT** to use (limitations)
5. Cross-reference to examples for similar cases

**Typical Applications** (from Chapter 2.1):

1. **Parking Garages**:
   - Long spans (40-60 ft typical)
   - MEP integration critical
   - Usually noncomposite
   - Example: Example 4.1 or 4.2

2. **Residential Buildings**:
   - Floor beams with utilities
   - Depth constraints (ceiling height)
   - Often composite with concrete slab
   - Example: Example 4.3 or 4.4

3. **Commercial Buildings**:
   - Office floors, retail
   - HVAC duct routing through openings
   - Architectural exposure possible
   - Composite or noncomposite

4. **Industrial Facilities**:
   - Equipment platforms
   - Utilities pass through openings
   - Moderate spans

**Advantages** (from Chapter 2.2):
- ✅ **Increased depth** without added weight (20-50% depth increase)
- ✅ **MEP integration** - utilities pass through openings
- ✅ **Material efficiency** - reuse parent section material
- ✅ **Reduced floor height** - services within beam depth
- ✅ **Architectural appeal** - exposed structure aesthetic

**Special Considerations** (from Chapter 2.3):
- ⚠️ **Deflection reduction** - Effective Ix only ~90% of gross Ix
- ⚠️ **Complex analysis** - Multiple failure modes (Vierendeel, web post)
- ⚠️ **Fabrication cost** - Cutting and welding labor intensive
- ⚠️ **Not suitable for**:
  - Heavy concentrated loads (unless reinforced)
  - Short spans (not economical)
  - High shear regions near supports
  - Dynamic/seismic critical applications (without special detailing)

**Keywords**: application, use case, when to use, 적용, 사용처, suitable, typical

---

# Quick Reference Tables

## Document Categories

| Type | Location | Files | Purpose |
|------|----------|-------|---------|
| **Chapter 1: Introduction** | data/design-guide/ | Chapter_1 | History, manufacturing, nomenclature |
| **Chapter 2: Use Cases** | data/design-guide/ | Chapter_2 | Applications, advantages, considerations |
| **Chapter 3: Design Procedures** | data/design-guide/ | Chapter_3 | Formulas, procedures, limit states |
| **Examples (Chapter 4)** | data/examples/ | 4 examples | Step-by-step calculations |
| **References** | references/ | 8 files | Symbols, glossary, geometry, workflows |

## Common Search Patterns

| Topic | Keywords | Chapter/Section | Examples Location | Unique Considerations |
|-------|----------|----------------|-------------------|----------------------|
| **Vierendeel Bending** | Vierendeel, local moment, tee stress | Chapter 3.2 | All 4 examples | Unique to web openings |
| **Web Post Buckling** | web post, buckling, spacing, slenderness | Chapter 3.3 | Examples 4.1, 4.2 | Critical spacing check |
| **Geometry** | expansion ratio, depth, spacing, opening | Chapter 1.3 | All examples | CB vs LB different |
| **Deflection** | deflection, serviceability, Ieff | Chapter 3.6 | Examples 4.3, 4.4 | 90% Ix reduction factor |
| **Composite Action** | composite, shear stud, concrete slab | Chapter 3.7 | Examples 4.3, 4.4 | Only composite examples |
| **Shear Strength** | shear, tee section, Vn | Chapter 3.4 | All examples | Reduced web area |
| **Manufacturing** | fabrication, cutting, welding | Chapter 1.2 | - | CB vs LB different cuts |
| **Applications** | parking, residential, MEP, utilities | Chapter 2.1 | - | Context for design |

## Chapter-to-Example Mapping

| Design Guide Chapter | Topic | Example 4.1 (NC-CB) | Example 4.2 (NC-LB) | Example 4.3 (C-CB) | Example 4.4 (C-LB) |
|---------------------|-------|-------------------|-------------------|------------------|------------------|
| **1.2 Manufacturing** | Cutting patterns | Hexagonal | Circular | Hexagonal | Circular |
| **1.3 Nomenclature** | Geometry | CB terms | LB terms | CB terms | LB terms |
| **2.1 Applications** | Use cases | Parking garage | Long-span floor | Residential | Commercial |
| **3.2 Vierendeel** | Flexural strength | ✅ Checked | ✅ Checked | ✅ Checked | ✅ Checked |
| **3.3 Web Post** | Buckling | ✅ Checked | ✅ Checked | ✅ Checked | ✅ Checked |
| **3.4 Shear** | Shear strength | ✅ Checked | ✅ Checked | ✅ Checked | ✅ Checked |
| **3.5 LTB** | Lateral buckling | ✅ Checked | ✅ Checked | ✅ Checked | ✅ Checked |
| **3.6 Deflection** | Serviceability | ✅ Checked | ✅ Checked | ✅ Checked | ✅ Checked |
| **3.7 Composite** | Slab interaction | N/A | N/A | ✅ Applied | ✅ Applied |

**Legend**: NC = Noncomposite, C = Composite, CB = Castellated Beam, LB = Cellular Beam (Long-span)

## Units Convention

| Quantity | AISC Unit | Symbol | Notes |
|----------|-----------|--------|-------|
| Force | kips | kip | 1 kip = 1000 lbs (same as AISC) |
| Moment | kip-ft or kip-in | kip-ft, kip-in | Context dependent |
| Stress | ksi | ksi | 1 ksi = 1 kip/in² |
| Length | inches or feet | in, ft | Beams in feet, sections in inches |
| Area | square inches | in² | Section properties |
| Modulus | ksi | ksi | E = 29,000 ksi for steel |
| Deflection | inches | in | Serviceability limits |
| Spacing | inches | in | Opening center-to-center |

---

# Performance Optimization

## Search Strategy Priority

1. **Beam type identification first**: Always determine CB vs LB before searching
   - Quick check: `references/geometry-guide.md` for terminology
   - Hexagonal openings → Castellated Beam (CB)
   - Circular openings → Cellular Beam (LB)

2. **Reference files before full search**:
   - Symbols → `references/symbols.md`
   - Terms → `references/glossary.md`
   - Examples → `references/examples-index.md`
   - Geometry → `references/geometry-guide.md`
   - Failure modes → `references/failure-modes-guide.md`
   - Workflow → `references/design-workflow-summary.md`

3. **Efficient chapter targeting**:
   - Use topic keywords to identify specific chapter/section
   - Don't search all files - target 1-2 relevant sections
   - Example: "Vierendeel bending" → Only search Chapter 3.2 + examples

4. **Smart document reading**:
   - Read only relevant sections
   - Use offset and limit parameters for large files
   - Cross-reference between chapters and examples when needed

## Python Script Usage

Execute automation scripts when appropriate (when implemented):

```bash
# Geometry calculation
python3 scripts/geometry_calculator.py --beam-type "CB" --parent-section "W16x26" --expansion-ratio 1.5

# Vierendeel moment calculation
python3 scripts/vierendeel_calculator.py --shear 25 --eT 12 --spacing 18

# Web post buckling check
python3 scripts/web_post_checker.py --spacing 18 --height 24 --thickness 0.25

# Category-aware search
python3 scripts/smart_search.py "web post buckling"

# Extract formula with context
python3 scripts/formula_finder.py "MV =" "Chapter_3"

# Find matching example
python3 scripts/example_matcher.py "composite cellular beam"
```

---

# Response Quality Checklist

Every response should include:

- ✅ **Accurate AISC DG31 citation** (AISC Design Guide 31, Section X.Y or Example 4.Z)
- ✅ **Beam type specified** (CB = Castellated or LB = Cellular)
- ✅ **Composite action clarified** (composite or noncomposite)
- ✅ **Opening geometry noted** (hexagonal or circular, size, spacing)
- ✅ **Opening size and spacing specified** (critical for web post buckling)
- ✅ **Units specified** (ksi, in, ft, kip)
- ✅ **Variable definitions** from symbols.md
- ✅ **Working Python code** for calculations (tested and validated)
- ✅ **Cross-references** to examples when explaining formulas
- ✅ **All failure modes checked** (Vierendeel, web post, shear, LTB, deflection)
- ✅ **Deflection reduction noted** (Ieff ≈ 0.9 Ix for service loads)
- ✅ **Limit states noted** (yielding, buckling, rupture, serviceability)

---

# Special Features: Unique Considerations

## Critical Differences from Solid Web Beam Design

### 1. Vierendeel Mechanism (Unique to Web Openings)
**Solid Beam**: Shear carried continuously through web
**CB/LB**: Shear transferred as **local moments** at opening corners (Vierendeel mechanism)

→ **Must check tee section stresses** combining flexure + Vierendeel moment

**Formula**: MV = V × eT (Vierendeel moment from shear force)

### 2. Web Post Buckling (Critical Spacing Check)
**Solid Beam**: Web buckling over full depth
**CB/LB**: **Web post acts as strut** between openings - can buckle if spacing too small

→ **Spacing ratio s/h must exceed minimum** (typically s/h > 1.0-1.5)

**Critical Check**: λ = (h/tw) × √(Fy/E) < λr (limiting slenderness)

### 3. Geometry-Dependent Design (CB vs LB)
**CB (Castellated)**: Hexagonal openings, diamond-shaped web posts, higher stress concentration
**LB (Cellular)**: Circular openings, rectangular web posts, smoother stress flow

→ **Different formulas and checks** apply for each type

**Key Difference**: Opening shape affects Vierendeel moment distribution

### 4. Deflection Reduction (90% Ix Factor)
**Solid Beam**: Use gross Ix for deflection
**CB/LB**: **Effective Ix reduced** to ~90% of gross due to Vierendeel deformation

→ **Deflection often controls design** (serviceability critical)

**Formula**: Ieff ≈ 0.9 × Ix (simplified method from DG31)

### 5. AISC Specification Integration
**Approach**: Design Guide 31 supplements (not replaces) AISC Specification
**Integration**: Use DG31 for opening-specific checks + AISC 360 for general provisions

→ **Both documents required** for complete design

**Hierarchy**: AISC 360 (base requirements) + DG31 (opening-specific procedures)

### 6. LRFD & ASD Dual Methods
**Available**: Both LRFD and ASD methods provided (unlike ADM which is ASD only)
**Typical**: LRFD more common in modern U.S. practice

→ **Specify which method** when presenting calculations

**Resistance Factors (LRFD)**: φ = 0.90 (flexure), φ = 0.90 (compression), φ = 1.00 (shear)
**Safety Factors (ASD)**: Ω = 1.67 (flexure), Ω = 1.67 (compression), Ω = 1.50 (shear)

## Beam Type Selection Guide

**For Castellated Beams (CB)**:
- Traditional applications (since 1910s)
- Moderate depth increase (e = 1.3-1.5 typical)
- Hexagonal aesthetic preferred
- Simpler fabrication (no CNC required)

**For Cellular Beams (LB)**:
- Long-span applications (40-80 ft)
- MEP integration critical (circular openings easier)
- Lower stress concentration (smooth edges)
- Modern CNC fabrication available

**For Composite Action**:
- Building floors with concrete slabs
- Deflection control critical
- Higher strength requirements
- Shear studs acceptable

**For Noncomposite**:
- Parking garages (exposed structure)
- Industrial platforms
- No concrete slab present
- Simpler detailing

## When to Use Chapter 1 vs 2 vs 3 vs Examples

**Use Chapter 1 (Introduction) when**:
- User asks "what is a castellated/cellular beam?"
- User needs manufacturing process explanation
- User wants nomenclature and terminology
- User asks "how are they made?"

**Use Chapter 2 (Use Cases) when**:
- User asks "when should I use this beam type?"
- User needs advantages/disadvantages
- User wants typical applications
- User asks "is this suitable for my project?"

**Use Chapter 3 (Design Procedures) when**:
- User asks "what is the formula?"
- User needs design check procedures
- User wants to understand limit states
- User asks "how do I check Vierendeel bending?"

**Use Examples (Chapter 4) when**:
- User asks "how do I calculate this?"
- User needs step-by-step procedure
- User wants to see complete worked solution
- User asks "show me a calculation"

**Use Reference Files when**:
- User asks about symbols or notation
- User needs geometric relationships
- User wants failure mode overview
- User needs quick lookup data

**Use All Together when**:
- Comprehensive design questions
- Teaching/learning scenarios
- Formula explanation with practical context
- Validation of calculations

---

# Error Handling

## Common Scenarios

1. **Beam type not specified**:
   - Ask user: "Is this a castellated beam (hexagonal openings) or cellular beam (circular openings)?"
   - Offer context: CB = traditional, LB = long-span/modern

2. **Composite action unclear**:
   - Ask user: "Is there a concrete slab providing composite action?"
   - Explain impact: Composite has higher strength and lower deflection

3. **Opening geometry missing**:
   - Ask user for:
     - Opening size (diameter or height)
     - Opening spacing (center-to-center)
     - Expansion ratio (for CB)
   - Note: These are critical for web post buckling

4. **No results found**:
   - Suggest alternative keywords
   - Check all document types (Chapters 1-3, Examples, References)
   - Recommend broader search terms
   - Check if query is in scope for DG31

5. **Ambiguous query**:
   - Clarify with multiple interpretations
   - Ask user: "Did you mean [castellated] or [cellular]?"
   - Present options for beam type and composite action

6. **Missing parameters for calculation**:
   - List required values:
     - Parent section (W-shape)
     - Expansion ratio or opening diameter
     - Spacing between openings
     - Span length
     - Loads (dead, live)
   - Offer typical default values from examples

7. **Out of scope**:
   - Clearly state DG31 limitations (normal gravity loads, typical buildings)
   - Not covered: seismic detailing, fatigue, fire design
   - Suggest consulting structural engineer for complex cases

## Validation Checks

For all calculations:
- ✅ Verify beam type specified (CB or LB)
- ✅ Verify composite action clarified
- ✅ Check opening geometry defined (size, spacing)
- ✅ Verify units consistency (ksi, in, ft, kip)
- ✅ Check spacing ratio (s/h > minimum for web post stability)
- ✅ Verify deflection includes reduction factor (Ieff ≈ 0.9 Ix)
- ✅ Check all failure modes addressed (Vierendeel, web post, shear, LTB, deflection)
- ✅ Warn if parameters outside typical ranges:
  - Expansion ratio e < 1.2 or e > 1.6 (unusual)
  - Spacing s < 1.0h (web post buckling risk)
  - Span > 80 ft (may need special consideration)
- ✅ Note all assumptions (bracing, load cases, boundary conditions)
- ✅ Cross-check with example from Chapter 4 when possible

---

# Special Notes

## LRFD & ASD Methods (Both Available)

Unlike some design guides that use only one method, AISC Design Guide 31 provides **both LRFD and ASD**:

**LRFD (Load and Resistance Factor Design)**:
- Design strength = φ × Nominal strength
- Load combinations from ASCE/SEI 7 (1.2D + 1.6L, etc.)
- Resistance factors (φ):
  - φ = 0.90 for flexure
  - φ = 0.90 for compression
  - φ = 1.00 for shear
  - φ = 0.75 for bolts/welds

**ASD (Allowable Strength Design)**:
- Allowable strength = Nominal strength / Ω
- Load combinations from ASCE/SEI 7 (D + L, D + L + W, etc.)
- Safety factors (Ω):
  - Ω = 1.67 for flexure
  - Ω = 1.67 for compression
  - Ω = 1.50 for shear
  - Ω = 2.00 for bolts/welds

**Which to use**: Specify based on user preference or project requirements. LRFD more common in modern U.S. practice.

## Design Examples Format

- Examples show **complete step-by-step calculations**
- Example numbering: **4.1, 4.2, 4.3, 4.4** (Chapter 4 examples)
- All examples cite specific AISC Specification and DG31 sections
- Results presented to **appropriate significant figures** (typically 3 sig figs)
- **All failure modes checked** in each example (comprehensive approach)
- Both LRFD and ASD methods shown (or noted when only one is applicable)

## Version Tracking

- Design Guide: **AISC Design Guide 31** (2nd Edition, 2016)
- Related Specification: **AISC 360-16** (Specification for Structural Steel Buildings)
- Published by: **American Institute of Steel Construction (AISC)**
- Always cite version in responses: "AISC Design Guide 31 (2016)"

## Default Assumptions (if not specified by user)

Unless specified otherwise, assume:
- Method: **LRFD** (more common in modern practice)
- Steel: **ASTM A992** (Fy = 50 ksi, Fu = 65 ksi) - typical for W-shapes
- Composite: **Noncomposite** (unless slab explicitly mentioned)
- Beam type: **Ask user** - CB vs LB must be specified
- Deflection limit: **L/360** for live load (typical floor beam)
- E = **29,000 ksi** (modulus of elasticity for steel)

**Always ask user to confirm** critical assumptions before calculations.

---

For comprehensive castellated and cellular beam design work, this skill integrates:
1. **Historical context** from Chapter 1 (Introduction)
2. **Application guidance** from Chapter 2 (Use Cases)
3. **Design procedures** from Chapter 3 (Design Procedures)
4. **Worked applications** from Chapter 4 (Illustrative Examples)
5. **Geometric relationships** from reference files
6. **Failure mode knowledge** from failure-modes-guide
7. **Workflow structure** from design-workflow-summary

**Always prioritize accuracy, cite sources (AISC DG31), specify beam type (CB/LB), clarify composite action, check all failure modes (especially Vierendeel and web post buckling), apply deflection reduction (0.9 Ix), and follow AISC methodology (LRFD or ASD).**
