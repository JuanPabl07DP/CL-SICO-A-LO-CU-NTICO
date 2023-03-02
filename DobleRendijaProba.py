#CNYT 2023-1
import libreria_complejos as lc
import numpy as np
import matplotlib.pyplot as plt
import VectoresYMatrices as vc
from tkinter import messagebox
import math as m

def grafica(v,clics):
    print('Vector estado final:', v)
    labels = []
    estado = []
    for i in range(len(v)):
        labels.append('Pto.'+str(i))
        estado.append(v[i][0][0])

    index = np.arange(len(labels))
    plt.bar(index, estado)
    plt.xlabel('Estado')
    plt.ylabel('Valor')
    plt.xticks(index, labels, rotation=45)
    plt.title('Evolución dinámica del sistema después de ' + str(clics) + ' clics de tiempo')
    plt.show()

def graficaCuantica(v,clics):
    print('Vector estado final:', v)
    labels = []
    estado = []
    for i in range(len(v)):
        labels.append('Pto.'+str(i))
        estado.append(lc.modulo(v[i][0])**2)

    index = np.arange(len(labels))
    plt.bar(index, estado)
    plt.xlabel('Estado')
    plt.ylabel('Valor')
    plt.xticks(index, labels, rotation=45)
    plt.title('Evolución dinámica del sistema después de ' + str(clics) + ' clics de tiempo')
    plt.show()
    
def proceso(v,m,clics):
    if clics == 0:
        return  v
    elif clics == 1:
        return vc.productoMatrices(m,v)
    else:
        return vc.productoMatrices(m,proceso(v,m,clics-1))


def main():
    V = [[[1,0]],
         [[0,0]],
         [[0,0]],
         [[0,0]],
         [[0,0]],
         [[0,0]],
         [[0,0]],
         [[0,0]],
        ]
    M = [[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
        [[1/2,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
        [[1/2,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
        [[0,0],[1/3,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0]],
        [[0,0],[1/3,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0]],
        [[0,0],[1/3,0],[1/3,0],[0,0],[0,0],[1,0],[0,0],[0,0]],
        [[0,0],[0,0],[1/3,0],[0,0],[0,0],[0,0],[1,0],[0,0]],
        [[0,0],[0,0],[1/3,0],[0,0],[0,0],[0,0],[0,0],[1,0]],
        ]
    for i in range(3):
        grafica(proceso(V,M,i),i)
main()
