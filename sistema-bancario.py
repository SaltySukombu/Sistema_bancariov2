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
    data_nascimento = input("Digite sua data de nascimento (em formato dd-mm-aaaa): ")
    endereco = input("Digite o seu endereço (em forato de: logradouro, número-bairro-cidade/sigla do estado): ")

def filtrar_usuario(cpf, usuarios):
    usuarios = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios[0] if usuarios else None

def criar_conta(agencia, numero_conta, usuarios):
   cpf = input("Digite o CPF do titular da conta: ")
   usuario = filtrar_usuario(cpf, usuarios)
   if usuarios:
       print("Conta criada com sucesso")
       return {
            "agência" == agencia,
           "número da conta" == numero_conta,
           "usuário" == usuario
       }
   else:
       print("Usuário não encontrado. Não foi possível criar uma conta.")
       return None

def listar_contas(contas):
    

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