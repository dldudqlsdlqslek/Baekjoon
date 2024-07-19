n = int(input())
f = 0
p = n//5
for i in range(p, -1, -1):
  t = n - 5*i
  if t%3 == 0:
    f = 0
    print(i+t//3)
    break;
  else:
    f = -1

if f == -1:
  print(-1)
