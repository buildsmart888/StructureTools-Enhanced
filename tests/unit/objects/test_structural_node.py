# -*- coding: utf-8 -*-
"""
Unit tests for StructuralNode class.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from StructureTools.objects.StructuralNode import StructuralNode


@pytest.mark.unit
class TestStructuralNode:
    """Test suite for StructuralNode class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.mock_obj = Mock()
        self.mock_obj.addProperty = Mock()
        self.node = StructuralNode(self.mock_obj)
    
    def test_node_initialization(self):
        """Test node object initialization."""
        assert self.node.Type == "StructuralNode"
        assert self.mock_obj.Proxy == self.node
        
        # Verify essential properties were added
        property_calls = [call.args for call in self.mock_obj.addProperty.call_args_list]
        property_names = [call[1] for call in property_calls]
        
        essential_properties = [
            "Position", "RestraintX", "RestraintY", "RestraintZ",
            "RestraintRX", "RestraintRY", "RestraintRZ", "NodeID"
        ]
        
        for prop in essential_properties:
            assert prop in property_names, f"Property {prop} not added during initialization"
    
    def test_restraint_code_generation(self):
        """Test restraint code generation."""
        # Set up specific restraint pattern (pinned support)
        self.mock_obj.RestraintX = True
        self.mock_obj.RestraintY = True
        self.mock_obj.RestraintZ = True
        self.mock_obj.RestraintRX = False
        self.mock_obj.RestraintRY = False
        self.mock_obj.RestraintRZ = False
        
        # Mock hasattr and getattr for the restraint properties
        def mock_getattr(obj, attr, default=False):
            restraint_values = {
                'RestraintX': True,
                'RestraintY': True,
                'RestraintZ': True,
                'RestraintRX': False,
                'RestraintRY': False,
                'RestraintRZ': False
            }
            return restraint_values.get(attr, default)
        
        with patch('builtins.getattr', side_effect=mock_getattr):
            restraint_code = self.node.get_restraint_code()
            assert restraint_code == "111000"  # Pinned support
    
    def test_fixed_support_restraint_code(self):
        """Test restraint code for fixed support."""
        # All restraints active
        restraint_values = {
            'RestraintX': True, 'RestraintY': True, 'RestraintZ': True,
            'RestraintRX': True, 'RestraintRY': True, 'RestraintRZ': True
        }
        
        def mock_getattr(obj, attr, default=False):
            return restraint_values.get(attr, default)
        
        with patch('builtins.getattr', side_effect=mock_getattr):
            restraint_code = self.node.get_restraint_code()
            assert restraint_code == "111111"  # Fixed support
    
    def test_roller_support_restraint_code(self):
        """Test restraint code for roller support."""
        # Only vertical restraint
        restraint_values = {
            'RestraintX': False, 'RestraintY': False, 'RestraintZ': True,
            'RestraintRX': False, 'RestraintRY': False, 'RestraintRZ': False
        }
        
        def mock_getattr(obj, attr, default=False):
            return restraint_values.get(attr, default)
        
        with patch('builtins.getattr', side_effect=mock_getattr):
            restraint_code = self.node.get_restraint_code()
            assert restraint_code == "001000"  # Roller support
    
    def test_free_node_restraint_code(self):
        """Test restraint code for free node."""
        # No restraints
        restraint_values = {
            'RestraintX': False, 'RestraintY': False, 'RestraintZ': False,
            'RestraintRX': False, 'RestraintRY': False, 'RestraintRZ': False
        }
        
        def mock_getattr(obj, attr, default=False):
            return restraint_values.get(attr, default)
        
        with patch('builtins.getattr', side_effect=mock_getattr):
            restraint_code = self.node.get_restraint_code()
            assert restraint_code == "000000"  # Free node
    
    def test_is_restrained_check(self):
        """Test restraint detection."""
        # Test with restraints
        restraint_values = {
            'RestraintX': True, 'RestraintY': False, 'RestraintZ': False,
            'RestraintRX': False, 'RestraintRY': False, 'RestraintRZ': False
        }
        
        def mock_getattr(obj, attr, default=False):
            return restraint_values.get(attr, default)
        
        with patch('builtins.getattr', side_effect=mock_getattr):
            assert self.node.is_restrained() == True
        
        # Test without restraints
        restraint_values_free = {
            'RestraintX': False, 'RestraintY': False, 'RestraintZ': False,
            'RestraintRX': False, 'RestraintRY': False, 'RestraintRZ': False
        }
        
        def mock_getattr_free(obj, attr, default=False):
            return restraint_values_free.get(attr, default)
        
        with patch('builtins.getattr', side_effect=mock_getattr_free):
            assert self.node.is_restrained() == False
    
    def test_degrees_of_freedom_calculation(self):
        """Test DOF calculation."""
        # Fixed support (0 DOF)
        restraint_values_fixed = {
            'RestraintX': True, 'RestraintY': True, 'RestraintZ': True,
            'RestraintRX': True, 'RestraintRY': True, 'RestraintRZ': True
        }
        
        def mock_getattr_fixed(obj, attr, default=False):
            return restraint_values_fixed.get(attr, default)
        
        with patch('builtins.getattr', side_effect=mock_getattr_fixed):
            assert self.node.get_degrees_of_freedom() == 0
        
        # Pinned support (3 DOF - rotations only)
        restraint_values_pinned = {
            'RestraintX': True, 'RestraintY': True, 'RestraintZ': True,
            'RestraintRX': False, 'RestraintRY': False, 'RestraintRZ': False
        }
        
        def mock_getattr_pinned(obj, attr, default=False):
            return restraint_values_pinned.get(attr, default)
        
        with patch('builtins.getattr', side_effect=mock_getattr_pinned):
            assert self.node.get_degrees_of_freedom() == 3
        
        # Free node (6 DOF)
        restraint_values_free = {
            'RestraintX': False, 'RestraintY': False, 'RestraintZ': False,
            'RestraintRX': False, 'RestraintRY': False, 'RestraintRZ': False
        }
        
        def mock_getattr_free(obj, attr, default=False):
            return restraint_values_free.get(attr, default)
        
        with patch('builtins.getattr', side_effect=mock_getattr_free):
            assert self.node.get_degrees_of_freedom() == 6
    
    def test_position_update_triggers_visual_update(self, mock_vector):
        """Test that position changes trigger visual updates."""
        new_position = mock_vector(1000, 2000, 3000)
        
        with patch.object(self.node, '_update_visual_representation') as mock_visual:
            with patch('builtins.hasattr', return_value=True):
                self.mock_obj.Position = new_position
                self.node.onChanged(self.mock_obj, "Position")
                mock_visual.assert_called_once_with(self.mock_obj)
    
    def test_restraint_change_triggers_visual_update(self):
        """Test that restraint changes trigger visual updates."""
        with patch.object(self.node, '_update_restraint_visualization') as mock_visual:
            self.node.onChanged(self.mock_obj, "RestraintX")
            mock_visual.assert_called_once_with(self.mock_obj)
    
    def test_connection_type_update(self):
        """Test connection type property updates."""
        with patch.object(self.node, '_update_connection_properties') as mock_update:
            self.node.onChanged(self.mock_obj, "ConnectionType")
            mock_update.assert_called_once_with(self.mock_obj)
    
    def test_nodal_load_validation(self):
        """Test nodal load array validation."""
        # Set up inconsistent load arrays
        self.mock_obj.NodalLoadsX = [1000, 2000]  # 2 load cases
        self.mock_obj.NodalLoadsY = [500]  # 1 load case
        self.mock_obj.NodalLoadsZ = [0, 500, 1000]  # 3 load cases
        
        with patch('builtins.hasattr', return_value=True):
            with patch('StructureTools.objects.StructuralNode.App.Console') as mock_console:
                self.node._validate_nodal_loads(self.mock_obj)
                # Should warn about inconsistent load cases
                mock_console.PrintWarning.assert_called_once()
    
    def test_consistent_nodal_loads_no_warning(self):
        """Test that consistent load arrays don't generate warnings."""
        # Set up consistent load arrays
        self.mock_obj.NodalLoadsX = [1000, 2000, 3000]  # 3 load cases
        self.mock_obj.NodalLoadsY = [500, 1000, 1500]   # 3 load cases
        self.mock_obj.NodalLoadsZ = [0, 0, 0]           # 3 load cases
        
        with patch('builtins.hasattr', return_value=True):
            with patch('StructureTools.objects.StructuralNode.App.Console') as mock_console:
                self.node._validate_nodal_loads(self.mock_obj)
                # Should not warn
                mock_console.PrintWarning.assert_not_called()


@pytest.mark.unit 
class TestStructuralNodeVisualRepresentation:
    """Test node visual representation and symbols."""
    
    def setup_method(self):
        """Set up node for visual testing."""
        self.mock_obj = Mock()
        self.mock_obj.addProperty = Mock()
        self.node = StructuralNode(self.mock_obj)
    
    def test_restraint_symbol_creation_fixed(self, mock_vector):
        """Test restraint symbol creation for fixed support."""
        # Set up fixed support
        self.mock_obj.Position = mock_vector(0, 0, 0)
        self.mock_obj.RestraintX = True
        self.mock_obj.RestraintY = True
        self.mock_obj.RestraintZ = True
        
        def mock_getattr(obj, attr, default=False):
            if attr == 'RestraintX' or attr == 'RestraintY' or attr == 'RestraintZ':
                return True
            return default
        
        with patch('builtins.getattr', side_effect=mock_getattr):
            with patch('builtins.hasattr', return_value=True):
                with patch('StructureTools.objects.StructuralNode.Part') as mock_part:
                    symbols = self.node._create_restraint_symbols(self.mock_obj)
                    # Should create symbol for fixed support
                    assert mock_part.makeCone.called
    
    def test_restraint_symbol_creation_pinned(self, mock_vector):
        """Test restraint symbol creation for pinned support."""
        # Set up pinned support
        self.mock_obj.Position = mock_vector(0, 0, 0)
        
        def mock_getattr(obj, attr, default=False):
            restraint_values = {
                'RestraintX': True, 'RestraintY': True, 'RestraintZ': True,
                'RestraintRX': False, 'RestraintRY': False, 'RestraintRZ': False
            }
            return restraint_values.get(attr, default)
        
        with patch('builtins.getattr', side_effect=mock_getattr):
            with patch('builtins.hasattr', return_value=True):
                with patch('StructureTools.objects.StructuralNode.Part') as mock_part:
                    symbols = self.node._create_restraint_symbols(self.mock_obj)
                    # Should create symbol for pinned support
                    assert mock_part.makeCylinder.called
    
    def test_restraint_symbol_creation_roller(self, mock_vector):
        """Test restraint symbol creation for roller support."""
        # Set up roller support
        self.mock_obj.Position = mock_vector(0, 0, 0)
        
        def mock_getattr(obj, attr, default=False):
            if attr == 'RestraintZ':
                return True
            return default
        
        with patch('builtins.getattr', side_effect=mock_getattr):
            with patch('builtins.hasattr', return_value=True):
                with patch('StructureTools.objects.StructuralNode.Part') as mock_part:
                    symbols = self.node._create_restraint_symbols(self.mock_obj)
                    # Should create symbol for roller support
                    assert mock_part.makeCylinder.called


@pytest.mark.unit
class TestStructuralNodeConnections:
    """Test node connection management."""
    
    def setup_method(self):
        """Set up node for connection testing."""
        self.mock_obj = Mock()
        self.mock_obj.addProperty = Mock()
        self.node = StructuralNode(self.mock_obj)
    
    def test_connection_type_pinned_releases(self):
        """Test that pinned connection sets proper releases."""
        self.mock_obj.ConnectionType = "Pinned"
        
        with patch('builtins.hasattr', return_value=True):
            self.node._update_connection_properties(self.mock_obj)
            
            # Should set moment releases
            assert self.mock_obj.RestraintRX == False
            assert self.mock_obj.RestraintRY == False
            assert self.mock_obj.RestraintRZ == False
    
    def test_connection_type_semi_rigid_stiffness(self):
        """Test that semi-rigid connection enables stiffness input."""
        self.mock_obj.ConnectionType = "Semi-Rigid"
        
        with patch('builtins.hasattr', return_value=False):  # Property doesn't exist yet
            self.node._update_connection_properties(self.mock_obj)
            # Should set default stiffness
            assert self.mock_obj.ConnectionStiffness == 1000.0


@pytest.mark.performance
class TestStructuralNodePerformance:
    """Performance tests for StructuralNode operations."""
    
    def test_node_creation_performance(self, benchmark):
        """Benchmark node object creation time."""
        mock_obj = Mock()
        mock_obj.addProperty = Mock()
        
        def create_node():
            return StructuralNode(mock_obj)
        
        result = benchmark(create_node)
        assert result is not None
    
    def test_restraint_code_performance(self, benchmark):
        """Benchmark restraint code generation performance."""
        mock_obj = Mock()
        mock_obj.addProperty = Mock()
        node = StructuralNode(mock_obj)
        
        def mock_getattr(obj, attr, default=False):
            # Simulate mixed restraints
            restraint_values = {
                'RestraintX': True, 'RestraintY': True, 'RestraintZ': True,
                'RestraintRX': False, 'RestraintRY': False, 'RestraintRZ': False
            }
            return restraint_values.get(attr, default)
        
        with patch('builtins.getattr', side_effect=mock_getattr):
            def generate_code():
                return node.get_restraint_code()
            
            result = benchmark(generate_code)
            assert result == "111000"