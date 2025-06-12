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
   if usuario:
       print("Conta criada com sucesso")
       return {
            "agência": agencia,
           "número da conta": numero_conta,
           "usuário": usuario
       }
   else:
       print("Usuário não encontrado. Não foi possível criar uma conta.")
       return None

def listar_contas(contas):
    for conta in contas:
        print(f"Número da agência é {conta['agencia']}")
        print(f"Número da conta é {conta['numero_conta']}")
        print(f"O titular é {conta['usuario']['nome']}")

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

            elif opcao == "nc":
                criar_conta(AGENCIA, numero_conta, usuarios)
                numero_conta += 1

            elif opcao == "lc":
                listar_contas(conta)

            elif opcao == "nu":
                criar_usuario(usuarios)

            elif opcao == "q":
                break
    main()