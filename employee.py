class Employee:
    """ Class Employee """

    def employee_details(self):
        """ Simulate construct method """
        self.name = 'Richard'

    @staticmethod
    def welcome_message():
        """ Static method, return message """

        print('Welcome to our organization')

    @classmethod  # ?
    def test(cls, name):
        """ Class method """

        print(f'This is a class method {name}')


employee_one = Employee()
employee_one.employee_details()
print(employee_one.name)

Employee.welcome_message()  # static method
employee_one.test('Rick')  # class method
