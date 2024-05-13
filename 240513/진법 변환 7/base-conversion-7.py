a= input()
a= a.split('.')
k = ''
a[1] = float('0.'+ a[1])
a[0] = str(bin(int(a[0])))[2:]
for i in range(4):
    a[1] *=2
    if a[1]>= 1:
        k += '1' 
        a[1] -= 1
    else:
        k += '0' 
a[1] = k
print('.'.join(a))