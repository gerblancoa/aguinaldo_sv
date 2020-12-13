class Calculo():
    """Clase calculo, contiene los datos generales y realiza el cálculo de aguinaldo"""

    #Constructor
    def __init__(self, nombre, dui, nit,salario,tiempo):
        self.nombre = nombre
        self.dui = dui
        self.nit = nit
        self.salario = salario
        self.tiempo = tiempo
        self.aguinaldo = 0

    #Calcula el aguinaldo
    def calcular(self):
        if self.tiempo >= 12 and self.tiempo < 36:
            self.aguinaldo = (self.salario/30)*15
        elif self.tiempo >= 36 and self.tiempo <120:
            self.aguinaldo = (self.salario/30)*19
        elif self.tiempo >= 120:
            self.aguinaldo = (self.salario/30)*21
        else:
            self.aguinaldo = (((self.salario/30)*15)/365 * 30*self.tiempo)
 
    #Imprime los resultados
    def imprimir(self):
        print("""|---------------------------------------------------------------------------------------------------------|
|                                                RESULTADOS                                               |
|---------------------------------------------------------------------------------------------------------|\n""")
        print("Nombre: " + self.nombre.title() + "\nDUI: " + self.dui + "\nNIT: " + self.nit)
        print("Tiempo laborado: " + str(self.tiempo) + " meses ("+ str(round(self.tiempo/12,2)) +" años)\nSalario: $" + str(self.salario))
        print("""\n|---------------------------------------------------------------------------------------------------------|
|---------------------------------------------------------------------------------------------------------|\n""")
        print("El aguinaldo a recibir es de: $" + str(round(self.aguinaldo,3)))

