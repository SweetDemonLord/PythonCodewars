
import math
from multiprocessing import Pool

# Генерируем список входных данных
inputs = [i ** 2 for i in range(100, 130)]

# Функция для вычислений
def f(x):
    return len(str(math.factorial(x)))

# Последовательное выполнение
%timeit [f(x) for x in inputs]
# Результат: ~1.44 сек

# Параллельное выполнение
p = Pool(4)  # Создаем пул из 4 процессов
%timeit p.map(f, inputs)
# Результат: ~451 мс
