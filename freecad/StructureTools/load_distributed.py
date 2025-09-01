# Setup FreeCAD stubs for standalone operation
try:
    from .utils.freecad_stubs import setup_freecad_stubs, is_freecad_available
    if not is_freecad_available():
        setup_freecad_stubs()
except ImportError:
    pass

# Import FreeCAD modules (now available via stubs if needed)
try:
    import FreeCAD, App, FreeCADGui, Part
    FREECAD_AVAILABLE = True
except ImportError:
    FREECAD_AVAILABLE = False

import os

# Import GUI framework with fallbacks
try:
    from PySide import QtWidgets
except ImportError:
    try:
        from PySide2 import QtWidgets
    except ImportError:
        # Mock QtWidgets for standalone operation
        class QtWidgets:
            class QDialog:
                def __init__(self): pass

# Import Global Units System
try:
    from .utils.units_manager import (
        get_units_manager, format_force, format_stress, format_modulus
    )
    GLOBAL_UNITS_AVAILABLE = True
except ImportError:
    GLOBAL_UNITS_AVAILABLE = False
    get_units_manager = lambda: None
    format_force = lambda x: f"{x/1000:.2f} kN"
    format_stress = lambda x: f"{x/1e6:.1f} MPa"
    format_modulus = lambda x: f"{x/1e9:.0f} GPa"


# Import Thai units support
try:
    from .utils.universal_thai_units import enhance_with_thai_units, thai_load_units, get_universal_thai_units
    from .utils.thai_units import get_thai_converter
    THAI_UNITS_AVAILABLE = True
except ImportError:
    THAI_UNITS_AVAILABLE = False
    enhance_with_thai_units = lambda x, t: x
    thai_load_units = lambda f: f
    get_universal_thai_units = lambda: None
    get_thai_converter = lambda: None

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")

def show_error_message(msg, english_msg=None):
    # If both Thai and English messages are provided, show both
    if english_msg:
        full_msg = f"{msg}\n{english_msg}"
    else:
        full_msg = msg
        
    msg_box = QtWidgets.QMessageBox()
    msg_box.setIcon(QtWidgets.QMessageBox.Critical)
    msg_box.setWindowTitle("Error")
    msg_box.setText(full_msg)
    msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg_box.exec_()


class LoadDistributed:
    def __init__(self, obj, selection):
        obj.Proxy = self
        obj.addProperty("App::PropertyLinkSubList", "ObjectBase", "Base", "Object base")
        obj.addProperty("App::PropertyForce", "InitialLoading", "Distributed", "Initial loading (load per unit length)").InitialLoading = 10000000
        obj.addProperty("App::PropertyForce", "FinalLoading", "Distributed", "Final loading (load per unit length)").FinalLoading = 10000000
        obj.addProperty("App::PropertyFloat", "ScaleDraw", "Load", "Scale from drawing").ScaleDraw = 1

        # Add properties for start and end positions of distributed load
        obj.addProperty("App::PropertyLength", "StartPosition", "Distributed", "Start position of distributed load along member (0 = start, measured from member start)").StartPosition = 0.0
        obj.addProperty("App::PropertyLength", "EndPosition", "Distributed", "End position of distributed load along member (0 = use full member length to end)").EndPosition = 0.0

        # Add Thai units properties for distributed loads
        if THAI_UNITS_AVAILABLE:
            obj.addProperty("App::PropertyFloat", "InitialLoadingKgfM", "Thai Units", "Initial loading in kgf/m").InitialLoadingKgfM = 1000000  # N/m to kgf/m
            obj.addProperty("App::PropertyFloat", "FinalLoadingKgfM", "Thai Units", "Final loading in kgf/m").FinalLoadingKgfM = 1000000
            obj.addProperty("App::PropertyFloat", "InitialLoadingTfM", "Thai Units", "Initial loading in tf/m").InitialLoadingTfM = 1000  # N/m to tf/m
            obj.addProperty("App::PropertyFloat", "FinalLoadingTfM", "Thai Units", "Final loading in tf/m").FinalLoadingTfM = 1000
            obj.addProperty("App::PropertyBool", "UseThaiUnits", "Thai Units", "Use Thai units display").UseThaiUnits = False

        # Load Type Properties
        obj.addProperty("App::PropertyEnumeration", "LoadType", "Load", "Type of load")
        obj.LoadType = ['DL', 'LL', 'H', 'F', 'W', 'E']
        obj.LoadType = 'DL'

        obj.addProperty("App::PropertyEnumeration", "GlobalDirection","Load","Global direction load")
        obj.GlobalDirection = ['+X','-X', '+Y','-Y', '+Z','-Z']
        obj.GlobalDirection = '-Z'
        
        print(selection)
        obj.ObjectBase = (selection[0], selection[1])
    
    def getDistributedLoadInThaiUnits(self, obj):
        """Get distributed load values in Thai units."""
        if not THAI_UNITS_AVAILABLE:
            return None
        
        converter = get_thai_converter()
        initial_n_m = obj.InitialLoading.Value  # Force per length in N/m
        final_n_m = obj.FinalLoading.Value
        
        return enhance_with_thai_units({
            'initial_force_N_m': initial_n_m,
            'final_force_N_m': final_n_m,
            'initial_force_kN_m': initial_n_m / 1000,
            'final_force_kN_m': final_n_m / 1000,
            'load_type': obj.LoadType,
            'direction': obj.GlobalDirection,
            'is_uniform': abs(initial_n_m - final_n_m) < 0.001,
            'description_thai': f'ภาระกระจาย {obj.LoadType} ทิศทาง {obj.GlobalDirection}',
            'load_pattern': 'uniform' if abs(initial_n_m - final_n_m) < 0.001 else 'triangular'
        }, 'load')
    
    def updateThaiUnits(self, obj):
        """Update Thai units properties when main loads change."""
        if not THAI_UNITS_AVAILABLE or not hasattr(obj, 'InitialLoadingKgfM'):
            return
        
        converter = get_thai_converter()
        initial_n_m = obj.InitialLoading.Value
        final_n_m = obj.FinalLoading.Value
        
        # Convert to kgf/m and tf/m
        obj.InitialLoadingKgfM = converter.n_to_kgf(initial_n_m)  # N/m to kgf/m (same conversion factor)
        obj.FinalLoadingKgfM = converter.n_to_kgf(final_n_m)
        obj.InitialLoadingTfM = converter.kn_to_tf(initial_n_m / 1000)  # N/m to tf/m
        obj.FinalLoadingTfM = converter.kn_to_tf(final_n_m / 1000)
    
    # Desenha carregamento pontual
    def drawNodeLoad(self, obj, vertex):
        pass
    
    # Retorna o subelemento asociado
    def getSubelement(self, obj, nameSubElement):
        
        if 'Edge' in  nameSubElement:
            index = int(nameSubElement.split('Edge')[1]) - 1
            return obj.ObjectBase[0][0].Shape.Edges[index]
        else:
            index = int(nameSubElement.split('Vertex')[1]) - 1
            return obj.ObjectBase[0][0].Shape.Vertexes[index]

    # Desenha a forma da seta levando em conta a escala informada
    def makeArrow(self, obj, load):
        radiusCone = 5
        heightCone = 20
        heightCylinder = 30
        radiusCylinder = 2

        cone = Part.makeCone(0 ,radiusCone * obj.ScaleDraw * load/1000000, heightCone * obj.ScaleDraw * load/1000000)
        cylinder = Part.makeCylinder(radiusCylinder * obj.ScaleDraw * load/1000000, heightCylinder * obj.ScaleDraw * load/1000000)        
        cylinder.translate(FreeCAD.Vector(0,0, heightCone * obj.ScaleDraw * load/1000000))
        return Part.makeCompound([cone, cylinder])
    
    
    def execute(self, obj):
        # Safety check for ObjectBase
        if not hasattr(obj, 'ObjectBase') or not obj.ObjectBase or len(obj.ObjectBase) == 0:
            return
        if not obj.ObjectBase[0] or len(obj.ObjectBase[0]) < 2 or not obj.ObjectBase[0][1]:
            return
            
        subelement = self.getSubelement(obj, obj.ObjectBase[0][1][0])
        if 'Edge' in obj.ObjectBase[0][1][0]:
            k = 1000000
            nArrow = int(k * (subelement.Length**(1/1.8))/(obj.ScaleDraw * ((obj.InitialLoading + obj.FinalLoading) / 2))) #calcula o numero de setas com base na distancia do menbro, escala do desenho e media das forças de inicio e fim
            
            # Limit the number of arrows to prevent performance issues
            nArrow = min(nArrow, 50)

            FEend = obj.FinalLoading / obj.InitialLoading #fator de escala entre as forças 'end' e 'start'
            distEndStart = subelement.Length

            # Calculate start and end positions for load visualization
            start_pos = 0.0
            end_pos = subelement.Length
            
            # Check if start and end positions are specified
            if hasattr(obj, 'StartPosition') and hasattr(obj, 'EndPosition'):
                # Convert to internal units (mm) for visualization
                start_pos = float(obj.StartPosition.getValueAs('mm'))
                end_pos = float(obj.EndPosition.getValueAs('mm'))
                
                # Special case: if both are explicitly 0, use full length
                if start_pos == 0.0 and end_pos == 0.0:
                    # Both are explicitly set to 0, which means use full length
                    start_pos = 0.0
                    end_pos = subelement.Length
                else:
                    # If only EndPosition is 0, interpret it as end of member
                    if end_pos == 0.0:
                        end_pos = subelement.Length
                
                # Ensure positions are within valid range
                start_pos = max(0.0, min(start_pos, subelement.Length))
                end_pos = max(0.0, min(end_pos, subelement.Length))
                
                # Ensure consistent ordering for visualization
                if start_pos > end_pos:
                    FreeCAD.Console.PrintWarning(f"StartPosition ({start_pos}) is greater than EndPosition ({end_pos}). The visualization will swap them.\n")
                    # Swap start and end positions
                    temp = start_pos
                    start_pos = end_pos
                    end_pos = temp
                
                # Adjust distance for arrow placement
                distEndStart = end_pos - start_pos
                # If start and end are the same, use full length
                if distEndStart == 0:
                    start_pos = 0.0
                    end_pos = subelement.Length
                    distEndStart = subelement.Length

            # Gera a lista de pontos 
            pInit = subelement.Vertexes[0].Point
            dist = distEndStart / nArrow if nArrow > 0 else 0
            
            # Calculate direction vector for the edge
            edge_vec = FreeCAD.Vector(
                subelement.Vertexes[1].Point.x - subelement.Vertexes[0].Point.x,
                subelement.Vertexes[1].Point.y - subelement.Vertexes[0].Point.y,
                subelement.Vertexes[1].Point.z - subelement.Vertexes[0].Point.z
            )
            
            # Normalize and calculate unit direction vector
            edge_length = edge_vec.Length
            if edge_length > 0:
                unit_dir_vec = FreeCAD.Vector(
                    edge_vec.x / edge_length,
                    edge_vec.y / edge_length,
                    edge_vec.z / edge_length
                )
            else:
                unit_dir_vec = FreeCAD.Vector(0,0,0)
            
            # Calculate start point based on start position
            start_point = FreeCAD.Vector(
                subelement.Vertexes[0].Point.x + (unit_dir_vec.x * start_pos),
                subelement.Vertexes[0].Point.y + (unit_dir_vec.y * start_pos),
                subelement.Vertexes[0].Point.z + (unit_dir_vec.z * start_pos)
            )
            
            # Only generate arrows if there's a valid distance to place them on
            if distEndStart > 0:
                # Generate the actual number of arrows to display between start_pos and end_pos
                nArrow = min(max(int(nArrow * (distEndStart / subelement.Length)), 3), 50)
                
                # Calculate step vector for arrow placement - only along the specified section
                step_length = distEndStart / max(1, nArrow - 1)  # Ensure we don't divide by zero
                step_vec = FreeCAD.Vector(
                    unit_dir_vec.x * step_length,
                    unit_dir_vec.y * step_length,
                    unit_dir_vec.z * step_length
                )
                
                listPoints = []
                # Create points from start_pos to end_pos
                for i in range(nArrow):
                    point = FreeCAD.Vector(
                        start_point.x + step_vec.x * i,
                        start_point.y + step_vec.y * i,
                        start_point.z + step_vec.z * i
                    )
                    listPoints.append(point)

                # gera a lista de setas já em suas devidas escalas e nas devidas distancia posicionadas sobre o eixo X
                listArrow = []            
                for i in range(len(listPoints)):
                    # Calculate load value at this position for scaling
                    load_value = obj.InitialLoading
                    if distEndStart > 0:
                        # Calculate position ratio between 0 and 1 based on position in the array
                        position_ratio = float(i) / max(1, len(listPoints) - 1)  # Avoid division by zero
                        # Interpolate between initial and final loading
                        load_value = obj.InitialLoading + (obj.FinalLoading - obj.InitialLoading) * position_ratio
                
                    arrowCopy = self.makeArrow(obj, load_value)
                    listArrow.append(arrowCopy)
                    Fe = 1.0
                    if obj.InitialLoading != 0:
                        Fe = load_value / obj.InitialLoading  # calculo do fator de escala               
                    
                    # Replace match-case with if-elif for compatibility
                    if obj.GlobalDirection == '+X':
                        arrowCopy.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(0,1,0), -90)
                    elif obj.GlobalDirection == '-X':
                        arrowCopy.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(0,1,0), 90)
                    elif obj.GlobalDirection == '+Y':
                        arrowCopy.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(1,0,0), 90)
                    elif obj.GlobalDirection == '-Y':
                        arrowCopy.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(1,0,0), -90)
                    elif obj.GlobalDirection == '+Z':
                        arrowCopy.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(1,0,0), 180)
                    elif obj.GlobalDirection == '-Z':
                        arrowCopy.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(1,0,0), 0)
                    
                    arrowCopy.scale(Fe)
                    arrowCopy.translate(listPoints[i])
            else:
                # Create a single arrow at the midpoint of the member if no valid range is specified
                midpoint = FreeCAD.Vector(
                    subelement.Vertexes[0].Point.x + (unit_dir_vec.x * subelement.Length * 0.5),
                    subelement.Vertexes[0].Point.y + (unit_dir_vec.y * subelement.Length * 0.5),
                    subelement.Vertexes[0].Point.z + (unit_dir_vec.z * subelement.Length * 0.5)
                )
                listPoints = [midpoint]
                listArrow = []
                
                # Create a single arrow
                arrowCopy = self.makeArrow(obj, obj.InitialLoading)
                
                # Apply rotation based on direction
                if obj.GlobalDirection == '+X':
                    arrowCopy.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(0,1,0), -90)
                elif obj.GlobalDirection == '-X':
                    arrowCopy.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(0,1,0), 90)
                elif obj.GlobalDirection == '+Y':
                    arrowCopy.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(1,0,0), 90)
                elif obj.GlobalDirection == '-Y':
                    arrowCopy.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(1,0,0), -90)
                elif obj.GlobalDirection == '+Z':
                    arrowCopy.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(1,0,0), 180)
                elif obj.GlobalDirection == '-Z':
                    arrowCopy.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(1,0,0), 0)
                
                arrowCopy.translate(midpoint)
            shape = Part.makeCompound(listArrow)
            obj.ViewObject.ShapeAppearance = (FreeCAD.Material(DiffuseColor=(0.00,0.00,1.00),AmbientColor=(0.33,0.33,0.33),SpecularColor=(0.53,0.53,0.53),EmissiveColor=(0.00,0.00,0.00),Shininess=(0.90),Transparency=(0.00),))
            if hasattr(obj, 'LoadType') and hasattr(obj, 'GlobalDirection'):
                # If the load has start and end positions, include them in the label
                if hasattr(obj, 'StartPosition') and hasattr(obj, 'EndPosition') and \
                   (obj.StartPosition.Value > 0 or obj.EndPosition.Value > 0):
                    # Get actual used positions after swapping if needed
                    actual_start = min(obj.StartPosition.Value, obj.EndPosition.Value)
                    actual_end = max(obj.StartPosition.Value, obj.EndPosition.Value)
                    # Show positions in the label
                    if actual_end > 0:
                        obj.Label = f'{obj.LoadType} distributed load ({obj.GlobalDirection}) [{actual_start}-{actual_end}]'
                    else:
                        obj.Label = f'{obj.LoadType} distributed load ({obj.GlobalDirection}) [{actual_start}]'
                else:
                    obj.Label = f'{obj.LoadType} distributed load ({obj.GlobalDirection})'
            else:
                obj.Label = 'distributed load'


        obj.Placement = shape.Placement
        obj.Shape = shape
        obj.ViewObject.DisplayMode = 'Shaded'

    def onChanged(self,obj,Parameter):
        if Parameter == 'edgeLength':
            self.execute(obj)
        elif Parameter == 'LoadType':
            # Update label when load type changes
            if hasattr(obj, 'LoadType') and hasattr(obj, 'GlobalDirection'):
                obj.Label = f'{obj.LoadType} distributed load ({obj.GlobalDirection})'
        elif Parameter == 'GlobalDirection':
            # Re-execute when direction changes
            if hasattr(obj, 'ObjectBase') and obj.ObjectBase:
                self.execute(obj)
        elif Parameter == 'StartPosition' or Parameter == 'EndPosition':
            # Re-execute when start or end position changes
            if hasattr(obj, 'ObjectBase') and obj.ObjectBase:
                # Validate that start position is not beyond end of member
                if hasattr(obj, 'StartPosition'):
                    if obj.StartPosition.Value < 0:
                        obj.StartPosition = 0.0
                        FreeCAD.Console.PrintWarning("StartPosition cannot be negative. Set to 0.\n")
                    
                # Handle special case for EndPosition = 0
                if hasattr(obj, 'EndPosition'):
                    if obj.EndPosition.Value < 0:
                        obj.EndPosition = 0.0
                        FreeCAD.Console.PrintWarning("EndPosition cannot be negative. Set to 0.\n")
                
                self.execute(obj)

class ViewProviderLoadDistributed:
    def __init__(self, obj):
        obj.Proxy = self
    

    def getIcon(self):
        return """
/* XPM */
static char * load_distributed_xpm[] = {
"32 32 17 1",
" 	c None",
".	c #1966FF",
"+	c #000000",
"#	c #1966FE",
"$	c #1966FD",
"%	c #1966FC",
"&	c #1966FB",
"*	c #1966FA",
"=	c #1966F9",
"-	c #1966F8",
";	c #1966F7",
">	c #1966F6",
",	c #1966F5",
"'	c #1966F4",
")	c #1966F3",
"!	c #1966F2",
"~	c #1966F1",
"                                ",
"                                ",
"      ......................    ",
"     .++++++++++++++++++++++.   ",
"    .++....................++  ",
"   .++......................++ ",
"  .++........................++",
" .++..........................+",
" .+...........................+",
" .+...........................+",
" .+...........................+",
" .+...........................+",
" .+...........................+",
" .+...........................+",
" .+...........................+",
" .+...........................+",
" .+...........................+",
" .+...........................+",
" .+...........................+",
" .+...........................+",
" .+...........................+",
" .+...........................+",
" .+...........................+",
" .++........................++ ",
"  .++......................++  ",
"   .++....................++   ",
"    .++++++++++++++++++++++.    ",
"     ......................     ",
"                                ",
"                                ",
"                                ",
"                                ",
"                                ",
"                                ",
"                                "};
        """


class CommandLoadDistributed():
    """My new command"""

    def GetResources(self):
        return {"Pixmap"  : os.path.join(ICONPATH, "icons/load_distributed.svg"), # the name of a svg file available in the resources
                "Accel"   : "Shift+L", # a default shortcut (optional)
                "MenuText": "Distributed Load",
                "ToolTip" : "Adds loads to the structure"}

    def Activated(self):
        try:
            selections = list(FreeCADGui.Selection.getSelectionEx())
            
            # Check if any selections were made
            if not selections:
                show_error_message("กรุณาเลือกเส้น (line) ก่อนสร้างภาระกระจาย", "Please select a line before creating a distributed load")
                return
    
            for selection in selections:
                if selection.HasSubObjects: #Valida se a seleção possui sub objetos
                    for subSelectionname in selection.SubElementNames:
                        # Check if the selection is an Edge before creating the object
                        if 'Edge' not in subSelectionname:
                            show_error_message("กรุณาเลือกเส้น (line) เท่านั้น สำหรับภาระกระจายนี้", "Please select only lines for this distributed load")
                            continue  # Skip this selection and continue with others

                        doc = FreeCAD.ActiveDocument
                        obj = doc.addObject("Part::FeaturePython", "Load_Distributed")

                        print(subSelectionname)
                        objLoad = LoadDistributed(obj,(selection.Object, subSelectionname))
                        ViewProviderLoadDistributed(obj.ViewObject)
                else:
                    # Check if the selection is a valid object with edges
                    if not hasattr(selection.Object, 'Shape') or not selection.Object.Shape:
                        show_error_message("วัตถุที่เลือกไม่มีรูปร่างที่ถูกต้องสำหรับภาระกระจาย", "Selected object does not have a valid shape for distributed load")
                        continue
                        
                    # pass
                    line = selection.Object
                    edges = line.Shape.Edges
                    if not edges:
                        show_error_message("วัตถุที่เลือกไม่มีเส้น (edges) สำหรับสร้างภาระกระจาย", "Selected object has no edges to create distributed load")
                        continue
                        
                    for i in range(len(edges)):
                        doc = FreeCAD.ActiveDocument
                        obj = doc.addObject("Part::FeaturePython", "Load_Distributed")
                        LoadDistributed(obj,(selection.Object, 'Edge'+str(i+1)))
                        ViewProviderLoadDistributed(obj.ViewObject)

        
            FreeCAD.ActiveDocument.recompute()
        except Exception as e:
            show_error_message(f"เกิดข้อผิดพลาดในการสร้างภาระกระจาย: {str(e)}", f"Error creating distributed load: {str(e)}")
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

# Only register command if FreeCAD GUI is available
if FREECAD_AVAILABLE and 'FreeCADGui' in globals():
    FreeCADGui.addCommand("load_distributed", CommandLoadDistributed())
