square = [x**2 for x in range(1, 11)]
print("Quadrados: ", square)

evens = [x for x in range(1, 21) if x % 2 == 0]
print("Pares: ", evens)

vowels = [vowels for vowels in "Programação" if vowels in "AEIOUaeiou"]
print("Vogais: ", vowels)