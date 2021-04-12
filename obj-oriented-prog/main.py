"""
Define your Salary class and Promotable class so that the Employee class objects may work like this:
rolf = Employee(15.0)
print(rolf.weekly_salary())     # --> prints out rolf's weekly salary (15.0 * 40 = 600.0)
rolf.promote(5.0)       # rolf's hourly salary (rate) increases by 5.0 (15.0 + 5.0 = 20.0)
print(rolf.weekly_salary())     # --> prints 800.0  (20.0 * 40 = 800.0)
"""


class Salary:
    # define Salary class and associated methods here
    def __init__(self, rate):
        self.rate = rate

    def calculate(self, hours):
        return self.rate * hours

    def rate(self):
        return self.rate


# interesante como dentro de esta clase se pueden modificar atributos no definidos aquí
# originalmente, lo que muestra que un objeto es transversal a las clases en Python
# El concepto de encapsulamiento no se cumple.
class Promotable:
    # define Promotable class and associated methods here
    def promote(self, increase):
        self.rate += increase


# Do NOT change the code below:
class Employee(Salary, Promotable):
    def __init__(self, rate: float):
        self.rate = rate

    def weekly_salary(self) -> float:
        return self.calculate(40)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rolf = Employee(15.0)
    print(rolf.weekly_salary())  # --> prints out rolf's weekly salary (15.0 * 40 = 600.0)
    rolf.promote(5.0)  # rolf's hourly salary (rate) increases by 5.0 (15.0 + 5.0 = 20.0)
    print(rolf.weekly_salary())  # --> prints 800.0  (20.0 * 40 = 800.0)
