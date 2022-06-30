import sys
from itertools import cycle


class Persona:

    def __init__(self):
        self.rut = ""
        self.nombre = ""
        self.edad = 0
        self.fechaNacimiento = ""
        self.estadoCivil = ""
        self.dictPersona = {}
        self.dictPersonas = {"Pedro Rio": {"rut": "1835245-6", "nombre": "Pedro Rio", "edad": 54, "fecha_nacimiento": "18/09/1958", "estado_civil": "Casado"},
                             "Ana Lizana": {"rut": "15854325-7", "nombre": "Ana Lizana", "edad": 48, "fecha_nacimiento": "25/04/1989", "estado_civil": "Casada"},
                             "Matias Lesquia": {"rut": "19547832-0", "nombre": "Matias Lesquia", "edad": 22, "fecha_nacimiento": "30/07/1998", "estado_civil": "Soltero"}}

    def setPersona(self, rut, nombre, edad, fecha, estado):
        self.rut = rut
        self.nombre = nombre
        self.edad = edad
        self.fechaNacimiento = fecha
        self.estadoCivil = estado
        self.dictPersonas.update({self.nombre: {"rut": rut, "nombre": nombre,
                                                "edad": edad, "fecha_nacimiento": fecha, "estado_civil": estado}})

    def setDictPersonas(self, dict):
        self.dictPersonas = dict

    def getDictPersonas(self):
        return self.dictPersonas

    def getDictPersona(self):
        return self.dictPersona

    def searchDict(self):
        try:
            cont = 0
            l = self.getDictPersonas()
            auxDict = self.getDictPersona()
            if auxDict != {}:
                l.update(auxDict)
            print("\nListas disponibles:\n")
            for i in l:
                cont += 1
                print(cont, ".- ", i, "--> ", l[i])
            print("\n")
        except TypeError as err:
            print("Ocurrió un problema. Motivo: ", err)

    def validarRut(self, rut):
        rut = rut.upper()
        rut = rut.replace("-", "")
        rut = rut.replace(".", "")
        aux = rut[:-1]
        dv = rut[-1:]

        revertido = map(int, reversed(str(aux)))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(revertido, factors))
        res = (-s) % 11

        if str(res) == dv:
            return True
        elif dv == "K" and res == 10:
            return True
        else:
            print("Rut inválido")
            return False

    def crearNuevaPersona(self, rut, nombre, edad, fecha, estado):
        try:
            if self.validarRut(rut) == True:
                self.setPersona(rut, nombre, edad, fecha, estado)
                print("¡Agregado con exito!")
                return True
            else:
                print("No se pudo crear el nuevo registro.")
                return False
        except ValueError as err:
            print("[Modulo Persona]. Error: ", err)
            return False
        except TypeError as err:
            print("[Modulo Persona]. Error: ", err)
            return False

    def buscarPersonaRut(self, rut):
        try:
            l = self.getDictPersonas()
            print("\nBusqueda por rut :", rut, "\n")
            for i in l.values():
                if rut == i["rut"]:
                    print("Resultado:\n",
                          "Nombre:\t\t", i["nombre"], "\n",
                          "Rut:\t\t\t", i["rut"], "\n",
                          "Edad:\t\t\t", i["edad"], "\n",
                          "Fecha de nacimiento:\t", i["fecha_nacimiento"], "\n",
                          "Estado civil:\t\t", i["estado_civil"])
                    break
            print("\n")
        except TypeError as err:
            print("Ocurrió un problema. Motivo: ", err)

    def imprimirCertificadoNacimiento(self, rut):
        try:
            l = self.getDictPersonas()
            print("\nCertificado de Nacimiento: ", rut, "\n")
            for i in l.values():
                if rut == i["rut"]:
                    print("Resultado:\n",
                        "Nombre:\t\t", i["nombre"], "\n",
                        "Rut:\t\t\t", i["rut"], "\n",
                        "Fecha de nacimiento:\t", i["fecha_nacimiento"], "\n")
                    break
            print("\n")
        except TypeError as err:
            print("Ocurrió un problema. Motivo: ", err)

    def imprimirCertificadoAntecedentes(self, rut):
        try:
            l = self.getDictPersonas()
            print("\nCertificado de Antecedentes: ", rut, "\n")
            for i in l.values():
                if rut == i["rut"]:
                    print("Resultado:\n",
                          "Nombre:\t\t", i["nombre"], "\n",
                          "Rut:\t\t\t", i["rut"], "\n",
                          "Edad:\t\t\t", i["edad"], "\n",
                          "Estado civil:\t\t", i["estado_civil"])
                    break
            print("\n")
        except TypeError as err:
            print("Ocurrió un problema. Motivo: ", err)
