"""
 Задайте натуральное число N. Напишите программу, которая составит 
 список простых множителей числа N.
"""

# import math

def Factor(n):
    lst = []
    a = 2
    while a * a <= n:
        if n % a == 0:
            lst.append(a)
            n //= a
        else:
            a += 1
    if n > 1:
        lst.append(n)
    return lst

# n = int(input("Задайте натуральное число n: "))
Factor(56)
