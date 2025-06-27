# Definicion de una clase

class Fraccion:
    ''' No son necesarias declarearlas el self las crea
    num = 0
    den = 0
    '''
    def __init__(self, n, d): # Asigna valores de Inicio a las Varibles de Clase y ejecuta el constructor 
        if isinstance(n,int):
            self.num = n
        else:
            self.num = 0
        if isinstance(d,int) and d != 0:
            self.den = d
        else:
            self.den = 1
        self.simplifica()

    #def  __del__(self): # destructor del objecto
    #    print("Destruyecndo objecto","(",self.num,"/",self.den,")")

    def __str__(self):
        return "( " + str(self.num) + " / " +str(self.den) + " )"

    def __mul__(self,b): # esta funcion se ejecuta cuando existe un (*) para multipicar
        n = self.num * b.num
        d = self.den * b.den
        r = Fraccion(n,d)
        r.simplifica()
        return r

    def __add__(self,b): # esta funcion se ejecuta cuando existe un (+) para sumar
        n = (self.num * b.den) + (self.den * b.num)
        d = self.den * b.den
        r = Fraccion(n,d)
        r.simplifica()
        return r

    def __sub__(self,b): # esta funcion se ejecuta cuando existe un (-) para restar
        n = (self.num * b.den) - (self.den * b.num)
        d = self.den * b.den
        r = Fraccion(n,d)
        r.simplifica()
        return r

    def __truediv__(self,b): # esta funcion se ejecuta cuando existe un (/) para division
        n = self.num * b.den
        d = self.den * b.num
        r = Fraccion(n,d)
        r.simplifica()
        return r

    def __eq__(self,b): # esta funcion se ejecuta cuando existe un (==) para Igual
        return (self.ret_resul() == b.ret_resul())

    def __lt__(self,b): # esta funcion se ejecuta cuando existe un (<) para menor
        return (self.ret_resul() < b.ret_resul())

    def __gt__(self,b): # esta funcion se ejecuta cuando existe un (>) para mayor
        return (self.ret_resul() > b.ret_resul())

    def imprime(self):
        print("(",self.num,"/",self.den,")")

    def ret_str(self):
        return "( " + str(self.num) + " / " +str(self.den) + " )"
    
    def ret_resul(self):
        return self.num / self.den

    def multiplicar(self,b):
        n = self.num * b.num
        d = self.den * b.den
        r = Fraccion(n,d)
        return r
    
    def simplifica(self):
        def mcd(a,b): # como esta dentro de otra funcion no utiliza self
            if b == 0:
                return a
            else:
                return mcd(b,a%b)

        #mc = self.mcd(self.num,self.den) no se necesita si esta dentro el self
        mc = mcd(self.num,self.den)
        if isinstance(mc,int):
            self.num = int(self.num / mc)
            self.den = int(self.den / mc)

    #def mcd(self,a,b): Se quita como clase y se coloca dentro de la funcion simplifuca
    #    if b == 0:
    #        return a
    #    else:
    #        return self.mcd(b,a%b)

class Lampara():
    _Estado = ["Encendida","Apagada"]
    def __init__(self,esta_encendida=False) -> None: # Asigna un valor por defecto
        if isinstance(esta_encendida,bool):
            self.esta_encedida = esta_encendida
        else:
            self.esta_encedida = False
    
    def muestra_lampara(self):
        if self.esta_encedida == True:
            print(self._Estado[0])
        else:
            print(self._Estado[1])
    def encender(self):
        self.esta_encedida = True
        self.muestra_lampara()
    def apagar(self):
        self.esta_encedida = False
        self.muestra_lampara()

    def __mul__(self,b:0): # esta funcion se ejecuta cuando existe un (*) para multipicar
        if b==1:
            self.encender()
        elif b==0:
            self.apagar()
        else:
            self.apagar()

class Vehiculo():
    def __init__(self,color="",ruedas=4) -> None: # Asigna un valor por defecto
        if isinstance(color,str):
            self.color = color
        else:
            self.color = ""
        if isinstance(ruedas,int):
            self.ruedas = ruedas
        else:
            self.ruedas = 4
    def __str__(self) -> str:
        return "Color {}, {} Ruedas".format(self.color,self.ruedas)

class Coche(Vehiculo):
    def __init__(self,color="",ruedas=4, velocidad=0, cilindradas=0) -> None: # Asigna un valor por defecto
        #Vehiculo.__init__(self,color,ruedas)
        super().__init__(color,ruedas) # tambien se puede usar super(), esto es igual que llamar a la Clase Padre, pero no necesita self
        if isinstance(velocidad,int):
            self.velocidad = velocidad
        else:
            self.velocidad = 0
        if isinstance(cilindradas,int):
            self.cilindradas = cilindradas
        else:
            self.cilindradas = 0

    def __str__(self) -> str:
        cad = " {} Km/h, {} cc."
        #return Vehiculo.__str__(self) + cad.format(self.velocidad, self.cilindradas)
        return super().__str__() + cad.format(self.velocidad, self.cilindradas)


def mult_fraccion(f1,f2):
    mnum = f1.num * f2.num
    mden = f1.den * f2.den
    r = Fraccion(mnum,mden)
    return r

def sum_fraccion(f1,f2):
    mcdc = f1.den * f2.den
    num1 = (mcdc / f1.den) * f1.num
    num2 = (mcdc / f2.den) * f2.num
    mnum = num1 + num2
    mden = mcdc
    r = Fraccion(mnum,mden)
    return r

def res_fraccion(f1,f2):
    mcdc = f1.den * f2.den
    num1 = (mcdc / f1.den) * f1.num
    num2 = (mcdc / f2.den) * f2.num
    mnum = num1 - num2
    mden = mcdc
    r = Fraccion(mnum,mden)
    return r

def div_fraccion(f1,f2):
    mnum = f1.num * f2.den
    mden = f1.den * f2.num
    r = Fraccion(mnum,mden)
    return r

def main():
    a = Fraccion(3,2) # Crea el objecto (a) y ahora lo podemos utilizar con sus funciones
    #a.imprime()
    b = Fraccion(7,4) # Crea el objecto (a) y ahora lo podemos utilizar con sus funciones
    #b.imprime()
    #r = a.multiplicar(b)
    #r.imprime()
    #r = b.multiplicar(a)
    #r.imprime()
    r = sum_fraccion(a,b)
    mens = "Sumar " + a.ret_str() + " con " + b.ret_str() + " es igual " + r.ret_str() + " -> " + str(r.ret_resul())
    print(mens)
    #r.imprime()
    r = res_fraccion(a,b)
    mens = "Restar " + a.ret_str() + " con " + b.ret_str() + " es igual " + r.ret_str() + " -> " + str(r.ret_resul())
    print(mens)
    #r.imprime()
    r = mult_fraccion(a,b)
    mens = "Multiplicar " + a.ret_str() + " con " + b.ret_str() + " es igual " + r.ret_str() + " -> " + str(r.ret_resul())
    print(mens)
    r = div_fraccion(a,b)
    mens = "Dividir " + a.ret_str() + " con " + b.ret_str() + " es igual " + r.ret_str() + " -> " + str(r.ret_resul())
    print(mens)
    #r.imprime()


def lamp():
    l = Lampara(False)
    l2 = Lampara()
    nm1 = 5
    nm2 = 1
    if nm1 >= nm2:
        l.encender()
    else:
        l.apagar()

    menu = '''
        Menu: 
        0 > Apagar Lampara
        1 > Encender Lampara
        x > Salir
        '''
    while True:
        print(menu)
        op = input("Aue opcion desea:")
        if op == "0":
            l2.apagar()
        elif op == "1":
            l2.encender()
        elif op == "x":
            break

def main2():
    a = Fraccion(11,4) # Crea el objecto (a) y ahora lo podemos utilizar con sus funciones
    #a.imprime()
    print(a)
    b = Fraccion(7,2) # Crea el objecto (a) y ahora lo podemos utilizar con sus funciones
    #b.imprime()
    print(b)
    r = a * b
    print("Multipiicacion",r)
    r = a + b
    print("Addicion",r)
    r = a - b
    print("Resta",r)
    r = a / b
    print("Division",r)
    if a==b:
        print(a," es igual/equivalente a ",b)
    elif a<b:
        print(a," es menor a ",b)
    elif a>b:
        print(a," es mayor a ",b)
    else:
        print(a," es completamente diferente a ",b)

    l=Lampara()
    (l*1)
    (l*0)
    

def main3():
    #v = Vehiculo("Azul",5)
    #print(v)
    c = Coche("azul",2,120,1500)
    print(c)

if __name__ == "__main__":
    #main()
    #lamp()
    main2()
    #main3()
    print("Fin")



