import os
nombre, precio1, precio2, precio3=",", 0, 0 ,0

#imput
nombre=os.sys.argv[1]
precio1=int(os.sys.argv[2])
precio2=int(os.sys.argv[3])
precio3=int(os.sys.argv[4])

#procesing
total=(precio1+precio2+precio3)

#verificador
comprobando=(total>=50)

#condicion simple
#si supera los 50 soles regalar un plato
if ( comprobando == True ):
    print("se ha ganado un plato")
#fin_if

#output
print("##############################")
print("#      Negocios linares      #")
print("##############################")
print("# Variables:    cantidad:")
print("# Nombre:",    nombre)
print("# Precio1:",  precio1)
print("# Precio2:",  precio2)
print("# Precio3:",  precio3)
print("##############################")
print("# Total:",     total)
print("##############################")
