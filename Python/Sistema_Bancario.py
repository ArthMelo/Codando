
def saque(saldo, numero_saques, LIMITE_SAQUE, limite):
    mensagem = '''
        [1] Realizar outro saque
        [2] Sair
    '''
    while True:
        retirar = int(input('Qual o valor de saque: '))
        if numero_saques >= LIMITE_SAQUE:
            print('Limites de Saldo atingido')
            break
        elif retirar < saldo:
            print('Nao sera possivel sacar o dinheiro por falta de saldo')
            while True:
                alternativa = int(input(mensagem))
                if alternativa == 1:
                    saque(saldo, numero_saques, LIMITE_SAQUE, limite)
                elif alternativa == 2:
                    break
                else: 
                    print('Escolha uma opcao valida!')
        elif retirar > limite:
            print('Valor acima do permitido para saque')
            while True:
                alternativa = int(input(mensagem))
                if alternativa == 1:
                    saque(saldo, numero_saques, LIMITE_SAQUE, limite)
                elif alternativa == 2:
                    break
                else:
                    print('Escolha uma opcao valida!')
        else:
            saldo -= retirar
            numero_saques += 1
            break

def visualizarExtrato(saldo):
    print(f"Saldo de R${saldo}")

mensagemMenu = '''
=================MENU==================

    [1] Deposito
    [2] Saque
    [3] Visualizar extrato
    [4] Sair

=======================================
'''

saldo = 0
limite = 500
extrato = ""
numeroSaques = 0
LIMITE_SAQUE = 3

while True:
    escolha = input(mensagemMenu)
    if escolha == '1':
        while True:
            valor = input('Qual o valor a ser depositado: ')
            valor_inteiro = int(valor)
            if valor_inteiro <= 1:
                print('Digite um valor valido!\n')
            else: 
                saldo += valor_inteiro
                extrato += f"Deposito realizado de R${valor_inteiro:.2f}\nSaldo atual é de R${saldo:.2f}\n\n"
                break

    elif escolha == '2':

        mensagem = '''
    [1] Realizar outro saque
    [2] Sair
        '''
        while True:
            retirar = int(input('Qual o valor de saque: '))
            if numeroSaques >= LIMITE_SAQUE:
                print('Limites de Saldo atingido\n')
                break
            elif retirar > saldo:
                print('Nao sera possivel sacar o dinheiro por falta de saldo\n')
                break
            elif retirar > limite:
                print('Valor acima do permitido para saque\n')
                break
            else:
                saldo -= retirar
                numeroSaques += 1
                extrato += f"Saque realizado de R${retirar:.2f}\nSaldo atual é de R${saldo:.2f}\n\n"
                break

    elif escolha == '3':
        print(extrato)
    elif escolha == '4':
        print('Saindo...')
        break
    else:
        print("Escolha uma opção válida")


