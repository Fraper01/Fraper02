import re
from os import system

system('cls')
texto = "Las reuniones están pautadas para el 05/09/2023 y el 21/11/2024, también el 32/01/2025 y 00/13/9999."
print("\nTexto original:")
print(texto)
"""
Explicación de la expresión regular:
    \b: Este es un límite de palabra. Asegura que la fecha no esté dentro de otra palabra o número.
    (0[1-9]|[1-2][0-9]|3[0-1]): Esta parte coincide con el día (DD):
        0[1-9]: Coincide con números del 01 al 09.
        |[1-2][0-9]: | es un "OR". Esto coincide con números del 10 al 29.
        |3[0-1]: Otra "OR". Esto coincide con los números 30 y 31.
        Los paréntesis () crean un grupo de captura para el día.
    /: Coincide con el carácter de la barra diagonal que separa el día, el mes y el año.
    (0[1-9]|1[0-2]): Esta parte coincide con el mes (MM):
        0[1-9]: Coincide con números del 01 al 09.
        |1[0-2]: "OR". Esto coincide con los números 10, 11 y 12.
        Los paréntesis () crean un grupo de captura para el mes.
    /: Coincide con la segunda barra diagonal.
    (d{4}): Esta parte coincide con el año (AAAA):
        d: Coincide con cualquier dígito (0-9).
        {4}: Especifica que deben haber exactamente cuatro dígitos.
        Los paréntesis () crean un grupo de captura para el año.
    \b: Otro límite de palabra al final de la fecha.

Cómo usarlo en Python:

    Importa el módulo re para trabajar con expresiones regulares.
"""

patron_fecha = r'\b(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/(\d{4})\b'

# para encontrar todas las coincidencias que cumplan con el patrón en el texto
fechas_encontradas = re.findall(patron_fecha, texto)

# Si solo quieres la cadena completa de la fecha:
fechas_formateadas = [f"{dia}/{mes}/{anio}" for dia, mes, anio in fechas_encontradas]

print("\nFechas encontradas en el Texto:")
print(fechas_formateadas)

