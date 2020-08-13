
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

harshit = Employee("Harshit",40000)

rohan = Employee("Rohan", 400000)

sahil = Employee.from_string("Sahil-400000")


print(rohan.printdetails())
print(harshit.printdetails())
print(sahil.salery)
