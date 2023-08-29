class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self.__marca = marca
        self.__canal = 1
        self.__precio = 500
        self.__estado = estado
        self.__volumen = 1
        self.__control = None
        TV.numTV += 1

    def setPrecio(self, precio):
        if self.__estado:
            self.__precio = precio

    @classmethod
    def setNumTV(cls, num):
        cls.numTV = num


    def getMarca(self):
        return self.__marca

    def getCanal(self):
        return self.__canal

    def setCanal(self, canal):
        if self.__estado and 1 <= canal <= 120:
            self.__canal = canal

    def getPrecio(self):
        return self.__precio

    def getEstado(self):
        return self.__estado

    def getVolumen(self):
        return self.__volumen

    def setVolumen(self, volumen):
        if self.__estado and 0 <= volumen <= 7:
            self.__volumen = volumen

    def setControl(self, control):
        self.__control = control

    def turnOn(self):
        self.__estado = True

    def turnOff(self):
        self.__estado = False

    def canalUp(self):
        if self.__estado:
            self.__canal = min(self.__canal + 1, 120)

    def canalDown(self):
        if self.__estado:
            self.__canal = max(self.__canal - 1, 1)

    def volumenUp(self):
        if self.__estado:
            self.__volumen = min(self.__volumen + 1, 7)

    def volumenDown(self):
        if self.__estado:
            self.__volumen = max(self.__volumen - 1, 0)

    def getControl(self):
        return self.__control