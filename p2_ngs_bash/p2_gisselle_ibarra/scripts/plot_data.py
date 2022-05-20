import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

# Crea el dataset con tus datos obtenidos en barplot_data.txt
frecuencias=[]
with open('barplot_data.txt','r') as data:
    lineas=data.readlines()
    for linea in lineas:
        if 'Columna'in linea or 'region' in linea or '1' in linea:
            continue
        else:
            linea=linea.replace("\n","").split("\t")
            frecuencias.append(int(linea[1]))

# Cambia el nombre de las categorías por las que obtuviste no lo dejes como "Categoría A", etc.
categorias = ['CDS', 'Gene', 'Exon', 'mRNA']
categorias = [ ''.join(wrap(l, 11)) for l in categorias]

y_pos = np.arange(len(categorias))

# Gráfico de barras
plt.bar(y_pos, frecuencias)
plt.show()
