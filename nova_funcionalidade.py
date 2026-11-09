
def buscar_cliente(nome, clientes):
    for cliente in clientes:
        if cliente["nome"].lower() == nome.lower():
            print("Cliente encontrado!")
            print("Nome:", cliente["nome"])
            print("E-mail:", cliente["email"])
            return

    print("Cliente não encontrado!")
