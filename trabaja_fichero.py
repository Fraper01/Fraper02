# tabaja con fichero

# .txt file
#txt_file = open("C:/Users/image/OneDrive/Documentos/PytonCurso/fichero.txt","r+") # los descriptore de aarchibos van con / y no \ como windows
#print(txt_file.read())
print("10")
#print(txt_file.read(20)) # continua la lectura despues del la ultima
#print(txt_file.readline())
#print(txt_file.readline())
#print(txt_file.readline())
#print(txt_file.readline())
#print(txt_file.readlines())
print("20")
#for line in txt_file.readlines():
#    print(line)
print("30")
#txt_file.write("Adiciona algo") # escribe al final del archivo
#txt_file.write("\ncon Saldo de linea") # escribe al final del archivo
#for line in txt_file.readlines():
#    print(line)

txt_file = open("C:/Users/image/OneDrive/Documentos/PytonCurso/fichero.txt","w+") # los descriptore de aarchibos van con / y no \ como windows
txt_file.write("Mi nombre es Francisco\nMi apellido es Perez\nMi edad es 62\nMi lenguaje preferido es python")
txt_file.close()

import os

#os.remove("C:/Users/image/OneDrive/Documentos/PytonCurso/fichero.txt")

# ficheris .json

import json
json_file = open("C:/Users/image/OneDrive/Documentos/PytonCurso/fichero_json.json","w+") # siempre crea el fichero desde cero
json_text = {
    "name":"Francisco",
    "apellido":"Perez",
    "edad":62,
    "lenguaje":["Python","Shift","php"],
    "website":"https/alamierda"
    }
json.dump(json_text,json_file,indent=2) # indent espacios en blanco
#json.dump(json_text,json_file,indent=2) # indent espacios en blanco

json_file.close()


with open("C:/Users/image/OneDrive/Documentos/PytonCurso/fichero_json.json") as otro_archivo:
    for line in otro_archivo.readlines():
        print(line)


json_dic = json.load(open("C:/Users/image/OneDrive/Documentos/PytonCurso/fichero_json.json"))
print(json_dic)


                 










