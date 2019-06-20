import time


def set_func(func):
    def call_func():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("函数总共运行时间%f" % (stop_time-start_time))
    return call_func

@set_func
def test1():
    print("这是test1")
    for i in range(100000):
        pass

test1()