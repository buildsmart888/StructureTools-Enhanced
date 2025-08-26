# -*- coding: utf-8 -*-
"""
SurfaceMesh - Surface mesh management and quality control

This module provides surface mesh management, quality assessment, and 
integration with structural analysis systems.
"""

import FreeCAD as App
import FreeCADGui as Gui
import Part
import math
import numpy as np
from typing import List, Dict, Tuple, Optional, Any


class SurfaceMesh:
    """
    Surface mesh management and quality control class.
    
    Manages 2D finite element meshes for structural surfaces with:
    - Quality assessment and reporting
    - Mesh refinement and coarsening
    - Integration with analysis systems
    """
    
    def __init__(self, mesh_data=None):
        """
        Initialize SurfaceMesh.
        
        Args:
            mesh_data: Dictionary containing mesh data
        """
        self.mesh_data = mesh_data or {}
        self.quality_metrics = {}
        self.refinement_zones = []
        self.boundary_conditions = {}
    
    def assessMeshQuality(self):
        """Assess overall mesh quality."""
        try:
            if not self.mesh_data or "elements" not in self.mesh_data:
                App.Console.PrintError("No mesh data available for quality assessment\n")
                return {}
            
            nodes = self.mesh_data["nodes"]
            quality_summary = {}
            
            for elem_type, elements in self.mesh_data["elements"].items():
                qualities = []
                aspect_ratios = []
                skewness = []
                
                for element in elements:
                    # Calculate quality metrics
                    quality = self.calculateElementQuality(element, nodes, elem_type)
                    aspect = self.calculateAspectRatio(element, nodes, elem_type)
                    skew = self.calculateSkewness(element, nodes, elem_type)
                    
                    qualities.append(quality)
                    aspect_ratios.append(aspect)
                    skewness.append(skew)
                
                if qualities:
                    quality_summary[elem_type] = {
                        "count": len(elements),
                        "quality": {
                            "min": min(qualities),
                            "max": max(qualities),
                            "avg": sum(qualities) / len(qualities),
                            "std": np.std(qualities) if len(qualities) > 1 else 0.0
                        },
                        "aspect_ratio": {
                            "min": min(aspect_ratios),
                            "max": max(aspect_ratios),
                            "avg": sum(aspect_ratios) / len(aspect_ratios)
                        },
                        "skewness": {
                            "min": min(skewness),
                            "max": max(skewness),
                            "avg": sum(skewness) / len(skewness)
                        }
                    }
            
            self.quality_metrics = quality_summary
            self.printQualityReport()
            
            return quality_summary
            
        except Exception as e:
            App.Console.PrintError(f"Error assessing mesh quality: {e}\n")
            return {}
    
    def calculateElementQuality(self, element, nodes, elem_type):
        """Calculate element quality metric (0-1, 1 being best)."""
        try:
            node_coords = [nodes[nid][:3] for nid in element["nodes"]]
            
            if elem_type.startswith("Tri"):
                return self.triangleQuality(node_coords)
            elif elem_type.startswith("Quad"):
                return self.quadrilateralQuality(node_coords)
            else:
                return 1.0
                
        except Exception:
            return 0.0
    
    def triangleQuality(self, coords):
        """Calculate triangle quality using area-to-perimeter ratio."""
        try:
            # Calculate side lengths
            a = self.distance3D(coords[0], coords[1])
            b = self.distance3D(coords[1], coords[2])
            c = self.distance3D(coords[2], coords[0])
            
            # Calculate area using cross product
            v1 = [coords[1][i] - coords[0][i] for i in range(3)]
            v2 = [coords[2][i] - coords[0][i] for i in range(3)]
            
            cross = [
                v1[1] * v2[2] - v1[2] * v2[1],
                v1[2] * v2[0] - v1[0] * v2[2],
                v1[0] * v2[1] - v1[1] * v2[0]
            ]
            
            area = 0.5 * math.sqrt(sum(x**2 for x in cross))
            perimeter = a + b + c
            
            # Quality metric: 4*sqrt(3)*area / perimeter^2
            # Equals 1 for equilateral triangle, decreases for poor shapes
            if perimeter > 0:
                quality = (4 * math.sqrt(3) * area) / (perimeter * perimeter)
                return min(quality, 1.0)
            
            return 0.0
            
        except Exception:
            return 0.0
    
    def quadrilateralQuality(self, coords):
        """Calculate quadrilateral quality."""
        try:
            # Calculate diagonal lengths
            d1 = self.distance3D(coords[0], coords[2])
            d2 = self.distance3D(coords[1], coords[3])
            
            # Calculate side lengths
            sides = []
            for i in range(4):
                next_i = (i + 1) % 4
                side = self.distance3D(coords[i], coords[next_i])
                sides.append(side)
            
            # Quality based on aspect ratio and skewness
            min_side = min(sides)
            max_side = max(sides)
            
            aspect_quality = min_side / max_side if max_side > 0 else 0.0
            
            # Diagonal ratio (should be close to 1 for squares)
            diag_ratio = min(d1, d2) / max(d1, d2) if max(d1, d2) > 0 else 0.0
            
            # Combined quality metric
            quality = (aspect_quality + diag_ratio) / 2.0
            return min(quality, 1.0)
            
        except Exception:
            return 0.0
    
    def calculateAspectRatio(self, element, nodes, elem_type):
        """Calculate element aspect ratio."""
        try:
            node_coords = [nodes[nid][:3] for nid in element["nodes"]]
            
            if elem_type.startswith("Tri"):
                # For triangles: ratio of longest to shortest side
                sides = []
                for i in range(3):
                    next_i = (i + 1) % 3
                    side = self.distance3D(node_coords[i], node_coords[next_i])
                    sides.append(side)
                
                return max(sides) / min(sides) if min(sides) > 0 else float('inf')
            
            elif elem_type.startswith("Quad"):
                # For quads: ratio of longest to shortest side
                sides = []
                for i in range(4):
                    next_i = (i + 1) % 4
                    side = self.distance3D(node_coords[i], node_coords[next_i])
                    sides.append(side)
                
                return max(sides) / min(sides) if min(sides) > 0 else float('inf')
            
            return 1.0
            
        except Exception:
            return float('inf')
    
    def calculateSkewness(self, element, nodes, elem_type):
        """Calculate element skewness (0-1, 0 being best)."""
        try:
            node_coords = [nodes[nid][:3] for nid in element["nodes"]]
            
            if elem_type.startswith("Tri"):
                # For triangles: deviation from equilateral
                angles = self.calculateTriangleAngles(node_coords)
                ideal_angle = math.pi / 3  # 60 degrees
                
                max_deviation = max(abs(angle - ideal_angle) for angle in angles)
                return max_deviation / ideal_angle
            
            elif elem_type.startswith("Quad"):
                # For quads: deviation from square
                angles = self.calculateQuadAngles(node_coords)
                ideal_angle = math.pi / 2  # 90 degrees
                
                max_deviation = max(abs(angle - ideal_angle) for angle in angles)
                return max_deviation / ideal_angle
            
            return 0.0
            
        except Exception:
            return 1.0
    
    def calculateTriangleAngles(self, coords):
        """Calculate interior angles of triangle."""
        try:
            angles = []
            
            for i in range(3):
                p1 = coords[i]
                p2 = coords[(i + 1) % 3]
                p3 = coords[(i + 2) % 3]
                
                # Vectors from p1
                v1 = [p2[j] - p1[j] for j in range(3)]
                v2 = [p3[j] - p1[j] for j in range(3)]
                
                # Calculate angle using dot product
                dot_product = sum(v1[j] * v2[j] for j in range(3))
                mag1 = math.sqrt(sum(v1[j]**2 for j in range(3)))
                mag2 = math.sqrt(sum(v2[j]**2 for j in range(3)))
                
                if mag1 > 0 and mag2 > 0:
                    cos_angle = dot_product / (mag1 * mag2)
                    cos_angle = max(-1.0, min(1.0, cos_angle))  # Clamp to valid range
                    angle = math.acos(cos_angle)
                    angles.append(angle)
            
            return angles
            
        except Exception:
            return [math.pi / 3] * 3  # Default to equilateral
    
    def calculateQuadAngles(self, coords):
        """Calculate interior angles of quadrilateral."""
        try:
            angles = []
            
            for i in range(4):
                p1 = coords[i]
                p2 = coords[(i + 1) % 4]
                p3 = coords[(i + 3) % 4]  # Previous vertex
                
                # Vectors from p1
                v1 = [p2[j] - p1[j] for j in range(3)]
                v2 = [p3[j] - p1[j] for j in range(3)]
                
                # Calculate angle
                dot_product = sum(v1[j] * v2[j] for j in range(3))
                mag1 = math.sqrt(sum(v1[j]**2 for j in range(3)))
                mag2 = math.sqrt(sum(v2[j]**2 for j in range(3)))
                
                if mag1 > 0 and mag2 > 0:
                    cos_angle = dot_product / (mag1 * mag2)
                    cos_angle = max(-1.0, min(1.0, cos_angle))
                    angle = math.acos(cos_angle)
                    angles.append(angle)
            
            return angles
            
        except Exception:
            return [math.pi / 2] * 4  # Default to square
    
    def distance3D(self, p1, p2):
        """Calculate 3D distance between two points."""
        return math.sqrt(sum((p1[i] - p2[i])**2 for i in range(3)))
    
    def identifyPoorElements(self, quality_threshold=0.3, aspect_threshold=4.0):
        """Identify elements with poor quality."""
        poor_elements = []
        
        try:
            if not self.mesh_data or "elements" not in self.mesh_data:
                return poor_elements
            
            nodes = self.mesh_data["nodes"]
            
            for elem_type, elements in self.mesh_data["elements"].items():
                for element in elements:
                    quality = self.calculateElementQuality(element, nodes, elem_type)
                    aspect = self.calculateAspectRatio(element, nodes, elem_type)
                    
                    if quality < quality_threshold or aspect > aspect_threshold:
                        poor_elements.append({
                            "element": element,
                            "type": elem_type,
                            "quality": quality,
                            "aspect_ratio": aspect,
                            "issues": []
                        })
                        
                        # Identify specific issues
                        if quality < quality_threshold:
                            poor_elements[-1]["issues"].append("Low quality")
                        if aspect > aspect_threshold:
                            poor_elements[-1]["issues"].append("High aspect ratio")
            
            App.Console.PrintMessage(f"Found {len(poor_elements)} poor quality elements\n")
            return poor_elements
            
        except Exception as e:
            App.Console.PrintError(f"Error identifying poor elements: {e}\n")
            return poor_elements
    
    def suggestRefinement(self, poor_elements):
        """Suggest mesh refinement strategies."""
        suggestions = []
        
        try:
            for poor_elem in poor_elements:
                element = poor_elem["element"]
                elem_type = poor_elem["type"]
                issues = poor_elem["issues"]
                
                suggestion = {
                    "element_id": element["id"],
                    "current_type": elem_type,
                    "actions": []
                }
                
                if "Low quality" in issues:
                    if elem_type.startswith("Tri"):
                        suggestion["actions"].append("Subdivide triangle")
                        suggestion["actions"].append("Convert to quadrilateral if possible")
                    elif elem_type.startswith("Quad"):
                        suggestion["actions"].append("Subdivide quadrilateral")
                        suggestion["actions"].append("Improve node positioning")
                
                if "High aspect ratio" in issues:
                    suggestion["actions"].append("Refine in direction of longest edge")
                    suggestion["actions"].append("Add intermediate nodes")
                
                suggestions.append(suggestion)
            
            return suggestions
            
        except Exception as e:
            App.Console.PrintError(f"Error generating refinement suggestions: {e}\n")
            return suggestions
    
    def printQualityReport(self):
        """Print comprehensive quality report."""
        try:
            App.Console.PrintMessage("\n" + "="*50 + "\n")
            App.Console.PrintMessage("SURFACE MESH QUALITY REPORT\n")
            App.Console.PrintMessage("="*50 + "\n")
            
            if not self.quality_metrics:
                App.Console.PrintMessage("No quality metrics available\n")
                return
            
            total_elements = 0
            for elem_type, metrics in self.quality_metrics.items():
                count = metrics["count"]
                total_elements += count
                
                App.Console.PrintMessage(f"\n{elem_type} Elements: {count}\n")
                App.Console.PrintMessage("-" * 30 + "\n")
                
                # Quality metrics
                quality = metrics["quality"]
                App.Console.PrintMessage(f"Quality:      Min={quality['min']:.3f}, "
                                       f"Max={quality['max']:.3f}, "
                                       f"Avg={quality['avg']:.3f}\n")
                
                # Aspect ratio
                aspect = metrics["aspect_ratio"]
                App.Console.PrintMessage(f"Aspect Ratio: Min={aspect['min']:.2f}, "
                                       f"Max={aspect['max']:.2f}, "
                                       f"Avg={aspect['avg']:.2f}\n")
                
                # Skewness
                skew = metrics["skewness"]
                App.Console.PrintMessage(f"Skewness:     Min={skew['min']:.3f}, "
                                       f"Max={skew['max']:.3f}, "
                                       f"Avg={skew['avg']:.3f}\n")
            
            App.Console.PrintMessage(f"\nTotal Elements: {total_elements}\n")
            
            # Overall assessment
            App.Console.PrintMessage("\nOVERALL ASSESSMENT:\n")
            App.Console.PrintMessage("-" * 20 + "\n")
            
            # Calculate overall quality score
            overall_quality = self.calculateOverallQuality()
            
            if overall_quality > 0.8:
                App.Console.PrintMessage("✅ EXCELLENT mesh quality\n")
            elif overall_quality > 0.6:
                App.Console.PrintMessage("✅ GOOD mesh quality\n")
            elif overall_quality > 0.4:
                App.Console.PrintMessage("⚠️  FAIR mesh quality - consider refinement\n")
            else:
                App.Console.PrintMessage("❌ POOR mesh quality - refinement recommended\n")
            
            App.Console.PrintMessage(f"Overall Quality Score: {overall_quality:.3f}\n")
            App.Console.PrintMessage("="*50 + "\n")
            
        except Exception as e:
            App.Console.PrintError(f"Error printing quality report: {e}\n")
    
    def calculateOverallQuality(self):
        """Calculate overall mesh quality score."""
        try:
            if not self.quality_metrics:
                return 0.0
            
            total_elements = 0
            weighted_quality = 0.0
            
            for elem_type, metrics in self.quality_metrics.items():
                count = metrics["count"]
                avg_quality = metrics["quality"]["avg"]
                
                weighted_quality += count * avg_quality
                total_elements += count
            
            return weighted_quality / total_elements if total_elements > 0 else 0.0
            
        except Exception:
            return 0.0
    
    def exportQualityReport(self, filename):
        """Export quality report to file."""
        try:
            with open(filename, 'w') as f:
                f.write("Surface Mesh Quality Report\n")
                f.write("="*40 + "\n\n")
                
                if not self.quality_metrics:
                    f.write("No quality metrics available\n")
                    return False
                
                for elem_type, metrics in self.quality_metrics.items():
                    f.write(f"{elem_type} Elements: {metrics['count']}\n")
                    f.write("-" * 30 + "\n")
                    
                    quality = metrics["quality"]
                    f.write(f"Quality:      Min={quality['min']:.3f}, "
                           f"Max={quality['max']:.3f}, "
                           f"Avg={quality['avg']:.3f}\n")
                    
                    aspect = metrics["aspect_ratio"]
                    f.write(f"Aspect Ratio: Min={aspect['min']:.2f}, "
                           f"Max={aspect['max']:.2f}, "
                           f"Avg={aspect['avg']:.2f}\n")
                    
                    f.write("\n")
                
                overall_quality = self.calculateOverallQuality()
                f.write(f"Overall Quality Score: {overall_quality:.3f}\n")
            
            App.Console.PrintMessage(f"Quality report exported to: {filename}\n")
            return True
            
        except Exception as e:
            App.Console.PrintError(f"Error exporting quality report: {e}\n")
            return False


class MeshIntegrationManager:
    """Manager for integrating surface meshes with analysis systems."""
    
    def __init__(self):
        """Initialize mesh integration manager."""
        self.meshes = {}
        self.analysis_systems = ["Pynite", "CalculiX", "FEM"]
    
    def registerMesh(self, mesh_id, surface_mesh):
        """Register a surface mesh."""
        self.meshes[mesh_id] = surface_mesh
        App.Console.PrintMessage(f"Registered mesh: {mesh_id}\n")
    
    def integratePynite(self, mesh_id):
        """Integrate mesh with Pynite analysis."""
        try:
            if mesh_id not in self.meshes:
                App.Console.PrintError(f"Mesh {mesh_id} not found\n")
                return False
            
            surface_mesh = self.meshes[mesh_id]
            mesh_data = surface_mesh.mesh_data
            
            # Convert to Pynite format
            App.Console.PrintMessage(f"Integrating mesh {mesh_id} with Pynite\n")
            
            # This would integrate with the existing Pynite analysis system
            # Implementation would convert nodes/elements to Pynite format
            
            return True
            
        except Exception as e:
            App.Console.PrintError(f"Error integrating with Pynite: {e}\n")
            return False
    
    def exportForAnalysis(self, mesh_id, format_type, filename):
        """Export mesh for external analysis."""
        try:
            if mesh_id not in self.meshes:
                App.Console.PrintError(f"Mesh {mesh_id} not found\n")
                return False
            
            surface_mesh = self.meshes[mesh_id]
            mesh_data = surface_mesh.mesh_data
            
            if format_type.lower() == "calculix":
                return self.exportCalculiX(mesh_data, filename)
            elif format_type.lower() == "nastran":
                return self.exportNastran(mesh_data, filename)
            else:
                App.Console.PrintError(f"Unsupported format: {format_type}\n")
                return False
                
        except Exception as e:
            App.Console.PrintError(f"Error exporting mesh: {e}\n")
            return False
    
    def exportCalculiX(self, mesh_data, filename):
        """Export mesh in CalculiX format."""
        try:
            with open(filename, 'w') as f:
                f.write("*HEADING\n")
                f.write("Surface Mesh Export\n")
                f.write("*NODE\n")
                
                # Write nodes
                for node_id, coords in mesh_data["nodes"].items():
                    f.write(f"{node_id}, {coords[0]:.6f}, {coords[1]:.6f}, {coords[2]:.6f}\n")
                
                # Write elements
                for elem_type, elements in mesh_data["elements"].items():
                    ccx_type = {"Tri3": "S3", "Quad4": "S4", "Tri6": "S6", "Quad8": "S8"}.get(elem_type, "S4")
                    f.write(f"*ELEMENT, TYPE={ccx_type}\n")
                    
                    for element in elements:
                        nodes_str = ", ".join(map(str, element["nodes"]))
                        f.write(f"{element['id']}, {nodes_str}\n")
            
            App.Console.PrintMessage(f"Mesh exported to CalculiX format: {filename}\n")
            return True
            
        except Exception as e:
            App.Console.PrintError(f"Error exporting to CalculiX: {e}\n")
            return False
    
    def exportNastran(self, mesh_data, filename):
        """Export mesh in Nastran format."""
        try:
            with open(filename, 'w') as f:
                f.write("$ Surface Mesh Export\n")
                f.write("BEGIN BULK\n")
                
                # Write nodes (GRID cards)
                for node_id, coords in mesh_data["nodes"].items():
                    f.write(f"GRID    {node_id:8d}        {coords[0]:8.3f}{coords[1]:8.3f}{coords[2]:8.3f}\n")
                
                # Write elements
                for elem_type, elements in mesh_data["elements"].items():
                    if elem_type == "Tri3":
                        for element in elements:
                            f.write(f"CTRIA3  {element['id']:8d}1       ")
                            f.write(f"{element['nodes'][0]:8d}{element['nodes'][1]:8d}{element['nodes'][2]:8d}\n")
                    elif elem_type == "Quad4":
                        for element in elements:
                            f.write(f"CQUAD4  {element['id']:8d}1       ")
                            f.write(f"{element['nodes'][0]:8d}{element['nodes'][1]:8d}")
                            f.write(f"{element['nodes'][2]:8d}{element['nodes'][3]:8d}\n")
                
                f.write("ENDDATA\n")
            
            App.Console.PrintMessage(f"Mesh exported to Nastran format: {filename}\n")
            return True
            
        except Exception as e:
            App.Console.PrintError(f"Error exporting to Nastran: {e}\n")
            return False
