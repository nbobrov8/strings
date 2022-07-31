#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
1) Даны два предложения. Для каждого слова первого предложения (в том числе для повторяющихся в этом предложении слов)
определить, входит ли оно во второе предложение.
2) Дано предложение. Определить количество слов: начинающихся с буквы н; оканчивающихся буквой р.
3) Даны два слова. Напечатать только те буквы слов, которые есть лишь в одном из них (в том числе повторяющиеся).
Например, если заданные слова процессор и информация, то ответом должно быть: п е с с и ф м а я.
"""


def find_word():  # Вхождение слова.
    s1 = input(">> ").split()
    s2 = input(">> ").split()
    for i in s1:
        if i in s2:
            print(i, '- входит')
        else:
            print(i, "- не входит")


def numb_words():  # Подсчет количества слов.
    # 1 способ
    sentence = input("> ").split()
    counter = 0
    for i in sentence:
        if i[0] == "н" and i[-1] == "р":
            counter += 1
    print(counter)

    # 2 способ
    for i in sentence:
        if i.startswith("н") and i.endswith("р"):
            counter += 1
    print(counter)


def repetitions():  # Удалить букву, если она есть в другом слове.
    s1 = list('процессор')
    s2 = list('информация')
    lst = []
    for i in s1:
        if i not in s2:
            lst.append(i)
    for k in s2:
        if k not in s1:
            lst.append(k)
    print(lst)
