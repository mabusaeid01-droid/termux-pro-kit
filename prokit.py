import os
print("\033[1;32m") # সবুজ রঙ
print("==============================")
print("   WELCOME TO PRO-KIT v1.0   ")
print("      BY: @saeid9.90         ")
print("==============================")
print("\033[0m")
print("1. Update System")
print("2. Exit")
opt = input("\nChoose: ")
if opt == '1':
    os.system("pkg update && pkg upgrade -y")
else:
    exit()
