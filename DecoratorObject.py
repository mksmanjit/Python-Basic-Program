class Tracer:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, *kwargs)
        return wrap


tracer = Tracer()

@tracer
def rotate_list(l):
    #l[1:] it means take the list from the first element
    # [l[0]] it means take the first element and make it list by adding [].
    return l[1:] + [l[0]]


lst = [1, 2, 3]
print(rotate_list(lst))