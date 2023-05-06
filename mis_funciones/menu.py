import re
from mis_funciones import funciones as f


def menu(text, stop):
    """

    :param text: String a trabajar
    :param stop: listado de stopwords elegidas
    :return: Debido a que yo presento el proyecto en un archivo .py y no en jupyter he preferido crear esta función
    para presentar los datos de manera más ordenada
    """
    estado = True
    while estado:

        print("Introduzca lo que desea ver del ejercicio")
        print("Si desea ver el texto original - 1")
        print("Si desea saber el número de palabras antes de normalizar - 2")
        print("Si desea ver todas las palabras que comienzan en mayúsculas (siglas incluidas) - 3")
        print("Si desea ver solo las siglas - 4")
        print("Si desea ver todas las palabras que contengan algún acento - 5")
        print("Si desea ver todos los signos de puntuación - 6")
        print("Si desea ver todos los números que aparecen - 7")
        print("Si desea ver el texto normalizado y su número de palabras - 8")
        print("Si desea ver las ocurrencias de cada palabra en el texto normalizado - 9")
        print("Si desea cerrar - 10")
        n = int(input(""))
        if n not in range(1,11):
            print("Lo siento, esa opción no era válida")
            print("\n")

        elif n == 1:
            print(text)

        elif n == 2:
            print(f.contarpalabras(text))

        elif n == 3:
            print(f.buscarprimeramayus(text))

        elif n == 4:

            print(f.buscarsiglas(text))

        elif n == 5:
            print(f.buscaracentos(text))

        elif n == 6:
            print(f.buscarpunt(text))

        elif n == 7:
            print(f.buscarnumeros(text))

        elif n == 8:
            text = re.sub("\n","",text)
            s = f.eliminaurluser(text)
            s = f.eliminapunt(s)
            s = f.minus(s)
            s = f.eliminanum(s)
            s = f.eliminastop(s, stop)
            s = f.susacents(s)

            a = f.contarpalabras(s)
            print(s)
            print(f"El texto normalizado tiene {a} palabras")

        elif n == 9:
            text1 = re.sub("\n", "", text)
            s = f.eliminapunt(text1)
            s = f.minus(s)
            s = f.eliminanum(s)
            s = f.eliminastop(s, stop)
            s = f.susacents(s)
            f.muestraOcurrencias(s)

        elif n == 10:
            print("Cerrando ")
            estado = False


