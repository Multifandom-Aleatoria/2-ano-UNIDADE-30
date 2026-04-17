Phrase = input("Digite uma frase: ")
Vowels = "aeiouAEIOU"
Counter = 0

for Letters in Phrase:
    if Letters in Vowels:
        Counter += 1

print("Quantidade de vogais na frase:", Counter)