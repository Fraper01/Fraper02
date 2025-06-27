# expresiones regulares

import re
ls_string="Esta es la leccion numero siete:, con Leccion Numero siete(7)"
ls_string2="Esta no es la leccion siete"
mathc=re.match("Esta es la leccion",ls_string,re.I)
print(mathc)
span=mathc.span()
iini, iend = span
print(span)
print(iini,iend)
print(ls_string[iini:iend])

mathc=re.match("Esta no es",ls_string2,re.I)
if mathc != None:
#if not(mathc==None):
    span=mathc.span()
    iini, iend = span
    print(iini,iend)
    print(ls_string2[iini:iend])


mathc = re.search("numero siete",ls_string,re.I)
if mathc != None:
#if not(mathc==None):
    span=mathc.span()
    iini, iend = span
    print(iini,iend)
    print(ls_string[iini:iend])

mathc = re.findall("numero siete",ls_string,re.I)
if mathc != None:
#if not(mathc==None):
    span=mathc
    print(span)

mathc = re.split(":",ls_string,re.I)
if mathc != None:
#if not(mathc==None):
    span=mathc
    print(span)

print(re.sub("Leccion|leccion","LECCION",ls_string))

# Patrones propios

lpatron = r"[L|l]eccion" # forma de elaborar expresiones regulares con la letra r(reservada en python)
print(re.sub(lpatron,"LECCIóN",ls_string))

lpatron = r"[L|l]eccion|siete" 
mathc = re.findall(lpatron,ls_string,re.I)
if mathc != None:
#if not(mathc==None):
    span=mathc
    print(span)

lpatron = r"[0-9]" 
mathc = re.findall(lpatron,ls_string,re.I)
if mathc != None:
#if not(mathc==None):
    span=mathc
    print(span)

# emal regulacion
email = "fraper02@gmail.com"
lpatron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9_.]+$" 
mathc=re.match(lpatron,email,re.I)
if mathc != None:
#if not(mathc==None):
    span=mathc.span()
    iini, iend = span
    print(iini,iend)
    print(email[iini:iend])

mathc = re.search(lpatron,email,re.I)
if mathc != None:
#if not(mathc==None):
    span=mathc.span()
    iini, iend = span
    print(iini,iend)
    print(email[iini:iend])

lpatron = r"^[a-zA-Z0-9_+-.]+@[a-zA-Z0-9_]+\.[a-zA-Z_.]+$" 
email = "fraper02.@gmail.com.es"
mathc = re.findall(lpatron,email,re.I)
if mathc != None:
#if not(mathc==None):
    span=mathc
    print(span)

# Para aprednder y validar expresiones regulares
# https://regex101.com






