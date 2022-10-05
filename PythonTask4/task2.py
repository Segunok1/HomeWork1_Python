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


nums = ["2", "2", 30, 54, "try", 30, "try"]
print(non_repeating_elements(nums))
