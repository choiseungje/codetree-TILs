a,b = map(int,input().split())
lst = []
for i in range(b):
    q,p = map(int,input().split())
    lst.append(q*p)
lst.sort(reverse = True)
count = 0
for i in lst:
    a -= i
    count += 1
    if a <= 0 :
        break
print(count)