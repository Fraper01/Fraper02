
class Empleado:
    def __init__(self, nombre, cargo, salario) -> None:
        self._nombre = nombre
        self._cargo = cargo
        self._salario = salario
    def info(self):
        return self._nombre, self._cargo, self._salario
    def Nombre(self):
        return self._nombre
    