from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
        self.lista_livros_emprestados = []

    @abstractmethod
    def pegar_emprestado(self, livro):
        pass

    @abstractmethod
    def devolver_livro(self, livro):
        pass