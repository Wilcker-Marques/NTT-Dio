def deposito(saldo, valor, extrato,/):
    if valor < 0:
        print('Valor invalido')
    else:
        saldo += valor
        extrato += f'{'Deposito':<9} R$:{valor}.00\n'
        print(f'{'='*50}')
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if numero_saques >= LIMITE_SAQUES:
        print('Limite de saques atingidos')
    elif valor > limite:
        print('Limite de valor por saque atingido')
    elif valor > saldo:
        print('Saldo insuficiente')
    else:
        saldo -= valor
        extrato += f'{'Saque':<10} R$:{valor}.00\n'
        numero_saques += 1
        print(f'{'='*50}')
    return saldo, extrato, numero_saques

def historico(saldo, *, extrato):
    print(extrato if extrato else 'Nenhum operação executada')
    if extrato:
        print(f'{'saldo':<10}R$:{saldo}.00')

def criar_usuario(usuarios):
    cpf = str(input('CPF (apenas numeros): '))
    if cpf in usuarios:
        print('usuario ja cadastrado')
        return usuarios
    else:
        nome = str(input('nome completo: '))
        data_nascimento = str(input('Data de nascimento(00/00/0000): '))
        endereço = str(input('Endereco(logradouro, numero - bairro - cidade/sigla estado): '))
        usuario = {'nome':nome,'data_nascimento':data_nascimento,'endereço':endereço}
        usuarios[cpf] = usuario
        print('Usuario cadastrado com sucesso')
        return usuarios

def criar_contas(usuarios, contas,AGENCIA):
    cpf = str(input('CPF (apenas numeros): '))
    if cpf not in usuarios:
        print('usuario nao cadastrado')
        return contas
    else:
        numero_conta = len(contas) + 1
        usuario = usuarios[cpf]
        conta = {'Agencia':AGENCIA,'Numero da conta':numero_conta,'Usuario':usuario}
        contas.append(conta)
        print('Conta criada com sucesso')
        return contas
    
menu = '''
[1]Deposito
[2]Saque
[3]Extrato
[4]Criar usuario
[5]Criar conta
[6]Listar contas
[7]Sair
'''

def main():

    usuarios = {}
    contas = []
    saldo = 0
    extrato = ''
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    while True:
        try:
            opcao = int(input(f'{menu}=>'))
            if opcao == 1:
                print(f'{'Deposito':=^50}')
                valor = int(input('Valor de Deposito R$: '))
                saldo, extrato = deposito(saldo, valor, extrato)
            elif opcao == 2:
                print(f'{'Saque':=^50}')
                valor = int(input('Valor do saque R$:'))
                saldo, extrato, numero_saques = saque(
                                        saldo=saldo, valor=valor, 
                                        extrato=extrato, limite=limite,  
                                        numero_saques=numero_saques, 
                                        LIMITE_SAQUES=LIMITE_SAQUES
                                       )
            elif opcao == 3:
                print(f'{'Extrato':=^50}')
                historico(saldo, extrato=extrato)           
            elif opcao == 4:
                usuarios = criar_usuario(usuarios)
            elif opcao == 5:
                criar_contas(usuarios, contas, AGENCIA)
            elif opcao == 6:
                for c in contas:
                    print(f'{c}\n')
            elif opcao == 7:
                break
            else:
                print('Entrada invalida')
        except ValueError:
            print('Entrada invalida')

main ()