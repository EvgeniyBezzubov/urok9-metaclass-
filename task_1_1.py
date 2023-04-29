class workervalidator:
    def __init__(self, my_atr):
        self.my_atr = my_atr

    def __set__(self, instanse, value):
        if type(value) != str:
            raise ValueError("{0} должно быть строкой!  ".format(instanse.__dict__.keys()) + str(value))

        if len(str(value)) > 10:
            print("слишком большая длинна, максимум :5 символов, твоё значение" + str(value))
            value = input("введи новое значение: ")
        print(value.isdigit())
        for i in value:
            if i.isdigit()== True:
                raise ValueError("В ФИО не может быть букв, твоё значение : ".format(instanse.__dict__.keys()) + str(value))

        instanse.__dict__[self.my_atr] = value


class Worker:

    name = workervalidator("name")


    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 80000, "bonus": 8000}


class Position(Worker):


    def get_full_name(self):
        #  print(self.name +" " + self.surname)
        get_full_name_otvet = self.name + " " + self.surname
        return get_full_name_otvet

    def get_total_income(self):
        # print(self._income.get("wage") + self._income.get("bonus"))
        get_total_income_otvet = self._income.get("wage") + self._income.get("bonus")
        return get_total_income_otvet

    def __str__(self):
        otvet = str(obj1.get_full_name()) + "  " + str(obj1.get_total_income())
        return otvet


obj1 = Position("Evgeniy", "Bezzubov", "admin")
print(obj1)