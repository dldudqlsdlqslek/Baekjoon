n = int(input())
memo = [0 for _ in range(n+1)]

for i in range(2, n+1):
  if i%3 == 0:
    if i%2 == 0:
      memo[i] = min(memo[i-1], memo[i//2], memo[i//3])+1
    else:
      memo[i] = min(memo[i-1], memo[i//3])+1
  else:
    if i%2 == 0:
      memo[i] = min(memo[i-1], memo[i//2])+1
    else:
      memo[i] = memo[i-1]+1

print(memo[n])
