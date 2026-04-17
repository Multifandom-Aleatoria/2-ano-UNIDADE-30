Num = [1000, 10010, 894, 5524, 1347, 163, 67, 765, 324]

Pair = 0
for numbers in Num:
    if numbers % 2 == 0:
        Pair += numbers

print("A soma dos valores pares é:", Pair)