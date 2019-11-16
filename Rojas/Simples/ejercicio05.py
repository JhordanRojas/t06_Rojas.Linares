import os
#CALCULADORA DEL TIEMPO DE VUELO DE UN PROYECTIL
#input
velocidad_inicial=float(os.sys.argv[1])
gravedad=float(os.sys.argv[2])
import math
y=float(os.sys.argv[3])
x=math.radians(y)

#processing
tiempo_vuelo=(2*velocidad_inicial*math.sin(x))/gravedad

#verificador
vuelo_corto=(tiempo_vuelo<5)

#output
print("                                                         ")
print("#########################################################")
print("#     CALCULADORA DE TIEMPO DE VUELO DE UN PROYECTIL    #")
print("#########################################################")
print("# El valor de la velocidad inicial: ",velocidad_inicial,"m/s")
print("# El valor de la gravedad es: ",gravedad,"m/s^2")
print("# El valor del seno del angulo",y,"es:",math.sin(x))
print("--------------------------------------------------------#")
print("# El tiempo de vuelo del proyectil es:",tiempo_vuelo,"s")
print("#########################################################")


#condicion simple
#si el tiempo de vuelo es corto mostrar
if (vuelo_corto == True):
    print("                 ESTO SERA RAPIDO!             ")
#FIN_IF
