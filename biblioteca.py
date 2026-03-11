from excecoes import (
    LivroIndisponivel,
    UsuarioNaoEncontrado,
    LivroNaoEncontrado
)

class Biblioteca:

    def __init__(self):
        self.acervo = []
        self.usuarios_cadastrados = []

    def cadastrar_livro(self, livro):
        self.acervo.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios_cadastrados.append(usuario)

    def buscar_usuario(self, matricula):

        for usuario in self.usuarios_cadastrados:
            if usuario.matricula == matricula:
                return usuario

        raise UsuarioNaoEncontrado("Usuário não encontrado.")

    def buscar_livro(self, isbn):

        for livro in self.acervo:
            if livro.isbn == isbn:
                return livro

        raise LivroNaoEncontrado("Livro não encontrado.")

    def registrar_emprestimo(self, matricula, isbn):

        usuario = self.buscar_usuario(matricula)
        livro = self.buscar_livro(isbn)

        if livro.disponivel == False:
            raise LivroIndisponivel("Livro indisponível.")

        usuario.pegar_emprestado(livro)

        print(f"{usuario.nome} pegou o livro '{livro.titulo}'.")

    def registrar_devolucao(self, matricula, isbn):

        usuario = self.buscar_usuario(matricula)
        livro = self.buscar_livro(isbn)

        usuario.devolver_livro(livro)

        print(f"{usuario.nome} devolveu o livro '{livro.titulo}'.")

def consultar_livros_emprestados(self):

    print("\nTABELA DE LIVROS EMPRESTADOS")
    print("-" * 60)
    print(f"{'Usuário':20} | {'Livro':30}")
    print("-" * 60)

    for usuario in self.usuarios_cadastrados:

        if len(usuario.lista_livros_emprestados) == 0:
            print(f"{usuario.nome:20} | Nenhum livro")
        else:
            for livro in usuario.lista_livros_emprestados:
                print(f"{usuario.nome:20} | {livro.titulo:30}")

    print("-" * 60)