n = int(input())
arr = [0,1,1]
if n ==0:
    arr=[0]
elif n==1:
    arr[1]
elif n==2:
    arr[1]
else:
    for _ in range(n-2):
        arr.pop(0)
        arr.append(arr[0]+arr[1])
       
print(max(arr))
