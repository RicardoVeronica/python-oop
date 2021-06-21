# superclass - clase padre
# subclass - clase que hereda, al mismo tiempo se hace superclass

class Vehicle:
    """ Class Vehicle """

    def __init__(self, brand, model):
        """ Construct method """
        self.brand = brand
        self.model = model
        self.go = False
        self.go_faster = False
        self.stop = False

    def on(self):
        """ Method of class """
        self.go = True

    def speed_up(self):
        """ Method of class """
        self.go_faster = True

    def brake(self):
        """ Method of class """
        self.stop = True

    def state(self):
        """ Simulate String method """

        print(f'Marca: {self.brand}\nModelo: {self.model}\neverything ok')


class Motorcycle(Vehicle):
    """ Class Motorcycle single inheritance from Vehicle """
    caballito = False

    def funcion_caballito(self):
        """ Class method """
        caballito = True

        return caballito


my_motorcycle = Motorcycle('Kawasaki', 'Ninja')

my_motorcycle.state()
print(my_motorcycle.caballito)
print(my_motorcycle.funcion_caballito())
