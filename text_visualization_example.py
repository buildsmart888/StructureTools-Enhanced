#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example of text-based reaction visualization output
"""

def show_sample_output():
    """Show a sample of what the text-based visualization looks like."""
    
    sample_output = """
================================================================================
REACTION FORCES AND MOMENTS TEXT-BASED VISUALIZATION
================================================================================
Load Combination: 100_DL
--------------------------------------------------------------------------------

Node N1 at (0.00, 0.00, 0.00):
  Supports: DX, DY, DZ, RX, RY, RZ
    FX: ←←←←←←←←←← (15.25 kN)
    FY: ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ (42.80 kN)
    FZ: ↗↗↗↗↗ (8.75 kN)
    MX: ↻ →↓←↑→↓←↑→↓←↑ (12.40 kN·m)
    MY: ↺ →↑←↓→↑←↓ (9.15 kN·m)
    MZ: ↻ →↓←↑→↓←↑→↓←↑→↓←↑→↓←↑ (18.30 kN·m)
    Resultant Force: ↗↗↗↗↗↗↗↗↗↗↗↗↗↗↗↗↗↗↗↗↗↗↗↗↗↗↗↗↗↗ (46.20 kN)
    Resultant Moment: ↻ →↓←↑→↓←↑→↓←↑→↓←↑→↓←↑→↓←↑ (22.10 kN·m)

Node N2 at (5.00, 0.00, 0.00):
  Supports: DY, DZ
    FY: ↓↓↓↓↓↓↓↓↓ (18.50 kN)
    FZ: ↙↙↙↙↙↙ (12.30 kN)
    MX: ↺ →↑←↓→↑←↓→↑←↓ (8.75 kN·m)
    Resultant Force: ↙↙↙↙↙↙↙↙↙↙↙↙ (22.10 kN)
    Resultant Moment: ↺ →↑←↓→↑←↓ (8.75 kN·m)

--------------------------------------------------------------------------------
END OF TEXT-BASED VISUALIZATION
================================================================================
"""
    
    print("Sample Text-Based Reaction Visualization Output:")
    print("=" * 50)
    print(sample_output)
    print("=" * 50)
    print("💡 This is an example of how the text-based visualization would appear in the FreeCAD console.")
    print("💡 Each arrow represents the direction and relative magnitude of the reaction force/moment.")
    print("💡 The text in parentheses shows the actual magnitude with units.")

if __name__ == "__main__":
    show_sample_output()