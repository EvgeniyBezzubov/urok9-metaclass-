class roadValidator:
    def __init__(self, my_atr):
        self.my_atr = my_atr

    def __set__(self, instanse, value):
        if type(value) != int:
            raise ValueError("{0} не может быть строкой  ".format(instanse.__dict__.keys()) + str(value))

        if value < 0:
            raise ValueError("{0} не может быть меньше 0".format(instanse.__dict__.keys()) + str(value))

        if len(str(value)) > 5:
            print("слишком большая длинна, максимум :99999, твоё значение" + str(value))
            value = int(input("введи новое значение: "))
        instanse.__dict__[self.my_atr] = value


class road:
    thickness = 0.05
    mass = 25
    _lenght = roadValidator("_lenght")
    _width = roadValidator("_width")

    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def asphalt_mass(self):
        return self._lenght * self._width * self.mass * self.thickness


obj1 = road(12, 99999999999)
