# StructureTools Usage Guide
## Section และ Section Manager การใช้งานร่วมกับ Calc

### 🎯 **Overview - ภาพรวมการใช้งาน**

StructureTools มี 3 ส่วนหลักที่ทำงานร่วมกัน:
1. **Section** - กำหนดคุณสมบัติหน้าตัดของวัสดุ  
2. **Section Manager** - จัดการฐานข้อมูลและการตรวจสอบหน้าตัด
3. **Calc** - วิเคราะห์โครงสร้างและคำนวณผลลัพธ์

---

## 📋 **Step-by-Step Usage Guide**

### **Step 1: สร้าง Section Object**

```python
# Method 1: ใช้ GUI Command
import FreeCADGui
FreeCADGui.runCommand("section")  # เปิด Section dialog

# Method 2: ใช้ Python Script
import FreeCAD
from freecad.StructureTools.section import Section, ViewProviderSection

# สร้าง section object
doc = FreeCAD.ActiveDocument
section_obj = doc.addObject("Part::FeaturePython", "W12x26_Section")
Section(section_obj, [])  # ไม่มี selection
ViewProviderSection(section_obj.ViewObject)
doc.recompute()

# กำหนดคุณสมบัติของ section
section_obj.SectionName = "W12x26"  # ชื่อหน้าตัดมาตรฐาน
section_obj.Area = 7.65 * 645.16  # mm² (converted from in²)
section_obj.Iy = 204.4e6  # mm⁴  
section_obj.Iz = 5.46e6   # mm⁴
section_obj.J = 127000    # mm⁴
```

### **Step 2: ใช้ Core Architecture (แนะนำ)**

```python
from freecad.StructureTools.core import (
    get_section_manager,
    detect_section_from_name, 
    get_section_properties,
    generate_section_geometry
)

# วิธีใหม่: ใช้ Section Manager
manager = get_section_manager()

# ตรวจหาหน้าตัดอัตโนมัติจากชื่อ
detected_section = detect_section_from_name("W12X26_BEAM_01")
print(f"Detected section: {detected_section}")  # Output: "W12x26"

# ดึงคุณสมบัติจากฐานข้อมูล
properties = get_section_properties("W12x26")
if properties:
    print(f"Area: {properties['Area']} mm²")
    print(f"Ix: {properties['Ix']} mm⁴") 
    print(f"Weight: {properties['Weight']} kg/m")

# สร้างเรขาคณิต 3D อัตโนมัติ
geometry = generate_section_geometry(properties)
```

### **Step 3: เชื่อมต่อกับ Member (Beam/Column)**

```python
from freecad.StructureTools.member import Member, ViewProviderMember

# สร้าง structural member
member_obj = doc.addObject("Part::FeaturePython", "Beam_01")
Member(member_obj, line_selections)  # line_selections = เส้น geometry
ViewProviderMember(member_obj.ViewObject)

# เชื่อมต่อ section กับ member
member_obj.Section = section_obj  # ผูก section object
member_obj.Label = "W12x26_Beam_Grid_A1-A2"

# หรือใช้ section properties โดยตรง
member_obj.SectionName = "W12x26"
member_obj.Area = properties['Area']
member_obj.Iy = properties['Ix']  # Major axis
member_obj.Iz = properties['Iy']  # Minor axis
```

### **Step 4: การเชื่อมต่อกับ Calc Object**

```python
from freecad.StructureTools.calc import Calc, ViewProviderCalc

# สร้าง calculation object
calc_obj = doc.addObject("Part::FeaturePython", "StructuralAnalysis")
Calc(calc_obj, [member_obj])  # ใส่ members ที่จะวิเคราะห์
ViewProviderCalc(calc_obj.ViewObject)

# Calc จะดึงข้อมูลจาก section โดยอัตโนมัติ
calc_obj.recompute()  # ทริกเกอร์การอัปเดต

# ตรวจสอบว่า section properties ถูกส่งไปแล้ว
print("Members in Calc:")
for member in calc_obj.Group:
    if hasattr(member, 'Section') and member.Section:
        section = member.Section
        print(f"  {member.Label}: Section={section.SectionName}")
        print(f"    Area: {section.Area}")
        print(f"    Iy: {section.Iy}")
```

---

## 🔧 **Advanced Usage - การใช้งานขั้นสูง**

### **1. Custom Section Properties**

```python
# กรณีหน้าตัดที่ไม่มีในฐานข้อมูล
section_obj.SectionName = "Custom"
section_obj.Area = 5000.0      # mm²
section_obj.Iy = 50000000.0    # mm⁴ 
section_obj.Iz = 10000000.0    # mm⁴
section_obj.J = 15000000.0     # mm⁴ (torsion)

# เพิ่มคุณสมบัติขั้นสูง
section_obj.Sy = 125000.0      # Section modulus Y
section_obj.Sz = 50000.0       # Section modulus Z
section_obj.ry = 45.0          # Radius of gyration Y
section_obj.rz = 20.0          # Radius of gyration Z
```

### **2. Section Validation และ Design Checks**

```python
from freecad.StructureTools.data.SectionValidator import (
    validate_section_for_design_code,
    calculate_section_classification
)

# ตรวจสอบตาม design code
is_valid, errors, warnings = validate_section_for_design_code(
    properties, design_code="AISC_360"
)

if not is_valid:
    print("Section validation errors:")
    for error in errors:
        print(f"  - {error}")

if warnings:
    print("Warnings:")
    for warning in warnings:
        print(f"  - {warning}")

# จำแนกประเภทหน้าตัด
classification = calculate_section_classification(
    properties, material_grade="A992"
)
print(f"Section classification: {classification}")  # Compact/Non-compact/Slender
```

### **3. Batch Processing - ประมวลผลหลายหน้าตัด**

```python
# ประมวลผลหลาย members พร้อมกัน
beam_list = ["W12x26", "W14x22", "W16x31", "W18x35"]
members = []

for i, section_name in enumerate(beam_list):
    # Auto-detect และสร้าง section
    properties = get_section_properties(section_name)
    
    if properties:
        # สร้าง member
        member = doc.addObject("Part::FeaturePython", f"Beam_{i+1:02d}")
        Member(member, line_selections[i])
        
        # กำหนด properties
        member.SectionName = section_name
        member.Area = properties['Area']
        member.Iy = properties['Ix']
        member.Iz = properties['Iy'] 
        
        members.append(member)
        print(f"Created {section_name} member with Area={properties['Area']:.0f} mm²")

# เชื่อมต่อทั้งหมดเข้า calc
calc_obj = doc.addObject("Part::FeaturePython", "BuildingAnalysis") 
Calc(calc_obj, members)
```

---

## 🏗️ **Integration Workflow - ลำดับการทำงานแบบครบวงจร**

### **Complete Building Analysis Workflow:**

```python
import FreeCAD
from freecad.StructureTools.core import get_section_manager, get_section_properties
from freecad.StructureTools.member import Member, ViewProviderMember
from freecad.StructureTools.calc import Calc, ViewProviderCalc

doc = FreeCAD.ActiveDocument

# 1. กำหนด structural grid และ sections
building_sections = {
    'beams': ['W12x26', 'W14x22'],
    'columns': ['W12x65', 'W12x79'], 
    'braces': ['HSS6x4x1/4', 'HSS4x4x1/4']
}

# 2. สร้าง members ตาม grid
members = []
section_manager = get_section_manager()

# Beams
for i, beam_section in enumerate(building_sections['beams']):
    properties = get_section_properties(beam_section)
    
    beam = doc.addObject("Part::FeaturePython", f"Beam_{beam_section}_{i+1}")
    Member(beam, beam_lines[i])  # beam_lines = เส้นที่วาดไว้แล้ว
    
    # Auto-assign properties
    beam.SectionName = beam_section
    if properties:
        beam.Area = properties['Area']
        beam.Iy = properties['Ix'] 
        beam.Iz = properties['Iy']
        beam.J = properties.get('J', 0)
    
    members.append(beam)

# Columns  
for i, col_section in enumerate(building_sections['columns']):
    properties = get_section_properties(col_section)
    
    column = doc.addObject("Part::FeaturePython", f"Column_{col_section}_{i+1}")
    Member(column, column_lines[i])
    
    column.SectionName = col_section
    if properties:
        column.Area = properties['Area']
        column.Iy = properties['Ix']
        column.Iz = properties['Iy'] 
    
    members.append(column)

# 3. สร้าง analysis object
calc = doc.addObject("Part::FeaturePython", "BuildingAnalysis")
Calc(calc, members)
ViewProviderCalc(calc.ViewObject)

# 4. ตั้งค่า analysis parameters
calc.LoadCombinations = ['1.2DL+1.6LL', '1.2DL+1.0W', '0.9DL+1.0W']
calc.AnalysisType = 'Linear Static'

# 5. รันการวิเคราะห์
calc.solve()  # เรียกใช้ analysis engine

print(f"Analysis completed with {len(members)} members")
print("Section assignments:")
for member in members:
    print(f"  {member.Label}: {member.SectionName} (Area: {member.Area:.0f} mm²)")
```

---

## 📊 **Results และ Output**

### **ดูผลลัพธ์การวิเคราะห์:**

```python
# ดูผล analysis จาก calc object
if hasattr(calc, 'results') and calc.results:
    print("Analysis Results Summary:")
    
    for member_name, results in calc.results.items():
        print(f"\n{member_name}:")
        print(f"  Max Moment: {results.get('max_moment', 0):.2f} kN⋅m")
        print(f"  Max Shear: {results.get('max_shear', 0):.2f} kN")  
        print(f"  Max Deflection: {results.get('max_deflection', 0):.2f} mm")
        
        # Design ratio check
        if 'design_ratio' in results:
            ratio = results['design_ratio']
            status = "OK" if ratio <= 1.0 else "FAIL"
            print(f"  Design Ratio: {ratio:.3f} [{status}]")

# Generate diagrams
from freecad.StructureTools.diagram import Diagram

for member in members:
    if hasattr(member, 'results'):
        # สร้าง moment diagram
        moment_diagram = doc.addObject("Part::FeaturePython", f"Moment_{member.Label}")
        Diagram(moment_diagram, member, diagram_type="Moment")
        
        # สร้าง shear diagram  
        shear_diagram = doc.addObject("Part::FeaturePython", f"Shear_{member.Label}")
        Diagram(shear_diagram, member, diagram_type="Shear")

doc.recompute()
```

---

## ⚡ **Performance Tips และ Best Practices**

### **1. การใช้งานที่มีประสิทธิภาพ:**

```python
# ใช้ section manager singleton
manager = get_section_manager()  # ครั้งแรก
# manager = get_section_manager()  # ครั้งต่อไปใช้ instance เดิม

# Batch property retrieval
section_names = ["W12x26", "W14x22", "W16x31"]
all_properties = {}
for name in section_names:
    all_properties[name] = get_section_properties(name)

# ใช้ properties ที่ cache แล้ว
for member, section_name in zip(members, section_names):
    props = all_properties[section_name]
    if props:
        member.Area = props['Area']
        member.Iy = props['Ix']
```

### **2. Error Handling:**

```python
from freecad.StructureTools.section import show_error_message, show_warning_message

try:
    properties = get_section_properties(section_name)
    if not properties:
        show_warning_message(
            f"Section '{section_name}' not found in database", 
            title="Section Warning"
        )
        # กำหนดค่าเริ่มต้น
        properties = {'Area': 1000, 'Ix': 10000000, 'Iy': 5000000}
    
    member.Area = properties['Area']
    
except Exception as e:
    show_error_message(
        f"Error setting section properties: {str(e)}", 
        title="Section Error",
        details=f"Section: {section_name}\nMember: {member.Label}"
    )
```

---

## 🎯 **Summary - สรุป**

**การใช้งาน StructureTools แบบ Integrated:**

1. **ใช้ Core Architecture** สำหรับการจัดการ sections ที่ทันสมัย
2. **เชื่อมต่อ Section → Member → Calc** แบบ seamless
3. **ใช้ฐานข้อมูล sections** สำหรับ standard profiles (AISC, EN, HSS)
4. **Validation และ Error Handling** แบบ professional
5. **Performance optimization** ด้วย singleton patterns

**ข้อดี:**
- ✅ ใช้งานง่าย ทั้ง GUI และ Python scripting
- ✅ Database integration ครบครัน 22+ sections  
- ✅ Automatic section detection และ property assignment
- ✅ Professional validation ตาม design codes
- ✅ Seamless integration กับ analysis engine

**พร้อมใช้งานจริงในโปรเจค structural analysis!** 🏗️