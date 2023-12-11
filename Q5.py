def powerset(s):
    return iter(powerset_rec(s))


def powerset_rec(s):
    if not s:
        return [[]]
    subset = powerset_rec(s[1:])
    return subset + [[s[0]] + lst for lst in subset]


def string_1():
    input_string = input("Enter a string: ")
    k = list(input_string)
    substrings = []
    for i in powerset(k):
        if (i != []):
            j = ''.join(i)
            substrings.append(j)
    return substrings


def length(a, b):
    result = []
    for i in a:
        if i not in result and len(i) == b:
            result.append(i)
    return result


def distinct(c, d):
    distinct_ = []
    for string in c:
        unique_chars = set(string)
        if len(unique_chars) == d:
            distinct_.append(string)
    return distinct_


def palindrome(e):
    palindrome_ = []
    for i in e:
        if (i == i[::-1]):
            palindrome_.append(i)
    return palindrome_


a1 = string_1()
print("All possible substrings :")
for r in range(len(a1)):
    print(f"{r+1}-{a1[r]}")
print("-----------------------")

b1 = int(input("Enter The length of string :"))
a2 = length(a1, b1)
print(f"All possible substrings of length {b1}:")
for q in range(len(a2)):
    print(f"{q+1}-{a2[q]}")
print("-----------------------")

b2 = int(input("Enter The length of distinct characters needed :"))
a3 = distinct(a2, b2)
if (len(a3) != 0):
    print(f"All possible substrings of length {b1} & {b2} distinct characters :")
    for w in range(len(a3)):
        print(f"{w+1}-{a3[w]}")

else:
    print(f"There is no substrings of length {b1} & {b2} distinct characters")
print("-----------------------")

a4 = palindrome(a1)
print("all possible palindrome :")
for e in range(len(a4)):
    print(f"{e+1}-{a4[e]}")
print("-----------------------")
