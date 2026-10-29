from controllers.cadastro_usuario import dados
from controllers.apagar_tela import apagar_tela
from controllers.cadastro_usuario import dados
from controllers.listar_usuarios import listar
from controllers.apagar_usuario import apagar
from models.menu import opcao_menu
from models.menu import exibir_menu

import time


while True:
    apagar_tela()
    exibir_menu()
    x = opcao_menu()
    
    match x:
            case 1:
                dados()
                input("Pressione qualquer tecla para continuar...")
            case 2:
                listar()
                input("Pressione qualquer tecla para continuar...")
            case 3:
                apagar()
                input("Pressione qualquer tecla para continuar...")
            case 4:
                print("Até mais!")
                break
            case _:
                print("Está opção não existe!")
    

    