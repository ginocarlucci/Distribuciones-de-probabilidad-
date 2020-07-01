import numpy as np
from scipy.stats import ksone
from scipy.stats import anderson
from scipy import stats


def Kolmogorov(numeros, alpha):

#Ordenar los numeros en forma ascendente
    num_ordenados = sorted(numeros)
    tamaño = len(num_ordenados)

#Calculo D+ Y D-
    D_Mas = max(((i+1)/tamaño - num_ordenados[i]) for i in range(tamaño))
    D_Menos = min((num_ordenados[i] - (i-1)/tamaño) for i in range(tamaño))

#Obtengo el mas grande
    D = max(abs(D_Mas) ,abs(D_Menos))

#Busco el valor critico de la tabla de kolmogorov para ese nivel de significancia y lo comparo con D
#Si D es menor que el valor critico puedo decir que los datos pertenecen a una distribucion uniforme
#Para buscar los datos uso la libreria de scipy
    valor_critico = (ksone.pdf(alpha/2, tamaño))
    if D < valor_critico:
        resultado = True
    else:
        resultado = False

    return resultado, D_Mas, D_Menos, valor_critico

def Anderson(array_distribucion,tipo):
    result = anderson(array_distribucion, tipo)
    print('Statistic: %.3f' % result.statistic)
    p = 0
    for i in range(len(result.critical_values)):
        sl, cv = result.significance_level[i], result.critical_values[i]
        if result.statistic < result.critical_values[i]:
            print('%.3f: %.3f, (Se acepta H0)' % (sl, cv))
        else:
            print('%.3f: %.3f, (Se rechaza H0)' % (sl, cv))

def ChiEmpirica(frec_observados):
    f_obs = np.histogram(frec_observados, bins=10)[0]
    p=[0.273,0.037,0.195,0.009,0.124,0.058,0.062,0.151,0.047,0.044]
    f_esp = []
    arreglo_suma_epic = []
    for i in range(10):
        f_esp.append(p[i]*10_000)
        calculo = ((f_obs[i] - f_esp[i]) ** 2) / f_esp[i]
        arreglo_suma_epic.append(calculo)
    suma_epic = sum(arreglo_suma_epic)
    chi_cuadrado_tabla = stats.chi2.ppf(q=0.95, df=9)
    if suma_epic < chi_cuadrado_tabla:
        resultado = True
    else:
        resultado = False
    return resultado, suma_epic, chi_cuadrado_tabla, arreglo_suma_epic



