"""
Вывести треугольник #3 с шириной N с помощью цикла while
"""

n = int(input())
a = n
while n > 0:
    print(' ' * (a - n) + '*' * n)
    n -= 1
