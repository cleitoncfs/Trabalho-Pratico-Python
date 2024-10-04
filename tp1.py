# Classe ItemBiblioteca (Classe Base)
class ItemBiblioteca:
    def consultar_disponibilidade(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")

# Classe Livro (Herda de ItemBiblioteca)
class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, ISBN, categoria, disponibilidade=True):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.categoria = categoria
        self.disponibilidade = disponibilidade

    def emprestar(self):
        if self.disponibilidade:
            self.disponibilidade = False
            print(f'O livro "{self.titulo}" foi emprestado.')
        else:
            print(f'O livro "{self.titulo}" não está disponível.')

    def devolver(self):
        self.disponibilidade = True
        print(f'O livro "{self.titulo}" foi devolvido.')

    def consultar_disponibilidade(self):
        return self.disponibilidade

# Classe Utilizador (Classe Base)
class Utilizador:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

    def registrar(self):
        print(f'O utilizador {self.nome} foi registrado.')

# Classe Aluno (Herda de Utilizador)
class Aluno(Utilizador):
    def __init__(self, nome, endereco, telefone, matricula):
        super().__init__(nome, endereco, telefone)
        self.matricula = matricula

# Classe Professor (Herda de Utilizador)
class Professor(Utilizador):
    def __init__(self, nome, endereco, telefone, departamento):
        super().__init__(nome, endereco, telefone)
        self.departamento = departamento

# Classe Emprestimo
from datetime import date

class Emprestimo:
    def __init__(self, livro, utilizador):
        self.livro = livro
        self.utilizador = utilizador
        self.data_emprestimo = date.today()
        self.data_devolucao = None

    def realizar_emprestimo(self):
        if self.livro.consultar_disponibilidade():
            self.livro.emprestar()
            print(f'Empréstimo realizado com sucesso para {self.utilizador.nome}.')
        else:
            print(f'O livro "{self.livro.titulo}" não está disponível.')

    def registrar_devolucao(self):
        self.livro.devolver()
        self.data_devolucao = date.today()
        print(f'Devolução registrada em {self.data_devolucao}.')

# Classe Relatorio
class Relatorio:
    def __init__(self):
        self.data_geracao = date.today()

    def gerar_relatorio(self, emprestimos):
        print(f'Relatório gerado em {self.data_geracao}')
        for emprestimo in emprestimos:
            status = "Devolvido" if emprestimo.data_devolucao else "Em andamento"
            print(f'Livro: {emprestimo.livro.titulo}, Utilizador: {emprestimo.utilizador.nome}, Status: {status}')

# Classe Biblioteca
class Biblioteca:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.livros = []
        self.utilizadores = []
        self.emprestimos = []

    def registrar_livro(self, livro):
        self.livros.append(livro)
        print(f'O livro "{livro.titulo}" foi registrado na biblioteca.')

    def registrar_utilizador(self, utilizador):
        self.utilizadores.append(utilizador)
        print(f'O utilizador {utilizador.nome} foi registrado na biblioteca.')

    def realizar_emprestimo(self, livro, utilizador):
        emprestimo = Emprestimo(livro, utilizador)
        emprestimo.realizar_emprestimo()
        self.emprestimos.append(emprestimo)

    def registrar_devolucao(self, emprestimo):
        emprestimo.registrar_devolucao()

    def gerar_relatorio(self):
        relatorio = Relatorio()
        relatorio.gerar_relatorio(self.emprestimos)



# Criação de uma biblioteca
biblioteca = Biblioteca("Biblioteca Central", "Rua Principal, 123")

# Registro de livros
livro1 = Livro("1984", "George Orwell", "1234567890", "Ficção")
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "0987654321", "Fantasia")
biblioteca.registrar_livro(livro1)
biblioteca.registrar_livro(livro2)

# Registro de utilizadores
aluno1 = Aluno("Carlos Silva", "Rua dos Estudantes, 45", "1234-5678", "A12345")
professor1 = Professor("Dra. Maria Souza", "Av. dos Professores, 78", "9876-5432", "Matemática")
biblioteca.registrar_utilizador(aluno1)
biblioteca.registrar_utilizador(professor1)

# Realização de empréstimos
biblioteca.realizar_emprestimo(livro1, aluno1)
biblioteca.realizar_emprestimo(livro2, professor1)

# Registro de devolução
emprestimo1 = biblioteca.emprestimos[0]
biblioteca.registrar_devolucao(emprestimo1)

# Geração de relatório
biblioteca.gerar_relatorio()
