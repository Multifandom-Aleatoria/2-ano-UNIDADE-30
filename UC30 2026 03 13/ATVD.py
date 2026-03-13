print("Hello World!")  # Pra ver se funciona

import random

names = [
    "Julinha", "Alice", "YunA", "laura", "Pedro", "Lucas", "Fernanda",
    "Juliana", "Rafael", "Camila", "Bruno", "Larissa", "Felipe",
    "Patrícia", "Diego", "Amanda", "Alicia", "Bianca", "TESTNAME", "Sofia"
]

Intruder = "TESTNAME"

RandomList = random.sample(names, 20)

for Pos, names in enumerate(RandomList, 1):
    print("Nome e posição: ", names, Pos, "º Lugar na lista")

print(input("Quem é o intruso? (Dica: ele não tem um nome comum, e tem um nome estranho)\n"))
if Intruder == "TESTNAME":
   print("DESCOBRIMOS O INTRUSO!")

else:
   print("Errou!")