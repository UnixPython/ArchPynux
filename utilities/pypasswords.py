#importaciones
import random
import secrets
import string

print(f"Welcome to Pypasswords!")

print("Inicio de sessión")

#input session
_pass_ = input("Ingrese el nombre: ")
passwd = input("Ingrese la contraseña: ")

#gen password
def gen_passw(longitud=12):
    caracteres = string.ascii_letters + string.digits
    return ''.join(secrets.choice(caracteres) for i in range(longitud))

# Verificación de credenciales
if _pass_ == "User11" and passwd == "Adb":
    print("Session iniciada")
    
    while True:
        print("1. Generar contraseña")
        print("2. Generar pin")
        print("3. Salir")
        op = input("Ingrese una opcion: ")
        
        if op == "1":
            usuario = input("Cree un usuario: ")
            print("Contraseña generada")
            print(gen_passw())
        elif op == "2":
            print("pin generado exitosamente")
            for _ in range(5):
                print(random.randint(1000, 9999))
        elif op == "3":
            print("Salido exitosamente")
            break
        else:
            print(f"Error: opción no válida")
else:
    print("Credenciales incorrectas. Session cerrada.")
