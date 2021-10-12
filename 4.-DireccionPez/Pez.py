# Puzle lineal con Busqueda en Profundidad - Deep First Search
from Nodos import Nodo


def busqueda_BPP(estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_raiz = Nodo(estado_inicial)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop()
        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_estado() == solucion:
            # Solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            # Expandir nodos hijos
            datos_nodo = nodo_actual.get_estado()

            # Operador Izquierdo
            hijo = [datos_nodo[1], datos_nodo[0], datos_nodo[2], datos_nodo[3], datos_nodo[4], datos_nodo[5], datos_nodo[6], datos_nodo[7]]
            hijo_izquierda = Nodo(hijo)

            # Operador Izquierdo
            if not hijo_izquierda.en_lista(nodos_visitados) and not hijo_izquierda.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierda)

            hijo = [datos_nodo[0], datos_nodo[2], datos_nodo[1], datos_nodo[3], datos_nodo[4], datos_nodo[5], datos_nodo[6], datos_nodo[7]]
            hijo_izquierda1 = Nodo(hijo)
            if not hijo_izquierda1.en_lista(nodos_visitados) and not hijo_izquierda.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierda1)

            hijo = [datos_nodo[0], datos_nodo[1], datos_nodo[3], datos_nodo[2], datos_nodo[4], datos_nodo[5], datos_nodo[6], datos_nodo[7]]
            hijo_izquierda2 = Nodo(hijo)
            if not hijo_izquierda2.en_lista(nodos_visitados) and not hijo_izquierda.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierda2)

            # Operador Central
            hijo = [datos_nodo[0], datos_nodo[1], datos_nodo[2], datos_nodo[4], datos_nodo[3], datos_nodo[5], datos_nodo[6], datos_nodo[7]]
            hijo_centro = Nodo(hijo)
            if not hijo_centro.en_lista(nodos_visitados) and not hijo_izquierda.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_centro)


            # Operador Derecho
            hijo = [datos_nodo[0], datos_nodo[1], datos_nodo[2], datos_nodo[3], datos_nodo[5], datos_nodo[4], datos_nodo[6], datos_nodo[7]]
            hijo_derecha = Nodo(hijo)
            if not hijo_derecha.en_lista(nodos_visitados) and not hijo_izquierda.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecha)
                
            hijo = [datos_nodo[0], datos_nodo[1], datos_nodo[2], datos_nodo[3], datos_nodo[4], datos_nodo[6], datos_nodo[5], datos_nodo[7]]
            hijo_derecha1 = Nodo(hijo)
            if not hijo_derecha1.en_lista(nodos_visitados) and not hijo_izquierda.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecha1)

            hijo = [datos_nodo[0], datos_nodo[1], datos_nodo[2], datos_nodo[3], datos_nodo[4], datos_nodo[5], datos_nodo[7], datos_nodo[6]]
            hijo_derecha2 = Nodo(hijo)
            if not hijo_derecha2.en_lista(nodos_visitados) and not hijo_izquierda.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecha2)
                
            nodo_actual.set_hijo([hijo_izquierda, hijo_izquierda1, hijo_izquierda2, hijo_centro, hijo_derecha, hijo_derecha1, hijo_derecha2])

if __name__ == "__main__":
    estado_inicial = [6, 4, 5, 2, 3, 1, 7, 8]
    solucion = [1, 2, 3, 4, 5, 6, 8, 7]
    nodo_solucion = busqueda_BPP(estado_inicial, solucion)
    # Mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_estado())
        nodo_actual = nodo_actual.get_padre()
    
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
