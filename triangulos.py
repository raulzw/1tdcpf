#Classificador de Triangulos

a = int(input("Digite o primeiro lado: "))
b = int(input("Digite o segundo lado: "))
c = int(input("Digite o terceiro lado: "))

def classificar(a, b, c):
    print(f"Lados: {a}, {b}, {c}")
    if (a <= 0 or b <= 0 or c <= 0) or (a + b <= c) or (a + c <= b) or (b + c <= a) :
        print("Nao forma triangulo")
    else:
        if a == b == c :
            tipo= "Equilatero"
        elif (a == b) or (a == c) or (b == c) :
            tipo= "Isosceles"
        else:   
            tipo= "Escaleno"
        print(f"Triangulo valido: {tipo}")

classificar(a, b, c)
