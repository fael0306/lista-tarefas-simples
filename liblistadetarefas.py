from datetime import date, timedelta

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

def addvencimento(lista, item, data):
    if item >= 1 and item <= len(lista):
        lista[item - 1]['data_vencimento'] = data
        print("Data de vencimento adicionada com sucesso.")
    else:
        print("Número de tarefa inválido.")

def agruparprazo(lista):
    hoje = date.today()
    grupos = {
        'Sem prazo': [],
        'Menos de uma semana': [],
        'Menos de duas semanas': [],
        'Mais de duas semanas': [],
        'Mais de um mês': []
    }

    for tarefa in lista:
        if 'data_vencimento' in tarefa:
            data_vencimento = tarefa['data_vencimento']
            if data_vencimento <= hoje:
                grupos['Sem prazo'].append(tarefa)
            elif data_vencimento <= hoje + timedelta(days=7):
                grupos['Menos de uma semana'].append(tarefa)
            elif data_vencimento <= hoje + timedelta(days=14):
                grupos['Menos de duas semanas'].append(tarefa)
            elif data_vencimento <= hoje + timedelta(days=30):
                grupos['Mais de duas semanas'].append(tarefa)
            else:
                grupos['Mais de um mês'].append(tarefa)

    for prazo, tarefas in grupos.items():
        print(f"Tarefas com {prazo}:")
        if not tarefas:
            print("Nenhuma tarefa neste grupo.")
        for tarefa in tarefas:
            print(f"{tarefa['tarefa']} - Prazo: {tarefa['data_vencimento']}")