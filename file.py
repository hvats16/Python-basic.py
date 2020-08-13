f1 = open("harshit.txt")
try:
    f = open("does.txt")
except Exception as e:
    print(e)
else:
    print("this will run only when except is not running ")
finally:
    print("run this anyway")
    # f.close()
    f1.close()