import FreeCAD, FreeCADGui, Part, math, os, logging

# Prefer PySide2 when available
try:
	from PySide2 import QtWidgets
except Exception:
	from PySide import QtWidgets

from .diagram_core import (
	separates_ordinates as core_separates_ordinates,
	generate_coordinates as core_generate_coordinates,
	normalize_loop_for_face,
	make_member_diagram_coords,
	compose_face_loops,
	get_label_positions,
)

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ICONPATH = os.path.join(os.path.dirname(__file__), "resources")
pathFont = os.path.join(os.path.dirname(__file__), "resources/fonts/ARIAL.TTF")
# pathFont = os.path.join(os.path.dirname(__file__), "ARIAL.TTF")

def show_error_message(msg):
	msg_box = QtWidgets.QMessageBox()
	msg_box.setIcon(QtWidgets.QMessageBox.Critical)  #Ícone de erro
	msg_box.setWindowTitle("Erro")
	msg_box.setText(msg)
	msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
	msg_box.exec_()

class Diagram:
	def __init__(self, obj, objCalc, listSelection):
		#Gera a lista de membros selecionados
		


		obj.Proxy = self
		obj.addProperty("App::PropertyLink", "ObjectBaseCalc", "Base", "elementos para a analise").ObjectBaseCalc = objCalc
		obj.addProperty("App::PropertyLinkSubList", "ObjectBaseElements", "Base", "elementos para a analise").ObjectBaseElements = self.getMembers(listSelection)
		

		obj.addProperty("App::PropertyColor", "Color", "Diagram", "elementos para a analise").Color = (255,0,0,0)
		obj.addProperty("App::PropertyInteger", "Transparency", "Diagram", "elementos para a analise").Transparency = 70		
		obj.addProperty("App::PropertyInteger", "FontHeight", "Diagram", "Tamanho da fonte no diagrama").FontHeight = 100
		obj.addProperty("App::PropertyInteger", "Precision", "Diagram", "precisão de casas decimais").Precision = 2
		obj.addProperty("App::PropertyBool", "DrawText", "Diagram", "precisão de casas decimais").DrawText = True

		obj.addProperty("App::PropertyBool", "MomentZ", "DiagramMoment", "Ver diagrama de momento em Z").MomentZ = False
		obj.addProperty("App::PropertyBool", "MomentY", "DiagramMoment", "Ver diagrama de momento em Y").MomentY = False
		obj.addProperty("App::PropertyFloat", "ScaleMoment", "DiagramMoment", "Escala dos diagramas de momento").ScaleMoment = 1


		obj.addProperty("App::PropertyBool", "ShearZ", "DiagramShear", "Ver diagrama de cortante em Z").ShearZ = False
		obj.addProperty("App::PropertyBool", "ShearY", "DiagramShear", "Ver diagrama de cortante em Y").ShearY = False
		obj.addProperty("App::PropertyFloat", "ScaleShear", "DiagramShear", "Escala dos diagramas de cortante").ScaleShear = 1
		
		obj.addProperty("App::PropertyBool", "Torque", "DiagramTorque", "Ver diagrama de torque").Torque = False
		obj.addProperty("App::PropertyFloat", "ScaleTorque", "DiagramTorque", "Escala do diagrama de torque").ScaleTorque = 1

		obj.addProperty("App::PropertyBool", "AxialForce", "DiagramAxial", "Ver diagrama de força normal").AxialForce = False
		obj.addProperty("App::PropertyFloat", "ScaleAxial", "DiagramAxial", "Escala do diagrama de força normal").ScaleAxial = 1
	


	# Pega os membros que deverão se plotados os seus diagramas
	def getMembers(self, listSelection):
		listMembers = []

		if listSelection != []: # Caso exista selecção de membros
			for selection in listSelection:
				member = (selection.Object, selection.SubElementNames)
				listMembers.append(member)
		
		else: #Caso não exista seleção de membros todos eles serão selecionados automaticamente
			objects = FreeCAD.ActiveDocument.Objects
			lines = list(filter(lambda object: 'Wire' in object.Name or 'Line' in object.Name, objects))
			members = list(filter(lambda line: 'MaterialMember' in line.PropertiesList, lines))

			for member in members:
				listSubObjects = [f'Edge{i+1}' for i in range(len(member.Shape.Edges))]
				listMembers.append((member, listSubObjects))
		
		return listMembers

	# Gera uma matriz baseado em umdos parâmetros do calc
	def getMatrix(self, param):
		matriz = []
		for linha in param:
			lista = [float(value) for value in linha.split(',')]
			matriz.append(lista)
		
		return matriz


	#  Mapeia os nós da estrutura
	def mapNodes(self, elements, tol: float = 1e-3):
		"""Map nodes with a tolerance to allow nearby points to merge.

		This function is numeric-only and does not depend on FreeCAD internals
		beyond accessing vertex coordinates.
		"""
		listNodes = []
		for element in elements:
			for edge in element.Shape.Edges:
				for vertex in edge.Vertexes:
					pt = (vertex.Point.x, vertex.Point.y, vertex.Point.z)
					# search for existing within tolerance
					found = False
					for existing in listNodes:
						if abs(existing[0] - pt[0]) <= tol and abs(existing[1] - pt[1]) <= tol and abs(existing[2] - pt[2]) <= tol:
							found = True
							break
					if not found:
						listNodes.append([round(pt[0], 2), round(pt[1], 2), round(pt[2], 2)])

		return listNodes


	# Mapeia os membros da estrutura
	def mapMembers(self, elements, listNodes):
		listMembers = {}
		for element in elements:
			for i, edge in enumerate(element.Shape.Edges):
				listIndexVertex = []
				for vertex in edge.Vertexes:
					node = [round(vertex.Point.x, 2), round(vertex.Point.y, 2), round(vertex.Point.z, 2)]
					index = listNodes.index(node)
					listIndexVertex.append(index)
				# valida se o primeiro nó é mais auto do que o segundo nó, se sim inverte os nós do membro (necessário para manter os diagramas voltados para a posição correta)
				n1 = listIndexVertex[0]
				n2 = listIndexVertex[1]
				if listNodes[n1][2] > listNodes[n2][2]:
					aux = n1
					n1 = n2
					n2 = aux
				listMembers[element.Name + '_' + str(i)] = {
					'nodes': [str(n1), str(n2)],
					'RotationSection': element.RotationSection.getValueAs('rad')
				}
		
		return listMembers
	
	# separa as ordenadas em grupos de valores positivos e negativos
	def separatesOrdinates(self, values):
		# delegate to pure-python core
		return core_separates_ordinates(values)


	# Função que cria os pares de coordenadas e já cria os valores que cruzam o eixo das absissas
	def generateCoordinates(self, ordinates, dist):
		# delegate to core implementation
		return core_generate_coordinates(ordinates, dist)
	

	# Gera as faces
	def generateFaces(self, loops):
		faces = []
		# normalize and filter degenerate loops before creating faces
		for loop in compose_face_loops(loops):
			vecs = [FreeCAD.Vector(value[0], 0, value[1]) for value in loop]

			edges = [Part.LineSegment(vecs[i], vecs[i+1]).toShape() for i in range(len(vecs)-1)]
			wire = Part.Wire(edges)
			face = Part.Face(wire)
			if face.Area > 0:
				faces.append(face)

		return faces
	
	# Faz a rotação do  diagrama na direção passada como argumento e o posiciona
	def rotate(self, element, dirStart, dirEnd, position = FreeCAD.Vector(0,0,0.1)):
		try:
			dirStart.normalize()
			dirEnd.normalize()

			if dirStart == dirEnd:
				return element.translate(position)       
			
			rotacao = FreeCAD.Rotation(dirStart, dirEnd)
			elementoRotacionado = element.transformGeometry(FreeCAD.Placement(position,rotacao).toMatrix())
			return elementoRotacionado
		except:
			print('Erro ao rotacionar diagrama.')
			return element
	
	# Gero os valores nos diagramas
	def makeText(self, values, listMatrix, dist, fontHeight, precision):
		"""Compatibility wrapper: compute label specs then create Part wires.

		This method keeps the original signature for callers that still pass
		(values, listMatrix, ...). Internally it delegates to
		`get_label_positions` and `makeTextFromSpecs`.
		"""
		labels = get_label_positions(values, listMatrix, dist, fontHeight, precision)
		return self.makeTextFromSpecs(labels, fontHeight)

	def makeTextFromSpecs(self, labels, fontHeight):
		"""Create Part wires for precomputed labels.

		labels: list of tuples (string, x, y)
		fontHeight: font size passed to Part.makeWireString
		Returns list of wire shapes.
		"""
		listWire = []
		for string, x, y in labels:
			text = Part.makeWireString(string, pathFont, fontHeight)
			for wires in text:
				for wire in wires:
					# rotate text to lie in X-Z plane and translate to position
					try:
						wire = wire.rotated(FreeCAD.Vector(0,0,0), FreeCAD.Vector(1,0,0), 90)
						wire = wire.translate(FreeCAD.Vector(x, 0, y))
					except Exception:
						# If wire objects are simple mocks in tests, allow no-op
						pass
					listWire.append(wire)
		return listWire


	# Gera o diagrama da matriz passada como argumento
	def makeDiagram(self, matrix,nodes, members, orderMembers, nPoints, rotacao, escale, fontHeight, precision, drawText):
		
		# e = 1e-11
		listDiagram = []
		for i, nameMember in orderMembers:
			p1 = nodes[int(members[nameMember]['nodes'][0])]
			p2 = nodes[int(members[nameMember]['nodes'][1])]
			length = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)**0.5
			dist = length / (nPoints -1) #Distancia entre os pontos no eixo X
			values = [value * escale for value in matrix[i]]

			coordinates, values_scaled = make_member_diagram_coords(matrix[i], dist, escale)
			faces = self.generateFaces(coordinates)
			# compute text labels/positions using core helper, then make wires
			labels = get_label_positions(values_scaled, matrix[i], dist, fontHeight, precision)
			# makeText still converts labels to Part wires; keep API
			texts = self.makeText(values_scaled, matrix[i], dist, fontHeight, precision)
			
			# Posiciona o diagrama
			dx = p2[0] - p1[0]
			dy = p2[1] - p1[1]
			dz = p2[2] - p1[2]
			element = Part.makeCompound(faces)
			if drawText: element = Part.makeCompound([element] + texts) 

			rot = FreeCAD.Rotation(FreeCAD.Vector(1,0,0), rotacao)
			element.Placement = FreeCAD.Placement(FreeCAD.Vector(0,0,0), rot)
			element = self.rotate(element, FreeCAD.Vector(1,0,0), FreeCAD.Vector(abs(dx), abs(dy), abs(dz)))

			if dx < 0 :
				element = element.mirror(FreeCAD.Vector(0,0,0), FreeCAD.Vector(1,0,0))
			
			if dy < 0 :
				element = element.mirror(FreeCAD.Vector(0,0,0), FreeCAD.Vector(0,1,0))

			
			element = element.translate(FreeCAD.Vector(p1[0], p1[1], p1[2]))
			
			listDiagram.append(element)
			# Part.show(element)
			# Part.show(Part.makeCompound(faces))
			# for face in faces:
			#     Part.show(Part.makeCompound(faces))
		
		return listDiagram

	def filterMembersSelected(self, obj):
		if obj.ObjectBaseElements == []: # se não existir objetos celecionados retorna to d a alista de objetos
			return list(enumerate(obj.ObjectBaseCalc.NameMembers))
		
		else: # caso haja objetos celecionados faz o filtro no nome destes objetos
			listaNames = []
			for element in obj.ObjectBaseElements:
				listMemberNames = [int(name.split('Edge')[1])-1 for name in element[1]]
				for memberName in listMemberNames:
					name = element[0].Name +'_'+ str(memberName)
					memberIndex = obj.ObjectBaseCalc.NameMembers.index(name)
					listaNames.append((memberIndex, name))
			
			return listaNames




	def execute(self, obj):
		elements = list(filter(lambda element: 'Line' in element.Name or 'Wire' in element.Name,  obj.ObjectBaseCalc.ListElements))
		nodes = self.mapNodes(elements)
		members = self.mapMembers(elements, nodes)
		orderMembers = self.filterMembersSelected(obj)

		listDiagram = []
		if obj.MomentZ:
			listDiagram += self.makeDiagram(self.getMatrix(obj.ObjectBaseCalc.MomentZ),nodes, members, orderMembers, obj.ObjectBaseCalc.NumPointsMoment, 0, obj.ScaleMoment, obj.FontHeight, obj.Precision, obj.DrawText)
		
		if obj.MomentY:
			listDiagram += self.makeDiagram(self.getMatrix(obj.ObjectBaseCalc.MomentY),nodes, members, orderMembers, obj.ObjectBaseCalc.NumPointsMoment, 90, obj.ScaleMoment, obj.FontHeight, obj.Precision, obj.DrawText)
		
		if obj.ShearY:
			listDiagram += self.makeDiagram(self.getMatrix(obj.ObjectBaseCalc.ShearY),nodes, members, orderMembers, obj.ObjectBaseCalc.NumPointsShear, 0, obj.ScaleShear, obj.FontHeight, obj.Precision, obj.DrawText)

		if obj.ShearZ:
			listDiagram += self.makeDiagram(self.getMatrix(obj.ObjectBaseCalc.ShearZ),nodes, members, orderMembers, obj.ObjectBaseCalc.NumPointsShear, 90, obj.ScaleShear, obj.FontHeight, obj.Precision, obj.DrawText)
		
		if obj.Torque:
			listDiagram += self.makeDiagram(self.getMatrix(obj.ObjectBaseCalc.Torque),nodes, members, orderMembers, obj.ObjectBaseCalc.NumPointsTorque, 0, obj.ScaleTorque, obj.FontHeight, obj.Precision, obj.DrawText)
		
		if obj.AxialForce:
			listDiagram += self.makeDiagram(self.getMatrix(obj.ObjectBaseCalc.AxialForce),nodes, members, orderMembers, obj.ObjectBaseCalc.NumPointsAxial, 0, obj.ScaleAxial, obj.FontHeight, obj.Precision, obj.DrawText)
		
		if not listDiagram:
			shape = Part.Shape()
		else:	
			shape = Part.makeCompound(listDiagram)

		obj.Shape = shape

		# Estilização
		obj.ViewObject.LineWidth = 1
		obj.ViewObject.PointSize = 1
		obj.ViewObject.LineColor = (int(obj.Color[0]*255),int(obj.Color[1]*255),int(obj.Color[2]*255))
		obj.ViewObject.PointColor = (int(obj.Color[0]*255),int(obj.Color[1]*255),int(obj.Color[2]*255))
		obj.ViewObject.ShapeAppearance = (FreeCAD.Material(DiffuseColor=obj.Color,AmbientColor=(0.33,0.33,0.33),SpecularColor=(0.53,0.53,0.53),EmissiveColor=(0.00,0.00,0.00),Shininess=(0.90),Transparency=(0.00),))
		obj.ViewObject.Transparency = obj.Transparency


	def onChanged(self,obj,Parameter):
		if Parameter == 'edgeLength':
			self.execute(obj)


class ViewProviderDiagram:
	def __init__(self, obj):
		obj.Proxy = self

	def getIcon(self):
		return """/* XPM */
static char * moment_xpm[] = {
"32 32 51 1",
" 	c None",
".	c #0D0000",
"+	c #000000",
"@	c #0E0000",
"#	c #390000",
"$	c #060000",
"%	c #410000",
"&	c #F60000",
"*	c #090000",
"=	c #100000",
"-	c #460000",
";	c #F80000",
">	c #FF0000",
",	c #530000",
"'	c #FB0000",
")	c #5F0000",
"!	c #FD0000",
"~	c #660000",
"{	c #FE0000",
"]	c #720000",
"^	c #7D0000",
"/	c #8C0000",
"(	c #990000",
"_	c #9E0000",
":	c #AB0000",
"<	c #0B0000",
"[	c #B00000",
"}	c #070000",
"|	c #4A0000",
"1	c #880000",
"2	c #040000",
"3	c #4B0000",
"4	c #B50000",
"5	c #0C0000",
"6	c #B10000",
"7	c #A60000",
"8	c #940000",
"9	c #850000",
"0	c #840000",
"a	c #6D0000",
"b	c #0F0000",
"c	c #670000",
"d	c #FC0000",
"e	c #5A0000",
"f	c #110000",
"g	c #FA0000",
"h	c #4D0000",
"i	c #470000",
"j	c #050000",
"k	c #3B0000",
"l	c #010000",
"                                ",
"                              .+",
"                             @#$",
"                            .%&*",
"                           =-;>*",
"                          =,'>>*",
"                         @)!>>>*",
"                        =~{>>>>*",
"                       @]>>>>>>*",
"                      .^>>>>>>>*",
"                     @/>>>>>>>>*",
"                    .(>>>>>>>>>*",
"                   @_>>>>>>>>>>*",
"                  @:>>>>>>>>>>>*",
"                 <[>>>>>>>>>>>>*",
"                }|11111111111112",
"211111111111113}                ",
"$>>>>>>>>>>>>45                 ",
"$>>>>>>>>>>>6.                  ",
"$>>>>>>>>>>7@                   ",
"$>>>>>>>>>(5                    ",
"$>>>>>>>>8@                     ",
"$>>>>>>>9.                      ",
"$>>>>>>0@                       ",
"$>>>>{ab                        ",
"$>>>{cb                         ",
"$>>def                          ",
"$>gh=                           ",
"$;i@                            ",
"jkf                             ",
"l.                              ",
"+                               "};
		"""



class CommandDiagram():

	def GetResources(self):
		return {"Pixmap"  : os.path.join(ICONPATH, "icons/diagram.svg"), # the name of a svg file available in the resources
				"Accel"   : "Shift+D", # a default shortcut (optional)
				"MenuText": "Diagram",
				"ToolTip" : "Gera os diagramas dos esforços"}
	
	def Activated(self):
		objCalc = FreeCADGui.Selection.getSelectionEx()[0].Object
		listSelects = list(filter(lambda select: 'Wire' in select.Object.Name or 'Line' in select.Object.Name, FreeCADGui.Selection.getSelectionEx()))
		
		if 'Calc' in objCalc.Name: #valida se o primeiro elemento de fato é um calc

			doc = FreeCAD.ActiveDocument
			obj = doc.addObject("Part::FeaturePython", "Diagram")
			Diagram(obj, objCalc, listSelects)
			ViewProviderDiagram(obj.ViewObject) 

		else:
			show_error_message('Deve ser selecionado um objeto calc para traçar o diagrama')
			print('Deve ser selecionado um objeto calc para traçar o diagrama')
	
	def IsActive(self):
		return True


FreeCADGui.addCommand("diagram", CommandDiagram())
