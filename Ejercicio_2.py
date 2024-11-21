print(" ")
print("Ordoñez Martinez Valeria")
print(" ")
class Cuenta:
    #Crear el constructor con sel, titular y la cantidad
    def __init__(self, titular, cantidad=0.0):
        if titular is None:
            raise ValueError("El titular es obligatorio.")
        self.titular = titular
        self.set_cantidad(cantidad) 
        #Defirnir self y titular 
    def set_titular(self, titular):
        if titular is None:
            raise ValueError("El titular no puede ser None.")
        self.titular = titular
        #Definir self
    def get_titular(self):
        return self.titular
    #Crear condiciones para sel y la cantidad
    def set_cantidad(self, cantidad):
        if not isinstance(cantidad, (int, float)) or cantidad < 0:
            raise ValueError("La cantidad debe ser un número mayor o igual a cero.")
        self.cantidad = cantidad
        #Devolver los resultados utuliando el return
    def get_cantidad(self):
        return self.cantidad
    #Imprimimos
    def mostrar(self):
        print(f"Titular: {self.get_titular().get_nombre()}")
        print(f"Cantidad en la cuenta: {self.get_cantidad()}")
        #Crear condicion
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print("La cantidad a ingresar debe ser positiva.")
            #Crear condicion definiendo nuestras variables
    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad
        else:
            print("La cantidad a retirar debe ser positiva.")
class Persona:
    #Crar otro constructor
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    def get_nombre(self):
        return self.nombre
    def get_edad(self):
        return self.edad
    def get_dni(self):
        return self.dni
    def es_mayor_de_edad(self):
        return self.edad >= 18
    #Llamamos todas las variables con nuestros datos
persona = Persona("Valeria", 16, "98765432A")
cuenta = Cuenta(titular=persona, cantidad=1000)
cuenta.mostrar()
cuenta.ingresar(600)
cuenta.mostrar()
cuenta.retirar(400)
cuenta.mostrar()
cuenta.retirar(60)