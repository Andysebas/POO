from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

        
    @abstractclassmethod
    def hacer_actividad(self):
            pass

    def presentarse(self):
            print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")


class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")


class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de: {self.actividad}")



Andy = Estudiante("Andy", 21, "No binario", "programacion")
dalto = Trabajador("Lucas", 21, "Masculino", "programacion")

dalto.hacer_actividad()
Andy.presentarse()
Andy.hacer_actividad()
