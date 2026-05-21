"""
Password checker
---
Checks the user password by having three cats:
    Must be over 6 chars
    Must contain 1 capital letter
    Must contain 1 lowercase letters
    Must contain digits
    Must contain special characters
"""

letters = "abcdefghijklmnopqrstuvwxyz"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789" # I know I could've done isdigit() but at the time I lowkey forgot that existed.
special_char = "/<>[]{}=-+()~`':;\\*&^%$#@"
special_char += '"'

from colorprint import cprint # Hehe I also made ts module

def check_password(password):
    checks = [] # Might use this later for logging in a file or something idk that's why I just saved it in dict.
    print("----------------------------")
    if password == "":
        cprint("There's no password you silly!", "yellow+italic")
        return
    if any(char in capital for char in password):
        checks.append("Capital Letter Check [OK]\n")
    else:
        checks.append("Capital Letter Check [NO]\n")
    if any(char in digits for char in password):
        checks.append("Number Check [OK]\n")
    else:
        checks.append("Number Check [NO]\n")
    if any(char in letters for char in password):
        checks.append("The Alpha Check [OK]\n")
    else:
        checks.append("The Alpha Check [NO]\n")
    if any(char in special_char for char in password):
        checks.append("Special Char Check [OK]\n")
    else:
        checks.append("Special Char Check [NO]\n")
    if len(password) > 6:
        checks.append("Len Check [OK]\n")
    else:
        checks.append("Len Check [NO]\n")
    for check in checks:
        if check.endswith("[OK]\n"):
            cprint(check, "green")
        else:
            cprint(check, "red")
