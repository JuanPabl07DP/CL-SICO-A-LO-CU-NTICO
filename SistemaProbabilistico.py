import libreria_complejos as lc
import numpy as np
import matplotlib.pyplot as plt
import VectoresYMatrices as vc
from tkinter import messagebox

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
    M = [[[0,0],[0.61,0],[0.39,0]],
        [[0.5,0],[0.09,0],[0.41,0]],
        [[0.5,0],[0.3,0],[0.2,0]]
        ]
    V = [[[0.7, 0]],
        [[0.1, 0]],
        [[0.2, 0]]
        ]
    
    for i in range(int(input("Ingrese el número de clics:"))+1):
        grafica(proceso(V,M,i),i)
        print('el proceso es:',proceso(V,M,i))

main()
