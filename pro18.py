import sys,pyperclip
para=str(input())
r=para.split('.')
j=0
for i in r:
	j+=1
	print(str(j)+' '+i)
	p=pyperclip.copy(str(j)+' '+i)
	
