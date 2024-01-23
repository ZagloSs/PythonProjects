#El diccionario en cuestion
dict = {
    "name" : "Charles",
    "surname" : "Ten",
    "age": 21
}

#Leer sus datos
print(dict) #Imprime el diccionario entero
print(dict.values()) #Son los valores que pertenecen a cada clave
print(dict.keys()) #Son las claves
print(dict["name"]) #Imprime el valor de la clave name
print(dict["surname"]) #Imprime el valor de la clave surname
print(dict["age"]) #Imprime el valor de la clave age

#Actualizar sus datos
dict.update({"name": "si"})
dict["name"] = "si"

#Añadir datos
dict.update({"favourite_game": "Outer Wilds"})
print(dict)

