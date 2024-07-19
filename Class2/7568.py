man = int(input())
man_list = []
for _ in range(man):
  wh = list(map(int, input().split()))
  man_list.append(wh)
  
rank = [1]*man
for i in range(man):
  for j in range(man):
    if man_list[i][0] > man_list[j][0] and man_list[i][1] > man_list[j][1]:
      rank[j] += 1

for k in range(man):
  print(rank[k], end = ' ')
