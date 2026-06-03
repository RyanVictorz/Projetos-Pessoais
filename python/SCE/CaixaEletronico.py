def Deposito(valor, saldo):
    if valor <= 0:
        print("Valor inválido!")
    else:
        saldo += valor
        print("Depósito realizado com sucesso!")
    return saldo

def Saque(valor, saldo):
    if valor < 0:
        print("Valor inválido!")
    elif valor > saldo:
        print("Valor insuficíente!")
    else:
        saldo -= valor
        print("Saque realizado com sucesso!")
    return saldo

saldo = 1000.0
while True:
    print("----------------\n")
    print("CAIXA ELETRÔNICO\n")
    print("1- Depósito.\n2- Saque.\n3- Ver extrato.\n4- Sair.")
    print("\n----------------")

    opcao = input("Informe sua opção: ")
    if opcao not in ("1", "2", "3", "4"):
        print("\nOpção ínvalida! Escolha uma das opções a seguir...")

    elif opcao == "1":
        valor = float(input("Informe o valor a ser depósitado: R$"))
        saldo = Deposito(valor, saldo)
    elif opcao == "2":
        valor = float(input("Informe o valor a ser retirado: R$"))
        saldo = Saque(valor, saldo)
    elif opcao == "3":
        print(f"Seu saldo é R${saldo:.2f}.")
    else:
        break
