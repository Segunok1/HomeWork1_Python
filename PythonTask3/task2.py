"""
Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
*Пример:*
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""
from hashlib import new

def the_product_of_pairs_of_numbers():
    list1 = [2, 3, 4, 5, 6]
    if len(list1) % 2 != 0:
        print('Нечётное')
        res = int(len(list1) / 2) + 1
    else:
        len(list) // 2 == 0
        print('Чётное')
        res = int(len(list1) / 2)
    new_list = []
    for i in range(0, res): 
        new_list.append(list1[i] * list1[len(list1)-i-1])
    return new_list
   
print(the_product_of_pairs_of_numbers())


