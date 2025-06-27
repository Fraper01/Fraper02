

import mysql.connector

def main():
    print("Inicio")
    cnn = mysql.connector.connect(host="localhost",user="root",passwd="sqlyo",database="word")
    if cnn.is_connected():
        print("Conectado")
        cur = cnn.cursor()
        cur.execute("SELECT * FROM city;")
        datos = cur.fetchall()
        for fila in datos:
            print(fila)
    cnn.disconnect()
    print("Fin")

def consulta_ciudades(acnn):
    print("Funcion Consulta")
    cur = acnn.cursor()
    cur.execute("SELECT * FROM countries;")
    datos = cur.fetchall()
    cur.close()
    return datos

def inserta_ciudades(acnn):
    print("Funcion Inserta")
    cur = acnn.cursor()
    lsql = "INSERT INTO countries(ISO3,CountryName,Capital,CurrencyCode) VALUES('CHL','Chile','Santiago','CLP');"
    cur.execute(lsql)
    n=cur.rowcount
    acnn.commit()
    cur.close()
    return n

def inserta_ciudadesAt(acnn,aISO3,aCountryName,aCapital,aCurrencyCode):
    print("Funcion Inserta")
    cur = acnn.cursor()
    lsql = "INSERT INTO countries(ISO3,CountryName,Capital,CurrencyCode) VALUES('{}','{}','{}','{}');".format(aISO3,aCountryName,aCapital,aCurrencyCode)
    cur.execute(lsql)
    n=cur.rowcount
    acnn.commit()
    cur.close()
    return n

def elimina_ciudades(acnn,aid):
    print("Funcion Elimina")
    cur = acnn.cursor()
    lsql = "DELETE FROM countries WHERE ID={};".format(aid)
    cur.execute(lsql)
    n=cur.rowcount
    acnn.commit()
    cur.close()
    return n

def modifica_ciudades(acnn,aid,aISO3='',aCountryName='',aCapital='',aCurrencyCode=''):
    print("Funcion Modifica")
    if aISO3=='' and aCountryName=='' and aCapital=='' and aCurrencyCode=='':
        return 0
    
    lsqlUp = "UPDATE countries "
    lsqlSe = "SET "
    lsqlWh = " WHERE ID={};".format(aid)

    if aISO3!='':
        lsqlSe = lsqlSe + "ISO3 = '{}'".format(aISO3)
    if aCountryName!='':
        if len(lsqlSe)>=5:
            lsqlSe = lsqlSe + ","
        lsqlSe = lsqlSe + "CountryName = '{}'".format(aCountryName) 
    if aCapital!='':
        if len(lsqlSe)>=5:
            lsqlSe = lsqlSe + ","
        lsqlSe = lsqlSe + "Capital = '{}'".format(aCapital) 
    if aCurrencyCode!='':
        if len(lsqlSe)>=5:
            lsqlSe = lsqlSe + ","
        lsqlSe = lsqlSe + "CurrencyCode = '{}'".format(aCurrencyCode) 
    lsql = lsqlUp + lsqlSe + lsqlWh 
    cur = acnn.cursor()
    try:
        cur.execute(lsql)
    except:
        cur.close()
        print("Error en la Sentencia Sql: "+lsql)
        n= 0
    else:
        n=cur.rowcount
        acnn.commit()
        cur.close()
    finally:
        return n

def main2():
    print("Inicio")
    cnn = mysql.connector.connect(host="localhost",user="root",passwd="sqlyo",database="bdejemplopy")
    if cnn.is_connected():
        print("Conectado")
        datos = consulta_ciudades(cnn)
        for fila in datos:
            print(fila)
    cnn.disconnect()
    cnn.close()
    print("Fin")

def main3():
    print("Inicio")
    cnn = mysql.connector.connect(host="localhost",user="root",passwd="sqlyo",database="bdejemplopy")
    if cnn.is_connected():
        print("Conectado")
        n = inserta_ciudades(cnn)
        print(n)
    cnn.disconnect()
    cnn.close()
    print("Fin")

def main4():
    print("Inicio")
    cnn = mysql.connector.connect(host="localhost",user="root",passwd="sqlyo",database="bdejemplopy")
    if cnn.is_connected():
        print("Conectado")
        n = inserta_ciudadesAt(cnn,"MEX","Mexico","CDMX","MXN")
        print(n)
    cnn.disconnect()
    cnn.close()
    print("Fin")

def main5():
    print("Inicio")
    cnn = mysql.connector.connect(host="localhost",user="root",passwd="sqlyo",database="bdejemplopy")
    if cnn.is_connected():
        print("Conectado")
        n = elimina_ciudades(cnn,3)
        if n == 0:
            print("No se puede Eliminar el ID:"+str(3))
        print(n)
    cnn.disconnect()
    cnn.close()
    print("Fin")

def main6():
    print("Inicio")
    cnn = mysql.connector.connect(host="localhost",user="root",passwd="sqlyo",database="bdejemplopy")
    if cnn.is_connected():
        print("Conectado")
        lId=10
        n = modifica_ciudades(cnn,lId,aCurrencyCode="CLL",aISO3="CHI",aCapital="Santiago",aCountryName="Chile")
        if n == 0:
            print("No se puede Modificar el ID:"+str(lId))
        else:
            print("Se Modifico el ID:"+str(lId))
    cnn.disconnect()
    cnn.close()
    print("Fin")

if __name__ == "__main__":
    #main()
    #main2()
    #main3()
    #main4()
    #main5()
    main6()

