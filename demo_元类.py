class UpperAttrMetaClass(type):
    def __new__(cls,class_name,class_parents,class_attr):
        new_attr = {}
        for name,value in class_attr.items():
            if not name.startswith("_"):
                new_attr[name.upper()] = value

        return type(class_name, class_parents, new_attr)


class Foo(object,metaclass=UpperAttrMetaClass):
    bar = 'bip'

f = Foo()
print(f.BAR)