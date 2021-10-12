from busquedas_02 import aestrella, ProblemaBusqueda
import math
import time

# OBJETIVO = '''1-2-3
# 4-5-6
# 7-8-e'''

# INICIAL = '''1-2-e
# 3-4-5
# 6-7-8'''

# OBJETIVO = '''a-b-c
# d-e-f
# g-h-0'''

# INICIAL = '''a-b-0
# c-d-e
# f-g-h'''

OBJETIVO = '''a-b-c-d
e-f-g-h
i-j-k-l
m-n-o-0'''

# INICIAL = '''a-b-c-0
# d-e-f-g
# h-i-j-k
# l-m-n-o'''
INICIAL = '''a-b-c-d
e-f-g-h
i-j-k-0
l-m-n-o'''


def list_to_string(list_):
    return '\n'.join(['-'.join(row) for row in list_])

# print(list_to_string(OBJETIVO))    
# exit()

def string_to_list(string_):
    return [row.split('-') for row in string_.split('\n')]

# print(string_to_list(OBJETIVO))    
# exit()

def find_location(filas, element_to_find):
    '''Encuentra la ubicacion de una pieza en el rompecabezas.
       DEvuelve una tupla: fila, columna'''
    for ir, row in enumerate(filas):
        for ic, element in enumerate(row):
            if element == element_to_find:
                return ir, ic


posiciones_objetivo = {}
filas_objetivo = string_to_list(OBJETIVO)
for numero in 'abcdefghijklmno0':
    posiciones_objetivo[numero] = find_location(filas_objetivo, numero)
    # print(posiciones_objetivo)
# exit()

class EigthPuzzleProblem(ProblemaBusqueda):
    def acciones(self, estado):
        '''Devuelve una lista de piesas que se pueden mover a un espacio vacio.'''
        filas = string_to_list(estado)
        fila_0, columna_0 = find_location(filas, '0')
        # print(filas)
        # print(fila_0, columna_0)

        acciones = []
        if fila_0 > 0:
            acciones.append(filas[fila_0 - 1][columna_0])
            
        if fila_0 < 3:
            acciones.append(filas[fila_0 + 1][columna_0])
            
        if columna_0 > 0:
            acciones.append(filas[fila_0][columna_0 - 1])
            
        if columna_0 < 3:
            acciones.append(filas[fila_0][columna_0 + 1])
            
        return acciones

    def resultado(self, estado, accion):
        '''Devuelve el resultado despues de mover una pieza a un espacio en vacio
        '''
        filas = string_to_list(estado)
        fila_0, columna_0 = find_location(filas, '0')
        fila_n, columna_n = find_location(filas, accion)

        # filas[fila_0][columna_0], filas[fila_n][columna_n] = filas[fila_n][columna_n], filas[fila_0][columna_0]
        filas[fila_0][columna_0], filas[fila_n][columna_n] = (
            filas[fila_n][columna_n], 
            filas[fila_0][columna_0],
            )

        return list_to_string(filas)

    def es_objetivo(self, estado):
        '''Devuelve True si un estado es el estado_objetivo.'''
        return estado == OBJETIVO

    def costo(self, estado1, accion, estado2):
        '''Devuelve el costo de ejecutar una accion. 
        '''
        return 1

    def heuristica(self, estado):
        '''Devuelve una estimacion de la distancia
        de un estado a otro, utilizando la distancia manhattan.
        '''
        filas = string_to_list(estado)

        distancia = 0

        for numero in 'abcdefghijklmno0':
            fila_n, columna_n = find_location(filas, numero)
            fila_n_objetivo, col_n_goal = posiciones_objetivo[numero]

            distancia += abs(fila_n - fila_n_objetivo) + abs(columna_n - col_n_goal)
            # distancia += math.sqrt((fila_n - fila_n_objetivo) ** 2 + (columna_n - col_n_goal) ** 2)

        return distancia

    # def heuristica(self, estado):
    #     filas = string_to_list(estado)

    #     distancia = 0

    #     for numero in 'abcdefghijklmn0':
    #         fila_n, columna_n = find_location(filas, numero)
    #         fila_n_objetivo, col_n_objetivo = posiciones_objetivo[numero]

    #         distancia += math.sqrt((fila_n - fila_n_objetivo) ** 2 + (columna_n - col_n_objetivo) ** 2)
            

    #     return distancia

    # def heuristica(self, estado):
    #     filas = string_to_list(estado)

    #     distancia = 0

    #     for numero in 'abcdefgh0':
    #         fila_n, columna_n = find_location(filas, numero)
    #         fila_n_objetivo, col_n_objetivo = posiciones_objetivo[numero]

    #         if(fila_n != fila_n_objetivo and columna_n != col_n_objetivo):
    #             distancia += 1 

    #     return distancia
def main():
    resultado = aestrella(EigthPuzzleProblem(INICIAL))

    for accion, estado in resultado.camino():
        print('Move numero', accion)
        print(estado)



if __name__ == "__main__":
    start_time=time.time()
    main()
    tiempo_ejecucion=time.time()-start_time
    print("\nEl tiempo de ejecucion del Rompecabezas es", round(tiempo_ejecucion,6)," segundos")

