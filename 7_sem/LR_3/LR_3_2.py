from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial

import math
import timeit

timeit_setup = "from __main__ import integrate, integrate_async, math"


def integrate(fn, a, b, n_iter=1000000):
    result = 0
    h = 1 / n_iter
    while a <= b - h:
        result += (fn(a) + fn(a + h)) / 2 * h
        a += h
    return round(result, 8)


def integrate_async(fn, a, b, n_jobs=8, n_iter=1000000):
    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        spawn = partial(executor.submit, integrate, fn, partition_count=n_iter // n_jobs)
        step = (b - a) / n_jobs
        fs = [spawn(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
        return sum(f.result() for f in as_completed(fs))


if __name__ == "__main__":
    assert integrate(math.sin, 0, 1) == 0.45969685, "Интеграл sin от 0 до 1 вычислен некорректно"
    assert integrate(math.sin, 1, math.pi/2) == 0.54030198, "Интеграл sin от 1 до pi/2 вычислен некорректно"
    assert integrate(math.cos, 1, math.pi/2) == 0.15852902, "Интеграл cos от 1 до pi/2 вычислен некорректно"
    assert integrate(math.tan, 0, 1) == 0.61562491, "Интеграл tan от 0 до 1 вычислен некорректно"
    assert integrate(math.tan, 0, math.pi/4) == 0.34657343, "Интеграл tan до 0 до pi/4 вычислен некорректно"

    print("Результат вычисления методом трапеций интеграла sin от 0 до 1:", integrate_async(math.sin, 0, 1))
    print("Время вычисления с 2 потоками:", timeit.timeit(stmt="integrate_async(math.sin, 0, 1, n_jobs=2)",
                                                          setup=timeit_setup, number=100))
    print("Время вычисления с 4 потоками:", timeit.timeit(stmt="integrate_async(math.sin, 0, 1, n_jobs=4)",
                                                          setup=timeit_setup, number=100))
    print("Время вычисления с 6 потоками:", timeit.timeit(stmt="integrate_async(math.sin, 0, 1, n_jobs=6)",
                                                          setup=timeit_setup, number=100))
    print("Время вычисления с 8 потоками:", timeit.timeit(stmt="integrate_async(math.sin, 0, 1, n_jobs=8)",
                                                          setup=timeit_setup, number=100))
    #  10^6, 1 поток: ~1.299 мс
    #  2 потока: ~0.604 мс, 4 потока: ~0.302 мс, 6 потоков: ~0.202 мс, 8 потоков: ~0.153 мс