from biblioteca import Biblioteca
from livro import Livro
from aluno import Aluno
from professor import Professor
from excecoes import *

biblioteca = Biblioteca()

livro1 = Livro("001", "Dom Casmurro", "Machado de Assis")
livro2 = Livro("002", "O Cortiço", "Aluísio Azevedo")
livro3 = Livro("003", "Capitães da Areia", "Jorge Amado")
livro4 = Livro("004", "Iracema", "José de Alencar")
livro5 = Livro("005", "Memórias Póstumas", "Machado de Assis")

biblioteca.cadastrar_livro(livro1)
biblioteca.cadastrar_livro(livro2)
biblioteca.cadastrar_livro(livro3)
biblioteca.cadastrar_livro(livro4)
biblioteca.cadastrar_livro(livro5)

aluno1 = Aluno("A001", "Bárbara Linda")
aluno2 = Aluno("A002", "Marina")
professor1 = Professor("P001", "Fernanda")

biblioteca.cadastrar_usuario(aluno1)
biblioteca.cadastrar_usuario(aluno2)
biblioteca.cadastrar_usuario(professor1)

try:

    biblioteca.registrar_emprestimo("A001", "001")
    biblioteca.registrar_emprestimo("A001", "002")
    biblioteca.registrar_emprestimo("A001", "003")

    biblioteca.registrar_emprestimo("A001", "004")

except Exception as erro:
    print("Erro:", erro)

try:

    biblioteca.registrar_emprestimo("P001", "004")
    biblioteca.registrar_emprestimo("P001", "005")

except Exception as erro:
    print("Erro:", erro)

biblioteca.consultar_livros_emprestados()

try:

    biblioteca.registrar_devolucao("A001", "001")

except Exception as erro:
    print("Erro:", erro)


biblioteca.consultar_livros_emprestados()