correctW = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
correctB = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

m, n = map(int, input().split())
chess = [list(input()) for _ in range(m)]


def check(startX, startY):
  wChange = 0
  bChange = 0
  for a in range(8):
    for b in range(8):
      if chess[startX+a][startY+b] != correctW[a][b]:
        wChange = wChange+1
      if chess[startX+a][startY+b] != correctB[a][b]:
        bChange = bChange+1
  if wChange>bChange:
    return bChange
  else:
    return wChange

min = check(0, 0)

for i in range(m-7):
  for j in range(n-7):
    t = check(i, j)
    if min>t:
      min = t

print(min)
