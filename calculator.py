class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2


    def Addition(self):
        return self.num1 + self.num2
    
    def Subtration(self):
        return self.num1 - self.num2
    
    def Multiplication(self):
        return self.num1 * self.num2
    
    def Division(self):
        if (self.num2 == 0):
            print("Second number cant be a 0")
        else:
            return self.num1 / self.num2
            
    def Modulo(self):
        return self.num1 % self.num2
    
