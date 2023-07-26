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
    for n in range(len(lista)):
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