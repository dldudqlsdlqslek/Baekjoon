n = int(input())

stack = []
s = []
t = 1
for i in range(n):
  pn = int(input())
  while t<=pn:
    stack.append(t)
    s.append("+")
    t = t + 1 

  if stack[-1] == pn:
    stack.pop()
    s.append("-")
  else:
    n = -1
    break



if n == -1:
  print("NO")
else:
  for i in s:
    print(i)
