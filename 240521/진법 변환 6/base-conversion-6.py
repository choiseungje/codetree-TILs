k = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a,b,c = input().split()
sum = 0
for i in range(len(b)):
    sum += int(b[i]) * int(k.index(a))**(len(b)-i-1)
answer = ''
while sum > 0:
    answer = str(sum%int(k.index(c))) + answer
    sum //= int(k.index(c))
print(answer)