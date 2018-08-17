d1 = {'a': 'apple', 'b': 'boy'}
d2 = {'c': 'cat', 'd': 'dog'}

#获取信息
print('len(d1): ', len(d1))
print('str(d1): ', str(d1))
print('type(d1): ', type(d1))

#浅拷贝
d3 = d1.copy()
print('d3: ', d3)
d3['b'] = '666'
print('d3: ', d3)

#读取字典中的值，如果不存在返回默认值
print('d1.get(a): ', d1.get('a', 0))
print('d2.get(u): ', d2.get('u', 100))
#print('d1.has_key(): ', dict.has_key())
print('dict.items(): ', d1.items())

#读取字典中的值，如果不存在返回默认值，并将值写入字典中
print('dict.setdefault(key, ): ', d1.setdefault('a', 111))
d1.clear()
print(d1)

#创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值
d1 = dict.fromkeys((1,2,3),3)
print(d1)

print('----------------')
#字典交换
print(d1)
print(d2)
d1, d2 = d2, d1
print(d1)
print(d2)