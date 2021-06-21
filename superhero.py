class SuperHero():  # class
    """ Create a super hero """

    def __init__(self, name, age, team):
        """ Construct __init__ method """
        self.name = name
        self.age = age
        self.__team = 'X-MEN'  # encapsulation, example: __foo

    def __str__(self):
        """ Rewrite __str__ method """
        return f'Super Hero name: {self.name}, Super Hero team: {self.__team}'

    def __len__(self):
        """ Rewrite length method """
        return self.age

    @staticmethod
    def message():
        return 'WELCOME TO OUR ORGANIZATION'


# instances (objects)
print('-------- Wolverine -------')
wolverine = SuperHero('Logan', 135, 'Justice Leage')  # encapsulation
print(f'Super hero {str(wolverine)}')
print(f'Super hero age: {len(wolverine)}')

print('-------- Cyclops -------')
cyclops = SuperHero('Ryan', 32, 'Avengers')  # encapsulation
print(f'Super hero {str(cyclops)}')
print(f'Super hero age: {len(cyclops)}')

print('----- Static method -----')
print(SuperHero.message())
