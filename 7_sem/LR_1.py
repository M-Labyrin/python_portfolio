import math


def integrate(fn, a, b, n_iter=10000):
    result = 0
    h = 1 / n_iter
    while a <= b - h:
        result += (fn(a) + fn(a + h)) / 2 * h
        a += h
    return round(result, 8)


if __name__ == "__main__":
    assert integrate(math.sin, 0, 1) == 0.45969769, "Интеграл sin от 0 до 1 неверно вычислен"
    assert integrate(math.cos, 1, math.pi/2) == 0.15852901, "Интеграл cos от 1 до pi/2 неверно вычислен"
    assert integrate(math.tan, 0, 1) == 0.61562647, "Интеграл tan от 0 до 1 неверно вычислен"

    print("Результат вычисления методом трапеций интеграла синуса от 0 до 1:", integrate(math.sin, 0, 1))