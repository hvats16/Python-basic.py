
class Employee:
    no_of_leaves = 8 
    
    def printdetails(self):
        return f"the name is {self.name} salery is {self.salery} "
    
    def __init__(self ,name ,salery):
        self.name = name
        self.salery = salery
        
    # @classmethod
    # def from_string(cls, string):
    #     # params =string.split("-")
    #     # # print(params)
    #     # return cls(params[0],params[1])
    #     return cls(*string.split("-"))
    
class Player:
    no_of_leaves = 4 
    def __init__(self,name,game):
        self.name = name
        self.game = game
    
    def print_details(self):
        return f"The name is {self.name} and the game is {self.game}"  
    
    
class CoolProgrammer( Player, Employee):
    # no_of_leaves = 10 
    

    
   
harshit = Employee("Harshit",40000)

rohan = Employee("Rohan", 400000)

# sahil = Employee.from_string("Sahil-400000")

yatin = Player("Yatin","Volleyball")

karan = CoolProgrammer("Karan",455)
print


# # print(rohan.printdetails())
# # print(harshit.printdetails())
# print(yatin.print_details())

print(karan.no_of_leaves)