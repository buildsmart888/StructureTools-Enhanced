---
name: basepl-connection-design
description: "AISC Design Guide 1 expert for steel column base plate and anchor rod connection design. Use when users ask about base connections, base plates, anchor rods, column-to-foundation connections, concrete bearing strength, eccentricity, small vs large moment classification, shear transfer, or AISC Design Guide 1. Supports both LRFD and ASD design methods with 15 worked examples covering axial, moment, shear, and biaxial loading."
---

# Base Plate and Anchor Rod Connection Design Expert

Expert system for designing steel column base plate connections per **AISC Design Guide 1: Base Connection Design for Steel Structures (3rd Edition)**.

## When to Use This Skill

Trigger this skill when users ask about:

**English keywords**: base plate, base connection, anchor rod, anchor bolt, column base, foundation connection, pedestal connection, pier connection, base detail, column footing, concrete bearing, bearing plate

**Loading conditions**: compression base, tension base, uplift, moment base, eccentric base, biaxial loading, shear transfer, combined loading

**Design features**: small moment, large moment, eccentricity, e_crit, shear lug, embedded connection, exposed connection, friction shear, concrete breakout

**Materials & codes**: F1554, ASTM anchor, concrete bearing, ACI 318, grout, LRFD base plate, ASD base plate

**Specific topics**: bearing strength, confinement factor, A2/A1 ratio, plate thickness, anchor embedment, h_ef, anchor spacing, tolerance, grouting

## Required Tools

- **Read**: Access chapter files and reference guides
- **Grep**: Search for formulas, equations, specific topics within chapters
- **Glob**: Locate files by pattern
- **Bash**: Execute Python automation scripts (optional, for calculations)
- **Write**: Generate calculation sheets or design summaries (optional)

## Document Structure

This skill provides access to AISC Design Guide 1 content organized as follows:

### Data Directory (`data/`)

**Main Chapter Files** (consolidated from 220 pages):

1. **Chapter_1_Introduction.md** (Pages 1-6, 5.3 KB)
   - General overview, scope, format of worked examples

2. **Chapter_2_Materials.md** (Pages 7-10, 11.9 KB)
   - Base plate materials (A36, A992)
   - Anchor rod specifications (ASTM F1554 Grades 36, 55, 105)
   - Grout and concrete materials
   - Weldability considerations

3. **Chapter_3_Base_Plate_Design.md** (Pages 11-18, 34.7 KB)
   - Base plate design theory
   - Interaction with frames
   - Rotational stiffness modeling
   - Axial load design concepts

4. **Chapter_4_Exposed_Connections.md** (Pages 19-140, 315.6 KB) ⭐ **PRIMARY CHAPTER**
   - Overall design process and flowcharts
   - Load combinations (LRFD and ASD)
   - Limit states for all loading conditions:
     * Axial tension (Section 4.4.1)
     * Axial compression (Section 4.4.2)
     * Combined axial tension + flexure (Section 4.4.3)
     * Combined axial compression + flexure (Section 4.4.4)
     * Biaxial flexure (Section 4.4.5)
     * Shear transfer (Section 4.4.6)
     * Combined loading (Sections 4.4.7, 4.4.8)
   - Anchor rod design per ACI 318 Chapter 17 (Section 4.5)
   - Fabrication and installation (Section 4.6)
   - **15 Worked Examples** (Examples 4.7.1 through 4.7.15)

5. **Chapter_5_Embedded_Connections.md** (Pages 141-150, 18.8 KB)
   - Embedded column base configuration
   - Load transfer mechanisms through embedment
   - Design approach for embedded bases

6. **Chapter_6_Seismic_Design.md** (Pages 151-162, 43.7 KB)
   - Seismic performance requirements
   - Capacity design principles
   - Story drift considerations
   - Braced frame base connections for seismic

7. **Appendix_A_Specialty_Anchors.md** (Pages 163-172, 33.2 KB)
   - Post-installed anchors
   - Specialty anchor systems
   - Alternative anchorage methods

8. **Appendix_B_Alternate_Methods.md** (Pages 173-220, 163.1 KB)
   - Triangular pressure distribution method
   - Alternative design approaches
   - Comparison with main methodology

**Total consolidated data**: 626.3 KB (8 files)

### Reference Directory (`references/`)

Quick-access guides extracted from main content:

1. **examples-index.md** - Complete catalog of 15 worked examples with:
   - Example titles and page numbers
   - Load types and design features
   - Quick reference table
   - Search by loading condition, design feature, or complexity
   - Workflow recommendations

2. **symbols.md** - Standard notation:
   - Geometric parameters (N, B, t_pl, m, n, λ, Y)
   - Load parameters (P_u, M_u, V_u for LRFD; P_a, M_a, V_a for ASD)
   - Stress parameters (f_p, f'_c, F_y, F_ya)
   - Resistance/safety factors (φ, Ω)
   - Material properties

3. **design-flowchart.md** - Decision tree and workflows:
   - Connection type selection (exposed vs embedded)
   - 7 design paths based on loading:
     * Path A: Simple compression
     * Path B: Compression + shear
     * Path C: Tension + shear
     * Path D: Compression + moment
     * Path E: Compression + moment + shear
     * Path F: Biaxial loading
     * Path G: Tension + biaxial
   - Step-by-step procedures for each path
   - Summary decision tree

4. **limit-states-guide.md** - All limit states organized by component:
   - Base plate: bending/yielding
   - Concrete: bearing strength, edge distance
   - Anchor rods: tensile (steel), breakout (concrete), pullout, side-face blowout, shear (steel), breakout (shear), pryout, combined tension-shear
   - Shear transfer: friction, shear lug bearing
   - Welds: column-to-plate
   - Serviceability: tolerances, grout thickness
   - Resistance factors summary table
   - Hierarchy of checks by connection type

5. **anchor-rod-guide.md** - ASTM F1554 anchor rod selection:
   - Grade comparison (36, 55, 105)
   - Common diameters and capacities
   - Embedment depth guidelines
   - Galvanizing considerations
   - Installation tolerances
   - Welding restrictions
   - Quick selection process

6. **load-combinations.md** - LRFD and ASD load combinations:
   - ASCE 7 combinations
   - Critical combinations for base plates
   - LRFD vs ASD comparison
   - Seismic and wind load combinations
   - Governing combination guidance

7. **moment-classification.md** - Small vs large moment:
   - Eccentricity calculation (e = M/P)
   - Critical eccentricity (e_crit)
   - Classification criterion
   - Small moment case characteristics (uniform bearing, no anchor tension)
   - Large moment case characteristics (triangular bearing, anchor tension required)
   - Comparison table and design implications

### Scripts Directory (`scripts/`)

Python automation tools:

1. **consolidate_chapters.py** - Combines 220 page files into 8 chapters (used during skill creation)

2. **smart_search.py** - Keyword-based search across chapters:
   ```bash
   python3 smart_search.py "bearing strength"
   python3 smart_search.py "shear lug" --max-results 10
   ```

3. **base_plate_calculator.py** - Preliminary sizing calculations:
   ```bash
   python3 base_plate_calculator.py --method lrfd --load 200 --fc 4000 --fy 36 --N 18 --B 14
   ```

4. **example_matcher.py** - Find relevant examples by loading:
   ```bash
   python3 example_matcher.py --compression --shear
   python3 example_matcher.py --tension --moment --biaxial
   ```

## Workflow Types

### WORKFLOW 1: Formula Query

**When user asks**: "What is the formula for...", "How do I calculate...", "Show me the equation for..."

**Examples**:
- "What is the formula for concrete bearing strength?"
- "How do I calculate base plate thickness?"
- "Show me the anchor rod tension equation"

**Procedure**:

1. **Identify the formula topic** from user query

2. **Determine relevant chapter**:
   - Concrete bearing → Chapter 4, Section 4.4.2
   - Plate thickness → Chapter 4, Sections 4.4.2, 4.4.3, 4.4.4
   - Anchor tension → Chapter 4, Section 4.5
   - Shear friction → Chapter 4, Section 4.4.6
   - Small/large moment → Chapter 4, Sections 4.4.4

3. **Use Grep to locate formula**:
   ```
   Use Grep tool:
   pattern: "formula keyword" (e.g., "bearing", "thickness", "tension")
   path: Chapter_4_Exposed_Connections.md
   output_mode: content
   -C: 5 (for context lines)
   ```

4. **Extract and present**:
   - Formula in LaTeX format ($$...$$)
   - Variable definitions
   - Applicable limits or conditions
   - LRFD and ASD versions (both shown)
   - Section reference

5. **Provide context**:
   - When this formula applies
   - Related limit states
   - Typical values or ranges
   - Link to relevant example

**Example Output Format**:
```
CONCRETE BEARING STRENGTH (per ACI 318)

LRFD:
φP_p = 0.65 × 0.85f'_c × A1 × √(A2/A1) ≤ 0.65 × 1.7f'_c × A1

ASD:
P_p/Ω = [0.85f'_c × A1 × √(A2/A1)] / 2.31 ≤ [1.7f'_c × A1] / 2.31

Where:
- A1 = base plate area (N × B), in²
- A2 = supporting concrete area
- √(A2/A1) = confinement factor (max = 2.0)
- f'_c = concrete compressive strength, ksi
- φ = 0.65 (LRFD resistance factor)
- Ω = 2.31 (ASD safety factor)

Source: Chapter 4, Section 4.4.2; ACI 318 Section 22.8

See Example 4.7.1 for application with confinement.
```

---

### WORKFLOW 2: Example Query

**When user asks**: "Show me an example...", "Is there a worked example for...", "I need an example of..."

**Examples**:
- "Show me an example of base plate design with shear"
- "Is there an example for biaxial loading?"
- "I need an example of small moment case"

**Procedure**:

1. **Identify loading conditions** from query:
   - Axial: compression, tension
   - Moment: small moment, large moment, biaxial
   - Shear: friction, shear lug
   - Special: braced frame, seismic

2. **Use examples-index.md reference**:
   ```
   Read tool:
   file_path: references/examples-index.md
   ```

3. **Match to appropriate example(s)**:
   - Use "Quick Reference Table" in examples-index.md
   - Match loading type to example number
   - Consider complexity level

4. **Option: Use example_matcher.py script**:
   ```
   Bash tool:
   cd scripts
   python3 example_matcher.py --compression --moment --shear
   ```

5. **Locate example in Chapter 4**:
   ```
   Grep tool:
   pattern: "Example 4\\.7\\.X" (where X is example number)
   path: Chapter_4_Exposed_Connections.md
   output_mode: content
   head_limit: 100 (to get example start)
   ```

6. **Present example summary**:
   - Example number and title
   - Page reference
   - Loading conditions
   - Design approach
   - Key steps
   - Final design results

7. **Suggest related examples** for progressive learning

**Example Output Format**:
```
RELEVANT EXAMPLE FOUND:

Example 4.7.12 - Base Connection for Bending and Axial Compression with Shear (Large Moment)
Pages: 118-124

LOADING:
- Axial compression: P_u = XXX kips (LRFD)
- Moment: M_u = XXX kip-in (large moment case, e > e_crit)
- Shear: V_u = XXX kips

DESIGN APPROACH:
1. Classify moment (large moment → anchor rods required)
2. Solve for bearing length Y (iterative)
3. Calculate anchor rod tension
4. Design anchor rods (steel strength + concrete breakout)
5. Calculate base plate thickness
6. Check shear transfer (friction or shear lug)

KEY RESULTS:
- Base plate: XX" × XX" × X" thick
- Anchor rods: (X) X" diameter, Grade XX
- Embedment: XX" h_ef

RELATED EXAMPLES:
- If moment is small: See Example 4.7.9 or 4.7.11
- For shear lug design: See Example 4.7.5
- For basic concepts: Start with Example 4.7.1 (compression only)

[Would you like me to read and summarize the full example calculations?]
```

---

### WORKFLOW 3: Calculation Query

**When user asks**: "Design a base plate for...", "Calculate the required...", "Size the anchor rods for..."

**Examples**:
- "Design a base plate for 200 kip compression on 4000 psi concrete"
- "Calculate required plate thickness for my column base"
- "Size anchor rods for 50 kips tension"

**Procedure**:

1. **Gather design inputs** from user:
   - Loading: P, M, V (LRFD or ASD)
   - Materials: f'_c (concrete), F_y (plate), anchor grade
   - Column size: W-shape designation or dimensions
   - Constraints: space limitations, existing conditions

2. **Clarify design method**: LRFD or ASD (ask if not specified)

3. **For simple compression** (no moment/shear):
   - Use **base_plate_calculator.py** script:
     ```
     Bash tool:
     cd scripts
     python3 base_plate_calculator.py --method lrfd --load 200 --fc 4000 --fy 36 --N 18 --B 14 --column-depth 12 --column-flange 8
     ```
   - Script calculates:
     * Concrete bearing capacity
     * Bearing stress
     * Required plate thickness
     * Standard plate size recommendation

4. **For complex loading** (moment/shear/biaxial):
   - Identify applicable example using Workflow 2
   - Follow example methodology step-by-step
   - Adapt calculations to user's specific inputs

5. **General calculation steps**:

   **A. Bearing design**:
   - Select trial plate size N × B
   - Calculate A1 = N × B
   - Determine confinement factor √(A2/A1)
   - Calculate φP_p (LRFD) or P_p/Ω (ASD)
   - Check: P_r ≤ available strength

   **B. Moment classification** (if moment present):
   - Calculate e = M_r / P_r
   - Calculate e_crit = N/2 - P_r/q_max
   - Classify: small (e ≤ e_crit) or large (e > e_crit)

   **C. Plate thickness**:
   - Calculate cantilever dimensions m, n
   - Determine critical cantilever
   - Calculate required thickness
   - Select standard plate thickness

   **D. Anchor rod design** (if tension or large moment):
   - Determine number and layout of rods
   - Calculate tension per rod
   - Check steel strength (ACI 318-17.6.1)
   - Check concrete breakout (ACI 318-17.6.2)
   - Select diameter and grade

   **E. Shear transfer** (if shear present):
   - Calculate friction resistance: φV_f = 0.75 × 0.55 × P
   - If insufficient, design shear lug

6. **Present calculation summary**:
   - Design inputs
   - Load combinations checked
   - Key calculations
   - Final design (plate size, thickness, anchor rods)
   - Limit states checked
   - Utilization ratios

7. **Recommend verification**:
   - Reference to applicable example
   - Suggest peer review for critical connections
   - Note any assumptions made

**Output Format**: Structured calculation sheet with inputs, calculations, checks, and final design.

---

### WORKFLOW 4: Design Procedure Query

**When user asks**: "What are the steps to...", "How do I design...", "What is the process for..."

**Examples**:
- "What are the steps to design a base plate?"
- "How do I design for combined compression and moment?"
- "What is the process for anchor rod design?"

**Procedure**:

1. **Identify design scenario**:
   - Connection type: exposed, embedded
   - Loading type: compression, tension, moment, shear, combined
   - Complexity: basic, intermediate, advanced

2. **Use design-flowchart.md reference**:
   ```
   Read tool:
   file_path: references/design-flowchart.md
   ```

3. **Match to design path**:
   - Path A: Simple compression
   - Path B: Compression + shear
   - Path C: Tension + shear
   - Path D: Compression + moment
   - Path E: Compression + moment + shear
   - Path F: Biaxial loading
   - Path G: Tension + biaxial

4. **Extract step-by-step procedure** from flowchart

5. **Enhance with specifics**:
   - Reference relevant section numbers
   - Link to applicable formulas
   - Point to worked examples
   - Note critical decisions (e.g., small vs large moment)

6. **Present as numbered workflow**:
   - Clear sequential steps
   - Decision points highlighted
   - Checks and verifications noted
   - References to detailed resources

**Example Output**:
```
DESIGN PROCEDURE: Base Plate with Compression + Moment + Shear

This follows Design Path E from the design flowchart.

STEP 1: Classify the Moment
  1.1. Calculate eccentricity: e = M_r / P_r
  1.2. Select trial base plate dimensions N × B
  1.3. Calculate e_crit = N/2 - P_r/q_max
  1.4. Determine classification:
       - If e ≤ e_crit → Small moment case (proceed to Step 2A)
       - If e > e_crit → Large moment case (proceed to Step 2B)

STEP 2A: Small Moment Case Design
  2A.1. Material selection (plate, concrete, grout)
  2A.2. Calculate bearing strength (with confinement if applicable)
  2A.3. Verify: P_r ≤ φP_p (LRFD) or P_r ≤ P_p/Ω (ASD)
  2A.4. Calculate required plate thickness
  2A.5. Design column-to-plate welds
  2A.6. Select anchor rods for erection only (typically (4) 3/4" Grade 36)
  2A.7. Proceed to Step 3 for shear design

STEP 2B: Large Moment Case Design
  2B.1. Material selection
  2B.2. Position anchor rods (distance f from column face)
  2B.3. Solve for bearing length Y (iterative solution)
  2B.4. Calculate anchor rod tension: T_r = (M_r + P_r×ε)/(d/2 + f)
  2B.5. Design anchor rods:
        - Number and layout
        - Steel tensile strength check (ACI 318-17.6.1)
        - Concrete breakout strength check (ACI 318-17.6.2)
        - Select diameter and grade
  2B.6. Calculate required plate thickness (bearing and tension zones)
  2B.7. Design column-to-plate welds
  2B.8. Proceed to Step 3 for shear design

STEP 3: Shear Transfer Design
  3.1. Calculate friction resistance: φV_f = 0.75 × 0.55 × P_r
  3.2. Check if V_r ≤ φV_f:
       - YES → Shear resisted by friction, done
       - NO → Shear lug required, proceed to Step 3.3
  3.3. Design shear lug:
       - Required shear: V_lug = V_r - φV_f
       - Size lug for concrete bearing
       - Design lug-to-plate welds

STEP 4: Final Checks
  4.1. If large moment with shear: Check anchor rods for combined tension-shear (ACI 318-17.8)
  4.2. Verify all limit states satisfied
  4.3. Check fabrication and installation requirements (Section 4.6)
  4.4. Document design

REFERENCES:
- Moment classification: references/moment-classification.md
- Small moment case: Chapter 4, Section 4.4.4; Example 4.7.11
- Large moment case: Chapter 4, Sections 4.4.3, 4.4.4; Example 4.7.12
- Shear friction: Chapter 4, Section 4.4.6; Example 4.7.4
- Shear lug: Chapter 4, Section 4.4.6; Example 4.7.5
- Complete flowchart: references/design-flowchart.md
```

---

### WORKFLOW 5: Code Reference Query

**When user asks**: "What does ACI 318 say about...", "What are the AISC requirements for...", "What code section covers..."

**Examples**:
- "What does ACI 318 say about anchor rod breakout?"
- "What are the AISC requirements for base plate welds?"
- "What code section covers concrete bearing?"

**Procedure**:

1. **Identify the code**: ACI 318, AISC Specification, ASCE 7, ASTM standards

2. **Search for code references**:
   ```
   Grep tool:
   pattern: "ACI 318" or "AISC Spec" or "Section X.X.X"
   path: Chapter_4_Exposed_Connections.md (or relevant chapter)
   output_mode: content
   -C: 10 (generous context)
   ```

3. **Common code references in Design Guide 1**:

   **ACI 318 Chapter 17** (Anchoring to Concrete):
   - Section 17.6: Tensile strength of anchors
     * 17.6.1: Steel strength
     * 17.6.2: Concrete breakout strength
     * 17.6.3: Pullout strength
     * 17.6.4: Side-face blowout strength
   - Section 17.7: Shear strength of anchors
     * 17.7.1: Steel strength
     * 17.7.2: Concrete breakout strength
     * 17.7.3: Concrete pryout strength
   - Section 17.8: Interaction of tensile and shear forces
   - Section 17.9: Minimum edge distances and spacing

   **ACI 318 Section 22.8**: Bearing strength of concrete

   **AISC Specification**:
   - Section J2: Welds
   - Chapter J: Connections
   - Section A3.1c: Heat treatment and welding

   **ASCE 7 Chapter 2**: Load combinations

4. **Extract relevant provisions**:
   - Section number and title
   - Key requirements or formulas
   - Resistance/safety factors
   - Applicable limits or conditions
   - Design Guide 1's implementation notes

5. **Present with context**:
   - Code requirement
   - How Design Guide 1 applies it
   - Relevant example demonstrating compliance
   - Related provisions

**Example Output**:
```
ACI 318 PROVISIONS: Anchor Rod Concrete Breakout Strength

CODE REFERENCE: ACI 318, Section 17.6.2

REQUIREMENT:
The nominal concrete breakout strength of a single anchor or anchor group in tension shall be calculated per:

N_cb = (A_Nc / A_Nco) × Ψ_ec,N × Ψ_ed,N × Ψ_c,N × Ψ_cp,N × N_b

Where:
- N_b = basic concrete breakout strength = k_c λ_a √f'_c h_ef^1.5
- k_c = 24 for cast-in anchors
- h_ef = effective embedment depth
- Ψ factors = modification factors for eccentricity, edge distance, cracking, post-installed

RESISTANCE/SAFETY FACTORS:
- LRFD: φ = 0.75
- ASD: Ω = 2.50

DESIGN GUIDE 1 IMPLEMENTATION:
Design Guide 1 applies these provisions in Section 4.5 "Anchorage Design for Concrete Limit States"

Key considerations:
1. Embedment depth h_ef is critical parameter
2. Anchor spacing affects overlapping breakout cones (A_Nc)
3. Edge distance affects Ψ_ed,N factor
4. Cracked concrete assumed (Ψ_c,N = 1.0 for tension)

WORKED EXAMPLES:
- Example 4.7.6: Anchor rod breakout calculation demonstrated
- Example 4.7.8: Anchor group breakout (overlapping cones)
- Example 4.7.12: Breakout strength check for large moment case

RELATED CODE SECTIONS:
- ACI 318-17.6.1: Steel strength of anchors (often governs for small rods)
- ACI 318-17.9: Minimum edge distances and spacing
- ACI 318-17.8: Combined tension and shear interaction

SOURCE:
Chapter 4, Section 4.5; ACI 318-25, Section 17.6.2
```

---

### WORKFLOW 6: Load Combination Query

**When user asks**: "What load combinations should I use...", "How do I combine loads for...", "What's the difference between LRFD and ASD load combinations..."

**Examples**:
- "What load combinations should I use for a base plate?"
- "How do I combine wind and dead load?"
- "What's the LRFD load combination for seismic?"

**Procedure**:

1. **Use load-combinations.md reference**:
   ```
   Read tool:
   file_path: references/load-combinations.md
   ```

2. **Determine applicable load types**:
   - Gravity: D (dead), L (live), S (snow), R (rain)
   - Lateral: W (wind), E (seismic)
   - Special: temperature, construction loads

3. **Identify design method**: LRFD or ASD

4. **Extract relevant combinations**:
   - For gravity-dominated: D + L combinations
   - For uplift/tension: 0.9D or 0.6D with W or E
   - For lateral: combinations with W or E
   - For seismic: E combinations with redundancy and vertical effects

5. **Highlight critical combinations** for base plates:
   - Maximum compression → bearing design
   - Maximum tension → anchor rod design
   - Maximum moment → eccentricity design
   - Maximum shear → shear transfer design

6. **Explain governing combinations**:
   - Different combinations may govern different limit states
   - Envelope design required

**Example Output**:
```
LOAD COMBINATIONS FOR BASE PLATE DESIGN

Your base plate is subjected to: Dead load (D), Live load (L), Wind load (W)

DESIGN METHOD: LRFD

APPLICABLE COMBINATIONS (per ASCE 7):

1. Gravity Loading (Maximum Compression):
   1.2D + 1.6L
   → Governs: Concrete bearing strength, plate thickness (compression zone)

2. Wind Uplift (Maximum Tension):
   0.9D + 1.0W
   → Governs: Anchor rod tension, concrete breakout strength
   → Critical for anchor rod design

3. Wind Lateral (Maximum Moment and Shear):
   1.2D + 1.0W + L
   → Governs: Moment/eccentricity classification, shear transfer
   → Check both upward and downward wind cases

4. Wind Lateral (Alternate):
   1.2D + 1.0W + 0.5L
   → May govern if live load is large

DESIGN WORKFLOW:

Step 1: Generate load cases
- Combine loads per above combinations
- Calculate base reactions: P (axial), M (moment), V (shear)

Step 2: Identify critical combinations
- Maximum P_compression from Combination 1 → bearing design
- Maximum P_tension from Combination 2 → anchor tension design
- Maximum M from Combination 3 → moment design
- Maximum V from Combination 3 → shear design

Step 3: Design for envelope
- Size base plate for maximum compression (Combination 1)
- Design anchor rods for maximum tension (Combination 2)
- Check plate thickness for moment (Combination 3)
- Verify shear transfer (Combination 3)

LRFD VS ASD COMPARISON:

If using ASD instead:
- Combination 1 → D + L (vs. 1.2D + 1.6L in LRFD)
- Combination 2 → 0.6D + 0.6W (vs. 0.9D + 1.0W in LRFD)
- Combination 3 → D + 0.6W (vs. 1.2D + 1.0W + L in LRFD)

Note: ASD loads are approximately 0.6-0.7× LRFD loads, but ASD resistance factors (Ω) are also different.

REFERENCES:
- Complete load combinations: references/load-combinations.md
- Load combination examples: All examples in Chapter 4 show both LRFD and ASD
- ASCE 7, Chapter 2 (source of combinations)
```

---

### WORKFLOW 7: Limit State Query

**When user asks**: "What limit states do I need to check...", "What is concrete breakout...", "How do I check for..."

**Examples**:
- "What limit states do I need to check for a base plate?"
- "What is concrete breakout strength?"
- "How do I check for anchor rod pullout?"

**Procedure**:

1. **Use limit-states-guide.md reference**:
   ```
   Read tool:
   file_path: references/limit-states-guide.md
   ```

2. **Identify connection type and loading**:
   - Compression-dominated → bearing, plate thickness
   - Tension-dominated → anchor steel, concrete breakout
   - Combined loading → multiple limit states

3. **Extract applicable limit states** from guide:
   - Base plate limit states (#1)
   - Concrete/grout limit states (#2-3)
   - Anchor rod limit states (#4-11)
   - Shear transfer limit states (#12-13)
   - Weld limit states (#14)
   - Serviceability (#15-16)

4. **For specific limit state inquiry**:
   - Provide description
   - Failure mode explanation
   - Design formula or check
   - Resistance/safety factors
   - Section references
   - Applicable examples

5. **For general "what to check" query**:
   - Use "Limit State Hierarchy" section
   - Provide checklist based on loading type
   - Order checks by typical sequence

**Example Output**:
```
LIMIT STATES FOR BASE PLATE WITH COMPRESSION + LARGE MOMENT

Based on your loading (axial compression with large moment), check these limit states in order:

PRIMARY LIMIT STATES:

1. Anchor Rod Steel Strength (Limit State #4)
   Description: Anchor rod steel yields or fractures in tension
   Check: φN_sa = 0.75 × 0.75 × A_se × F_uta ≥ T_u (LRFD)
   Status: CRITICAL - Large moment requires anchor rod tension
   Reference: Chapter 4, Section 4.4.1; ACI 318-17.6.1
   Example: 4.7.10, 4.7.12

2. Concrete Breakout Strength (Limit State #5)
   Description: Conical concrete failure around anchor rods
   Failure mode: 35° cone extending from anchor
   Key parameters: Embedment depth h_ef, anchor spacing, edge distance
   Check: Per ACI 318-17.6.2
   φ = 0.75, Ω = 2.50
   Status: CRITICAL - Often governs for anchor groups or shallow embedment
   Reference: Chapter 4, Section 4.5; Example 4.7.6, 4.7.8

3. Concrete Bearing Strength (Limit State #2)
   Description: Concrete crushing under base plate
   Check: φP_p = 0.65 × 0.85f'_c × A1 × √(A2/A1) ≥ C (bearing force)
   Note: Only portion of plate in bearing for large moment case
   Reference: Chapter 4, Section 4.4.2; Example 4.7.12

4. Base Plate Bending (Limit State #1)
   Description: Plate yields under tension or bearing stress
   Critical locations:
   - Tension zone: Between anchor rods
   - Bearing zone: Cantilever beyond column
   Check: Calculate required thickness, select standard plate ≥ t_reqd
   φ = 0.90 (LRFD), Ω = 1.67 (ASD)
   Reference: All examples in Chapter 4

SECONDARY LIMIT STATES (if shear present):

5. Anchor Rod Shear Strength (Limit State #8) - if anchor rods resist shear

6. Shear Friction (Limit State #12) - if compression provides clamping force

SERVICEABILITY CHECKS:

7. Anchor rod hole size and tolerances (Limit State #15)

8. Grout thickness (Limit State #16)

DESIGN SEQUENCE:

Step 1: Design anchor rods for tension
   - Check Limit States #4 and #5
   - Select diameter, grade, embedment h_ef

Step 2: Check concrete bearing
   - Limit State #2 for bearing zone

Step 3: Calculate plate thickness
   - Limit State #1 for both tension and bearing zones

Step 4: Add shear checks if applicable
   - Limit States #8, #12

TYPICAL GOVERNING LIMIT STATES:
For your case (compression + large moment):
- Anchor rod steel strength OR concrete breakout (one will govern)
- Base plate thickness in tension zone
- Concrete bearing (usually satisfied if plate sized for breakout)

REFERENCE:
Complete guide: references/limit-states-guide.md
Resistance factors summary table: See limit-states-guide.md, bottom section
```

---

### WORKFLOW 8: Fabrication/Installation Query

**When user asks**: "What are the tolerances for...", "How do I install...", "What are the grouting requirements..."

**Examples**:
- "What are the anchor rod placement tolerances?"
- "How do I grout a base plate?"
- "What hole size should I use for anchor rods?"

**Procedure**:

1. **Identify fabrication/installation topic**:
   - Tolerances: anchor placement, hole sizes
   - Grouting: thickness, materials, procedures
   - Anchor rod supports and leveling
   - Washers and nuts
   - Field modifications and repairs

2. **Search Chapter 4, Section 4.6**:
   ```
   Grep tool:
   pattern: "fabrication" or "installation" or "tolerance" or "grout"
   path: Chapter_4_Exposed_Connections.md
   output_mode: content
   -C: 10
   ```

3. **Extract specific requirements**:
   - Numerical tolerances
   - Material specifications
   - Procedural steps
   - Code references (AISC Code of Standard Practice)

4. **For field modifications** (Section 4.7):
   - Identify problem type (bent rod, wrong hole, rotated pattern)
   - Locate applicable repair method
   - Provide step-by-step solution

5. **Present with practical guidance**:
   - Standard requirements
   - Best practices
   - Common issues and solutions
   - Quality control checkpoints

**Example Output**:
```
ANCHOR ROD INSTALLATION TOLERANCES AND REQUIREMENTS

PLACEMENT TOLERANCES (per AISC Code of Standard Practice):

Preferred tolerance: ± 1/4"
Maximum tolerance: ± 1/2"

Implications:
- Design base plate holes to accommodate tolerance
- Check anchor rod locations before setting base plate
- Document as-built locations if outside preferred tolerance

ANCHOR ROD HOLE SIZES:

Standard hole size:
- Minimum: d_h = anchor diameter + 1/4"
- Typical: d_h = anchor diameter + 3/8"
- Maximum: d_h = anchor diameter + 1/2"

Example:
- For 1" diameter anchor rod:
  * Minimum hole: 1-1/4" diameter
  * Typical hole: 1-3/8" diameter
  * Maximum hole: 1-1/2" diameter

Oversized holes:
- May require plate washers
- Check load transfer assumptions

GROUTING REQUIREMENTS:

Grout thickness:
- Minimum: 1/2" (some specifications require 1")
- Typical: 1" to 3"
- Maximum: 3" (without special provisions)

Grout strength:
- f'_g ≥ f'_c (concrete strength)
- Typically f'_g = 4000-6000 psi

Grouting procedure:
1. Clean concrete surface (remove laitance, loose material)
2. Dampen concrete surface (SSD condition)
3. Set and level base plate on leveling nuts or shims
4. Pour grout from one side until flows out opposite side
5. Ensure complete fill with no voids
6. Allow proper curing time before applying load

Quality control:
- Verify grout flows completely under plate
- Check for voids by observing grout emergence
- Test grout strength (cylinders per specifications)
- Document grout date and batch information

ANCHOR ROD SUPPORTS:

Leveling methods:
- Leveling nuts on anchor rods
- Shim stacks (removed after grouting or left if designed)
- Templates or frames to hold rod pattern

Requirements:
- Must support erection loads
- Maintain rod verticality
- Allow for final adjustment

WASHERS AND NUTS:

Washer requirements:
- Standard plate washers per ASTM F436
- Oversized washers if holes are oversized
- Beveled washers if anchor rods not perpendicular

Nut requirements:
- Heavy hex nuts per ASTM A563
- Double nut system common (top nut for adjustment, bottom for bearing)

FIELD MODIFICATIONS:

Common issues and solutions (per Section 4.7):

1. Anchor rod bent or not vertical:
   - Minor: Use beveled washers
   - Moderate: Enlarge hole, use oversized washer
   - Severe: Replace anchor rod

2. Anchor rod hole too small:
   - Enlarge hole (verify edge distance maintained)
   - Check plate thickness adequate after enlargement

3. Anchor rod hole too large:
   - Use plate washers
   - Verify bearing area adequate

4. Anchor rod pattern rotated 90°:
   - Check if base plate is symmetric
   - If asymmetric, may require new holes or plate modifications

INSPECTION CHECKLIST:

Before grouting:
☐ Anchor rod locations verified
☐ Anchor rods vertical and plumb
☐ Holes align with anchor rods
☐ Base plate level
☐ Adequate clearance for nuts and washers
☐ Column alignment correct

After grouting:
☐ Grout fully fills space under plate
☐ No voids observed
☐ Grout strength adequate (test cylinders)
☐ Final torque applied to nuts (if specified)

REFERENCES:
- Chapter 4, Section 4.6: Fabrication and Installation
- Chapter 4, Section 4.7: Repair and Field Modification
- AISC Code of Standard Practice, Section 7.13
- Chapter 2, Section 2.5: Grout materials
```

---

## Performance Optimization

To maintain efficiency and token economy:

1. **Progressive disclosure**: Start with references/, only Read full chapters when detailed content needed

2. **Script priority**: Use Python scripts for calculations when applicable (more token-efficient than manual calculation)

3. **Search strategy**:
   - Start: Check references/ for quick answers
   - If not found: Use Grep on specific chapter
   - Last resort: Read entire chapter sections

4. **Example usage**: Direct users to examples-index.md first, only Read full example text if user wants detailed walkthrough

5. **Chapter priority** by frequency:
   - Primary: Chapter 4 (most queries), references/
   - Secondary: Chapter 3, Chapter 2
   - Occasional: Chapter 5, Chapter 6, Appendices

## Quality Checklist

Before providing final answer, verify:

- ✓ Both LRFD and ASD methods addressed (if applicable)
- ✓ Resistance/safety factors stated correctly
- ✓ Formula variables defined
- ✓ Units specified (kips, ksi, inches)
- ✓ Section/page references provided
- ✓ Applicable example cited
- ✓ Limitations or assumptions noted
- ✓ Safety-critical information flagged

## Error Handling

**If data files not found**:
- Check paths relative to skill directory
- Verify consolidation completed
- Fall back to describing methodology

**If formula search yields no results**:
- Try alternate keywords
- Broaden search to related topics
- Reference section numbers from references/

**If user loading is unclear**:
- Ask clarifying questions using AskUserQuestion tool
- Provide examples of typical load cases
- Use example_matcher.py to explore options

**If calculation is beyond scope**:
- Direct to most applicable example
- Provide methodology overview
- Recommend structural engineer review for critical connections

## Critical Distinctions to Emphasize

1. **LRFD vs ASD**: Always present both unless user specifies one method

2. **Small vs Large Moment**: This classification fundamentally changes design approach
   - Small (e ≤ e_crit): Uniform bearing, no anchor tension
   - Large (e > e_crit): Triangular bearing, anchor rods required

3. **Exposed vs Embedded**: Different load transfer mechanisms

4. **Confinement factor**: √(A2/A1) can significantly increase bearing strength (up to 2.0×)

5. **Anchor rod grades**: Grade 36 is default; higher grades for space constraints, not routine

6. **Friction vs Shear Lug**: Friction coefficient μ = 0.55; if insufficient, shear lug required

7. **ACI 318 Chapter 17**: Governs all anchor rod design (steel strength, concrete breakout, interaction)

## Usage Notes

- This skill covers **AISC Design Guide 1 (3rd Edition)** content only
- For other base plate standards or international codes, note limitations
- Seismic design (Chapter 6) supplements, but doesn't replace AISC Seismic Provisions
- Post-installed anchors: Mentioned but not detailed (refer to ACI 355.2)
- Field modifications: Guidance provided, but engineer judgment required

---

*Last Updated: 2025-11-14*
*Skill Version: 1.0*
*Data Source: AISC Design Guide 1, Base Connection Design for Steel Structures (3rd Edition)*
