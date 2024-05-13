lst = [chr(i+65) for i in range(26)]
lst = ['0','1','2','3','4','5','6','7','8','9'] + lst
a,b = input().split()
b = int(b)
lst = lst[:b+1]
k = len(a) - 1
answer = 0
for i in a:
    for u in lst:
        if i == u:
            answer += lst.index(u) * b ** k
            k -= 1
print(answer)