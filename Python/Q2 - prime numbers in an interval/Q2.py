a=int(input("Enter the beginning of interval:"))
b=int(input("Enter the end of interval"))

for i in range(a,(b+1)):
	c=0
	for j in range(1,(i+1)):
		if(i%j==0):
			c=c+1
	if(c==2):
		print(i)

