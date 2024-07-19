n = int(input()) 
hcard = list(map(int, input().split()))  
m = int(input()) 
fcard = list(map(int, input().split())) 


fin = {}


for i in hcard:
    if i in fin:
        fin[i] += 1
    else:
        fin[i] = 1

for j in fcard:
    if j in fin:
        print(fin[j], end=' ')
    else:
        print(0, end=' ')
