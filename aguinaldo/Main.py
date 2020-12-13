from os import system, name #Nos permitirá limpiar la pantalla en un futuro
from Calculo import * #Importamos nuestra clase Calculo
from Datos import * #Importamos el módulo Datos

#Función para limpiar la pantalla
def limpiar():
    """Limpia la pantalla de la terminal"""
    if name == 'nt': #Evalúa si se encuentra en un sistema operativo Windows
        _ = system('cls')
    else: #Si se encuentra en Mac o Linux
        _ = system('clear')

#Declaración de variables
nombre, dui, dui_real, nit, nit_real, salario, tiempo = Datos() 

limpiar() #Nos permite limpiar la terminal. Se utiliza para presentar de manera ordenada los datos.

#Instancia de clase Calculo
mi_aguinaldo = Calculo(nombre,str(dui_real(dui)),str(nit_real(nit)),salario, tiempo) 
mi_aguinaldo.calcular() #Calcula el aguinaldo
mi_aguinaldo.imprimir() #Imprime los resultados

#Si se abre desde el ejecutable, evita que se cierre sin haber mostrado resultados
input("\n\n\nFIN DE LA EJECUCION -- Presione cualquier tecla para salir")
