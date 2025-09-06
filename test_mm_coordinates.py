#!/usr/bin/env python3
"""
Test: Reaction Labels with MM Coordinates Display
================================================

This test shows how reaction labels will display with:
1. Correct positioning at node coordinates (in mm)
2. Position information shown in mm units
3. Proper unit conversion from meters to mm if needed

Based on your actual structure data:
"""

def test_mm_coordinate_display():
    """Test the new MM coordinate display format"""
    
    print("UPDATED: Reaction Labels with MM Coordinates")
    print("="*55)
    
    # Your actual node data - assuming coordinates are in meters, need conversion to mm
    nodes_data = [
        {"id": "Node 0", "coords_m": (0.000, 0.000, 0.000), "reactions": {"Fx": 0.082, "Fy": 15.170, "Fz": 0.094}},
        {"id": "Node 2", "coords_m": (3.000, 0.000, 0.000), "reactions": {"Fx": -0.033, "Fy": 33.493, "Fz": 0.094}},
        {"id": "Node 4", "coords_m": (3.000, 0.000, 3.000), "reactions": {"Fx": -0.018, "Fy": 42.950, "Fz": -0.096}},
        {"id": "Node 6", "coords_m": (0.000, 0.000, 3.000), "reactions": {"Fx": 0.107, "Fy": 14.382, "Fz": -0.115}},
        {"id": "Node 12", "coords_m": (6.000, 0.000, 0.000), "reactions": {"Fx": -0.091, "Fy": 32.865, "Fz": 0.071}},
        {"id": "Node 14", "coords_m": (6.000, 0.000, 3.000), "reactions": {"Fx": -0.048, "Fy": 54.151, "Fz": -0.048}},
    ]
    
    print("New Label Format (Position + Reactions):")
    print("-"*55)
    
    for node in nodes_data:
        node_id = node["id"]
        coords_m = node["coords_m"]
        reactions = node["reactions"]
        
        # Convert coordinates to mm
        x_mm = coords_m[0] * 1000
        y_mm = coords_m[1] * 1000  
        z_mm = coords_m[2] * 1000
        coords_mm = (x_mm, y_mm, z_mm)
        
        # Format reaction components (only significant values)
        reaction_components = []
        for component, value in reactions.items():
            if abs(value) > 0.01:  # MinReactionThreshold
                reaction_components.append(f"{component}={value:.2f}")
        
        # Create label format as it will appear in FreeCAD
        print(f"\n{node_id}:")
        print(f"  Original coords (m): {coords_m}")
        print(f"  Label position (mm): {coords_mm}")
        print(f"  Label display:")
        
        # Show label format - position first, then reactions
        position_text = f"({x_mm:.0f}, {y_mm:.0f}, {z_mm:.0f}) mm"
        reaction_text = ", ".join(reaction_components)
        
        print(f"    Line 1: {position_text}")
        print(f"    Line 2: {reaction_text}")
    
    print("\n" + "="*55)
    print("KEY IMPROVEMENTS:")
    print("+ Labels positioned exactly at node coordinates")
    print("+ Coordinates converted to mm for precision")
    print("+ Position shown in mm units: (0, 0, 0) mm")
    print("+ Standard FreeCAD coordinate system (X, Y, Z)")
    print("+ No coordinate swapping (Y/Z confusion)")
    print("+ Multi-line format: Position + Reactions")
    
    print("\n" + "="*55)
    print("COORDINATE CONVERSION:")
    print("- Input: Node coordinates in meters")
    print("- Auto-detect: Convert to mm if values < 100")
    print("- Output: FreeCAD.Vector in mm coordinates")
    print("- Display: Position shown as '(x, y, z) mm'")

if __name__ == "__main__":
    test_mm_coordinate_display()