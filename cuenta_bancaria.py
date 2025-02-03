'''CUENTA BANCARIA
Crea una clase "CuentaBancaria" con atributos como número de cuenta y
saldo. Implementa métodos para depositar y retirar dinero, y muestra el
saldo actual.'''

class CuentaBancaria:
    def __init__(self, num_cuenta, saldo=0):
        self.num_cuenta = num_cuenta
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depositado {monto} euros. El nuevo saldo es {self.saldo} euros.")

    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"Retirado {monto} euros. El nuevo saldo es {self.saldo} euros.")
        else:
            print("Saldo insuficiente para realizar la operación.")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo} euros.")

# Prueba de ejemplo
cuenta = CuentaBancaria("1234567890", 100)
cuenta.depositar(50)  # Saldo esperado: 150
cuenta.retirar(30)  # Saldo esperado: 120
cuenta.mostrar_saldo()  # Saldo esperado: 120