import os
#CALCULADORA DEL AREA DE UN TRAPECIO
#input
base_mayor=int(os.sys.argv[1])
base_menor=int(os.sys.argv[2])
altura=int(os.sys.argv[3])

#processing
area=((base_mayor+base_menor)*altura)/2

#verificador
area_pequenia=(area<100)

#output
print("                                            ")
print("############################################")
print("#    CALCULADORA DEL AREA DE UN TRAPECIO   #")
print("############################################")
print("# Base mayor:", base_mayor)
print("# Base menor:", base_menor)
print("# Altura    :", altura)
print("#------------------------------------------#")
print("# El valor del area del trapecio es:", area)
print("############################################")


#condicion multiple
#si el area es pequeña mostrar
if (area > 100):
    print("           ESTA AREA ES SUFICIENTE        ")
if (area < 100 and area>50):
    print(" Esta area es algo pequeña ")
if (area > 500):
    print(" Esta area es muy grande ")
#FIN_IF

