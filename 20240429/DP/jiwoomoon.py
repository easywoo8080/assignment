"""
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.

n=17일때 까지 피보나치 수를 써보면 다음과 같다.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

"""
import time

# 피보나치 수열 계산 함수 (DP를 사용하지 않음)
def fibo_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)


# 피보나치 수열 계산 함수 (DP 사용)
def fibo_fn(n):
    a = 0
    b = 1
    if n <= 0:
        return [0]
    elif n == 1:
        return [a]
    elif n == 2:
        return [a, b]
    else:
        fibo = [a, b]
        for _ in range(n - 1):
            next_fib = fibo[-1] + fibo[-2]
            fibo.append(next_fib)
        return fibo

# 입력 받기
n = int(input("n 값을 입력하세요: "))

# DP를 사용하지 않는 경우 실행 시간 측정
start_time = time.time()
result_no_dp = fibo_recursive(n)
end_time = time.time()
execution_time_no_dp = end_time - start_time
print("DP를 사용하지 않음 : 최종 값 -", result_no_dp, ", 경과 시간 -", execution_time_no_dp, "초")

# DP를 사용하는 경우 실행 시간 측정
start_time = time.time()
result_with_dp = fibo_fn(n)
end_time = time.time()
execution_time_with_dp = end_time - start_time

# 결과 출력

print("DP를 사용함       : 최종 값 -", result_with_dp[-1], ", 경과 시간 -", execution_time_with_dp, "초")
