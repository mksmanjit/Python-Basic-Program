class MyCallableClass:
    def __init__(self):
        self.buffer = []

    def __call__(self, host_name):
        self.buffer.append(host_name)


my_callable_class = MyCallableClass()
my_callable_class("Test")
my_callable_class("Test1")
my_callable_class("Test2")

print(my_callable_class.buffer)