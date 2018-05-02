class A:

    @staticmethod
    def display():
        print('This is Parent Class')


class B(A):
    @staticmethod
    def display():
        print('This is Child Class')


A.display()
B.display()
a = A()
a.display()
a = B()
a.display()
