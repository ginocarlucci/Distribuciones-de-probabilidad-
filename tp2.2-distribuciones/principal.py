import distribuciones
import graficas
import numpy as np
import pruebas


#DISTRIBUCIONES

uniforme = distribuciones.distribucion_uniforme(0,20)
exponencial = distribuciones.distribucion_exponencial(0.5)
gamma = distribuciones.distribucion_gamma(5,1)
normal = distribuciones.distribucion_normal(10,20)
pascal = distribuciones.distribucion_pascal(5,0.4)
binomial = distribuciones.distribucion_binomial(20,0.5)
hipergeometrica = distribuciones.distribucion_hipergeometrica(5000000,500,0.4)
poisson = distribuciones.distribucion_poisson(10)
empirica = distribuciones.distribucion_empirica()

#GRAFICAS
graficas.histograma(uniforme)
graficas.histograma(exponencial)
graficas.histograma(gamma)
graficas.histograma(normal)
graficas.histograma(pascal)
graficas.histograma(binomial)
graficas.histograma(hipergeometrica)
graficas.histograma(poisson)
graficas.histograma(empirica)

#PRUEBAS
print(pruebas.Kolmogorov(uniforme, 0.05))
pruebas.Anderson(exponencial,'expon')
pruebas.Anderson(normal,'norm')
print(pruebas.ChiEmpirica(empirica))
#Para las demas pruebas se utilizó las funciones np.mean() y np.var() para comparar con los valores esperados

