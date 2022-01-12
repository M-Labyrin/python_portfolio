from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial

import math
import timeit

timeit_setup = "from __main__ import integrate, math"


def integrate(fn, a, b, n_iter=100000):
    result = 0
    h = 1 / n_iter
    while a <= b - h:
        result += (fn(a) + fn(a + h)) / 2 * h
        a += h
    return round(result, 8)


if __name__ == "__main__":
    assert integrate(math.sin, 0, 1) == 0.45969769, "Интеграл sin от 0 до 1 вычислен некорректно"
    assert integrate(math.sin, 1, math.pi/2) == 0.54029598, "Интеграл sin от 1 до pi/2 вычислен некорректно"
    assert integrate(math.cos, 1, math.pi/2) == 0.15852902, "Интеграл cos от 1 до pi/2 вычислен некорректно"
    assert integrate(math.tan, 0, 1) == 0.61562647, "Интеграл tan от 0 до 1 вычислен некорректно"
    assert integrate(math.tan, 0, math.pi/4) == 0.34656543, "Интеграл tan до 0 до pi/4 вычислен некорректно"

    print("Результат вычисления методом трапеций интеграла sin от 0 до 1:", integrate(math.sin, 0, 1))
    print("Время вычисления с точностью 10^5:",
          timeit.timeit(stmt="integrate(math.sin, 0, 1)", setup=timeit_setup, number=100))
    print("Время вычисления с точностью 10^6:",
          timeit.timeit(stmt="integrate(math.sin, 0, 1, n_iter=1000000)", setup=timeit_setup, number=100))
    #  для 10^5: ~0.126 мс, для 10^6: ~1.299 мс