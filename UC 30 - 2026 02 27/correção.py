print("Hello World!")

Num01 = float(input("Número 1: "))
Num02 = float(input("Número 2: "))

soma = Num01 + Num02
prod = Num01 * Num02

print("Soma: ", soma)

print("Produto: ", prod)

Num03 = int(input("Coloque um outro Number aqui! "))
if (Num03 % 2 == 00):
    result = Num03 ** 2
else:
    result = Num03 ** 3


user = input("Nome de usuário: ")
password = input("Senha:")

if (user == "procopio" and password == "12345" ) or (user == "paiva" and password == "54321"):
    print("Pode entrar!")
elif (user == "procopio" and password == "12345" ) or (user == "paiva" and password == "54321"):
    print("Pode entrar!")
else:
    print("Nome de usuário ou senha incorretos")




name = input("Seu nome: ")
passw = "123456"

tries = 3

while tries > 3:
    passwo = input("Digite a senha: ")
    if passwo == passw:
        print("Hello back! ", name, " !")
        break
    else:
        tries -= 1
        print("Senha incorreta, digite novamente")
        if tries == 1:
            print("Uma tentativa restante...")
        else:
            print("SENHA BLOQUEADA, AGUARDE 97104 Horas :)")