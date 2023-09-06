

menu = """
/////////////////////////////  BANCO AMAZONIA /////////////////////////////

MENU - Escolha a opção: 

[d] Depositar     [s] Sacar     [e] Extrato     [x] Sair

=> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3 

while True:
    opcao = input(menu)

    if opcao.upper() == 'D':
        valor_dep = float(input('Informe o valor do depósito: '))

        if valor_dep > 0:
            saldo += valor_dep
            extrato += f'Depósito : R$ {valor_dep:.2f}\n'
            print('\nDepósito efetuado com sucesso. Obrigado por estar conosco!\n')
            print(f'Saldo atual: R$ {saldo:.2f}\n')
        
        else:
            print("\033[31m'Operação falhou! O valor informado é inválido'\033[m")
    
    elif opcao.upper() == 'S':
        valor_saq = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor_saq > saldo
        
        excedeu_limite = valor_saq > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\033[31m'Operação falhou! Você não tem saldo suficiente.'\033[m")
        
        elif excedeu_limite:
            print("\033[31m'Operação falhou! O valor do saque excede o limite para cada saque.'\033[m")

        elif excedeu_saques:
            print("\033[31m'Operação falhou! Número máximo de saques excedido.'\033[m")
        
        elif valor_saq > 0:
            saldo -= valor_saq
            extrato += f'Saque: R$ {valor_saq:.2f}\n'
            numero_saques += 1
            print('\nSaque efetuado com sucesso. SEJA FELIZ!\n')
            print(f'Saldo atual: R$ {saldo:.2f}\n')

        else:
            print("\033[31m'Operação falhou! O valor informado é inválido.'\033[m")

    elif opcao.upper() == 'E':
        print('\n============== EXTRATO ==============')
        print('Não foram realizadas movimentações.' if not extrato else extrato) #else extrato = exibe o extrato
        print(f'\nSaldo atual: R$ {saldo:.2f}')
        print('=====================================')

    elif opcao.upper() == 'X':
        break

    else:
        print("\033[31m'Operação inválida, por favor selecione novamente a operação desejada.'\033[m")


