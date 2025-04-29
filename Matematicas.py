def Suma(a,b):
    return a+b

a = 5
b = 8 
c = Suma(a,b)
print(f"El resultado de la Suma {a} y {b} es igual a {c}" )

a = int(input("Ingrese el valor a:"))
b = int(input("Ingrese el valor b:"))
c = Suma(a,b)
print(f"El resultado de la Suma {a} y {b} es igual a {c}" )


def SumaS()->int:
    a = int(input("Ingrese el valor a1:"))
    b = int(input("Ingrese el valor b1:"))
    c = Suma(a,b)
    print(f"El resultado de la Suma {a} y {b} es igual a {c}" )
    return c

r = SumaS()
print(f"El Resultado es con int {r}")

def Sumaf()->float:
    a = float(input("Ingrese el valor a1:"))
    b = float(input("Ingrese el valor b1:"))
    c = Suma(a,b)
    print(f"El resultado de la Suma {a} y {b} es igual a {c}" )
    return c

r = Sumaf()
print(f"El Resultado es con float {r}")

