# Вычислить площадь треугольника с помощью формулы Герона

import math

def calculate_the_area(a_side, b_side, c_side):
    P = (a_side + b_side + c_side) / 2
    S = math.sqrt(P * (P - a_side) * (P - b_side) * (P - c_side))
    return S

print("Введите первую сторону треугольника: ")
a = int(input())
print("Введите вторую сторону треугольника: ")
b = int(input())
print("Введите третью сторону треугольника: ")
c = int(input())

print("Площадь треугольника: ", calculate_the_area(a, b, c))
