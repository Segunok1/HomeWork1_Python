"""Напишите программу, которая принимает на вход цифру, 
 обозначающую день недели, и проверяет, является ли этот день выходным.
*Пример:*
- 6 -> да
- 7 -> да
- 1 -> нет
"""
import numbers


numbers = int(input("Введите цифру дня недели: "))
if 6 > numbers < 7:
    print("Нет, это не выходной")
else:
    print("Да, это выходной")
