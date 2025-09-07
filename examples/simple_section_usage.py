# -*- coding: utf-8 -*-
"""
Simple Section Usage Examples
ตัวอย่างการใช้งาน Section แบบง่าย
"""

import FreeCAD

def example_1_basic_section_creation():
    """
    ตัวอย่างที่ 1: การสร้าง Section พื้นฐาน
    Example 1: Basic Section Creation
    """
    print("=== Example 1: Basic Section Creation ===")
    
    doc = FreeCAD.ActiveDocument
    if not doc:
        doc = FreeCAD.newDocument("SectionExample")
    
    # วิธีที่ 1: ใช้ Core Architecture (แนะนำ)
    from freecad.StructureTools.core import get_section_properties, detect_section_from_name
    
    # ตรวจหา section อัตโนมัติ
    section_name = detect_section_from_name("W12X26_BEAM_A1")
    print(f"Detected section: {section_name}")  # จะได้ "W12x26"
    
    # ดึงคุณสมบัติจากฐานข้อมูล
    properties = get_section_properties(section_name)
    if properties:
        print("Section Properties from Database:")
        print(f"  Area: {properties['Area']:.0f} mm²")
        print(f"  Ix: {properties['Ix']:,.0f} mm⁴")
        print(f"  Iy: {properties['Iy']:,.0f} mm⁴")
        print(f"  Weight: {properties.get('Weight', 0):.1f} kg/m")
        print(f"  Type: {properties.get('Type', 'Unknown')}")
    
    return properties

def example_2_section_object_creation():
    """
    ตัวอย่างที่ 2: สร้าง Section Object ใน FreeCAD
    Example 2: Create Section Object in FreeCAD
    """
    print("\n=== Example 2: Section Object Creation ===")
    
    doc = FreeCAD.ActiveDocument
    if not doc:
        doc = FreeCAD.newDocument("SectionExample")
    
    from freecad.StructureTools.section import Section, ViewProviderSection
    from freecad.StructureTools.core import get_section_properties
    
    # สร้าง section object
    section_obj = doc.addObject("Part::FeaturePython", "W12x26_Section")
    Section(section_obj, [])
    ViewProviderSection(section_obj.ViewObject)
    
    # กำหนดคุณสมบัติจากฐานข้อมูล
    properties = get_section_properties("W12x26")
    if properties:
        section_obj.SectionName = "W12x26"
        section_obj.Area = properties['Area']
        section_obj.Iy = properties['Ix']  # Major axis
        section_obj.Iz = properties['Iy']  # Minor axis
        section_obj.J = properties.get('J', 100000)
        
        print(f"Created section object: {section_obj.Label}")
        print(f"  Area: {section_obj.Area:.0f} mm²")
        print(f"  Iy: {section_obj.Iy:,.0f} mm⁴")
    
    doc.recompute()
    return section_obj

def example_3_custom_section():
    """
    ตัวอย่างที่ 3: การสร้าง Custom Section
    Example 3: Create Custom Section
    """
    print("\n=== Example 3: Custom Section Creation ===")
    
    doc = FreeCAD.ActiveDocument
    if not doc:
        doc = FreeCAD.newDocument("SectionExample")
    
    from freecad.StructureTools.section import Section, ViewProviderSection
    
    # สร้าง custom section
    custom_section = doc.addObject("Part::FeaturePython", "CustomSection_200x100x10")
    Section(custom_section, [])
    ViewProviderSection(custom_section.ViewObject)
    
    # กำหนดคุณสมบัติเอง
    custom_section.SectionName = "Custom_RectHSS_200x100x10"
    custom_section.Area = 2840.0      # mm²
    custom_section.Iy = 13200000.0    # mm⁴ (major axis)
    custom_section.Iz = 5800000.0     # mm⁴ (minor axis) 
    custom_section.J = 18000000.0     # mm⁴ (torsion)
    custom_section.Sy = 132000.0      # mm³ (section modulus)
    custom_section.Sz = 116000.0      # mm³
    
    print(f"Created custom section: {custom_section.Label}")
    print(f"  Dimensions: 200x100x10 mm HSS")
    print(f"  Area: {custom_section.Area:.0f} mm²")
    print(f"  Iy: {custom_section.Iy:,.0f} mm⁴")
    
    doc.recompute()
    return custom_section

def example_4_section_with_member():
    """
    ตัวอย่างที่ 4: เชื่อมต่อ Section กับ Member
    Example 4: Connect Section with Member
    """
    print("\n=== Example 4: Section with Member ===")
    
    doc = FreeCAD.ActiveDocument
    if not doc:
        doc = FreeCAD.newDocument("SectionExample")
    
    import Draft
    from freecad.StructureTools.section import Section, ViewProviderSection
    from freecad.StructureTools.member import Member, ViewProviderMember
    from freecad.StructureTools.core import get_section_properties
    
    # สร้างเส้นสำหรับ member
    start_point = FreeCAD.Vector(0, 0, 0)
    end_point = FreeCAD.Vector(5000, 0, 0)  # 5 meter beam
    beam_line = Draft.makeLine(start_point, end_point)
    beam_line.Label = "BeamLine_5m"
    
    # สร้าง section object
    section = doc.addObject("Part::FeaturePython", "IPE200_Section")
    Section(section, [])
    ViewProviderSection(section.ViewObject)
    
    # ใช้ IPE200 properties
    properties = get_section_properties("IPE200")
    if properties:
        section.SectionName = "IPE200"
        section.Area = properties['Area']
        section.Iy = properties['Ix']
        section.Iz = properties['Iy']
        section.J = properties.get('J', 50000)
    
    # สร้าง member object
    member = doc.addObject("Part::FeaturePython", "Beam_IPE200_5m")
    Member(member, [beam_line])
    ViewProviderMember(member.ViewObject)
    
    # เชื่อมต่อ section กับ member
    member.Section = section  # เชื่อมโยง section object
    member.Label = f"Beam_{section.SectionName}_5m"
    
    # กำหนดคุณสมบัติใน member ด้วย (สำหรับ calc)
    member.SectionName = section.SectionName
    member.Area = section.Area
    member.Iy = section.Iy
    member.Iz = section.Iz
    
    print(f"Created member: {member.Label}")
    print(f"  Connected to section: {section.Label}")
    print(f"  Length: 5000 mm")
    print(f"  Section: {member.SectionName}")
    print(f"  Area: {member.Area:.0f} mm²")
    
    # ซ่อน construction line
    beam_line.ViewObject.Visibility = False
    
    doc.recompute()
    return member, section

def example_5_batch_sections():
    """
    ตัวอย่างที่ 5: สร้าง Sections แบบ Batch
    Example 5: Batch Section Creation
    """
    print("\n=== Example 5: Batch Sections ===")
    
    doc = FreeCAD.ActiveDocument
    if not doc:
        doc = FreeCAD.newDocument("SectionExample")
    
    from freecad.StructureTools.section import Section, ViewProviderSection
    from freecad.StructureTools.core import get_section_properties
    
    # รายการ sections ที่ต้องการ
    section_list = ["W12x26", "W14x22", "IPE200", "HEB160", "HSS6x4x1/4"]
    created_sections = []
    
    print("Creating multiple sections:")
    
    for i, section_name in enumerate(section_list):
        # ดึงคุณสมบัติจากฐานข้อมูล
        properties = get_section_properties(section_name)
        
        if properties:
            # สร้าง section object
            section_obj = doc.addObject("Part::FeaturePython", f"Section_{section_name.replace('/', '_')}_{i+1}")
            Section(section_obj, [])
            ViewProviderSection(section_obj.ViewObject)
            
            # กำหนดคุณสมบัติ
            section_obj.SectionName = section_name
            section_obj.Area = properties['Area']
            section_obj.Iy = properties['Ix']
            section_obj.Iz = properties['Iy']
            section_obj.J = properties.get('J', 100000)
            
            created_sections.append(section_obj)
            
            print(f"  {i+1}. {section_name}: Area={properties['Area']:.0f} mm², Type={properties.get('Type', 'Unknown')}")
        else:
            print(f"  {i+1}. {section_name}: Not found in database")
    
    doc.recompute()
    print(f"Successfully created {len(created_sections)} sections")
    
    return created_sections

def example_6_section_validation():
    """
    ตัวอย่างที่ 6: การตรวจสอบ Section ตาม Design Code
    Example 6: Section Validation with Design Codes
    """
    print("\n=== Example 6: Section Validation ===")
    
    from freecad.StructureTools.core import get_section_properties
    from freecad.StructureTools.data.SectionValidator import (
        validate_section_for_design_code,
        calculate_section_classification
    )
    
    # ทดสอบกับ W12x26
    properties = get_section_properties("W12x26")
    
    if properties:
        print(f"Validating {properties.get('SectionName', 'W12x26')}:")
        
        # ตรวจสอบตาม AISC 360
        is_valid, errors, warnings = validate_section_for_design_code(
            properties, design_code="AISC_360"
        )
        
        print(f"  AISC 360 Validation: {'PASS' if is_valid else 'FAIL'}")
        
        if errors:
            print("  Errors:")
            for error in errors:
                print(f"    - {error}")
        
        if warnings:
            print("  Warnings:")
            for warning in warnings:
                print(f"    - {warning}")
        
        # จำแนกประเภทหน้าตัด
        classification = calculate_section_classification(properties, "A992")
        print(f"  Section Classification: {classification}")
        
        # แสดงข้อมูลสำคัญ
        print(f"  Steel Grade: A992")
        print(f"  Yield Strength: 345 MPa (assumed)")
        print(f"  Section Type: {properties.get('Type', 'Unknown')}")
    else:
        print("Section properties not found")

def run_all_examples():
    """รันตัวอย่างทั้งหมด"""
    print("🏗️  StructureTools Section Usage Examples")
    print("=" * 50)
    
    # รันตัวอย่างทีละตัว
    try:
        example_1_basic_section_creation()
        example_2_section_object_creation()
        example_3_custom_section()
        example_4_section_with_member()
        example_5_batch_sections()
        example_6_section_validation()
        
        print("\n" + "=" * 50)
        print("✅ All examples completed successfully!")
        print("\nNext Steps:")
        print("1. เพิ่ม Materials และ Supports")
        print("2. เพิ่ม Loads (Distributed, Nodal)")
        print("3. สร้าง Calc object สำหรับวิเคราะห์")
        print("4. รัน Analysis และดูผลลัพธ์")
        
        if FreeCAD.ActiveDocument:
            print(f"\nDocument: {FreeCAD.ActiveDocument.Label}")
            print(f"Objects created: {len(FreeCAD.ActiveDocument.Objects)}")
    
    except Exception as e:
        print(f"❌ Error in examples: {str(e)}")
        import traceback
        traceback.print_exc()

# Main execution
if __name__ == "__main__":
    run_all_examples()