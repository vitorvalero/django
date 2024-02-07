class Forma:
    def area(self):
        pass


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado**2


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio**2)


quadrado = Quadrado(4)
print(quadrado.area())

circulo = Circulo(4)
print(circulo.area())
