"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


from functools import reduce
from itertools import groupby


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    

    """
    x = open("data.csv", "r").readlines()
    x=[z.replace("\t",",") for z in x]
    x=[z.split(",")for z in x]
    x_segunda_col=[int(z[1])for z in x]
    return sum(x_segunda_col)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    
    from collections import Counter
    x = open("data.csv", "r").readlines()
    col_1=[z[0]for z in x]
    col_1
    cuenta_unicos=Counter(col_1)
    cuenta_unicos
    y=[(k,v)for k,v in cuenta_unicos.items()]
    return sorted(y)


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    x = open("data.csv", "r").readlines()
    x=[z.replace("\t",",") for z in x]
    x=[z.split(",")for z in x]
    from collections import Counter
    col_1_2=[(z[0],int(z[1])) for z in x]
    contador=Counter()
    for k,v in col_1_2:
        contador[k]+=v
    return sorted(list(contador.items()))


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    x = open("data.csv", "r").readlines()
    x=[z.replace("\t",",") for z in x]
    x=[z.split(",")for z in x]
    from collections import Counter
    mes_segundacol=[(z[2].split("-")[1],int(z[1])) for z in x]
    mes_segundacol
    contador2=Counter()
    for k,v in mes_segundacol:
        contador2[k]+=1   
    return sorted(list(contador2.items()))


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    x = open("data.csv", "r").readlines()
    x = [z.replace('\n', '') for z in x]
    x = [z.replace('\t', ',') for z in x]
    x = [z.split(',') for z in x]
    primera_y_segunda_columna = sorted([(z[0], int(z[1])) for z in x])

    agrupada_por_primera = [(k, [z[1] for z in g]) for k, g in groupby(primera_y_segunda_columna, lambda a: a[0])]

    return [(primera_columna, max(segundas_columnas), min(segundas_columnas)) for primera_columna, segundas_columnas in
            agrupada_por_primera]


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    x = open("data.csv", "r").readlines()
    x = [z.replace('\n', '') for z in x]
    x = [z.replace('\t', ';') for z in x]
    x = [z.split(';') for z in x]
    quinta_columna = [z[4].split(',') for z in x]
    quinta_columna_plana = sorted(item.split(':') for linea in quinta_columna for item in linea)
    quinta_columna_agrupada = [(k, [int(z[1]) for z in g]) for k, g in groupby(quinta_columna_plana, lambda a: a[0])]

    return [(primera_columna, min(segundas_columnas), max(segundas_columnas)) for primera_columna, segundas_columnas in
            quinta_columna_agrupada]


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    x = open("data.csv", "r").readlines()
    x = [z.replace('\n', '') for z in x]
    x = [z.replace('\t', ',') for z in x]
    x = [z.split(',') for z in x]
    primera_y_segunda_columna = [(z[1], z[0]) for z in x]

    def reducir(valor, par):
        if par[0] in valor:
            valor[par[0]] = valor[par[0]] + [par[1]]
        else:
            valor[par[0]] = [par[1]]
        return valor

    conteo = reduce(reducir, primera_y_segunda_columna, {})

    return sorted((int(k), v) for k, v in conteo.items())


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    x = open("data.csv", "r").readlines()
    x = [z.replace('\n', '') for z in x]
    x = [z.replace('\t', ',') for z in x]
    x = [z.split(',') for z in x]
    
    primera_y_segunda_columna = [(z[1], z[0]) for z in x]

    def reducir(valor, par):
        if par[0] in valor:
            valor[par[0]] = valor[par[0]] + [par[1]]
        else:
            valor[par[0]] = [par[1]]
        return valor

    conteo = reduce(reducir, primera_y_segunda_columna, {})

    return sorted((int(k), sorted(list(set(v)))) for k, v in conteo.items())
    
    


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    x = open("data.csv", "r").readlines()
    x=[z.replace("\t",",") for z in x]
    x=[z.split(",")for z in x]
    lista_p9=[]
    lista_p9_2=[]
    dict_p9={}
    cuenta=0
    lista_aux9=[]

    col_4=[[y for y in z if ":" in y] for z in x]
    col_4=[[y.split(",") for y in z] for z in col_4]
    col_4=[[[y[:-1] if "\n" in y else y for y in x] for x in z]for z in col_4]
    col_4=[[[y[0:3] for y in x] for x in z]for z in col_4]
    col_4

    for i in col_4:
        lista_p9 = lista_p9+ i
    lista_p9

    for j in lista_p9:
        lista_p9_2 = lista_p9_2+ j
    lista_p9_2

    for c in lista_p9_2:
        if c in list(dict_p9.keys()):
            dict_p9[c]=dict_p9[c]+1
        else:
            dict_p9[c]=1

    return dict_p9


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    x = open("data.csv", "r").readlines()
    x=[z.replace("\t",",") for z in x]
    x=[z.split(",")for z in x]

    col_1=[z[0] for z in x]
    col_1

    col_4=[z[3:7] for z in x]
    col_4=[[y for y in z if ":" not in y] for z in col_4]
    col_4=[len(z) for z in col_4]
    col_4

    col_5=[z[5:]for z in x]
    col_5=[[o for o in z if ":" in o] for z in col_5]
    col_5=[[o[:-1] if "\n" in o else o for o in z]for z in col_5]
    col_5=[len(z) for z in col_5]
    col_5

    resultado=zip(col_1,col_4,col_5)
    
    return list(resultado)


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    x = open("data.csv", "r").readlines()
    x=[z.replace("\t",",") for z in x]
    x=[z.split(",")for z in x]

    dict_p11={}
    contador=0

    col_p11=[z[1:7] for z in x]
    col_p11=[[y for y in z if ":" not in y] for z in col_p11]
    col_p11=[[y for y in z if "-" not in y] for z in col_p11]
    col_p11=[[z[0],z[1:]] for z in col_p11]
    col_p11


    for i in col_p11:
        contador=int(i[0])
        for j in i[1]:
            if j in dict_p11:
                dict_p11[j]+=contador
            else:
                dict_p11[j]=contador     
    
    return dict_p11

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    x = open("data.csv", "r").readlines()
    x=[z.replace("\t",",") for z in x]
    x=[z.split(",")for z in x]

    lista_p12=[]
    contador=0
    dict_p12={}

    col_1=[z[0] for z in x]
    col_1

    col_5=[z[5:]for z in x]
    col_5=[[o for o in z if ":" in o] for z in col_5]
    col_5=[[o[:-1] if "\n" in o else o for o in z]for z in col_5]
    col_5=[[o[4:] for o in z]for z in col_5]
    col_5

    for i in col_5:
        contador=0
        for j in i:
            contador+=int(j)
        lista_p12.append(contador)
    lista_p12

    lista_p12_f=list(zip(col_1,lista_p12))
    lista_p12_f

    for a,b in lista_p12_f:
        if a in dict_p12:
            dict_p12[a]+=int(b)
        else:
            dict_p12[a]=int(b)
    
    return dict_p12
