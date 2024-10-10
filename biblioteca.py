from datetime import date

# Classe base para todas as entidades
class Entidade:
    def __init__(self, nome: str, telefone: str, e_mail: str, aniversario: date, data_criacao: date, nif: int):
        self.nome = nome
        self.telefone = telefone
        self.e_mail = e_mail
        self.aniversario = aniversario
        self.data_criacao = data_criacao
        self.nif = nif
        self.endereco = None

    def registar_pessoa(self, pessoa):
        pass  # Implementação do método para registrar pessoa

    def registar_endereco(self, endereco):
        self.endereco = endereco

# Biblioteca herda de Entidade
class Biblioteca(Entidade):
    def __init__(self, nome: str, telefone: str, e_mail: str, aniversario: date, data_criacao: date, nif: int, logotipo: str, site: str):
        super().__init__(nome, telefone, e_mail, aniversario, data_criacao, nif)
        self.logotipo = logotipo
        self.site = site
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

# Classe de endereço
class Endereco:
    def __init__(self, morada: str, cidade: str, codigo_postal: str, pais: str):
        self.morada = morada
        self.cidade = cidade
        self.codigo_postal = codigo_postal
        self.pais = pais

# Classe Pessoa herda de Entidade
class Pessoa(Entidade):
    def __init__(self, nome: str, telefone: str, e_mail: str, aniversario: date, data_criacao: date, nif: int, sexo: str, 
                 doc_identificacao: str, tipo_doc_identificacao: str, tipo_pessoa: str, tipo_acesso: str):
        super().__init__(nome, telefone, e_mail, aniversario, data_criacao, nif)
        self.sexo = sexo
        self.doc_identificacao = doc_identificacao
        self.tipo_doc_identificacao = tipo_doc_identificacao
        self.tipo_pessoa = tipo_pessoa
        self.tipo_acesso = tipo_acesso

# Classe Bibliotecário herda de Pessoa
class Bibliotecario(Pessoa):
    def __init__(self, nome: str, telefone: str, e_mail: str, aniversario: date, data_criacao: date, nif: int, sexo: str, 
                 doc_identificacao: str, tipo_doc_identificacao: str, tipo_pessoa: str, tipo_acesso: str, identificacao: str):
        super().__init__(nome, telefone, e_mail, aniversario, data_criacao, nif, sexo, doc_identificacao, tipo_doc_identificacao, 
                         tipo_pessoa, tipo_acesso)
        self.identificacao = identificacao

    def registar_livro(self, livro):
        pass  # Implementação do método para registrar livro

    def gerar_relatorio(self):
        pass  # Implementação para gerar relatório

    def gerar_devolucao(self, emprestimo):
        pass  # Implementação para gerar devolução

    def registar_reserva(self, reserva):
        pass  # Implementação para registrar reserva

# Classe Livro
class Livro:
    def __init__(self, titulo: str, descricao: str):
        self.titulo = titulo
        self.descricao = descricao
        self.exemplares = []

    def registar_exemplar(self, exemplar):
        self.exemplares.append(exemplar)

# Classe Exemplar
class Exemplar:
    def __init__(self, num_exemplar: str, isbn: str, capa: str, ano_publicacao: int, estado_exemplar: str):
        self.num_exemplar = num_exemplar
        self.isbn = isbn
        self.capa = capa
        self.ano_publicacao = ano_publicacao
        self.estado_exemplar = estado_exemplar

    def registar_idioma(self, idioma):
        self.idioma = idioma

    def registar_editora(self, editora):
        self.editora = editora

    def registar_estante(self, estante):
        self.estante = estante

# Classe Emprestimo
class Emprestimo:
    def __init__(self, data_emprestimo: date, data_prevista_devolucao: date, data_devolucao: date = None):
        self.data_emprestimo = data_emprestimo
        self.data_prevista_devolucao = data_prevista_devolucao
        self.data_devolucao = data_devolucao

# Exemplo de execução
if __name__ == "__main__":
    # Criando um objeto da classe Biblioteca
    biblioteca = Biblioteca(nome="Biblioteca Central", telefone="1234-5678", e_mail="contato@biblioteca.com", 
                            aniversario=date(2000, 1, 1), data_criacao=date(2024, 10, 10), nif=123456789, 
                            logotipo="Logo", site="www.biblioteca.com")

    # Criando um livro
    livro1 = Livro(titulo="Python Avançado", descricao="Um livro sobre técnicas avançadas em Python.")
    
    # Adicionando o livro à biblioteca
    biblioteca.adicionar_livro(livro1)

    # Criando um bibliotecário
    bibliotecario = Bibliotecario(nome="Carlos Silva", telefone="123456789", e_mail="carlos@biblioteca.com", 
                                  aniversario=date(1985, 5, 15), data_criacao=date(2020, 1, 10), 
                                  nif=987654321, sexo="Masculino", doc_identificacao="123456789", tipo_doc_identificacao="BI", 
                                  tipo_pessoa="Funcionário", tipo_acesso="Admin", identificacao="B001")

    # Exibindo informações da biblioteca e do bibliotecário
    print(f"Biblioteca: {biblioteca.nome}, Site: {biblioteca.site}, NIF: {biblioteca.nif}")
    print(f"Bibliotecário: {bibliotecario.nome}, Identificação: {bibliotecario.identificacao}")
    print(f"Livro adicionado: {livro1.titulo}, Descrição: {livro1.descricao}")
