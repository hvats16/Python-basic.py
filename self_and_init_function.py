
class Employee:
    no_of_leaves = 8 
    
    def printdetails(self):
        return f"the name is {self.name} salery is {self.salery} "
    
    def __init__(self ,name ,salery):
        self.name = name
        self.salery = salery

harshit = Employee("Harshit",40000)

rohan = Employee("Rohan", 400000)

# harshit.name = 'Harshit'
# rohan.name = "Rohan"

# harshit.salery = 4000000
# rohan.salery = 4000000

print(rohan.printdetails())
print(harshit.printdetails())