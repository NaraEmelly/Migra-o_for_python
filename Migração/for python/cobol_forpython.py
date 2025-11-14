

# COBOL (COmmon Business Oriented Language) é uma das linguagens mais antigas ainda em uso, criada em 1959.

# Objetivos da linguagem COBOL
# - Processamento de grandes quantidades de dados.
# - Confiabilidade em sistemas bancários e governamentais.
# - Estrutura clara e próxima da linguagem humana.
# - Alta legibilidade para facilitar manutenção por equipes empresariais.

# Foco principal em projetos
# - Sistemas bancários
# - Folha de pagamento
# - Cadastros corporativos
# - Processamento de registros
# - Softwares de governo e previdência
# O programa que você enviou é um exemplo clássico de uso de COBOL: entrada de dados, processamento e relatório.

# ANOTAÇÕES:
# Cadastro de 5 alunos
# Nome e nota
# Soma das notas
# Cálculo da média
# Exibição da lista

# LINGUAGEM COBOL PARA PYTHON

def main():
    NUM_ALUNOS = 5
    nomes = []
    notas = []

    print("SISTEMA DE CADASTRO DE ALUNOS")

    for i in range(NUM_ALUNOS):
        nome = input(f"\nDigite o nome do aluno {i+1}: ").strip()
        nota = float(input(f"\nDigite a nota de {nome}: "))

        nomes.append(nome)
        notas.append(nota)

    total_notas = sum(notas)
    media = total_notas / NUM_ALUNOS

    print("\n=== LISTA DE ALUNOS ===")
    for i in range(NUM_ALUNOS):
        print(f"\n{nomes[i]} | Nota: {notas[i]:.2f}")

    print(f"\nMédia da turma: {media:.2f}")


if __name__ == "__main__":
    main()
