# -*- coding: utf-8 -*-
"""
StructureTools Utilities Package

This package contains utility modules for various StructureTools functionality.
"""

# Make MaterialHelper available at package level
try:
    from .MaterialHelper import (
        create_material_from_database,
        get_calc_properties_from_database,
        list_available_standards,
        list_standards_by_category,
        search_materials,
        validate_material_properties,
        update_material_from_database,
        create_steel_a992,
        create_steel_a36,
        create_concrete_25mpa,
        create_concrete_30mpa
    )
except ImportError:
    pass
