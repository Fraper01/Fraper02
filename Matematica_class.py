from os import system

class calculadora:
    def suma(self,a,b):
        return a+b
    
    def resta(self,a,b):
        return a-b

    def multiplicacion(self,a,b):
        return a*b

    def division(self,a,b)->float|str:
        if b!= 0:
            return a/b
        else:
            return "No se puede Realizar (Dividendo=0)"

class Uso_Calculadora:
    def __init__(self):
        self.calc = calculadora()

    def ejecutar(self):
        self.opraciones = ["Suma","Resta","Multiplicacón","División"]
        while True:
            system('cls')
            print("Bienvenidos a la Calculadora")
            print("Operaciones disponibles")
            print("1. Suma")
            print("2. Resta")
            print("3. Multiplicacon")
            print("4. Division")
            print("5. Salir")
            self.opcion = int(input("\nSeleccione su opcion (1-5)"))
            if (self.opcion >=1 and self.opcion <=4):
                self.num1 = float(input("Ingrese el primer numero:"))
                self.num2 = float(input("Ingrese el segundo numero:"))
            
            if self.opcion == 5:
                break

            if self.opcion == 1:
                self.resultado = self.calc.suma(self.num1,self.num2)
            if self.opcion == 2:
                self.resultado = self.calc.resta(self.num1,self.num2)
            if self.opcion == 3:
                self.resultado = self.calc.multiplicacion(self.num1,self.num2)
            if self.opcion == 4:
                self.resultado = self.calc.division(self.num1,self.num2)
            if self.opcion == 5:
                break
            if self.opcion <= 4:
                self.esperar()
            else:
                print("Indique una opcion valida")
                input("Presione enter para Continuar")
  
    def esperar(self):
        if isinstance(self.resultado, str):
            print(f"El resultado de la {self.opraciones[self.opcion-1]} entre los números {self.num1} y {self.num2} {self.resultado}")
        else:
            print(f"El resultado de la {self.opraciones[self.opcion-1]} entre los números {self.num1} y {self.num2} es igual a {self.resultado}")
        input("Presione enter para Continuar")

if __name__ == "__main__":
    calculadora = Uso_Calculadora()
    calculadora.ejecutar()

            
                
