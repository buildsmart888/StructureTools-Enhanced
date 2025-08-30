# Utility functions for calc.py

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
                quantity_str = f"{value} {from_unit}"
                quantity = FreeCAD.Units.Quantity(quantity_str)
            elif hasattr(value, 'getValueAs'):
                # It's already a Quantity object
                quantity = value
            else:
                # Try to convert string or other types
                quantity = FreeCAD.Units.Quantity(str(value))
            
            if to_unit:
                # Convert to target unit
                converted_value = quantity.getValueAs(to_unit)
                return float(converted_value)
            return float(quantity.Value)
    except Exception:
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


def _find_matching_node_index(nodes_map, target_node, tol=1e-6):
    """Find index of node in nodes_map that matches target_node within tolerance"""
    import math
    for i, node in enumerate(nodes_map):
        # Calculate Euclidean distance between nodes
        dist = math.sqrt(sum((a - b)**2 for a, b in zip(node, target_node)))
        if dist < tol:
            return i
    return None