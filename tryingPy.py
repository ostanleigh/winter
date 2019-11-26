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

print("Misha's modification")