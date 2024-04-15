import sys, heapq
input = sys.stdin.readline
n=int(input())
arr = []
for i in range(n):
    a,b = map(int, input().split())
arr.sort()
heap=[]
heapq.heappush(heap,arr[0][1])
for i in range(len(arr)): 
    if i==0 :
        continue
    elif arr[i][0]>=heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap,arr[i][1])
    else:
        heapq.heappush(heap,arr[i][1])
print(len(heap))