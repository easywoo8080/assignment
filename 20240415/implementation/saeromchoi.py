n = int(input())
arr=[0]
sum = 1
for i in range(n):
    arr.append(sum)
    sum += arr[i]
print(arr[n])