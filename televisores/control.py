class Control:
    def __init__(self):
        self._tv = None

    def turn_on(self):
        if self._tv:
            self._tv.turn_on()

    def turn_off(self):
        if self._tv:
            self._tv.turn_off()

    def canal_up(self):
        if self._tv:
            self._tv.canal_up()

    def canal_down(self):
        if self._tv:
            self._tv.canal_down()

    def volumen_up(self):
        if self._tv:
            self._tv.volumen_up()

    def volumen_down(self):
        if self._tv:
            self._tv.volumen_down()

    def set_canal(self, canal):
        if self._tv:
            self._tv.set_canal(canal)

    def set_volumen(self, volumen):
        if self._tv:
            self._tv.set_volumen(volumen)

    def enlazar(self, tv):
        self._tv = tv
        tv.set_control(self)

    def get_tv(self):
        return self._tv

    def set_tv(self, tv):
        self._tv = tv