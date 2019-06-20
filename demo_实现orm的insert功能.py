class ModelMetaclass(type):
    def __new__(cls, name, base, attrs):
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v,tuple):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)  #删除这些已经在字典存在的属性

        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, base, attrs)


class User(metaclass=ModelMetaclass):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")

    def __init__(self,**kwargs):
        for name,value in kwargs.items():
            setattr(self,name,value)

    def save(self):
        fields = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self,k,None))

        sql = 'insert into %s (%s) values (%s)' % \
              (self.__table__, ','.join(fields), ','.join([str(i) for i in args]))
        print('SQL: %s' % sql)

u = User(uid=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()