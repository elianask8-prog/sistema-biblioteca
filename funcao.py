# CADASTRAR LIVROS
def cadastrarLivro():  # cadastra os livros

    codigo = proximoCodigo()  # LIGA AUTOMATICAMENTE AS DUAS FUNÇOES
    titulo = input("Informe o titulo:")
    autor = input("Informe o autor:")
    ano = input("Informe o anos:")
    
    with open("livros.txt", "a", encoding="utf-8") as arquivo:  # quarda a inf. no arquivo ta a informaçao
        arquivo.write(f"{codigo};{titulo};{autor};{ano}\n")

    print("livro cadrastado!")


# PARA ARMAZENAR O CODIGO NO PROXIMO DEPOIS DO ULTIMO


def proximoCodigo():

    livros = lerLivros()
    codigo = []

    for livro in livros:
        colunas = livro.split(";")
        codigo.append(int(colunas[0]))
    ultimo = max(codigo)

    return ultimo + 1


# CADASTRO DO USUARIO


def cadastroUsuario():

    codigo = proximoCodigoUsuario()  # LIGA AUTOMATICAMENTE AS DUAS FUNÇOES
    nome = input("Informe o nome:")
    email = input("Informe o email:")
    
    with open("usuarios.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{codigo};{nome};{email}\n")


# PROXIMO CADASTRO DEPOIS DO ULTIMO
def proximoCodigoUsuario():
    usuarios = lerUsuarios()
    codigo = []
    for usuario in usuarios:
        coluna = usuario.strip().split(";")
        codigo.append(int(coluna[0]))
    ultimo = max(codigo)
    return ultimo + 1


# LISTAR LIVROS


def listarLivros():

    livros = lerLivros()

    if len(livros) == 0:
        print("Nenhum livro cadastrado")
        return

    for livro in livros:
        print(livro)


# LISTAR USUARIO


def listarUsuarios():
    usuarios = lerUsuarios()

    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado")
        return

    for usuario in usuarios:
        print(usuario)


# MOSTRAR OS LIVROS
def lerLivros():
    with open("livros.txt", "r", encoding="utf-8") as arquivo:
        dados = arquivo.readlines()
        return dados


# MOSTRAR OS USUARIOS
def lerUsuarios():
    with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
        dados = arquivo.readlines()
        return dados


# BUSCAR OS LIVROS MESMO SE O USUARIO ESCREVER DE LETRA MAIUSCULA
def buscarPorTitulo(termo: str):
    livros = lerLivros()
    for livro in livros:
        if termo.lower() in livro.lower():
            print(livro)


# REGISTRAR EMPRÉSTIMOS

# BUSCA OS LIVROS PELO ID= numero


def buscaLivrosPorId(id: int):
    livros = lerLivros()
    for livro in livros:
        coluna = livro.strip().split(";")
        if id == int(coluna[0]):
            return livro


# print(buscaLivrosPorId(3))


# BUSCA USUARIO, SABER SE ELE EXISTE, BUSCA POR ID


def buscaUsuarioPorId(id: int):
    usuarios = lerUsuarios()
    for usuario in usuarios:
        coluna = usuario.strip().split(";")
        if id == int(coluna[0]):
            return usuario


# print(buscaUsuarioPorId(2))


# VERIFICAR SE O LIVRO NÃO ESTÁ EMPRESTADO


def verificarEmprestimos():
    with open("emprestimos.txt", "r", encoding="utf-8") as arquivo:
        dados = arquivo.readlines()
        return dados


def consultaEmprestimos(id: int):
    emprestimos = verificarEmprestimos()
    for emprestimo in emprestimos:
        coluna = emprestimo.strip().split(";")
        if (int(coluna[0]) == id) and  coluna[4] == "ativo":  # coluna[0] codigo do livro,  id percorre pra ver se se há algum emprestado  # status
             
                print("Livro emprestado")
                return True
    return False





# GRAVAR EMPRESTIMOS


def registrarEmprestimo():
    codigo_livro = int(input("Informe o código do livro:"))
    id_usuario = int(input("Informe o código do usuario:"))
    data = input("Informe a data :")
    data_devolucao = ""
    status = "ativo"

    if not livroExiste(codigo_livro):
        print("Livro não encontado.")
        return

    if not usuarioExiste(id_usuario):
        print("Usuario não encontrado")
        return

    if livroEstaEmprestado(codigo_livro):
        print("Esse livro encontrasse emprestado")
        return

    with open("emprestimos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{codigo_livro};{id_usuario};{data};{data_devolucao};{status}\n")
        print("Emprestimo registrado com sucesso")


# registrarEmprestimo()

# FUNCAO AUXILIAR SUGERIDA, PARA VER SE EXISTE O LIVRO


def livroExiste(codigo):
    livros = buscaLivrosPorId(codigo)

    if livros:
        return True

    return False


# FUNCAO AUXILIAR SUGERIDA, PARA VER SE EXISTE O USUARIO


def usuarioExiste(id):
    usuario = buscaUsuarioPorId(id)

    if usuario:
        return True
    return False


# FUNCAO AUXILIAR SUGERIDA, PARA VER SE O LIVRO ESTÁ DISPONIVEL


def livroEstaEmprestado(codigo):
    emprestimo = consultaEmprestimos(codigo)

    if emprestimo:
        return True
    return False


# REGISTRAR DEVOLUÇÃO


def registrarDevolucao():
    import  datetime

    codigo = int(input("Informe o código do livro:"))  # solicita o codigo

    livros = verificarEmprestimos()
    resto = []  # guarda todo os emprestimos q deve ficar
    encontrou = False  # informa se foi encontado ou não

    for livro in livros:  # percorre
        coluna = livro.strip().split(";")  # quebra e tira os espaços

        if int(coluna[0]) == codigo:  # condição

            encontrou = True
        else:
            resto.append(livro)

    if encontrou:

        with open("emprestimos.txt", "w", encoding="utf-8") as arquivo:
            for livro in resto:
                arquivo.write(livro)

        print("Devolução efetuada com sucesso")
    else:
        print("Código não existente")


# registrarDevolucao()

# GERAR RELATORIO


def relatorioLivros():

    livrosCadastrado = lerLivros()

    cont = 0

    for livroCadastrado in livrosCadastrado:

        cont += 1

    # print("A quantidade livros cadastrasdos é : ", cont)
    return cont


# relatorioLivros()


def relatorioUsuarios():

    usuariosCadastrado = lerUsuarios()

    cont = 0

    for usuarioCadastrado in usuariosCadastrado:

        cont += 1
    # print("A quantidade usuarios cadastrasdos é : ", cont)
    return cont


# relatorioUsuarios()


"""def relatorioEmprestimo():

    livrosEmprestado = verificarEmprestimos()  # Quantidade de livros emprestados
"""

#MENU PRINCIPAL

def menuPrincipal():
    import os

    menu = {
    "1": cadastrarLivro,
    "2": listarLivros,
    "3": cadastroUsuario,
    "4": listarUsuarios,
    "5": registrarEmprestimo,
    "6": registrarDevolucao
}
    os.system('cls')
    while True:
        print("\n=== SISTEMA DE BIBLIOTECA ===")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Cadastrar usuário")
        print("4 - Listar usuários")
        print("5 - Registrar empréstimo")
        print("6 - Devolver livro")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            break

        if escolha in menu:
            menu[escolha]()
            input()
        else:
            print("Opção inválida")

menuPrincipal()