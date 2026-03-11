from usuario import Usuario
from excecoes import LimiteEmprestimosExcedido

class Professor(Usuario):

    def pegar_emprestado(self, livro):

        if len(self.lista_livros_emprestados) >= 5:
            raise LimiteEmprestimosExcedido(
                "Professor só pode pegar até 5 livros."
            )

        self.lista_livros_emprestados.append(livro)
        livro.emprestar()
        
    def devolver_livro(self, livro):

        if livro in self.lista_livros_emprestados:
            self.lista_livros_emprestados.remove(livro)
            livro.devolver()