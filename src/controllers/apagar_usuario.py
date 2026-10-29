from controllers.cadastro_usuario import lista_usuarios
from controllers.apagar_tela import apagar_tela

def apagar():
    apagar_tela()
    nome_apagar = input("Digite o nome do usuário que deseja apagar: ")
    for i in lista_usuarios:
        if['nome'] == nome_apagar:
            lista_usuarios.remove(i)
            print(f"Usuário {nome_apagar} removido com sucesso!")
            break