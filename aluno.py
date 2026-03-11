from usuario import Usuario
from excecoes import LimiteEmprestimosExcedido

class Aluno(Usuario):
    def pegar_emprestado(self, livro):

        if len(self.lista_livros_emprestados) >= 3:
            raise LimiteEmprestimosExcedido(
                "Aluno só pode pegar até 3 livros."
            )

        self.lista_livros_emprestados.append(livro)
        livro.emprestar()
        
    def devolver_livro(self, livro):

        if livro in self.lista_livros_emprestados:
            self.lista_livros_emprestados.remove(livro)
            livro.devolver()