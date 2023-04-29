class TypeMeta(type):
    a = None
    b = None

    def __call__(cls):
        if TypeMeta.b == None:
            TypeMeta.b = 1
            TypeMeta.a = MyClass()
        return TypeMeta.a


class MyClass(metaclass=TypeMeta):
    def metod(self):
        pass

    def metod2(self):
        pass


Obj1 = MyClass()
Obj2 = MyClass()
print(Obj1 is Obj2)
