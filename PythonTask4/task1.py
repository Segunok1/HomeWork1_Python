"""
 Задайте натуральное число N. Напишите программу, которая составит 
 список простых множителей числа N.
"""


def fact(N):
    lst = []
    a = 2
    while a <= N:
        if (N % a) == 0:
            lst.append(a)
            N /= a
        else:
            a += 1
    return lst


N = int(input("Задайте натуральное число N: "))
print(fact(N))
