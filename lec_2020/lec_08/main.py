import itertools


class User:
    class_counter = 0

    def __init__(self, firstname: str, lastname: str, sex: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.sex = sex
        self.age = age
        self.id = User.class_counter
        User.class_counter += 1

    def print_all_info(self):
        print('ID: ' + str(self.id))
        print('Name: ' + self.firstname)
        print('Surname: ' + self.lastname)
        print('Sex: ' + self.sex)
        print('Age: ' + str(self.age))


user1 = User('Anatoliy', 'Kulishov', 'Male', 21)
user2 = User('Sergey', 'Kulishov', 'Male', 25)
user3 = User('Name', 'Surname', 'Sex', 0)
user1.print_all_info()
user2.print_all_info()
user3.print_all_info()