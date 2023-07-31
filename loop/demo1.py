num1 = int(input())
num2 = int(input())
num3= int(input())
def form_tringle(num1,num2,num3):
    if (num1+num2)<=num3 or(num2+num3) <= num1 or (num1+num3)<= num2:
        failure = "Triangle can't be formed"
        return failure

    else:
        success = "Triangle can be formed"
        return success


result = form_tringle(num1,num2, num3)
print(result)