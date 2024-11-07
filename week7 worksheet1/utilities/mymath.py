import greetings

class Calc:
    def __init__(self, add, sub):
        self.add = add
        self.sub = sub
        def add(num1, num2):
            return num1 + num2
        def sub(num1, num2):
            return num1 - num2

greetings.say_hello()