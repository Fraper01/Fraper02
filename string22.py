# string

svar ="Este es un String"
print(svar, "Len:"+ str(len(svar)))

svar ="Este es un String\ncon salto de Linea"
print(svar, "Len:"+ str(len(svar)))

svar ="Este es un String\tcon Tabulacion de Linea"
print(svar, "Len:"+ str(len(svar)))

svar ="Este es un String\n\tcon Salto de Liena y Tabulacion"
print(svar, "Len:"+ str(len(svar)))

svar ="\\tEste es un String\\ncon doble n y doble t\nSe puede Utilizar para imprimir '\'"
print(svar, "Len:"+ str(len(svar)))

# formateo
snombre, sapellido, iedad = "Francisco","Perez",62
print("My Nombre es  {} Apellido  {} Edad: {}" .format(snombre,sapellido,iedad))
print("My Nombre es  %s Apellido  %s Edad: %d" %(snombre,sapellido,iedad))
print(f"My Nombre es  {snombre} Apellido  {sapellido} Edad: {iedad}" )

# Desenpaquetado de Caracteres
svar = "python"
sa, sb, sc, sd, se, sf  = svar
print(sa)
print(sb)

# Division
svarDiv = svar[0:4]
print(svarDiv)
svarDiv = svar[3:]
print(svarDiv)
svarDiv = svar[-6]
print(svarDiv)
svarDiv = svar[0:-3]
print(svarDiv)
svarDiv = svar[0:6:3]
print(svarDiv)

# Reverse
svarRev = svar[::-1]
print(svarRev)

# Funciones sobre string
print(svar.capitalize())
print(svar.upper())
print(svar.count("t"))
print(svar.isnumeric())
print(str(iedad).isnumeric())
print(svar.lower())
print(svar.upper().islower())
print(svar.upper().isupper())
print(svar.replace("p","F"))




