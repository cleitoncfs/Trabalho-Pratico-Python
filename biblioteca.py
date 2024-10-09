from datetime import date

class Biblioteca:
    def __init__(self, logotipo: str, site: str, nif: int):
        self.logotipo = logotipo
        self.site = site
        self.nif = nif
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

class Entidade:
    def __init__(self, nome: str, telefone: str, e_mail: str, aniversario: date, data_criacao: date):
        self.nome = nome
        self.telefone = telefone
        self.e_mail = e_mail
        self.aniversario = aniversario
        self.data_criacao = data_criacao
        self.endereco = None

    def registar_pessoa(self, pessoa):
        pass  # Implementação do método para registrar pessoa

    def registar_endereco(self, endereco):
        self.endereco = endereco

class Endereco:
    def __init__(self, morada: str, cidade: str, codigo_postal: str, pais: str):
        self.morada = morada
        self.cidade = cidade
        self.codigo_postal = codigo_postal
        self.pais = pais

class Pessoa(Entidade):
    def __init__(self, nome: str, telefone: str, e_mail: str, aniversario: date, data_criacao: date, sexo: str, 
                 doc_identificacao: str, tipo_doc_identificacao: str, tipo_pessoa: str, tipo_acesso: str, nif: int):
        super().__init__(nome, telefone, e_mail, aniversario, data_criacao)
        self.sexo = sexo
        self.doc_identificacao = doc_identificacao
        self.tipo_doc_identificacao = tipo_doc_identificacao
        self.tipo_pessoa = tipo_pessoa
        self.tipo_acesso = tipo_acesso
        self.nif = nif

class Bibliotecario(Pessoa):
    def __init__(self, nome: str, telefone: str, e_mail: str, aniversario: date, data_criacao: date, sexo: str, 
                 doc_identificacao: str, tipo_doc_identificacao: str, tipo_pessoa: str, tipo_acesso: str, nif: int, identificacao: str):
        super().__init__(nome, telefone, e_mail, aniversario, data_criacao, sexo, doc_identificacao, tipo_doc_identificacao, 
                         tipo_pessoa, tipo_acesso, nif)
        self.identificacao = identificacao

    def registar_livro(self, livro):
        pass  # Implementação do método para registrar livro

    def gerar_relatorio(self):
        pass  # Implementação para gerar relatório

    def gerar_devolucao(self, emprestimo):
        pass  # Implementação para gerar devolução

    def registar_reserva(self, reserva):
        pass  # Implementação para registrar reserva

class Aluno(Pessoa):
    def __init__(self, nome: str, telefone: str, e_mail: str, aniversario: date, data_criacao: date, sexo: str, 
                 doc_identificacao: str, tipo_doc_identificacao: str, tipo_pessoa: str, tipo_acesso: str, nif: int, matricula: str):
        super().__init__(nome, telefone, e_mail, aniversario, data_criacao, sexo, doc_identificacao, tipo_doc_identificacao, 
                         tipo_pessoa, tipo_acesso, nif)
        self.matricula = matricula

class Professor(Pessoa):
    def __init__(self, nome: str, telefone: str, e_mail: str, aniversario: date, data_criacao: date, sexo: str, 
                 doc_identificacao: str, tipo_doc_identificacao: str, tipo_pessoa: str, tipo_acesso: str, nif: int, departamento: str):
        super().__init__(nome, telefone, e_mail, aniversario, data_criacao, sexo, doc_identificacao, tipo_doc_identificacao, 
                         tipo_pessoa, tipo_acesso, nif)
        self.departamento = departamento

class Utilizador(Pessoa):
    def __init__(self, nome: str, telefone: str, e_mail: str, aniversario: date, data_criacao: date, sexo: str, 
                 doc_identificacao: str, tipo_doc_identificacao: str, tipo_pessoa: str, tipo_acesso: str, nif: int, tipo: str):
        super().__init__(nome, telefone, e_mail, aniversario, data_criacao, sexo, doc_identificacao, tipo_doc_identificacao, 
                         tipo_pessoa, tipo_acesso, nif)
        self.tipo = tipo

class ItemBiblioteca:
    def consultar_disponibilidade(self):
        pass  # Implementação para consultar disponibilidade

class Livro(ItemBiblioteca):
    def __init__(self, titulo: str, descricao: str):
        self.titulo = titulo
        self.descricao = descricao
        self.exemplares = []

    def registar_exemplar(self, exemplar):
        self.exemplares.append(exemplar)

    def registar_autor(self, autor):
        pass  # Implementação para registrar autor

    def emprestar(self, emprestimo):
        pass  # Implementação para emprestar livro

    def devolver(self, devolucao):
        pass  # Implementação para devolver livro

class Autor:
    def __init__(self, nome_autor: str):
        self.nome_autor = nome_autor

class CategoriaGenero:
    def __init__(self, nome_cat_genero: str):
        self.nome_cat_genero = nome_cat_genero

class Exemplar:
    def __init__(self, num_exemplar: str, isbn: str, capa: str, ano_publicacao: int, estado_exemplar: str):
        self.num_exemplar = num_exemplar
        self.isbn = isbn
        self.capa = capa
        self.ano_publicacao = ano_publicacao
        self.estado_exemplar = estado_exemplar
        self.idioma = None
        self.editora = None
        self.estante = None

    def registar_idioma(self, idioma):
        self.idioma = idioma

    def registar_editora(self, editora):
        self.editora = editora

    def registar_estante(self, estante):
        self.estante = estante

class Acronimo:
    def __init__(self, acronimo: str, nome_acronimo: str):
        self.acronimo = acronimo
        self.nome_acronimo = nome_acronimo

class Editora:
    def __init__(self, nome_editora: str):
        self.nome_editora = nome_editora

class Idioma:
    def __init__(self, abreviatura: str, nome_idioma: str):
        self.abreviatura = abreviatura
        self.nome_idioma = nome_idioma

class Estante:
    def __init__(self, identificacao_estante: str):
        self.identificacao_estante = identificacao_estante

class Emprestimo:
    def __init__(self, data_emprestimo: date, data_prevista_devolucao: date, data_devolucao: date = None):
        self.data_emprestimo = data_emprestimo
        self.data_prevista_devolucao = data_prevista_devolucao
        self.data_devolucao = data_devolucao

    def realizar_emprestimo(self):
        pass  # Implementação para realizar empréstimo

    def registar_devolucao(self):
        pass  # Implementação para registrar devolução

class Reserva:
    def __init__(self, data_pedido_reserva: date, data_mudanca_estado: date, estado_reserva: str):
        self.data_pedido_reserva = data_pedido_reserva
        self.data_mudanca_estado = data_mudanca_estado
        self.estado_reserva = estado_reserva

class Relatorio:
    def __init__(self, num_relatorio: int, tipo_relatorio: str, data_geracao: date):
        self.num_relatorio = num_relatorio
        self.tipo_relatorio = tipo_relatorio
        self.data_geracao = data_geracao

    def gerar_relatorio(self):
        pass  # Implementação para gerar relatório

# Exemplo de execução
if __name__ == "__main__":
    # Criando um objeto da classe Biblioteca
    biblioteca = Biblioteca(logotipo="Biblioteca Central", site="www.bibliotecacentral.com", nif=123456789)

    # Criando um livro
    livro1 = Livro(titulo="Python Avançado", descricao="Um livro sobre técnicas avançadas em Python.")
    
    # Adicionando o livro à biblioteca
    biblioteca.adicionar_livro(livro1)

    # Criando um bibliotecário
    bibliotecario = Bibliotecario(nome="Carlos Silva", telefone="123456789", e_mail="carlos@biblioteca.com", 
                                  aniversario=date(1985, 5, 15), data_criacao=date(2020, 1, 10), 
                                  sexo="Masculino", doc_identificacao="123456789", tipo_doc_identificacao="BI", 
                                  tipo_pessoa="Funcionário", tipo_acesso="Admin", nif=987654321, identificacao="B001")

    # Exibindo informações da biblioteca e do bibliotecário
    print(f"Biblioteca: {biblioteca.logotipo}, Site: {biblioteca.site}, NIF: {biblioteca.nif}")
    print(f"Bibliotecário: {bibliotecario.nome}, Identificação: {bibliotecario.identificacao}")
    print(f"Livro adicionado: {livro1.titulo}, Descrição: {livro1.descricao}")