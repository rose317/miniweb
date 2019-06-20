a = 10
def fun1():
    global a
    print(a)
    a += 10

def fun2():
    global a
    print(a)


fun1()
fun2()