def make_caps(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return x.upper()
    return wrap


def make_reverse(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return reverse(x)
    return wrap


def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

# multiple decorator are executed in a reverse order and output of one decorator is passed to the next one.
@make_caps
@make_reverse
def get_text():
    return "hello"


print(get_text())