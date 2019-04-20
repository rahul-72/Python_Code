class A:
    def hello(self):
        B()


class B:
    print("Hello world")


a = A()
a.hello()