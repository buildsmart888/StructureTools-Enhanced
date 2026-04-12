# AISC Steel Design Skill - Change Log

All notable changes to this skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [2.0.0] - 2025-11-10

### Major Enhancement: ADM-Inspired Knowledge Management System

This release represents a significant upgrade to the AISC skill, implementing best practices learned from the ADM (Aluminum Design Manual) skill. The primary enhancement is the addition of a **response-saving mechanism** for accumulated knowledge, transforming the skill from a static document repository into a living knowledge management system.

### Added

#### 1. Accumulated Knowledge System

**New Directory**: `references/accumulated-knowledge/`

A complete knowledge management system for saving useful Q&A responses as permanent reference documents:

- **README.md** (600 lines)
  - Guidelines for when and how to save responses
  - Template structure for accumulated knowledge documents
  - Quality control guidelines
  - Maintenance procedures
  - Proposed future topics list

- **composite-beam-construction-sequence.md** (1,200 lines)
  - Comprehensive guide for composite beam design
  - Shored vs unshored construction comparison
  - Complete worked example (W18×50, 30 ft span)
  - Step-by-step workflow from load calculation through deflection
  - Construction stage vs final stage strength checks
  - Deflection calculations with camber recommendations
  - Design checklist with 25+ verification items
  - Common pitfalls and best practices
  - Synthesizes AISC 360 Chapters F, G, I, and L

- **seismic-moment-connection-workflow.md** (1,100 lines)
  - Complete RBS (Reduced Beam Section) connection design procedure
  - Comparison of all AISC 358 prequalified connection types
  - SMF vs IMF vs OMF frame systems
  - Step-by-step design workflow (10 steps)
  - Complete worked example (W27×94 beam, W14×211 column)
  - Panel zone design with doubler plate calculations
  - Strong-column/weak-beam verification
  - Continuity plate requirements
  - Quality control and welding requirements per AWS D1.8
  - Design checklist with 30+ verification items
  - Synthesizes AISC 358, AISC 341, and AISC 360

**Impact**: These accumulated knowledge documents provide comprehensive design guidance that goes beyond the AISC specification, incorporating practical insights, worked examples, and best practices that would typically only be learned through years of experience.

#### 2. Material Selection Guide

**New File**: `references/steel-grade-guide.md` (650 lines)

Comprehensive guide for selecting appropriate structural steel grades:

- **7 common steel grades** with detailed properties:
  - ASTM A992 (modern building shapes)
  - ASTM A572 Gr.50 (plates and misc. steel)
  - ASTM A36 (traditional carbon steel)
  - ASTM A500 Gr.C (hollow structural sections)
  - ASTM A913 Gr.65 (high-strength shapes)
  - ASTM A588 (weathering steel)
  - ASTM A514 (high-strength quenched/tempered plate)

- **Comparison tables** for:
  - Properties (Fy, Fu, Ry, Rt)
  - Availability by form (shapes, plates, HSS)
  - Cost comparison (relative pricing)
  - Weldability comparison (preheat requirements)

- **Selection guidance**:
  - Steel grade selection flowchart
  - Compatibility table for matching grades in connections
  - Bolt selection by steel grade
  - Quick reference card for common applications

- **Application-specific recommendations**:
  - Building beams, columns, bracing
  - Base plates and gusset plates
  - Exposed structure (AESS)
  - Seismic applications (SMF, IMF)

**Impact**: This fills a critical gap in the AISC skill. While steel is more uniform than aluminum, structural engineers still need guidance on when to use A992 vs A572 vs A36, and this guide provides that in an easily accessible format.

#### 3. Comprehensive Limit States Checklist

**New File**: `references/limit-states-checklist.md` (700 lines)

Systematic checklist of all limit states to verify for each member type:

- **9 member categories**:
  1. W-shape beams (flexural members)
  2. W-shape columns (compression members)
  3. HSS (hollow structural sections)
  4. Plate girders
  5. Angles (single and double)
  6. Trusses
  7. Connections (bolted and welded)
  8. Base plates
  9. Braced frame connections (SCBF, OCBF)

- **60+ limit state checks** covering:
  - Flexure (yielding, LTB, FLB, WLB)
  - Compression (flexural buckling, local buckling)
  - Tension (yielding, rupture, block shear)
  - Shear (yielding, buckling)
  - Combined forces (interaction equations)
  - Connections (bolts, welds, bearing)
  - Local effects (web crippling, yielding, bearing)
  - Serviceability (deflection, vibration)

- **Design phase checklist**:
  - Preliminary design
  - Detailed design
  - Final checks

**Impact**: Ensures no limit states are overlooked during design. This is especially valuable for junior engineers or when designing unfamiliar member types.

#### 4. Version Control System

**New File**: `CHANGELOG.md` (this file)

Tracks all changes to the skill over time:

- Documents feature additions
- Records bug fixes and corrections
- Tracks improvements to existing content
- Links to AISC specification updates and errata

**Impact**: Provides transparency into skill evolution and helps users understand what's new or changed.

### Changed

None in this release (all changes are additions to preserve existing functionality).

### Deprecated

None in this release.

### Removed

None in this release.

### Fixed

None in this release (initial changelog entry).

---

## [1.0.0] - 2025-11-01 (Approximate)

### Initial Release

**Core Features**:

- **Data Organization**:
  - AISC 360-22 Specification (14 chapters consolidated from 780 pages)
  - AISC Design Examples v16.0 (93 examples across 16 chapter files)
  - 7 reference files (symbols, glossary, indexes)

- **Python Scripts** (5 automation tools):
  - `smart_search.py` - Category-aware keyword search
  - `formula_finder.py` - Pattern-based formula extraction
  - `cross_reference.py` - Spec ↔ Examples linking
  - `example_matcher.py` - Query-to-example matching
  - `extract_front_matter.py` - Automated reference generation

- **SKILL.md**: 446-line skill definition with 7 query types

**Capabilities**:
- Intelligent document search (130+ keywords mapped to categories)
- Automatic formula extraction (50+ engineering formulas)
- Cross-reference tracking between specification and examples
- Example matching (93 examples indexed)

**Coverage**:
- Complete AISC 360-22 Specification
- Complete AISC Design Examples v16.0
- Chapters A through N (general provisions through fabrication)
- 93 worked examples across 16 categories

---

## Comparison: v1.0.0 vs v2.0.0

| Feature | v1.0.0 | v2.0.0 | Improvement |
|---------|--------|--------|-------------|
| **Document types** | 2 (Spec + Examples) | 2 + Accumulated Knowledge | +Knowledge management |
| **Reference files** | 7 (extracted) | 10 (7 extracted + 3 custom) | +43% |
| **Knowledge accumulation** | Static | **Dynamic** (response-saving) | Transformative |
| **Material guidance** | None | Steel grade guide | New capability |
| **Design checklists** | None | Limit states checklist | New capability |
| **Version tracking** | None | CHANGELOG.md | New capability |
| **Total reference content** | ~50 KB | ~200 KB | +300% |
| **Practical guides** | 0 | 2 (composite beams, seismic connections) | New capability |

---

## Future Roadmap

### Planned for v2.1.0

**Additional Accumulated Knowledge Documents**:
1. Braced frame stability analysis (direct analysis vs effective length method)
2. Connection selection flowchart (simple vs moment vs braced)
3. Base plate design for high axial loads
4. Torsional analysis of open sections

**Additional Reference Guides**:
5. Temperature effects guide (elevated temperature, fire, cold brittle fracture)
6. Welding quality guide (AWS D1.1, prequalified connections, inspection)

**Enhanced Automation**:
7. `grade_selector.py` - Interactive steel grade selection tool
8. `beam_design_template.py` - Complete beam design automation
9. Enhanced `smart_search.py` - Include accumulated-knowledge directory in searches

**Organizational Improvements**:
10. `examples-by-topic.md` - Reorganize 93 examples by topic (not just chapter)
11. `flowcharts/member-selection.md` - Visual decision trees for member selection

### Planned for v2.2.0

**Calculation Templates**:
- Python templates for common design tasks (beams, columns, connections)
- Automated limit state checking
- Result formatting with AISC citations

**Enhanced Cross-Referencing**:
- Spec section → Commentary (if available)
- Spec section → Related seismic provisions (AISC 341)
- Example → All referenced spec sections
- Dependency graph (which formulas require which inputs)

**Additional Examples**:
- HSS connection design workflows
- Composite beam with construction sequence variations
- Plate girder design procedure

### Planned for v3.0.0

**RAG Integration**:
- ChromaDB vector indexing of all documents
- Semantic search capabilities
- Query understanding and intent classification

**Interactive Tools**:
- Web-based calculation tools
- Visual design aids
- Connection design visualization

**Extended Coverage**:
- AISC 341 (Seismic Provisions) integration
- AISC 358 (Prequalified Connections) full coverage
- ASCE 7 load combinations and combinations

---

## How to Contribute Accumulated Knowledge

If you create a particularly useful response that should be saved to accumulated knowledge:

1. **Check if it meets criteria** (see `references/accumulated-knowledge/README.md`):
   - Synthesizes multiple AISC chapters
   - Includes complete worked examples
   - Provides practical insights beyond specification text
   - Addresses complex multi-step questions

2. **Use the template** from README.md:
   - Include creation date, source chapters, purpose
   - Provide overview, workflow, worked example, checklist
   - Distinguish AISC requirements from engineering judgment
   - Include all AISC citations

3. **Save to accumulated-knowledge directory**:
   - Use descriptive filename (e.g., `plate-girder-design-procedure.md`)
   - Add entry to README.md current topics list
   - Update this CHANGELOG.md under "Added" section

4. **Quality control**:
   - Verify all formulas cite AISC sections
   - Check worked examples against AISC Design Examples
   - Use consistent terminology (AISC nomenclature)
   - Include units for all numerical values

---

## Acknowledgments

**v2.0.0 Enhancements Inspired By**:
- ADM (Aluminum Design Manual) skill architecture
- ADM's response-saving mechanism (evidence: `알루미늄기둥.md`)
- ADM's material-specific reference system (alloy-guide, HAZ-factors, etc.)
- ADM's comprehensive documentation approach

**Why ADM Architecture Was Adopted**:

The ADM skill demonstrated superior knowledge management through:

1. **Response-saving mechanism** - Converts useful Q&A into permanent knowledge
2. **Material-specific guidance** - Detailed guides for complex material properties
3. **Comprehensive coverage** - All manual parts included (Spec + Commentary + Guide + Examples + Reference Data)
4. **Accumulated knowledge** - Growing knowledge base that improves with use

While aluminum design is inherently more complex than steel design (alloy/temper variations, HAZ effects, temperature limits), the **knowledge management principles** are universally applicable. The AISC skill v2.0.0 adopts these principles while focusing on steel-specific needs.

---

## Version Numbering

This project follows [Semantic Versioning](https://semver.org/):

- **MAJOR version** (X.0.0): Incompatible changes or major restructuring
- **MINOR version** (0.X.0): New features added in backward-compatible manner
- **PATCH version** (0.0.X): Bug fixes and minor corrections

**Current version**: 2.0.0 (major enhancement with new knowledge management system)

---

## AISC Specification Updates

**Current AISC Version Coverage**: AISC 360-22 (16th Edition, July 2022)

**Future Updates**:
- AISC 360 errata and clarifications will be tracked here
- When AISC 360-25 (or later) is released, this changelog will document migration

**Related Standards**:
- AISC 341-22: Seismic Provisions (partial coverage in accumulated knowledge)
- AISC 358-22: Prequalified Connections (covered in seismic-moment-connection-workflow.md)
- AWS D1.1/D1.8: Welding codes (referenced in guides)

---

**Changelog Format**: Follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
**Version History**: This file documents all changes from v1.0.0 forward
**Last Updated**: 2025-11-10
