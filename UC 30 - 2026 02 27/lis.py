#o nome do arquivo era pra ser "list.py". Digitação rápida é triste

print("! World Hello")

nome = ["Português", "English", "日本語"]
print(nome)

data = ["yume", 0, 97.104, True]
print(data)
print(type(data))
print(type(data[0]))
print(type(data[1]))
print(type(data[2]))
print(type(data[3]))

add = input("Digite algo: ")
list = ["Dog", "Cat"]
print("Origial: ", list)
list.append("Bunny")
print("Atualizado: ", list)

list.insert(1, "Grilo")
print("Atualizado: ", list)

list.extend(["Monkey", "Sheep"])
print("Final list: ", list)