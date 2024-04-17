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