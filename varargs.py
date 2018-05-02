def hyper_volume(*lengths):
    i = iter(lengths)
    print(i)
    v = next(i)
    print(v)
    for length in i:
        print(length)
        v *= length
    return v


def print_args(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    print(arg1)
    print(arg2)
    print(args)
    print(type(args))
    print(kwarg1)
    print(kwarg2)
    print(type(kwargs))
    print(kwargs)


def print_args1(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)


def print_args2(kwarg1, kwarg2, **kwargs):
    print(kwarg1)
    print(kwarg2)
    print(kwargs)


print(hyper_volume(2, 3))
print(hyper_volume(2, 3, 4))
print_args(1, 2, 3, 4, kwarg1=10, kwarg2=20, text=123, value=456)
t = (1, 2, 3, 4, 5, 56)
print_args1(*t)
k = {'kwarg1':21, 'kwarg2':68, 'test':1, 'mytest':2}
print_args2(**k)
