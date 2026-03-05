value = [91, 34, 67, 15, 82]
NewV = [6, 7, 8, 9, 10]

import random

print("Lista atual: ", value)

value.sort()
print("Alterado: ", value)
value.sort( reverse= True)
print("Alterado inversamente: ", value)

random.shuffle(NewV)
print(NewV)