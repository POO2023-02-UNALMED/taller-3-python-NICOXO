class Control:
    def __init__(self):
        self._tv = None

    def set_tv(self, tv):
        self._tv = tv

    def get_tv(self):
        return self._tv

    def turnOn(self):
        if self._tv:
            self._tv.turnOn()

    def turnOff(self):
        if self._tv:
            self._tv.turnOff()

    def canalUp(self):
        if self._tv:
            self._tv.canalUp()

    def canalDown(self):
        if self._tv:
            self._tv.canalDown()

    def volumenUp(self):
        if self._tv:
            self._tv.volumenUp()

    def volumenDown(self):
        if self._tv:
            self._tv.volumenDown()

    def setCanal(self, canal):
        if self._tv:
            self._tv.set_canal(canal)

    def setVolumen(self, volumen):
        if self._tv:
            self._tv.set_volumen(volumen)