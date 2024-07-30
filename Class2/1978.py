n = int(input())
dp = [2, 3]
a = list(map(int, input().split()))
count = 0
for i in range(2, 1000):
    r = 0
    for j in dp:
        if i%j == 0:
                r = r + 1
    if r == 0:
        dp.append(i)
for num in a:
     if num in dp:
          count = count + 1
print(count)
