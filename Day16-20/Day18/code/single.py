class Foo:  # 单例模式
    __v=None
    @classmethod
    # def ge_instance(cls):
    #     if cls.__v:
    #         return cls.__v
    #     else:
    #         cls.__v=Foo()
    #         return cls.__v
    def ge_instance(self):
        if self.__v:
            print('old')
            return self.__v
        else:
            print('new')
            self.__v = Foo()
            return self.__v

def main():
    obj1=Foo.ge_instance()
    print(obj1)
    obj2=Foo.ge_instance()
    print(obj2)
    obj3=Foo.ge_instance()
    print(obj3)

if __name__ == '__main__':
    main()