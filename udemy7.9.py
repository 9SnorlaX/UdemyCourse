#HomeWork 2
class Calculator:
    #def calc(self, a, b):
        #self.a = a
        #self.b = b

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return max(a, b) - min(a, b)

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a/b

calculator = Calculator()

print(calculator.add(10, 5))
print(calculator.subtract(10, 90))
print(calculator.multiply(10, 5))
print(calculator.divide(10, 5))
