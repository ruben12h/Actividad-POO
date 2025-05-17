class libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.prestado = False
        

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return f"el libro {self.titulo} ha sido prestado"
        else:
            return f"el libro {self.titulo} ya esta prestado"

    def devolver(self):
        if self.prestado:
            self.prestado = False
            return f"el libro {self.titulo} ha sido devuelto"
        else:
            return f"el libro {self.titulo} no estaba prestado"


class Biblioteca:
    def __init__(self, nombre):
        self.nombres = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"se agrego {libro.titulo} a la biblioteca ")

    def mostrar_libros(self):
        for libro in self.libros:
            estado = "prestado" if libro.prestado else "disponible"
            print(f" libro {libro.titulo} , {libro.autor} , {libro.año} , {estado} ")


libro1 = libro("cien años de soledad", "gabriel garcia", "1999")

biblioteca = Biblioteca("biblioteca general")
biblioteca.agregar_libro(libro1)
biblioteca.mostrar_libros()
print(libro1.prestar())
biblioteca.mostrar_libros()
print(libro1.devolver())
biblioteca.mostrar_libros()

