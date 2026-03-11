class Livro:
    def __init__(self, isbn, titulo, autor, disponivel=True):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def emprestar(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True

    def __str__(self):
        return f"{self.titulo} - {self.autor} - ISBN: {self.isbn}"