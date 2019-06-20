def set_func(func):
    def call_func(num):
        func(num)
    return call_func


def test1(num):
    print("num为%d" % num)

test1(100)