def calcular_inss(salario):
    faixas = [
        (1518.00, 0.075, "Faixa 7.5%"),
        (2793.88, 0.09, "Faixa 9%"),
        (4190.83, 0.12, "Faixa 12%"),
        (8157.41, 0.14, "Faixa 14%"),
    ]

    inss_total = 0
    detalhes = []
    limite_anterior = 0

    for limite, aliquota, nome in faixas:
        if salario > limite_anterior:
            base_faixa = min(salario, limite) - limite_anterior
            valor_faixa = base_faixa * aliquota
            detalhes.append((nome, valor_faixa))
            inss_total += valor_faixa
            limite_anterior = limite
        else:
            detalhes.append((nome, 0.0))

    inss_total = int(inss_total * 100) / 100
    return inss_total, detalhes

def calcular_base_ir(salario, dependentes, pensao, idoso):
    inss_total, detalhes_inss = calcular_inss(salario)

    desconto_dependentes = dependentes * 189.59
    desconto_idoso = 1903.98 if idoso else 0.0

    base_ir = salario - inss_total - desconto_dependentes - pensao - desconto_idoso

    if base_ir < 0:
        base_ir = 0.0

    return base_ir, inss_total, detalhes_inss, desconto_dependentes, desconto_idoso

def calcular_ir(base_ir):
    faixas = [
        (2259.20, 0.00, "Faixa isenta"),
        (2826.65, 0.075, "Faixa 7.5%"),
        (3751.05, 0.15, "Faixa 15%"),
        (4664.68, 0.225, "Faixa 22.5%"),
        (float("inf"), 0.275, "Faixa 27.5%"),
    ]

    ir_total = 0
    detalhes = []
    limite_anterior = 0

    for limite, aliquota, nome in faixas:
        if base_ir > limite_anterior:
            base_faixa = min(base_ir, limite) - limite_anterior
            valor_faixa = base_faixa * aliquota
            detalhes.append((nome, valor_faixa))
            ir_total += valor_faixa
            limite_anterior = limite
        else:
            detalhes.append((nome, 0.0))

    ir_total = int(ir_total * 100) / 100
    return ir_total, detalhes

def formatar_reais(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def contracheque_ir(salario, dependentes, pensao, idoso):
    base_ir, inss_total, detalhes_inss, desconto_dependentes, desconto_idoso = calcular_base_ir(
        salario, dependentes, pensao, idoso
    )

    ir_total, detalhes_ir = calcular_ir(base_ir)

    salario_liquido = salario - inss_total - pensao - ir_total

    print("==============================")
    print("CONTRACHEQUE - Calculo de IR Mensal")
    print("==============================")

    print(f"Salario bruto:      {formatar_reais(salario)}")
    print()

    print(f"(-) INSS:           {formatar_reais(inss_total)}")
    for nome, valor in detalhes_inss:
        print(f"   {nome:<15}{formatar_reais(valor)}")

    print()
    print(f"(-) Dependentes ({dependentes}): {formatar_reais(desconto_dependentes)}")
    print(f"(-) Pensao:         {formatar_reais(pensao)}")
    print(f"(-) Isencao 65+:    {formatar_reais(desconto_idoso)}")

    print()
    print(f"Base de calculo IR: {formatar_reais(base_ir)}")

    print()
    print(f"(-) IR:             {formatar_reais(ir_total)}")
    for nome, valor in detalhes_ir:
        print(f"   {nome:<15}{formatar_reais(valor)}")

    print()
    print("==============================")
    print(f"Salario liquido:    {formatar_reais(salario_liquido)}")
    print("==============================")

salario = float(input("Salario bruto mensal: R$ "))
dependentes = int(input("Numero de dependentes: "))
tem_pensao = input("Paga pensao alimenticia? (sim/nao): ").strip().lower()

if tem_pensao == "sim":
    pensao = float(input("Valor da pensao alimenticia: R$ "))
else:
    pensao = 0.0

idoso = input("Tem 65 anos ou mais? (sim/nao): ").strip().lower() == "sim"

contracheque_ir(salario, dependentes, pensao, idoso)