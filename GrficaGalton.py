import numpy as np
import matplotlib.pyplot as plt
import random as rd

import matplotlib.pyplot as plt
#declaracion de variables
media = 6 #mu 
desviacion = 1 #sigma
canicas =  3000 #n cantidad de muestras
bins =  [0,12]

#Se definen funciones para hacer el calculo de las canicas por medio de la funcion de densidad de probabilidad 
def calculo_histograma():
    muestras = np.random.normal(media, desviacion, canicas) # generacion de 3mil canicas aleatorias
    plt.figure(figsize=(9,4)) #Tamaño de grafica
    conteo, x, barras = plt.hist(muestras, 100, density=True, color = "green", alpha=0.7 )
    #Campana utilizando la funcion de densidad de probabilidad
    plt.plot(x, 1/ (desviacion*np.sqrt(2*np.pi) ) * np.exp(-0.5*((x-media)/desviacion)**2), linewidth=4, color = 'red')
# Se calculan las desviaciones estandar y la media
lados = [media - 3*desviacion, media - 2*desviacion, media - desviacion, media + desviacion,
media + 2*desviacion, media + 3*desviacion, media]
calculo_histograma()


#Se define funcion para la graficacion del histograma
def grafica():
    for s in lados:  # Se dibujan las desviaciones estandar y la media
        plt.axvline(s, color = 'teal', linewidth=1.5, linestyle='dashed')
    plt.yticks()
    plt.xlabel('Distribucion de canicas') #titulo del eje x
    plt.ylabel('Cantidad de canicas')#titulo del eje y
    plt.title('Simulacion de maquina de Galton')#titulo de la gra=ica
    plt.xticks()
    plt.show()
grafica()

