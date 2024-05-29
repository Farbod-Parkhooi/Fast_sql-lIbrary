try:
    from colorama import init, Fore
except: 
    print("use: pip install colorama")
    exit()
from os import system, mkdir
from platform import uname
from fast_sql import fast_sql
init()
try:
    mkdir("Importants")
except: pass
fsql = fast_sql("Importants/database.db", "users", ["username", "password", "os_release"])
fsql.connect()
Platform = uname()[0].lower()
if Platform == "windows": system("cls")
else: system("clear")
print("For read the passwords use 'admin' username and password(password: admin, username: admin)")
dir = input(Fore.GREEN + "[+] " + Fore.RESET + "Select an option(create/login): ").lower()
def admin():
    if Platform == "windows": system("cls")
    else: system("clear")
    print("Write users to see usernames.")
    def user_names():
            users = []
            user_list = list(fsql.Custome_command("SELECT username FROM users;"))
            for i in range(len(user_list)):
                users.append(user_list[i][0])
            users.remove("admin")
            print(Fore.GREEN + "--> " + Fore.RESET + "These are the usernames:")
            for i in range(len(users)):
                print("    " + Fore.GREEN + "[+] " + Fore.RESET + users[i])
    user_names()
    while True:
        command = input(Fore.GREEN + "[+] " + Fore.RESET + "write username: ")
        if command == "users": user_names()
        else: 
            try:
                password = str(fsql.Select_from("password", "username", command))[0][0]
                print(Fore.GREEN + f"The {command}'s password: " + Fore.RESET + password)
            except: print(Fore.RED + "Username not found!")
def Create(): 
    print("\n")
    print(Fore.BLUE + "Entering to login panel...\n")
    username = input(Fore.GREEN + "[+] " + Fore.RESET + "Enter your username: ").lower()
    password = input(Fore.GREEN + "[+] " + Fore.RESET + "Enter your password: ").lower()
    os_release = uname()[2]
    fsql.Insert_in([username, password, os_release])
    print(Fore.BLUE + "Account is created.")
    exit()
def Login(): 
    print("\n") 
    print(Fore.BLUE + "Entering to create account panel...")
    username = input(Fore.GREEN + "[+] " + Fore.RESET + "Enter your username: ").lower()
    password = input(Fore.GREEN + "[+] " + Fore.RESET + "Enter your password: ").lower()
    saved_password = fsql.Select_from("password", "username", username)
    try:
        saved_password = str(saved_password[0][0])
    except:
        print(Fore.RED + "User not found!")
        exit()
    if password == saved_password: print(Fore.GREEN + "Password is accepted.")
    else: print(Fore.RED + "Password is not acceptable."), exit()
    if username == "admin": admin()
if dir == "create": Create()
elif dir == "login": Login()
else: 
    print(Fore.RED + "Invalid Input!")
    exit()
