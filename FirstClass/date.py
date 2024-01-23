import datetime

day = input("Introduce el dia de tu nacimiento: ")
mnth = input("Introduce el mes de tu nacimiento: ")
anio = input("Introduce el año de tu nacimiento: ")

fechaNacimiento = datetime.datetime(int(anio), int(mnth), int(day) )

fechaHoy = datetime.datetime.now()

diffFechas = fechaHoy - fechaNacimiento

print(f'{diffFechas.days} dias desde tu nacimiento')
