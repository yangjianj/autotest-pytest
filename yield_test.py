def g():
    mylist = range(5)
    for i in mylist:
        print(222)
        yield i*i
        print(111)
        yield 'vvv'
        print('wwwww')

g()
print('xxxxx')
for i in g():
    print(i)
    print('next loop')
