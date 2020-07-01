import numpy as np
from math import pow

def generadorgcl(seed, a, c, m, n):
    #Args:
    #seed = Semilla del generador
    #a = cte multiplicativa
    #c = cte aditiva
    #m = modulo

    numeros = []
    numeros_0y1 = []

    numeros.append(seed)
    for i in range(n):
        num  =  ((a * numeros[i - 1]) + c) % m
        numeros.append(num)
        numeros_0y1.append(num/m) #Lo dividimos por m para que devuelva un generador uniforme (0;1)
    return numeros_0y1


