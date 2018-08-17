def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def operate(func, x, y):
    result = func(x, y)
    return result

def main():
    print(operate(add, 5, 5))
    print(operate(subtract, 5, 4))

if __name__ == '__main__':
    main()