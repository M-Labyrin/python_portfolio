# Написать программу с функцией, решающей физическую задачу
# Условие: ящик, имеющий форму куба с ребром "a" см без одной грани, нужно покрасить со всех сторон снаружи.
# Найдите площадь поверхности, которую необходимо покрасить.

import math

def square(a):
    S = (a * a) * 5
    return S

print("Введите длину ребра: ")
edge = int(input())

print("Нужно закрасить" ,square(edge), "см^2")