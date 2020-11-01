class G:
    def text(self):
        print('g')

class E(G):
    def text(self):
        print('e')

class B(E):
    def text(self):
        print('b')

class F(G):
    def text(self):
        print('F')

class C(F):
    def text(self):
        print('D')

class D(G):
    def text(self):
        print('d')

class A(B,C,D):
    def text(self):
        print('a')

obj=A()
print(A.mro())
