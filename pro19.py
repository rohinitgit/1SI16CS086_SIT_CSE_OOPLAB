import os
p=os.listdir(os.getcwd())
print(p)
print("\n")
sum=0
for i in p :
	d=os.path.getsize(i)
	sum=sum+d
print(sum)
    
