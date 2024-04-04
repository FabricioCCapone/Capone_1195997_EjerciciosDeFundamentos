#Crear un programa que pida un número de día (ejemplo: 1) y escriba el nombre del día en letras ("lunes"). 
#Verificar que el día esté entre 1 y 7, e informar en caso de que no lo sea. 

numero_dia = 0
while numero_dia > 7 or numero_dia < 1:
    numero_dia = int(input("Ingrese el numero del dia que desea ver. Ejemplo: 1. Lunes, 2. Martes, etc. "))
    if(numero_dia > 7 or numero_dia < 1 ):
        print("El numero debe ser del 1 al 7.")
    elif (numero_dia == 1):
            print("Lunes.")
    elif (numero_dia == 2):
            print("Martes.")
    elif (numero_dia == 3):
            print("Miercoles.")
    elif (numero_dia == 4):
            print("Jueves.")
    elif (numero_dia == 5):
            print("Viernes.")
    elif (numero_dia == 6):
            print("Sabado.")
    elif (numero_dia == 7):
            print("Domingo.")