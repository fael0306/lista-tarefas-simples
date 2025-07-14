import liblistadetarefas

listadetarefas = []

def menu_gerenciar():
    print("\nGerenciar Tarefas:")
    print("1 - Adicionar")
    print("2 - Remover")
    print("3 - Editar")
    print("4 - Marcar como concluído")
    print("5 - Remover concluídas")

def menu_exibir():
    print("\nExibir Tarefas:")
    print("1 - Todas")
    print("2 - Concluídas")
    print("3 - Pendentes")
    print("4 - Contar tarefas")

def menu_organizar():
    print("\nOrganizar Tarefas:")
    print("1 - Ordenar alfabeticamente")

def menu_arquivo():
    print("\nArquivo:")
    print("1 - Salvar")
    print("2 - Carregar")

while True:
    print("\nMenu Principal:")
    print("1 - Gerenciar Tarefas")
    print("2 - Exibir Tarefas")
    print("3 - Organizar Tarefas")
    print("4 - Arquivo")
    print("5 - Encerrar")

    try:
        op = int(input("Escolha a opção desejada: "))
    except ValueError:
        print("Digite um número válido.")
        continue

    if op == 1:
        menu_gerenciar()
        try:
            subop = int(input("Escolha a opção: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if subop == 1:
            tarefa = input("Tarefa que deseja adicionar: ")
            liblistadetarefas.adicionar(listadetarefas, tarefa)
        elif subop == 2:
            try:
                indice = int(input("Índice da tarefa que deseja remover: ")) - 1
                liblistadetarefas.remover(listadetarefas, indice)
            except ValueError:
                print("Digite um número válido.")
        elif subop == 3:
            try:
                indice = int(input("Índice da tarefa que deseja editar: ")) - 1
                novatarefa = input("Nova descrição da tarefa: ")
                liblistadetarefas.editar(listadetarefas, indice, novatarefa)
            except ValueError:
                print("Digite um número válido.")
        elif subop == 4:
            try:
                indice = int(input("Índice da tarefa que deseja concluir: ")) - 1
                liblistadetarefas.concluir(listadetarefas, indice)
            except ValueError:
                print("Digite um número válido.")
        elif subop == 5:
            liblistadetarefas.removerconcluidos(listadetarefas)

    elif op == 2:
        menu_exibir()
        try:
            subop = int(input("Escolha a opção: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if subop == 1:
            liblistadetarefas.mostrar(listadetarefas)
        elif subop == 2:
            liblistadetarefas.tconcluidas(listadetarefas)
        elif subop == 3:
            liblistadetarefas.tpendentes(listadetarefas)
        elif subop == 4:
            liblistadetarefas.qtd(listadetarefas)

    elif op == 3:
        menu_organizar()
        try:
            subop = int(input("Escolha a opção: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if subop == 1:
            liblistadetarefas.ordenar(listadetarefas)

    elif op == 4:
        menu_arquivo()
        try:
            subop = int(input("Escolha a opção: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if subop == 1:
            liblistadetarefas.salvararq(listadetarefas)
        elif subop == 2:
            liblistadetarefas.carregararq(listadetarefas)

    elif op == 5:
        print("Encerrando programa... Até logo!")
        break
    else:
        print("Digite uma opção válida.")
