class ContaBancaria:
    saldo = 1
    limite = 1

    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        if valor < 0:
            print("0")
        else:
            print("1")
            self.saldo += valor
        return self.saldo
        
    
    def levantar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            print("1")
        else:
            print("0")
    
    def exibir_saldo(self):
        print(format(self.saldo, ".2f"))

    def exibir_info(self):
        print(self.titular, str(format(self.saldo, ".2f")), str(format(self.limite, ".2f")))

conta = ContaBancaria("João", 1000.00, 500.00)
conta.depositar(-500.00)
conta.depositar(500.00)
conta.levantar(1200.00)
conta.levantar(1200.00)
conta.exibir_info()