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
    import FreeCAD as App
    import FreeCADGui
    import Part
    FREECAD_AVAILABLE = True
except ImportError:
    FREECAD_AVAILABLE = False
    print("FreeCAD modules not available and stubs failed to load")
    # Minimal fallback to prevent immediate crash, though functionality will be broken
    class MockApp:
        class Console:
            @staticmethod
            def PrintError(msg): print("ERROR:", msg)
            @staticmethod
            def PrintWarning(msg): print("WARNING:", msg)
            @staticmethod
            def PrintMessage(msg): print("MESSAGE:", msg)
        Console = Console()
    App = MockApp()
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


try:
    from .analysis.model_builder import ModelBuilder
    from .analysis.pynite_adapter import PyniteAdapter
    from .analysis.result_manager import ResultManager
except ImportError:
    # Log error if needed, but this should work in struct
    print("Failed to import Analysis components")



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
		msg_box.exec()
	except Exception:
		# Fallback if QMessageBox is not available
		print("ERROR:", msg)


class Calc:
	def __init__(self, obj, elements):
		obj.Proxy = self
		self.builder = ModelBuilder()

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
		_addProp("App::PropertyFloatList", "MaxAxial", "Calc", "max axial force per member", default=[])
		_addProp("App::PropertyFloatList", "MinAxial", "Calc", "min axial force per member", default=[])
		_addProp("App::PropertyFloatList", "MinDeflectionY", "Calc", "min deflection Y per member", default=[])
		_addProp("App::PropertyFloatList", "MaxDeflectionY", "Calc", "max deflection Y per member", default=[])
		_addProp("App::PropertyFloatList", "MinDeflectionZ", "Calc", "min deflection Z per member", default=[])
		_addProp("App::PropertyFloatList", "MaxDeflectionZ", "Calc", "max deflection Z per member", default=[])
		
		_addProp("App::PropertyFloatList", "MemberLengths", "Calc", "list of member lengths", default=[])
		_addProp("App::PropertyString", "ActiveLoadCombination", "Result", "The load combination used for current results", default="")

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


	def _ensure_instance_state(self):
		"""Recreate transient instance attributes lost on FreeCAD document restore."""
		if not hasattr(self, 'builder') or self.builder is None:
			self.builder = ModelBuilder()

	def _ensure_properties(self, obj):
		"""Add properties that were introduced after the file was saved (backward compat)."""
		def _add_if_missing(prop_type, name, group, desc, default=None):
			if not hasattr(obj, name):
				try:
					obj.addProperty(prop_type, name, group, desc)
					if default is not None:
						setattr(obj, name, default)
				except Exception:
					pass

		# Reaction storage — added after initial release
		_add_if_missing("App::PropertyStringList", "ReactionNodes",    "Reactions", "List of node indices with reactions", [])
		_add_if_missing("App::PropertyFloatList",  "ReactionX",        "Reactions", "Reaction forces in X direction",      [])
		_add_if_missing("App::PropertyFloatList",  "ReactionY",        "Reactions", "Reaction forces in Y direction",      [])
		_add_if_missing("App::PropertyFloatList",  "ReactionZ",        "Reactions", "Reaction forces in Z direction",      [])
		_add_if_missing("App::PropertyFloatList",  "ReactionMX",       "Reactions", "Reaction moments about X axis",       [])
		_add_if_missing("App::PropertyFloatList",  "ReactionMY",       "Reactions", "Reaction moments about Y axis",       [])
		_add_if_missing("App::PropertyFloatList",  "ReactionMZ",       "Reactions", "Reaction moments about Z axis",       [])
		_add_if_missing("App::PropertyString",     "ReactionLoadCombo","Reactions", "Current load combination for reactions", "100_DL")

		# Reaction display — added after initial release
		_add_if_missing("App::PropertyBool",  "ShowReactions",          "Reaction Display", "Show reaction force visualizations", True)
		_add_if_missing("App::PropertyFloat", "ReactionScale",          "Reaction Display", "Scale factor for reaction arrows",   1.0)
		_add_if_missing("App::PropertyFloat", "ReactionTextOffset",     "Reaction Display", "Text offset distance",               500.0)
		_add_if_missing("App::PropertyFloat", "ReactionFontSize",       "Reaction Display", "Font size for reaction text",        200.0)
		_add_if_missing("App::PropertyBool",  "ShowReactionForces",     "Reaction Components", "Show reaction forces",   True)
		_add_if_missing("App::PropertyBool",  "ShowReactionMoments",    "Reaction Components", "Show reaction moments",  True)
		_add_if_missing("App::PropertyBool",  "ShowReactionResultant",  "Reaction Components", "Show resultant reaction", False)
		_add_if_missing("App::PropertyPythonObject", "ReactionTextShapes", "Internal", "Storage for reaction text shapes", [])

		# Diagram points — added after initial release
		_add_if_missing("App::PropertyInteger", "NumPointsMoment",     "Diagram Points", "Points for moment diagram",     5)
		_add_if_missing("App::PropertyInteger", "NumPointsAxial",      "Diagram Points", "Points for axial diagram",      3)
		_add_if_missing("App::PropertyInteger", "NumPointsShear",      "Diagram Points", "Points for shear diagram",      4)
		_add_if_missing("App::PropertyInteger", "NumPointsTorque",     "Diagram Points", "Points for torque diagram",     3)
		_add_if_missing("App::PropertyInteger", "NumPointsDeflection", "Diagram Points", "Points for deflection diagram", 4)

		# Member results — added after initial release
		_add_if_missing("App::PropertyPythonObject", "MemberResults", "Calc", "structured per-member results", [])

	# Maps structure nodes (inverts y and z axis to match solver coordinates)
	def mapNodes(self, elements, unitLength):
		self._ensure_instance_state()
		return self.builder.map_nodes(elements, unitLength)

	# Maps structure members 
	def mapMembers(self, elements, listNodes, unitLength):
		return self.builder.map_members(elements, listNodes, unitLength)

	# Creates nodes in the solver model
	def setNodes(self, model, nodes_map):
		return self.builder.set_nodes(model, nodes_map)

	# Creates members in the solver model
	def setMembers(self, model, members_map, selfWeight=True):
		return self.builder.set_members(model, members_map, selfWeight)

	# Get load factors based on load case or combination
	# Get load factors based on load case or combination
	def getLoadFactors(self, load_case_or_combination, load_type):
		"""Returns load factor for given load case/combination and load type"""
		# Delegate to LoadCombinationManager
		from .analysis.load_combination_manager import LoadCombinationManager
		# We can instantiate lazily or static, but clean is new instance or singleton
		manager = LoadCombinationManager()
		return manager.get_load_factor(load_case_or_combination, load_type)

	# Check wind/earthquake direction compatibility
	def checkDirectionCompatibility(self, load_combination, load_direction):
		return self.builder.check_direction_compatibility(load_combination, load_direction)

	# Sets up loads
	def setLoads(self, model, loads, nodes_map, unitForce, unitLength, load_combination):
		return self.builder.set_loads(model, loads, nodes_map, unitForce, unitLength, load_combination)

	# Sets up supports
	def setSuports(self, model, suports, nodes_map, unitLength):
		return self.builder.set_supports(model, suports, nodes_map, unitLength)

	def setMaterialAndSections(self, model, lines, unitLength, unitForce):
		return self.builder.set_materials_and_sections(model, lines, unitLength, unitForce)

	def merge_mesh_nodes(self, nodes_map, plate_meshes):
		"""Merge nodes from plate meshes into the global nodes map."""
		for mesh_data in plate_meshes:
			for tag, node in mesh_data['nodes'].items():
				# Node format from builder: {'x': val, 'y': val, 'z': val}
				# nodes_map format: [x, z, y]
				candidate = [round(node['x'], 4), round(node['z'], 4), round(node['y'], 4)]
				if candidate not in nodes_map:
					nodes_map.append(candidate)
		return nodes_map

	def split_members_at_intersections(self, members_map, nodes_map):
		"""Split members that are intersected by nodes."""
		new_members_map = []
		TOLERANCE = 1e-4
		
		for member in members_map:
			start_idx = member['NodeStart']
			end_idx = member['NodeEnd']
			
			P1 = App.Vector(nodes_map[start_idx][0], nodes_map[start_idx][2], nodes_map[start_idx][1])
			P2 = App.Vector(nodes_map[end_idx][0], nodes_map[end_idx][2], nodes_map[end_idx][1])
			
			member_length = (P2 - P1).Length
			if member_length < TOLERANCE:
				continue
				
			direction = (P2 - P1).normalize()
			intersecting_indices = []
			
			for i, node_coords in enumerate(nodes_map):
				if i == start_idx or i == end_idx:
					continue
				nx, nz, ny = node_coords
				min_x, max_x = min(P1.x, P2.x) - TOLERANCE, max(P1.x, P2.x) + TOLERANCE
				min_y, max_y = min(P1.y, P2.y) - TOLERANCE, max(P1.y, P2.y) + TOLERANCE
				min_z, max_z = min(P1.z, P2.z) - TOLERANCE, max(P1.z, P2.z) + TOLERANCE
				
				if not (min_x <= nx <= max_x and min_y <= ny <= max_y and min_z <= nz <= max_z):
					continue
					
				P_node = App.Vector(nx, ny, nz)
				vec_to_node = P_node - P1
				projection = vec_to_node.dot(direction)
				
				if 0 < projection < member_length:
					closest_point = P1 + direction * projection
					if (closest_point - P_node).Length < TOLERANCE:
						intersecting_indices.append((i, projection))
			
			if not intersecting_indices:
				new_members_map.append(member)
			else:
				intersecting_indices.sort(key=lambda x: x[1])
				current_start = start_idx
				
				for idx, dist in intersecting_indices:
					new_members_map.append({
						'NodeStart': current_start,
						'NodeEnd': idx,
						'Element': member['Element'],
						'IsSplit': True
					})
					current_start = idx
				
				new_members_map.append({
					'NodeStart': current_start,
					'NodeEnd': end_idx,
					'Element': member['Element'],
					'IsSplit': True
				})
				
		return new_members_map

	
	def execute(self, obj):
		self._ensure_instance_state()
		self._ensure_properties(obj)
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
		# Filters different element types
		lines = list(filter(lambda element: 'Line' in element.Name or 'Wire' in element.Name, obj.ListElements))
		loads = list(filter(lambda element: 'Load' in element.Name, obj.ListElements))
		suports = list(filter(lambda element: 'Suport' in element.Name, obj.ListElements))
		# Collect plate and area-load objects (StructuralPlate and AreaLoad)
		plates = list(filter(lambda element: getattr(element, 'Type', '') == 'StructuralPlate' or 'Plate' in element.Name, obj.ListElements))
		area_loads = list(filter(lambda element: getattr(element, 'Type', '') == 'AreaLoad' or 'AreaLoad' in element.Name, obj.ListElements))

		# =====================================================================
		# PHASE 3: INTEGRATED PLATE MESHING WORKFLOW
		# =====================================================================
		# 1. Map initial nodes from beam/column endpoints
		nodes_map = self.mapNodes(lines, obj.LengthUnit)
		
		# 2. Generate plate meshes BEFORE mapping members (to get all nodes)
		plate_meshes = []
		if plates:
			try:
				plate_meshes = self.builder.generate_plate_meshes(plates, obj.LengthUnit)
				_print_message(f"Generated meshes for {len(plate_meshes)} plates\n")
			except Exception as me:
				_print_warning(f"Plate mesh generation failed: {me}\n")
		
		# 3. Merge plate mesh nodes into global node map
		if plate_meshes:
			nodes_map = self.merge_mesh_nodes(nodes_map, plate_meshes)
			_print_message(f"Total nodes after mesh merge: {len(nodes_map)}\n")
		
		# 4. Map initial members
		members_map = self.mapMembers(lines, nodes_map, obj.LengthUnit)
		
		# 5. Split members at plate mesh node intersections
		if plate_meshes:
			original_member_count = len(members_map)
			members_map = self.split_members_at_intersections(members_map, nodes_map)
			_print_message(f"Members: {original_member_count} -> {len(members_map)} after splitting\n")
		# =====================================================================

		# Set up materials, nodes, and members
		model = self.setMaterialAndSections(model, lines, obj.LengthUnit, obj.ForceUnit)
		model = self.setNodes(model, nodes_map)
		
		# Handle self-weight setting with backwards compatibility
		use_self_weight = True  # Default to True
		if hasattr(obj, 'selfWeight'):
			use_self_weight = obj.selfWeight
		model = self.setMembers(model, members_map, use_self_weight)

		# ---- Add plates/quads to FE model ----
		# Use precomputed meshes if available
		model, self._plate_mesh_elements = self.builder.process_plates(
			model, plates, nodes_map, obj.LengthUnit, obj.ForceUnit, 
			precomputed_meshes=plate_meshes
		)
		
		# ---- Apply area loads to plates ----
		model = self.builder.process_area_loads(model, area_loads, self._plate_mesh_elements, obj.LengthUnit, obj.ForceUnit)


		
		# Use the selected load combination
		active_load_combination = obj.LoadCombination if hasattr(obj, 'LoadCombination') else '100_DL'
		_print_message(f"Starting analysis with LoadCombination: {active_load_combination}\n")
		

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

		# *** CRITICAL: Store the FE model for later access by reaction display features ***
		# Store on the Proxy (self) to ensure accessibility
		try:
			self.model = model
			_print_message(f"FE model stored successfully with {len(model.nodes)} nodes\n")
		except Exception as store_e:
			_print_warning(f"Could not store FE model: {store_e}\n")

		# Update analysis summary
		# Update analysis summary
		from .analysis.load_combination_manager import LoadCombinationManager
		analysis_type = LoadCombinationManager().get_analysis_type(active_load_combination)
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

		# Collect results using ResultManager
		try:
			from .analysis.result_manager import ResultManager
			# Initialize adapter and manager
			# Pass the existing Pynite model to the adapter
			result_manager = ResultManager(PyniteAdapter(model=self.model))
			# But calc.py still uses self.model.add_node etc directly in some places or via ModelBuilder.
			# ModelBuilder returns the raw model currently because PyniteAdapter wraps it newly?
			# Wait. ModelBuilder receives 'model'. 
			
			# Current flow:
			# calc.py line 408: model = FEModel3D()
			# calc.py line 462: model = self.mapNodes(lines...) -> delegates to builder which returns raw list
			# calc.py line 467: model = self.setNodes(model...) -> delegates to builder
			
			# Issue: ModelBuilder expects 'model' to provide .add_node etc. PyniteAdapter provides that.
			# FEModel3D provides that too.
			# ResultManager expects 'solver' which is PyniteAdapter (wrapping model).
			
			# Solution: Wrap the existing raw model in the Adapter just for results?
			# PyniteAdapter.__init__ creates a NEW FEModel3D(). We need to inject the existing one.
			
			if model is None:
				_print_warning("FE model is None after analysis — skipping result extraction\n")
				return

			adapter = PyniteAdapter()
			adapter.model = model  # Inject populated model into adapter

			result_manager = ResultManager(adapter)
			
			# Configuration for result points
			config = {
				'moment': getattr(obj, 'NumPointsMoment', 5),
				'shear': getattr(obj, 'NumPointsShear', 4),
				'axial': getattr(obj, 'NumPointsAxial', 3),
				'torque': getattr(obj, 'NumPointsTorque', 3),
				'deflection': getattr(obj, 'NumPointsDeflection', 4)
			}
			_print_message(f"Processing results for combination: {active_load_combination}\n")
			result_manager.prepare_results_for_object(obj, active_load_combination, config)
			
		except Exception as e:
			_print_warning(f"Result processing failed: {e}\n")
			import traceback
			_print_warning(traceback.format_exc())



			# Also collect structured numeric results for this member (lists of floats)

		
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
		# Safely get the Object reference - it might not exist during restoration
		if hasattr(obj, 'Object'):
			self.Object = obj.Object
		else:
			self.Object = None
		self.reaction_texts = []  # Store reaction text objects
	
	def attach(self, obj):
		"""Called when the view provider is attached to an object"""
		if hasattr(obj, 'Object'):
			self.Object = obj.Object
	
	def updateData(self, obj, prop):
		"""Called when the object's data changes"""
		# Handle reaction text display properties
		if prop in ['ShowReactionText', 'ReactionPrecision', 'ReactionTextOffset', 'ReactionFontSize', 'LoadCombination']:
			self.updateReactionTextDisplay()
		
		# Handle reaction component display properties
		if prop in ['ShowReactionResultant', 'ShowReactionForces', 'ShowReactionMoments']:
			self.updateReactionTextDisplay()
	
	def onChanged(self, obj, prop):
		"""Called when view properties change"""
		if prop == 'ShowReactionText':
			self.updateReactionTextDisplay()
	
	def updateReactionTextDisplay(self):
		"""Update the display of reaction texts based on ShowReactionText property"""
		try:
			# Check if we have the necessary attributes
			if not hasattr(self, 'reaction_texts'):
				self.reaction_texts = []
			
			if not hasattr(self, 'Object') or self.Object is None:
				return
			
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
			if not model:
				return
			
			# Check for nodes (PyNite uses lowercase 'nodes', but FreeCAD sometimes uses 'Nodes')
			nodes_dict = None
			if hasattr(model, 'nodes') and model.nodes:
				nodes_dict = model.nodes
			elif hasattr(model, 'Nodes') and model.Nodes:
				nodes_dict = model.Nodes
			
			if not nodes_dict:
				return
			
			# Get display properties
			precision = getattr(self.Object, 'ReactionPrecision', 2)
			offset = getattr(self.Object, 'ReactionTextOffset', 100.0)  # mm
			font_size = getattr(self.Object, 'ReactionFontSize', 12.0)
			active_combination = getattr(self.Object, 'LoadCombination', '100_DL')
			
			# Iterate through nodes to find supports with reactions
			for node_name, node in nodes_dict.items():
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
		
		# Get display preferences
		show_forces = getattr(self.Object, 'ShowReactionForces', True)
		show_moments = getattr(self.Object, 'ShowReactionMoments', True)
		show_resultant = getattr(self.Object, 'ShowReactionResultant', False)
		
		# Format forces if enabled
		if show_forces:
			force_lines = []
			for component in ['FX', 'FY', 'FZ']:
				if component in reactions:
					value = reactions[component]
					if abs(value) > 1e-6:  # Only show significant values
						force_lines.append(f"{component}: {value:.{precision}f} kN")
			
			if force_lines:
				lines.extend(force_lines)
		
		# Format moments if enabled
		if show_moments:
			moment_lines = []
			for component in ['MX', 'MY', 'MZ']:
				if component in reactions:
					value = reactions[component]
					if abs(value) > 1e-6:  # Only show significant values
						moment_lines.append(f"{component}: {value:.{precision}f} kN·m")
			
			if moment_lines:
				lines.extend(moment_lines)
		
		# Calculate and display resultant force if enabled
		if show_resultant:
			fx = reactions.get('FX', 0.0)
			fy = reactions.get('FY', 0.0)
			fz = reactions.get('FZ', 0.0)
			resultant = (fx**2 + fy**2 + fz**2)**0.5
			if abs(resultant) > 1e-6:
				lines.append(f"Resultant: {resultant:.{precision}f} kN")
		
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
			# Ensure reaction_texts attribute exists
			if not hasattr(self, 'reaction_texts'):
				self.reaction_texts = []
				return
			
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
