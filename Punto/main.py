from control.persona import Persona
import sys

p = Persona()


def imprimirMenu():
    while True:
        try:
            print("¿Qué deseas hacer?\n")
            print("1.- Registrar persona\n")
            print("2.- Buscar por rut\n")
            print("3.- Imprimir certificados\n")
            print("4.- Salir\n")

            op = int(input("---> "))
            if op == 1:
                menuRegistro()
                break
            elif op == 2:
                menuBuscar()
                break
            elif op == 3:
                menuCertificados()
                break
            elif op == 4:
                print("Adios")
                sys.exit()
                break
                
            else:
                print("Ingrese una opcion correcta")

        except ValueError() as err:
            print("Algo salio mal, Motivo: ", err)
        except TypeError() as err:
            print("Algo salio mal, Motivo: ", err)


def menuRegistro():
    print("Menu de Registro Civil - Registrar\n")
    while True:
        try:
            rut = str(input("Ingrese su rut---> "))
            if p.validarRut(rut) == True:
                nombre = str(input("Ingrese su nombre---> "))
                edad = int(input("Ingrese su edad ---> "))
                if edad > 0:
                    fecha = str(
                        input("Ingresa tu fecha de nacimiento. Formato requerido dd/mm/aaaa---> "))
                    estado = str(input("Ingresa tu estado civil---> "))
                    if p.crearNuevaPersona(rut, nombre, edad, fecha, estado) == True:
                        print("\n")
                        while True:
                            print(
                                "¿Deseas seguir continuando el menu? Escribe 'Si' para continuar y 'No' para salir")
                            op = str(input("---> "))
                            op = op.lower()
                            if op == "si" or "s" and op != "":
                                imprimirMenu()
                            elif op == "no" or "n" and op != "":
                                break
                            else:
                                print("Debes ingresar una opcion valida.")

                        break

                    else:
                        raise ValueError()
                else:
                    print("La edad debe ser mayor a 0")
            else:
                print("Comprueba nuevamente.")

        except ValueError() as err:
            print("Algo salio mal. Razon: ", err)
        except TypeError() as err:
            print("Algo salio mal. Razon: ", err)
        except:
            print("No se puedo agregar.")


def menuBuscar():
    print("Menu de Registro Civil - Buscar por Rut\n")
    while True:
        try:
            rut = str(input("Ingrese el rut que desee buscar---> "))
            if p.validarRut(rut) == True:
                p.buscarPersonaRut(rut)
                while True:
                    print(
                        "¿Deseas seguir continuando el menu? Escribe 'Si' para continuar y 'No' para salir")
                    op = str(input("---> "))
                    op = op.lower()
                    if op == "si" or "s" and op != "":
                        imprimirMenu()
                    elif op == "no" or "n" and op != "":
                        break
                    else:
                        print("Debes ingresar una opcion valida.")
                break
            else:
                print("Comprueba nuevamente.")
        except ValueError() as err:
            print("Ha ocurriod un error. Motivo: ", err)


def menuCertificados():
    print("Menu de Registro Civil - Certificados")
    while True:
        try:
            rut = str(input("Ingrese el rut que desee buscar---> "))
            if p.validarRut(rut) == True:
                while True:
                    print("Selecciona el cetificado que desees imprimir\n")
                    print("1.- Nacimiento\n")
                    print("2.- Antecedentes\n")
                    print("3.- Ir al menu principal.")
                    op = int(input("---> "))
                    if op == 1:
                        p.imprimirCertificadoNacimiento(rut)
                        while True:
                            print("¿Deseas seguir continuando el menu? Escribe 'Si' para continuar y 'No' para salir")
                            op = str(input("---> "))
                            op = op.lower()
                            if op == "si" or "s" and op != "":
                                imprimirMenu()
                            elif op == "no" or "n" and op != "":
                                break
                            else:
                                print("Debes ingresar una opcion valida.")
                    elif op == 2:
                        p.imprimirCertificadoAntecedentes(rut)
                        while True:
                            print("¿Deseas seguir continuando el menu? Escribe 'Si' para continuar y 'No' para salir")
                            op = str(input("---> "))
                            op = op.lower()
                            if op == "si" or "s" and op != "":
                                imprimirMenu()
                            elif op == "no" or "n" and op != "":
                                break
                            else:
                                print("Debes ingresar una opcion valida.")
                    elif op == 3:
                        imprimirMenu()
                    else:
                        print("Debes escoger una opcion valida.")
                    break
            else:
                print("Comprueba nuevamente.")
        except ValueError() as err:
            print("Ocurrio un error. Motivo:", err)


imprimirMenu()
