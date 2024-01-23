import hashlib
import json

def getIndex(user_name):
    return usernames.index(user_name)


def hashing(str):
    encrypted = hashlib.sha256(str.encode()).hexdigest()
    return encrypted


def registro(nUser):
    okPass = False
    while not okPass:
        nPass = input("Introduce la contraseña: ")
        nPassVer = input("Repita la contraseña: ")

        if nPass == nPassVer:
            okPass = True
            introducirDatos(nUser, hashing(nPass))
            print("usuario registrado")
        else:
            print("Las contraseñas no coinciden")


def introducirDatos(name, passw):
    newUser = {
        "username": name,
        "password": passw
    }
    usersData["users"].append(newUser)
    writeable.write(json.dumps(usersData))


writeable = open("users.json", "r+")
users = open("users.json")
usersData = json.load(users)
usernames = []
for i in usersData['users']:
    usernames.append(i["username"])



print("------------SecLogCorp----------\n")
user_name = input("Introduzca su nombre de usuario: ")
if usernames.__contains__(user_name):
    passw = input("Introduzca su contraseña: ")
    if str(usersData["users"][getIndex(user_name)]["password"]) == hashing(passw):
        print("Contraseña correcta")
        print("Has entrado")
    else:
        print("contraseña incorrecta")

else:
    elect = input("ese nombre de usuario no esta registrado, quieres registrate?: ")
    if elect.lower() == "si":
        registro(user_name)

users.close()

