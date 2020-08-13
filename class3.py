class Employee:
    no_of_leaves = 8 
    
    # def printdetails(self):
    #     return f"the name is {self.name} salery is {self.salery} "
    
    # def __init__(self ,name ,salery):
    #     self.name = name
    #     self.salery = salery
        
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves
        

harshit = Employee()
harshit.change_leaves(34)

print(harshit.no_of_leaves)

