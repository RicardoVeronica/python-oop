class Auto:
    """ Class Auto """

    def move(self):
        """ Class method """

        print('Move by 4 wheels')


class Motorcycle:
    """ Class Motorcycle """

    def move(self):
        """ Class method """

        print('Move by 2 wheels')


class Truck:
    """ Class Truck """

    def move(self):
        """ Class method """

        print('Move by 18 wheels')


def vehicle_move(obj):
    """ Polimorfism """
    obj.move()


my_moto = Motorcycle()
vehicle_move(my_moto)

my_truck = Truck()
vehicle_move(my_truck)

my_auto = Auto()
vehicle_move(my_auto)
