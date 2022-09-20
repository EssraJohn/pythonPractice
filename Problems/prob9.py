# using class and object
# noinspection SpellCheckingInspection
class Student:
    name: str
    rollno: str
    per: float
# default values

    def __init__(self):
        self.name = "Essra"
        self.rollno = "19P81A0528"
        self.per = 69.5

    def registration(self):
        self.name = input("Enter your name:")
        self.rollno = input("Enter your roll-No:")
        self.per = float(input("Enter your percentage:"))

    def display(self):
        print("Your name is {}".format(self.name))
        print("Your roll-no is {}".format(self.rollno))
        print("Your percentage is {}".format(self.per))


S1 = Student()
S1.display()    # used to display initial values
S1.registration()
S1.display()
