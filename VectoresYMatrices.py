#Juan Pablo Daza Pereira
#CNYT

import libreria_complejos as lc
import math
"V: vectores"
"M: matrices"

def sumaV(v1, v2):

    res = []
    if len(v1) == len(v2):
        for i in range(len(v1)):
            res.append(lc.suma(v1[i][0], v2[i][0]))
        return res
    else:
        return "Syntax Error"


def restaV(v1, v2):

    res = []
    if len(v1) == len(v2):
        for i in range(len(v1)):
            res.append(lc.resta(v1[i][0], v2[i][0]))
        return res
    else:
        return "Syntax Error"


def inversoAditivoV(v1):

    res = []
    for i in range(len(v1)):
        res.append(lc.producto(v1[i][0], [-1, 0]))
    return res


def productoEscalarV(v1, ec1):

    res = []
    for i in range(len(v1)):
        for j in range(len(v1[0])):
            res.append(lc.producto(v1[i][0], ec1))
    return res


def adicionM(m1, m2):

    res = []
    if len(m1) == len(m2):
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                res.append(lc.suma(m1[i][j], m2[i][j]))
        return res
    else:
        return "Syntax Error"


def inversoAditivoM(m1):

    res = []
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res.append(lc.producto(m1[i][j], [-1, 0]))
    return res


def productoEscalarM(m1, ec1):

    res = []
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            res.append(lc.producto(m1[i][j], ec1))
    return res


def transpuestaMV(m1):

    filas = len(m1)
    columnas = len(m1[0])
    m2 = [[None for i in range(filas)]for j in range(columnas)]

    for i in range(filas):
        for j in range(columnas):
            m2[j][i] = m1[i][j]
    return m2


def conjugadoMV(m1):

    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] = lc.conjugado(m1[i][j])
    return m1


def dagaMV(m1):

    return transpuestaMV(conjugadoMV(m1))


def productoM(m1, m2):

    filasm1, filasm2 = len(m1), len(m2)
    columnasm1, columnasm2 = len(m1[0]), len(m2[0])
    if columnasm1 == filasm2:
        mr = [[[0, 0] for columnas in range(columnasm2)]for filas in range(filasm1)]
        for i in range(filasm1):
            for j in range(columnasm2):
                for k in range(filasm2):
                    mr[i][j] = lc.suma(mr[i][j],lc.producto(m1[i][k], m2[k][j]))
        return mr
    else:
        return "Syntax Error"


def accionMV(m1, v2):

    return productoM(m1, v2)

def productoInterno(v1,v2):

    return productoM(dagaMV(v1),v2)


def normaV(v1):

    x = productoInterno(v1, v1)
    complejo = [x[0][0][0], x[0][0][1]]
    return lc.modulo(complejo)


def distanciaV(v1,v2):

    resta = restaV(v1,v2)
    res = normaV(resta)
    return res


def unitariaM(m1):

    filas = len(m1)
    columnas = len(m1[0])
    mIdentidad = [[1 if  j==i else 0 for j in range(columnas)]for i in range(filas)]
    
    if productoM(m1,dagaMV(m1)) == mIdentidad:
        return True
    else:
        return False


def hermitianaM(m1):

    if dagaMV(m1) == m1:
        return True
    else:
        return False


def productoTensorialM(m1, m2):

    filasm1, filasm2 = len(m1), len(m2)
    columnasm1, columnasm2 = len(m1[0]), len(m2[0])
    mr = [[[0, 0] for i in range(columnasm1*columnasm2)]for j in range(filasm1*filasm2)]
    for i in range(len(mr)):
        for j in range(len(mr[0])):
            mr[i][j] = lc.producto(m1[i//filasm2][j//columnasm2], m2[i%filasm2][j%columnasm2])
    return mr
