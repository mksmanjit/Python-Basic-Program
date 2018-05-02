class NotCallableClass:
    def __init__(self):
        print("")


class CallableClass:
    def __call__(self):
        print("")


def my_function():
    print("")


print(callable(list))
print(callable(list.append))
print(callable("Hello"))
print(callable(my_function()))
print(callable(NotCallableClass))
print(callable(CallableClass))
var = NotCallableClass()
var1 = CallableClass()
print(callable(var))
print(callable(var1))