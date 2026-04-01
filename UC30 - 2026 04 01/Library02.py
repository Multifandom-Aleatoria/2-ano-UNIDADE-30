Catalogue = {}
Loan = {}
History = []

def AddBook(Code, Title, Writer, Quantity):
    if Code in Catalogue:
        print("O livro", Code, "já existe!")
        return False
    
    Catalogue[Code] = {
        "Title": Title,
        "Autor": Writer,
        "Quantidade": Quantity
    }
    print("Livro", Title, "adicionado à biblioteca")
    return True
