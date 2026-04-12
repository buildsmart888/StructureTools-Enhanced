# ระบบฐานข้อมูล Material Standards ใน StructureTools

คู่มือการใช้งานระบบฐานข้อมูลวัสดุที่ปรับปรุงใหม่ สำหรับการสร้างและจัดการวัสดุเพื่อใช้ในการวิเคราะห์โครงสร้าง

## ✨ ความสามารถใหม่

### 🔧 ระบบ Material ที่ปรับปรุงแล้ว
- ✅ **รองรับฐานข้อมูลมาตรฐาน**: ดึงข้อมูลจาก ASTM, EN, ACI และ มาตรฐานอลูมิเนียม
- ✅ **รองรับทั้ง Material เดิมและ StructuralMaterial ใหม่**: ทำงานร่วมกันได้อย่างสมบูรณ์
- ✅ **เชื่อมต่อกับ calc โดยตรง**: ส่งคุณสมบัติไปยัง Pynite analysis engine อัตโนมัติ
- ✅ **ตรวจสอบความถูกต้อง**: ตรวจสอบค่า Poisson ratio และคุณสมบัติอื่นๆ
- ✅ **จัดการหน่วยโดยอัตโนมัติ**: รองรับหน่วย m-kN, mm-N และระบบหน่วยอื่นๆ

### 🎯 มาตรฐานที่รองรับ

#### เหล็ก (Steel)
- **ASTM_A36**: เหล็กโครงสร้างมาตรฐาน (Fy = 250 MPa)
- **ASTM_A992**: เหล็กคาน H-beam มาตรฐาน (Fy = 345 MPa)  
- **ASTM_A572_Gr50**: เหล็กความแข็งแรงสูง (Fy = 345 MPa)
- **EN_S235**: เหล็กยุโรป S235 (Fy = 235 MPa)
- **EN_S355**: เหล็กยุโรป S355 (Fy = 355 MPa)
- **EN_S460**: เหล็กยุโรป S460 (Fy = 460 MPa)

#### คอนกรีต (Concrete)
- **ACI_Normal_25MPa**: คอนกรีตปกติ fc' = 25 MPa
- **ACI_Normal_30MPa**: คอนกรีตปกติ fc' = 30 MPa
- **EN_C25/30**: คอนกรีตตามมาตรฐานยุโรป C25/30

#### อลูมิเนียม (Aluminum)
- **ASTM_6061_T6**: อลูมิเนียม 6061-T6
- **EN_6082_T6**: อลูมิเนียม 6082-T6 ตามมาตรฐานยุโรป

## 🚀 วิธีการใช้งาน

### 1. สร้าง Material จากฐานข้อมูล

#### ผ่าน GUI
```
เมนู StructureTools → Material (Enhanced)
หรือ กด Shift+M
```
- เลือกหมวดหมู่วัสดุ (Steel, Concrete, Aluminum)
- เลือกมาตรฐานที่ต้องการ
- ดูคุณสมบัติที่จะถูกตั้งค่า
- กด "Create Material" เพื่อสร้าง

#### ผ่าน Database Manager
```
เมนู StructureTools → Material Database Manager
หรือ กด Ctrl+Shift+M
```
- ค้นหาวัสดุตามชื่อหรือมาตรฐาน
- ดูคุณสมบัติและความเข้ากันได้กับ calc
- สร้าง Material แบบธรรมดาหรือ Enhanced

### 2. สร้าง Material ด้วย Python

#### วิธีง่าย - ใช้ฟังก์ชันสำเร็จรูป
```python
# สร้างเหล็ก ASTM A992
from freecad.StructureTools.utils import create_steel_a992
steel = create_steel_a992("MySteel")

# สร้างคอนกรีต 25 MPa
from freecad.StructureTools.utils import create_concrete_25mpa
concrete = create_concrete_25mpa("MyConcrete")

# สร้างเหล็ก A36
from freecad.StructureTools.utils import create_steel_a36
steel_a36 = create_steel_a36("Steel_A36")
```

#### วิธีละเอียด - เลือกมาตรฐานเอง
```python
from freecad.StructureTools.utils import create_material_from_database

# สร้างวัสดุจากมาตรฐานใดก็ได้
steel_s355 = create_material_from_database("EN_S355", "Steel_S355")
aluminum = create_material_from_database("ASTM_6061_T6", "Aluminum_6061")
concrete_30 = create_material_from_database("ACI_Normal_30MPa", "Concrete_30")
```

### 3. จัดการฐานข้อมูล

#### ดูมาตรฐานที่มี
```python
from freecad.StructureTools.utils import list_available_standards, list_standards_by_category

# ดูมาตรฐานทั้งหมด
all_standards = list_available_standards()
print(all_standards)

# ดูมาตรฐานตามหมวดหมู่
steel_standards = list_standards_by_category("Steel")
concrete_standards = list_standards_by_category("Concrete")
```

#### ค้นหาวัสดุ
```python
from freecad.StructureTools.utils import search_materials

# ค้นหาเหล็ก ASTM
astm_materials = search_materials("ASTM")
print(astm_materials)

# ค้นหา Grade 50
grade50_materials = search_materials("Grade 50")
print(grade50_materials)
```

#### ตรวจสอบความถูกต้อง
```python
from freecad.StructureTools.utils import validate_material_properties

# ตรวจสอบ material object
warnings = validate_material_properties(my_material)
if warnings:
    for warning in warnings:
        print(f"⚠️ {warning}")
else:
    print("✅ Material is valid")
```

### 4. การใช้งานกับ calc

#### การเชื่อมต่อโดยอัตโนมัติ
```python
# สร้าง beam และกำหนด material
beam.MaterialMember = my_steel_material  # ใช้ได้ทั้ง material เดิมและใหม่

# สร้าง plate และกำหนด material
plate.Material = my_concrete_material  # รองรับ plate elements

# calc จะดึงคุณสมบัติไปใช้โดยอัตโนมัติ
# ไม่ต้องตั้งค่าอะไรเพิ่มเติม
```

#### ดูคุณสมบัติที่ calc จะใช้
```python
from freecad.StructureTools.utils import get_calc_properties_from_database

# ดูคุณสมบัติในหน่วย m-kN
props_m_kn = get_calc_properties_from_database("ASTM_A992", "m", "kN")
print(f"E = {props_m_kn['E']} kN/m²")
print(f"G = {props_m_kn['G']} kN/m²")
print(f"density = {props_m_kn['density']} kN/m³")

# ดูคุณสมบัติในหน่วย mm-N
props_mm_n = get_calc_properties_from_database("ASTM_A992", "mm", "N")
print(f"E = {props_mm_n['E']} N/mm²")
```

## 🔧 การปรับแต่ง Material

### แก้ไขคุณสมบัติหลังสร้าง
```python
# หลังสร้าง material แล้ว สามารถแก้ไขได้
material = create_steel_a992("MySteel")

# แก้ไขคุณสมบัติ
material.YieldStrength = "400 MPa"  # เพิ่มกำลังการยืด
material.Density = "7800 kg/m^3"   # ปรับความหนาแน่น

# หรือเปลี่ยนมาตรฐาน (จะอัพเดตคุณสมบัติใหม่ทั้งหมด)
material.MaterialStandard = "EN_S355"
```

### สร้าง Material แบบกำหนดเอง
```python
# สร้าง Custom material โดยใช้เป็นพื้นฐาน
custom_steel = create_material_from_database("Custom", "MyCustomSteel")

# ตั้งค่าคุณสมบัติตามต้องการ
custom_steel.ModulusElasticity = "210000 MPa"
custom_steel.YieldStrength = "300 MPa"
custom_steel.UltimateStrength = "420 MPa"
custom_steel.PoissonRatio = 0.30
custom_steel.Density = "7850 kg/m^3"
custom_steel.GradeDesignation = "My Special Steel"
```

## 📊 การส่งออกและนำเข้าข้อมูล

### ส่งออกฐานข้อมูล
```python
from freecad.StructureTools.utils import export_material_database

# ส่งออกเป็นไฟล์ JSON
success = export_material_database("my_materials.json")
```

หรือผ่าน GUI: `Material Database Manager → Export Database`

### ดูโครงสร้างฐานข้อมูล
ฐานข้อมูลเก็บอยู่ที่ `freecad/StructureTools/data/MaterialStandards.py`:

```python
MATERIAL_STANDARDS = {
    "ASTM_A992": {
        "YieldStrength": "345 MPa",
        "UltimateStrength": "450 MPa", 
        "ModulusElasticity": "200000 MPa",
        "Density": "7850 kg/m^3",
        "PoissonRatio": 0.30,
        "ThermalExpansion": 12e-6,
        "GradeDesignation": "Grade 50",
        "TestingStandard": "ASTM A6"
    },
    # ... มาตรฐานอื่นๆ
}
```

## 🛠️ แก้ไขปัญหา

### ปัญหาที่พบบ่อย

#### 1. ไม่พบฐานข้อมูลมาตรฐาน
```
Error: Material standards database is not available
```

**วิธีแก้**: ตรวจสอบว่าไฟล์ `MaterialStandards.py` อยู่ในโฟลเดอร์ `data/`

#### 2. Material ไม่ทำงานกับ calc
```
Warning: Material lacks calc integration method
```

**วิธีแก้**: สร้าง material ใหม่ด้วยคำสั่งที่ปรับปรุงแล้ว หรือ:
```python
from freecad.StructureTools.utils import update_material_from_database
update_material_from_database(old_material, "ASTM_A992")
```

#### 3. ค่า Poisson ratio ไม่ถูกต้อง
```
Error: Invalid Poisson ratio 0.800. Must be between 0.0 and 0.5
```

**วิธีแก้**: ระบบจะแก้ไขเป็น 0.3 โดยอัตโนมัติ หรือตั้งค่าใหม่:
```python
material.PoissonRatio = 0.30
```

### การตรวจสอบการทำงาน

#### ตรวจสอบว่า material ใช้งานกับ calc ได้
```python
# วิธีที่ 1: ตรวจสอบว่ามีเมธอด get_calc_properties
if hasattr(material.Proxy, 'get_calc_properties'):
    print("✅ Material ใช้งานกับ calc ได้")
    props = material.Proxy.get_calc_properties(material)
    print(f"E = {props['E']} kN/m²")
else:
    print("❌ Material ไม่รองรับ calc")

# วิธีที่ 2: ใช้ฟังก์ชันตรวจสอบ
from freecad.StructureTools.commands.CreateMaterial import validate_material_for_calc
is_valid = validate_material_for_calc(material)
```

## 🎉 สรุป

ระบบ Material ที่ปรับปรุงใหม่นี้จะช่วยให้:

1. **สร้าง Material ได้ง่ายขึ้น** - เลือกจากมาตรฐานที่มีอยู่แล้ว
2. **ความแม่นยำสูงขึ้น** - ใช้ค่ามาตรฐานที่ถูกต้องตาม ASTM, EN, ACI
3. **ใช้งานกับ calc ได้ทันที** - ไม่ต้องตั้งค่าเพิ่มเติม
4. **จัดการง่าย** - มี GUI และ Python API ครบครัน
5. **ขยายได้** - สามารถเพิ่มมาตรฐานใหม่ได้

ระบบนี้รองรับทั้ง Material เดิมและ StructuralMaterial ใหม่ และทำงานร่วมกับ calc ได้อย่างสมบูรณ์แบบ!