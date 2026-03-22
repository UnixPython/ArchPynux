import random
import secrets
import string

def gen_passw(long=12):  # Función de creación de contraseña de 12 dígitos
    caracters = string.ascii_letters + string.digits  # ✅ PUNTO, no coma
    return "".join(secrets.choice(caracters) for i in range(long))

def validation_menu():
    # Validación de entrada
    while True:  # Loop infinito
        try:  # Manejo de error
            op = input("Ingrese una opción: ")
            if op not in ["1", "2", "3", "4", "5", "6"]:  # Lista de operador negativo
                raise ValueError("Opción no válida")
            return op
        except ValueError as e:  # ✅ ValueError con V mayúscula
            print(f"Error: {e}. Intente de nuevo")  # Mensaje de error

print("=== WELCOME TO Pypasswords! ===")
print("Inicio de sesión")

# Validación de manejo de errores y entradas
intentos = 3  # Cantidad de veces = 3
while intentos > 0:  # Mayor a 0
    try:
        passw = input("Ingrese el nombre de usuario: ")
        passwd = input("Ingrese la contraseña: ")

        if not passw or not passwd:
            raise ValueError("Usuario o contraseña incorrectos o vacíos")
        
        if passw == "user11" and passwd == "Adb":  # Booleano true
            print("Usuario conectado.")
            break
        else:
            intentos -= 1  # Resta un intento
            if intentos > 0:
                print(f"Credencial incorrecta. Intentos restantes: {intentos}")
            else:
                print("ACCESS DENIED!!!")
                exit()  # Sale del programa
    
    except ValueError as e:
        print(f"Error: {e}")
        intentos -= 1

else:
    print("Se alcanzó el límite de intentos.")
    exit()  # Sale del programa

passwords = []  # ✅ Lista vacía (era 'paswords')

while True:
    try:
        print("\n=== MENÚ ===")
        print("1. Generar contraseña")
        print("2. Generar pin")
        print("3. Crear contraseña")
        print("4. Buscar credencial")
        print("5. Ver historial de contraseñas")
        print("6. Salir")

        op = validation_menu()

        if op == "1":
            print("Ha seleccionado Generar contraseña.")
            create = input("Usuario: ").strip()  # Borra espacios

            if not create:
                raise ValueError("El nombre de usuario no puede estar vacío")

            new_pass = gen_passw()
            print(f"Nombre creado: {create}")
            print(f"Contraseña generada: {new_pass}")
            passwords.append({"usuario": create, "contraseña": new_pass})
        
        elif op == "2":
            print("Ha seleccionado Generar pin.")
            counts = int(input("¿Cuántos pines desea generar? (máx 10): "))

            if counts <= 0 or counts > 10:  # ✅ 'counts' no 'cantidad'
                raise ValueError("Cantidad aceptada entre 1 y 10")

            print("Pines generados:")
            for i in range(counts):
                print(random.randint(1000, 9999))  # Genera pin

        elif op == "3":
            print("Ha seleccionado Crear contraseña.")
            op_user = input("Usuario: ").strip()  # Borra espacios
            op_passwd = input("Contraseña: ").strip()

            if not op_user or not op_passwd:  # ✅ 'op_user' no 'op user'
                raise ValueError("Usuario y contraseña no pueden estar vacíos")

            if len(op_passwd) < 4:
                raise ValueError("La contraseña debe tener al menos 4 caracteres")

            print(f"Usuario: {op_user}")
            print(f"Contraseña: {op_passwd}")
            passwords.append({"usuario": op_user, "contraseña": op_passwd})
            print("✅ Credencial guardada exitosamente")

        elif op == "4":
            print("Ha seleccionado Buscar credencial.")
            
            if len(passwords) == 0:  # len con valor 0
                print("No hay credenciales guardadas.")
                continue  # Sigue a la siguiente línea

            buscar = input("Buscar usuario: ").strip()  # ✅ 'buscar' no 'browser'
            encontrado = False  # ✅ 'encontrado' no 'ops'

            for cred in passwords:  # Iteración
                if cred["usuario"] == buscar:
                    print(f"✅ Encontrado - Usuario: {cred['usuario']}, Contraseña: {cred['contraseña']}")
                    encontrado = True
                    break

            if not encontrado:
                print("❌ Usuario no encontrado")

        elif op == "5":
            print("Ha seleccionado Ver historial.")
            
            if len(passwords) == 0:
                print("No hay credenciales guardadas.")
            else:
                print("\n--- HISTORIAL DE CREDENCIALES ---")
                for i, cred in enumerate(passwords, 1):
                    print(f"{i}. Usuario: {cred['usuario']} | Contraseña: {cred['contraseña']}")

        elif op == "6":
            confirm = input("¿Desea salir? (s/n): ").lower()  # ✅ 'confirm' no 'conf'

            if confirm == "s":
                print("Saliendo exitosamente...")
                break
            else:
                print("Operación cancelada.")
                continue

    # Manejo de excepciones errores
    except ValueError as e:  # Excepción de error
        print(f"Error de validación: {e}")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
        break
    except Exception as e:
        print(f"Error inesperado: {e}")
