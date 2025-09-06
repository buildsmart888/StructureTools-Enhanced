# Calc Units Enhancement Summary

## 1. แก้ไข NameError: 'FreeCAD' 

**ปัญหา**: `cannot access free variable 'FreeCAD' where it is not associated with a value in enclosing scope`

**การแก้ไข**:
```python
# เพิ่ม import ใน scope ที่มีปัญหา
obj.NameMembers = model.members.keys()
# Import FreeCAD in case it's not available in this scope
try:
    import FreeCAD
except ImportError:
    import App as FreeCAD
obj.Nodes = [FreeCAD.Vector(node[0], node[2], node[1]) for node in nodes_map]
```

**ผลลัพธ์**: ✅ แก้ไข NameError เรียบร้อยแล้ว

## 2. เพิ่ม Default Properties และหน่วย kgf, tf

### 2.1 ปรับปรุง Unit Properties:

**เดิม**:
```python
_addProp("App::PropertyString", "LengthUnit", "Calc", "set the length unit for calculation", default='m')
_addProp("App::PropertyString", "ForceUnit", "Calc", "set the length unit for calculation", default='kN')
```

**ใหม่**:
```python
# Unit properties with proper defaults and enumeration
_addProp("App::PropertyEnumeration", "LengthUnit", "Calc", "set the length unit for calculation")
if hasattr(obj, 'addProperty'):
    obj.LengthUnit = ['m', 'mm', 'cm']
    obj.LengthUnit = 'm'  # default

_addProp("App::PropertyEnumeration", "ForceUnit", "Calc", "set the force unit for calculation") 
if hasattr(obj, 'addProperty'):
    obj.ForceUnit = ['kN', 'N', 'kgf', 'tf']  # เพิ่ม kgf และ tf
    obj.ForceUnit = 'kN'  # default

# Add moment unit property (derived from force and length)
_addProp("App::PropertyString", "MomentUnit", "Calc", "moment unit (derived from force and length)", default='kN·m')
```

### 2.2 เพิ่ม Auto-Update MomentUnit:

```python
def onChanged(self, obj, Parameter):
    """Handle property changes to update dependent properties"""
    if Parameter == "ForceUnit":
        # Auto-update MomentUnit based on ForceUnit and LengthUnit
        self.updateMomentUnit(obj)
    elif Parameter == "LengthUnit":
        # Auto-update MomentUnit based on ForceUnit and LengthUnit
        self.updateMomentUnit(obj)

def updateMomentUnit(self, obj):
    """Update MomentUnit based on current ForceUnit and LengthUnit"""
    force_unit = getattr(obj, 'ForceUnit', 'kN')
    length_unit = getattr(obj, 'LengthUnit', 'm')
    
    # Create moment unit string
    moment_unit = f"{force_unit}·{length_unit}"
    
    # Update MomentUnit property
    if hasattr(obj, 'MomentUnit'):
        obj.MomentUnit = moment_unit
```

### 2.3 ขยาย GlobalUnitsSystem:

**เดิม**:
```python
obj.GlobalUnitsSystem = ["SI (kN, kN·m)", "THAI (kgf, kgf·m)", "THAI_TF (tf, tf·m)"]
```

**ใหม่**:
```python
obj.GlobalUnitsSystem = [
    "SI (kN, kN·m)",        # SI system  
    "THAI (kgf, kgf·m)",    # Thai system with kgf
    "THAI_TF (tf, tf·m)",   # Thai system with tf
    "METRIC_N (N, N·m)",    # Metric with Newtons
    "METRIC_KGF (kgf, kgf·cm)",  # Traditional metric
    "MIXED (tf, tf·cm)"     # Mixed units
]
```

## 3. คุณสมบัติใหม่

### ✅ Unit Properties:
- **LengthUnit**: `['m', 'mm', 'cm']` - เลือกหน่วยความยาว
- **ForceUnit**: `['kN', 'N', 'kgf', 'tf']` - เลือกหน่วยแรง (เพิ่ม kgf และ tf)
- **MomentUnit**: อัปเดตอัตโนมัติตาม ForceUnit × LengthUnit

### ✅ Auto-Update System:
- เปลี่ยน ForceUnit → MomentUnit อัปเดตทันที
- เปลี่ยน LengthUnit → MomentUnit อัปเดตทันที
- ตัวอย่าง: ForceUnit = "tf", LengthUnit = "m" → MomentUnit = "tf·m"

### ✅ Extended GlobalUnitsSystem:
- รองรับระบบหน่วยเพิ่มเติม 6 แบบ
- รวม kgf และ tf ตามที่ร้องขอ
- รองรับ traditional metric (kgf·cm) และ mixed units

## 4. วิธีใช้งาน

### การตั้งค่าหน่วยแบบใหม่:

1. **เลือก Calc object** ใน Model Tree
2. **Properties Panel** จะแสดง:
   - **LengthUnit**: เลือก m, mm, หรือ cm
   - **ForceUnit**: เลือก kN, N, kgf, หรือ tf
   - **MomentUnit**: อัปเดตอัตโนมัติ (เช่น tf·m)
3. **GlobalUnitsSystem**: เลือกระบบหน่วยที่ต้องการ

### ตัวอย่างการใช้งาน:

- **กรณีไทย tf**: ForceUnit = "tf" → MomentUnit = "tf·m" 
- **กรณีไทย kgf**: ForceUnit = "kgf" → MomentUnit = "kgf·m"
- **กรณี SI**: ForceUnit = "kN" → MomentUnit = "kN·m"

## 5. ผลลัพธ์

✅ **NameError แก้ไขแล้ว** - ไม่มี FreeCAD scope error อีก  
✅ **Default Properties** - มี LengthUnit และ ForceUnit enumeration  
✅ **เพิ่ม kgf และ tf** - รองรับหน่วยไทยครบถ้วน  
✅ **Auto-Update MomentUnit** - อัปเดตทันทีเมื่อเปลี่ยนหน่วย  
✅ **Extended Unit Systems** - 6 ระบบหน่วยให้เลือก  
✅ **Backward Compatibility** - ไฟล์เก่ายังทำงานได้  

ระบบตอนนี้รองรับหน่วยไทย (kgf, tf) ครบถ้วนและมีการจัดการหน่วยที่ดีขึ้น!