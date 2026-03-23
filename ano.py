dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))


def verificar_data(dia, mes, ano):
    bissexto = (ano  % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

    print(f"Data: {dia:02d}/{mes:02d}/{ano}")
    print(f"Ano bissexto: {"Sim" if bissexto else "Nao"}")

    if mes < 1 or mes > 12 :
        print("Data invalida")
        return
   
    if mes == 2:
        if bissexto:
            dias_no_mes = 29
        else:
            dias_no_mes = 28
    elif mes in (1, 3, 5, 7, 8, 10, 12):
        dias_no_mes = 31
    else:
        dias_no_mes = 30

    if dia <1 or dia > dias_no_mes:
        if mes == 2:
            print(f"Data invalida: fevereiro de {ano} tem apenas {dias_no_mes} dias")
        else:
            print("Data invalida: dia nao existe")
    else:
        print("Data valida")



verificar_data(dia, mes, ano)