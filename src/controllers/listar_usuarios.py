from controllers.cadastro_usuario import lista_usuarios

def listar():
    print("Lista de Usuários!\n")
    
    for usuario in lista_usuarios:
        if not isinstance(usuario, dict):
            print(f"Registro inválido: {usuario!r}")
        else:
            print(
                f"Nome: {usuario['nome']}, "
                f"Idade: {usuario['idade']}, "
                f"Email: {usuario['email']}"
            )
    print("\nFim da lista de usuários!")
listar()