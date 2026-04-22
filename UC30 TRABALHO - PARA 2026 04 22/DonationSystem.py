print("Hello World!")

print("Bem vindo(a) ao sistema de doação para BKHbvqd!\nSomos uma organização criada para ajudar no combate à violência contra a mulher.\nPara isso precisamos da sua ajuda!\nAntes de começarmos uma doação, precisamos das informações básicas:\n")

while True:
    email = input("Digite seu email: ")
    password = input("Agora digite sua senha: ")

    print("Email:", email)
    print("Senha:", password)

    awnser = input("Tem certeza que é isso mesmo? S/N\n").strip().lower()

    if awnser in ("sim", "s"):
        print("Ótimo, vamos começar a doação!")
        break
    elif awnser in ("não", "nao", "n"):
        print("Ok, vamos tentar de novo.")
    else:
        print("Resposta inválida. Por favor, responda com 'Sim' ou 'Não'.")

#===================================================

print("Quanto você gostaria de doar?")

while True:
    try:
        amount = float(input("Digite o valor em R$: "))

        if amount <= 0:
            print("Valor inválido. Doação cancelada.")
            print("Mesmo assim, sua participação foi tudo! :)")
            break
        else:
            print("Obrigado pela doação de R$", amount, "!")
            print("Doação feita!")
            break

    except ValueError:
        print("Valor inválido. Por favor, digite um número.")

print("\nObrigado(a) pela participação!")
print("Sua doação ajuda a transformar o impossível em possível.")
print("Feito por J.V. e Luan, estudantes de T.I. do Senac RN")

# :)
