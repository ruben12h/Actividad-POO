class compu:
    def __init__(self, marca, procesador, memoria, sistema_operativo):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.sistema_operativo = sistema_operativo
        self.encendida= False
        

    def info(self):
        print(
            f"computador marca {self.marca} y su procesador es {self.procesador} y su capacidad de memoria es {self.memoria} y con sistema operativo{self.sistema_operativo}"
        )


    def encender(self):

        if not self.encendida:
            self.encendida = True
            print(f"La computadora {self.marca} {self.procesador} esta encendida.")
        else:
            print("La computadora esto ya esta encendido.")

    def apagar(self):

        if self.encendida:
            self.encendida = False

            print(
                f"La computadora con la marca {self.marca} {self.procesador} está apagada."
            )
        else:
            print("este computador  ya está apagada.")

    def actualizar_memoria(self, nueva_memoria):
        if  self.encendida:
            print(
                f"Actualizando memoria de {self.memoria}GB a {nueva_memoria}GB.")
            self.memoria = nueva_memoria
                
            return
        if   nueva_memoria < self.memoria:
             print(
             "Por favor, encienda la computadora antes de actualizar la memoria para evitar daños  o bugs en la memoria xd."
            )
        else:
            print("La nueva memoria debe ser mayor que la actual.")


compu = compu("lenovo", "intel core 3", "32", "linux")
compu.info()
compu.encender()
compu.actualizar_memoria(256)
compu.apagar()