def adicionar(lista, item):
    lista.append(item)

def remover(lista, item):
    lista.pop(item-1)

def mostrar(lista):
    if len(lista)==0:
        print("\nA lista está vazia.")
    else:
        print("")
        for n in range(len(lista)):
            print(n+1," - ",lista[n])

def concluir(lista,item):
    lista[item] = lista[item]+" ✓"

def removerconcluidos(lista):
    for n in range(0,len(lista)):
        for k in lista[n]:
            if k=="✓":
                remover(lista,n)

def editar(lista,item,tarefaeditada):
    lista[item] = tarefaeditada

def ordenar(lista):
    lista.sort(key=str.lower)

def qtd(lista):
    if len(lista)>1:
        return print("\nA lista possui",len(lista),"tarefas.")
    elif len(lista)==1:
        return print("\nA lista possui",len(lista),"tarefa.")
    else:
        return print("\nA lista está vazia.")

def tconcluidas(lista):
    concluidas = []
    for n in range(0,len(lista)):
        for k in lista[n]:
            if k=="✓":
                concluidas.append(lista[n])
    mostrar(concluidas)

def tpendentes(lista):
    pendentes = []
    a = 0
    for n in range(0,len(lista)):
        for k in lista[n]:
            if k=="✓":
                a = 1
        if a==0:
            pendentes.append(lista[n])
    mostrar(pendentes)

def salvararq(lista):
    with open("listadetarefas.txt", mode="w") as arquivo:
        for k in lista:
            arquivo.write(f"{k}\n")

def carregararq(lista):
    try:
        with open("listadetarefas.txt", mode="r") as arquivo:
            for k in arquivo:
                tarefa = k.strip()
                adicionar(lista, tarefa)
    except FileNotFoundError as e:
        print(f"Erro ao carregar arquivo: {e}\nFavor, salvar as tarefas antes de solicitar o carregamento.\n")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}\n")