
clientes = []

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o e-mail do cliente: ")

    cliente = {
        "nome": nome,
        "email": email
    }

    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    print("\n--- CLIENTES CADASTRADOS ---")

    for cliente in clientes:
        print(f"Nome: {cliente['nome']}")
        print(f"E-mail: {cliente['email']}")
        print("----------------------")

cadastrar_cliente()
listar_clientes()
