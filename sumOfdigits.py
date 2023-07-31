def sumdigit():
    n = 1967
    s = 0
    for i in (0, 1967 ,1):
        r = n%10
        s = s+r
        n = n/10

        print("this is sum of digit" ,s)

sumdigit()
