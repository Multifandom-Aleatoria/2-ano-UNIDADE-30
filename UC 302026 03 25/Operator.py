print("Hello World!")

sum = "Soma"
multi = "Multiplicação"
sub = "Subtração"
divi = "Divisão"

def operation():
    opt = input("Qual operação você quer fazer?\n")
    
    if opt == sum:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("A soma deles é igual a:", num1 + num2)
        
    elif opt == sub:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("A subtração deles é igual a:", num1 - num2)
        
    elif opt == multi:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("A multiplicação deles é igual a:", num1 * num2)
        
    elif opt == divi:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 == 0:
            print("Dá sempre zero! Tente outro")
        else:
            print("A divisão deles é igual a:", num1 / num2)

operation()