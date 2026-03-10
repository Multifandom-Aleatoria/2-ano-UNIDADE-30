print("...")

contatos = ["Teste00", "Teste01", "teste02", "Teste03"]

removed = contatos.pop("Teste00")
print(f"Removido: {removed}")
print("Atualizado: ", contatos)

del contatos["Teste01"]
print("Após isso: ", contatos)

print("Números", len(contatos))