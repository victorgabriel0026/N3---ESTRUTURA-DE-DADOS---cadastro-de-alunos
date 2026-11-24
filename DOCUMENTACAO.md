# Documentação - Sistema de Cadastro de Alunos

**Atividade N3 - Estrutura de Dados e Organização de Arquivos**
**Linguagem:** Python 3

## 1. Descrição

Programa de console para cadastro de alunos. Os dados ficam salvos em um arquivo JSON (`alunos.json`), então continuam existindo depois que o programa é fechado.

## 2. Requisitos atendidos

| Requisito | Implementação |
|---|---|
| Incluir, alterar e excluir | funções `incluir`, `alterar` e `excluir` |
| Persistência de dados em JSON | função `salvar` e leitura com `json.load` |
| Pesquisa por campos do tipo texto | função `pesquisar` (nome e curso) |
| Listas ordenadas por 2 campos diferentes | `listarPorNome` e `listarPorIdade` |

## 3. Estrutura do arquivo JSON

O arquivo `alunos.json` guarda um dicionário com a chave `"alunos"`. Dentro dela, cada aluno é identificado pelo **ID** (a chave, em formato de texto), e o valor é outro dicionário com nome, curso e idade.

```json
{
    "alunos": {
        "1": {
            "nome": "lucas",
            "curso": "fisioterapia",
            "idade": 30
        },
        "2": {
            "nome": "victor",
            "curso": "ads",
            "idade": 19
        }
    }
}
```

| Campo | Tipo | Descrição |
|---|---|---|
| ID (chave) | texto | identificador único do aluno |
| `nome` | texto | nome do aluno |
| `curso` | texto | curso do aluno |
| `idade` | inteiro | idade do aluno |

Para começar sem alunos, o arquivo deve conter `{"alunos": {}}`.

## 4. Como executar

1. Deixe `chamada.py` e `alunos.json` na **mesma pasta**.
2. Abra a pasta no terminal e execute:

```
python chamada.py
```

## 5. Menu

```
|  -------------------- CHAMADA --------------------  |
(lista de alunos)
|  ---------------- FINAL DA CHAMADA ---------------  |
       SAIR [0]
     LISTAR [1]
  ADICIONAR [2]
    ALTERAR [3]
     EXCLUI [4]
  PESQUISAR [5]
 ORDEM NOME [6]
ORDEM IDADE [7]
```

O menu roda dentro de um laço `while True`. Ele reaparece, com a lista atualizada, depois de cada operação, e só termina quando o usuário digita `0`.

## 6. Funções

### `salvar(dadosAlunos)`
Grava o dicionário completo no `alunos.json`.
- Abre o arquivo em modo `"w"` (escrita).
- `encoding="utf-8"` permite gravar acentos.
- `ensure_ascii=False` mantém os acentos legíveis no arquivo (sem isso, "João" viraria `João`).
- `indent=4` deixa o arquivo organizado em linhas.

### `incluir()`
Cadastra um novo aluno.
1. Lê o arquivo.
2. Pede nome, curso e idade.
3. Percorre as chaves existentes, converte para número e acha o maior ID.
4. O novo ID é o maior mais 1 (convertido para texto). Com `max(ids, default=0)`, se não houver alunos, o primeiro recebe o ID `"1"`.
5. Adiciona o aluno ao dicionário e chama `salvar`.

### `listar()`
Lê o arquivo e imprime um aluno por linha, no formato:
`ID: 1, Nome: lucas, curso: fisioterapia, idade: 30`.
Usa `.items()` para receber o ID e os dados de cada aluno juntos.

### `alterar()`
Altera os dados de um aluno existente.
1. Lê o arquivo e mostra a lista.
2. Pede o ID.
3. Se o ID existe (`in`), pede os novos dados, substitui o registro e chama `salvar`.
4. Se não existe, mostra "ID não encontrado".

### `excluir()`
Remove um aluno.
1. Lê o arquivo e mostra a lista.
2. Pede o ID.
3. Se o ID existe, remove com `del dadosAlunos["alunos"][ID]` e chama `salvar`.
4. Se não existe, mostra "ID não encontrado".

### `pesquisar()`
Pesquisa por campo de **texto** (nome ou curso).
- O termo digitado e os campos são convertidos com `.lower()`, então a busca ignora maiúsculas e minúsculas.
- A busca é parcial: o operador `in` confere se o termo está **dentro** do texto (por exemplo, "mar" encontra "Maria").
- A variável `encontrou` indica se houve resultado. Se não houve, mostra "Nenhum aluno encontrado".

### `listarPorNome()`
Lista os alunos em **ordem alfabética de nome**.
Usa `sorted()` com `key=lambda item: item[1]["nome"].lower()`. O `item` é o par `(ID, dados)`, e `item[1]` são os dados do aluno.

### `listarPorIdade()`
Lista os alunos em **ordem crescente de idade**.
Usa `sorted()` com `key=lambda item: item[1]["idade"]`.

### `IDfimChamada(IDmenu)`
Recebe a opção escolhida e chama a função correspondente. Para uma opção inválida, mostra "Numero não encontrado, tente novamente".

### `menu()`
Função principal. Dentro de um `while True`, mostra o cabeçalho, a lista de alunos e as opções, lê a escolha e chama `IDfimChamada`. A opção `0` encerra o laço com `break`.

## 7. Conceitos utilizados

- **Dicionários e listas:** estrutura dos dados e percurso com `for`.
- **Arquivos JSON:** `json.load` (leitura) e `json.dump` (escrita).
- **Gerenciador de contexto `with`:** abre o arquivo e o fecha automaticamente.
- **Ordenação:** `sorted()` com `key` e `lambda`.
- **Busca em texto:** `.lower()` e o operador `in`.
- **Funções:** cada operação em uma função separada.
- **Laço `while`:** repete o menu até o usuário sair.

## 8. Limitações conhecidas

- Digitar letras onde se espera número (opção do menu ou idade) gera `ValueError` e encerra o programa.
- O arquivo `alunos.json` precisa existir na pasta antes de executar.
- Um aluno com campo `null` no JSON causa erro na pesquisa e na ordenação por nome.
- Ao excluir o último aluno, seu ID é reutilizado no próximo cadastro.
