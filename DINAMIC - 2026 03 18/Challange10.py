Num = int(input("Digite um número:\n"))

def NumDecide():
    if Num >= 1:
        print("Positivo!")
    elif Num == 0:
        print("Neutro")
    else:
        print("Negativo")
NumDecide()