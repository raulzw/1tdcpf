#Conversor de Moedas

print("Menu:")
print("[1] Real = Dolar")
print("[2] Real = Euro")
print("[3] Real = Libra")
opcao = int(input("Escolha uma opcao: "))

def converter(cotacao, simbolo):
        valor = float(input("Digite o valor em reais: "))
        resultado = valor / cotacao
        print (f"R$ {valor:.2f} = {simbolo} {resultado:.2f}")

if opcao== 1 :
    converter(5.15, "US$")
elif opcao== 2:
    converter(5.55, "€")
elif opcao== 3:
    converter(6.45, "£") 
else:
    print("opcao invalida")     

