k = int(input())
a = 1
b = 1
c = 0
if k == 1 or k == 2:
    print(a)
else:
    for i in range(k-2):
        c = a+b
        a = b
        b = c   
    print(c)