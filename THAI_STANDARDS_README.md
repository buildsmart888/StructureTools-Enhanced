# Thai Ministry B.E. 2566 Standards Integration
# การผสานรวมมาตรฐานกฎกระทรวง พ.ศ. 2566

## Overview / ภาพรวม

This integration adds comprehensive support for Thai structural design standards according to **Ministry Regulation B.E. 2566** (กฎกระทรวงกำหนดหลักเกณฑ์และวิธีการในการออกแบบและก่อสร้างอาคาร พ.ศ. 2566) into the StructureTools FreeCAD workbench.

การผสานรวมนี้เพิ่มการรองรับมาตรฐานการออกแบบโครงสร้างไทยตาม **กฎกระทรวง พ.ศ. 2566** อย่างครบถ้วนในชุดเครื่องมือ StructureTools สำหรับ FreeCAD

## Features / คุณสมบัติ

### 🏗️ Materials Database / ฐานข้อมูลวัสดุ
- **Thai Concrete Standards**: Fc180, Fc210, Fc280, Fc350 (คอนกรีตมาตรฐานไทย)
- **Thai Steel Standards**: SR24, SD40, SD50 (เหล็กมาตรฐานไทย)
- **Bilingual Support**: English and Thai descriptions (รองรับสองภาษา)
- **ksc Units**: Traditional Thai engineering units (หน่วยวิศวกรรมไทยแบบดั้งเดิม)

### 📏 Units Converter / ตัวแปลงหน่วย
- **Pressure/Stress**: ksc ↔ MPa, kPa, Pa
- **Force**: tf (metric ton-force) ↔ kN, kgf ↔ N
- **Thai Traditional Units**: วา, ไร่, งาน, ตารางวา
- **Load Conversions**: ksc/m² ↔ kN/m², structural loads

### 🌪️ Load Generation / การสร้างภาระ
- **Thai Wind Loads**: Regional wind speeds, terrain factors (ภาระลมแบบไทย)
- **Thai Seismic Loads**: Zone factors for Thailand regions (ภาระแผ่นดินไหวแบบไทย)
- **Thai Live Loads**: Building occupancy types per Thai standards (ภาระจรตามมาตรฐานไทย)
- **Load Combinations**: LRFD and ASD per Ministry B.E. 2566 (การรวมภาระ)

### 🔧 Design Requirements / ข้อกำหนดการออกแบบ
- **Load Factors**: Thai-specific safety factors (ปัจจัยความปลอดภัย)
- **Resistance Factors**: Material strength reduction factors (ปัจจัยลดกำลัง)
- **Deflection Limits**: Thai building code limits (ขีดจำกัดการโก่ง)
- **Reinforcement Design**: Thai concrete design methods (การออกแบบเหล็กเสริม)

## File Structure / โครงสร้างไฟล์

```
freecad/StructureTools/
├── data/
│   └── MaterialDatabase.py          # Enhanced with Thai materials
├── utils/
│   └── thai_units.py               # Thai units converter
├── design/
│   └── thai_design_requirements.py # Thai design standards
├── commands/
│   └── LoadGenerator.py           # Enhanced with Thai load methods
└── test_thai_integration.py       # Integration tests
```

## Usage Examples / ตัวอย่างการใช้งาน

### 1. Material Selection / การเลือกวัสดุ

```python
from data.MaterialDatabase import MaterialDatabase

db = MaterialDatabase()

# Get Thai concrete
concrete = db.get_material('Concrete_Fc280_Thai')
print(f"fc' = {concrete['fc_ksc']} ksc = {concrete['fc_MPa']} MPa")
print(f"Description: {concrete['description_thai']}")

# Get Thai steel
steel = db.get_material('Steel_SD40_Thai')
print(f"fy = {steel['fy_ksc']} ksc = {steel['fy_MPa']} MPa")
```

### 2. Unit Conversions / การแปลงหน่วย

```python
from utils.thai_units import get_thai_converter

converter = get_thai_converter()

# Pressure conversion
fc_ksc = 280  # Fc280
fc_mpa = converter.ksc_to_mpa(fc_ksc)
print(f"{fc_ksc} ksc = {fc_mpa:.2f} MPa")

# Force conversion
load_tf = 10  # metric tons
load_kn = converter.tf_to_kn(load_tf)
print(f"{load_tf} tf = {load_kn:.2f} kN")

# Concrete strength with Thai grades
result = converter.concrete_strength_conversion(280, 'ksc')
print(f"Closest Thai grade: {result['closest_thai_grade']}")
```

### 3. Load Calculations / การคำนวณภาระ

```python
from commands.LoadGenerator import LoadGeneratorManager

manager = LoadGeneratorManager()

# Thai wind load
wind_result = manager.calculate_wind_load_thai(
    basic_wind_speed=35,      # m/s
    height=20,                # m
    terrain_category='urban', 
    structure_type='building',
    region='central'          # Bangkok region
)

print(f"Wind pressure: {wind_result['total_wind_pressure_ksc_m2']:.2f} ksc/m²")
print(f"Description: {wind_result['description_thai']}")

# Thai seismic load
seismic_result = manager.calculate_seismic_load_thai(
    zone_factor='low',        # Central Thailand
    soil_type='C',           # Medium stiff soil
    structure_type='concrete_frame',
    height=20,               # m
    weight=5000              # kN
)

print(f"Base shear: {seismic_result['design_base_shear_tf']:.2f} tf")

# Thai live load
live_result = manager.calculate_live_load_thai(
    occupancy_type='office',
    area=100,                # m²
    location='general'
)

print(f"Live load: {live_result['live_load_ksc_m2']:.2f} ksc/m²")
```

### 4. Design Calculations / การคำนวณการออกแบบ

```python
from design.thai_design_requirements import get_thai_design_instance

design = get_thai_design_instance()

# Concrete design strength
concrete_result = design.get_concrete_design_strength(280, 'ksc')
print(f"Design strength: {concrete_result['design_strength_ksc']:.0f} ksc")
print(f"Elastic modulus: {concrete_result['elastic_modulus_ksc']:.0f} ksc")

# Load combinations
combinations = design.get_load_combinations()
basic_lrfd = combinations['LRFD']['basic']
print(f"Basic combination: {basic_lrfd['formula']}")
print(f"Description: {basic_lrfd['description_thai']}")

# Reinforcement calculation
rebar_result = design.calculate_reinforcement_requirements(
    moment=150,      # kN.m
    fc_prime=280,    # ksc
    fy=4000,         # ksc (SD40)
    b=300,           # mm
    d=450            # mm
)

print(f"Required steel: {rebar_result['As_required_mm2']:.0f} mm²")
print(f"Suggested: {rebar_result['num_bars_DB16']} bars DB16")
```

## Thai Standards Coverage / ครอบคลุมมาตรฐานไทย

### Materials / วัสดุ
- ✅ **TIS 20-2543**: Steel bars grade SR24 (เหล็กเส้นกลม SR24)
- ✅ **TIS 24-2548**: Deformed steel bars SD40, SD50 (เหล็กข้ออ้อย SD40, SD50)
- ✅ **Concrete Grades**: Fc180, Fc210, Fc280, Fc350 (คอนกรีตเกรดต่างๆ)
- ✅ **Thai Formulas**: Ec = 15000√fc' (ksc), Ec = 4700√fc' (MPa)

### Loads / ภาระ
- ✅ **Wind Loads**: Regional wind speeds for Thai provinces (ภาระลมตามภูมิภาค)
- ✅ **Seismic Loads**: Thailand seismic zones and soil types (ภาระแผ่นดินไหว)
- ✅ **Live Loads**: Thai building occupancy requirements (ภาระจรตามการใช้งาน)
- ✅ **Load Factors**: 1.2D + 1.6L (LRFD), D + L (ASD)

### Design / การออกแบบ
- ✅ **Resistance Factors**: φc = 0.85, φs = 0.90 (ปัจจัยลดกำลัง)
- ✅ **Deflection Limits**: L/360 (live), L/240 (total) (ขีดจำกัดการโก่ง)
- ✅ **Reinforcement**: ρmin, ρmax per Thai standards (อัตราเหล็กเสริม)

## Regional Data / ข้อมูลภูมิภาค

### Seismic Zones / เขตแผ่นดินไหว
- **Very Low (0.15g)**: Bangkok, Central Plains (กรุงเทพฯ, ภาคกลาง)
- **Low (0.25g)**: Eastern, Western regions (ภาคตะวันออก, ตะวันตก)
- **Moderate (0.35g)**: Lower Northern region (ภาคเหนือตอนล่าง)
- **High (0.50g)**: Upper Northern, Myanmar border (ภาคเหนือตอนบน, แดนพม่า)

### Wind Speeds / ความเร็วลม
- **Central**: 35 m/s (Bangkok metropolitan) (ภาคกลาง)
- **Northern**: 30 m/s (Chiang Mai, Chiang Rai) (ภาคเหนือ)
- **Northeastern**: 32 m/s (Korat Plateau) (ภาคตะวันออกเหนือ)
- **Eastern**: 40 m/s (Coastal areas) (ภาคตะวันออก - ชายฝั่ง)
- **Southern**: 45 m/s (High wind coastal) (ภาคใต้ - ชายฝั่งลมแรง)

## Testing / การทดสอบ

Run the integration tests to verify Thai standards implementation:

```bash
cd StructureTools
python test_thai_integration.py
```

The test suite covers:
- ✅ Material database completeness (ความครบถ้วนของฐานข้อมูลวัสดุ)
- ✅ Unit conversion accuracy (ความถูกต้องของการแปลงหน่วย)
- ✅ Design calculation validation (การตรวจสอบการคำนวณการออกแบบ)
- ✅ Integration workflow scenarios (สถานการณ์การทำงานร่วมกัน)

## Standards Compliance / การปฏิบัติตามมาตรฐาน

This implementation follows:
- **กฎกระทรวง พ.ศ. 2566**: Thai Ministry Building Code
- **TIS Standards**: Thai Industrial Standards for materials
- **ACI 318**: Referenced for concrete design methods
- **AISC**: Referenced for steel design methods
- **ASCE 7**: Referenced for load calculation methods

## Future Enhancements / การพัฒนาในอนาคต

### Phase 2 Planned Features:
- 🔄 **Advanced Seismic Analysis**: Response spectrum analysis (การวิเคราะห์แผ่นดินไหวขั้นสูง)
- 🔄 **Wind Tunnel Integration**: CFD wind analysis (การวิเคราะห์ลมด้วย CFD)
- 🔄 **Thai Code Verification**: Automated code checking (การตรวจสอบมาตรฐานอัตโนมัติ)
- 🔄 **BIM Integration**: Thai standard templates (การผสานรวม BIM)

## Support / การสนับสนุน

For issues related to Thai standards integration:

1. **Material Issues**: Check MaterialDatabase.py for Thai materials
2. **Unit Conversion**: Use thai_units.py converter utilities  
3. **Design Standards**: Reference thai_design_requirements.py
4. **Load Calculations**: Use enhanced LoadGenerator methods

## License / ใบอนุญาต

This Thai standards integration is part of the StructureTools project and follows the same license terms.

การผสานรวมมาตรฐานไทยนี้เป็นส่วนหนึ่งของโครงการ StructureTools และใช้เงื่อนไขใบอนุญาตเดียวกัน

---

**Developed with support from Thai structural engineering community**
**พัฒนาด้วยการสนับสนุนจากชุมชนวิศวกรรมโครงสร้างไทย**
