def Datos():
    """Función para solicitar los datos del usuario"""

    
    print("""-----------------------------------------------------------------------------------------------------------
|                                        CALCULADORA DE AGUINALDO                                         |
-----------------------------------------------------------------------------------------------------------\n""")

    nombre = input("Ingrese su nombre completo: ")

    #----DUI----
    dui = input("Ingrese su número de DUI (SIN GUIONES): ")

    #Verifica que el DUI tenga una longitud válida
    while(len(dui) != 9):
        print("¡El número de DUI no es válido!")
        dui = input("Ingrese nuevamente su número de DUI (SIN GUIONES): ")

    #Lambda que nos permite dar formato al número del DUI
    dui_real = lambda dui: dui[:-1] + "-" + dui[-1]

    #----NIT----
    nit = input("Ingrese su número de NIT (SIN GUIONES): ")

    #Verifica que el NIT tenga una longitud válida
    while(len(nit) != 14):
        print("¡El número de NIT no es válido!")
        nit = input("Ingrese nuevamente su número de NIT (SIN GUIONES): ")

    #Lambda que nos permite dar formato al número del NIT
    nit_real = lambda nit: nit[:4] + "-" + nit[4:10] + "-" + nit[10:13] + "-" + nit[-1] #lambda que nos permite dar formato al número del NIT

    salario = float(input("Ingrese su sueldo: $"))
    tiempo = int(input("Ingrese el número de meses trabajados: "))

    return nombre, dui, dui_real, nit, nit_real, salario, tiempo #Devuelve las variables a utilizar
