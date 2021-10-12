# Búsqueda Coste Uniforme - Uniform Cost Search
from Nodos import Nodo

def Comparar(nodo):
    return nodo.get_costo()

def busqueda_BCU(conecciones, estado_inicial, solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_raiz = Nodo(estado_inicial)
    nodo_raiz.set_costo(0)
    nodos_frontera.append(nodo_raiz)
    while (not resuelto) and len(nodos_frontera) != 0:
        # Ordenar lista de nodos frontera
        nodos_frontera = sorted(nodos_frontera, key=Comparar)
        nodo_actual = nodos_frontera[0]
        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo_actual.get_estado() == solucion:
            # Solucion encontrada
            resuelto = True
            return nodo_actual
        else:
            # Expandir nodos hijo (ciudades con conexion)
            datos_nodo = nodo_actual.get_estado()
            lista_hijos = []
            for achild in conecciones[datos_nodo]:
                hijo = Nodo(achild)
                costo = conecciones[datos_nodo][achild]
                hijo.set_costo(nodo_actual.get_costo() + costo)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados):
                    # Si está en la lista lo sustituimos con el nuevo valor de coste si es menor
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:
                            if n.equal(hijo) and n.get_costo() < hijo.get_costo():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)
            nodo_actual.set_hijo(lista_hijos)


if __name__ == "__main__":
    # conecciones = {
    #     'Malaga': {'Granada': 125, 'Madrid': 513},
    #     'Sevilla': {'Madrid': 514},
    #     'Granada': {'Malaga': 125, 'Madrid': 423, 'Valencia': 491},
    #     'Valencia': {'Granada': 491, 'Madrid': 356, 'Zaragoza': 309, 'Barcelona': 346},
    #     'Madrid': {'Salamanca': 203, 'Sevilla': 514, 'Malaga': 513, 'Granada': 423, 'Barcelona': 603, 'Santander': 437, 'Valencia': 356, 'Zaragoza': 313, 'Santiago': 599},
    #     'Salamanca': {'Santiago': 390, 'Madrid': 203},
    #     'Santiago': {'Salamanca': 390, 'Madrid': 599},
    #     'Santander': {'Madrid': 437, 'Zaragoza': 394},
    #     'Zaragoza': {'Barcelona': 296, 'Valencia': 309, 'Madrid': 313},
    #     'Barcelona': {'Zaragoza': 296, 'Madrid': 603, 'Valencia': 396}

    # }
    
    conecciones = {
        'Parque_Sucre':{'Plazuela_San_Juanillo':1100, 'Stadium_Patria':1000},
        'Plazuela_San_Juanillo':{'Mercado_campesino': 350, 'Parque_Sucre': 1100},
        'Mercado_campesino':{'Reloj': 900, 'Stadium_Patria': 800, 'Plazuela_San_Juanillo': 350},
        'Stadium_Patria': {'Caja_Petrolera': 280 , 'Tribunal_constitucional': 700, 'Reloj': 600, 'iglesia_SanMatias': 550, 'coliseo_JRA': 350, 'Mercado_campesino': 800, 'Parque_Sucre': 1000},

        'Caja_Petrolera': {'Stadium_Patria': 280, 'Tribunal_constitucional': 400},
        'Tribunal_constitucional':{'Rotonda':350},
        'iglesia_SanMatias':{'Rotonda':400, 'Stadium_Patria': 280},
        'Rotonda':{'iglesia_SanMatias': 400 },
        'coliseo_JRA':{'Mercado_Negro': 450, 'Mercado_Central': 950},
        'Reloj':{'Stadium_Patria': 600, 'Mercado_Central': 900, 'Mercado_Negro': 120, 'Mercado_campesino': 900},
        'Mercado_Negro': {'Reloj': 120, 'Mercado_Central': 700},
        'Parque_Bolivar':{'Mercado_Central': 650, 'H_Santa_Barabara': 400},
        'H_Santa_Barabara':{'Plaza25Mayo': 500},
        'Mercado_Central': {'Mercado_Negro': 700, 'Parque_Bolivar': 650, 'Reloj': 900, 'coliseo_JRA': 950, 'I_San_Francisco': 220},
        'USFX':{'Plaza25Mayo': 210, 'H_Santa_Barabara': 450, 'Plazuela_Zudañez': 200},
        'I_San_Francisco':{'Plaza25Mayo': 230, 'Mercado_Central': 220},
        'Plaza25Mayo': {'I_San_Francisco': 230, 'USFX': 210, 'Plazuela_Zudañez': 290, 'Parque_Bolivar': 900, 'Super_Mercado_SAS': 450, 'Teatro_Aire_Libre': 1200, 'Recoleta': 1000, },

        'Teatro_Aire_Libre':{'Recoleta', 650},
        'Recoleta':{'Plaza25Mayo': 1000},
        'Plazuela_Zudañez':{'USFX': 200, 'Super_Mercado_SAS': 420, 'Seguro_Universitario': 600},
        'Seguro_Universitario':{'Cementerio_General': 500, 'Plazuela_Zudañez': 600},
        'Super_Mercado_SAS': {'Plaza25Mayo': 450, 'Plazuela_Zudañez': 420},
        'Cementerio_General': {'Seguro_Universitario': 500},

    }
    
    estado_inicial = 'Stadium_Patria'
    solucion = 'Caja_Petrolera'
    nodo_solucion = busqueda_BCU(conecciones, estado_inicial, solucion)
    # Mostrar resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_estado())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    print("Costo: %s" % str(nodo_solucion.get_costo()))
