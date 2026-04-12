# Steel Design Check & Traffic Light System (MVP Plan)

## 1. Objective
Implement a "Traffic Light" visual feedback system for steel members to indicate structural safety based on a simplified stress ratio check (Demand / Capacity).

## 2. Architecture Overview

### A. Core Logic (`analysis/steel_check.py`)
Create a new module `SteelCheck` responsible for calculating the utilization ratio of members.

*   **Inputs:**
    *   `Internal Forces`: P (Axial), M (Moment), V (Shear) - from `ResultManager`.
    *   `Section Properties`: Area, Sx (Section Modulus), I (Inertia) - from `Member` objects.
    *   `Material Properties`: Yield Strength (Fy), Elastic Modulus (E).
*   **Logic (Simplified MVP - AISC ASD Style):**
    *   **Axial Capacity (Pn):** `0.6 * Fy * Area` (Tensile) / `Buckling Formula` (Compressive - optional for Phase 1).
    *   **Bending Capacity (Mn):** `0.66 * Fy * Sx` (Compact sections).
    *   **Interaction Ratio (IR):** `(P_actual / P_n) + (M_actual / M_n)`
*   **Output:**
    *   `Utilization Ratio (float)`: e.g., 0.85
    *   `Status`: PASS / FAIL

### B. Data Storage
Store the results directly on the FreeCAD objects (Proxy properties) so they can be persisted and viewed later.
*   `obj.DesignRatio` (Float)
*   `obj.DesignStatus` (String: "Pass", "Fail", "Warning")

### C. Visualization (`view/design_view_provider.py`)
A new tool or toggle button "Show Design Status" that changes the color of members in the 3D view.
*   **Green:** Ratio < 0.80 (Safe)
*   **Yellow:** 0.80 <= Ratio <= 1.00 (Warning)
*   **Red:** Ratio > 1.00 (Fail)

## 3. Implementation Steps

### Phase 1: Property Enhancement
Ensure all Member objects correctly map their Material Yield Strength (Fy).
*   *Task:* Add `YieldStrength` to standard materials in `StructureTools`.
*   *Task:* Ensure `ModelBuilder` passes these properties correctly.

### Phase 2: Design Checker Module
Create `freecad/StructureTools/analysis/steel_design.py`.
*   *Task:* Implement `calculate_stress_ratio(member, forces)` function.
*   *Task:* Implement basic interaction formula.

### Phase 3: Integration with `calc.py`
Update the `execute` method in `calc.py` to run the design check **after** the structural analysis (Pynite) is finished.
*   *Task:* Iterate through all members, fetch Max Forces from `ResultManager`.
*   *Task:* Call `Design Checker`.
*   *Task:* Store `Ratio` back into the objects.

### Phase 4: Visualization Command
Create a Gui Command `CommandShowDesign`.
*   *Task:* Iterate `ActiveDocument.Objects`.
*   *Task:* Read `DesignRatio`.
*   *Task:* Set `ViewObject.ShapeColor`.

## 4. Future Expansion
*   Implement full AISC 360-16 / Eurocode 3 compliance.
*   Add Buckling checks (Length factors K, L).
*   PDF Report generation of the failing members.
