import os.path

dirPath = "dirTest"
archivoNombre = "archivoCreado"

archivo = open(os.path.join(dirPath, archivoNombre), "x")
archivo.write("y whats up")

print("Archivo creado")

