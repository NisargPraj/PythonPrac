class A:
    def demo(self):
        print(" In class A")


class B(A):
    def demo(self):
        print(" In class B")


class C(A):
    def demo(self):
        print("In class C")


class D(B, C):
    pass


obj_d = D()
obj_d.demo()