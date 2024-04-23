"""
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

"""
#
# def fibo_fn(a, b, n):
#     if n <= 0:
#         return [0]
#     elif n == 1:
#         return [a]
#     elif n == 2:
#         return [a, b]
#     else:
#         fibo = [a, b]
#         for i in range(n - 1):
#             next_fib = fibo[-1] + fibo[-2]
#             fibo.append(next_fib)
#
#         return fibo
#
# # 시작값 a와 b, 그리고 피보나치 수열의 길이 n
# a = 0
# b = 1
# n = int(input())
#
# result = fibo_fn(a, b, n)
#
# print( result[-1]
#
#
# def fibonacci(n):
#     if n <= 1:
#         return n
#
#     prev = 0
#     curr = 1
#     for _ in range(2, n + 1):
#         prev, curr = curr, prev + curr
#
#     return curr


n = int(input())
prev = 0
curr = 1
# result = fibonacci(n)
for _ in range(2, n + 1):
    prev, curr = curr, prev + curr


print(curr)
