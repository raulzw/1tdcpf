def caixa(valor):
    if valor <= 0:
        print("Invalido - valor negativo ou zero")
        return
    if valor % 10 != 0:
        print("Invalido - nao é multiplo de 10")
        return
    
    print(f"=== Saque: R$ {valor} ===")

    total_cedulas= 0

    notas_200 = valor // 200
    valor %= 200
    total_cedulas += notas_200

    notas_100 = valor // 100
    valor %= 100
    total_cedulas += notas_100

    notas_50 = valor // 50
    valor %= 50
    total_cedulas += notas_50

    notas_20 = valor // 20
    valor = valor % 20
    total_cedulas += notas_20


    notas_10 = valor // 10
    valor %= 10
    total_cedulas += notas_10

    print(f"R$ 200: {notas_200} cedula(s)")
    print(f"R$ 100: {notas_100} cedula(s)")
    print(f"R$ 50: {notas_50} cedula(s)")
    print(f"R$ 20: {notas_20} cedula(s)")
    print(f"R$ 10: {notas_10} cedula(s)")
    print(f"Total de cedulas: {total_cedulas}")

valor = int(input("Digite o valor do saque: "))
caixa(valor)