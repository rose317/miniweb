def line(k,b):
    def create_y(x):
        print(k*x+b)
    return create_y

line_6 = line(1,1)
line_6(5)