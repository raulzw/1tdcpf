import random

def jogar(escolha_usuario):
    opcoes = {
        1: "Pedra",
        2: "Papel",
        3: "Tesoura",
        4: "Lagarto",
        5: "Spock"
    }

    regras = {
        (1, 3): "quebra",
        (1, 4): "esmaga",
        (2, 1): "cobre",
        (2, 5): "refuta",
        (3, 2): "corta",
        (3, 4): "decapita",
        (4, 2): "come",
        (4, 5): "envenena",
        (5, 1): "vaporiza",
        (5, 3): "derrete"
    }

    escolha_pc = random.randint(1,5)
    print(f"Voce: {opcoes[escolha_usuario]}")
    print(f"Computador: {opcoes[escolha_pc]}")

    if escolha_usuario == escolha_pc:
        print("Empate!")
    elif (escolha_usuario, escolha_pc) in regras:
        acao = regras [(escolha_usuario, escolha_pc)]
        print(f"{opcoes[escolha_usuario]} {acao} {opcoes[escolha_pc]} - Voce venceu!")
    else:
        acao = regras [(escolha_pc, escolha_usuario)]
        print(f"{opcoes[escolha_pc]} {acao} {opcoes[escolha_usuario]} - Computador venceu!")

print("1 = Pedra") 
print("2 = Papel")
print("3 = Tesoura")
print("4 = Lagarto")
print("5 = Spock")

escolha = int(input("Escolha (1-5): "))

jogar(escolha)