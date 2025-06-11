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

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > 0:
        excedeu_saldo = valor > saldo
        excedeu_o_limite = limite > 500
        excedeu_o_limite_de_saques = limite_saques > 3
        if excedeu_o_limite:
            print("Voce excedeu o limite")
        elif excedeu_o_limite_de_saques:
            print("Voce excedeu o limite de saques")
        elif excedeu_saldo:
            print("Voce excedeu o saldo")
        elif valor>0:
            saldo -= valor
            extrato +=f"Saque:R${valor:.2f}\n"
            numero_saques += 1
        else:
            print("A operação falhou")
        return saldo,extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n========EXTRATO========")
    print("Não foram realizado as movimentaçoes."if not extrato else extrato)
    print(f"\nSaldo:R${saldo:.2f}")
    print("\n=======================")
    

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

            elif opcao =="s":
                 valor = float(input("Informe o valor do saque: "))

                 saldo,extrato = sacar(
                     saldo = saldo, 
                     valor = valor, 
                     extrato = extrato, 
                     limite = limite, 
                     numero_saques = numero_saques, 
                     limite_saques = LIMITE_SAQUES
                     )
            elif opcao == "e":
                exibir_extrato(saldo, extrato = extrato)

            elif opcao == "q":
                break
    main()