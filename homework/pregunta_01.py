"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    datos = 'files/input/data.csv'  

    suma_columna2 = sum(
    float(line.split('\t')[1]) for line in open(datos, 'r', encoding='utf-8')
    if len(line.split('\t')) > 1 and line.split('\t')[1].replace('.', '', 1).isdigit()
)
    return suma_columna2
