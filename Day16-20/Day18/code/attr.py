class Foo:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        return self.name,self.age

def main():
    obj=Foo("xiaoming",18)
    print(getattr(obj,"name")) # 获取的是个对象
    setattr(obj,"k1","v1") # 设置成员
    print(obj.k1)
    print(hasattr(obj,"k1")) # 检查成员
    delattr(obj,"k1") # 删除成员
    show_fun=getattr(obj,"show")
    print(show_fun())

if __name__ == '__main__':
    main()