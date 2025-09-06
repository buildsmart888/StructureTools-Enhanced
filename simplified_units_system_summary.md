# Simplified Units System - แก้ไขปัญหา GlobalUnitsSystem

## ปัญหาที่เกิดขึ้น

### ❌ ปัญหาจาก GlobalUnitsSystem ที่ซับซ้อน:
```
20:41:33  Invalid unit system: SI (kN, kN·m)
20:42:12  AttributeError: module 'App' has no attribute 'Console'  
20:43:17  Could not cache FE model: 'FeaturePython' object has no attribute '_cached_fe_model'
```

### 🔍 สาเหตุ:
1. **GlobalUnitsSystem ซับซ้อนเกินไป** - มีการจัดการ unit หลายระดับที่ทับซ้อนกัน
2. **Units Manager ขัดแย้งกัน** - ระบบ global units ไปชนกับ local force/length units  
3. **Console API ไม่สอดคล้องกัน** - `App.Console` ไม่มีใน scope บางที่
4. **ความซับซ้อนที่ไม่จำเป็น** - ผู้ใช้สับสนว่าต้องตั้งหน่วยที่ไหน

## การแก้ไข - ทำให้เรียบง่าย

### ✅ 1. ลบ GlobalUnitsSystem ที่ซับซ้อน

**เดิม (ซับซ้อน)**:
```python
# Global Units System (New Enhanced System)
_addProp("App::PropertyEnumeration", "GlobalUnitsSystem", "Global Units", "global units system")
obj.GlobalUnitsSystem = ["SI (kN, kN·m)", "THAI (kgf, kgf·m)", "THAI_TF (tf, tf·m)", ...]
```

**ใหม่ (เรียบง่าย)**:
```python
# Simple Units System (แทน GlobalUnitsSystem ที่ซับซ้อน)
# ใช้แค่ ForceUnit และ LengthUnit ให้เพียงพอ
```

### ✅ 2. แก้ไข Console API Error

**เดิม**:
```python
App.Console.PrintWarning(f"Error: {e}\n")  # ❌ Error
```

**ใหม่**:
```python
_print_warning(f"Error: {e}\n")  # ✅ ใช้ helper function ที่มี fallback
```

### ✅ 3. ปิด Global Units Complex Processing

**เดิม**:
```python
# Set global units system
from .utils.units_manager import get_units_manager
units_manager = get_units_manager()
units_manager.set_unit_system_by_display_name(obj.GlobalUnitsSystem)  # ❌ ซับซ้อน
```

**ใหม่**:
```python
# Simple unit system logging (disable complex global units to avoid conflicts)
if hasattr(obj, 'ForceUnit') and hasattr(obj, 'LengthUnit'):
    force_unit = getattr(obj, 'ForceUnit', 'kN')
    length_unit = getattr(obj, 'LengthUnit', 'm')
    _print_message(f"Using units: Force={force_unit}, Length={length_unit}\n")  # ✅ เรียบง่าย
```

### ✅ 4. ปรับปรุง Diagram Unit Detection

**เดิม**:
```python
# ใช้ GlobalUnitsSystem ที่ซับซ้อน
if "THAI_TF" in unit_system or "tf" in unit_system.lower():
    obj.ForceUnit = "tf"
```

**ใหม่**:
```python
# ใช้ ForceUnit และ LengthUnit ตรงจาก Calc object
if hasattr(calc_obj, 'ForceUnit'):
    obj.ForceUnit = calc_obj.ForceUnit  # ✅ ง่ายและตรงไปตรงมา
    
obj.MomentUnit = f"{obj.ForceUnit}·{length_unit}"  # ✅ สร้างอัตโนมัติ
```

## ระบบใหม่ที่เรียบง่าย

### 🎯 **การใช้งานที่เรียบง่าย:**

1. **เลือก Calc object** → Properties Panel
2. **ForceUnit**: เลือก kN, N, kgf, หรือ tf
3. **LengthUnit**: เลือก m, mm, หรือ cm
4. **MomentUnit**: อัปเดตอัตโนมัติ (เช่น tf·m, kgf·m)
5. **Diagram**: sync หน่วยจาก Calc อัตโนมัติ

### 🔧 **Properties ที่เหลือ (จำเป็น)**:

```python
# หน่วยพื้นฐาน (เพียงพอสำหรับทุกการใช้งาน)
ForceUnit: ['kN', 'N', 'kgf', 'tf']     # เลือกหน่วยแรง  
LengthUnit: ['m', 'mm', 'cm']           # เลือกหน่วยความยาว
MomentUnit: "tf·m"                      # อัปเดตอัตโนมัติ
```

### ❌ **Properties ที่ลบออก (ซับซ้อนไม่จำเป็น)**:

```python
# ลบออกแล้ว - ทำให้เกิดปัญหาและความซับซ้อน
GlobalUnitsSystem: ["SI (kN, kN·m)", ...]  # ❌ ลบ
UseGlobalUnits: True                       # ❌ ลบ  
FormattedForces: [...]                     # ❌ ลบ
FormattedStresses: [...]                   # ❌ ลบ
FormattedMoments: [...]                    # ❌ ลบ
```

## ผลลัพธ์

### ✅ **ปัญหาที่แก้ไขแล้ว:**
- ❌ ~~Invalid unit system errors~~ → ✅ ใช้ ForceUnit/LengthUnit ง่ายๆ
- ❌ ~~Console API AttributeError~~ → ✅ ใช้ _print_warning helper
- ❌ ~~Complex unit system conflicts~~ → ✅ ระบบเรียบง่าย
- ❌ ~~User confusion about unit settings~~ → ✅ ตั้งหน่วยใน Calc properties เท่านั้น

### ✅ **ข้อดีของระบบใหม่:**
- 🎯 **เรียบง่าย**: เลือกหน่วยใน Calc object เท่านั้น
- 🔧 **ไม่มีขัดแย้ง**: ไม่มี global vs local unit conflicts  
- 🚀 **เสียรเสถียร**: ลด error และ complexity
- 💡 **ง่ายต่อการใช้**: ผู้ใช้เข้าใจได้ทันที
- 🛡️ **Backward Compatible**: ไฟล์เก่ายังใช้ได้

### 🎉 **สรุป:**
**GlobalUnitsSystem ไม่จำเป็นจริง!** ใช้แค่ **ForceUnit + LengthUnit** เพียงพอสำหรับทุกการใช้งาน และทำให้ระบบเสียรเสถียรกว่าเดิมมาก