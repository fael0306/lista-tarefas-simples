import liblistadetarefas

listadetarefas = []

while True:
    print("\nEscolha a opção desejada:")
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Mostrar")
    print("4 - Marcar como concluído")
    print("5 - Remover concluídos")
    print("6 - Encerrar")

    try:
        op = int(input())
    except ValueError:
        print("Digite um número válido.")
        continue

    if op == 1:
        tarefa = input("\nTarefa que deseja adicionar: ")
        liblistadetarefas.adicionar(listadetarefas, tarefa)
    elif op == 2:
        try:
            indice = int(input("\nÍndice da tarefa que deseja remover: ")) - 1
        except ValueError:
            print("Digite um número válido.")
            continue
        liblistadetarefas.remover(listadetarefas, indice)
    elif op == 3:
        liblistadetarefas.mostrar(listadetarefas)
    elif op == 4:
        try:
            indice = int(input("\nÍndice da tarefa que deseja marcar como cuncluída: ")) - 1
        except ValueError:
            print("Digite um número válido.")
            continue
        liblistadetarefas.concluir(listadetarefas, indice)
    elif op == 5:
        liblistadetarefas.removerconcluidos(listadetarefas)
    elif op == 6:
        break
    else:
        print("Digite uma opção válida.")
