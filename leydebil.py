# Ley de debil de los grandes numeros
'''
Esta ley establece que cuando hay una secuencia de variables aleatorias independientes
y distribuidas identicamente dentro de un rango (Como (0,1)), la media de estas variables
se aproxima a su valor esperado/teorico a medida que el tamaño de la muestra aumenta y se 
van calculando las medias paciales.
'''

import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

def calcular_medias_parciales(valores):
    # Las medias parciales tienden a oscilar hacia la media teórica, al inicio
    # teniendo valores que oscilan bastante pero a medida que se van calculando
    # las medias parciales se acercan mas a la media teorica
    medias_parciales = np.cumsum(valores) / np.arange(1, len(valores) + 1)
    return medias_parciales

def graficar_medias_parciales(medias_parciales, media_teorica):
    with PdfPages('leydebil.pdf') as pdf:
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, len(medias_parciales) + 1), medias_parciales, label="Medias parciales")
        plt.axhline(y=media_teorica, color='r', linestyle='--', label="Media teórica (ų)")
        plt.xlabel("n")
        plt.ylabel("Media")
        plt.title("Ley débil de los grandes números")
        plt.legend()
        plt.grid(True)
        pdf.savefig()
        plt.show()

def main():
    n = 1000000  # Cantidad de valores aleatorios a generar
    valores_aleatorios = np.random.uniform(0, 1, n) # Generacion de n valores aleatorios dentro de (0, 1)
    media_teorica = 0.5  # Media teórica de la distribución uniforme (ų)
    medias_parciales = calcular_medias_parciales(valores_aleatorios) # Calculo de las medias parciales
    graficar_medias_parciales(medias_parciales, media_teorica)

if __name__ == "__main__":
    main()

