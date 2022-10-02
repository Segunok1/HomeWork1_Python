"""
Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
*Пример:*
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""
from hashlib import new

def the_product_of_pairs_of_numbers():
    lst = [2, 3, 4, 5, 6]
    if len(lst) % 2 != 0:
        res = int(len(lst) / 2) + 1
    else:
        res = int(len(lst) / 2)
    new_lst = []
    for i in range(0, res): 
        new_lst.append(lst[i] * lst[-i-1])
    return new_lst
   
print(the_product_of_pairs_of_numbers())


