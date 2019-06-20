class test(object):
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("这里是装饰器的功能")
        return self.func()

@test
def get_str():
    return "hahaha"

print(get_str())