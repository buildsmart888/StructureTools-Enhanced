# Sign Convention Correction Summary

## ปัญหาที่พบ
ผู้ใช้รายงานว่าการแสดง diagram จากโค้ดต้นฉบับ ([GitHub source](https://github.com/maykowsm/StructureTools/blob/main/freecad/StructureTools/diagram.py)) ดูถูกต้องกว่าโค้ดที่เราแก้ไข โดยเฉพาะเรื่อง sign convention ที่เปลี่ยนจากค่าลบเป็นบวกไม่ถูกต้อง

## การวิเคราะห์โค้ดต้นฉบับ

### Original Sign Convention Logic:
```python
# จากโค้ดต้นฉบับ GitHub
def makeText(self, values, listMatrix, dist, fontHeight, precision):
    for i, value in enumerate(values):
        valueString = listMatrix[i] * -1  # ✓ CRITICAL: Sign flip
        string = f"{valueString:.{precision}e}"  # ✓ Scientific notation
```

### เหตุผลของ Sign Flip (* -1):
1. **PyNite Engine**: ใช้ internal sign convention 
2. **Structural Engineering**: ต้องการ standard sign convention
3. **การแปลง**: `* -1` แปลงจาก PyNite → Structural Engineering convention
4. **ความถูกต้อง**: นี่คือพฤติกรรมที่ถูกต้องตามโค้ดต้นฉบับ

## การแก้ไขที่ทำผิด

### ❌ สิ่งที่เราทำผิดในการแก้ไขครั้งแรก:
1. **เปลี่ยน Format**: จาก scientific notation เป็น decimal format
2. **รบกวน Sign Logic**: เพิ่ม `+` prefix ทำให้ sign display เปลี่ยน
3. **Consistent Positioning**: เพิ่ม logic ที่ทำให้ค่าแสดงผลเปลี่ยนไป

### 🔧 การแก้ไขที่ถูกต้อง:

#### 1. คืนค่า Scientific Notation (diagram_core.py):
```python
def get_label_positions(...):
    for i, value in enumerate(values_scaled):
        # IMPORTANT: Keep the original sign flip logic (* -1) 
        value_string = list_matrix_row[i] * -1
        
        # Use original scientific notation format
        string = f"{value_string:.{precision}e}"  # ✓ เหมือนต้นฉบับ
```

#### 2. ปรับ Unit Conversion (diagram.py):
```python
# Extract numeric value from scientific notation
value = float(label_text)  # ✓ Sign ถูกต้องแล้วจาก * -1 logic

# Convert without adding + prefix
return converted, f"{converted:.{obj.Precision}f} kgf·m"  # ✓ ไม่มี + prefix
```

#### 3. เก็บ Original Text Positioning:
```python
# Keep original positioning logic  
y = value + offset if value > 0 else value - offset  # ✓ เหมือนต้นฉบับ
```

## ความแตกต่างระหว่างก่อนและหลังการแก้ไข

### ก่อนแก้ไข (ผิด):
- ❌ Decimal format แทน scientific notation
- ❌ มี `+` prefix ทำให้ sign display เปลี่ยน
- ❌ Consistent positioning ทำให้ค่าเปลี่ยนไป

### หลังแก้ไข (ถูก):
- ✅ Scientific notation เหมือนต้นฉบับ
- ✅ Sign flip (* -1) เหมือนต้นฉบับ  
- ✅ Text positioning เหมือนต้นฉบับ
- ✅ Unit conversion ทำงานกับ sign ที่ถูกต้อง

## การทำงานที่ถูกต้อง

### Flow การทำงาน:
1. **PyNite Results**: `[10.5, -15.2, 8.7]` (kN⋅m)
2. **Sign Flip**: `[-10.5, 15.2, -8.7]` (structural convention)
3. **Scientific Format**: `["-1.05e+01", "1.52e+01", "-8.70e+00"]`
4. **Unit Conversion**: `["-1071.7 kgf·m", "1551.0 kgf·m", "-887.4 kgf·m"]`

### ผลลัพธ์:
- ✅ Sign convention ถูกต้องตาม structural engineering
- ✅ ค่าแสดงผลเหมือนโค้ดต้นฉบับ
- ✅ Unit conversion ทำงานได้โดยไม่รบกวน sign
- ✅ Compatible กับ original StructureTools

## สรุป
การแก้ไขนี้แก้ไขปัญหา sign convention ให้กลับไปตรงกับโค้ดต้นฉบับจาก GitHub พร้อมเก็บ feature unit conversion ที่เราเพิ่มเข้าไป ทำให้ได้ทั้งความถูกต้องและ functionality ใหม่