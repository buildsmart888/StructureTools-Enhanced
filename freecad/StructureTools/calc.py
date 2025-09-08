import os, math
import sys

# Setup FreeCAD stubs for standalone operation
try:
	from .utils.freecad_stubs import setup_freecad_stubs, is_freecad_available
	if not is_freecad_available():
		setup_freecad_stubs()
except ImportError:
	pass

# Import utility functions
try:
	from .calc_utils import _find_matching_node_index
except ImportError:
	# Fallback implementation if calc_utils.py is not available
	def _find_matching_node_index(nodes_map, target_node, tol=1e-6):
		"""Find index of node in nodes_map that matches target_node within tolerance"""
		import math
		for i, node in enumerate(nodes_map):
			# Calculate Euclidean distance between nodes
			dist = math.sqrt(sum((a - b)**2 for a, b in zip(node, target_node)))
			if dist < tol:
				return i
		return None

# Import FreeCAD modules (now available via stubs if needed)
try:
	import FreeCAD
	import FreeCADGui
	import Part
	FREECAD_AVAILABLE = True
except ImportError:
	FreeCAD = None
	FreeCADGui = None
	FREECAD_AVAILABLE = False
	print("FreeCAD modules not available - using stub mode")

# Ensure 'App' alias exists for legacy code that references App.*
try:
	import App as _App
	App = _App
except Exception:
	# If App not available, set App to FreeCAD (may be None in stub mode)
	App = FreeCAD

# Import Qt modules with better fallback handling
QtWidgets = None
QMessageBox = None

# Try to import Qt modules in order of preference
qt_imported = False

# Try PySide2 first (most common in modern FreeCAD)
try:
	from PySide2 import QtWidgets
	from PySide2.QtWidgets import QMessageBox
	qt_imported = True
except ImportError:
	pass

# Try PySide (older FreeCAD versions)
if not qt_imported:
	try:
		from PySide import QtGui as QtWidgets
		from PySide.QtGui import QMessageBox
		qt_imported = True
	except ImportError:
		pass

# Try PyQt5
if not qt_imported:
	try:
		from PyQt5 import QtWidgets
		from PyQt5.QtWidgets import QMessageBox
		qt_imported = True
	except ImportError:
		pass

# Try PyQt4 (oldest)
if not qt_imported:
	try:
		from PyQt4 import QtGui as QtWidgets
		from PyQt4.QtGui import QMessageBox
		qt_imported = True
	except ImportError:
		pass

# If no Qt modules are available, set to None
if not qt_imported:
	QtWidgets = None
	QMessageBox = None
	print("No Qt modules available")

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
		if FreeCAD is not None and hasattr(FreeCAD, 'Console'):
			FreeCAD.Console.PrintWarning(msg)
			return
	except Exception:
		pass
	try:
		print('WARNING:', msg)
	except Exception:
		pass


def _print_message(msg):
	try:
		if FreeCAD is not None and hasattr(FreeCAD, 'Console'):
			FreeCAD.Console.PrintMessage(msg)
			return
	except Exception:
		pass
	try:
		print(msg)
	except Exception:
		pass


def _print_error(msg):
	try:
		if FreeCAD is not None and hasattr(FreeCAD, 'Console'):
			FreeCAD.Console.PrintError(msg)
			return
	except Exception:
		pass
	try:
		print('ERROR:', msg)
	except Exception:
		pass


# helper to convert FreeCAD.Quantity or numeric values to float in desired units
def qty_val(value, from_unit='mm', to_unit=None):
	"""Convert quantity values with units, with fallback handling"""
	# Import FreeCAD modules safely
	FreeCAD = None
	try:
		import FreeCAD
	except ImportError:
		try:
			import App as FreeCAD
		except ImportError:
			FreeCAD = None
    
	# Prefer FreeCAD Units when available
	try:
		if FreeCAD is not None and hasattr(FreeCAD, 'Units') and hasattr(FreeCAD.Units, 'Quantity'):
			# Handle different types of input values
			if isinstance(value, (int, float)):
				# Create quantity using string format to avoid constructor issues
				quantity_str = f"{value} {from_unit}"
				quantity = FreeCAD.Units.Quantity(quantity_str)
			elif hasattr(value, 'getValueAs'):
				# It's already a Quantity object
				quantity = value
			else:
				# Try to convert string or other types
				quantity_str = str(value)
				if ' ' not in quantity_str and from_unit:
					# If no unit in string, add the from_unit
					quantity_str = f"{quantity_str} {from_unit}"
				quantity = FreeCAD.Units.Quantity(quantity_str)
            
			if to_unit:
				# Convert to target unit
				converted_value = quantity.getValueAs(to_unit)
				return float(converted_value)
			return float(quantity.Value)
	except Exception as e:
		# If FreeCAD units fail, continue to fallback
		pass
    
	# Fallback: try numeric or MockQuantity
	try:
		if hasattr(value, 'Value'):  # Check for Value attribute first
			return float(value.Value)
		elif hasattr(value, 'value'):  # Then check for value attribute
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
	if QtWidgets is not None and QMessageBox is not None:
		msg_box = QMessageBox()
		msg_box.setIcon(QMessageBox.Critical)
		msg_box.setWindowTitle("Error")
		msg_box.setText(msg)
		msg_box.setStandardButtons(QMessageBox.Ok)
		msg_box.exec_()
	else:
		print("Error:", msg)

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

		# Unit properties with proper defaults and enumeration
		_addProp("App::PropertyEnumeration", "LengthUnit", "Calc", "set the length unit for calculation")
		if hasattr(obj, 'addProperty'):
			obj.LengthUnit = ['m', 'mm', 'cm']
			obj.LengthUnit = 'm'  # default
		else:
			obj.LengthUnit = 'm'
			
		_addProp("App::PropertyEnumeration", "ForceUnit", "Calc", "set the force unit for calculation") 
		if hasattr(obj, 'addProperty'):
			obj.ForceUnit = ['kN', 'N', 'kgf', 'tf']  # เพิ่ม kgf และ tf
			obj.ForceUnit = 'kN'  # default
		else:
			obj.ForceUnit = 'kN'
			
		# Add moment unit property (derived from force and length)
		_addProp("App::PropertyString", "MomentUnit", "Calc", "moment unit (derived from force and length)", default='kN·m')
		_addProp("App::PropertyBool", "selfWeight", "Calc", "include self weight in analysis", default=False)
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

			# Determine axis and direction based on GlobalDirection
			axis = 'FX'  # Default
			direction = 1  # Default

			# Handle force directions (forces and moments)
			if load.GlobalDirection in ['+X', '+x']:
				axis = 'FX' if load.GlobalDirection[1].isupper() else 'Fx'
				direction = 1
			elif load.GlobalDirection in ['-X', '-x']:
				axis = 'FX' if load.GlobalDirection[1].isupper() else 'Fx'
				direction = -1
			elif load.GlobalDirection in ['+Y', '+y']:
				axis = 'FZ' if load.GlobalDirection[1].isupper() else 'Fz'
				direction = 1
			elif load.GlobalDirection in ['-Y', '-y']:
				axis = 'FZ' if load.GlobalDirection[1].isupper() else 'Fz'
				direction = -1
			elif load.GlobalDirection in ['+Z', '+z']:
				axis = 'FY' if load.GlobalDirection[1].isupper() else 'Fy'
				direction = 1
			elif load.GlobalDirection in ['-Z', '-z']:
				axis = 'FY' if load.GlobalDirection[1].isupper() else 'Fy'
				direction = -1
			elif load.GlobalDirection in ['+My', '-My']:
				axis = 'Mz' if load.GlobalDirection[0] == '+' else '-Mz'
				direction = 1 if load.GlobalDirection[0] == '+' else -1
			elif load.GlobalDirection in ['+Mz', '-Mz']:
				axis = 'My' if load.GlobalDirection[0] == '+' else '-My'
				direction = 1 if load.GlobalDirection[0] == '+' else -1
			elif load.GlobalDirection in ['+Mx', '-Mx']:
				axis = 'Mx'
				direction = 1 if load.GlobalDirection[0] == '+' else -1

			# Check direction compatibility for wind and earthquake loads
			if load_type in ['W', 'E']:
				if not self.checkDirectionCompatibility(load_combination, load.GlobalDirection):
					continue  # Skip loads that don't match the required direction
			
			# Valida se o carregamento é distribuido
			if 'Edge' in load.ObjectBase[0][1][0] and hasattr(load, 'InitialLoading'):
				initial = float(load.InitialLoading.getValueAs(unitForce))
				final = float(load.FinalLoading.getValueAs(unitForce))

				# Apply load factor based on load combination and load type
				factored_initial = initial * direction * load_factor
				factored_final = final * direction * load_factor
				
				subname = int(load.ObjectBase[0][1][0].split('Edge')[1]) - 1
				name = load.ObjectBase[0][0].Name + '_' + str(subname)
				
				# Check if start and end positions are specified, otherwise use full length
				x1 = None
				x2 = None
				if hasattr(load, 'StartPosition') and hasattr(load, 'EndPosition'):
					# Only use start/end positions if they are not both zero (which would indicate full length)
					if load.StartPosition.Value != 0.0 or load.EndPosition.Value != 0.0:
						x1 = float(load.StartPosition.getValueAs(unitLength))
						x2 = float(load.EndPosition.getValueAs(unitLength))
				
				model.add_member_dist_load(name, axis, factored_initial, factored_final, x1, x2, case=load_type)

			# Valida se o carregamento é pontual (point load) em membro
			elif 'Edge' in load.ObjectBase[0][1][0] and hasattr(load, 'PointLoading'):
				# This is a point load on a member
				force = float(load.PointLoading.getValueAs(unitForce))
				
				# Apply load factor based on load combination and load type
				factored_load = force * direction * load_factor
				
				subname = int(load.ObjectBase[0][1][0].split('Edge')[1]) - 1
				name = load.ObjectBase[0][0].Name + '_' + str(subname)
				
				# Get position along member (default to 0.5 if not specified)
				position_ratio = getattr(load, 'RelativePosition', 0.5)
				# Clamp position between 0.0 and 1.0
				position_ratio = max(0.0, min(1.0, position_ratio))
				
				# Calculate actual position in member length units
				member_length = model.members[name].L()
				x_position = position_ratio * member_length
				
				# For moments, we need to use the appropriate moment axis
				load_axis = axis
				if axis in ['My', '-My', 'Mz', '-Mz', 'Mx']:
					# Moments use different axis notation
					if axis == 'My':
						load_axis = 'MZ'
					elif axis == '-My':
						load_axis = 'MZ'
						factored_load *= -1
					elif axis == 'Mz':
						load_axis = 'MY'
					elif axis == '-Mz':
						load_axis = 'MY'
						factored_load *= -1
					elif axis == 'Mx':
						load_axis = 'MX'
				
				model.add_member_pt_load(name, load_axis, factored_load, x_position, case=load_type)

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
				A  = float(section.Area.getValueAs(unitLength+"^2"))
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
		# Store the model as an attribute so tests can access it
		self.model = model
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
		for plate_obj in plates:
			# Try to use object-level exporter first (preferred)
			payload = None
			try:
				if hasattr(plate_obj, 'Proxy') and hasattr(plate_obj.Proxy, 'to_calc_payload'):
					payload = plate_obj.Proxy.to_calc_payload(plate_obj, length_unit=obj.LengthUnit)
			except Exception as e:
				_print_warning(f"to_calc_payload failed for plate '{getattr(plate_obj, 'Name', '')}': {e}\n")

			# If we got a mesh payload, add mesh nodes/elements to model (try to reuse existing nodes_map)
			if payload and payload.get('elements'):
				node_id_map = {}
				created_elems = []
				for tag, coord in payload.get('nodes', {}).items():
					try:
						x = float(coord.get('x', 0))
						y = float(coord.get('y', 0))
						z = float(coord.get('z', 0))
						coord_rounded = [round(x, 2), round(z, 2), round(y, 2)]
						match_idx = _find_matching_node_index(nodes_map, coord_rounded, tol=1e-2)
						if match_idx is not None:
							node_name = str(match_idx)
							node_id_map[str(tag)] = node_name
							continue
						# add new node
						try:
							node_name = model.add_node(None, x, y, z)
							node_id_map[str(tag)] = node_name
						except Exception as e:
							_print_warning(f"Could not add mesh node {tag}: {e}\n")
					except Exception:
						# skip this node on any parsing error
						continue

				# Add elements
				for eid, elem in payload.get('elements', {}).items():
					nodes = elem.get('nodes', [])
					if len(nodes) < 3:
						_print_warning(f"Mesh element {eid} has insufficient nodes; skipping\n")
						continue
					if len(nodes) == 3:
						nodes = nodes + [nodes[2]]
					i_n = node_id_map.get(str(nodes[0]))
					j_n = node_id_map.get(str(nodes[1]))
					m_n = node_id_map.get(str(nodes[2]))
					n_n = node_id_map.get(str(nodes[3]))
					if None in (i_n, j_n, m_n, n_n):
						_print_warning(f"Mesh element {eid} references unknown nodes; skipping\n")
						continue
					# thickness
					thk = payload.get('thickness', getattr(plate_obj, 'Thickness', 0.1))
					try:
						thk = qty_val(thk, 'mm', obj.LengthUnit)
					except Exception:
						try:
							thk = float(thk)
						except Exception:
							thk = 0.1
					# material
					mat_name = payload.get('material', 'default') or 'default'
					if mat_name not in materiais:
						# best-effort: add a default material to avoid missing reference
						try:
							model.add_material(mat_name, 200000.0, 77000.0, 0.3, 78.5)
							materiais.append(mat_name)
						except Exception:
							_print_warning(f"Could not add material {mat_name} for plate '{plate_obj.Name}'\n")
					# create element name
					elem_name = f"{plate_obj.Name}_{eid}"
					try:
						model.add_quad(elem_name, i_n, j_n, m_n, n_n, float(thk), mat_name)
						created_elems.append(elem_name)
					except Exception as e:
						_print_warning(f"Could not add mesh element {eid}: {e}\n")

				# record created element names so area loads can be mapped later
				if created_elems:
					if not hasattr(self, '_plate_mesh_elements'):
						self._plate_mesh_elements = {}
					self._plate_mesh_elements[plate_obj.Name] = created_elems

			else:
				# Fallback to previous behavior (corner nodes / add_plate)
				# Try to get corner vertices from the object's Shape (if available) or use a property named CornerNodes
				try:
					shape = plate_obj.Shape
				except Exception:
					shape = None

				corner_indices = None
				if hasattr(plate_obj, 'CornerNodes') and plate_obj.CornerNodes:
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

				if corner_indices and len(corner_indices) >= 4:
					i_name = str(corner_indices[0])
					j_name = str(corner_indices[1])
					m_name = str(corner_indices[2])
					n_name = str(corner_indices[3])
					thk = getattr(plate_obj, 'Thickness', 0.1)
					mat_obj = getattr(plate_obj, 'Material', None)
					if mat_obj and hasattr(mat_obj, 'Name'):
						mat_name = mat_obj.Name
						if mat_name not in materiais:
							# try to add material (best-effort)
							try:
								model.add_material(mat_name, 200000.0, 77000.0, 0.3, 78.5)
								materiais.append(mat_name)
							except Exception:
								_print_warning(f"Could not add material {mat_name} for plate '{plate_obj.Name}'\n")
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

			# Determine pressure magnitude (in force per area units)
			# Prefer AreaLoad exporter when available
			try:
				if hasattr(aload, 'Proxy') and hasattr(aload.Proxy, 'to_solver_loads'):
					# Attempt to find matching plate payload if targets exist
					mesh_payload = None
					if targets:
						# Build a minimal mesh_payload if we have recorded plate meshes
						for t in targets:
							if hasattr(self, '_plate_mesh_elements') and t.Name in self._plate_mesh_elements:
								mesh_payload = {'elements': {}, 'nodes': {}, 'area': None}
								for q in self._plate_mesh_elements.get(t.Name, []):
									mesh_payload['elements'][q] = {'nodes': []}
					# Ask exporter for solver loads
					loads_result = aload.Proxy.to_solver_loads(aload, mesh_payload=mesh_payload, force_unit=obj.ForceUnit, length_unit=obj.LengthUnit)
					if loads_result and loads_result.get('entries'):
						for entry in loads_result.get('entries', []):
							if 'element' in entry:
								ename = entry['element']
								pressure = entry.get('pressure', 0.0)
								# try to map to recorded quad names
								if hasattr(self, '_plate_mesh_elements'):
									for plate_name, quads in getattr(self, '_plate_mesh_elements', {}).items():
										for qname in quads:
											if ename == qname or ename.endswith(qname):
												try:
													model.add_quad_surface_pressure(qname, float(pressure), case=aload.LoadCategory if hasattr(aload, 'LoadCategory') else None)
													_print_message(f"  Applied pressure {pressure:.4f} to quad {qname} (from exporter)\n")
												except Exception as e:
													_print_warning(f"Could not add quad pressure for {qname}: {e}\n")
							elif 'plate' in entry:
								pname = entry['plate']
								pressure = entry.get('pressure', 0.0)
								if pname in model.plates:
									try:
										model.add_plate_surface_pressure(pname, float(pressure), case=aload.LoadCategory if hasattr(aload, 'LoadCategory') else None)
									except Exception as e:
										_print_warning(f"Could not add plate pressure for {pname}: {e}\n")
					# If exporter provided entries, skip geometric fallback
					if loads_result and loads_result.get('entries'):
						continue
			except Exception as e:
				_print_warning(f"AreaLoad exporter failed for '{getattr(aload, 'Name', '')}': {e}\n")

			pressure_value = None
			
			# First try LoadIntensity property (preferred)
			if hasattr(aload, 'LoadIntensity'):
				try:
					pressure_value = qty_val(aload.LoadIntensity, 'N/m^2', obj.ForceUnit + '/' + obj.LengthUnit + '^2')
				except Exception as e:
					_print_warning(f"Could not convert LoadIntensity for AreaLoad '{aload.Name}': {e}\n")

			# Fall back to Magnitude property if needed
			if pressure_value is None and hasattr(aload, 'Magnitude'):
				try:
					pressure_value = qty_val(aload.Magnitude, 'N/m^2', obj.ForceUnit + '/' + obj.LengthUnit + '^2')
				except Exception:
					try:
						pressure_value = float(aload.Magnitude)
					except Exception:
						pressure_value = None

			# Get load direction vector
			load_direction = App.Vector(0, 0, -1)  # Default downward
			if hasattr(aload, 'LoadDirection'):
				load_direction = aload.LoadDirection
			elif hasattr(aload, 'Direction'):
				# Use the Direction property if LoadDirection is not available
				direction_map = {
					"+X Global": App.Vector(1, 0, 0),
					"-X Global": App.Vector(-1, 0, 0),
					"+Y Global": App.Vector(0, 1, 0),
					"-Y Global": App.Vector(0, -1, 0),
					"+Z Global": App.Vector(0, 0, 1),
					"-Z Global": App.Vector(0, 0, -1),
					"Normal": App.Vector(0, 0, -1)  # Default
				}
				if aload.Direction in direction_map:
					load_direction = direction_map[aload.Direction]
				elif aload.Direction == "Custom" and hasattr(aload, 'CustomDirection'):
					load_direction = aload.CustomDirection

			# Normalize the direction vector
			try:
				length = math.sqrt(load_direction.x**2 + load_direction.y**2 + load_direction.z**2)
				if length > 0:
					load_direction = App.Vector(load_direction.x/length, load_direction.y/length, load_direction.z/length)
			except Exception as e:
				_print_warning(f"Error normalizing load direction for AreaLoad '{aload.Name}': {e}\n")
				load_direction = App.Vector(0, 0, -1)

			# Apply coordinate system mapping (FreeCAD X→Solver X, FreeCAD Y→Solver Z, FreeCAD Z→Solver Y)
			load_direction = App.Vector(load_direction.x, load_direction.z, load_direction.y)

			# Determine load distribution method (one-way vs two-way)
			distribution_method = "TwoWay"  # Default to two-way distribution
			if hasattr(aload, 'LoadDistribution'):
				distribution_method = aload.LoadDistribution

			# Get load case from load category
			load_case = "DL"  # Default to dead load
			if hasattr(aload, 'LoadCategory'):
				load_case = aload.LoadCategory

			_print_message(f"Processing AreaLoad '{aload.Name}' with {distribution_method} distribution, pressure: {pressure_value} {obj.ForceUnit}/{obj.LengthUnit}²\n")

			for tgt in targets:
				# try to find the plate we added by name
				plate_name = getattr(tgt, 'Name', None)
				
				# Process each face of the target to calculate effective pressure
				if hasattr(tgt, 'Shape') and hasattr(tgt.Shape, 'Faces'):
					face_count = len(tgt.Shape.Faces)
					for i, face in enumerate(tgt.Shape.Faces):
						try:
							# Calculate face normal at center
							u_range = face.ParameterRange[0:2]
							v_range = face.ParameterRange[2:4]
							u_center = (u_range[0] + u_range[1]) / 2
							v_center = (v_range[0] + v_range[1]) / 2
							face_normal = face.normalAt(u_center, v_center)
							
							# Normalize face normal
							normal_length = math.sqrt(face_normal.x**2 + face_normal.y**2 + face_normal.z**2)
							if normal_length > 0:
								face_normal = App.Vector(face_normal.x/normal_length, face_normal.y/normal_length, face_normal.z/normal_length)
							
							# Apply coordinate system mapping (FreeCAD X→Solver X, FreeCAD Y→Solver Z, FreeCAD Z→Solver Y)
							face_normal = App.Vector(face_normal.x, face_normal.z, face_normal.y)
							
							# Calculate dot product between load direction and face normal
							# This gives us the effective pressure considering the angle
							dot_product = load_direction.x * face_normal.x + load_direction.y * face_normal.y + load_direction.z * face_normal.z
							
							# Calculate effective pressure
							effective_pressure = pressure_value * dot_product if pressure_value is not None else 0.0
							
							# For plates or directly mapped quads
							face_plate_name = f"{plate_name}_{i}" if face_count > 1 else plate_name

							# Get edge factors based on distribution method
							edge_factors = [0.25, 0.25, 0.25, 0.25]  # Default equal distribution
							
							if distribution_method == "OneWay":
								# One-way distribution - load goes to two parallel edges
								one_way_direction = App.Vector(1, 0, 0)  # Default X direction
								
								if hasattr(aload, 'OneWayDirection'):
									if aload.OneWayDirection == "X":
										one_way_direction = App.Vector(1, 0, 0)
									elif aload.OneWayDirection == "Y":
										one_way_direction = App.Vector(0, 1, 0)
									elif aload.OneWayDirection == "Custom" and hasattr(aload, 'CustomDistributionDirection'):
										one_way_direction = aload.CustomDistributionDirection
								
								# Reset factors to 0
								edge_factors = [0.0, 0.0, 0.0, 0.0]
								
								# Find edges perpendicular to distribution direction
								edges = face.Edges
								perpendicular_edges = []
								
								for j, edge in enumerate(edges):
									if edge.Length > 0:
										edge_dir = edge.Vertexes[1].Point - edge.Vertexes[0].Point
										edge_length = math.sqrt(edge_dir.x**2 + edge_dir.y**2 + edge_dir.z**2)
										if edge_length > 0:
											edge_dir = App.Vector(edge_dir.x/edge_length, edge_dir.y/edge_length, edge_dir.z/edge_length)
											# Check if edge is perpendicular to direction (using dot product)
											edge_dot = abs(edge_dir.x * one_way_direction.x + edge_dir.y * one_way_direction.y + edge_dir.z * one_way_direction.z)
											if edge_dot < 0.3:  # If dot product is close to 0, they're perpendicular
												perpendicular_edges.append(j)
								
								# Set perpendicular edges to 0.5 each (shared load)
								if len(perpendicular_edges) >= 2:
									for j in perpendicular_edges[:2]:  # Use first two perpendicular edges
										if j < len(edge_factors):
											edge_factors[j] = 0.5
							
							elif distribution_method == "TwoWay":
								# Two-way distribution - load is distributed based on relative span lengths
								edges = face.Edges
								
								if len(edges) >= 4:
									# Get edge lengths
									edge_lengths = [edge.Length for edge in edges[:4]]  # Use first 4 edges
									
									# Calculate edge factors based on relative lengths
									# For a rectangle, longer edges get more load
									total_length = sum(edge_lengths)
									
									if total_length > 0:
										edge_factors = [length/total_length for length in edge_lengths]
										
										# Pad to 4 elements if needed
										while len(edge_factors) < 4:
											edge_factors.append(0.0)
							
							elif distribution_method == "OpenStructure":
								# Open structure - load is distributed based on projected area
								# Calculate edge factors based on projection and edge orientation
								edges = face.Edges
								
								if len(edges) >= 4:
									# Project load direction onto each edge normal
									for j, edge in enumerate(edges[:4]):
										if edge.Length > 0:
											# Get edge normal (perpendicular to edge, in plane of face)
											edge_dir = edge.Vertexes[1].Point - edge.Vertexes[0].Point
											edge_normal = App.Vector(edge_dir.y, -edge_dir.x, edge_dir.z)  # Simplified 2D normal
											
											# Normalize edge normal
											normal_length = math.sqrt(edge_normal.x**2 + edge_normal.y**2 + edge_normal.z**2)
											if normal_length > 0:
												edge_normal = App.Vector(edge_normal.x/normal_length, edge_normal.y/normal_length, edge_normal.z/normal_length)
											
											# Get projection factor (dot product with load direction)
											proj_factor = abs(edge_normal.x * load_direction.x + 
																edge_normal.y * load_direction.y + 
																edge_normal.z * load_direction.z)
											
											# Use projection factor to adjust edge factor
											edge_factors[j] = proj_factor
									
									# Normalize edge factors to sum to 1.0
									factor_sum = sum(edge_factors)
									if factor_sum > 0:
										edge_factors = [factor / factor_sum for factor in edge_factors]
							
							# Apply pressure to plates/quads with edge factors
							if plate_name and face_plate_name in model.plates and effective_pressure is not None:
								try:
									model.add_plate_surface_pressure(face_plate_name, effective_pressure, case=load_case)
									_print_message(f"  Applied pressure {effective_pressure:.4f} to plate {face_plate_name} with edge factors: {[f'{ef:.2f}' for ef in edge_factors]}\n")
								except Exception as e:
									_print_warning(f"Could not map AreaLoad '{aload.Name}' to plate '{face_plate_name}': {e}\n")
									
							# Map to meshed quads created for this plate (if any)
							if hasattr(self, '_plate_mesh_elements') and plate_name in getattr(self, '_plate_mesh_elements', {}):
								for qname in self._plate_mesh_elements.get(plate_name, []):
									if qname in model.quads and effective_pressure is not None:
										try:
											model.add_quad_surface_pressure(qname, effective_pressure, case=load_case)
											_print_message(f"  Applied pressure {effective_pressure:.4f} to quad {qname} with edge factors: {[f'{ef:.2f}' for ef in edge_factors]}\n")
										except Exception as e:
											_print_warning(f"Could not map AreaLoad '{aload.Name}' to quad '{qname}': {e}\n")
						except Exception as e:
							_print_warning(f"Error processing face {i} of AreaLoad '{aload.Name}': {e}\n")
				else:
					# Fallback to original method if no face information available
					if plate_name and plate_name in model.plates and pressure_value is not None:
						try:
							model.add_plate_surface_pressure(plate_name, pressure_value, case=load_case)
							_print_message(f"  Applied pressure {pressure_value:.4f} to plate {plate_name} (fallback method)\n")
						except Exception as e:
							_print_warning(f"Could not map AreaLoad '{aload.Name}' to plate '{plate_name}': {e}\n")
							
					# Map to meshed quads created for this plate (if any)
					if hasattr(self, '_plate_mesh_elements') and plate_name in getattr(self, '_plate_mesh_elements', {}):
						for qname in self._plate_mesh_elements.get(plate_name, []):
							if qname in model.quads and pressure_value is not None:
								try:
									model.add_quad_surface_pressure(qname, pressure_value, case=load_case)
									_print_message(f"  Applied pressure {pressure_value:.4f} to quad {qname} (fallback method)\n")
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
		self.Object = obj.Object if hasattr(obj, 'Object') else None
		self.reaction_texts = []  # Store reaction text objects
	
	# Add __getstate__ and __setstate__ methods to handle serialization
	def __getstate__(self):
		# Don't serialize the Object reference and reaction_texts as they may not be JSON serializable
		state = self.__dict__.copy()
		# Remove potentially problematic attributes
		state['Object'] = None
		state['reaction_texts'] = []
		return state

	def __setstate__(self, state):
		self.__dict__.update(state)
		# Ensure Object and reaction_texts are properly initialized
		if not hasattr(self, 'Object'):
			self.Object = None
		if not hasattr(self, 'reaction_texts'):
			self.reaction_texts = []
		return None
	
	def updateData(self, obj, prop):
		"""Called when the object's data changes"""
		if prop in ['ShowReactionText', 'ReactionPrecision', 'ReactionTextOffset', 'ReactionFontSize', 'LoadCombination']:
			self.updateReactionTextDisplay()
		
		# Notify reaction results objects when load combination changes
		if prop == 'LoadCombination':
			self.notify_reaction_results_update(obj)
	
	def notify_reaction_results_update(self, obj):
		"""Notify all reaction results objects to update when load combination changes."""
		try:
			import FreeCAD
			FreeCAD.Console.PrintMessage(f"📢 Calc LoadCombination changed to: {obj.LoadCombination}\n")
			
			# Find all ReactionResults objects in the document that reference this calc
			for doc_obj in FreeCAD.ActiveDocument.Objects:
				if (hasattr(doc_obj, 'Proxy') and 
					hasattr(doc_obj.Proxy, '__class__') and
					doc_obj.Proxy.__class__.__name__ == 'ReactionResults' and
					hasattr(doc_obj, 'ObjectBaseCalc') and
					doc_obj.ObjectBaseCalc == obj):
					
					FreeCAD.Console.PrintMessage(f"🔄 Updating ReactionResults: {doc_obj.Name}\n")
					
					# Update the ActiveLoadCombination to match calc
					doc_obj.ActiveLoadCombination = obj.LoadCombination
					
					# Trigger update
					if hasattr(doc_obj.Proxy, 'execute'):
						doc_obj.Proxy.execute(doc_obj)
						
		except Exception as e:
			import FreeCAD
			FreeCAD.Console.PrintError(f"❌ Error notifying reaction results: {str(e)}\n")

	def onChanged(self, obj, prop):
		"""Called when view properties change"""
		if prop == 'ShowReactionText':
			self.updateReactionTextDisplay()
	
	def updateReactionTextDisplay(self):
		"""Update the display of reaction texts based on ShowReactionText property"""
		try:
			# Clear existing reaction texts
			self.clearReactionTexts()
			
			# Check if Object is properly set
			if self.Object is None:
				return
			
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
			# Check if reaction_texts exists
			if not hasattr(self, 'reaction_texts'):
				return
				
			doc = App.ActiveDocument
			if not doc:
				return
			
			for text_obj in self.reaction_texts:
				if text_obj and hasattr(text_obj, 'Name') and text_obj.Name in doc.Objects:
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
        # Set the Object property explicitly
        obj.ViewObject.Proxy.Object = obj

        App.ActiveDocument.recompute()        
        return

    def IsActive(self):
        
        return True

# Only register command if FreeCAD GUI is available
if FREECAD_AVAILABLE and 'FreeCADGui' in globals():
    FreeCADGui.addCommand("calc", CommandCalc())
