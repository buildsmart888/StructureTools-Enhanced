import sys
import os

# Add the StructureTools path to sys.path
structure_tools_path = r"c:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools"
if structure_tools_path not in sys.path:
    sys.path.append(structure_tools_path)

print("Testing StructureTools Point Load Implementation")
print("=" * 50)

# Test 1: Import LoadPoint class
try:
    from freecad.StructureTools.load_point import LoadPoint
    print("✓ LoadPoint class imported successfully")
except ImportError as e:
    print(f"✗ Failed to import LoadPoint: {e}")
    sys.exit(1)

# Test 2: Check if the class has the expected attributes
try:
    # Create a mock object to test the LoadPoint class
    class MockObject:
        def __init__(self):
            self.properties = {}
            
        def addProperty(self, prop_type, name, group, desc, default=None):
            self.properties[name] = {
                'type': prop_type,
                'group': group,
                'desc': desc,
                'default': default
            }
    
    mock_obj = MockObject()
    # Create a mock selection
    mock_selection = (MockObject(), "Edge1")
    
    # Initialize LoadPoint
    load_point = LoadPoint(mock_obj, mock_selection)
    
    # Check if expected properties exist
    expected_properties = ['PointLoading', 'RelativePosition', 'LoadType', 'GlobalDirection']
    missing_properties = []
    
    for prop in expected_properties:
        if prop not in mock_obj.properties:
            missing_properties.append(prop)
    
    if not missing_properties:
        print("✓ All expected properties created successfully")
    else:
        print(f"✗ Missing properties: {missing_properties}")
        
    # Check GlobalDirection options
    print(f"  GlobalDirection options: {mock_obj.properties['GlobalDirection']['default']}")
    
except Exception as e:
    print(f"✗ Error testing LoadPoint properties: {e}")

# Test 3: Check calc.py modification
try:
    calc_file_path = os.path.join(structure_tools_path, "freecad", "StructureTools", "calc.py")
    with open(calc_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if point load processing code exists
    if "elif 'Edge' in load.ObjectBase[0][1][0] and hasattr(load, 'PointLoading'):" in content:
        print("✓ Point load processing code found in calc.py")
    else:
        print("✗ Point load processing code NOT found in calc.py")
        
except Exception as e:
    print(f"✗ Error checking calc.py: {e}")

# Test 4: Check init_gui.py modification
try:
    init_gui_file_path = os.path.join(structure_tools_path, "freecad", "StructureTools", "init_gui.py")
    with open(init_gui_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if load_point import exists
    if "from freecad.StructureTools import load_point" in content:
        print("✓ load_point import found in init_gui.py")
    else:
        print("✗ load_point import NOT found in init_gui.py")
        
    # Check if load_point command is registered in toolbar
    if '"load_point"' in content:
        print("✓ load_point command registered in init_gui.py")
    else:
        print("✗ load_point command NOT registered in init_gui.py")
        
except Exception as e:
    print(f"✗ Error checking init_gui.py: {e}")

# Test 5: Check icon file
try:
    icon_file_path = os.path.join(structure_tools_path, "freecad", "StructureTools", "resources", "icons", "load_point.svg")
    if os.path.exists(icon_file_path):
        print("✓ load_point.svg icon file exists")
    else:
        print("✗ load_point.svg icon file NOT found")
except Exception as e:
    print(f"✗ Error checking icon file: {e}")

print("=" * 50)
print("Testing completed!")