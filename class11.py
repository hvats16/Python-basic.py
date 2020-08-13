class A:
    classvar1 = "HEy there i am harshit rajput"
    def __init__(self):
        self.var = "i am inside class A's constructor"
        self.classvar1= "Instance var in class A"
        self.special = "special"
        
class B(A):
    
    classvar1 = "I am in class B"
    
    def __init__(self):
        super().__init__()
        self.var = "i am inside class b's constructor"
        self.classvar1= "Instance var in class B"
    
    
a = A()
b = B()


print(b.special)