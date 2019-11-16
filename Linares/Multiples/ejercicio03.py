import os
nombre, zapatos, zapatillas, tacones=",", 0, 0 ,0

#imput
nombre=os.sys.argv[1]
zapatos=int(os.sys.argv[2])
zapatillas=int(os.sys.argv[3])
tacones=int(os.sys.argv[4])

#procesing
total=(zapatos+zapatillas+tacones)

#verificador
comprador_compulsivo=(total>=150)

#condicion simple
#si s comprador compulsivo mostrar la tarjeta dorada
if ( comprador_compulsivo == True ):
    print("se gano la tarjeta dorada")
if ( comprador_compulsivo>=140 and comprador_compulsivo<150 ):
    print("se gano la tarjeta platino")
if ( comprador_compulsivo <139 ):
    print("gracias")
#fin_if

#output
print("##############################")
print("#            BATA            #")
print("##############################")
print("# Variables:    cantidad:")
print("# Nombre:",       nombre)
print("# Zapatos:",     zapatos)
print("# Zapatillas:",  zapatillas)
print("# Tacones:",     tacones)
print("------------------------------")
print("# Total:",        total)
print("##############################")
