names = ["português", "English", "한국어", "ideia de nome","ideiaDeNome02"]
print("Nomes: ", names)

names.remove("ideiaDeNome02")
print("Atualizado: ", names)

remove = names.pop()
remove = names.pop(1)
print(f"Removido: {remove}")
print("Depois do pop: ", names)

# del remove pelo índicie
 
del names[0]
print("Lista final após del: ", names)