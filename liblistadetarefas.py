def adicionar(lista, item):
    lista.append(item)

def remover(lista, item):
    lista.pop(item-1)

def mostrar(lista):
    for n in range(len(lista)):
        print(n+1," - ",lista[n])