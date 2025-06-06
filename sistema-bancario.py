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
    if valor > 0:
        saldo += valor
        extrato = f"Deposito:R${valor:.2f}\n"
        print("O deposito foi realizado com sucesso")
    else:
        print("A operação falhou, o valor informado e invalido")
    return saldo,extrato
    #complete o código

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > 0:
        valor -= saldo
        excedeu_o_limite = limite > 500
        excedeu_o_limite_de_saques = limite_saques > 3
    #complete o código

#def exibir_extrato(saldo, /, *, extrato):
    #complete o código

#def criar_usuario (usuarios):
    #complete o código

#def filtrar_usuario(cpf, usuarios):
    #complete o código

#def criar_conta(agencia, numero_conta, usuarios):
    #complete o código

#def listar_contas(contas):
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

                saldo,extrato = depositar(saldo,valor,extrato)

                print(extrato)

            elif opcao == "q":
                break
    main()