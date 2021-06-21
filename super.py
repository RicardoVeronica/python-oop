class Person:
    """ Class Person """

    def __init__(self, name, age, country):
        """ Construct method """
        self.name = name
        self.age = age
        self.country = country

    def __str__(self):
        """ String method """

        return f'{self.name} {self.age} {self.country}'


class Employee(Person):
    """ Class Employee inheritance from Person """

    def __init__(self, salary, name, age, country):
        """ Construct method """
        super().__init__(name, age, country)
        self.salary = salary

    def __str__(self):
        """ String method """
        super().__str__()

        return f'{self.name} {self.country} {self.age} {self.salary}'


setcain = Person('Set', 35, 'Mexico')
ricardo = Employee(30000, 'Ricardo', 35, 'Mexico')

print(setcain)
print(ricardo)

print(isinstance(ricardo, Person))  # Pertenece a
