---
name: aci-318-concrete-design
description: "ACI 318-25 콘크리트 구조설계 기준(Building Code for Structural Concrete)을 검색하고 설계 계산을 수행하며, 설계 워크플로우를 제공합니다. 콘크리트 구조설계, 철근콘크리트, 프리스트레스트 콘크리트, 노출등급, 내진설계, 부재 설계 관련 질문에 즉시 활성화되며, 공식 추출, 노출등급 선택, SDC 요구사항, 설계 검증을 지원합니다."
---

# ACI 318-25 Concrete Design Standards Expert

Use this skill when users ask questions about concrete structural design, ACI 318-25, reinforced concrete, prestressed concrete, exposure classes, seismic design (SDC), or any concrete construction related queries.

## Trigger Keywords

**English**: ACI 318, concrete design, reinforced concrete, prestressed concrete, post-tensioned, slab, beam, column, wall, foundation, exposure class, freezing, sulfate, corrosion, SDC, seismic, moment frame, shear wall, development length, splice, hook, flexure, shear, punching shear, deflection, crack control, strut-and-tie, strength reduction factor, phi factor

**Korean**: ACI 318, 콘크리트설계, 철근콘크리트, 프리스트레스트, 슬래브, 보, 기둥, 벽체, 기초, 노출등급, 동결융해, 황산염, 부식, 내진설계, 모멘트골조, 전단벽, 정착길이, 이음, 갈고리, 휨, 전단, 뚫림전단, 처짐, 균열제어, 스트럿-타이, 강도감소계수

## Tools Required

- **Grep**: Search for keywords in ACI 318-25 documents
- **Read**: Read specific chapters and reference files
- **Glob**: Pattern matching to find files
- **Bash**: Execute Python scripts for searches and calculations
- **Write**: (Optional) Save calculation results or reports

## Document Structure

This skill provides access to **comprehensive concrete design documentation**:

### 1. ACI 318-25 CODE (Part 1-10)
**Location**: `data/code/*.md` (9 part files)

**Purpose**: What you **must** follow - requirements, formulas, limits, design criteria

**Parts**:
- **Part 1**: General (Chapters 1-4)
  - Chapter 1: General
  - Chapter 2: Notation and Terminology
  - Chapter 3: Referenced Standards
  - Chapter 4: Structural System Requirements

- **Part 2**: Loads & Analysis (Chapters 5-6)
  - Chapter 5: Loads
  - Chapter 6: Structural Analysis

- **Part 3**: Members (Chapters 7-13)
  - Chapter 7: One-Way Slabs
  - Chapter 8: Two-Way Slabs
  - Chapter 9: Beams
  - Chapter 10: Columns
  - Chapter 11: Walls
  - Chapter 12: Diaphragms
  - Chapter 13: Foundations

- **Part 4**: Joints and Connections (Chapters 14-16)
  - Chapter 14: Joints
  - Chapter 15: Connections Between Members
  - Chapter 16: Connections to Concrete (Anchoring)

- **Part 5**: Earthquake Resistance (Chapter 17)
  - Chapter 17: Earthquake-Resistant Structures (SDC B through F)

- **Part 6**: Materials, Construction & Durability (Chapters 18-20)
  - Chapter 18: Concrete: Design and Durability Requirements
  - Chapter 19: Concrete: Design and Durability Requirements (continued)
  - Chapter 20: Steel Reinforcement Properties, Durability, and Embedments

- **Part 7**: Strength & Serviceability (Chapters 21-25)
  - Chapter 21: Strength Reduction Factors (φ factors)
  - Chapter 22: Sectional Strength
  - Chapter 23: Strut-and-Tie Method
  - Chapter 24: Serviceability
  - Chapter 25: Reinforcement Details

- **Part 8**: Construction (Chapter 26)
  - Chapter 26: Construction Documents and Submittals

- **Part 10**: Evaluation (Chapter 27)
  - Chapter 27: Strength Evaluation of Existing Structures

### 2. COMMENTARY (Background and Rationale)
**Location**: `data/commentary/*.md` (9 commentary files)

**Purpose**: Understand **why** - background, research basis, design considerations

**Contents**: Detailed commentary on each CODE section with:
- Historical development
- Research background
- Design considerations
- Limit state explanations
- Examples and comparisons

### 3. Appendices (A-D)
**Location**: `data/appendices/*.md` (4 appendix files)

- **Appendix A**: Design Verification Using Nonlinear Response History Analysis
- **Appendix B**: Performance-Based Wind Design
- **Appendix C**: Sustainability and Resilience
- **Appendix D**: Steel Reinforcement Information

### 4. Notation and Symbols
**Location**: `data/Notation_Symbols.md` (from Chapter 2)

**Purpose**: Mathematical notation and variable definitions

**Key Distinction**:
- **CODE** → "What are the requirements?" "What formula should I use?"
- **COMMENTARY** → "Why is this required?" "What's the background?"
- **Appendices** → "Advanced topics" "Special analysis methods"

## Reference Files

This skill includes comprehensive reference materials:

- `references/exposure-guide.md`: **Exposure class selection flowchart (F/W/C/S series)**
- `references/seismic-categories.md`: **SDC A-F requirements and system selection**

## Automation Scripts

Python scripts are available in `scripts/` directory:
- `consolidate_pages.py`: Merge 702 page files into chapters (already run)
- `smart_search.py`: Category-aware keyword search across documents
- `formula_finder.py`: Extract formulas with context and variables

---

# Workflow by Query Type

## 1. Formula Query (공식 질의)

**User Intent**: Find a specific formula or equation from ACI 318-25 CODE.

**Example Queries**:
- "What is the formula for shear strength of beams?"
- "Show me the flexural capacity equation for slabs"
- "철근콘크리트 보의 전단강도 공식을 알려줘"
- "기둥의 축하중 강도식은?"

**Quick Process**:
1. Identify topic:
   - Flexure → Chapter 22, Chapters 7-10
   - Shear → Chapter 22.5-22.6
   - Development → Chapter 25
   - Columns → Chapter 10, Chapter 22
2. Use `formula_finder.py` or Grep in `data/code/`
3. Extract formula with variable definitions from `Notation_Symbols.md`
4. Present with ACI citation (e.g., "ACI 318-25 Section 22.5.5.1")
5. Show COMMENTARY if explanation needed

**Keywords**: formula, equation, 공식, 계산식, strength, capacity

---

## 2. Design Requirement Query (설계 요구사항 질의)

**User Intent**: Find specific design requirements, limits, or criteria.

**Example Queries**:
- "What is the minimum slab thickness for two-way slabs?"
- "What are the spacing requirements for stirrups in beams?"
- "2방향 슬래브의 최소 두께는?"
- "보의 최소 철근비는 얼마야?"

**Quick Process**:
1. Identify member type and requirement:
   - Minimum dimensions → Chapter 7-13 (member chapters)
   - Reinforcement limits → Chapter 25, member chapters
   - Cover requirements → Chapter 20, exposure guide
   - Spacing → Chapter 25
2. Search CODE sections with `smart_search.py`
3. List all applicable requirements
4. Reference tables if applicable
5. Note COMMENTARY for context

**Keywords**: minimum, maximum, requirement, limit, spacing, 최소, 최대, 요구사항

---

## 3. Exposure Class Selection Query (노출등급 선택 - CONCRETE-SPECIFIC)

**User Intent**: Determine appropriate exposure class for durability design.

**Example Queries**:
- "What exposure class for a parking garage deck?"
- "How to select exposure class for basement wall?"
- "주차장 슬래브의 노출등급은?"
- "해양 구조물의 노출조건은?"

**Quick Process**:
1. Read `references/exposure-guide.md` for flowchart
2. Ask user about environmental conditions:
   - Freezing exposure? → F0, F1, F2, F3
   - Water penetration? → W0, W1, W2
   - Chloride exposure? → C0, C1, C2
   - Sulfate in soil? → S0, S1, S2, S3
3. Determine most restrictive requirements
4. Return required:
   - Minimum f'c
   - Maximum w/cm ratio
   - Minimum cover
   - Air content (if needed)
   - Cement type
5. Reference Chapter 19 sections

**Keywords**: exposure, durability, freezing, sulfate, chloride, corrosion, 노출등급, 내구성, 동결

---

## 4. Seismic Design Query (내진 설계 질의 - EARTHQUAKE-SPECIFIC)

**User Intent**: Understand or apply seismic design requirements based on SDC.

**Example Queries**:
- "What are the requirements for SDC D special moment frames?"
- "How to detail beam-column joints in IMF?"
- "SDC D 특수모멘트골조의 요구사항은?"
- "전단벽 경계요소는 언제 필요해?"

**Quick Process**:
1. Identify SDC level (A, B, C, D, E, or F)
2. Read `references/seismic-categories.md` for system selection
3. Determine required system:
   - SDC A: No Chapter 17
   - SDC B: OMF + Section 17.2
   - SDC C: IMF or Ordinary Walls + Sections 17.6, 17.9
   - SDC D/E/F: SMF or Special Walls + Full Chapter 17
4. Search Chapter 17 sections in CODE:
   - 17.5: Special Moment Frames (SMF)
   - 17.6: Intermediate Moment Frames (IMF)
   - 17.7: Special Structural Walls
   - 17.8: Diaphragms
5. List detailing requirements:
   - Confinement reinforcement
   - Boundary elements (if walls)
   - Strong-column/weak-beam (if frames)
   - Joint shear requirements
6. Show equations and limits

**Keywords**: seismic, earthquake, SDC, moment frame, shear wall, ductility, confinement, 내진, 지진, 모멘트골조

---

## 5. Calculation Query (계산 질의)

**User Intent**: Perform structural calculations using ACI 318-25 formulas.

**Example Queries**:
- "Calculate beam shear capacity: b=12 in, d=20 in, f'c=4000 psi"
- "Determine development length: #8 bar, f'c=5000 psi, fy=60 ksi"
- "보의 휨강도를 계산해줘: b=300mm, d=500mm, As=1500mm²"

**Quick Process**:
1. Identify calculation type (flexure, shear, development, etc.)
2. Find formula from CODE using `formula_finder.py`
3. Identify required inputs:
   - Material properties: f'c, fy
   - Geometry: b, d, h, As, etc.
   - Load conditions
4. Find similar examples from COMMENTARY
5. Generate Python code following CODE requirements
6. Apply strength reduction factors (φ) from Chapter 21
7. Execute and validate against CODE limits
8. Present results with citations

**Concrete-Specific Checks**:
- ✅ f'c within typical range (3,000-10,000 psi)
- ✅ fy verified (typically 60,000 or 80,000 psi)
- ✅ Reinforcement ratio within min/max limits
- ✅ Spacing requirements satisfied
- ✅ Cover requirements met
- ✅ φ factor applied correctly

**Keywords**: calculate, compute, determine, design, 계산, 산정, 설계

---

## 6. Commentary/Explanation Query (해설 질의)

**User Intent**: Understand the reasoning or background behind CODE requirements.

**Example Queries**:
- "Why is the strength reduction factor different for tension and compression?"
- "Explain the background for minimum reinforcement in slabs"
- "왜 전단강도 공식에 크기효과가 포함되나요?"

**Quick Process**:
1. Find CODE section reference
2. Read corresponding COMMENTARY section (R-prefixed)
3. Extract:
   - Research background
   - Historical development
   - Design philosophy
   - Limit state explanation
4. Present with citations to research papers if mentioned
5. Provide examples from COMMENTARY

**Keywords**: why, explain, background, reason, 왜, 이유, 배경

---

## 7. Cross-Reference Query (교차 참조 질의)

**User Intent**: Find all related sections on a topic.

**Example Queries**:
- "Find all sections related to development of reinforcement"
- "What chapters discuss punching shear in slabs?"
- "정착길이와 관련된 모든 섹션을 찾아줘"

**Quick Process**:
1. Use `smart_search.py` with query keywords
2. Search across all CODE and COMMENTARY files
3. Group results by:
   - Primary requirements (CODE)
   - Explanations (COMMENTARY)
   - Related topics
4. Show chapter/section hierarchy
5. Note dependencies between sections

**Keywords**: related, sections, chapters, reference, 관련, 참조

---

# Quick Reference Tables

## Document Categories

| Type | Location | Files | Purpose |
|------|----------|-------|---------|
| **CODE** | data/code/ | 9 parts | Requirements, formulas, limits |
| **COMMENTARY** | data/commentary/ | 9 | Background, rationale, research |
| **Appendices** | data/appendices/ | 4 | Advanced topics |
| **Notation** | data/ | 1 | Symbols and definitions |
| **References** | references/ | 2 | Exposure guide, seismic guide |

## Common Search Patterns

| Topic | Keywords | CODE Chapters | Key Sections | Unique Considerations |
|-------|----------|---------------|--------------|----------------------|
| **Beam Design** | flexure, bending, moment | 9, 22 | 22.3, 22.5 | Deflection check (Chapter 24) |
| **Column Design** | compression, axial, column | 10, 22 | 22.4 | Slenderness effects (Chapter 6) |
| **Slab Design** | slab, one-way, two-way | 7, 8, 22 | 22.6 (punching) | Minimum thickness (7.3, 8.3) |
| **Shear** | shear, stirrups, Vc, Vs | 9, 22 | 22.5, 22.6 | Size effect factor |
| **Development** | development, splice, hook | 25 | 25.4, 25.5 | Bar size dependent |
| **Seismic** | SDC, moment frame, wall | 17 | 17.5-17.9 | SDC-dependent |
| **Exposure** | durability, corrosion | 19, 20 | 19.3 | F/W/C/S classes |
| **Serviceability** | deflection, crack | 24 | 24.2, 24.3 | Long-term effects |

## ACI Chapter-to-Topic Mapping

| CODE Chapter | Topic | Key Sections | Critical Formulas |
|--------------|-------|--------------|-------------------|
| 7 | One-Way Slabs | 7.3, 7.6 | Minimum thickness |
| 8 | Two-Way Slabs | 8.3, 8.4 | Punching shear, minimum thickness |
| 9 | Beams | 9.3, 9.6 | Minimum dimensions, shear reinforcement |
| 10 | Columns | 10.5, 10.6 | Minimum dimensions, ties/spirals |
| 11 | Walls | 11.5, 11.6 | Thickness, reinforcement |
| 13 | Foundations | 13.2, 13.3 | Shear provisions |
| 17 | Seismic | 17.5-17.9 | SMF, IMF, Walls |
| 19 | Exposure/Durability | 19.3 | F/W/C/S classes |
| 21 | φ Factors | 21.2 | Strength reduction |
| 22 | Sectional Strength | 22.3-22.7 | Mn, Vn, Pn |
| 24 | Serviceability | 24.2, 24.3 | Deflection, crack width |
| 25 | Detailing | 25.2-25.5 | Development, splices, hooks |

## Units Convention

| Quantity | ACI Unit | Symbol | Notes |
|----------|----------|--------|-------|
| Force | kips or pounds | kip, lb | 1 kip = 1000 lbs |
| Moment | kip-in or kip-ft | kip-in | Mixed units common |
| Stress | psi or ksi | psi, ksi | f'c in psi, fy in ksi |
| Length | inches or feet | in, ft | Typically inches for dimensions |
| Area | square inches | in² | - |
| Strength | psi | f'c, fy | Concrete: psi, Steel: ksi |

---

# Performance Optimization

## Search Strategy Priority

1. **Exposure class queries first**: Check `references/exposure-guide.md`

2. **Seismic queries**: Check `references/seismic-categories.md`

3. **Reference notation**: Check `data/Notation_Symbols.md` for variable definitions

4. **Efficient chapter targeting**:
   - Use topic keywords to identify specific chapter
   - Don't search all files - target 1-2 relevant chapters
   - Example: "beam shear" → Only search Chapter 9 + Chapter 22

5. **Smart document reading**:
   - Read only relevant sections
   - Use CODE for requirements, COMMENTARY for explanation
   - Cross-reference when needed

## Python Script Usage

Execute automation scripts when appropriate:

```bash
# Smart keyword search
python3 scripts/smart_search.py "beam shear" --max-results 10

# Find formulas
python3 scripts/formula_finder.py --pattern "V_c =" --section "22.5"

# Search with commentary
python3 scripts/smart_search.py "exposure class" --no-commentary
```

---

# Response Quality Checklist

Every response should include:

- ✅ **Accurate ACI citation** (ACI 318-25 Section X.Y.Z)
- ✅ **Material properties specified** (f'c, fy)
- ✅ **Units specified** (psi, ksi, in, ft)
- ✅ **Variable definitions** from Notation_Symbols.md
- ✅ **φ factor applied** (strength reduction from Chapter 21)
- ✅ **Working code for calculations** (tested and validated)
- ✅ **Cross-references** to COMMENTARY when explaining CODE
- ✅ **Limit states noted** (yielding, crushing, shear, etc.)
- ✅ **Minimum/maximum checks** (reinforcement ratios, spacing, cover)

---

# Special Features: Concrete-Specific Considerations

## Critical Differences from Steel Design

### 1. Material Behavior
**Steel**: Linear-elastic until yield, then plastic
**Concrete**: Nonlinear compression behavior, brittle in tension

→ **Concrete requires reinforcement** for tension resistance

### 2. Strength Reduction Factors (φ)
**Steel**: Single factor (0.90 for LRFD)
**Concrete**: **Variable φ factors** based on tension-controlled vs compression-controlled (Chapter 21)

→ **Check strain conditions** to determine appropriate φ

### 3. Exposure and Durability
**Steel**: Mainly corrosion protection (paint, galvanizing)
**Concrete**: **Comprehensive exposure class system (F/W/C/S)**

→ **Select exposure classes** early in design (affects f'c, w/cm, cover)

### 4. Time-Dependent Effects
**Steel**: Minimal long-term effects
**Concrete**: **Creep, shrinkage, long-term deflection**

→ **Apply time-dependent factors** for serviceability (Chapter 24)

### 5. Member Design Philosophy
**Steel**: Compact/non-compact sections
**Concrete**: **Reinforcement ratio limits, minimum dimensions**

→ **Check minimum AND maximum reinforcement** (ductility)

### 6. Seismic Design
**Steel**: R-factor based
**Concrete**: **SDC-based system classification** (OMF, IMF, SMF)

→ **Different detailing requirements** by SDC level (Chapter 17)

## Exposure Class Decision Guide

**For Climate-Controlled Interior**:
- F0, W0, C0, S0 → Minimal restrictions

**For Exterior Above Grade**:
- F1 or F2 (depends on freezing + moisture)
- W0
- C1 (if no chlorides)
- S0 (typically)

**For Parking Structures**:
- F3 (de-icing salts + saturation)
- C2 (chloride exposure)
- W1
- **Required**: f'c ≥ 5,000 psi, w/cm ≤ 0.40

**For Marine Structures**:
- F2 or F3 (if freezing climate)
- C2 (seawater chlorides)
- S2 (seawater sulfates)
- **Required**: f'c ≥ 5,000 psi, w/cm ≤ 0.40, sulfate-resistant cement

**For Foundations on Soil**:
- F0 (below frost line)
- W0 or W1
- C1
- S0/S1/S2 (MUST test soil)
- **Required**: Soil sulfate test mandatory

## Seismic Design System Selection

**SDC A**: No special seismic requirements

**SDC B**: Ordinary systems + Section 17.2 (basic detailing)

**SDC C**:
- Moment frames → Intermediate Moment Frames (IMF) per 17.6
- Walls → Ordinary walls + Section 17.9

**SDC D/E/F**:
- Moment frames → Special Moment Frames (SMF) per 17.5
- Walls → Special Structural Walls per 17.7
- **Most restrictive detailing**

## φ Factor Selection (Chapter 21)

**Tension-Controlled** (εt ≥ 0.005):
- φ = 0.90 (flexure)

**Transition** (0.002 < εt < 0.005):
- φ = 0.65 + (εt - 0.002) × (250/3)

**Compression-Controlled** (εt ≤ 0.002):
- φ = 0.65 (tied members)
- φ = 0.75 (spirally reinforced)

**Shear and Torsion**:
- φ = 0.75

**Bearing**:
- φ = 0.65

## When to Use CODE vs COMMENTARY

**Use CODE when**:
- User asks "what is the formula?"
- User needs official requirements or limits
- User wants to verify compliance
- User asks about design criteria

**Use COMMENTARY when**:
- User asks "why is this required?"
- User needs background or research basis
- User wants to understand design philosophy
- User asks "what's the history?"

**Use Both when**:
- Comprehensive design questions
- Teaching/learning scenarios
- Formula explanation with context
- Validation of complex calculations

---

# Error Handling

## Common Scenarios

1. **Material properties not specified**:
   - Ask user: "What is f'c and fy?" (e.g., f'c = 4,000 psi, fy = 60,000 psi)
   - Offer common values: f'c = 4,000 psi (typical), 5,000 psi (higher strength)

2. **Exposure class unclear**:
   - Ask user: "What are the environmental conditions?"
   - Use `references/exposure-guide.md` flowchart
   - Explain F/W/C/S implications

3. **SDC not specified**:
   - Ask user: "What is the Seismic Design Category (A-F)?"
   - Reference ASCE 7 for determination

4. **No results found**:
   - Suggest alternative keywords
   - Check both CODE and COMMENTARY
   - Recommend broader search terms

5. **Ambiguous query**:
   - Clarify with multiple interpretations
   - Ask user: "Did you mean [option A] or [option B]?"

6. **Missing parameters**:
   - List required values for calculation
   - Offer typical default values

7. **Out of scope**:
   - Clearly state limitations
   - Suggest consulting structural engineer for complex cases

## Validation Checks

For all calculations:
- ✅ Verify f'c and fy specified
- ✅ Check units consistency (psi, ksi, in)
- ✅ Verify reinforcement ratios within min/max limits
- ✅ Check spacing requirements
- ✅ Verify cover requirements met
- ✅ Apply correct φ factor
- ✅ Warn if parameters outside typical ranges
- ✅ Note all assumptions
- ✅ Cross-check with COMMENTARY examples when possible

---

# Special Notes

## ACI 318-25 Version

- **Version**: ACI CODE-318-25 (2025 edition)
- **Units**: Inch-Pound (IN-LB) - official version
- **Published by**: American Concrete Institute
- Always cite version in responses

## Code + Commentary Structure

- Each CODE section has corresponding COMMENTARY (R-prefix)
- Example: Section 9.6.3 ↔ R9.6.3
- COMMENTARY provides background but is **not mandatory**
- CODE requirements are **mandatory** when adopted

## Material Defaults (if not specified by user)

Unless specified otherwise, assume:
- Concrete: f'c = 4,000 psi (normal weight)
- Reinforcement: fy = 60,000 psi (Grade 60)
- Exposure: Interior (F0, W0, C0, S0)
- Cover: Per Chapter 20 minimum (typically 1.5" for beams/columns)

**Always ask user to confirm** if critical to calculation.

## Equation Numbering

- Equations are numbered by section (e.g., Eq. 22.5.5.1)
- Some formulas have no equation number (described in text)
- Cross-references use section numbers

---

For comprehensive concrete structural design work, this skill integrates:
1. **CODE requirements** from ACI 318-25 (mandatory)
2. **Background understanding** from COMMENTARY
3. **Exposure class selection** from reference guide (F/W/C/S)
4. **Seismic system selection** from reference guide (SDC A-F)
5. **Material and section properties** from Notation
6. **Automation tools** (search, formula extraction)

**Always prioritize accuracy, cite sources, apply φ factors, check exposure classes, verify seismic requirements, and follow CODE provisions.**
