menu = f'''
{'Dio Bank':=^50}
[1] Deposito
[2] Saque
[3] Extrato
[4] Sair

=>'''

contador = 0
LIMITE = 500
LIMITE_SAQUE = 3
extrato = ""
saldo = 0

while True:
    opçao = int(input(menu))

    if opçao == 1:
        print(f'\n{'Deposito':=^50}\n')
        deposito = int(input("Informe o valor : R$ "))
        saldo += deposito
        extrato += f'Deposito R$ {deposito:.2f}\n'
    
    elif opçao == 2:
        print(f'\n{'Saque':=^50}\n')
        saque = int(input("Informe o valor : R$ "))
        if contador >= LIMITE_SAQUE:
            print('Numeros de saques diarios atingidos')        
        elif saque > saldo:
            print('Saldo insufisiente para saque')
        elif saque > LIMITE:
            print('Valor de saque maior que permitido')
        else:
            saldo -= saque
            extrato += f'Saque R$ {saque:.2f}\n'
            contador += 1

    elif opçao == 3:
        print(f'\n{'Extrato':=^50}')
        print(f'{'Nenhum valor depositado 'if not extrato else extrato}')#if not verifica se extrato esta vazia,se não esiver imprime extrato
        print(f'{'='*50}')
        print(f'Saldo R$ {saldo:.2f}')
        print(f'{'='*50}')

    elif opçao == 4:
        break

    else:
        print("Entrada invalida, tente novamente.")