import os
import sys
import time

# Colors
green = "\033[1;32m"
white = "\033[1;37m"
red = "\033[1;31m"
cyan = "\033[1;36m"
yellow = "\033[1;33m"

def banner():
    os.system("clear")
    print(f"{cyan}")
    print("  ____    _      _____ ___ ____   ___  ")
    print(" / ___|  / \    | ____|_ _|  _ \ / _ \ ")
    print(" \___ \ / _ \   |  _|  | || | | | (_) |")
    print("  ___) / ___ \  | |___ | || |_| |\__, |")
    print(" |____/_/   \_\ |_____|___|____/   /_/ ")
    print(f"{yellow}      Termux Pro-Kit v2.0 | By: @saeid9.90")
    print(f"{green}========================================")

def menu():
    banner()
    print(f"{white}[1] {cyan}System Update & Upgrade")
    print(f"{white}[2] {cyan}Device System Info")
    print(f"{white}[3] {cyan}Network/IP Details")
    print(f"{white}[4] {cyan}Install All Basic Packages")
    print(f"{white}[0] {red}Exit")
    
    choice = input(f"\n{green}Select Option >> {white}")
    
    if choice == '1':
        os.system("pkg update && pkg upgrade -y")
    elif choice == '2':
        print(f"\n{yellow}--- Device Info ---")
        os.system("uname -a")
        input(f"\n{green}Press Enter to return...")
        menu()
    elif choice == '3':
        print(f"\n{yellow}--- Network Info ---")
        os.system("ifconfig")
        input(f"\n{green}Press Enter to return...")
        menu()
    elif choice == '4':
        print(f"\n{yellow}Installing basics... please wait.")
        os.system("pkg install python git php curl wget nano -y")
        print(f"{green}Done!")
        time.sleep(2)
        menu()
    elif choice == '0':
        print(f"{red}Exiting... Goodbye!")
        sys.exit()
    else:
        print(f"{red}Invalid Selection!")
        time.sleep(1)
        menu()

if __name__ == "__main__":
    menu()
