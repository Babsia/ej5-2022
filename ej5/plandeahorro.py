


class plandeahorro:
    __code=''
    __mod=''
    __ver=''
    __valor=0
    __cuotas=1
    __cuotasl=1
    #metodos de instancia
    def __init__(self,code,mod,ver,valor):
        self.__code=code
        self.__mod=mod
        self.__ver=ver
        self.__valor=valor
        pass
    def __str__(self):
        return "Codigo del plan: {0}\nModelo del vehiculo: {1}\nVersion del vehiculo: {2}\n".format(self.getCodigoPlan(), self.getModelo(), self.getVersion())
   
    def  getCodigoPlan(self):
        return self.__code
    def getModelo(self):
        return self.__mod
    def getVersion(self):
        return self.__ver
    def getvalor(self):
        return self.__valor
    def valorv(self,valor):
        bandera=False
        if str.isdigit(valor):
            self.__valor=valor
            bandera=True
        return bandera
    def getvalorcuota(self):
        #valor cuota = (importe vehículo/ cantidad de cuotas) + importe vehículo * 0.10 47816,66
        valor=((self.getvalor()/self.getcuotas()) + self.getvalor() * 0.1)
        return valor




    #metodos de clase
    @classmethod
    def setcuotas(cls,valor):
        cls.__cuotas=valor
        return
    @classmethod
    def setcuotasl(cls,valor):
        cls.__cuotasl=valor
        return
    @classmethod
    def getcuotas(cls):
        return(cls.__cuotas)
    @classmethod
    def getcuotasl(cls):
        return (cls.__cuotasl)


