print("Test Hello World")

Name = "CityBoy!"
Password = "676767"
Tries = 3

print("tentativas: ", Tries)
print(input("Digite o nome de usuário: "))
print(input("Digite a senha agora: "))

if Name == "CityBoY!" and Password == "676767":
    print("Login feito!")
else:
    Tries -= 1
    print(Tries)
    print(input("Errou, tente novamente: \n"))
    print(input("Digite a senha novamente: "))
    if Name == "CityBoY!" and Password == "676767":
        print("Login feito!")
    else:
        Tries -= 1
        print(Tries)
        print("Errou novamente, só mais uma tentativas: ")
        if Name == "CityBoY!" and Password == "676767":
            print("Login feito!")
        else:
            Tries -= 1
            print(Tries)
            print("Errou, Limite de tentativas excedido, volte aqui mais tarde!")

#Eu esqueci a forma mais facíl, por isso escrevi o mais difícil :(