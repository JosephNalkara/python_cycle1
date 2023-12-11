def sum_number(a):
	k=0
	for i in range(4):
	    n=int(a%10)
	    k=k+n
	    a=(a//10)
	return k

def reverse(b):
    reversed_num = 0
    while b > 0:
        digit = b % 10
        reversed_num = (reversed_num * 10) + digit
        b = b // 10
    return reversed_num

def difference(c):
	e=1
	o=1
	for i in range (1,5):
		digit= c % 10
		if (i%2==0):
			e=e*digit
		else:
			o=o*digit
		c=c//10
	diff=o-e
	return diff
			
number=int(input ("Enter your number :"))
l=sum_number(number)
m=reverse(number)
n=difference(number)
print("Sum of the digits = ",l)
print("Reverse of the number",m)
print("Difference :",n)
