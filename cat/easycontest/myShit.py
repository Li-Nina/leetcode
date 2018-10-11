class MyShit(object):
    def __init__(self, val):
        self.val = val

    def __iadd__(self, other):
        print('shit ', other)

    def __add__(self, other):
        print('shit2', other)

    def __str__(self):
        return 'hehehe' + str(self.val)


if __name__ == '__main__':
    a = MyShit(1)
    b = MyShit(2)
    a + b
    a += b
