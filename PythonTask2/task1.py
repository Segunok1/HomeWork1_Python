"""
Напишите программу, которая принимает на вход вещественное или целое 
число и показывает сумму его цифр. Через строку нельзя решать.
*Пример:*
- 6782 -> 23
- 0,56 -> 11
"""

num = input("Введите число: ")
sum = 0
for i in num:
    if i != '.':
        sum += int(i)
print(sum)