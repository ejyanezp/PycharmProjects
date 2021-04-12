class Addition:
    @classmethod
    def add(cls, num1, num2):
        return num1 + num2


class Calculator:

    # a sample add() method in our calculator is shown below
    # you may learn from it and implement the other methods
    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)  # make use of add() from addition module

    # implement a class method `subtract()` that takes in num1 and num2 and return num1 - num2
    # your `subtract()` method cannot use the + - * / calculation operators, but can use - as a negative sign operator
    @classmethod
    def subtract(cls, num1, num2):
        return Addition.add(num1, -num2)  # make use of add() from addition module

    # implement a class method `multiply()` that takes in num1 and num2 and return num1 * num2
    # your `multiply()` method cannot use the + - * / calculation operators, but can use - as a negative sign operator
    # you may assume num1 and num2 are always non-negative integers
    @classmethod
    def multiply(cls, num1, num2):
        result = 0
        while num2 > 0:
            # result += num1
            result = Addition.add(result, num1)
            # num2 -= 1
            num2 = Addition.add(num2, -1)
        return result

    # implement a class method `divide()` that takes in num1 and num2 and return num1 // num2
    # your `divide()` method cannot use the + - * / calculation operators, but can use - as a negative sign operator
    # you may assume num1 is always a non-negative integer, and num2 is always a positive integer
    @classmethod
    def divide(cls, num1, num2):
        result = 0
        while num1 > 0:
            # num1 -= num2
            num1 = Addition.add(num1, -num2)
            # result += 1
            result = Addition.add(result, 1)
        return result


print(Calculator.multiply(5, 6))
print(Calculator.divide(30, 5))
