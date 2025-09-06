import FreeCAD, App, FreeCADGui, Part, os
from PySide import QtWidgets

# Import Thai units support
try:
    from .utils.universal_thai_units import enhance_with_thai_units, thai_material_units
    THAI_UNITS_AVAILABLE = True
except ImportError:
    THAI_UNITS_AVAILABLE = False
    enhance_with_thai_units = lambda x, t: x
    thai_material_units = lambda f: f

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")

def show_error_message(msg):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setIcon(QtWidgets.QMessageBox.Critical)  # Ícone de erro
    msg_box.setWindowTitle("Erro")
    msg_box.setText(msg)
    msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg_box.exec_()




class CommandMember():
    """My new command"""

    def GetResources(self):
        return {"Pixmap"  : os.path.join(ICONPATH, "icons/member.svg"), # the name of a svg file available in the resources
                "Accel"   : "Shift+D", # a default shortcut (optional)
                "MenuText": "Define Member",
                "ToolTip" : "Defines the members of the structure"}

    def Activated(self):
        selections = FreeCADGui.Selection.getSelection()
        selection = list(filter(lambda element: 'Wire' in element.Name or 'Line' in element.Name, selections ))
             
        for selection in selections:
            selection.addProperty('App::PropertyLink', 'MaterialMember', 'Structure','Member material')
            selection.addProperty('App::PropertyLink', 'SectionMember', 'Structure','Member section')
            selection.addProperty('App::PropertyAngle', 'RotationSection', 'Structure','Member section rotation')
            selection.addProperty('App::PropertyBool', 'TrussMember', 'Structure','Define como membro de treliça').TrussMember = False
        FreeCAD.ActiveDocument.recompute()        

        return

    def IsActive(self):
        
        return True

FreeCADGui.addCommand("member", CommandMember())
