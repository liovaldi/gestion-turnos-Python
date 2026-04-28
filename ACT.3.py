#TP integrador – Repetitivas- Condicionales y Secuenciales. // Iovaldi Ludmila // Comision 2
#Ejercicio 3 (Alta) — “Agenda de Turnos con nombres (sin listas)”

#Variables a definir
Lunes1=Lunes2=Lunes3=Lunes4=""

Martes1=Martes2=Martes3=""

#Datos del operador
operador=input("Ingrese el nombre del operador: ").strip().lower()
while not operador.isalpha():
        print("Error!:El nombre del operador solo debe contener letras.")
        operador=input("Ingrese el nombre del operador: ").strip().lower()
#Menu de opciones
while True:    
    print(">>MENU<<")
    print("1) Reservar turno")
    print("2) Cancelar turno (por nombre)")
    print("3) Ver agenda del dia")
    print("4) Ver resumen general")
    print("5)Cerrar el sistema")
    
    opcion = input("Por favor, escoja alguna de las opciones: ").strip()
    while not opcion.isdigit():
        print("Error: escoja un numero valido")
        opcion = input("Por favor, escoja alguna de las opciones: ").strip()
    opcion=int(opcion)
    if opcion > 5 or opcion < 1:
        print("Error:escoja un numero valido")

    match opcion:
#Desarrollo de reserva de turnos
        case 1: 
            dia=input("Escoja un dia: 1) Lunes - 2) Martes: ").strip()
            while not dia.isdigit():
                print("Error: escoja un numero valido")
                dia=input("Escoja un dia: 1) Lunes - 2) Martes: ").strip()
            dia=int(dia)
            while dia < 1 or dia > 2:
                print("Error:escoja un numero valido")
                dia=input("Escoja un dia: 1) Lunes - 2) Martes: ").strip()

#Desarrollo de dia escogido 1:Lunes        
            if dia == 1:
                turno1=input("Escoja un turno: 1) 1er turno // 2) 2do turno// 3) 3er turno // 4) 4to turno: ").strip()
                while not turno1.isdigit():
                    print("Error: escoja un numero valido")
                    turno1=input("Escoja un turno: 1) 1er turno // 2) 2do turno// 3) 3er turno // 4) 4to turno: ").strip()
                turno1=int(turno1)
                while turno1 < 1 or turno1 > 4:
                    print("Error:escoja un numero valido")
                    turno1=input("Escoja un turno: 1) 1er turno // 2) 2do turno// 3) 3er turno // 4) 4to turno: ").strip()

                
#Solicitud de nombre del paciente:
                
                paciente1=input("Ingrese el nombre del paciente: ").strip().lower()
                while not paciente1.isalpha():
                    print("Error: ingrese un paciente que solo contenga letras: ")
                    paciente1=input("Ingrese el nombre del paciente: ").strip().lower()
                    
#opciones de turno LUNES
                if turno1 == 1 and Lunes1 == "":
                    Lunes1 = paciente1
                    print(operador,"Su turno se agendo con exito para: ",paciente1)
                    print("-------------------------------------")
                elif turno1 == 2 and Lunes2 == "":
                    Lunes2 = paciente1
                    print(operador,"Su turno se agendo con exito para: ",paciente1)
                    print("-------------------------------------")
                elif turno1 == 3 and Lunes3 == "":
                    Lunes3 = paciente1
                    print(operador,"Su turno se agendo con exito para: ",paciente1)
                    print("-------------------------------------")
                elif turno1 == 4 and Lunes4 == "":
                    Lunes4 = paciente1
                    print(operador,"Su turno se agendo con exito para: ",paciente1)
                    print("-------------------------------------")
                else:
                    print("Error!:Turno ya reservado, por favor escoja otro")
                    print("-------------------------------------")
#Desarrollo de dia escogido 2: MARTES     
            elif dia == 2:
                turno2=input("Escoja un turno: 1) 1er turno // 2) 2do turno// 3) 3er turno: ").strip()
                while not turno2.isdigit():
                    print("Error: escoja un numero valido")
                    turno2=input("Escoja un turno: 1) 1er turno // 2) 2do turno// 3) 3er turno: ").strip()  
                turno2=int(turno2)
                while turno2 < 1 or turno2 > 3:
                    print("Error:escoja un numero valido")
                    turno2=input("Escoja un turno: 1) 1er turno // 2) 2do turno// 3) 3er turno: ").strip()  
#Solicitud de nombre del paciente
                paciente2=input("Ingrese el nombre del paciente: ").strip().lower()
                while not paciente2.isalpha():
                    print("Error: ingrese un paciente que solo contenga letras: ")
                    paciente2=input("Ingrese el nombre del paciente: ").strip().lower()
                    
#Opciones de turno MARTES
                if turno2 == 1 and Martes1 == "":
                    Martes1 = paciente2
                    print(operador,"Su turno se agendo con exito para: ",paciente2)
                    print("-------------------------------------")
                elif turno2 == 2 and Martes2 == "":
                    Martes2= paciente2
                    print(operador,"Su turno se agendo con exito para: ",paciente2)
                    print("-------------------------------------")
                elif turno2 == 3 and Martes3 == "":
                    Martes3 = paciente2
                    print(operador,"Su turno se agendo con exito para: ",paciente2)
                    print("-------------------------------------")
                else:
                    print("Error!:Turno ya reservado, por favor escoja otro")
                    print("-------------------------------------")
#Cancelacion de turnos
#Seleccion de dia
        case 2: 
            dia_cancel=input("Por favor, escoja el dia del turno a cancelar: 1) Lunes - 2) Martes: ").strip()
            while not dia_cancel.isdigit():
                print("Error: escoja un numero valido")
                dia_cancel=input("Por favor, escoja el dia del turno a cancelar: 1) Lunes - 2) Martes: ").strip()
            dia_cancel=int(dia_cancel)
            while dia_cancel < 1 or dia_cancel > 2:
                print("Error: escoja un numero correcto")
                dia_cancel=input("Por favor, escoja el dia del turno a cancelar: 1) Lunes - 2) Martes: ").strip()
#Solicitud de nombre de paciente a cancelar
            paciente_cancel=input("Ingrese el nombre del paciente: ").strip().lower()
            while not paciente_cancel.isalpha():
                print("Error: ingrese un paciente que solo contenga letras: ")
                paciente_cancel=input("Ingrese el nombre del paciente: ").strip().lower()
                
#cancelacion LUNES            
            if dia_cancel == 1:
                if paciente_cancel == Lunes1:
                    print("Su turno se ha cancelado con exito.")
                    print("-------------------------------------")
                    Lunes1=""
                elif paciente_cancel == Lunes2:
                    print("Su turno se ha cancelado con exito.")
                    print("-------------------------------------")
                    Lunes2= ""
                elif paciente_cancel== Lunes3:
                    print("Su turno se ha cancelado con exito.")
                    print("-------------------------------------")
                    Lunes3=""
                elif paciente_cancel == Lunes4:
                    print("Su turno se ha cancelado con exito.")
                    print("-------------------------------------")
                    Lunes4=""
                else:
                    print("El nombre del paciente no es correcto")
#Cancelacion MARTES
            elif dia_cancel == 2:
                if paciente_cancel == Martes1:
                    print("Su turno se ha cancelado con exito.")
                    print("-------------------------------------")
                    Martes1=""
                elif paciente_cancel == Martes2:
                    print("Su turno se ha cancelado con exito.")
                    print("-------------------------------------")
                    Martes2=""
                elif paciente_cancel == Martes3:
                    print("Su turno se ha cancelado con exito.")
                    print("-------------------------------------")
                    Martes3=""
                else:
                    print("El nombre del paciente no es correcto")
        case 3:
            print(">>Agenda del dia LUNES<<")
            if Lunes1 == "":
                print("Turno 1) libre")
            else:
                print("Turno 1) reservado")
            if Lunes2 == "":
                print("Turno 2) libre")
            else:
                print("Turno 2) reservado")
            if Lunes3 == "":
                print("Turno 3) libre")
            else:
                print("Turno 3) reservado")
            if Lunes4 == "":
                print("Turno 4) libre")
            else:
                print("Turno 4) reservado")

            print(">>Agenda del dia MARTES<<")
            if Martes1 == "":
                print("Turno 1) libre")
            else:
                print("Turno 1) reservado")
            if Martes2 == "":
                print("Turno 2) libre")
            else:
                print("Turno 2) reservado")
            if Martes3 == "":
                print("Turno 3) libre")
            else:
                print("Turno 3) reservado")
                print("-------------------------------------")

            continue
        case 4:
            print(">>Resumen general<<")
            ocupados_lunes = 0
            if Lunes1 != "":
                ocupados_lunes +=1
            elif Lunes2 != "":
                ocupados_lunes += 1
            elif Lunes3 != "":
                ocupados_lunes += 1
            elif Lunes4 != "":
                ocupados_lunes +=1
            desocupados_lunes= 4 - ocupados_lunes
            print(f"Lunes: total de dias disponibles : {desocupados_lunes} // total de dias ocupados: {ocupados_lunes}")

            ocupados_martes = 0
            if Martes1 != "":
                ocupados_martes +=1
            elif Martes2 != "":
                ocupados_martes += 1
            elif Martes3 != "":
                ocupados_martes += 1
            desocupados_martes= 3 - ocupados_martes
            print(f"Martes: total de dias disponibles : {desocupados_martes} // total de dias ocupados: {ocupados_martes}")

            if ocupados_lunes > ocupados_martes:
                print("El dia con mas turnos ocupados es el Lunes")
            else: 
                print("El dia con mas turnos ocupados es el Martes")
                print("-------------------------------------")

        case 5:
            print("Sistema cerrado")
            break
