import os

dirPath = "dirTest"
archivo = "file2"
print(f"Quieres sobreescribir o añadir contenido a {archivo}")

elect = int(input("1. Sobreescribir, 2. Añadir: "))

if elect == 1:
    sobreescribir = open(os.path.join(dirPath, archivo), "w")
    sobreescribir.write(input(": "))
elif elect == 2:
    anadir = open(os.path.join(dirPath, archivo), "a")
    anadir.write(input(": "))
print("Archivo modificado")