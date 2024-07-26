n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
rt = 0
rp = 0
rpe = 0
for i in size:
    if i != 0:
        rt = rt + i//t + 1
        if i%t == 0:
            rt = rt - 1
rp = n//p
rpe = n%p
print(rt)
print(rp, rpe)
    
    
