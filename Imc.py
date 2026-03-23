peso = float(input("Qual e o seu peso? (Kg) "))
altura = float(input("Qual e a sua altura? (m) "))

imc = peso / (altura **2)

def calculo_de_imc(imc):
    if imc <18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <24.9:
        return "Peso normal"
    elif 25.0 <= imc <29.9:
        return "Sobrepeso"
    else :
        return "Obesidade"
    
print (f"Peso:{peso:.1f} kg | Altura:{altura:.2f} m")
print (f"IMC: {imc:.1f} - {calculo_de_imc(imc)}")