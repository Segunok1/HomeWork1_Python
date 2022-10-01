"""
Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
*Пример:*
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

from hashlib import new


# list = [2, 3, 4, 5, 6]
# new_list = []
# if len(list) % 2 != 0:
#     print(len(list))
# else:
#     len(list) // 2 == 0
#     print(len(list))
# for i in range(len(list)): 
#     new_list = list[i] * list[len-i-1]
#     new_list.appendK(new_list)
# print(new_list)
