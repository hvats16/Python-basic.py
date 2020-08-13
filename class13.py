
class Employee:
    no_of_leaves = 8 
    
    def printdetails(self):
        return f"the name is {self.name} salery is {self.salery} "
    
    def __init__(self ,name ,salery):
        self.name = name
        self.salery = salery
        
    @classmethod
    def from_string(cls, string):
        # params =string.split("-")
        # # print(params)
        # return cls(params[0],params[1])
        return cls(*string.split("-"))
    
    
    def __add__(self):
        return self.name + others.name 
    
    def __repr__(self):
        return f" Employee '{self.name}' ,'{self.salery}'"
    
    def __str__(self):
        return f"the name is {self.name} salery is {self.salery} "
    
    
    
harshit = Employee("Harshit",40000)

# rohan = Employee("Rohan", 400000)




# print(rohan.printdetails())
# print(harshit.printdetails())

print(harshit)

