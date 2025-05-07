class number_group():
    def __init__(self):
        self.number1 = 1
        self.number2 = 2
        self.number3 = 3
        self.number4 = 4
        self.number5 = 5

    def square(self):
        message = "The squares of the numbers are: "
        message += str(self.number1**2)+" "
        message += str(self.number2**2)+" "
        message += str(self.number3**2)+" "
        message += str(self.number4**2)+" "
        message += str(self.number5**2)+" "
        return message
    
    def cube(self):
        message = "The cubes of the numbers are: "
        message += str(self.number1**3)+" "
        message += str(self.number2**3)+" "
        message += str(self.number3**3)+" "
        message += str(self.number4**3)+" "
        message += str(self.number5**3)+" "
        return message
    
mynumbers = number_group()
print(mynumbers.square())
print(mynumbers.cube())