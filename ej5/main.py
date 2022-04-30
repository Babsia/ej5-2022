from menu import menuu

if __name__=='__main__':
    bandera = False
    m=menuu()
    while not bandera:
        print("")
        print("a actualizar valor de vehiculo ")
        print("b buscar cuotas inferiores a un valor dado ")
        print("c mostrar monto que se pago para licitar ")
        print("d modificar cuotas a licitar")
        print("e para salir")
        opcion= input("Ingrese una opción: ")
        m.opcion(opcion)
        bandera =(opcion)=='e'

