inventario = 100
contador = 0 

while inventario > 0:
    if inventario <= 10:
        print('Alerta: quedan pocos zapatos')
        
    pedido = (int(input('Cuantos zapatos quiere? ')))
    
    if pedido > inventario:
        print(f'Lo sentimos no hay tantos zapatos en el inventario, solo hay {inventario}')
    else:
        inventario -= pedido
        print(f'El cliente ha pedido {pedido} zapatos, el inventario ahora tiene {inventario} zapatos')  
        contador += 1
         
print(f'Ha realizado {contador} transacciones ')