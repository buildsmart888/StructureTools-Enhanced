import ast

# Read the file
with open('c:/Users/thani/AppData/Roaming/FreecAD/Mod/StructureTools/freecad/StructureTools/commands/command_seismic_load_gui.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Parse the AST
tree = ast.parse(content)

# Find the SeismicLoadGUI class
classes = [node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == 'SeismicLoadGUI']
print('Found SeismicLoadGUI class:', len(classes) > 0)

if classes:
    seismic_class = classes[0]
    methods = [item for item in seismic_class.body if isinstance(item, ast.FunctionDef)]
    method_names = [method.name for method in methods]
    print('Methods in SeismicLoadGUI class:')
    for name in method_names:
        print(f'  {name}')
    print('Has connect_signals:', 'connect_signals' in method_names)
else:
    print('SeismicLoadGUI class not found')