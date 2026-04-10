print("Hello World!")

# As variáveis básicas do Python:

Num = 4102224  # Variável tipo número inteiro (1, 2, 3...).
Name = "TestName01"  # Variável tipo string (texto). Apenas é considerada se tiver entre aspas.
PiValue = 3.14  # Variável tipo número real (como números decimais).
HaveReadABookToday = False  # Variável tipo bool (verdadeiro ou falso).

# Variáveis são valores definidos pelo programador ou digitados pelo usuário
# que são usados para armazenar informações e dados importantes.

# As variáveis não podem começar com números.
# Por exemplo: 3Num = 3 (isso não funciona como variável).

print("Valor pra testes:", Num, type(Num))
print("Nome:", Name, type(Name))
print("Valor aprox. de Pi:", PiValue, type(PiValue))
print("Já leu um livro hoje:", HaveReadABookToday, type(HaveReadABookToday))


# Tipos de dados são identificados automaticamente pelo Python usando a função type()
#Aqui alguns dos operadores aritmétricos

print("Soma:", 5 + 3)
print("Subtração:", 10 - 4)
print("Multiplicação:", 6 * 2)
print("Divisão:", 8 / 2)

# Alguns operaores de atribuição

print("\nOperadores de atribuição:")

x = 10  # atribuição inicial
print("Valor inicial de x:", x)

x += 5  # x = x + 5
print("Depois de x += 5:", x)

x -= 3  # x = x - 3
print("Depois de x -= 3:", x)

x *= 2  # x = x * 2
print("Depois de x *= 2:", x)

x == 2  # x EXATAMENTE igual a 2
print("Depois de x *= 2:", x)

x != 2  # x indiferente de 2
print("Depois de x *= 2:", x)
