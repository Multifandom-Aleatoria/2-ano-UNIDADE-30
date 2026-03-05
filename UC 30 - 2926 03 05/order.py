print("Hello W... cê sabe o que")

import random

numbers = [4, 10, 22, 24]
print("Lista: ", numbers)

#ordem crescente
numbers.sort()
print("Numeros:", numbers)

#ordem DEcrescente
numbers.sort(reverse=True)
print("Numeros no reverse do sort():", numbers)

#embaralha numbers
random.shuffle(numbers)
print("Random: ", numbers)