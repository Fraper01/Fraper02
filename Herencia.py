class animal():
    def __init__(self,_nombre,_sonido):
        self.nombre = _nombre
        self.sonido = _sonido
    def hacesonido(self):
        return f"{self.nombre} dice {self.sonido}"
    
class perro(animal):
    def __init__(self, _nombre ):
        super().__init__(_nombre, "Guao")


class gato(animal):
    def __init__(self, _nombre):
        super().__init__(_nombre, "Miau")

if __name__ == "__main__":
    miperro = perro("Bobby")
    migato = gato("Michi")
    print(miperro.hacesonido())
    print(migato.hacesonido())

    