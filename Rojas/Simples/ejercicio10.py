import os
#CALCULADORA DE LA SUMATORIA DE UNA SUCESION
#input
primer_elemento=int(os.sys.argv[1])
ultimo_elemento=int(os.sys.argv[2])
total_elementos=int(os.sys.argv[3])

#processing
sumatoria=(primer_elemento+ultimo_elemento)*total_elementos/2

#verifcador
sumatoria_baja=(sumatoria < 550)

#output
print("                                                                     ")
print("#####################################################################")
print("#     SUMATORIA DE UNA SUCESION ARITMETICA DE NUMEROS NATURALES     #")
print("#####################################################################")
print("# El valor del primer elemento es:", primer_elemento)
print("# El valor del ultimo elemento es:", ultimo_elemento)
print("# El total de elementos es:",total_elementos)
print("#-------------------------------------------------------------------#")
print("# El valor de la sumatoria de los elementos de la sucesion es:",sumatoria)
print("#####################################################################")

#condicion simple
#si la sumatoria es baja mostrar
if (sumatoria_baja == True):
    print("                         LA SUMATORIA ES BAJA                      ")
#FIN_IF
