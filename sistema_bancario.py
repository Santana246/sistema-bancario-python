# Menu
menu = """

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair da conta

=> """

# Variáveis de contas
conta1 = [1, "1234", 0, 700, "", 0, 3]
conta2 = [2, "5678", 0, 500, "", 0, 4]
conta3 = [3, "kelly09", 0, 600, "", 0, 4]

# Menu de login
menu_login = """
Para entrar, digite os dados de sua conta no seguinte formato => Número da conta/Senha

Para sair do sistema, digite q

=>"""

# Função principal
def progBanco(saldo, limite, extrato, num_saques, LIM_SAQUES):

    # Variáveis funcionais
    saldo = saldo
    limite = limite
    extrato = extrato
    num_saques = num_saques
    LIM_SAQUES = LIM_SAQUES

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"

            else:
                print("Erro! Valor inválido.")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = num_saques >= LIM_SAQUES

            if excedeu_saldo:
                print("Erro! Saldo insuficiente.")

            elif excedeu_limite:
                print("Erro! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Erro! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                num_saques += 1

            else:
                print("Erro! Valor inválido.")

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            if not extrato:
                print("Sem movimentações.")
                print("=========================================")
            else:
                print(extrato)
                print(f"\nSaldo: R$ {saldo:.2f}")
                print("=========================================")

        elif opcao == "q":
            break

        else:
            print("Selecione uma operação válida dentre as apresentadas.")

# Código principal
while True:
    login = input(menu_login)

    if login == "q":
        break

    num_conta = login.split('/')[0]
    senha_conta = login.split('/')[1]

    if int(num_conta) == int(conta1[0]) and senha_conta == conta1[1]:
        progBanco(conta1[2], conta1[3], conta1[4], conta1[5], conta1[6])
    elif int(num_conta) == int(conta2[0]) and senha_conta == conta2[1]:
        progBanco(conta2[2], conta2[3], conta2[4], conta2[5], conta2[6])
    elif int(num_conta) == int(conta3[0]) and senha_conta == conta3[1]:
        progBanco(conta3[2], conta3[3], conta3[4], conta3[5], conta3[6])
    else:
        print("Insira os dados para uma conta válida.")