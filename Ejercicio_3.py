print(" ")
print("Ordoñez Martinez Valeria")
print(" ")
#Creamos el constructor usando funciones
class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
        #Definimos la cantidad y self
    def retirarDinero(self, cantidad):
        #Creamos condiciones
        if cantidad <= self.cantidad:    
            self.cantidad -= cantidad
            print(f"Has retirado {cantidad}$. Ahora cuentas con {self.cantidad}$ en la cuenta.")
        else:
            print("No tenemos suficiente saldo.")
    def mostrar(self):
        #Mostrar el saldo
        print(f"Titular: {self.titular}\nSaldo: {self.cantidad}€")
class CuentaJoven(Cuenta):
    #Definimos la cuenta joven con self, titular, cantidad y bonificacion
    def __init__(self, titular, cantidad, bonificacion):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
    def setBonificacion(self, bonificacion):
        self.bonificacion = bonificacion
    def getBonificacion(self):
        #Devolvemos datos
        return self.bonificacion
    def esTitularValido(self):
        edad = self.titular['edad']
        #Devolvemos datos  
        return 18 <= edad < 25
    def retirarDinero(self, cantidad):
        #Creamos condiciones
        if self.esTitularValido():
            super().retirarDinero(cantidad)
        else:
            print("No puedes retirar dinero")
    def mostrar(self):
        print(f"Cuenta Joven\nTitular: {self.titular['nombre']} {self.titular['apellido']}\nBonificación: {self.bonificacion}%")
        super().mostrar()
        #Poner al tirular con nuestros datos
titular = {'nombre': 'Valeria', 'apellido': 'Ordoñez', 'edad': 16}
cuenta_joven = CuentaJoven(titular, 600, 5)
cuenta_joven.mostrar()
cuenta_joven.retirarDinero(200)
cuenta_joven.setBonificacion(10)
print(f"Bonificación actual: {cuenta_joven.getBonificacion()}%")

