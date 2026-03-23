def cacular_estacionamento(entrada, saida, placa_final, dia):
    print("=== Estacionamento ===")

    if saida <= entrada :
        horas = (24 - entrada) + saida
    else:
        horas = saida - entrada

    if horas == 0:
        horas = 1

    print(f"Entrada: {entrada:02d}h | Saida: {saida:02d}h")
    print(f"Permanencia: {horas} horas")

    if horas == 1:
        total = 10
    else:
        total = 10 + (horas - 1) * 5

    print(f"Tarifa base: R$ {total:.2f}")

    
    adicional_noturno = 0
    if entrada >= 22 or saida <= 6:
        adicional_noturno = total * 0.5
        total += adicional_noturno
        print(f"Adicional noturno (50%): R$ {adicional_noturno:.2f}")


    desconto = 0
    if dia == "segunda" and placa_final % 2 == 0:
        desconto = total * 0.10
        total -= desconto
        print(f"Desconto (10%): R$ {desconto:.2f}")

    print(f"Total: R$ {total:.2f}")

entrada = int(input("Entrada: "))
saida = int(input("Saida: "))
placa_final = int(input("Ultimo numero da placa: "))
dia = input("Dia da semana: ").strip().lower()

cacular_estacionamento(entrada, saida, placa_final, dia)