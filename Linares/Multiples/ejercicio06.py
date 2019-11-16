import os
nombre, nota1, nota2, nota3=",", 0, 0, 0

#imput
nombre=os.sys.argv[1]
nota1=int(os.sys.argv[2])
nota2=int(os.sys.argv[3])
nota3=int(os.sys.argv[4])

#procesing
total=(nota1+nota2+nota3)/3

#verificador
promedio=(total>=17.5)

#condicion simple
#si el promedio supera 17.5 dar media bece
if ( promedio == True ):
    print("se ha ganado media beca")
if ( promedio>=16 and promedio<17.5 ):
    print("estudie mas y gane una beca")
if ( promedio<15.9 ):
    print("estudie mas")
#fin_if

#output
print("##############################")
print("#            UNPRG           #")
print("##############################")
print("# Variables:    cantidad:")
print("# Nombre:",    nombre)
print("# Nota1:",  nota1)
print("# Nota2:",  nota2)
print("# Nota3:",  nota3)
print("------------------------------")
print("# Total:",     total)
print("##############################")
