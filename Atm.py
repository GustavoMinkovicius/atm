class Atm:
    def __init__(self, saldo, senha):
        self.saldo = saldo 
        self.senha = senha 
    def inicial(self):
            i = 0
            print("passe seu cartão")
            pin=int(input("Digite sua senha de 4 dígitos: "))
            if pin == self.senha:
                self.loop()
            else: 
                print(" Senha incorreta ")
 
    def loop(self):
            print("""....BEM-VINDO..... 1.Consultar saldo 2.Sacar 3.Depositar 4.Sair """)
            option=int(input("Digite sua opção: "))
            if option==1: 
                print("Seu saldo é R${}".format(self.consultar_saldo()))
                self.loop()
            if option==2:
                print("Seu saldo atualizado é R$ {}".format(self.sacar() ))
                self.loop()
            if option==3: 
                print("Seu saldo atualizado é R$ {}".format(self.depositar())) 
                self.loop()
            if option==4: 
                self.quit()
    def consultar_saldo(self):
        return self.saldo
    def sacar(self):
        valor=float(input("Informe o valor que deseja sacar:"))
        if (valor>self.saldo):
            print("Saldo inválido")
        else: 
            self.saldo=(self.saldo-valor) 
            print("""............A transação está sendo processada...........""")
            print(""".............Retire seu dinheiro..........""")
            return self.saldo 
    def depositar(self):
        valor=float(input("Informe o valor que deseja depositar:"))
        if (valor<0):
            print("Valor inválido")
        else: 
            self.saldo=self.saldo+valor 
            return self.saldo 
    def quit(self): 
        print("Obrigado por sua transação!") 
        quit() 
atm1 = Atm(100, 1234)
atm1.inicial()