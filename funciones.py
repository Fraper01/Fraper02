# funciones

def my_function(): # Al igual que todo los demas es por tabulador
    print("mi funtion")

my_function()

#def lf_sum(var_num1: int,var_num2: int): # Este tipado no sirve Python es dinamico toma el argumento de la variable es inutil colocar int no le para
def lf_sum(var_num1: int,var_num2: int): # Este tipado no sirve Python es dinamico toma el argumento de la variable es inutil colocar int no le para
    print(var_num1+var_num2)

lf_sum(5,7)
lf_sum("5","7")
lf_sum(1.10,3.30)

def lf_sum_conRet(var_num1,var_num2): 
    return (var_num1+var_num2)


ll_resul = lf_sum_conRet(1.10,3.30)
print("Resultado de Sumar ",ll_resul)

def prin_name(aNombre: str, aApellido: str):
    print(f"{aNombre} {aApellido}")

prin_name("Francisco","Perez")
prin_name(5,6)
prin_name(aApellido="Perez",aNombre="Francisco") # esto si es interesante aunque verga medio completado uno deberia manejar la funcion como fue creada

def prin_name_conDefault(aNombre: str, aApellido: str, aAlias="S/Alias"):
    print(f"{aNombre} {aApellido} {aAlias}" )

prin_name_conDefault("Francisco","Perez","Papucho")
prin_name_conDefault("Francisco","Perez")

def print_text(*atext): # Numero de parametros dinamicos 
    print(atext)

print_text("Hola","otro","verga")

def print_text2(*atext): # Numero de parametros dinamicos 
    for text in atext:
        print(text.upper())

print_text2("Hola","otro","verga")












