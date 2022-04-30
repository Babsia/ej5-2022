from manejado import manejador
class menuu:
    __switcher=None
    __M=None

    def __init__(self):
        self.__switcher = { 
            'a':self.opcion1,
            'b':self.opcion2,
            'c':self.opcion3,
            'd':self.opcion4,
            'e':self.salir
            }
        self.__M=manejador()
        self.__M.Cargar()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Salir')

    def opcion1(self):
        print("opcion a")
        self.__M.setvalorV()
        
    def opcion2(self):
        print("opcion b")
        valor=int(input("ingrese el valor de cuota para verificar cuotas menores: "))
        self.__M.buscarcuotas(valor)
        
        
    def opcion3(self):
        print("C")
        codigo=int(input("ingrese un codigo de vehiculo"))
        print("el monto a pagar para licitar es: {}".format(self.__M.mostartLicitacion(codigo)))
    def opcion4(self):
        print ('opcion d')
        valor=int(input("ingrese valor de cuotas a licitar para modificar"))
        self.__M.cambiarcuotasl(valor)
        
    

        
