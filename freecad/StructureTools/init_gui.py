import os
import FreeCADGui as Gui
import FreeCAD as App
import subprocess

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



translate=App.Qt.translate
QT_TRANSLATE_NOOP=App.Qt.QT_TRANSLATE_NOOP

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")
TRANSLATIONSPATH = os.path.join(os.path.dirname(__file__), "resources", "translations")

# Add translations path
Gui.addLanguagePath(TRANSLATIONSPATH)
Gui.updateLocale()



from .Pynite_main.FEModel3D import FEModel3D

# from .Pynite_main.FEModel3D import FEModel3D
# try:
# 	from Pynite import FEModel3D
# except:
# 	print('Instalando dependencias')
# 	subprocess.check_call(["pip", "install", "PyniteFEA"])

class StructureTools(Gui.Workbench):
	"""
	class which gets initiated at startup of the gui
	"""
	MenuText = translate("Workbench", "StructureTools")
	ToolTip = translate("Workbench", "a simple StructureTools")
	Icon = os.path.join(ICONPATH, "icone.svg")
	toolbox = []

	def GetClassName(self):
		return "Gui::PythonWorkbench"

	def Initialize(self):
		"""
		This function is called at the first activation of the workbench.
		here is the place to import all the commands
		"""
		from freecad.StructureTools import load_distributed
		from freecad.StructureTools import load_nodal
		from freecad.StructureTools import load_point
		from freecad.StructureTools import suport
		from freecad.StructureTools import section
		from freecad.StructureTools import material
		from freecad.StructureTools.commands import CreateMaterial
		
		# Import BIM integration module
		try:
			from freecad.StructureTools.integration import BIMIntegration
			from freecad.StructureTools.integration import BIMCommands
			from freecad.StructureTools.integration import TechDrawIntegration
			from freecad.StructureTools.integration import FEMIntegration
		except ImportError:
			App.Console.PrintWarning("Some integration modules not available\n")
		from freecad.StructureTools.commands import MaterialDatabaseManager
		from freecad.StructureTools import member
		from freecad.StructureTools import calc
		from freecad.StructureTools import diagram
		from freecad.StructureTools import command_reaction_table
		
		# New Phase 1 components
		from freecad.StructureTools import command_plate
		from freecad.StructureTools import command_area_load
		# Phase 2 - Advanced Analysis
		from freecad.StructureTools import command_modal_analysis
		from freecad.StructureTools import command_buckling_analysis
		# Phase 2 - Design Code Integration
		from freecad.StructureTools import command_aisc_design
		from freecad.StructureTools import command_aci_design
		# Phase 2 - Advanced Load Generation
		from freecad.StructureTools import command_load_generator
		# Phase 2 - Professional Wind Load GUI
		try:
			from freecad.StructureTools.commands import command_wind_load_gui
			App.Console.PrintMessage("Wind Load GUI command loaded successfully\n")
		except Exception as e:
			App.Console.PrintError(f"Failed to load Wind Load GUI command: {e}\n")
		# Phase 2 - Professional Seismic Load GUI
		try:
			from freecad.StructureTools.commands import command_seismic_load_gui
			App.Console.PrintMessage("Seismic Load GUI command loaded successfully\n")
		except Exception as e:
			App.Console.PrintError(f"Failed to load Seismic Load GUI command: {e}\n")
		# Phase 2 - Design Optimization
		from freecad.StructureTools import command_design_optimizer
		# Phase 2 - Comprehensive Reporting
		from freecad.StructureTools import command_report_generator
		
		# Advanced Section Manager with steelpy integration
		try:
			from freecad.StructureTools.commands import advanced_section_manager
			App.Console.PrintMessage("Advanced Section Manager command loaded successfully\n")
		except Exception as e:
			App.Console.PrintError(f"Failed to load Advanced Section Manager command: {e}\n")
		
		# TaskPanel version of Advanced Section Manager (more stable)
		try:
			from freecad.StructureTools.gui import SectionManagerTaskPanel
			App.Console.PrintMessage("Advanced Section Manager TaskPanel loaded successfully\n")
		except Exception as e:
			App.Console.PrintError(f"Failed to load Advanced Section Manager TaskPanel: {e}\n")

		
		import DraftTools, SketcherGui
		# NOTE: Context for this commands must be "Workbench"
		self.appendToolbar('DraftDraw', ["Sketcher_NewSketch","Draft_Line", "Draft_Wire", "Draft_ArcTools", "Draft_BSpline", "Draft_Dimension"])
		self.appendToolbar('DraftEdit', ["Draft_Move", "Draft_Rotate", "Draft_Clone", "Draft_Offset", "Draft_Trimex", "Draft_Join", "Draft_Split","Draft_Stretch","Draft_Draft2Sketch"])
		self.appendToolbar('DraftSnap', ["Draft_Snap_Lock", "Draft_Snap_Endpoint", "Draft_Snap_Midpoint", "Draft_Snap_Center", "Draft_Snap_Angle", "Draft_Snap_Intersection", "Draft_Snap_Perpendicular", "Draft_Snap_Extension", "Draft_Snap_Parallel", "Draft_Snap_Special", "Draft_Snap_Near", "Draft_Snap_Ortho", "Draft_Snap_Grid", "Draft_Snap_WorkingPlane", "Draft_Snap_Dimensions", "Draft_ToggleGrid"])
		self.appendToolbar('DraftTools', ["Draft_SelectPlane", "Draft_SetStyle"])

		self.appendToolbar('StructureLoad', ["load_distributed","load_nodal", "load_point", "CreateAreaLoad", "RunLoadGenerator", "wind_load_gui", "seismic_load_gui"])
		self.appendToolbar('StructureTools', ["member", "suport", "section", "material", "CreateMaterial", "MaterialDatabaseManager", "StructureTools_AdvancedSectionManager", "StructureTools_AdvancedSectionManagerTaskPanel", "CreateStructuralPlate"])
		self.appendToolbar('StructureResults', ["calc","diagram", "ViewReactionTable", "GenerateStructuralReport"])
		self.appendToolbar('AdvancedAnalysis', ["RunModalAnalysis", "ViewModalResults", "RunBucklingAnalysis", "RunDesignOptimizer"])
		self.appendToolbar('DesignCodes', ["RunAISCDesign", "RunACIDesign"])
		self.appendToolbar('BIMIntegration', ["BIM_Import", "BIM_Export", "BIM_Sync", "CreateStructuralDrawing", "ExportToFEM"])
		
		self.appendMenu('StructureTools',["load_distributed", "load_nodal", "load_point", "CreateAreaLoad", "RunLoadGenerator", "wind_load_gui", "seismic_load_gui", "member" ,"suport", "section", "material", "CreateMaterial", "MaterialDatabaseManager", "StructureTools_AdvancedSectionManager", "StructureTools_AdvancedSectionManagerTaskPanel", "CreateStructuralPlate", "calc", "diagram", "ViewReactionTable", "GenerateStructuralReport"])
		self.appendMenu('Advanced Analysis',["RunModalAnalysis", "ViewModalResults", "RunBucklingAnalysis", "RunDesignOptimizer"])
		self.appendMenu('Design Codes',["RunAISCDesign", "RunACIDesign"])
		self.appendMenu('BIM Integration',["BIM_Import", "BIM_Export", "BIM_Sync", "CreateStructuralDrawing", "ExportToFEM"])

	def Activated(self):
		'''
		code which should be computed when a user switch to this workbench
		'''
		

		App.Console.PrintMessage(translate(
			"Log",
			"Workbench StructureTools activated.") + "\n")

	def Deactivated(self):
		'''
		code which should be computed when this workbench is deactivated
		'''
		App.Console.PrintMessage(translate(
			"Log",
			"Workbench StructureTools de-activated.") + "\n")


Gui.addWorkbench(StructureTools())