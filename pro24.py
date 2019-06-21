import sys,pyperclip
import shelve
if save==save() :
	print("saved sucessfully")
elif list1==list1() :
	print(kk)
else :
	key1()

def save() :
	shelffile=shelve.open("datasave")
	shelffile['newvar']=pyperclip.paste()
	
	#shelffile.close()
def list1() :
	kk=(pyperclip.paste())
	print(kk)

def key1() :
	shelffile=shelve.open("datasave")
	l=shelfile['newvar']
	print(l)




 