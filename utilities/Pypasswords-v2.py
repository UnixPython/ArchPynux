import random
import secrets
import string

print("Welcome to Pypasswords!")

# Sesión
print("Inicio de sesión")
passw = input("Ingrese el nombre de usuario: ")
passwd = input("Ingrese la contraseña de entrada: ")

# Función para generar contraseña
def gen_passw(long=12):
    caracters = string.ascii_letters + string.digits
    return "".join(secrets.choice(caracters) for i in range(long))

# Credenciales de usuario
if passw == "User11" and passwd == "Adb":
    print("Usuario conectado.")
    passwords = []  # Lista vacía

    while True:
        print("\n=== MENÚ DE CONSOLA ===")
        print("1. Generar contraseña")
        print("2. Generar pin")
        print("3. Crear contraseña")
        print("4. Ver credenciales creados del usuario")
        print("5. Ver historial de la contraseña creada")
        print("6. Borrar historial")
        print("7. Salir")
        op = input("Ingrese una opción: ")

        # Opciones del menú
        if op == "1":
            print("Ha seleccionado Generar contraseña.")
            create = input("Usuario: ")
            password_generada = gen_passw()  # Genera UNA SOLA vez
            print("Nombre creado exitosamente!", create)
            print("Contraseña generada:", password_generada)
            passwords.append(f"Usuario: {create} | Contraseña: {password_generada}")

        elif op == "2":
            print("Ha seleccionado Generar pin.")
            print("Pines generados exitosamente:")
            for _ in range(4):
                print(random.randint(1000, 9999))

        elif op == "3":
            print("Ha seleccionado Crear contraseña.")
            op_user = input("Usuario: ")
            op_passwd = input("Contraseña: ")
            print(f"Usuario: {op_user}")
            print(f"Contraseña: {op_passwd}")
            print("ID de usuario:", id(op_user))
            passwords.append(f"Usuario: {op_user} | Contraseña: {op_passwd}")

        elif op == "4":
            print("Ha seleccionado ver credenciales creados del usuario.")
            create_polity = input("Usuario: ")
            create_passwd = input("Contraseña: ")  # Ahora pregunta la contraseña
            passwords.append(f"Usuario: {create_polity} | Contraseña: {create_passwd}")
            print("ID OTP Generada por ram:", id(create_polity))
            print("Usuario creado")

        elif op == "5":
            print("Ha seleccionado Ver historial de la contraseña generada.")
            if len(passwords) == 0:
                print("No hay historial.")
            else:
                print("\n--- HISTORIAL ---")
                for element in passwords:
                    print(element)

        elif op == "6":
            print("Ha seleccionado borrar historial")
            passwords.clear()
            print("Historial borrado exitosamente")

        elif op == "7":
            print("Saliendo exitosamente.")
            break

        else:
            print("Error de entrada. Por favor seleccione una opción válida.")

else:
    print("Credenciales incorrectas. Acceso denegado.")
