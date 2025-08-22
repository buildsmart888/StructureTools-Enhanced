# -*- coding: utf-8 -*-
"""
StructuralNode - Professional node object with connectivity and constraints

This module provides a comprehensive node object for structural engineering
with connection details, boundary conditions, and analysis integration.
"""

import FreeCAD as App
import FreeCADGui as Gui
import Part
from typing import List, Dict, Tuple, Optional
import os


class StructuralNode:
    """
    Custom Document Object for structural nodes with enhanced functionality.
    
    This class provides professional-grade node objects for structural analysis
    with connection details, constraint handling, and visual representation.
    """
    
    def __init__(self, obj):
        """
        Initialize StructuralNode object.
        
        Args:
            obj: FreeCAD DocumentObject to be enhanced
        """
        self.Type = "StructuralNode"
        obj.Proxy = self
        
        # Geometric properties
        obj.addProperty("App::PropertyVector", "Position", "Geometry", 
                       "Node position in global coordinates")
        obj.Position = App.Vector(0, 0, 0)
        
        obj.addProperty("App::PropertyFloat", "Tolerance", "Geometry",
                       "Tolerance for node coincidence checking")
        obj.Tolerance = 1.0  # mm
        
        # Boundary conditions (restraints)
        obj.addProperty("App::PropertyBool", "RestraintX", "Restraints", 
                       "Restraint in global X direction")
        obj.addProperty("App::PropertyBool", "RestraintY", "Restraints",
                       "Restraint in global Y direction") 
        obj.addProperty("App::PropertyBool", "RestraintZ", "Restraints",
                       "Restraint in global Z direction")
        obj.addProperty("App::PropertyBool", "RestraintRX", "Restraints",
                       "Restraint for rotation about X axis")
        obj.addProperty("App::PropertyBool", "RestraintRY", "Restraints", 
                       "Restraint for rotation about Y axis")
        obj.addProperty("App::PropertyBool", "RestraintRZ", "Restraints",
                       "Restraint for rotation about Z axis")
        
        # Spring supports
        obj.addProperty("App::PropertyFloat", "SpringX", "Springs",
                       "Spring stiffness in X direction (0 = rigid)")
        obj.addProperty("App::PropertyFloat", "SpringY", "Springs", 
                       "Spring stiffness in Y direction (0 = rigid)")
        obj.addProperty("App::PropertyFloat", "SpringZ", "Springs",
                       "Spring stiffness in Z direction (0 = rigid)")
        obj.addProperty("App::PropertyFloat", "SpringRX", "Springs",
                       "Rotational spring stiffness about X axis")
        obj.addProperty("App::PropertyFloat", "SpringRY", "Springs",
                       "Rotational spring stiffness about Y axis") 
        obj.addProperty("App::PropertyFloat", "SpringRZ", "Springs",
                       "Rotational spring stiffness about Z axis")
        
        # Prescribed displacements
        obj.addProperty("App::PropertyFloat", "PrescribedDX", "Prescribed",
                       "Prescribed displacement in X direction")
        obj.addProperty("App::PropertyFloat", "PrescribedDY", "Prescribed",
                       "Prescribed displacement in Y direction")
        obj.addProperty("App::PropertyFloat", "PrescribedDZ", "Prescribed", 
                       "Prescribed displacement in Z direction")
        obj.addProperty("App::PropertyFloat", "PrescribedRX", "Prescribed",
                       "Prescribed rotation about X axis")
        obj.addProperty("App::PropertyFloat", "PrescribedRY", "Prescribed",
                       "Prescribed rotation about Y axis")
        obj.addProperty("App::PropertyFloat", "PrescribedRZ", "Prescribed",
                       "Prescribed rotation about Z axis")
        
        # Nodal loads
        obj.addProperty("App::PropertyFloatList", "NodalLoadsX", "Loads",
                       "Applied forces in X direction by load case")
        obj.addProperty("App::PropertyFloatList", "NodalLoadsY", "Loads",
                       "Applied forces in Y direction by load case")
        obj.addProperty("App::PropertyFloatList", "NodalLoadsZ", "Loads", 
                       "Applied forces in Z direction by load case")
        obj.addProperty("App::PropertyFloatList", "NodalMomentsX", "Loads",
                       "Applied moments about X axis by load case")
        obj.addProperty("App::PropertyFloatList", "NodalMomentsY", "Loads",
                       "Applied moments about Y axis by load case")
        obj.addProperty("App::PropertyFloatList", "NodalMomentsZ", "Loads",
                       "Applied moments about Z axis by load case")
        
        # Connection details
        obj.addProperty("App::PropertyEnumeration", "ConnectionType", "Connection",
                       "Type of connection at this node")
        obj.ConnectionType = ["Rigid", "Pinned", "Semi-Rigid", "Special"]
        obj.ConnectionType = "Rigid"
        
        obj.addProperty("App::PropertyLinkList", "ConnectedMembers", "Connection",
                       "List of members connected to this node")
        
        obj.addProperty("App::PropertyFloat", "ConnectionStiffness", "Connection", 
                       "Connection stiffness for semi-rigid connections")
        
        # Analysis results storage
        obj.addProperty("App::PropertyFloatList", "DisplacementX", "Results",
                       "Calculated displacements in X by load combination")
        obj.addProperty("App::PropertyFloatList", "DisplacementY", "Results",
                       "Calculated displacements in Y by load combination")
        obj.addProperty("App::PropertyFloatList", "DisplacementZ", "Results",
                       "Calculated displacements in Z by load combination")
        obj.addProperty("App::PropertyFloatList", "RotationX", "Results", 
                       "Calculated rotations about X by load combination")
        obj.addProperty("App::PropertyFloatList", "RotationY", "Results",
                       "Calculated rotations about Y by load combination")
        obj.addProperty("App::PropertyFloatList", "RotationZ", "Results",
                       "Calculated rotations about Z by load combination")
        
        # Reaction forces (for restrained nodes)
        obj.addProperty("App::PropertyFloatList", "ReactionX", "Results",
                       "Reaction forces in X by load combination")
        obj.addProperty("App::PropertyFloatList", "ReactionY", "Results", 
                       "Reaction forces in Y by load combination")
        obj.addProperty("App::PropertyFloatList", "ReactionZ", "Results",
                       "Reaction forces in Z by load combination")
        obj.addProperty("App::PropertyFloatList", "ReactionMX", "Results",
                       "Reaction moments about X by load combination")
        obj.addProperty("App::PropertyFloatList", "ReactionMY", "Results",
                       "Reaction moments about Y by load combination")
        obj.addProperty("App::PropertyFloatList", "ReactionMZ", "Results",
                       "Reaction moments about Z by load combination")
        
        # Identification and organization
        obj.addProperty("App::PropertyString", "NodeID", "Identification",
                       "Unique node identifier")
        obj.addProperty("App::PropertyString", "Description", "Identification", 
                       "Node description or notes")
        
        # Internal properties
        obj.addProperty("App::PropertyInteger", "InternalID", "Internal",
                       "Internal numbering for analysis")
        obj.addProperty("App::PropertyBool", "IsActive", "Internal",
                       "Node is active in current analysis")
        obj.IsActive = True
    
    def onChanged(self, obj, prop: str) -> None:
        """
        Handle property changes with validation and updates.
        
        Args:
            obj: The DocumentObject being changed
            prop: Name of the changed property
        """
        if prop == "Position":
            self._update_visual_representation(obj)
        elif prop in ["RestraintX", "RestraintY", "RestraintZ", 
                     "RestraintRX", "RestraintRY", "RestraintRZ"]:
            self._update_restraint_visualization(obj)
        elif prop == "ConnectionType":
            self._update_connection_properties(obj)
    
    def _update_visual_representation(self, obj) -> None:
        """Update the 3D visual representation of the node."""
        if not hasattr(obj, 'Position'):
            return
        
        # Create node geometry
        node_size = 5.0  # mm - make this configurable
        sphere = Part.makeSphere(node_size, obj.Position)
        
        # Add restraint symbols if applicable
        restraint_symbols = self._create_restraint_symbols(obj)
        if restraint_symbols:
            combined_shape = Part.makeCompound([sphere] + restraint_symbols)
            obj.Shape = combined_shape
        else:
            obj.Shape = sphere
    
    def _create_restraint_symbols(self, obj) -> List[Part.Shape]:
        """Create visual symbols for boundary conditions."""
        symbols = []
        
        if not hasattr(obj, 'Position'):
            return symbols
        
        pos = obj.Position
        symbol_size = 15.0  # mm
        
        # Fixed support (all translations restrained)
        if (getattr(obj, 'RestraintX', False) and 
            getattr(obj, 'RestraintY', False) and 
            getattr(obj, 'RestraintZ', False)):
            
            # Create triangular base symbol
            base = Part.makeCone(symbol_size, 0, symbol_size * 0.8)
            base.translate(App.Vector(pos.x, pos.y, pos.z - symbol_size * 0.8))
            symbols.append(base)
        
        # Pinned support (translations restrained, rotations free)
        elif (getattr(obj, 'RestraintX', False) and 
              getattr(obj, 'RestraintY', False) and 
              getattr(obj, 'RestraintZ', False) and
              not getattr(obj, 'RestraintRX', False) and
              not getattr(obj, 'RestraintRY', False) and
              not getattr(obj, 'RestraintRZ', False)):
            
            # Create circular base symbol
            cylinder = Part.makeCylinder(symbol_size * 0.6, symbol_size * 0.3)
            cylinder.translate(App.Vector(pos.x, pos.y, pos.z - symbol_size * 0.3))
            symbols.append(cylinder)
        
        # Roller support (vertical restraint only)
        elif getattr(obj, 'RestraintZ', False):
            # Create roller symbol (cylinder)
            roller = Part.makeCylinder(symbol_size * 0.4, symbol_size * 0.2)
            roller.translate(App.Vector(pos.x, pos.y, pos.z - symbol_size * 0.2))
            symbols.append(roller)
        
        return symbols
    
    def _update_restraint_visualization(self, obj) -> None:
        """Update visualization when restraints change."""
        self._update_visual_representation(obj)
    
    def _update_connection_properties(self, obj) -> None:
        """Update connection-related properties based on connection type."""
        if not hasattr(obj, 'ConnectionType'):
            return
        
        conn_type = obj.ConnectionType
        
        if conn_type == "Pinned":
            # Set default pinned connection (moment releases)
            obj.RestraintRX = False
            obj.RestraintRY = False  
            obj.RestraintRZ = False
        elif conn_type == "Rigid":
            # Rigid connection - no releases
            pass  # Keep existing settings
        elif conn_type == "Semi-Rigid":
            # Enable connection stiffness input
            if not hasattr(obj, 'ConnectionStiffness'):
                obj.ConnectionStiffness = 1000.0  # Default stiffness
    
    def execute(self, obj) -> None:
        """
        Update node geometry and validate properties.
        
        Args:
            obj: The DocumentObject being executed
        """
        # Update visual representation
        self._update_visual_representation(obj)
        
        # Validate nodal loads consistency
        self._validate_nodal_loads(obj)
        
        # Update connected members if needed
        self._update_member_connections(obj)
    
    def _validate_nodal_loads(self, obj) -> None:
        """Validate that nodal loads are consistent across load cases."""
        load_properties = [
            'NodalLoadsX', 'NodalLoadsY', 'NodalLoadsZ',
            'NodalMomentsX', 'NodalMomentsY', 'NodalMomentsZ'
        ]
        
        # Check that all load arrays have the same length
        lengths = []
        for prop in load_properties:
            if hasattr(obj, prop):
                lengths.append(len(getattr(obj, prop, [])))
        
        if lengths and len(set(lengths)) > 1:
            App.Console.PrintWarning(
                f"Node {obj.Label}: Inconsistent load case count across load types\n"
            )
    
    def _update_member_connections(self, obj) -> None:
        """Update the list of connected members."""
        if not hasattr(obj, 'ConnectedMembers'):
            return
        
        # This would be implemented to automatically detect
        # which members are connected to this node
        # For now, it's manually managed
        pass
    
    def get_restraint_code(self) -> str:
        """
        Get restraint code for analysis (e.g., "111000" for pinned).
        
        Returns:
            6-character string representing restraints (1=restrained, 0=free)
        """
        restraints = [
            getattr(self.Object, 'RestraintX', False),
            getattr(self.Object, 'RestraintY', False), 
            getattr(self.Object, 'RestraintZ', False),
            getattr(self.Object, 'RestraintRX', False),
            getattr(self.Object, 'RestraintRY', False),
            getattr(self.Object, 'RestraintRZ', False)
        ]
        
        return ''.join('1' if r else '0' for r in restraints)
    
    def is_restrained(self) -> bool:
        """Check if node has any restraints."""
        restraint_props = [
            'RestraintX', 'RestraintY', 'RestraintZ',
            'RestraintRX', 'RestraintRY', 'RestraintRZ'
        ]
        
        return any(getattr(self.Object, prop, False) for prop in restraint_props)
    
    def get_degrees_of_freedom(self) -> int:
        """Get number of free degrees of freedom."""
        restraint_count = sum(1 for prop in [
            'RestraintX', 'RestraintY', 'RestraintZ', 
            'RestraintRX', 'RestraintRY', 'RestraintRZ'
        ] if getattr(self.Object, prop, False))
        
        return 6 - restraint_count


class ViewProviderStructuralNode:
    """
    ViewProvider for StructuralNode with enhanced visualization.
    """
    
    def __init__(self, vobj):
        """Initialize ViewProvider."""
        vobj.Proxy = self
        self.Object = vobj.Object
        
        # Visualization properties
        vobj.addProperty("App::PropertyBool", "ShowRestraints", "Display",
                        "Show restraint symbols")
        vobj.ShowRestraints = True
        
        vobj.addProperty("App::PropertyBool", "ShowNodeID", "Display", 
                        "Show node ID label")
        vobj.ShowNodeID = True
        
        vobj.addProperty("App::PropertyFloat", "NodeSize", "Display",
                        "Node symbol size")
        vobj.NodeSize = 5.0
        
        vobj.addProperty("App::PropertyColor", "NodeColor", "Display",
                        "Node color")
        vobj.NodeColor = (0.0, 0.5, 1.0)  # Blue
        
        vobj.addProperty("App::PropertyColor", "RestraintColor", "Display",
                        "Restraint symbol color") 
        vobj.RestraintColor = (1.0, 0.0, 0.0)  # Red
    
    def getIcon(self) -> str:
        """
        Return icon based on node type and restraints.
        
        Returns:
            Path to appropriate icon file
        """
        if not hasattr(self.Object, 'RestraintX'):
            return self._get_icon_path("node_free.svg")
        
        # Determine support type
        if self.Object.Proxy.is_restrained():
            restraint_code = self.Object.Proxy.get_restraint_code()
            
            if restraint_code == "111111":  # Fixed
                return self._get_icon_path("node_fixed.svg")
            elif restraint_code == "111000":  # Pinned
                return self._get_icon_path("node_pinned.svg") 
            elif restraint_code == "001000":  # Roller
                return self._get_icon_path("node_roller.svg")
            else:  # General restraint
                return self._get_icon_path("node_restrained.svg")
        else:
            return self._get_icon_path("node_free.svg")
    
    def _get_icon_path(self, icon_name: str) -> str:
        """Get full path to icon file."""
        icon_dir = os.path.join(os.path.dirname(__file__), "..", "resources", "icons")
        return os.path.join(icon_dir, icon_name)
    
    def setEdit(self, vobj, mode: int) -> bool:
        """
        Open custom task panel for node editing.
        
        Args:
            vobj: ViewObject being edited
            mode: Edit mode
            
        Returns:
            True if edit mode started successfully
        """
        if mode == 0:
            from ..taskpanels.NodePropertiesPanel import NodePropertiesPanel
            self.panel = NodePropertiesPanel(vobj.Object)
            Gui.Control.showDialog(self.panel)
            return True
        return False
    
    def unsetEdit(self, vobj, mode: int) -> bool:
        """Close node editing panel."""
        Gui.Control.closeDialog() 
        return True
    
    def doubleClicked(self, vobj) -> bool:
        """Handle double-click to open properties panel."""
        return self.setEdit(vobj, 0)
    
    def updateData(self, obj, prop: str) -> None:
        """Update visualization when object data changes."""
        if prop in ["Position", "RestraintX", "RestraintY", "RestraintZ",
                   "RestraintRX", "RestraintRY", "RestraintRZ"]:
            # Trigger visual update
            pass
    
    def getDisplayModes(self, vobj) -> list:
        """Return available display modes."""
        return ["Standard", "Wireframe"]
    
    def getDefaultDisplayMode(self) -> str:
        """Return default display mode."""
        return "Standard"
    
    def setDisplayMode(self, mode: str) -> str:
        """Set display mode."""
        return mode