n1=int(input('Enter 1st number:'))
n2=int(input('Enter 2nd number:'))
n3=1
n4=2
while n4<=n1 and n4<=n2:
	if n1%n4==0 and n2%n4==0:
		n3=n3*n4
		n1=n1/n4
		n2=n2/n4
	else:
		n4=n4+1
else:
	print ('LCM is ',n1*n2*n3)
