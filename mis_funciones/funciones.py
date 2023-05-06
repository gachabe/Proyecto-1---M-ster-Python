import re



"""
Funciones auxiliares de expresiones regulares con las que normalizaremos el texto articulo.txt y haremos el análisis
de sentimientos de sentweets.txt
"""
#Funciones de conteo

def contarpalabras(text):
    """

    :param text: string a trabajar
    :return: nos devuelve el numero de palabras en el String text
    """
    s = text.split(" ")
    return len(s)
def muestraOcurrencias(text):
    contar_palabras = {}
    for palabra in text.split():
        if contar_palabras.get(palabra) is None:
            contar_palabras[palabra] = 0
        contar_palabras[palabra] = contar_palabras[palabra] + 1

    for c in contar_palabras.keys():
        print(c + ": " + str(contar_palabras[c]) + " ocurrencias")

#Funciones de busqueda y muestra

def buscarsiglas(text):
    """

    :param text: string a trabajar
    :return: Nos devolverá todas las palabras del string que esten completamente escritas en mayusculas
    """
    s = re.findall("[A-Z][A-Z]+",text)
    return s

def buscarprimeramayus(text):
    """

    :param text: string a trabajar
    :return: Nos devolverá todas las palabras que empiecen por mayusucla, incluye las palabras que sean totalmente
    mayuscula, como las siglas del apartado anterior, si no quisieramos las siglas bastaria quitar la primera forma
    de mi patrón de busqueda
    """
    s = re.findall("[A-Z][A-Z]+|[A-Z][a-z]+",text)
    return s

def buscarpunt(text):
    """

    :param text: String a trabajar
    :return: Nos devolverá todos los signos de puntuación del string
    """

    s =re.findall(r'[^\w\s]','',text)
    return s

def buscaracentos(text):
    """

    :param text: String a trabajar
    :return: Nos devolvera todos las palabras que contengan alguna letra con acento, tanto mayúscula como minúsucla
    """
    s = re.findall("[a-zA-Z]+[áéíóú][a-z]*|[ÁÉÍÓÚ][a-z]+",text)
    return s

def buscarnumeros(text):
    """

    :param text: String a trabajar
    :return: Nos devolverá todos los numeros escritos en cifra que aparezca, no aparecerá por tanto palabras como "tres"
    """
    s = re.findall("[0-9]+",text)
    return s
def buscaurl(text):
    """


    :return: Busca las urls posibles del texto
    """

    patron = "(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]" \
             "[a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\." \
             "[a-zA-Z0-9]+\.[^\s]{2,})"


    s = re.findall(patron, text)
    return s
def buscauser(text):
    """


       :return: Todos los usuarios expresados como @usuarioABC
       """
    patron = "\@[a-zA-Z0-9_ ]+"
    s = re.findall(patron, text)
    return s

#Funciones de sustitución y transfomación

def susacents(text):
    """

    :param text: String a trabajar
    :return: Nos devolerá el String sustituyendo cada vocal acentuada que aparezca por su versión sin acentuar
    """
    l = re.sub("á", "a", text)
    l = re.sub("é", "e", l)
    l = re.sub("í", "i", l)
    l = re.sub("ó", "o", l)
    l = re.sub("ú", "u", l)
    l = re.sub("É", "E", l)
    l = re.sub("Í", "I", l)
    l = re.sub("Ó", "O", l)
    l = re.sub("Ú", "U", l)
    l = re.sub("Á", "A", l)

    return l

def minus(text):
    """

    :param text: String a trabajar
    :return: convierte el string text a minusculas
    """
    s = text.lower()
    return s

def eliminanum(text):
    """

    :param text: String a trabajar
    :return: nos devuelve el string quitando todos los números escritos en cifra
    """
    s = re.sub("[0-9]*","",text)
    return s

def eliminapunt(text):
    """

    :param text: String a trabajar
    :return: Nos devuelve el mismo string pero sin signos de puntuación
    """

    s = re.sub(r'[^\w\s]','',text)
    return s

def eliminastop(text1,lista):
    """

    :param text1: String a trabajar
    :param lista: lista usada para guardar las palabras que queremos eliminar, en nuestro caso serán las stopwords
    :return: nos devuelve un string con las palabras del string original eliminando las pertenecientes a "lista"
    """
    s1 = text1.split(" ")

    aux = ""

    for i in s1:

        if i not in lista:

            aux += i+" "

    return aux

def eliminaurluser(text):
    patron1 =  "(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9]" \
             "[a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\." \
             "[a-zA-Z0-9]+\.[^\s]{2,})"

    patron2 = "\@[a-zA-Z0-9_]+"

    s = re.sub(patron1,"",text)
    s = re.sub(patron2,"",s)
    return s

def preparadoanalisis(text, stop):
    " Esta es una función para relajar la computación del análisis de sentiminetos haciendo una criba previa"
    s = re.sub("\n", "", text)
    s = eliminaurluser(s)
    s = re.sub("j[aeoujm]+","",s) # elimina las risas
    s = eliminapunt(s)
    s = minus(s)
    s = eliminastop(s, stop)
    s = eliminanum(s)
    return s

def sent(text,stop,sentP, sentN):
    """

    :param text: String a analizar
    :param stop: stopwords, se usra para relajar los cálculos
    :param sentP: lista donde los lugares pares son las palabras y los impares su valor, POSITIVO
    :param sentN: lista donde los lugares pares son las palabras y los impares su valor, NEGATIVO
    :return: el valor del analisis
    """
    s = preparadoanalisis(text,stop)
    acumP = 0
    acumN = 0
    for i in range(0,len(sentP),2):
        (s, num) = re.subn(sentP[i],"",s)
        if s != 0:
            acumP += num * float(sentP[i + 1])
    for i in range(0,len(sentN),2):
        (s,num) = re.subn(sentN[i],"",s)
        if s != 0:
            acumN += num * float(sentN[i + 1])
    return (f"El balance positivo es {acumP}, el balance negativo es {acumN}, el toal es {acumP+acumN}")
