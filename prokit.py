import os
import sys
import time

# রং সেট করা
green = "\033[1;32m"
white = "\033[1;37m"
red = "\033[1;31m"
cyan = "\033[1;36m"

def banner():
    os.system("clear")
    print(f"{green}======================================")
    print(f"{white}       WELCOME TO PRO-KIT v2.0")
    print(f"{cyan}      Developed by: @saeid9.90")
    print(f"{green}======================================")

def menu():
    banner()
    print(f"{white}1. {cyan}Update & Upgrade System")
    print(f"{white}2. {cyan}Check Device Info")
    print(f"{white}3. {cyan}Check Network/IP Info")
    print(f"{white}4. {cyan}Install Basic Packages")
    print(f"{white}0. {red}Exit")
    
    choice = input(f"\n{green}Select Option >> {white}")
    
    if choice == '1':
        os.system("pkg update && pkg upgrade -y")
    elif choice == '2':
        os.system("uname -a")
        input("\nPress Enter to back...")
    elif choice == '3':
        os.system("ifconfig")
        input("\nPress Enter to back...")
    elif choice == '4':
        os.system("pkg install python git php curl wget -y")
    elif choice == '0':
        sys.exit()
    else:
        print(f"{red}Invalid Choice!")
        time.sleep(1)
        menu()

if __name__ == "__main__":
    menu()

