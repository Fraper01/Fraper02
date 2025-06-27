from  clase_ciudades import Ciudades

ciudad = Ciudades()
menu ='''
***********************************
* i) Inserta Ciudades             *
* e) Elimina Ciudades             *
* m) Modifica Ciudades            *
* p) Imprime Ciudades             *
* x) Salir                        *
***********************************
'''

def main():
    opc = "0"
    while opc != "X":
        print(menu)
        opc = input("Que Opcion desea Ejecutar:").upper()
        if opc == "I":
            lISO3 = input("Indique el ISO3 del Pais:")
            lCountryName = input("Indique el CountryName del Pais:")
            lCapital = input("Indique la Capital del Pais:")
            lCurrencyCode = input("Indique el CurrencyCode del Pais:")
            liret=ciudad.inserta_ciudadesAt(lISO3,lCountryName,lCapital,lCurrencyCode)
            if liret == 1:
                print("Se Inserto el Pais Correctamente")
            else:
                print("Fallo Insertar el Pais")
        elif opc == "E":
            liid = int(input("Indique el Id a Elminar:"))
            liret = ciudad.elimina_ciudades(liid)
            if liret == 1:
                print("Se Elimino la Ciudad con el ID="+str(liid))
            else:
                print("Fallo/No Existe Eliminar la Ciudad con el ID="+str(liid))
        elif opc == "M":
            liid = int(input("Indique el Id a Modificar:"))
            lpais = ciudad.buscar_ciudades(liid)
            if lpais == None:
                print("La Ciudad con el ID="+str(liid)+" No Existe")
            else:
                print(lpais)
                lISO3 = input("Indique el ISO3 del Pais:")
                lCountryName = input("Indique el CountryName del Pais:")
                lCapital = input("Indique la Capital del Pais:")
                lCurrencyCode = input("Indique el CurrencyCode del Pais:")
                liret=ciudad.modifica_ciudades(liid, lISO3,lCountryName,lCapital,lCurrencyCode)
                if liret == 1:
                    print("Se Modifico el Pais Correctamente con el ID="+str(liid))
                else:
                    print("Fallo Modificar el Pais con el ID="+str(liid))
        elif opc == "P":
            print(ciudad)
        elif opc == "X":
            print("Fin")
        else:
            print("Opcion Invalida")
    
if __name__ == "__main__":
    main()



