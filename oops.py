class A:
    def __init__(self):
        print("class A constructor")

    def abc(self):
        print("class A method is called")


class B(A):

    def __init__(self):
        print("class B constructor is called")

    def abc(self):
        print("class B method is called ")

    def pqr(self):
        print("class B pqr method is called")


class C(A,B):
    def __init__(self):
        super(A,B)
        print("class C constructor is called")

    def abc(self):
        print("c class method is called")


obj = C()
obj.abc()
obj.pqr()
