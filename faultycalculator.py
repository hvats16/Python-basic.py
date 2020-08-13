# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result

print("enter first number")
num1=int(input())
print("enter second number")
num2=int(input())
print("what do you want to do? +,-,*,/")
operator=input()

if num1==45 and num2==3 and operator=='*':
    print("555")
elif num1==56 and num2==9 and operator=='+':
    print("77")
elif num1==56 and num2==6 and operator=='/':
    print("4")
elif operator=='+':
    addition=num1+num2
    print(addition)
elif operator=='*':
    multiplication =num1*num2
    print(multiplication)
elif operator=='/':
    division=num1/num2
    print(division)
elif operator=='-':
    substraction=num1-num2
    print(substraction)
else:
    print("go to hell")