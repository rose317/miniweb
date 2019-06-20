#通用装饰器
def set_func(func):
    def call_func(*args,**kwargs):
        print("---验证一---")
        return func(*args,**kwargs) #*args,**kwargs这里是拆包
    return call_func

@set_func
def test1(num,*args,**kwargs):
    print("---test---%d" % num)
    print("---test---",args)
    print("---test---",kwargs)
    return "ok","200"

ret = test1(100,200,300,mm=400)
print(ret)