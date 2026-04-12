# Accumulated Knowledge Repository

This directory contains comprehensive design guides synthesized from useful Claude responses. These are **NOT** extracted from AISC documents - they are **curated knowledge** created through Q&A interactions and saved for future reference.

## Purpose

When Claude provides particularly useful responses that synthesize multiple AISC chapters, include worked examples, or provide practical insights beyond the specification text, those responses can be saved here as permanent reference documents. This creates institutional knowledge that benefits all future users of this skill.

## When to Save a Response

Save a response as an accumulated knowledge document when it meets one or more of these criteria:

1. **Synthesizes multiple AISC chapters** - Combines information from various specification sections into a cohesive workflow
2. **Includes complete worked examples** - Provides step-by-step calculations beyond what's in the standard Design Examples
3. **Provides practical design tips** - Includes engineering judgment and best practices not explicitly stated in AISC
4. **Answers complex multi-step questions** - Addresses sophisticated design scenarios requiring integrated analysis
5. **Creates decision-making frameworks** - Develops flowcharts, checklists, or selection criteria
6. **Fills knowledge gaps** - Addresses topics not thoroughly covered in existing AISC documents

## File Naming Conventions

Use descriptive, hyphenated lowercase names:

- **Good**: `seismic-moment-connection-workflow.md`, `composite-beam-construction-sequence.md`
- **Bad**: `response1.md`, `misc.md`, `notes.md`

Include material or system type if specific:
- `hss-connection-design.md` (HSS-specific)
- `plate-girder-design-procedure.md` (Plate girder-specific)
- `braced-frame-stability-analysis.md` (Braced frame-specific)

## Template Structure

Each accumulated knowledge file should follow this structure:

```markdown
# [Topic] Design Procedure

**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD
**Source Chapters**: AISC 360-22 Chapters [X, Y, Z]
**Purpose**: [One-sentence description of what this document covers]

---

## Overview

[Brief introduction explaining the design scenario and why this topic requires comprehensive guidance]

## Applicable Standards

- AISC 360-22: [Specific chapters/sections]
- AISC Design Examples: [Related examples if any]
- Other references: [e.g., AISC 341, AISC 358, AWS D1.1, etc.]

## Design Workflow

### Step 1: [Task Name]

[Detailed explanation]

**AISC Reference**: Section X.Y

**Formula**:
```
[Formula with clear variable definitions]
```

**Example**:
```
[Numerical example if applicable]
```

### Step 2: [Task Name]

[Continue for all steps...]

## Complete Worked Example

### Given Information

- [List all inputs]

### Solution

[Step-by-step calculations with AISC citations]

### Results Summary

[Tabulated or bulleted final results]

## Design Checklist

Use this checklist to verify all requirements are met:

- [ ] [Verification item 1]
- [ ] [Verification item 2]
- [ ] [Verification item 3]
...

## Common Pitfalls and Best Practices

### Common Pitfalls

1. **[Pitfall description]** - [How to avoid]
2. **[Pitfall description]** - [How to avoid]

### Best Practices

1. **[Practice description]** - [Why it's recommended]
2. **[Practice description]** - [Why it's recommended]

## Comparison with Alternatives

[If applicable, compare this approach with alternative design methods or materials]

| Aspect | Method A | Method B | Recommendation |
|--------|----------|----------|----------------|
| ... | ... | ... | ... |

## Related Topics

- [Link to other accumulated knowledge documents]
- [Link to relevant AISC chapters]
- [Link to relevant Design Examples]

## AISC References

Complete list of all AISC sections cited in this document:

- AISC 360-22 Section X.Y: [Description]
- AISC 360-22 Section Z.W: [Description]
- AISC Design Example [Number]: [Description]

---

**Notes**:
- This is accumulated knowledge, not an official AISC document
- All formulas and procedures cited from AISC 360-22 unless noted
- Practical tips and recommendations are based on engineering judgment
- Always verify critical calculations independently
```

## Quality Control Guidelines

Before saving a response as accumulated knowledge:

1. **Verify all AISC citations** - Ensure every formula references the correct AISC section
2. **Check calculations** - Verify worked examples against AISC Design Examples
3. **Distinguish spec from judgment** - Clearly mark what's from AISC vs. practical tips
4. **Use consistent terminology** - Follow AISC nomenclature (e.g., Fy not fy, LRFD not lrfd)
5. **Include units** - All numerical values must have units (ksi, ft, kip, etc.)
6. **Format formulas clearly** - Use standard AISC notation
7. **Add cross-references** - Link to related accumulated knowledge documents

## Maintenance

Accumulated knowledge documents should be:

- **Updated** when AISC releases new specifications or errata
- **Expanded** when new insights or examples are added
- **Reviewed** periodically for accuracy and completeness
- **Versioned** using the "Last Updated" field

## Current Topics

This directory currently contains the following accumulated knowledge:

### Structural Design

- `composite-beam-construction-sequence.md` - Complete guide for composite beam design considering construction loads, shored/unshored methods, and deflection calculations
- `seismic-moment-connection-workflow.md` - Step-by-step procedure for designing moment connections in seismic applications per AISC 358

### [Additional categories will be added as content grows]

## Proposed Future Topics

Suggested topics for future accumulated knowledge documents:

- Braced frame stability analysis (direct analysis vs effective length method)
- Connection selection flowchart (simple vs moment vs braced)
- Base plate design for high axial loads
- Torsional analysis of open sections
- Serviceability considerations (vibration, drift, deflection)
- HSS connection design (welded vs bolted)
- Plate girder design procedure
- Built-up column design and fabrication
- Pretensioned bolt installation
- Fire protection requirements and elevated temperature design

## Contributing

When adding new accumulated knowledge:

1. Create file following naming conventions
2. Use the template structure above
3. Add entry to "Current Topics" section in this README
4. Consider adding cross-references to related documents
5. Update the "Last Updated" field when making revisions

## Difference from Standard References

| Type | Location | Source | Purpose |
|------|----------|--------|---------|
| **Accumulated Knowledge** | `accumulated-knowledge/` | Synthesized from Q&A | Comprehensive workflows and practical guides |
| **Standard References** | `references/` (parent) | Extracted from AISC | Quick lookup (symbols, glossary, indexes) |
| **AISC Specification** | `data/specification/` | AISC 360-22 official | Authoritative code requirements |
| **AISC Examples** | `data/design-examples/` | AISC official examples | Verified calculation examples |

---

**Last Updated**: 2025-11-10
**Purpose**: Knowledge management system inspired by ADM skill best practices
**Status**: Active - continuously growing with use
