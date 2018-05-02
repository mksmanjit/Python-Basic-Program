message = "global"


def outer():
    text = "enclosing"

    def inner():
        global message
        message = "local"
        nonlocal text
        text = "local"
    print(message + ">>" + text)
    inner()
    print(message + ">>" + text)


outer()
