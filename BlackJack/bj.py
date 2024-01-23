import random

class Carta:
    def __init__(self, nombre, palo, valor):
        self.nombre = nombre
        self.palo = palo
        self.valor = valor

    def __str__(self):
        return f"{self.nombre}"



def repartir(who):
    who.append(baraja.pop())

def verCartas(who):
    for cartas in who:
        print (cartas)
def getValor(who):
    vl=0
    for cartas in who:
        vl+= cartas.valor
    return vl

manoJugador = []
manoMaquina = []

minBound = 1;
maxBound = 21;


#---Creación de la Baraja---
baraja = []
palos = ["bastos", "oros", "copas", "espadas"]
for palo in palos:
    for j in range(1,11):
        if j == 1:
            baraja.append(Carta(f"As de {palo}", palo, 1))
        elif j == 8:
            baraja.append(Carta(f"Sota de {palo}", palo, 10))
        elif j == 9:
            baraja.append(Carta(f"Caballo de {palo}", palo, 10))
        elif j == 10:
            baraja.append(Carta(f"Rey de {palo}", palo, 10))
        else:
            baraja.append(Carta(f"{j} de {palo}", palo, j))
random.shuffle(baraja)
#---Fin de creación de la baraja---



def finJuego():
    print("Veamos quien ha ganado...\n")
    print(f"El valor de tu mano ha quedado en {getValor(manoJugador)} puntos")
    print(f"El valor del crupier ha quedado en {getValor(manoMaquina)} puntos\n")

    if getValor(manoMaquina) == getValor(manoJugador):
        print("Ha habido un empate!")
    else:
        if maxBound >= getValor(manoJugador) >= minBound:
            if maxBound >= getValor(manoMaquina) >= minBound:
                if getValor(manoJugador) > getValor(manoMaquina):
                    print("Has ganado")
                else:
                    print("Ha ganado el curpier")
            else:
                print(f"ha ganado el jugador, el crupier se ha pasado de {maxBound}")
        elif maxBound >= getValor(manoMaquina) >= minBound:
                print(f"Ha ganado el crupier, te has pasado de {maxBound}")
        else:
            if getValor(manoJugador)>getValor(manoMaquina):
                print(f"Ambos os habeis pasado de {maxBound}, pero el que mas cerca ha estado fue udt, ha ganado")
            else:
                print(f"Ambos os habeis pasado de {maxBound}, pero el que mas cerca ha estado fue el crupier")


#---Repartir cartas iniciales---
for i in range(2):
    repartir(manoJugador)
    repartir(manoMaquina)
#---Fin de repartir cartas iniciales---
print("Se repartieron las cartas\n")
print("Tus cartas: \n")
verCartas(manoJugador)
print(f"\nEl valor total de tus cartas es de {getValor(manoJugador)}")

elect = 0

while not elect == 2:
    elect = int(input("1.Robar\n2.Plantarse: "))
    if elect == 1:
        repartir(manoJugador)
        print("Tus cartas son: \n")
        verCartas(manoJugador)
        print(f"\nEl valor de tus cartas es de {getValor(manoJugador)}")

        if getValor(manoJugador) > 21:
            elect = 2
            print("Vaya te has pasado...")

    elif elect == 2:
        print(f"Te plantaste con {getValor(manoJugador)} puntos")


print("Es el turno de la maquina")

elect = 0

while not elect == 2:
    if getValor(manoMaquina) < 16:
        repartir(manoMaquina)
    else:
        elect = 2

print("El crupuier se ha plantado")
finJuego()




































