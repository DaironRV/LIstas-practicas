# listas intoduccon

# arrai = ["futbol", "pc", 18.7, 18, [5,5,8], True, False]


# # el "[5]", es el numeor de dato que necedito, en este caso es el true, comienzan desde el 0
# print(arrai[-3])

# # si quiero usar para solamente un bloque, se le agrega un rango.
# print(arrai[2:-1])

# lsitas mis cosas


# # se pueden llamar listas dentro de listas.
# musica = ["gitarra", "flauta", "violin"]

# deporte = ["futbol", "spining", "basquetbool"]

# comida = ["papa", "verduras", "pan"]

# Conjuntos = [comida, deporte, musica]

# conjuntos2 = [comida, deporte]

# conjuntos3 = [musica,deporte]


# print(musica)

# print(conjuntos2)


# listas

arrai = ["cosas de la vida", "de la vida cosas", 22, 20.2, ["hola", "que", "hace"], True, False, 22]

# funcion "len " es para contal la cantidad de datos que hay en una lista
print(len(arrai))

# la funcion append, es para agregar algo mas a la lista, al final
arrai.append(int(input("datoa a ingresar a la lsita: ")))
print(arrai)

# funcón .insert, es para colocar un dato en la posicion señalada: .insert(1,) (el 1 es la posicion que quieres poner el dato)
arrai.insert(1,int(input("dato en numero que deseas agregar a la lisne ne la posicón 1")))
print(arrai)



# si necesito agregar mas de  un dato en especifico, puedo usar la funcion .exted([]), ya agregar una lista a una lista basia
arrai2 = []

arrai2.extend([str(input("que valir tipo str deas aagregar: ")),
            int(input("que valor int deas agregar: ")),
            float(input("que valor tipo flotante deas agregar: ")),
            bool(input("que tipo de valor bool deas agregar: "))])
print(f"datos  que ingresaste: {arrai2}")
print(f"Datos que ingresaste junto a datos extras: {arrai2} {arrai}")


# puedes concatenar diferentes listas:

arra3 = [True, False, "pito", 44.5]
print(f"etas es otra lisat: {arra3}")

arra4 = arrai + arrai2 + arra3

print(f"esta es la convinacion que hiciste de lsistas: {arra4}")

# asi se pueden buscar cosas en una lista: 
busacar = input("que deseas buscar en las lista: ")
print(int(busacar) in arrai)


# asi se busca la posicion del dato en el index

buscarPosicion = int(input("dame el dato del que quieras saber su posición: "))

resultado = arrai.index(buscarPosicion)

print(resultado)

# asi se muestra cuantas veces esta repetido el dato en el la lista. 
cantidadVecesDato = int(input("cual es el dato que quieres saber que se repite: "))
resultadoCuentaDatos = arrai.count(cantidadVecesDato)
print(resultadoCuentaDatos)

# borrar daros de una lista: 
datoQueSeBorra = int(input("que dato numerico quieres borra: "))
resultadoEliminacion = arrai.remove(datoQueSeBorra)
print(arrai)


# asi se basia un arrai :
Acccion = input("que deas hacer: (solo existe la funcion clear) ")
if Acccion == "clear": 
    arrai.clear()
    print(arrai)
else: 
    print("solo se peude la funcion clrear")

