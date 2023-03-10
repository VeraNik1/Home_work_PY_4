# Домашнее задание Семинар 4
# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)

# Output: 6 12

import random as r
while True:
    try:
        n = int(input("Введите длину первого набора >>> "))
        m = int(input("Введите длину второго набора >>> "))
        if n > 0 and m > 0:
            break
        else:
            raise Exception

    except:
        print('Вы ввели не натуральное число, попробуйте еще раз')

N = [r.randint(0, 10) for _ in range(n)]
M = [r.randint(0, 10) for _ in range(m)]
print('первый набор чисел:', N)
print('второй набор чисел:', M)

print('Числа, встерчающиеся в обоих наборах: ', *sorted(set(N).intersection(set(M))))



# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. 
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло 
# различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
#  Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
#  находясь перед некоторым кустом заданной во входном файле грядки.

# Input: 4
# (значения сгенерированы случайным образом
# 4 2 3 1 )

# Output: 9

import random as r
while True:
    try:
        N = int(input("Введите количество кустов черники >>> "))
        if N <= 0:
            raise Exception
        
        break
    except:
        print('Вы ввели не натуральное число, попробуйте еще раз')


def get_berries_max_amount(arr):
    if len(arr) <= 3:
        return sum(arr)
    else:
        arr.extend(arr[:2])
        max_amount = sum(arr[:3])
        for i in range(1, len(arr) - 2):
            temp = sum(arr[i:i+3])
            if temp > max_amount:
                max_amount= temp
        return max_amount
N = [r.randint(1, 50) for _ in range(N)]
print('количество ягод на кустах:', *N)

print('Максимальное количество ягод, которое может собрать собирающий модуль за один проход: ', get_berries_max_amount(N))


# Задачи на повторение по материалам предыдущих семинаров (по желанию)
# Задача 101 Вычислить число π c заданной точностью d

# Пример: 
# при d = 0.001, π = 3.141    0.1 ≤ d ≤ 0.00000000001

from math import pi

while True:
    try:
        d = int(input("Укажите точность числа pi (количество знаков после запятой от 1 до 11) >>> "))
        if d < 1 or d > 11:
            raise Exception
        break
    except:
        print('Число знаков введено некорректно, попробуйте еще раз')

print(round(pi, d)) #вычисление pi с округлением

print(str(pi)[:d+2]) #pi без округления




# Задача 102 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
while True:
    try:
        N = int(input("Введите натуральное число N >>> "))
        if N <= 0:
            raise Exception
        break
    except:
        print('Вы ввели не натуральное число, попробуйте еще раз')

def prime_factorization(N): #функция разложения числа на простые множители
    res = []
    while N % 2 == 0:
        res.append(2)
        N //= 2
    while N % 3 == 0:
        res.append(3)
        N //= 3
    while N > 3:
        for i in range(5, N + 1):
            if N % i == 0:
                res.append(i)
                N //= i
                break
        
    return res
print(N, end=' = ')
print(*prime_factorization(N), sep='*')



# Задача 103 Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл file1.txt многочлен степени k.
# Пример:  k=2 

# Возможные варианты многочленов:
# 2*x*x + 4*x + 5 = 0 
# x*x + 5 = 0 
# 10*x*x = 0
import random as r
def input_int():
    while True:
        try:
            k = int(input())
            if k <= 0:
                raise Exception
            return k
        except:
            print('Вы ввели не натуральное число, попробуйте еще раз')

def get_polynomial(K):
    polynom = ''
    for i in range(K):
        temp = r.randint(0, 100)
        if temp:
            polynom = ' + ' + str(temp) + i * '*x' + polynom
    polynom = str(r.randint(1, 100)) + K * '*x' + polynom + ' = 0'
    return polynom

print('Введите натуральную степень первого многочлена >>>')
k_1 = input_int()    
with open('file1.txt', 'w', encoding='UTF-8') as file_1:
    file_1.write(get_polynomial(k_1))
print('Введите натуральную степень второго многочлена >>>')

k_2 = input_int()    
with open('file2.txt', 'w', encoding='UTF-8') as file_2:
    file_2.write(get_polynomial(k_2))

# Задача 104. Даны два файла file1.txt и file2.txt, в каждом из которых находится запись многочлена 
# (полученные в результате работы программы из задачи 103). Необходимо сформировать файл file_sum.txt, 
# содержащий сумму многочленов.
def get_dict_from_polinom(text):
    res = {}
    arr = text[:-4].split(' + ')
    for item in arr:
        key = item.count('x')
        res[key] = int(''.join([i for i in item if i.isdigit()]))
    return res

def sum_dict(d1, d2):
    sum_dict = {}
    keys = set(list(d1) + list(d2))
    for k in sorted(keys, reverse=True):
        if k in d1: 
            sum_dict[k] = d1[k]
        if k in d2:
            sum_dict[k] += d2[k]
    return sum_dict

def get_polinom_from_dict(data):
    res = ''
    for k, v in data.items():
        if k:
            res += str(v) + k*'*x' + ' + '
        else:
            res += str(v) + ' = 0'
    return res

with open('file1.txt', 'r', encoding='UTF-8') as file_1,\
    open('file2.txt', 'r', encoding='UTF-8') as file_2,\
    open('file_sum.txt', 'w', encoding='UTF-8') as out:
    poly_1 = file_1.readline()
    poly_2 = file_2.readline()
    dict_1 = get_dict_from_polinom(poly_1)
    dict_2 = get_dict_from_polinom(poly_2)
    dict_sum = sum_dict(dict_1, dict_2)
    print(get_polinom_from_dict(dict_sum), file=out)

# 105-108 приложу к семинару 5)
# Задача 105 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Задача 106 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента? (Добавьте игру против бота)

# Задача 107 Создайте программу для игры в ""Крестики-нолики"" (Добавьте игру против бота)

# Задача 108 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (модуль в отдельном файле, импортируется как библиотека)
# метод Упаковка: на вход подается текстовый файл, на выходе текстовый файл со сжатием.
# метод Распаковка: на вход подается сжатый текстовый файл, на выходе текстовый файл восстановленный.
# Прикинуть достигаемую степень сжатия (отношение количества байт сжатого к исходному).