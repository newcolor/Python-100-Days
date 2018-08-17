class Mytype(type):
    def __init__(self, what, bases=None, dict=None):
        print('Mytype.__init__')
        super(Mytype,self).__init__(what, bases, dict)

    def __call__(self, *args, **kwargs):
        print('Mytype.__call__')
        obj=self.__new__(self)
        self.__init__(obj, *args, **kwargs)
        return obj

class Foo:
    __metaclass__=Mytype
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

def main():
    obj=Foo("xiaoming",18)
    print(obj.name,obj.age)
    print(isinstance(obj,Mytype))

if __name__ == '__main__':
    main()