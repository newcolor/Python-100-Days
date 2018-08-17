def main():
    a = (x*x for x in range(10))
    print(a)
    print(sum(a))

if __name__ == '__main__':
    main()