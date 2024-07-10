a = int(input())
if a%400 == 0:
    res = 1
elif a%4 == 0:
    if a%100 != 0:
        res = 1
    else:
        res = 0
else:
    res = 0

print(res)
