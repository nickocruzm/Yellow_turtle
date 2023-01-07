class A:
    def __init__(self):
        self.x = 1
    
    def f(self):
       print ('f called, ', self.x + 1)
    
    def g(self):
        print('g called, ',  self.x * 5)
    
    def evaluate(self, usr_choice):
        
        
    
    
a = A()

a.evaluate('g')