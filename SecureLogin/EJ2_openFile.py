import os.path

filePath = "dirTest/file2"
#Si es un archivo entonces lo leo y muestro lo que hay dentro, si no, muestro un mensaje indicando que no es un archivo
print(open(filePath, "r").read()) if os.path.isfile(filePath) else print(f"{filePath} no es un archivo")