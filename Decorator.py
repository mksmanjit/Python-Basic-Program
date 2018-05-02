def make_caps(f):
    print("First")
    def wrap(*args, **kwargs):
        print("Third")
        x = f(*args, **kwargs)
        print("Fifth")
        return x.upper()
    print("Second")
    return wrap


@make_caps
def get_text():
    print("Fourth")
    return "hello"


print(get_text())