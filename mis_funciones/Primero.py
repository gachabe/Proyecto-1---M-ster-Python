import sys
from mis_funciones import menu as m

try:
    ruta = 'articulo.txt'
    archivo = open("data\\" + ruta, encoding="utf8")
    articulo = archivo.read()
    archivo.close()
except IOError as error:
    print('Problema con el fichero: {}.  {}'.format(ruta, error))
except:  # si es un error diferente a IOError
    print("Error inesperado:", sys.exc_info()[0])
    raise



try:
    ruta2 = 'stopwords_español.txt'
    file = open("data\\" + ruta2, encoding="utf8")
    stopW = file.read().split("\n")
    file.close()
except IOError as error:
    print('Problema con el fichero: {}.  {}'.format(ruta2, error))
except:  # si es un error diferente a IOError
    print("Error inesperado:", sys.exc_info()[0])
    raise



