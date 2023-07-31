
number  = int (input())
sum  = 0;
temp = number
while(number!=0):
    rem = number % 10;
    sum = sum+ rem * rem * rem;
    number = number/10
if(temp == sum):
    print("this is aramstrong")
else:
    print("this not")

