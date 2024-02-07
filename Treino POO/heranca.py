class Carro:
    numero_rodas = 4
    quantidade_passageiros = 5

    def acelerar(self):
        print("Acelerando...")

    def frear(self):
        print("Freando...")

    def buzinar(self):
        print("Buzinando...")


class Uno(Carro):
    modelo = "Uno"
    marca = "Fiat"
    ano = 1992


uno = Uno()
uno.acelerar()
uno.frear()
uno.buzinar()
print(uno.numero_rodas)
print(uno.quantidade_passageiros)
print(uno.modelo)
print(uno.marca)
print(uno.ano)
