class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        TV.numTV += 1

    def set_marca(self, marca):
        self._marca = marca

    def get_marca(self):
        return self._marca

    def set_canal(self, canal):
        if self._estado and 1 <= canal <= 120:
            self._canal = canal

    def get_canal(self):
        return self._canal

    def set_precio(self, precio):
        self._precio = precio

    def get_precio(self):
        return self._precio

    def set_volumen(self, volumen):
        if self._estado and 0 <= volumen <= 7:
            self._volumen = volumen

    def get_volumen(self):
        return self._volumen

    def set_control(self, control):
        self._control = control

    def turn_on(self):
        self._estado = True

    def turn_off(self):
        self._estado = False

    def get_estado(self):
        return self._estado

    def canal_up(self):
        if self._estado:
            self._canal = min(120, self._canal + 1)

    def canal_down(self):
        if self._estado:
            self._canal = max(1, self._canal - 1)

    def volumen_up(self):
        if self._estado:
            self._volumen = min(7, self._volumen + 1)

    def volumen_down(self):
        if self._estado:
            self._volumen = max(0, self._volumen - 1)