# using class and creating an object
# passing parameters as input
class Student:
    name: str
    core: str
    cl: str
    per: float

    def registration(self, a, b, c, d):
        self.name = a
        self.core = b
        self.cl = c
        self.per = d
# print(a, b, c, d)

    @staticmethod
    def display(a, b, c, d):
        print(a, b, c, d)


S1 = Student()
S1.registration("SA ", "Chemical Engineering", "CE-3", 92.34)
S1.display("SA ", "Chemical Engineering", "CE-3", 92.34)
S2 = Student()
S2.registration("Essra ", "Computer Science Engineering", "CSE-A", 72)
S2.display("Essra ", "Computer Science Engineering", "CSE-A", 72)
