def outer():
    def inner(n):
        sum = 0
        for i in range(1, n):
            sum += i
        return sum
    return inner

def outer2(n):
    def inner2(n):
        sum = 0
        for i in range(1, n):
            sum += i
        return sum
    
    sum = 0
    for i in range(1, inner2(n)):
        sum += i
    return sum

def main():
    #f = outer()
    #print(f(5))
    print(outer2(5))

if __name__ == '__main__':
    main()