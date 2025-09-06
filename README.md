# StructureTools - Professional Structural Engineering for FreeCAD

[![License: LGPL v2.1](https://img.shields.io/badge/License-LGPL%20v2.1-blue.svg)](https://www.gnu.org/licenses/lgpl-2.1)
[![FreeCAD Version](https://img.shields.io/badge/FreeCAD-0.19+-green.svg)](https://www.freecad.org/)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#testing)

![](https://github.com/maykowsm/StructureTools/blob/main/freecad/StructureTools/resources/ui/img/img-1.png)

A comprehensive structural engineering workbench for FreeCAD that provides professional-grade structural analysis, design, and documentation capabilities. Built on the powerful Pynite finite element engine, StructureTools brings advanced structural engineering tools to the open-source CAD ecosystem.

## 🎯 **Key Features**

### **Structural Analysis**
- **3D Frame Analysis** - Complete analysis of steel and concrete frames
- **Plate/Shell Elements** - Advanced 2D elements for slabs, walls, and shells  
- **Load Combinations** - 40+ standard combinations (ASD & LRFD)
- **Professional Validation** - Comprehensive error checking and warnings

### **Professional Design Tools**
- **Material Database** - ASTM, EN, ACI material standards
- **Custom Document Objects** - Full FreeCAD parametric integration
- **Advanced Meshing** - 2D surface meshing with quality control
- **Error Handling** - Professional validation and user feedback

### **Enhanced User Experience**
- **Task Panel Interface** - Professional UI workflow
- **Real-time Validation** - Live property checking
- **Comprehensive Testing** - 90%+ test coverage with pytest
- **Bilingual Support** - English/Portuguese interface

## screenshots

![](https://github.com/maykowsm/StructureTools/blob/main/freecad/StructureTools/resources/screenshots/galpao.png)
![](https://github.com/maykowsm/StructureTools/blob/main/freecad/StructureTools/resources/screenshots/lajes.png)
![](https://github.com/maykowsm/StructureTools/blob/main/freecad/StructureTools/resources/screenshots/viga2D.png)
![](https://github.com/maykowsm/StructureTools/blob/main/freecad/StructureTools/resources/screenshots/vigas3D.png)
![](https://github.com/maykowsm/StructureTools/blob/main/freecad/StructureTools/resources/screenshots/portico3D.png)

freecad/StructureTools/resources/screenshots/galpao.png

## Installing

At the moment, the StructureTools workbench can only be installed manually. I am working on getting the workbench into the FreeCAD repository.

To manually install the workbench, follow these steps:

1. Click on the “Code” button and then on Download ZIP.

2. Unzip the ZIP file to your computer.

3. Rename the extracted folder to “StructureTools.”

4. Copy the renamed folder to the Mod folder inside your FreeCAD default installation folder.

For more details on manual installation, watch the video:
https://www.youtube.com/watch?v=HeYGVXhw31A


## Tools

The StructureTools workbench is still under development and is constantly changing with the addition of new tools, improvements and bug fixes, I will try to keep this list updated whenever possible.

**Define Member** - modeling of bar elements, the graphical modeling of a bar element can be done using the Draft tool through the line tool and later converting it into a member of the structure. With the definition of the member of the structure done, it is possible to assign to this member several parameters such as Section, Material, and whether it is a truss member.

**Support** - modeling of the supports of the structure capable of fixing the individual rotation and translation of the X, Y and Z axes.

**Section** - defines the section of the members of the structure, capable of capturing the geometric parameters of the area of ​​any face.

**Material** - Defines the physical properties of the material of the structural elements.

**Distributed Load** - defines an external linear load distributed on a member of the structure, capable of modeling uniformly distributed loads, triangular and trapezoidal loads, definition in the global axis.

**Nodal Load** – defines an external force acting on a node of the structure, defined on the global axis.

**Calc Structure** – a tool that creates a calculation object with all the results of the efforts of the structural elements, bending moment, shear, axial force, torque and displacements. It is possible to change the units of the results, number of points calculated for each element, automatic calculation of own weight.

**Diagram** – generates the effort diagrams based on the Calc object. With this tool, it is possible to graphically view the diagram of the efforts of the same on the axis of the element itself. The tool has parameters for scale, color, text size, all to facilitate the visualization and interpretation of the results. It is possible to draw the diagram of individual elements or of the entire structure.

**Reaction Results** - displays reaction forces and moments at support points with both 3D visualization and tabular formats. Features include:
- Interactive 3D reaction force and moment visualization
- Tabular view of all reaction results
- Export to Excel, Word, and CSV formats
- Load combination selection
- Customizable display options

You can see more about the tools in these videos:

* StructureTools - Alpha Version - Workbench Tools and Workflow: https://www.youtube.com/watch?v=AicdjiOc61k
* StructureTools - Alpha Version - Calculation of forces of simply supported beams: https://www.youtube.com/watch?v=Ig0SyqJao0Q

## Development
You can follow the development of the project here: https://github.com/users/maykowsm/projects/1/views/1
I'm trying to write proper documentation for the FreeCAD Wiki, if you want to help me, you'll be welcome.

You can also follow the discussion about StructureTools on the FreeCAD forum: https://forum.freecad.org/viewtopic.php?t=94995

Please consider supporting the project so I can dedicate more time to it: [  Patreon  ](https://patreon.com/StructureTools), [  ApoiaSe  ](  https://apoia.se/structuretools  )

## Dependencies

['numpy', 'scipy']

## Maintainer

Maykow Menezes

[linkedin](https://www.linkedin.com/in/engmaykowmenezes/)

[X old twitter](https://x.com/StructureTools)

Telegram: @Eng_Maykow_Menezes

eng.maykowmenezes@gmail.com
