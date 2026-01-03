from datetime import datetime, timedelta
import json

# -------------------------------
# Funções de manipulação de tarefas
# -------------------------------

def adicionar(lista, descricao, vencimento):
    tarefa = {
        "descricao": descricao,
        "vencimento": vencimento,
        "concluida": False
    }
    lista.append(tarefa)

def remover(lista, indice):
    try:
        lista.pop(indice)
    except IndexError:
        print("Este número de tarefa não existe.")

def mostrar(lista):
    if not lista:
        print("\nNenhuma tarefa encontrada.")
        return
    for i, t in enumerate(lista, start=1):
        status = "✓" if t["concluida"] else "✗"
        print(f"{i} - {t['descricao']} | Vencimento: {t['vencimento']} | Concluída: {status}")

def concluir(lista, indice):
    try:
        lista[indice]["concluida"] = True
    except IndexError:
        print("Este número de tarefa não existe.")

def remover_concluidos(lista):
    lista[:] = [tarefa for tarefa in lista if not tarefa["concluida"]]

def editar(lista, indice, descricao, vencimento):
    try:
        lista[indice]["descricao"] = descricao
        lista[indice]["vencimento"] = vencimento
    except IndexError:
        print("Este número de tarefa não existe.")

def ordenar_por_nome(lista):
    lista.sort(key=lambda t: t["descricao"].lower())

def ordenar_por_data(lista):
    try:
        lista.sort(key=lambda t: datetime.strptime(t["vencimento"], "%Y-%m-%d"))
    except ValueError:
        print("Erro: formato de data inválido em alguma tarefa. Use AAAA-MM-DD.")

def qtd(lista):
    total = len(lista)
    if total == 0:
        print("\nNão há tarefas.")
    elif total == 1:
        print("\nA lista possui 1 tarefa.")
    else:
        print(f"\nA lista possui {total} tarefas.")

def tconcluidas(lista):
    concluidas = [t for t in lista if t["concluida"]]
    mostrar(concluidas)

def tpendentes(lista):
    pendentes = [t for t in lista if not t["concluida"]]
    mostrar(pendentes)

def salvararq(lista, nome="listadetarefas.json"):
    try:
        with open(nome, mode="w", encoding="utf-8") as arquivo:
            json.dump(lista, arquivo, ensure_ascii=False, indent=4)
        print("Arquivo JSON salvo com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")

def carregararq(lista, nome="listadetarefas.json"):
    try:
        with open(nome, mode="r", encoding="utf-8") as arquivo:
            lista.clear()
            lista.extend(json.load(arquivo))
        print("\nTarefas carregadas com sucesso (JSON).")
    except FileNotFoundError:
        print("Arquivo JSON não encontrado. Salve as tarefas antes de carregar.")
    except json.JSONDecodeError:
        print("Erro: arquivo JSON corrompido ou inválido.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def tarefas_vencidas(lista):
    hoje = datetime.now().date()
    vencidas = [t for t in lista if not t["concluida"] and datetime.strptime(t["vencimento"], "%Y-%m-%d").date() < hoje]
    mostrar(vencidas)

def tarefas_proximas(lista, dias=3):
    hoje = datetime.now().date()
    proximas = [
        t for t in lista
        if not t["concluida"] and hoje <= datetime.strptime(t["vencimento"], "%Y-%m-%d").date() <= hoje + timedelta(days=dias)
    ]
    mostrar(proximas)

# -------------------------------
# Menus
# -------------------------------

def menu_principal():
    print("\nMenu Principal:")
    print("1 - Gerenciar Tarefas")
    print("2 - Exibir Tarefas")
    print("3 - Organizar Tarefas")
    print("4 - Arquivo")
    print("5 - Encerrar")

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
    print("5 - Vencidas")
    print("6 - Próximas (até 3 dias)")

def menu_organizar():
    print("\nOrganizar Tarefas:")
    print("1 - Ordenar alfabeticamente")
    print("2 - Ordenar por data de entrega")

def menu_arquivo():
    print("\nArquivo:")
    print("1 - Salvar")
    print("2 - Carregar")

# -------------------------------
# Programa Principal
# -------------------------------

def obter_opcao(mensagem, max_op):
    """
    Solicita ao usuário uma opção numérica entre 1 e max_op.
    Retorna o número escolhido ou None se inválido.
    """
    try:
        op = int(input(mensagem))
        if 1 <= op <= max_op:
            return op
        else:
            print(f"Digite um número entre 1 e {max_op}.")
            return None
    except ValueError:
        print("Digite um número válido.")
        return None

def main():
    lista = []
    while True:
        menu_principal()
        op = obter_opcao("Escolha a opção desejada: ", 5)
        if op is None:
            continue

        if op == 1:
            menu_gerenciar()
            subop = obter_opcao("Escolha a opção: ", 5)
            if subop is None:
                continue

            if subop == 1:
                tarefa = input("Tarefa que deseja adicionar: ")
                vencimento = input("Data de vencimento (AAAA-MM-DD): ")
                adicionar(lista, tarefa, vencimento)
            elif subop == 2:
                indice = obter_opcao("Índice da tarefa que deseja remover: ", len(lista))
                if indice:
                    remover(lista, indice - 1)
            elif subop == 3:
                indice = obter_opcao("Índice da tarefa que deseja editar: ", len(lista))
                if indice:
                    novadescricao = input("Nova descrição da tarefa: ")
                    novavencimento = input("Nova data de vencimento (AAAA-MM-DD): ")
                    editar(lista, indice - 1, novadescricao, novavencimento)
            elif subop == 4:
                indice = obter_opcao("Índice da tarefa que deseja concluir: ", len(lista))
                if indice:
                    concluir(lista, indice - 1)
            elif subop == 5:
                remover_concluidos(lista)

        elif op == 2:
            menu_exibir()
            subop = obter_opcao("Escolha a opção: ", 6)
            if subop is None:
                continue
            if subop == 1:
                mostrar(lista)
            elif subop == 2:
                tconcluidas(lista)
            elif subop == 3:
                tpendentes(lista)
            elif subop == 4:
                qtd(lista)
            elif subop == 5:
                tarefas_vencidas(lista)
            elif subop == 6:
                tarefas_proximas(lista)

        elif op == 3:
            menu_organizar()
            subop = obter_opcao("Escolha a opção: ", 2)
            if subop == 1:
                ordenar_por_nome(lista)
            elif subop == 2:
                ordenar_por_data(lista)

        elif op == 4:
            menu_arquivo()
            subop = obter_opcao("Escolha a opção: ", 2)
            if subop == 1:
                salvararq(lista)
            elif subop == 2:
                carregararq(lista)

        elif op == 5:
            print("Encerrando programa... Até logo!")
            break

if __name__ == "__main__":
    main()