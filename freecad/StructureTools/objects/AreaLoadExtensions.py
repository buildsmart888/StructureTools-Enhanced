# -*- coding: utf-8 -*-
"""
AreaLoad Extensions - Additional methods for enhanced AreaLoad functionality

This module contains the remaining methods that were too large for the main AreaLoad file.
"""

import FreeCAD as App
import Part
import math

class AreaLoadExtensions:
    """Extension methods for AreaLoad class"""
    
    def _createTwoWayVisualization(self, obj):
        """Create visualization for two-way load distribution."""
        try:
            # Show grid pattern indicating two-way distribution
            vis_objects = []
            
            # Create grid lines on loaded faces
            for face_obj in obj.TargetFaces:
                if hasattr(face_obj, 'Shape'):
                    grid_lines = self._createDistributionGrid(face_obj.Shape, "TwoWay")
                    vis_objects.extend(grid_lines)
            
            return vis_objects
            
        except Exception as e:
            App.Console.PrintError(f"Error creating two-way visualization: {e}\n")
            return []
    
    def _createOpenStructureVisualization(self, obj):
        """Create visualization for open structure distribution."""
        try:
            # Show load paths to individual members
            vis_objects = []
            
            if obj.TributaryAreas:
                doc = App.ActiveDocument
                if doc:
                    # Create lines connecting load center to members
                    load_center = obj.LoadCenter
                    
                    for member_name, data in obj.TributaryAreas.items():
                        member_obj = data.get('member_obj')
                        if member_obj and hasattr(member_obj, 'Shape'):
                            member_center = member_obj.Shape.CenterOfMass
                            
                            # Create connection line
                            connection_line = Part.makeLine(load_center, member_center)
                            
                            line_name = f"LoadPath_{member_name}"
                            line_obj = doc.addObject("Part::Feature", line_name)
                            line_obj.Shape = connection_line
                            
                            # Style the line
                            if hasattr(line_obj, 'ViewObject'):
                                line_obj.ViewObject.LineColor = (0.0, 0.8, 0.0)  # Green
                                line_obj.ViewObject.LineWidth = 2.0
                                line_obj.ViewObject.LineStyle = "Dashed"
                            
                            vis_objects.append(line_obj)
            
            return vis_objects
            
        except Exception as e:
            App.Console.PrintError(f"Error creating open structure visualization: {e}\n")
            return []
    
    def _createDirectionArrow(self, doc, position, direction, label):
        """Create a direction arrow for distribution visualization."""
        try:
            # Normalize direction
            length = math.sqrt(direction.x**2 + direction.y**2 + direction.z**2)
            if length > 0:
                direction = App.Vector(direction.x/length, direction.y/length, direction.z/length)
            
            # Create arrow
            arrow_length = 500  # 500mm
            arrow = self._createArrow(doc, position, direction, 1.0, arrow_length)
            
            if arrow and hasattr(arrow, 'ViewObject'):
                arrow.ViewObject.ShapeColor = (0.0, 0.0, 1.0)  # Blue for direction
                arrow.Label = f"Direction_{label}"
            
            return arrow
            
        except Exception as e:
            App.Console.PrintWarning(f"Error creating direction arrow: {e}\n")
            return None
    
    def _createDistributionGrid(self, shape, distribution_type):
        """Create grid lines showing distribution pattern."""
        try:
            grid_lines = []
            
            if not hasattr(shape, 'Faces') or not shape.Faces:
                return grid_lines
            
            face = shape.Faces[0]
            bbox = face.BoundBox
            
            doc = App.ActiveDocument
            if not doc:
                return grid_lines
            
            # Create grid lines
            grid_spacing = 200  # 200mm
            
            # Vertical lines
            x_start = bbox.XMin
            x_end = bbox.XMax
            y_start = bbox.YMin
            y_end = bbox.YMax
            z_level = bbox.ZMin
            
            x_count = int((x_end - x_start) / grid_spacing) + 1
            y_count = int((y_end - y_start) / grid_spacing) + 1
            
            # Create X-direction lines
            for i in range(x_count):
                x = x_start + i * grid_spacing
                if x <= x_end:
                    line = Part.makeLine(
                        App.Vector(x, y_start, z_level),
                        App.Vector(x, y_end, z_level)
                    )
                    
                    line_name = f"GridX_{i}_{distribution_type}"
                    line_obj = doc.addObject("Part::Feature", line_name)
                    line_obj.Shape = line
                    
                    if hasattr(line_obj, 'ViewObject'):
                        line_obj.ViewObject.LineColor = (0.7, 0.7, 0.7)  # Light gray
                        line_obj.ViewObject.LineWidth = 1.0
                    
                    grid_lines.append(line_obj)
            
            # Create Y-direction lines
            for j in range(y_count):
                y = y_start + j * grid_spacing
                if y <= y_end:
                    line = Part.makeLine(
                        App.Vector(x_start, y, z_level),
                        App.Vector(x_end, y, z_level)
                    )
                    
                    line_name = f"GridY_{j}_{distribution_type}"
                    line_obj = doc.addObject("Part::Feature", line_name)
                    line_obj.Shape = line
                    
                    if hasattr(line_obj, 'ViewObject'):
                        line_obj.ViewObject.LineColor = (0.7, 0.7, 0.7)  # Light gray
                        line_obj.ViewObject.LineWidth = 1.0
                    
                    grid_lines.append(line_obj)
            
            return grid_lines
            
        except Exception as e:
            App.Console.PrintWarning(f"Error creating distribution grid: {e}\n")
            return []

    # ===== TRANSIENT LOAD CASE GENERATION =====
    
    def generateTransientLoadCase(self, obj):
        """Generate transient load case for verification (RISA-3D style)."""
        try:
            if not hasattr(obj, 'GenerateTransientCase') or not obj.GenerateTransientCase:
                return None
            
            # Generate unique transient case name
            case_name = obj.TransientCaseName if hasattr(obj, 'TransientCaseName') and obj.TransientCaseName else f"Transient_{obj.Label}"
            
            transient_case = {
                'name': case_name,
                'load_type': 'Transient_Verification',
                'original_area_load': obj.Label,
                'member_loads': {},
                'verification_data': {}
            }
            
            # Calculate tributary areas if not done
            if not obj.TributaryAreas:
                self.calculateTributaryAreas(obj)
            
            if not obj.TributaryAreas:
                App.Console.PrintWarning(f"No tributary areas calculated for transient case generation\n")
                return None
            
            # Convert area loads to member loads
            for member_name, tributary_data in obj.TributaryAreas.items():
                member_obj = tributary_data.get('member_obj')
                if not member_obj:
                    continue
                
                # Create equivalent point loads on member
                member_loads = self._createEquivalentMemberLoads(obj, member_obj, tributary_data)
                
                if member_loads:
                    transient_case['member_loads'][member_name] = member_loads
            
            # Add verification data
            transient_case['verification_data'] = {
                'total_original_load': self._calculateTotalOriginalLoad(obj),
                'total_distributed_load': self._calculateTotalDistributedLoad(transient_case['member_loads']),
                'load_balance_check': self._checkLoadBalance(obj, transient_case),
                'distribution_method': obj.DistributionMethod,
                'created_timestamp': str(App.Console.PrintLog(''))
            }
            
            # Store transient case
            self._storeTransientCase(obj, transient_case)
            
            # Display transient case summary
            self._displayTransientCaseSummary(transient_case)
            
            return transient_case
            
        except Exception as e:
            App.Console.PrintError(f"Error generating transient load case: {e}\n")
            return None
    
    def _createEquivalentMemberLoads(self, area_load_obj, member_obj, tributary_data):
        """Create equivalent point loads for a member based on tributary area."""
        try:
            member_loads = []
            
            if not hasattr(member_obj, 'Shape') or not member_obj.Shape:
                return member_loads
            
            total_load = tributary_data['load']  # Already in kN
            
            # For beam members, distribute as distributed load
            if hasattr(member_obj.Shape, 'Edges') and member_obj.Shape.Edges:
                longest_edge = None
                max_length = 0.0
                
                for edge in member_obj.Shape.Edges:
                    length = edge.Length
                    if length > max_length:
                        max_length = length
                        longest_edge = edge
                
                if longest_edge and max_length > 0:
                    # Create distributed load along member
                    load_intensity = total_load / (max_length / 1000.0)  # kN/m
                    
                    member_load = {
                        'type': 'distributed',
                        'member': member_obj.Label,
                        'intensity': load_intensity,  # kN/m
                        'total_load': total_load,  # kN
                        'length': max_length / 1000.0,  # m
                        'direction': area_load_obj.Direction,
                        'load_case': area_load_obj.LoadCase if hasattr(area_load_obj, 'LoadCase') else 'DL1'
                    }
                    
                    member_loads.append(member_load)
                else:
                    # Fallback to point load at center
                    center = member_obj.Shape.CenterOfMass
                    
                    member_load = {
                        'type': 'point',
                        'member': member_obj.Label,
                        'position': center,
                        'magnitude': total_load,  # kN
                        'direction': area_load_obj.Direction,
                        'load_case': area_load_obj.LoadCase if hasattr(area_load_obj, 'LoadCase') else 'DL1'
                    }
                    
                    member_loads.append(member_load)
            
            return member_loads
            
        except Exception as e:
            App.Console.PrintWarning(f"Error creating equivalent member loads: {e}\n")
            return []
    
    def _calculateTotalOriginalLoad(self, obj):
        """Calculate total load from original area load."""
        try:
            intensity = self.parseLoadIntensity(obj.LoadIntensity)
            area = float(str(obj.LoadedArea).split()[0]) / 1000000.0 if hasattr(obj, 'LoadedArea') else 0.0  # Convert to m²
            
            return intensity * area  # kN
            
        except Exception as e:
            return 0.0
    
    def _calculateTotalDistributedLoad(self, member_loads):
        """Calculate total load from distributed member loads."""
        try:
            total = 0.0
            
            for member_name, loads in member_loads.items():
                for load in loads:
                    if 'total_load' in load:
                        total += load['total_load']
                    elif 'magnitude' in load:
                        total += load['magnitude']
            
            return total
            
        except Exception as e:
            return 0.0
    
    def _checkLoadBalance(self, area_load_obj, transient_case):
        """Check if distributed loads balance with original load."""
        try:
            original_load = transient_case['verification_data']['total_original_load']
            distributed_load = transient_case['verification_data']['total_distributed_load']
            
            if original_load == 0:
                return {'balanced': False, 'error': 'Zero original load'}
            
            balance_ratio = distributed_load / original_load
            tolerance = 0.01  # 1% tolerance
            
            is_balanced = abs(balance_ratio - 1.0) < tolerance
            
            return {
                'balanced': is_balanced,
                'original_load': original_load,
                'distributed_load': distributed_load,
                'balance_ratio': balance_ratio,
                'error_percent': abs(balance_ratio - 1.0) * 100.0
            }
            
        except Exception as e:
            return {'balanced': False, 'error': str(e)}
    
    def _storeTransientCase(self, obj, transient_case):
        """Store transient case data."""
        try:
            # Store in object properties
            if not hasattr(obj, 'TransientCases'):
                obj.addProperty("App::PropertyPythonObject", "TransientCases", "Advanced",
                               "Generated transient load cases")
                obj.TransientCases = {}
            
            cases = obj.TransientCases if obj.TransientCases else {}
            cases[transient_case['name']] = transient_case
            obj.TransientCases = cases
            
            App.Console.PrintMessage(f"Stored transient case: {transient_case['name']}\n")
            
        except Exception as e:
            App.Console.PrintError(f"Error storing transient case: {e}\n")
    
    def _displayTransientCaseSummary(self, transient_case):
        """Display summary of generated transient case."""
        try:
            App.Console.PrintMessage(f"\n=== Transient Load Case: {transient_case['name']} ===\n")
            
            verification = transient_case['verification_data']
            App.Console.PrintMessage(f"Original Area Load: {verification['total_original_load']:.2f} kN\n")
            App.Console.PrintMessage(f"Distributed Load: {verification['total_distributed_load']:.2f} kN\n")
            
            balance = verification['load_balance_check']
            if balance['balanced']:
                App.Console.PrintMessage(f"✓ Load Balance: OK (Error: {balance['error_percent']:.2f}%)\n")
            else:
                App.Console.PrintWarning(f"⚠ Load Balance: FAIL (Error: {balance.get('error_percent', 'N/A')}%)\n")
            
            App.Console.PrintMessage(f"Distribution Method: {verification['distribution_method']}\n")
            App.Console.PrintMessage(f"Member Loads Created: {len(transient_case['member_loads'])}\n")
            
            # List member loads
            for member_name, loads in transient_case['member_loads'].items():
                for load in loads:
                    if load['type'] == 'distributed':
                        App.Console.PrintMessage(f"  {member_name}: {load['intensity']:.2f} kN/m over {load['length']:.2f} m\n")
                    else:
                        App.Console.PrintMessage(f"  {member_name}: {load['magnitude']:.2f} kN point load\n")
            
            App.Console.PrintMessage("=" * 50 + "\n")
            
        except Exception as e:
            App.Console.PrintError(f"Error displaying transient case summary: {e}\n")
    
    # ===== PERFORMANCE OPTIMIZATION =====
    
    def optimizePerformance(self, obj):
        """Optimize performance with adaptive meshing and caching."""
        try:
            # Check if optimization is needed
            if not self._needsOptimization(obj):
                return
            
            # Adaptive mesh refinement
            if obj.AdaptiveMeshing:
                self._adaptiveMeshRefinement(obj)
            
            # Cache frequently used calculations
            self._cacheCalculations(obj)
            
            # Optimize visualization
            self._optimizeVisualization(obj)
            
            App.Console.PrintMessage(f"Performance optimization completed for {obj.Label}\n")
            
        except Exception as e:
            App.Console.PrintError(f"Error during performance optimization: {e}\n")
    
    def _needsOptimization(self, obj):
        """Check if performance optimization is needed."""
        try:
            # Check mesh size
            if obj.MeshData and 'elements' in obj.MeshData:
                element_count = len(obj.MeshData['elements'])
                if element_count > 1000:  # Large mesh
                    return True
            
            # Check loaded area size
            if hasattr(obj, 'LoadedArea'):
                area = float(str(obj.LoadedArea).split()[0])
                if area > 1000000000:  # > 1000 m²
                    return True
            
            return False
            
        except Exception as e:
            return False
    
    def _adaptiveMeshRefinement(self, obj):
        """Perform adaptive mesh refinement."""
        try:
            if not obj.MeshData or not obj.MeshData.get('elements'):
                return
            
            # Check mesh quality and refine poor elements
            mesh_quality = obj.MeshData.get('mesh_quality', {})
            
            needs_refinement = False
            for face_name, quality in mesh_quality.items():
                if quality.get('quality_score', 100) < 70:  # Poor quality
                    needs_refinement = True
                    break
            
            if needs_refinement:
                # Reduce mesh size for better quality
                original_size = obj.MeshSize
                obj.MeshSize = original_size * 0.8  # 20% smaller elements
                
                App.Console.PrintMessage(f"Adaptive refinement: reducing mesh size from {original_size} to {obj.MeshSize}\n")
                
                # Regenerate mesh
                self.generateAdvancedMesh(obj)
            
        except Exception as e:
            App.Console.PrintWarning(f"Error in adaptive mesh refinement: {e}\n")
    
    def _cacheCalculations(self, obj):
        """Cache frequently used calculations."""
        try:
            # Cache calculation results
            cache = getattr(obj, 'CalculationCache', {})
            
            # Cache load properties
            cache['load_intensity'] = self.parseLoadIntensity(obj.LoadIntensity)
            cache['direction_vector'] = self._get_direction_vector(obj)
            cache['load_center'] = obj.LoadCenter if hasattr(obj, 'LoadCenter') else App.Vector(0, 0, 0)
            
            # Store cache
            if not hasattr(obj, 'CalculationCache'):
                obj.addProperty("App::PropertyPythonObject", "CalculationCache", "Performance",
                               "Cached calculation results")
            obj.CalculationCache = cache
            
        except Exception as e:
            App.Console.PrintWarning(f"Error caching calculations: {e}\n")
    
    def _optimizeVisualization(self, obj):
        """Optimize visualization for better performance."""
        try:
            # Limit number of visualization objects
            if hasattr(obj, 'LoadVisualization') and obj.LoadVisualization:
                vis_count = len(obj.LoadVisualization)
                
                if vis_count > 500:  # Too many objects
                    # Reduce visualization density
                    App.Console.PrintMessage(f"Reducing visualization density from {vis_count} objects\n")
                    
                    # Keep only every Nth object
                    reduction_factor = max(2, vis_count // 300)
                    reduced_vis = obj.LoadVisualization[::reduction_factor]
                    
                    # Remove excess objects
                    doc = App.ActiveDocument
                    if doc:
                        for vis_obj in obj.LoadVisualization[300:]:
                            if vis_obj and hasattr(doc, 'getObject'):
                                try:
                                    doc.removeObject(vis_obj.Name)
                                except:
                                    continue
                    
                    obj.LoadVisualization = reduced_vis
            
        except Exception as e:
            App.Console.PrintWarning(f"Error optimizing visualization: {e}\n")