import os


dirPath = "dirTest"

#----1ª forma de hacerlo----
#con el metodo isdir / isfile

directoriesForma1 =[]
filesForma1 = []
elements = os.listdir(dirPath)

for el in elements:
    if os.path.isdir(os.path.join(dirPath, el)):
        directoriesForma1.append(el)
    else:
        filesForma1.append(el)
print("Forma 1")
print(f"Directorios: {directoriesForma1}")
print(f"Archivos: {filesForma1}")
print("\n------------------------------------\n")


#----2ª forma de hacerlo----
#con el metodo walk

directoriesForma2 = []
filesForma2 = []
for (dirpath, dirnames, filenames) in os.walk(dirPath):
    directoriesForma2.extend(dirnames)
    filesForma2.extend(filenames)
print("Forma 2")
print(f"Directorios: {directoriesForma2}")
print(f"Archivos: {filesForma2}")

