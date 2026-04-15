print("Hello World!")

Price1 = float(input("Digite o valo do produto: "))
Price2 = float(input("Digite o valor do outro produto: "))
Price3 = float(input("Digite o valo do outro produto: "))
Sum = Price1 + Price2 + Price3

def Calculator():
    try:
        print("O total a se pagar é: ", Sum)
    except:
        print("Valor inválido!")
Calculator()