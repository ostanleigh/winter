print("hello world")

def Test(a):
    if a == 1:
        return a,
    else:
        print(a)
        count = Test (a-1)
        return count
        print(count)

Test(32)

def gcdIter1(a, b):
    for x in range(a, -1, -1):
        if a % x == 0 and b % x == 0:
            print ("The anwer is: ")
            return x


print(gcdIter1(24, 48))
print("Now it is time for, home, home on the Range!")
print(list(range(12, 20, 2)))