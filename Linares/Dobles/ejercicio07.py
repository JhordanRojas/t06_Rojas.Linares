import os
nombre, refrijeradora, televisor, lavadora=",", 0, 0, 0

#imput
nombre=os.sys.argv[1]
refrijeradora=int(os.sys.argv[2])
televisor=int(os.sys.argv[3])
lavadora=int(os.sys.argv[4])

#procesing
total=(refrijeradora+televisor+lavadora)

#verificador
comprador_potencial=(total>=2000)

#condicion simple
#si el el total supera 2000 regalar una olla arrocera
if ( comprador_potencial== True ):
    print("se ha ganado una olla arrocera")
else:
    print("compre mas y gane premios")

#fin_if

#output
print("##############################")
print("#        Tiendas EFE         #")
print("##############################")
print("# Variables:    cantidad:")
print("# Nombre:",          nombre)
print("# Refrijeradora:",  refrijeradora)
print("# Televisor:",      televisor)
print("# Lavadora:",       lavadora)
print("------------------------------")
print("# Total:",           total)
print("##############################")
