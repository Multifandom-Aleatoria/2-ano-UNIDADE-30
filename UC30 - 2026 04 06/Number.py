print("Hello World!")

import random

SecretNum = random.randint(1, 100)
Tries = 0
Guess = 0

while Guess != SecretNum:
    Guess = int(input("Digite um número entre 1 e 100: "))
    Tries += 1

    if Guess < SecretNum:
        print("Maior")
    elif Guess > SecretNum:
        print("Menor")
    else:
        print("Acertou!")

print("Você acertou em", Tries, " tentativas!")

if Tries >= 8:
    print("Sem mais tentativas!")