# -*- coding: utf-8 -*-
"""
Simple AreaLoad - Simplified version without enumeration issues

This is a temporary simplified version to test basic functionality
without complex enumeration properties that cause syntax errors.
"""

import FreeCAD as App
import FreeCADGui as Gui
import Part
import math

class SimpleAreaLoad:
    """Simplified AreaLoad object for basic functionality testing"""
    
    def __init__(self, obj):
        """Initialize simple area load object"""
        self.Type = "SimpleAreaLoad"
        obj.Proxy = self
        
        # Basic properties only (no enumerations)
        obj.addProperty("App::PropertyLinkList", "TargetFaces", "Geometry",
                       "Faces or surfaces to apply load")
        
        obj.addProperty("App::PropertyPressure", "LoadIntensity", "Load",
                       "Load intensity (pressure)")
        obj.LoadIntensity = "5.0 kN/m^2"
        
        obj.addProperty("App::PropertyVector", "LoadDirection", "Geometry",
                       "Load direction vector")
        obj.LoadDirection = App.Vector(0, 0, -1)  # Downward
        
        obj.addProperty("App::PropertyString", "LoadType", "Load",
                       "Type of area load")
        obj.LoadType = "Dead Load"
        
        obj.addProperty("App::PropertyString", "LoadCategory", "Load",
                       "Load category")
        obj.LoadCategory = "DL"
        
        obj.addProperty("App::PropertyArea", "LoadedArea", "Results",
                       "Total loaded area")
        
        obj.addProperty("App::PropertyForce", "TotalLoad", "Results",
                       "Total applied load")
        
        obj.addProperty("App::PropertyString", "LoadID", "Identification",
                       "Unique load identifier")
        
        # Visualization properties
        obj.addProperty("App::PropertyBool", "ShowLoadArrows", "Visualization",
                       "Show load arrows")
        obj.ShowLoadArrows = True
        
        obj.addProperty("App::PropertyFloat", "ArrowScale", "Visualization",
                       "Scale factor for load arrows")
        obj.ArrowScale = 1.0
        
        obj.addProperty("App::PropertyInteger", "ArrowDensity", "Visualization",
                       "Number of arrows per direction")
        obj.ArrowDensity = 5
        
        App.Console.PrintMessage("SimpleAreaLoad initialized successfully\n")
    
    def execute(self, obj):
        """Update load properties and visualization"""
        try:
            if obj.TargetFaces:
                self._calculateLoadProperties(obj)
                if obj.ShowLoadArrows:
                    self._createSimpleVisualization(obj)
        except Exception as e:
            App.Console.PrintError(f"Error in SimpleAreaLoad.execute: {e}\n")
    
    def _calculateLoadProperties(self, obj):
        """Calculate basic load properties"""
        try:
            total_area = 0.0
            for face_obj in obj.TargetFaces:
                if hasattr(face_obj, 'Shape') and hasattr(face_obj.Shape, 'Area'):
                    total_area += face_obj.Shape.Area
            
            obj.LoadedArea = f"{total_area} mm^2"
            
            # Calculate total force
            if hasattr(obj, 'LoadIntensity'):
                intensity_str = str(obj.LoadIntensity).split()[0]
                try:
                    intensity = float(intensity_str)
                    total_force = intensity * total_area / 1000000.0  # Convert mm² to m²
                    obj.TotalLoad = f"{total_force} N"
                except:
                    obj.TotalLoad = "0 N"
            
            App.Console.PrintMessage(f"Calculated area: {total_area:.2f} mm², total load: {obj.TotalLoad}\n")
            
        except Exception as e:
            App.Console.PrintError(f"Error calculating load properties: {e}\n")
    
    def _createSimpleVisualization(self, obj):
        """Create simple load visualization"""
        try:
            if not obj.TargetFaces:
                return
            
            doc = App.ActiveDocument
            if not doc:
                return
            
            # Clear existing visualization
            existing_arrows = [o for o in doc.Objects if o.Label.startswith(f"LoadArrow_{obj.Label}")]
            for arrow in existing_arrows:
                try:
                    doc.removeObject(arrow.Name)
                except:
                    pass
            
            # Create simple arrows
            arrow_count = 0
            density = obj.ArrowDensity if obj.ArrowDensity > 0 else 5
            
            for face_obj in obj.TargetFaces:
                if hasattr(face_obj, 'Shape'):
                    for face in face_obj.Shape.Faces:
                        # Get face bounding box
                        bbox = face.BoundBox
                        
                        # Create arrows in grid pattern
                        x_step = (bbox.XMax - bbox.XMin) / density
                        y_step = (bbox.YMax - bbox.YMin) / density
                        
                        for i in range(density):
                            for j in range(density):
                                try:
                                    x = bbox.XMin + (i + 0.5) * x_step
                                    y = bbox.YMin + (j + 0.5) * y_step
                                    z = bbox.ZMin
                                    
                                    # Create arrow at this position
                                    position = App.Vector(x, y, z)
                                    arrow = self._createArrow(doc, position, obj.LoadDirection, obj.ArrowScale, arrow_count)
                                    if arrow:
                                        arrow_count += 1
                                        
                                except Exception as e:
                                    continue
            
            App.Console.PrintMessage(f"Created {arrow_count} load arrows for {obj.Label}\n")
            
        except Exception as e:
            App.Console.PrintError(f"Error creating visualization: {e}\n")
    
    def _createArrow(self, doc, position, direction, scale, index):
        """Create a single load arrow"""
        try:
            # Arrow dimensions
            length = 200 * scale  # 200mm base length
            radius = length * 0.05
            head_length = length * 0.3
            head_radius = radius * 2
            
            # Normalize direction
            dir_length = math.sqrt(direction.x**2 + direction.y**2 + direction.z**2)
            if dir_length > 0:
                norm_dir = App.Vector(direction.x/dir_length, direction.y/dir_length, direction.z/dir_length)
            else:
                norm_dir = App.Vector(0, 0, -1)
            
            # Create arrow shaft
            shaft_end = position + norm_dir * (length - head_length)
            shaft = Part.makeCylinder(radius, length - head_length, position, norm_dir)
            
            # Create arrow head
            head = Part.makeCone(head_radius, 0, head_length, shaft_end, norm_dir)
            
            # Combine shaft and head
            arrow_shape = Part.makeCompound([shaft, head])
            
            # Create FreeCAD object
            arrow_name = f"LoadArrow_{App.ActiveDocument.getObject('SimpleAreaLoad').Label}_{index}"
            arrow_obj = doc.addObject("Part::Feature", arrow_name)
            arrow_obj.Shape = arrow_shape
            
            # Set color
            if hasattr(arrow_obj, 'ViewObject'):
                arrow_obj.ViewObject.ShapeColor = (1.0, 0.0, 0.0)  # Red
                arrow_obj.ViewObject.Transparency = 20
            
            return arrow_obj
            
        except Exception as e:
            App.Console.PrintWarning(f"Error creating arrow: {e}\n")
            return None
    
    def onChanged(self, obj, prop):
        """Handle property changes"""
        try:
            if prop == "TargetFaces":
                self._calculateLoadProperties(obj)
            elif prop in ["ShowLoadArrows", "ArrowScale", "ArrowDensity"]:
                if obj.ShowLoadArrows:
                    self._createSimpleVisualization(obj)
                else:
                    self._clearVisualization(obj)
            elif prop == "LoadIntensity":
                self._calculateLoadProperties(obj)
        except Exception as e:
            App.Console.PrintError(f"Error in onChanged: {e}\n")
    
    def _clearVisualization(self, obj):
        """Clear load visualization"""
        try:
            doc = App.ActiveDocument
            if not doc:
                return
            
            # Remove arrows
            existing_arrows = [o for o in doc.Objects if o.Label.startswith(f"LoadArrow_{obj.Label}")]
            for arrow in existing_arrows:
                try:
                    doc.removeObject(arrow.Name)
                except:
                    pass
        except Exception as e:
            App.Console.PrintError(f"Error clearing visualization: {e}\n")

class ViewProviderSimpleAreaLoad:
    """ViewProvider for SimpleAreaLoad"""
    
    def __init__(self, vobj):
        vobj.Proxy = self
        self.Object = vobj.Object
    
    def getIcon(self):
        """Return icon path"""
        return ":/icons/area_load.svg"
    
    def doubleClicked(self, vobj):
        """Handle double click"""
        return True

def makeSimpleAreaLoad(target_faces=None, magnitude="5.0 kN/m^2", load_type="Dead Load", name="SimpleAreaLoad"):
    """
    Create a simple AreaLoad object for testing.
    
    Args:
        target_faces: List of faces to apply load to
        magnitude: Load magnitude
        load_type: Type of load
        name: Object name
        
    Returns:
        Created SimpleAreaLoad object
    """
    try:
        doc = App.ActiveDocument
        if not doc:
            App.Console.PrintError("No active document\n")
            return None
        
        App.Console.PrintMessage(f"Creating SimpleAreaLoad: {name}\n")
        
        # Create object
        obj = doc.addObject("App::DocumentObjectGroupPython", name)
        if not obj:
            App.Console.PrintError("Failed to create object\n")
            return None
        
        # Initialize proxy
        SimpleAreaLoad(obj)
        
        # Create ViewProvider
        if App.GuiUp:
            try:
                ViewProviderSimpleAreaLoad(obj.ViewObject)
            except Exception as e:
                App.Console.PrintWarning(f"ViewProvider warning: {e}\n")
        
        # Set properties
        if target_faces:
            obj.TargetFaces = target_faces if isinstance(target_faces, list) else [target_faces]
        
        obj.LoadIntensity = magnitude
        obj.LoadType = load_type
        
        # Generate ID
        load_count = len([o for o in doc.Objects if o.Label.startswith("SimpleAreaLoad")])
        obj.LoadID = f"SAL{load_count + 1:03d}"
        
        # Update
        obj.recompute()
        doc.recompute()
        
        App.Console.PrintMessage(f"Successfully created SimpleAreaLoad: {obj.Label}\n")
        return obj
        
    except Exception as e:
        App.Console.PrintError(f"Error creating SimpleAreaLoad: {e}\n")
        return None