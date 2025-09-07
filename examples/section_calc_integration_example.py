# -*- coding: utf-8 -*-
"""
ตัวอย่างการใช้งาน Section + Section Manager + Calc Integration
Example: Complete workflow from section definition to structural analysis
"""

import FreeCAD
import FreeCADGui
import Draft
import Part

def create_simple_building_frame():
    """
    สร้างโครงสร้างอาคารง่าย ๆ และวิเคราะห์
    Create simple building frame and analyze it
    """
    
    print("=== StructureTools Integration Example ===")
    
    # สร้าง document ใหม่
    doc = FreeCAD.newDocument("StructureExample")
    
    # 1. สร้างเรขาคณิตพื้นฐาน (Basic Geometry)
    print("\n1. Creating basic geometry...")
    
    # สร้าง structural grid 3x2 bays, 4m x 6m each
    grid_points = []
    for x in [0, 4000, 8000, 12000]:  # mm
        for y in [0, 6000, 12000]:    # mm
            grid_points.append(FreeCAD.Vector(x, y, 0))
            grid_points.append(FreeCAD.Vector(x, y, 3500))  # 3.5m height
    
    # สร้าง beams (horizontal members)
    beam_lines = []
    for y in [0, 6000, 12000]:
        for z in [3500]:  # Second floor
            # Beams in X direction
            for x_start in [0, 4000, 8000]:
                start = FreeCAD.Vector(x_start, y, z)
                end = FreeCAD.Vector(x_start + 4000, y, z)
                line = Draft.makeLine(start, end)
                line.Label = f"Beam_X_{x_start//1000}_{y//1000}"
                beam_lines.append(line)
    
    # สร้าง columns (vertical members) 
    column_lines = []
    for x in [0, 4000, 8000, 12000]:
        for y in [0, 6000, 12000]:
            start = FreeCAD.Vector(x, y, 0)
            end = FreeCAD.Vector(x, y, 3500)
            line = Draft.makeLine(start, end)
            line.Label = f"Column_{x//1000}_{y//1000}"
            column_lines.append(line)
    
    doc.recompute()
    print(f"Created {len(beam_lines)} beams and {len(column_lines)} columns")
    
    # 2. ใช้ Section Manager สำหรับ section properties
    print("\n2. Setting up sections using Core Architecture...")
    
    from freecad.StructureTools.core import (
        get_section_manager,
        detect_section_from_name,
        get_section_properties,
        generate_section_geometry
    )
    
    # ตั้งค่า sections สำหรับ members ต่าง ๆ
    section_assignments = {
        'beams': 'W12x26',      # AISC Wide Flange
        'columns': 'W12x65'     # AISC Wide Flange  
    }
    
    manager = get_section_manager()
    print(f"Section Manager initialized. Database available: {manager.database_available}")
    
    # ดึง properties จากฐานข้อมูล
    beam_properties = get_section_properties(section_assignments['beams'])
    column_properties = get_section_properties(section_assignments['columns'])
    
    if beam_properties:
        print(f"Beam {section_assignments['beams']} properties:")
        print(f"  Area: {beam_properties['Area']:.0f} mm²")
        print(f"  Ix: {beam_properties['Ix']:,.0f} mm⁴")
        print(f"  Iy: {beam_properties['Iy']:,.0f} mm⁴")
    
    if column_properties:
        print(f"Column {section_assignments['columns']} properties:")
        print(f"  Area: {column_properties['Area']:.0f} mm²") 
        print(f"  Ix: {column_properties['Ix']:,.0f} mm⁴")
    
    # 3. สร้าง Section Objects
    print("\n3. Creating section objects...")
    
    from freecad.StructureTools.section import Section, ViewProviderSection
    
    # Beam section
    beam_section_obj = doc.addObject("Part::FeaturePython", "BeamSection_W12x26")
    Section(beam_section_obj, [])
    ViewProviderSection(beam_section_obj.ViewObject)
    
    if beam_properties:
        beam_section_obj.SectionName = section_assignments['beams']
        beam_section_obj.Area = beam_properties['Area']
        beam_section_obj.Iy = beam_properties['Ix']  # Major axis
        beam_section_obj.Iz = beam_properties['Iy']  # Minor axis
        beam_section_obj.J = beam_properties.get('J', 100000)  # Torsion constant
        beam_section_obj.Sy = beam_properties.get('Sx', 500000)  # Section modulus
    
    # Column section
    column_section_obj = doc.addObject("Part::FeaturePython", "ColumnSection_W12x65")
    Section(column_section_obj, [])
    ViewProviderSection(column_section_obj.ViewObject)
    
    if column_properties:
        column_section_obj.SectionName = section_assignments['columns']
        column_section_obj.Area = column_properties['Area']
        column_section_obj.Iy = column_properties['Ix']
        column_section_obj.Iz = column_properties['Iy'] 
        column_section_obj.J = column_properties.get('J', 200000)
        column_section_obj.Sy = column_properties.get('Sx', 800000)
    
    print(f"Created section objects: {beam_section_obj.Label}, {column_section_obj.Label}")
    
    # 4. สร้าง Member Objects
    print("\n4. Creating structural members...")
    
    from freecad.StructureTools.member import Member, ViewProviderMember
    
    # Create beam members
    beam_members = []
    for i, beam_line in enumerate(beam_lines):
        member = doc.addObject("Part::FeaturePython", f"Beam_{i+1:02d}")
        Member(member, [beam_line])
        ViewProviderMember(member.ViewObject)
        
        # เชื่อมต่อกับ section
        member.Section = beam_section_obj
        member.Label = f"Beam_{section_assignments['beams']}_{i+1:02d}"
        
        # กำหนดคุณสมบัติโดยตรง (สำหรับ calc)
        member.SectionName = section_assignments['beams']
        if beam_properties:
            member.Area = beam_properties['Area']
            member.Iy = beam_properties['Ix']
            member.Iz = beam_properties['Iy']
        
        beam_members.append(member)
    
    # Create column members  
    column_members = []
    for i, column_line in enumerate(column_lines):
        member = doc.addObject("Part::FeaturePython", f"Column_{i+1:02d}")
        Member(member, [column_line])
        ViewProviderMember(member.ViewObject)
        
        # เชื่อมต่อกับ section
        member.Section = column_section_obj
        member.Label = f"Column_{section_assignments['columns']}_{i+1:02d}"
        
        # กำหนดคุณสมบัติโดยตรง
        member.SectionName = section_assignments['columns']
        if column_properties:
            member.Area = column_properties['Area']
            member.Iy = column_properties['Ix']  
            member.Iz = column_properties['Iy']
            
        column_members.append(member)
    
    all_members = beam_members + column_members
    print(f"Created {len(beam_members)} beam members and {len(column_members)} column members")
    
    # 5. สร้าง Materials
    print("\n5. Creating materials...")
    
    from freecad.StructureTools.material import Material, ViewProviderMaterial
    
    steel_material = doc.addObject("Part::FeaturePython", "Steel_A992")
    Material(steel_material, [])
    ViewProviderMaterial(steel_material.ViewObject)
    
    # Steel A992 properties
    steel_material.MaterialName = "Steel_A992"
    steel_material.ElasticModulus = "200000 MPa"  # 200 GPa
    steel_material.ShearModulus = "77000 MPa"     # 77 GPa  
    steel_material.Density = "7850 kg/m^3"       # Steel density
    steel_material.PoissonRatio = 0.3
    steel_material.YieldStrength = "345 MPa"     # Fy for A992
    
    # กำหนด material ให้กับทุก members
    for member in all_members:
        member.Material = steel_material
    
    print("Steel A992 material assigned to all members")
    
    # 6. เพิ่ม Supports
    print("\n6. Adding boundary conditions...")
    
    from freecad.StructureTools.suport import Suport, ViewProviderSuport
    
    # Fixed supports ที่ฐานของ columns
    supports = []
    for i, column in enumerate(column_members):
        # หาจุดฐานของ column (z=0)
        if hasattr(column, 'Geometry') and column.Geometry:
            geom = column.Geometry[0]
            if hasattr(geom, 'Shape') and hasattr(geom.Shape, 'Vertexes'):
                # หาจุดที่ z=0 
                base_vertex = None
                for vertex in geom.Shape.Vertexes:
                    if abs(vertex.Point.z) < 10:  # ใกล้ z=0
                        base_vertex = vertex
                        break
                
                if base_vertex:
                    support = doc.addObject("Part::FeaturePython", f"Support_Column_{i+1:02d}")
                    Suport(support, [(geom, [f"Vertex{geom.Shape.Vertexes.index(base_vertex)+1}"])])
                    ViewProviderSuport(support.ViewObject)
                    
                    # Fixed support (ยึดทุกทิศทาง)
                    support.SupportDX = True
                    support.SupportDY = True  
                    support.SupportDZ = True
                    support.SupportRX = True
                    support.SupportRY = True
                    support.SupportRZ = True
                    support.Label = f"Fixed_Support_{i+1:02d}"
                    
                    supports.append(support)
    
    print(f"Created {len(supports)} fixed supports at column bases")
    
    # 7. เพิ่ม Loads
    print("\n7. Adding loads...")
    
    from freecad.StructureTools.load_distributed import LoadDistributed, ViewProviderLoadDistributed
    from freecad.StructureTools.load_nodal import LoadNodal, ViewProviderLoadNodal
    
    # Distributed loads บน beams (dead + live load)
    distributed_loads = []
    for i, beam in enumerate(beam_members):
        if hasattr(beam, 'Geometry') and beam.Geometry:
            # Dead load: 2.5 kN/m
            dead_load = doc.addObject("Part::FeaturePython", f"DeadLoad_Beam_{i+1:02d}")
            LoadDistributed(dead_load, beam.Geometry)
            ViewProviderLoadDistributed(dead_load.ViewObject)
            
            dead_load.Load = "2.5 kN/m"
            dead_load.Direction = "Z-"  # ลงเต็มแรงโน้มถ่วง
            dead_load.LoadType = "DL"
            dead_load.Label = f"DL_2.5kN/m_Beam_{i+1:02d}"
            distributed_loads.append(dead_load)
            
            # Live load: 4.0 kN/m
            live_load = doc.addObject("Part::FeaturePython", f"LiveLoad_Beam_{i+1:02d}")
            LoadDistributed(live_load, beam.Geometry)
            ViewProviderLoadDistributed(live_load.ViewObject)
            
            live_load.Load = "4.0 kN/m"
            live_load.Direction = "Z-"
            live_load.LoadType = "LL"
            live_load.Label = f"LL_4.0kN/m_Beam_{i+1:02d}"
            distributed_loads.append(live_load)
    
    print(f"Created {len(distributed_loads)} distributed loads on beams")
    
    # 8. สร้าง Calc Object และวิเคราะห์
    print("\n8. Creating analysis object and running calculation...")
    
    from freecad.StructureTools.calc import Calc, ViewProviderCalc
    
    # รวบรวมทุก objects สำหรับ analysis
    analysis_objects = all_members + [steel_material] + supports + distributed_loads
    
    # สร้าง calc object
    calc = doc.addObject("Part::FeaturePython", "BuildingAnalysis")
    Calc(calc, analysis_objects)
    ViewProviderCalc(calc.ViewObject)
    
    # ตั้งค่า analysis parameters
    calc.LoadCombinations = [
        "101_DL+LL",           # Service load combination  
        "1001_1.2DL+1.6LL",    # LRFD ultimate load combination
        "1002_1.2DL+0.5LL"     # LRFD with reduced live load
    ]
    
    calc.Label = "3x2_Frame_Analysis"
    print(f"Analysis object created: {calc.Label}")
    print(f"Load combinations: {calc.LoadCombinations}")
    
    # แสดงสรุปโมเดล
    print(f"\nModel Summary:")
    print(f"  Members: {len(all_members)} ({len(beam_members)} beams, {len(column_members)} columns)")
    print(f"  Materials: 1 (Steel A992)")
    print(f"  Supports: {len(supports)} fixed supports") 
    print(f"  Loads: {len(distributed_loads)} distributed loads")
    print(f"  Load Combinations: {len(calc.LoadCombinations)}")
    
    # แสดงรายละเอียด sections
    print(f"\nSection Properties Summary:")
    if beam_properties:
        print(f"  Beams ({section_assignments['beams']}):")
        print(f"    Area: {beam_properties['Area']:.0f} mm²")
        print(f"    Ix: {beam_properties['Ix']:,.0f} mm⁴")
        print(f"    Weight: {beam_properties.get('Weight', 0):.1f} kg/m")
    
    if column_properties:
        print(f"  Columns ({section_assignments['columns']}):")
        print(f"    Area: {column_properties['Area']:.0f} mm²") 
        print(f"    Ix: {column_properties['Ix']:,.0f} mm⁴")
        print(f"    Weight: {column_properties.get('Weight', 0):.1f} kg/m")
    
    doc.recompute()
    
    # 9. จัดการหน้าจอและ view
    print("\n9. Setting up 3D view...")
    
    if hasattr(FreeCADGui, 'ActiveDocument'):
        FreeCADGui.ActiveDocument.ActiveView.fitAll()
        FreeCADGui.ActiveDocument.ActiveView.viewAxonometric()
        
        # ซ่อน construction lines
        for line in beam_lines + column_lines:
            if hasattr(line, 'ViewObject'):
                line.ViewObject.Visibility = False
    
    print("\n=== Example Completed Successfully! ===")
    print(f"Document: {doc.Label}")
    print("Ready for analysis and results visualization")
    print("\nNext steps:")
    print("1. Select the Calc object")  
    print("2. Run analysis: calc.solve() in Python console")
    print("3. Generate result diagrams using Diagram command")
    
    return doc, calc, all_members

# Main execution
if __name__ == "__main__":
    if FreeCAD.ActiveDocument:
        reply = FreeCADGui.Windows.questionDialog(
            "Create Example",
            "This will create a new document with example structure.\nContinue?"
        )
        if reply == 16384:  # Yes clicked
            create_simple_building_frame()
    else:
        create_simple_building_frame()