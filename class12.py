class A:
    def met(self):
        print("My name is harshit rajput")
        

class B(A):
    def met(self):
        print("My name is harshit ")
     
class C(A):
    def met(self):
        print("My name is harshu")


class D(B,C):
    def met(self):
        # print("My name is harsh")


a = A()
b = B()
c = C()
d = D()

print(d.met())
