n = int(input())
flag = 0
for i in range(n):
    sum = i + (i//100000) + ((i%100000)//10000) + ((i%10000)//1000) + ((i%1000)//100) + ((i%100)//10) + (i%10)
    if sum == n:
        flag = 1
        print(i)
        break
if flag == 0:
    print(0)
