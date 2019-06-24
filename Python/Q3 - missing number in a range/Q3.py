print("Enter the list of numbers into the array from 1 to 100/Enter 0 to exit:")
a=[]
#Inputting the numbers
v=int(input("Enter number:"))

while(v!=0):
	a.append(v)
	v=int(input("Enter number:"))
n=len(a) 

print("Missing number:")
for i in range(n):
	if(a[i]!=i+1):
		print(i+1)
		break
