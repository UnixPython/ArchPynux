import getpass
import random
import string

MAX_TRIES = 3


# ------------------------
# GUARDAR USUARIO
# ------------------------
def save_user(username, password):
    with open("users.txt", "a") as f:
        f.write(f"{username}:{password}\n")


# ------------------------
# VERIFICAR SI EXISTE
# ------------------------
def user_exists(username):
    try:
        with open("users.txt", "r") as f:
            for line in f:
                user = line.strip().split(":")[0]
                if user == username:
                    return True
    except FileNotFoundError:
        return False
    return False


# ------------------------
# REGISTRO
# ------------------------
def register_user():
    username = input("New user: ")

    if user_exists(username):
        print("User already exists")
        return

    password = getpass.getpass("New password: ")

    save_user(username, password)
    print("[+] User created")


# ------------------------
# LOGIN
# ------------------------
def login_user(username, password):
    try:
        with open("users.txt", "r") as f:
            for line in f:
                try:
                    user, pwd = line.strip().split(":")
                except ValueError:
                    continue

                if user == username and pwd == password:
                    return True
    except FileNotFoundError:
        return False

    return False


# ------------------------
# LOGIN FLOW
# ------------------------
def login_flow():
    attempts = 0

    while attempts < MAX_TRIES:
        username = input("User: ")
        password = getpass.getpass("Password: ")

        if login_user(username, password):
            print("ACCESS GRANTED")
            return True
        else:
            print("ACCESS DENIED")
            attempts += 1

    print("Too many attempts")
    return False


# ------------------------
# GENERAR PASSWORD
# ------------------------
def generate_password(length=12):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


# ------------------------
# GENERAR OTP
# ------------------------
def generate_otp(length=6):
    return ''.join(str(random.randint(0, 9)) for _ in range(length))


# ------------------------
# MENU
# ------------------------

def banner():
    print("""
██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗
██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝ ╚████╔╝ ██████╔╝███████║███████╗███████╗
██╔═══╝   ╚██╔╝  ██╔═══╝ ██╔══██║╚════██║╚════██║
██║        ██║   ██║     ██║  ██║███████║███████║
╚═╝        ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
        [ Security Toolkit v1.0 ]
     --------------------------------
""")

def menu():
    while True:
        banner()
        print("\n=== MENU ===")
        print("1. Register")
        print("2. Login")
        print("3. Generate Password")
        print("4. Generate OTP")
        print("5. Exit")

        option = input("Select option: ")

        if option == "1":
            register_user()

        elif option == "2":
            login_flow()

        elif option == "3":
            pwd = generate_password()
            print(f"Generated password: {pwd}")

        elif option == "4":
            otp = generate_otp()
            print(f"OTP: {otp}")

        elif option == "5":
            print("Bye")
            break

        else:
            print("Invalid option")


# ------------------------
# ENTRY POINT
# ------------------------
if __name__ == "__main__":
    menu()
