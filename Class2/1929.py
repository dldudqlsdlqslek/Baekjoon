def sosu(num):
    if num <= 1:
        return 0
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return 0
    return 1

n, m = map(int, input().split())

for num in range(n, m + 1):
    if sosu(num) == 1:
        print(num)
