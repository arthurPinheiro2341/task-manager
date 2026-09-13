def mostrar_menu():
    print("=== Gerenciador de Tarefas ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("0 - Sair")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha: ")
        print("Você escolheu:", opcao)

        if opcao == "1":
            print("Adicionar tarefa")

        elif opcao == "2":
            print("Listar tarefas")

        elif opcao == "3":
            print("Concluir tarefa")

        elif opcao == "4":
            print("Remover tarefa")

        elif opcao == "0":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
