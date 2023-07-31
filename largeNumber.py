num1 ,num2,num3 = input("enter three numbers: ").split()
print("num1 : ",num1)
print("num2: ",num2)
print("num3: ",num3)
if(num1<num2):
    if(num1<num3):
        print("num1 smallest")

    elif(num2<num3):
        print("num2 smallest")
    else:
        print("num3 smallest")