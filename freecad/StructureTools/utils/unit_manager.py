
import FreeCAD as App

class UnitManager:
    """
    Centralized unit conversion and management.
    Handles FreeCAD Quantity conversions safely.
    """

    @staticmethod
    def get_quantity_value(value, from_unit=None, to_unit=None):
        """
        Convert a value (number or Quantity) to a float in target units.
        
        Args:
            value: The input value. Can be float, int, string (with units), or FreeCAD.Units.Quantity.
            from_unit (str, optional): The unit of the input value if it is a raw number (e.g. 'mm').
            to_unit (str, optional): The target unit to convert to (e.g. 'm').
            
        Returns:
            float: The numeric value in target unit. Returns default (e.g. float(value)) if conversion fails.
        """
        # If value is already a Quantity object
        if hasattr(value, 'getValueAs'): 
            if to_unit:
                try:
                    return float(value.getValueAs(to_unit))
                except Exception:
                    pass
            # If no target unit or conversion failed, try getting value as float
            # Often Quantity().Value is base unit value
            try:
                return float(value.Value)
            except:
                pass

        # If standard FreeCAD Units module is available
        if hasattr(App, 'Units') and hasattr(App.Units, 'Quantity'):
            try:
                # If we have a from_unit, treat as quantity
                if from_unit and not isinstance(value, str):
                    qty = App.Units.Quantity(value, from_unit)
                else:
                    # Try to parse string or raw value
                    qty = App.Units.Quantity(value)
                
                if to_unit:
                     return float(qty.getValueAs(to_unit))
                return float(qty.Value)
            except Exception:
                pass
        
        # Fallback: just try to float it
        try:
            return float(value)
        except:
            return 0.0

    @staticmethod
    def convert(value, to_unit):
        """Simple alias for converting any quantity-like to a specific unit."""
        return UnitManager.get_quantity_value(value, to_unit=to_unit)
