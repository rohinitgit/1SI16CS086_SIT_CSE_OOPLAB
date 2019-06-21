import random
print("when will I get married\n")

print("1.I dont know\n2.Never\n3.Anytime now\n3.wait for the rigth time\n5.Anymore questions\n")
a=int(input())
if a==1:
    print("I dont know")
elif a==2:
    print("Never")
elif a==3:
    print("Anytime now")
elif a==4:
    print("wait for the rigth time")
else:
    print("Anymore questions")
    print("1.yes\n2.no")
    b=int(input())
    if b==1:
        print(random.randint())
    elif b==0:
        sys.exit()

 