def check(num):
    if '666' in str(num):
      return 1
    else:
      return 0

n = int(input())
temp = 0
a = 665
while temp != n:
    a = a + 1
    temp = temp + check(a)
    if temp == n:
      break;

print(a)
