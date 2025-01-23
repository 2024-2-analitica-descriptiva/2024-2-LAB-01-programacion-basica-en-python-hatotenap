"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    datos = 'files/input/data.csv'
    conteo_claves = {}

    with open(datos, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            columnas = linea.strip().split('\t')  
            if len(columnas) > 4:  
                diccionario_codificado = columnas[4] 
                # Divido en pares clave:valor 
                pares = diccionario_codificado.split(',')  
                for par in pares:
                    try:
                        clave, _ = par.split(':')  
                        conteo_claves[clave] = conteo_claves.get(clave, 0) + 1  
                    except ValueError:
                        pass  

    conteo_claves_ordenado = dict(sorted(conteo_claves.items()))

    return(conteo_claves_ordenado)