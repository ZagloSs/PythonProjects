import random

if __name__ == '__main__':
    print("Adivina un numero aleatorio entre 0 y 100")
    numRand = random.randint(1, 100)
    exit = False

    player = input("Elige un numero del 1 al 100: ")

    while not exit:
        if int(player) == numRand:
            print("Acertaste!")
            exit = True
        elif int(player) > numRand:
            player = input("Prueba un numero mas pequeño: ")
        else:
            player = input("Prueba un numero mas grande: ")




