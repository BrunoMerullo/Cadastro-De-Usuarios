lista_usuarios = [{"nome": "Bruno Merullo", "idade": 7, "email": "dev.brunomerullo@gmail.com"}]

def dados():
    try:
        nome = str(input("Entre como seu nome: "))
        idade = int(input("Entre com sua idade: "))
        email = str(input("Entre com seu emaiil: "))
        try:
            lista_usuarios.append([{"nome": nome, "idade": idade, "email": email}])
            print(f"Usuário, {nome}. Criado com sucesso!")
        except ValueError:
            print("Erro ao criar Usuário, verifique log e tente novamente!")
    except:
        print("Erro ao executar função de criar usuário")




