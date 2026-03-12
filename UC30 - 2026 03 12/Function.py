#Sem funções 🤮

print("Hello World!") 
print("Hello World!") 
print("Hello World!") 

#Com funções 😎

def Mensage():
    print("Hello World!")
Mensage()

def saudaçao(nome):
    print("olá", nome, " !")

saudaçao("Julinha")
saudaçao("Jade")

def exiba(nome, mensage):
    print(mensage, nome)

exiba("TESTNAME", "hello World!")


#Parâmetros
exiba(nome = "TESTNAME01", mensage = "OLÁMUNDO!")

def nota(grade01, grade02):
    media = (grade01 + grade02) / 2
    return media

result = nota(8.4, 8.9)
print("A média foi: ", result)