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
            class QVBoxLayout:
                def __init__(self): pass
            class QLabel:
                def __init__(self, text): pass

# Import Thai units support
try:
    from .utils.universal_thai_units import enhance_with_thai_units, thai_material_units, get_universal_thai_units
    from .utils.thai_units import get_thai_converter
    from .utils.units_manager import get_units_manager, format_stress, format_modulus
    THAI_UNITS_AVAILABLE = True
    GLOBAL_UNITS_AVAILABLE = True
except ImportError:
    THAI_UNITS_AVAILABLE = False
    GLOBAL_UNITS_AVAILABLE = False
    enhance_with_thai_units = lambda x, t: x
    thai_material_units = lambda f: f
    get_universal_thai_units = lambda: None
    get_thai_converter = lambda: None
    get_units_manager = lambda: None
    format_stress = lambda x: f"{x/1e6:.1f} MPa"
    format_modulus = lambda x: f"{x/1e6:.0f} MPa"

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")

# Import material standards database
try:
    from .data.MaterialDatabase import MaterialDatabase
    from .data.MaterialStandards import MATERIAL_STANDARDS, MATERIAL_CATEGORIES, get_material_info
    DATABASE_AVAILABLE = True
    print(f"[OK] MaterialStandards imported successfully: {len(MATERIAL_STANDARDS)} standards")
except ImportError as e:
    print(f"[ERROR] MaterialStandards import failed: {e}")
    # Try absolute import as fallback
    try:
        import freecad.StructureTools.data.MaterialStandards as MS
        MATERIAL_STANDARDS = MS.MATERIAL_STANDARDS
        MATERIAL_CATEGORIES = MS.MATERIAL_CATEGORIES 
        get_material_info = MS.get_material_info
        DATABASE_AVAILABLE = True
        print(f"[OK] MaterialStandards absolute import successful: {len(MATERIAL_STANDARDS)} standards")
    except ImportError as e2:
        print(f"[ERROR] Absolute import also failed: {e2}")
        # Fallback if data module not available
        MATERIAL_STANDARDS = {}
        MATERIAL_CATEGORIES = {}
        MaterialDatabase = None
        DATABASE_AVAILABLE = False
        print("[ERROR] Using empty MATERIAL_STANDARDS fallback")
        def get_material_info(standard_name):
            return {}

def show_error_message(msg):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setIcon(QtWidgets.QMessageBox.Critical)  # Ícone de erro
    msg_box.setWindowTitle("Erro")
    msg_box.setText(msg)
    msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg_box.exec_()


class Material:
    def __init__(self, obj):
        obj.Proxy = self

        # Basic material properties - Initialize with minimal values, user must select MaterialStandard
        obj.addProperty("App::PropertyPressure", "ModulusElasticity", "Material", "Modulus of elasticity")
        obj.ModulusElasticity = "1 MPa"  # Minimal value - user must select MaterialStandard
        
        obj.addProperty("App::PropertyFloat", "PoissonRatio", "Material", "Poisson ratio")
        obj.PoissonRatio = 0.0001  # Minimal value - user must select MaterialStandard
        
        obj.addProperty("App::PropertyDensity", "Density", "Material", "Material density")
        obj.Density = "1 kg/m^3"  # Minimal value - user must select MaterialStandard
        
        # Add missing properties that calc expects
        obj.addProperty("App::PropertyString", "Name", "Material", "Material name")
        obj.Name = obj.Label if hasattr(obj, 'Label') else 'Material'
        
        # Add additional material properties with minimal defaults
        obj.addProperty("App::PropertyPressure", "YieldStrength", "Strength", "Yield strength")
        obj.YieldStrength = "1 MPa"  # Minimal value - user must select MaterialStandard
        
        obj.addProperty("App::PropertyPressure", "UltimateStrength", "Strength", "Ultimate tensile strength")
        obj.UltimateStrength = "1 MPa"  # Minimal value - user must select MaterialStandard
        
        obj.addProperty("App::PropertyString", "GradeDesignation", "Standard", "Grade designation")
        obj.GradeDesignation = "Undefined"  # User must select MaterialStandard
        
        # Add material standard support with intelligent default
        obj.addProperty("App::PropertyEnumeration", "MaterialStandard", "Standard", "Material standard from database")
        if MATERIAL_STANDARDS:
            obj.MaterialStandard = list(MATERIAL_STANDARDS.keys())
            
            # Set intelligent default based on object name/label
            default_standard = self._determine_default_standard(obj)
            obj.MaterialStandard = default_standard
            
            # Force initial property update
            self._update_standard_properties(obj)
        else:
            obj.MaterialStandard = ["Custom"]
            obj.MaterialStandard = "Custom"
        
        # Note: Additional properties already added above - no duplicates needed
    
    def _determine_default_standard(self, obj):
        """Determine appropriate default MaterialStandard based on object name/label."""
        obj_name = getattr(obj, 'Label', getattr(obj, 'Name', ''))
        
        # Check for concrete indicators
        if ('ACI' in obj_name and ('30MP' in obj_name or 'concrete' in obj_name.lower())):
            return "ACI_Normal_30MPa"
        elif ('ACI' in obj_name and ('25MP' in obj_name)):
            return "ACI_Normal_25MPa"
        elif 'concrete' in obj_name.lower():
            return "ACI_Normal_30MPa"  # Default concrete
        
        # Check for steel indicators
        elif 'ASTM_A36' in obj_name:
            return "ASTM_A36"
        elif 'ASTM_A992' in obj_name or 'steel' in obj_name.lower():
            return "ASTM_A992"
        elif 'EN_S235' in obj_name:
            return "EN_S235"
        elif 'EN_S355' in obj_name:
            return "EN_S355"
        
        # Default fallback - prefer concrete over steel for new objects
        return "ACI_Normal_30MPa"

    def execute(self, obj): 
        # Update Name to match Label
        if hasattr(obj, 'Label'):
            obj.Name = obj.Label
        else:
            obj.Label = 'Material'
            obj.Name = 'Material'
    
    def onChanged(self, obj, prop):
        """Handle property changes with validation."""
        if prop == 'Label':
            # Update Name to match Label for calc compatibility
            if hasattr(obj, 'Name'):
                obj.Name = obj.Label
        elif prop == 'MaterialStandard':
            # Update properties based on selected standard
            self._update_standard_properties(obj)
        elif prop == 'PoissonRatio':
            # Validate Poisson ratio
            if hasattr(obj, 'PoissonRatio'):
                nu = obj.PoissonRatio
                if not (0.0 <= nu <= 0.5):
                    FreeCAD.Console.PrintError(f"Invalid Poisson ratio {nu:.3f}. Must be between 0.0 and 0.5\n")
                    obj.PoissonRatio = 0.3  # Reset to default
    
    def get_calc_properties(self, obj, unit_length='m', unit_force='kN'):
        """
        Get material properties formatted for calc integration.
        
        This method provides compatibility with the calc system by formatting
        material properties in the expected units and structure.
        """
        try:
            # Convert density from kg/m³ to target force/volume units
            density_kg_m3 = obj.Density.getValueAs('kg/m^3')
            density_kn_m3 = density_kg_m3 * 9.81 / 1000  # Convert to kN/m³
            
            # Get elastic properties
            E = obj.ModulusElasticity.getValueAs(f'{unit_force}/{unit_length}^2')
            nu = obj.PoissonRatio
            G = E / (2 * (1 + nu))  # Calculate shear modulus
            
            return {
                'name': obj.Name if hasattr(obj, 'Name') else obj.Label,
                'E': float(E),
                'G': float(G), 
                'nu': float(nu),
                'density': float(density_kn_m3),
                'unit_system': f'{unit_force}-{unit_length}'
            }
            
        except Exception as e:
            FreeCAD.Console.PrintError(f"Error getting calc properties for material: {e}\n")
            # Return warning - no defaults should be used
            App.Console.PrintWarning(f"Material {getattr(obj, 'Name', 'Unknown')} has no valid properties. Please select MaterialStandard.\n")
            return {
                'name': getattr(obj, 'Name', getattr(obj, 'Label', 'Material')),
                'E': 1.0,  # Minimal value to prevent calc errors - user should select material standard
                'G': 1.0,   # Minimal value to prevent calc errors
                'nu': 0.0001,
                'density': 0.001,  # Minimal value to prevent calc errors
                'unit_system': f'{unit_force}-{unit_length}'
            }
    
    def _update_standard_properties(self, obj):
        """Update material properties based on selected standard from database."""
        if not hasattr(obj, 'MaterialStandard'):
            FreeCAD.Console.PrintWarning("Object has no MaterialStandard property\n")
            return
        
        standard = obj.MaterialStandard
        FreeCAD.Console.PrintMessage(f"[UPDATE] Updating properties for MaterialStandard: {standard}\n")
        
        if not MATERIAL_STANDARDS:
            FreeCAD.Console.PrintError("[ERROR] MATERIAL_STANDARDS is empty!\n")
            return
            
        if standard in MATERIAL_STANDARDS:
            props = MATERIAL_STANDARDS[standard]
            FreeCAD.Console.PrintMessage(f"[OK] Found properties for {standard}: {props}\n")
            
            # Update properties from database
            try:
                if 'ModulusElasticity' in props:
                    obj.ModulusElasticity = props['ModulusElasticity']
                    FreeCAD.Console.PrintMessage(f"   [OK] ModulusElasticity: {props['ModulusElasticity']}\n")
                    
                if 'PoissonRatio' in props:
                    obj.PoissonRatio = props['PoissonRatio']
                    FreeCAD.Console.PrintMessage(f"   [OK] PoissonRatio: {props['PoissonRatio']}\n")
                    
                if 'Density' in props:
                    obj.Density = props['Density']
                    FreeCAD.Console.PrintMessage(f"   [OK] Density: {props['Density']}\n")
                    
                if 'YieldStrength' in props and hasattr(obj, 'YieldStrength'):
                    obj.YieldStrength = props['YieldStrength']
                    FreeCAD.Console.PrintMessage(f"   [OK] YieldStrength: {props['YieldStrength']}\n")
                    
                if 'UltimateStrength' in props and hasattr(obj, 'UltimateStrength'):
                    obj.UltimateStrength = props['UltimateStrength']
                    FreeCAD.Console.PrintMessage(f"   [OK] UltimateStrength: {props['UltimateStrength']}\n")
                    
                if 'GradeDesignation' in props and hasattr(obj, 'GradeDesignation'):
                    obj.GradeDesignation = props['GradeDesignation']
                    FreeCAD.Console.PrintMessage(f"   [OK] GradeDesignation: {props['GradeDesignation']}\n")
                
                FreeCAD.Console.PrintMessage(f"[SUCCESS] Material properties updated successfully for {standard}\n")
                
                # Force object and document recompute to refresh UI
                obj.recompute()
                if hasattr(App, 'ActiveDocument') and App.ActiveDocument:
                    App.ActiveDocument.recompute()
                
            except Exception as e:
                FreeCAD.Console.PrintError(f"[ERROR] Error updating material properties: {e}\n")
                import traceback
                traceback.print_exc()
        else:
            available_standards = list(MATERIAL_STANDARDS.keys())
            FreeCAD.Console.PrintError(f"[ERROR] Standard '{standard}' not found in database\n")
            FreeCAD.Console.PrintMessage(f"Available standards: {available_standards}\n")
    
    def get_available_standards(self):
        """Get list of available material standards."""
        return list(MATERIAL_STANDARDS.keys())
    
    def get_standards_by_category(self, category):
        """Get material standards by category (Steel, Concrete, Aluminum)."""
        if category in MATERIAL_CATEGORIES:
            return MATERIAL_CATEGORIES[category]
        return []
    
    def get_standard_info(self, standard_name):
        """Get detailed information about a material standard."""
        return get_material_info(standard_name)


    def onChanged(self,obj,Parameter):
        if Parameter == 'edgeLength':
            self.execute(obj)
    

class ViewProviderMaterial:
    def __init__(self, obj):
        obj.Proxy = self
    

    def getIcon(self):
        return """
        /* XPM */
static char * material_xpm[] = {
"32 32 340 2",
"  	c None",
". 	c #020303",
"+ 	c #06080B",
"@ 	c #040506",
"# 	c #010102",
"$ 	c #07080B",
"% 	c #030305",
"& 	c #020203",
"* 	c #080B11",
"= 	c #2F3C57",
"- 	c #4E648E",
"; 	c #6680B4",
"> 	c #718BC0",
", 	c #758EC0",
"' 	c #7087B3",
") 	c #586A8D",
"! 	c #374257",
"~ 	c #0A0C10",
"{ 	c #020304",
"] 	c #000002",
"^ 	c #010203",
"/ 	c #172032",
"( 	c #5475B5",
"_ 	c #7BA6FC",
": 	c #81ACFF",
"< 	c #86AFFF",
"[ 	c #8BB2FF",
"} 	c #90B6FF",
"| 	c #95B9FF",
"1 	c #9ABCFF",
"2 	c #9FC0FF",
"3 	c #A0C0FF",
"4 	c #9EBEFC",
"5 	c #7188B4",
"6 	c #202632",
"7 	c #030304",
"8 	c #020202",
"9 	c #020507",
"0 	c #0A101B",
"a 	c #4769AD",
"b 	c #6D9DFE",
"c 	c #72A1FF",
"d 	c #77A5FF",
"e 	c #7CA8FF",
"f 	c #81ABFF",
"g 	c #90B5FF",
"h 	c #9FBFFF",
"i 	c #9FBFFE",
"j 	c #6B81AB",
"k 	c #10141A",
"l 	c #050607",
"m 	c #020407",
"n 	c #16233D",
"o 	c #568AED",
"p 	c #6297FF",
"q 	c #679AFF",
"r 	c #6C9EFF",
"s 	c #71A1FF",
"t 	c #76A4FF",
"u 	c #7BA8FF",
"v 	c #80ABFF",
"w 	c #85AEFF",
"x 	c #8AB2FF",
"y 	c #8FB5FF",
"z 	c #94B8FF",
"A 	c #94B2EC",
"B 	c #262D3C",
"C 	c #040508",
"D 	c #020307",
"E 	c #1C335D",
"F 	c #518AFA",
"G 	c #5890FF",
"H 	c #5D93FF",
"I 	c #6C9DFF",
"J 	c #7BA7FF",
"K 	c #8AB1FF",
"L 	c #99BBFF",
"M 	c #9EBFFF",
"N 	c #9DBCFA",
"O 	c #3A465C",
"P 	c #040507",
"Q 	c #020409",
"R 	c #0F1D38",
"S 	c #4683F9",
"T 	c #4D89FF",
"U 	c #528CFF",
"V 	c #5790FF",
"W 	c #5C93FF",
"X 	c #6196FF",
"Y 	c #669AFF",
"Z 	c #6B9DFF",
"` 	c #70A0FF",
" .	c #75A4FF",
"..	c #7AA7FF",
"+.	c #80AAFF",
"@.	c #8FB4FF",
"#.	c #ACC8FF",
"$.	c #E5EEFF",
"%.	c #F7F9FF",
"&.	c #EBF1FF",
"*.	c #BFD4FF",
"=.	c #272E3D",
"-.	c #050507",
";.	c #060D1C",
">.	c #3A76ED",
",.	c #4382FF",
"'.	c #4885FF",
").	c #578FFF",
"!.	c #6699FF",
"~.	c #75A3FF",
"{.	c #7FAAFF",
"].	c #84ADFF",
"^.	c #A3C2FF",
"/.	c #FDFEFF",
"(.	c #FFFFFF",
"_.	c #C3D7FF",
":.	c #000202",
"<.	c #010204",
"[.	c #2352AE",
"}.	c #387BFF",
"|.	c #3D7EFF",
"1.	c #4282FF",
"2.	c #4785FF",
"3.	c #4C88FF",
"4.	c #518CFF",
"5.	c #568FFF",
"6.	c #5B92FF",
"7.	c #6B9CFF",
"8.	c #7AA6FF",
"9.	c #DDE8FF",
"0.	c #F3F7FF",
"a.	c #6B80AA",
"b.	c #000205",
"c.	c #081733",
"d.	c #2E74FE",
"e.	c #3377FF",
"f.	c #4281FF",
"g.	c #518BFF",
"h.	c #6095FF",
"i.	c #6599FF",
"j.	c #6A9CFF",
"k.	c #6F9FFF",
"l.	c #74A3FF",
"m.	c #79A6FF",
"n.	c #F0F5FF",
"o.	c #A5C3FF",
"p.	c #1F2531",
"q.	c #000204",
"r.	c #194EB6",
"s.	c #2870FF",
"t.	c #2D74FF",
"u.	c #3277FF",
"v.	c #377AFF",
"w.	c #3C7EFF",
"x.	c #4784FF",
"y.	c #568EFF",
"z.	c #6598FF",
"A.	c #74A2FF",
"B.	c #F5F8FF",
"C.	c #9CBDFF",
"D.	c #020711",
"E.	c #1E68FC",
"F.	c #236DFF",
"G.	c #2D73FF",
"H.	c #3C7DFF",
"I.	c #4181FF",
"J.	c #4684FF",
"K.	c #4B87FF",
"L.	c #508BFF",
"M.	c #558EFF",
"N.	c #5A91FF",
"O.	c #5F95FF",
"P.	c #6498FF",
"Q.	c #699BFF",
"R.	c #6E9FFF",
"S.	c #98BAFF",
"T.	c #FEFFFF",
"U.	c #C0D5FF",
"V.	c #96BAFF",
"W.	c #9BBDFF",
"X.	c #9DBDFB",
"Y.	c #090B0E",
"Z.	c #000203",
"`.	c #082457",
" +	c #1966FF",
".+	c #1D69FF",
"++	c #236CFF",
"@+	c #3276FF",
"#+	c #4180FF",
"$+	c #508AFF",
"%+	c #5F94FF",
"&+	c #E9F0FF",
"*+	c #FEFEFF",
"=+	c #EFF5FF",
"-+	c #B9D0FF",
";+	c #8CB3FF",
">+	c #91B6FF",
",+	c #96B9FF",
"'+	c #353F54",
")+	c #01050B",
"!+	c #0E398F",
"~+	c #226CFF",
"{+	c #276FFF",
"]+	c #2C73FF",
"^+	c #3176FF",
"/+	c #3679FF",
"(+	c #3B7DFF",
"_+	c #4080FF",
":+	c #4583FF",
"<+	c #4A87FF",
"[+	c #4F8AFF",
"}+	c #548DFF",
"|+	c #5991FF",
"1+	c #5E94FF",
"2+	c #6398FF",
"3+	c #689BFF",
"4+	c #6D9EFF",
"5+	c #72A2FF",
"6+	c #9BBCFF",
"7+	c #58698C",
"8+	c #07090B",
"9+	c #010206",
"0+	c #1147B1",
"a+	c #1D68FF",
"b+	c #2C72FF",
"c+	c #3B7CFF",
"d+	c #6397FF",
"e+	c #6A82B0",
"f+	c #000102",
"g+	c #134DC1",
"h+	c #1C68FF",
"i+	c #216BFF",
"j+	c #266FFF",
"k+	c #2B72FF",
"l+	c #3075FF",
"m+	c #3579FF",
"n+	c #3A7CFF",
"o+	c #3F80FF",
"p+	c #4483FF",
"q+	c #4986FF",
"r+	c #4E8AFF",
"s+	c #538DFF",
"t+	c #5D94FF",
"u+	c #86AEFF",
"v+	c #708BC0",
"w+	c #010202",
"x+	c #266EFF",
"y+	c #3F7FFF",
"z+	c #4E89FF",
"A+	c #6C88C0",
"B+	c #1B67FF",
"C+	c #206BFF",
"D+	c #256EFF",
"E+	c #2A72FF",
"F+	c #2F75FF",
"G+	c #3478FF",
"H+	c #397CFF",
"I+	c #3E7FFF",
"J+	c #4886FF",
"K+	c #6296FF",
"L+	c #71A0FF",
"M+	c #5F7AB0",
"N+	c #040406",
"O+	c #0E398E",
"P+	c #2A71FF",
"Q+	c #397BFF",
"R+	c #485E8B",
"S+	c #06070B",
"T+	c #1A67FF",
"U+	c #1F6AFF",
"V+	c #246EFF",
"W+	c #2971FF",
"X+	c #2E74FF",
"Y+	c #3378FF",
"Z+	c #4D88FF",
"`+	c #5C92FF",
" @	c #2A3753",
".@	c #020710",
"+@	c #1964FB",
"@@	c #246DFF",
"#@	c #72A0FA",
"$@	c #07090E",
"%@	c #000104",
"&@	c #1248B5",
"*@	c #1E6AFF",
"=@	c #2970FF",
"-@	c #387AFF",
";@	c #4D6FB2",
">@	c #020204",
",@	c #051431",
"'@	c #1966FE",
")@	c #1E69FF",
"!@	c #5A92FF",
"~@	c #6497FE",
"{@	c #141D2F",
"]@	c #020305",
"^@	c #1145AC",
"/@	c #3F62A8",
"(@	c #030A1A",
"_@	c #175EEC",
":@	c #4584FF",
"<@	c #4D83EB",
"[@	c #080E19",
"}@	c #010207",
"|@	c #051738",
"1@	c #1864F9",
"2@	c #4984FA",
"3@	c #12213C",
"4@	c #030508",
"5@	c #010307",
"6@	c #09245C",
"7@	c #1964FA",
"8@	c #216CFF",
"9@	c #3076FF",
"0@	c #3E7DFA",
"a@	c #18305C",
"b@	c #06183B",
"c@	c #3170EB",
"d@	c #0D1E3C",
"e@	c #020308",
"f@	c #010407",
"g@	c #1144AA",
"h@	c #1B68FF",
"i@	c #256EFE",
"j@	c #1C4CA9",
"k@	c #040B19",
"l@	c #010408",
"m@	c #000000",
"n@	c #1248B3",
"o@	c #1348B2",
"p@	c #061430",
"q@	c #010205",
"r@	c #01060F",
"s@	c #082255",
"t@	c #0E388C",
"u@	c #1147B2",
"v@	c #134DC0",
"w@	c #0E388B",
"x@	c #082254",
"y@	c #01060E",
"                        . + @ # # @ $ .                         ",
"                  % & * = - ; > , ' ) ! ~ { %                   ",
"              ] ^ / ( _ : < [ } | 1 2 3 4 5 6 7 8               ",
"            9 0 a b c d e f < [ g | 1 h 3 3 i j k l             ",
"          m n o p q r s t u v w x y z 1 h 3 3 3 A B C           ",
"        D E F G H p q I s t J v w K y z L M 3 3 3 N O P         ",
"      Q R S T U V W X Y Z `  ...+.w K @.#.$.%.&.*.3 N =.-.      ",
"    ] ;.>.,.'.T U ).W X !.Z ` ~...{.].^./.(.(.(.(._.3 A k :.    ",
"    <.[.}.|.1.2.3.4.5.6.X !.7.` ~.8.{.9.(.(.(.(.(.0.3 3 a.{     ",
"  b.c.d.e.}.|.f.2.3.g.5.6.h.i.j.k.l.m.n.(.(.(.(.(.(.o.3 i p.%   ",
"  q.r.s.t.u.v.w.f.x.3.g.y.6.h.z.j.k.A.9.(.(.(.(.(.B.C.3 3 ' {   ",
"  D.E.F.s.G.u.v.H.I.J.K.L.M.N.O.P.Q.R.S.T.(.(.(.(.U.V.W.3 X.Y.  ",
"Z.`. +.+++s.G.@+v.H.#+J.K.$+M.N.%+P.Q.R.M &+*+=+-+;+>+,+W.3 '+. ",
")+!+ + +.+~+{+]+^+/+(+_+:+<+[+}+|+1+2+3+4+5+..e : < [ } | 6+7+8+",
"9+0+ + + +a+~+{+b+^+/+c+_+:+<+[+}+|+1+d+3+4+c d e f < [ g | e+@ ",
"f+g+ + + + +h+i+j+k+l+m+n+o+p+q+r+s+G t+p q r s t u f u+[ g v+w+",
"f+g+ + + + + +h+i+x+k+l+m+n+y+p+q+z+s+G H p q I s t J v w K A+w+",
"9+0+ + + + + + +B+C+D+E+F+G+H+I+,.J+T U V W K+q I L+t J +.w M+N+",
")+O+ + + + + + + +B+C+D+P+F+G+Q+I+,.'.T U ).W X !.Z ` ~...{.R+S+",
"Z.`. + + + + + + + +T+U+V+W+X+Y+}.|.1.'.Z+U ).`+X !.7.` ~.8. @& ",
"  .@+@ + + + + + + + +T+U+@@W+X+e.}.|.f.2.3.g.5.6.h.i.j.k.#@$@  ",
"  %@&@ + + + + + + + + + +*@F.=@X+e.-@|.f.x.3.g.y.6.h.z.j.;@>@  ",
"  Z.,@'@ + + + + + + + + + +)@F.s.G.u.v.H.I.J.K.L.M.!@O.~@{@]@  ",
"    q.^@ + + + + + + + + + + +)@++s.G.@+v.H.#+J.K.L.M.N./@>@    ",
"    ] (@_@ + + + + + + + + + + +.+~+{+]+^+/+(+_+:@<+[+<@[@]     ",
"      }@|@1@ + + + + + + + + + + +a+~+{+b+^+/+(+_+:+2@3@4@      ",
"        5@6@7@ + + + + + + + + + + +h+8@j+k+9@m+n+0@a@D         ",
"          5@b@_@ + + + + + + + + + + +h+i+j+k+l+c@d@e@          ",
"            f@(@g@'@ + + + + + + + + + +h@C+i@j@k@l@            ",
"              m@%@,@n@+@ + + + + + + + ++@o@p@q@]               ",
"                  b.q.r@s@t@u@v@v@0+w@x@y@q.b.                  ",
"                        Z.)+5@f+f+5@)+Z.                        "};
        """


class CommandMaterial():
    """Enhanced material command with database support"""

    def GetResources(self):
        return {"Pixmap"  : os.path.join(ICONPATH, "icons/material.svg"),
                "Accel"   : "Shift+M",
                "MenuText": "Material (Enhanced)",
                "ToolTip" : "Create material with database standards support"}

    def Activated(self):
        # Show material selection dialog if standards are available
        if MATERIAL_STANDARDS:
            self.show_material_selection_dialog()
        else:
            self.create_basic_material()

    def show_material_selection_dialog(self):
        """Show dialog to select material standard from database."""
        try:
            from PySide2 import QtWidgets, QtCore
        except ImportError:
            from PySide import QtWidgets, QtCore
        
        # Create dialog
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Select Material Standard")
        dialog.setMinimumWidth(400)
        dialog.setMinimumHeight(300)
        
        layout = QtWidgets.QVBoxLayout()
        
        # Category selection
        category_group = QtWidgets.QGroupBox("Material Category")
        category_layout = QtWidgets.QVBoxLayout()
        
        category_combo = QtWidgets.QComboBox()
        categories = list(MATERIAL_CATEGORIES.keys())
        category_combo.addItems(categories)
        category_layout.addWidget(category_combo)
        category_group.setLayout(category_layout)
        layout.addWidget(category_group)
        
        # Material standard selection
        standard_group = QtWidgets.QGroupBox("Material Standard")
        standard_layout = QtWidgets.QVBoxLayout()
        
        standard_list = QtWidgets.QListWidget()
        standard_layout.addWidget(standard_list)
        standard_group.setLayout(standard_layout)
        layout.addWidget(standard_group)
        
        # Properties preview
        preview_group = QtWidgets.QGroupBox("Properties Preview")
        preview_layout = QtWidgets.QVBoxLayout()
        preview_text = QtWidgets.QTextEdit()
        preview_text.setMaximumHeight(120)
        preview_text.setReadOnly(True)
        preview_layout.addWidget(preview_text)
        preview_group.setLayout(preview_layout)
        layout.addWidget(preview_group)
        
        # Buttons
        button_layout = QtWidgets.QHBoxLayout()
        create_button = QtWidgets.QPushButton("Create Material")
        cancel_button = QtWidgets.QPushButton("Cancel")
        button_layout.addWidget(create_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)
        
        dialog.setLayout(layout)
        
        # Connect signals
        def update_standards():
            category = category_combo.currentText()
            standard_list.clear()
            if category in MATERIAL_CATEGORIES:
                standards = MATERIAL_CATEGORIES[category]
                standard_list.addItems(standards)
        
        def update_preview():
            current = standard_list.currentItem()
            if current:
                standard_name = current.text()
                props = get_material_info(standard_name)
                preview_text.clear()
                for key, value in props.items():
                    preview_text.append(f"{key}: {value}")
        
        category_combo.currentTextChanged.connect(update_standards)
        standard_list.itemClicked.connect(update_preview)
        cancel_button.clicked.connect(dialog.reject)
        
        # Initialize
        update_standards()
        
        def create_material():
            current = standard_list.currentItem()
            if current:
                standard_name = current.text()
                self.create_material_from_standard(standard_name)
                dialog.accept()
            else:
                QtWidgets.QMessageBox.warning(dialog, "Warning", "Please select a material standard")
        
        create_button.clicked.connect(create_material)
        
        # Show dialog
        dialog.exec_()

    def create_material_from_standard(self, standard_name):
        """Create material from selected standard."""
        doc = FreeCAD.ActiveDocument
        if not doc:
            return
        
        # Create material object
        obj = doc.addObject("Part::FeaturePython", f"Material_{standard_name}")
        Material(obj)
        ViewProviderMaterial(obj.ViewObject)
        
        # Set standard
        obj.MaterialStandard = standard_name
        
        # Properties will be auto-updated by onChanged handler
        doc.recompute()
        
        FreeCAD.Console.PrintMessage(f"Created material with standard: {standard_name}\n")

    def create_basic_material(self):
        """Create basic material (fallback)."""
        doc = FreeCAD.ActiveDocument
        if not doc:
            return
        
        obj = doc.addObject("Part::FeaturePython", "Material")
        Material(obj)
        ViewProviderMaterial(obj.ViewObject)
        doc.recompute()

    def IsActive(self):
        return FreeCAD.ActiveDocument is not None

# Only register command if FreeCAD GUI is available
if FREECAD_AVAILABLE and 'FreeCADGui' in globals():
    FreeCADGui.addCommand("material", CommandMaterial())
