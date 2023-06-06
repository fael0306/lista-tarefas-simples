import liblistadetarefas

listadetarefas = []
op = 0

print("Escolha a opção desejada:")

while op != 4:
    try:
        op = int(input("\n\n1 - Adicionar\n2 - Remover\n3 - Mostrar\n4 - Encerrar\n"))
    except ValueError:
        print("Digite um número válido.")
        continue

    if op == 1:
        tarefa = input("\nTarefa que deseja adicionar: ")
        liblistadetarefas.adicionar(listadetarefas, tarefa)
    elif op == 2:
        try:
            tarefa = int(input("\nTarefa que deseja remover: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if 0 <= tarefa-1 < len(listadetarefas):
            liblistadetarefas.remover(listadetarefas, tarefa)
        else:
            print("Esta tarefa não existe.")
    elif op == 3:
        if len(listadetarefas) > 0:
            print("\nSegue a lista:\n")
            liblistadetarefas.mostrar(listadetarefas)
        else:
            print("\nA lista está vazia.")
    else:
        if op != 4:
            print("Digite uma opção válida.")