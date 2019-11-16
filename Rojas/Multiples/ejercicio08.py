import os
#CALUCLADORA DEL TRABAJO SOBRE UN OBJETO
#Input
masa=float(os.sys.argv[1])
aceleracion=float(os.sys.argv[2])
distancia=float(os.sys.argv[3])

#Processing
fuerza=(masa*aceleracion)
trabajo=(fuerza*distancia)

#verificador
trabajo_alto=(trabajo > 5000)

#Output
print("                                                            ")
print("############################################################")
print("#    CALCULADORA DEL TRABAJO REALIZADO SOBRE UN OBJETO     #")
print("############################################################")
print("# El valor de la masa es:        ",masa)
print("# El valor de la aceleracion es: ", aceleracion)
print("# El valor de la distancia es:   ", distancia)
print("# El valor de la fuerza ejercida es: ", fuerza)
print("#----------------------------------------------------------#")
print("# El valor del trabajo realizado es: ", trabajo)
print("############################################################")

#condicion multiple
#Si el trabajo es alto mostrar
if (trabajo_alto == False):
    print("                 HACE FALTA MAS POTENCIA             ")
if (1000<trabajo<5000):
    print(" El trabajo es normal ")
if (trabajo_alto == True):
    print(" El valor del trabajo es alto ")
#FIN_IF
