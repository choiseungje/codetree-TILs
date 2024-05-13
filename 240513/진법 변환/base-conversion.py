lst = [chr(i+65) for i in range(26)]
lst = ['0','1','2','3','4','5','6','7','8','9'] + lst
a,b = input().split()
k = 0
for idx,i in enumerate(lst):
    if i == b:
        k = idx
answer = 0
p = 0
for i in range(len(a)):
    answer += int(a[-(i+1)])*k**p
    p += 1
print(answer)