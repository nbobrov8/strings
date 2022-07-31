#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
1) Дано слово. Проверить, является ли оно палиндромом.
2) Даны два слова. Определить, сколько начальных букв первого слова совпадает с начальными буквами второго слова.
Рассмотреть два случая:
- известно, что слова разные;
- слова могут быть одинаковыми.
3) Дано слово из 15 букв. Переставить в обратном порядке буквы, расположенные между k-й и
s-й буквами (т. е. с (k + 1)-й по (s - 1)-ю). Значения k и s вводятся с клавиатуры, k < s.
"""


def palindrome():  # Палиндром.
    word = input(">> ")
    check_word = word[::-1]
    if word == check_word:
        print("Слово является палиндромом")
    else:
        print("Слово не является палиндромом")


def check_words():  # Определение начальных букв.
    inp = input("> ").split()
    counter = 0
    if len(inp) >= 2:
        s = inp[:2]
        for x, y in zip(s[0], s[1]):
            if x != y:
                break
            counter += 1
        print(counter)
    else:
        print("Для сравнения необходимо минимум 2 слова.")


def permutation():  # Перестановка букв.
    word = "самодержавность"
    k = int(input())
    s = int(input())
    if k < s:
        word_slice = word[k:s][::-1]
        new_word = word.replace(word[k:s], word_slice)
        print(word, " > ", new_word)
