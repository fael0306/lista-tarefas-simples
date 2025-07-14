def adicionar(lista, descricao, vencimento):
    tarefa = {
        "descricao": descricao,
        "vencimento": vencimento,
        "concluida": False
    }
    lista.append(tarefa)

def remover(lista, item):
    try:
        lista.pop(item-1)
    except IndexError:
        print("Este número de tarefa não existe.")

def mostrar(lista):
    for i, t in enumerate(lista, start=1):
        status = "✓" if t["concluida"] else "✗"
        print(f"{i} - {t['descricao']} | Vencimento: {t['vencimento']} | Concluída: {status}")

def concluir(lista,item):
    try:
        lista[item] = lista[item]+" ✓"
    except IndexError:
        print("Este número de tarefa não existe.")

def removerconcluidos(lista):
    for n in range(0,len(lista)):
        for k in lista[n]:
            if k=="✓":
                remover(lista,n)

def editar(lista,item,tarefaeditada):
    try:
        lista[item] = tarefaeditada
    except IndexError:
        print("Este número de tarefa não existe.")

def ordenar(lista):
    lista.sort(key=str.lower)

def qtd(lista):
    if len(lista)>1:
        return print("\nA lista possui",len(lista),"tarefas.")
    elif len(lista)==1:
        return print("\nA lista possui",len(lista),"tarefa.")
    else:
        return print("\nNão há tarefas.")

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
    print("Arquivo salvo com sucesso.")

def carregararq(lista):
    try:
        with open("listadetarefas.txt", mode="r") as arquivo:
            for k in arquivo:
                tarefa = k.strip()
                adicionar(lista, tarefa)
        print("\nTarefas carregadas com sucesso.")
    except FileNotFoundError as e:
        print(f"Erro ao carregar arquivo: {e}\nFavor, salvar as tarefas antes de solicitar o carregamento.\n")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}\n")

from datetime import datetime, timedelta

def tarefas_vencidas(lista):
    hoje = datetime.now().date()
    vencidas = [t for t in lista if not t["concluida"] and datetime.strptime(t["vencimento"], "%Y-%m-%d").date() < hoje]
    mostrar(vencidas)

def tarefas_proximas(lista, dias=3):
    hoje = datetime.now().date()
    proximas = []
    for t in lista:
        venc = datetime.strptime(t["vencimento"], "%Y-%m-%d").date()
        if not t["concluida"] and hoje <= venc <= hoje + timedelta(days=dias):
            proximas.append(t)
    mostrar(proximas)