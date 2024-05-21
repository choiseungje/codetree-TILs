n,a,b = map(int,input().split())
k = list(map(int,input().split()))
p = k.index(a)
k = k[p:]
answer = 0
while True:
    if a in k:
        answer += 1
        a += b
    else:
        break
print(answer)