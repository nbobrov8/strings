#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
1) Дано слово. Удалить из него все повторяющиеся буквы, оставив их первые вхождения.
2) Дан текст, в начале которого имеются пробелы и цифры. Найти порядковый номер максимальной цифры, начиная счет с
первого символа, не являющегося пробелом. Если максимальных цифр несколько, то должен быть найден номер первой из них.
3) Дан текст, в котором имеется несколько идущих подряд цифр. Получить число, образованное этими цифрами.
"""


def recurring():  # Удалить повторяющиеся буквы.
    w = 'asfaswefd'
    lst = []
    for i in w:
        if i not in lst:
            lst.append(i)
    s = ''.join(lst)
    print(s)


def max_digit():  # Порядковый номер максимальной цифры.
    s = '7 6 8 20 14 16 2 12 20 1 4 20'.split()
    lst = []
    for i in s:
        i = int(i)
        if i > 0:
            lst.append(i)
    print(lst.index(max(lst)))


def text_digit():  # Получить число из разбросанных цифр.
    s = 'avcde732dsfsdf23nh90'
    num = ""
    for i in s:
        if i.isdigit():
            num += i
    print(num)
