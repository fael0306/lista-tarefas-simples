# 📋 Lista de Tarefas CLI

Um gerenciador de tarefas por linha de comando (CLI) desenvolvido em Python, com suporte a categorias, tags, datas de vencimento, persistência em JSON e controle de desfazer/refazer.

**Versão atual:** `v1.4.0`

---

## ✨ Funcionalidades

- ✅ Adicionar, remover, editar e marcar tarefas como concluídas
- 🏷️ Categorias e tags personalizáveis
- 📅 Validação de datas e visualização de tarefas vencidas/próximas
- 📊 Filtros por categoria, tag ou ambos
- 🔄 Ordenação por nome, data de vencimento ou categoria
- 📂 Persistência em arquivo JSON (salvar / carregar)
- ⏮️ Desfazer (undo) e refazer (redo) ações
- 🗑️ Confirmação para ações destrutivas (remoção, carga de arquivo, etc.)
- 📄 Exibição paginada da lista de tarefas
- 🎨 Mensagens padronizadas com prefixos `[OK]`, `[ERRO]` e `[INFO]`

---

## 📦 Requisitos

- Python **3.7+** (testado com Python 3.10+)
- Nenhuma biblioteca externa necessária (apenas bibliotecas padrão)

---

## 🚀 Instalação e execução

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/nome-do-repo.git
   cd nome-do-repo
   ```
2. Execute o script:
   ```bash
   python listadetarefas.py
   ```

O programa inicia com uma lista vazia. Utilize o menu interativo para gerenciar suas tarefas.

---

## 📖 Guia de uso

### Menu Principal
```
Menu Principal:
1 - Gerenciar Tarefas
2 - Exibir Tarefas
3 - Organizar Tarefas
4 - Arquivo
5 - Desfazer
6 - Refazer
7 - Encerrar
```

### Exemplo rápido
1. Adicione uma tarefa: `1` → `1` → informe descrição, data, categoria e tags.
2. Liste todas as tarefas: `2` → `1`.
3. Marque como concluída: `1` → `4` → informe o índice.
4. Salve as tarefas: `4` → `1`.
5. Carregue um arquivo existente: `4` → `2` (confirmação necessária).

---

## 🗂️ Estrutura do arquivo JSON

As tarefas são salvas como uma lista de objetos com o seguinte formato:

```json
[
  {
    "descricao": "Estudar Python",
    "vencimento": "2026-05-10",
    "concluida": false,
    "categoria": "estudos",
    "tags": ["python", "programacao"]
  }
]
```
- `descricao` (string) – obrigatório  
- `vencimento` (string) – formato `AAAA-MM-DD`, obrigatório  
- `concluida` (boolean) – estado da tarefa  
- `categoria` (string) – pode ser vazio  
- `tags` (list de strings) – pode ser vazia  

O carregamento valida a estrutura e as datas, rejeitando qualquer formato inválido.

---

## 🏗️ Estrutura do código

| Função / Módulo              | Descrição                                                                 |
|-----------------------------|---------------------------------------------------------------------------|
| `adicionar()`                | Insere nova tarefa (com validação e limpeza de tags)                     |
| `remover()` / `editar()`    | Modificam tarefas com confirmação                                        |
| `concluir()`                 | Marca tarefa como concluída                                              |
| `remover_concluidos()`      | Exclui tarefas concluídas (com confirmação)                              |
| `mostrar(paginação)`        | Exibe tarefas com paginação dinâmica                                     |
| `filtrar_por_categoria/tag` | Filtros combinados                                                       |
| `ordenar_por_nome/data/categoria` | Ordenações com validação de integridade das datas                 |
| `salvararq()` / `carregararq()` | Persistência com validação estrutural                                |
| `desfazer()` / `refazer()`  | Histórico de estados (undo/redo)                                         |
| `validar_data()` / `validar_estrutura_tarefa()` | Verificações de integridade                          |
| `confirmar()`                | Pergunta sim/não padronizada                                             |
| `obter_indice_valido()`      | Coleta índice com possibilidade de cancelamento                          |

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para sugerir melhorias ou reportar bugs:

1. Abra uma **issue** descrevendo o problema ou sugestão.
2. Faça um **fork** do repositório e crie uma branch com sua feature.
3. Envie um **pull request** com uma descrição clara das alterações.

Por favor, siga o estilo de codificação utilizado e garanta que as funcionalidades existentes permaneçam intactas.

---

## 🗒️ Changelog

Consulte o arquivo [`CHANGELOG.md`](./CHANGELOG.md) para o histórico detalhado de versões.

**Principais mudanças na v1.4.0:**
- Correção de bug crítico no menu de exibição (opções inacessíveis)
- Paginação na visualização de tarefas
- Confirmação para operações destrutivas
- Validação rigorosa de entrada de dados e de arquivos JSON
- Padronização de mensagens com prefixos

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [`LICENSE`](./LICENSE) para mais detalhes.

---

Feito com 💻 para organização pessoal e aprendizado em Python.
