class Shipping:

    next_serial = 1337

    @classmethod
    def _get_next_serial_class_method(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _get_next_serial():
        result = Shipping.next_serial
        Shipping.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = Shipping._get_next_serial()


c1 = Shipping('ABC', 'noodles')
print(c1.owner_code)
print(c1.contents)
print(c1.serial)

c2 = Shipping('DEF', 'text')
print(c2.owner_code)
print(c2.contents)
print(c2.serial)
print('hello')
print(Shipping._get_next_serial_class_method())