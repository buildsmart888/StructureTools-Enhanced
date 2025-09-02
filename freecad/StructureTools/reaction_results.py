import FreeCAD, FreeCADGui, Part, math, os
from typing import List, Tuple, Any, Optional, Dict
import logging

# Prefer PySide2 when available
try:
    from PySide2 import QtWidgets, QtCore, QtGui
except ImportError:
    try:
        from PySide import QtWidgets, QtCore, QtGui
    except ImportError as e:
        raise ImportError("Neither PySide2 nor PySide could be imported. Please install one of them.") from e

# Import Global Units System
try:
    from .utils.units_manager import (
        get_units_manager, format_force, format_stress, format_modulus, format_moment
    )
    GLOBAL_UNITS_AVAILABLE = True
except ImportError:
    GLOBAL_UNITS_AVAILABLE = False
    get_units_manager = lambda: None
    format_force = lambda x: f"{x:.2f} kN"
    format_stress = lambda x: f"{x/1e6:.1f} MPa"
    format_modulus = lambda x: f"{x/1e9:.0f} GPa"
    format_moment = lambda x: f"{x:.2f} kN·m"

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")


class ReactionResults:
    """Class for displaying and managing reaction force and moment results from structural analysis."""
    
    def __init__(self, obj: Any, objCalc: Any) -> None:
        """Initialize the ReactionResults object.
        
        Args:
            obj: The FreeCAD object to attach to
            objCalc: The calculation object containing analysis results
        """
        obj.Proxy = self
        obj.addProperty("App::PropertyLink", "ObjectBaseCalc", "Base", "Calculation object with analysis results").ObjectBaseCalc = objCalc
        
        # Reaction force display properties
        obj.addProperty("App::PropertyBool", "ShowReactionFX", "Reaction Forces", "Show X-direction reaction forces").ShowReactionFX = True
        obj.addProperty("App::PropertyBool", "ShowReactionFY", "Reaction Forces", "Show Y-direction reaction forces").ShowReactionFY = True
        obj.addProperty("App::PropertyBool", "ShowReactionFZ", "Reaction Forces", "Show Z-direction reaction forces").ShowReactionFZ = True
        obj.addProperty("App::PropertyFloat", "ScaleReactionForces", "Reaction Forces", "Scale factor for reaction force arrows").ScaleReactionForces = 10.0
        
        # Reaction moment display properties
        obj.addProperty("App::PropertyBool", "ShowReactionMX", "Reaction Moments", "Show X-axis reaction moments").ShowReactionMX = True
        obj.addProperty("App::PropertyBool", "ShowReactionMY", "Reaction Moments", "Show Y-axis reaction moments").ShowReactionMY = True
        obj.addProperty("App::PropertyBool", "ShowReactionMZ", "Reaction Moments", "Show Z-axis reaction moments").ShowReactionMZ = True
        obj.addProperty("App::PropertyFloat", "ScaleReactionMoments", "Reaction Moments", "Scale factor for reaction moment arrows").ScaleReactionMoments = 10.0
        
        # Resultant reaction display properties
        obj.addProperty("App::PropertyBool", "ShowResultantForces", "Resultant Reactions", "Show resultant forces").ShowResultantForces = False
        obj.addProperty("App::PropertyBool", "ShowResultantMoments", "Resultant Reactions", "Show resultant moments").ShowResultantMoments = False
        obj.addProperty("App::PropertyFloat", "ScaleResultantForces", "Resultant Reactions", "Scale factor for resultant force arrows").ScaleResultantForces = 10.0
        obj.addProperty("App::PropertyFloat", "ScaleResultantMoments", "Resultant Reactions", "Scale factor for resultant moment arrows").ScaleResultantMoments = 10.0
        
        # Display options
        obj.addProperty("App::PropertyColor", "ForceArrowColor", "Display", "Color for force arrows").ForceArrowColor = (1.0, 0.0, 0.0, 0.0)  # Red
        obj.addProperty("App::PropertyColor", "MomentArrowColor", "Display", "Color for moment arrows").MomentArrowColor = (0.0, 1.0, 0.0, 0.0)  # Green
        obj.addProperty("App::PropertyBool", "ShowLabels", "Display", "Show reaction value labels").ShowLabels = True
        obj.addProperty("App::PropertyInteger", "LabelFontSize", "Display", "Font size for reaction labels").LabelFontSize = 8
        obj.addProperty("App::PropertyInteger", "Precision", "Display", "Decimal places for reaction values").Precision = 2
        obj.addProperty("App::PropertyFloat", "ArrowThickness", "Display", "Thickness of reaction arrows").ArrowThickness = 2.0
        
        # Language selection
        obj.addProperty("App::PropertyEnumeration", "Language", "Display", "Language for labels").Language = ["English", "Thai"]
        obj.Language = "English"  # Default to English
        
        # Minimum reaction threshold
        obj.addProperty("App::PropertyFloat", "MinReactionThreshold", "Display", "Minimum reaction magnitude to display").MinReactionThreshold = 1e-6
        
        # Auto-scaling option
        obj.addProperty("App::PropertyBool", "AutoScaleReactions", "Display", "Automatically scale reactions based on model size").AutoScaleReactions = False
        
        # Color gradient options
        obj.addProperty("App::PropertyBool", "UseColorGradient", "Display", "Use color gradient based on reaction magnitude").UseColorGradient = False
        obj.addProperty("App::PropertyColor", "MinGradientColor", "Display", "Color for minimum reaction values").MinGradientColor = (0.0, 1.0, 0.0, 0.0)  # Green
        obj.addProperty("App::PropertyColor", "MaxGradientColor", "Display", "Color for maximum reaction values").MaxGradientColor = (1.0, 0.0, 0.0, 0.0)  # Red
        
        # Specialized reaction type visualization
        obj.addProperty("App::PropertyBool", "ShowOnlyMaximumReactions", "Display", "Show only maximum reactions at each node").ShowOnlyMaximumReactions = False
        obj.addProperty("App::PropertyBool", "ShowOnlySignificantReactions", "Display", "Show only reactions above a significance threshold").ShowOnlySignificantReactions = False
        obj.addProperty("App::PropertyFloat", "SignificanceThreshold", "Display", "Threshold for significant reactions (ratio of max reaction)").SignificanceThreshold = 0.1
        
        # Load combination selection
        obj.addProperty("App::PropertyString", "ActiveLoadCombination", "Analysis", "Currently selected load combination").ActiveLoadCombination = "100_DL"
        
        # Internal storage for reaction visualization objects
        self.reaction_objects = []
        self.label_objects = []

    def execute(self, obj):
        """Execute the reaction visualization update."""
        try:
            self.clear_existing_visualization(obj)
            self.create_reaction_visualization(obj)
        except Exception as e:
            logger.error(f"Error in ReactionResults.execute: {str(e)}")
            FreeCAD.Console.PrintError(f"ReactionResults error: {str(e)}\n")

    def clear_existing_visualization(self, obj):
        """Clear all existing reaction visualization objects."""
        # Remove existing reaction arrows and labels
        for react_obj in self.reaction_objects + self.label_objects:
            try:
                if hasattr(react_obj, 'Document') and react_obj.Document:
                    react_obj.Document.removeObject(react_obj.Name)
            except:
                pass
        
        self.reaction_objects.clear()
        self.label_objects.clear()

    def create_reaction_visualization(self, obj):
        """Create 3D visualization of reaction forces and moments."""
        if not obj.ObjectBaseCalc:
            logger.warning("No calculation object found")
            return
            
        calc_obj = obj.ObjectBaseCalc
        
        # Get the FE model from the calculation
        model = None
        
        # Debug: Show what properties the calc object has
        FreeCAD.Console.PrintMessage(f"Debug: Calc object {calc_obj.Name} properties check:\n")
        FreeCAD.Console.PrintMessage(f"  - Has FEModel: {hasattr(calc_obj, 'FEModel')}\n")
        if hasattr(calc_obj, 'FEModel'):
            FreeCAD.Console.PrintMessage(f"  - FEModel value: {calc_obj.FEModel is not None}\n")
        FreeCAD.Console.PrintMessage(f"  - Has model: {hasattr(calc_obj, 'model')}\n")
        
        # Try different ways to get the FE model
        if hasattr(calc_obj, 'FEModel') and calc_obj.FEModel:
            model = calc_obj.FEModel
            FreeCAD.Console.PrintMessage(f"  ✅ Using FEModel with {len(model.nodes) if hasattr(model, 'nodes') else 0} nodes\n")
        elif hasattr(calc_obj, 'model') and calc_obj.model:
            model = calc_obj.model
            FreeCAD.Console.PrintMessage(f"  ✅ Using model with {len(model.nodes) if hasattr(model, 'nodes') else 0} nodes\n")
        elif hasattr(calc_obj, 'Proxy') and hasattr(calc_obj.Proxy, 'model'):
            model = calc_obj.Proxy.model
            FreeCAD.Console.PrintMessage(f"  ✅ Using Proxy.model with {len(model.nodes) if hasattr(model, 'nodes') else 0} nodes\n")
        
        if not model or not hasattr(model, 'nodes') or not model.nodes:
            logger.warning("No FE model found with valid nodes in calculation object - run analysis first")
            FreeCAD.Console.PrintWarning("❌ No FE model with valid nodes found - please run structural analysis first\n")
            FreeCAD.Console.PrintWarning("   Make sure the calc command completed successfully\n")
            return
            
        # Check for valid load combination
        load_combo = obj.ActiveLoadCombination
        if not load_combo and hasattr(model, 'LoadCombos') and model.LoadCombos:
            # Use the first available load combo
            load_combo = list(model.LoadCombos.keys())[0]
            obj.ActiveLoadCombination = load_combo
            FreeCAD.Console.PrintMessage(f"  ℹ️ Using first available load combination: {load_combo}\n")
        
        # Print detailed reaction information as requested
        self.print_detailed_reaction_info(model, load_combo)
        
        # Calculate auto scale factors if enabled
        if obj.AutoScaleReactions:
            force_scale, moment_scale = self.calculate_auto_scale_factors(obj)
            obj.ScaleReactionForces = force_scale
            obj.ScaleReactionMoments = moment_scale
            # Update resultant scales proportionally
            obj.ScaleResultantForces = force_scale
            obj.ScaleResultantMoments = moment_scale
        
        # Create reaction arrows for each supported node
        for node_name, node in model.nodes.items():
            if self.is_node_supported(node):
                node_pos = FreeCAD.Vector(node.X, node.Z, node.Y)  # Convert Pynite coords to FreeCAD
                
                # Collect all reaction values for this node
                reaction_values = []
                
                if obj.ShowReactionFX and hasattr(node, 'RxnFX') and load_combo in node.RxnFX and abs(node.RxnFX[load_combo]) > obj.MinReactionThreshold:
                    reaction_values.append(node.RxnFX[load_combo])
                    
                if obj.ShowReactionFY and hasattr(node, 'RxnFY') and load_combo in node.RxnFY and abs(node.RxnFY[load_combo]) > obj.MinReactionThreshold:
                    reaction_values.append(node.RxnFY[load_combo])
                    
                if obj.ShowReactionFZ and hasattr(node, 'RxnFZ') and load_combo in node.RxnFZ and abs(node.RxnFZ[load_combo]) > obj.MinReactionThreshold:
                    reaction_values.append(node.RxnFZ[load_combo])
                    
                if obj.ShowReactionMX and hasattr(node, 'RxnMX') and load_combo in node.RxnMX and abs(node.RxnMX[load_combo]) > obj.MinReactionThreshold:
                    reaction_values.append(node.RxnMX[load_combo])
                    
                if obj.ShowReactionMY and hasattr(node, 'RxnMY') and load_combo in node.RxnMY and abs(node.RxnMY[load_combo]) > obj.MinReactionThreshold:
                    reaction_values.append(node.RxnMY[load_combo])
                    
                if obj.ShowReactionMZ and hasattr(node, 'RxnMZ') and load_combo in node.RxnMZ and abs(node.RxnMZ[load_combo]) > obj.MinReactionThreshold:
                    reaction_values.append(node.RxnMZ[load_combo])
                
                # Check if reactions should be displayed based on specialized visualization options
                if self.should_display_reaction(obj, node, load_combo, reaction_values):
                    # Create force arrows
                    if obj.ShowReactionFX and hasattr(node, 'RxnFX') and load_combo in node.RxnFX and abs(node.RxnFX[load_combo]) > obj.MinReactionThreshold:
                        self.create_force_arrow(obj, node_pos, 'X', node.RxnFX[load_combo], node_name)
                        
                    if obj.ShowReactionFY and hasattr(node, 'RxnFY') and load_combo in node.RxnFY and abs(node.RxnFY[load_combo]) > obj.MinReactionThreshold:
                        self.create_force_arrow(obj, node_pos, 'Y', node.RxnFY[load_combo], node_name)
                        
                    if obj.ShowReactionFZ and hasattr(node, 'RxnFZ') and load_combo in node.RxnFZ and abs(node.RxnFZ[load_combo]) > obj.MinReactionThreshold:
                        self.create_force_arrow(obj, node_pos, 'Z', node.RxnFZ[load_combo], node_name)
                    
                    # Create moment arrows
                    if obj.ShowReactionMX and hasattr(node, 'RxnMX') and load_combo in node.RxnMX and abs(node.RxnMX[load_combo]) > obj.MinReactionThreshold:
                        self.create_moment_arrow(obj, node_pos, 'X', node.RxnMX[load_combo], node_name)
                        
                    if obj.ShowReactionMY and hasattr(node, 'RxnMY') and load_combo in node.RxnMY and abs(node.RxnMY[load_combo]) > obj.MinReactionThreshold:
                        self.create_moment_arrow(obj, node_pos, 'Y', node.RxnMY[load_combo], node_name)
                        
                    if obj.ShowReactionMZ and hasattr(node, 'RxnMZ') and load_combo in node.RxnMZ and abs(node.RxnMZ[load_combo]) > obj.MinReactionThreshold:
                        self.create_moment_arrow(obj, node_pos, 'Z', node.RxnMZ[load_combo], node_name)
                
                # Create resultant force and moment arrows if enabled
                if obj.ShowResultantForces or obj.ShowResultantMoments:
                    # Get all reaction components for this node
                    fx = node.RxnFX.get(load_combo, 0.0) if hasattr(node, 'RxnFX') else 0.0
                    fy = node.RxnFY.get(load_combo, 0.0) if hasattr(node, 'RxnFY') else 0.0
                    fz = node.RxnFZ.get(load_combo, 0.0) if hasattr(node, 'RxnFZ') else 0.0
                    mx = node.RxnMX.get(load_combo, 0.0) if hasattr(node, 'RxnMX') else 0.0
                    my = node.RxnMY.get(load_combo, 0.0) if hasattr(node, 'RxnMY') else 0.0
                    mz = node.RxnMZ.get(load_combo, 0.0) if hasattr(node, 'RxnMZ') else 0.0
                    
                    # Calculate resultant magnitudes
                    force_magnitude = math.sqrt(fx*fx + fy*fy + fz*fz)
                    moment_magnitude = math.sqrt(mx*mx + my*my + mz*mz)
                    
                    # Check if resultants should be displayed based on specialized visualization options
                    reaction_values = [fx, fy, fz, mx, my, mz]
                    if self.should_display_reaction(obj, node, load_combo, reaction_values):
                        # Create resultant force arrow
                        if obj.ShowResultantForces and force_magnitude > obj.MinReactionThreshold:
                            self.create_resultant_force_arrow(obj, node_pos, fx, fy, fz, node_name)
                        
                        # Create resultant moment arrow
                        if obj.ShowResultantMoments and moment_magnitude > obj.MinReactionThreshold:
                            self.create_resultant_moment_arrow(obj, node_pos, mx, my, mz, node_name)

    def create_text_based_visualization(self, obj):
        """Create a text-based (ASCII art) visualization of reaction forces and moments."""
        if not obj.ObjectBaseCalc:
            FreeCAD.Console.PrintWarning("No calculation object found for text visualization\n")
            return
            
        calc_obj = obj.ObjectBaseCalc
        model = None
        
        # Try different ways to get the FE model
        if hasattr(calc_obj, 'FEModel') and calc_obj.FEModel:
            model = calc_obj.FEModel
        elif hasattr(calc_obj, 'model') and calc_obj.model:
            model = calc_obj.model
        elif hasattr(calc_obj, 'Proxy') and hasattr(calc_obj.Proxy, 'model'):
            model = calc_obj.Proxy.model
        
        if not model or not hasattr(model, 'nodes') or not model.nodes:
            FreeCAD.Console.PrintWarning("No FE model found with valid nodes - run analysis first\n")
            return
            
        # Check for valid load combination
        load_combo = obj.ActiveLoadCombination
        if not load_combo and hasattr(model, 'LoadCombos') and model.LoadCombos:
            # Use the first available load combo
            load_combo = list(model.LoadCombos.keys())[0]
        
        # Print header
        FreeCAD.Console.PrintMessage("\n" + "="*80 + "\n")
        FreeCAD.Console.PrintMessage("REACTION FORCES AND MOMENTS TEXT-BASED VISUALIZATION\n")
        FreeCAD.Console.PrintMessage("="*80 + "\n")
        FreeCAD.Console.PrintMessage(f"Load Combination: {load_combo}\n")
        FreeCAD.Console.PrintMessage("-"*80 + "\n")
        
        # Create reaction arrows for each supported node
        supported_nodes = []
        for node_name, node in model.nodes.items():
            if self.is_node_supported(node):
                supported_nodes.append((node_name, node))
        
        if not supported_nodes:
            FreeCAD.Console.PrintMessage("No supported nodes found.\n")
            return
        
        # Sort nodes by name for consistent output
        supported_nodes.sort(key=lambda x: x[0])
        
        # Process each supported node
        for node_name, node in supported_nodes:
            node_pos = FreeCAD.Vector(node.X, node.Z, node.Y)  # Convert Pynite coords to FreeCAD
            
            # Get reaction values for this node
            rx = node.RxnFX.get(load_combo, 0.0) if hasattr(node, 'RxnFX') else 0.0
            ry = node.RxnFY.get(load_combo, 0.0) if hasattr(node, 'RxnFY') else 0.0
            rz = node.RxnFZ.get(load_combo, 0.0) if hasattr(node, 'RxnFZ') else 0.0
            mx = node.RxnMX.get(load_combo, 0.0) if hasattr(node, 'RxnMX') else 0.0
            my = node.RxnMY.get(load_combo, 0.0) if hasattr(node, 'RxnMY') else 0.0
            mz = node.RxnMZ.get(load_combo, 0.0) if hasattr(node, 'RxnMZ') else 0.0
            
            # Check if any reactions are significant
            has_reactions = any(abs(val) > obj.MinReactionThreshold for val in [rx, ry, rz, mx, my, mz])
            
            if has_reactions:
                # Print node header
                FreeCAD.Console.PrintMessage(f"\nNode {node_name} at ({node.X:.2f}, {node.Y:.2f}, {node.Z:.2f}):\n")
                
                # Print support conditions
                support_conditions = []
                if node.support_DX: support_conditions.append("DX")
                if node.support_DY: support_conditions.append("DY")
                if node.support_DZ: support_conditions.append("DZ")
                if node.support_RX: support_conditions.append("RX")
                if node.support_RY: support_conditions.append("RY")
                if node.support_RZ: support_conditions.append("RZ")
                FreeCAD.Console.PrintMessage(f"  Supports: {', '.join(support_conditions)}\n")
                
                # Print reaction forces
                if abs(rx) > obj.MinReactionThreshold:
                    self._print_force_ascii("FX", rx, node_pos)
                if abs(ry) > obj.MinReactionThreshold:
                    self._print_force_ascii("FY", ry, node_pos)
                if abs(rz) > obj.MinReactionThreshold:
                    self._print_force_ascii("FZ", rz, node_pos)
                
                # Print reaction moments
                if abs(mx) > obj.MinReactionThreshold:
                    self._print_moment_ascii("MX", mx, node_pos)
                if abs(my) > obj.MinReactionThreshold:
                    self._print_moment_ascii("MY", my, node_pos)
                if abs(mz) > obj.MinReactionThreshold:
                    self._print_moment_ascii("MZ", mz, node_pos)
                
                # Calculate and print resultant force and moment
                force_magnitude = math.sqrt(rx*rx + ry*ry + rz*rz)
                moment_magnitude = math.sqrt(mx*mx + my*my + mz*mz)
                
                if force_magnitude > obj.MinReactionThreshold:
                    self._print_resultant_ascii("Force", force_magnitude, FreeCAD.Vector(rx, ry, rz))
                
                if moment_magnitude > obj.MinReactionThreshold:
                    self._print_resultant_ascii("Moment", moment_magnitude, FreeCAD.Vector(mx, my, mz))
        
        # Print summary
        FreeCAD.Console.PrintMessage("\n" + "-"*80 + "\n")
        FreeCAD.Console.PrintMessage("END OF TEXT-BASED VISUALIZATION\n")
        FreeCAD.Console.PrintMessage("="*80 + "\n")

    def _print_force_ascii(self, direction: str, magnitude: float, position: FreeCAD.Vector):
        """Print ASCII representation of a reaction force."""
        # Determine arrow direction
        arrow = "→" if magnitude >= 0 else "←"
        if direction == "FY":
            arrow = "↑" if magnitude >= 0 else "↓"
        elif direction == "FZ":
            arrow = "↗" if magnitude >= 0 else "↙"
        
        # Scale for visualization (adjust as needed)
        scale = 10.0
        length = int(abs(magnitude) * scale)
        if length < 1:
            length = 1
        elif length > 30:
            length = 30  # Cap maximum length for readability
        
        # Create force bar
        bar = arrow * length
        
        # Format magnitude
        formatted_magnitude = f"{abs(magnitude):.2f}"
        
        FreeCAD.Console.PrintMessage(f"    F{direction}: {bar} ({formatted_magnitude} kN)\n")

    def _print_moment_ascii(self, axis: str, magnitude: float, position: FreeCAD.Vector):
        """Print ASCII representation of a reaction moment."""
        # Determine rotation direction
        if magnitude >= 0:
            symbol = "↻"  # Clockwise
            arrow_seq = "→↓←↑" * 4  # Repeating sequence
        else:
            symbol = "↺"  # Counter-clockwise
            arrow_seq = "→↑←↓" * 4  # Repeating sequence
        
        # Scale for visualization (adjust as needed)
        scale = 5.0
        segments = int(abs(magnitude) * scale)
        if segments < 1:
            segments = 1
        elif segments > 16:
            segments = 16  # Cap maximum segments for readability
        
        # Create moment visualization
        moment_vis = symbol + " " + arrow_seq[:segments]
        
        # Format magnitude
        formatted_magnitude = f"{abs(magnitude):.2f}"
        
        FreeCAD.Console.PrintMessage(f"    M{axis}: {moment_vis} ({formatted_magnitude} kN·m)\n")

    def _print_resultant_ascii(self, type_name: str, magnitude: float, vector: FreeCAD.Vector):
        """Print ASCII representation of a resultant force or moment."""
        # Normalize vector for direction
        if vector.Length > 0:
            norm_vector = vector.normalize()
        else:
            norm_vector = FreeCAD.Vector(1, 0, 0)
        
        # Create directional arrow
        # Simple 2D projection for visualization
        angle = math.atan2(norm_vector.y, norm_vector.x)
        angle_deg = math.degrees(angle)
        
        # Map angle to compass direction
        if -22.5 <= angle_deg < 22.5:
            arrow = "→"
        elif 22.5 <= angle_deg < 67.5:
            arrow = "↗"
        elif 67.5 <= angle_deg < 112.5:
            arrow = "↑"
        elif 112.5 <= angle_deg < 157.5:
            arrow = "↖"
        elif 157.5 <= angle_deg or angle_deg < -157.5:
            arrow = "←"
        elif -157.5 <= angle_deg < -112.5:
            arrow = "↙"
        elif -112.5 <= angle_deg < -67.5:
            arrow = "↓"
        else:  # -67.5 <= angle_deg < -22.5
            arrow = "↘"
        
        # Scale for visualization
        scale = 10.0
        length = int(magnitude * scale)
        if length < 1:
            length = 1
        elif length > 30:
            length = 30  # Cap maximum length for readability
        
        # Create resultant bar
        bar = arrow * length
        
        # Format magnitude
        formatted_magnitude = f"{magnitude:.2f}"
        
        FreeCAD.Console.PrintMessage(f"    Resultant {type_name}: {bar} ({formatted_magnitude} {'kN' if type_name == 'Force' else 'kN·m'})\n")

    def print_detailed_reaction_info(self, model, load_combo):
        """Print detailed reaction information as requested."""
        try:
            FreeCAD.Console.PrintMessage(f"\nCollecting reactions for load combination: {load_combo}\n")
            
            # Count supported nodes
            supported_nodes = []
            for node_name, node in model.nodes.items():
                if self.is_node_supported(node):
                    supported_nodes.append((node_name, node))
            
            FreeCAD.Console.PrintMessage(f"  Found {len(supported_nodes)} supported nodes\n")
            
            # Initialize sums for total reactions
            sum_fx = sum_fy = sum_fz = 0.0
            
            # Process each supported node
            for node_name, node in supported_nodes:
                # Get reaction values
                rx = node.RxnFX.get(load_combo, 0.0) if hasattr(node, 'RxnFX') else 0.0
                ry = node.RxnFY.get(load_combo, 0.0) if hasattr(node, 'RxnFY') else 0.0
                rz = node.RxnFZ.get(load_combo, 0.0) if hasattr(node, 'RxnFZ') else 0.0
                mx = node.RxnMX.get(load_combo, 0.0) if hasattr(node, 'RxnMX') else 0.0
                my = node.RxnMY.get(load_combo, 0.0) if hasattr(node, 'RxnMY') else 0.0
                mz = node.RxnMZ.get(load_combo, 0.0) if hasattr(node, 'RxnMZ') else 0.0
                
                # Add to totals
                sum_fx += rx
                sum_fy += ry
                sum_fz += rz
                
                # Print node reactions
                FreeCAD.Console.PrintMessage(f" Node {node_name} reactions: FX={rx:.3f}, FY={ry:.3f}, FZ={rz:.3f}, MX={mx:.3f}, MY={my:.3f}, MZ={mz:.3f}\n")
                
                # Print support conditions
                support_conditions = []
                if node.support_DX: support_conditions.append("DX")
                if node.support_DY: support_conditions.append("DY")
                if node.support_DZ: support_conditions.append("DZ")
                if node.support_RX: support_conditions.append("RX")
                if node.support_RY: support_conditions.append("RY")
                if node.support_RZ: support_conditions.append("RZ")
                FreeCAD.Console.PrintMessage(f"    Support conditions: {', '.join(support_conditions)}\n")
                
                # Print node coordinates
                FreeCAD.Console.PrintMessage(f"   Node coordinates: ({node.X:.3f}, {node.Y:.3f}, {node.Z:.3f})\n")
            
            # Print total reactions
            FreeCAD.Console.PrintMessage(f"  Total reactions - Sum FX: {sum_fx:.3f}, Sum FY: {sum_fy:.3f}, Sum FZ: {sum_fz:.3f}\n")
            FreeCAD.Console.PrintMessage(f"  Storing {len(supported_nodes)} reaction nodes with their values\n")
            FreeCAD.Console.PrintMessage("  Unit system set to: SI (Metric Engineering)\n")
            
        except Exception as e:
            FreeCAD.Console.PrintError(f"Error printing detailed reaction info: {str(e)}\n")

    def is_node_supported(self, node) -> bool:
        """Check if a node has any support conditions."""
        return (node.support_DX or node.support_DY or node.support_DZ or 
                node.support_RX or node.support_RY or node.support_RZ)

    def format_reaction_label(self, obj, component_type: str, direction: str, magnitude: float) -> str:
        """Format reaction label text based on selected language."""
        # Format value with units
        if GLOBAL_UNITS_AVAILABLE:
            if component_type == "force":
                formatted_value = format_force(magnitude)
            else:  # moment
                formatted_value = format_moment(magnitude)
        else:
            if component_type == "force":
                formatted_value = f"{magnitude:.{obj.Precision}f} kN"
            else:  # moment
                formatted_value = f"{magnitude:.{obj.Precision}f} kN·m"
        
        # Format label based on language
        if hasattr(obj, "Language") and obj.Language == "Thai":
            # Thai language labels
            if direction == "Resultant":
                if component_type == "force":
                    return f"แรงรวม: {formatted_value}"
                else:  # moment
                    return f"โมเมนต์รวม: {formatted_value}"
            else:
                if component_type == "force":
                    direction_map = {"X": "ในแนวแกน X", "Y": "ในแนวแกน Y", "Z": "ในแนวแกน Z"}
                    direction_text = direction_map.get(direction, direction)
                    return f"แรง{direction_text}: {formatted_value}"
                else:  # moment
                    direction_map = {"X": "รอบแกน X", "Y": "รอบแกน Y", "Z": "รอบแกน Z"}
                    direction_text = direction_map.get(direction, direction)
                    return f"โมเมนต์{direction_text}: {formatted_value}"
        else:
            # English language labels (default)
            if direction == "Resultant":
                if component_type == "force":
                    return f"Resultant Force: {formatted_value}"
                else:  # moment
                    return f"Resultant Moment: {formatted_value}"
            else:
                if component_type == "force":
                    return f"F{direction}: {formatted_value}"
                else:  # moment
                    return f"M{direction}: {formatted_value}"

    def create_force_arrow(self, obj, position: FreeCAD.Vector, direction: str, magnitude: float, node_name: str):
        """Create a 3D arrow representing a reaction force."""
        try:
            # Determine arrow direction vector
            if direction == 'X':
                arrow_dir = FreeCAD.Vector(1, 0, 0) if magnitude > 0 else FreeCAD.Vector(-1, 0, 0)
            elif direction == 'Y':
                arrow_dir = FreeCAD.Vector(0, 0, 1) if magnitude > 0 else FreeCAD.Vector(0, 0, -1)  # FreeCAD Y is Pynite Z
            else:  # Z direction
                arrow_dir = FreeCAD.Vector(0, 1, 0) if magnitude > 0 else FreeCAD.Vector(0, -1, 0)  # FreeCAD Z is Pynite Y
            
            # Calculate arrow length based on magnitude and scale
            arrow_length = abs(magnitude) * obj.ScaleReactionForces
            if arrow_length < 0.5:  # Minimum arrow length for visibility
                arrow_length = 0.5
            
            # Create arrow geometry
            arrow_shape = self.create_arrow_shape(position, arrow_dir, arrow_length, obj.ArrowThickness)
            
            # Create FreeCAD object
            arrow_obj = FreeCAD.ActiveDocument.addObject("Part::Feature", f"Reaction_F{direction}_{node_name}")
            arrow_obj.Shape = arrow_shape
            
            # Set appearance
            if arrow_obj.ViewObject:
                # Use gradient color if enabled, otherwise use default force color
                if obj.UseColorGradient:
                    gradient_color = self.get_gradient_color(obj, abs(magnitude))
                    if gradient_color:
                        arrow_obj.ViewObject.ShapeColor = gradient_color
                    else:
                        arrow_obj.ViewObject.ShapeColor = obj.ForceArrowColor[:3]
                else:
                    arrow_obj.ViewObject.ShapeColor = obj.ForceArrowColor[:3]
                arrow_obj.ViewObject.LineWidth = obj.ArrowThickness
                arrow_obj.ViewObject.Transparency = 0
            
            self.reaction_objects.append(arrow_obj)
            
            # Create label if enabled
            if obj.ShowLabels:
                # Format force label based on language
                label_text = self.format_reaction_label(obj, "force", direction, magnitude)
                self.create_reaction_label(obj, position + arrow_dir * arrow_length * 1.1, 
                                         label_text, node_name, direction)
                
        except Exception as e:
            logger.error(f"Error creating force arrow: {str(e)}")

    def create_moment_arrow(self, obj, position: FreeCAD.Vector, axis: str, magnitude: float, node_name: str):
        """Create a 3D curved arrow representing a reaction moment."""
        try:
            # Determine rotation axis
            if axis == 'X':
                axis_dir = FreeCAD.Vector(1, 0, 0)
                perp_dir1 = FreeCAD.Vector(0, 1, 0)
                perp_dir2 = FreeCAD.Vector(0, 0, 1)
            elif axis == 'Y':
                axis_dir = FreeCAD.Vector(0, 1, 0)
                perp_dir1 = FreeCAD.Vector(1, 0, 0)
                perp_dir2 = FreeCAD.Vector(0, 0, 1)
            else:  # Z axis
                axis_dir = FreeCAD.Vector(0, 0, 1)
                perp_dir1 = FreeCAD.Vector(1, 0, 0)
                perp_dir2 = FreeCAD.Vector(0, 1, 0)
            
            # Create curved arrow for moment
            radius = abs(magnitude) * obj.ScaleReactionMoments * 0.2
            if radius < 1.0:  # Minimum radius for visibility
                radius = 1.0
            
            # Create moment arrow geometry (simplified as straight arrow for now)
            arrow_dir = axis_dir if magnitude > 0 else axis_dir * -1
            arrow_shape = self.create_curved_arrow_shape(position, axis_dir, radius, magnitude > 0)
            
            # Create FreeCAD object
            arrow_obj = FreeCAD.ActiveDocument.addObject("Part::Feature", f"Reaction_M{axis}_{node_name}")
            arrow_obj.Shape = arrow_shape
            
            # Set appearance
            if arrow_obj.ViewObject:
                # Use gradient color if enabled, otherwise use default moment color
                if obj.UseColorGradient:
                    gradient_color = self.get_gradient_color(obj, abs(magnitude))
                    if gradient_color:
                        arrow_obj.ViewObject.ShapeColor = gradient_color
                    else:
                        arrow_obj.ViewObject.ShapeColor = obj.MomentArrowColor[:3]
                else:
                    arrow_obj.ViewObject.ShapeColor = obj.MomentArrowColor[:3]
                arrow_obj.ViewObject.LineWidth = obj.ArrowThickness
                arrow_obj.ViewObject.Transparency = 0
            
            self.reaction_objects.append(arrow_obj)
            
            # Create label if enabled
            if obj.ShowLabels:
                label_pos = position + perp_dir1 * radius * 1.5
                
                # Format moment label based on language
                label_text = self.format_reaction_label(obj, "moment", axis, magnitude)
                self.create_reaction_label(obj, label_pos,
                                         label_text, node_name, axis)
                
        except Exception as e:
            logger.error(f"Error creating moment arrow: {str(e)}")

    def create_arrow_shape(self, start_point: FreeCAD.Vector, direction: FreeCAD.Vector, length: float, thickness: float) -> Part.Shape:
        """Create a 3D arrow shape."""
        try:
            # Normalize direction
            direction.normalize()
            
            # Create arrow shaft
            shaft_length = length * 0.8
            shaft_end = start_point + direction * shaft_length
            shaft = Part.makeLine(start_point, shaft_end)
            
            # Create arrow head
            head_length = length * 0.2
            head_width = thickness * 2
            
            # Arrow head tip
            head_tip = start_point + direction * length
            
            # Create perpendicular vectors for arrow head
            if abs(direction.dot(FreeCAD.Vector(0, 0, 1))) < 0.9:
                perp1 = direction.cross(FreeCAD.Vector(0, 0, 1))
            else:
                perp1 = direction.cross(FreeCAD.Vector(1, 0, 0))
            perp1.normalize()
            perp2 = direction.cross(perp1)
            perp2.normalize()
            
            # Arrow head base points
            head_base1 = shaft_end + perp1 * head_width
            head_base2 = shaft_end - perp1 * head_width
            head_base3 = shaft_end + perp2 * head_width
            head_base4 = shaft_end - perp2 * head_width
            
            # Create arrow head faces
            head_lines = [
                Part.makeLine(shaft_end, head_tip),
                Part.makeLine(head_base1, head_tip),
                Part.makeLine(head_base2, head_tip),
                Part.makeLine(head_base3, head_tip),
                Part.makeLine(head_base4, head_tip),
                Part.makeLine(head_base1, head_base3),
                Part.makeLine(head_base3, head_base2),
                Part.makeLine(head_base2, head_base4),
                Part.makeLine(head_base4, head_base1)
            ]
            
            # Combine all lines
            all_lines = [shaft] + head_lines
            compound = Part.makeCompound(all_lines)
            
            return compound
            
        except Exception as e:
            logger.error(f"Error creating arrow shape: {str(e)}")
            # Fallback to simple line
            return Part.makeLine(start_point, start_point + direction * length)

    def create_curved_arrow_shape(self, center: FreeCAD.Vector, axis: FreeCAD.Vector, radius: float, clockwise: bool) -> Part.Shape:
        """Create a curved arrow shape for moments."""
        try:
            # Create a circular arc
            axis.normalize()
            
            # Find two perpendicular vectors to the axis
            if abs(axis.dot(FreeCAD.Vector(0, 0, 1))) < 0.9:
                perp1 = axis.cross(FreeCAD.Vector(0, 0, 1))
            else:
                perp1 = axis.cross(FreeCAD.Vector(1, 0, 0))
            perp1.normalize()
            perp2 = axis.cross(perp1)
            perp2.normalize()
            
            # Create arc points
            num_points = 20
            arc_points = []
            angle_range = math.pi * 1.8  # 324 degrees for a more complete arc
            
            for i in range(num_points + 1):
                angle = (i / num_points) * angle_range
                if not clockwise:
                    angle = -angle
                
                point = center + perp1 * radius * math.cos(angle) + perp2 * radius * math.sin(angle)
                arc_points.append(point)
            
            # Create lines connecting the points
            lines = []
            for i in range(len(arc_points) - 1):
                lines.append(Part.makeLine(arc_points[i], arc_points[i + 1]))
            
            # Add arrow head at the end
            if len(arc_points) >= 2:
                last_direction = arc_points[-1] - arc_points[-2]
                last_direction.normalize()
                arrow_head = self.create_simple_arrow_head(arc_points[-1], last_direction, radius * 0.4)
                lines.append(arrow_head)
            
            return Part.makeCompound(lines)
            
        except Exception as e:
            logger.error(f"Error creating curved arrow: {str(e)}")
            # Fallback to simple circle
            return Part.makeCircle(radius, center, axis)

    def create_simple_arrow_head(self, tip: FreeCAD.Vector, direction: FreeCAD.Vector, size: float) -> Part.Shape:
        """Create a simple arrow head."""
        try:
            direction.normalize()
            
            # Find perpendicular vector
            if abs(direction.dot(FreeCAD.Vector(0, 0, 1))) < 0.9:
                perp = direction.cross(FreeCAD.Vector(0, 0, 1))
            else:
                perp = direction.cross(FreeCAD.Vector(1, 0, 0))
            perp.normalize()
            
            # Arrow head points
            base = tip - direction * size
            side1 = base + perp * size * 0.5
            side2 = base - perp * size * 0.5
            
            # Create triangle
            lines = [
                Part.makeLine(tip, side1),
                Part.makeLine(side1, side2),
                Part.makeLine(side2, tip)
            ]
            
            return Part.makeCompound(lines)
            
        except Exception as e:
            logger.error(f"Error creating arrow head: {str(e)}")
            return Part.makeLine(tip, tip - direction * size)

    def create_reaction_label(self, obj, position: FreeCAD.Vector, text: str, node_name: str, component: str):
        """Create a text label for reaction values."""
        try:
            # Try to use draggable labels first
            try:
                from .draggable_label import create_draggable_reaction_label
                
                # Determine text color based on component type
                text_color = obj.ForceArrowColor[:3] if 'F' in component else obj.MomentArrowColor[:3]
                
                # Get connected point (the reaction location)
                connected_point = position - FreeCAD.Vector(0, 0, 100)  # Offset downward for visibility
                
                # Create draggable label
                label_obj = create_draggable_reaction_label(
                    text=text,
                    position=position,
                    connected_point=connected_point,
                    font_size=obj.LabelFontSize,
                    text_color=text_color + (0.0,)  # Add alpha channel
                )
                
                if label_obj:
                    self.label_objects.append(label_obj)
                    return
                    
            except ImportError:
                logger.info("Draggable labels not available, using simple annotations")
            except Exception as e:
                logger.warning(f"Draggable label creation failed: {str(e)}, using fallback")
            
            # Fallback to simple annotation
            label_obj = FreeCAD.ActiveDocument.addObject("App::Annotation", f"Label_{component}_{node_name}")
            label_obj.LabelText = text
            label_obj.Position = position
            
            if hasattr(label_obj, 'ViewObject'):
                label_obj.ViewObject.FontSize = obj.LabelFontSize
                text_color = obj.ForceArrowColor[:3] if 'F' in component else obj.MomentArrowColor[:3]
                if hasattr(label_obj.ViewObject, 'TextColor'):
                    label_obj.ViewObject.TextColor = text_color
            
            self.label_objects.append(label_obj)
            
        except Exception as e:
            logger.error(f"All label creation methods failed: {str(e)}")
            FreeCAD.Console.PrintError(f"Could not create reaction label: {str(e)}\n")

    def get_available_load_combinations(self, obj) -> List[str]:
        """Get list of available load combinations from the calculation object."""
        try:
            if not obj.ObjectBaseCalc or not hasattr(obj.ObjectBaseCalc, 'model'):
                return []
                
            model = obj.ObjectBaseCalc.model
            if not model or not hasattr(model, 'LoadCombos'):
                return []
                
            return list(model.LoadCombos.keys())
            
        except Exception as e:
            logger.error(f"Error getting load combinations: {str(e)}")
            return []

    def calculate_auto_scale_factors(self, obj):
        """Calculate appropriate scale factors based on model size and reaction magnitudes."""
        try:
            if not obj.ObjectBaseCalc:
                return 1.0, 1.0
                
            calc_obj = obj.ObjectBaseCalc
            model = None
            
            # Try different ways to get the FE model
            if hasattr(calc_obj, 'FEModel') and calc_obj.FEModel:
                model = calc_obj.FEModel
            elif hasattr(calc_obj, 'model') and calc_obj.model:
                model = calc_obj.model
                
            if not model or not hasattr(model, 'nodes') or not model.nodes:
                return 1.0, 1.0
                
            # Calculate model bounding box
            min_x = min_y = min_z = float('inf')
            max_x = max_y = max_z = float('-inf')
            
            for node in model.nodes.values():
                min_x = min(min_x, node.X)
                max_x = max(max_x, node.X)
                min_y = min(min_y, node.Y)
                max_y = max(max_y, node.Y)
                min_z = min(min_z, node.Z)
                max_z = max(max_z, node.Z)
                
            # Calculate model size
            model_size = max(max_x - min_x, max_y - min_y, max_z - min_z)
            if model_size <= 0:
                model_size = 1.0
                
            # Find maximum reaction magnitudes
            max_force = 0.0
            max_moment = 0.0
            load_combo = obj.ActiveLoadCombination
            
            for node in model.nodes.values():
                if self.is_node_supported(node):
                    # Check force reactions
                    for reaction_attr in ['RxnFX', 'RxnFY', 'RxnFZ']:
                        if hasattr(node, reaction_attr):
                            reaction_dict = getattr(node, reaction_attr)
                            if load_combo in reaction_dict:
                                max_force = max(max_force, abs(reaction_dict[load_combo]))
                                
                    # Check moment reactions
                    for reaction_attr in ['RxnMX', 'RxnMY', 'RxnMZ']:
                        if hasattr(node, reaction_attr):
                            reaction_dict = getattr(node, reaction_attr)
                            if load_combo in reaction_dict:
                                max_moment = max(max_moment, abs(reaction_dict[load_combo]))
                                
            # Calculate scale factors (target arrow length is 5% of model size)
            target_length = model_size * 0.05
            
            force_scale = 1.0
            moment_scale = 1.0
            
            if max_force > 1e-6:
                force_scale = target_length / max_force
                
            if max_moment > 1e-6:
                moment_scale = target_length / max_moment
                
            # Limit scale factors to reasonable ranges
            force_scale = max(0.1, min(force_scale, 100.0))
            moment_scale = max(0.1, min(moment_scale, 100.0))
            
            return force_scale, moment_scale
            
        except Exception as e:
            logger.error(f"Error calculating auto scale factors: {str(e)}")
            return 1.0, 1.0

    def calculate_reaction_extremes(self, obj):
        """Calculate minimum and maximum reaction magnitudes for color gradient."""
        try:
            if not obj.ObjectBaseCalc:
                return 0.0, 1.0
                
            calc_obj = obj.ObjectBaseCalc
            model = None
            
            # Try different ways to get the FE model
            if hasattr(calc_obj, 'FEModel') and calc_obj.FEModel:
                model = calc_obj.FEModel
            elif hasattr(calc_obj, 'model') and calc_obj.model:
                model = calc_obj.model
                
            if not model or not hasattr(model, 'nodes') or not model.nodes:
                return 0.0, 1.0
                
            # Find min and max reaction magnitudes
            min_magnitude = float('inf')
            max_magnitude = float('-inf')
            load_combo = obj.ActiveLoadCombination
            
            for node in model.nodes.values():
                if self.is_node_supported(node):
                    # Check all reaction components
                    for reaction_attr in ['RxnFX', 'RxnFY', 'RxnFZ', 'RxnMX', 'RxnMY', 'RxnMZ']:
                        if hasattr(node, reaction_attr):
                            reaction_dict = getattr(node, reaction_attr)
                            if load_combo in reaction_dict:
                                magnitude = abs(reaction_dict[load_combo])
                                if magnitude > obj.MinReactionThreshold:  # Only consider significant reactions
                                    min_magnitude = min(min_magnitude, magnitude)
                                    max_magnitude = max(max_magnitude, magnitude)
                                    
            # Handle edge cases
            if min_magnitude == float('inf'):
                min_magnitude = 0.0
            if max_magnitude == float('-inf'):
                max_magnitude = 1.0
            if min_magnitude >= max_magnitude:
                max_magnitude = min_magnitude + 1.0
                
            return min_magnitude, max_magnitude
            
        except Exception as e:
            logger.error(f"Error calculating reaction extremes: {str(e)}")
            return 0.0, 1.0

    def get_gradient_color(self, obj, magnitude):
        """Calculate gradient color based on reaction magnitude."""
        try:
            # If color gradient is disabled, return default colors
            if not obj.UseColorGradient:
                return None
                
            # Get min and max magnitudes
            min_mag, max_mag = self.calculate_reaction_extremes(obj)
            
            # Normalize magnitude to 0-1 range
            if max_mag > min_mag:
                normalized = (magnitude - min_mag) / (max_mag - min_mag)
            else:
                normalized = 0.5
                
            # Clamp to 0-1 range
            normalized = max(0.0, min(normalized, 1.0))
            
            # Interpolate between min and max colors
            min_color = obj.MinGradientColor[:3]
            max_color = obj.MaxGradientColor[:3]
            
            r = min_color[0] + normalized * (max_color[0] - min_color[0])
            g = min_color[1] + normalized * (max_color[1] - min_color[1])
            b = min_color[2] + normalized * (max_color[2] - min_color[2])
            
            return (r, g, b)
            
        except Exception as e:
            logger.error(f"Error calculating gradient color: {str(e)}")
            return None

    def should_display_reaction(self, obj, node, load_combo, reaction_values):
        """Determine if a reaction should be displayed based on specialized visualization options."""
        try:
            # Always show if no specialized options are enabled
            if not obj.ShowOnlyMaximumReactions and not obj.ShowOnlySignificantReactions:
                return True
                
            # Get all reaction magnitudes at this node for the current load combination
            all_magnitudes = []
            
            # Collect force reaction magnitudes
            for reaction_attr in ['RxnFX', 'RxnFY', 'RxnFZ']:
                if hasattr(node, reaction_attr):
                    reaction_dict = getattr(node, reaction_attr)
                    if load_combo in reaction_dict:
                        magnitude = abs(reaction_dict[load_combo])
                        if magnitude > obj.MinReactionThreshold:
                            all_magnitudes.append(magnitude)
                            
            # Collect moment reaction magnitudes
            for reaction_attr in ['RxnMX', 'RxnMY', 'RxnMZ']:
                if hasattr(node, reaction_attr):
                    reaction_dict = getattr(node, reaction_attr)
                    if load_combo in reaction_dict:
                        magnitude = abs(reaction_dict[load_combo])
                        if magnitude > obj.MinReactionThreshold:
                            all_magnitudes.append(magnitude)
                            
            # If no reactions found, don't display
            if not all_magnitudes:
                return False
                
            # Find maximum magnitude at this node
            max_magnitude = max(all_magnitudes)
            
            # Check if this specific reaction is the maximum
            if obj.ShowOnlyMaximumReactions:
                # For each reaction value passed in, check if it's the maximum
                for magnitude in reaction_values:
                    if abs(magnitude) >= max_magnitude - 1e-9:  # Account for floating point precision
                        return True
                return False
                
            # Check if this reaction is significant
            if obj.ShowOnlySignificantReactions:
                # For each reaction value passed in, check if it meets significance threshold
                for magnitude in reaction_values:
                    if max_magnitude > 0 and abs(magnitude) / max_magnitude >= obj.SignificanceThreshold:
                        return True
                return False
                
            return True
            
        except Exception as e:
            logger.error(f"Error in should_display_reaction: {str(e)}")
            return True  # Default to showing reaction if there's an error

    def create_resultant_force_arrow(self, obj, position: FreeCAD.Vector, fx: float, fy: float, fz: float, node_name: str):
        """Create a 3D arrow representing the resultant force."""
        try:
            # Calculate resultant force vector
            resultant = FreeCAD.Vector(fx, fz, fy)  # Convert Pynite to FreeCAD coords
            magnitude = resultant.Length
            
            if magnitude < obj.MinReactionThreshold:  # No significant resultant force
                return
            
            # Normalize the resultant vector
            direction = resultant.normalize()
            
            # Calculate arrow length based on magnitude and scale
            arrow_length = magnitude * obj.ScaleResultantForces
            if arrow_length < 0.5:  # Minimum arrow length for visibility
                arrow_length = 0.5
            
            # Create arrow geometry
            arrow_shape = self.create_arrow_shape(position, direction, arrow_length, obj.ArrowThickness)
            
            # Create FreeCAD object
            arrow_obj = FreeCAD.ActiveDocument.addObject("Part::Feature", f"Resultant_Force_{node_name}")
            arrow_obj.Shape = arrow_shape
            
            # Set appearance
            if arrow_obj.ViewObject:
                # Use gradient color if enabled, otherwise use default force color
                if obj.UseColorGradient:
                    gradient_color = self.get_gradient_color(obj, magnitude)
                    if gradient_color:
                        arrow_obj.ViewObject.ShapeColor = gradient_color
                    else:
                        arrow_obj.ViewObject.ShapeColor = obj.ForceArrowColor[:3]
                else:
                    arrow_obj.ViewObject.ShapeColor = obj.ForceArrowColor[:3]
                arrow_obj.ViewObject.LineWidth = obj.ArrowThickness
                arrow_obj.ViewObject.Transparency = 0
            
            self.reaction_objects.append(arrow_obj)
            
            # Create label if enabled
            if obj.ShowLabels:
                # Format resultant force label based on language
                label_text = self.format_reaction_label(obj, "force", "Resultant", magnitude)
                self.create_reaction_label(obj, position + direction * arrow_length * 1.1, 
                                         label_text, node_name, "Resultant")
                
        except Exception as e:
            logger.error(f"Error creating resultant force arrow: {str(e)}")

    def create_resultant_moment_arrow(self, obj, position: FreeCAD.Vector, mx: float, my: float, mz: float, node_name: str):
        """Create a 3D arrow representing the resultant moment."""
        try:
            # Calculate resultant moment vector
            resultant = FreeCAD.Vector(mx, mz, my)  # Convert Pynite to FreeCAD coords
            magnitude = resultant.Length
            
            if magnitude < obj.MinReactionThreshold:  # No significant resultant moment
                return
            
            # Normalize the resultant vector
            direction = resultant.normalize()
            
            # Calculate arrow length based on magnitude and scale
            arrow_length = magnitude * obj.ScaleResultantMoments
            if arrow_length < 0.5:  # Minimum arrow length for visibility
                arrow_length = 0.5
            
            # Create arrow geometry
            arrow_shape = self.create_arrow_shape(position, direction, arrow_length, obj.ArrowThickness)
            
            # Create FreeCAD object
            arrow_obj = FreeCAD.ActiveDocument.addObject("Part::Feature", f"Resultant_Moment_{node_name}")
            arrow_obj.Shape = arrow_shape
            
            # Set appearance
            if arrow_obj.ViewObject:
                # Use gradient color if enabled, otherwise use default moment color
                if obj.UseColorGradient:
                    gradient_color = self.get_gradient_color(obj, magnitude)
                    if gradient_color:
                        arrow_obj.ViewObject.ShapeColor = gradient_color
                    else:
                        arrow_obj.ViewObject.ShapeColor = obj.MomentArrowColor[:3]
                else:
                    arrow_obj.ViewObject.ShapeColor = obj.MomentArrowColor[:3]
                arrow_obj.ViewObject.LineWidth = obj.ArrowThickness
                arrow_obj.ViewObject.Transparency = 0
            
            self.reaction_objects.append(arrow_obj)
            
            # Create label if enabled
            if obj.ShowLabels:
                # Format resultant moment label based on language
                label_text = self.format_reaction_label(obj, "moment", "Resultant", magnitude)
                self.create_reaction_label(obj, position + direction * arrow_length * 1.1, 
                                         label_text, node_name, "Resultant")
                
        except Exception as e:
            logger.error(f"Error creating resultant moment arrow: {str(e)}")


class ViewProviderReactionResults:
    """View provider for reaction results."""
    
    def __init__(self, vobj):
        vobj.Proxy = self
    
    def getIcon(self):
        return os.path.join(ICONPATH, "reaction.svg")
    
    def attach(self, vobj):
        self.ViewObject = vobj
        self.Object = vobj.Object
    
    def updateData(self, obj, prop):
        """Update visualization when properties change."""
        if prop in ["ShowReactionFX", "ShowReactionFY", "ShowReactionFZ", 
                   "ShowReactionMX", "ShowReactionMY", "ShowReactionMZ",
                   "ShowResultantForces", "ShowResultantMoments",
                   "ScaleReactionForces", "ScaleReactionMoments", 
                   "ScaleResultantForces", "ScaleResultantMoments",
                   "MinReactionThreshold", "AutoScaleReactions",
                   "UseColorGradient", "MinGradientColor", "MaxGradientColor",
                   "ShowOnlyMaximumReactions", "ShowOnlySignificantReactions", "SignificanceThreshold",
                   "ActiveLoadCombination", "ShowLabels"]:
            if hasattr(obj, 'Proxy') and obj.Proxy:
                obj.Proxy.execute(obj)
    
    def showTextVisualization(self, obj):
        """Public method to show text-based visualization."""
        self.create_text_based_visualization(obj)

    def onChanged(self, vobj, prop):
        pass
    
    def doubleClicked(self, vobj):
        """Open reaction results panel on double-click."""
        try:
            from .reaction_results_panel import ReactionResultsPanel
            panel = ReactionResultsPanel(vobj.Object)
            FreeCADGui.Control.showDialog(panel)
            return True
        except ImportError as e:
            FreeCAD.Console.PrintError(f"Could not import reaction results panel: {str(e)}\n")
            return False
        except Exception as e:
            FreeCAD.Console.PrintError(f"Error opening reaction results panel: {str(e)}\n")
            return False
    
    def getDisplayModes(self, obj):
        return []
    
    def getDefaultDisplayMode(self):
        return "Shaded"
    
    def setDisplayMode(self, mode):
        return mode
    
    def setupContextMenu(self, vobj, menu):
        """Add context menu option to open reaction table panel."""
        action1 = menu.addAction("Open Reaction Table")
        action1.triggered.connect(lambda: self.openReactionTable(vobj.Object))
        
        # Add new action for text-based visualization
        action2 = menu.addAction("Show Text Visualization")
        action2.triggered.connect(lambda: self.showTextVisualization(vobj.Object))
        return False
    
    def openReactionTable(self, obj):
        """Open the reaction table panel."""
        try:
            from .reaction_table_panel import ReactionTablePanel
            panel = ReactionTablePanel(obj)
            FreeCADGui.Control.showDialog(panel)
        except ImportError as e:
            FreeCAD.Console.PrintError(f"Could not import reaction table panel: {str(e)}\n")
        except Exception as e:
            FreeCAD.Console.PrintError(f"Error opening reaction table panel: {str(e)}\n")
    
    def showTextVisualization(self, obj):
        """Show text-based visualization of reactions."""
        try:
            if hasattr(obj, 'Proxy') and obj.Proxy:
                obj.Proxy.create_text_based_visualization(obj)
            else:
                FreeCAD.Console.PrintError("ReactionResults proxy not found\n")
        except Exception as e:
            FreeCAD.Console.PrintError(f"Error showing text visualization: {str(e)}\n")


class CommandReactionResults:
    """Command to create reaction results visualization."""
    
    def GetResources(self):
        return {
            'Pixmap': os.path.join(ICONPATH, "reaction.svg"),
            'MenuText': "Reaction Results", 
            'ToolTip': "Display reaction forces and moments at support points"
        }
    
    def Activated(self):
        try:
            # Check if a calculation object is selected
            selection = FreeCADGui.Selection.getSelection()
            calc_obj = None
            
            for obj in selection:
                if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, '__class__'):
                    if 'Calc' in obj.Proxy.__class__.__name__:
                        calc_obj = obj
                        break
            
            if not calc_obj:
                # Try to find calc object in document
                for obj in FreeCAD.ActiveDocument.Objects:
                    if hasattr(obj, 'Proxy') and hasattr(obj.Proxy, '__class__'):
                        if 'Calc' in obj.Proxy.__class__.__name__:
                            calc_obj = obj
                            break
            
            if not calc_obj:
                QtWidgets.QMessageBox.warning(None, "Warning", 
                    "Please select or create a calculation object first, and run the analysis.")
                return
            
            # Check if analysis has been run
            model_available = False
            if hasattr(calc_obj, 'model') and calc_obj.model:
                model_available = True
            elif hasattr(calc_obj, 'FEModel') and calc_obj.FEModel:
                model_available = True
            
            if not model_available:
                QtWidgets.QMessageBox.warning(None, "Warning", 
                    "Please run the structural analysis first or select a valid calculation object.")
                return
            
            # Create reaction results object
            reaction_obj = FreeCAD.ActiveDocument.addObject("App::DocumentObjectGroupPython", "ReactionResults")
            ReactionResults(reaction_obj, calc_obj)
            ViewProviderReactionResults(reaction_obj.ViewObject)
            
            FreeCAD.ActiveDocument.recompute()
            
            # Show the control panel
            try:
                from .reaction_results_panel import ReactionResultsPanel
                panel = ReactionResultsPanel(reaction_obj)
                FreeCADGui.Control.showDialog(panel)
            except ImportError as e:
                FreeCAD.Console.PrintError(f"Could not import reaction results panel: {str(e)}\n")
                # Continue without panel - user can double-click object to open it later
            except Exception as e:
                FreeCAD.Console.PrintWarning(f"Could not open reaction panel: {str(e)}\n")
            
        except Exception as e:
            logger.error(f"Error in CommandReactionResults.Activated: {str(e)}")
            QtWidgets.QMessageBox.critical(None, "Error", f"Failed to create reaction results: {str(e)}")
    
    def IsActive(self):
        return FreeCAD.ActiveDocument is not None


# Register the command
if hasattr(FreeCADGui, 'addCommand'):
    FreeCADGui.addCommand('ReactionResults', CommandReactionResults())