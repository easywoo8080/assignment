n = int(input())

#Fn = Fn-1 + Fn-2 (n ≥ 2)

f = [0, 1]


for i in range(2, n + 1):
    pi = f[i - 1] + f[i - 2]
    f.append(pi)


print(f[n])
