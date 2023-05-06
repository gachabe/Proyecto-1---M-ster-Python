from mis_funciones import Primero as p
from mis_funciones import menu as m
from mis_funciones import Segundo as s
from mis_funciones import funciones as f
from mis_funciones import Conclusiones as c

if __name__ == '__main__':
    print("Proyecto I ")
    print("Gabriel Chaves Benítez")
    eleccion = int(input("Qué ejercicio quiere ver\n"
                         "ejercicio 1 - 1\n"
                         "ejercicio 2 - 2\n"
                         "conclusiones - 3"))
    if eleccion == 1:
        m.menu(p.articulo, p.stopW)
    elif eleccion == 2:
        print(f.sent(s.texto, s.stopW, s.listapos, s.listaneg))
        m.menu(s.texto, s.stopW)
    else :
        c.concl()