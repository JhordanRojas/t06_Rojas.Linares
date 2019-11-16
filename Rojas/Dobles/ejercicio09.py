import os
#CALCULAR EL VOLUMEN DE UNA PIRAMIDE TRIANGULAR
#input
altura_piramide=float(os.sys.argv[1])
base_triangle=float(os.sys.argv[2])
altura_triangle=float(os.sys.argv[3])

#processing
area_base=((base_triangle*altura_triangle)/2)
volumen=((area_base*altura_piramide)/3)

#verificador
piramide_pequena=(volumen < 78)

#output
print("                                                         ")
print("#########################################################")
print("#        CALCULADORA DE VOLUMEN DE UNA PIRAMIDE         #")
print("#########################################################")
print("# La base de la piramide es un triangulo y su area es:",area_base)
print("# La altura de la piramide es:",altura_piramide)
print("#-------------------------------------------------------#")
print("# El volumen de la piramide es:",volumen,"metros cubicos")
print("#########################################################")

#condicion doble
#si el volumen es mayor del recomendado mostrar
if (piramide_pequena == False):
    print("               ESTO ES LIGERAMENTE GRANDE              ")
else:
    print(" Esto no es grande ")
#FIN_IF
