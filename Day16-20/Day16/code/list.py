#增:
def insertList():
    or_list = [1, "abc", 2.51]
    or_list.append("JavaScript")    # append()方法在列表末尾追加元素(以整体形式追加)
    or_list.insert(0, "Python")
    print("or_list is: ", or_list)
#用insert()方法可以实现在列表中增加元素。insert()方法需要写明增加在哪个位置和增加的内容，新元素的实际位置是在指定位置元素之前的位置；如果指定的位置不存在，默认会增加在列表末尾；
    or_list = [1, "abc", 2.51]
    or_list[0:0] = [9]      # [0:0]是指在列表中的第1个位置插入新元素
    or_list[3:3] = "a"      # [3:3]是指在列表中的第4个位置插入新元素
    print("or_list is: ", or_list)

#上面的这两种方法都是添加单个元素，除了添加单个元素，还可以添加多个元素，用extend()方法来实现：
    or_list = [1, "abc", 2.51]
    ex_list = ["Python", 23, "game"]
    or_list.extend(ex_list)         # extend()方法用于在列表末尾一次性追加另一个列表的多个值
    print("or_list is: ", or_list)

#删：
def deleteList():
    or_list = [1, "abc", 2.51]
    or_list.remove(1)
    print("or_list is: ", or_list)
    or_list.pop()  #移除最后一个
    print("or_list is: ", or_list)
    #删除列表元素除了remove()方法外，也可以用del关键字来声明：
    del or_list[0:2]    # [0:2]删除第1个和第2个位置元素
    print("or_list is: ", or_list)

#改：
def updateList():
    lst = [1, "abc", 2.51]
    lst[0] = "start"
    lst[2] = 777
    print("lst is: ", lst)
    #如果想要替换掉列表中的某个元素，可以直接给列表某位置的元素重新赋值，lst[2]指lst列表中的第3个元素；

#查：
def searchList():
    #列表的索引与字符串的索引类似，同样是分正反两种索引方式，可以从后往前，也可以从前往后所以，比如：
    src_list = [1, "abc", 2.51]
    # 输出第2个位置和倒数第1个位置的元素
    print(src_list[1], src_list[-1])

    # 输出第1、2个元素和第2到最后一个元素
    print(src_list[:2], src_list[1:])
    #但是如果想查看某个元素的位置，就需要使用下面这种方式：
    src_list = [1, "abc", 2.5, 360]
    print(src_list.index(2.5))
    #这里需要注意的是，如果index()查找的元素不在列表里面，程序会产生ValueError："xxx" is not in list

#其他:
def func(a, b):
    return True if a > b else False

def sortList():
    '''
    list.sort(cmp=None, key=None, reverse=False)
    cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
    key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
    reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
    '''
    src_list = [1, 7, 2, 5, 4, 6, 3]
    src_list.sort() #排序
    print(src_list)
    src_list = [1, 7, 2, 5, 4, 6, 3]
    src_list.sort(reverse=True)
    print(src_list)

def otherListOperate():
    #src_list = [1, "abc", 2.51]
    src_list = [1, 7, 2, 5, 4, 6, 3]
    src_list.reverse() #反转
    print(src_list)
    

#操作符  +  -  in  for
def main():
    #insertList()
    #deleteList()
    #updateList()
    #searchList()
    sortList()
    #otherListOperate()

if __name__ == '__main__':
    main()