Price = float(input("Digite o preço do produto: R$"))

if Price >= 500:
    descount = 20

elif Price >= 200:
    descount = 10
    
else:
    descount = 0

FinalP = Price - (Price * descount / 100)
print("O preço final com desconto é: R$", FinalP)

if Price <= 200:
    print("Não houve desconto aplicado.")

elif Price <= 0:
    print("Valor inválido.")