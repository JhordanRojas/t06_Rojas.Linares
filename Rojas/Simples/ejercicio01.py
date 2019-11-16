import os
#CALCULADORA DE LA VELOCIDAD FINAL DE UN MOVIL
#input
velocidad_inicial = int(os.sys.argv[1])
aceleracion = int(os.sys.argv[2])
tiempo = int(os.sys.argv[3])

#processing
velocidad_final = velocidad_inicial+(aceleracion*tiempo)

#verificador
alta_velocidad=(velocidad_final > 200)

#output
print("                                                    ")
print("####################################################")
print("#    CALCULADORA DE VELOCIDAD FINAL DE UN MOVIL    #")
print("####################################################")
print("# Velocidad inicial    :" , velocidad_inicial)
print("# Aceleracion          :" , aceleracion)
print("# Tiempo               :" , tiempo)
print("#--------------------------------------------------#")
print("# Velocidad final del auto :  ", velocidad_final,"km/h")
print("####################################################")


#condicion simple
#si la velocidad es mayor que 200 mostrar advertencia
if (alta_velocidad == True ):
    print("                VAS COMO UN RAYO!!!              ")
#FIN_IF
