# 1) Сумма ряда 0-100
from numpy import array, random, mean

print('Сумма ряда 0-100', sum(array(range(100))))

# 2) Сумма ряда 0-input()
y = input("До какого числа считаем сумму ряда, начиная с 0:")
print('Сумма ряда 0-input()', sum(array(range(int(y)))))

# 3) Среднее среди 100 случайных чисел
random_array = random.randint(99, size=100)

print("Случайные 100 чисел: ", random_array)
print("Среднее среди них:", mean(random_array))
