""" 
tipo_calculo <-- el tipo de calculo que el usuario desee realizar

#Valores de tipo de calculo
    1 <-- multiplicacion_base | multiplicacion_estado <-- (1Positiva, 2Negativa)
    2 <-- potencia_base |   potencia_estado <-- (1Positiva, 2Negativa)

    

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

repeat_initial_ui = 1
repeat_multiplication_tables = 0
print("\033[93mMultiplixado\033[0m \n Bienvenido a Multiplixado, tu programa de calculo estrella. \n")
tipo_calculo = int(input("Ingrese el valor de el calculo que desee realizar: "))


while repeat_initial_ui == 1:
    try:
        if tipo_calculo == 1:
            repeat_initial_ui = 0
            repeat_multiplication_tables = 1
        if tipo_calculo == 2:
            repeat_initial_ui = 0
            repeat_power_tables = 1
    except ValueError:
         print("No reconocido")

#Tablas de multiplicacion

if repeat_multiplication_tables == 1:
    repeat_multiplication_tables = 0
    #Valores de tabla
    print("Por favor indica los valores de las tablas que quieras en orden de menor a mayor.")

    tabla_inicial = int(input("\033[94mIngrese la primer tabla: \033[0m"))
    tabla_final = int(input("\033[94mIngrese la segunda tabla: \033[0m"))
    #Aquí se piden los numeros de tabla que quiera indicar el usuario

    tabla_indicada = tabla_inicial
    multiplicador = 1
    #Valores utilizados para indicar la tabla actual

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


if repeat_power_tables == 1:
    repeat_power_tables = 0
    #Valores de tabla
    print("Por favor indica los valores de las tablas que quieras en orden de menor a mayor.")

    tabla_inicial = int(input("\033[94mIngrese la primer tabla: \033[0m"))
    tabla_final = int(input("\033[94mIngrese la segunda tabla: \033[0m"))
    #Aquí se piden los numeros de tabla que quiera indicar el usuario

    tabla_indicada = tabla_inicial
    multiplicador = 1
    #Valores utilizados para indicar la tabla actual

    while tabla_indicada <= tabla_final:
            if multiplicador <= 12:
                if multiplicador == 1:
                    print("\033[94mTabla del \033[0m", tabla_indicada)
                valor_final = tabla_indicada ** multiplicador
                print(tabla_indicada, "^", multiplicador, "=", valor_final)
                multiplicador += 1

            elif tabla_indicada < tabla_final+1:
                tabla_indicada += 1
                multiplicador = 1