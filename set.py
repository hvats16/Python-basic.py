s = set()


l = [1, 2, 3, 4]
s_from_list = set(1)

s.add(1)
s.add(2)
s.add(5)
s1 = s.intersection({1,2,3,4})
#s1 = s.union({1,2,3,4})
print(s,s1)