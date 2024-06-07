contatos = {}

def listar_contato():
    if contatos:
        print("Lista de contatos:")
        for contatoID, (contatoNome, contatoNumero) in contatos.items():
            print(f"ID: {contatoID}, NOME: {contatoNome}, NÚMERO: {contatoNumero}")

    else:
        print("Não há contatos registrados!")

def pesquisar_contato():
    if len(contatos) > 0:
        try:
            contatoID = int(input("Digite o id do contato a ser pesquisado: ").strip())
            if contatoID in contatos:
                contatoID, contatoNome, contatoNumero = contatos[contatoID]
                print("Contato encontrado com sucesso!")
                print(f"ID: {contatoID}, NOME: {contatoNome}, NÚMERO: {contatoNumero}")

            else:
                print("Contato não encontrado!")

        except ValueError:
            print("ID invalido!")

    else:
        print("Não há contatos registrados!")

def adcionar_contato():
    try:
        contatoNome = input("Digite o nome do contato: ").title().strip()

    except ValueError:
        print("Opção invalida!")
        return -1

    try:
        contatoNumero = input("Digite o número do contato: ").strip()

    except ValueError:
        print("Opção invalida!")
        return -1

    try:
        contatoID = int(input("Digite o id do seu contato: ").strip())

    except ValueError:
        print("Opção invalida!!!")
        return -1

    if contatoID in contatos:
        print("Contato já registrado! Tente adicionar com outro ID.")
        return

    contatos[contatoID] = (contatoNome, contatoNumero)
    print("Contato salvo com sucesso!")

def remover_contato():
    if contatos:
        try:
            contatoID = int(input("Digite o id do contato há ser removido: ").strip())
            if contatoID in contatos:
                del contatos[contatoID]
                print("Contato removido com sucesso!")

        except ValueError:
            print("Opção invalida!")

    else:
        print("Não há contatos registrados!")

def opcao_menu():
    try:
        return int(input("Digite a opção requerida, 1 Listar, 2 Pesquisar, 3 Adicionar, 4 Remover, 0 Sair: ").strip())

    except ValueError:
        print("Opção invalido!")
        return -1

opcao = opcao_menu()

while opcao != 0:
    if opcao == 1:
        listar_contato()

    elif opcao == 2:
        pesquisar_contato()

    elif opcao == 3:
        adcionar_contato()

    elif opcao == 4:
        remover_contato()

    else:
        print("Opção invalida!")

    opcao = opcao_menu()

print("Obrigado por usar o sistema de gerenciamento de contatos!")