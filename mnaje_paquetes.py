# manuejo de paquetes externos a Python

#Pypi
'''
Instalación de paquetes
no me funciona bien pero mas adelante lo verremos
'''
#import pandas
#pandas.array

import pyodbc
ls_connect = r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\image\OneDrive\Documentos\Access Lilu\Bd\Data\Plan de Intervención_be.accdb;' 
conn = pyodbc.connect(ls_connect)
cursor = conn.cursor()
cursor.execute("SELECT * FROM PACIENTES")
for row in cursor.fetchall():
    print(row)


cursor.close()
conn.close()
