import json
# id = alunos["alunos"].keys()

# print(id)

#função para salvar os arquivos no json
def salvar(dadosAlunos):
    with open("alunos.json", "w", encoding="utf-8") as arquivos: 
        json.dump(dadosAlunos, arquivos, ensure_ascii=False, indent=4) 
        # "ensure_ascii=False:" por padrão, o json.dump troca letras com acento por códigos. "João" viraria "Jo\u00e3o" no arquivo. Com False, ele escreve "João"
        # "indent=4:" deixa o arquivo organizado em linhas, com 4 espaços de recuo. Sem ele, tudo fica numa linha só

# função para incluir novos alunos, e chama a função salvar para adicionar ao json
def incluir():
    # "r" lé o arquivo "read", só le o arquivo não altera
    with open("alunos.json", "r", encoding="utf-8") as arquivos: # encoding="utf-8": le o arquivo no padrão que aceita acentos.
        dadosAlunos = json.load(arquivos)
    ids = []
    nome = str(input("Qual o seu nome: "))
    curso = str(input("Qual o curso que deseja cursar: "))
    idade = int(input("Qual a sua idade: "))
    for i in dadosAlunos["alunos"]:
        ids.append(int(i))
    ultimoID = max(ids, default=0)
    novoID = str(ultimoID + 1)
    print("seu no ID é:", novoID)
    dadosAlunos["alunos"][novoID] = {"nome": nome, "curso": curso, "idade": idade }
    salvar(dadosAlunos)


def listar():
    with open("alunos.json", "r", encoding="utf-8") as arquivos: # encoding="utf-8": le o arquivo no padrão que aceita acentos.
        dadosAlunos = json.load(arquivos)
    for id, aluno in dadosAlunos["alunos"].items():
        print("ID:", id+",", "Nome:", aluno["nome"]+",", "curso:", aluno["curso"]+",", "idade:", aluno["idade"])

def alterar():
    with open("alunos.json", "r", encoding="utf-8") as arquivos: # encoding="utf-8": le o arquivo no padrão que aceita acentos.
        dadosAlunos = json.load(arquivos)
    listar()
    procurarID = input("Qual o seu ID? ")
    if procurarID in dadosAlunos["alunos"] :
        nome = str(input("Qual o nome: "))
        curso = str(input("Qual o curso que deseja alterar: "))
        idade = int(input("Qual a idade: "))
        print("seu ID é:", procurarID)
        dadosAlunos["alunos"][procurarID] = {"nome": nome, "curso": curso, "idade": idade }
        salvar(dadosAlunos)
    else:
        print("ID não encontrado")

def excluir():
    with open("alunos.json", "r", encoding="utf-8") as arquivos: # encoding="utf-8": le o arquivo no padrão que aceita acentos.
            dadosAlunos = json.load(arquivos)
    listar()
    procurarID = input("Qual ID para ser excluir? ")
    if procurarID in dadosAlunos["alunos"] :
        print("ID excluido:", procurarID)
        del dadosAlunos["alunos"][procurarID]
        salvar(dadosAlunos)
    else:
        print("ID não encontrado")

def pesquisar():
    with open("alunos.json", "r", encoding="utf-8") as arquivos:
        dadosAlunos = json.load(arquivos)
    termo = input("Digite o nome ou curso para pesquisar: ").lower()
    encontrou = False
    for id, aluno in dadosAlunos["alunos"].items():
        if termo in aluno["nome"].lower() or termo in aluno["curso"].lower():
            print(f"ID: {id}, Nome: {aluno['nome']}, curso: {aluno['curso']}, idade: {aluno['idade']}")
            encontrou = True
    if not encontrou:
        print("Nenhum aluno encontrado")

def listarPorNome():
    with open("alunos.json", "r", encoding="utf-8") as arquivos:
        dadosAlunos = json.load(arquivos)
    ordenados = sorted(dadosAlunos["alunos"].items(), key=lambda item: item[1]["nome"].lower())
    for id, aluno in ordenados:
        print(f"ID: {id}, Nome: {aluno['nome']}, curso: {aluno['curso']}, idade: {aluno['idade']}")

def listarPorIdade():
    with open("alunos.json", "r", encoding="utf-8") as arquivos:
        dadosAlunos = json.load(arquivos)
    ordenados = sorted(dadosAlunos["alunos"].items(), key=lambda item: item[1]["idade"])
    for id, aluno in ordenados:
        print(f"ID: {id}, Nome: {aluno['nome']}, curso: {aluno['curso']}, idade: {aluno['idade']}")


def IDfimChamada(IDmenu):
    if IDmenu == 1:
        listar()    
    elif IDmenu == 2:
        incluir()
    elif IDmenu == 3:
        alterar()
    elif IDmenu == 4:
        excluir()
    elif IDmenu == 5:
        pesquisar()
    elif IDmenu == 6:
        listarPorNome()
    elif IDmenu == 7:
        listarPorIdade()
    else:
        print("Numero não encontrado, tente novamente")

def menu():
    while True:
        print("|","-"*20, "CHAMADA" ,"-"*20, "|")
        listar()
        print("|","-"*16, "FINAL DA CHAMADA" ,"-"*15, "|")
        print("       SAIR [0]")
        print("     LISTAR [1]")
        print("  ADICIONAR [2]")
        print("    ALTERAR [3]")
        print("     EXCLUI [4]")
        print("  PESQUISAR [5]")
        print(" ORDEM NOME [6]")
        print("ORDEM IDADE [7]")
        IDmenu = int(input())
        if IDmenu == 0:
            break
        IDfimChamada(IDmenu)
        
menu()