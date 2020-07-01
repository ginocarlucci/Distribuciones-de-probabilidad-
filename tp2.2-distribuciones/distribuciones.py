import numpy as np
import generador
import random


numerosGCL = generador.generadorgcl(1234,134775813, 1, pow(2, 32),10000)


uniforme = []
exponencial = []
normal = []
gamma = []
pascal = []
binomial = []
hipergeometrica = []
poisson = []
empirica = []

def distribucion_uniforme(a,b):
    for r in numerosGCL:
        x = a+(b-a)*r
        uniforme.append(x)
    return uniforme

def distribucion_exponencial(ex):
    for r in numerosGCL:
        x = -ex*np.log(r)
        exponencial.append(x)
    return exponencial

def distribucion_gamma(k,alpha):
    for i in range(10000):
        tr = 1.0
        for i in range(k):
            r = random.choice(numerosGCL)
            tr = tr *  r
        x = -np.log(tr)/alpha
        gamma.append(x)
    return gamma

def distribucion_normal(mu,sigma):
    for i in range(10000):
        sum = 0.0
        for i in range(12):
            r = random.choice(numerosGCL)
            sum = sum + r
        x = sigma * (sum - 6.0) + mu
        normal.append(x)
    return normal

def distribucion_pascal(k,q):
    for i in range(10000):
        tr = 1.0
        qr = np.log(q)
        for i in range(k):
            r = random.choice(numerosGCL)
            tr = tr * r
        nx = np.log(tr)/qr
        x = nx
        pascal.append(x)
    return pascal

def distribucion_binomial(n,p):
    for i in range(10000):
        x = 0.0
        for i in range(n):
            r = random.choice(numerosGCL)
            if (r-p) < 0:
                x += 1
        binomial.append(x)
    return binomial

def distribucion_hipergeometrica(tn,ns,p):
    for i in range(10000):
        x = 0.0
        for i in range(ns):
            r = random.choice(numerosGCL)
            if (r-p) > 0:
                s = 0.0
            else:
                s = 1.0
                x = x + 1.0
            p = (tn*p-s) / (tn-1.0)
            tn = tn - 1.0
            if(tn<2):break
        hipergeometrica.append(x)
    return hipergeometrica

def distribucion_poisson(p):
    for i in range(10000):
        x = 0.0
        b = np.exp(-p)
        tr = 1.0
        while (tr-b) >= 0:
            r = random.choice(numerosGCL)
            tr = tr * r
            if(tr-b >= 0):
                x = x + 1.0
        poisson.append(x)
    return poisson

def distribucion_empirica():
    p=[0.273,0.037,0.195,0.009,0.124,0.058,0.062,0.151,0.047,0.044]
    for i in range(10000):
        r = random.choice(numerosGCL)
        acum=0
        cont=1
        for j in p:
            acum = acum + j
            if (r<=acum):
                break
            else:
                cont+=1
        empirica.append(cont)
    return empirica

