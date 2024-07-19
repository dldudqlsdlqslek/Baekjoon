from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()
    if 0<= x-1 < n and 0<= y < m and box[x-1][y] == 0:
        box[x-1][y] = box[x][y] + 1
        q.append((x-1, y))
    
    if 0<= x+1 < n and 0<= y < m and box[x+1][y] == 0:
        box[x+1][y] = box[x][y] + 1
        q.append((x+1, y))
    
    if 0<= x < n and 0<= y-1 < m and box[x][y-1] == 0:
        box[x][y-1] = box[x][y] + 1
        q.append((x, y-1))
    
    if 0<= x < n and 0<= y+1 < m and box[x][y+1] == 0:
        box[x][y+1] = box[x][y] + 1
        q.append((x, y+1))

    
max = 0

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit(0)
        if box[i][j] > max:
            max = box[i][j]
print(max-1)
