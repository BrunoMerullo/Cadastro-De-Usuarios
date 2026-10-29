import platform
import os

def apagar_tela():
    plataforma = platform.platform()
    print(plataforma)
    if plataforma == "Windows":
        os.system("cls")
    else:
        os.system("clear")
        

