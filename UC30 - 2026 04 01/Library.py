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

def LoanBook(Code, Student):
    if Code not in Catalogue:
        print("Livro com código ", Code, " Não encontrado!")
        return False
    
    if Catalogue[Code]["Quantidade"] <= 0:
        print(Catalogue[Code["Titulo"]], "Não enontrado")
        return False
    
    BookSTudent = CountBooksS(Student)
    if BookSTudent >= 2:
        print("O aluno já pegou o livro a quantidade máxima de livros!")
        return False
    
    if Code in ActiveLoans and StudentName in ActiveLoans[Code]:
    print(Student, "Já pegou esse livro!") 

    #