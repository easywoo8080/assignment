n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[0])
result = 1

t = arr[0][1]
arr.pop(0)
while len(arr) !=0:
    while any(t in sub_arr for sub_arr in arr):
        for i in arr:
            if i[0] == t:
                t = i[1]
                arr.remove(i)
                break
    result += 1
    t = arr[0][1]
    arr.pop(0)
    
        

print(result)