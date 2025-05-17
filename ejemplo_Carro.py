class Carro:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False
        self.gasolina = 50 #esto es para saber inicial de la gasolina

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"este Carro esta encendido.")
        else:
            print("el Carro ya esta encendido")

    def apagar(self):
        if  self.encendido:
            self.encendido = False
            print(f"este carro esta apagado.")
        else:
            print("el Carro ya esta apagado")

    def mostrar_gasolina(self):
        print(f"nivel de gasolina: {self.gasolina}%")

    def cargar_gasolina(self,cantidad):
        if cantidad <=0:
           print("no se puede aser una cantidad negativa o cero de gasolina")
        else:
            self.gasolina += cantidad
            if self.gasolina > 100 :
                self.gasolina = 100
            print(f"gasolina cargada. nivel de ahorro o actual: {self.gasolina}%")

    def info(self):
        estado = "encendido" if self.encendido else "apagado"
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, gasolina: {self.gasolina}%")

Carro = Carro("toyota", "corolla",  "rojo")
    
    
Carro.encender()
Carro.cargar_gasolina(30)
Carro.mostrar_gasolina()
Carro.info()
Carro.apagar()


    

    
