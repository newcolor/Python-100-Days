Python基本数据结构

数据结构：通俗点儿说，就是存储数据的容器。这里主要介绍Python的4种基本数据结构：列表、元组、字典、集合；
格式如下：
列表：list = [val1, val2, val3, val4]，用中括号；
元组：tuple = (val1, val2, val3, val4)，用小括号；
字典：dict = {key1: val1, key2: val2, key3: val3}，用大括号；
集合：set = {val1, val2, val3, val4}，用大括号；

### 列表
list = [val1, val2, val3, val4]，列表最显著的特征是：
列表中每个元素都是可变的；
列表中元素是有序的，即每个元素都有一个位置；
列表可以容纳Python的任何对象；
接下来看列表的增删改查：

```Python
#增:
or_list = [1, "abc", 2.51]
or_list.append("JavaScript")    # append()方法在列表末尾追加元素(以整体形式追加)
or_list.insert(0, "Python")
print("or_list is: ", or_list)
#用insert()方法可以实现在列表中增加元素。insert()方法需要写明增加在哪个位置和增加的内容，新元素的实际位置是在指定位置元素之前的位置；如果指定的位置不存在，默认会增加在列表末尾；
or_list = [1, "abc", 2.51]
or_list[0:0] = [9]      # [0:0]是指在列表中的第1个位置插入新元素
or_list[3:3] = "a"      # [3:3]是指在列表中的第4个位置插入新元素
print("or_list is: ", or_list)
#上面的这两种方法都是天价单个元素，除了添加单个元素，还可以添加多个元素，用extend()方法来实现：

or_list = [1, "abc", 2.51]
ex_list = ["Python", 23, "game"]
or_list.extend(ex_list)         # extend()方法用于在列表末尾一次性追加另一个列表的多个值
print("or_list is: ", or_list)

#删：
or_list = [1, "abc", 2.51]
or_list.remove(1)
print("or_list is: ", or_list)
or_list.pop()  #移除最后一个
print("or_list is: ", or_list)
#删除列表元素除了remove()方法外，也可以用del关键字来声明：
del or_list[0:2]    # [0:2]删除第1个和第2个位置元素
print("or_list is: ", or_list)

#改：
lst = [1, "abc", 2.51]
lst[0] = "start"
lst[2] = 777
print("lst is: ", lst)
#如果想要替换掉列表中的某个元素，可以直接给列表某位置的元素重新赋值，lst[2]指lst列表中的第3个元素；

#查：
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
src_list.reverse() #反转
src_list.sort(func) #排序

#操作符  +  -  in  for
```

### 元组
tuple = (val1,val2,val3,val4)，Python中的元组与列表类似，不同之处在于元组不可修改，类似于稳定版的列表，因此在列表中可以使用的增删改的方法在元组中是不可以使用的，但是可以对元组中的元素进行索引，和列表类似。

```Python
tup = (1, 2.5, "hello", 26, "abc")
print(tup[0])
print(tup[1])
print(tup[2])
print(tup.index(26))
print(tup.index("hello"))
#同样的，index()方法查找的元素不在元组中时，会产生ValueError异常。
```

### 字典
dict = {key1:val1,key2:val2}，编程世界中的很多概念都源自于生活，字典也是。这种数据结构如我们使用的字典一样，通过"名称->内容"来构建，在Python中每个元素都是带有冒号的kye与value的对应关系，习惯称之为键值对。字典的特征如下：

字典中的元素必须时键值对的形式；
键(key)不可以重复，而值(value)可以重复；
键不可变，无法修改；值可以修改，可以是任何对象；
即使字典中有重复的键，输出时也只会出现一次，比如：

d = {"A": "art", "B": "blog", "C": "ascii", "C": "cute", "C": "Java"}
print(d)        # {'A': 'art', 'C': 'Java', 'B': 'blog'}
接下来看字典的增删改查：

```Python
增：
字典中没有像列表那样的insert()方法，但是可以通过下面这种方式插入元素，元素默认插入在最后一个位置。

d = {'A': 'art', 'B': 'Java', 'C': 'blog'}
d["D"] = "dictionary"
print(d)
再列表中可以通过extend()方法来为列表增加多个元素，在字典中可以使用update()方法来实现添加多个元素；

d = {'A': 'art', 'B': 'Java', 'C': 'blog'}
d.update({"D": "dictionary", "E": "example"})
print(d)

删：
在字典中删除某个元素，也可以使用del关键字：
d = {'A': 'art', 'B': 'Java', 'C': 'blog'}
del d["A"]
print(d)
需要注意的是，虽然字典是用大括号，但删除时依然使用中括号。

改：
如果要修改字典里的元素，直接重新给键赋值即可：
d = {'A': 'art', 'B': 'Java', 'C': 'blog'}
d["B"] = "beyond"
print(d)

查：
在字典中进行查询时，跟删除一样需要通过字典的键来，也就是说对字典的查询和删除都是通过键来的：
d = {'A': 'art', 'B': 'Java', 'C': 'blog'}
d["B"]
print(d["B"])

其他:
d = {'e': 'englist'}
d1 = {'a': 'apple', 'b': 'boy'}
d2 = {'c': 'cat', 'd': 'dog'}
cmp(d1, d2)
len(d1)
str(d1)
type(variable)
dict.clear()
dict.copy()
dict.fromkeys()
dict.get(key, default=None)
dict.has_key()
dict.items()
dict.setdefault(key, )

```

### 集合
set = {val1,val2,val3,val4}，集合的概念有点接近数学上的集合。每个集合中的元素时无序的、不重复的任何Python对象，我们可以通过集合去判断数据的从属关系，有时还可以通过集合把数据结构中重复的元素过滤掉。集合不可以被切片也不能被索引，除了做集合运算外，集合元素可以被添加和删除。

```Python
s = {9, 3, 4, 6, 4, 2, 8}
s.add(5)        # 新增元素5
s.discard(4)    # 删除元素4

print(s)        # 输出的集合会从小到大排列，并取重：{2, 3, 5, 6, 8, 9}
```


### numpy中的array
标准的python库中一般使用list来保存一组数值，并且可以使用自带的各种函数对数值进行各种运算。由于list中的元素可以是各种对象，list中保存的是对象的指针，这样为了保存['q','w','r']，需要生成3个指针和三个字符串对象，对于大数据量的运算来说这种显然很耗费内存和cpu。
此外python还提供了array模块，array对象和list不同，它直接保存数值，但是由于不支持多维数组，也没有各种运算函数，因此不适合做数值运算。numpy弥补了上面的不足，提供了两种基本的对象，ndarray（N-dimensional array object）和ufunc（universal function object）。ndarray用来存储单一数据类型的多为数组，ufunc则提供能够对数组进行处理的函数。

5.1 创建
可以使用给array对象传递python的序列对象来创建数组，如果传递的是多层嵌套的序列，将会创建多维的数组。
a=array([1,2,3,4])
b=array((4,5,6,7))
c=array([[1,2,3],[4,5,6],[7,8,9]])
c.dtype
dtype('int32')

https://blog.csdn.net/zhang_xinxiu/article/details/53750389
