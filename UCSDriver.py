import Graph as grafo

#se construye el grafo agregando el nodo inicial
#agregando los demas nodos
#para luego agregar las conexiones de los nodos

unGrafo = grafo.Graph('S')
unGrafo.addNode('A')
unGrafo.addNode('B')
unGrafo.addNode('C')
unGrafo.addNode('D')
unGrafo.addNode('E')
unGrafo.addNode('F')
unGrafo.addNode('G1')
unGrafo.addNode('G2')
unGrafo.addNode('G3')
unGrafo.addConection('S','A',5)
unGrafo.addConection('S','B',9)
unGrafo.addConection('S','D',6)
unGrafo.addConection('A','B',3)
unGrafo.addConection('A','G1',9)
unGrafo.addConection('B','C',9)
unGrafo.addConection('D','C',2)
unGrafo.addConection('D','E',2)
unGrafo.addConection('C','G2',5)
unGrafo.addConection('C','F',7)
unGrafo.addConection('E','G3',7)

#se visita los nodos y se realiza la busqueda de costo uniforme (UCS)
unGrafo.nodosVisitados()
unGrafo.UCS('S', ('G1','G2','G3'))