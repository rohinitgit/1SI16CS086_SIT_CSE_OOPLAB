def func1(a,b):
	sum=a+b
	product=a*b
	sub=a-b
	div=a/b
	return sum,product,sub,div

if __name__=="__main__" :
    print(__name__)
    x,y,p,z=func1(20,4)
    print(x,y,p,z)
else:
	print(__name__)
    #main is not equal name while importing