class A:
      def __init__(self, x):
            self.class_A_atr = x * 3

      def some_method(self):
            return 'Text'

class B(A):
      def __init__(self, x):
            self.class_B_atr = x

class C(B, A):
      def __init__(self, x, y):
            self.class_C_atr = y
            super(B, self).__init__(x)

a = A('Text A')
b = B('Text B')
c = C('Text C - 1', 'Text C - 2')

print(dir(a))
print(dir(b))
print(dir(c))

print(c.__module__)