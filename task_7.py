# 7. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день
# спортсмен увеличивал результат на 10% относительно предыдущего. Требуется определить номер дня, на который результат
# спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и выводить
# одно натуральное число — номер дня.

a = 2
b = 3
day = 0
while a < b:
    day += 1
    print(f"День :{day} результат{round(a, 2)}")
    a = a * 1.1
day += 1
print(f"На {day} день спортсмен достиг результата — не менее {round(a, 0)} км")


