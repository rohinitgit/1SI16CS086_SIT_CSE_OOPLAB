def spam(divdidBy):
	try:
		return 42 / divdidBy
	except Exception as e:
		print('Error : Invaild argument')
		print(e)
    else:
    	print("dividion went fine")

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))