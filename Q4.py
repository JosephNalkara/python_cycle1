def is_happy(num):
    count = 0
    while (num != 1 and count < 100):
        s = 0
        while (num > 0):
            digit = num % 10
            s += (digit ** 2)
            num //= 10
        num = s
        count += 1
    return num == 1


def in_range(a, b):
    print(f"Happy numbers between {a} and {b}:")

    for i in range(a, b + 1):
        num = i
        if (is_happy(num)):
            print(i)



def first_n(n):
    count = 0
    num = 1
    print(f"First {n} happy numbers:")
    while (count < n):
        if (is_happy(num)):
            print(num)
            count += 1
        num += 1


n1 = int(input("Enter a number: "))
checking = is_happy(n1)
if (checking == 1):
    print(n1, " is a happy number")
else:
    print(n1, "is not a happy number")
n2 = int(input("Enter the starting number :"))
n3 = int(input("Enter the ending number :"))
in_range(n2, n3)
n4 = int(input("How many happy numbers needed starting from 1 : "))
first_n(n4)
