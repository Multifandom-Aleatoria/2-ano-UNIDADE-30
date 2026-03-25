print("Hello World!")

Grade1 = float(input("Nota 1: "))
Grade2 = float(input("Nota 2: "))
Grade3 = float(input("Nota 3: "))

def CalculateAverage():
    if Grade1 >=11 or Grade2 >= 11 or Grade3 >= 11:
        print("Notas inválidas")
        return

    Total = Grade1 + Grade2 + Grade3
    Average = Total / 3
    
    print("A soma das notas é:", Total)
    print("A média das notas é:", Average)

CalculateAverage()