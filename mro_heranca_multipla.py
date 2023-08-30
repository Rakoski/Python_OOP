class A:
    def foo(self):
        print("A's foo")


class B(A):
    def foo(self):
        print("B's foo")


class C(A):
    def foo(self):
        print("C's foo")


class D(B, C):
    pass

d = D()
d.foo()  # This will follow the MRO and call B's foo
print(D.mro())  # This will show the method resolution order

# The C3 algorithm follows these rules:
#
#     Parents are considered in the order they appear in the inheritance declaration.
#     A class and all its parents are considered before moving to the next class in the list.
#     When traversing parent classes, the algorithm tries to find a consistent linearization order
#     that respects the order of appearance and maintains a consistent hierarchy.
