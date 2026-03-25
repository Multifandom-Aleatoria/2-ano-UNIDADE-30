def SumAll(*Numbers):
    total = 0
    for num in Numbers:
        total += num
    return total

print(SumAll(1, 2, 3))

print(SumAll(10, 20, 30, 40, 50))

print(SumAll())
