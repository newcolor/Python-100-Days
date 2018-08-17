def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    # index = 1
    while True:
        n = next(it) # 返回序列的第一个数
        print("n: ", n)
        # print("index: ", index)
        # index += 1
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
        for m in it:
            if m < 1000:
                print(m)
            else:
                break
#F:\github\python\Python-100-Days-master\Day16-20\Day17\code

# Test
def call_divi(n):
    print(_not_divisible(n)(100))

def main():
    for n in primes():
        if n < 1000:
            #print(n)
            n
        else:
            break

if __name__ == '__main__':
    main()
    # call_divi(100)