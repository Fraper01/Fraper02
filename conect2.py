
'''
import clase_ciudades

city = clase_ciudades.Ciudades()
print(city)
'''

from  clase_ciudades import Ciudades
city = Ciudades()
city.elimina_ciudades(15)
#city.inserta_ciudadesAt("HHH","Name Pais","Name Capital","MON")
city.modifica_ciudades(aid=16,aISO3='IND',aCountryName='India',aCapital='New Dely',aCurrencyCode='INR')
print(city)

