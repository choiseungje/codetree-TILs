a = input()
answer =0
for i in range(len(a)):
    answer += int(a[i])*8**(len(a)-1-i)
answer = str(bin(answer))[2:]
print(answer)