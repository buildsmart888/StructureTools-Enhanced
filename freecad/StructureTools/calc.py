import os, math
import sys

# Setup FreeCAD stubs for standalone operation
try:
    from .utils.freecad_stubs import setup_freecad_stubs, is_freecad_available
    if not is_freecad_available():
        setup_freecad_stubs()
except ImportError:
    pass

# Import FreeCAD modules (now available via stubs if needed)
try:
    import FreeCAD as App, FreeCADGui, Part
    FREECAD_AVAILABLE = True
except ImportError:
    FREECAD_AVAILABLE = False
    print("FreeCAD modules not available - using stub mode")
    # Create more comprehensive mock objects for App and FreeCADGui when not available
    class MockQuantity:
        def __init__(self, value, unit=None):
            self.value = value
            self.unit = unit
            
        def getValueAs(self, unit):
            return self
            
        def __float__(self):
            if hasattr(self.value, '__float__'):
                return float(self.value)
            return 0.0
        
        def __mul__(self, other):
            # Handle multiplication with numbers
            if isinstance(other, (int, float)):
                return MockQuantity(self.value * other, self.unit)
            return NotImplemented
        
        def __rmul__(self, other):
            # Handle reverse multiplication (10 * quantity)
            return self.__mul__(other)
    
    class MockUnits:
        def __init__(self):
            self.Quantity = MockQuantity
    
    class MockConsole:
        def PrintWarning(self, msg):
            print("WARNING:", msg)
            
        def PrintMessage(self, msg):
            print("MESSAGE:", msg)
            
        def PrintError(self, msg):
            print("ERROR:", msg)
    
    class MockVector:
        def __init__(self, x=0, y=0, z=0):
            self.x = x
            self.y = y
            self.z = z
    
    class MockDocument:
        def addObject(self, type, name):
            class MockObject:
                def __init__(self):
                    self.Name = name
                    self.ViewObject = None  # Add ViewObject attribute
            return MockObject()
            
        def recompute(self):
            pass
    
    class MockApp:
        def __init__(self):
            self.Console = MockConsole()
            self.Units = MockUnits()
            self.Vector = MockVector
            self.ActiveDocument = MockDocument()
    
    class MockSelection:
        @staticmethod
        def getSelection():
            return []
    
    class MockFreeCADGui:
        def __init__(self):
            self.Selection = MockSelection()
            
        def addCommand(self, name, command):
            pass
    
    App = MockApp()
    FreeCADGui = MockFreeCADGui()
from PySide import QtWidgets
import subprocess

# Import Thai units support
try:
    from .utils.universal_thai_units import enhance_with_thai_units, thai_auto_units, get_universal_thai_units
    from .utils.thai_units import get_thai_converter
    from .utils.units_manager import get_units_manager, format_force, format_stress, format_modulus
    THAI_UNITS_AVAILABLE = True
    GLOBAL_UNITS_AVAILABLE = True
except ImportError:
    THAI_UNITS_AVAILABLE = False
    GLOBAL_UNITS_AVAILABLE = False
    enhance_with_thai_units = lambda x, t: x
    thai_auto_units = lambda f: f
    get_universal_thai_units = lambda: None
    get_thai_converter = lambda: None
    get_units_manager = lambda: None
    format_force = lambda x: f"{x:.2f} kN"
    format_stress = lambda x: f"{x/1e6:.1f} MPa"
    format_modulus = lambda x: f"{x/1e6:.0f} MPa"

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")

from .Pynite_main.FEModel3D import FEModel3D

# Import material standards database
try:
	from .data.MaterialStandards import MATERIAL_STANDARDS, get_material_info
	HAS_MATERIAL_DATABASE = True
except ImportError:
	MATERIAL_STANDARDS = {}
	def get_material_info(standard_name):
		return {}
	HAS_MATERIAL_DATABASE = False


def _find_matching_node_index(nodes_map, coord, tol=1e-3):
	"""Return index of node in nodes_map whose coordinates match coord within tol, or None."""
	import math as _math
	for idx, n in enumerate(nodes_map):
		if _math.isclose(n[0], coord[0], abs_tol=tol) and _math.isclose(n[1], coord[1], abs_tol=tol) and _math.isclose(n[2], coord[2], abs_tol=tol):
			return idx
	return None


# Try to import PlateMesher at module import time so tests can monkeypatch module attribute
try:
	try:
		# prefer package import when available
		from StructureTools.meshing.PlateMesher import PlateMesher
	except Exception:
		from .meshing.PlateMesher import PlateMesher
except Exception:
	PlateMesher = None


def _print_warning(msg):
	# Try App.Console, fallback to print
	try:
		if hasattr(App, 'Console'):
			App.Console.PrintWarning(msg)
			return
	except Exception:
		pass
	try:
		print('WARNING:', msg)
	except Exception:
		pass


def _print_message(msg):
	try:
		if hasattr(App, 'Console'):
			App.Console.PrintMessage(msg)
			return
	except Exception:
		pass
	try:
		print(msg)
	except Exception:
		pass


def _print_error(msg):
	try:
		if hasattr(App, 'Console'):
			App.Console.PrintError(msg)
			return
	except Exception:
		pass
	try:
		print('ERROR:', msg)
	except Exception:
		pass


# helper to convert FreeCAD.Quantity or numeric values to float in desired units
def qty_val(value, from_unit='mm', to_unit=None):
	# Prefer FreeCAD Units when available
	try:
		if hasattr(App, 'Units') and hasattr(App.Units, 'Quantity'):
			if to_unit:
				return float(App.Units.Quantity(value, from_unit).getValueAs(to_unit))
			return float(App.Units.Quantity(value, from_unit))
	except Exception:
		pass
	# Fallback: try numeric or MockQuantity
	try:
		if hasattr(value, 'value'):
			return float(value.value)
		return float(value)
	except Exception:
		return 0.0

# try:
# 	from Pynite import FEModel3D
# except:
# 	print('Instalando dependencias')
# 	subprocess.check_call(["pip", "install", "PyniteFEA"])

def show_error_message(msg):
	try:
		msg_box = QtWidgets.QMessageBox()
		msg_box.setIcon(QtWidgets.QMessageBox.Critical)  #Ícone de erro
		msg_box.setWindowTitle("Erro")
		msg_box.setText(msg)
		msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
		msg_box.exec_()
	except Exception:
		# Fallback if QMessageBox is not available
		print("ERROR:", msg)


class Calc:
	def __init__(self, obj, elements):
		obj.Proxy = self

		# helper to add properties when running inside FreeCAD or fallback to plain attributes for tests
		def _addProp(prop_type, name, group, desc, default=None, set_value=None):
			if hasattr(obj, 'addProperty'):
				try:
					obj.addProperty(prop_type, name, group, desc)
				except Exception:
					pass

			if set_value is not None:
				setattr(obj, name, set_value)
			elif default is not None:
				setattr(obj, name, default)

		# Basic properties
		_addProp("App::PropertyLinkList", "ListElements", "Calc", "elementos para a analise", default=None)
		if elements is not None:
			setattr(obj, 'ListElements', elements)

		_addProp("App::PropertyString", "LengthUnit", "Calc", "set the length unit for calculation", default='m')
		_addProp("App::PropertyString", "ForceUnit", "Calc", "set the length unit for calculation", default='kN')

		# Load Case Properties (Basic load types)
		_addProp("App::PropertyEnumeration", "LoadCase", "Load Cases", "Select primary load case type")
		obj.LoadCase = ['DL', 'LL', 'H', 'F', 'W', 'E']
		obj.LoadCase = 'DL'

		# Load Combination Properties (Both Allowable Stress and Strength Design)
		_addProp("App::PropertyEnumeration", "LoadCombination", "Load Combinations", "Select load combination for analysis")
		obj.LoadCombination = [
			'100_DL', '101_DL+LL', '102_DL+0.75(LL+W(X+))', '103_DL+0.75(LL+W(x-))',
			'104_DL+0.75(LL+W(y+))', '105_DL+0.75(LL+W(y-))', '106_0.6DL+W(X+)', '107_0.6DL+W(x-)',
			'108_0.6DL+W(y+)', '109_0.6DL+W(y-)', '110_DL+0.7E(X+)', '111_DL+0.7E(x-)',
			'112_DL+0.7E(y+)', '113_DL+0.7E(y-)', '114_DL+0.525E(X+)+0.75LL', '115_DL+0.525E(x-)+0.75LL',
			'116_DL+0.525E(Z+)+0.75LL', '117_DL+0.525E(z-)+0.75LL', '118_0.6DL+0.7E(X+)', '119_0.6DL+0.7E(x-)',
			'120_0.6DL+0.7E(y+)', '121_0.6DL+0.7E(y-)', '122_DL+LL+H+F',
			'1000_1.4DL', '1001_1.4DL+1.7LL', '1002_1.05DL+1.275LL+1.6W(x+)', '1003_1.05DL+1.275LL+1.6W(x-)',
			'1004_1.05DL+1.275LL+1.6W(y+)', '1005_1.05DL+1.275LL+1.6W(y-)', '1006_0.9DL+1.6W(X+)', '1007_0.9DL+1.6W(x-)',
			'1008_0.9DL+1.6W(y+)', '1009_0.9DL+1.6W(y-)', '1010_1.05DL+1.275LL+E(x+)', '1011_1.05DL+1.275LL+E(x-)',
			'1012_1.05DL+1.275LL+E(y+)', '1013_1.05DL+1.275LL+E(y-)', '1014_0.9DL+E(X+)', '1015_0.9DL+E(x-)',
			'1016_0.9DL+E(y+)', '1017_0.9DL+E(y-)', '1018_1.4DL+1.7LL+1.7H', '1019_0.9DL+1.7H',
			'1020_1.4DL+1.7LL+1.4F', '1021_0.9DL+1.4F'
		]
		obj.LoadCombination = '100_DL'

		# Structured per-member results (stored as a python object so tests and UI can access lists/dicts)
		_addProp("App::PropertyPythonObject", "MemberResults", "Calc", "structured per-member results", default=[])

		# Other result properties written by execute(); provide safe defaults to avoid AttributeError
		_addProp("App::PropertyStringList", "NameMembers", "Calc", "list of member names", default=[])
		_addProp("App::PropertyVectorList", "Nodes", "Calc", "list of node vectors", default=[])
		# Time-series and diagram data as string lists (comma-joined values per member)
		_addProp("App::PropertyStringList", "MomentZ", "Calc", "per-member moment Z series", default=[])
		_addProp("App::PropertyStringList", "MomentY", "Calc", "per-member moment Y series", default=[])
		_addProp("App::PropertyStringList", "ShearY", "Calc", "per-member shear Y series", default=[])
		_addProp("App::PropertyStringList", "ShearZ", "Calc", "per-member shear Z series", default=[])
		_addProp("App::PropertyStringList", "AxialForce", "Calc", "per-member axial force series", default=[])
		_addProp("App::PropertyStringList", "Torque", "Calc", "per-member torque series", default=[])
		_addProp("App::PropertyStringList", "DeflectionY", "Calc", "per-member deflection Y series", default=[])
		_addProp("App::PropertyStringList", "DeflectionZ", "Calc", "per-member deflection Z series", default=[])

		# Min/max scalar lists (floats)
		_addProp("App::PropertyFloatList", "MinMomentY", "Calc", "min moment Y per member", default=[])
		_addProp("App::PropertyFloatList", "MinMomentZ", "Calc", "min moment Z per member", default=[])
		_addProp("App::PropertyFloatList", "MaxMomentY", "Calc", "max moment Y per member", default=[])
		_addProp("App::PropertyFloatList", "MaxMomentZ", "Calc", "max moment Z per member", default=[])
		_addProp("App::PropertyFloatList", "MinShearY", "Calc", "min shear Y per member", default=[])
		_addProp("App::PropertyFloatList", "MinShearZ", "Calc", "min shear Z per member", default=[])
		_addProp("App::PropertyFloatList", "MaxShearY", "Calc", "max shear Y per member", default=[])
		_addProp("App::PropertyFloatList", "MaxShearZ", "Calc", "max shear Z per member", default=[])
		_addProp("App::PropertyFloatList", "MinTorque", "Calc", "min torque per member", default=[])
		_addProp("App::PropertyFloatList", "MaxTorque", "Calc", "max torque per member", default=[])
		_addProp("App::PropertyFloatList", "MinDeflectionY", "Calc", "min deflection Y per member", default=[])
		_addProp("App::PropertyFloatList", "MinDeflectionZ", "Calc", "min deflection Z per member", default=[])
		_addProp("App::PropertyFloatList", "MaxDeflectionY", "Calc", "max deflection Y per member", default=[])
		_addProp("App::PropertyFloatList", "MaxDeflectionZ", "Calc", "max deflection Z per member", default=[])

		# Thai Units Support (Legacy)
		_addProp("App::PropertyBool", "UseThaiUnits", "Thai Units", "enable Thai units for calculation results", default=False)
		_addProp("App::PropertyStringList", "MomentZKsc", "Thai Units", "per-member moment Z in ksc", default=[])
		_addProp("App::PropertyStringList", "MomentYKsc", "Thai Units", "per-member moment Y in ksc", default=[])
		_addProp("App::PropertyStringList", "AxialForceKgf", "Thai Units", "per-member axial force in kgf", default=[])
		_addProp("App::PropertyStringList", "AxialForceTf", "Thai Units", "per-member axial force in tf", default=[])
		_addProp("App::PropertyStringList", "ShearYKgf", "Thai Units", "per-member shear Y in kgf", default=[])
		_addProp("App::PropertyStringList", "ShearZKgf", "Thai Units", "per-member shear Z in kgf", default=[])
		
		# Global Units System (New Enhanced System)
		_addProp("App::PropertyEnumeration", "GlobalUnitsSystem", "Global Units", "global units system")
		# Set enum options for GlobalUnitsSystem immediately after creating the property
		if hasattr(obj, 'GlobalUnitsSystem'):
			obj.GlobalUnitsSystem = ["SI", "US", "THAI"]
			obj.GlobalUnitsSystem = "SI"  # Set default value after defining enum options
		_addProp("App::PropertyBool", "UseGlobalUnits", "Global Units", "enable global units system", default=True)
		_addProp("App::PropertyStringList", "FormattedForces", "Global Units", "formatted force results", default=[])
		_addProp("App::PropertyStringList", "FormattedStresses", "Global Units", "formatted stress results", default=[])
		_addProp("App::PropertyStringList", "FormattedMoments", "Global Units", "formatted moment results", default=[])
		# Load summary and metadata
		_addProp("App::PropertyStringList", "LoadSummary", "Calc", "summary of active loads", default=[])
		_addProp("App::PropertyInteger", "TotalLoads", "Calc", "total number of loads", default=0)
		_addProp("App::PropertyString", "AnalysisType", "Calc", "text description of analysis type", default='')
		
		# Reaction text display properties
		_addProp("App::PropertyBool", "ShowReactionText", "Reaction Display", "Show reaction values as text", default=False)
		_addProp("App::PropertyBool", "ShowReactionUnits", "Reaction Display", "Show units in reaction text", default=True)
		_addProp("App::PropertyInteger", "ReactionPrecision", "Reaction Display", "Decimal precision for reaction values", default=1)
		_addProp("App::PropertyFloat", "ReactionTextOffset", "Reaction Display", "Text offset distance from support node", default=500.0)
		_addProp("App::PropertyEnumeration", "ReactionTextOrientation", "Reaction Display", "Text orientation")
		_addProp("App::PropertyFloat", "ReactionFontSize", "Reaction Display", "Font size for reaction text", default=200.0)
		_addProp("App::PropertyColor", "ReactionTextColor", "Reaction Display", "Color for reaction text", default=(0.0, 0.0, 1.0, 0.0))
		
		# Set text orientation options
		obj.ReactionTextOrientation = ["Horizontal", "Vertical"]
		obj.ReactionTextOrientation = "Horizontal"
		
		# Reaction component selection
		_addProp("App::PropertyBool", "ShowReactionForces", "Reaction Components", "Show reaction forces (Fx, Fy, Fz)", default=True)
		_addProp("App::PropertyBool", "ShowReactionMoments", "Reaction Components", "Show reaction moments (Mx, My, Mz)", default=True)
		_addProp("App::PropertyBool", "ShowReactionResultant", "Reaction Components", "Show resultant reaction force", default=False)
		
		# Internal storage for reaction text shapes
		_addProp("App::PropertyPythonObject", "ReactionTextShapes", "Internal", "Storage for reaction text shapes", default=[])
		
		# Reaction values storage
		_addProp("App::PropertyStringList", "ReactionNodes", "Reactions", "List of node indices with reactions", default=[])
		_addProp("App::PropertyFloatList", "ReactionX", "Reactions", "Reaction forces in X direction", default=[])
		_addProp("App::PropertyFloatList", "ReactionY", "Reactions", "Reaction forces in Y direction", default=[])
		_addProp("App::PropertyFloatList", "ReactionZ", "Reactions", "Reaction forces in Z direction", default=[])
		_addProp("App::PropertyFloatList", "ReactionMX", "Reactions", "Reaction moments about X axis", default=[])
		_addProp("App::PropertyFloatList", "ReactionMY", "Reactions", "Reaction moments about Y axis", default=[])
		_addProp("App::PropertyFloatList", "ReactionMZ", "Reactions", "Reaction moments about Z axis", default=[])
		_addProp("App::PropertyString", "ReactionLoadCombo", "Reactions", "Current load combination for reactions", default="100_DL")
		
		# Self-weight consideration
		_addProp("App::PropertyBool", "selfWeight", "Analysis", "Consider self-weight of members", default=True)
		
		# Number of points for diagram discretization
		_addProp("App::PropertyInteger", "NumPointsMoment", "Diagram Points", "Number of points for moment diagram calculation", default=5)
		_addProp("App::PropertyInteger", "NumPointsAxial", "Diagram Points", "Number of points for axial force diagram calculation", default=3)
		_addProp("App::PropertyInteger", "NumPointsShear", "Diagram Points", "Number of points for shear force diagram calculation", default=4)
		_addProp("App::PropertyInteger", "NumPointsTorque", "Diagram Points", "Number of points for torque diagram calculation", default=3)
		_addProp("App::PropertyInteger", "NumPointsDeflection", "Diagram Points", "Number of points for deflection diagram calculation", default=4)


	#  Mapeia os nós da estrutura, (inverte o eixo y e z para adequação as coordenadas do sover)
	def mapNodes(self, elements, unitLength):	
		# Varre todos os elementos de linha e adiciona seus vertices à tabela de nodes
		listNodes = []
		for element in elements:
			for edge in element.Shape.Edges:
				for vertex in edge.Vertexes:
					node = [round(float(App.Units.Quantity(vertex.Point.x,'mm').getValueAs(unitLength)), 2), round(float(App.Units.Quantity(vertex.Point.z,'mm').getValueAs(unitLength)),2), round(float(App.Units.Quantity(vertex.Point.y,'mm').getValueAs(unitLength)),2)]
					if not node in listNodes:
						listNodes.append(node)

		return listNodes

	# Mapeia os membros da estrutura 
	def mapMembers(self, elements, listNodes, unitLength):
		listMembers = {}
		for element in elements:
			for i, edge in enumerate(element.Shape.Edges):
				listIndexVertex = []
				for vertex in edge.Vertexes:
					node = [round(float(App.Units.Quantity(vertex.Point.x,'mm').getValueAs(unitLength)), 2), round(float(App.Units.Quantity(vertex.Point.z,'mm').getValueAs(unitLength)),2), round(float(App.Units.Quantity(vertex.Point.y,'mm').getValueAs(unitLength)),2)]
					index = listNodes.index(node)
					listIndexVertex.append(index)

				# valida se o primeiro nó é mais auto do que o segundo nó, se sim inverte os nós do membro (necessário para manter os diagramas voltados para a posição correta)
				n1 = listIndexVertex[0]
				n2 = listIndexVertex[1]
				if listNodes[n1][1] > listNodes[n2][1]:
					aux = n1
					n1 = n2
					n2 = aux
				listMembers[element.Name + '_' + str(i)] = {
					'nodes': [str(n1), str(n2)],
					'material': element.MaterialMember.Name,
					'section': element.SectionMember.Name,
					'trussMember': element.TrussMember
					}
		
		return listMembers

	# Cria os nós no modelo do solver
	def setNodes(self, model, nodes_map):
		for i, node in enumerate(nodes_map):
			model.add_node(str(i), node[0], node[1], node[2])
		
		return model

	# Cria os membros no modelo do solver
	def setMembers(self, model, members_map, selfWeight=True):
		# First add all members to the model
		for memberName in list(members_map):  
			model.add_member(memberName, members_map[memberName]['nodes'][0], members_map[memberName]['nodes'][1], 
				members_map[memberName]['material'], members_map[memberName]['section'])
			
			# Apply truss member releases if needed
			if members_map[memberName]['trussMember']:
				model.def_releases(memberName, Dxi=False, Dyi=False, Dzi=False, Rxi=False, Ryi=True, Rzi=True, 
					Dxj=False, Dyj=False, Dzj=False, Rxj=False, Ryj=True, Rzj=True)
		
		# Apply self-weight after all members are added
		if selfWeight:
			try:
				_print_message("Adding self-weight to all members as distributed loads\n")
				
				# Apply self-weight as distributed loads for each member - γ · A
				for memberName in list(members_map):
					try:
						# Get member material and section
						material_name = members_map[memberName]['material']
						section_name = members_map[memberName]['section']
						
						# Get material density if available
						if material_name in model.materials:
							density = model.materials[material_name].rho
							
							# Get section area if available
							if section_name in model.sections:
								area = model.sections[section_name].A
								
								# Calculate distributed load (w = γ · A)
								line_load = density * area
								
								# Apply as distributed load in -Y direction (FY)
								if abs(line_load) > 1e-10:  # Only apply if non-zero
									_print_message(f"Member {memberName}: Applying self-weight of {line_load:.4f}\n")
									model.add_member_dist_load(memberName, 'FY', -line_load, -line_load, case='DL')
								else:
									_print_message(f"Member {memberName}: Self-weight calculation resulted in zero load\n")
									_print_message(f"  Density: {density}, Area: {area}\n")
					except Exception as e:
						_print_warning(f"Failed to apply self-weight to member {memberName}: {e}\n")
			except Exception as e:
				_print_warning(f"Failed to apply self-weight as distributed loads: {e}\n")
				_print_message("Falling back to built-in self-weight function\n")
				model.add_member_self_weight('FY', -1)
		
		return model

	# Get load factors based on load case or combination
	def getLoadFactors(self, load_case_or_combination, load_type):
		"""Returns load factor for given load case/combination and load type"""
		# Load combinations (Both Allowable stress design and Strength design)
		load_combinations = {
			# Allowable Stress Design (100 series)
			'100_DL': {'DL': 1.0, 'LL': 0.0, 'W': 0.0, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'101_DL+LL': {'DL': 1.0, 'LL': 1.0, 'W': 0.0, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'102_DL+0.75(LL+W(X+))': {'DL': 1.0, 'LL': 0.75, 'W': 0.75, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'103_DL+0.75(LL+W(x-))': {'DL': 1.0, 'LL': 0.75, 'W': 0.75, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'104_DL+0.75(LL+W(y+))': {'DL': 1.0, 'LL': 0.75, 'W': 0.75, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'105_DL+0.75(LL+W(y-))': {'DL': 1.0, 'LL': 0.75, 'W': 0.75, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'106_0.6DL+W(X+)': {'DL': 0.6, 'LL': 0.0, 'W': 1.0, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'107_0.6DL+W(x-)': {'DL': 0.6, 'LL': 0.0, 'W': 1.0, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'108_0.6DL+W(y+)': {'DL': 0.6, 'LL': 0.0, 'W': 1.0, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'109_0.6DL+W(y-)': {'DL': 0.6, 'LL': 0.0, 'W': 1.0, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'110_DL+0.7E(X+)': {'DL': 1.0, 'LL': 0.0, 'W': 0.0, 'E': 0.7, 'H': 0.0, 'F': 0.0},
			'111_DL+0.7E(x-)': {'DL': 1.0, 'LL': 0.0, 'W': 0.0, 'E': 0.7, 'H': 0.0, 'F': 0.0},
			'112_DL+0.7E(y+)': {'DL': 1.0, 'LL': 0.0, 'W': 0.0, 'E': 0.7, 'H': 0.0, 'F': 0.0},
			'113_DL+0.7E(y-)': {'DL': 1.0, 'LL': 0.0, 'W': 0.0, 'E': 0.7, 'H': 0.0, 'F': 0.0},
			'114_DL+0.525E(X+)+0.75LL': {'DL': 1.0, 'LL': 0.75, 'W': 0.0, 'E': 0.525, 'H': 0.0, 'F': 0.0},
			'115_DL+0.525E(x-)+0.75LL': {'DL': 1.0, 'LL': 0.75, 'W': 0.0, 'E': 0.525, 'H': 0.0, 'F': 0.0},
			'116_DL+0.525E(Z+)+0.75LL': {'DL': 1.0, 'LL': 0.75, 'W': 0.0, 'E': 0.525, 'H': 0.0, 'F': 0.0},
			'117_DL+0.525E(z-)+0.75LL': {'DL': 1.0, 'LL': 0.75, 'W': 0.0, 'E': 0.525, 'H': 0.0, 'F': 0.0},
			'118_0.6DL+0.7E(X+)': {'DL': 0.6, 'LL': 0.0, 'W': 0.0, 'E': 0.7, 'H': 0.0, 'F': 0.0},
			'119_0.6DL+0.7E(x-)': {'DL': 0.6, 'LL': 0.0, 'W': 0.0, 'E': 0.7, 'H': 0.0, 'F': 0.0},
			'120_0.6DL+0.7E(y+)': {'DL': 0.6, 'LL': 0.0, 'W': 0.0, 'E': 0.7, 'H': 0.0, 'F': 0.0},
			'121_0.6DL+0.7E(y-)': {'DL': 0.6, 'LL': 0.0, 'W': 0.0, 'E': 0.7, 'H': 0.0, 'F': 0.0},
			'122_DL+LL+H+F': {'DL': 1.0, 'LL': 1.0, 'W': 0.0, 'E': 0.0, 'H': 1.0, 'F': 1.0},
			# Strength Design (1000 series)
			'1000_1.4DL': {'DL': 1.4, 'LL': 0.0, 'W': 0.0, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'1001_1.4DL+1.7LL': {'DL': 1.4, 'LL': 1.7, 'W': 0.0, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'1002_1.05DL+1.275LL+1.6W(x+)': {'DL': 1.05, 'LL': 1.275, 'W': 1.6, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'1003_1.05DL+1.275LL+1.6W(x-)': {'DL': 1.05, 'LL': 1.275, 'W': 1.6, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'1004_1.05DL+1.275LL+1.6W(y+)': {'DL': 1.05, 'LL': 1.275, 'W': 1.6, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'1005_1.05DL+1.275LL+1.6W(y-)': {'DL': 1.05, 'LL': 1.275, 'W': 1.6, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'1006_0.9DL+1.6W(X+)': {'DL': 0.9, 'LL': 0.0, 'W': 1.6, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'1007_0.9DL+1.6W(x-)': {'DL': 0.9, 'LL': 0.0, 'W': 1.6, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'1008_0.9DL+1.6W(y+)': {'DL': 0.9, 'LL': 0.0, 'W': 1.6, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'1009_0.9DL+1.6W(y-)': {'DL': 0.9, 'LL': 0.0, 'W': 1.6, 'E': 0.0, 'H': 0.0, 'F': 0.0},
			'1010_1.05DL+1.275LL+E(x+)': {'DL': 1.05, 'LL': 1.275, 'W': 0.0, 'E': 1.0, 'H': 0.0, 'F': 0.0},
			'1011_1.05DL+1.275LL+E(x-)': {'DL': 1.05, 'LL': 1.275, 'W': 0.0, 'E': 1.0, 'H': 0.0, 'F': 0.0},
			'1012_1.05DL+1.275LL+E(y+)': {'DL': 1.05, 'LL': 1.275, 'W': 0.0, 'E': 1.0, 'H': 0.0, 'F': 0.0},
			'1013_1.05DL+1.275LL+E(y-)': {'DL': 1.05, 'LL': 1.275, 'W': 0.0, 'E': 1.0, 'H': 0.0, 'F': 0.0},
			'1014_0.9DL+E(X+)': {'DL': 0.9, 'LL': 0.0, 'W': 0.0, 'E': 1.0, 'H': 0.0, 'F': 0.0},
			'1015_0.9DL+E(x-)': {'DL': 0.9, 'LL': 0.0, 'W': 0.0, 'E': 1.0, 'H': 0.0, 'F': 0.0},
			'1016_0.9DL+E(y+)': {'DL': 0.9, 'LL': 0.0, 'W': 0.0, 'E': 1.0, 'H': 0.0, 'F': 0.0},
			'1017_0.9DL+E(y-)': {'DL': 0.9, 'LL': 0.0, 'W': 0.0, 'E': 1.0, 'H': 0.0, 'F': 0.0},
			'1018_1.4DL+1.7LL+1.7H': {'DL': 1.4, 'LL': 1.7, 'W': 0.0, 'E': 0.0, 'H': 1.7, 'F': 0.0},
			'1019_0.9DL+1.7H': {'DL': 0.9, 'LL': 0.0, 'W': 0.0, 'E': 0.0, 'H': 1.7, 'F': 0.0},
			'1020_1.4DL+1.7LL+1.4F': {'DL': 1.4, 'LL': 1.7, 'W': 0.0, 'E': 0.0, 'H': 0.0, 'F': 1.4},
			'1021_0.9DL+1.4F': {'DL': 0.9, 'LL': 0.0, 'W': 0.0, 'E': 0.0, 'H': 0.0, 'F': 1.4}
		}
		
		# Return load factor
		if load_case_or_combination in load_combinations:
			return load_combinations[load_case_or_combination].get(load_type, 0.0)
		else:
			return 1.0  # Default factor

	# Organize loads by type and check compatibility with selected load combination
	def organizeLoadsByType(self, loads, load_combination):
		"""Organizes loads by type and validates compatibility with load case"""
		load_types = {'DL': [], 'LL': [], 'H': [], 'F': [], 'W': [], 'E': [], 'FACTOR': []}
		
		for load in loads:
			load_type = getattr(load, 'LoadType', 'DL')
			if load_type in load_types:
				load_types[load_type].append(load)
				
		# Check if the selected load combination requires load types that are not present
		# This line was incorrect - it's not needed and was causing confusion
		# required_factors = self.getLoadFactors(load_combination, 'DL')  # Get all factors for this combination
		
		return load_types

	# Check wind/earthquake direction compatibility
	def checkDirectionCompatibility(self, load_combination, load_direction):
		"""Check if load direction is compatible with load combination direction requirements"""
		direction_mapping = {
			'+X': ['X+', 'x+'], '-X': ['X-', 'x-'],
			'+Y': ['Y+', 'y+'], '-Y': ['Y-', 'y-'],
			'+Z': ['Z+', 'z+'], '-Z': ['Z-', 'z-']
		}
		
		# Extract direction from load combination name if it contains directional info
		for direction, patterns in direction_mapping.items():
			for pattern in patterns:
				if pattern in load_combination:
					return direction == load_direction
					
		return True  # No specific direction requirement

	# Cria os carregamentos
	def setLoads(self, model, loads, nodes_map, unitForce, unitLength, load_combination):
		for load in loads:
			# Check if load has LoadType property, if not default to 'DL'
			load_type = getattr(load, 'LoadType', 'DL')
			
			# Don't apply load factors here - let Pynite handle them via load combinations
			# Just use factor 1.0 for all loads and specify the load case
			load_factor = 1.0

			if load.GlobalDirection == '+X':
				axis = 'FX'
				direction = 1

			elif load.GlobalDirection == '-X':
				axis = 'FX'
				direction = -1

			elif load.GlobalDirection == '+Y':
				axis = 'FZ'
				direction = 1

			elif load.GlobalDirection == '-Y':
				axis = 'FZ'
				direction = -1

			elif load.GlobalDirection == '+Z':
				axis = 'FY'
				direction = 1

			elif load.GlobalDirection == '-Z':
				axis = 'FY'
				direction = -1

			else:
				# Default case to prevent unbound variables
				axis = 'FX'
				direction = 1

			# Check direction compatibility for wind and earthquake loads
			if load_type in ['W', 'E']:
				if not self.checkDirectionCompatibility(load_combination, load.GlobalDirection):
					continue  # Skip loads that don't match the required direction
			
			# Valida se o carregamento é distribuido
			if 'Edge' in load.ObjectBase[0][1][0]:
				initial = float(load.InitialLoading.getValueAs(unitForce))
				final = float(load.FinalLoading.getValueAs(unitForce))

				# Apply load factor based on load combination and load type
				factored_initial = initial * direction * load_factor
				factored_final = final * direction * load_factor
				
				subname = int(load.ObjectBase[0][1][0].split('Edge')[1]) - 1
				name = load.ObjectBase[0][0].Name + '_' + str(subname)
				model.add_member_dist_load(name, axis, factored_initial, factored_final, case=load_type)

			# Valida se o carregamento é nodal
			elif 'Vertex' in load.ObjectBase[0][1][0]:
				numVertex = int(load.ObjectBase[0][1][0].split('Vertex')[1]) - 1
				vertex = load.ObjectBase[0][0].Shape.Vertexes[numVertex]
				
				node = list(filter(lambda element: element == [round(float(App.Units.Quantity(vertex.Point.x,'mm').getValueAs(unitLength)), 2), round(float(App.Units.Quantity(vertex.Point.z,'mm').getValueAs(unitLength)),2), round(float(App.Units.Quantity(vertex.Point.y,'mm').getValueAs(unitLength)),2)], nodes_map))[0]
				indexNode = nodes_map.index(node)

				# Apply load factor based on load combination and load type
				factored_load = float(load.NodalLoading.getValueAs(unitForce)) * direction * load_factor
				
				name = str(indexNode)
				model.add_node_load(name, axis, factored_load, case=load_type)
			

					
		return model

	# Cria os suportes
	def setSuports(self, model, suports, nodes_map, unitLength):
		support_count = 0
		
		_print_message(f"Applying {len(suports)} support conditions\n")
		
		for suport in suports:
			try:
				suportvertex = list(suport.ObjectBase[0][0].Shape.Vertexes[int(suport.ObjectBase[0][1][0].split('Vertex')[1])-1].Point)
				support_found = False
				
				for i, node in enumerate(nodes_map):
					if (round(float(App.Units.Quantity(suportvertex[0],'mm').getValueAs(unitLength)),2) == round(node[0],2) and 
						round(float(App.Units.Quantity(suportvertex[1],'mm').getValueAs(unitLength)),2) == round(node[2],2) and 
						round(float(App.Units.Quantity(suportvertex[2],'mm').getValueAs(unitLength)),2) == round(node[1],2)):
						
						name = str(i)
						_print_message(f"Applying support at node {name} with coordinates ({node[0]:.2f}, {node[1]:.2f}, {node[2]:.2f})\n")
						_print_message(f"  Support conditions: X={suport.FixTranslationX}, Y={suport.FixTranslationZ}, Z={suport.FixTranslationY}, ")
						_print_message(f"RX={suport.FixRotationX}, RY={suport.FixRotationZ}, RZ={suport.FixRotationY}\n")
						
						model.def_support(name, 
							suport.FixTranslationX, 
							suport.FixTranslationZ, 
							suport.FixTranslationY, 
							suport.FixRotationX, 
							suport.FixRotationZ, 
							suport.FixRotationY)
						
						support_count += 1
						support_found = True
						break
				
				if not support_found:
					_print_warning(f"Could not find a node matching support location for {suport.Label}\n")
					_print_warning(f"  Support vertex coordinates: {suportvertex}\n")
			
			except Exception as e:
				_print_warning(f"Failed to apply support {suport.Label}: {e}\n")
		
		_print_message(f"Applied {support_count} out of {len(suports)} support conditions\n")
		return model

	def setMaterialAndSections(self, model, lines, unitLength, unitForce):
		materiais = []
		sections = []
		for line in lines:
			material = line.MaterialMember
			section = line.SectionMember

			if not material.Name in materiais:
				# Try to get calc properties from material object first (supports both old and new materials)
				if hasattr(material, 'Proxy') and hasattr(material.Proxy, 'get_calc_properties'):
					# New StructuralMaterial or updated old Material with get_calc_properties method
					try:
						mat_props = material.Proxy.get_calc_properties(material, unitLength, unitForce)
						model.add_material(mat_props['name'], mat_props['E'], mat_props['G'], mat_props['nu'], mat_props['density'])
						materiais.append(material.Name)
						continue
					except Exception as e:
						App.Console.PrintWarning(f"Error using material calc properties for {material.Name}: {e}\n")
				
				# Fallback to original method for compatibility
				try:
					density = App.Units.Quantity(material.Density).getValueAs('t/m^3') * 10 #Converte a unidade de entrada em t/m³ e na sequencia converte em kN/m³
					density = float(App.Units.Quantity(density, 'kN/m^3').getValueAs(unitForce+"/"+unitLength+"^3")) #Converte kN/m³ para as unidades definidas no calc
					modulusElasticity = float(material.ModulusElasticity.getValueAs(unitForce+"/"+unitLength+"^2"))
					poissonRatio = float(material.PoissonRatio)
					G = modulusElasticity / (2 * (1 + poissonRatio))
					model.add_material(material.Name, modulusElasticity, G, poissonRatio, density)
					materiais.append(material.Name)
				except Exception as e:
					App.Console.PrintError(f"Error processing material {material.Name}: {e}\n")
					# Add default material as fallback
					model.add_material(material.Name, 200000.0, 77000.0, 0.3, 78.5)
					materiais.append(material.Name)
				

			if not section.Name in sections:

				ang = line.RotationSection.getValueAs('rad')
				J  = float(App.Units.Quantity(section.MomentInertiaPolar, 'mm^4').getValueAs(unitLength+"^4"))
				A  = float(section.AreaSection.getValueAs(unitLength+"^2"))
				Iy = float(App.Units.Quantity(section.MomentInertiaY, 'mm^4').getValueAs(unitLength+"^4"))
				Iz = float(App.Units.Quantity(section.MomentInertiaZ, 'mm^4').getValueAs(unitLength+"^4"))
				Iyz = float(App.Units.Quantity(section.ProductInertiaYZ, 'mm^4').getValueAs(unitLength+"^4"))

				
				# Aplica a rotação de eixo
				RIy = ((Iz + Iy) / 2 ) - ((Iz - Iy) / 2 )*math.cos(2 * ang) + Iyz * math.sin(2 * ang)
				RIz = ((Iz + Iy) / 2 ) + ((Iz - Iy) / 2 )*math.cos(2 * ang) - Iyz * math.sin(2 * ang)
				
				model.add_section(section.Name, A, RIy, RIz, J)
				sections.append(section.Name)
		
		return model

	
	def execute(self, obj):
		model = FEModel3D()
		# Initialize materials list to track processed materials
		materiais = []
		
		# Ensure there's a default material so meshed quads can be assigned a material name
		# Tests and minimal workflows may not define materials; create a light default.
		try:
			if 'default' not in model.materials:
				# Try to use ASTM A992 from database as default
				if HAS_MATERIAL_DATABASE and 'ASTM_A992' in MATERIAL_STANDARDS:
					props = get_material_info('ASTM_A992')
					E = float(props.get('ModulusElasticity', '200000 MPa').replace(' MPa', ''))
					nu = props.get('PoissonRatio', 0.3)
					G = E / (2 * (1 + nu))
					density_kg_m3 = float(props.get('Density', '7850 kg/m^3').replace(' kg/m^3', ''))
					density = density_kg_m3 * 9.81 / 1000  # Convert to kN/m³
					model.add_material('default', E, G, nu, density)
					_print_message(f"Using ASTM A992 as default material from database\n")
				else:
					# Fallback to hardcoded values
					model.add_material('default', 200000.0, 77000.0, 0.3, 78.5)
		except Exception as e:
			# Non-fatal if FEModel internals differ; proceed without failing
			_print_warning(f"Could not create default material: {e}\n")
		# Filtra os diferentes tipos de elementos
		lines = list(filter(lambda element: 'Line' in element.Name or 'Wire' in element.Name, obj.ListElements))
		loads = list(filter(lambda element: 'Load' in element.Name, obj.ListElements))
		suports = list(filter(lambda element: 'Suport' in element.Name, obj.ListElements))
		# Collect plate and area-load objects (StructuralPlate and AreaLoad)
		plates = list(filter(lambda element: getattr(element, 'Type', '') == 'StructuralPlate' or 'Plate' in element.Name, obj.ListElements))
		area_loads = list(filter(lambda element: getattr(element, 'Type', '') == 'AreaLoad' or 'AreaLoad' in element.Name, obj.ListElements))

		# Map nodes and members
		nodes_map = self.mapNodes(lines, obj.LengthUnit)
		members_map = self.mapMembers(lines, nodes_map, obj.LengthUnit)

		# Set up materials, nodes, and members
		model = self.setMaterialAndSections(model, lines, obj.LengthUnit, obj.ForceUnit)
		model = self.setNodes(model, nodes_map)
		
		# Handle self-weight setting with backwards compatibility
		use_self_weight = True  # Default to True
		if hasattr(obj, 'selfWeight'):
			use_self_weight = obj.selfWeight
		model = self.setMembers(model, members_map, use_self_weight)

		# ---- New: map plates (StructuralPlate objects) into the FE model ----
		# For each StructuralPlate, attempt to find four corner nodes in nodes_map and add a Plate element to the model.
		for plate_obj in plates:
			# Try to get corner vertices from the object's Shape (if available) or use a property named CornerNodes
			try:
				shape = plate_obj.Shape
			except Exception:
				shape = None

			# Determine corner node indices (best-effort). If CornerNodes property exists and matches nodes_map, prefer it.
			corner_indices = None
			if hasattr(plate_obj, 'CornerNodes') and plate_obj.CornerNodes:
				# CornerNodes expected as list of FreeCAD.Vector or similar
				try:
					corner_points = [App.Vector(v) if not isinstance(v, App.Vector) else v for v in plate_obj.CornerNodes]
				except Exception:
					corner_points = []
				if corner_points and len(corner_points) >= 4:
					corner_indices = []
					for pt in corner_points[:4]:
						node = [round(qty_val(pt.x, 'mm', obj.LengthUnit), 2), round(qty_val(pt.z, 'mm', obj.LengthUnit), 2), round(qty_val(pt.y, 'mm', obj.LengthUnit), 2)]
						if node in nodes_map:
							corner_indices.append(nodes_map.index(node))

			# Fallback: try to use the first Face's Vertexes
			if corner_indices is None or len(corner_indices) < 4:
				if shape and hasattr(shape, 'Faces') and len(shape.Faces) > 0:
					face = shape.Faces[0]
					verts = list(face.Vertexes)
					if len(verts) >= 4:
						corner_indices = []
						for v in verts[:4]:
							node = [round(qty_val(v.Point.x, 'mm', obj.LengthUnit), 2), round(qty_val(v.Point.z, 'mm', obj.LengthUnit), 2), round(qty_val(v.Point.y, 'mm', obj.LengthUnit), 2)]
							if node in nodes_map:
								corner_indices.append(nodes_map.index(node))

			# If user requested a mesh (MeshDensity property) use PlateMesher to create elements
			use_mesh = hasattr(plate_obj, 'MeshDensity') and getattr(plate_obj, 'MeshDensity')
			if use_mesh:
				# Prefer module-level PlateMesher (test can monkeypatch `calc.PlateMesher`).
				_PlateMesher = PlateMesher
				if _PlateMesher is None:
					# Try importing as a last resort
					try:
						from .meshing.PlateMesher import PlateMesher as _PlateMesher
					except Exception as e:
						_print_warning(f"PlateMesher import failed for plate '{plate_obj.Name}': {e}\n")
						_PlateMesher = None
				if _PlateMesher is None:
					mesh_data = None
				else:
					mesher = _PlateMesher()
					# Determine target mesh size: prefer plate property, then mesher default if present
					plate_mesh_density = getattr(plate_obj, 'MeshDensity', None)
					if plate_mesh_density is None:
						mesher_default = getattr(mesher, 'target_size', 100.0)
						mesh_kwargs = {'target_size': float(mesher_default)}
					else:
						mesh_kwargs = {'target_size': float(plate_mesh_density)}
					mesh_data = None
					if shape and hasattr(shape, 'Faces') and len(shape.Faces) > 0:
						try:
							mesh_data = mesher.meshFace(shape.Faces[0], **mesh_kwargs)
						except Exception as e:
							_print_warning(f"PlateMesher.meshFace failed for plate '{plate_obj.Name}': {e}\n")
					if mesh_data and 'nodes' in mesh_data and 'elements' in mesh_data:
						# map mesh nodes to model nodes (try to reuse existing nodes_map first)
						node_id_map = {}
						for tag, coord in mesh_data['nodes'].items():
							x = float(coord.get('x', 0))
							y = float(coord.get('y', 0))
							z = float(coord.get('z', 0))
							# try to match against existing nodes_map using same rounding rule
							coord_rounded = [round(x, 2), round(z, 2), round(y, 2)]
							match_idx = _find_matching_node_index(nodes_map, coord_rounded, tol=1e-2)
							if match_idx is not None:
								# reuse existing node name (setNodes used str(index))
								node_name = str(match_idx)
								node_id_map[tag] = node_name
								continue
							# otherwise add a new node to the model
							try:
								node_name = model.add_node(None, x, y, z)
								node_id_map[tag] = node_name
							except Exception as e:
								_print_warning(f"Could not add mesh node {tag}: {e}\n")
						# add elements (support quads and fallback triangle handling)
						created_elems = []
						for elem_id, elem in mesh_data['elements'].items():
							nodes = elem.get('nodes', [])
							if len(nodes) < 3:
								_print_warning(f"Mesh element {elem_id} has insufficient nodes; skipping\n")
								continue
							# If triangle, duplicate last node to create a degenerate quad (placeholder)
							if len(nodes) == 3:
								nodes = nodes + [nodes[2]]
							# Lookup mapped node names
							i_n = node_id_map.get(nodes[0])
							j_n = node_id_map.get(nodes[1])
							m_n = node_id_map.get(nodes[2])
							n_n = node_id_map.get(nodes[3])
							if None in (i_n, j_n, m_n, n_n):
								_print_warning(f"Mesh element {elem_id} references unknown nodes; skipping\n")
								continue
							# thickness conversion with fallback
							thk = getattr(plate_obj, 'Thickness', 0.1)
							try:
								thk = qty_val(thk, 'mm', obj.LengthUnit)
							except Exception:
								try:
									thk = float(thk)
								except Exception:
									thk = 0.1
							# Get material name and ensure material is added to model
							mat_obj = getattr(plate_obj, 'Material', None)
							if mat_obj and hasattr(mat_obj, 'Name'):
								mat_name = mat_obj.Name
								# Ensure plate material is added to FE model
								if mat_name not in materiais:
									if hasattr(mat_obj, 'Proxy') and hasattr(mat_obj.Proxy, 'get_calc_properties'):
										try:
											mat_props = mat_obj.Proxy.get_calc_properties(mat_obj, obj.LengthUnit, obj.ForceUnit)
											model.add_material(mat_props['name'], mat_props['E'], mat_props['G'], mat_props['nu'], mat_props['density'])
											materiais.append(mat_name)
										except Exception:
											model.add_material(mat_name, 200000.0, 77000.0, 0.3, 78.5)
											materiais.append(mat_name)
									else:
										try:
											density = App.Units.Quantity(mat_obj.Density).getValueAs('t/m^3') * 10
											density = float(App.Units.Quantity(density, 'kN/m^3').getValueAs(obj.ForceUnit+"/"+obj.LengthUnit+"^3"))
											E = float(mat_obj.ModulusElasticity.getValueAs(obj.ForceUnit+"/"+obj.LengthUnit+"^2"))
											nu = float(mat_obj.PoissonRatio)
											G = E / (2 * (1 + nu))
											model.add_material(mat_name, E, G, nu, density)
											materiais.append(mat_name)
										except Exception:
											model.add_material(mat_name, 200000.0, 77000.0, 0.3, 78.5)
											materiais.append(mat_name)
							else:
								mat_name = 'default'
							# Create a stable element name linked to the plate
							elem_name = f"{plate_obj.Name}_{elem_id}"
							try:
								model.add_quad(elem_name, i_n, j_n, m_n, n_n, float(thk), mat_name)
								created_elems.append(elem_name)
							except Exception as e:
								_print_warning(f"Could not add mesh element {elem_id}: {e}\n")
						# record created element names so area loads can be mapped later
						if created_elems:
							if not hasattr(self, '_plate_mesh_elements'):
								self._plate_mesh_elements = {}
							self._plate_mesh_elements[plate_obj.Name] = created_elems
					else:
						_print_warning(f"PlateMesher: failed to create mesh for plate '{plate_obj.Name}'\n")
			else:
				# If no mesh requested and we have 4 corner node indices, add a plate to the FE model
				if corner_indices and len(corner_indices) >= 4:
					# convert to string node names used by model (setNodes used str(i) indices)
					i_name = str(corner_indices[0])
					j_name = str(corner_indices[1])
					m_name = str(corner_indices[2])
					n_name = str(corner_indices[3])
					# thickness and material
					thk = getattr(plate_obj, 'Thickness', 0.1)
					mat_obj = getattr(plate_obj, 'Material', None)
					if mat_obj and hasattr(mat_obj, 'Name'):
						mat_name = mat_obj.Name
						# Ensure plate material is added to FE model
						if mat_name not in materiais:
							if hasattr(mat_obj, 'Proxy') and hasattr(mat_obj.Proxy, 'get_calc_properties'):
								try:
									mat_props = mat_obj.Proxy.get_calc_properties(mat_obj, obj.LengthUnit, obj.ForceUnit)
									model.add_material(mat_props['name'], mat_props['E'], mat_props['G'], mat_props['nu'], mat_props['density'])
									materiais.append(mat_name)
								except Exception:
									model.add_material(mat_name, 200000.0, 77000.0, 0.3, 78.5)
									materiais.append(mat_name)
							else:
								try:
									density = App.Units.Quantity(mat_obj.Density).getValueAs('t/m^3') * 10
									density = float(App.Units.Quantity(density, 'kN/m^3').getValueAs(obj.ForceUnit+"/"+obj.LengthUnit+"^3"))
									E = float(mat_obj.ModulusElasticity.getValueAs(obj.ForceUnit+"/"+obj.LengthUnit+"^2"))
									nu = float(mat_obj.PoissonRatio)
									G = E / (2 * (1 + nu))
									model.add_material(mat_name, E, G, nu, density)
									materiais.append(mat_name)
								except Exception:
									model.add_material(mat_name, 200000.0, 77000.0, 0.3, 78.5)
									materiais.append(mat_name)
					else:
						mat_name = 'default'
					try:
						model.add_plate(plate_obj.Name, i_name, j_name, m_name, n_name, float(thk), mat_name)
					except Exception as e:
						_print_warning(f"Could not add plate '{plate_obj.Name}' to model: {e}\n")

		# ---- New: map area loads to plates (best-effort by geometric containment or explicit target) ----
		for aload in area_loads:
			# If AreaLoad has TargetFaces or similar pointing to a plate_obj, use that
			targets = []
			if hasattr(aload, 'TargetFaces') and aload.TargetFaces:
				for t in aload.TargetFaces:
					if getattr(t, 'Type', '') == 'StructuralPlate' or 'Plate' in getattr(t, 'Name', ''):
						targets.append(t)
			# Else try to use the Parent/linked object
			elif hasattr(aload, 'ObjectBase') and aload.ObjectBase:
				try:
					parent = aload.ObjectBase[0][0]
					if getattr(parent, 'Type', '') == 'StructuralPlate' or 'Plate' in getattr(parent, 'Name', ''):
						targets.append(parent)
				except Exception:
					pass

			# Determine pressure magnitude (in force per area units) - assume Magnitude property
			pressure_value = None
			if hasattr(aload, 'Magnitude'):
				try:
					# Try to convert FreeCAD.Quantity to model units
					pressure_value = qty_val(aload.Magnitude, 'N/m^2', obj.ForceUnit + '/' + obj.LengthUnit + '^2')
				except Exception:
					try:
						pressure_value = float(aload.Magnitude)
					except Exception:
						pressure_value = None

			for tgt in targets:
				# try to find the plate we added by name
				plate_name = getattr(tgt, 'Name', None)
				# Map to rectangular plates
				if plate_name and plate_name in model.plates and pressure_value is not None:
					try:
						model.add_plate_surface_pressure(plate_name, pressure_value, case='Case 1')
					except Exception as e:
							_print_warning(f"Could not map AreaLoad '{aload.Name}' to plate '{plate_name}': {e}\n")
				# Map to meshed quads created for this plate (if any)
				if hasattr(self, '_plate_mesh_elements') and plate_name in getattr(self, '_plate_mesh_elements', {}):
					for qname in self._plate_mesh_elements.get(plate_name, []):
						if qname in model.quads and pressure_value is not None:
							try:
								model.add_quad_surface_pressure(qname, pressure_value, case='Case 1')
							except Exception as e:
								_print_warning(f"Could not map AreaLoad '{aload.Name}' to quad '{qname}': {e}\n")

		
		# Use the selected load combination
		active_load_combination = obj.LoadCombination if hasattr(obj, 'LoadCombination') else '100_DL'
		_print_message(f"Starting analysis with LoadCombination: {active_load_combination}\n")
		
		# Filter and organize loads by type for current load combination
		organized_loads = self.organizeLoadsByType(loads, active_load_combination)
		
		# Load ALL loads regardless of combination - Pynite will handle factors via combinations
		# We now load all loads with their LoadType as case names
		model = self.setLoads(model, loads, nodes_map, obj.ForceUnit, obj.LengthUnit, active_load_combination)
		model = self.setSuports(model, suports, nodes_map, obj.LengthUnit)

		# Create individual load cases and combinations for Pynite
		load_factors = {}
		for load_type in ['DL', 'LL', 'W', 'E', 'H', 'F']:
			factor = self.getLoadFactors(active_load_combination, load_type)
			if factor != 0.0:
				load_factors[load_type] = factor
		
		# Clear existing load combinations and add the current one
		model.load_combos.clear()
		
		# Create load combination with proper factors for each load type
		# Now loads are loaded with factor 1.0, so Pynite will apply the factors
		model.add_load_combo(active_load_combination, load_factors)
		
		_print_message(f"Added load combination '{active_load_combination}' with factors: {load_factors}\n")
		_print_message(f"Model now has load combinations: {list(model.load_combos.keys())}\n")
		
		# Debug: Show available load cases in model
		if hasattr(model, 'load_cases'):
			load_cases = model.load_cases
			_print_message(f"Available load cases in model: {load_cases}\n")
		else:
			_print_message("No load_cases property found in model\n")

		# Run analysis but don't let exceptions abort headless tests; capture and warn instead
		try:
			_print_message("Starting structural analysis...\n")
			
			# Check that we have necessary components for analysis
			if not model.nodes:
				_print_warning("No nodes defined in model! Analysis cannot proceed.\n")
				return
			
			if not model.members:
				_print_warning("No members defined in model! Analysis cannot proceed.\n")
				return
			
			# Check if we have any supports defined
			support_count = 0
			for node_name, node in model.nodes.items():
				if (node.support_DX or node.support_DY or node.support_DZ or
					node.support_RX or node.support_RY or node.support_RZ):
					support_count += 1
			
			if support_count == 0:
				_print_warning("No supports defined in model! Analysis cannot proceed.\n")
				return
			
			_print_message(f"Model ready for analysis with {len(model.nodes)} nodes, {len(model.members)} members, and {support_count} supports.\n")
			
			# Run analysis with verification
			model.analyze()
			
			# Verify analysis ran successfully by checking if reaction attributes exist
			supported_node = None
			for node_name, node in model.nodes.items():
				if (node.support_DX or node.support_DY or node.support_DZ or
					node.support_RX or node.support_RY or node.support_RZ):
					supported_node = node
					break
					
			if supported_node:
				if not hasattr(supported_node, 'RxnFX'):
					_print_warning("Analysis completed but reaction attributes not created! Check model setup.\n")
				else:
					_print_message("Analysis completed successfully with reaction attributes.\n")
			
			# Print magnitudes of self-weight loads for debugging
			self_weight_total = 0
			for member_name, member in model.members.items():
				# PhysMember contains sub_members, need to access through them
				if hasattr(member, 'sub_members'):
					for sub_member in member.sub_members.values():
						if hasattr(sub_member, 'distributed_loads'):
							for load_case, loads in sub_member.distributed_loads.items():
								for load in loads:
									if load[0] == 'FY':
										load_w1 = load[1]
										load_w2 = load[2]
										avg_load = (abs(load_w1) + abs(load_w2)) / 2
										self_weight_total += avg_load
			
			_print_message(f"Total self-weight load magnitude: {self_weight_total:.4f}\n")
			
			# Debug: Check if analysis results exist for the selected combination
			if model.members:
				first_member = list(model.members.values())[0]
				if hasattr(first_member, 'moment_array'):
					try:
						test_result = first_member.moment_array('My', 2, combo_name=active_load_combination)
						_print_message(f"Analysis successful - test moment result for first member: {test_result[1][0]:.6f}\n")
					except Exception as test_e:
						_print_warning(f"Could not get results for combo '{active_load_combination}': {test_e}\n")
			
		except Exception as e:
			_print_warning(f"Model analysis failed (continuing): {str(e)}\n")
			# Print stack trace for better debugging
			import traceback
			_print_warning(f"Stack trace:\n{traceback.format_exc()}\n")

		# Update analysis summary
		analysis_type = "Allowable Stress Design" if active_load_combination.startswith('1') and not active_load_combination.startswith('10') else "Strength Design" if active_load_combination.startswith('10') else "Allowable Stress Design"
		obj.AnalysisType = f"{analysis_type}: {active_load_combination}"
		
		# Create load summary
		load_summary = []
		total_loads = 0
		for load in loads:  # Use all loads for summary
			load_type = getattr(load, 'LoadType', 'DL')
			load_factor = self.getLoadFactors(active_load_combination, load_type)
			load_summary.append(f"{load_type} (Factor: {load_factor}) - {load.Label}")
			total_loads += 1
				
		obj.LoadSummary = load_summary
		obj.TotalLoads = total_loads

		# Extract reaction forces and moments
		reaction_nodes = []
		reaction_x = []
		reaction_y = []
		reaction_z = []
		reaction_mx = []
		reaction_my = []
		reaction_mz = []

		# Set current load combination for reactions
		if hasattr(obj, 'ReactionLoadCombo'):
			obj.ReactionLoadCombo = active_load_combination

		# Find all supported nodes and collect their reactions
		_print_message(f"Collecting reactions for load combination: {active_load_combination}\n")
		
		# Count total supported nodes
		support_node_count = 0
		for node_name, node in model.nodes.items():
			if (hasattr(node, 'support_DX') and node.support_DX) or \
			   (hasattr(node, 'support_DY') and node.support_DY) or \
			   (hasattr(node, 'support_DZ') and node.support_DZ) or \
			   (hasattr(node, 'support_RX') and node.support_RX) or \
			   (hasattr(node, 'support_RY') and node.support_RY) or \
			   (hasattr(node, 'support_RZ') and node.support_RZ):
				support_node_count += 1
		
		_print_message(f"Found {support_node_count} supported nodes\n")
		
		# Check if reaction attributes are created
		reaction_attrs_exist = False
		for node_name, node in model.nodes.items():
			if hasattr(node, 'RxnFX'):
				reaction_attrs_exist = True
				break
		
		if not reaction_attrs_exist:
			_print_warning("No reaction attributes found in any nodes! Make sure analysis was successful.\n")
		
		# Sum of all reactions for validation
		total_fx = 0.0
		total_fy = 0.0
		total_fz = 0.0
		
		for node_name, node in model.nodes.items():
			is_supported = False
			
			# Check each support direction
			support_conditions = []
			if hasattr(node, 'support_DX') and node.support_DX:
				is_supported = True
				support_conditions.append('DX')
			if hasattr(node, 'support_DY') and node.support_DY:
				is_supported = True
				support_conditions.append('DY')
			if hasattr(node, 'support_DZ') and node.support_DZ:
				is_supported = True
				support_conditions.append('DZ')
			if hasattr(node, 'support_RX') and node.support_RX:
				is_supported = True
				support_conditions.append('RX')
			if hasattr(node, 'support_RY') and node.support_RY:
				is_supported = True
				support_conditions.append('RY')
			if hasattr(node, 'support_RZ') and node.support_RZ:
				is_supported = True
				support_conditions.append('RZ')

			if is_supported:
				# Add node to reaction list
				reaction_nodes.append(node_name)
				
				# Get reaction forces (default to 0.0 if not present)
				fx = node.RxnFX.get(active_load_combination, 0.0) if hasattr(node, 'RxnFX') and active_load_combination in node.RxnFX else 0.0
				fy = node.RxnFY.get(active_load_combination, 0.0) if hasattr(node, 'RxnFY') and active_load_combination in node.RxnFY else 0.0
				fz = node.RxnFZ.get(active_load_combination, 0.0) if hasattr(node, 'RxnFZ') and active_load_combination in node.RxnFZ else 0.0
				
				# Get reaction moments (default to 0.0 if not present)
				mx = node.RxnMX.get(active_load_combination, 0.0) if hasattr(node, 'RxnMX') and active_load_combination in node.RxnMX else 0.0
				my = node.RxnMY.get(active_load_combination, 0.0) if hasattr(node, 'RxnMY') and active_load_combination in node.RxnMY else 0.0
				mz = node.RxnMZ.get(active_load_combination, 0.0) if hasattr(node, 'RxnMZ') and active_load_combination in node.RxnMZ else 0.0
				
				# Accumulate totals for validation
				total_fx += fx
				total_fy += fy
				total_fz += fz
				
				# Print diagnostic information
				_print_message(f"Node {node_name} reactions: FX={fx:.3f}, FY={fy:.3f}, FZ={fz:.3f}, MX={mx:.3f}, MY={my:.3f}, MZ={mz:.3f}\n")
				_print_message(f"  Support conditions: {', '.join(support_conditions)}\n")
				_print_message(f"  Node coordinates: ({node.X:.3f}, {node.Y:.3f}, {node.Z:.3f})\n")
				
				# Append to reaction lists
				reaction_x.append(fx)
				reaction_y.append(fy)
				reaction_z.append(fz)
				reaction_mx.append(mx)
				reaction_my.append(my)
				reaction_mz.append(mz)
		
		_print_message(f"Total reactions - Sum FX: {total_fx:.3f}, Sum FY: {total_fy:.3f}, Sum FZ: {total_fz:.3f}\n")

		# Store reaction values in object properties
		_print_message(f"Storing {len(reaction_nodes)} reaction nodes with their values\n")
		obj.ReactionNodes = reaction_nodes
		obj.ReactionX = reaction_x
		obj.ReactionY = reaction_y
		obj.ReactionZ = reaction_z
		obj.ReactionMX = reaction_mx
		obj.ReactionMY = reaction_my
		obj.ReactionMZ = reaction_mz

		# Gera os resultados
		momentz = []
		momenty = []
		mimMomenty = []
		mimMomentz = []
		maxMomenty = []
		maxMomentz = []
		axial = []
		torque = []
		minTorque = []
		maxTorque = []
		sheary = []
		shearz = []
		minSheary = []
		maxSheary = []
		minShearz = []
		maxShearz = []
		deflectiony = []
		minDeflectiony = []
		maxDeflectiony = []
		deflectionz = []
		minDeflectionz = []
		maxDeflectionz = []

		# Structured per-member results (list of dicts) for easier downstream consumption
		member_results = []

		# helper: create a member summary dict from model/member
		def _build_member_summary(member_name: str) -> dict:
			"""Build a dict summary for a member.

			Returns keys: name, section, nodes, momentY, momentZ, shearY, shearZ,
			axial, torque, deflectionY, deflectionZ and min/max scalar values.
			"""
			m = model.members[member_name]
			# numeric arrays (try-except to tolerate missing methods)
			try:
				my_vals = [float(v) for v in m.moment_array('My', getattr(obj, 'NumPointsMoment', 3))[1]]
			except Exception:
				my_vals = []
			try:
				mz_vals = [float(v) for v in m.moment_array('Mz', getattr(obj, 'NumPointsMoment', 3))[1]]
			except Exception:
				mz_vals = []
			try:
				fy_vals = [float(v) for v in m.shear_array('Fy', getattr(obj, 'NumPointsShear', 3))[1]]
			except Exception:
				fy_vals = []
			try:
				fz_vals = [float(v) for v in m.shear_array('Fz', getattr(obj, 'NumPointsShear', 3))[1]]
			except Exception:
				fz_vals = []
			try:
				ax_vals = [float(v) for v in m.axial_array(getattr(obj, 'NumPointsAxial', 2))[1]]
			except Exception:
				ax_vals = []
			try:
				tq_vals = [float(v) for v in m.torque_array(getattr(obj, 'NumPointsTorque', 2))[1]]
			except Exception:
				tq_vals = []
			try:
				dy_vals = [float(v) for v in m.deflection_array('dy', getattr(obj, 'NumPointsDeflection', 2))[1]]
			except Exception:
				dy_vals = []
			try:
				dz_vals = [float(v) for v in m.deflection_array('dz', getattr(obj, 'NumPointsDeflection', 2))[1]]
			except Exception:
				dz_vals = []

			return {
				'name': member_name,
				'section': (members_map.get(member_name, {}).get('section') if 'members_map' in locals() else None),
				'nodes': (members_map.get(member_name, {}).get('nodes') if 'members_map' in locals() else []),
				'momentY': my_vals,
				'momentZ': mz_vals,
				'shearY': fy_vals,
				'shearZ': fz_vals,
				'axial': ax_vals,
				'torque': tq_vals,
				'deflectionY': dy_vals,
				'deflectionZ': dz_vals,
				'minMomentY': m.min_moment('My', combo_name=active_load_combination),
				'maxMomentY': m.max_moment('My', combo_name=active_load_combination),
				'minMomentZ': m.min_moment('Mz', combo_name=active_load_combination),
				'maxMomentZ': m.max_moment('Mz', combo_name=active_load_combination),
				'minShearY': m.min_shear('Fy', combo_name=active_load_combination),
				'maxShearY': m.max_shear('Fy', combo_name=active_load_combination),
				'minShearZ': m.min_shear('Fz', combo_name=active_load_combination),
				'maxShearZ': m.max_shear('Fz', combo_name=active_load_combination),
				'minTorque': m.min_torque(combo_name=active_load_combination),
				'maxTorque': m.max_torque(combo_name=active_load_combination),
				'minDeflectionY': m.min_deflection('dy', combo_name=active_load_combination),
				'maxDeflectionY': m.max_deflection('dy', combo_name=active_load_combination),
				'minDeflectionZ': m.min_deflection('dz', combo_name=active_load_combination),
				'maxDeflectionZ': m.max_deflection('dz', combo_name=active_load_combination)
			}

		for name in model.members.keys():
			try:
				momenty.append(','.join( str(value) for value in model.members[name].moment_array('My', getattr(obj, 'NumPointsMoment', 5), combo_name=active_load_combination)[1]))
				momentz.append(','.join( str(value) for value in model.members[name].moment_array('Mz', getattr(obj, 'NumPointsMoment', 5), combo_name=active_load_combination)[1]))
			except Exception as e:
				_print_warning(f"Error getting moment arrays for member '{name}' with combo '{active_load_combination}': {e}\n")
				momenty.append('0.0')
				momentz.append('0.0')

			try:
				sheary.append(','.join( str(value) for value in model.members[name].shear_array('Fy', getattr(obj, 'NumPointsShear', 4), combo_name=active_load_combination)[1]))
				shearz.append(','.join( str(value) for value in model.members[name].shear_array('Fz', getattr(obj, 'NumPointsShear', 4), combo_name=active_load_combination)[1]))

				axial.append(','.join( str(value) for value in model.members[name].axial_array(getattr(obj, 'NumPointsAxial', 3), combo_name=active_load_combination)[1]))
				
				torque.append(','.join( str(value) for value in model.members[name].torque_array(getattr(obj, 'NumPointsTorque', 3), combo_name=active_load_combination)[1]))

				deflectiony.append(','.join( str(value) for value in model.members[name].deflection_array('dy', getattr(obj, 'NumPointsDeflection', 4), combo_name=active_load_combination)[1]))
				deflectionz.append(','.join( str(value) for value in model.members[name].deflection_array('dz', getattr(obj, 'NumPointsDeflection', 4), combo_name=active_load_combination)[1]))
			except Exception as e:
				_print_warning(f"Error getting force/deflection arrays for member '{name}' with combo '{active_load_combination}': {e}\n")
				sheary.append('0.0')
				shearz.append('0.0')
				axial.append('0.0')
				torque.append('0.0')
				deflectiony.append('0.0')
				deflectionz.append('0.0')

			try:
				mimMomenty.append(model.members[name].min_moment('My', combo_name=active_load_combination))
				mimMomentz.append(model.members[name].min_moment('Mz', combo_name=active_load_combination))
				maxMomenty.append(model.members[name].max_moment('My', combo_name=active_load_combination))
				maxMomentz.append(model.members[name].max_moment('Mz', combo_name=active_load_combination))

				minSheary.append(model.members[name].min_shear('Fy', combo_name=active_load_combination))
				minShearz.append(model.members[name].min_shear('Fz', combo_name=active_load_combination))
				maxSheary.append(model.members[name].max_shear('Fy', combo_name=active_load_combination))
				maxShearz.append(model.members[name].max_shear('Fz', combo_name=active_load_combination))

				minTorque.append(model.members[name].min_torque(combo_name=active_load_combination))
				maxTorque.append(model.members[name].max_torque(combo_name=active_load_combination))

				minDeflectiony.append(model.members[name].min_deflection('dy', combo_name=active_load_combination))
				minDeflectionz.append(model.members[name].min_deflection('dz', combo_name=active_load_combination))
				maxDeflectiony.append(model.members[name].max_deflection('dy', combo_name=active_load_combination))
				maxDeflectionz.append(model.members[name].max_deflection('dz', combo_name=active_load_combination))
			except Exception as e:
				_print_warning(f"Error getting min/max values for member '{name}' with combo '{active_load_combination}': {e}\n")
				mimMomenty.append(0.0)
				mimMomentz.append(0.0)
				maxMomenty.append(0.0)
				maxMomentz.append(0.0)
				minSheary.append(0.0)
				minShearz.append(0.0)
				maxSheary.append(0.0)
				maxShearz.append(0.0)
				minTorque.append(0.0)
				maxTorque.append(0.0)
				minDeflectiony.append(0.0)
				minDeflectionz.append(0.0)
				maxDeflectiony.append(0.0)
				maxDeflectionz.append(0.0)

			# Also collect structured numeric results for this member (lists of floats)
			try:
				my_vals = [float(v) for v in model.members[name].moment_array('My', getattr(obj, 'NumPointsMoment', 3), combo_name=active_load_combination)[1]]
			except Exception:
				my_vals = []
			try:
				mz_vals = [float(v) for v in model.members[name].moment_array('Mz', getattr(obj, 'NumPointsMoment', 3), combo_name=active_load_combination)[1]]
			except Exception:
				mz_vals = []
			try:
				fy_vals = [float(v) for v in model.members[name].shear_array('Fy', getattr(obj, 'NumPointsShear', 3), combo_name=active_load_combination)[1]]
			except Exception:
				fy_vals = []
			try:
				fz_vals = [float(v) for v in model.members[name].shear_array('Fz', getattr(obj, 'NumPointsShear', 3), combo_name=active_load_combination)[1]]
			except Exception:
				fz_vals = []
			try:
				ax_vals = [float(v) for v in model.members[name].axial_array(getattr(obj, 'NumPointsAxial', 2), combo_name=active_load_combination)[1]]
			except Exception:
				ax_vals = []
			try:
				tq_vals = [float(v) for v in model.members[name].torque_array(getattr(obj, 'NumPointsTorque', 2), combo_name=active_load_combination)[1]]
			except Exception:
				tq_vals = []
			try:
				dy_vals = [float(v) for v in model.members[name].deflection_array('dy', getattr(obj, 'NumPointsDeflection', 2), combo_name=active_load_combination)[1]]
			except Exception:
				dy_vals = []
			try:
				dz_vals = [float(v) for v in model.members[name].deflection_array('dz', getattr(obj, 'NumPointsDeflection', 2), combo_name=active_load_combination)[1]]
			except Exception:
				dz_vals = []

			# build structured summary and append
			summary = _build_member_summary(name)
			member_results.append(summary)
			

		obj.NameMembers = model.members.keys()
		obj.Nodes = [App.Vector(node[0], node[2], node[1]) for node in nodes_map]
		obj.MomentZ = momentz
		obj.MomentY = momenty
		obj.MinMomentY = mimMomenty
		obj.MinMomentZ = mimMomentz
		obj.MaxMomentY = maxMomenty
		obj.MaxMomentZ = maxMomentz
		obj.AxialForce = axial
		obj.Torque = torque
		obj.MinTorque = minTorque
		obj.MaxTorque = maxTorque
		obj.MinShearY = minSheary
		obj.MinShearZ = minShearz
		obj.MaxShearY = maxSheary
		obj.MaxShearZ = maxShearz
		obj.ShearY = sheary
		obj.ShearZ = shearz
		obj.DeflectionY = deflectiony
		obj.DeflectionZ = deflectionz
		obj.MinDeflectionY = minDeflectiony
		obj.MinDeflectionZ = minDeflectionz
		obj.MaxDeflectionY = maxDeflectiony
		obj.MaxDeflectionZ = maxDeflectionz
		# expose structured per-member results (backwards-compatible addition)
		if hasattr(obj, 'MemberResults'):
			obj.MemberResults = member_results
		else:
			# For older Calc objects without MemberResults property, add it dynamically
			try:
				obj.addProperty("App::PropertyPythonObject", "MemberResults", "Calc", "structured per-member results")
				obj.MemberResults = member_results
			except Exception as e:
				_print_warning(f"Could not add MemberResults property: {e}\n")
		
		# Update Thai units if enabled (Legacy support)
		if hasattr(obj, 'UseThaiUnits') and getattr(obj, 'UseThaiUnits', False):
			self.updateThaiUnitsResults(obj)
			
		# Update Global Units if enabled (New enhanced system)
		if hasattr(obj, 'UseGlobalUnits') and getattr(obj, 'UseGlobalUnits', True):
			self.updateGlobalUnitsResults(obj)
	   

	def updateThaiUnitsResults(self, obj):
		"""Update Thai units calculation results"""
		try:
			from .utils.universal_thai_units import UniversalThaiUnits
			converter = UniversalThaiUnits()
		except ImportError:
			# Thai units not available
			return
			
		try:
			
			# Convert moment results to ksc
			moment_z_ksc = []
			moment_y_ksc = []
			for mz_str in obj.MomentZ:
				values = [float(v) for v in mz_str.split(',')]
				# Use a more generic conversion method if kn_m_to_ksc_m is not available
				ksc_values = [v * 101.97162129779283 for v in values]  # Approximate conversion factor
				moment_z_ksc.append(','.join(str(v) for v in ksc_values))
			
			for my_str in obj.MomentY:
				values = [float(v) for v in my_str.split(',')]
				# Use a more generic conversion method if kn_m_to_ksc_m is not available
				ksc_values = [v * 101.97162129779283 for v in values]  # Approximate conversion factor
				moment_y_ksc.append(','.join(str(v) for v in ksc_values))
			
			obj.MomentZKsc = moment_z_ksc
			obj.MomentYKsc = moment_y_ksc
			
			# Convert axial forces to kgf and tf
			axial_kgf = []
			axial_tf = []
			for ax_str in obj.AxialForce:
				values = [float(v) for v in ax_str.split(',')]
				# Use a more generic conversion method if kn_to_kgf is not available
				kgf_values = [v * 101.97162129779283 for v in values]  # Approximate conversion factor
				tf_values = [v * 0.0010197162129779283 for v in values]  # Approximate conversion factor
				axial_kgf.append(','.join(str(v) for v in kgf_values))
				axial_tf.append(','.join(str(v) for v in tf_values))
			
			obj.AxialForceKgf = axial_kgf
			obj.AxialForceTf = axial_tf
			
			# Convert shear forces to kgf
			shear_y_kgf = []
			shear_z_kgf = []
			for sy_str in obj.ShearY:
				values = [float(v) for v in sy_str.split(',')]
				# Use a more generic conversion method if kn_to_kgf is not available
				kgf_values = [v * 101.97162129779283 for v in values]  # Approximate conversion factor
				shear_y_kgf.append(','.join(str(v) for v in kgf_values))
			
			for sz_str in obj.ShearZ:
				values = [float(v) for v in sz_str.split(',')]
				# Use a more generic conversion method if kn_to_kgf is not available
				kgf_values = [v * 101.97162129779283 for v in values]  # Approximate conversion factor
				shear_z_kgf.append(','.join(str(v) for v in kgf_values))
			
			obj.ShearYKgf = shear_y_kgf
			obj.ShearZKgf = shear_z_kgf
			
		except Exception as e:
			_print_warning(f"Thai units conversion failed: {e}\n")

	def getResultsInThaiUnits(self, obj):
		"""Get calculation results in Thai units format"""
		if not hasattr(obj, 'UseThaiUnits') or not obj.UseThaiUnits:
			return None
			
		thai_results = {
			'moments_ksc': {
				'momentY': getattr(obj, 'MomentYKsc', []),
				'momentZ': getattr(obj, 'MomentZKsc', [])
			},
			'forces_kgf': {
				'axial': getattr(obj, 'AxialForceKgf', []),
				'shearY': getattr(obj, 'ShearYKgf', []),
				'shearZ': getattr(obj, 'ShearZKgf', [])
			},
			'forces_tf': {
				'axial': getattr(obj, 'AxialForceTf', [])
			}
		}
		return thai_results
	
	def updateGlobalUnitsResults(self, obj):
		"""Update calculation results using Global Units System"""
		if not GLOBAL_UNITS_AVAILABLE:
			return
			
		try:
			# Get units manager and set system
			units_manager = get_units_manager()
			if hasattr(obj, 'GlobalUnitsSystem') and units_manager is not None:
				units_manager.set_unit_system(obj.GlobalUnitsSystem)
			
			# Format force results
			if hasattr(obj, 'MaxAxialForce') and obj.MaxAxialForce:
				formatted_forces = []
				for force_n in obj.MaxAxialForce:
					formatted = format_force(force_n * 1000)  # Convert kN to N for function
					formatted_forces.append(formatted)
				obj.FormattedForces = formatted_forces
			
			# Format moment results (as stress equivalent)
			if hasattr(obj, 'MaxMomentZ') and obj.MaxMomentZ:
				formatted_moments = []
				for moment_knm in obj.MaxMomentZ:
					# Convert moment to equivalent stress for display
					moment_nm = moment_knm * 1000000  # kN⋅m to N⋅mm
					formatted = format_stress(moment_nm)  # Display as stress-like unit
					formatted_moments.append(formatted)
				obj.FormattedMoments = formatted_moments
			
			# Format general stress results (if available)
			if hasattr(obj, 'MaxStress') and getattr(obj, 'MaxStress', None):
				formatted_stresses = []
				for stress_pa in obj.MaxStress:
					formatted = format_stress(stress_pa)
					formatted_stresses.append(formatted)
				obj.FormattedStresses = formatted_stresses
				
		except Exception as e:
			_print_warning(f"Global units formatting failed: {e}\n")
		
	   


	def onChanged(self,obj,Parameter):
		pass

	def member_results_to_json(self, obj) -> str:
		"""Return a JSON string of obj.MemberResults.

		This helper serializes the structured MemberResults for export or UI use.
		"""
		import json
		results = getattr(obj, 'MemberResults', [])
		# Ensure numeric types are JSON serializable (lists of floats are fine)
		return json.dumps(results)

	def member_results_to_csv(self, obj, include_header: bool = True) -> str:
		"""Return a CSV string for obj.MemberResults.

		CSV columns: name,section,nodes,momentY,momentZ,shearY,shearZ,axial,torque,deflectionY,deflectionZ,minMomentY,...
		Lists are serialized as semicolon-separated numeric strings inside cells.
		"""
		import csv, io
		results = getattr(obj, 'MemberResults', [])
		if not results:
			return ''

		# determine header keys (preserve order)
		header = list(results[0].keys())
		output = io.StringIO()
		writer = csv.writer(output)
		if include_header:
			writer.writerow(header)
		for r in results:
			row = []
			for k in header:
				val = r.get(k, '')
				if isinstance(val, list):
					# join numeric lists with semicolon
					row.append(';'.join(str(x) for x in val))
				else:
					row.append(str(val))
			writer.writerow(row)
		return output.getvalue()
	

class ViewProviderCalc:
	def __init__(self, obj):
		obj.Proxy = self
		self.Object = obj.Object
		self.reaction_texts = []  # Store reaction text objects
	
	def updateData(self, obj, prop):
		"""Called when the object's data changes"""
		if prop in ['ShowReactionText', 'ReactionPrecision', 'ReactionTextOffset', 'ReactionFontSize', 'LoadCombination']:
			self.updateReactionTextDisplay()
	
	def onChanged(self, obj, prop):
		"""Called when view properties change"""
		if prop == 'ShowReactionText':
			self.updateReactionTextDisplay()
	
	def updateReactionTextDisplay(self):
		"""Update the display of reaction texts based on ShowReactionText property"""
		try:
			# Clear existing reaction texts
			self.clearReactionTexts()
			
			# Only proceed if ShowReactionText is True
			if not getattr(self.Object, 'ShowReactionText', False):
				return
			
			# Get reaction data from analysis results
			if not hasattr(self.Object, 'model') or self.Object.model is None:
				return
			
			# Create reaction texts for each support node
			self.createReactionTexts()
			
		except Exception as e:
			print(f"Error updating reaction text display: {e}")
	
	def createReactionTexts(self):
		"""Create 3D text objects for reaction forces and moments"""
		try:
			model = self.Object.model
			if not model or not hasattr(model, 'Nodes'):
				return
			
			# Get display properties
			precision = getattr(self.Object, 'ReactionPrecision', 2)
			offset = getattr(self.Object, 'ReactionTextOffset', 100.0)  # mm
			font_size = getattr(self.Object, 'ReactionFontSize', 12.0)
			active_combination = getattr(self.Object, 'LoadCombination', '100_DL')
			
			# Iterate through nodes to find supports with reactions
			for node_name, node in model.Nodes.items():
				# Check if node has support conditions
				has_support = any([
					node.support_DX, node.support_DY, node.support_DZ,
					node.support_RX, node.support_RY, node.support_RZ
				])
				
				if not has_support:
					continue
				
				# Get reaction values
				reactions = self.getNodeReactions(node, active_combination)
				if not reactions:
					continue
				
				# Create text for this node
				text_content = self.formatReactionText(node_name, reactions, precision)
				if text_content:
					text_obj = self.createTextObject(node, text_content, offset, font_size)
					if text_obj:
						self.reaction_texts.append(text_obj)
			
		except Exception as e:
			print(f"Error creating reaction texts: {e}")
	
	def getNodeReactions(self, node, combo_name):
		"""Extract reaction values for a node from analysis results"""
		reactions = {}
		
		try:
			# Get reaction forces
			if hasattr(node, 'RxnFX') and combo_name in node.RxnFX:
				reactions['FX'] = node.RxnFX[combo_name]
			if hasattr(node, 'RxnFY') and combo_name in node.RxnFY:
				reactions['FY'] = node.RxnFY[combo_name]
			if hasattr(node, 'RxnFZ') and combo_name in node.RxnFZ:
				reactions['FZ'] = node.RxnFZ[combo_name]
			
			# Get reaction moments
			if hasattr(node, 'RxnMX') and combo_name in node.RxnMX:
				reactions['MX'] = node.RxnMX[combo_name]
			if hasattr(node, 'RxnMY') and combo_name in node.RxnMY:
				reactions['MY'] = node.RxnMY[combo_name]
			if hasattr(node, 'RxnMZ') and combo_name in node.RxnMZ:
				reactions['MZ'] = node.RxnMZ[combo_name]
				
		except Exception as e:
			print(f"Error getting node reactions: {e}")
		
		return reactions
	
	def formatReactionText(self, node_name, reactions, precision):
		"""Format reaction values into display text"""
		lines = [f"Node: {node_name}"]
		
		# Format forces
		force_lines = []
		for component in ['FX', 'FY', 'FZ']:
			if component in reactions:
				value = reactions[component]
				if abs(value) > 1e-6:  # Only show significant values
					force_lines.append(f"{component}: {value:.{precision}f} kN")
		
		if force_lines:
			lines.extend(force_lines)
		
		# Format moments
		moment_lines = []
		for component in ['MX', 'MY', 'MZ']:
			if component in reactions:
				value = reactions[component]
				if abs(value) > 1e-6:  # Only show significant values
					moment_lines.append(f"{component}: {value:.{precision}f} kN·m")
		
		if moment_lines:
			lines.extend(moment_lines)
		
		return '\n'.join(lines) if len(lines) > 1 else ""
	
	def createTextObject(self, node, text_content, offset, font_size):
		"""Create a 3D text object at the node location"""
		try:
			doc = App.ActiveDocument
			if not doc:
				return None
			
			# Calculate text position (offset from node)
			node_pos = App.Vector(node.X, node.Y, node.Z)
			text_pos = node_pos + App.Vector(offset, offset, 0)
			
			# Try different methods to create text
			text_obj = None
			
			# Method 1: Try using Part workbench for 3D text
			try:
				import Part
				# Create simple text using Part.makeText (if available)
				text_obj = doc.addObject("Part::Feature", f"Reactions_{node.name}")
				
				# Create simple wire geometry for text display
				# Since Part.makeText might not be available, create basic shapes
				lines = text_content.split('\n')
				shapes = []
				
				for i, line in enumerate(lines):
					if line.strip():
						# Create a simple line/wire to represent text
						start_point = text_pos + App.Vector(0, -i * font_size * 2, 0)
						end_point = start_point + App.Vector(len(line) * font_size * 0.8, 0, 0)
						
						# Create a simple line
						line_wire = Part.makeLine(start_point, end_point)
						shapes.append(line_wire)
				
				if shapes:
					# Combine all lines
					compound = Part.makeCompound(shapes)
					text_obj.Shape = compound
					text_obj.Label = f"Reactions_{node.name}_Wire"
					
					# Set visual properties
					if hasattr(text_obj.ViewObject, 'ShapeColor'):
						text_obj.ViewObject.ShapeColor = (1.0, 0.0, 0.0)  # Red
					if hasattr(text_obj.ViewObject, 'LineWidth'):
						text_obj.ViewObject.LineWidth = 2.0
					
					print(f"Created wire-based text for {node.name}: {text_content}")
					return text_obj
				
			except Exception as e:
				print(f"Part method failed: {e}")
			
			# Method 2: Try Draft workbench
			try:
				import Draft
				text_obj = Draft.make_text(text_content, point=text_pos)
				text_obj.Label = f"Reactions_{node.name}_Draft"
				
				# Set text properties
				if hasattr(text_obj.ViewObject, 'FontSize'):
					text_obj.ViewObject.FontSize = font_size
				if hasattr(text_obj.ViewObject, 'TextColor'):
					text_obj.ViewObject.TextColor = (1.0, 0.0, 0.0)  # Red color
				
				print(f"Created Draft text for {node.name}: {text_content}")
				return text_obj
				
			except Exception as e:
				print(f"Draft method failed: {e}")
			
			# Method 3: Create annotation object
			try:
				text_obj = doc.addObject("App::Annotation", f"Reactions_{node.name}_Annotation")
				text_obj.LabelText = text_content
				text_obj.Position = text_pos
				
				print(f"Created annotation for {node.name}: {text_content}")
				return text_obj
				
			except Exception as e:
				print(f"Annotation method failed: {e}")
			
			# Method 4: Simple debug print
			print(f"All text creation methods failed. Text content for {node.name}:")
			print(f"  Position: {text_pos}")
			print(f"  Content: {text_content}")
			
			return None
			
		except Exception as e:
			print(f"Error creating text object: {e}")
			return None
	
	def clearReactionTexts(self):
		"""Remove all existing reaction text objects"""
		try:
			doc = App.ActiveDocument
			if not doc:
				return
			
			for text_obj in self.reaction_texts:
				if text_obj and text_obj.Name in doc.Objects:
					doc.removeObject(text_obj.Name)
			
			self.reaction_texts.clear()
			
		except Exception as e:
			print(f"Error clearing reaction texts: {e}")

	def getIcon(self):
		return """
/* XPM */
static char * calc_xpm[] = {
"32 32 282 2",
"  	c None",
". 	c #030C1D",
"+ 	c #05112D",
"@ 	c #051129",
"# 	c #061129",
"$ 	c #071229",
"% 	c #08142C",
"& 	c #0A152E",
"* 	c #0B162E",
"= 	c #0A1426",
"- 	c #0C1527",
"; 	c #0F192E",
"> 	c #101A2E",
", 	c #111B2E",
"' 	c #121C2E",
") 	c #111827",
"! 	c #121826",
"~ 	c #151E2E",
"{ 	c #171E2E",
"] 	c #181E2C",
"^ 	c #171E29",
"/ 	c #181E29",
"( 	c #191F29",
"_ 	c #1D212D",
": 	c #13161D",
"< 	c #030C1C",
"[ 	c #1044AB",
"} 	c #1966FF",
"| 	c #1B67FF",
"1 	c #226CFF",
"2 	c #2870FF",
"3 	c #2F75FF",
"4 	c #3679FF",
"5 	c #3C7EFF",
"6 	c #4382FF",
"7 	c #4A86FF",
"8 	c #508BFF",
"9 	c #578FFF",
"0 	c #5E94FF",
"a 	c #6498FF",
"b 	c #6B9CFF",
"c 	c #72A1FF",
"d 	c #78A5FF",
"e 	c #7FAAFF",
"f 	c #86AEFF",
"g 	c #8CB3FF",
"h 	c #93B7FF",
"i 	c #9ABBFF",
"j 	c #6B80AA",
"k 	c #12161D",
"l 	c #040D1F",
"m 	c #206BFF",
"n 	c #266FFF",
"o 	c #2D73FF",
"p 	c #3478FF",
"q 	c #3A7CFF",
"r 	c #4181FF",
"s 	c #4885FF",
"t 	c #4E89FF",
"u 	c #558EFF",
"v 	c #5C92FF",
"w 	c #6297FF",
"x 	c #699BFF",
"y 	c #70A0FF",
"z 	c #76A4FF",
"A 	c #7DA8FF",
"B 	c #84ADFF",
"C 	c #8AB1FF",
"D 	c #91B6FF",
"E 	c #98BAFF",
"F 	c #13181F",
"G 	c #1964FA",
"H 	c #0F409E",
"I 	c #0C2E72",
"J 	c #0B2C6E",
"K 	c #0D2D6E",
"L 	c #0F2F6E",
"M 	c #12316E",
"N 	c #15336E",
"O 	c #19356E",
"P 	c #1B366D",
"Q 	c #1E386D",
"R 	c #213B6E",
"S 	c #243D6E",
"T 	c #263F6E",
"U 	c #2A406E",
"V 	c #2D426E",
"W 	c #2F446E",
"X 	c #344972",
"Y 	c #4D69A0",
"Z 	c #7FA9FA",
"` 	c #88B0FF",
" .	c #8FB4FF",
"..	c #13161F",
"+.	c #0C2F76",
"@.	c #02060E",
"#.	c #060A0E",
"$.	c #384E77",
"%.	c #80AAFF",
"&.	c #86AFFF",
"*.	c #12161F",
"=.	c #04122C",
"-.	c #141C2C",
";.	c #77A5FF",
">.	c #7EA9FF",
",.	c #10151F",
"'.	c #041128",
").	c #111929",
"!.	c #6E9FFF",
"~.	c #75A3FF",
"{.	c #0F141F",
"].	c #04122B",
"^.	c #111A2C",
"/.	c #6699FF",
"(.	c #6D9DFF",
"_.	c #0E141F",
":.	c #0C2D71",
"<.	c #274073",
"[.	c #5D93FF",
"}.	c #0D131F",
"|.	c #1964FB",
"1.	c #0E3A92",
"2.	c #0A2B6B",
"3.	c #0A2A69",
"4.	c #0A2762",
"5.	c #092459",
"6.	c #0B2559",
"7.	c #0D2759",
"8.	c #0F2859",
"9.	c #112959",
"0.	c #142B59",
"a.	c #172C59",
"b.	c #254585",
"c.	c #4D87FB",
"d.	c #5B92FF",
"e.	c #0C131F",
"f.	c #1D69FF",
"g.	c #246DFF",
"h.	c #2B72FF",
"i.	c #3176FF",
"j.	c #387BFF",
"k.	c #3F7FFF",
"l.	c #4583FF",
"m.	c #4C88FF",
"n.	c #538CFF",
"o.	c #0B121F",
"p.	c #1B68FF",
"q.	c #2970FF",
"r.	c #3D7EFF",
"s.	c #4A87FF",
"t.	c #09101F",
"u.	c #0D327E",
"v.	c #030E25",
"w.	c #1453D0",
"x.	c #276FFF",
"y.	c #2D74FF",
"z.	c #3B7CFF",
"A.	c #05112C",
"B.	c #0D3482",
"C.	c #1E69FF",
"D.	c #256EFF",
"E.	c #3277FF",
"F.	c #397BFF",
"G.	c #080F1F",
"H.	c #1864F9",
"I.	c #165BE3",
"J.	c #030E22",
"K.	c #092457",
"L.	c #1860F1",
"M.	c #175EEB",
"N.	c #1658DD",
"O.	c #175FEE",
"P.	c #1B64F4",
"Q.	c #236CFF",
"R.	c #2971FF",
"S.	c #3075FF",
"T.	c #070F1F",
"U.	c #0B2E74",
"V.	c #040C20",
"W.	c #030C1E",
"X.	c #020916",
"Y.	c #03091A",
"Z.	c #030D21",
"`.	c #030D1F",
" +	c #1451CA",
".+	c #1556D8",
"++	c #020A1A",
"@+	c #030B1E",
"#+	c #216BFF",
"$+	c #2770FF",
"%+	c #060E1F",
"&+	c #092254",
"*+	c #030D1E",
"=+	c #020816",
"-+	c #040B1A",
";+	c #030A18",
">+	c #1249B6",
",+	c #1249B9",
"'+	c #030918",
")+	c #040D22",
"!+	c #040B1E",
"~+	c #020812",
"{+	c #030C1F",
"]+	c #081F4E",
"^+	c #1F6AFF",
"/+	c #050D1F",
"(+	c #1450C8",
"_+	c #124BBB",
":+	c #071D48",
"<+	c #134DC0",
"[+	c #165AE0",
"}+	c #1554D3",
"|+	c #134EC3",
"1+	c #1863F7",
"2+	c #031027",
"3+	c #0B2E72",
"4+	c #020918",
"5+	c #124ABA",
"6+	c #0F3990",
"7+	c #061739",
"8+	c #1557D9",
"9+	c #0F3C93",
"0+	c #04132F",
"a+	c #1454D1",
"b+	c #0C317B",
"c+	c #030D20",
"d+	c #1659DF",
"e+	c #0B2A69",
"f+	c #1554D2",
"g+	c #031026",
"h+	c #0A2C6C",
"i+	c #030A1A",
"j+	c #0C2F75",
"k+	c #051027",
"l+	c #04132E",
"m+	c #1658DC",
"n+	c #071A42",
"o+	c #134DC1",
"p+	c #02060F",
"q+	c #124ABB",
"r+	c #071E49",
"s+	c #0F3E9B",
"t+	c #030E21",
"u+	c #082152",
"v+	c #010712",
"w+	c #1147B0",
"x+	c #1556D6",
"y+	c #1148B5",
"z+	c #0E3A8F",
"A+	c #030B1A",
"B+	c #010813",
"C+	c #020C1C",
"D+	c #1555D5",
"E+	c #040D20",
"F+	c #020B1B",
"G+	c #041431",
"H+	c #061637",
"I+	c #1861F3",
"J+	c #030F24",
"K+	c #1144AA",
"L+	c #040C1E",
"M+	c #06183D",
"N+	c #134FC5",
"O+	c #1041A1",
"P+	c #144FC6",
"Q+	c #0E3685",
"R+	c #1862F4",
"S+	c #1860F0",
"T+	c #124CBC",
"U+	c #1861F2",
"V+	c #092255",
"W+	c #1966FE",
"X+	c #1044AA",
"Y+	c #030B1D",
"Z+	c #031029",
"`+	c #04122D",
" @	c #04122E",
".@	c #040F28",
"+@	c #030E24",
"@@	c #030F26",
"#@	c #03112A",
"$@	c #031028",
"        . + @ # $ % & * = - ; > , ' ) ! ~ { ] ^ / ( _ :         ",
"      < [ } } | 1 2 3 4 5 6 7 8 9 0 a b c d e f g h i j k       ",
"      l } } } } } m n o p q r s t u v w x y z A B C D E F       ",
"      l } } G H I J K L M N O P Q R S T U V W X Y Z `  ...      ",
"      l } } +.@.                                #.$.%.&.*.      ",
"      l } } =.                                    -.;.>.,.      ",
"      l } } '.                                    ).!.~.{.      ",
"      l } } ].                                    ^./.(._.      ",
"      l } } :.                                    <.[.a }.      ",
"      l } } |.1.2.3.3.3.3.4.5.5.5.5.6.7.8.9.0.a.b.c.u d.e.      ",
"      l } } } } } } } } } } } } } } } f.g.h.i.j.k.l.m.n.o.      ",
"      l } } } } } } } } } } } } } } } } p.1 q.3 4 r.6 s.t.      ",
"      l } } } } } u.v.w.} } } } } } } } } } m x.y.p z.r t.      ",
"      l } } } } } A.  B.} } } } } } } } } } } C.D.h.E.F.G.      ",
"      l } } } H.I.J.  K.L.} } } } } M.N.N.N.I.O.P.Q.R.S.T.      ",
"      l } } U.V.W.X.  Y.Z.`. +} } .+++W.W.W.W.W.@+J #+$+%+      ",
"      l } } &+*+=+      -+;+>+} } ,+'+)+!+~+~+~+{+]+} ^+/+      ",
"      l } } H.(+_+{+  :+<+[+} } } } }+_+_+_+_+_+|+1+} } l       ",
"      l } } } } } 2+  3+} } } } } } } } } } } } } } } } l       ",
"      l } } } } } 5.4+5+} } } } } } } } } } } } } } } } l       ",
"      l } } } } } } 1+} } } } } } } } } } } } } } } } } l       ",
"      l } } } } } } } } } } } } } } } } } } } } } } } } l       ",
"      l } } } 6+7+8+} 9+0+a+} } } } b+c+6+} d+e+f+} } } l       ",
"      l } } } g+  . h+i+  j+} } } } k+  l+m+J.  n+} } } l       ",
"      l } } } o+i+  p+  '.M.} } } } q+r+s+t+  ++o+} } } l       ",
"      l } } } } u+    v+w+} } } } } } x+J.  ++y+} } } } l       ",
"      l } } } z+A+  B+  C+D+} } } } }+E+  F+1.G+H+I+} } l       ",
"      l } } } J+  G+K+L+  B.} } } } M+  L+N+O+  @+ +} } l       ",
"      l } } } P+Q+R+} N.B.S+} } } } T+n+f+} U+V+e+W+} } l       ",
"      l } } } } } } } } } } } } } } } } } } } } } } } } l       ",
"      . [ } } } } } } } } } } } } } } } } } } } } } } X+.       ",
"        Y++ Z+Z+Z+`+ @ @.@+@ @ @ @ @v.@@ @ @ @#@Z+Z+$@.         "};
		"""


class CommandCalc():

    def GetResources(self):
        return {"Pixmap"  : os.path.join(ICONPATH, "icons/calc.svg"), # the name of a svg file available in the resources
                "Accel"   : "Shift+C", # a default shortcut (optional)
                "MenuText": "Calc estructure",
                "ToolTip" : "Calcula a estrutura"}
    
    def Activated(self):
        selection = FreeCADGui.Selection.getSelection()
        doc = App.ActiveDocument
        obj = doc.addObject("Part::FeaturePython", "Calc")

        objSuport = Calc(obj, selection)
        ViewProviderCalc(obj.ViewObject)           

        App.ActiveDocument.recompute()        
        return

    def IsActive(self):
        
        return True

# Only register command if FreeCAD GUI is available
if FREECAD_AVAILABLE and 'FreeCADGui' in globals():
    FreeCADGui.addCommand("calc", CommandCalc())
