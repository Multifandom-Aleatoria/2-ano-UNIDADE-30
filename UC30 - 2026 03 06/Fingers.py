print("Hello World!")

grades = [7.5, 9.5, 8.0, 6.0, 8.5]
print("Suas notas: ", grades)

media = sum(grades) / len(grades)

print("Menores notas: ", min(grades))
print("Maiores notas: ", max(grades))
print("Soma das notas: ", sum(grades))
print("Média notas: ", sum(grades) / len(grades))

if media >= 7.0:
    print("Passou!")
else:
    print("Não passou :(")

names = ["A1", "A2", "A3", "A3"]

for name in names:
    print(f"Olá {name}!")

print("\n Enumeradamente: ")
for indice, name in enumerate(names):
    print(f"Posição {indice}: {name}")
    
original = ["a", "b", "c"]

copia = list(original)

print(original)
print(copia)
print("Iguais?? ", copia == original)

copia.append("D")
print(original)
print(copia)
print("Agora mudou: ", original == copia, "\noxi??")