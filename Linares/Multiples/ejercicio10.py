import os
nombre, precio_de_las_pastillas, precio_de_los_jarabes, precio_del_shampoo=",", 0, 0, 0

#imput
nombre=os.sys.argv[1]
precio_de_las_pastillas=int(os.sys.argv[2])
precio_de_los_jarabes=int(os.sys.argv[3])
precio_del_shampoo=int(os.sys.argv[4])

#procesing
total=(precio_de_las_pastillas+precio_de_los_jarabes+precio_del_shampoo)

#verificador
descuento_los_martes=(total>=20)

#condicion simple
#si el total supera los 20 soles dar puntos bonus
if ( descuento_los_martes == True ):
    print("se gano puntos banus para su siguiente compra")
if ( descuento_los_martes>=18 and descuento_los_martes<20 ):
    print("compra mas y gana puntos bonus")
if ( descuento_los_martes<17 ):
    print("gracias por su compra")
#fin_if

#output
print("##############################")
print("#            MIFARMA         #")
print("##############################")
print("# Variables:                cantidad:")
print("# Nombre:",    nombre)
print("# Precio de las pastillas:", precio_de_las_pastillas)
print("# Precio del jarabe:",       precio_de_los_jarabes)
print("# Precio de el shampoo:",    precio_del_shampoo)
print("-------------------------------")
print("# Total:",                    total)
print("##############################")
