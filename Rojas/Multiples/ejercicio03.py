import os
#CALCULADORA DE INDICE DE MASA CORPORAL
#input
peso=float(os.sys.argv[1])
altura=float(os.sys.argv[2])

#processing
imc=peso/altura**2

#verificador
sobrepeso=(imc >= 25)

#output
print("                                                 ")
print("#################################################")
print("#    CALCULADORA DE INDICE DE MASA CORPORAL     #")
print("#################################################")
print("# El valor del peso es:",peso,"kg")
print("# El valor de la altura es:",altura,"m")
print("#-----------------------------------------------#")
print("# El valor del IMC es:", imc)
print("#################################################")
print("El valor normal oscila entre 18.5 - 24.9")
print("mas que eso es obesidad, menos significa delgadez")
print("#################################################")

#condicion multiple
#si la persona tiene sobrepeso mostrar
if (sobrepeso == True):
    print(">> USTED AH DESBLOQUEADO NUESTRA DIETA EXCLUSIVA <<")
if (19< imc <25):
    print(" Usted esta en el peso correcto ")
if (0< imc <19):
    print(" Usted tiene delgadez, visite un medico ")
#FIN_IF

