# numbers = ['2','3','4','5']

# # for i in range(len(numbers)):
# #     numbers[i]=int(numbers[i])

# numbers = list(map(int,numbers))
    
# numbers[2]=numbers[2]+1

# print(numbers[2])



# square = [1,2,3,4,5,6,7,8,9]

# no_square = list(map(lambda x:x*x,square))

# print(no_square)



# def square(a):
#     return a*a

# def cube(a):
#     return a*a*a

# func = [square,cube]

# for i in range(5):
#     val = list(map(lambda x:x(i),func))
#     print(val)



#######################  filter function ###############################

# list1  = [1,2,3,4,5,6,7,8,9]

# def is_greater_5(num):
#     return num>5

# gr_than_5 = list (filter(is_greater_5,list1))
# print(gr_than_5)



#############  reduce ##########

list1  = [1,2,3,4,5,6,7,8,9]

num = reduce(lambda x,y:x+y , list1 )

print(num)
