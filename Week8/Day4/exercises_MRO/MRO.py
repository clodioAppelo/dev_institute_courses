
# class A:
#     num = 10


# class B(A):
#     pass


# class C(A):
#     num = 1


# class D(B, C):
#     pass


# print(D.mro())
# D.num
# ----------------------------------------------------------------------------------------------------------------------------------
# class X: pass
# class Y: pass
# class Z: pass
# class A(X,Y): pass
# class B(Y,Z): pass
# class M (B,A,Z): pass

# print(M.__mro__)

# This is the way that Python works to determine hey when you call a method or an attribute.
# To look up the hierarchy of inheritances.