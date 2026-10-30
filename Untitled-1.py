#un crematorio requiere un sistema para gestionar los pacientes que fallecieron y llegaron al crematorio
#opcion 1: un registro en una lista donde pueden ingresar maximo 5 ingresos al horno como tope, nombre completo en minusculas
        #  solo se pueden quemar edades mayor o igual a 3 
#opcion 2: Registro de insumos que se nececitan para cremar a una persona (maximo 15 en formato lista)
#regla 1: cada integrante del grupo tiene su propia rama 
#regla 2: cada integrante va a tener su repositorio
#regla 3: deben usar la misma estructura en terminos de variable, indentacion etc#


def menu():
    print(" === MENÚ CREMATORIO === ")
    print("1. Registrar pacientes")
    print("2. Registrar insumos")
    print("3. Ver pacientes")
    print("4. Salir")


def solicitar_opcion():
    opcion = 0

    while opcion < 1 or opcion > 4:
        try:
            opcion = int(input("Ingrese una opcion: "))

            if opcion < 1 or opcion > 4:
                print("Error, ingrese una opcion valida")

        except ValueError:
            print("Error, ingrese un numero valido")

    return opcion


def registro_pacientes(pacientes):

    try:
        cant_registros = int(input("Cantidad de pacientes (maximo 5): "))

        if cant_registros < 1 or cant_registros > 5:
            print("Error, cantidad no admitida")
            return

    except ValueError:
        print("Error, ingrese un numero valido")
        return

    for i in range(cant_registros):

        try:
            edad = int(input("Ingrese la edad del paciente: "))

            if edad >= 3:
                nombre = input("Ingrese nombre del paciente: ")

                if nombre.strip() != "":
                    pacientes.append(nombre)
                    print("Paciente registrado")
                else:
                    print("Registro fallido")

            else:
                print("Edad no admitida")

        except ValueError:
            print("Error, ingrese una edad valida")


def registro_insumos(insumos):

    try:
        cant_insumos = int(input("Cantidad de insumos (maximo 15): "))

        if cant_insumos < 1 or cant_insumos > 15:
            print("Error, cantidad no admitida")
            return

    except ValueError:
        print("Error, ingrese un numero valido")
        return

    for i in range(cant_insumos):

        nombre = input("Ingrese el nombre del insumo: ")

        if nombre.strip() != "":
            insumos.append(nombre)
            print("Insumo registrado")
        else:
            print("Registro fallido")

pacientes = []
insumos = []

while True:

    menu()
    opcion = solicitar_opcion()

    match opcion:

        case 1:
            registro_pacientes(pacientes)

        case 2:
            registro_insumos(insumos)

        case 3:
            print("Lista de pacientes:")
            print(pacientes)

        case 4:
            print("Saliendo...")
            break


