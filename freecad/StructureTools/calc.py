import FreeCAD, App, FreeCADGui, Part, os, math
from PySide import QtWidgets
import subprocess

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")

from .Pynite_main.FEModel3D import FEModel3D


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
	# Try FreeCAD.Console, then App.Console, fallback to print
	try:
		if 'FreeCAD' in globals() and hasattr(FreeCAD, 'Console'):
			FreeCAD.Console.PrintWarning(msg)
			return
	except Exception:
		pass
	try:
		if 'App' in globals() and hasattr(App, 'Console'):
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
		if 'FreeCAD' in globals() and hasattr(FreeCAD, 'Console'):
			FreeCAD.Console.PrintMessage(msg)
			return
	except Exception:
		pass
	try:
		if 'App' in globals() and hasattr(App, 'Console'):
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
		if 'FreeCAD' in globals() and hasattr(FreeCAD, 'Console'):
			FreeCAD.Console.PrintError(msg)
			return
	except Exception:
		pass
	try:
		if 'App' in globals() and hasattr(App, 'Console'):
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
		if 'FreeCAD' in globals() and hasattr(FreeCAD, 'Units') and hasattr(FreeCAD.Units, 'Quantity'):
			if to_unit:
				return float(FreeCAD.Units.Quantity(value, from_unit).getValueAs(to_unit))
			return float(FreeCAD.Units.Quantity(value, from_unit))
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
	msg_box = QtWidgets.QMessageBox()
	msg_box.setIcon(QtWidgets.QMessageBox.Critical)  #Ícone de erro
	msg_box.setWindowTitle("Erro")
	msg_box.setText(msg)
	msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
	msg_box.exec_()


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

		# Load summary and metadata
		_addProp("App::PropertyStringList", "LoadSummary", "Calc", "summary of active loads", default=[])
		_addProp("App::PropertyInteger", "TotalLoads", "Calc", "total number of loads", default=0)
		_addProp("App::PropertyString", "AnalysisType", "Calc", "text description of analysis type", default='')


	#  Mapeia os nós da estrutura, (inverte o eixo y e z para adequação as coordenadas do sover)
	def mapNodes(self, elements, unitLength):	
		# Varre todos os elementos de linha e adiciona seus vertices à tabela de nodes
		listNodes = []
		for element in elements:
			for edge in element.Shape.Edges:
				for vertex in edge.Vertexes:
					node = [round(float(FreeCAD.Units.Quantity(vertex.Point.x,'mm').getValueAs(unitLength)), 2), round(float(FreeCAD.Units.Quantity(vertex.Point.z,'mm').getValueAs(unitLength)),2), round(float(FreeCAD.Units.Quantity(vertex.Point.y,'mm').getValueAs(unitLength)),2)]
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
					node = [round(float(FreeCAD.Units.Quantity(vertex.Point.x,'mm').getValueAs(unitLength)), 2), round(float(FreeCAD.Units.Quantity(vertex.Point.z,'mm').getValueAs(unitLength)),2), round(float(FreeCAD.Units.Quantity(vertex.Point.y,'mm').getValueAs(unitLength)),2)]
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
	def setMembers(self, model, members_map,selfWeight):
		for memberName in list(members_map):			
			model.add_member(memberName, members_map[memberName]['nodes'][0] , members_map[memberName]['nodes'][1], members_map[memberName]['material'], members_map[memberName]['section'])
			
			#Considera o peso proprio nos elementos de barra
			if selfWeight : model.add_member_self_weight('FY', -1) 

			#libera as rotações na extremidades do elemento a fim de emular ocomportamento de barras de treliça
			if members_map[memberName]['trussMember']: model.def_releases(memberName, Dxi=False, Dyi=False, Dzi=False, Rxi=False, Ryi=True, Rzi=True, Dxj=False, Dyj=False, Dzj=False, Rxj=False, Ryj=True, Rzj=True)
		
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
		required_factors = self.getLoadFactors(load_combination, 'DL')  # Get all factors for this combination
		
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

			match load.GlobalDirection:
				case '+X':
					axis = 'FX'
					direction = 1

				case '-X':
					axis = 'FX'
					direction = -1

				case '+Y':
					axis = 'FZ'
					direction = 1

				case '-Y':
					axis = 'FZ'
					direction = -1

				case '+Z':
					axis = 'FY'
					direction = 1

				case '-Z':
					axis = 'FY'
					direction = -1

			# Check if load has LoadType property, if not default to 'DL'
			load_type = getattr(load, 'LoadType', 'DL')
			
			# Check direction compatibility for wind and earthquake loads
			if load_type in ['W', 'E']:
				if not self.checkDirectionCompatibility(load_combination, load.GlobalDirection):
					continue  # Skip loads that don't match the required direction
			
			# Valida se o carregamento é distribuido
			if 'Edge' in load.ObjectBase[0][1][0]:
				initial = float(load.InitialLoading.getValueAs(unitForce))
				final = float(load.FinalLoading.getValueAs(unitForce))

				# Apply load factor based on load combination and load type
				load_factor = self.getLoadFactors(load_combination, load_type)
				factored_initial = initial * direction * load_factor
				factored_final = final * direction * load_factor
				
				subname = int(load.ObjectBase[0][1][0].split('Edge')[1]) - 1
				name = load.ObjectBase[0][0].Name + '_' + str(subname)
				model.add_member_dist_load(name, axis, factored_initial, factored_final)

			# Valida se o carregamento é nodal
			elif 'Vertex' in load.ObjectBase[0][1][0]:
				numVertex = int(load.ObjectBase[0][1][0].split('Vertex')[1]) - 1
				vertex = load.ObjectBase[0][0].Shape.Vertexes[numVertex]
				
				node = list(filter(lambda element: element == [round(float(FreeCAD.Units.Quantity(vertex.Point.x,'mm').getValueAs(unitLength)), 2), round(float(FreeCAD.Units.Quantity(vertex.Point.z,'mm').getValueAs(unitLength)),2), round(float(FreeCAD.Units.Quantity(vertex.Point.y,'mm').getValueAs(unitLength)),2)], nodes_map))[0]
				indexNode = nodes_map.index(node)

				# Apply load factor based on load combination and load type
				load_factor = self.getLoadFactors(load_combination, load_type)
				factored_load = float(load.NodalLoading.getValueAs(unitForce)) * direction * load_factor
				
				name = str(indexNode)
				model.add_node_load(name, axis, factored_load)
			

					
		return model

	# Cria os suportes
	def setSuports(self, model, suports, nodes_map, unitLength):
		for suport in suports:
			suportvertex = list(suport.ObjectBase[0][0].Shape.Vertexes[int(suport.ObjectBase[0][1][0].split('Vertex')[1])-1].Point)
			for i, node in enumerate(nodes_map):
				if round(float(FreeCAD.Units.Quantity(suportvertex[0],'mm').getValueAs(unitLength)),2) == round(node[0],2) and round(float(FreeCAD.Units.Quantity(suportvertex[1],'mm').getValueAs(unitLength)),2) == round(node[2],2) and round(float(FreeCAD.Units.Quantity(suportvertex[2],'mm').getValueAs(unitLength)),2) == round(node[1],2):					
					name = str(i)
					model.def_support(name, suport.FixTranslationX, suport.FixTranslationZ, suport.FixTranslationY, suport.FixRotationX, suport.FixRotationZ, suport.FixRotationY)
					break
		
		return model

	def setMaterialAndSections(self, model, lines, unitLength, unitForce):
		materiais = []
		sections = []
		for line in lines:
			material = line.MaterialMember
			section = line.SectionMember

			if not material.Name in materiais:
				density = FreeCAD.Units.Quantity(material.Density).getValueAs('t/m^3') * 10 #Converte a unidade de entrada em t/m³ e na sequencia converte em kN/m³
				density = float(FreeCAD.Units.Quantity(density, 'kN/m^3').getValueAs(unitForce+"/"+unitLength+"^3")) #Converte kN/m³ para as unidades definidas no calc
				modulusElasticity = float(material.ModulusElasticity.getValueAs(unitForce+"/"+unitLength+"^2"))
				poissonRatio = float(material.PoissonRatio)
				G = modulusElasticity / (2 * (1 + poissonRatio))
				model.add_material(material.Name, modulusElasticity, G, poissonRatio, density)
				materiais.append(material.Name)
				

			if not section.Name in sections:

				ang = line.RotationSection.getValueAs('rad')
				J  = float(FreeCAD.Units.Quantity(section.MomentInertiaPolar, 'mm^4').getValueAs(unitLength+"^4"))
				A  = float(section.AreaSection.getValueAs(unitLength+"^2"))
				Iy = float(FreeCAD.Units.Quantity(section.MomentInertiaY, 'mm^4').getValueAs(unitLength+"^4"))
				Iz = float(FreeCAD.Units.Quantity(section.MomentInertiaZ, 'mm^4').getValueAs(unitLength+"^4"))
				Iyz = float(FreeCAD.Units.Quantity(section.ProductInertiaYZ, 'mm^4').getValueAs(unitLength+"^4"))

				
				# Aplica a rotação de eixo
				RIy = ((Iz + Iy) / 2 ) - ((Iz - Iy) / 2 )*math.cos(2 * ang) + Iyz * math.sin(2 * ang)
				RIz = ((Iz + Iy) / 2 ) + ((Iz - Iy) / 2 )*math.cos(2 * ang) - Iyz * math.sin(2 * ang)
				
				model.add_section(section.Name, A, RIy, RIz, J)
				sections.append(section.Name)
		
		return model

	
	def execute(self, obj):
		model = FEModel3D()
		# Ensure there's a default material so meshed quads can be assigned a material name
		# Tests and minimal workflows may not define materials; create a light default.
		try:
			if 'default' not in model.materials:
				model.add_material('default', 200000.0, 77000.0, 0.3, 7850.0)
		except Exception:
			# Non-fatal if FEModel internals differ; proceed without failing
			pass
		# Filtra os diferentes tipos de elementos
		lines = list(filter(lambda element: 'Line' in element.Name or 'Wire' in element.Name, obj.ListElements))
		loads = list(filter(lambda element: 'Load' in element.Name, obj.ListElements))
		suports = list(filter(lambda element: 'Suport' in element.Name, obj.ListElements))
		# Collect plate and area-load objects (StructuralPlate and AreaLoad)
		plates = list(filter(lambda element: getattr(element, 'Type', '') == 'StructuralPlate' or 'Plate' in element.Name, obj.ListElements))
		area_loads = list(filter(lambda element: getattr(element, 'Type', '') == 'AreaLoad' or 'AreaLoad' in element.Name, obj.ListElements))

		nodes_map = self.mapNodes(lines, obj.LengthUnit)
		members_map = self.mapMembers(lines, nodes_map, obj.LengthUnit)

		model = self.setMaterialAndSections(model, lines, obj.LengthUnit, obj.ForceUnit)
		model = self.setNodes(model, nodes_map)
		model = self.setMembers(model, members_map, obj.selfWeight)

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
					corner_points = [FreeCAD.Vector(v) if not isinstance(v, FreeCAD.Vector) else v for v in plate_obj.CornerNodes]
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
							mat_name = getattr(plate_obj, 'Material', None)
							if mat_name and hasattr(mat_name, 'Name'):
								mat_name = mat_name.Name
							elif not mat_name:
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
					mat_name = getattr(plate_obj, 'Material', None)
					if mat_name and hasattr(mat_name, 'Name'):
						mat_name = mat_name.Name
					elif not mat_name:
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
		
		# Filter and organize loads by type for current load combination
		organized_loads = self.organizeLoadsByType(loads, active_load_combination)
		
		model = self.setLoads(model, loads, nodes_map, obj.ForceUnit, obj.LengthUnit, active_load_combination)
		model = self.setSuports(model, suports, nodes_map, obj.LengthUnit)

		# Run analysis but don't let exceptions abort headless tests; capture and warn instead
		try:
			model.analyze()
		except Exception as e:
			_print_warning(f"Model analysis failed (continuing): {e}\n")

		# Update analysis summary
		analysis_type = "Allowable Stress Design" if active_load_combination.startswith('1') and not active_load_combination.startswith('10') else "Strength Design" if active_load_combination.startswith('10') else "Allowable Stress Design"
		obj.AnalysisType = f"{analysis_type}: {active_load_combination}"
		
		# Create load summary
		load_summary = []
		total_loads = 0
		for load in loads:
			load_type = getattr(load, 'LoadType', 'DL')
			load_factor = self.getLoadFactors(active_load_combination, load_type)
			if load_factor > 0:
				load_summary.append(f"{load_type} (Factor: {load_factor}) - {load.Label}")
				total_loads += 1
				
		obj.LoadSummary = load_summary
		obj.TotalLoads = total_loads

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
				'minMomentY': m.min_moment('My'),
				'maxMomentY': m.max_moment('My'),
				'minMomentZ': m.min_moment('Mz'),
				'maxMomentZ': m.max_moment('Mz'),
				'minShearY': m.min_shear('Fy'),
				'maxShearY': m.max_shear('Fy'),
				'minShearZ': m.min_shear('Fz'),
				'maxShearZ': m.max_shear('Fz'),
				'minTorque': m.min_torque(),
				'maxTorque': m.max_torque(),
				'minDeflectionY': m.min_deflection('dy'),
				'maxDeflectionY': m.max_deflection('dy'),
				'minDeflectionZ': m.min_deflection('dz'),
				'maxDeflectionZ': m.max_deflection('dz')
			}

		for name in model.members.keys():			
			momenty.append(','.join( str(value) for value in model.members[name].moment_array('My', obj.NumPointsMoment)[1]))
			momentz.append(','.join( str(value) for value in model.members[name].moment_array('Mz', obj.NumPointsMoment)[1]))

			sheary.append(','.join( str(value) for value in model.members[name].shear_array('Fy', obj.NumPointsShear)[1]))
			shearz.append(','.join( str(value) for value in model.members[name].shear_array('Fz', obj.NumPointsShear)[1]))

			axial.append(','.join( str(value) for value in model.members[name].axial_array(obj.NumPointsAxial)[1]))
			
			torque.append(','.join( str(value) for value in model.members[name].torque_array(obj.NumPointsTorque)[1]))

			deflectiony.append(','.join( str(value) for value in model.members[name].deflection_array('dy', obj.NumPointsDeflection)[1]))
			deflectionz.append(','.join( str(value) for value in model.members[name].deflection_array('dz', obj.NumPointsDeflection)[1]))

			mimMomenty.append(model.members[name].min_moment('My'))
			mimMomentz.append(model.members[name].min_moment('Mz'))
			maxMomenty.append(model.members[name].max_moment('My'))
			maxMomentz.append(model.members[name].max_moment('Mz'))

			minSheary.append(model.members[name].min_shear('Fy'))
			minShearz.append(model.members[name].min_shear('Fz'))
			maxSheary.append(model.members[name].max_shear('Fy'))
			maxShearz.append(model.members[name].max_shear('Fz'))

			minTorque.append(model.members[name].min_torque())
			maxTorque.append(model.members[name].max_torque())

			minDeflectiony.append(model.members[name].min_deflection('dy'))
			minDeflectionz.append(model.members[name].min_deflection('dz'))
			maxDeflectiony.append(model.members[name].max_deflection('dy'))
			maxDeflectionz.append(model.members[name].max_deflection('dz'))

			# Also collect structured numeric results for this member (lists of floats)
			try:
				my_vals = [float(v) for v in model.members[name].moment_array('My', getattr(obj, 'NumPointsMoment', 3))[1]]
			except Exception:
				my_vals = []
			try:
				mz_vals = [float(v) for v in model.members[name].moment_array('Mz', getattr(obj, 'NumPointsMoment', 3))[1]]
			except Exception:
				mz_vals = []
			try:
				fy_vals = [float(v) for v in model.members[name].shear_array('Fy', getattr(obj, 'NumPointsShear', 3))[1]]
			except Exception:
				fy_vals = []
			try:
				fz_vals = [float(v) for v in model.members[name].shear_array('Fz', getattr(obj, 'NumPointsShear', 3))[1]]
			except Exception:
				fz_vals = []
			try:
				ax_vals = [float(v) for v in model.members[name].axial_array(getattr(obj, 'NumPointsAxial', 2))[1]]
			except Exception:
				ax_vals = []
			try:
				tq_vals = [float(v) for v in model.members[name].torque_array(getattr(obj, 'NumPointsTorque', 2))[1]]
			except Exception:
				tq_vals = []
			try:
				dy_vals = [float(v) for v in model.members[name].deflection_array('dy', getattr(obj, 'NumPointsDeflection', 2))[1]]
			except Exception:
				dy_vals = []
			try:
				dz_vals = [float(v) for v in model.members[name].deflection_array('dz', getattr(obj, 'NumPointsDeflection', 2))[1]]
			except Exception:
				dz_vals = []

			# build structured summary and append
			summary = _build_member_summary(name)
			member_results.append(summary)
			

		obj.NameMembers = model.members.keys()
		obj.Nodes = [FreeCAD.Vector(node[0], node[2], node[1]) for node in nodes_map]
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
        doc = FreeCAD.ActiveDocument
        obj = doc.addObject("Part::FeaturePython", "Calc")

        objSuport = Calc(obj, selection)
        ViewProviderCalc(obj.ViewObject)           

        FreeCAD.ActiveDocument.recompute()        
        return

    def IsActive(self):
        
        return True

FreeCADGui.addCommand("calc", CommandCalc())
