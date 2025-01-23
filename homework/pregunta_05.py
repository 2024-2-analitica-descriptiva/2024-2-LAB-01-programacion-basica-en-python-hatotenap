"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """

    datos = 'files/input/data.csv'

    valores_por_letra = {}

    with open(datos, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')
            if len(columnas) > 1:
                letra, valor = columnas[0], columnas[1]
                try:
                    valor = int(valor)
                    if letra not in valores_por_letra:
                        valores_por_letra[letra] = [valor, valor]
                    else:
                        valores_por_letra[letra] = [
                            max(valores_por_letra[letra][0], valor),
                            min(valores_por_letra[letra][1], valor),
                            ]
                except ValueError:
                    continue

    resultado = [(letra, maximo, minimo) for letra, (maximo, minimo) in sorted(valores_por_letra.items())]
    return (resultado)