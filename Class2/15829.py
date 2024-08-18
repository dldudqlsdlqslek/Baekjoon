n = int(input())
sent = input()
res = 0
for i in range(len(sent)):
    res = res + ((ord(sent[i])-96) * (31**i))
res = res%1234567891
print(res)
