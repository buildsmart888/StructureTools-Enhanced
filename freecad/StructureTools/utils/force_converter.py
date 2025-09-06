# -*- coding: utf-8 -*-
"""
Enhanced Force Unit Converter for StructureTools

This module provides comprehensive force unit conversion capabilities
supporting SI, MKS, and US Customary systems with high precision.

Units Supported:
  SI: 'N', 'kN', 'MN'
  MKS: 'kgf', 'tf' (metric ton-force)
  US: 'lbf', 'kip', 'tonf_us' (short ton-force)

Conversion Factors to Newton (N):
  1 N = 1 N
  1 kN = 1,000 N
  1 MN = 1,000,000 N
  1 kgf = 9.80665 N
  1 tf = 9,806.65 N
  1 lbf = 4.4482216152605 N
  1 kip = 4,448.2216152605 N
  1 tonf_us = 8,896.443230521 N
"""

import math
from typing import Union, Dict, List, Tuple

# Conversion factors to Newton (N) with high precision
FORCE_CONVERSION_FACTORS = {
    # SI System
    "N": 1.0,                    # Newton
    "kN": 1_000.0,               # Kilonewton
    "MN": 1_000_000.0,           # Meganewton
    
    # MKS System (Metric)
    "kgf": 9.80665,              # Kilogram-force
    "tf": 9_806.65,              # Metric ton-force (tonne-force)
    
    # US Customary System
    "lbf": 4.4482216152605,      # Pound-force (exact conversion)
    "kip": 4_448.2216152605,     # Kilopound-force (exact conversion)
    "tonf_us": 8_896.443230521,  # Short ton-force (US ton-force, exact conversion)
}

# Unit system categories
UNIT_SYSTEMS = {
    "SI": {
        "name": "International System (SI)",
        "description": "Newton-based system used internationally",
        "units": ["N", "kN", "MN"],
        "base_unit": "N"
    },
    "MKS": {
        "name": "Meter-Kilogram-Second System",
        "description": "Metric system using kilogram-force as base",
        "units": ["kgf", "tf"],
        "base_unit": "kgf"
    },
    "US": {
        "name": "US Customary System",
        "description": "Imperial system used in the United States",
        "units": ["lbf", "kip", "tonf_us"],
        "base_unit": "lbf"
    }
}

# Common engineering unit combinations
ENGINEERING_UNITS = {
    "structural": {
        "SI": "kN",
        "MKS": "tf", 
        "US": "kip"
    },
    "detailed": {
        "SI": "N",
        "MKS": "kgf",
        "US": "lbf"
    }
}


class ForceConverter:
    """Enhanced force unit converter with multiple system support"""
    
    def __init__(self):
        """Initialize the force converter"""
        self.conversion_factors = FORCE_CONVERSION_FACTORS.copy()
        self.unit_systems = UNIT_SYSTEMS.copy()
        self.engineering_units = ENGINEERING_UNITS.copy()
    
    def convert(self, value: Union[float, int], from_unit: str, to_unit: str) -> float:
        """
        Convert force value from one unit to another
        
        Args:
            value: Force value to convert
            from_unit: Source unit (e.g., 'kN', 'kgf', 'kip')
            to_unit: Target unit (e.g., 'lbf', 'tf', 'N')
            
        Returns:
            float: Converted force value
            
        Raises:
            ValueError: If units are not supported
        """
        # Validate units
        if from_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported source unit: {from_unit}")
        if to_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported target unit: {to_unit}")
        
        # Direct conversion: value -> Newton -> target unit
        value_in_newtons = value * self.conversion_factors[from_unit]
        converted_value = value_in_newtons / self.conversion_factors[to_unit]
        
        return converted_value
    
    def convert_multiple(self, values: List[Union[float, int]], from_unit: str, to_unit: str) -> List[float]:
        """
        Convert multiple force values from one unit to another
        
        Args:
            values: List of force values to convert
            from_unit: Source unit
            to_unit: Target unit
            
        Returns:
            List[float]: List of converted force values
        """
        return [self.convert(value, from_unit, to_unit) for value in values]
    
    def get_system_info(self, system: str) -> Dict:
        """
        Get information about a unit system
        
        Args:
            system: System name ('SI', 'MKS', 'US')
            
        Returns:
            Dict: System information
        """
        if system not in self.unit_systems:
            raise ValueError(f"Unsupported system: {system}")
        return self.unit_systems[system]
    
    def get_engineering_unit(self, system: str, precision: str = "structural") -> str:
        """
        Get recommended engineering unit for a system
        
        Args:
            system: System name ('SI', 'MKS', 'US')
            precision: Precision level ('structural' or 'detailed')
            
        Returns:
            str: Recommended unit for the system
        """
        if system not in self.engineering_units.get(precision, {}):
            raise ValueError(f"Unsupported system or precision: {system}, {precision}")
        return self.engineering_units[precision][system]
    
    def format_value(self, value: float, unit: str, precision: int = 2, show_unit: bool = True) -> str:
        """
        Format a force value with proper precision and unit
        
        Args:
            value: Force value
            unit: Unit to display
            precision: Number of decimal places
            show_unit: Whether to include unit in output
            
        Returns:
            str: Formatted force value
        """
        formatted_value = f"{value:.{precision}f}"
        if show_unit:
            formatted_value += f" {unit}"
        return formatted_value
    
    def auto_convert(self, value: float, from_unit: str, target_system: str) -> Tuple[float, str]:
        """
        Automatically convert to the most appropriate unit in the target system
        
        Args:
            value: Force value to convert
            from_unit: Source unit
            target_system: Target system ('SI', 'MKS', 'US')
            
        Returns:
            Tuple[float, str]: (converted_value, target_unit)
        """
        # Get the recommended engineering unit for the target system
        target_unit = self.get_engineering_unit(target_system)
        
        # Convert to that unit
        converted_value = self.convert(value, from_unit, target_unit)
        
        return converted_value, target_unit
    
    def get_conversion_table(self) -> Dict[str, Dict[str, float]]:
        """
        Generate a comprehensive conversion table
        
        Returns:
            Dict: Conversion table with all units as both source and target
        """
        table = {}
        units = list(self.conversion_factors.keys())
        
        # Create conversion table: source_unit -> {target_unit: factor}
        for source_unit in units:
            table[source_unit] = {}
            for target_unit in units:
                if source_unit == target_unit:
                    table[source_unit][target_unit] = 1.0
                else:
                    # Calculate conversion factor: source -> N -> target
                    factor = self.conversion_factors[source_unit] / self.conversion_factors[target_unit]
                    table[source_unit][target_unit] = factor
                    
        return table
    
    def get_common_conversions(self, value: float, from_unit: str) -> Dict[str, str]:
        """
        Get common conversions for a value in a convenient format
        
        Args:
            value: Force value to convert
            from_unit: Source unit
            
        Returns:
            Dict[str, str]: Dictionary of common conversions with formatted strings
        """
        conversions = {}
        
        # Convert to all units
        for unit in self.conversion_factors:
            if unit != from_unit:
                converted = self.convert(value, from_unit, unit)
                # Format with appropriate precision based on magnitude
                if abs(converted) >= 1000:
                    precision = 2
                elif abs(converted) >= 10:
                    precision = 2
                elif abs(converted) >= 1:
                    precision = 3
                else:
                    precision = 4
                conversions[unit] = self.format_value(converted, unit, precision)
                
        return conversions


# Global instance
_force_converter = None

def get_force_converter() -> ForceConverter:
    """Get global force converter instance"""
    global _force_converter
    if _force_converter is None:
        _force_converter = ForceConverter()
    return _force_converter


def convert_force(value: Union[float, int], from_unit: str, to_unit: str) -> float:
    """
    Convert force units between SI, MKS, and US customary systems.
    
    Units supported:
      SI: 'N', 'kN', 'MN'
      MKS: 'kgf', 'tf'
      US: 'lbf', 'kip', 'tonf_us'
      
    Args:
        value: Force value to convert
        from_unit: Source unit
        to_unit: Target unit
        
    Returns:
        float: Converted force value
        
    Examples:
        >>> convert_force(1, "kip", "kN")
        4.4482216152605
        >>> convert_force(1000, "N", "kgf") 
        101.97162129779284
        >>> convert_force(1, "tf", "kip")
        2.2046226218487757
    """
    converter = get_force_converter()
    return converter.convert(value, from_unit, to_unit)


def get_force_system_info(system: str) -> Dict:
    """
    Get information about a force unit system
    
    Args:
        system: System name ('SI', 'MKS', 'US')
        
    Returns:
        Dict: System information
    """
    converter = get_force_converter()
    return converter.get_system_info(system)


def format_force_value(value: float, unit: str, precision: int = 2) -> str:
    """
    Format a force value with unit
    
    Args:
        value: Force value
        unit: Unit to display
        precision: Number of decimal places
        
    Returns:
        str: Formatted force value with unit
    """
    converter = get_force_converter()
    return converter.format_value(value, unit, precision)


def get_common_force_conversions(value: float, from_unit: str) -> Dict[str, str]:
    """
    Get common force conversions for a value
    
    Args:
        value: Force value to convert
        from_unit: Source unit
        
    Returns:
        Dict[str, str]: Dictionary of formatted conversions
    """
    converter = get_force_converter()
    return converter.get_common_conversions(value, from_unit)


# Example usage and testing
if __name__ == "__main__":
    # Test basic conversion
    print("=== Force Unit Conversion Examples ===")
    print(f"1 kip = {convert_force(1, 'kip', 'kN'):.5f} kN")
    print(f"1000 N = {convert_force(1000, 'N', 'kgf'):.5f} kgf")
    print(f"1 tf = {convert_force(1, 'tf', 'kip'):.5f} kip")
    
    # Test common conversions
    print("\n=== Common Conversions for 1 kip ===")
    conversions = get_common_force_conversions(1, "kip")
    for unit, formatted in conversions.items():
        print(f"1 kip = {formatted}")
    
    # Test system information
    print("\n=== System Information ===")
    for system in ["SI", "MKS", "US"]:
        info = get_force_system_info(system)
        print(f"{system}: {info['name']} - {info['description']}")