과제 리뷰

우선순위큐

`import heapq`
`heapq.heappop(heap_list)`
`heapq.heappush(heap_list, 5)`

## 구현알고리즘

머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정

**⇒ 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제**

- 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
- 실수 연산을 다루고 특정 소수점 자리까지 출력해야 하는 문제
- 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
- 적절한 라이브러리를 찾아서 사용해야 하는 문제

eval함수

수식문자열을 진짜수식으로

‘2+2’ ⇒ 2+2

a= eval(’2+2’)

a= 2+2

stack & que

stack

list.append(’5’)

list.append(’6’)

list.append(’7’)

list.pop() ⇒ ‘7’

que

[1,2,3,4]

list.pop(0) [2,3,4]

list.append(’5’)

list.append(’6’)

list.append(’7’)

list.pop(0) ⇒ ‘5’

문자열

input()

숫자 1개

a = int(input())

숫자2개

1)

a,b = input().split()

a=int(a)

b=int(b)

2)

a,b = map(int,input().split())

a,b = map(str,input().split())

숫자를 하나하나 배열화

a=120

num = list(str(a))

[’1’,’2’,’0’]

속도빠른 input

import sys
input = sys.stdin.readline

input()

다차원배열

1) 1차원 배열

a = [1 for _ in range(5)]
a= [1,1,1,1,1]

2) 2차원 배열
res = [ [0] * 19 for _ in range(19) ]

https://codeup.kr/problem.php?id=6095

board = [input().split() for _ in range(10)]

https://codeup.kr/problem.php?id=6098

문제1) **수 나열하기3 코드업100**

https://codeup.kr/problem.php?id=6090

과제1) 피보나치수열

https://www.acmicpc.net/problem/2747
