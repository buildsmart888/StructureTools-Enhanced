import os, math, copy

# Guard FreeCAD imports so this module can be imported in headless/test environments
try:
    import FreeCAD, App, FreeCADGui, Part
    FREECAD_AVAILABLE = True
except Exception:
    FreeCAD = None
    App = None
    FreeCADGui = None
    Part = None
    FREECAD_AVAILABLE = False

# Safe GUI imports with fallbacks
try:
    from PySide import QtWidgets
    from PySide.QtGui import QPixmap
    GUI_AVAILABLE = True
except ImportError:
    try:
        from PySide2 import QtWidgets
        from PySide2.QtGui import QPixmap
        GUI_AVAILABLE = True
    except ImportError:
        try:
            # Fallback to FreeCAD's GUI if available
            import FreeCADGui as Gui
            QtWidgets = None
            QPixmap = None
            GUI_AVAILABLE = False
        except ImportError:
            # No GUI available
            QtWidgets = None
            QPixmap = None 
            GUI_AVAILABLE = False

# Import Section Standards Database and Core Components
try:
    from .data.SectionStandards import SECTION_STANDARDS, SECTION_CATEGORIES, get_section_info
    from .core import get_section_manager, get_geometry_factory, calculate_properties_from_face
    SECTION_DATABASE_AVAILABLE = True
    CORE_ARCHITECTURE_AVAILABLE = True
except ImportError:
    SECTION_DATABASE_AVAILABLE = False
    CORE_ARCHITECTURE_AVAILABLE = False
    SECTION_STANDARDS = {}
    SECTION_CATEGORIES = {}
    get_section_info = lambda x: {}
    get_section_manager = lambda: None
    get_geometry_factory = lambda: None
    calculate_properties_from_face = lambda x: {}

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
    from .utils.universal_thai_units import enhance_with_thai_units, thai_geometric_units
    THAI_UNITS_AVAILABLE = True
except ImportError:
    THAI_UNITS_AVAILABLE = False
    enhance_with_thai_units = lambda x, t: x
    thai_geometric_units = lambda f: f

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")
# path_ui = str(os.path.dirname(__file__))+'/resources/ui/sectionGui.ui'

# Console logging helper functions with proper imports
def safe_console_log(msg, log_type="message"):
    """Safe console logging with fallback"""
    try:
        import FreeCAD
        if log_type == "error":
            FreeCAD.Console.PrintError(f"{msg}\n")
        elif log_type == "warning":
            FreeCAD.Console.PrintWarning(f"{msg}\n")
        else:
            FreeCAD.Console.PrintLog(f"{msg}\n")
    except:
        print(f"{log_type.upper()}: {msg}")

def show_error_message(msg, title="Section Error", details=None):
    """Show professional error message with optional details"""
    # Always log to console first
    safe_console_log(f"{title}: {msg}", "error")
    if details:
        safe_console_log(f"Details: {details}", "message")
    
    # Try to show GUI dialog if available
    if GUI_AVAILABLE and QtWidgets:
        try:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Critical)
            msg_box.setWindowTitle(title)
            msg_box.setText(msg)
            
            if details:
                msg_box.setDetailedText(details)
            
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg_box.exec_()
            
        except Exception as e:
            # GUI failed, already logged to console
            safe_console_log(f"GUI Error: {str(e)}", "error")

def show_warning_message(msg, title="Section Warning"):
    """Show warning message"""
    # Always log to console first
    safe_console_log(f"{title}: {msg}", "warning")
    
    # Try to show GUI dialog if available
    if GUI_AVAILABLE and QtWidgets:
        try:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Warning)
            msg_box.setWindowTitle(title)
            msg_box.setText(msg)
            msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg_box.exec_()
        except Exception as e:
            # GUI failed, already logged to console
            safe_console_log(f"GUI Error: {str(e)}", "error")

def validate_section_properties(obj):
    """Validate section properties for engineering reasonableness"""
    errors = []
    warnings = []
    
    try:
        # Check area
        if hasattr(obj, 'Area') and obj.Area:
            area_value = float(str(obj.Area).split()[0]) if ' ' in str(obj.Area) else float(obj.Area)
            if area_value <= 0:
                errors.append("Section area must be positive")
            elif area_value < 100:  # mm²
                warnings.append(f"Very small section area: {area_value} mm² - check units")
            elif area_value > 1000000:  # mm²
                warnings.append(f"Very large section area: {area_value} mm² - check units")
        
        # Check moments of inertia
        for prop_name, prop_attr in [("Moment of Inertia Y", "MomentInertiaY"), ("Moment of Inertia Z", "MomentInertiaZ")]:
            if hasattr(obj, prop_attr):
                value = getattr(obj, prop_attr, 0)
                if value < 0:
                    errors.append(f"{prop_name} cannot be negative")
                elif value == 0 and hasattr(obj, 'Area') and obj.Area > 0:
                    warnings.append(f"{prop_name} is zero - may indicate calculation error")
        
        # Check dimensions
        for dim_name, dim_attr in [("Depth", "Depth"), ("Flange Width", "FlangeWidth")]:
            if hasattr(obj, dim_attr):
                dim_str = str(getattr(obj, dim_attr, "0 mm"))
                if "mm" in dim_str:
                    try:
                        dim_value = float(dim_str.split()[0])
                        if dim_value <= 0:
                            errors.append(f"{dim_name} must be positive")
                        elif dim_value < 10:  # mm
                            warnings.append(f"Very small {dim_name.lower()}: {dim_value} mm")
                        elif dim_value > 2000:  # mm
                            warnings.append(f"Very large {dim_name.lower()}: {dim_value} mm")
                    except (ValueError, IndexError):
                        warnings.append(f"Could not parse {dim_name} value: {dim_str}")
        
        # Check section standard consistency
        if hasattr(obj, 'SectionStandard') and hasattr(obj, 'SectionType'):
            standard = obj.SectionStandard
            section_type = obj.SectionType
            
            if standard != "Custom":
                if "W" in standard and "Wide Flange" not in section_type:
                    warnings.append(f"Section standard '{standard}' doesn't match type '{section_type}'")
                elif "IPE" in standard and "I-Beam" not in section_type:
                    warnings.append(f"Section standard '{standard}' doesn't match type '{section_type}'")
                elif "HSS" in standard and "HSS" not in section_type:
                    warnings.append(f"Section standard '{standard}' doesn't match type '{section_type}'")
    
    except Exception as e:
        errors.append(f"Validation error: {str(e)}")
    
    return errors, warnings


class Section:
    def __init__(self, obj, selection):

        # Define pre-selected objects
        objectSelected = (selection[0].Object, selection[0].SubElementNames[0]) if len(selection) > 0 else ()
            
        
        obj.Proxy = self
        obj.addProperty("App::PropertyLinkSub", "ObjectBase", "Base", "Object base").ObjectBase = objectSelected
        
        # Section Standard Selection (similar to MaterialStandards)
        if SECTION_DATABASE_AVAILABLE:
            obj.addProperty("App::PropertyEnumeration", "SectionStandard", "SectionProperty", 
                           "Standard section from database")
            obj.SectionStandard = list(SECTION_STANDARDS.keys()) + ["Custom"]
            
            # Intelligent section detection from object name
            section_name = self._detect_section_from_name(obj.Name if hasattr(obj, 'Name') else "")
            obj.SectionStandard = section_name if section_name else "Custom"
        
        # Enhanced Section properties (fixed typo: SectionProprety → SectionProperty)
        # Check if properties already exist to avoid duplicates
        if not hasattr(obj, "Area"):
            obj.addProperty("App::PropertyArea", "Area", "SectionProperty", "Cross-sectional area").Area = 0.00
        if not hasattr(obj, "MomentInertiaY"):
            obj.addProperty("App::PropertyFloat", "MomentInertiaY", "SectionProperty", "Moment of inertia about local Y axis (Iy)").MomentInertiaY = 0.00
        if not hasattr(obj, "MomentInertiaZ"):
            obj.addProperty("App::PropertyFloat", "MomentInertiaZ", "SectionProperty", "Moment of inertia about local Z axis (Iz)").MomentInertiaZ = 0.00
        if not hasattr(obj, "MomentInertiaPolar"):
            obj.addProperty("App::PropertyFloat", "MomentInertiaPolar", "SectionProperty", "Polar moment of inertia (J)").MomentInertiaPolar = 0.00
        if not hasattr(obj, "ProductInertiaYZ"):
            obj.addProperty("App::PropertyFloat", "ProductInertiaYZ", "SectionProperty", "Product of inertia (Iyz)").ProductInertiaYZ = 0.00
        
        # Additional professional section properties  
        if not hasattr(obj, "SectionModulusY"):
            obj.addProperty("App::PropertyFloat", "SectionModulusY", "SectionProperty", "Section modulus about Y axis (Sy)").SectionModulusY = 0.00
        if not hasattr(obj, "SectionModulusZ"):
            obj.addProperty("App::PropertyFloat", "SectionModulusZ", "SectionProperty", "Section modulus about Z axis (Sz)").SectionModulusZ = 0.00
        if not hasattr(obj, "RadiusGyrationY"):
            obj.addProperty("App::PropertyFloat", "RadiusGyrationY", "SectionProperty", "Radius of gyration about Y axis (ry)").RadiusGyrationY = 0.00
        if not hasattr(obj, "RadiusGyrationZ"):
            obj.addProperty("App::PropertyFloat", "RadiusGyrationZ", "SectionProperty", "Radius of gyration about Z axis (rz)").RadiusGyrationZ = 0.00
        if not hasattr(obj, "WarpingConstant"):
            obj.addProperty("App::PropertyFloat", "WarpingConstant", "SectionProperty", "Warping constant (Cw)").WarpingConstant = 0.00
        
        # Geometric properties
        obj.addProperty("App::PropertyLength", "Depth", "Dimensions", "Section depth (overall height)").Depth = "0 mm"
        obj.addProperty("App::PropertyLength", "FlangeWidth", "Dimensions", "Flange width").FlangeWidth = "0 mm"
        obj.addProperty("App::PropertyLength", "WebThickness", "Dimensions", "Web thickness").WebThickness = "0 mm"
        obj.addProperty("App::PropertyLength", "FlangeThickness", "Dimensions", "Flange thickness").FlangeThickness = "0 mm"
        
        # Classification
        obj.addProperty("App::PropertyString", "SectionType", "Classification", "Section type (W, IPE, HSS, etc.)").SectionType = "Custom"
        obj.addProperty("App::PropertyString", "SectionGrade", "Classification", "Material grade (A992, S355, etc.)").SectionGrade = "A992"
        obj.addProperty("App::PropertyFloat", "Weight", "Properties", "Weight per unit length (kg/m)").Weight = 0.00

        obj.addProperty("App::PropertyBool", "ViewSection", "DrawSection", "Show section on member").ViewSection = False
        obj.addProperty("App::PropertyBool", "ViewFullSection", "DrawSection", "Show full section extrusion").ViewFullSection = False
        


    # Rotate face so that its normal coincides with the passed vector argument
    def rotate(self, face, normal, position=None):
        """Rotate face so that its normal coincides with the passed vector argument.

        This function is safe to import in headless/test environments where FreeCAD
        may not be available: it will return the original face unchanged in that case.
        """
        # If FreeCAD is not present, avoid runtime operations during import
        if not FREECAD_AVAILABLE:
            return face

        if position is None:
            position = FreeCAD.Vector(0, 0, 0)

        normal.normalize()
        try:
            normalface = face.normalAt(0, 0)
        except Exception:
            normalface = face.Faces[0].normalAt(0, 0)

        rotation = FreeCAD.Rotation(normalface, normal)
        rotatedFace = face.transformGeometry(FreeCAD.Placement(position, rotation).toMatrix())
        return rotatedFace


    def execute(self, obj):
        """Execute section object - generate geometry and calculate properties"""
        try:
            # Ensure face is always defined to avoid unbound local errors
            face = None
            # Validate object state
            if not hasattr(obj, 'Proxy') or obj.Proxy != self:
                safe_console_log("Section object proxy mismatch", "error")
                return
            
            # Get structural members for visualization
            objects = FreeCAD.ActiveDocument.Objects if FreeCAD.ActiveDocument else []
            lines = list(filter(lambda object: 'Wire' in object.Name or 'Line' in object.Name, objects))

            # Try to generate section geometry from database first
            generated_face = None
            if SECTION_DATABASE_AVAILABLE and hasattr(obj, 'SectionStandard') and obj.SectionStandard != "Custom":
                try:
                    generated_face = self.generate_section_geometry(obj)
                    if generated_face:
                        safe_console_log(f"Generated geometry for {obj.SectionStandard}")
                except Exception as e:
                    safe_console_log(f"Failed to generate section geometry: {str(e)}", "error")
                    generated_face = None
            
            # Validate if section has an assigned object and if section drawing is active
            if obj.ObjectBase or generated_face:
                # Use generated face from database or custom face from ObjectBase
                if generated_face:
                    face = generated_face
                    # Calculate properties from generated geometry
                    self._calculate_and_update_properties(obj, face)
                else:
                    # Capture face properties and add them to their respective fields
                    try:
                        face = obj.ObjectBase[0].getSubObject(obj.ObjectBase[1][0])
                    except Exception as e:
                        show_warning_message(
                            "กรุณาเลือกผิว (face) ในมุมมอง 3D ก่อนดำเนินการ\n\nPlease select a face in the 3D view before proceeding",
                            "Face Required / ต้องการผิว (Face)",
                            str(e)
                        )
                        obj.Shape = Part.Shape()
                        return

            # If no geometry found at all, show bilingual popup and abort
            if not generated_face and not obj.ObjectBase:
                show_warning_message(
                    "กรุณาเลือกผิว (face) ในมุมมอง 3D ก่อนดำเนินการ\n\nPlease select a face in the 3D view before proceeding",
                    "Face Required / ต้องการผิว (Face)",
                    "No section geometry or ObjectBase defined"
                )
                obj.Shape = Part.Shape()
                return
            
            if face and (getattr(face, 'ShapeType', '') == 'Face' or hasattr(face, 'Area')): # validate if object is a face
                try:
                    # Extract geometric properties safely
                    if not hasattr(face, 'CenterOfMass') or not hasattr(face, 'Area'):
                        raise AttributeError("Face missing required geometric properties")
                    
                    cx, cy, cz = face.CenterOfMass
                    A = face.Area
                    
                    # Validate area
                    if A <= 0:
                        raise ValueError(f"Invalid section area: {A}")
                    
                    # Extract moments of inertia with error checking
                    if not hasattr(face, 'MatrixOfInertia'):
                        raise AttributeError("Face missing MatrixOfInertia")
                    
                    matrix = face.MatrixOfInertia
                    if not hasattr(matrix, 'A') or len(matrix.A) < 6:
                        raise AttributeError("Invalid inertia matrix")
                    
                    Iy = matrix.A[5]
                    Iz = matrix.A[0] 
                    Iyz = matrix.A[1] if abs(matrix.A[1]) > 1 else 0
                    
                except (AttributeError, IndexError, ValueError) as e:
                    show_error_message(
                        f"Error extracting face properties: {str(e)}",
                        "Face Property Error",
                        f"Face type: {getattr(face, 'ShapeType', 'Unknown')}\nObject: {getattr(obj, 'Name', 'Unknown')}"
                    )
                    return
                
                # Apply parallel axis theorem (Steiner's theorem)
                Iy = Iy + A * cx**2
                Iz = Iz + A * cy**2
                Iyz = Iyz + A * cx * cy


                # Only update calculated properties if not using database values
                if not generated_face or obj.SectionStandard == "Custom":
                    obj.Area = A
                    obj.MomentInertiaZ = Iz
                    obj.MomentInertiaY = Iy
                    obj.ProductInertiaYZ = Iyz
                    obj.MomentInertiaPolar = Iy + Iz                   

                # Validate if elements are assigned to section and add section at element center
                listSections = []
                listBar = []
                if len(lines) > 0 and (obj.ViewSection == True or obj.ViewFullSection == True):
                    for line in lines:
                        section = face.copy()
                        if 'SectionMember' in line.PropertiesList: # validate if line has the property
                            if line.SectionMember: # validate if property has value
                                if line.SectionMember.Name == obj.Name:
                                    rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,1), 90 + float(line.RotationSection)) # Rotate 90° cross-section (standard position)
                                    section.Placement = FreeCAD.Placement(FreeCAD.Vector(0,0,0), rot)

                                    dx = line.Shape.Vertexes[1].Point.x - line.Shape.Vertexes[0].Point.x
                                    dy = line.Shape.Vertexes[1].Point.y - line.Shape.Vertexes[0].Point.y
                                    dz = line.Shape.Vertexes[1].Point.z - line.Shape.Vertexes[0].Point.z

                                    if not(abs(dx) < 1e-2 and abs(dy) < 1e-2): # validate if element is not vertical

                                        if obj.ViewSection:
                                            section1 = section.copy()
                                            section1 = self.rotate(section1, FreeCAD.Vector(1,0,0)) # Place section vertical with normal on X axis
                                            section1 = self.rotate(section1, FreeCAD.Vector(dx, dy, 0)) # Place section in direction of element projection on plane
                                            section1 = self.rotate(section1, FreeCAD.Vector(dx, dy, dz), line.Shape.CenterOfGravity) # Place section in element direction and translate to element center                                    
                                            listSections.append(section1.copy())
                                        
                                        # Validate if bar will be fully visualized
                                        if obj.ViewFullSection:
                                            section2 = section.copy()
                                            section2 = self.rotate(section2, FreeCAD.Vector(1,0,0)) # Place section vertical with normal on X axis
                                            section2 = self.rotate(section2, FreeCAD.Vector(dx, dy, 0)) # Place section in direction of element projection on plane
                                            section2 = self.rotate(section2, FreeCAD.Vector(dx, dy, dz), line.Shape.Vertexes[0].Point) # Place section in element direction and translate to initial point                                    

                                            bar = section2.extrude(section2.Faces[0].normalAt(0,0) * (line.Length))
                                            listBar.append(bar)
                                                                    
                                    else:
                                        rot = FreeCAD.Rotation(FreeCAD.Vector(0,0,1), 90 + float(line.RotationSection))
                                        section.Placement = FreeCAD.Placement(line.Shape.CenterOfGravity, rot)
                                        if obj.ViewSection:
                                            listSections.append(section.copy())
                                        
                                        # Validate if bar will be fully visualized  
                                        if obj.ViewFullSection:
                                            bar1 = section.extrude(section.Faces[0].normalAt(0,0) * (line.Length / 2))
                                            bar2 = section.extrude(section.Faces[0].normalAt(0,0) * (-line.Length / 2))
                                            bar = bar1.fuse([bar2])
                                            bar = bar.removeSplitter()
                                            listBar.append(bar)


                    try:
                        shape = Part.makeCompound(listSections + listBar) if (listSections or listBar) else Part.Shape()
                        obj.Shape = shape
                        safe_console_log(f"Created section visualization with {len(listSections)} sections and {len(listBar)} bars\n")
                    except Exception as e:
                        safe_console_log(f"Error creating section compound: {str(e)}\n")
                        obj.Shape = Part.Shape()
                else:
                    obj.Shape = Part.Shape()
            else:
                # No valid face found
                # Provide a bilingual warning when no valid face is available
                if not generated_face and not obj.ObjectBase:
                    show_warning_message(
                        "กรุณาเลือกผิว (face) ในมุมมอง 3D ก่อนดำเนินการ\n\nPlease select a face in the 3D view before proceeding",
                        "Face Required / ต้องการผิว (Face)",
                        "No section geometry or ObjectBase defined"
                    )
                else:
                    safe_console_log("Invalid face geometry for section\n")
                obj.Shape = Part.Shape()
        
        except Exception as e:
            show_error_message(
                f"Section execution failed: {str(e)}",
                "Section Execution Error", 
                f"Object: {getattr(obj, 'Name', 'Unknown')}\nSectionStandard: {getattr(obj, 'SectionStandard', 'Unknown')}"
            )
            # Ensure object has valid shape even on error
            try:
                obj.Shape = Part.Shape()
            except:
                pass
        

    def onChanged(self, obj, Parameter):
        """Handle property changes, especially SectionStandard updates"""
        if Parameter == 'edgeLength':
            self.execute(obj)
        elif Parameter == 'SectionStandard' and SECTION_DATABASE_AVAILABLE:
            self._update_standard_properties(obj)
    
    def _update_standard_properties(self, obj):
        """Update section properties based on selected standard section"""
        try:
            # Validate inputs
            if not hasattr(obj, 'SectionStandard'):
                safe_console_log("Object missing SectionStandard property\n")
                return
                
            if obj.SectionStandard == "Custom":
                safe_console_log("Custom section selected - properties not updated from database\n")
                return  # Don't override custom values
            
            if not SECTION_DATABASE_AVAILABLE:
                show_error_message(
                    "Section database not available", 
                    "Database Error",
                    "SectionStandards.py could not be imported. Check installation."
                )
                return
            
            section_data = get_section_info(obj.SectionStandard)
            if not section_data:
                show_warning_message(
                    f"No data found for section '{obj.SectionStandard}'", 
                    "Section Data Warning"
                )
                return
            
            # Update properties from database
            if "Area" in section_data:
                obj.Area = f"{section_data['Area']} mm^2"
            
            if "Ix" in section_data:
                obj.MomentInertiaZ = section_data["Ix"] / 1e6  # Convert to mm⁴ to m⁴
            
            if "Iy" in section_data:
                obj.MomentInertiaY = section_data["Iy"] / 1e6  # Convert to mm⁴ to m⁴
            
            if "J" in section_data:
                obj.MomentInertiaPolar = section_data["J"] / 1e6
            
            # Calculate polar moment if not provided
            if "J" not in section_data and "Ix" in section_data and "Iy" in section_data:
                obj.MomentInertiaPolar = (section_data["Ix"] + section_data["Iy"]) / 1e6
            
            # Update section moduli
            if "Zx" in section_data:
                obj.SectionModulusZ = section_data["Zx"] / 1e9  # Convert mm³ to m³
            
            if "Zy" in section_data:
                obj.SectionModulusY = section_data["Zy"] / 1e9
            
            # Update radii of gyration
            if "rx" in section_data:
                obj.RadiusGyrationZ = section_data["rx"] / 1000  # Convert mm to m
            
            if "ry" in section_data:
                obj.RadiusGyrationY = section_data["ry"] / 1000
            
            # Update warping constant
            if "Cw" in section_data:
                obj.WarpingConstant = section_data["Cw"] / 1e18  # Convert mm⁶ to m⁶
            
            # Update dimensional properties
            if "Depth" in section_data:
                obj.Depth = f"{section_data['Depth']} mm"
            
            if "FlangeWidth" in section_data:
                obj.FlangeWidth = f"{section_data['FlangeWidth']} mm"
            
            if "WebThickness" in section_data:
                obj.WebThickness = f"{section_data['WebThickness']} mm"
            
            if "FlangeThickness" in section_data:
                obj.FlangeThickness = f"{section_data['FlangeThickness']} mm"
            
            # Update classification
            if "Type" in section_data:
                obj.SectionType = section_data["Type"]
            
            if "Grade" in section_data:
                obj.SectionGrade = section_data["Grade"]
            
            if "Weight" in section_data:
                obj.Weight = section_data["Weight"]
            
            # Update label with section name
            if obj.SectionStandard != "Custom":
                obj.Label = f"Section_{obj.SectionStandard}"
            
            # Validate updated properties
            try:
                errors, warnings = validate_section_properties(obj)
            except AttributeError as e:
                # Likely the object is missing a required runtime property like Area
                show_error_message(
                    f"Property validation failed due to missing object property: {str(e)}",
                    "Section Validation Error",
                    f"Section: {getattr(obj, 'SectionStandard', 'Unknown')}\nObject: {getattr(obj, 'Name', 'Unknown')}"
                )
                return
            
            if errors:
                error_msg = f"Property validation failed for {obj.SectionStandard}:\n" + "\n".join(errors)
                show_error_message(error_msg, "Section Validation Error")
            
            if warnings:
                warning_msg = "\n".join(warnings)
                safe_console_log(f"Section warnings for {obj.SectionStandard}:\n{warning_msg}\n")
            
            safe_console_log(f"Successfully updated section properties for {obj.SectionStandard}\n")
            
        except KeyError as e:
            show_error_message(
                f"Missing property in section database: {str(e)}", 
                "Database Error",
                f"Section: {obj.SectionStandard}\nMissing key: {str(e)}"
            )
        except ValueError as e:
            show_error_message(
                f"Invalid property value: {str(e)}", 
                "Value Error",
                f"Check section database for {obj.SectionStandard}"
            )
        except Exception as e:
            show_error_message(
                f"Unexpected error updating section properties: {str(e)}", 
                "Section Update Error",
                f"Section: {getattr(obj, 'SectionStandard', 'Unknown')}\nObject: {getattr(obj, 'Name', 'Unknown')}"
            )
    
    def _detect_section_from_name(self, name: str) -> str:
        """Detect section standard from object name or label using core architecture"""
        try:
            if CORE_ARCHITECTURE_AVAILABLE:
                # Use centralized section manager
                section_manager = get_section_manager()
                return section_manager.detect_section_from_name(name)
            else:
                # Fallback to legacy detection
                return self._legacy_detect_section_from_name(name)
        except Exception as e:
            safe_console_log(f"Error detecting section from name: {str(e)}\n")
            return "Custom"
    
    def _legacy_detect_section_from_name(self, name: str) -> str:
        """Legacy section detection method"""
        name_upper = name.upper()
        
        # Check for specific section patterns
        section_patterns = {
            'W': ['W12X26', 'W14X22', 'W16X31', 'W18X35'],
            'IPE': ['IPE100', 'IPE120', 'IPE160', 'IPE200', 'IPE240', 'IPE300'],
            'HEB': ['HEB100', 'HEB120', 'HEB160', 'HEB200'],
            'HSS': ['HSS6X4X1/4', 'HSS8X6X1/4', 'HSS4.000X0.250', 'HSS6.625X0.280']
        }
        
        # Look for exact matches first
        for section_name in SECTION_STANDARDS.keys():
            if section_name.upper() in name_upper or name_upper in section_name.upper():
                return section_name
        
        # Look for pattern matches
        for pattern_prefix, sections in section_patterns.items():
            if pattern_prefix in name_upper:
                # Find closest match
                for section in sections:
                    if section in SECTION_STANDARDS:
                        return section
        
        return "Custom"
    
    def generate_section_geometry(self, obj):
        """Generate section geometry using modern architecture"""
        try:
            # Input validation
            if not hasattr(obj, 'SectionStandard'):
                safe_console_log("Object missing SectionStandard property for geometry generation\n")
                return None
                
            if obj.SectionStandard == "Custom":
                safe_console_log("Custom section - no automatic geometry generation\n")
                return None
            
            # Use modern architecture if available
            if CORE_ARCHITECTURE_AVAILABLE:
                return self._generate_geometry_with_core_architecture(obj)
            elif SECTION_DATABASE_AVAILABLE:
                return self._generate_geometry_legacy(obj)
            else:
                safe_console_log("Section database not available - cannot generate geometry\n")
                return None
                
        except Exception as e:
            safe_console_log(f"Error in geometry generation: {str(e)}\n")
            return None
    
    def _generate_geometry_with_core_architecture(self, obj):
        """Generate geometry using new core architecture"""
        try:
            # Get section manager and geometry factory
            section_manager = get_section_manager()
            geometry_factory = get_geometry_factory()
            
            # Get section properties from manager
            section_properties = section_manager.get_section_properties(obj.SectionStandard)
            if not section_properties:
                safe_console_log(f"No properties found for {obj.SectionStandard}\n")
                return None
            
            # Generate geometry using factory
            geometry = geometry_factory.generate_geometry(section_properties)
            
            if geometry:
                safe_console_log(f"Generated geometry using core architecture for {obj.SectionStandard}\n")
            else:
                safe_console_log(f"Failed to generate geometry for {obj.SectionStandard}\n")
            
            return geometry
            
        except Exception as e:
            safe_console_log(f"Error in core architecture geometry generation: {str(e)}\n")
            # Fallback to legacy method
            return self._generate_geometry_legacy(obj)
    
    def _generate_geometry_legacy(self, obj):
        """Legacy geometry generation method"""
        try:
            section_data = get_section_info(obj.SectionStandard)
            if not section_data:
                safe_console_log(f"No geometry data available for {obj.SectionStandard}\n")
                return None
            
            # Validate required properties
            section_type = section_data.get("Type", "")
            if not section_type:
                safe_console_log(f"Section type not defined for {obj.SectionStandard}\n")
                return None
            
            # Use legacy generators
            if "Wide Flange" in section_type or "I-Beam" in section_type or "H-Beam" in section_type:
                return self._create_i_section_geometry(section_data)
            elif "HSS" in section_type and "Rectangular" in section_type:
                return self._create_rectangular_hss_geometry(section_data)
            elif "HSS" in section_type and "Circular" in section_type:
                return self._create_circular_hss_geometry(section_data)
            elif "Angle" in section_type:
                return self._create_angle_geometry(section_data)
            elif "Channel" in section_type:
                return self._create_channel_geometry(section_data)
            
            safe_console_log(f"Unsupported section type for geometry generation: {section_type}\n")
            return None
            
        except Exception as e:
            safe_console_log(f"Error in legacy geometry generation: {str(e)}\n")
            return None
    
    def _create_i_section_geometry(self, section_data):
        """Create I-shaped section geometry (W, IPE, HEB)"""
        try:
            # Validate and extract dimensions with proper error checking
            required_props = ["Depth", "FlangeWidth", "WebThickness", "FlangeThickness"]
            for prop in required_props:
                if prop not in section_data:
                    raise KeyError(f"Required property '{prop}' missing for I-section geometry")
            
            d = float(section_data["Depth"])  # mm
            bf = float(section_data["FlangeWidth"])
            tw = float(section_data["WebThickness"])
            tf = float(section_data["FlangeThickness"])
            
            # Engineering validation
            if d <= 0 or bf <= 0 or tw <= 0 or tf <= 0:
                raise ValueError("All section dimensions must be positive")
            
            if tw >= bf:
                raise ValueError(f"Web thickness ({tw}) cannot exceed flange width ({bf})")
            
            if 2*tf >= d:
                raise ValueError(f"Total flange thickness ({2*tf}) cannot exceed depth ({d})")
            
            # Check reasonable proportions
            if d/bf > 10 or d/bf < 0.5:
                safe_console_log(f"Unusual depth/flange width ratio: {d/bf:.2f}\n")
            
            if bf/tw > 50:
                safe_console_log(f"Very slender web: bf/tw = {bf/tw:.1f}\n")
            
            # Create I-section profile points
            points = [
                FreeCAD.Vector(-bf/2, -d/2, 0),    # Bottom left of bottom flange
                FreeCAD.Vector(bf/2, -d/2, 0),     # Bottom right of bottom flange
                FreeCAD.Vector(bf/2, -d/2+tf, 0),  # Top right of bottom flange
                FreeCAD.Vector(tw/2, -d/2+tf, 0),  # Bottom right of web
                FreeCAD.Vector(tw/2, d/2-tf, 0),   # Top right of web
                FreeCAD.Vector(bf/2, d/2-tf, 0),   # Bottom right of top flange
                FreeCAD.Vector(bf/2, d/2, 0),      # Top right of top flange
                FreeCAD.Vector(-bf/2, d/2, 0),     # Top left of top flange
                FreeCAD.Vector(-bf/2, d/2-tf, 0),  # Bottom left of top flange
                FreeCAD.Vector(-tw/2, d/2-tf, 0),  # Top left of web
                FreeCAD.Vector(-tw/2, -d/2+tf, 0), # Bottom left of web
                FreeCAD.Vector(-bf/2, -d/2+tf, 0), # Top left of bottom flange
                FreeCAD.Vector(-bf/2, -d/2, 0)     # Close polygon
            ]
            
            # Create wire and face
            wire = Part.makePolygon(points)
            face = Part.Face(wire)
            
            return face
            
        except KeyError as e:
            safe_console_log(f"Missing I-section property: {str(e)}\n")
            return None
        except ValueError as e:
            safe_console_log(f"Invalid I-section dimension: {str(e)}\n")
            return None
        except Exception as e:
            safe_console_log(f"Error creating I-section geometry: {str(e)}\n")
            return None
    
    def _create_rectangular_hss_geometry(self, section_data):
        """Create rectangular HSS geometry"""
        try:
            # Validate required properties
            required_props = ["Depth", "Width", "WallThickness"]
            for prop in required_props:
                if prop not in section_data:
                    raise KeyError(f"Required property '{prop}' missing for rectangular HSS geometry")
            
            h = float(section_data["Depth"])  # Height
            b = float(section_data["Width"])   # Width  
            t = float(section_data["WallThickness"])  # Wall thickness
            
            # Engineering validation
            if h <= 0 or b <= 0 or t <= 0:
                raise ValueError("All HSS dimensions must be positive")
            
            if 2*t >= h or 2*t >= b:
                raise ValueError(f"Wall thickness ({t}) too large for section size ({h}x{b})")
            
            # Check slenderness
            if h/t > 50 or b/t > 50:
                safe_console_log(f"Very slender HSS walls: h/t={h/t:.1f}, b/t={b/t:.1f}\n")
            
            # Create outer rectangle
            outer_points = [
                FreeCAD.Vector(-b/2, -h/2, 0),
                FreeCAD.Vector(b/2, -h/2, 0),
                FreeCAD.Vector(b/2, h/2, 0),
                FreeCAD.Vector(-b/2, h/2, 0),
                FreeCAD.Vector(-b/2, -h/2, 0)
            ]
            
            # Create inner rectangle
            inner_points = [
                FreeCAD.Vector(-(b/2-t), -(h/2-t), 0),
                FreeCAD.Vector((b/2-t), -(h/2-t), 0),
                FreeCAD.Vector((b/2-t), (h/2-t), 0),
                FreeCAD.Vector(-(b/2-t), (h/2-t), 0),
                FreeCAD.Vector(-(b/2-t), -(h/2-t), 0)
            ]
            
            outer_wire = Part.makePolygon(outer_points)
            inner_wire = Part.makePolygon(inner_points)
            
            outer_face = Part.Face(outer_wire)
            inner_face = Part.Face(inner_wire)
            
            # Subtract inner from outer
            section_face = outer_face.cut(inner_face)
            
            return section_face
            
        except KeyError as e:
            safe_console_log(f"Missing rectangular HSS property: {str(e)}\n")
            return None
        except ValueError as e:
            safe_console_log(f"Invalid rectangular HSS dimension: {str(e)}\n")
            return None
        except Exception as e:
            safe_console_log(f"Error creating rectangular HSS geometry: {str(e)}\n")
            return None
    
    def _create_circular_hss_geometry(self, section_data):
        """Create circular HSS geometry"""
        try:
            # Validate required properties
            required_props = ["Diameter", "WallThickness"]
            for prop in required_props:
                if prop not in section_data:
                    raise KeyError(f"Required property '{prop}' missing for circular HSS geometry")
            
            d = float(section_data["Diameter"])
            t = float(section_data["WallThickness"])
            
            # Engineering validation
            if d <= 0 or t <= 0:
                raise ValueError("Diameter and wall thickness must be positive")
            
            if t >= d/2:
                raise ValueError(f"Wall thickness ({t}) cannot exceed radius ({d/2})")
            
            # Check slenderness
            if d/t > 100:
                safe_console_log(f"Very slender circular HSS: D/t = {d/t:.1f}\n")
            
            # Create outer and inner circles
            outer_circle = Part.makeCircle(d/2, FreeCAD.Vector(0,0,0))
            inner_circle = Part.makeCircle(d/2-t, FreeCAD.Vector(0,0,0))
            
            outer_face = Part.Face(outer_circle)
            inner_face = Part.Face(inner_circle)
            
            # Subtract inner from outer
            section_face = outer_face.cut(inner_face)
            
            return section_face
            
        except KeyError as e:
            safe_console_log(f"Missing circular HSS property: {str(e)}\n")
            return None
        except ValueError as e:
            safe_console_log(f"Invalid circular HSS dimension: {str(e)}\n")
            return None
        except Exception as e:
            safe_console_log(f"Error creating circular HSS geometry: {str(e)}\n")
            return None
    
    def _calculate_and_update_properties(self, obj, face):
        """Calculate properties from face geometry using modern architecture"""
        try:
            if not face or not hasattr(face, 'Area'):
                return
            
            # Use core architecture if available
            if CORE_ARCHITECTURE_AVAILABLE:
                self._calculate_properties_with_core_architecture(obj, face)
            else:
                self._calculate_properties_legacy(obj, face)
                
        except Exception as e:
            safe_console_log(f"Error calculating section properties: {str(e)}\n")
    
    def _calculate_properties_with_core_architecture(self, obj, face):
        """Calculate properties using core architecture"""
        try:
            # Use centralized property calculator
            properties = calculate_properties_from_face(face)
            
            if not properties:
                safe_console_log("No properties calculated from face\n")
                return
            
            # Update object properties if custom section
            if not hasattr(obj, 'SectionStandard') or obj.SectionStandard == "Custom":
                # Area
                if "Area" in properties:
                    obj.Area = properties["Area"]
                
                # Moments of inertia
                if "Iy" in properties:
                    obj.MomentInertiaY = properties["Iy"]
                if "Iz" in properties:
                    obj.MomentInertiaZ = properties["Iz"]
                if "Iyz" in properties:
                    obj.ProductInertiaYZ = properties["Iyz"]
                if "J" in properties:
                    obj.MomentInertiaPolar = properties["J"]
                
                # Section moduli
                if "Sx" in properties:
                    obj.SectionModulusZ = properties["Sx"] / 1e9  # Convert to m³
                if "Sy" in properties:
                    obj.SectionModulusY = properties["Sy"] / 1e9
                
                # Radii of gyration
                if "ry" in properties:
                    obj.RadiusGyrationY = properties["ry"] / 1000  # Convert to m
                if "rz" in properties:
                    obj.RadiusGyrationZ = properties["rz"] / 1000
                
                # Dimensions
                if "Depth" in properties:
                    obj.Depth = f"{properties['Depth']} mm"
                if "Width" in properties:
                    obj.FlangeWidth = f"{properties['Width']} mm"
            
            safe_console_log("Successfully calculated properties using core architecture\n")
            
        except Exception as e:
            safe_console_log(f"Error in core architecture property calculation: {str(e)}\n")
            # Fallback to legacy method
            self._calculate_properties_legacy(obj, face)
    
    def _calculate_properties_legacy(self, obj, face):
        """Legacy property calculation method"""
        try:
            cx, cy, cz = face.CenterOfMass
            A = face.Area
            Iy = face.MatrixOfInertia.A[5]
            Iz = face.MatrixOfInertia.A[0]
            Iyz = face.MatrixOfInertia.A[1] if abs(face.MatrixOfInertia.A[1]) > 1 else 0
            
            # Apply parallel axis theorem (Steiner's theorem)
            Iy = Iy + A * cx**2
            Iz = Iz + A * cy**2
            Iyz = Iyz + A * cx * cy
            
            # Update only if not using database (i.e., custom section)
            if not hasattr(obj, 'SectionStandard') or obj.SectionStandard == "Custom":
                obj.Area = A
                obj.MomentInertiaZ = Iz
                obj.MomentInertiaY = Iy
                obj.ProductInertiaYZ = Iyz
                obj.MomentInertiaPolar = Iy + Iz
                
                # Calculate section moduli and radii of gyration for custom sections
                if hasattr(face, 'BoundBox'):
                    bbox = face.BoundBox
                    depth = bbox.YMax - bbox.YMin
                    width = bbox.XMax - bbox.XMin
                    
                    # Estimate section moduli (rough approximation)
                    if Iy > 0 and depth > 0:
                        obj.SectionModulusY = (2 * Iy / depth) / 1e9  # Convert to m³
                    if Iz > 0 and width > 0:
                        obj.SectionModulusZ = (2 * Iz / width) / 1e9  # Convert to m³
                    
                    # Calculate radii of gyration
                    if A > 0:
                        obj.RadiusGyrationY = math.sqrt(Iy / A) / 1000  # Convert to m
                        obj.RadiusGyrationZ = math.sqrt(Iz / A) / 1000  # Convert to m
                    
                    # Update dimensions for custom sections
                    obj.Depth = f"{depth} mm"
                    obj.FlangeWidth = f"{width} mm"
        
        except Exception as e:
            safe_console_log(f"Error in legacy property calculation: {str(e)}\n")
    
    def _create_angle_geometry(self, section_data):
        """Create angle section geometry (L-shapes)"""
        try:
            leg_width = section_data.get("LegWidth", 100.0)
            leg_height = section_data.get("LegHeight", 100.0)
            thickness = section_data.get("Thickness", 10.0)
            
            # Create L-shape points
            points = [
                FreeCAD.Vector(0, 0, 0),
                FreeCAD.Vector(leg_width, 0, 0),
                FreeCAD.Vector(leg_width, thickness, 0),
                FreeCAD.Vector(thickness, thickness, 0),
                FreeCAD.Vector(thickness, leg_height, 0),
                FreeCAD.Vector(0, leg_height, 0),
                FreeCAD.Vector(0, 0, 0)
            ]
            
            wire = Part.makePolygon(points)
            face = Part.Face(wire)
            
            return face
            
        except Exception as e:
            safe_console_log(f"Error creating angle geometry: {str(e)}\n")
            return None
    
    def _create_channel_geometry(self, section_data):
        """Create channel section geometry (C-shapes)"""
        try:
            depth = section_data.get("Depth", 200.0)
            flange_width = section_data.get("FlangeWidth", 60.0)
            web_thickness = section_data.get("WebThickness", 8.0)
            flange_thickness = section_data.get("FlangeThickness", 12.0)
            
            # Create C-shape points
            points = [
                FreeCAD.Vector(0, -depth/2, 0),
                FreeCAD.Vector(flange_width, -depth/2, 0),
                FreeCAD.Vector(flange_width, -depth/2 + flange_thickness, 0),
                FreeCAD.Vector(web_thickness, -depth/2 + flange_thickness, 0),
                FreeCAD.Vector(web_thickness, depth/2 - flange_thickness, 0),
                FreeCAD.Vector(flange_width, depth/2 - flange_thickness, 0),
                FreeCAD.Vector(flange_width, depth/2, 0),
                FreeCAD.Vector(0, depth/2, 0),
                FreeCAD.Vector(0, -depth/2, 0)
            ]
            
            wire = Part.makePolygon(points)
            face = Part.Face(wire)
            
            return face
            
        except Exception as e:
            safe_console_log(f"Error creating channel geometry: {str(e)}\n")
            return None


class ViewProviderSection:
    def __init__(self, obj):
        obj.Proxy = self
    
    # def setupContextMenu(self, obj, menu):
    #     # Adiciona uma opção ao menu de contexto do objeto
    #     action = QtWidgets.QAction("Edit Section", menu)
    #     action.triggered.connect(lambda: self.editSection(obj))
    #     menu.addAction(action)
    
    # def editSection(self, obj):
    #     # Função executada ao clicar no menu de contexto
    #     FreeCAD.Console.PrintMessage(f"Objeto {obj.Object.Name} foi clicado!\n")
    #     janela = EditSectionGui(obj)
    #     FreeCADGui.Control.showDialog(janela)

    def getIcon(self):
        return """/* XPM */
static char * profile_xpm[] = {
"32 32 213 2",
"  	c None",
". 	c #060B17",
"+ 	c #09101D",
"@ 	c #0B1222",
"# 	c #0C1222",
"$ 	c #0C1422",
"% 	c #0D1422",
"& 	c #0D1522",
"* 	c #0E1522",
"= 	c #0F1522",
"- 	c #0F1622",
"; 	c #101622",
"> 	c #101722",
", 	c #111722",
"' 	c #121722",
") 	c #121822",
"! 	c #141822",
"~ 	c #141922",
"{ 	c #151922",
"] 	c #161A22",
"^ 	c #171A22",
"/ 	c #171B22",
"( 	c #14171D",
"_ 	c #101316",
": 	c #08101E",
"< 	c #4075E1",
"[ 	c #4C88FF",
"} 	c #518CFF",
"| 	c #568FFF",
"1 	c #5B92FF",
"2 	c #6095FF",
"3 	c #6599FF",
"4 	c #6A9CFF",
"5 	c #6F9FFF",
"6 	c #73A2FF",
"7 	c #78A6FF",
"8 	c #7DA9FF",
"9 	c #82ACFF",
"0 	c #87AFFF",
"a 	c #8CB3FF",
"b 	c #91B6FF",
"c 	c #95B9FF",
"d 	c #9ABDFF",
"e 	c #9FC0FF",
"f 	c #A4C3FF",
"g 	c #A9C6FF",
"h 	c #97B0DE",
"i 	c #15181E",
"j 	c #070E1E",
"k 	c #3972E1",
"l 	c #4684FF",
"m 	c #4B87FF",
"n 	c #4F8AFF",
"o 	c #548EFF",
"p 	c #5991FF",
"q 	c #5E94FF",
"r 	c #6397FF",
"s 	c #689BFF",
"t 	c #6D9EFF",
"u 	c #72A1FF",
"v 	c #76A4FF",
"w 	c #7BA8FF",
"x 	c #80ABFF",
"y 	c #85AEFF",
"z 	c #8AB1FF",
"A 	c #8FB5FF",
"B 	c #94B8FF",
"C 	c #98BBFF",
"D 	c #9DBFFF",
"E 	c #A2C2FF",
"F 	c #91ACDE",
"G 	c #336DE1",
"H 	c #3F7FFF",
"I 	c #4483FF",
"J 	c #4986FF",
"K 	c #4E89FF",
"L 	c #528CFF",
"M 	c #5790FF",
"N 	c #5C93FF",
"O 	c #6196FF",
"P 	c #6699FF",
"Q 	c #6B9DFF",
"R 	c #70A0FF",
"S 	c #75A3FF",
"T 	c #79A6FF",
"U 	c #7EAAFF",
"V 	c #83ADFF",
"W 	c #88B0FF",
"X 	c #8DB3FF",
"Y 	c #92B7FF",
"Z 	c #97BAFF",
"` 	c #9BBDFF",
" .	c #8BA8DE",
"..	c #14181E",
"+.	c #050E1E",
"@.	c #2D6AE1",
"#.	c #387BFF",
"$.	c #3D7EFF",
"%.	c #4281FF",
"&.	c #4785FF",
"*.	c #518BFF",
"=.	c #558EFF",
"-.	c #5A92FF",
";.	c #5F95FF",
">.	c #6498FF",
",.	c #699BFF",
"'.	c #6E9FFF",
").	c #78A5FF",
"!.	c #7CA8FF",
"~.	c #81ACFF",
"{.	c #86AFFF",
"].	c #8BB2FF",
"^.	c #90B5FF",
"/.	c #86A4DE",
"(.	c #12161E",
"_.	c #050D1E",
":.	c #2865E1",
"<.	c #3276FF",
"[.	c #367AFF",
"}.	c #3B7DFF",
"|.	c #4080FF",
"1.	c #4583FF",
"2.	c #4A87FF",
"3.	c #548DFF",
"4.	c #5890FF",
"5.	c #5D94FF",
"6.	c #6297FF",
"7.	c #679AFF",
"8.	c #6C9DFF",
"9.	c #71A1FF",
"0.	c #7BA7FF",
"a.	c #7FAAFF",
"b.	c #84AEFF",
"c.	c #89B1FF",
"d.	c #8EB4FF",
"e.	c #80A0DE",
"f.	c #030A19",
"g.	c #030B1A",
"h.	c #040C1B",
"i.	c #060C1B",
"j.	c #060D1B",
"k.	c #070D1B",
"l.	c #050A13",
"m.	c #355FB1",
"n.	c #578FFF",
"o.	c #6096FF",
"p.	c #4568AE",
"q.	c #080C13",
"r.	c #0C111B",
"s.	c #0C121B",
"t.	c #0D121B",
"u.	c #0F131B",
"v.	c #0E121A",
"w.	c #0D1219",
"x.	c #2C53A0",
"y.	c #508BFF",
"z.	c #5A91FF",
"A.	c #3A5B9D",
"B.	c #2850A0",
"C.	c #538DFF",
"D.	c #36599D",
"E.	c #244DA0",
"F.	c #4282FF",
"G.	c #32569D",
"H.	c #1F4BA0",
"I.	c #377AFF",
"J.	c #3C7DFF",
"K.	c #4584FF",
"L.	c #2E539D",
"M.	c #1B48A0",
"N.	c #3075FF",
"O.	c #3579FF",
"P.	c #3A7CFF",
"Q.	c #29509D",
"R.	c #1745A0",
"S.	c #2971FF",
"T.	c #2E74FF",
"U.	c #3377FF",
"V.	c #264E9D",
"W.	c #1342A0",
"X.	c #236CFF",
"Y.	c #2770FF",
"Z.	c #2C73FF",
"`.	c #3176FF",
" +	c #214A9D",
".+	c #1040A0",
"++	c #1C68FF",
"@+	c #216BFF",
"#+	c #266EFF",
"$+	c #2A72FF",
"%+	c #1D489D",
"&+	c #1966FF",
"*+	c #1A67FF",
"=+	c #1F6AFF",
"-+	c #246DFF",
";+	c #19459D",
">+	c #1D69FF",
",+	c #15429D",
"'+	c #113F9D",
")+	c #0F3F9D",
"!+	c #020A19",
"~+	c #020A1A",
"{+	c #020B1B",
"]+	c #020813",
"^+	c #1147B1",
"/+	c #1146AE",
"(+	c #030C1E",
"_+	c #165AE1",
":+	c #1659DE",
"<+	c #010915",
"[+	c #030C1D",
"}+	c #030D22",
"|+	c #010916",
"        . + @ # $ % & * = - ; > , ' ) ! ~ { { ] ^ / ( _         ",
"        : < [ } | 1 2 3 4 5 6 7 8 9 0 a b c d e f g h i         ",
"        j k l m n o p q r s t u v w x y z A B C D E F i         ",
"        j G H I J K L M N O P Q R S T U V W X Y Z `  ...        ",
"        +.@.#.$.%.&.[ *.=.-.;.>.,.'.6 ).!.~.{.].^.c /.(.        ",
"        _.:.<.[.}.|.1.2.n 3.4.5.6.7.8.9.v 0.a.b.c.d.e.(.        ",
"        f.g.h.i.i.j.k.k.l.m.L n.1 o.p.q.r.r.s.t.t.u.v.w.        ",
"                          x.m y.=.z.A.                          ",
"                          B.I J K C.D.                          ",
"                          E.$.F.&.[ G.                          ",
"                          H.I.J.|.K.L.                          ",
"                          M.N.O.P.H Q.                          ",
"                          R.S.T.U.#.V.                          ",
"                          W.X.Y.Z.`. +                          ",
"                          .+++@+#+$+%+                          ",
"                          .+&+*+=+-+;+                          ",
"                          .+&+&+&+>+,+                          ",
"                          .+&+&+&+&+'+                          ",
"                          .+&+&+&+&+)+                          ",
"                          .+&+&+&+&+)+                          ",
"                          .+&+&+&+&+)+                          ",
"                          .+&+&+&+&+)+                          ",
"                          .+&+&+&+&+)+                          ",
"                          .+&+&+&+&+)+                          ",
"                          .+&+&+&+&+)+                          ",
"        !+~+{+{+{+{+{+{+]+^+&+&+&+&+/+]+{+{+{+{+{+{+~+!+        ",
"        (+_+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+:+(+        ",
"        (+_+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+:+(+        ",
"        (+_+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+:+(+        ",
"        (+_+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+:+(+        ",
"        (+_+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+&+:+(+        ",
"        <+[+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+}+[+|+        "};
        """


# class EditSectionGui():
#     def __init__(self, obj):
#         self.obj = obj
#         self.form = FreeCADGui.PySideUic.loadUi(path_ui)

#         #Define a função do botão ok        
#         self.form.btn_ok.clicked.connect(self.accept)

#         self.form.comboBox.textActivated.connect(self.changeImage)

#         # self.form.image.pixmap = str(os.path.dirname(__file__))+'/resources/ui/img/sectionRetangle.svg'
#         pixmap = QPixmap(str(os.path.dirname(__file__))+'/resources/ui/img/sectionI.svg')
#         self.form.image.setPixmap(pixmap)
    
#     def changeImage(self, selection):
#         match selection:
#             case 'Rectangle Section':
#                 pixmap = QPixmap(str(os.path.dirname(__file__))+'/resources/ui/img/sectionRetangle.svg')

#             case 'Circular Section':
#                 pixmap = QPixmap(str(os.path.dirname(__file__))+'/resources/ui/img/sectionI.svg')
            
#             case 'W Section':
#                 pixmap = QPixmap(str(os.path.dirname(__file__))+'/resources/ui/img/sectionI.svg')

#         self.form.image.setPixmap(pixmap)
    
#     def accept(self):
#         print('botao ok clicado')



class CommandProfile():
    """My new command"""

    def GetResources(self):
        return {"Pixmap"  : os.path.join(ICONPATH, "icons/section.svg"), # the name of a svg file available in the resources
                "Accel"   : "S+C", # a default shortcut (optional)
                "MenuText": "Section",
                "ToolTip" : "Adds section to structure member"}

    def Activated(self):
        selections = list(FreeCADGui.Selection.getSelectionEx())
        
        doc = FreeCAD.ActiveDocument
        obj = doc.addObject("Part::FeaturePython", "Section")

        Section(obj, selections)
        ViewProviderSection(obj.ViewObject)
        FreeCAD.ActiveDocument.recompute()        
        return

    def IsActive(self):
        
        return True

FreeCADGui.addCommand("section", CommandProfile())
