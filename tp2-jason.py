import json
from datetime import datetime

# Definição da interface ItemBiblioteca
class ItemBiblioteca:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        self.disponivel = True

# Classe Livro que herda de ItemBiblioteca
class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, isbn, categoria):
        super().__init__(titulo, autor, isbn)
        self.categoria = categoria

# Classe Utilizador
class Utilizador:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

# Classe Aluno que herda de Utilizador
class Aluno(Utilizador):
    pass

# Classe Professor que herda de Utilizador
class Professor(Utilizador):
    pass

# Classe Empréstimo
class Emprestimo:
    def __init__(self, utilizador, livro, data_emprestimo):
        self.utilizador = utilizador
        self.livro = livro
        self.data_emprestimo = data_emprestimo

# Classe Relatório para gerar relatórios de empréstimos
class Relatorio:
    def __init__(self):
        self.emprestimos = []
        self.devolucoes = []

    def registrar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)
        print(f"Empréstimo registrado com sucesso para o item '{emprestimo.livro.titulo}' por {emprestimo.utilizador.nome}.")

    def registrar_devolucao(self, emprestimo):
        self.devolucoes.append(emprestimo)
        print(f"Item '{emprestimo.livro.titulo}' devolvido por {emprestimo.utilizador.nome} com sucesso.")

    def relatorio_emprestimos(self):
        print("\nRelatório de Itens Emprestados:")
        for emprestimo in self.emprestimos:
            print(f"Item: {emprestimo.livro.titulo} | Emprestado por: {emprestimo.utilizador.nome} | Data do Empréstimo: {emprestimo.data_emprestimo}")

    def relatorio_disponibilidade(self, livros):
        print("\nRelatório de Itens Disponíveis:")
        for livro in livros:
            status = "Disponível" if livro.disponivel else "Indisponível"
            print(f"Item: {livro.titulo} | Status: {status}")

    def relatorio_utilizadores(self, utilizadores):
        print("\nRelatório de Utilizadores:")
        for utilizador in utilizadores:
            print(f"Nome: {utilizador.nome} | Endereço: {utilizador.endereco} | Telefone: {utilizador.telefone}")

# Função para carregar dados do arquivo JSON
def carregar_dados(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    livros = []
    utilizadores = []
    emprestimos = []

    # Criar livros
    for livro in data['livros']:
        livro_obj = Livro(livro['titulo'], livro['autor'], livro['isbn'], livro['categoria'])
        livro_obj.disponivel = livro['disponivel']
        livros.append(livro_obj)

    # Criar utilizadores
    for utilizador in data['utilizadores']:
        utilizador_obj = Utilizador(utilizador['nome'], utilizador['endereco'], utilizador['telefone'])
        utilizadores.append(utilizador_obj)

    # Criar empréstimos
    for emprestimo in data['emprestimos']:
        utilizador = next((u for u in utilizadores if u.nome == emprestimo['utilizador']), None)
        livro = next((l for l in livros if l.titulo == emprestimo['livro']), None)
        if utilizador and livro:
            emprestimo_obj = Emprestimo(utilizador, livro, emprestimo['data_emprestimo'])
            emprestimos.append(emprestimo_obj)

    return livros, utilizadores, emprestimos

# Exemplo de uso
if __name__ == "__main__":
    # Carregar dados do arquivo JSON
    livros, utilizadores, emprestimos = carregar_dados("arquivo.json")

    # Criando um relatório
    relatorio = Relatorio()

    # Processar empréstimos
    for emprestimo in emprestimos:
        if emprestimo.livro.emprestar():
            print(f"Item '{emprestimo.livro.titulo}' emprestado com sucesso para {emprestimo.utilizador.nome}.")
            relatorio.registrar_emprestimo(emprestimo)
        else:
            print(f"O item '{emprestimo.livro.titulo}' já foi emprestado anteriormente.")

    # Exibindo relatório de empréstimos
    relatorio.relatorio_emprestimos()

    # Simulando devoluções e registrando
    for emprestimo in emprestimos:
        relatorio.registrar_devolucao(emprestimo)
        emprestimo.livro.devolver()  # Devolver o livro após registro

    # Exibindo relatório de itens disponíveis
    relatorio.relatorio_disponibilidade(livros)

    # Exibindo relatório de utilizadores
    relatorio.relatorio_utilizadores(utilizadores)

# ===================================================================
# Classes Implementadas:
# ItemBiblioteca: Classe base para itens da biblioteca.
# Livro: Classe que herda de ItemBiblioteca.
# Utilizador: Classe base para utilizadores da biblioteca.
# Aluno e Professor: Classes que herdam de Utilizador.
# Emprestimo: Classe que representa um empréstimo de livro.
# Relatorio: Classe que gera relatórios sobre empréstimos e devoluçõe

# Atributos:
# ItemBiblioteca:
# titulo, autor, isbn, disponivel.
# Livro:
# Herda os atributos de ItemBiblioteca e adiciona categoria.
# Utilizador:
# nome, endereco, telefone.
# Emprestimo:
# utilizador, livro, data_emprestimo.

# Métodos:
# ItemBiblioteca:
# emprestar(), devolver().
# Relatorio:
# registrar_emprestimo(), registrar_devolucao(), relatorio_emprestimos(), relatorio_disponibilidade().

# Funcionalidades do Sistema
# Empréstimos e Devoluções:
# O código permite registrar empréstimos, verificar a disponibilidade dos livros e registrar devoluções.
# Geração de Relatórios:
# O código gera relatórios de itens emprestados e disponíveis, conforme solicitado.
# O código permite a criação de livros, utilizadores e a gestão de empréstimos, o que cobre as operações 
# essenciais do sistema de gestão de biblioteca.
# O código inclui a leitura do arquivo JSON, a criação de instâncias das classes a partir dos dados lidos e o 
# ssssregistro dos empréstimos.



