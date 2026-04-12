---
name: aisc-steel-design
description: "AISC 강구조 기준(360-22 Specification) 및 설계 예제집(v16.0 Design Examples)을 검색하고, 구조계산을 수행하며, 설계 워크플로우를 제공합니다. 미국 강구조 설계 관련 질문에 즉시 활성화되며, 공식 추출, 예제 매칭, 계산 수행, 용어 설명, 기호 정의를 지원합니다."
---

# AISC Steel Design Standards Expert

Use this skill when users ask questions about AISC steel design, structural calculations, beam/column design, connections, LRFD/ASD methods, or any AISC 360-22 Specification and Design Examples related queries.

## Trigger Keywords

**English**: AISC, steel design, steel construction, LRFD, ASD, load resistance factor design, allowable stress design, flexural strength, shear strength, connection design, beam design, column design, compression member, tension member, lateral-torsional buckling, local buckling, compact section, non-compact section, slender section, W-shape, HSS, hollow structural section, composite beam, composite column, shear stud, bolt design, weld design, moment connection, shear connection, simple connection, bracing connection, slip-critical, bearing-type, fillet weld, groove weld, Specification 360, Design Examples, nominal strength, available strength, resistance factor, safety factor

**Korean**: AISC, 미국강구조기준, 강구조설계, 강구조, 보설계, 기둥설계, 연결부설계, 볼트설계, 용접설계, 휨강도, 전단강도, 압축강도, 인장강도, 합성보, 전단연결재, 하중저항계수설계, 허용응력설계

## Tools Required

- **Grep**: Search for keywords in AISC documents
- **Read**: Read specific chapters and reference files
- **Glob**: Pattern matching to find files
- **Bash**: Execute Python scripts for searches and calculations
- **Write**: (Optional) Save calculation results or reports

## Document Structure

This skill provides access to **two interconnected document systems**:

### 1. AISC 360-22 Specification (Code Requirements)
**Location**: `data/specification/*.md` (14 chapter files)

**Purpose**: What you **must** follow - formulas, requirements, limits, design criteria

**Chapters**:
- **A**: General Provisions (scope, materials, documents)
- **B**: Design Requirements (loads, analysis, member properties)
- **C**: Stability (direct analysis method)
- **D**: Tension Members (tensile strength, net area)
- **E**: Compression Members (flexural buckling, local buckling)
- **F**: Flexural Members (lateral-torsional buckling, yielding, rupture)
- **G**: Shear Members (shear strength of webs and flanges)
- **H**: Combined Forces (interaction equations, torsion)
- **I**: Composite Members (steel-concrete composite design)
- **J**: Connections (bolts, welds, bearing, block shear)
- **K**: HSS Connections (hollow section connections)
- **L**: Serviceability (deflection limits)
- **M**: Fabrication (fabrication and erection requirements)
- **N**: Quality (QC/QA requirements)

### 2. Design Examples v16.0 (Step-by-Step Applications)
**Location**: `data/design-examples/Part_I/`, `Part_II/`, `Part_III/` (16 chapter files)

**Purpose**: How to **apply** the specification - worked examples with calculations

**Structure**:
- **Part I** (11 chapters): Specification-based member design examples (Chapters A-K)
- **Part II** (4 chapters): Manual-based connection design examples
  - II-A: Simple Shear Connections (27 examples)
  - II-B: Moment Connections (15+ examples)
  - II-C: Bracing Connections
  - II-D: Miscellaneous Connections
- **Part III** (1 chapter): Building system analysis (4-story braced and moment frames)

**Key Distinction**:
- **Specification** → "What formula should I use?" "What are the limits?"
- **Design Examples** → "How do I calculate this step-by-step?" "Show me a worked example"

## Reference Files

This skill includes comprehensive reference materials:

### Standard References (Extracted from AISC Front Matter)

- `references/symbols.md`: Complete symbols table (100+ engineering symbols)
- `references/glossary.md`: Technical terms and definitions (150+ terms)
- `references/abbreviations.md`: Standard abbreviations (QC, LRFD, ASD, etc.)
- `references/specification-structure.md`: Chapter structure and section mapping
- `references/design-examples-index.md`: Complete example index (93 examples)
- `references/conventions.md`: Design conventions and methodology
- `references/key-modifications-360-22.md`: 2022 edition major changes

### Custom Reference Guides (NEW in v2.0.0)

- `references/steel-grade-guide.md`: **Steel grade selection guide** (A992, A572, A36, A500, A588, A913, A514)
  - Properties, availability, cost comparison, weldability
  - Selection flowchart and application recommendations
  - Compatibility tables for connections and bolts
- `references/limit-states-checklist.md`: **Comprehensive limit states checklist**
  - 60+ checks organized by member type (beams, columns, HSS, plate girders, angles, trusses, connections)
  - Design phase checklist (preliminary, detailed, final)
  - All limit states per AISC 360-22

### Accumulated Knowledge (NEW in v2.0.0 - Response-Saving System)

**Location**: `references/accumulated-knowledge/`

**Purpose**: Comprehensive design guides synthesized from useful Q&A responses. These documents go beyond the AISC specification to provide practical workflows, worked examples, and best practices.

**Current Topics**:
- `composite-beam-construction-sequence.md`: Complete composite beam design considering shored/unshored construction, deflections, and camber (1,200 lines)
- `seismic-moment-connection-workflow.md`: RBS and prequalified seismic connections per AISC 358/341 (1,100 lines)
- `README.md`: Guidelines for saving future responses (600 lines)

**How it works**: When Claude provides particularly useful responses that synthesize multiple AISC chapters or provide comprehensive workflows, those responses can be saved as permanent reference documents for future use. This creates institutional knowledge that grows with use.

## Automation Scripts

Python scripts are available in `scripts/` directory:
- `extract_front_matter.py`: Extract reference materials from page files
- `smart_search.py`: Category-aware keyword search (to be created)
- `formula_finder.py`: Extract formulas with context (to be created)
- `example_matcher.py`: Match user queries to appropriate examples (to be created)
- `cross_reference.py`: Cross-reference Specification ↔ Examples (to be created)

---

# Workflow by Query Type (Summary)

## 1. Formula Query (공식 질의)

**User Intent**: Find a specific formula or equation from AISC Specification.

**Example Queries**:
- "What is the formula for lateral-torsional buckling strength?"
- "Show me the Mn equation for compact W-shapes"
- "휨강도 공식을 알려줘"

**Quick Process**:
1. Identify topic (flexure → Chapter F, compression → Chapter E, etc.)
2. Grep relevant chapter file in `data/specification/`
3. Extract formula with variable definitions from `references/symbols.md`
4. Present with AISC citation (e.g., "AISC 360-22 Section F2.1")

**Keywords**: formula, equation, 공식, 계산식

---

## 2. Design Example Query (예제 질의)

**User Intent**: See a step-by-step worked example of a design calculation.

**Example Queries**:
- "Show me how to design a W-shape beam for flexure"
- "I need an example of column design with KL/r"
- "볼트 연결부 설계 예제를 보여줘"

**Quick Process**:
1. Check `references/design-examples-index.md` for example number
2. Identify appropriate example (e.g., Example F.1-1A: W-shape beam, LRFD)
3. Read from `data/design-examples/Part_I/Chapter_F_Flexural_Members.md`
4. Present step-by-step with both LRFD and ASD calculations

**Keywords**: example, 예제, how to, step-by-step, 설계과정

---

## 3. Calculation Query (계산 질의)

**User Intent**: Perform structural calculations using AISC formulas.

**Example Queries**:
- "Calculate flexural strength: W18x50, Fy=50ksi, Lb=15ft, Cb=1.0"
- "Determine column capacity: W14x90, KL=20ft, Fy=50ksi"
- "합성보 전단연결재 개수를 계산해줘"

**Quick Process**:
1. Identify calculation type and required formula
2. Find formula from Specification (use Formula Query workflow)
3. Find similar example from Design Examples for methodology
4. Generate Python code following example structure
5. Execute and validate against AISC limits

**Keywords**: calculate, compute, determine, 계산, 산정, 구해줘

---

## 4. Terminology Query (용어 설명)

**User Intent**: Understand the meaning and context of AISC terminology.

**Example Queries**:
- "What is a compact section?"
- "Explain lateral-torsional buckling"
- "허용강도설계법이 뭐야?"

**Quick Process**:
1. Check `references/glossary.md` first (150+ terms)
2. If not found, search "Glossary" or chapter sections in Specification
3. Present definition with AISC citation
4. Provide usage examples from Specification chapters

**Keywords**: what is, explain, definition, 뭐야, 설명, 의미

---

## 5. Symbol/Notation Query (기호 질의)

**User Intent**: Understand what a mathematical symbol represents.

**Example Queries**:
- "What does Cb mean?"
- "Define φ (phi) resistance factor"
- "Mn 기호는 무엇을 의미하나요?"

**Quick Process**:
1. Check `references/symbols.md` (100+ symbols)
2. Return: Symbol | Definition | Units | Section Reference
3. Example: *Cb* = Lateral-torsional buckling modification factor | dimensionless | Section F2.2

**Keywords**: symbol, notation, 기호, 표기

---

## 6. Cross-Reference Query (교차참조)

**User Intent**: Connect Specification requirements with worked examples.

**Example Queries**:
- "Show me an example using the Chapter E formulas"
- "Where can I see this formula applied?"
- "이 공식을 사용하는 예제를 보여줘"

**Quick Process**:
1. Identify formula location in Specification (e.g., Chapter F, Section F2.1)
2. Find matching examples in Design Examples (e.g., Part_I/Chapter_F)
3. Present both side-by-side:
   - Specification: Formula and requirements
   - Design Example: Step-by-step application

**Keywords**: example of, show me, cross-reference, 예제, 적용

---

## 7. Comparison Query (비교 질의)

**User Intent**: Compare LRFD vs ASD, or different design approaches.

**Example Queries**:
- "What's the difference between LRFD and ASD?"
- "Compare compact vs non-compact sections"
- "허용응력설계와 하중저항계수설계의 차이는?"

**Quick Process**:
1. Identify items to compare
2. Locate relevant sections (e.g., Chapter B for design philosophies)
3. Extract key differences (resistance factors, safety factors, load combinations)
4. Present in comparison table format

**Keywords**: compare, difference, vs, 차이, 비교

---

## 8. Comprehensive Design Workflow Query (종합 설계 절차) - NEW

**User Intent**: Get complete design guidance for complex topics that span multiple AISC chapters.

**Example Queries**:
- "How do I design a composite beam considering construction sequence?"
- "Walk me through seismic moment connection design"
- "What's the complete procedure for plate girder design?"

**Quick Process**:
1. **Check accumulated knowledge first**: `references/accumulated-knowledge/`
   - Composite beams → `composite-beam-construction-sequence.md`
   - Seismic connections → `seismic-moment-connection-workflow.md`
2. If topic exists: Use comprehensive guide with worked examples
3. If topic doesn't exist:
   - Synthesize from Specification chapters and Design Examples
   - Consider saving response to accumulated-knowledge for future use
4. Include: Overview, step-by-step procedure, worked example, checklist, common pitfalls

**Available Comprehensive Guides** (as of v2.0.0):
- Composite beam design with construction loads and deflections
- Seismic moment connections (RBS, AISC 358/341)

**Keywords**: workflow, procedure, complete design, comprehensive, step-by-step, how to design, 설계절차, 전체과정

---

# Quick Reference Tables

## Document Categories

| Type | Location | Files | Purpose |
|------|----------|-------|---------|
| **Specification** | data/specification/ | 14 | Formulas, limits, requirements |
| **Examples Part I** | data/design-examples/Part_I/ | 11 | Specification-based examples |
| **Examples Part II** | data/design-examples/Part_II/ | 4 | Connection design examples |
| **Examples Part III** | data/design-examples/Part_III/ | 1 | Building system analysis |
| **Standard References** | references/ | 7 | Symbols, glossary, indexes (extracted from AISC) |
| **Custom References** | references/ | 2 | Steel grades, limit states (custom guides) |
| **Accumulated Knowledge** | references/accumulated-knowledge/ | 2+ | Comprehensive workflows (grows with use) |

## Common Search Patterns

| Topic | Keywords | Specification Chapter | Design Examples Location |
|-------|----------|----------------------|--------------------------|
| **Beam Design** | flexure, bending, Cb, Lb, yielding | Chapter F | Part_I/Chapter_F |
| **Column Design** | compression, buckling, KL/r, slenderness | Chapter E | Part_I/Chapter_E |
| **Tension Members** | tension, net area, gross area, yielding | Chapter D | Part_I/Chapter_D |
| **Shear** | shear strength, web, tension field action | Chapter G | Part_I/Chapter_G |
| **Connections** | bolts, welds, shear tab, bearing | Chapter J | Part_II/Chapter_IIA |
| **Composite** | shear studs, effective width, Qn | Chapter I | Part_I/Chapter_I |
| **Stability** | second-order, P-delta, direct analysis | Chapter C | Part_III |
| **HSS** | hollow section, RHS, tube, round | Chapter K | Part_I/Chapter_K |

## AISC Chapter-to-Example Mapping

| Spec Chapter | Topic | Part I Example Chapter | Part II Examples |
|--------------|-------|------------------------|------------------|
| A | General | Chapter_A | - |
| B | Design Requirements | Chapter_B | - |
| C | Stability | Chapter_C | Part III (system) |
| D | Tension | Chapter_D | - |
| E | Compression | Chapter_E | - |
| F | Flexure | Chapter_F | - |
| G | Shear | Chapter_G | - |
| H | Combined Forces | Chapter_H | - |
| I | Composite | Chapter_I | - |
| J | Connections | Chapter_J | II-A, II-B, II-C, II-D |
| K | HSS Connections | Chapter_K | II-D (some) |

## Units Convention

| Quantity | AISC Unit | Symbol | Notes |
|----------|-----------|--------|-------|
| Force | kips | kip | 1 kip = 1000 lbs |
| Moment | kip-ft, kip-in | kip-ft | context-dependent |
| Stress | ksi | ksi | 1 ksi = 1 kip/in² |
| Length | inches, feet | in, ft | specify clearly |
| Area | square inches | in² | - |
| Modulus | ksi | ksi | E = 29,000 ksi for steel |

---

# Performance Optimization

## Search Strategy Priority

1. **Reference files first**: Always check indexed references before full search
   - Symbols → `references/symbols.md`
   - Terms → `references/glossary.md`
   - Examples → `references/design-examples-index.md`
   - Structure → `references/specification-structure.md`

2. **Efficient chapter targeting**:
   - Use topic keywords to identify specific chapter
   - Don't search all 30 files - target 1-2 relevant chapters
   - Example: "beam design" → Only search Chapter_F

3. **Smart document reading**:
   - Read only relevant sections
   - Use offset and limit parameters for large files
   - Cross-reference between Specification and Examples when both are needed

## Python Script Usage

Execute automation scripts when appropriate:

```bash
# Category-aware search
python3 scripts/smart_search.py "lateral-torsional buckling"

# Extract formula with context
python3 scripts/formula_finder.py "Mn =" "Chapter_F"

# Find matching example
python3 scripts/example_matcher.py "W-shape beam" "flexure"

# Cross-reference between docs
python3 scripts/cross_reference.py "Chapter_E" --show-examples
```

---

# Response Quality Checklist

Every response should include:

- ✅ **Accurate AISC citation** (360-22 Section X.Y or Example Z.W)
- ✅ **Clear LRFD vs ASD distinction** when applicable
- ✅ **Units specified** (kips, in, ksi, ft, etc.)
- ✅ **Variable definitions** from symbols.md
- ✅ **Working Python code** for calculations (tested and validated)
- ✅ **Cross-references** to examples when explaining formulas
- ✅ **Limit states noted** (yielding, buckling, rupture, etc.)

---

# Special Features: Two-Document System

## When to Use Specification vs Examples

**Use Specification when**:
- User asks "what is the formula?"
- User needs official requirements or limits
- User wants to understand code provisions
- User asks about limit states or design philosophy

**Use Design Examples when**:
- User asks "how do I calculate?"
- User needs step-by-step procedure
- User wants to see LRFD and ASD side-by-side
- User asks "show me an example"

**Use Both when**:
- User asks comprehensive design questions
- Formula explanation needs practical context
- Calculation validation required
- Teaching/learning scenarios

## Cross-Reference Workflow

**Typical pattern**:
1. **User asks**: "How do I design a W-shape beam?"
2. **Response structure**:
   - **Part 1 - Specification**: Show formulas from Chapter F
   - **Part 2 - Example**: Reference Example F.1-1A for step-by-step
   - **Part 3 - Calculation**: Generate Python code following example
   - **Part 4 - Validation**: Check against limits from Specification

---

# Error Handling

## Common Scenarios

1. **No results found**:
   - Suggest alternative keywords
   - Check both Specification and Examples
   - Recommend broader search terms

2. **Ambiguous query**:
   - Clarify with multiple interpretations
   - Ask user: "Did you mean [option A] or [option B]?"

3. **Missing parameters**:
   - List required values for calculation
   - Offer typical default values from examples

4. **Out of scope**:
   - Clearly state limitations (no FEM, no legal advice)
   - Suggest consulting structural engineer for complex cases

## Validation Checks

For all calculations:
- Verify units consistency (all kips, in, ksi)
- Check against AISC limits (Fy ≤ 65 ksi typically, width-to-thickness ratios, etc.)
- Warn if parameters outside typical ranges
- Note all assumptions (bracing conditions, load cases, etc.)
- Compare LRFD and ASD results when both are calculated

---

# Special Notes

## LRFD vs ASD

**LRFD (Load and Resistance Factor Design)**:
- Design strength = φ × Nominal strength
- Load combinations from ASCE/SEI 7-22 (1.2D + 1.6L, etc.)
- Resistance factors (φ) vary by limit state (φ = 0.90 for flexure, 0.75 for bolts, etc.)

**ASD (Allowable Strength Design)**:
- Allowable strength = Nominal strength / Ω
- Load combinations from ASCE/SEI 7-22 (D + L, etc.)
- Safety factors (Ω) vary by limit state (Ω = 1.67 for flexure, 2.00 for bolts, etc.)

**Key**: Same nominal strength, different factors. Both methods give equivalent safety.

## Design Examples Format

- Examples show **LRFD and ASD side-by-side** on same page
- Example numbering: **Letter-Number-Variant** (e.g., E.1A, E.1B, F.1-1A)
- All examples cite specific Specification sections
- Results presented to **three significant figures**

## Version Tracking

- Specification: **AISC 360-22** (August 1, 2022, revised September 2023)
- Design Examples: **Version 16.0** (companion to 16th Edition Manual)
- Always cite version in responses

## Material Defaults

Unless specified otherwise:
- Fy = 50 ksi (typical for W-shapes, Grade 50)
- Fu = 65 ksi (typical for Grade 50)
- E = 29,000 ksi (modulus of elasticity for steel)
- f'c = 4 ksi (typical for normal-weight concrete in composite)

---

For comprehensive structural design work, this skill integrates:
1. **Code requirements** from AISC 360-22 Specification
2. **Practical applications** from Design Examples v16.0
3. **Standard reference materials** (symbols, glossary, indexes)
4. **Custom reference guides** (steel grades, limit states checklist) - NEW in v2.0.0
5. **Accumulated knowledge** (comprehensive design workflows) - NEW in v2.0.0
6. **Automation tools** (search, formula extraction, example matching)

**Always prioritize accuracy, cite sources, and validate calculations against AISC limits.**

---

## What's New in v2.0.0 (2025-11-10)

This version introduces a **response-saving mechanism** inspired by the ADM (Aluminum Design Manual) skill. Key enhancements:

1. **Accumulated Knowledge System**: Comprehensive design guides saved from useful Q&A responses
   - Composite beam construction sequence (1,200 lines)
   - Seismic moment connection workflows (1,100 lines)
   - Growing library of practical guides

2. **Steel Grade Selection Guide**: Complete reference for selecting A992, A572, A36, A500, A588, A913, A514
   - Properties, cost, weldability, applications
   - Selection flowcharts and compatibility tables

3. **Limit States Checklist**: Systematic verification for all member types (60+ checks)
   - Beams, columns, HSS, plate girders, angles, trusses, connections
   - Design phase organization

See `CHANGELOG.md` for complete version history and roadmap.

**Skill Version**: 2.0.0 | **AISC Specification**: 360-22 (2022) | **Design Examples**: v16.0 (2022)
