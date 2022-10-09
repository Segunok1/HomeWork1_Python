""" 
Напишите программу, удаляющую из текста все слова, содержащие "абв".
"""


def text_filtering():
    txt = list(filter(lambda x: x != 'абв', input().split()))
    return txt


print('Введите текст содержащий слова с "абв": ')
print(text_filtering())
