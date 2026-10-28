from cadastro_usuario import lista_usuarios

def listar_usuarios():
    print("Lista de Usuários!")
    for i in lista_usuarios:
        print(f"Nome: {i['nome']} | Idade: {i['idade']} | Email: {i['email']}")

lista_usuarios()