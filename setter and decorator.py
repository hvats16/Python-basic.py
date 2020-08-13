class Employee:
    
    
    def __init__(self,name,lastname):
        self.name = name 
        self.lastname = lastname
        
        
    def explain(self):
        return f"The name is {self.name} {self.lastname}"
    

    @property
    def email(self):
        return  f"{self.name}.{self.lastname}@gmail.com"
    
    @email.setter
    def email(self,string):
        name = string.split("@")[0]
        self.name = name.split(".")[0]
        self.lastname.split(".")[0]
        
        
        @email.deleter
        def email(self):
            self.name = None
            self.lastname = None
        
    
harshit = Employee("Harshit", "Vats")
rohan = Employee("Rohan", "kapoor")

print(harshit.email)
rohan.name = "Lambo"
print(rohan.email)

# harshit.email = "hvats1603@gamil.com"
print(harshit.email)

del harshit.email