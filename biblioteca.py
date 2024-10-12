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

    def registar_endereco(self, endereco):
        self.endereco = endereco

# Classe de Endereço
class Endereco:
    def __init__(self, morada: str, cidade: str, codigo_postal: str, pais: str):
        self.morada = morada
        self.cidade = cidade
        self.codigo_postal = codigo_postal
        self.pais = pais

# Biblioteca herda de Entidade
class Biblioteca(Entidade):
    def __init__(self, nome: str, telefone: str, e_mail: str, aniversario: date, data_criacao: date, nif: int, logotipo: str, site: str):
        super().__init__(nome, telefone, e_mail, aniversario, data_criacao, nif)
        self.logotipo = logotipo
        self.site = site
        self.itens_biblioteca = []

    def adicionar_item(self, item_biblioteca):
        self.itens_biblioteca.append(item_biblioteca)

    def exibir_informacoes(self):
        print(f"Biblioteca: {self.nome}")
        print(f"Site: {self.site}")
        print(f"NIF: {self.nif}")
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.e_mail}")
        print(f"Logotipo: {self.logotipo}")
        print(f"Quantidade de itens: {len(self.itens_biblioteca)}")

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

    def exibir_informacoes(self):
        print(f"\nBibliotecário: {self.nome}")
        print(f"Identificação: {self.identificacao}")
        print(f"Telefone: {self.telefone}")
        print(f"E-mail: {self.e_mail}")
        print(f"Sexo: {self.sexo}")

# Classe ItemBiblioteca (substitui Livro)
class ItemBiblioteca:
    def __init__(self, num_inventario: str, ident_item: str, data_entrada: date, titulo: str, descricao: str, tipo_item: str, 
                 imagem: str, ano_publicacao: int, estado_exemplar: str):
        self.num_inventario = num_inventario
        self.ident_item = ident_item
        self.data_entrada = data_entrada
        self.titulo = titulo
        self.descricao = descricao
        self.tipo_item = tipo_item
        self.imagem = imagem
        self.ano_publicacao = ano_publicacao
        self.estado_exemplar = estado_exemplar
        self.categorias_genero = []
        self.temas = []
        self.intervenientes = []
        self.idioma = None
        self.estante = None

    def registar_categoria_genero(self, categoria_genero):
        self.categorias_genero.append(categoria_genero)

    def registar_tema(self, tema):
        self.temas.append(tema)

    def registar_interveniente(self, interveniente):
        self.intervenientes.append(interveniente)

    def registar_idioma(self, idioma):
        self.idioma = idioma

    def registar_estante(self, estante):
        self.estante = estante

    def exibir_informacoes(self):
        print(f"\nItem: {self.titulo}")
        print(f"Identificador: {self.ident_item}")
        print(f"Número de Inventário: {self.num_inventario}")
        print(f"Descrição: {self.descricao}")
        print(f"Tipo: {self.tipo_item}")
        print(f"Ano de Publicação: {self.ano_publicacao}")
        print(f"Estado: {self.estado_exemplar}")
        if self.estante:
            print(f"Estante: {self.estante.identificacao_estante}")

# Classes auxiliares: CategoriaGenero, Tema, Interveniente, Idioma, Estante
class CategoriaGenero:
    def __init__(self, nome_cat_genero: str):
        self.nome_cat_genero = nome_cat_genero

class Tema:
    def __init__(self, nome_tema: str):
        self.nome_tema = nome_tema

class Interveniente:
    def __init__(self, num_interveniente: str, nome_interveniente: str, descricao_interveniente: str, tipo_interveniente: str):
        self.num_interveniente = num_interveniente
        self.nome_interveniente = nome_interveniente
        self.descricao_interveniente = descricao_interveniente
        self.tipo_interveniente = tipo_interveniente

class Idioma:
    def __init__(self, abreviatura: str, nome_idioma: str):
        self.abreviatura = abreviatura
        self.nome_idioma = nome_idioma

class Estante:
    def __init__(self, identificacao_estante: str):
        self.identificacao_estante = identificacao_estante

# Exemplo de execução
if __name__ == "__main__":
    # Criando um objeto da classe Biblioteca
    biblioteca = Biblioteca(nome="Biblioteca Central", telefone="1234-5678", e_mail="contato@biblioteca.com", 
                            aniversario=date(2000, 1, 1), data_criacao=date(2024, 10, 10), nif=123456789, 
                            logotipo="Logo", site="www.biblioteca.com")

    # Criando um item de biblioteca
    item1 = ItemBiblioteca(num_inventario="123", ident_item="ITM001", data_entrada=date(2024, 10, 10), 
                           titulo="Programação Python Avançada", descricao="Livro técnico sobre Python", 
                           tipo_item="Livro", imagem="capa.jpg", ano_publicacao=2023, estado_exemplar="Novo")

    # Criando uma estante e associando ao item
    estante1 = Estante(identificacao_estante="Estante 1")
    item1.registar_estante(estante1)

    # Adicionando o item à biblioteca
    biblioteca.adicionar_item(item1)

    # Criando um bibliotecário
    bibliotecario = Bibliotecario(nome="Carlos Silva", telefone="123456789", e_mail="carlos@biblioteca.com", 
                                  aniversario=date(1985, 5, 15), data_criacao=date(2020, 1, 10), 
                                  nif=987654321, sexo="Masculino", doc_identificacao="123456789", tipo_doc_identificacao="BI", 
                                  tipo_pessoa="Funcionário", tipo_acesso="Admin", identificacao="B001")

    # Exibindo informações da biblioteca
    biblioteca.exibir_informacoes()

    # Exibindo informações do item
    item1.exibir_informacoes()

    # Exibindo informações do bibliotecário
    bibliotecario.exibir_informacoes()


# Principais alterações:

# Substituição da classe Livro pela ItemBiblioteca para uma maior generalização de itens de biblioteca.
# Adicionadas as classes CategoriaGenero, Tema, Interveniente, Idioma, e Estante, conforme o diagrama atualizado.
# Métodos ajustados para permitir o registro de categorias, intervenientes, temas, idioma, e estantes no ItemBiblioteca.

# O que foi adicionado:
# Método exibir_informacoes() para as classes Biblioteca, Bibliotecario, e ItemBiblioteca.
# Mais detalhes são impressos no terminal ao executar o código, incluindo informações da biblioteca, itens, estante e bibliotecário.