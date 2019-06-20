def set_level(num):
    def set_func(func):
        def call_func(*args,**kwargs):
            if num == 1:
                print("这是级别1")
            elif num == 2:
                print("这是级别2")
            return func()
        return call_func
    return set_func

@set_level(1)
def test1():
    return "---test1---"

@set_level(2)
def test2():
    return "---test2---"

print(test1())