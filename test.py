import re
import os
import random
import string
def check_password_strength(password):
    strength = 0
    if re.search("[\u0600-\u06FF]", password):
        print("dont Arabic")
        exit()
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    return strength
def menu():
    print("Home Of Project\n")
    print("1 - Check password strength")
    print("2 - Create a strong password")
    print("0 - Exit")
    choice = input("Put Number of Choice: ")
    match choice:
        case "1":
            os.system("cls")
            password = input("Put Your Password : ")
            os.system("cls")
            strength = check_password_strength(password)
            if strength == 5:
                print("Password is strong✅\n")
            elif strength >= 3:
                print("Password is average🟢\n")
            else:
                print("Password is weak📛\n")      
        case "2":
            os.system("cls")
            letters = ''.join(random.choices(string.ascii_letters, k=2))
            symbols = ''.join(random.choices("@#$&*", k=random.choice([2, 3])))
            digits_count = 12 - len(letters) - len(symbols)
            digits = ''.join(random.choices(string.digits, k=digits_count))
            password = letters + digits + symbols
            print("Your Password:", password)
            exit()
        case "0":
            print("Exit!")
            return
        case _:
            os.system("cls")
            print("Invalid option, Please Try Again:")
    menu()
menu()
