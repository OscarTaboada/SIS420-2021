import numpy as np

"""EDAD"""
x = np.array([3,4,7,15,17,20,25,27,30,33,38,40,45,50,55,60,65,70,75,80])
"""Ingresos"""
y = np.array([1,2,3,5,10,50,500,800,6000,8000,12000,15000,18000,25000,23000,20000,9000,3800,3500,3000])

theta0 = 1065
theta1 = 166
m = len(x)

def calculo_costo_DC():
    rh = []
    rj = []
    for i in x:
        h = theta0 + theta1 * i
        rh.append(h)
    # print(rh)
    # print(y)
    j = list(np.array(rh) - np.array(y))
    # print(j)
    for potencia in j:
        resultado = potencia ** 2
        rj.append(resultado)
    # print(rj)
    Suma = sum(rj)
    RDC = Suma * (1/(2*m))
    return RDC


def descenso_Gradiente(x, y):
    theta0 = 1065
    theta1 = 166
    interacciones = 1000
    alfha = 0.00001

    for i in range(interacciones):
        h = theta0 + theta1 * np.array(x)
        temp0 = theta0 - alfha * (1/m) * sum(list(np.array(h) - np.array(y)))
        temp1 = theta1 - alfha * (1/m) * sum(list(np.array(h) - np.array(y) * np.array(x)))
        theta0 = temp0
        theta1 = temp1
        print("theta0 {}, theta1 {}, interacciones {}".format(theta0, theta1, i))

print(descenso_Gradiente(x, y))
print(f"costo es = {calculo_costo_DC()}")
