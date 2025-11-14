# SISTEMA DE VOTAÇÃO (java -> python)

# - 3 opções fixas ("Opção 1", "Opção 2", "Opção 3")
# - Loop de votação até digitar 0
# - Contagem total de votos
# - Exibição final dos resultados

# OBJETIVOS PRINCIPAIS:
# - Sistemas de votação

# - Sistemas de cadastro

# - Sistemas educacionais

# - Aplicativos corporativos

# - Backend de APIs

# - Aplicativos Android

#ANOTAÇÕES:
# Opções fixas de voto
# Loop até o usuário digitar 0
# Contagem de votos
# Mensagens iguais às do Java

def main():
    opcoes = ["Opção 1", "Opção 2", "Opção 3"]
    votos = [0] * len(opcoes)
    votacao_ativa = True

    print("=== SISTEMA DE VOTAÇÃO ===")
    print("As opções são:")
    for i, opc in enumerate(opcoes, start=1):
        print(f"{i} - {opc}")

    while votacao_ativa:
        try:
            escolha = int(input(f"\nEscolha uma opção (1-{len(opcoes)}) ou 0 para encerrar: "))
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            continue

        if escolha == 0:
            votacao_ativa = False
        elif 1 <= escolha <= len(opcoes):
            votos[escolha - 1] += 1
            print(f"Você votou na {opcoes[escolha - 1]}")
        else:
            print("Opção inválida. Tente novamente.")

    print("\n=== RESULTADOS FINAIS ===")
    for i, opc in enumerate(opcoes):
        print(f"{opc}: {votos[i]} voto(s)")


if __name__ == "__main__":
    main()
