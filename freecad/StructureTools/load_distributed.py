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

def show_error_message(msg):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setIcon(QtWidgets.QMessageBox.Critical)  # Ícone de erro
    msg_box.setWindowTitle("Erro")
    msg_box.setText(msg)
    msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg_box.exec_()


class LoadDistributed:
    def __init__(self, obj, selection):
        obj.Proxy = self
        obj.addProperty("App::PropertyLinkSubList", "ObjectBase", "Base", "Object base")
        obj.addProperty("App::PropertyForce", "InitialLoading", "Distributed", "Initial loading (load per unit length)").InitialLoading = 10000000
        obj.addProperty("App::PropertyForce", "FinalLoading", "Distributed", "Final loading (load per unit length)").FinalLoading = 10000000
        obj.addProperty("App::PropertyFloat", "ScaleDraw", "Load", "Scale from drawing").ScaleDraw = 1

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
            
            

            FEend = obj.FinalLoading / obj.InitialLoading #fator de escala entre as forças 'end' e 'start'
            distEndStart = subelement.Length

            # Gera a lista de pontos 
            pInit = subelement.Vertexes[0].Point
            dist = subelement.Length / nArrow
            distx = (subelement.Vertexes[1].Point.x - subelement.Vertexes[0].Point.x) / nArrow #Calcula a distancia entre cada seta no eixo x
            disty = (subelement.Vertexes[1].Point.y - subelement.Vertexes[0].Point.y) / nArrow #Calcula a distancia entre cada seta no eixo y
            distz = (subelement.Vertexes[1].Point.z - subelement.Vertexes[0].Point.z) / nArrow #Calcula a distancia entre cada seta no eixo z
            listPoints = []
            for i in range(nArrow + 1):
                x = distx * i 
                y = disty * i 
                z = distz * i 
                listPoints.append(FreeCAD.Vector(x,y,z))

            # gera a lista de setas já em suas devidas escalas e nas devidas distancia posicionadas sobre o eixo X
            listArrow = []            
            for i in range(nArrow + 1):
                arrowCopy = self.makeArrow(obj, obj.InitialLoading)
                listArrow.append(arrowCopy)
                Fe = ((dist * i * (FEend - 1)) / distEndStart)  + 1 #calculo do fator de escala               
                
                match obj.GlobalDirection:
                    case '+X':
                        arrowCopy.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(0,1,0), -90)
                    case '-X':
                        arrowCopy.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(0,1,0), 90)
                    case '+Y':
                        arrowCopy.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(1,0,0), 90)
                    case '-Y':
                        arrowCopy.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(1,0,0), -90)
                    case '+Z':
                        arrowCopy.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(1,0,0), 180)
                    case '-Z':
                        arrowCopy.rotate(FreeCAD.Vector(0,0,0),FreeCAD.Vector(1,0,0), 0)
                
                arrowCopy.scale(Fe)
                arrowCopy.translate(listPoints[i])
                listArrow.append(arrowCopy)

            shape = Part.makeCompound(listArrow)
            shape.translate(subelement.Vertexes[0].Point)
            obj.ViewObject.ShapeAppearance = (FreeCAD.Material(DiffuseColor=(0.00,0.00,1.00),AmbientColor=(0.33,0.33,0.33),SpecularColor=(0.53,0.53,0.53),EmissiveColor=(0.00,0.00,0.00),Shininess=(0.90),Transparency=(0.00),))
            if hasattr(obj, 'LoadType') and hasattr(obj, 'GlobalDirection'):
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
    

class ViewProviderLoadDistributed:
    def __init__(self, obj):
        obj.Proxy = self
    

    def getIcon(self):
        return """
/* XPM */
static char * load_distributed_xpm[] = {
"32 32 99 2",
"  	c None",
". 	c #030D22",
"+ 	c #0E3B93",
"@ 	c #1144AA",
"# 	c #0E398F",
"$ 	c #1658DD",
"% 	c #1966FF",
"& 	c #1556D6",
"* 	c #1860F0",
"= 	c #1452CC",
"- 	c #1555D5",
"; 	c #175EEA",
"> 	c #1861F2",
", 	c #0D3483",
"' 	c #030A17",
") 	c #030E26",
"! 	c #020611",
"~ 	c #1966FE",
"{ 	c #09255B",
"] 	c #030C1D",
"^ 	c #030917",
"/ 	c #0E388C",
"( 	c #0D337F",
"_ 	c #020C1E",
": 	c #092256",
"< 	c #0E3789",
"[ 	c #030918",
"} 	c #040D20",
"| 	c #165BE4",
"1 	c #0D398D",
"2 	c #020917",
"3 	c #030914",
"4 	c #020B1C",
"5 	c #01060F",
"6 	c #0A2863",
"7 	c #020916",
"8 	c #020A18",
"9 	c #020712",
"0 	c #01050F",
"a 	c #010815",
"b 	c #030D1F",
"c 	c #165AE1",
"d 	c #0E3687",
"e 	c #020B1D",
"f 	c #1862F6",
"g 	c #0A2966",
"h 	c #0E3C96",
"i 	c #1659DF",
"j 	c #030C1E",
"k 	c #0C317A",
"l 	c #031026",
"m 	c #1042A5",
"n 	c #1864F9",
"o 	c #020B1E",
"p 	c #04122D",
"q 	c #0C3078",
"r 	c #1965FD",
"s 	c #1450C8",
"t 	c #061637",
"u 	c #020A19",
"v 	c #1554D2",
"w 	c #030C1F",
"x 	c #030C1C",
"y 	c #134CBE",
"z 	c #092459",
"A 	c #165AE0",
"B 	c #06173B",
"C 	c #0B2A69",
"D 	c #124ABA",
"E 	c #020C1D",
"F 	c #081F4E",
"G 	c #0C3179",
"H 	c #1964FA",
"I 	c #081E49",
"J 	c #040C1E",
"K 	c #1760EF",
"L 	c #0F40A0",
"M 	c #1146AE",
"N 	c #020C1F",
"O 	c #041433",
"P 	c #020A1B",
"Q 	c #134CBD",
"R 	c #030F24",
"S 	c #07193F",
"T 	c #0E3A91",
"U 	c #04132F",
"V 	c #1659DE",
"W 	c #081F4D",
"X 	c #134DC1",
"Y 	c #030B1D",
"Z 	c #030D1E",
"` 	c #175CE6",
" .	c #041129",
"..	c #071E4C",
"+.	c #061B44",
"@.	c #082155",
"#.	c #01040B",
"$.	c #020815",
"%.	c #010307",
"                                                                ",
"                                                                ",
"                                                                ",
"    . + @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ # .     ",
"    . $ % % % % % % % % % % % % % % % % % % % % % % % % & .     ",
"    . $ % * = = = = = = = = - % % ; = = = = = = = = > % & .     ",
"    . $ % , ' ) ) ) ) ) ) ) ! ~ % { ] ) ) ) ) ) ) ^ / % & .     ",
"    . $ % (                 _ ~ % :                 < % & .     ",
"    . $ % (                 _ ~ % :                 < % & .     ",
"    . $ % (                 _ ~ % :                 < % & .     ",
"    . $ % (                 _ ~ % :                 < % & .     ",
"    . $ % (                 _ ~ % :                 < % & .     ",
"    . $ % (                 _ ~ % :                 < % & .     ",
"    . $ % (                 _ ~ % :                 < % & .     ",
"    . $ % (                 _ ~ % :                 < % & .     ",
"    . $ % (                 _ ~ % :                 < % & .     ",
"    . $ % (                 _ ~ % :                 < % & .     ",
"    . $ % (                 _ ~ % :                 < % & .     ",
"    . $ % (                 _ ~ % :                 < % & .     ",
"    . $ % (                 _ ~ % :                 < % & .     ",
"    . $ % (                 _ ~ % :                 < % & .     ",
"[ } ! | % 1 2 }         3 4 5 ~ % 6 7 4       8 4 9 + % $ 0 4 a ",
"b c % % % % % d         e f % % % % % g         h % % % % % i j ",
"  k % % % % % l           m % % % % n o         p % % % % % q   ",
"  . r % % % s j           t % % % % @ u         b v % % % r w   ",
"  x y % % % z             b A % % % B             C % % % D E   ",
"    F % % f _               G % % | b             b H % % I     ",
"    J K % L                 . r % (               7 M % * N     ",
"      h % O                 P Q % R                 S % T       ",
"      U V w                   W X Y                 Z `  .      ",
"      b ..                    _ +.                    @.Z       ",
"        #.                      $.                    %.        "};
        """


class CommandLoadDistributed():
    """My new command"""

    def GetResources(self):
        return {"Pixmap"  : os.path.join(ICONPATH, "icons/load_distributed.svg"), # the name of a svg file available in the resources
                "Accel"   : "Shift+L", # a default shortcut (optional)
                "MenuText": "Distributed Load",
                "ToolTip" : "Adds loads to the structure"}

    def Activated(self):
        # try:
        selections = list(FreeCADGui.Selection.getSelectionEx())
    
        for selection in selections:
            if selection.HasSubObjects: #Valida se a seleção possui sub objetos
                for subSelectionname in selection.SubElementNames:

                    doc = FreeCAD.ActiveDocument
                    obj = doc.addObject("Part::FeaturePython", "Load_Distributed")

                    print(subSelectionname)
                    objLoad = LoadDistributed(obj,(selection.Object, subSelectionname))
                    ViewProviderLoadDistributed(obj.ViewObject)
            else:
                # pass
                line = selection.Object
                edges = line.Shape.Edges
                for i in range(len(edges)):
                    doc = FreeCAD.ActiveDocument
                    obj = doc.addObject("Part::FeaturePython", "Load_Distributed")
                    LoadDistributed(obj,(selection.Object, 'Edge'+str(i+1)))
                    ViewProviderLoadDistributed(obj.ViewObject)

        
        FreeCAD.ActiveDocument.recompute()
        # except:
        #     show_error_message("Seleciona uma barra para adicionar um carregamento distribuido.")
        return

    def IsActive(self):
        """Here you can define if the command must be active or not (greyed) if certain conditions
        are met or not. This function is optional."""
        return True

# Only register command if FreeCAD GUI is available
if FREECAD_AVAILABLE and 'FreeCADGui' in globals():
    FreeCADGui.addCommand("load_distributed", CommandLoadDistributed())
