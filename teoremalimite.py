'''
Teorema del Limite Central (TLC)

n (tamano de la muestra): tamano de cada muestra individual extraida de la
distribucion. La cantidad de valores aleatorios que se toman en una 
iteracion para calcular el promedio. La simulacion genera "n" valores
aleatorios y calcula su promedio.

N (numero de simulaciones): indica cuantas veces se repite el proceso de
tomar una muestra de tamano "n" y calcular el promedio. Se realizan "N"
experimentos independientes, cada uno con muestra de tamano "n". Despues,
se analizan las distribuciones de los promedios obtenidos de estas "N"
simulaciones.

Por ejemplo, cuando se dice  "n = 20 y N = 50" o "n = 20 y N = 100",
se describe el escenario en el que se toma 20 valores aleatorios en cada
una de las 50 o 100 simulaciones, respectivamente. Entonces se calculan
50 o 100 promedios de 20 valores aleatorios en cada simulacion, y luego se 
analizan la distribucion de estos promedios.

Los valores permiten observar como se comporta el Teorema del Limite 
Central a medida que se aumenta de tamano las muestras individuales "n" y 
la cantidad de simulaciones "N". En teoria, a medida que "n" aumenta, la
distribucion de los promedios se acerca cada vez a una distribucion normal, 
independientemente de la distribucion original de los datos. 

>> Esto se puede observar claramente en las graficas, ya que entre mas 
aumenta de tamano las muestras individuales "n" y la cantidad de 
simulaciones "N", la distribucion de los promedios se acerca mas a una 
distribucion normal. << 

Esto es una caracteristica clave del Teorema del Limite Central y su 
importancia en la inferencia estadistica.

Sigma: Se usa en la simulacion para ajustar la distribucion uniforme en 
el intervalo (0,1) a la formula del Teorema del Limite Central, que 
normaliza la diferencia entre la media muestral y la media poblacional 
por la desviacion estandar. La distribucion uniforme en el intervalo (0,1) 
tiene una varianza teorica de sigma^2 = 1/12


Frecuencia Relativa Acumulada (Funcion de Distribucion Empirica)

Es una forma de representar la distribucion de datos observados en un 
conjunto de valores. La idea es contar cuantos valores son menores o 
iguales a un cierto valor, y expresar esa cantidad como una proporcion
del tamano total de la muestra. La funcion de distribucion empirica se 
construye trazando estos valores acumulados en una grafica. 

Es la probabilidad acumulada de que un valor aleatorio del TLC sea menor
o igual a un cierto valor. Al trazar estos valores acumulados en una 
grafica y unirlos con una linea recta, se puede ver como se 
acumulan las probabilidades a medida que los valores aumentan.


Funcion de Distribucion Acumulada de N(0,1)

La FDA es una funcion que da la probabilidad de que una variable sea menor
o igual a un cierto valor. En el contexto de la distribucion normal 
estandar N(0,1), la FDA describe como se acumulan las probabilidades para
los valores de una variable aleatoria que sigue una distribucion normal
estandar.

Para cualquier valor dado, la FDA nos dice cual es la probabilidad de 
obtener un valor menor o igual a ese. Se representa con una curva suave y
se usa en estadisticas para calcular probabilidades y realizar inferencias
sobre variables aleatorias que siguen una distribucion normal estandar.

Unir los puntos con una linea recta en la grafica de FRA es comun para
visualizar la acumulacion gradual de probabilidades a medida que los 
valores aumentan. Asi es mas facil ver como se comporta la distribucion
de los valores observados en relacion con la distribucion teorica (Normal
Estandar).

'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from scipy.stats import norm

# Parametros iniciales
mu = 0.5  # Media de la distribucion uniforme
sigma = np.sqrt(1/12)  # Desviacion estandar de la distribucion uniforme

# Valores de n y N
valores_n = [20, 40, 60, 80, 100]
valores_N = [50, 100, 1000, 10000]


# Funcion para calcular el promedio centrado
def calcularPromedioCentrado(n, N):
    promedios = []
    for _ in range(N):
        valores = np.random.uniform(0, 1, n)
        mediaAritmetica = np.mean(valores)
        promedioCentrado = (mediaAritmetica - mu) / (sigma / np.sqrt(n))
        promedios.append(promedioCentrado)
    return promedios


# Realizar la simulacion y graficar los resultados
with PdfPages('graficasTLC_histogramas.pdf') as pdf_histogramas:
    with PdfPages('graficasTLC_distribucion.pdf') as pdf_distribucion:
        for n in valores_n:
            for N in valores_N:
                promedios = calcularPromedioCentrado(n, N)

                plt.hist(promedios, bins=30, density=True,
                         alpha=0.6, label='Histograma')

                # Crear una distribucion normal estandar para graficar
                x = np.linspace(min(promedios), max(promedios), 100)
                y = norm.pdf(x, 0, 1)

                plt.plot(x, y, 'r', label='N(0,1)')

                plt.title(
                    f'Simulacion Teorema del Limite Central (n={n}, N={N})')
                plt.xlabel('Promedio Centrado')
                plt.ylabel('Densidad')
                plt.axvline(x=0, color='r', linestyle='--',
                            label='Media poblacional')
                plt.legend()

                # Calcular y mostrar la media en la consola
                mediaSimulada = np.mean(promedios)
                print(f"Media simulada (n={n}, N={N}): {mediaSimulada}")

                # Agregar la grafica al PDF de histogramas
                pdf_histogramas.savefig()
                plt.close()

                # Graficar la frecuencia relativa acumulada y la distribucion acumulada
                plt.figure()
                plt.hist(promedios, bins=30, density=True, cumulative=True,
                         histtype='step', label='Frecuencia Relativa Acumulada')
                plt.plot(x, norm.cdf(x, 0, 1), 'r',
                         label='Distribucion Acumulada N(0,1)')
                plt.title(
                    f'Frecuencia Relativa Acumulada vs. Distribucion Acumulada (n={n}, N={N})')
                plt.xlabel('Promedio Centrado')
                plt.ylabel('Probabilidad acumulada')
                plt.legend()

                # Agregar la grafica al PDF de distribucion
                pdf_distribucion.savefig()
                plt.close()
