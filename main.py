"""
Password
---
A simple program where you can store password, generator password, and chek how strong a password is.

Storing: Uses the keyring python module to store you password in your os's password manager.
Generator: Uses the python secrets lib to generate the password.
Checker: I created a custom python module that checks the password and used it.
"""
import os
import secrets
import sys
import winsound
from password_check import check_password
import keyring

def checker_mode():
    print("*######|Checker Mode|######*")
    print("----------------------------")
    check_password(input("Please enter your password\n----------------------------\n"))
    print("----------------------------")
    input("Press enter to continue...\n")
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    home_screen()

def pass_generator():
    print("*######|Password Generator|######*")
    password = secrets.token_urlsafe(16)
    print("----------------------------------")
    print("Password: ", password)
    print("----------------------------------")
    input("Press enter to continue...\n")
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    home_screen()

def pass_saver():
    print("*######|Password Saver|######*")
    print("-----------------------------")
    password = input("Please enter your password\n")
    print("-----------------------------")
    User_name = input("Please enter your username\n")
    print("-----------------------------")
    keyring.set_password(username=User_name, password=password, service_name="Password Vault")
    print("Password has been saved!")
    print("-----------------------------")
    input("Press enter to continue...\n")
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    home_screen()
def pass_get():
    print("*######|Password Fetcher|######*")
    print("-----------------------------")
    User_name = input("Please enter your username\n")
    print("-----------------------------")
    print(keyring.get_password(username=User_name, service_name="Password Vault"))
    print("-----------------------------")
    input("Press enter to continue...\n")
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    home_screen()

def home_screen():
    print("*######|Home screen|######*")
    print("-----------------------------")
    print("Welcome to Password Vault!\n")
    print("[C] Password checker")
    print("[G] Password generator")
    print("[S] Password saver")
    print("[D] Password get")
    print("[E] Exit")
    print("Protip: Click enter to return to main menu.")
    print("------------------------------")
    while True:
        command = input(">$ ").upper()
        if command == "C":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            checker_mode()
        elif command == "G":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            pass_generator()
        elif command == "S":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            pass_saver()
        elif command == "D":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            pass_get()
        elif command == "E":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            sys.exit()
        else:
            print("Unknown command!")

if not keyring.get_password(username="PasswordVaultUsr", service_name="Password Vault"):
    print("Oops!")
    print("Looks like its your first use!!!")
    print("Password Vault needs you to sign up so that you can access you saved passwords!")
    password = input("Enter your password: ")
    keyring.set_password(username="PasswordVaultUsr", service_name="Password Vault", password=password)
    print("Done! Taking you back to the main menu...")
    home_screen()
else:
    print("------------------------------------")
    print("######-Password Vault sign in-######")
    password = input("Enter your password: ")
    if password == keyring.get_password(username="PasswordVaultUsr", service_name="Password Vault"):
        print("Entering password vault...")
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        home_screen()
    else:
        print("Oops!")
        print("-----------------")
        print("WRONG PASSWORD!!!")
        print("-----------------")
        if os.name == "nt":
            for i in range(50):
                winsound.Beep(800, 200)
                winsound.Beep(1500, 200)
            sys.exit()
        else:
            sys.exit()


