import os
#CALCULADORA DE PRESION HIDROSTATICA DE UN CUERPO SUMERGIDO
#input
densidad_liquido=float(os.sys.argv[1])
gravedad=float(os.sys.argv[2])
profundidad=float(os.sys.argv[3])

#processing
presion_hidrostatica=densidad_liquido*gravedad*profundidad

#verificador
presion_alta=(presion_hidrostatica>400)

#output
print("                                                              ")
print("##############################################################")
print("# CALCULADORA DE PRESION HIDROSTATICA DE UN CUERPO SUMERGIDO #")
print("##############################################################")
print("# El valor de la densidad del liquido es:",densidad_liquido)
print("# El valor de la gravedad es:",gravedad)
print("# El valor de la profundidad es:",profundidad)
print("#------------------------------------------------------------#")
print("# La presion hidrostatica a la que esta sometida el")
print("# cuerpo es de:",presion_hidrostatica)
print("##############################################################")


#condicion doble
#si la presion es muy alta mostrar
if (presion_alta == True):
    print("             CUIDADO LA PRESION ES MUY ALTA !!         ")
else:
    print(" La presion no es alta ")
#FIN_IF
