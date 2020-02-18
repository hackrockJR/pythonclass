# Juan Romero

#netstel list

# Lista de listas

likedby = [10,14,21]

tweet = "Primer Mensaje"

lista =[1, "agonzalez", tweet]

lista.append(likedby)

# Print1

print (lista)

Resultado= lista[3]

# Print2

print(Resultado)

Resultado2 = lista [3][1]

# Print3
print(Resultado2)

#Tuplas inmutables

# A diferencia de las listas no se puede modificar sus valores

autor = "Juan Romero"
creditos = ("oferta",2016,autor)


# Print4
print (creditos)

#Eliminar la tuplas

#del creditos

# Diccionario
# Clave con valor


tweet2 = {"Autor": "Juan", "Fecha": "2020-02-18", "Texto": "Mi primer Mensaje"}
tweet3 = {"Autor": "Fernando", "Fecha": "2020-02-18", "Texto": "Mi Segundo Mensaje"}

Resultado3= tweet2["Autor"]

# Print5
print ("Nombre del autor en el diccionario=", Resultado3)

# Agregar los diccionarios a una lista

lista_tweets = [tweet2, tweet3]

#Print6

print (lista_tweets)

#Imprimir del diccionario 1 el autor

Resultado4= lista_tweets[0]["Autor"]

# Print7

print (Resultado4)

# Imprimir del diccionario 2 el autor 

Resultado5 = lista_tweets[1]["Autor"]

#Print8

print (Resultado5)

# RESULTADOS DE LOS 8 PRINT>

# [1, 'agonzalez', 'Primer Mensaje', [10, 14, 21]]
# [10, 14, 21]
# 14
# ('oferta', 2016, 'Juan Romero')
# Nombre del autor en el diccionario= Juan
# [{'Autor': 'Juan', 'Fecha': '2020-02-18', 'Texto': 'Mi primer Mensaje'}, {'Autor': 'Fernando', 'Fecha': '2020-02-18', 'Texto': 'Mi Segundo Mensaje'}]
# Juan
# Fernando

# Manipular Diccionarios 

# Actualizar elemento>


tweet2["Texto"] = "Mi primer tweet" 

Resultado6 = tweet2

print (Resultado6)

# Resultado6= {'Autor': 'Juan', 'Fecha': '2020-02-18', 'Texto': 'Mi primer tweet'}


# Eliminar Elemento

del tweet3 ["Autor"]

Resultado7 = tweet3

print (Resultado7)

# {'Fecha': '2020-02-18', 'Texto': 'Mi Segundo Mensaje'}

# Vaciar todo el diccionario

tweet2.clear()

Resultado8 = tweet2

print (Resultado8)

# {}

# Eliminar el diccionario

# del tweet2

# print (tweet2)

# REsultado> 
#     print (tweet2)
# NameError: name 'tweet2' is not defined

# Agregar una clave y valor  al diccionario

print (tweet3)

tweet3["Likes"]= 0

print (tweet3)

# Metodos para diccionario 

tweet4 = {"Autor": "Romero", "Fecha": "2020-02-18", "Texto": "Mi Tercer Mensaje"}

# Pendiente impresion de resultado de keys y values
# Se puede ver el resultado en el interprete 3.8 del Kali
# No me genera resultado en cmd o visual studio code en Windows 

clave= (tweet4.keys())
valor= (tweet4.values())

# Copiar un diccionario en otro sin ocupar mismo espacio en memoria

tweet5 = tweet4.copy ()

print ("Original", tweet4)
print ("Copia",tweet5)

tweet4["likes"]=2 
print ("Original con modificacion",tweet4)

print ("Copia sin ser alterado por el original",tweet5)

# Resultado> 

# Original {'Autor': 'Romero', 'Fecha': '2020-02-18', 'Texto': 'Mi Tercer Mensaje'}
# Copia {'Autor': 'Romero', 'Fecha': '2020-02-18', 'Texto': 'Mi Tercer Mensaje'}
# Original con modificacion {'Autor': 'Romero', 'Fecha': '2020-02-18', 'Texto': 'Mi Tercer Mensaje', 'likes': 2}
# Copia sin ser alterado por el original {'Autor': 'Romero', 'Fecha': '2020-02-18', 'Texto': 'Mi Tercer Mensaje'}

# Gnerar lista para recorrer el Diccionario usando items
# PENDIENTE mostar en pantalla , no me funciona con el comando print

#Listado= tweet4.items()

#print (Listado)

# otras Funciones 

Resultado11 = len(tweet4)
print(Resultado11)

Resultado12= str(tweet4)

print(Resultado12)

# Constantes 

# True
# False 
# None 

Activo = True
Desactivado = False
print("")
print (Activo)
print (Desactivado)

# Inicializar una variable con el valor nulo

apellidos = None

print("La variable apellidos No contiene ningun valor de inicio", apellidos)


















































































































