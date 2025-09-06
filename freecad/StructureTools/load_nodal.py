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


class LoadNodal:
    def __init__(self, obj, selection):
        obj.Proxy = self
        obj.addProperty("App::PropertyLinkSubList", "ObjectBase", "Base", "Object base")
        obj.addProperty("App::PropertyForce", "NodalLoading", "Nodal", "Nodal loading").NodalLoading = 10000000
        obj.addProperty("App::PropertyFloat", "ScaleDraw", "Load", "Scale from drawing").ScaleDraw = 1
        
        # Add Thai units properties
        if THAI_UNITS_AVAILABLE:
            obj.addProperty("App::PropertyFloat", "NodalLoadingKgf", "Thai Units", "Nodal loading in kgf").NodalLoadingKgf = 1000000  # ~10000000 N in kgf
            obj.addProperty("App::PropertyFloat", "NodalLoadingTf", "Thai Units", "Nodal loading in tf").NodalLoadingTf = 1000  # ~10000000 N in tf
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
    
    def getLoadInThaiUnits(self, obj):
        """Get load values in Thai units."""
        if not THAI_UNITS_AVAILABLE:
            return None
        
        converter = get_thai_converter()
        force_n = obj.NodalLoading.Value  # Force in N
        
        return enhance_with_thai_units({
            'force_N': force_n,
            'force_kN': force_n / 1000,
            'load_type': obj.LoadType,
            'direction': obj.GlobalDirection,
            'description_thai': f'ภาระจุด {obj.LoadType} ทิศทาง {obj.GlobalDirection}'
        }, 'load')
    
    def updateThaiUnits(self, obj):
        """Update Thai units properties when main load changes."""
        if not THAI_UNITS_AVAILABLE or not hasattr(obj, 'NodalLoadingKgf'):
            return
        
        converter = get_thai_converter()
        force_n = obj.NodalLoading.Value
        
        obj.NodalLoadingKgf = converter.n_to_kgf(force_n)
        obj.NodalLoadingTf = converter.kn_to_tf(force_n / 1000)
    
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
        if 'Vertex' in obj.ObjectBase[0][1][0]:
            # Desenha carregamento pontual 
            shape = self.makeArrow(obj, obj.NodalLoading)
            
            match obj.GlobalDirection:
                case '+X':
                    shape.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(0,1,0), -90)
                case '-X':
                    shape.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(0,1,0), 90)
                case '+Y':
                    shape.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(1,0,0), 90)
                case '-Y':
                    shape.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(1,0,0), -90)
                case '+Z':
                    shape.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(1,0,0), 180)
                case '-Z':
                    shape.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(1,0,0), 0)
            
            
            shape.translate(subelement.Point)
            obj.ViewObject.ShapeAppearance = (FreeCAD.Material(DiffuseColor=(1.00,0.00,0.00),AmbientColor=(0.33,0.33,0.33),SpecularColor=(0.53,0.53,0.53),EmissiveColor=(0.00,0.00,0.00),Shininess=(0.90),Transparency=(0.00),))
            if hasattr(obj, 'LoadType') and hasattr(obj, 'GlobalDirection'):
                obj.Label = f'{obj.LoadType} nodal load ({obj.GlobalDirection})'
            else:
                obj.Label = 'nodal load'

            # Set shape properties only when shape is defined
            obj.Placement = shape.Placement
            obj.Shape = shape
            obj.ViewObject.DisplayMode = 'Shaded'
        else:
            # If selection is not a Vertex (e.g., Edge), show error and don't create shape
            show_error_message("กรุณาเลือกจุด (point) เท่านั้น สำหรับภาระจุดนี้", "Please select only points for this nodal load")
            # Clear any existing shape
            obj.Shape = Part.Shape()
    
    def onChanged(self,obj,Parameter):
        if Parameter == 'edgeLength':
            self.execute(obj)
        elif Parameter == 'LoadType':
            # Update label when load type changes
            if hasattr(obj, 'LoadType') and hasattr(obj, 'GlobalDirection'):
                obj.Label = f'{obj.LoadType} nodal load ({obj.GlobalDirection})'
        elif Parameter == 'GlobalDirection':
            # Re-execute when direction changes
            if hasattr(obj, 'ObjectBase') and obj.ObjectBase:
                self.execute(obj)
    

class ViewProviderLoadNodal:
    def __init__(self, obj):
        obj.Proxy = self
    

    def getIcon(self):
        return """
              /* XPM */
static char * load_nodal_xpm[] = {
"32 32 36 1",
" 	c None",
".	c #110101",
"+	c #220303",
"@	c #1C0303",
"#	c #190303",
"$	c #200303",
"%	c #FF1919",
"&	c #DC1616",
"*	c #1A0303",
"=	c #1D0303",
"-	c #190202",
";	c #DE1616",
">	c #100101",
",	c #160202",
"'	c #D11414",
")	c #DD1616",
"!	c #E61717",
"~	c #790C0C",
"{	c #E71717",
"]	c #E91717",
"^	c #180202",
"/	c #5D0A0A",
"(	c #5D0909",
"_	c #1B0202",
":	c #D51515",
"<	c #D81515",
"[	c #1A0202",
"}	c #420707",
"|	c #420606",
"1	c #C31313",
"2	c #C61313",
"3	c #2D0404",
"4	c #FE1919",
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


class CommandLoadNodal():
    """My new command"""

    def GetResources(self):
        return {"Pixmap"  : os.path.join(ICONPATH, "icons/load_nodal.svg"), # the name of a svg file available in the resources
                "Accel"   : "Shift+N", # a default shortcut (optional)
                "MenuText": "Nodal load",
                "ToolTip" : "Adds loads to the structure"}

    def Activated(self):
        try:
            selections = list(FreeCADGui.Selection.getSelectionEx())   
            
            # Check if any selections were made
            if not selections:
                show_error_message("กรุณาเลือกจุด (point) ก่อนสร้างภาระจุด", "Please select a point before creating a nodal load")
                return
            
            for selection in selections:
                for subSelectionname in selection.SubElementNames:
                    # Check if the selection is a Vertex (point) before creating the object
                    if 'Vertex' not in subSelectionname:
                        show_error_message("กรุณาเลือกจุด (point) เท่านั้น สำหรับภาระจุดนี้", "Please select only points for this nodal load")
                        continue  # Skip this selection and continue with others
                        
                    doc = FreeCAD.ActiveDocument
                    obj = doc.addObject("Part::FeaturePython", "Load_Nodal")

                    objLoad = LoadNodal(obj,(selection.Object, subSelectionname))
                    ViewProviderLoadNodal(obj.ViewObject)
            
            FreeCAD.ActiveDocument.recompute()
        except:
            show_error_message("กรุณาเลือกจุด (point) สำหรับเพิ่มภาระจุด", "Please select a point to add a nodal load")
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

# Only register command if FreeCAD GUI is available
if FREECAD_AVAILABLE and 'FreeCADGui' in globals():
    FreeCADGui.addCommand("load_nodal", CommandLoadNodal())
