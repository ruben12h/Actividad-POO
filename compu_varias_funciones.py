class Computadora:
    def __init__(self, marca, procesador, ram):
        self.marca = marca
        self.procesador = procesador
        self.ram = ram
        self.encendida = False

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Procesador: {self.procesador}, RAM: {self.ram} GB")

    def encender(self):
        if not self.encendida:
            self.encendida = True
            print("La computadora se ha encendido.")
        else:
            print("La computadora ya estaba encendida.")

    def apagar(self):
        if self.encendida:
            self.encendida = False
            print("La computadora se ha apagado.")
        else:
            print("La computadora ya estaba apagada.")

    def actualizar_ram(self, nueva_ram):
        if nueva_ram > self.ram:
            print(f"RAM actualizada de {self.ram} GB a {nueva_ram} GB.")
            self.ram = nueva_ram
        else:
            print("La nueva RAM debe ser mayor que la actual.")

# Ejemplo de uso
compu2 = Computadora("HP", "Ryzen 5", 8)
compu2.encender()
compu2.actualizar_ram(16)
compu2.apagar()