def check(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                return "NO"
            stack.pop()
    if not stack:
      return "YES"
    else:
      return "NO"




n = int(input()) 

for _ in range(n):
    instr = input()
    print(check(instr)) 
