"""
Задайте последовательность чисел. Напишите программу, которая выведет список 
неповторяющихся элементов исходной последовательности.
"""


def non_repeating_elements(nums):
   lst = []
   for num in nums:
      if num in lst:
         continue
      else:
         lst.append(num)
   return lst


print('Задайте последовательность чисел.')
nums = list(map(int, input().split()))
print(non_repeating_elements(nums))
