#import itertools
from itertools import islice

def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, curr + prev

def main():
    f = fib()
    print(list(islice(f, 0, 20)))

if __name__ == '__main__':
    main()