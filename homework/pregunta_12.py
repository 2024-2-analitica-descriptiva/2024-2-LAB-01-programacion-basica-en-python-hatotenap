"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """

    datos = 'files/input/data.csv'

    suma_por_letra = {}

    with open(datos, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')  
            if len(columnas) > 4:  
                letra = columnas[0]  
                valores_columna_5 = columnas[4].split(',')  
                suma_valores = 0
                for par in valores_columna_5:
                    try:
                        _, valor = par.split(':')  
                        suma_valores += int(valor)  
                    except ValueError:
                        pass  
                suma_por_letra[letra] = suma_por_letra.get(letra, 0) + suma_valores  


    suma_por_letra_ordenado = dict(sorted(suma_por_letra.items()))

    return(suma_por_letra_ordenado)