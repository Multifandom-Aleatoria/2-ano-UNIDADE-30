Word = input("Digite algo aqui: \n")
Count = int(len(Word))

def CountLetters():
    if Count >= 2:
        print("Tem:", len(Word), "Letras!")
    elif Count == 1:
        print("Tem:", len(Word), "Letra")
    else:
        print("Não existem letras negativas!!!")
CountLetters()