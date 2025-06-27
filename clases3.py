# Fracciones Mixtas

from clases2 import Fraccion

class FraccionMixta(Fraccion):
    def __init__(self, ent, num=0, den=1):
        self.ent = ent
        super().__init__(num, den)
        self.simplifica()
        super().simplifica()
    def __str__(self):
        if self.ent != 0:
            r = str(self.ent) + super().__str__()
        else:
            r = super().__str__()
        return r
    def simplifica(self):
        if self.num > self.den:
            aux = self.num//self.den
            self.ent = self.ent + aux
            self.num -= (aux*self.den)
    def __add__(self, obj):
        ent = self.ent + obj.ent
        f = super().__add__(obj)
        r = FraccionMixta(ent,f.num,f.den)
        return r
    def toFraccion(self):
        n,d = self.num, self.den
        if self.ent != 0:
            n = (self.ent * d) + n
            f = Fraccion(n,d)
        return f
    def __add__(self,obj):
        ''' Simplificando
        a = self.toFraccion()
        b = obj.toFraccion()
        r = a + b
        '''
        r = self.toFraccion() + obj.toFraccion()
        r = FraccionMixta(0,r.num,r.den)
        r.simplifica()
        return r
    def __sub__(self,obj):
        r = self.toFraccion() - obj.toFraccion()
        r = FraccionMixta(0,r.num,r.den)
        r.simplifica()
        return r
    def __mul__(self,obj):
        r = self.toFraccion() * obj.toFraccion()
        r = FraccionMixta(0,r.num,r.den)
        r.simplifica()
        return r
    def __truediv__(self,obj):
        r = self.toFraccion() / obj.toFraccion()
        r = FraccionMixta(0,r.num,r.den)
        r.simplifica()
        return r
    def __eq__(self,b): # esta funcion se ejecuta cuando existe un (==) para Igual
        return (self.toFraccion() == b.toFraccion())

def main():
    a = FraccionMixta(4,8,6)
    print(a)
    b = FraccionMixta(3,7,4)
    print(b)
    r = a + b
    print("Suma:",r)
    r = a - b
    print("Resta",r)

def main2():
    a = FraccionMixta(2,3,4)
    b = FraccionMixta(3,1,2)
    print(a)
    print(a.toFraccion())
    print(b)
    print(b.toFraccion())
    print("Suma:",a+b)
    print("Resta:",a-b)
    print("Multi:",a*b)
    print("Divis:",a/b)
    b = FraccionMixta(2,3,4)
    print("Igual:",a==b)



if __name__ == "__main__":
    #main()
    main2()
    print("Fin")
