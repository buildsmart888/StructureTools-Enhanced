# Load Distribution Visualization - Quick Reference

## 🚀 Quick Start (5 นาที)

### 1. ทดสอบว่าติดตั้งสำเร็จ
```python
# เปิด FreeCAD Python Console แล้วรัน:
from freecad.StructureTools.visualization.LoadDistributionVisualizer import *
from freecad.StructureTools import test_load_distribution
test_load_distribution.run_all_tests()
```

### 2. สร้าง Visualization แบบเร็ว
```python
import FreeCAD as App
from freecad.StructureTools.visualization.LoadDistributionVisualizer import *

# สร้าง document
doc = App.ActiveDocument or App.newDocument("Test")

# กำหนดมุมพื้น (6m × 5m)
corners = [
    App.Vector(0, 0, 0),
    App.Vector(6000, 0, 0),
    App.Vector(6000, 5000, 0),
    App.Vector(0, 5000, 0)
]

# สร้าง visualization
viz = LoadDistributionVisualizer(doc)
viz.visualize_slab_with_beam_loads(corners, 10.0, "two_way", "QuickTest")

doc.recompute()
```

## 📋 Commands Reference

### GUI Commands

| Command | Location | Hotkey | Description |
|---------|----------|--------|-------------|
| **Create Area Load** | StructureLoad Toolbar | - | สร้าง area load บนหน้าที่เลือก |
| **Visualize Load Distribution** | StructureLoad Toolbar | - | แสดง visualization (ต้องเลือก AreaLoad ก่อน) |
| **Clear Load Distribution** | StructureLoad Toolbar | - | ลบ visualization ทั้งหมด |

### Python API

```python
# Import
from freecad.StructureTools.visualization.LoadDistributionVisualizer import (
    LoadDistributionVisualizer, 
    SlabLoadCalculator
)

# Create visualizer
viz = LoadDistributionVisualizer(App.ActiveDocument)

# Two-Way Slab
viz.visualize_two_way_yield_line(corners, load_intensity=10.0, name_prefix="TwoWay")

# One-Way Slab
viz.visualize_one_way_distribution(corners, span_direction="short", 
                                   load_intensity=10.0, name_prefix="OneWay")

# Beam Loads
viz.visualize_beam_distributed_load(start, end, load_type="triangular", 
                                    w1=20.0, w2=0, name_prefix="Beam")

# Complete (All-in-One)
viz.visualize_slab_with_beam_loads(corners, load_intensity=10.0,
                                   distribution_type="two_way",  # or "one_way"
                                   name_prefix="Complete")

# Clear
viz.clear_visualization()

# Calculator
calc = SlabLoadCalculator()
beam_loads = calc.calculate_two_way_beam_loads(corners, load_intensity=10.0)
calc.print_beam_loads(beam_loads)
```

## 📐 Corner Definition Rules

### ✅ Correct (Counterclockwise)
```
D(0,5000) -------- C(6000,5000)
   |                    |
   |                    |
   |                    |
A(0,0) ---------- B(6000,0)

corners = [A, B, C, D]  # Counterclockwise
```

### ❌ Wrong (Clockwise)
```
corners = [A, D, C, B]  # Don't use!
```

## 🎨 Visualization Objects

### Two-Way Slab Creates:
```
✓ 4 Yield Lines (orange, dashed)
✓ 4 Tributary Areas (colored, 50% transparent)
✓ 1 Boundary (black, solid)
✓ 4 Beam Loads (below slab, with arrows)
✓ 1 Load Label (text annotation)
```

### One-Way Slab Creates:
```
✓ 4 Strip Lines (blue, dashed)
✓ 1 Slab Face (colored, 50% transparent)
✓ 1 Boundary (black, solid)
✓ 2 Beam Loads (on supporting edges)
✓ 1 Load Label (text annotation)
```

## 💡 Common Use Cases

### Use Case 1: Two-Way Slab Load Pattern
```python
# For slabs with Lx/Ly < 2.0
viz.visualize_two_way_yield_line(corners, load_intensity=12.0, name_prefix="Floor")
```
**When to use:** 
- Square or nearly square slabs
- All 4 edges supported
- Need to show yield line pattern

### Use Case 2: One-Way Slab Load Pattern
```python
# For slabs with Lx/Ly >= 2.0
viz.visualize_one_way_distribution(corners, "short", load_intensity=8.0, name_prefix="Balcony")
```
**When to use:**
- Long rectangular slabs
- 2 parallel edges supported
- Clear spanning direction

### Use Case 3: Calculate Beam Reactions Only
```python
calc = SlabLoadCalculator()
results = calc.calculate_two_way_beam_loads(corners, 10.0)

# Access data
for edge, data in results.items():
    load_type = data['load_type']  # 'triangular' or 'trapezoidal'
    total_force = data['total_force']  # kN
    length = data['length']  # m
```

### Use Case 4: Compare Two-Way vs One-Way
```python
# Two-Way at origin
corners_2way = [App.Vector(0,0,0), ...]
viz.visualize_slab_with_beam_loads(corners_2way, 10.0, "two_way", "Compare_2Way")

# One-Way offset
corners_1way = [App.Vector(10000,0,0), ...]
viz.visualize_slab_with_beam_loads(corners_1way, 10.0, "one_way", "Compare_1Way")
```

## 🔧 Troubleshooting

### Problem: ไม่เห็น visualization
**Solution:**
```python
App.ActiveDocument.recompute()
Gui.updateGui()
Gui.SendMsgToActiveView("ViewFit")
```

### Problem: Load ไม่สมดุล (total ≠ sum of reactions)
**Check:**
1. หน่วย: Corners ใช้ mm, Load ใช้ kN/m²
2. มุม: ต้องเป็น counterclockwise
3. รูปร่าง: ต้องเป็นสี่เหลี่ยมจัตุรัส

### Problem: Commands ไม่แสดงใน toolbar
**Fix:**
```python
# ตรวจสอบใน init_gui.py
from freecad.StructureTools import command_load_distribution

# Restart FreeCAD
```

### Problem: สี visualization เหมือนสี background
**Solution:**
```python
# เปลี่ยนสี
viz.yield_line_color = (1.0, 0.0, 0.0)  # Red
viz.one_way_color = (0.0, 1.0, 0.0)     # Green
viz.load_arrow_color = (0.0, 0.0, 1.0)  # Blue
```

## 📊 Load Calculation Formulas

### Two-Way Slab

**Short Edges (Triangular):**
```
w_max = q × (L_short / 2)
F_total = q × L_short × L_long / 4
```

**Long Edges (Trapezoidal):**
```
w_uniform = q × (L_short / 2)
F_total = q × L_long × L_short / 4
```

### One-Way Slab

**Supporting Edges (Uniform):**
```
w = q × L_span / 2
F_total = w × L_beam
```

## 🎯 Best Practices

### 1. Naming Convention
```python
# Good
viz.visualize_two_way_yield_line(corners, 10.0, "Floor_L2_Grid_A1")
viz.visualize_one_way_distribution(corners, "short", 8.0, "Balcony_North")

# Bad
viz.visualize_two_way_yield_line(corners, 10.0, "test")
viz.visualize_two_way_yield_line(corners, 10.0, "abc123")
```

### 2. Clear Before Recreate
```python
# Always clear before creating new visualization
viz.clear_visualization()
viz.visualize_slab_with_beam_loads(corners, ...)
```

### 3. Check Results
```python
# Always verify load balance
calc = SlabLoadCalculator()
results = calc.calculate_two_way_beam_loads(corners, load)
calc.print_beam_loads(results)  # Check console output

# Verify total
total_load = load * Lx * Ly
total_reactions = sum(d['total_force'] for d in results.values())
print(f"Error: {abs(total_load - total_reactions):.2f} kN")
```

### 4. Document Settings
```python
# Add comments in your script
# Slab: 6m × 5m, Two-Way
# Load: 10 kN/m² (DL + LL)
# Code: ACI 318-19
viz.visualize_slab_with_beam_loads(corners, 10.0, "two_way", "Floor_6x5")
```

## 📚 Example Scripts

### Example 1: Simple Two-Way Slab
```python
import FreeCAD as App
from freecad.StructureTools.visualization.LoadDistributionVisualizer import *

doc = App.ActiveDocument or App.newDocument("Example1")
corners = [
    App.Vector(0, 0, 0),
    App.Vector(5000, 0, 0),
    App.Vector(5000, 5000, 0),
    App.Vector(0, 5000, 0)
]

viz = LoadDistributionVisualizer(doc)
viz.visualize_two_way_yield_line(corners, 10.0, "Example1")
doc.recompute()
```

### Example 2: Multiple Slabs
```python
slabs = [
    {"corners": [...], "load": 10.0, "type": "two_way", "name": "Slab_A"},
    {"corners": [...], "load": 8.0, "type": "one_way", "name": "Slab_B"},
    {"corners": [...], "load": 12.0, "type": "two_way", "name": "Slab_C"},
]

viz = LoadDistributionVisualizer(App.ActiveDocument)
for slab in slabs:
    viz.visualize_slab_with_beam_loads(
        slab["corners"],
        slab["load"],
        slab["type"],
        slab["name"]
    )
```

### Example 3: Export Beam Loads to CSV
```python
import csv

calc = SlabLoadCalculator()
results = calc.calculate_two_way_beam_loads(corners, 10.0)

with open('beam_loads.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Edge', 'Type', 'w_max (kN/m)', 'Length (m)', 'Total Force (kN)'])
    
    for edge, data in results.items():
        writer.writerow([
            edge,
            data['load_type'],
            data.get('w_max', data.get('w', 0)),
            data['length'],
            data['total_force']
        ])
```

## ⚡ Performance Tips

1. **Large Models:** Clear visualization before creating new ones
2. **Multiple Slabs:** Use batch processing with loop
3. **Recompute:** Only recompute when needed
4. **Memory:** Remove unused visualizations with `ClearLoadDistribution` command

## 🔗 Related Documentation

- **Full Documentation:** `visualization/README_LoadDistribution.md`
- **Development Summary:** `DEVELOPMENT_SUMMARY_LoadDistribution.md`
- **Test Suite:** `test_load_distribution.py`
- **Source Code:** `visualization/LoadDistributionVisualizer.py`

## 📞 Support

For issues or questions:
1. Check troubleshooting section above
2. Review full documentation
3. Run test suite to verify installation
4. Check FreeCAD console for error messages

---

**Version:** 1.0  
**Last Updated:** 2025-12-17  
**Status:** Production Ready ✅
