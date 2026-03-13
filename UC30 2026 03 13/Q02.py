print("Test")

def EvenNum(list):
    Counter = 0
    for num in list:
        if num % 2 == 0:
            Counter += 1
    return Counter

num = [1, 2, 3, 4, 5, 6, 7, 8]
print("Quantidade de números pares:", EvenNum(num))