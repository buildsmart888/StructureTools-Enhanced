# Setup FreeCAD stubs for standalone operation
try:
    from .utils.freecad_stubs import setup_freecad_stubs, is_freecad_available
    if not is_freecad_available():
        setup_freecad_stubs()
except ImportError:
    pass

# Import FreeCAD modules (now available via stubs if needed)
try:
    import FreeCAD as App
    import FreeCADGui
    import Part
    FREECAD_AVAILABLE = True
except ImportError:
    FREECAD_AVAILABLE = False
    # Create mock objects for standalone operation
    class MockApp:
        class Vector:
            def __init__(self, x=0, y=0, z=0):
                self.x = x
                self.y = y
                self.z = z
            
            def translate(self, vec):
                pass
                
        class Material:
            def __init__(self, **kwargs):
                pass
    
    class MockPart:
        @staticmethod
        def makeCone(r1, r2, h):
            return MockPart()
            
        @staticmethod
        def makeCylinder(r, h):
            return MockPart()
            
        def translate(self, vec):
            pass
            
        @staticmethod
        def makeCompound(list):
            return MockPart()
    
    class MockFreeCADGui:
        @staticmethod
        def Selection():
            class SelectionEx:
                def getSelectionEx():
                    return []
            return SelectionEx()
    
    App = MockApp()
    FreeCADGui = MockFreeCADGui()
    Part = MockPart()

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
            class QMessageBox:
                Critical = 0
                Ok = 1
                
                def __init__(self):
                    pass
                    
                def setIcon(self, icon):
                    pass
                    
                def setWindowTitle(self, title):
                    pass
                    
                def setText(self, text):
                    pass
                    
                def setStandardButtons(self, buttons):
                    pass
                    
                def exec_(self):
                    pass

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
        
    try:
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText(full_msg)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec_()
    except Exception:
        # Fallback if QMessageBox is not available
        print("ERROR:", full_msg)


class LoadPoint:
    def __init__(self, obj, selection):
        obj.Proxy = self
        obj.addProperty("App::PropertyLinkSubList", "ObjectBase", "Base", "Object base")
        obj.addProperty("App::PropertyForce", "PointLoading", "Point", "Point loading").PointLoading = 10000000
        obj.addProperty("App::PropertyFloat", "ScaleDraw", "Load", "Scale from drawing").ScaleDraw = 1
        # Add property for position of point load along member (0.0 to 1.0)
        obj.addProperty("App::PropertyFloat", "RelativePosition", "Point", "Relative position along member (0.0 to 1.0)").RelativePosition = 0.5

        # Add Thai units properties
        if THAI_UNITS_AVAILABLE:
            obj.addProperty("App::PropertyFloat", "PointLoadingKgf", "Thai Units", "Point loading in kgf").PointLoadingKgf = 1000000  # ~10000000 N in kgf
            obj.addProperty("App::PropertyFloat", "PointLoadingTf", "Thai Units", "Point loading in tf").PointLoadingTf = 1000  # ~10000000 N in tf
            obj.addProperty("App::PropertyBool", "UseThaiUnits", "Thai Units", "Use Thai units display").UseThaiUnits = False
        
        # Load Type Properties
        obj.addProperty("App::PropertyEnumeration", "LoadType", "Load", "Type of load")
        obj.LoadType = ['DL', 'LL', 'H', 'F', 'W', 'E']
        obj.LoadType = 'DL'
        
        obj.addProperty("App::PropertyEnumeration", "GlobalDirection","Load","Global direction load")
        # Point Load Directions
        # x, y, z          - Load applied in local x,y or z direction
        # X, Y, Z          - Load applied in global X,Y or Z direction
        # My, Mz           - Moment about member local y or z axis
        # Mx               - Torsional Moment about member local x-axis
        obj.GlobalDirection = ['+X','-X', '+Y','-Y', '+Z','-Z', '+x','-x', '+y','-y', '+z','-z', '+My','-My', '+Mz','-Mz', '+Mx','-Mx']
        obj.GlobalDirection = '-Z'
        
        print(selection)
        obj.ObjectBase = (selection[0], selection[1])
    
    def getLoadInThaiUnits(self, obj):
        """Get load values in Thai units."""
        if not THAI_UNITS_AVAILABLE:
            return None
        
        converter = get_thai_converter()
        if converter is None:
            return None
            
        force_n = obj.PointLoading.Value  # Force in N
        
        return enhance_with_thai_units({
            'force_N': force_n,
            'force_kN': force_n / 1000,
            'load_type': obj.LoadType,
            'direction': obj.GlobalDirection,
            'description_thai': f'ภาระจุด {obj.LoadType} ทิศทาง {obj.GlobalDirection}'
        }, 'load')
    
    def updateThaiUnits(self, obj):
        """Update Thai units properties when main load changes."""
        if not THAI_UNITS_AVAILABLE or not hasattr(obj, 'PointLoadingKgf'):
            return
        
        converter = get_thai_converter()
        if converter is None:
            return
            
        force_n = obj.PointLoading.Value
        
        try:
            obj.PointLoadingKgf = converter.n_to_kgf(force_n)
            obj.PointLoadingTf = converter.kn_to_tf(force_n / 1000)
        except Exception:
            # Handle case where converter methods might not exist
            obj.PointLoadingKgf = force_n / 9.81  # Approximate conversion
            obj.PointLoadingTf = force_n / 9810  # Approximate conversion
    
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
        cylinder.translate(App.Vector(0,0, heightCone * obj.ScaleDraw * load/1000000))
        return Part.makeCompound([cone, cylinder])
    
    
    def execute(self, obj):
        # Safety check for ObjectBase
        if not hasattr(obj, 'ObjectBase') or not obj.ObjectBase or len(obj.ObjectBase) == 0:
            return
        if not obj.ObjectBase[0] or len(obj.ObjectBase[0]) < 2 or not obj.ObjectBase[0][1]:
            return
            
        subelement = self.getSubelement(obj, obj.ObjectBase[0][1][0])
        if 'Edge' in obj.ObjectBase[0][1][0]:
            # Desenha carregamento pontual 
            shape = self.makeArrow(obj, obj.PointLoading)
            
            # Calculate position along the edge based on RelativePosition (0.0 to 1.0)
            position_ratio = max(0.0, min(1.0, obj.RelativePosition))  # Clamp between 0.0 and 1.0
            
            # Calculate point along edge
            start_point = subelement.Vertexes[0].Point
            end_point = subelement.Vertexes[1].Point
            
            # Calculate edge length
            edge_length = subelement.Length
            
            # Linear interpolation between start and end points
            load_point = App.Vector(
                start_point.x + (end_point.x - start_point.x) * position_ratio,
                start_point.y + (end_point.y - start_point.y) * position_ratio,
                start_point.z + (end_point.z - start_point.z) * position_ratio
            )
            
            # Replace match-case with if-elif for compatibility
            # Handle force directions
            if obj.GlobalDirection == '+X':
                shape.rotate(App.Vector(0,0,0),App.Vector(0,1,0), -90)
            elif obj.GlobalDirection == '-X':
                shape.rotate(App.Vector(0,0,0),App.Vector(0,1,0), 90)
            elif obj.GlobalDirection == '+Y':
                shape.rotate(App.Vector(0,0,0),App.Vector(1,0,0), 90)
            elif obj.GlobalDirection == '-Y':
                shape.rotate(App.Vector(0,0,0),App.Vector(1,0,0), -90)
            elif obj.GlobalDirection == '+Z':
                shape.rotate(App.Vector(0,0,0),App.Vector(1,0,0), 180)
            elif obj.GlobalDirection == '-Z':
                shape.rotate(App.Vector(0,0,0),App.Vector(1,0,0), 0)
            elif obj.GlobalDirection == '+x':
                shape.rotate(App.Vector(0,0,0),App.Vector(0,1,0), -90)
            elif obj.GlobalDirection == '-x':
                shape.rotate(App.Vector(0,0,0),App.Vector(0,1,0), 90)
            elif obj.GlobalDirection == '+y':
                shape.rotate(App.Vector(0,0,0),App.Vector(1,0,0), 90)
            elif obj.GlobalDirection == '-y':
                shape.rotate(App.Vector(0,0,0),App.Vector(1,0,0), -90)
            elif obj.GlobalDirection == '+z':
                shape.rotate(App.Vector(0,0,0),App.Vector(1,0,0), 180)
            elif obj.GlobalDirection == '-z':
                shape.rotate(App.Vector(0,0,0),App.Vector(1,0,0), 0)
            # Handle moment directions (no rotation needed for moments, just position)
            elif obj.GlobalDirection in ['+My', '-My', '+Mz', '-Mz', '+Mx', '-Mx']:
                # For moments, we'll use a different visualization
                # For now, we'll just position it without rotation
                pass
            
            shape.translate(load_point)
            obj.ViewObject.ShapeAppearance = (App.Material(DiffuseColor=(0.00,1.00,0.00),AmbientColor=(0.33,0.33,0.33),SpecularColor=(0.53,0.53,0.53),EmissiveColor=(0.00,0.00,0.00),Shininess=(0.90),Transparency=(0.00),))
            if hasattr(obj, 'LoadType') and hasattr(obj, 'GlobalDirection'):
                obj.Label = f'{obj.LoadType} point load ({obj.GlobalDirection}) at {obj.RelativePosition*100:.0f}%'
            else:
                obj.Label = 'point load'

        obj.Placement = shape.Placement
        obj.Shape = shape
        obj.ViewObject.DisplayMode = 'Shaded'
        
        
    def onChanged(self,obj,Parameter):
        if Parameter == 'edgeLength':
            self.execute(obj)
        elif Parameter == 'LoadType':
            # Update label when load type changes
            if hasattr(obj, 'LoadType') and hasattr(obj, 'GlobalDirection'):
                position = getattr(obj, 'RelativePosition', 0.5) if hasattr(obj, 'RelativePosition') else 0.5
                obj.Label = f'{obj.LoadType} point load ({obj.GlobalDirection}) at {position*100:.0f}%'
        elif Parameter == 'GlobalDirection':
            # Re-execute when direction changes
            if hasattr(obj, 'ObjectBase') and obj.ObjectBase:
                self.execute(obj)
        elif Parameter == 'RelativePosition':
            # Re-execute when position changes
            if hasattr(obj, 'ObjectBase') and obj.ObjectBase:
                self.execute(obj)
            # Update label
            if hasattr(obj, 'LoadType') and hasattr(obj, 'GlobalDirection'):
                position = getattr(obj, 'RelativePosition', 0.5) if hasattr(obj, 'RelativePosition') else 0.5
                obj.Label = f'{obj.LoadType} point load ({obj.GlobalDirection}) at {position*100:.0f}%'

class ViewProviderLoadPoint:
    def __init__(self, obj):
        obj.Proxy = self
    

    def getIcon(self):
        return """
/* XPM */
static char * load_point_xpm[] = {
"32 32 36 1",
" 	c None",
".	c #110101",
"+	c #220303",
"@	c #1C0303",
"#	c #190303",
"$	c #200303",
"%	c #008000",
"&	c #006600",
"*	c #1A0303",
"=	c #1D0303",
"-	c #190202",
";	c #007700",
">	c #100101",
",	c #160202",
"'	c #008800",
")	c #007700",
"!	c #009900",
"~	c #790C0C",
"{	c #00AA00",
"]	c #00BB00",
"^	c #180202",
"/	c #5D0A0A",
"(	c #5D0909",
"_	c #1B0202",
":	c #00CC00",
"<	c #00DD00",
"[	c #1A0202",
"}	c #420707",
"|	c #420606",
"1	c #00EE00",
"2	c #00FF00",
"3	c #2D0404",
"4	c #008000",
"5	c #2E0404",
"6	c #A91010",
"7	c #210303",
"             .+++@#             ",
"             $%%%&$             ",
"             $%%%&$             ",
"             $%%%&$             ",
"             $%%%&$             ",
"             $%%%&$             ",
"             $%%%&$             ",
"             $%%%&$             ",
"             $%%%&$             ",
"             $%%%&$             ",
"             $%%%&$             ",
"             $%%%&$             ",
"             $%%%&$             ",
"             $%%%&$             ",
"             $%%%&$             ",
"             $%%%&$             ",
"             $%%%&$             ",
"             $%%%&$             ",
"             $%%%&$             ",
"             $%%%&$             ",
"          *==-%%%;>==*          ",
"          ,')!%%%%;)',          ",
"           ~%%%%%%%%~           ",
"           -{%%%%%%]^           ",
"            /%%%%%%(            ",
"            _:%%%%<[            ",
"             }%%%%|             ",
"             #1%%2@             ",
"              34%5              ",
"              ^66*              ",
"               77               ",
"                                "};
        """


class CommandLoadPoint():
    """Point Load Command"""

    def GetResources(self):
        return {"Pixmap"  : os.path.join(ICONPATH, "icons/load_point.svg"), # the name of a svg file available in the resources
                "Accel"   : "Shift+P", # a default shortcut (optional)
                "MenuText": "Point Load",
                "ToolTip" : "Adds point loads to the structure at a specified position along members"}

    def Activated(self):
        try:
            selections = list(FreeCADGui.Selection.getSelectionEx())
        
            # Check if any selections were made
            if not selections:
                show_error_message("กรุณาเลือกเส้น (line) ก่อนสร้างภาระจุด", "Please select a line before creating a point load")
                return
                
            for selection in selections:
                if selection.HasSubObjects: #Valida se a seleção possui sub objetos
                    for subSelectionname in selection.SubElementNames:
                        # Check if the selection is an Edge before creating the object
                        if 'Edge' not in subSelectionname:
                            show_error_message("กรุณาเลือกเส้น (line) เท่านั้น สำหรับภาระจุดนี้", "Please select only lines for this point load")
                            continue  # Skip this selection and continue with others
                            
                        doc = App.activeDocument()
                        obj = doc.addObject("Part::FeaturePython", "Load_Point")
                        objLoad = LoadPoint(obj,(selection.Object, subSelectionname))
                        ViewProviderLoadPoint(obj.ViewObject)
                else:
                    # Check if the selection is a valid object with edges
                    if not hasattr(selection.Object, 'Shape') or not selection.Object.Shape:
                        show_error_message("วัตถุที่เลือกไม่มีรูปร่างที่ถูกต้องสำหรับภาระจุด", "Selected object does not have a valid shape for point load")
                        continue
                        
                    # If no subobjects selected, create point loads on all edges
                    line = selection.Object
                    edges = line.Shape.Edges
                    if not edges:
                        show_error_message("วัตถุที่เลือกไม่มีเส้น (edges) สำหรับสร้างภาระจุด", "Selected object has no edges to create point load")
                        continue
                        
                    for i in range(len(edges)):
                        doc = App.activeDocument()
                        obj = doc.addObject("Part::FeaturePython", "Load_Point")
                        LoadPoint(obj,(selection.Object, 'Edge'+str(i+1)))
                        ViewProviderLoadPoint(obj.ViewObject)

            App.activeDocument().recompute()
        except Exception as e:
            show_error_message(f"เกิดข้อผิดพลาดในการสร้างภาระจุด: {str(e)}", f"Error creating point load: {str(e)}")
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

# Only register command if FreeCAD GUI is available
if FREECAD_AVAILABLE and hasattr(FreeCADGui, 'addCommand'):
    FreeCADGui.addCommand("load_point", CommandLoadPoint())