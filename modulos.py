# Modulos y fechas

'''
Se Utilizan para utilizar otros ficheros o programas externos a nuesto proyecot
Al igual que puedo utilizar mis ficheros desde otros fichero propios

'''

#import moduless
from moduless import suma, lf_sum_conRet

'''
cuando utilizas import fichero
'''
#moduless.suma(1,2,2)
#print(moduless.lf_sum_conRet(1,2))

'''
cuando utilizas from import fichero se llama directo
'''
suma(1,3,1)
print(lf_sum_conRet(1,2))

import math

print(math.pi)
print(math.sqrt(25))
print(math.pow(2,3))

from math import pi as pi_value

print(pi_value)

import datetime
now = datetime.datetime
print(now)

from datetime import datetime as ldt_var

now = ldt_var.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

nowhora = now.timestamp() # un numero flotante que tine la fecha desde 1970
print(nowhora)

hoy = now.date()
print(f"{hoy.day}/{hoy.month}/{hoy.year}")
year_2025 = ldt_var(2025,1,1)
print(year_2025)
print("antes de la funcion")

def print_datetime(date):
    print(date)
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

def print_date(date):
    print(date)
    print(date.year)
    print(date.month)
    print(date.day)

def print_time(date):
    print(date.hour)
    print(date.minute)
    print(date.second)

print("funcion datetime")
now = ldt_var.now()
print_datetime(now)

from datetime import time as lt_hora
hora = lt_hora(15,4)
hora = now.time()
print("funcion time")
print_time(hora)

from datetime import date as ld_fecha
fecha = ld_fecha.today()
print("funcion date")
print_date(fecha)

dif = year_2025 - now  # para hacer directo deben ser del mismo tipo este ejemplo es DateTime
print(dif)
dif = year_2025.date() - fecha  # para hacer directo deben ser del mismo tipo este ejemplo es Date
print(dif)
#dif = hora - year_2025.time() # no resta horas por los momentos
#print(year_2025.time())
#print(hora)

from datetime import timedelta
ini_timedelta = timedelta(200,100,100, weeks=10)  # define un espacio de tiempo son valores absolutos no trabaja con fechas
end_timedelta = timedelta(300,100,100, weeks=13)
dif = end_timedelta - ini_timedelta
print(dif)
dif = end_timedelta + ini_timedelta
print(dif)


















