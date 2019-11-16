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


#condicion multiple
#si la velocidad es mayor que 200 mostrar advertencia
if (velocidad_final > 200):
    print("                VAS COMO UN RAYO!!!              ")
if (100<velocidad_final<200):
    print(" Buena velocidad ")
if (0<velocidad_final<100):
    print(" La velocidad es muy baja ")
else:
    print(" valores erroneos ")
#FIN_IF
