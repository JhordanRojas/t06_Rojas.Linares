import os
#CALCULADORA DE DILATACION LINEAL
#input
longitud=float(os.sys.argv[1])
coef=float(os.sys.argv[2])
variacion_temp=float(os.sys.argv[3])

#processing
dilatacion_lineal=longitud*coef*variacion_temp
longitud_final=longitud+dilatacion_lineal

#verificador
mucha_dilatacion=(dilatacion_lineal>0.5)

#output
print("                                                            ")
print("############################################################")
print("#            CALCULADORA DE DILATACION LINEAL              #")
print("############################################################")
print("# El valor de la longitud inicial de la varilla es:",longitud,"m")
print("# El valor de la variacion de la temperatura es:",variacion_temp,"C")
print("# El valor del coeficiente de dilatacion es:",coef)
print("#----------------------------------------------------------#")
print("# La dilatacion de la varilla es:",dilatacion_lineal,"m")
print("# La longitud final de la varilla es:",longitud_final,"m")
print("############################################################")

#condicion simple
#si la dilatacion lineal es alta mostrar
if (mucha_dilatacion == True):
    print("              LA DILATACION ES EXCESIVA           ")
#FIN_IF
