import os
import shutil

# Backup original files
shutil.copy(r'c:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\freecad\StructureTools\objects\AreaLoad.py', 
            r'c:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\freecad\StructureTools\objects\AreaLoad.py.bak2')

shutil.copy(r'c:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\freecad\StructureTools\objects\StructuralPlate.py', 
            r'c:\Users\thani\AppData\Roaming\FreeCAD\Mod\StructureTools\freecad\StructureTools\objects\StructuralPlate.py.bak2')

print("Backup completed successfully")