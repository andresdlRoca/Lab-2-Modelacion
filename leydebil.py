# Ley de debil de los grandes numeros

import numpy as np
import matplotlib.pyplot as plt

def calcular_medias_parciales(valores):
    medias_parciales = np.cumsum(valores) / np.arange(1, len(valores) + 1)
    return medias_parciales

def graficar_medias_parciales(medias_parciales, media_teorica):
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(medias_parciales) + 1), medias_parciales, label="Medias parciales")
    plt.axhline(y=media_teorica, color='r', linestyle='--', label="Media teórica (ų)")
    plt.xlabel("n")
    plt.ylabel("Media")
    plt.title("Ley débil de los grandes números")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    n = 10000
    valores_aleatorios = np.random.uniform(0, 1, n)
    media_teorica = 0.5  # Media teórica de la distribución uniforme (ų)
    medias_parciales = calcular_medias_parciales(valores_aleatorios)
    graficar_medias_parciales(medias_parciales, media_teorica)

if __name__ == "__main__":
    main()

