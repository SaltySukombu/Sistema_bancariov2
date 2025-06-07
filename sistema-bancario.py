import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    #complete o código

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    #complete o código

def exibir_extrato(saldo, /, *, extrato):
    #complete o código

def criar_usuario (usuarios):
    cpf = int(input("Informe seu cpf (apenas números): "))
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Este usuário já existe.")
        return
    nome = input("Digite o seu nome: ").lower()
    data_nascimento = int(input("Digite sua data de nascimento (em formato dd-mm-aaaa): "))
    endereco = float("Digite o seu endereço (em forato de: logradouro, número-bairro-cidade/sigla do estado): ")

def filtrar_usuario(cpf, usuarios):
    usuarios = ("",)
    cpfs = ("",)

def criar_conta(agencia, numero_conta, usuarios):
    

def listar_contas(contas):
    #complete o código

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo 

main()