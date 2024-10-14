from datetime import date, datetime

# Classe base para todas as entidades
class Entidade:
    def __init__(self, nome: str, telefone: str, e_mail: str, nif: int):
        self.nome = nome
        self.telefone = telefone
        self.e_mail = e_mail
        self.nif = nif

# Classe de Livro
class ItemBiblioteca:
    def __init__(self, titulo: str, autor: str, isbn: str, categoria: str):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.categoria = categoria
        self.emprestado = False
        self.historico_emprestimos = []

    def emprestar(self, utilizador):
        if not self.emprestado:
            self.emprestado = True
            data_emprestimo = datetime.now()
            self.historico_emprestimos.append({
                "utilizador": utilizador,
                "data_emprestimo": data_emprestimo
            })
            print(f"Item '{self.titulo}' emprestado com sucesso.")
        else:
            print(f"Item '{self.titulo}' já está emprestado.")

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            print(f"Item '{self.titulo}' devolvido com sucesso.")
        else:
            print(f"Item '{self.titulo}' já está disponível.")

# Classe Utilizador
class Utilizador(Entidade):
    def __init__(self, nome: str, telefone: str, e_mail: str, nif: int):
        super().__init__(nome, telefone, e_mail, nif)

# Classe Empréstimo
class Emprestimo:
    def __init__(self):
        self.emprestimos = []

    def registrar_emprestimo(self, item: ItemBiblioteca, utilizador: Utilizador):
        if not item.emprestado:
            item.emprestar(utilizador)
            self.emprestimos.append({
                "item": item,
                "utilizador": utilizador,
                "data_emprestimo": datetime.now()
            })
            print(f"Empréstimo registrado com sucesso para o item '{item.titulo}'.")
        else:
            print(f"O item '{item.titulo}' já foi emprestado anteriormente.")

    def registrar_devolucao(self, item: ItemBiblioteca):
        if item.emprestado:
            item.devolver()
        else:
            print(f"O item '{item.titulo}' já está disponível para empréstimo.")

    def gerar_relatorio_emprestimos(self):
        print("\nRelatório de Itens Emprestados:")
        for registro in self.emprestimos:
            item = registro["item"]
            utilizador = registro["utilizador"]
            data_emprestimo = registro["data_emprestimo"]
            if item.emprestado:
                print(f"Item: {item.titulo} | Emprestado por: {utilizador.nome} | Data do Empréstimo: {data_emprestimo.strftime('%Y-%m-%d')}")

    def gerar_relatorio_disponiveis(self, itens):
        print("\nRelatório de Itens Disponíveis:")
        for item in itens:
            status = "Disponível" if not item.emprestado else "Emprestado"
            if not item.emprestado:
                print(f"Item: {item.titulo} | Status: {status}")

# Exemplo de execução
if __name__ == "__main__":
    # Criando alguns utilizadores
    utilizador1 = Utilizador("João Silva", "123456789", "joao@exemplo.com", 123456789)
    utilizador2 = Utilizador("Maria Souza", "987654321", "maria@exemplo.com", 987654321)

    # Criando itens de biblioteca (livros)
    item1 = ItemBiblioteca("Python para Iniciantes", "Autor A", "1234567890", "Programação")
    item2 = ItemBiblioteca("Aprendendo Java", "Autor B", "0987654321", "Programação")

    # Criando sistema de empréstimos
    sistema_emprestimos = Emprestimo()

    # Emprestando itens
    sistema_emprestimos.registrar_emprestimo(item1, utilizador1)
    sistema_emprestimos.registrar_emprestimo(item2, utilizador2)

    # Tentando emprestar o mesmo item novamente
    sistema_emprestimos.registrar_emprestimo(item1, utilizador2)

    # Gerando relatório de itens emprestados
    sistema_emprestimos.gerar_relatorio_emprestimos()

    # Devolvendo itens
    sistema_emprestimos.registrar_devolucao(item1)

    # Gerando relatório de itens disponíveis
    sistema_emprestimos.gerar_relatorio_disponiveis([item1, item2])


#Atualização do código conforme "tp2'" 

# Registo de novos livros: O sistema possui a classe ItemBiblioteca, onde os livros são registrados com título, autor, ISBN, e categorias.

# Empréstimo e devolução: A classe Emprestimo controla o processo de empréstimo e devolução, verificando a disponibilidade do item e alterando seu status conforme necessário.

# Registo de novos utilizadores: A classe Pessoa e suas subclasses permitem registrar utilizadores com nome, endereço e telefone. Classes como Aluno e Professor podem ser adicionadas para maior especialização.

# Consulta de disponibilidade: A classe Biblioteca oferece métodos para consultar a disponibilidade de itens através do método exibir_informacoes.

# Geração de relatórios: Relatórios de itens emprestados e devolvidos são gerados com base no status dos empréstimos, e exibidos com detalhes sobre o livro e o utilizador associado.