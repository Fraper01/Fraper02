class persona():
    def __init__(self,_nombre,_actividad):
        self.nombre = _nombre
        self.actividad = _actividad
    def hacesactividad(self):
        return f"{self.nombre} esta realizando una actividad como {self.actividad}"
class cliente(persona):
    def __init__(self, _nombre ):
        super().__init__(_nombre, "Cliente")
class vendedor(persona):
    def __init__(self, _nombre):
        super().__init__(_nombre, "Vendedor")
if __name__ == "__main__":
    micliente = cliente("Francisco")
    mivendedor = vendedor("Javier")
    print(micliente.hacesactividad())
    print(mivendedor.hacesactividad())

