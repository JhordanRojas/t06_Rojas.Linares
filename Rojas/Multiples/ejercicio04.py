import os
#CALCULADORA DE AHORRO
#input
dinero_inicial=float(os.sys.argv[1])
dinero_mensual=float(os.sys.argv[2])
meses=float(os.sys.argv[3])

#processing
dinero_final=dinero_inicial+(dinero_mensual*meses)

#verificador
ahorro_alto=(dinero_final > 1000)

#condicional multiple
#si el  ahorro es alto mostrar el siguiente mensaje
if (ahorro_alto == True):
    print("       Usted ha ganado una tarjeta debito premium     ")
    print("                >>>> FELICIDADES <<<<                 ")
if (100<dinero_final<1000):
    print(" El ahorro es muy bueno ")
if (10<dinero_final<100):
    print(" Este ahorro es muy pobre :( ")
#FIN_IF

#output
print("                                                        ")
print("########################################################")
print("#           CALCULADORA DE AHORRO DE DINERO            #")
print("########################################################")
print("# El valor del dinero inicial es:",dinero_inicial,"s/.")
print("# El valor del dinero ahorrado por mes es:",dinero_mensual,"s/.")
print("# El numero de meses a ahorrar es:", meses)
print("#------------------------------------------------------#")
print("# El dinero total al final del ahorro es de:",dinero_final,"s/.")
print("########################################################")

