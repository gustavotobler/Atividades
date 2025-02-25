from datetime import datetime
import pytz 
class contaCorrente:
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR
    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))
        pass

    def depositar_dinheiro(self, valor):
        self.saldo += valor
        self.transacoes.appedn((valor , self.saldo, contaCorrente._data_hora()))
        pass
    
    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    
    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self.limite_conta():
            print('Você não tem saldo suficiente para sacar este valor!')
            self.consultar_saldo()
        else:
            self.saldo -= val
            self.transacoes.append((valor, self.saldo, contaCorrente._data_hora()))or
        pass

conta_Kalledy = contaCorrente("Kalledy", "111.222.333-45")
conta_Kalledy.consultar_saldo()

conta_Kalledy.depositar_dinheiro(10000)
conta_Kalledy.consultar_saldo()

conta_Kalledy.sacar_dinheiro(1000)
conta_Kalledy.consultar_saldo()




print("O saldo da conta é: ",conta_Kalledy.saldo)
print(conta_Kalledy.cpf)

