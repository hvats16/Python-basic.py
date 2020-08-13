# dict = { i: f"item{i}" for i in range(5)}
# dict1 = {value:key for key,value in dict.items()}
# print(dict,"\n",dict1)

n = int(input("how many items you want in list"))

for lis in range(n):
    lis = input("Input your list and next item in list will be seperae by :")
    lis1 = lis.split(":")

print("1:List Comprehension \n 2:Dictonary Comprehension \n 3:Set Comprehension")
s = int(input())

if s==1:
    list1 = [i for i in lis]
    print(list1)
elif s==2:
    dict11={f"items{i}":i for i in lis}
    print(dict11)
elif s==3:
    set1 = {i for i in list}
    print(set1)    

