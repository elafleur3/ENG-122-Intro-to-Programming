from stack import stack

class stackcalc(stack):
    def __init__(self):
        super().__init__()
    def add(self):
        if self.size()>1:
            x= self.pop()
            y= self.pop()
            self.push(y+x)
            print(x+y)
        else:
            print("Not enough values")
    def subtract(self):
        if self.size()>1:
            x= self.pop()
            y= self.pop()
            self.push(y-x)
        else:
            print("Not enough values")
    def multiply(self):
        if self.size()>1:
            x= self.pop()
            y= self.pop()
            self.push(x*y)
        else:
            print("Not enough values")
    def add(self):
        if self.size()>1:
            x= self.pop()
            y= self.pop()
            self.push(y/x)
        else:
            print("Not enough values")
