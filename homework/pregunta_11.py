"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    datos = 'files/input/data.csv'

    suma_por_letra = {}

    with open(datos, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')  
            if len(columnas) > 3:  
                try:
                    valor_columna_2 = int(columnas[1])  
                
                    letras_columna_4 = [letra.strip() for letra in columnas[3].replace(',', ' ').split()]
                    for letra in letras_columna_4:
                        suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor_columna_2
                except ValueError:
                    pass  


    suma_por_letra_ordenado = dict(sorted(suma_por_letra.items()))

    return(suma_por_letra_ordenado)