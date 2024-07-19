def check(s):
    stack = []
    for char in s:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return "no"
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                return "no"
            stack.pop()
    
    return "yes" if not stack else "no"

while True:
    instr = input()
    if instr == ".":
        break
    print(check(instr))
