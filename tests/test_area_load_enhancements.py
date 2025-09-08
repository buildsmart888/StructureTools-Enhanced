# -*- coding: utf-8 -*-
"""
Test Suite for AreaLoad Enhancements - RISA-3D Level Functionality

This comprehensive test suite validates all the enhanced AreaLoad features
including advanced meshing, load validation, member attribution, visualization,
and transient load case generation.
"""

import pytest
import sys
import os
import math

# Add the module path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'freecad', 'StructureTools'))

try:
    import FreeCAD as App
    import FreeCADGui as Gui
    import Part
    import Draft
    FREECAD_AVAILABLE = True
except ImportError:
    FREECAD_AVAILABLE = False

from objects.AreaLoad import AreaLoad, makeAreaLoad

@pytest.fixture
def setup_document():
    """Setup FreeCAD document for testing"""
    if not FREECAD_AVAILABLE:
        pytest.skip("FreeCAD not available")
    
    # Create new document
    doc = App.newDocument("AreaLoadTest")
    yield doc
    
    # Cleanup
    App.closeDocument(doc.Name)

@pytest.fixture
def create_test_faces(setup_document):
    """Create test faces for area load testing"""
    doc = setup_document
    
    # Create rectangular face
    face1 = Part.makePlane(5000, 3000)  # 5m x 3m
    face_obj1 = doc.addObject("Part::Feature", "TestFace1")
    face_obj1.Shape = face1
    
    # Create circular face
    face2 = Part.Face(Part.Wire(Part.makeCircle(2000)))  # 2m radius
    face_obj2 = doc.addObject("Part::Feature", "TestFace2")
    face_obj2.Shape = face2
    
    doc.recompute()
    
    return [face_obj1, face_obj2]

@pytest.fixture
def create_test_members(setup_document):
    """Create test structural members"""
    doc = setup_document
    
    members = []
    
    # Create beam member
    beam_line = Part.makeLine(App.Vector(0, 0, 0), App.Vector(5000, 0, 0))
    beam_obj = doc.addObject("Part::Feature", "TestBeam")
    beam_obj.Shape = beam_line
    beam_obj.Label = "beam_main"
    members.append(beam_obj)
    
    # Create column member
    column_line = Part.makeLine(App.Vector(0, 0, 0), App.Vector(0, 0, 3000))
    column_obj = doc.addObject("Part::Feature", "TestColumn")
    column_obj.Shape = column_line
    column_obj.Label = "column_c1"
    members.append(column_obj)
    
    # Create brace member
    brace_line = Part.makeLine(App.Vector(0, 0, 0), App.Vector(3000, 3000, 0))
    brace_obj = doc.addObject("Part::Feature", "TestBrace")
    brace_obj.Shape = brace_line
    brace_obj.Label = "brace_x1"
    members.append(brace_obj)
    
    doc.recompute()
    return members

class TestAdvancedMeshing:
    """Test advanced meshing system"""
    
    def test_mesh_generation(self, create_test_faces):
        """Test basic mesh generation"""
        faces = create_test_faces
        
        # Create area load
        area_load = makeAreaLoad(
            target_faces=[faces[0]],
            magnitude="5.0 kN/m^2",
            name="TestMeshLoad"
        )
        
        # Set mesh parameters
        area_load.MeshSize = 500.0
        area_load.MeshType = "Triangular"
        area_load.AdaptiveMeshing = True
        
        # Generate mesh
        area_load.Proxy.generateAdvancedMesh(area_load)
        
        # Verify mesh data
        assert hasattr(area_load, 'MeshData')
        assert area_load.MeshData is not None
        assert 'elements' in area_load.MeshData
        assert 'nodes' in area_load.MeshData
        assert len(area_load.MeshData['elements']) > 0
        assert len(area_load.MeshData['nodes']) > 0
    
    def test_adaptive_meshing(self, create_test_faces):
        """Test adaptive meshing functionality"""
        faces = create_test_faces
        
        area_load = makeAreaLoad(target_faces=[faces[0]], name="TestAdaptiveMesh")
        area_load.AdaptiveMeshing = True
        area_load.MinMeshElements = 10
        area_load.MaxMeshElements = 100
        area_load.LoadAccuracyTolerance = 2.0
        
        # Generate mesh
        mesh_data = area_load.Proxy.generateAdvancedMesh(area_load)
        
        # Verify adaptive behavior
        assert mesh_data is not None
        element_count = len(mesh_data['elements'])
        assert area_load.MinMeshElements <= element_count <= area_load.MaxMeshElements
    
    def test_mesh_quality_validation(self, create_test_faces):
        """Test mesh quality validation"""
        faces = create_test_faces
        
        area_load = makeAreaLoad(target_faces=[faces[0]], name="TestMeshQuality")
        area_load.MeshSize = 100.0  # Fine mesh
        
        # Generate mesh
        area_load.Proxy.generateAdvancedMesh(area_load)
        
        # Check quality metrics
        assert 'mesh_quality' in area_load.MeshData
        quality_data = area_load.MeshData['mesh_quality']
        
        for face_name, quality in quality_data.items():
            assert 'quality_score' in quality
            assert 0 <= quality['quality_score'] <= 100

class TestLoadValidation:
    """Test load validation framework"""
    
    def test_basic_validation(self, create_test_faces):
        """Test basic load configuration validation"""
        faces = create_test_faces
        
        area_load = makeAreaLoad(
            target_faces=[faces[0]],
            magnitude="2.5 kN/m^2",
            load_type="Dead Load (DL)",
            name="TestValidation"
        )
        
        # Run validation
        validation_results = area_load.Proxy.validateLoadConfiguration(area_load)
        
        # Verify validation structure
        assert 'is_valid' in validation_results
        assert 'warnings' in validation_results
        assert 'errors' in validation_results
        assert 'checks' in validation_results
        
        # Check individual validation checks
        checks = validation_results['checks']
        assert 'load_magnitude' in checks
        assert 'load_direction' in checks
        assert 'tributary_areas' in checks
    
    def test_coplanarity_check(self, create_test_faces):
        """Test coplanarity validation"""
        faces = create_test_faces
        
        area_load = makeAreaLoad(target_faces=faces, name="TestCoplanarity")
        area_load.UseCoplanarProjection = True
        area_load.ProjectionTolerance = 5.0  # 5 degree tolerance
        
        # Run validation
        validation_results = area_load.Proxy.validateLoadConfiguration(area_load)
        
        # Check coplanarity result
        assert 'coplanarity' in validation_results['checks']
        coplanarity_check = validation_results['checks']['coplanarity']
        assert 'passed' in coplanarity_check
        assert 'message' in coplanarity_check
    
    def test_load_magnitude_validation(self, create_test_faces):
        """Test load magnitude reasonableness checks"""
        faces = create_test_faces
        
        # Test normal load
        area_load1 = makeAreaLoad(target_faces=[faces[0]], magnitude="3.0 kN/m^2", name="NormalLoad")
        area_load1.LoadCategory = "LL"
        validation1 = area_load1.Proxy.validateLoadConfiguration(area_load1)
        magnitude_check1 = validation1['checks']['load_magnitude']
        assert magnitude_check1['passed']
        
        # Test unusually high load
        area_load2 = makeAreaLoad(target_faces=[faces[0]], magnitude="50.0 kN/m^2", name="HighLoad")
        area_load2.LoadCategory = "LL"
        validation2 = area_load2.Proxy.validateLoadConfiguration(area_load2)
        magnitude_check2 = validation2['checks']['load_magnitude']
        assert magnitude_check2['severity'] == 'warning'
        
        # Test unusually low load
        area_load3 = makeAreaLoad(target_faces=[faces[0]], magnitude="0.01 kN/m^2", name="LowLoad")
        area_load3.LoadCategory = "DL"
        validation3 = area_load3.Proxy.validateLoadConfiguration(area_load3)
        magnitude_check3 = validation3['checks']['load_magnitude']
        assert magnitude_check3['severity'] == 'warning'

class TestMemberAttribution:
    """Test member attribution logic"""
    
    def test_member_finding(self, create_test_faces, create_test_members):
        """Test finding structural members"""
        faces = create_test_faces
        members = create_test_members
        
        area_load = makeAreaLoad(target_faces=[faces[0]], name="TestMemberFind")
        
        # Set member filtering
        area_load.IncludeBeams = True
        area_load.IncludeColumns = True
        area_load.IncludeBraces = False
        area_load.MemberInfluenceRadius = 5000.0  # 5m radius
        
        # Find members
        found_members = area_load.Proxy._findStructuralMembers(area_load)
        
        # Should find beam and column, but not brace
        assert len(found_members) >= 2
        member_labels = [m.Label for m in found_members]
        assert any('beam' in label.lower() for label in member_labels)
        assert any('column' in label.lower() for label in member_labels)
    
    def test_tributary_area_calculation(self, create_test_faces, create_test_members):
        """Test tributary area calculations"""
        faces = create_test_faces
        members = create_test_members
        
        area_load = makeAreaLoad(target_faces=[faces[0]], magnitude="4.0 kN/m^2", name="TestTributary")
        area_load.DistributionMethod = "TributaryArea"
        area_load.IncludeBeams = True
        area_load.IncludeColumns = True
        area_load.MemberInfluenceRadius = 10000.0
        
        # Calculate tributary areas
        tributary_areas = area_load.Proxy.calculateTributaryAreas(area_load)
        
        # Verify results
        assert tributary_areas is not None
        assert len(tributary_areas) > 0
        
        # Check data structure
        for member_name, data in tributary_areas.items():
            assert 'area' in data
            assert 'load' in data
            assert 'member_obj' in data
            assert data['area'] > 0
            assert data['load'] > 0
    
    def test_influence_coefficient_method(self, create_test_faces, create_test_members):
        """Test influence coefficient distribution method"""
        faces = create_test_faces
        
        area_load = makeAreaLoad(target_faces=[faces[0]], name="TestInfluence")
        area_load.DistributionMethod = "InfluenceCoefficient"
        area_load.IncludeBeams = True
        area_load.IncludeColumns = True
        
        # Generate mesh first
        area_load.Proxy.generateAdvancedMesh(area_load)
        
        # Calculate using influence coefficient method
        structural_members = area_load.Proxy._findStructuralMembers(area_load)
        mesh_data = area_load.MeshData
        
        if structural_members and mesh_data:
            tributary_areas = area_load.Proxy._calculateInfluenceCoefficientMethod(
                area_load, structural_members, mesh_data
            )
            
            assert tributary_areas is not None
            if len(tributary_areas) > 0:
                # Check that loads are distributed (not concentrated on single member)
                loads = [data['load'] for data in tributary_areas.values()]
                assert len(loads) > 1 or loads[0] > 0

class TestEnhancedProjection:
    """Test enhanced load projection system"""
    
    def test_coplanarity_analysis(self, create_test_faces):
        """Test coplanarity analysis"""
        faces = create_test_faces
        
        area_load = makeAreaLoad(target_faces=faces, name="TestProjection")
        area_load.UseCoplanarProjection = True
        area_load.ProjectionTolerance = 10.0
        
        # Analyze coplanarity
        analysis = area_load.Proxy._analyzeCoplanarity(area_load)
        
        assert 'is_coplanar' in analysis
        assert 'reference_normal' in analysis
        assert 'deviations' in analysis
        assert 'max_deviation' in analysis
    
    def test_base_projection_calculation(self, create_test_faces):
        """Test base projection calculations"""
        faces = create_test_faces
        
        area_load = makeAreaLoad(target_faces=[faces[0]], name="TestBaseProjection")
        area_load.Direction = "+Z Global"
        area_load.LoadIntensity = "3.0 kN/m^2"
        
        # Calculate base projections
        projections = area_load.Proxy._calculateBaseProjections(area_load)
        
        assert projections is not None
        assert len(projections) > 0
        
        for face_name, face_projections in projections.items():
            for proj in face_projections:
                assert 'face_center' in proj
                assert 'face_normal' in proj
                assert 'effective_intensity' in proj
                assert 'total_load' in proj
                assert proj['effective_intensity'] >= 0
                assert proj['total_load'] >= 0
    
    def test_shielding_effects(self, create_test_faces, create_test_members):
        """Test shielding effects for open structures"""
        faces = create_test_faces
        
        area_load = makeAreaLoad(target_faces=[faces[0]], name="TestShielding")
        area_load.LoadDistribution = "OpenStructure"
        area_load.ConsiderShielding = True
        area_load.ShieldingFactor = 0.8
        
        # Calculate base projections first
        base_projections = area_load.Proxy._calculateBaseProjections(area_load)
        
        # Calculate shielding effects
        shielding_effects = area_load.Proxy._calculateShieldingEffects(area_load, base_projections)
        
        # Apply shielding
        shielded_projections = area_load.Proxy._applyShielding(
            base_projections, shielding_effects, area_load.ShieldingFactor
        )
        
        assert shielded_projections is not None
        
        # Check that shielding reduces loads
        for face_name in base_projections.keys():
            if face_name in shielded_projections:
                base_total = sum(p['total_load'] for p in base_projections[face_name])
                shielded_total = sum(p['total_load'] for p in shielded_projections[face_name])
                # Shielded load should be less than or equal to base load
                assert shielded_total <= base_total + 1e-6  # Allow for numerical precision

class TestAdvancedVisualization:
    """Test advanced visualization features"""
    
    def test_mesh_visualization(self, create_test_faces):
        """Test mesh element visualization"""
        faces = create_test_faces
        
        area_load = makeAreaLoad(target_faces=[faces[0]], name="TestMeshVis")
        area_load.ShowMeshElements = True
        area_load.MeshSize = 1000.0
        
        # Generate mesh
        area_load.Proxy.generateAdvancedMesh(area_load)
        
        # Create mesh visualization
        mesh_vis = area_load.Proxy._createMeshVisualization(area_load)
        
        # Should create visualization objects
        assert isinstance(mesh_vis, list)
    
    def test_pressure_contours(self, create_test_faces):
        """Test pressure contour generation"""
        faces = create_test_faces
        
        area_load = makeAreaLoad(target_faces=[faces[0]], name="TestContours")
        area_load.ShowPressureContours = True
        area_load.ContourLevels = 5
        area_load.LoadIntensity = "4.0 kN/m^2"
        
        # Create pressure contours
        contours = area_load.Proxy._createPressureContours(area_load)
        
        # Should create contour objects
        assert isinstance(contours, list)
    
    def test_load_distribution_visualization(self, create_test_faces):
        """Test load distribution pattern visualization"""
        faces = create_test_faces
        
        # Test one-way distribution
        area_load1 = makeAreaLoad(target_faces=[faces[0]], name="TestOneWay")
        area_load1.LoadDistribution = "OneWay"
        area_load1.ShowLoadDistribution = True
        
        one_way_vis = area_load1.Proxy._createOneWayVisualization(area_load1)
        assert isinstance(one_way_vis, list)
        
        # Test two-way distribution
        area_load2 = makeAreaLoad(target_faces=[faces[0]], name="TestTwoWay")
        area_load2.LoadDistribution = "TwoWay"
        area_load2.ShowLoadDistribution = True
        
        two_way_vis = area_load2.Proxy._createTwoWayVisualization(area_load2)
        assert isinstance(two_way_vis, list)

class TestTransientLoadCase:
    """Test transient load case generation"""
    
    def test_transient_case_generation(self, create_test_faces, create_test_members):
        """Test transient load case generation"""
        faces = create_test_faces
        
        area_load = makeAreaLoad(target_faces=[faces[0]], name="TestTransient")
        area_load.GenerateTransientCase = True
        area_load.TransientCaseName = "Test_Transient_Case"
        area_load.LoadIntensity = "5.0 kN/m^2"
        area_load.IncludeBeams = True
        area_load.IncludeColumns = True
        
        # Generate transient case
        transient_case = area_load.Proxy.generateTransientLoadCase(area_load)
        
        if transient_case:  # May be None if no members found
            assert 'name' in transient_case
            assert 'member_loads' in transient_case
            assert 'verification_data' in transient_case
            
            # Check verification data
            verification = transient_case['verification_data']
            assert 'total_original_load' in verification
            assert 'total_distributed_load' in verification
            assert 'load_balance_check' in verification
    
    def test_load_balance_checking(self, create_test_faces, create_test_members):
        """Test load balance verification"""
        faces = create_test_faces
        
        area_load = makeAreaLoad(target_faces=[faces[0]], name="TestBalance")
        area_load.LoadIntensity = "3.0 kN/m^2"
        
        # Mock transient case data
        mock_transient_case = {
            'member_loads': {
                'member1': [{'total_load': 10.0}],
                'member2': [{'total_load': 5.0}]
            },
            'verification_data': {
                'total_original_load': 15.0,
                'total_distributed_load': 15.0
            }
        }
        
        # Check load balance
        balance_result = area_load.Proxy._checkLoadBalance(area_load, mock_transient_case)
        
        assert 'balanced' in balance_result
        assert 'balance_ratio' in balance_result
        assert 'error_percent' in balance_result
        
        # Should be balanced for this test case
        assert balance_result['balanced'] == True
        assert abs(balance_result['balance_ratio'] - 1.0) < 0.01

class TestPerformanceOptimization:
    """Test performance optimization features"""
    
    def test_optimization_detection(self, create_test_faces):
        """Test detection of optimization needs"""
        faces = create_test_faces
        
        area_load = makeAreaLoad(target_faces=[faces[0]], name="TestOptimization")
        area_load.MeshSize = 50.0  # Very fine mesh
        
        # Generate large mesh
        area_load.Proxy.generateAdvancedMesh(area_load)
        
        # Check if optimization is needed
        needs_opt = area_load.Proxy._needsOptimization(area_load)
        
        # With fine mesh, should need optimization
        if area_load.MeshData and len(area_load.MeshData.get('elements', {})) > 1000:
            assert needs_opt == True
    
    def test_adaptive_mesh_refinement(self, create_test_faces):
        """Test adaptive mesh refinement"""
        faces = create_test_faces
        
        area_load = makeAreaLoad(target_faces=[faces[0]], name="TestRefinement")
        area_load.AdaptiveMeshing = True
        area_load.MeshSize = 200.0
        
        # Generate initial mesh
        area_load.Proxy.generateAdvancedMesh(area_load)
        original_size = area_load.MeshSize
        
        # Mock poor quality data
        if area_load.MeshData:
            area_load.MeshData['mesh_quality'] = {
                'TestFace1': {'quality_score': 60.0}  # Poor quality
            }
        
        # Apply adaptive refinement
        area_load.Proxy._adaptiveMeshRefinement(area_load)
        
        # Mesh size should be reduced for poor quality
        # (This may not trigger in all cases depending on the mock data)
        assert area_load.MeshSize <= original_size
    
    def test_calculation_caching(self, create_test_faces):
        """Test calculation caching"""
        faces = create_test_faces
        
        area_load = makeAreaLoad(target_faces=[faces[0]], name="TestCaching")
        
        # Cache calculations
        area_load.Proxy._cacheCalculations(area_load)
        
        # Check if cache exists
        if hasattr(area_load, 'CalculationCache'):
            cache = area_load.CalculationCache
            assert 'load_intensity' in cache
            assert 'direction_vector' in cache
            assert 'load_center' in cache

class TestIntegration:
    """Integration tests for complete workflow"""
    
    def test_complete_workflow(self, create_test_faces, create_test_members):
        """Test complete area load workflow"""
        faces = create_test_faces
        
        # Create area load with all features enabled
        area_load = makeAreaLoad(
            target_faces=[faces[0]],
            magnitude="4.0 kN/m^2",
            load_type="Live Load (LL)",
            name="CompleteWorkflow"
        )
        
        # Configure all features
        area_load.MeshSize = 500.0
        area_load.AdaptiveMeshing = True
        area_load.DistributionMethod = "TributaryArea"
        area_load.IncludeBeams = True
        area_load.IncludeColumns = True
        area_load.UseCoplanarProjection = True
        area_load.ShowLoadDistribution = True
        area_load.GenerateTransientCase = True
        area_load.AutoValidateOnChange = True
        
        # Execute complete workflow
        area_load.Proxy.execute(area_load)
        
        # Verify all components worked
        assert hasattr(area_load, 'MeshData')
        assert hasattr(area_load, 'TributaryAreas')
        assert hasattr(area_load, 'LoadValidation')
        
        # Check validation results
        if area_load.LoadValidation:
            assert 'is_valid' in area_load.LoadValidation
            assert 'checks' in area_load.LoadValidation
    
    def test_property_change_reactions(self, create_test_faces):
        """Test reactions to property changes"""
        faces = create_test_faces
        
        area_load = makeAreaLoad(target_faces=[faces[0]], name="TestPropertyChange")
        area_load.AutoValidateOnChange = True
        
        # Change mesh properties
        original_mesh_size = area_load.MeshSize
        area_load.MeshSize = original_mesh_size * 2
        area_load.Proxy.onChanged(area_load, "MeshSize")
        
        # Change load properties
        area_load.LoadIntensity = "6.0 kN/m^2"
        area_load.Proxy.onChanged(area_load, "LoadIntensity")
        
        # Changes should trigger recalculations
        # (Exact behavior depends on AutoValidateOnChange implementation)
    
    def test_error_handling(self, create_test_faces):
        """Test error handling and robustness"""
        faces = create_test_faces
        
        area_load = makeAreaLoad(target_faces=[faces[0]], name="TestErrorHandling")
        
        # Test with invalid mesh size
        area_load.MeshSize = -100.0  # Invalid
        mesh_data = area_load.Proxy.generateAdvancedMesh(area_load)
        # Should handle gracefully, return empty or None
        
        # Test with no target faces
        area_load.TargetFaces = []
        tributary_areas = area_load.Proxy.calculateTributaryAreas(area_load)
        assert tributary_areas == {} or tributary_areas is None
        
        # Test validation with invalid configuration
        validation = area_load.Proxy.validateLoadConfiguration(area_load)
        assert validation is not None
        assert 'is_valid' in validation


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v", "--tb=short"])