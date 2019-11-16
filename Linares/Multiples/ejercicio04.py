import os
nombre, fierro, cemento, tubos=",", 0, 0 ,0

#imput
nombre=os.sys.argv[1]
fierro=int(os.sys.argv[2])
cemento=int(os.sys.argv[3])
tubos=int(os.sys.argv[4])

#procesing
total=(fierro+cemento+tubos)

#verificador
comprador_rentable=(total>=500)

#condicion simple
#si es comprador rentable hacerle un descuento
if ( comprador_rentable == True ):
    print("se ha ganado un descuento")
if ( comprador_rentable>=490 and comprador_rentable<500 ):
    print("gane descuentos comprando mas")
if ( comprador_rentable <489 ):
    print("gracias por su compra")
#fin_if

#output
print("##############################")
print("#    Ferreteria linares      #")
print("##############################")
print("# Variables:    cantidad:")
print("# Nombre:",    nombre)
print("# Fierro:",   fierro)
print("# Cemento:",  cemento)
print("# Tubos:",    tubos)
print("------------------------------")
print("# Total:",     total)
print("##############################")
