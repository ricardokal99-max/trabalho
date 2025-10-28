# PASSO 1: Definição da classe Livro
class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def __str__(self):
        return f"Título: {self.titulo} | Autor: {self.autor} | Gênero: {self.genero} | Quantidade: {self.quantidade}"


# PASSO 2: Lista para armazenar os livros cadastrados
biblioteca = []  # Lista vazia que armazenará objetos da classe Livro


# PASSO 3.1: Função para cadastrar um novo livro
def cadastrar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o gênero do livro: ")
    quantidade = int(input("Digite a quantidade disponível: "))
    livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.append(livro)
    print("Livro cadastrado com sucesso!\n")


# PASSO 3.2: Função para listar todos os livros
def listar_livros():
    if not biblioteca:
        print("Nenhum livro cadastrado ainda.\n")
    else:
        print("Lista de livros disponíveis:\n")
        for livro in biblioteca:
            print(livro)
        print()


# PASSO 3.3: Função para buscar livro pelo título
def buscar_livro():
    titulo_busca = input("Digite o título do livro que deseja buscar: ").lower()
    encontrados = [livro for livro in biblioteca if livro.titulo.lower() == titulo_busca]

    if encontrados:
        print("Livro(s) encontrado(s):\n")
        for livro in encontrados:
            print(livro)
    else:
        print("Livro não encontrado.\n")


# PASSO 4: Gerar gráfico com quantidade de livros por gênero
def gerar_grafico():
    import matplotlib.pyplot as plt
    from collections import defaultdict

    if not biblioteca:
        print("Nenhum livro cadastrado para gerar gráfico.\n")
        return

    genero_contagem = defaultdict(int)
    for livro in biblioteca:
        genero_contagem[livro.genero] += livro.quantidade

    generos = list(genero_contagem.keys())
    quantidades = list(genero_contagem.values())

    plt.figure(figsize=(10, 6))
    plt.bar(generos, quantidades, color='skyblue')
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade de Livros")
    plt.title("Quantidade de Livros por Gênero")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# PASSO 5: Menu principal para testar o sistema
def menu():
    while True:
        print("=== Sistema de Gerenciamento de Livros ===")
        print("1. Cadastrar novo livro")
        print("2. Listar todos os livros")
        print("3. Buscar livro por título")
        print("4. Gerar gráfico por gênero")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            buscar_livro()
        elif opcao == '4':
            gerar_grafico()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


# Iniciar o menu do sistema
menu()