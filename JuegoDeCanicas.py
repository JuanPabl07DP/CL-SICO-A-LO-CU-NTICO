#Juan Pablo Daza Pereira
#CNYT 2023-1
#De lo clasico a lo cuantico
import libreria_complejos as lc
import numpy as np
import matplotlib.pyplot as plt
import Vectores_matrices as vc
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
    vector = [[[8, 0]],
             [[2, 0]],
             [[0, 0]],
             [[4, 0]],
             [[5, 0]],
             [[10, 0]]
             ]
    matriz = [[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
             [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
             [[0,0],[1,0],[0,0],[0,0],[0,0],[1,0]],
             [[0,0],[0,0],[0,0],[1,0],[0,0],[0,0]],
             [[0,0],[0,0],[1,0],[0,0],[0,0],[0,0]],
             [[1,0],[0,0],[0,0],[0,0],[1,0],[0,0]],
             ]
    for i in range(int(input("Ingrese el número de clics:"))+1):
        grafica(proceso(vector,matriz,i),i)
        #print('el proceso es:',proceso(vector,matriz,i))

main()
