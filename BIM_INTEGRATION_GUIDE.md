# คู่มือการใช้งาน BIM Integration สำหรับ StructureTools

## ภาพรวมการเชื่อมโยง BIM Workbench

ระบบ BIM Integration ของ StructureTools ช่วยให้คุณสามารถ:

1. **นำเข้า BIM objects** เป็น structural elements
2. **ส่งออกผลการวิเคราะห์** กลับไปยัง BIM objects
3. **ซิงค์การเปลี่ยนแปลง** ระหว่าง BIM และ structural models
4. **สร้าง structural drawings** ใน TechDraw
5. **ส่งออกไปยัง FEM** สำหรับการวิเคราะห์ขั้นสูง

## 🚀 วิธีการใช้งาน

### ขั้นตอนที่ 1: เตรียม BIM Model

1. **เปิด BIM Workbench** ใน FreeCAD
2. **สร้าง structural elements** โดยใช้:
   - `Structure > Beam` สำหรับคานและโครงสร้าง
   - `Structure > Column` สำหรับเสา
   - `Structure > Slab` สำหรับพื้นและแผ่นคอนกรีต
   - หรือใช้ `Arch > Wall` สำหรับกำแพงโครงสร้าง

3. **กำหนด properties** ให้กับ BIM objects:
   ```
   - IfcType: IfcBeam, IfcColumn, IfcSlab
   - Material: Steel, Concrete, etc.
   - Width, Height, Length (สำหรับ sections)
   ```

### ขั้นตอนที่ 2: Import เป็น Structural Elements

1. **เลือก BIM objects** ที่ต้องการวิเคราะห์โครงสร้าง
2. **เปลี่ยนไปที่ StructureTools Workbench**
3. **คลิกไอคอน "Import from BIM"** หรือไปที่เมนู:
   ```
   BIM Integration → Import from BIM
   ```
4. **ตรวจสอบผลลัพธ์** ใน console:
   ```
   Successfully imported X structural elements
   Imported structural elements:
   - Beam_Column001
   - Beam_Beam001
   - Plate_Slab001
   ```

### ขั้นตอนที่ 3: กำหนด Material และ Section Properties

หลังจาก import แล้ว ระบบจะพยายามแปลง BIM materials โดยอัตโนมัติ แต่คุณสามารถปรับแต่งเพิ่มเติม:

```python
# ตัวอย่าง: ปรับแต่ง material ด้วย Python
steel_beam = App.ActiveDocument.getObject('Beam_Column001')
if steel_beam and steel_beam.MaterialMember:
    steel_beam.MaterialMember.MaterialStandard = "ASTM_A992"
    steel_beam.MaterialMember.YieldStrength = "345 MPa"
```

### ขั้นตอนที่ 4: วิเคราะห์โครงสร้าง

1. **สร้าง Calc object** เพื่อรวม structural elements
2. **กำหนด supports และ loads**
3. **รัน structural analysis**
4. **ตรวจสอบผลลัพธ์** ด้วย diagrams

### ขั้นตอนที่ 5: Export Results กลับไปยัง BIM

1. **หลังจากวิเคราะห์เสร็จแล้ว** คลิกไอคอน "Export Results to BIM"
2. **ระบบจะเพิ่ม analysis results** ไปยัง BIM objects โดยอัตโนมัติ:
   ```
   Properties ที่เพิ่ม:
   - StructuralResults: สรุปผลการวิเคราะห์
   - สีของ objects เปลี่ยนตาม capacity ratio:
     • เขียว: ปลอดภัย (ratio < 0.8)
     • เหลือง: ใช้งานสูง (0.8 < ratio < 1.0)
     • แดง: เกินขีดจำกัด (ratio > 1.0)
   ```

### ขั้นตอนที่ 6: การ Synchronization

เมื่อมีการเปลี่ยนแปลง geometry ใน BIM model:

1. **คลิก "Sync BIM Changes"** เพื่ออัพเดต structural model
2. **รันการวิเคราะห์ใหม่** หากจำเป็น
3. **ตรวจสอบสถานะ** ด้วย "BIM Integration Status"

## 🔧 คำสั่งใน BIM Integration Toolbar

### BIM_Import
- **ไอคอน**: Import symbol
- **ฟังก์ชัน**: นำเข้า BIM objects เป็น structural elements
- **วิธีใช้**: เลือก BIM objects แล้วคลิก
- **ผลลัพธ์**: สร้าง structural members, plates ตาม BIM geometry

### BIM_Export
- **ไอคอน**: Export symbol  
- **ฟังก์ชัน**: ส่งออกผลการวิเคราะห์กลับไปยัง BIM objects
- **วิธีใช้**: รันหลังจากทำ structural analysis เสร็จแล้ว
- **ผลลัพธ์**: เพิ่ม properties และ color coding ใน BIM objects

### BIM_Sync
- **ไอคอน**: Sync arrows
- **ฟังก์ชัน**: ซิงค์การเปลี่ยนแปลง geometry ระหว่าง BIM และ structural
- **วิธีใช้**: คลิกเมื่อมีการแก้ไข BIM geometry
- **ผลลัพธ์**: อัพเดต structural model ตาม BIM changes

### CreateStructuralDrawing
- **ไอคอน**: Drawing symbol
- **ฟังก์ชัน**: สร้าง structural drawings ใน TechDraw workbench
- **วิธีใช้**: คลิกหลังจากสร้าง structural model แล้ว
- **ผลลัพธ์**: สร้าง TechDraw pages พร้อม plan views และ diagrams

### ExportToFEM
- **ไอคอน**: FEM symbol
- **ฟังก์ชัน**: ส่งออก structural model ไปยัง FEM workbench
- **วิธีใช้**: คลิกเพื่อทำ advanced FEM analysis
- **ผลลัพธ์**: สร้าง FEM analysis container พร้อม mesh และ boundary conditions

## 📋 ตัวอย่างการใช้งานแบบครบวงจร

### สถานการณ์: วิเคราะห์โครงสร้างอาคาร 3 ชั้น

1. **สร้าง BIM model**:
   ```
   BIM Workbench:
   - สร้าง columns (6 ต้น)
   - สร้าง beams (12 เส้น)
   - สร้าง slabs (3 แผ่น)
   - กำหนด materials (Steel columns/beams, Concrete slabs)
   ```

2. **Import เป็น structural model**:
   ```
   StructureTools Workbench:
   - เลือก BIM objects ทั้งหมด
   - คลิก "Import from BIM" 
   - ได้ structural elements 21 ชิ้น
   ```

3. **วิเคราะห์โครงสร้าง**:
   ```
   - สร้าง supports ที่ฐานเสา
   - เพิ่ม dead loads และ live loads
   - สร้าง Calc object
   - รันการวิเคราะห์
   ```

4. **Export results**:
   ```
   - คลิก "Export Results to BIM"
   - BIM objects แสดงสีตาม capacity ratio
   - Properties แสดงผลการวิเคราะห์
   ```

5. **สร้าง drawings**:
   ```
   - คลิก "Create Structural Drawing"
   - ได้ TechDraw pages พร้อม:
     * Structural plan
     * Analysis results diagrams
     * Member schedule
   ```

## 🔍 การตรวจสอบและแก้ไขปัญหา

### ปัญหาที่พบบ่อย

#### 1. "No valid BIM objects found for import"
**สาเหตุ**: BIM objects ไม่มี properties ที่จำเป็น
**วิธีแก้**:
- ตรวจสอบว่า objects มี IfcType หรือ Role properties
- ตรวจสอบชื่อ objects ว่ามีคำว่า beam, column, slab หรือไม่

#### 2. "No linked BIM objects found"
**สาเหตุ**: ไม่ได้ import จาก BIM หรือ mapping หายไป
**วิธีแก้**:
- ตรวจสอบสถานะด้วย "BIM Integration Status"
- Import BIM objects ใหม่หากจำเป็น

#### 3. Materials ไม่ถูกต้อง
**สาเหตุ**: BIM materials ไม่ตรงกับ structural database
**วิธีแก้**:
- ปรับแต่ง MaterialStandard properties ด้วยตนเอง
- ใช้ Material Database Manager เพื่อเลือก materials ที่เหมาะสม

### การตรวจสอบสถานะการเชื่อมโยง

```python
# ตรวจสอบ BIM integration status
from freecad.StructureTools.integration.BIMIntegration import bim_integration

print(f"BIM to Structural links: {len(bim_integration.bim_to_structural_map)}")
print(f"Structural to BIM links: {len(bim_integration.structural_to_bim_map)}")

# แสดง linked objects
for bim_obj, struct_obj in bim_integration.bim_to_structural_map.items():
    print(f"{bim_obj.Label} -> {struct_obj.Label}")
```

## 🎯 เคล็ดลับการใช้งาน

### 1. การเตรียม BIM Model ที่ดี
- ตั้งชื่อ objects อย่างมีระบบ (เช่น B1, B2 สำหรับ beams)
- กำหนด IfcType ให้ถูกต้อง
- ใส่ material information ใน BIM objects

### 2. การจัดการ Large Models
- Import เป็นกลุ่มๆ แทนที่จะ import ทั้งหมดพร้อมกัน
- ใช้ layers หรือ groups ใน BIM เพื่อจัดระเบียบ
- ซิงค์เฉพาะส่วนที่เปลี่ยนแปลงเท่านั้น

### 3. การใช้งานร่วมกับ Workbenches อื่น
- ใช้ TechDraw สำหรับสร้าง construction documents
- ใช้ FEM workbench สำหรับ advanced analysis
- ใช้ Spreadsheet สำหรับ load calculations

## 📚 API Reference

### Python API สำหรับ Advanced Users

```python
# Import BIM integration
from freecad.StructureTools.integration.BIMIntegration import bim_integration

# Import specific objects
bim_objects = [App.ActiveDocument.getObject('Column001'), 
               App.ActiveDocument.getObject('Beam001')]
imported = bim_integration.import_from_bim(bim_objects)

# Export results manually
results = {
    'Beam_Column001': {
        'max_moment': 150.5,
        'max_deflection': 12.3, 
        'capacity_ratio': 0.85
    }
}
bim_integration.export_results_to_bim(imported, results)

# Sync geometry changes
bim_integration.sync_geometry_changes()
```

การใช้งาน BIM Integration จะช่วยให้การทำงานระหว่าง architectural design และ structural analysis เป็นไปอย่างราบรื่น โดยไม่ต้องสร้าง structural model จากศูนย์ และสามารถส่งผลการวิเคราะห์กลับไปปรับปรุง design ได้อย่างต่อเนื่อง!