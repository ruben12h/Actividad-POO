class Computadora:
    def __init__(self, marca, procesador, ram):
        self.marca = marca
        self.procesador = procesador
        self.ram = ram

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Procesador: {self.procesador}, RAM: {self.ram} GB")

# Ejemplo de uso
compu1 = Computadora("Lenovo", "Intel Core i5", 8)
compu1.mostrar_info()