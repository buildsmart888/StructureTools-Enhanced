import os
import shutil

# Replace original files with clean versions
shutil.copy(r'c:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\freecad\StructureTools\objects\AreaLoad_clean.py', 
            r'c:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\freecad\StructureTools\objects\AreaLoad.py')

shutil.copy(r'c:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\freecad\StructureTools\objects\StructuralPlate_clean.py', 
            r'c:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\freecad\StructureTools\objects\StructuralPlate.py')

print("Files replaced with clean versions successfully")