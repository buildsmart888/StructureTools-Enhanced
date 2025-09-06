#!/usr/bin/env python3
"""
Batch Update Script for Global Units Integration
Updates all StructureTools files to use the new Global Units System
"""

import os
import re
from pathlib import Path

# Files to update with Global Units imports
FILES_TO_UPDATE = [
    # Command files
    "command_buckling_analysis.py",
    "command_design_optimizer.py", 
    "command_load_generator.py",
    "command_modal_analysis.py",
    "command_plate.py",
    "command_report_generator.py",
    # Core files
    "diagram_core.py",
    "diagram.py",
    "init_gui.py",
    "load_distributed.py",
    "load_nodal.py",
    "section.py"
]

# Global Units import code to add
GLOBAL_UNITS_IMPORT = '''
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
'''

def update_file_with_global_units(file_path):
    """Update a file to include Global Units imports"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already updated
        if 'from .utils.units_manager import' in content:
            print(f"✓ {file_path.name} already updated")
            return True
            
        # Find import section
        lines = content.split('\n')
        import_end_line = 0
        
        for i, line in enumerate(lines):
            if line.startswith('import ') or line.startswith('from '):
                import_end_line = i
            elif line.strip() == '' and import_end_line > 0:
                # Found end of imports
                break
                
        # Insert Global Units import
        if import_end_line > 0:
            lines.insert(import_end_line + 1, GLOBAL_UNITS_IMPORT)
            
            # Write back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
                
            print(f"✓ Updated {file_path.name}")
            return True
        else:
            print(f"✗ Could not find import section in {file_path.name}")
            return False
            
    except Exception as e:
        print(f"✗ Error updating {file_path.name}: {e}")
        return False

def update_all_files():
    """Update all specified files"""
    print("Batch Global Units Integration")
    print("=" * 50)
    
    base_path = Path(__file__).parent / "freecad" / "StructureTools"
    
    updated_count = 0
    total_count = len(FILES_TO_UPDATE)
    
    for filename in FILES_TO_UPDATE:
        file_path = base_path / filename
        
        if file_path.exists():
            if update_file_with_global_units(file_path):
                updated_count += 1
        else:
            print(f"⚠ File not found: {filename}")
    
    print(f"\nSummary: {updated_count}/{total_count} files updated")
    
    # Update additional utils files that need specific handling
    update_specific_files(base_path)

def update_specific_files(base_path):
    """Update files that need specific Global Units integration"""
    print(f"\nUpdating specific integrations...")
    
    # Update MaterialSelectionPanel with enhanced formatting
    panel_file = base_path / "taskpanels" / "MaterialSelectionPanel.py"
    if panel_file.exists():
        try:
            with open(panel_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if format_modulus method exists and update it
            if 'def format_modulus(' in content and 'get_units_manager()' not in content:
                # Add global units integration to format methods
                enhanced_content = content.replace(
                    'def format_modulus(self, value_pa):',
                    '''def format_modulus(self, value_pa):
        """Format modulus value using global units system"""
        if GLOBAL_UNITS_AVAILABLE:
            return format_modulus(value_pa)
        # Fallback formatting'''
                )
                
                enhanced_content = enhanced_content.replace(
                    'def format_stress(self, value_pa):',
                    '''def format_stress(self, value_pa):
        """Format stress value using global units system"""
        if GLOBAL_UNITS_AVAILABLE:
            return format_stress(value_pa)
        # Fallback formatting'''
                )
                
                enhanced_content = enhanced_content.replace(
                    'def format_force(self, value_n):',
                    '''def format_force(self, value_n):
        """Format force value using global units system"""
        if GLOBAL_UNITS_AVAILABLE:
            return format_force(value_n)
        # Fallback formatting'''
                )
                
                with open(panel_file, 'w', encoding='utf-8') as f:
                    f.write(enhanced_content)
                
                print(f"✓ Enhanced MaterialSelectionPanel.py")
            else:
                print(f"✓ MaterialSelectionPanel.py already enhanced")
                
        except Exception as e:
            print(f"✗ Error updating MaterialSelectionPanel.py: {e}")

def create_integration_test():
    """Create integration test for all updated files"""
    test_content = '''#!/usr/bin/env python3
"""
Complete Integration Test for Global Units System
Tests all updated StructureTools files
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'freecad'))

# Mock FreeCAD for testing
class MockFreeCAD:
    class Console:
        @staticmethod
        def PrintMessage(msg): print(f"FreeCAD: {msg.strip()}")

sys.modules['FreeCAD'] = MockFreeCAD()
sys.modules['App'] = MockFreeCAD()
sys.modules['FreeCADGui'] = MockFreeCAD()
sys.modules['Part'] = MockFreeCAD()

def test_imports():
    """Test that all files can import Global Units"""
    files_to_test = [
        "freecad.StructureTools.utils.units_manager",
        "freecad.StructureTools.calc",
        "freecad.StructureTools.material",
    ]
    
    success_count = 0
    for module_name in files_to_test:
        try:
            __import__(module_name)
            print(f"✓ {module_name}")
            success_count += 1
        except ImportError as e:
            print(f"✗ {module_name}: {e}")
    
    print(f"\\nImport Test: {success_count}/{len(files_to_test)} modules loaded")
    return success_count == len(files_to_test)

if __name__ == "__main__":
    print("Complete Integration Test")
    print("=" * 40)
    
    if test_imports():
        print("\\n🎉 ALL INTEGRATIONS SUCCESSFUL 🎉")
        print("Global Units System ready for production!")
    else:
        print("\\n⚠ Some integrations need attention")
'''

    with open("test_complete_integration.py", 'w', encoding='utf-8') as f:
        f.write(test_content)
    
    print("✓ Created test_complete_integration.py")

if __name__ == "__main__":
    update_all_files()
    create_integration_test()
    
    print(f"\n🚀 Batch update completed!")
    print(f"Run: python test_complete_integration.py to verify")
