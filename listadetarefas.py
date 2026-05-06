from datetime import datetime, timedelta
import json
import copy

historico_undo = []
historico_redo = []

# -------------------------------
# Funções auxiliares de mensagens padronizadas (#32)
# -------------------------------
def msg_sucesso(texto):
    print(f"[OK] {texto}")

def msg_erro(texto):
    print(f"[ERRO] {texto}")

def msg_info(texto):
    print(f"[INFO] {texto}")

def confirmar(mensagem):
    """Solicita confirmação s/n e retorna True/False."""
    while True:
        resp = input(f"{mensagem} (s/n): ").strip().lower()
        if resp in ('s', 'sim'):
            return True
        elif resp in ('n', 'não', 'nao'):
            return False
        else:
            msg_erro("Responda apenas 's' (sim) ou 'n' (não).")

# -------------------------------
# Funções de manipulação de tarefas
# -------------------------------

def validar_data(data_str):
    """Valida se a string está no formato AAAA-MM-DD."""
    try:
        datetime.strptime(data_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def solicitar_data():
    """Loop até que o usuário forneça uma data válida."""
    while True:
        data = input("Data de vencimento (AAAA-MM-DD): ").strip()
        if validar_data(data):
            return data
        else:
            msg_erro("Data inválida. Tente novamente no formato AAAA-MM-DD.")

def salvar_estado(lista):
    historico_undo.append(copy.deepcopy(lista))
    historico_redo.clear()

def desfazer(lista):
    if not historico_undo:
        msg_info("Nada para desfazer.")
        return
    historico_redo.append(copy.deepcopy(lista))
    estado_anterior = historico_undo.pop()
    lista.clear()
    lista.extend(estado_anterior)
    msg_info("Última ação foi desfeita. Estado atual restaurado.")

def refazer(lista):
    if not historico_redo:
        msg_info("Nada para refazer.")
        return
    historico_undo.append(copy.deepcopy(lista))
    estado_refeito = historico_redo.pop()
    lista.clear()
    lista.extend(estado_refeito)
    msg_info("Ação refeita.")

# ---------- Funções de ordenação (registram estado apenas se modificarem) ----------
def ordenar_por_categoria(lista):
    salvar_estado(lista)
    lista.sort(key=lambda t: t["categoria"].lower())
    msg_sucesso("Tarefas ordenadas por categoria.")

def ordenar_por_nome(lista):
    salvar_estado(lista)
    lista.sort(key=lambda t: t["descricao"].lower())
    msg_sucesso("Tarefas ordenadas por nome.")

def ordenar_por_data(lista):
    # Validação prévia para evitar lista corrompida durante ordenação
    for t in lista:
        if not validar_data(t["vencimento"]):
            msg_erro(f"Data inválida na tarefa: '{t['descricao']}' ({t['vencimento']}). Ordenação cancelada.")
            return
    salvar_estado(lista)
    lista.sort(key=lambda t: datetime.strptime(t["vencimento"], "%Y-%m-%d"))
    msg_sucesso("Tarefas ordenadas por data.")

# ---------- Exibições e contagens ----------
def mostrar(lista, por_pagina=10):
    if not lista:
        print("\nNenhuma tarefa encontrada.")
        return

    total = len(lista)
    inicio = 0
    while inicio < total:
        fim = min(inicio + por_pagina, total)
        for i, t in enumerate(lista[inicio:fim], start=inicio + 1):
            status = "✓" if t["concluida"] else "✗"
            tags = ", ".join(t["tags"]) if t["tags"] else "-"
            print(
                f"{i} - {t['descricao']} | Vencimento: {t['vencimento']} | "
                f"Concluída: {status} | Categoria: {t['categoria']} | Tags: {tags}"
            )
        inicio = fim
        if inicio < total:
            cont = input("\nMostrar mais tarefas? (s/n): ").lower()
            if cont != "s":
                break

def listar_categorias(lista):
    categorias = sorted(set(t["categoria"] for t in lista if t["categoria"]))
    msg_info(
        f"Categorias existentes: {', '.join(categorias) if categorias else 'Nenhuma categoria.'}"
    )

def listar_tags(lista):
    todas_tags = set(tag for t in lista for tag in t["tags"])
    msg_info(
        f"Tags existentes: {', '.join(sorted(todas_tags)) if todas_tags else 'Nenhuma tag.'}"
    )

def qtd(lista):
    total = len(lista)
    if total == 0:
        msg_info("Não há tarefas.")
    elif total == 1:
        msg_info("A lista possui 1 tarefa.")
    else:
        msg_info(f"A lista possui {total} tarefas.")

def tconcluidas(lista):
    concluidas = [t for t in lista if t["concluida"]]
    mostrar(concluidas)

def tpendentes(lista):
    pendentes = [t for t in lista if not t["concluida"]]
    mostrar(pendentes)

# ---------- Filtros ----------
def filtrar_por_categoria(lista, categoria):
    filtradas = [t for t in lista if t["categoria"].lower() == categoria.lower()]
    mostrar(filtradas)

def filtrar_por_tag(lista, tag):
    filtradas = [t for t in lista if tag.lower() in [tg.lower() for tg in t["tags"]]]
    mostrar(filtradas)

def filtrar_categoria_tag(lista, categoria, tag):
    filtradas = [
        t for t in lista
        if t["categoria"].lower() == categoria.lower()
        and tag.lower() in [tg.lower() for tg in t["tags"]]
    ]
    mostrar(filtradas)

# ---------- CRUD ----------
def adicionar(lista, descricao, vencimento, categoria="", tags=None):
    salvar_estado(lista)
    if tags is None:
        tags = []
    # Remove tags vazias acidentalmente inseridas
    tags = [tag.strip() for tag in tags if tag.strip()]
    tarefa = {
        "descricao": descricao,
        "vencimento": vencimento,
        "concluida": False,
        "categoria": categoria.strip(),
        "tags": tags,
    }
    lista.append(tarefa)
    msg_sucesso(f"Tarefa '{descricao}' adicionada na categoria '{categoria}' com tags {tags}.")

def remover(lista, indice):
    """índice 0‑based, validado externamente como 1‑based."""
    if not confirmar("Tem certeza que deseja remover esta tarefa?"):
        msg_info("Remoção cancelada.")
        return
    salvar_estado(lista)
    removida = lista.pop(indice)
    msg_sucesso(f"Tarefa '{removida['descricao']}' removida.")

def concluir(lista, indice):
    salvar_estado(lista)
    lista[indice]["concluida"] = True
    msg_sucesso("Tarefa concluída.")

def editar(lista, indice, descricao, vencimento, categoria="", tags=None):
    salvar_estado(lista)
    lista[indice]["descricao"] = descricao
    lista[indice]["vencimento"] = vencimento
    lista[indice]["categoria"] = categoria.strip()
    lista[indice]["tags"] = [t.strip() for t in tags if t.strip()] if tags else []
    msg_sucesso("Tarefa editada.")

def remover_concluidos(lista):
    if not confirmar("Confirma remoção de todas as tarefas concluídas?"):
        msg_info("Operação cancelada.")
        return
    salvar_estado(lista)
    antes = len(lista)
    lista[:] = [tarefa for tarefa in lista if not tarefa["concluida"]]
    removidas = antes - len(lista)
    msg_sucesso(f"{removidas} tarefa(s) concluída(s) removida(s).")

# ---------- Datas vencidas e próximas ----------
def tarefas_vencidas(lista):
    hoje = datetime.now().date()
    vencidas = []
    for t in lista:
        if t["concluida"]:
            continue
        try:
            dt = datetime.strptime(t["vencimento"], "%Y-%m-%d").date()
        except ValueError:
            msg_erro(f"Aviso: data inválida na tarefa '{t['descricao']}' ({t['vencimento']}). Ignorando.")
            continue
        if dt < hoje:
            vencidas.append(t)
    mostrar(vencidas)

def tarefas_proximas(lista, dias=3):
    hoje = datetime.now().date()
    limite = hoje + timedelta(days=dias)
    proximas = []
    for t in lista:
        if t["concluida"]:
            continue
        try:
            dt = datetime.strptime(t["vencimento"], "%Y-%m-%d").date()
        except ValueError:
            msg_erro(f"Aviso: data inválida na tarefa '{t['descricao']}' ({t['vencimento']}). Ignorando.")
            continue
        if hoje <= dt <= limite:
            proximas.append(t)
    mostrar(proximas)

# ---------- Arquivo ----------
def validar_estrutura_tarefa(tarefa):
    """Verifica se o dicionário tem as chaves obrigatórias e tipos básicos."""
    if not isinstance(tarefa, dict):
        return False
    chaves = {"descricao", "vencimento", "concluida", "categoria", "tags"}
    return all(chave in tarefa for chave in chaves) and isinstance(tarefa["tags"], list)

def salvararq(lista, nome="listadetarefas.json"):
    try:
        with open(nome, mode="w", encoding="utf-8") as arquivo:
            json.dump(lista, arquivo, ensure_ascii=False, indent=4)
        msg_sucesso("Arquivo JSON salvo com sucesso.")
    except Exception as e:
        msg_erro(f"Erro ao salvar arquivo: {e}")

def carregararq(lista, nome="listadetarefas.json"):
    if not confirmar("Carregar arquivo apagará a lista atual. Confirma?"):
        msg_info("Carregamento cancelado.")
        return
    try:
        with open(nome, mode="r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        if not isinstance(dados, list):
            msg_erro("Arquivo JSON inválido: não é uma lista de tarefas.")
            return
        for i, tarefa in enumerate(dados, start=1):
            if not validar_estrutura_tarefa(tarefa):
                msg_erro(f"Tarefa {i} com estrutura inválida: {tarefa}. Verifique o arquivo.")
                return
            if not validar_data(tarefa["vencimento"]):
                msg_erro(f"Tarefa {i} com data inválida: {tarefa['vencimento']}. Verifique o arquivo.")
                return
        # Tudo válido, carregar
        salvar_estado(lista)
        lista.clear()
        lista.extend(dados)
        msg_sucesso(f"Tarefas carregadas com sucesso ({len(lista)} registros).")
    except FileNotFoundError:
        msg_erro("Arquivo JSON não encontrado.")
    except json.JSONDecodeError:
        msg_erro("Erro: arquivo JSON corrompido ou inválido.")
    except Exception as e:
        msg_erro(f"Ocorreu um erro inesperado: {e}")

# -------------------------------
# Menus (ajustados)
# -------------------------------
def menu_principal():
    print("\nMenu Principal:")
    print("1 - Gerenciar Tarefas")
    print("2 - Exibir Tarefas")
    print("3 - Organizar Tarefas")
    print("4 - Arquivo")
    print("5 - Desfazer")
    print("6 - Refazer")
    print("7 - Encerrar")

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
    print("7 - Filtrar por categoria")
    print("8 - Filtrar por tag")
    print("9 - Filtrar por categoria + tag")
    print("10 - Listar categorias existentes")
    print("11 - Listar tags existentes")

def menu_organizar():
    print("\nOrganizar Tarefas:")
    print("1 - Ordenar alfabeticamente")
    print("2 - Ordenar por data de entrega")
    print("3 - Ordenar por categoria")

def menu_arquivo():
    print("\nArquivo:")
    print("1 - Salvar")
    print("2 - Carregar")

# -------------------------------
# Programa Principal
# -------------------------------
def obter_opcao(mensagem, max_op):
    """Lê uma opção do usuário garantindo que esteja entre 1 e max_op."""
    try:
        op = int(input(mensagem))
        if 1 <= op <= max_op:
            return op
        else:
            msg_erro(f"Digite um número entre 1 e {max_op}.")
            return None
    except ValueError:
        msg_erro("Digite um número válido.")
        return None

def obter_indice_valido(lista, acao):
    """Solicita índice 1‑based, retorna índice 0‑based ou None se cancelar/lista vazia."""
    if not lista:
        msg_info("A lista está vazia.")
        return None
    while True:
        entrada = input(f"Índice da tarefa que deseja {acao} (1-{len(lista)}): ").strip()
        try:
            idx = int(entrada)
            if 1 <= idx <= len(lista):
                return idx - 1
            else:
                msg_erro(f"Índice fora do intervalo (1 a {len(lista)}).")
        except ValueError:
            msg_erro("Digite um número inteiro válido.")
        # Oferece cancelamento
        if confirmar("Deseja cancelar a operação?"):
            return None

def main():
    lista = []
    while True:
        menu_principal()
        op = obter_opcao("Escolha a opção desejada: ", 7)
        if op is None:
            continue

        if op == 1:
            menu_gerenciar()
            subop = obter_opcao("Escolha a opção: ", 5)
            if subop is None:
                continue

            if subop == 1:  # Adicionar
                descricao = input("Tarefa que deseja adicionar: ").strip()
                if not descricao:
                    msg_erro("Descrição não pode ser vazia.")
                    continue
                vencimento = solicitar_data()
                categoria = input("Categoria da tarefa (opcional): ").strip()
                # Entrada única para tags, aceita vírgulas
                tags_input = input("Tags separadas por vírgula (opcional): ").strip()
                tags = [t.strip() for t in tags_input.split(",") if t.strip()] if tags_input else []
                adicionar(lista, descricao, vencimento, categoria, tags)

            elif subop == 2:  # Remover
                idx = obter_indice_valido(lista, "remover")
                if idx is not None:
                    remover(lista, idx)

            elif subop == 3:  # Editar
                idx = obter_indice_valido(lista, "editar")
                if idx is None:
                    continue
                novadesc = input("Nova descrição da tarefa: ").strip()
                if not novadesc:
                    msg_erro("Descrição não pode ser vazia.")
                    continue
                print("Nova data de vencimento:")
                novadata = solicitar_data()
                novacat = input("Nova categoria (opcional): ").strip()
                tags_input = input("Novas tags separadas por vírgula (opcional): ").strip()
                novatags = [t.strip() for t in tags_input.split(",") if t.strip()] if tags_input else []
                editar(lista, idx, novadesc, novadata, novacat, novatags)

            elif subop == 4:  # Concluir
                idx = obter_indice_valido(lista, "concluir")
                if idx is not None:
                    concluir(lista, idx)

            elif subop == 5:  # Remover concluídas
                remover_concluidos(lista)

        elif op == 2:  # Exibir
            menu_exibir()
            subop = obter_opcao("Escolha a opção: ", 11)  # Corrigido para 11 (#25)
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
            elif subop == 7:
                categoria = input("Digite a categoria: ").strip()
                if categoria:
                    filtrar_por_categoria(lista, categoria)
                else:
                    msg_erro("Categoria não pode ser vazia.")
            elif subop == 8:
                tag = input("Digite a tag: ").strip()
                if tag:
                    filtrar_por_tag(lista, tag)
                else:
                    msg_erro("Tag não pode ser vazia.")
            elif subop == 9:
                categoria = input("Digite a categoria: ").strip()
                tag = input("Digite a tag: ").strip()
                if categoria and tag:
                    filtrar_categoria_tag(lista, categoria, tag)
                else:
                    msg_erro("Categoria e tag não podem ser vazias.")
            elif subop == 10:
                listar_categorias(lista)
            elif subop == 11:
                listar_tags(lista)

        elif op == 3:  # Organizar
            menu_organizar()
            subop = obter_opcao("Escolha a opção: ", 3)
            if subop == 1:
                ordenar_por_nome(lista)
            elif subop == 2:
                ordenar_por_data(lista)
            elif subop == 3:
                ordenar_por_categoria(lista)

        elif op == 4:  # Arquivo
            menu_arquivo()
            subop = obter_opcao("Escolha a opção: ", 2)
            if subop == 1:
                salvararq(lista)
            elif subop == 2:
                carregararq(lista)

        elif op == 5:
            desfazer(lista)
        elif op == 6:
            refazer(lista)
        elif op == 7:
            if confirmar("Encerrar programa. Confirma?"):
                msg_info("Encerrando... Até logo!")
                break

if __name__ == "__main__":
    main()
