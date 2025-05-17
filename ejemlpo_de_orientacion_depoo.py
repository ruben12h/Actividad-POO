# clase y objecto
class perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre}dice ¡guau!")

# crear un objeto
mi_perro = perro("fido","labrador")
mi_perro.ladrar()  #fido dice ¡guau!

# 2. Herencia

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

class gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice ¡miau!")
    
gato = gato("mishi")
gato.hablar()   #Mishi dice ¡miau!

#3  Encasulamiento

class cuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo   #Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def ver_saldo(self):
        return self.__saldo
    
cuenta = cuentaBancaria(100)
cuenta.depositar(50)
print(cuenta.ver_saldo())     #150


#4 Polimorfismo

class Ave:
    def volar(self):
        print("esta ave vuela.")

class Pinguino(Ave):
    def volar(self):
        print("El pingüino no puede volar.")

aves = [Ave(), Pinguino()]
for ave in aves:
    ave.volar()