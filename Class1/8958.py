a = int(input())
for i in range(a):
    str = input()
    cnt = 0
    cnt_temp = 0
    for j in range(len(str)):
        if str[j] == 'O':
            cnt_temp += 1
        else:
            cnt_temp = 0
        cnt = cnt + cnt_temp 
    print(cnt)
