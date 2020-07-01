import matplotlib.pyplot as plt

def histograma(distribucion):
    plt.hist(distribucion, bins=50, color='skyblue', histtype="bar",alpha=0.8,ec="black")
    plt.xlabel('Valores')
    plt.ylabel('Probabilidad')
    plt.show()
