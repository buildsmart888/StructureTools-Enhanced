# AISC 360-22 Specification - Consolidated Chapters

**Generated**: 2025-11-09 19:53:14
**Source**: ANSI/AISC 360-22 Specification for Structural Steel Buildings
**Published**: August 1, 2022 (Revised September 2023)
**Output**: 14 chapter files
**Total Size**: 0.42 MB

---

## Document Overview

This directory contains the **AISC 360-22 Specification** organized by chapters. This is the **primary design code** for structural steel buildings in the United States.

**Relationship to Design Examples**:
- **This document (Specification)**: What you **must** follow - formulas, requirements, limits
- **Design Examples**: How to **apply** the specification - step-by-step examples

---

## Chapter Structure

### Specification Chapters (A-N)

| Chapter | Title | Pages | Description |
|---------|-------|------:|-------------|
| **A** | General Provisions | 14 | Scope, materials, and design documents |
| **B** | Design Requirements | 11 | Loads, design basis, member properties |
| **C** | Stability | 6 | Direct analysis method |
| **D** | Tension | 6 | Tensile strength |
| **E** | Compression | 12 | Compressive strength and buckling |
| **F** | Flexure | 25 | Bending strength |
| **G** | Shear | 7 | Shear strength |
| **H** | Combined Forces | 7 | Interaction equations |
| **I** | Composite | 32 | Steel-concrete composite |
| **J** | Connections | 36 | Bolts and welds |
| **K** | HSS Connections | 17 | Hollow section connections |
| **L** | Serviceability | 2 | Deflection limits |
| **M** | Fabrication | 6 | Fabrication requirements |
| **N** | Quality | 13 | QC/QA requirements |

---

## Usage

### For Design Work

Navigate by design topic:
- Need compression member formulas? → `Chapter_E_Compression.md`
- Need beam design criteria? → `Chapter_F_Flexure.md`
- Need connection requirements? → `Chapter_J_Connections.md`

### For AI Skills Development

Each chapter file is optimized for AI context windows (50KB - 150KB).

Example queries:
```python
# Find compression design formulas
Read("a360_chapters/Chapter_E_Compression.md")

# Search for bolt requirements
Grep("bolt spacing", "a360_chapters/Chapter_J_Connections.md")
```

### Cross-Reference with Design Examples

**Workflow**:
1. **Specification** (this directory): Look up the formula/requirement
2. **Design Examples** (`chapters/`): See how to apply it

**Example**:
- Specification Chapter E → Formula for Fcr = ...
- Design Example E.1A → How to use the formula for W-shape column

---

## Statistics

| Chapter | Pages | Size (KB) |
|---------|------:|----------:|
| Chapter A General Provisions | 14 | 31.5 |
| Chapter B Design Requirements | 11 | 24.4 |
| Chapter C Stability | 6 | 15.7 |
| Chapter D Tension | 6 | 11.7 |
| Chapter E Compression | 12 | 22.7 |
| Chapter F Flexure | 25 | 42.1 |
| Chapter G Shear | 7 | 13.1 |
| Chapter H Combined Forces | 7 | 12.6 |
| Chapter I Composite | 32 | 76.2 |
| Chapter J Connections | 36 | 90.8 |
| Chapter K HSS Connections | 17 | 43.8 |
| Chapter L Serviceability | 2 | 3.0 |
| Chapter M Fabrication | 6 | 12.8 |
| Chapter N Quality | 13 | 27.4 |

**Total**: 194 pages, 427.9 KB

---

## Related Files

- **Design Examples**: `../chapters/` (Companion to this Specification)
- **Original Pages**: `../markdown/` (780 files, a360-22w format)
- **Consolidation Script**: `../scripts/consolidate_a360_specification.py`
- **Methodology Guide**: `../MARKDOWN_CONSOLIDATION_GUIDE.md`

---

## Document Structure Not Included

This consolidation includes **only** the Specification chapters (A-N).

**Not included** (available in original pages):
- Front Matter (Symbols, Glossary, Abbreviations) - pages 1-68
- Appendices 1-8 - pages 263-362
- Commentary - pages 363-780

**Rationale**: The Specification chapters are the most frequently referenced content for design work. Appendices and Commentary can be accessed from original page files when needed.

---

## Key Differences: Specification vs. Design Examples

| Aspect | Specification (this) | Design Examples |
|--------|---------------------|-----------------|
| **Purpose** | Code requirements | Application examples |
| **Content** | Formulas, limits, rules | Step-by-step calculations |
| **Structure** | 14 chapters (A-N) | 16 chapters (3 parts) |
| **Pages** | 194 pages | 1,037 pages |
| **Use Case** | "What is required?" | "How do I do it?" |

---

**For questions or issues, refer to the consolidation guide.**
