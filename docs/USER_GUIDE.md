# StructureTools User Guide

StructureTools is a workbench for FreeCAD that implements a set of tools for modeling and analyzing structural stresses, similar to software like SAP2000, ETABS, SkyCiv, or Cype3D. 

It integrates the [Pynite](https://github.com/JWock82/PyNite) 3D finite element analysis engine directly into FreeCAD's parametric modeling environment.

## Getting Started

1. **Open FreeCAD** and switch to the **StructureTools Workbench** from the Workbench dropdown menu.
2. The StructureTools toolbar will appear, presenting icons for modeling, loading, analysis, and design.

## 1. Modeling Geometry

StructureTools uses a node-and-member approach:
- **Structural Node**: The fundamental building block. Represents a joint or support in 3D space.
- **Structural Beam**: A 1D frame element connecting two nodes. Can be assigned cross-sections and materials.
- **Structural Column**: Functionally identical to a beam but oriented vertically in the UI.
- **Structural Plate**: A 2D rectangular shell element for modeling floors, walls, and slabs.

### Creating Members
1. Click the **Create Node** button to place nodes at key coordinates.
2. Select two nodes in the 3D view, then click the **Create Beam** or **Create Column** button to connect them.

## 2. Assigning Properties

### Materials
Materials define the stiffness and strength of elements.
- Select members and click the **Material Selection Panel**.
- Choose from standard steel (A36, A992, S355) or concrete (4000 psi) grades.

### Sections
- Click the **Beam Properties Panel**.
- Choose a section from the built-in database (e.g., AISC W-shapes, HSS). 
- *Note: Version 0.5.0 includes 67 AISC W-shapes (W44 through W4).*

### Supports
- Select a node on the ground.
- Open the **Node Properties Panel** and check the corresponding degrees of freedom (Dx, Dy, Dz, Rx, Ry, Rz) to create pinned, fixed, or roller supports.

## 3. Applying Loads

Loads can be applied to nodes, members, or areas.

- **Point Loads**: Select a node, click the Load Panel, and define Fx, Fy, or Fz force.
- **Distributed Loads**: Select a beam, click the Load Panel, and define a uniform load (w).
- **Area Loads**: Select a plate or a perimeter of beams, click the **Area Load Panel**. Define the pressure magnitude and the load will automatically distribute to supporting members according to yield line theory.

## 4. Running the Analysis

Once the model is fully connected, supported, and loaded:
1. Click the **Run Analysis** button.
2. The model will be exported to the Pynite engine, solved, and results will be read back.
3. *Note: For models with significant axial loads undergoing lateral displacement, you can enable **P-Delta / Second-Order Analysis** to capture geometric nonlinear effects.*

## 5. Viewing Results

### Diagrams
Use the result visualization toggles to display:
- Axial Force Diagrams
- Shear Force Diagrams (V2, V3)
- Bending Moment Diagrams (M2, M3)
- Deflected Shape

### Reactions and Member Forces
- Click the **Reaction Table** to see tabulated support reactions.
- Click the **Member Force Panel** for detailed tables of internal forces along member lengths.

## 6. Design Checks (Code Validation)

StructureTools includes built-in design validation:

### Steel Design
- **AISC 360**: Automatic cross-section classification (Compact, Non-compact, Slender), flexural, shear, compression, and combined loading checks.
- **Eurocode 3 (EN 1993-1-1)**: Classification (Table 5.2), bending, shear, flexural buckling, and LTB checks.

### Concrete Design
- **ACI 318-19**: P-M Interaction Diagram generation for rectangular columns under combined axial/flexural loads.

### Connections and Foundations
- Basic AISC bolted/welded connection checks (`design/connections.py`).
- Basic ACI 318 spread footing design (bearing, shear, flexure) (`design/foundations.py`).

## 7. Interoperability

You can import external models using the SAP2000 feature:
- Click **Import SAP2000** and select a `$2k` or exported `.xlsx` file to bring in geometry, sections, materials, and loads.
