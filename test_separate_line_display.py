#!/usr/bin/env python3
"""
Test: Each Reaction Component on Separate Line
==============================================

This test shows the new display format where each reaction component 
(Fx, Fy, Fz, Mx, My, Mz) is displayed on its own line for better readability.

Format:
(x, y, z) mm
Fx=value
Fy=value
Fz=value
Mx=value (if significant)
My=value (if significant)
Mz=value (if significant)
"""

def test_separate_line_display():
    """Test the new separate line display format"""
    
    print("NEW FORMAT: Each Reaction Component on Separate Line")
    print("="*60)
    
    # Sample node data with reactions
    nodes_data = [
        {
            "id": "Node 0", 
            "coords_mm": (0, 0, 0), 
            "reactions": {"Fx": 0.082, "Fy": 15.170, "Fz": 0.094, "Mx": 0.001, "My": 0.002, "Mz": 0.003}
        },
        {
            "id": "Node 2", 
            "coords_mm": (3000, 0, 0), 
            "reactions": {"Fx": -0.033, "Fy": 33.493, "Fz": 0.094, "Mx": 0.05, "My": -0.08, "Mz": 0.02}
        },
        {
            "id": "Node 4", 
            "coords_mm": (3000, 0, 3000), 
            "reactions": {"Fx": -0.018, "Fy": 42.950, "Fz": -0.096, "Mx": 0.12, "My": -0.15, "Mz": 0.18}
        },
        {
            "id": "Node 6", 
            "coords_mm": (0, 0, 3000), 
            "reactions": {"Fx": 0.107, "Fy": 14.382, "Fz": -0.115, "Mx": 0.001, "My": 0.002, "Mz": 0.003}
        }
    ]
    
    print("Label Display Format (Each Component on Separate Line):")
    print("-" * 60)
    
    for node in nodes_data:
        node_id = node["id"]
        coords_mm = node["coords_mm"]
        reactions = node["reactions"]
        
        print(f"\n{node_id}:")
        print("  Label Content:")
        
        # Position line
        x_mm, y_mm, z_mm = coords_mm
        print(f"    ({x_mm}, {y_mm}, {z_mm}) mm")
        
        # Force components (always shown if above threshold)
        min_threshold = 0.01
        if abs(reactions.get("Fx", 0)) > min_threshold:
            print(f"    Fx={reactions['Fx']:.2f}")
        if abs(reactions.get("Fy", 0)) > min_threshold:
            print(f"    Fy={reactions['Fy']:.2f}")
        if abs(reactions.get("Fz", 0)) > min_threshold:
            print(f"    Fz={reactions['Fz']:.2f}")
        
        # Moment components (only if significant > 0.05)
        moment_threshold = 0.05
        if abs(reactions.get("Mx", 0)) > moment_threshold:
            print(f"    Mx={reactions['Mx']:.2f}")
        if abs(reactions.get("My", 0)) > moment_threshold:
            print(f"    My={reactions['My']:.2f}")
        if abs(reactions.get("Mz", 0)) > moment_threshold:
            print(f"    Mz={reactions['Mz']:.2f}")
    
    print("\n" + "=" * 60)
    print("KEY IMPROVEMENTS:")
    print("+ Each reaction component on separate line")
    print("+ Better readability for multiple components")
    print("+ Consistent order: Fx, Fy, Fz, Mx, My, Mz")
    print("+ Position coordinates at the top")
    print("+ Only significant moments shown (>0.05 threshold)")
    print("+ Forces always shown if above minimum threshold (>0.01)")
    
    print("\n" + "=" * 60)
    print("EXAMPLE MULTI-LINE LABEL:")
    print("(3000, 0, 3000) mm")
    print("Fx=-0.02")
    print("Fy=42.95") 
    print("Fz=-0.10")
    print("Mx=0.12")
    print("My=-0.15")
    print("Mz=0.18")
    
    print("\n" + "=" * 60)
    print("COMPARISON:")
    print("OLD FORMAT (single/few lines):")
    print("  (3000, 0, 3000) mm")
    print("  Fx=-0.02, Fy=42.95, Fz=-0.10")
    print("  Mx=0.12, My=-0.15, Mz=0.18")
    print("")
    print("NEW FORMAT (each component separate):")
    print("  (3000, 0, 3000) mm")
    print("  Fx=-0.02")
    print("  Fy=42.95") 
    print("  Fz=-0.10")
    print("  Mx=0.12")
    print("  My=-0.15")
    print("  Mz=0.18")

if __name__ == "__main__":
    test_separate_line_display()