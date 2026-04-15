print("Hello World!")

Grade1 = float(input("Digite a primeira nota: "))
Grade2 = float(input("Digite a segunda nota: "))
Grade3 = float(input("Digite a terceira nota: "))
Media = (Grade1 + Grade2 + Grade3) / 3

def SIm():
    try:
        Media == (Grade1 + Grade2 + Grade3) / 3
        print("A média do aluno é: ", Media)
    except:
        print("Valor inválido!")
SIm()