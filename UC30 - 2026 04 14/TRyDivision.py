x = float(input("Digite um número: "))
y = float(input("Digite outro número: "))
          
def Division(x, y):
    try:
        x / y
        print("Dá ", x / y)
    except ZeroDivisionError:
        print("ERRO")
Division(x, y)