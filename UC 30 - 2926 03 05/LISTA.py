data = [9, 7, 1, 0, 4, False]

soma = [21, True]

print(data)

#Número de elementos
print("comprimento: ", len(data) - 1) #não quero que conte o "false" aqui

print("Quantas vezes 7 aparece: ", data.count(7))

print("Índicie de 4: ", data.index(4))

print("A soma é igual a 21? ", 21 in soma)
print("Há 21 aí? ", 21 in data)