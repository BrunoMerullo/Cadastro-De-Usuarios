from time import sleep
from apagar_tela import apagar_tela

lista_usuarios = [{"nome": "Bruno Merullo", "idade": 17, "email": "dev.brunomerullo@gmail.com"}]
lista_usuarios.append({"nome": "Joao Amaral", "idade": 27, "email": "joaoamaral@hotmail.com"})

def dados():
    try:
        nome = str(input("Entre como seu nome: "))
        idade = int(input("Entre com sua idade: "))
        email = str(input("Entre com seu emaiil: "))
        try:
            apagar_tela()
            lista_usuarios.append([{"nome": nome, "idade": idade, "email": email}])
            print(f"Usuário, {nome}. Criado com sucesso!")
            
            
            sleep(2)
            
        except ValueError:
            print("Erro ao criar Usuário, verifique log e tente novamente!")
    except:
        print("Erro ao executar função de criar usuário")








