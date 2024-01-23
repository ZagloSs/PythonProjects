from pathlib import Path

archivo = input("de que archivo quieres saber la extension?: ")

sufijos = Path(archivo).suffixes

print(sufijos)

