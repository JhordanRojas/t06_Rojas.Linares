import os
nombre, samsung, iphone, LG=",", 0, 0, 0

#imput
nombre=os.sys.argv[1]
samsung=int(os.sys.argv[2])
iphone=int(os.sys.argv[3])
LG=int(os.sys.argv[4])

#procesing
total=(samsung+iphone+LG)

#verificador
comprador_potencial=(total>=5000)

#condicion simple
#si el el total supera 5000 regalar una tarjeta para google play
if ( comprador_potencial== True ):
    print("se ha ganado tres tarjeta para google play")
if ( comprador_potencial>=4900 and comprador_potencial<4999 ):
    print("se ha ganado una tarjeta para google play")
if ( comprador_potencial<4899):
    print("gane tarhetas para google play por compras superiores a 5000 soles")
#fin_if

#output
print("###############################")
print("#  Distribuidor de celulares  #")
print("###############################")
print("# Variables:    cantidad:")
print("# Nombre:",    nombre)
print("# Samsung:",  samsung)
print("# Iphone:",   iphone)
print("# LG:",       LG)
print("-------------------------------")
print("# Total:",     total)
print("###############################")

