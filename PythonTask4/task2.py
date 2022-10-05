
def factors(N):


lst = []
a = 2
while a <= N:
    if (N % a) == 0:
        lst.append(a)
        N /= a
    else:
        a += 1
print(lst)


N = int(input("Задайте натуральное число N: "))
factors(N)
