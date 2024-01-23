import os.path

dirPath = "dirTest"
archivoNombre = "archivoCreado"

#Se crea el archivo si no existe y se introduce el mensaje, si existe salta un error
archivo = open(os.path.join(dirPath, archivoNombre), "x")
archivo.write("y whats up")

print("Archivo creado")

