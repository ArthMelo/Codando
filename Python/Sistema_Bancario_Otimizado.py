menu = """
=================MENU===================
[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar Conta
[n] Novo Usuario
[l] Listar Contas
[q] Sair
=======================================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
AGENCIA = "0001"

def deposito(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return saldo, extrato
    else:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato

def saque(*, valor, saldo, extrato, numero_saques, limite, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato, numero_saques
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastro_usuario(usuario):
    cpf = input("Informe o CPF do usuário: ")
    if verifica_cpf(cpf, usuarios):
        print("CPF já cadastrado!\n")
        return

    data_de_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço: ")
    usuarios.append({"Nome": usuario, "Data_de_nascimento": data_de_nascimento, "CPF": cpf, "Endereco": endereco})
    print(f"Usuário {usuario} cadastrado com sucesso!")

def cadastro_conta(agencia, numero_conta, usuario):
    conta = {"Agencia": agencia, "Numero_conta": numero_conta, "Usuario": usuario}
    contas.append(conta)
    print(f"Conta {numero_conta} criada com sucesso para o usuário {usuario['Nome']}!")

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        print("\n======= LISTA DE CONTAS =======")
        for conta in contas:
            print(f"Agência: {conta['Agencia']}, Conta: {conta['Numero_conta']}, Usuário: {conta['Usuario']['Nome']}")
        print("================================")

def verifica_cpf(cpf, usuarios):
    for usuario in usuarios:
        if usuario["CPF"] == cpf:
            return usuario
    return None

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(valor, saldo, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = saque(valor=valor, saldo=saldo, extrato=extrato, numero_saques=numero_saques, limite=limite, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "c":
        cpf = input("Informe o CPF do usuário para a conta: ")
        usuario = verifica_cpf(cpf, usuarios)
        if usuario:
            numero_conta = len(contas) + 1
            cadastro_conta(AGENCIA, numero_conta, usuario)
        else:
            print("Usuário não encontrado. Cadastre o usuário primeiro.")

    elif opcao == "n":
        usu = input("Informe o nome do usuário: ")
        cadastro_usuario(usuario=usu)

    elif opcao == "l":
        listar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
