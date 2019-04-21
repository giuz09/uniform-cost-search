# this file contains graph
# import queue as q
import Heap as monticulo
#inicializo el  costo, el recorrido y el nodo inicial
COSTO = 0
RECORRIDO = 2
NODE= 1

#clase grafo
class Graph:
    def __init__(self, nodoInicial=None):
        self.nodos = set(nodoInicial)
        self.conecciones = {}
        self.isDirected = True
#        self.isDirected = Directed
        if (nodoInicial is not None):
            self.conecciones[nodoInicial] = list()
#funcion para agregar conexiones entre nodos
    def addConection(self, NodoOrigen, NodoDestino, costo):
        if (NodoOrigen in self.nodos and self.isDirected == False):
            self.conecciones[NodoOrigen].append((costo,NodoDestino ))
        elif (self.isDirected == True):
            self.conecciones[NodoOrigen].append((costo,NodoDestino))
            self.conecciones[NodoDestino].append((costo,NodoOrigen ))
        else:
            raise Exception('error al crear una conexión: no existe el nodo en el grafo')
#funcion para agregar nodo
    def addNode(self, nodoNuevo):
        if (nodoNuevo in self.nodos):
            raise Exception('error al agregar nodo: el nodo ya existe en el grafo')
        else:
            self.nodos.add(nodoNuevo)
            self.conecciones[nodoNuevo] = list()
#funcion de los nodos visitados
    def nodosVisitados(self):
        self.visitedNodes = dict.fromkeys(self.nodos, False)
#funcion de nodo visitado
    def nodoVisitado(self, node):
        self.visitedNodes[node] = True

    def __str__(self):
        return str(self.conecciones)
#funcion UCS (uniform cost search)
    def UCS(self, nodoInicial, nodoFinal):
        unaColaPrioridad = monticulo.PriorityQueue()
        unaColaPrioridad.insertarElemento((0, nodoInicial, nodoInicial))  
        #una vez que se inicializa la cola de prioridad se chequea que no este vacia
        while (not (unaColaPrioridad.empty())): 
            #prueba recorrido
#            print(unaColaPrioridad.queue)
            node = unaColaPrioridad.eliminarElemento()
            #si se llega al nodo final
            if (node[NODE] in nodoFinal):
#                print("Se llego al nodo final")
                print("Recorrido al nodo final: " + node[RECORRIDO] + " Costo: " + str(node[COSTO]))
                break
            #sino recorre los nodos
            elif(self.visitedNodes[node[NODE]]):
                continue
            #sino recorre los nodos hijos
            else:
                self.nodoVisitado(node[NODE])
                nodosHijos = self.conecciones[node[NODE]]
                for nodoHijo in nodosHijos:
                    if (self.visitedNodes[nodoHijo[NODE]] is not True):
                        unaColaPrioridad.insertarElemento((nodoHijo[COSTO] + node[COSTO], nodoHijo[NODE], node[RECORRIDO] + "->" + str(nodoHijo[NODE]))) 
                    else:
                        continue
















