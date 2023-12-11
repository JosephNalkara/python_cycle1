def salary(bp):
	if(bp<10000):
		da=bp*0.05
		hra=bp*0.025
		ma=500
		pt=20
		pf=bp*0.08
		it=0
	elif(bp<30000 and bp>10000):
		da=bp*0.075
		hra=bp*0.05
		ma=2500
		pt=60
		pf=bp*0.08
		it=0
	elif(bp<50000 and bp>30000):
		da=bp*0.11
		hra=bp*0.075
		ma=5000
		pt=60
		pf=bp*0.11
		it=11
	else:
		da=bp*0.25
		hra=bp*0.11
		ma=7000
		pt=80
		pf=bp*0.12
		it=20
	gs=bp+da+hra+ma
	d=pt+pf+it
	ns=gs-d
	return gs,d,ns,da,hra,ma,pt,pf,it

name=str(input("Enter Employee Name :"))
code=int(input("Enter Employee code :"))
basicpay=float(input("Enter Basic Pay :"))
gs,d,ns,da,hra,ma,pt,pf,it=salary(basicpay)
print("SALARY SLIP")
print("-----------")
print("Employee Name : ",name)
print("Employee code : ",code)
print("BASIC PAY : ",basicpay)
print("DA : ",da)
print("HRA : ",hra)
print("MA : ",ma)
print("PT : ",pt)
print("PF : ",pf)
print("IT : ",it)
print("GROSS SALARY : ",gs)
print("DEDUCTION : ",d)
print("NET SALARY : ",ns)
