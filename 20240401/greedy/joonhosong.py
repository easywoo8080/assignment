# 1번
print('hello')

# 2번
print("Hello World")

# 3번
print("Hello")
print("World")

# 4번
print("'Hello'")

# 5번
print('"Hello World"')

# 6번
print("\"!@#$%^&*()\'")

# 7번
print('"C:\\Download\\\'hello\'.py"')  # 첫번쨰 코드
print('\"C:\\Download\\\'hello\'.py\"') # 두번째 코드

# 8번
print('print("Hello\\nWorld")')

# 9번
a = input()
print(a)

# 10번
a = input()
b = int(a)
print(b)

# 11번
f1 = input()
f2 = float(f1)
print(f2)

# 12번
a1 = input()
a2 = input()
a3 = int(a1)
a4 = int(a2)
print(a3)
print(a4)

# 13번
a=input()
c=input()
print(c)
print(a)

# 14번
a = input()
print(a)
print(a)
print(a)
#-------------
a = input()
f=float(a)
print(f)
print(f)
print(f)

# 15번
a, b = input().split()
a = int(a)
b = int(b)
print(a)
print(b)

# 16번
a, b = input().split()
print(b, a)

# 17번
i = input()
print(i, i, i)

# 18번
a, b = input().split(':')
print(a, b, sep=':')

# 19번
y, m, d = input().split('.')
print(d, m, y, sep='-')

# 20번
a, b = input().split("-")
print(a+b)
#-----------------------------------------
a, b = input().split("-")
print(a, b, sep="")

# 21번
s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# 22번
s = input() 
print(s[0:2], s[2:4], s[4:6], sep=' ')

# 23번
h, m, s = input().split(':') 
print(m)

# 24번
w1, w2 = input().split()
s = w1 + w2
print(s)

# 25번
a, b = input().split()
c = int(a) + int(b)
print(c)


# 26번 ?? 왜 스플릿으로 입력 받으면 에러가 나지?
a = input()
b = input()
c = float(a) + float(b)
print(c)

# 27번
a = input()
n = int(a)
print('%x'% n)

# 28번
a=input() 
a=int(a) 
print("%X"%a)

# 29번
a=input() 
a=int(a,16) 
print("%o"%a)

# 30번
n=input() 
n=ord(n) 
print(n)

# 31번
c=int(input())
print(chr(c))

# 32번
i=int(input())
print(-i)

# 33번
c=ord(input())
print(chr(c+1))

# 34번
a, b = input().split()
c = int(a) - int(b)
print(c)

# 35번
c, d = input().split()
m = float(c) * float(d)
print(m)

# 36번
w, n = input().split()
print(w*int(n))

# 37번
n = input()
s = input()
print(int(n)*s)

# 38번
a, b = input().split()
c = int(a)**int(b)
print(c)

# 39번
a, b = input().split()
c = float(a)**float(b)
print(c)

# 40번
a, b = input().split()
c = int(a)//int(b)
print(c)

# 41번
a, b = input().split()
c = int(a)%int(b)
print(c)

# 42번
f = float(input())
print(format(f, ".2f"))

# 43번
f1, f2 = input().split()
f3 = float(f1)/float(f2)
print(format(f3, ".3f"))

# 44번
a, b = input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format((a/b), ".2f"))

# 45번
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
s = a+b+c
print(s)
print(format((s/3), ".2f"))

# 46번

""" 정수 1개를 입력받아 2배 곱해 출력해보자.

참고
*2 를 계산한 값을 출력해도 되지만,
정수를 2배로 곱하거나 나누어 계산해 주는 비트단위시프트연산자 <<, >>를 이용할 수 있다.
컴퓨터 내부에는 2진수 형태로 값들이 저장되기 때문에,
2진수 형태로 저장되어 있는 값들을 왼쪽(<<)이나 오른쪽(>>)으로
지정한 비트 수만큼 밀어주면 2배씩 늘어나거나 1/2로 줄어드는데,

왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고,
오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0(0 또는 양의 정수인 경우)이나 1(음의 정수인 경우)이 개수만큼 추가되고,
가장 오른쪽에 있는 1비트는 사라진다.

예시
n = 10
print(n<<1)  #10을 2배 한 값인 20 이 출력된다.
print(n>>1)  #10을 반으로 나눈 값인 5 가 출력된다.
print(n<<2)  #10을 4배 한 값인 40 이 출력된다.
print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.

정수 10의 2진수 표현은 ... 1010 이다.
10 << 1 을 계산하면 ... 10100 이 된다 이 값은 10진수로 20이다.
10 >> 1 을 계산하면 ... 101 이 된다. 이 값은 10진수로 5이다.

n = 10 과 같이 키보드로 입력받지 않고 직접 작성해 넣은 코드에서, 숫자로 시작하는 단어(식별자, identifier)는 자동으로 수로 인식된다.  

n = 10 에서 10 은 10진수 정수 값으로 인식된다.
변수 n 에 문자열을 저장하고 싶다면, n = "10" 또는 n = '10'으로 작성해 넣으면 되고,

n = 10.0 으로 작성해 넣으면 자동으로 실수 값으로 저장된다.
n = 0o10 으로 작성해 넣으면 8진수(octal) 10으로 인식되어 10진수 8값이 저장되고,
n = 0xf 나 n = 0XF 으로 작성해 넣으면 16진수(hexadecimal) F로 인식되어 10진수 15값으로 저장된다.

** python에서 실수 값에 대한 비트시프트 연산은 허용되지 않고 오류가 발생한다.
(실수 값도 컴퓨터 내부적으로는 2진수 형태로 저장되고 비트시프트 처리가 될 수 있지만, python 에서는 허용하지 않는다.) """


a = int(input())
print(a<<1)


# 47번
a, b = input().split()
a = int(a)
b = int(b)
print(a<<b)

# 48번
a, b = input().split()
a = int(a)
b = int(b)
print(a<b)

# 49번
a, b = input().split()
a = int(a)
b = int(b)
print(a==b)

# 50번
a, b = input().split()
a = int(a)
b = int(b)
print(a<=b)

# 51번
a, b = input().split()
a = int(a)
b = int(b)
print(a!=b)

# 52번
a = int(input())
print(bool(a))

# 53번
a = int(input())
print(not(bool(a)))

# 54번
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

# 55번
a, b = input().split()
print(bool(int(a)) or bool(int(b)))

# 56번 2가지
a, b = input().split()
print(not(bool(int(a))) and bool(int(b)) or bool(int(a)) and not(bool(int(b))))
#------------------------------------------------------------------------------
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and (not d)) or ((not c) and d))

# 57번 2가지
a, b = input().split()
print(bool(int(a)) and bool(int(b)) or not(bool(int(a))) and not(bool(int(b))))
#------------------------------------------------------------------------------
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print((c and d) or ((not c) and (not d)))

# 58번
a, b = input().split()
print(not(bool(int(a))) and not(bool(int(b))))

# 59번 ~ing
a = int(input())
print(~a)

