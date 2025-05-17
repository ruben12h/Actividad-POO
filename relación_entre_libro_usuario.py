class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libro_prestado = None

    def tomar_prestado(self, libro):
        if not libro.prestado:
            libro.prestado = True
            libro.usuario_actual = self
            self.libro_prestado = libro
            print(f"{self.nombre} ha tomado prestado el libro '{libro.titulo}'.")
        else:
            print(f"El libro '{libro.titulo}' ya está prestado por {libro.usuario_actual.nombre}.")

    def devolver_libro(self):
        if self.libro_prestado:
            print(f"{self.nombre} ha devuelto el libro '{self.libro_prestado.titulo}'.")
            self.libro_prestado.prestado = False
            self.libro_prestado.usuario_actual = None
            self.libro_prestado = None
        else:
            print(f"{self.nombre} no tiene ningún libro prestado.")

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False
        self.usuario_actual = None

# Ejemplo de uso
libro2 = Libro("1984", "George Orwell")
usuario1 = Usuario("Juan")
usuario2 = Usuario("Ruben")

usuario1.tomar_prestado(libro2)
usuario2.tomar_prestado(libro2)
usuario1.devolver_libro()
usuario2.tomar_prestado(libro2)