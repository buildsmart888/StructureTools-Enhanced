# Steel Grade Selection Guide

Quick reference for selecting appropriate structural steel grades for building construction per AISC 360-22.

---

## Common Structural Steel Grades - Summary Table

| Grade | Typical Fy (ksi) | Fu (ksi) | Forms | Typical Cost* | Common Applications |
|-------|-----------------|----------|-------|--------------|---------------------|
| **A992** | 50 (min 50, max 65) | 65 | W, S, M, HP shapes | $$ | Building frames (most common) |
| **A572 Gr.50** | 50 | 65 | Plates, bars, shapes | $$ | Plates, misc. steel |
| **A36** | 36 | 58-80 | Plates, bars, shapes | $ | Older construction, plates |
| **A500 Gr.B/C** | 42/46 (rect), 46/50 (round) | 58/62 | HSS (hollow sections) | $$$ | Columns, bracing, trusses |
| **A913 Gr.50/65** | 50/65 | 65/80 | W, S, M, HP shapes | $$$ | High-strength applications |
| **A588** | 50 | 70 | Plates, shapes | $$$$ | Weathering steel, exposed |
| **A514 Gr.Q** | 100 | 110-130 | Plates (≤2.5 in thick) | $$$$ | High-strength plate girders |

*Relative cost: $ (low) to $$$$ (high)

---

## 1. ASTM A992 - Modern Building Shapes

**Official designation**: ASTM A992/A992M Standard Specification for Structural Steel Shapes

### Key Properties

| Property | Value | Notes |
|----------|-------|-------|
| **Fy** | 50 ksi minimum, 65 ksi maximum | Dual certification (min and max) |
| **Fu** | 65 ksi minimum | |
| **Ry** | 1.1 | Expected yield ratio (AISC 341 Table A3.1) |
| **Rt** | 1.1 | Expected tensile ratio |
| **Carbon equivalent** | ≤ 0.47% (max) | Improved weldability |
| **C/V ratio** | ≤ 5 | Improved toughness |

### Available Forms

- **W-shapes**: W4 through W44 (all standard sizes)
- **HP-shapes**: All standard sizes
- **S-shapes**: Most sizes
- **M-shapes**: Most sizes
- **NOT available**: Plates, bars, angles, channels, tees

### Advantages

1. **Most economical for shapes** - Industry standard, readily available
2. **Excellent weldability** - Low carbon equivalent
3. **Predictable properties** - Maximum Fy limit prevents over-strength
4. **Seismic-ready** - Qualified for SMF, IMF (AISC 341)
5. **Dual certification** - Replaces older A36 and A572 for shapes

### Limitations

1. **Shapes only** - Not available for plates or connection material
2. **Maximum Fy** - 65 ksi cap (but rarely an issue)

### When to Use

- **Default choice** for all W-shape beams and columns in buildings
- Moment frames (ordinary, intermediate, special)
- Braced frames
- Gravity framing
- Any application where Fy = 50 ksi is adequate

### Typical Applications

- Office buildings (beams, columns, girders)
- Industrial buildings (frames, cranes)
- Residential construction (light framing)
- Parking structures

**Design tip**: Always specify "A992" for shapes, not "A36" or "A572 Gr.50". A992 has better properties and same cost.

---

## 2. ASTM A572 Grade 50 - High-Strength Plates and Misc. Steel

**Official designation**: ASTM A572/A572M Standard Specification for High-Strength Low-Alloy Columbium-Vanadium Structural Steel

### Key Properties (Grade 50)

| Property | Value | Notes |
|----------|-------|-------|
| **Fy** | 50 ksi | Same as A992 |
| **Fu** | 65 ksi | Same as A992 |
| **Ry** | 1.1 | Expected yield ratio |
| **Rt** | 1.2 | Expected tensile ratio |

**Other grades available**: Gr. 42, 50, 55, 60, 65 (Fy in ksi)

### Available Forms

- **Plates**: All thicknesses
- **Bars**: Rectangular, square, round
- **Shapes**: W, S, HP (if specifically ordered, but A992 more common)
- **Angles**: All sizes
- **Channels**: All sizes

### Advantages

1. **Versatile** - Available in many forms (plates, bars, angles)
2. **Higher strength than A36** - 39% higher Fy (50 vs 36 ksi)
3. **Good weldability** - Low-alloy steel
4. **Cost-effective** - Only slightly more than A36

### Limitations

1. **Not always stocked** - Check availability for odd sizes
2. **Slightly more expensive** than A36 for plates

### When to Use

- **Plates**: Base plates, gusset plates, shear tabs, stiffeners
- **Connection material**: Angles, channels for connections
- **High-strength bars**: Threaded rods, misc. steel
- **Shapes**: If A992 not available (rare)

### Typical Applications

- Base plates for columns
- Gusset plates in braced frames
- Shear tabs and connection plates
- Beam seats and shelf angles
- Stiffeners for plate girders

**Design tip**: Specify "A572 Gr.50" for all plates and connection material to match A992 beam/column strength.

---

## 3. ASTM A36 - Traditional Carbon Steel

**Official designation**: ASTM A36/A36M Standard Specification for Carbon Structural Steel

### Key Properties

| Property | Value | Notes |
|----------|-------|-------|
| **Fy** | 36 ksi | Lower than A992/A572 |
| **Fu** | 58-80 ksi | Depends on thickness |
| **Ry** | 1.5 (shapes), 1.3 (plates) | Higher variability |
| **Rt** | 1.2 (shapes), 1.1-1.2 (plates) | |

### Available Forms

- **Plates**: All thicknesses (most common use)
- **Bars**: All sizes
- **Shapes**: W, S, HP, L, C (but A992 has replaced for most shapes)

### Advantages

1. **Lowest cost** - Cheapest structural steel grade
2. **Excellent ductility** - High elongation (20% min in 8 in)
3. **Excellent weldability** - Low carbon content
4. **Widely available** - Universal availability
5. **Forgiving** - Easy to work with (cutting, drilling, welding)

### Limitations

1. **Lower strength** - 28% weaker than A992/A572 (Fy = 36 vs 50 ksi)
2. **Heavier members** - Requires larger sections for same capacity
3. **Variable properties** - No maximum Fy (can overshoot)
4. **Shapes being phased out** - A992 has replaced A36 for most W-shapes

### When to Use

- **Large base plates** - Where strength less critical than stiffness
- **Light-duty applications** - Non-critical miscellaneous steel
- **Existing construction** - Matching older buildings (pre-2000)
- **Cost-sensitive projects** - When budget is extremely tight
- **Very thick plates** - Where A572 Gr.50 not available (>4 in thick)

### Typical Applications

- Base plates (light loads)
- Embed plates
- Miscellaneous supports
- Stairs and railings
- Non-structural items
- Older buildings (historical context)

**Design tip**: A36 is being phased out for structural shapes. Use A992 for shapes, A572 Gr.50 for plates in new construction.

---

## 4. ASTM A500 - Hollow Structural Sections (HSS)

**Official designation**: ASTM A500/A500M Standard Specification for Cold-Formed Welded and Seamless Carbon Steel Structural Tubing

### Key Properties

| Shape | Grade | Fy (ksi) | Fu (ksi) | Notes |
|-------|-------|----------|----------|-------|
| **Round** | B | 42 | 58 | Older grade |
| **Round** | C | 46 | 62 | Preferred |
| **Rectangular** | B | 46 | 58 | Older grade |
| **Rectangular** | C | 50 | 62 | Preferred |

**Ry values**: 1.4 (Grade B), 1.3 (Grade C) per AISC 341 Table A3.1

### Available Forms

- **Round HSS**: All standard sizes (e.g., HSS 8.625×0.500)
- **Rectangular HSS**: All standard sizes (e.g., HSS 12×8×1/2)
- **Square HSS**: All standard sizes (e.g., HSS 10×10×5/8)

### Advantages

1. **Torsionally efficient** - Closed section resists torsion
2. **Aesthetically pleasing** - Clean appearance for exposed structure
3. **Efficient columns** - High radius of gyration
4. **Fire protection** - Can fill with concrete (CFT)
5. **Symmetry** - Same strong/weak axis properties (square HSS)

### Limitations

1. **Connection complexity** - Through-plate, slotted, or specialized fittings required
2. **Higher cost** - More expensive than W-shapes per pound
3. **Availability** - Not all sizes stocked, longer lead times
4. **Welding access** - Difficult to weld inside (backup bars)
5. **Inspection** - Interior not accessible for UT

### When to Use

- **Columns** - Especially for architecturally exposed structure (AESS)
- **Bracing members** - Tension and compression bracing in X-braces, K-braces
- **Truss chords and webs** - Roof and floor trusses
- **Composite columns** - Fill with concrete for CFT (concrete-filled tubes)
- **Torsion members** - Beams or members subject to torsion

### Typical Applications

- Exposed structural columns (lobbies, atriums)
- Diagonal bracing in braced frames (X-bracing, chevron bracing)
- Truss members (space frames, long-span roofs)
- Handrails and architectural features
- Canopies and awnings

**Design tip**: Specify "A500 Gr.C" for new construction (higher strength than Gr.B). Check local availability before specifying odd sizes.

---

## 5. ASTM A913 - High-Strength Shapes

**Official designation**: ASTM A913/A913M Standard Specification for High-Strength Low-Alloy Steel Shapes

### Key Properties

| Grade | Fy (ksi) | Fu (ksi) | Notes |
|-------|----------|----------|-------|
| **50** | 50 | 65 | Same as A992 (redundant) |
| **65** | 65 | 80 | High-strength option |
| **70** | 70 | 90 | Rarely used |

### Available Forms

- **W-shapes**: Limited availability (check with suppliers)
- **HP-shapes**: Limited availability

### Advantages

1. **Higher strength** - Gr.65 provides 30% more yield strength than A992
2. **Lighter members** - Can use smaller sections for same capacity
3. **Improved toughness** - Better fracture resistance

### Limitations

1. **Limited availability** - Not stocked, must special-order
2. **Higher cost** - Premium pricing (15-30% more than A992)
3. **Reduced ductility** - Lower elongation at failure
4. **Welding concerns** - May require preheat for thick sections

### When to Use

- **Long-span beams** - Where deflection governs (lighter section still works)
- **Heavy columns** - High axial loads (reduce section size)
- **Special applications** - Unusual loading or span conditions

### Typical Applications

- Transfer girders (heavy loads)
- Crane runway beams (impact loads)
- Long-span floor beams (architectural constraints)

**Design tip**: Rarely specified due to availability and cost. Consider only when A992 sections are too large or too heavy.

---

## 6. ASTM A588 - Weathering Steel

**Official designation**: ASTM A588/A588M Standard Specification for High-Strength Low-Alloy Structural Steel with 50 ksi Minimum Yield Point to 4 in. Thick

### Key Properties

| Property | Value | Notes |
|----------|-------|-------|
| **Fy** | 50 ksi (to 4 in thick) | Reduces for thicker sections |
| **Fu** | 70 ksi | Higher than A992/A572 |
| **Ry** | 1.1 | Expected yield ratio |

### Available Forms

- **Plates**: Up to 8 in thick
- **W-shapes**: Most standard sizes
- **Angles**: Most sizes
- **Channels**: Most sizes

### Advantages

1. **Corrosion resistance** - Forms protective rust patina (no paint needed)
2. **Aesthetic appeal** - Distinctive rust-brown color for architectural exposed steel
3. **Low maintenance** - No repainting required
4. **Long service life** - 2-4x longer than painted carbon steel in many environments

### Limitations

1. **Not for all environments** - Not suitable for marine or high-chloride areas
2. **Staining** - Rust runoff stains adjacent surfaces (concrete, masonry)
3. **Appearance** - Rust color not acceptable for all owners/architects
4. **Higher cost** - 20-40% premium over A992/A572
5. **Welding** - Requires matching electrodes (E8018-C1, etc.)

### When to Use

- **Exposed structure** - Buildings with architectural exposed structural steel
- **Bridges** - Highway and pedestrian bridges (most common application)
- **Outdoor structures** - Sculptures, towers, canopies
- **Coastal areas** - (Not high-salt environments, but moderate coastal)

### Typical Applications

- Architecturally exposed steel buildings (museums, civic buildings)
- Highway bridges (girders, stringers)
- Pedestrian bridges
- Outdoor sculptures and monuments
- Transmission towers

**Design tip**: Requires owner approval due to appearance and runoff staining. Detail to prevent water entrapment (no back-to-back angles, drain holes in HSS, etc.).

---

## 7. ASTM A514 - High-Strength Quenched and Tempered Alloy Steel Plate

**Official designation**: ASTM A514/A514M Standard Specification for High-Yield-Strength, Quenched and Tempered Alloy Steel Plate, Suitable for Welding

### Key Properties (Grade Q, most common)

| Property | Value | Notes |
|----------|-------|-------|
| **Fy** | 100 ksi (plates ≤2.5 in), 90 ksi (2.5-6 in) | Thickness-dependent |
| **Fu** | 110-130 ksi | Very high tensile strength |
| **Ry** | 1.1 | Expected yield ratio |

### Available Forms

- **Plates only**: 1/4 in to 6 in thick

### Advantages

1. **Very high strength** - 2× yield strength of A992/A572
2. **Lighter structures** - Can significantly reduce weight
3. **Tough** - Good impact properties (heat-treated)

### Limitations

1. **Expensive** - 3-5× cost of A572 Gr.50
2. **Limited availability** - Special order, long lead times
3. **Welding complexity** - Requires preheat, controlled interpass temperature, special electrodes
4. **Brittle fracture risk** - Must check toughness at low temperatures
5. **Fastener compatibility** - Requires high-strength bolts (A490 or higher)

### When to Use

- **Plate girders** - Long-span bridges, crane girders
- **High-strength connections** - Gusset plates for heavy loads
- **Weight-critical applications** - Minimize dead load
- **Blast-resistant design** - High ductility and strength

### Typical Applications

- Bridge plate girders (long spans)
- Crane runway girders (heavy-duty industrial)
- Blast-resistant structures (petrochemical, military)
- Heavy equipment supports

**Design tip**: Rarely used in building construction due to cost and complexity. Consider only when weight savings justify premium cost.

---

## Steel Grade Selection Flowchart

```
START: Need to select steel grade
    |
    ├─ SHAPES (W, S, M, HP)?
    |   |
    |   ├─ Standard building frame? → A992 (most common)
    |   ├─ High-strength needed? → A913 Gr.65 (special order)
    |   └─ Exposed weathering? → A588 (architectural)
    |
    ├─ PLATES?
    |   |
    |   ├─ Standard (Fy = 50 ksi)? → A572 Gr.50 (most common)
    |   ├─ Economy (Fy = 36 ksi)? → A36 (low-cost option)
    |   ├─ Exposed weathering? → A588 (architectural)
    |   └─ High-strength (Fy = 100 ksi)? → A514 (special applications)
    |
    ├─ HOLLOW SECTIONS (HSS)?
    |   |
    |   └─ Round or rectangular? → A500 Gr.C (standard)
    |
    └─ ANGLES, CHANNELS, MISC.?
        |
        ├─ Match shapes (Fy = 50)? → A572 Gr.50
        └─ Economy (Fy = 36)? → A36
```

---

## Compatibility Table - Matching Grades for Connections

When designing connections, match steel grades for:
- Base metal and connection material
- Similar strength (avoid weak link)
- Compatible welding characteristics

| Main Member | Connection Material | Notes |
|-------------|-------------------|-------|
| **W-shape (A992, Fy=50)** | A572 Gr.50 plates/angles | Strength match |
| **W-shape (A992, Fy=50)** | A36 plates (if OK for strength) | Lower strength, check carefully |
| **HSS (A500 Gr.C)** | A572 Gr.50 plates | Strength match for through-plates |
| **A588 (weathering)** | A588 plates/angles | Must match for corrosion resistance |
| **A514 (high-strength)** | A514 or A572 Gr.50 | Check connection strength carefully |

**Bolts for each grade**:

| Steel Grade | Bolt Grade | Notes |
|-------------|-----------|-------|
| **A36, A572, A992** | A325 or A490 | A325 typically sufficient |
| **A588** | A325 or A490 | Compatible with weathering steel |
| **A514** | A490 required | Higher-strength bolts required |

---

## Weldability Comparison

| Grade | Carbon Equivalent (CE) | Preheat Required? | Welding Difficulty | Notes |
|-------|----------------------|------------------|-------------------|-------|
| **A992** | ≤ 0.47% | Rarely (>1 in thick) | Easy | Best weldability |
| **A572 Gr.50** | ~0.40-0.45% | Rarely | Easy | Good weldability |
| **A36** | ~0.35-0.40% | No | Very easy | Excellent weldability |
| **A500 Gr.C** | ~0.40-0.45% | Sometimes | Moderate | Cold-formed, may have residual stress |
| **A588** | ~0.50-0.55% | Often (>1/2 in) | Moderate | Requires matching filler (E8018-C1) |
| **A514** | ~0.55-0.70% | Always | Difficult | Requires strict preheat/interpass control |

**Preheat temperatures** (AWS D1.1 Table 3.2):
- A992, A572, A36: 70°F (often no preheat unless thick or cold ambient)
- A588: 150°F (thickness > 3/4 in)
- A514: 225-300°F (depending on thickness and CE)

---

## Cost Comparison (Relative)

Based on typical 2023-2024 pricing (subject to market fluctuations):

| Grade | Relative Cost | $/ton (approx.) | Notes |
|-------|--------------|----------------|-------|
| **A36** | 1.0× (baseline) | $900-1,100 | Cheapest |
| **A572 Gr.50** | 1.05-1.10× | $950-1,200 | Slight premium |
| **A992** | 1.05-1.10× | $950-1,200 | Same as A572 for shapes |
| **A500 Gr.C** | 1.3-1.5× | $1,200-1,600 | Fabrication adds cost |
| **A588** | 1.2-1.4× | $1,100-1,500 | Weathering premium |
| **A913 Gr.65** | 1.5-2.0× | $1,400-2,200 | Special order |
| **A514** | 3.0-5.0× | $2,700-5,500 | Very expensive |

**Note**: Prices are for raw material only. Fabrication, welding, and finishing add to total cost.

---

## Summary Recommendations by Application

| Application | Primary Grade | Alternative | Notes |
|-------------|--------------|-------------|-------|
| **Building beams** | A992 | A913 Gr.65 (heavy) | Use A992 for 95%+ of cases |
| **Building columns** | A992 | HSS A500 Gr.C (AESS) | Shapes cheaper than HSS |
| **Base plates** | A572 Gr.50 | A36 (light loads) | Match column strength (A992) |
| **Gusset plates** | A572 Gr.50 | A36 (light) | Match member strength |
| **Bracing** | HSS A500 Gr.C | W-shapes (heavy) | HSS preferred for bracing |
| **Exposed structure** | A588 (weathering) | A992 (painted) | Weathering if approved |
| **Long-span girders** | A992 | A913 Gr.65 (very long) | Check deflection |
| **Crane runways** | A992 | A913 Gr.65 (heavy-duty) | Impact resistance important |
| **Seismic SMF** | A992 | A913 Gr.50/65 | A992 most common |
| **Seismic bracing** | HSS A500 Gr.C | W-shapes | HSS preferred |

---

## Quick Reference Card

**For 90% of building projects, use:**

1. **W-shapes (beams, columns, girders)**: ASTM A992
2. **Plates (base plates, shear tabs, stiffeners)**: ASTM A572 Gr.50
3. **Hollow sections (columns, bracing)**: ASTM A500 Gr.C
4. **Bolts**: ASTM A325 (bearing), A490 (slip-critical or high-strength)
5. **Weld electrodes**: E70XX (for A992, A572, A36)

**Special cases:**

- Exposed weathering steel: A588 (requires owner approval)
- High-strength applications: A913 Gr.65 or A514 (special order, expensive)
- Historic match: A36 (older buildings, pre-2000)

---

**Last Updated**: 2025-11-10
**References**: AISC 360-22 Table A-3.1, ASTM standards (A36, A572, A588, A992, A500, A913, A514), AWS D1.1 Table 3.2
**Note**: Always verify availability and cost with local suppliers before specifying. Market conditions affect availability.
