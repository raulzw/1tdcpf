#criança (0-11), adolescente (12-17), adulto (18-59) ou idoso (60+)
 
def calculo_de_idade(idade):
    if idade >= 0 and idade <= 11:
        return "Crianca"
    elif idade >= 12 and  idade <= 17:
        return "Adolescente"
    elif idade >= 18 and idade <= 59:
        return "Adulto"
    elif idade >= 60 and idade <= 120:
        return "Idoso"
    else:
        return "Invalido"
    
idade = int(input("Coloque sua idade para verificacao: "))
resultado = calculo_de_idade(idade)
print(resultado)