import os.path

filePath = "dirTest/file2"
print(open(filePath, "r").read()) if os.path.isfile(filePath) else print(f"{filePath} no es un archivo")