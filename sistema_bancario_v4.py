class Cliente:
    def __init__(self, endereco, contas=None):
        self._endereco = endereco
        self._contas = contas if contas else []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento, contas=None):
        super().__init__(endereco, contas)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente, saldo=0, agencia='0001'):
        self._saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    def nova_conta(self, cliente, conta):
        cliente.adicionar_conta(conta)

    def sacar(self, valor):
        if self._saldo < valor:
            print('Valor insuficiente')
        else:
            self._saldo -= valor

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f'Depósito de {valor} realizado com sucesso!')
        else:
            print('Valor de depósito inválido')

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, saldo=0, agencia='0001', limite=500, limite_saques=3):
        super().__init__(numero, cliente, saldo, agencia)
        self._limite = limite
        self._limite_saques = limite_saques

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Transacao:
    def registrar(self, conta):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)
