import os
nombre, servicio_de_internet, serv_de_telefono, serv_de_cable=",", 0, 0, 0

#imput
nombre=os.sys.argv[1]
servicio_de_internet=int(os.sys.argv[2])
serv_de_telefono=int(os.sys.argv[3])
serv_de_cable=int(os.sys.argv[4])

#procesing
total=(servicio_de_internet+serv_de_telefono+serv_de_cable)

#verificador
cliente_potencial=(total>=130)

#condicion simple
#si el total supera los 130 soles mostrarle el servicio de internet 5G de velocidad
if ( cliente_potencial== True ):
    print("tiene posibilidad de adquirir el interne con velocidad 5G")
if ( cliente_potencial>=120 and cliente_potencial<129 ):
    print("gracias por usar nuestro servicio")
if ( cliente_potencial<119 ):
    print("gracias")
#fin_if

#output
print("###############################")
print("#      Servicios Movistar     #")
print("###############################")
print("# Variables:    cantidad:")
print("# Nombre:",    nombre)
print("# Servicio de internet:", servicio_de_internet)
print("# Servicio de telefono:", serv_de_telefono)
print("# Servicio de cable:",    serv_de_cable)
print("-------------------------------")
print("# Total:",                 total)
print("###############################")
