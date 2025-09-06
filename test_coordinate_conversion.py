#!/usr/bin/env python3
"""
Test: Pynite to FreeCAD Coordinate System Conversion
===================================================

This test shows how coordinates are converted between Pynite and FreeCAD:

Pynite coordinate system:
- X: Horizontal (left-right)  
- Y: Vertical (up-down)
- Z: Depth (in-out of screen)

FreeCAD coordinate system:  
- X: Horizontal (left-right)
- Y: Depth (in-out of screen)
- Z: Vertical (up-down)

Conversion: FreeCAD.X = Pynite.X, FreeCAD.Y = Pynite.Z, FreeCAD.Z = Pynite.Y
"""

def test_coordinate_conversion():
    """Test coordinate conversion from Pynite to FreeCAD"""
    
    print("COORDINATE SYSTEM CONVERSION TEST")
    print("="*50)
    
    # Your actual node data from Pynite (in meters)
    pynite_nodes = [
        {"id": "Node 0", "pynite": (0.000, 0.000, 0.000)},
        {"id": "Node 2", "pynite": (3.000, 0.000, 0.000)},  
        {"id": "Node 4", "pynite": (3.000, 0.000, 3.000)},
        {"id": "Node 6", "pynite": (0.000, 0.000, 3.000)},
        {"id": "Node 12", "pynite": (6.000, 0.000, 0.000)},
        {"id": "Node 14", "pynite": (6.000, 0.000, 3.000)},
    ]
    
    print("Coordinate System Mapping:")
    print("Pynite -> FreeCAD")
    print("X (horizontal) -> X (horizontal)")  
    print("Y (vertical) -> Z (vertical)")
    print("Z (depth) -> Y (depth)")
    print("-"*50)
    
    for node in pynite_nodes:
        node_id = node["id"]
        pynite_coords = node["pynite"]
        
        # Extract Pynite coordinates
        pynite_x, pynite_y, pynite_z = pynite_coords
        
        # Convert to mm  
        pynite_x_mm = pynite_x * 1000
        pynite_y_mm = pynite_y * 1000
        pynite_z_mm = pynite_z * 1000
        
        # Convert to FreeCAD coordinate system
        freecad_x = pynite_x_mm  # X remains same
        freecad_y = pynite_z_mm  # Y becomes Pynite's Z (depth)
        freecad_z = pynite_y_mm  # Z becomes Pynite's Y (vertical)
        
        freecad_coords = (freecad_x, freecad_y, freecad_z)
        display_coords = (pynite_x_mm, pynite_y_mm, pynite_z_mm)
        
        print(f"\n{node_id}:")
        print(f"  Pynite (m):     ({pynite_x:.3f}, {pynite_y:.3f}, {pynite_z:.3f})")
        print(f"  Pynite (mm):    ({pynite_x_mm:.0f}, {pynite_y_mm:.0f}, {pynite_z_mm:.0f})")
        print(f"  FreeCAD (mm):   ({freecad_x:.0f}, {freecad_y:.0f}, {freecad_z:.0f})")
        print(f"  Label shows:    ({pynite_x_mm:.0f}, {pynite_y_mm:.0f}, {pynite_z_mm:.0f}) mm")
    
    print("\n" + "="*50)
    print("KEY POINTS:")
    print("1. Label positioned at FreeCAD coordinates")
    print("2. Label text shows original Pynite coordinates") 
    print("3. Y and Z are swapped between systems")
    print("4. All coordinates converted to mm")
    
    print("\n" + "="*50)
    print("EXAMPLE:")
    print("Node 4 at Pynite (3.0, 0.0, 3.0) meters:")
    print("- Positioned in FreeCAD at: (3000, 3000, 0) mm")
    print("- Label displays: '(3000, 0, 3000) mm' (original Pynite)")
    print("- This ensures labels show the coordinates engineers expect")

if __name__ == "__main__":
    test_coordinate_conversion()