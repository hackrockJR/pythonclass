#print("Hola")
#print("Bienvenido al curso de Python")
#print ("Cambio desde Kali en la empresa1")
#print ("Cambio desde Windows en la empresa1")


#Crear una lista con variables y mensaje a imprimir
lista1= [0,1,2,3,4]

print("Este es el resultado de la lista ", lista1[3])

# Variable len permite enumerar de la lista o cadena de caracteres
Resultado= len(lista1)

print ("Total de la lista=", Resultado)

#Modificar lista 

lista1[4] = "Ultimo"

print (lista1)

lista2 = [1,"user", "mensaje"]

lista2.append("Fecha")

print (lista2)

# Agregar a la lista a partir de una posicion indicada (n,"valor agregar")

lista2.insert(2,"Insertado")

# 2 es la posicion e insertado el valor agregar

print (lista2)

# Eliminar el ultimo elemento 

lista2.pop()

print (lista2)





















