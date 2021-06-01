def dan(num):
    for i in range (1, 10):
        print('{} * {} = {:2}'.format(num, i, num*i))

def gugudan():
    for i in range (2, 10):
        dan(i)
        print()

def gugudan2():
    for i in range (1, 10):
        for j in range (2, 10):
            print('{} * {} = {:2}'.format(j, i, j*i), end="      ")
        print()

if __name__=="__main__":
    gugudan2()