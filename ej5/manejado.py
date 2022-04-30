import csv
from plandeahorro import plandeahorro
class manejador:
    __lista=[]
    def __init__(self):
        self.__lista=[]
        pass
    def Cargar(self):
        archivo=open('planes.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            if fila[3].isdecimal() and fila[4].isdecimal() and fila[5].isdecimal():
                plan=plandeahorro(int(fila[0]),fila[1],fila[2],int (fila[3]))
                self.__lista.append(plan)
                plandeahorro.setcuotas(int(fila[4]))
                plandeahorro.setcuotasl(int(fila[5]))
        return
    def setvalorV(self):
        for plan in self.__lista:
            print(plan)
            valor=(input('ingrese el valor de un vehiculo: '))
            control=plan.valorv(valor)
            while not control:
                valor=(input('el valor ingresado es erroneo ingrese uno nuevo: '))
                control=plan.valorv(valor)
        return
    def buscarcuotas(self,valor):
        for plan in self.__lista:
            if valor > plan.getvalorcuota():
                print(plan)
        

    def mostartLicitacion(self,codigo):
        indice = self.buscarPlanPorCodigo(codigo)
        if indice != -1:
            unPlan = self.__lista[indice]
        else:
            unPlan = None
            print("[ERROR] No hay un vehiculo con el codigo {0}".format(codigo))
        return plandeahorro.getcuotasl() * unPlan.getvalorcuota()

    def buscarPlanPorCodigo(self, codigo):
        i = 0
        while i < len(self.__lista) and self.__lista[i].getCodigoPlan() != codigo:
            i += 1
        if i == len(self.__lista):
            i = -1
        return i
    def cambiarcuotasl(self,valor):
        plandeahorro.setcuotasl(valor)
        
