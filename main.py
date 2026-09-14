def mostrar_menu():
    print("=== Gerenciador de Tarefas ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("0 - Sair")


def main():
    tarefas = []
    while True:
        mostrar_menu()
        opcao = input("Escolha: ")
        print("Você escolheu:", opcao)

        if opcao == "1":
            descricao = input("Descreva a nova tarefa: ")
            tarefa = {
                "descricao": descricao,
                "concluida": False
}
            tarefas.append(tarefa)
            print("Tarefa adicionada com sucesso!")

        elif opcao == "2":
            if tarefas:
                for indice, tarefa in enumerate(tarefas, start=1):
                    print(indice, tarefa["descricao"], tarefa["concluida"])
            else:
                print("Nenhuma tarefa cadastrada.")

        elif opcao == "3":
            if tarefas:
                for indice, tarefa in enumerate(tarefas, start=1):
                    print(indice, tarefa["descricao"], tarefa["concluida"]) 
                indice =input("Digite a tarefa que deseja concluir:") 
                tarefas[int(indice)-1]["concluida"] = True
                print("Tarefa concluída com sucesso!")    
            else:
                print("Nenhuma tarefa cadastrada.")
            
            


        elif opcao == "4":
            print("Remover tarefa")

        elif opcao == "0":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
