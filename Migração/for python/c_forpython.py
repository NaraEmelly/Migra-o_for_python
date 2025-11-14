# Linguagem C 

#PESQUISA SOBRE: 
# Um linguagem de baixo nível estruturada, muito usada em sistemas que necessitam
# de eficiência e controle de memória.

# OBJETIVOS PRINCIPAIS DO C:
# - Criar programas rápidos e ficientes.
# - Fornecer controle direto sobre memória e hadware.
# - Ser base para desenvolvimento de sistemas operacionais, drivers,compiladores.
# FOCO PRINCIPAL EM PROJETOS:
# - Sistemas embarcados(microcontroladores).
# - Aplicações de alto desempenho.
# - Programas que exigem uso eficientes de memória.
# - Softwares de sistema(Linux, Windows e outros com componentes em C).

# MIGRAÇÃO PARA PYTHON:

funcionarios = []  # Lista para armazenar funcionários

def adicionar_funcionario():
    print("\n=== Adicionar Funcionário ===")
    nome = input("Nome: ").strip()
    cargo = input("Cargo: ").strip()
    
    try:
        salario = float(input("Salário: R$ "))
    except ValueError:
        print("Valor inválido para salário!")
        return
    
    funcionario = {
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    }

    funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!")

def listar_funcionarios():
    print("\n=== Lista de Funcionários ===")
    
    if len(funcionarios) == 0:
        print("Nenhum funcionário cadastrado.")
        return

    for i, f in enumerate(funcionarios, start=1):
        print(f"{i}) {f['nome']} - {f['cargo']} - R$ {f['salario']:.2f}")

def buscar_funcionario():
    print("\n=== Buscar Funcionário ===")
    nome_busca = input("Nome do funcionário: ").strip()

    for f in funcionarios:
        if f["nome"].lower() == nome_busca.lower():
            print(f"Cargo: {f['cargo']} | Salário: R$ {f['salario']:.2f}")
            return

    print("Funcionário não encontrado.")

def menu():
    while True:
        print("\n=== SISTEMA DE FUNCIONÁRIOS ===")
        print("1 - Adicionar funcionário")
        print("2 - Listar funcionários")
        print("3 - Buscar funcionário")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_funcionario()
        elif opcao == "2":
            listar_funcionarios()
        elif opcao == "3":
            buscar_funcionario()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()


