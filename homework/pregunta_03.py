"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    datos = 'files/input/data.csv'

    suma_por_letra = {}

    with open(datos, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            if len(columnas) > 1:
                letra = columnas[0]
                try:
                    valor = float(columnas[1])  
                    suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor
                except ValueError:
                    pass  

    
    resultado = sorted(suma_por_letra.items())
    return resultado





