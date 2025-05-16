#C5G808 Diego Josue Martinez Alfaro
#Entrega: imprimir en pantalla las tablas de multiplicar (incluye valores multiplicados desde el 1 hasta el 12),
#  segun el rango de tablas especificado por el usuario. Cada tabla debe tener un encabezado y en cada fila se imprime el resultado de una multiplicacion. Por ejemplo "1 x 2 = 2"

#Este fue el planteamineto inicial
"""
tabla_menor <-- input
tabla_mayor <-- input
multiplicando <-- tabla_menor
tabla <-- ("Tabla de", multiplicando \n multiplicando "x" )
print(tabla, "x", multiplicador, "=", tabla * multiplicador)


tamano de tabla es 12



#Estas son las tablas indicadas por el usuario
tabla_menor = int(input("Ingrese la tabla inicial: "))
tabla_mayor = int(input("Ingrese la tabla final: "))

#Este valor es lo que sera la tabla que se esta utilizando en el momento
multiplicando = tabla_menor

#Aqui se obtendran los valores de las tablas, la multiplicacion hecha

for multiplicando in range(tabla_menor, tabla_menor):
    """

#De aquí en adelante comienza el planteamiento actual


"""
tabla_inicial <-- input
tabla_final <-- input
#Tablas indicadas por el usuario

tabla indicada <-- tabla inicial
#La tabla indicada se usara como variable para indicar la tabla actual

multiplicador <-- 1-12
#La variable multiplicador sera el valor que indica el numero por el cual se va a multiplicar

cuando tabla_indicada sea menor o igual a tabla_final, va a imprimir la tabla actual con los valores de multiplicando y multiplicador
cuando multiplicador llegue a 12, se revertira su valor a 1, y se continuara a la siguiente tabla hasta llegar al fin de las indicadas

"""
#De aquí empiezan las líneas válidas

#Valores de tabla
print("\033[93mMultiplixado\033[0m \n Bienvenido a Multiplixado, tu programa de multiplicación estrella. \n Por favor indica los valores de las tablas que quieras en orden de menor a mayor.")

tabla_inicial = int(input("\033[94mIngrese la primer tabla: \033[0m"))
tabla_final = int(input("\033[94mIngrese la segunda tabla: \033[0m"))
#Aquí se piden los numeros de tabla que quiera indicar el usuario

tabla_indicada = tabla_inicial
multiplicador = 1
#Valores utilizados para indicar la tabla actual

#El juguito

while tabla_indicada <= tabla_final:
        if multiplicador <= 12:
            if multiplicador == 1:
                 print("\033[94mTabla del \033[0m", tabla_indicada)
            valor_final = tabla_indicada * multiplicador
            print(tabla_indicada, "x", multiplicador, "=", valor_final)
            multiplicador += 1

        elif tabla_indicada < tabla_final+1:
            tabla_indicada += 1
            multiplicador = 1
# Aquí se crea un loop que hace que cuando la tabla que se está utilizando en el momento sea menor que la tabla final,
#revise si el numero por el que se multiplica es menor que 12, e imprima el nombre de la tabla, luego imprima el valor
#1 de la tabla, y continuamente lo incremente hasta que ese valor sea 12, en cual caso cambiará de loop y comenzará a
#la siguiente tabla. 

#Aquí terminan las líneas válidas


# La siguiente fue la idea inicial, la cual luego dejo con el propósito de demostrar el avance
'''
if tabla_indicada < tabla_final+1:
    print("Tabla del ", tabla_indicada)
    print(tabla_indicada, "x", multiplicandos, "=", valor_final)

elif tabla_indicada <= tabla_final+1:
    print("Nada")

else:
    print("pepe")
'''