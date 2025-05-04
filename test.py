#Aqui estoy importando una funcion que hace que haya un buffer entre cosas
import time

#Esto es lo principal y la manera en que se utiliza el try
'''Account interface (accint)'''
while accint == 0:
    try:
        welcome = int(input("Please select a provided option: "))
        if welcome == 1 :
            print(" ──────────────────────────────────────────────────────────────────────")
            print("|    -=AUB=-                                                           |")
            print("|                                                                      |")
            print("|                                                                      |")
            print("|                                                                      |")
            print("|                                                                      |")
            print("|                                                                      |")
            print("|                                                                      |")
            print("|                                                                      |")
            print(" ──────────────────────────────────────────────────────────────────────")
            accint = 1
            login = 1
            
        if welcome == 2 :
            
            print(" ──────────────────────────────────────────────────────────────────────")
            print("|    -=AUB=-                                                           |")
            print("|                                                                      |")
            print("|                option2                                               |")
            print("|                                                                      |")
            print("|                                                                      |")
            print("|                                                                      |")
            print("|                                                                      |")
            print("|                                                                      |")
            print(" ──────────────────────────────────────────────────────────────────────")
            accint = 1
            login = 2
            
        else:
            print(" ───────────────────────────────────────────────────────────────────────────────────────────")
            print("|    -=AUB=-                                                                                |")
            print("|                                                                                           |")
            print("|      1- Log In                                                                            |")
            print("|                                                                                           |")
            print("|      Don't have an account?                                                               |")
            print("|      2- Create Account                                                                    |")
            print("|                                                                                           |")
            print("|        Invalid selection (Provided options only)                                          |")
            print(" ───────────────────────────────────────────────────────────────────────────────────────────")
            #Este time.sleep es algo que hace que espere cierto tiempo para continuar
            time.sleep(2)
            print(" ───────────────────────────────────────────────────────────────────────────────────────────")
            print("|    -=AUB=-                                                                                |")
            print("|                                                                                           |")
            print("|      1- Log In                                                                            |")
            print("|                                                                                           |")
            print("|      Don't have an account?                                                               |")
            print("|      2- Create Account                                                                    |")
            print("|                                                                                           |")
            print("|                                                                                           |")
            print(" ───────────────────────────────────────────────────────────────────────────────────────────")
    #El "except ValueError" es algo que se utiliza siempre al final de un try, es para cuando algo no funciona como se quiere, entonces se da un resultado distinto
    except ValueError:
            print(" ───────────────────────────────────────────────────────────────────────────────────────────")
            print("|    -=AUB=-                                                                                |")
            print("|                                                                                           |")
            print("|      1- Log In                                                                            |")
            print("|                                                                                           |")
            print("|      Don't have an account?                                                               |")
            print("|      2- Create Account                                                                    |")
            print("|                                                                                           |")
            print("|        Invalid selection (Provided options only)                                          |")
            print(" ───────────────────────────────────────────────────────────────────────────────────────────")