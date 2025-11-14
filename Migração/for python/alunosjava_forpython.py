

# Armazena alunos em:
# - listaNomes (ArrayList<String>)
# - notas (HashMap<String, Double>)
# Possui menu:
# 1. Adicionar aluno
# 2. Listar alunos
# 3. Buscar nota
# 4. Sair
#- Aceita nome + nota
#- Lista alunos
#- Busca nota pelo nome

# *JAVA* PARA PYTHON

alunos = {}  # nome -> nota

def adicionar_aluno():
    print("\n=== Adicionar Aluno ===")
    nome = input("Nome do aluno: ").strip()

    try:
        nota = float(input("Nota final: "))
    except ValueError:
        print("Valor inválido para a nota!")
        return

    alunos[nome] = nota
    print("Aluno cadastrado com sucesso!")


def listar_alunos():
    print("\n=== Lista de Alunos ===")
    
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    for nome, nota in alunos.items():
        print(f"- {nome} | Nota: {nota:.2f}")


def buscar_nota():
    print("\n=== Buscar Nota ===")
    nome = input("Nome do aluno: ").strip()

    if nome in alunos:
        print(f"Nota de {nome}: {alunos[nome]:.2f}")
    else:
        print("Aluno não encontrado.")


def menu():
    while True:
        print("\n=== SISTEMA DE ALUNOS ===")
        print("1 - Adicionar aluno")
        print("2 - Listar alunos")
        print("3 - Buscar nota")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            buscar_nota()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
