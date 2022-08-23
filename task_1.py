"""
1. Поработайте с переменными, создайте несколько, выведите на экран. Запросите у пользователя некоторые числа и
строки и сохраните в переменные, затем выведите на экран.
"""
text_1 = "hello world"
print(text_1)

const_pi = 3.14
print(const_pi)

const_e = 2.71
print(const_e)

sum_1 = const_pi * const_e
print(sum_1)

in_1 = int(input("Введите число 1: "))
in_2 = int(input("Введите число 2: "))
sum_2 = in_1 + in_2 * const_pi
print(f"Выполнение операции - {in_1} + {in_2} * {const_pi} = {round (sum_2, 2)}")
