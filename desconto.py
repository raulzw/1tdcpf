valor = float(input("valor total da compra: "))
vip = input("voce possui vip?: ").strip().lower()

def calcular(valor, vip):
    if valor <= 100:
        desconto = 0
        porcentagem = 0
    elif valor <= 300:
        desconto = valor * 0.10
        porcentagem= 10
    elif valor <= 500:
        desconto = valor * 0.15
        porcentagem= 15
    else:
        desconto = valor * 0.20
        porcentagem= 20
    if vip == "sim":
        desconto_vip = valor * 0.05
        porcentagem_vip = 5
    else:
        desconto_vip = 0
        porcentagem_vip = 0    
        
    valor_final = valor - desconto - desconto_vip
    print("=== Resumo da Compra ===\n")
    print(f"Valor original: R$ {valor:.2f}")
    print(f"Desconto ({porcentagem}%): R$ {desconto:.2f}")
    print(f"Desconto VIP ({porcentagem_vip}%): R$ {desconto_vip:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")

calcular(valor, vip)        