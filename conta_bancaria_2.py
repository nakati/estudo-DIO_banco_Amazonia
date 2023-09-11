
import textwrap

def menu():
    menu = """
    \033[32m//////////////////////////////////////////////  BANCO AMAZONIA //////////////////////////////////////////////

    MENU - Escolha a opção: 

    [d] Depositar   [s] Sacar   [e] Extrato   [nc] Nova Conta   [lc] Listar Contas   [nu] Novo Usuário   [x] Sair

    => \033[m"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor_dep, extrato, /): # recebendo argumentos por posição "/" o q estiver antes deve ser por posição
    if valor_dep > 0:
        saldo += valor_dep
        extrato += f'Depósito:\tR$ {valor_dep:.2f}\n'
        print('\nDepósito efetuado com sucesso. Obrigado por estar conosco!\n')
        print(f'Saldo atual: R$ {saldo:.2f}\n')
                
    else:
        print("\033[31m'Operação falhou! O valor informado é inválido'\033[m")

    return saldo, extrato

def sacar(*, saldo, valor_saq, extrato, limite, numero_saques, limite_saques): # argumentos de forma nomeada (*)
    excedeu_saldo = valor_saq > saldo
    excedeu_limite = valor_saq > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\033[31m'Operação falhou! Você não tem saldo suficiente.'\033[m")
            
    elif excedeu_limite:
        print("\033[31m'Operação falhou! O valor do saque excede o limite para cada saque.'\033[m")

    elif excedeu_saques:
        print("\033[31m'Operação falhou! Número máximo de saques excedido.'\033[m")
            
    elif valor_saq > 0:
        saldo -= valor_saq
        extrato += f'Saque:\t\tR$ {valor_saq:.2f}\n'
        numero_saques += 1
        print('\nSaque efetuado com sucesso. SEJA FELIZ!\n')
        print(f'Saldo atual: R$ {saldo:.2f}\n')

    else:
        print("\033[31m'Operação falhou! O valor informado é inválido.'\033[m")    
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n============== EXTRATO ==============')
    print('Não foram realizadas movimentações.' if not extrato else extrato) #else extrato = exibe o extrato
    print(f'\nSaldo atual:\tR$ {saldo:.2f}')
    print('=====================================')

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n\033[31m'Já existe usuário com este CPF!'\033[m")
        return # aqui ele retorna pro criar_usuario do main pra dar sequencia exibindo o menu
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informa a data de nascimento (dd-mm-aa): ')
    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco}) # adiciona p/ lista

    print('Usuário criado com sucesso!')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf] # na lista de usuarios(in usuarios) faço um filtro=se o usuario q estou percorrendo naquele momento, ou seja, se o cpf dele for igual ao que eu passei (==cpf) no argumento(cpf), vai retornar usuario pra mim, se não for, a lista vai ficar vazia.
    return usuarios_filtrados[0] if usuarios_filtrados else None # verificando se usuarios filtrados tem conteudo(if usuarios filtrados). Se não for uma lista vazia, ele retorna o 1º elemento(usuarios_filtrados[0]). Se não encontrar, retornará None.

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print("\n\033[31m'Usuário não encontrado, fluxo de criação de conta encerrado!'\033[m")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print('=' * 100)
        print(textwrap.dedent(linha)) #dedent funciona pra formatação do codigo

def main():
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    LIMITE_SAQUES = 3 
    AGENCIA = "0001"


    while True:
        opcao = menu()

        if opcao.upper() == 'D':
            valor_dep = float(input('Informe o valor do depósito: '))
            saldo, extrato = depositar(saldo, valor_dep, extrato)
        
        elif opcao.upper() == 'S':
            valor_saq = float(input('Informe o valor do saque: '))
            saldo, extrato = sacar(
                saldo=saldo, # daqui pra baixo é passagem por chave (keyword only)
                valor_saq=valor_saq, # CHECAR ESTA VARIAVEL VALOR ///////////////////////////////////////////////////////////////////////
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,            
            )
            

        elif opcao.upper() == 'E':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao.upper() == "NU":
            criar_usuario(usuarios) # passado parametro chamado usuarios(é uma lista)
        
        elif opcao.upper() == "NC": # feito diferente nc
            
            listar_contas(contas)
     
        
        elif opcao.upper() == 'X':
            break

        else:
            print("\033[31m'Operação inválida, por favor selecione novamente a operação desejada.'\033[m")

main()


