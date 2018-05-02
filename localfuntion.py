def factorial(num):
    fact = 1
    for i in range(num, 1, -1):
        fact = fact * i
    def print_num_in_style(n):
        print("The factorial for {0} is {1} ".format(num, fact))
    print_num_in_style(fact)


def outer():
    x = "first number "
    y = "second number"
    z = 20
    def inner():
        print("Inside Inner {0}".format(z) + x + y)
    return inner


def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp


factorial(5)
f = outer()
f()
print(f.__closure__)
square = raise_to(2)
print(square(5))
print(square(10))
cube = raise_to(3)
print(cube(5))
print(cube(10))