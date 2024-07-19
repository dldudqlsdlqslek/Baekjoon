def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [word for word in arr if len(word) < len(pivot)]
    middle = [word for word in arr if len(word) == len(pivot)]
    right = [word for word in arr if len(word) > len(pivot)]

    return quick_sort(left) + middle + quick_sort(right)


n = int(input())
w = [input().strip() for _ in range(n)]
w.sort()
sw = quick_sort(w)
res = []
for i in sw:
    if i not in res:
        res.append(i)
for j in res:
    print(j)
