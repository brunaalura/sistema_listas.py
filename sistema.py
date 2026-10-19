"""Sistema de lista (CRUD) em Python: adicionar, listar, alterar e excluir itens."""

itens = []


def mostrar_lista():
    print("\n--- LISTA ---")
    if not itens:
        print("A lista está vazia.")
    else:
        for i, item in enumerate(itens, start=1):
            print(f"{i}. {item}")


def ler_posicao():
    """Pede o número do item e devolve o índice (ou None se inválido)."""
    try:
        numero = int(input("Número do item: "))
    except ValueError:
        print("Digite um número válido.")
        return None
    if 1 <= numero <= len(itens):
        return numero - 1
    print("Posição inexistente.")
    return None


def adicionar():
    nome = input("Novo item: ").strip()
    if nome:
        itens.append(nome)
        print("Item adicionado!")
    else:
        print("O item não pode ser vazio.")


def alterar():
    if not itens:
        print("Não há itens para alterar.")
        return
    mostrar_lista()
    pos = ler_posicao()
    if pos is not None:
        novo = input(f"Novo valor para '{itens[pos]}': ").strip()
        if novo:
            itens[pos] = novo
            print("Item alterado!")
        else:
            print("O item não pode ser vazio.")


def excluir():
    if not itens:
        print("Não há itens para excluir.")
        return
    mostrar_lista()
    pos = ler_posicao()
    if pos is not None:
        removido = itens.pop(pos)
        print(f"Item '{removido}' excluído!")


def menu():
    while True:
        print("\n===== MENU =====")
        print("1 - Adicionar")
        print("2 - Listar")
        print("3 - Alterar")
        print("4 - Excluir")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            adicionar()
        elif opcao == "2":
            mostrar_lista()
        elif opcao == "3":
            alterar()
        elif opcao == "4":
            excluir()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()