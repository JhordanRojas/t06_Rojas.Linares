import os
precio_de_polos, precio_de_pantalones, precio_de_chompas=0, 0 ,0

#imput
precio_de_polos=int(os.sys.argv[1])
precio_de_pantalones=int(os.sys.argv[2])
precio_de_chompas=int(os.sys.argv[3])

#procesing
total=(precio_de_polos+precio_de_polos+precio_de_chompas)

#verificador
comprobando=(total>=100)

#condicion simple
#si el total supera los 100 soles, regalar un descuento adicional
if ( comprobando == True ):
    print("usted se gano un descuento adicional")
if ( comprobando>=90 and comprobando<100 ):
    print("gane descuentos adicionales")
if ( comprobando<89):
    print("vuelva pronto")
#fin_if

#output
print("#################################")
print("#            RIPLEY             #")
print("#################################")
print("# Variables:                cantidad:")
print("# Precio de polos:",         precio_de_polos)
print("# Precio de pantalones:",   precio_de_pantalones)
print("# Precio de chompas:",      precio_de_chompas)
print("---------------------------------")
print("# Total:",                  total)
print("#################################")
