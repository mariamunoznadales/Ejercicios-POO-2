class A:
    def __init__(self, a):
        self.a = a


class B(A):
    def __init__(self, b):
        super().__init__(b)
        self.b = b


class C(A):
    def __init__(self, c):
        super().__init__(c)
        self.c = c


class D(B, C):
    def __init__(self, a, b, c):
        A.__init__(self, a)  # Inicializa el atributo 'a' de la clase A
        B.__init__(self, b)  # Inicializa el atributo 'b' de la clase B
        C.__init__(self, c)  # Inicializa el atributo 'c' de la clase C


# Ejemplo
d = D(1, 2, 3)
print(isinstance(d, A), isinstance(d, B), isinstance(d, C))  # True True True
print(d.a, d.b, d.c)  # 1 2 3
