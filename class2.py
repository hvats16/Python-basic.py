class Employee:
    no_of_leaves = 8 
    pass


harshit = Employee()

rohan = Employee()

harshit.name = 'Harshit'
rohan.name = "Rohan"

harshit.salery = 4000000
rohan.salery = 4000000
# print(rohan.no_of_leaves)
# print(rohan.__dict__)
# rohan.no_of_leaves =10
# print(rohan.no_of_leaves)

# print(rohan.__dict__)

print(Employee.no_of_leaves)

print(Employee.__dict__)

print("The first employee is "+harshit.name+ "And his salery is ",harshit.salery)