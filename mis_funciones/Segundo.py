import re
from mis_funciones import funciones as f
import sys


#TEXTO
try:
    tweets_file = 'sentweets_esp.txt'
    file_s = open("data\\" + tweets_file, encoding="utf8")
    texto= file_s.read()
    file_s.close()
except IOError as error:
    print('Problema con el fichero: {}.  {}'.format(file_s, error) )
except:  # si es un error diferente a IOError
    print("Error inesperado:", sys.exc_info()[0])
    raise
#STOPWORDS
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


try:
    positive_file = 'positive_lex.txt'
    positive_s = open("data\\"+positive_file, encoding="utf8")
    sentpos = positive_s.read()
    listapos = re.split("\n|\s", sentpos)[0:-1]
    positive_s.close()
except IOError as error:
    print('Problema con el fichero: {}.  {}'.format(positive_s, error) )
except:  # si es un error diferente a IOError
    print("Error inesperado:", sys.exc_info()[0])
    raise


try:
    negative_file = 'negative_lex.txt'
    negative_s = open("data\\"+negative_file, encoding="utf8") # PASO 11 CONTROL DE EXCEPCIONES
    sentneg = negative_s.read()
    listaneg = re.split("\n|\s", sentneg)[0:-1]
    negative_s.close()
except IOError as error:
    print('Problema con el fichero: {}.  {}'.format(negative_s, error) )
except:  # si es un error diferente a IOError
    print("Error inesperado:", sys.exc_info()[0])
    raise

