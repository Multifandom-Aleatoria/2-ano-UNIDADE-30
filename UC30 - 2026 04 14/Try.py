print("Hello World!")

A = int(input("Digite um número: "))
B = int(input("Digite o próximo número: "))

def Some_Segura(A, B):
    try:
        A + B
        print("Dá ", A + B)

    except TypeError:
        print("Soma inválida!")

Some_Segura(A, B)